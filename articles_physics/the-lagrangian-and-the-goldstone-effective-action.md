# __The Lagrangian and the Goldstone Effective Action__

## Introduction

This article writes the Goldstone field's effective action as an extremum of a functional in which every term carries a derivative, and shows that the resulting soft limit is a property of the action's structure and not of the dynamics that produced it. It is the action-first companion of *Goldstone's Theorem in Biquaternionic Form*, which derives the theorem and the soft limit; this article asks what functional the Goldstone field extremises below the radial mass, and why no term without a derivative can appear in it.

The equation. The parent's equation is the free wave equation for the phase, corrected by the derivative interactions,

$$
\Box_\Phi\vartheta_{\mathrm{fld}}-\frac{4c_4}{f^4}\frac{\partial}{\partial R_{\imath}}\Bigl(\bigl(\partial_{\jmath}\vartheta_{\mathrm{fld}}\partial_{\jmath}\vartheta_{\mathrm{fld}}\bigr)\frac{\partial\vartheta_{\mathrm{fld}}}{\partial R_{\imath}}\Bigr)+\cdots=0 ,
$$

which at leading order is $\Box_\Phi\vartheta_{\mathrm{fld}}=0$, the massless equation the theorem guarantees.

Three things are established.

*First, the action.* With $\vartheta_{\mathrm{fld}}$ the canonically normalized phase,

$$
S_{\mathrm{eff}}[\vartheta_{\mathrm{fld}}]=\int d^4r\;\Bigl[\frac12\sum_{\imath}\frac{\partial\vartheta_{\mathrm{fld}}}{\partial R_{\imath}}\frac{\partial\vartheta_{\mathrm{fld}}}{\partial R_{\imath}}+\frac{c_4}{f^4}\Bigl(\sum_{\imath}\frac{\partial\vartheta_{\mathrm{fld}}}{\partial R_{\imath}}\frac{\partial\vartheta_{\mathrm{fld}}}{\partial R_{\imath}}\Bigr)^{2}+\cdots\Bigr],
$$

the stationarity condition is the parent's equation, and every term in the integrand contains a derivative of the field.

*Second, the absence of a non-derivative term is the theorem.* A term without a derivative would be a potential, a potential would give the field a mass, and the theorem says the mass is zero. The effective action's shape is therefore the theorem written as a functional: it contains no invariant of $\vartheta_{\mathrm{fld}}$ alone, because the only such invariant is a constant.

*Third, the soft limit is visible in the action.* A Goldstone leg carries a derivative, so an amplitude with an additional soft Goldstone is proportional to its momentum and vanishes as the momentum goes to zero. That is the Adler zero, and it is a statement about the vertex's derivative count and not about the loop integrals.

What is not new. The theorem, the coset construction, the derivative expansion and the soft limit are standard. What the corpus contributes is the biquaternionic writing of the phase's kinetic term and the identification of the decay constant as the normalization of the canonical field.

## Conventions

The conventions are restated here so that every sign below is checkable from this page. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_k^{2}=-e_t$; the Goldstone field is the phase of a complex element, and its kinetic term is the corpus's gradient norm.

The field. $\vartheta_{\mathrm{fld}}$ is the canonically normalized phase, $\vartheta_{\mathrm{fld}}=\sqrt2\,\mathrm{Im}\,\ln\tilde\Xi$ in the abelian case, so that its kinetic term carries no factor of $f$. The dimensionless phase is $\vartheta_{\mathrm{fld}}/f$, and the two normalizations differ by the decay constant.

The scale. $f=\sqrt2\,v$ is the decay constant, the order parameter of the breaking; $\Lambda$ is the radial mass, $\Lambda=\sqrt{2\lambda}\,v$, and the expansion is in $p/\Lambda$ and in $\vartheta/f$.

The coefficients. $c_4,c_6,\dots$ are dimensionless and of order one in units of $f$ and $\Lambda$; they are fixed by the radial sector, which the effective action has integrated out.

The sign convention. The kinetic term enters with $+\tfrac12$ and the interactions with $+$, so that the energy is positive and the interaction's sign is the one that follows from the expansion.

## The Action in Element Form

The derivative series. The effective action is the most general functional of $\vartheta_{\mathrm{fld}}$ invariant under $\vartheta_{\mathrm{fld}}\mapsto\vartheta_{\mathrm{fld}}+\text{const}$, and invariance under a constant shift means that only derivatives appear:

$$
\mathcal{L}_{\mathrm{eff}}=\frac12\sum_{\imath}\partial_{\imath}\vartheta_{\mathrm{fld}}\partial_{\imath}\vartheta_{\mathrm{fld}}+\frac{c_4}{f^4}\Bigl(\sum_{\imath}\partial_{\imath}\vartheta_{\mathrm{fld}}\partial_{\imath}\vartheta_{\mathrm{fld}}\Bigr)^{2}+\frac{c_6}{f^8}(\cdots)^{3}+\cdots .
$$

Each term is a power of the same invariant $X=\sum_{\imath}\partial_{\imath}\vartheta_{\mathrm{fld}}\partial_{\imath}\vartheta_{\mathrm{fld}}$, and that is not a choice of basis: in four dimensions the only invariants of a single scalar built from derivatives are the powers of $X$, because any other contraction needs more than one index per factor.

Why the first term is fixed and the rest are not. The coefficient of $X$ is fixed by the canonical normalization: it must be $\tfrac12$ for the field to have the standard kinetic term. The coefficients of $X^2,X^3,\dots$ are not fixed by anything in the low-energy theory; they are determined by whatever the radial sector was, and that is exactly the sense in which the effective action trades predictability for generality.

Why no mass term and no potential. A term $V(\vartheta_{\mathrm{fld}})$ would break the shift, and the shift is the nonlinear realization of the broken symmetry. The theorem states that no such term is generated; the action's shape is the statement. What can break it is an explicit breaking — a fermion mass, a gauge anomaly — and those terms are the parent's, not this article's.

The two normalizations, and why both are used. In the canonical normalization the kinetic term is $\tfrac12(\partial\vartheta)^2$ and the interaction is $c_4(\partial\vartheta)^4/f^4$; in the dimensionless normalization the kinetic term is $\tfrac{f^2}{2}(\partial\vartheta)^2$ and the interaction is $c_4(\partial\vartheta)^4$. The two differ by $\vartheta\to f\vartheta$, and each makes a different fact look simple: the first makes the canonical field obvious, the second makes the decay constant's role as a normalization obvious.

The pairing. The pairing is the real gradient norm, and it is real because the phase is real. $\sum_{\imath}\partial_{\imath}\vartheta_{\mathrm{fld}}\partial_{\imath}\vartheta_{\mathrm{fld}}$ is a real number with the corpus's sign rule, and every power of it is real. No conjugation is needed and no imaginary part arises, because the field is a phase and not an element with a phase.

Why the complex writing gives the same answer. If the field is written as $\tilde\Xi=v\,e^{i\vartheta/v}$-type, the kinetic term $|D\tilde\Xi|^2$ contains the phase's gradient and the radial field's, and integrating out the radial field leaves exactly the phase's gradient term. The two writings agree because the modulus is fixed by the constraint and only the phase fluctuates.

The type of the coefficient. One scale and a tower of dimensionless numbers. $f$ has dimension of mass and is the only dimensionful quantity; $c_4,c_6,\dots$ are dimensionless and of order one. The expansion parameter is $p/(4\pi f)$, and the effective action is predictive below that scale.

Why the coefficients are not free in principle and are free in practice. They are computed from the radial sector by matching, and that computation is the parent's subject. In the low-energy theory they are parameters, and the effective action's content is that their number is infinite while their effect is ordered.

The selection rule. The selection rule is the shift symmetry, and it is the only thing that selects. Any functional invariant under a constant shift is a series in derivatives; any term that is not so invariant is excluded. The selection is exact and it is what makes the massless field massless.

What reality does not buy. **Reality does not buy a mass, a coupling, or a scale.** Three things the reality of the action does not supply:

- *No mass, even radiatively.* The shift symmetry protects it; that is the theorem.
- *No fixed $f$.* The decay constant is measured, and the action accepts it.
- *No fixed $c_4$.* The coefficient is a matching datum, not a prediction.

## The Variation: The Free Equation, Corrected

The leading variation. For the two-derivative term alone,

$$
\delta S=\int d^4r\;\delta\vartheta_{\mathrm{fld}}\,\tilde\nabla_\Phi^{\natural}\tilde\nabla_\Phi\vartheta_{\mathrm{fld}}=0
\quad\Longrightarrow\quad
\boxed{\;\Box_\Phi\vartheta_{\mathrm{fld}}=0\;}
$$

which is the massless wave equation. The field propagates at the speed of light, has no mass, and has one degree of freedom.

The correction. Varying the four-derivative term gives a contribution proportional to $\partial_{\imath}(X\,\partial_{\imath}\vartheta_{\mathrm{fld}})$, which is quartic in the field and vanishes on a constant or a plane wave at leading order. The exact equation is the parent's, and it differs from the free one only at second order in the amplitude.

Why the correction's order matters for the soft limit. The interaction's vertex carries four derivatives, so a process with one extra Goldstone is suppressed by $k^2/f^2$ at the amplitude level rather than by $k/f$. That suppression is stronger than the minimal one a Goldstone could have, and it follows from the interaction term's derivative count.

The check on the overall sign. For a plane wave $\vartheta_{\mathrm{fld}}=\vartheta_0\cos(k\cdot r)$ the energy density is positive and proportional to $k^2\vartheta_0^2/2$, and the pressure equals the energy density, which is the statement that the two-derivative action is conformally invariant. The vanishing trace is the check that the sign and the normalization are right.

## The Constraints the Action Imposes: A Shift, Not a Constraint

**There is no constraint in the Dirac sense.** One real field, one second-order equation, one degree of freedom; the canonical momentum is invertible and there is no primary constraint. The action is unconstrained.

The shift symmetry is not a constraint and does something different. It is a symmetry of the action that is realized nonlinearly — the field transforms by a constant, which is not a linear representation — and its consequence is a conserved current rather than a restriction on the variation. The distinction between a gauge symmetry, which removes degrees of freedom, and a nonlinear symmetry, which does not, is the point of this section.

Why the nonlinear realization is forced. The symmetry is spontaneously broken, so it is not a symmetry of the vacuum and cannot act linearly on the field that parameterizes the vacuum manifold. The constant shift is the nonlinear action, and the derivative-only structure is its consequence.

## The Structural Consequence: Every Leg Carries a Derivative

The statement. Because the action contains only derivatives, every Goldstone leg in every amplitude carries a momentum factor. An amplitude with an additional Goldstone of momentum $k$ is therefore proportional to $k$ at small $k$, and it vanishes as $k\to0$.

Why this is the Adler zero and not an approximation. The statement is exact at each order in the derivative expansion: the leading term gives one power of $k$, the four-derivative term gives three, and every term is odd in $k$ for an odd number of legs. The vanishing is not a cancellation between diagrams; it is a factor in each vertex.

The consequence for the theory's strength. A symmetry broken at scale $f$ gives interactions that are weak at energies below $4\pi f$, because each interaction brings powers of $p/f$. The Goldstone sector is therefore the most weakly coupled part of a strongly coupled theory, and that is why pion physics is computable at low energy even though QCD is not.

What the structure does not give. **It does not give the coefficients, it does not give $f$, and it does not tell us what the underlying theory is.** It gives the low-energy form of any theory with the same breaking pattern, and that universality is the effective action's content.

## The Noether Currents: The Shift Current Is the Order Parameter

The current. The shift symmetry gives

$$
j_{\imath}=f\,\partial_{\imath}\vartheta_{\mathrm{fld}} ,
$$

and its conservation, $\partial_{\imath} j_{\imath}=f\,\Box_\Phi\vartheta_{\mathrm{fld}}=0$, is the equation of motion. The current's normalization is the decay constant, and that is why $f$ is called the decay constant: a single Goldstone carries $f$ units of the broken charge.

The matrix element. $\langle0\rvert j_{\imath}(0)\lvert\vartheta(k)\rangle=ifk_{\imath}$, which is the statement that the current creates the Goldstone with strength $f$. The relation is the definition of $f$ and the reason the decay constant appears in every weak decay rate.

The improved current. With the higher-derivative terms the current acquires corrections proportional to $c_4\partial_{\imath} X/f^3$, and the corrections are what make the current's matrix element exact beyond leading order. The corrections do not change the leading statement.

Energy–momentum. Translation invariance gives $T_{\imath\jmath}$ with contributions from each term; the two-derivative part is traceless, so the leading theory is conformally invariant, and the four-derivative part breaks the trace at order $p^4/f^4$.

What there is not. **No topological current, no second independent current beyond the shift's, and no central phase.** The sector has one broken current and one tensor.

## What the Principle Adds and What It Relabels

Adds.

- *The theorem as a functional statement.* The masslessness is the absence of a non-derivative term, and the action makes that visible in one line.
- *The soft limit as a derivative count.* The Adler zero is a property of the vertices, not of the loop integrals.
- *The universality.* Every theory with the same breaking pattern has this action at low energy, whatever its ultraviolet completion.

Relabels.

- *The "effective" of the effective action.* It is not an approximation to a known action; it is the complete low-energy description, with a known error.
- *The decay constant.* It is the current's normalization and the expansion's scale at once, and the two roles are the same role.
- *The nonlinear realization.* It is not a technical device; it is what a broken symmetry does to a field that parameterizes the vacuum manifold.

The distinction that matters. The action is derivative-only and the physics is universal. Everything in this article follows from the shift symmetry, and the shift symmetry is what the breaking leaves behind.

## Open Questions

Do the coefficients $c_4,\dots$ have a biquaternionic form? The corpus writes the two-derivative term exactly and the four-derivative terms in the Skyrme article. Whether the full tower has a uniform algebra expression is not established.

## Summary

The action. $S_{\mathrm{eff}}=\int d^4r\,[\tfrac12(\partial\vartheta)^2+c_4(\partial\vartheta)^4/f^4+\cdots]$, invariant under a constant shift, whose leading variation is $\Box_\Phi\vartheta_{\mathrm{fld}}=0$.

The three findings. The absence of a non-derivative term is the theorem's masslessness. Every leg carries a derivative, which is the Adler zero. The coefficients are matching data and the scale $f$ is measured, so the action is universal in form and not in numbers.

The boundary. The kinetic term's biquaternionic form is the algebra's; the coefficients, the decay constant and the anomaly's term are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\vartheta_{\mathrm{fld}}$ | canonically normalized Goldstone phase |
| $f=\sqrt2\,v$ | decay constant |
| $\Lambda=\sqrt{2\lambda}\,v$ | radial mass, the expansion's scale |
| $c_4,c_6,\dots$ | dimensionless matching coefficients |
| $X=\sum_{\imath}\partial_{\imath}\vartheta\partial_{\imath}\vartheta$ | the invariant whose powers form the series |
| $j_{\imath}=f\partial_{\imath}\vartheta_{\mathrm{fld}}$ | shift current |

## Further Reading

- [Goldstone's Theorem in Biquaternionic Form](goldstones-theorem-in-biquaternionic-form.html) — the parent: the theorem, the coset, the soft limit.
- [The Lagrangian and the Nonlinear Sigma Model](the-lagrangian-and-the-nonlinear-sigma-model.html) — the same series written for a group-valued field.
- [The Lagrangian and the Skyrme Model](the-lagrangian-and-the-skyrme-model.html) — the four-derivative term that stabilises a soliton.
- [The Lagrangian and the Stueckelberg Mechanism](the-lagrangian-and-the-stueckelberg-mechanism.html) — the phase promoted to a field, and the abelian analogue of the shift.
- [The Axion and the Peccei–Quinn Mechanism in Biquaternionic Form](the-axion-and-the-peccei-quinn-mechanism-in-biquaternionic-form.html) — the shift symmetry and its anomaly.
