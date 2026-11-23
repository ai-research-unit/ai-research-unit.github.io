# __The Lagrangian and the Stueckelberg Mechanism__

## Introduction

This article writes the Stueckelberg action for a massive abelian vector and shows that its two ways of counting the same physics — the unitary gauge and the covariant gauges — are two readings of one functional. It is the action-first companion of *The Stueckelberg Mechanism in Biquaternionic Form*, which states the mechanism and the degree-of-freedom count; this article asks what action makes a mass term gauge invariant, and at what price.

Its place in the sector. The vector here is abelian, so this functional is not a term of [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html): the sector masses its bosons with the Higgs and not with a shift field. The construction is filed beside the electroweak articles because that is where a massive vector is discussed, not because the sector uses it. The general statement, with no sector attached, is [The Stueckelberg Mechanism for a Massive Abelian Vector in Biquaternionic Form](the-stueckelberg-mechanism-for-a-massive-abelian-vector-in-biquaternionic-form.html).

The equation. The parent's equations are the Proca equation for $A_{\imath}$ and the equation for the scalar $\xi$,

$$
\partial_{\jmath} F_{\imath\jmath}-\mu^2 A_{\imath}+\mu\,\partial_{\imath}\xi=0 ,
\qquad
\partial_{\imath} A_{\imath}-\frac{1}{\mu}\Box\xi=0 ,
$$

the second being the deformed Lorenz condition that the divergence of the first implies. The two together are the Proca system in the unitary gauge, and the article asks what functional has them as its stationary conditions.

Three things are established.

*First, the action.* With the scalar entering only through the combination $A_{\imath}-\partial_{\imath}\xi/\mu$,

$$
S=\int d^4r\;\Bigl[-\tfrac14\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}-\tfrac12\mu^2\sum_{\imath}\Bigl(A_{\imath}-\frac{1}{\imath}\partial_{\imath}\xi\Bigr)^{2}\Bigr],
$$

the stationarity conditions are the two equations above, and the action is invariant under $A_{\imath}\mapsto A_{\imath}+\partial_{\imath}\Lambda$, $\xi\mapsto\xi+\mu\Lambda$. The mass term has become invariant at the cost of a field.

*Second, the price is one scalar and no ghost.* The Stueckelberg scalar is a non-dynamical mode in the unitary gauge and an $\zeta$-dependent mode in the covariant gauges; the Faddeev–Popov determinant of an abelian fixing is field independent, so there is no ghost. The unphysical sector is the smallest one a massive vector can have.

*Third, the count is gauge independent and the distribution is not.* Four components of $A_{\imath}$ plus one scalar, minus one gauge symmetry, minus one mass-shell constraint, gives three physical modes in every gauge. What changes between gauges is which modes are called physical.

The mechanism is standard, and it is the abelian case of what the electroweak sector does with a doublet. What the corpus contributes is the exact biquaternionic writing of the invariant combination and the comparison of the two gauge choices on one page.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$. The potential is $\tilde A_\Phi\in\mathbb{B}_\Phi$, real, with $\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)$ and $\partial_{\imath}=\partial/\partial R_{\imath}$.

The scalar. $\xi$ is a real central scalar, dimensionless in this normalization, and the combination $A_{\imath}-\partial_{\imath}\xi/\mu$ is the invariant one. The parameter $\mu$ is the mass, with dimension of mass.

The gauge. The Stueckelberg symmetry is $A_{\imath}\mapsto A_{\imath}+\partial_{\imath}\Lambda$, $\xi\mapsto\xi+\mu\Lambda$, with $\Lambda$ a function of the coordinates. The unitary gauge is $\xi=0$; the covariant family is $G=\partial_{\imath} A_{\imath}-\zeta\mu^2\xi=0$ with $\zeta\in\mathbb{R}$.

The sign convention. The curvature term enters with $-\tfrac14$ and the mass term with $-\tfrac12$, as in the Proca article, so that the Hamiltonian is positive.

## The Action in Element Form

The two-term action. Write $\tilde A_\Phi$ and $\xi$ together and note that the mass term depends only on the combination

$$
\tilde C_\Phi=\tilde A_\Phi-\frac{1}{\mu}\tilde\nabla_\Phi\xi ,
$$

so that

$$
\boxed{\;S[\tilde A_\Phi,\xi]=\int d^4r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,\mu^2\,\langle\tilde C_\Phi\rangle_\natural\Bigr]\;}
$$

with $\langle\cdot\rangle_\natural$ the Minkowski square. The field strength is that of $\tilde A_\Phi$ alone, because $\mathrm{Vect}(\tilde\nabla_\Phi\tilde\nabla_\Phi^{\natural}\xi)=0$ for a central scalar: the gradient of a gradient has no vector part, so the shift $\tilde A_\Phi\to\tilde A_\Phi+\tilde\nabla_\Phi\xi/\mu$ leaves $\tilde F$ unchanged.

Why that identity is the whole mechanism. The mass term is not invariant under the shift, but the shift of $\tilde A_\Phi$ is compensated by the shift of $\xi$. The compensation works because $\xi$ enters only through its gradient, and the gradient is what the field strength cannot see. In the algebra's letters the statement is one line: $\tilde F$ depends on the vector part of the conjugate gradient, and a gradient of a scalar has none.

The invariant, written out. In components,

$$
\tilde C_\Phi=\sum_{\imath}\Bigl(A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi\Bigr)\vec e_{\imath} ,
\qquad
\langle\tilde C_\Phi\rangle_\natural=\sum_{\imath}\Bigl(A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi\Bigr)^{2},
$$

with the corpus's sign rule, so that the mass term is $-\tfrac12\mu^2\sum_{\imath}(\cdots)^2$ and the unitary gauge $\xi=0$ gives the Proca mass term exactly.

The gauge transformation, checked. Under $A_{\imath}\mapsto A_{\imath}+\partial_{\imath}\Lambda$ and $\xi\mapsto\xi+\mu\Lambda$,

$$
A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi\longmapsto A_{\imath}+\partial_{\imath}\Lambda-\frac{1}{\mu}\partial_{\imath}\xi-\partial_{\imath}\Lambda=A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi ,
$$

so the combination is invariant term by term. The invariance is exact and not up to a total derivative; this is what distinguishes the Stueckelberg mass term from a hand-written one, which is not invariant at all.

The limit that recovers Proca. For $\xi=0$ the action is the Proca action, and for $\mu\to0$ the scalar decouples and the action is Maxwell's. Both limits are exact, and they are the two ends of the family the parent article describes.

**The pairing is the real scalar part, and the mass term's reality is what lets the invariant be written as one square.** $\langle\tilde C_\Phi\rangle_\natural$ is real and negative-definite with the corpus's sign rule, so $-\tfrac12\mu^2\langle\tilde C_\Phi\rangle_\natural$ is real and positive. There is no imaginary part to cancel, because the combination $\tilde C_\Phi$ is a real vector in the material sector and the mass term is its norm.

Why the invariant is a single square and not a sum of two. The Stueckelberg trick consists in replacing $A_{\imath} A_{\imath}$ by $(A_{\imath}-\partial_{\imath}\xi/\mu)^2$, and the replacement preserves reality because the shift is real. A complex scalar would require a modulus and would give a non-polynomial action; the real scalar gives a polynomial one, which is why the abelian mechanism is the simplest case.

One mass and no new coupling. The action has $\mu$ and one gauge coupling, and the scalar's coupling is not independent: it is fixed to $\mu$ by the requirement that the combination be invariant. A different coefficient in front of $\partial_{\imath}\xi$ would break the symmetry, so the scalar's normalization is not a parameter.

What that means for the parameter count. The theory has two numbers, $e$ and $\mu$, and it had two before the scalar was introduced. The mechanism adds a field and no parameter, which is the sharpest way to say that it is a rewriting and not a new theory.

The selection rule is the shift symmetry, and it fixes the scalar's coupling exactly. The action is the most general one of dimension four built from $F_{\imath\jmath}$ and the invariant combination; any term with $\xi$ alone would break the shift and would give the scalar a potential. The absence of such a term is what makes the scalar non-dynamical in the unitary gauge and what makes the mechanism exact.

Reality does not buy renormalizability or a physical scalar. Three things the reality of the action does not supply:

- *No renormalizability claim.* The Stueckelberg action is renormalizable as a gauge theory and not as a Proca theory; the distinction is the whole reason the mechanism is used.
- *No physical scalar.* The scalar is not an asymptotic state; it is the longitudinal polarization in another variable.
- *No ghost freedom by itself.* The absence of ghosts follows from the abelian determinant being field independent, which is a property of the gauge group and not of the action's reality.

## The Variation: Two Equations, One of Them a Constraint

The variation with respect to $\tilde A_\Phi$. Varying and integrating by parts,

$$
\delta S=\int d^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl(\delta\tilde A_\Phi\bigl[\tilde\nabla_\Phi\tilde F-\mu^2\tilde C_\Phi\bigr]\Bigr),
$$

so stationarity gives $\tilde\nabla_\Phi\tilde F=\mu^2\tilde C_\Phi$, which in components is

$$
\partial_{\jmath} F_{\imath\jmath}-\mu^2\Bigl(A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi\Bigr)=0 .
$$

The variation with respect to $\xi$. Varying $\xi$ and integrating by parts,

$$
\delta S=\int d^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl(\delta\xi\,\frac{1}{\mu}\tilde\nabla_\Phi^{\natural}\bigl(\mu^2\tilde C_\Phi\bigr)\Bigr)=0
\quad\Longrightarrow\quad
\partial_{\imath}\Bigl(A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi\Bigr)=0 ,
$$

which is the deformed Lorenz condition, $\partial_{\imath} A_{\imath}=\frac{1}{\mu}\Box\xi$.

**The two equations are consistent, and that is not automatic.** Taking the divergence of the vector equation gives $\mu^2\partial_{\imath}(A_{\imath}-\partial_{\imath}\xi/\mu)=0$, which is the scalar equation. So the scalar's equation is the divergence of the vector's, and the system over-determines nothing. This is the same structure the Proca article records: the constraint is implied and not imposed, and here it is implied twice over, once from each variation.

The gauge redundancy of the two equations. Because the action is invariant, the equations cannot determine $\xi$ and the longitudinal part of $A_{\imath}$ separately; they determine only the combination $\tilde C_\Phi$. The unitary gauge picks a representative, and that is a choice of section in the orbit, not an extra equation.

The check that would catch a missing factor. In the unitary gauge the first equation is $\partial_{\jmath} F_{\imath\jmath}=\mu^2A_{\imath}$ and its divergence gives $\mu^2\partial_{\imath} A_{\imath}=0$, which is the Lorenz condition with the right sign. If the mass term had been written $\tfrac12\mu^2A_{\imath} A_{\imath}$ without the scalar, the divergence would give $\partial_{\imath} A_{\imath}=0$ as an identity, which is false; the scalar is what makes the constraint consistent with the equation.

## The Constraints the Action Imposes: One Scalar, Three Modes, No Ghost

The count in the unitary gauge. Four components of $A_{\imath}$, one constraint from the deformed Gauss law, three physical modes. The scalar has been gauged to zero and has become the longitudinal polarization; it has not disappeared, it has been relabelled.

The count in the covariant gauge. The same four plus one, with the gauge condition $G=\partial_{\imath} A_{\imath}-\zeta\mu^2\xi=0$ removing one and the scalar carrying an $\zeta$-dependent mass $\zeta\mu^2$. At $\zeta\to\infty$ the scalar's mass diverges and it decouples, leaving the Proca propagator; at $\zeta=0$ its mass vanishes and it is a free scalar. The physical amplitudes are $\zeta$ independent, and the independence is the statement that the scalar and the longitudinal vector carry one mode between them.

Why there is no ghost. The Faddeev–Popov determinant for the abelian condition is $\det(\Box-\zeta\mu^2)$, which is field independent, so it contributes a constant to the path integral and no propagating ghost. In the non-abelian case the determinant is field dependent, the ghosts propagate, and the counting involves them. The abelian mechanism's unphysical sector is therefore one scalar and nothing else, and that is the minimum for a massive vector.

The constraint that must survive. The mass-shell constraint $\partial_{\imath} A_{\imath}=\Box\xi/\mu$ — which in the unitary gauge $\xi=0$ is the Lorenz condition $\partial_{\imath} A_{\imath}=0$ — is not optional: without it the time component of $A_{\imath}$ would propagate and the energy would be unbounded. The constraint is implied by the vector equation, as shown above, and the derivation is what makes the count three rather than four.

## The Structural Consequence: The Mass Term Becomes Invariant, and the Field Becomes a Coordinate

The statement. A mass term is not invariant under a gauge transformation, and the mechanism makes it invariant by promoting the gauge parameter to a field. The promoted field is not a new particle; it is the gauge parameter made dynamical, and its dynamics is fixed by the requirement that it cancel the shift of the vector.

Why the structure recurs. Every massive gauge field in the corpus has this shape, and the electroweak sector is the non-abelian case with a doublet. The Stueckelberg action is the abelian prototype: one scalar, one vector, one invariant combination, and the count of three modes. Reading it once makes the electroweak count a special case rather than a separate fact.

The equivalence, stated carefully. The Stueckelberg theory and the Proca theory have the same physical spectrum and the same amplitudes. They differ in what is manifest: the Stueckelberg action is manifestly gauge invariant and manifestly renormalizable by power counting; the Proca action is manifestly unitary and manifestly three-mode. The equivalence is exact at the level of the S-matrix and is the content of the parent's comparison.

**What the structure does not give.** It does not give the scalar a mass, a potential or an interaction. It does not explain why a mass exists. It gives a consistent description of a mass that is already there.

## The Noether Currents: The Conserved Current of the Shift

The shift current. The action is invariant under $\xi\mapsto\xi+\mu\Lambda$ with constant $\Lambda$ only when combined with a constant shift of $A_{\imath}$, and the constant shift of $A_{\imath}$ by a gradient is a gauge transformation, so the global symmetry is trivial on the physical fields. The would-be Noether current is

$$
j_{\imath}=\mu\bigl(A_{\imath}-\frac{1}{\mu}\partial_{\imath}\xi\bigr)=\mu\,\tilde C_{\Phi,\imath} ,
$$

and its conservation, $\partial_{\imath} j_{\imath}=0$, is exactly the scalar's equation. The current is not an independent object: it is the mass term's argument, and its conservation is the constraint.

The electromagnetic current, and its absence. There is no charged matter in the action, so there is no $\mathrm{U}(1)$ current beyond the shift current. Adding a charged field would gauge the shift symmetry, and the resulting current would be the source of $A_{\imath}$; the corpus's coupled articles do that and this one does not.

Energy–momentum. Translation invariance gives $T_{\imath\jmath}$ with contributions from the curvature and from the invariant combination, and the static energy is positive. The trace is nonzero because of the mass term, and the trace is the classical part of the anomaly.

**What there is not.** No second current, no central phase, no topological charge. The Stueckelberg sector's current content is one conserved combination, and that is the minimum a massive vector can have.

## What the Principle Adds and What It Relabels

Adds.

- *The invariance in one line.* The action shows that the mass term depends on the invariant combination and on nothing else, which the equations hide.
- *The parameter count.* The mechanism adds a field and no parameter, and the count is visible only when the action is written.
- *The reason for no ghost.* The abelian determinant's field independence is a property of the action's gauge structure.

Relabels.

- *The "mechanism".* It is not a dynamical process; it is a rewriting of the same theory in variables where the invariance is manifest.
- *The scalar.* It is not a particle; it is the gauge parameter promoted to a field, and in the unitary gauge it is the longitudinal polarization.
- *The gauge choice.* The unitary gauge and the covariant gauges are not two theories; they are two readings of one action.

The distinction that matters. The action is invariant and the physical content is three modes. Everything in this article follows from the tension between those two statements and from the fact that the invariant combination is what the action depends on.

## Open Questions

**Does the algebra fix the form of the invariant?** The invariant is the vector part of the conjugate gradient of the difference, and that form is the algebra's. Whether a different pairing would give a different invariant is not explored.

## Summary

The action. $S=\int d^4r\,[\tfrac12\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)-\tfrac12\mu^2\langle\tilde A_\Phi-\tilde\nabla_\Phi\xi/\mu\rangle_\natural]$, invariant under $A_{\imath}\mapsto A_{\imath}+\partial_{\imath}\Lambda$, $\xi\mapsto\xi+\mu\Lambda$. The variation gives the Proca equation and the deformed Lorenz condition, the second being the divergence of the first.

The three findings. The mass term is invariant because the field strength cannot see a gradient of a scalar. The count is three modes in every gauge, with one scalar and no ghost in the abelian case. The mechanism adds a field and no parameter.

The boundary. The invariant combination and its biquaternionic form are the algebra's; the value of $\mu$, and the embedding of the scalar in a spontaneously broken theory, are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde A_\Phi$ | real vector potential in the material sector |
| $\tilde F$ | field strength, $\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ |
| $\xi$ | Stueckelberg scalar, real central |
| $\mu$ | mass |
| $\tilde C_\Phi=\tilde A_\Phi-\tilde\nabla_\Phi\xi/\mu$ | the gauge-invariant combination |
| $\Lambda$, $\zeta$ | gauge parameter; covariant-gauge parameter |
| $G=\partial_{\imath} A_{\imath}-\zeta\mu^2\xi$ | covariant gauge condition |

## Further Reading

- [The Stueckelberg Mechanism in Biquaternionic Form](the-stueckelberg-mechanism-in-biquaternionic-form.html) — the parent: the two gauges, the propagator, the degree-of-freedom count.
- [The Lagrangian and the Proca Equation](the-lagrangian-and-the-proca-equation.html) — the unitary-gauge action, and the Lorenz condition as a consequence.
- [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html) — the non-abelian case, where the scalar is a Goldstone of a broken symmetry.
- [The Stueckelberg Mechanism for a Massive Abelian Vector in Biquaternionic Form](the-stueckelberg-mechanism-for-a-massive-abelian-vector-in-biquaternionic-form.html) — the Proca obstruction in the algebra.
- [Gauge Fixing in the Electroweak Theory: $R_\xi$ Gauges, Ghosts and the Goldstone Equivalence Theorem](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html) — the $\zeta$-dependent propagator in the non-abelian case.
