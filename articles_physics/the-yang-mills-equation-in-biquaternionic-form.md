# __The Yang–Mills Equation in Biquaternionic Form__

## Introduction

*Maxwell's Equations in the Biquaternionic Formulation* compresses the four Maxwell equations into a single biquaternion equation, $\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi}$, in which a biquaternionic field strength is sourced by a biquaternionic current. *Non-Abelian Connections in Biquaternionic Form* then lets the connection of the same framework take values in the compact factor $\mathrm{SU}(2) = \mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ of the material sector, obtains the non-abelian curvature

$$
F_{\imath\jmath} = \partial/\partial R_{\imath} \mathcal{A}_{\jmath} - \partial/\partial R_{\jmath} \mathcal{A}_{\imath} + i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}],
\qquad [D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath},
$$

and records, in its discussion of the Yang–Mills action, that the source-free field equation is $\sum_{\imath} D_{\imath} F_{\imath\jmath} = 0$ "in place of the abelian $\sum_{\imath}\partial/\partial R_{\imath} F_{\imath\jmath} = 0$". It does not develop that equation: the sourced equation, the current that appears on its right-hand side, and the conservation law that current obeys are all left open. This article takes them up. It also takes up the functional whose variation produces the equation. A field equation met without the action behind it gives no reason to believe it is an equation of motion rather than an identity, so the former companion on the non-abelian Lagrangian is folded into §*The Yang–Mills Action* and §*The Variation*.

The Yang–Mills equation is the non-abelian generalisation of the Maxwell source equation,

$$
\boxed{\;\sum_{\imath} D_{\imath} F_{\imath\jmath} = J_{\jmath},
\qquad
\tilde D\tilde F = \tilde\nabla_\Phi\tilde F + i\kappa\,[\mathcal{A}, \tilde F]\;},
$$

with the covariant derivative $D_{\imath} = \partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath}$ acting on the curvature through the commutator, in the adjoint action of the algebra. The subject of this article is what changes from the abelian case, and the answer is a short list.

- **The field equation itself acquires a term.** In the abelian case the connection coefficients commute (in the parent's $\mathrm{U}(1)$ case they are central), so $[\mathcal{A}_{\imath},F_{\imath\jmath}] = 0$ and the field equation is the ordinary divergence. In the non-abelian case the commutator term is present and cannot be dropped: the covariant derivative is not the ordinary one, and the source of a non-abelian connection is itself charged.
- **The current is covariantly conserved, not ordinarily conserved.** Taking the covariant divergence of the field equation gives $\sum_{\imath} D_{\imath} J_{\imath} = 0$. This is *not* $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = 0$: the ordinary divergence of the current is $-i\kappa[\mathcal{A}_{\imath},J_{\imath}]$, which is nonzero for a generic non-abelian field. Writing ordinary conservation here would be a defect, not a simplification.
- **The terms that vanish in the abelian limit do so because the abelian connection commutes.** Every commutator that distinguishes the non-abelian equation from Maxwell contains either $[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$ or $[\mathcal{A}_{\imath},\,\cdot\,]$; all of them vanish when the connection coefficients commute, and none of them cancels against a nonvanishing partner.

The division between what is established and what is interpretation is kept explicit.

- **Established, and recomputed below.** The curvature identity $[D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath}$; the Bianchi identity $D_{\imath} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0$; the Yang–Mills equation $\sum_{\imath} D_{\imath} F_{\imath\jmath} = J_{\jmath}$ with the commutator term $i\kappa[\mathcal{A}_{\imath},F_{\imath\jmath}]$; the covariant conservation $\sum_{\imath} D_{\imath} J_{\imath} = 0$ and the failure of ordinary conservation; the reduction to Maxwell on a commuting generator set; and the adjoint transformation $J_{2,\jmath} = \tilde U J_{\jmath} \tilde U^{-1}$ of the source. Each was recomputed on a generic, non-constant $\mathrm{SU}(2)$-valued connection — all three generators, non-commuting — at four generic points, by exact polynomial arithmetic; no claim below rests on the abelian case.
- **Established, and recomputed below: the action.** The density $-\tfrac12\mathrm{Tr}(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath})$, with $\mathrm{Tr}$ the matrix trace on the $\mathrm{SU}(2)$ factor, is invariant because the trace is cyclic, and it is *not* the informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, which is not cyclic and would cost the invariance. Its variation is $\delta S_{\mathrm{YM}} = 2\int d^4r\,\mathrm{Tr}(\sum_{\jmath}\delta\mathcal{A}_{\jmath} D_{\imath}F_{\imath\jmath})$, so stationarity is the field equation. The constraints are first class and leave two polarizations per generator; the currents are covariantly conserved and their ordinary divergence is not zero; and the ceiling at $\mathrm{U}(1)\oplus\mathrm{SU}(2)$ is a property of the algebra and not of the density.
- **Interpretation.** Reading $\sum_{\imath} D_{\imath} F_{\imath\jmath}$ as the conserved current of a non-abelian connection, and the density as the standard Yang–Mills action, is the standard interpretation of the algebra, placed in the framework's notation. It is labelled as interpretation where it occurs.
- **Gaps and defects, left visible.** The biquaternion packaging of the curvature that the parent articles use, $\mathcal{F} = \tfrac12\sum_{\imath\jmath}F_{\imath\jmath}\bar{e}_{\imath} e_{\jmath}$, does not inherit the adjoint transformation as a single algebra conjugation, and the naive product $\vec\nabla_\Phi\!\cdot\!(\sum_{\jmath} F_{\imath\jmath}e_{\jmath})$ is not the covariant divergence of the field equation; both are stated precisely and neither is smoothed over. The framework's inability to fix the fixing condition is inherited unchanged and bounds the whole construction; no representative is chosen anywhere below.

## The Non-Abelian Curvature and the Adjoint Covariant Derivative

The constructions of this article are those of its two parents, and they are recalled here only far enough to fix the conventions the field equation uses.

The connection is an $\mathrm{SU}(2)$-valued one-form, $\mathcal{A}_{\imath}$, and the covariant derivative is $D_{\imath} = \partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath}$, with $[D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath}$. Under a local transformation $\tilde U(\tilde{Q})\in SU(2)$ the connection and field strength transform in the adjoint representation,

$$
\mathcal{A}_{2,\imath} = \tilde U\mathcal{A}_{\imath} \tilde U^{-1} + \frac{i}{\kappa}(\partial/\partial R_{\imath} \tilde U)\tilde U^{-1},
\qquad
F_{2,\imath\jmath} = \tilde U F_{\imath\jmath} \tilde U^{-1},
$$

and $F_{\imath\jmath}$ is *not* invariant: it is an algebra element rotated by the group. The covariance of the first-order operator is what forces the inhomogeneous term in the first law.

Two derived objects carry the rest of the article. The first is the **adjoint covariant derivative**, the action of the connection on an algebra-valued field $\tilde{Q}$:

$$
D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa\,[\mathcal{A}_{\imath}, \tilde{Q}].
$$

It is the unique first-order operator whose action on $\tilde{Q}$ is the commutator of the covariant derivative operator with multiplication by $\tilde{Q}$. Recomputing that commutator directly,

$$
[D_{\imath}, \tilde{Q}]\tilde{Ξ} = D_{\imath}(\tilde{Q}\tilde{Ξ}) - \tilde{Q}(D_{\imath}\tilde{Ξ})
= (\partial/\partial R_{\imath} \tilde{Q} + i\kappa[\mathcal{A}_{\imath},\tilde{Q}])\tilde{Ξ},
$$

for every $\tilde{Ξ}$, so that as operators

$$
[D_{\imath}, \tilde{Q}] = D_{\imath} \tilde{Q},
$$

with $\tilde{Q}$ read as multiplication by the algebra element. (The notation table and the Bianchi discussion of *Non-Abelian Connections in Biquaternionic Form* print $[D_{\imath},\tilde{Q}] = i\kappa D_{\imath} \tilde{Q}$; that line is not consistent with the definition $D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa[\mathcal{A}_{\imath},\tilde{Q}]$ given in the same article, and the factor $i\kappa$ is an evident slip — the operator commutator is first order in $\partial/\partial R_{\imath}$ and equal to multiplication by $D_{\imath} \tilde{Q}$. The Bianchi identity itself is unaffected, because the substitution that produces it is the same either way once the identity is corrected. The recomputed identity $[D_{\imath},\tilde{Q}] = D_{\imath} \tilde{Q}$ is the one used here, and it was checked numerically — see the companion.) The second is the **Bianchi identity**,

$$
D_{\imath} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0,
$$

where each $D$ is the adjoint covariant derivative. It is the statement that the exterior derivative of the curvature is a cycle, and it is automatic for a curvature built from a connection: it follows from the Jacobi identity for the operators $D_{\imath}$, $[D_{\imath},[D_{\imath},D_{\jmath}]] + \text{cyclic} = 0$, together with $[D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath}$; equally, at the level of components, from the derivation property of the adjoint action.

The biquaternion packaging of the curvature, inherited from the parents, is the definition

$$
\mathcal{F} = \tfrac12\sum_{\imath,\jmath}F_{\imath\jmath}\,\bar{e}_{\imath} e_{\jmath} \;\in\; \mathbb{B},
\qquad \bar{e}_t = e_t,\; \bar{e}_{\imath} = -\vec e_{\imath} .
$$

It collects the six independent curvature components against the quaternion-basis products $\bar{e}_{\imath} e_{\jmath}$. What this object does and does not inherit under a local transformation is treated in its own section below; the reader should not assume that the componentwise transformation law $F_{\imath\jmath}\mapsto \tilde UF_{\imath\jmath}\tilde U^{-1}$ promotes to a single conjugation of $\mathcal{F}$.

## The Yang–Mills Action

The field equation this article is about is the stationarity condition of one functional. The functional settles three things the equation alone cannot: which pairing makes the density invariant, where the coupling sits, and why the theory is interacting. This section writes it, and §*The Variation* takes its derivative.

**The density, and the invariance in one line.** With $\mathrm{Tr}$ the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$ restricted to the $\mathrm{SU}(2)$ factor,

$$
\mathcal{L}=-\tfrac12\,\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr),
\qquad
S_{\mathrm{YM}}=\int d^4r\;\mathcal{L}.
$$

The curvature rotates in the adjoint, $F_{\mathrm g,\imath\jmath}=\tilde QF_{\imath\jmath}\tilde Q^{-1}$, so the density is unchanged, and the reason is one line:

$$
\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\mathrm g,\imath\jmath}F_{\mathrm g,\imath\jmath}\Bigr)
=\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}\bigl(\tilde QF_{\imath\jmath}\tilde Q^{-1}\bigr)\bigl(\tilde QF_{\imath\jmath}\tilde Q^{-1}\bigr)\Bigr)
=\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr).
$$

Two facts and nothing else are used: the adjoint law of the field strength, and the cyclicity of the trace. In the abelian case the adjoint law degenerates to invariance and cyclicity is not needed; here cyclicity is the whole of the invariance.

**The trace is the matrix trace, and it is not the informational reduction.** The corpus carries a second two-slot functional, $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, inherited from the plain form. It is not cyclic. Substituted into the density it would leave the action changed by a local transformation, and the theory would no longer be a connection theory: the transformation that the connection was introduced to make local would move the action. The two functionals agree when one slot is a scalar, and a curvature is not a scalar. [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html) states the three requirements on a density, proves cyclicity is the whole of the invariance, and exhibits a pairing that fails it; the point is cited here rather than repeated, because it is a statement about the module and belongs to no sector.

**Why this term and no other.** At dimension four the only invariant built from the curvature alone is its square. A cubic term does not exist, since the trace of an odd number of generators vanishes. A term carrying one derivative of the curvature has dimension five. The overall coefficient is then fixed by the normalisation of the generators and by nothing else, and the normalisations the corpus uses — $T_a=\tfrac12 e_a$, $2\,\mathrm{Sc}(T_aT_b)=-\tfrac12\delta_{ab}$ — are the ones that make the coefficient $\tfrac12$.

**Why the commutator makes the theory interacting.** In the abelian case the curvature is linear in the connection, and the density is quadratic. Here $F_{\imath\jmath}$ contains $i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$, which is quadratic in $\mathcal{A}$; squaring $F$ therefore produces cubic and quartic terms. Those are the connection's self-coupling. Nothing was added: the self-coupling is the square of a curvature that is itself non-linear, and that non-linearity is the statement that the group is non-abelian.

**The reality and the sign.** The density must be a real scalar and its sign must leave the energy bounded below. Both follow from the Hermiticity type of the field and from the normalisation of the basis, and neither is an extra condition imposed on the action. [The Invariant Density](the-invariant-density-which-pairing-the-action-can-integrate.html) carries the argument and fixes $\tfrac12$ in the element form and $\tfrac14$ in the component form.

**Where the coupling sits, and why it cannot be removed.** Rescaling $\mathcal{A}_{\imath}\to\mathcal{A}_{\imath}/\kappa$ moves the coupling out of the commutator and into the overall coefficient as $1/\kappa^{2}$; the two placements are one theory. What matters is which term carries the coupling relative to the other. In the abelian case the coupling multiplies the whole density and cancels from the equation. Here the commutator carries one power of the coupling and the derivative carries none, so the ratio of the two terms is physical, and that ratio is the coupling. This is the sharpest structural difference between the two theories, and it is the reason the non-abelian coupling runs while the abelian one does not.

### The Two Settings

**The element setting.** The density as $-\tfrac12\mathrm{Tr}(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath})$ with $F$ an algebra element. The invariance is one line and the trace-versus-reduction distinction is visible; the vertices are not.

**The component setting.** The same density with the structure constants written out,

$$
\mathcal{L}=-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},
\qquad
F_{a,\imath\jmath}=\partial/\partial R_{\imath}\mathcal{A}_{a,\jmath}-\partial/\partial R_{\jmath}\mathcal{A}_{a,\imath}+g\sum_{b,c}\varepsilon_{abc}\mathcal{A}_{b,\imath}\mathcal{A}_{c,\jmath},
$$

with the coupling $g$ absorbed into the normalisation of $\mathcal{A}_{a}$. The vertices are visible and the coupling's place in the commutator is visible; the local invariance is not.

The two settings hide each other's strengths. The passage between them is the passage between the trace and the structure constants, through $[T_a,T_b]=\varepsilon_{abc}T_c$ with $T_a=\tfrac12 e_a$. They differ in the reality of the coupling: with $g$ real the curvature is anti-Hermitian and the density is a sum of squares, while the element setting above carries $i\kappa$ inside the commutator and a curvature in $\mathrm{SU}(2)\oplus i\,\mathrm{SU}(2)$. The trade of $g$ for $i\kappa$ changes no vertex and no equation. Both settings are one action read two ways, and the component setting is the one in which "the coupling is a number" is literal.

## The Variation: The Equation from the Curvature's Square

Vary the connection, $\mathcal{A}_{\imath}\mapsto\mathcal{A}_{\imath}+\delta\mathcal{A}_{\imath}$, with $\delta\mathcal{A}_{\imath}$ an $\mathrm{SU}(2)$-valued element that vanishes on the boundary. The variation of the curvature is the covariant derivative of the variation,

$$
\delta F_{\imath\jmath}=D_{\imath}\,\delta\mathcal{A}_{\jmath}-D_{\jmath}\,\delta\mathcal{A}_{\imath}.
$$

That display is the whole content of "the curvature is a tensor": the variation of a tensor is a tensor, and the derivative that appears is the covariant one. The commutator terms of $\delta F$ have combined into exactly this, which is why the connection's inhomogeneous transformation law and the curvature's homogeneous one are the same statement.

**The variation of the action.** Substituting, using the antisymmetry of $F_{\imath\jmath}$ and the cyclicity of the trace, and integrating by parts with the boundary term dropped,

$$
\delta S_{\mathrm{YM}}
=-\int d^4r\;\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}\delta F_{\imath\jmath}\,F_{\imath\jmath}\Bigr)
=2\int d^4r\;\mathrm{Tr}\Bigl(\sum_{\jmath}\delta\mathcal{A}_{\jmath}\,D_{\imath}F_{\imath\jmath}\Bigr).
$$

The factor two comes from the two ways the variation meets the two curvature slots, and the two ways are equal by the trace's symmetry. The derivative that has been moved onto $F$ is covariant, because the integration by parts on an adjoint-valued field must use the adjoint covariant derivative and not the ordinary one; using the ordinary derivative would leave a non-covariant boundary term.

**The equation.** Stationarity for every $\delta\mathcal{A}_{\jmath}$ gives

$$
\boxed{\;\sum_{\imath}D_{\imath}F_{\imath\jmath}=0\;}
$$

the source-free Yang–Mills equation. Three things are worth separating in it. The derivative is covariant, so the equation is covariant. The contraction is between the derivative's index and the curvature's first index, which is the placement §*The Yang–Mills Equation* fixes from a different direction. And the equation is not the Bianchi identity: the Bianchi identity is an identity of any curvature, while this is a condition on the connection.

**The variation is the derivative of the density, and the density is not the equation.** This is the place where the two orders can be confused. The density is quadratic in a curvature that is quadratic in the connection; its variation is linear in the variation and linear in the equation. The equation is therefore not "the density set to zero": a configuration whose density vanishes pointwise need not be stationary, and a solution need not have vanishing density. Nor is the equation obtained by reading coefficients off the Lagrangian, because the variation acts on the connection inside $F$ and not on $F$ itself.

**The source.** Away from matter the equation is the one boxed above. With matter the right-hand side is a current, and the current is not an independent object: it is the covariant divergence of the curvature, defined so that the equation holds identically. §*The Yang–Mills Equation* defines it that way, and §*The Noether Currents* shows that the current of the global symmetry is the same object.

## The Yang–Mills Equation

Let the current be the covariant divergence of the curvature,

$$
\boxed{\;\tilde J_{\Phi} := \tilde D\tilde F = \tilde\nabla_\Phi\tilde F + i\kappa\,[\mathcal{A}, \tilde F], \qquad \tilde J_{\Phi} \in \mathrm{SU}(2)\;},
$$

summed over $\mu$. This is the definition of the source in this article; the equation

$$
\,\sum_{\imath} D_{\imath} F_{\imath\jmath} = J_{\jmath}\,
$$

is the Yang–Mills equation, and the two terms of its expansion are the whole of its content.

- **The ordinary divergence $\sum_{\imath}\partial/\partial R_{\imath} F_{\imath\jmath}$.** In the abelian limit this term alone is Maxwell's source equation. In the non-abelian case it is not covariant on its own.
- **The commutator term $i\kappa[\mathcal{A}_{\imath},F_{\imath\jmath}]$.** The index $\mu$ of the connection is contracted with the *derivative* index of $F_{\imath\jmath}$ — the first index — and the commutator is taken with that same $\mathcal{A}_{\imath}$. This is the only placement that makes the equation covariant and the current covariantly conserved; it is the term most often got wrong. In the abelian case $\mathcal{A}_{\imath}$ commutes with the curvature (it is central in the parent's $\mathrm{U}(1)$ case, and lies on a single generator otherwise), so the term vanishes.

The two slots of the index structure are fixed. The derivative that acts is the one whose index is contracted, and it must be the same index that labels the connection inside the commutator; and the curvature is contracted in its first index by that derivative. Writing $[\mathcal{A}_{\jmath},F_{\imath\jmath}]$ (connection index equal to the free index), or $[\mathcal{A}_{\imath},F_{\jmath\imath}]$ (the two curvature slots exchanged), or reversing the sign of the commutator term, each destroys the conservation law derived in the next section. This was checked directly on a generic non-commuting connection: the correct placement gives $\sum_{\jmath} D_{\jmath}(\sum_{\imath} D_{\imath} F_{\imath\jmath}) = 0$ to $3\times10^{-15}$, while the three alternatives and the ordinary divergence give residuals of order $10$ — order unity on the same field. The reader who is unsure of a sign convention should repeat that one computation rather than consult memory.

**Covariance.** The equation is covariant without any representative being chosen. With $F_{2,\imath\jmath} = \tilde UF_{\imath\jmath}\tilde U^{-1}$ and the transformation of the connection, the covariant derivative satisfies $D_{2,\imath}(\tilde U\tilde{Ξ}) = \tilde U D_{\imath}\tilde{Ξ}$, so the current transforms in the adjoint,

$$
J_{2,\jmath} = \tilde U J_{\jmath} \tilde U^{-1},
$$

and $\sum_{\imath} D_{2,\imath}F_{2,\imath\jmath} = \tilde U(\sum_{\imath} D_{\imath} F_{\imath\jmath})\tilde U^{-1}$. The equation $\sum_{\imath} D_{\imath} F_{\imath\jmath} = J_{\jmath}$ therefore holds in one representative if and only if it holds in every representative; no condition such as $S = \mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\mathcal{A}) = 0$, and no other fixing the representative surface, is imposed or available. This point is worth stating because the framework's canonical-quantisation article records that it *cannot* fix the representative; the Yang–Mills equation inherits that situation rather than relieving it. The adjoint transformation of the source was verified numerically on a generic connection with a generic (constant) group rotation; the covariance for a general local $\tilde U$ follows from the transformation laws above and was not separately rechecked.

**Biquaternionic form.** Pack the four components of the current into a biquaternion in the quaternion basis,

$$
\mathcal{J} = \sum_{\jmath\in\{t,x,y,z\}} J_{\jmath} e_{\jmath} \;\in\; \mathbb{B}.
$$

Then the Yang–Mills equation is the single biquaternion equation

$$\boxed{\;\sum_{\jmath\in\{t,x,y,z\}} \bigl(D_{\imath} F_{\imath\jmath}\bigr) e_{\jmath} = \mathcal{J},
\qquad\text{equivalently}\qquad
\sum_{\jmath\in\{t,x,y,z\}} \bigl(D_{\imath} F_{\imath\jmath}\bigr) e_{\jmath} = \sum_{\jmath\in\{t,x,y,z\}} J_{\jmath}\, e_{\jmath}\;},$$

in which the covariant derivative acts on the $\mathrm{SU}(2)$-valued curvature components by the adjoint action $D_{\imath} F_{\imath\jmath} = \partial/\partial R_{\imath} F_{\imath\jmath} + i\kappa[\mathcal{A}_{\imath},F_{\imath\jmath}]$, and the sum over $\mu$ is the divergence. The left-hand side is the covariant divergence of the curvature, expanded in the quaternion basis; the right-hand side is the source biquaternion. This is the direct non-abelian analogue of the parent's $\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi}$: the parent's source $Z\,\tilde{J}_{\Phi}$, with $\tilde J_{\Phi}$ the four-current, plays the role of $-\mathcal{J}$ up to the parent's normalisation of $\tilde{F}$ (the parent uses $R_0 = i\rho/\epsilon$, $\vec R = Z\,\vec J$, and writes its equation with the opposite sign). The sign of the source is a convention, fixed here by defining $J_{\jmath}$ through the field equation; what is not a convention is that the derivative on the left is covariant.

**The biquaternion packaging does not collapse.** It is tempting to write the left-hand side as $\sum_{\imath} D_{\imath} F_{\imath}$ with $F_{\imath} := \sum_{\jmath} F_{\imath\jmath}e_{\jmath}$, and to advertise a one-line product. That is not correct, and the failure is instructive. Because the adjoint commutator does not pass through the quaternion basis,

$$
D_{\imath}\bigl(F_{\imath\jmath}e_{\jmath}\bigr) = \bigl(D_{\imath} F_{\imath\jmath}\bigr)e_{\jmath} + i\kappa\,F_{\imath\jmath}\,[\mathcal{A}_{\imath},e_{\jmath}],
$$

the extra term $i\kappa\sum_{\imath\jmath}F_{\imath\jmath}[\mathcal{A}_{\imath},e_{\jmath}]$ is present whenever $\mathcal{A}_{\imath}$ fails to commute with the basis elements. It does not vanish for a generic non-abelian connection, and it was verified to be of order unity. The biquaternionic field equation is therefore the basis-expanded contraction written above, not a single adjoint-covariant product of a packaged curvature. This is the same lesson the parent article records about $\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\mathcal{A})$: the quaternion packaging of a non-abelian curvature is a bookkeeping device, and products of packaged objects hide index mixing that must be checked.

## Covariant Conservation of the Current

The source defined by the field equation is not free. Applying the adjoint covariant derivative to the field equation and using the antisymmetry of the curvature,

$$
\sum_{\jmath} D_{\jmath} J_{\jmath} = \sum_{\imath,\jmath}D_{\jmath} D_{\imath} F_{\imath\jmath}
= \tfrac12\sum_{\imath,\jmath}\{D_{\jmath},D_{\imath}\}F_{\imath\jmath} + \tfrac12\sum_{\imath,\jmath}[D_{\jmath},D_{\imath}]F_{\imath\jmath}.
$$

The two pieces are handled separately.

- **The symmetric piece vanishes by antisymmetry.** The anticommutator $\{D_{\jmath},D_{\imath}\}$ is symmetric in $\mu\jmath$, while $F_{\imath\jmath}$ is antisymmetric; contracting the two gives zero. Explicitly, relabelling ${\imath}\leftrightarrow\jmath$ in one half of the sum turns $\sum_{\imath,\jmath}\{D_{\jmath},D_{\imath}\}F_{\imath\jmath}$ into its own negative.
- **The antisymmetric piece vanishes by antisymmetry and the curvature identity.** Since $[D_{\jmath},D_{\imath}] = i\kappa F_{\jmath\imath}$ acts on $F_{\imath\jmath}$ by commutation,
$$
\tfrac12\sum_{\imath,\jmath}[D_{\jmath},D_{\imath}]F_{\imath\jmath} = \tfrac12 i\kappa\,\sum_{\imath,\jmath}[F_{\jmath\imath},F_{\imath\jmath}],
$$
and the summed commutator vanishes: relabelling ${\imath}\leftrightarrow\jmath$ and using $F_{\jmath\imath} = -F_{\imath\jmath}$ shows the sum equals its own negative.

Hence

$$
\boxed{\,\sum_{\jmath} D_{\jmath} J_{\jmath} = 0}
$$

the current is **covariantly conserved**. Expanding the definition, this is

$$
\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} + i\kappa\,[\mathcal{A}, \tilde J_{\Phi}] = 0,
\qquad\text{that is}\qquad
\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = -\,i\kappa\,[\mathcal{A}, \tilde J_{\Phi}].
$$

The ordinary divergence does not vanish. For a generic non-abelian connection it is of order unity, and only the covariant divergence is zero; the difference is exactly the commutator of the connection with the current. This was recomputed on a generic non-commuting connection: $\sum_{\jmath} D_{\jmath} J_{\jmath}$ vanishes to $3\times10^{-15}$ while $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural}$ has magnitude $\approx 7$. Writing $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = 0$ for the non-abelian current is false, and would drop the term that carries the adjoint action.

**What the conservation uses, and what it does not.** It is often said that the current is conserved "by the Bianchi identity". In this derivation the differential Bianchi identity $D_{\imath} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0$ is *not* used. What is used is the field equation, the antisymmetry of $F_{\imath\jmath}$, and the curvature identity $[D_{\jmath},D_{\imath}] = i\kappa F_{\jmath\imath}$; the vanishing commutator $\sum_{\imath,\jmath}[F_{\jmath\imath},F_{\imath\jmath}] = 0$ is an algebraic consequence of antisymmetry, not the differential identity. (That algebraic identity is itself sometimes called a Bianchi identity, being the contracted statement that the curvature is an algebra element; the differential identity is a different object, and it is the differential one that is not needed here.) The differential Bianchi identity is the independent *homogeneous* half of the non-abelian system, treated in its own section below. The two are sometimes conflated because both are identities of the curvature and both trace back to the Jacobi identity at the level of operators; the reader is entitled to know which one does the work. The claim to be verified for the conservation is therefore field equation plus antisymmetry, and that is what was checked.

**Consistency, not an extra condition.** In the abelian case the analogous statement $\sum_{\imath,\jmath}\partial/\partial R_{\jmath}\,\partial/\partial R_{\imath} F_{\imath\jmath} = 0$ is automatic, and charge conservation is recovered from the field equation rather than imposed. In the non-abelian case the same logic gives the covariant law; the current defined by the field equation is covariantly conserved automatically, and no independent condition on $\rho$ and $\vec J$ is added. In this sense $\sum_{\jmath} D_{\jmath} J_{\jmath} = 0$ is the integrability condition of the Yang–Mills system, exactly as ordinary conservation is the integrability condition of Maxwell's system.

## The Constraints the Action Imposes: Gauss's Law and Two Polarizations

**The time component is not an evolution equation.** Writing the source-free equation at $\jmath=0$,

$$
\sum_{j}D_{j}F_{j0}=0,
$$

gives an equation with no time derivative of $\mathcal{A}_{0}$: it constrains the connection at each instant. This is the non-abelian Gauss law. Every component of the equation with $\jmath$ spatial is second order in time and evolves the three spatial components of $\mathcal{A}_{\imath}$.

**The count.** A first-class constraint removes two components per generator, one as the constraint and one as the redundancy that a local transformation still has after the constraint is imposed. The remaining two per generator are the transverse polarizations of a massless spin-one field. For $\mathrm{SU}(2)$ that is $3\times(4-2)=6$ physical modes among the twelve components of $\mathcal{A}_{\imath}$. In the abelian case the same count holds, and the reason the count is the same is that the constraint's *class* is the same; what changes is the constraint's content.

**Why the constraint is non-linear.** The Gauss law contains the connection, $D_{j}F_{j0}=\partial/\partial R_{j}F_{j0}+i\kappa[\mathcal{A}_{j},F_{j0}]$. In the abelian case it is a Poisson equation for the scalar potential, solved once and for all, and the propagation problem is then linear. Here it is a non-linear equation for $\mathcal{A}_{0}$ given the spatial components, and it has no closed-form solution. This is the technical content of "the connection carries the charge it couples to": the charge density that sources $\mathcal{A}_{0}$ depends on $\mathcal{A}_{0}$.

**The consequence for quantisation.** A non-linear first-class constraint is why the non-abelian theory is not quantised by imposing the constraint on a Fock space built from free fields. The route is the path integral over the orbit, with the constraint's gauge-fixing and its field-dependent determinant. [The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form](the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html) carries that construction, and the field dependence of the determinant there is exactly the non-linearity found here.

## The Noether Currents: The Colour Current and Its Own Source

**The current.** The density is invariant under the *global* $\mathrm{SU}(2)$, so Noether's theorem gives a conserved current. In the component setting, with the coupling real,

$$
j_{a,\imath}=\sum_{b,c}\varepsilon_{abc}F_{b,\imath\jmath}\mathcal{A}_{c,\jmath}.
$$

Noether's theorem itself, and the reason the current is a bivector contracted into a vector, are the subject of [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html); here only the non-abelian structure of the result matters.

**The current contains the connection.** The abelian current is built from $F$ alone. This one is bilinear and carries $\mathcal{A}_{c,\jmath}$ explicitly. That is not a defect of the formula; it is the statement that the connection is charged under the group it defines. A current built from $F$ alone cannot be the non-abelian current, because $F$ transforms in the adjoint and its square is a singlet.

**Conservation is covariant.** The ordinary divergence $\sum_{\imath}\partial/\partial R_{\imath}j_{a,\imath}$ does not vanish, and the covariant one does, $\sum_{\imath}D_{\imath}j_{a,\imath}=0$. The difference is a term linear in the connection, and it is the same term that separates the covariant from the ordinary divergence in §*Covariant Conservation*. The identity of the two statements is not a coincidence: the current of the global symmetry is the source defined by the field equation, up to the sign and the normalisation conventions of the two derivations.

**Energy–momentum.** Translation invariance gives

$$
T_{\imath\jmath}=\mathrm{Tr}\Bigl(\sum_{k}F_{\imath k}F_{\jmath k}\Bigr)-\tfrac14\delta_{\imath\jmath}\,\mathrm{Tr}\Bigl(\sum_{a,b}F_{ab}F_{ab}\Bigr),
$$

symmetric and traceless at the classical level. The tracelessness is the classical scale invariance of a density with no dimensionful parameter. Its violation in the quantum theory is the beta function, so the trace anomaly and the running coupling are one statement seen twice; [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html) takes the running, and [The Conformal Anomaly in Biquaternionic Form](the-conformal-anomaly-in-biquaternionic-form.html) takes the trace.

**What the classical density does not give.** It gives no $\theta$ term, which is a total derivative and a separate coupling; it gives no mass gap, which is a non-perturbative question the density states but does not answer; and it gives no running, which is a one-loop object. Each of the three has its own article, and none of them is a correction to what is written here.

## The Abelian Limit

The abelian case is the case of a **commuting generator set**: the connection takes values in a one-dimensional subalgebra, so that all its coefficients commute. Two settings realise it in the framework. The parent's abelian connection lies in the centre $\mathbb{B}_{C}$, whose imaginary scalar $ie_t$ commutes with every biquaternion; and any connection proportional to a single fixed generator, $\mathcal{A}_{\imath} = a_{\imath}(\tilde{Q})\,\vec e_x$, has commuting coefficients even though $\vec e_x$ is not central. The reduction to Maxwell is the same in both, and it is worth saying exactly which terms vanish and why.

Write $\mathcal{A}_{\imath} = a_{\imath}\,g$ for a fixed generator $g$ with $a_{\imath}$ scalar functions (for the centre, $g = ie_t$; for a single spatial generator, $g = \vec e_x$). Then

$$
[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}] = a_{\imath} a_{\jmath}\,[g,g] = 0,
$$

so the curvature loses its commutator,

$$
F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath} = (\partial/\partial R_{\imath} a_{\jmath} - \partial/\partial R_{\jmath} a_{\imath})\,g,
$$

and the Yang–Mills equation loses its own commutator term for the same reason:

$$
[\mathcal{A}_{\imath},F_{\imath\jmath}] = \sum_{\imath} a_{\imath}\,(\partial/\partial R_{\imath} a_{\jmath} - \partial/\partial R_{\jmath} a_{\imath})\,[g,g] = 0 .
$$

The field equation is therefore

$$
\tilde D\tilde F = \tilde\nabla_\Phi\tilde F = \tilde J_{\Phi},
$$

which is Maxwell's source equation, and the current is now a commuting biquaternion, invariant under the abelian local transformations that preserve the generator set. Correspondingly the conservation law degenerates,

$$
\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} + i\kappa\,[\mathcal{A},\tilde J_{\Phi}] = \langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = 0,
$$

because $[\mathcal{A}_{\jmath},J_{\jmath}] = \sum_{\jmath} a_{\jmath}[g,g]J_{\jmath} = 0$; the current is **ordinarily** conserved, and it is invariant under the abelian local transformations that preserve the commuting generator set, $J_{2,\jmath} = \tilde U J_{\jmath} \tilde U^{-1} = J_{\jmath}$ (in the centre case every central $\tilde U$ qualifies, since $\tilde U$ is central; on a single spatial generator, the qualifying $\tilde U$ are those of the abelian subgroup generated by $g$).

Nothing here cancels. Every non-abelian term vanishes because the abelian connection commutes — with itself, with the curvature it generates, and with the current — not because two nonzero contributions are arranged to cancel. This is the precise sense in which the abelian case is the degenerate one, and it is why agreement on a commuting generator set is a consistency check on normalisation and signs but *not* evidence for the non-abelian statement: every non-abelian identity above was checked on the full non-commuting $\mathrm{SU}(2)$ connection, where the commutators are nonzero, and the abelian reduction was checked separately.

## The Bianchi Identity and the Homogeneous Half

The Yang–Mills equation is half of the non-abelian system. The other half is the Bianchi identity,

$$
D_{\imath} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0,
\qquad\text{equivalently}\qquad
D_{\imath} {\star}F_{\imath\jmath} = 0,
$$

where ${\star}F$ is the dual field strength. Unlike Maxwell's source equation, this identity is not an equation of motion: it is a consequence of building $F$ from $\mathcal{A}$, and it holds for every connection. It is the non-abelian analogue of "the homogeneous Maxwell equations are identities once the field strength is a curl". The index-mixing term displayed earlier is the kind of contribution that the naive one-line product leaves behind; the Bianchi identity is the statement that the corresponding antisymmetrised combination of covariant derivatives of $F$ vanishes, and it is the homogeneous half of the system.

The relation between the two halves is worth stating without overclaim. The field equation determines $J_{\jmath}$ and implies its covariant conservation; the Bianchi identity constrains the curvature independently of the source and is what the dual equation $D_{\imath}{\star}F_{\imath\jmath} = 0$ expresses. Neither implies the other: the conservation of the current is not the Bianchi identity, and the source-free Yang–Mills equation $\sum_{\imath} D_{\imath} F_{\imath\jmath} = 0$ is not the Bianchi identity either — a distinction the minimal coupling companion records explicitly for the abelian one-line equation $\tilde\nabla_\Phi\tilde{F} = 0$, and which survives verbatim here.

## What the Biquaternion Packaging Does and Does Not Give

The framework's compact form of the abelian equations, $\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi}$, is a genuine one-line equation. For the non-abelian system the analogous packaging is more delicate, and this article records the limits of what the packaging delivers rather than presenting a formula that would not survive a recheck.

The curvature biquaternion is defined, as in the parent, by $\mathcal{F} = \tfrac12\sum_{\imath\jmath}F_{\imath\jmath}\bar{e}_{\imath} e_{\jmath}$. Its *components* transform in the adjoint, $F_{2,\imath\jmath} = \tilde UF_{\imath\jmath}\tilde U^{-1}$, so $\mathcal{F}$ inherits the componentwise adjoint law

$$
\mathcal{F}_2 = \tfrac12\sum_{\imath\jmath}\bigl(\tilde UF_{\imath\jmath}\tilde U^{-1}\bigr)\bar{e}_{\imath} e_{\jmath} .
$$

This is **not** the single algebra conjugation $\tilde Q\mathcal{F}\tilde Q^{-1}$, because $\tilde Q^{-1}$ does not pass through the basis product $\bar{e}_{\imath} e_{\jmath}$. The two agree only when the group element $\tilde Q$ commutes with the basis product $\bar{e}_{\imath} e_{\jmath}$, i.e. in the centre case. This was verified: with a generic constant $*$-unitary $\tilde Q$, $\mathcal{F}_2 = \tfrac12\sum(\tilde UF_{\imath\jmath}\tilde Q^{-1})\bar{e}_{\imath} e_{\jmath}$ holds to machine precision, while $\mathcal{F}_2 = \tilde Q\mathcal{F}\tilde Q^{-1}$ fails by order unity. The componentwise law is what makes the current transform as $J_{2,\jmath} = \tilde UJ_{\jmath} \tilde Q^{-1}$ and what keeps the field equation covariant; the packaged law is simply not available.

Two consequences follow, and both are stated as findings rather than repairs.

- **The source biquaternion $\mathcal{J} = \sum_{\jmath} J_{\jmath} e_{\jmath}$ is a valid packaging.** Its components transform in the adjoint, and the equation $\sum_{\jmath} \bigl(D_{\imath} F_{\imath\jmath}\bigr) e_{\jmath} = \mathcal{J}$ is exact and covariant. This is the biquaternionic form of the Yang–Mills equation used here.
- **A single adjoint-covariant product of the curvature is not that equation.** As shown in the previous section, $\sum_{\imath} D_{\imath}(\sum_{\jmath} F_{\imath\jmath}e_{\jmath})$ differs from $\sum_{\imath,\jmath} \bigl(\sum_{\imath} D_{\imath} F_{\imath\jmath}\bigr) e_{\jmath}$ by the index-mixing term $i\kappa\sum_{\imath\jmath}F_{\imath\jmath}[\mathcal{A}_{\imath},e_{\jmath}]$, which is nonzero for a generic connection. Whether some other representative of the non-abelian curvature makes the field equation a one-line product, in the way the pure-vector Riemann–Silberstein representative does in the abelian case, is not settled here.

**A neighbouring claim: the triplet from the electromagnetic potential.** One external programme makes a stronger statement than anything above, and it is worth separating because it reverses the direction of dependence between the abelian and non-abelian fields. In Kassandrov's algebrodynamics (recorded in *The Algebrodynamical Programme*) the biquaternion connection is split into a trace part and a scalar-free part, $\Gamma_{\jmath}=\tfrac12A_{\jmath} I+N_{\jmath}$, and the scalar-free part is prescribed **linearly** by the same complex four-vector that serves as the electromagnetic potential,

$$
N_{a0}=A_a, \qquad N_{ab}=\delta_{ab}A_0-i\sum_c\varepsilon_{abc}A_c .
$$

Its strength $L_{\imath\jmath}=\tfrac12\left(\partial/\partial R_{\imath}\,N_{\jmath}-\partial/\partial R_{\jmath}\,N_{\imath}\right)-[N_{\imath},N_{\jmath}]$ is self-dual on the solutions of the programme's primary equation, and the Bianchi identity then gives the Yang–Mills equation $\sum_{\jmath}\partial/\partial R_{\jmath} L_{\imath\jmath}=\sum_{\jmath}[N_{\jmath},L_{\imath\jmath}]$. The abelian–non-abelian link is a determinant: the curvature splits into a trace part proportional to the electromagnetic field strength $F_{\mathrm{em},\imath\jmath}=\partial/\partial R_{\imath} A_{\jmath}-\partial/\partial R_{\jmath} A_{\imath}$ and the trace-free $L_{\imath\jmath}$, and $\det \mathrm{Ric}_{\imath\jmath}=0$ — which holds because the non-trivial spinor lies in its kernel — makes the electromagnetic field strength the **modulus of the triplet**, $\sum_a(L_{a\imath\jmath})^2\propto(F_{\mathrm{em},\imath\jmath})^2$ (the constant is convention-dependent and is not reconciled; the superscript marks the abelian quantity, to be read apart from this article's $F_{\imath\jmath}$). Here the Yang–Mills field has **no independent existence**, being a function of the electromagnetic potential, which is a different relation between the two fields from any construction in this article. It is a claim of that programme, conditional on its nonlinear primary equation, recorded there and not adopted here.

## The Ceiling Is in the Algebra and Not in the Action

**The statement.** Everything above holds for any subalgebra of the algebra's compact part. It gives $\mathrm{U}(1)$ and $\mathrm{SU}(2)$ exactly. It gives nothing for $\mathrm{SU}(3)$.

**Where the ceiling sits.** Not in the density. The functional $-\tfrac12\mathrm{Tr}(\sum F F)$ is form-invariant: written for a connection valued in any matrix algebra it defines a Yang–Mills action, and the strong-force articles do write one, in components and on a transcribed matrix connection. The obstruction is the carrier. The compact part of $\mathbb{B}$ has real dimension four and consists of $\mathrm{U}(1)\oplus\mathrm{SU}(2)$; a connection in $\mathfrak{su}(3)$ needs eight independent anti-Hermitian generators with $\mathrm{SU}(3)$ commutators, and the algebra supplies no such eight. The action can be written for a group the algebra cannot carry, and then it is a matrix transcription rather than an action on the algebra's own elements.

**What follows for the four sectors.** The electromagnetic and weak densities are written on the algebra's elements; the strong density only in components, on the transcribed side of the ceiling; and the gravitational one as a quadratic density without a carrier. The asymmetry among the sectors is therefore a statement about the algebra, and the ceiling article argues it once: [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). Nothing in this article weakens or repairs it, and a reader who wants a $\mathrm{SU}(3)$ action written on elements will not get one here.

## A Biwave Equation with a Vector Structural Coefficient

There is a second biquaternion equation in the literature whose matrix form has been called Yang–Mills-like, and it is worth separating from the construction above. In a four-part series on the differential algebra of biquaternions, L. A. Alexeyeva studies the wave equation

$$
\vec\nabla_{+} B + F \circ B = G(\tau, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),
\qquad
\vec\nabla_{-} B + F \circ B = G(\tau, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),
$$
$$
\vec\nabla_{+} = \partial/\partial \tau + i\,\vec\nabla_\Phi ,
\qquad
\vec\nabla_{-} = \partial/\partial \tau - i\,\vec\nabla_\Phi ,
$$

where $\tau$ is time in units of length, $\circ$ the biquaternion product, $G$ a given biquaternionic source, and $F = f + \vec F$ a **constant** biquaternion — the *structural coefficient* — with scalar part $f$ and vector part $\vec F$ [Alexeyeva 2014]. The four papers are a sequence of specialisations of this one equation: the earlier ones treat the members equivalent to the biquaternionic Maxwell system ($F = 0$) and to the biquaternionic Dirac system ($F = f$, a complex scalar), with their generalisations, and the fourth takes the **vector-valued** coefficient $\vec F \neq 0$. The author's remark for that case is that the equation, written in matrix (tensor) form, belongs to the class of Yang–Mills equations. Recording the series here gives the corpus a single source for the Maxwell–Dirac–Yang–Mills web that the framework's own articles reach by separate routes.

**What the identification is, and what it is not.** The coefficient is constant, so the equation carries no non-constant connection, no commutator curvature and no covariant derivative of the kind $D_{\imath}$ above. "Belongs to the class of Yang–Mills equations" is a statement about the **matrix form of a linear first-order system with matrix coefficients** — the shape of the equation, not its structure. The two constructions are therefore not competing derivations of one object: this article's equation is non-linear in a field-valued connection and its current is only covariantly conserved, while the biwave equation is linear with a fixed coefficient. That one route reaches a Yang–Mills-type matrix form from a constant coefficient, and the other from a connection, is a genuine difference of route, and the corpus records it as such rather than as an agreement.

**Second-order form and solution.** Composing the two mutual operators for constant $\vec F$ gives the single second-order operator

$$
\left(\vec\nabla_{-} - \vec F\right)\circ\left(\vec\nabla_{+} + \vec F\right)
= \Box_A + (\vec F,\vec F) + 2i(\vec F,\vec\nabla_\Phi),
\qquad
\Box_A = \partial^2/\partial \tau^2 - \Delta_\Phi ,
$$

so each component of $B$ solves a Klein–Gordon–Fock-type equation whose mass is the norm $(\vec F,\vec F)$ of the coefficient, plus one first-order directional term. *The Klein–Gordon Equation in Biquaternionic Form* treats that operator and the sense in which the vector coefficient makes it factor into first-order operators, which is the point of contrast with its scalar-coefficient case. The inhomogeneous equation is solved by convolution with the fundamental solution

$$
\tilde{Ξ}(\tau,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \frac{\exp(i\theta_{\mathrm{spa}})}{4\pi|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|},\qquad \theta_{\mathrm{spa}}=(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\in\mathbb{R},\left((1-a)\,\delta(\tau-|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|) + a\,\delta(\tau+|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|)\right) + \tilde{Ξ}^0(\tau,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),
\qquad a \in \mathbb{C},
$$

with $\tilde{Ξ}^0$ an arbitrary solution of the homogeneous scalar equation: a superposition of the retarded and advanced $\delta$-layers on the light cone carrying the exponential weight $\exp(i\theta_{\mathrm{spa}})$, the constant $a$ choosing the branch. The published form of the solution is $B = (\vec\nabla_{-} - \vec F)(\tilde{Ξ} * G) + B^0$, the homogeneous part $B^0$ being built from the same kernel and arbitrary biquaternionic fields. The weight is not decoration: the Fourier denominator is $(\vec\zeta + \vec F, \vec\zeta + \vec F) - \omega^2$, which is *linear* in the wave vector, and that is why the kernel is a $\delta$-layer on the cone rather than the Bessel-type kernel of the ordinary massive case.

**The characteristic surface, by case.** The homogeneous equation $\vec\nabla_{+} B + \vec F\circ B = 0$ has plane-wave solutions supported on

$$
S = \left\{(\omega,\vec\zeta) : (\vec\zeta + \vec F, \vec\zeta + \vec F) = \omega^2\right\},
$$

with $(\cdot,\cdot)$ the complex-bilinear pairing. Writing $\vec F = -E - iH$ with $E, H$ real vectors, the surface degenerates according to which part of the coefficient is present:

| Coefficient | Surface $S$ | Interpretation |
|---|---|---|
| real, $\vec F = -E$ | cone in $\mathbb{R}^4$ with vertex $(\omega,\vec\zeta) = (0,E)$ | the coefficient shifts the vertex of the light cone; the kernel carries the phase weight $\exp(-i(E,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, a drift of the wave vector, not a curvature |
| imaginary, $\vec F = -iH$ | the plane $(\vec\zeta,H) = 0$ with the disc $\|\vec\zeta\| < \|H\|$ removed | real frequencies exist only off the disc; the weight is $\exp(-(H,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, an exponential growth or decay along $H$ |
| complex, $\vec F = -E - iH$ | the plane through $\vec\zeta^* = E$ perpendicular to $H$, with the disc $\|\vec\zeta - E\| < \|H\|$ removed | both effects at once, on a cone translated by $E$ |

The separation of the two parts of the coefficient is the point of the exercise: its **real part** shifts the wave vector and appears as the phase of the fundamental solution, while its **imaginary part** makes the amplitude grow or decay off the surface, so a complex coefficient describes a driven or dissipative medium. When $\|\vec\zeta - E\| \leq \|H\|$ the potentials become standing waves with exponentially growing or decaying amplitude, and the elementary solutions of that regime are catalogued in the article that holds the programme's solution classes. Separating a harmonic time dependence, $B = B(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\exp(-i\theta_{\mathrm{mat}})$, replaces the mutual bigradients by $\omega+\vec\nabla_\Phi$ and $\omega-\vec\nabla_\Phi$ and gives the stationary surface

Throughout, $\theta_{\mathrm{mat}}:=\omega_n\tau$ is the Matsubara angle: $\omega_n=2\pi n/\mathcal{B}$ is real, so the thermal factor $\exp(-i\theta_{\mathrm{mat}})$ is a phase of modulus one even though it lives on the Euclidean circle. It carries the periodicity and no decay.

$$
S^{\omega} = \left\{\vec\zeta : (\vec\zeta + i\vec F, \vec\zeta + i\vec F) = \omega^2\right\},
$$

with the same complex-bilinear pairing: the circle of radius $\sqrt{\omega^2 + \|A\|^2}$ centred at $B$ in the plane through $B$ perpendicular to $A$, where $\vec F = A + iB$ — a sphere of radius $|\omega|$ centred at $B$ when $A = 0$. Both characteristic surfaces are written here in the coefficient $\vec F$ itself, so they hold whatever identification it is given with the physical vectors. Letting $\omega \to 0$ gives the static solutions, and the elementary stationary potential is the plane wave of wave vector $P_{\mathrm{pw}} = H + \vec u_E\sqrt{\omega^2 + \|E\|^2}$ with $\vec u_E \perp E$, whose invariants are recorded in that catalogue.

**The stationary kernel and its Helmholtz provenance.** The stationary problem has a fundamental solution of its own, and its kernel is Helmholtz rather than d'Alembert, because a weight strips the directional term. For constant $\vec F$ the compensated operator satisfies the exact identity

$$
\left(\Delta_\Phi + 2(\vec F,\vec\nabla_\Phi) + \omega^2 + (\vec F,\vec F)\right)\left(\exp(-(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))\xi_{\mathrm{scl}}\right)
= \exp(-(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))\left(\Delta_\Phi + \omega^2\right)\xi_{\mathrm{scl}} ,
$$

and it holds for the **upper** sign alone: checked on random complex coefficients and random smooth amplitudes, the residual is $1.6\times10^{-6}$ at a finite-difference step of $3\times10^{-4}$ for the upper sign and $O(50)$ for the lower. The directional term is therefore not obstinate — it is removed by the weight — and the complex amplitude of the stationary solution solves the ordinary Helmholtz equation. The kernel is the Helmholtz Green function times that weight,

$$
\tilde{Ξ}_{\omega}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = -\,\frac{\exp(-(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))}{4\pi\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|}\left(a\,\exp(i\omega\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|) + (1-a)\,\exp(-i\omega\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|)\right),
\qquad a \in \mathbb{C},
$$

the outgoing and incoming spherical waves dressed by the exponential weight, and the theorem's form is $B = \bigl(\omega+\vec\nabla_\Phi - \vec F\bigr)(\tilde{Ξ}_{\omega} * G) + T_\omega$ with $T_\omega$ a solution of the homogeneous stationary equation. Two caveats go with the kernel before it is copied. The source prints $\tilde{Ξ}_{\omega}$ with the sign its own Helmholtz formula $\xi = -\frac{1}{4\pi\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|}(a\exp(i\omega\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|) + (1-a)\exp(-i\omega\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|))$ does **not** carry, so the printed kernel is the negative of the one its own $(\Delta_\Phi + \omega^2)\xi = \delta$ gives; and the source fixes $\vec F = -E - iH$ in section 4.2 and $\vec F = E + iH$ in section 4.3, so the letters $E$ and $H$ swap roles between the two, one carrying the phase and the other the exponential. Both the kernel and the surfaces above are written in $\vec F$ itself for that reason, and the mirror between the printed exponent and the printed Fourier denominator is the same one *The Biquaternion D'Alembertian and Its Green's Functions* records for the series' later paper.

## Open Questions

1. **A one-line biquaternion form.** The abelian parent compresses its four equations into $\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi}$. Is there a representative of the non-abelian curvature, or a modified product, for which the Yang–Mills equation is a single adjoint-covariant biquaternion identity, or is the index-mixing obstruction of this article fatal to that program? The obstruction found here is sharp enough to state and not resolved.

2. **Which compact algebra, and how many factors.** The algebra used here is the $\mathrm{SU}(2)$ factor of the material sector, with the abelian factor $\mathbb{R}(ie_t)$ beside it. Whether larger algebras are available, and whether the framework selects one, is the gap recorded by the non-abelian parent and untouched here.

3. **The reality class of the connection.** The non-abelian parent shows that no single Hermitian-conjugation eigenspace accommodates the connection across all four components, with the obstruction sitting in the time direction because $\partial/\partial R_t = -i\partial/\partial r'_t$. The field equation and its conservation law are statements about the algebra and do not depend on resolving that, but the physical identification of $\mathcal{A}_{\imath}$ does.

4. **The matter representation.** The covariant derivative here acts by left multiplication, and the current is defined from the curvature alone. For coupled matter the representation carried by the matter field must be specified, and it is not fixed here; the chiral-fermion and minimal-coupling articles pose that question.

5. **Fixing the representative.** The framework cannot fix the representative, and the Yang–Mills equation supplies no selection principle. The non-abelian case adds the Gribov question of whether an orbit meets a fixing surface more than once; nothing here addresses it.

6. **Topological terms.** The Bianchi identity and the invariant density are the ingredients of $\int\mathrm{Tr}(F\wedge F)$ and of instanton solutions. The self-dual truncation of the field equation is treated elsewhere; its relation to the biquaternion packaging is open.

7. **Empirical contact.** As everywhere in the framework, whether any of this yields a prediction distinguishing it from standard Yang–Mills theory is untouched. The construction is a reformulation.

8. **The matrix form called Yang–Mills-like.** Alexeyeva's vector-coefficient biwave equation is reported to belong to the class of Yang–Mills equations once written in matrix (tensor) form. Whether that form carries any of the structure this article's $D_{\imath}$ carries — a connection, a covariant conservation law, covariance — or only the shape of a linear first-order system with a constant coefficient, is not settled by the source and is left open here. It is the one question on which the two routes might be made to meet.

## Summary

The action of the non-abelian connection is $S_{\mathrm{YM}}=\int d^4r\,\mathcal{L}$ with $\mathcal{L}=-\tfrac12\mathrm{Tr}(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath})$, the matrix trace on the $\mathrm{SU}(2)$ factor. The trace is the matrix trace and not the informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, which is not cyclic; with the reduction in place of the trace the action would be moved by a local transformation and the theory would not be a connection theory. The invariance is one line, $\mathrm{Tr}(F_{\mathrm g}F_{\mathrm g})=\mathrm{Tr}(\tilde QF\tilde Q^{-1}\tilde QF\tilde Q^{-1})=\mathrm{Tr}(FF)$, and it uses the adjoint law of the field strength and the cyclicity of the trace and nothing else. At dimension four the square of the curvature is the only invariant: a cubic term vanishes by the trace of an odd number of generators, and a derivative term has dimension five.

The variation is $\delta S_{\mathrm{YM}}=2\int d^4r\,\mathrm{Tr}(\sum_{\jmath}\delta\mathcal{A}_{\jmath}\,D_{\imath}F_{\imath\jmath})$, from $\delta F_{\imath\jmath}=D_{\imath}\delta\mathcal{A}_{\jmath}-D_{\jmath}\delta\mathcal{A}_{\imath}$, the antisymmetry of $F$, the cyclicity of the trace and an integration by parts. The derivative that the integration by parts moves onto $F$ is covariant, not ordinary, because the field is adjoint-valued. Stationarity is $\sum_{\imath}D_{\imath}F_{\imath\jmath}=0$, the source-free equation, with the contraction between the derivative index and the curvature's first index. The commutator makes $F$ quadratic in $\mathcal{A}$, so the density carries cubic and quartic terms, which are the self-coupling; the coupling sits in the commutator against a derivative term that carries none, so its ratio is physical and the coupling runs. The time component of the equation is a first-class constraint, the non-linear Gauss law, which leaves two polarizations per generator; the current of the global symmetry is bilinear in the connection and covariantly conserved, with a non-vanishing ordinary divergence; and the energy–momentum is symmetric and traceless classically, its trace anomaly being the beta function. The ceiling at $\mathrm{U}(1)\oplus\mathrm{SU}(2)$ is a property of the algebra that carries the connection and not of the density, which is form-invariant.

The Yang–Mills equation in biquaternionic form is the covariant divergence equation

$$
\sum_{\imath} D_{\imath} F_{\imath\jmath} = J_{\jmath},
\qquad
\tilde D\tilde F = \tilde\nabla_\Phi\tilde F + i\kappa\,[\mathcal{A},\tilde F],
\qquad
J_{\jmath} \in \mathrm{SU}(2),
$$

with $D_{\imath} = \partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath}$ and $F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath} + i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$. Two things change from the abelian case, and both come from the single fact that the covariant derivative is not the ordinary one.

- The field equation acquires the commutator term $i\kappa[\mathcal{A}_{\imath},F_{\imath\jmath}]$, with the derivative index contracted with the first index of the curvature and with the connection of the same index inside the commutator. This is the only placement that makes the equation covariant and the current conserved; the three alternatives tested fail at order unity.
- The current is **covariantly** conserved, $\sum_{\jmath} D_{\jmath} J_{\jmath} = 0$, not ordinarily conserved: $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = -i\kappa[\mathcal{A}_{\jmath},J_{\jmath}] \neq 0$. The conservation follows from the field equation and the antisymmetry of the curvature, through $\tfrac12\sum_{\imath,\jmath}[D_{\jmath},D_{\imath}]F_{\imath\jmath} = \tfrac12 i\kappa\sum_{\imath,\jmath}[F_{\jmath\imath},F_{\imath\jmath}] = 0$; the differential Bianchi identity is the independent homogeneous half and is not what makes it true.

In the abelian limit — a commuting generator set, whether the centre $\mathbb{B}_{C}$ of the parent or a single fixed generator — every commutator vanishes: $[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}] = 0$ removes the curvature's commutator term, $[\mathcal{A}_{\imath},F_{\imath\jmath}] = 0$ removes the field equation's, and $[\mathcal{A}_{\jmath},J_{\jmath}] = 0$ removes the one separating covariant from ordinary conservation. The equation reduces to Maxwell's, $\sum_{\imath}\partial/\partial R_{\imath} F_{\imath\jmath} = J_{\jmath}$, with an ordinarily conserved current that is invariant under the abelian local transformations preserving the generator set. Nothing cancels; the abelian connection commutes with everything it meets.

The biquaternionic packaging is exact for the current, $\mathcal{J} = \sum_{\jmath} J_{\jmath} e_{\jmath}$ with $\sum_{\jmath} \bigl(D_{\imath} F_{\imath\jmath}\bigr) e_{\jmath} = \mathcal{J}$ and $J_{2,\jmath} = \tilde UJ_{\jmath} \tilde U^{-1}$, and limited for the curvature: the representative $\mathcal{F} = \tfrac12\sum_{\imath\jmath}F_{\imath\jmath}\bar{e}_{\imath} e_{\jmath}$ inherits the componentwise adjoint law, not a single conjugation, and the naive one-line product picks up an index-mixing term of order unity. That limitation is stated, not papered over.

A second, independent route to a biquaternion equation with a Yang–Mills-type matrix form is recorded from the literature: the biwave equation $\vec\nabla_{+} B + F\circ B = G$ — and the same with $\vec\nabla_{-}$ — with a constant vector structural coefficient, whose homogeneous solutions are the programme's unit-norm plane waves and whose second-order operator carries a mass $(\vec F,\vec F)$ and a directional term. It is linear, with a fixed coefficient, and therefore carries no connection and no covariant conservation law. The corpus keeps the two routes apart by name and records the matrix-form claim as a class statement, not an equivalence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_{\imath}^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; abelian group factor |
| $\tilde\nabla_\Phi = e_t\partial/\partial R_t + \sum_{\imath}\,\vec e_{\imath}\partial/\partial R_{\imath}$ | Biquaternionic gradient; $\partial/\partial R_t = -i\partial/\partial r'_t$ |
| $(\tilde\nabla_\Phi)^{\natural} = e_t\partial/\partial R_t - \sum_{\imath}\,\vec e_{\imath}\partial/\partial R_{\imath}$ | Quaternion-conjugate gradient |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$ | d'Alembertian |
| $[e_a,e_b] = 2\varepsilon_{abc}e_c$ | Commutator on the vector part of $\mathbb{B}_{\Phi}$ |
| $\mathrm{SU}(2) = \mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | Compact algebra inside $\mathbb{B}_{\Phi}$ |
| $T_a = \tfrac12 e_a$, $2\,\mathrm{Sc}(T_aT_b) = -\tfrac12\delta_{ab}$ | Normalized generators; matrix trace |
| $\tilde U(\tilde{Q}) \in SU(2)$ | Unit real quaternion, $\tilde U^{-1} = \bar{\tilde U} = \tilde U^\dagger$ |
| $\mathcal{A}_{\imath} = \sum_a\mathcal{A}_{\imath a} e_a \in \mathrm{SU}(2)$, $\mathcal{A} = \sum_{\imath}\mathcal{A}_{\imath} e_{\imath}$ | Non-abelian connection |
| $\kappa =\frac{2\pi ϙ}{h}$ | Coupling |
| $D_{\imath} = \partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath}$, $D = \tilde\nabla_\Phi + i\kappa\mathcal{A}$ | Covariant derivative (left multiplication on matter) |
| $\mathcal{A}_{2,\imath} = \tilde U\mathcal{A}_{\imath} \tilde U^{-1} + \frac{i}{\kappa}(\partial/\partial R_{\imath} \tilde U)\tilde U^{-1}$ | Adjoint local transformation of the connection |
| $F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath} + i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$ | Non-abelian curvature |
| $F_{2,\imath\jmath} = \tilde UF_{\imath\jmath}\tilde U^{-1}$ | Adjoint transformation of the curvature (not invariant) |
| $[D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath}$ | Curvature as commutator of covariant derivatives |
| $D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa[\mathcal{A}_{\imath},\tilde{Q}]$ | Adjoint covariant derivative; $[D_{\imath},\tilde{Q}] = D_{\imath} \tilde{Q}$ |
| $D_{\imath} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0$ | Bianchi identity (homogeneous half) |
| $\tilde J_{\Phi} = \tilde D\tilde F = \tilde\nabla_\Phi\tilde F + i\kappa[\mathcal{A},\tilde F]$ | Yang–Mills current (source) |
| $\sum_{\imath} D_{\imath} F_{\imath\jmath} = J_{\jmath}$ | Yang–Mills equation |
| $\sum_{\jmath} D_{\jmath} J_{\jmath} = 0$ | Covariant conservation of the current |
| $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = -i\kappa[\mathcal{A},\tilde J_{\Phi}]$ | Failure of ordinary conservation |
| $J_{2,\jmath} = \tilde UJ_{\jmath} \tilde U^{-1}$ | Adjoint transformation of the source |
| $\mathcal{J} = \sum_{\jmath} J_{\jmath} e_{\jmath}$ | Source biquaternion |
| $\sum_{\jmath} \bigl(D_{\imath} F_{\imath\jmath}\bigr) e_{\jmath} = \mathcal{J}$ | Biquaternionic form of the field equation |
| $\mathcal{F} = \tfrac12\sum_{\imath\jmath}F_{\imath\jmath}\bar{e}_{\imath} e_{\jmath}$ | Curvature biquaternion (componentwise adjoint law) |
| $-\tfrac12\mathrm{Tr}(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath})$ | Invariant Yang–Mills density (matrix trace) |
| $S_{\mathrm{YM}}=\int d^4r\,\mathcal{L}$ | Yang–Mills action |
| $\delta F_{\imath\jmath}=D_{\imath}\delta\mathcal{A}_{\jmath}-D_{\jmath}\delta\mathcal{A}_{\imath}$ | Variation of the curvature; a covariant derivative of the variation |
| $\delta S_{\mathrm{YM}}=2\int d^4r\,\mathrm{Tr}(\sum_{\jmath}\delta\mathcal{A}_{\jmath}D_{\imath}F_{\imath\jmath})$ | Variation of the action; stationarity is the field equation |
| $\sum_{j}D_{j}F_{j0}=0$ | Non-abelian Gauss law; first-class constraint |
| $j_{a,\imath}=\sum_{b,c}\varepsilon_{abc}F_{b,\imath\jmath}\mathcal{A}_{c,\jmath}$ | Noether current of the global $\mathrm{SU}(2)$ (component setting, real coupling) |
| $T_{\imath\jmath}=\mathrm{Tr}(\sum_{k}F_{\imath k}F_{\jmath k})-\tfrac14\delta_{\imath\jmath}\mathrm{Tr}(\sum_{a,b}F_{ab}F_{ab})$ | Energy–momentum of the connection; traceless classically |
| $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Inherited plain trace reading (distinct from the matrix trace) |
| $Z\,\tilde{J}_{\Phi}$, with $\tilde J_{\Phi}=ic\rho\,e_t+\vec J$ | Parent's abelian source; plays the role of $-\mathcal{J}$ up to the parent's normalisation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\vec F = -E - iH$ | Constant complex-vector structural coefficient of the biwave equation (Alexeyeva); $E, H$ real vectors |
| $\vec\nabla_{+} = \partial/\partial \tau + i\vec\nabla_\Phi$, $\vec\nabla_{-} = \partial/\partial \tau - i\vec\nabla_\Phi$, $\Box_A = \partial^2/\partial \tau^2 - \Delta_\Phi$ | The source's mutual bigradients and wave operator, in her letters and without the corpus sector mark; $\Box_A$ is minus this article's $\Box_\Phi$ |
| $\tilde{Ξ}$, $P_{\mathrm{pw}}$ | Fundamental solution of the biwave equation; wave vector of its elementary stationary solution |
| $\omega+\vec\nabla_\Phi$, $\omega-\vec\nabla_\Phi$ | The two bigradients of the time-harmonic reduction, written out |
| $\tilde{Ξ}_{\omega}$, $\xi$ | Stationary fundamental solution (Helmholtz kernel times the weight $\exp(-(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$); the source's Helmholtz Green function |
| $T_\omega$ | Solution of the homogeneous stationary equation |

## Further Reading

- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html) — the three requirements on a density, cyclicity as the whole of the invariance, and the coefficients $\tfrac12$ and $\tfrac14$ that the normalisation forces.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) — the ceiling: why the density is form-invariant while the carrier is not.
- [Non-Abelian Connections in Biquaternionic Form](non-abelian-connections-in-biquaternionic-form.html) — the immediate parent; the $\mathrm{SU}(2)$ factor, the curvature with its commutator, the adjoint transformation, and the source-free equation $\sum_{\imath} D_{\imath} F_{\imath\jmath} = 0$ that this article sources.
- [The Covariant Derivative and Connection in Biquaternionic Form](the-covariant-derivative-and-connection-in-biquaternionic-form.html) — the abelian connection and covariant derivative, the curvature as a commutator that closes on the algebra, and the gap this article and its non-abelian companion take up.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the abelian field equation $\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi}$, the source biquaternion, and the conservation law whose non-abelian generalisation is the subject here.
- [The Minimal coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html) — the origin of the connection and the transformation law, and the preview of the non-abelian curvature used here.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the abelian invariants and the biquaternion norm, whose non-abelian extension remains open.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the covariant derivative on the spinor module and the matter representation that the current of this article does not fix.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) — the left/right matter-representation question and the coupled Dirac equation.
- [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html) — the framework's inability to fix the representative, which bounds the non-abelian orbit.
- [Instantons and Solitons in Biquaternionic Form](instantons-and-solitons-in-biquaternionic-form.html) — the self-dual truncation $\sum_{\imath} D_{\imath} F_{\imath\jmath} = 0$ and the topological charge built from the Bianchi identity.
- [Lie Algebras: A General Introduction](../articles_maths/lie-algebras-a-general-introduction.html) — the Jacobi identity, the adjoint action as a derivation, and the commutator bracket on an associative algebra.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) and [Quaternion Algebra](../articles_maths/quaternion-algebra.html) — the multiplication rule, the conjugations and the centre used throughout.
- [Four-Vectors and the Interval](four-vectors-and-the-interval.html) — the sector basis and the imaginary-scalar/real-vector structure on which the $\mathrm{SU}(2)$ group factor rests.
- [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) — the Hermitian sector and the pairing formula distinguished here from the matrix trace.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html) — the two-sided gravitational connection, distinct from the one-sided connection of this article.
- V. V. Kassandrov, "Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time", *Gravitation & Cosmology* **1** (1995) 216, arXiv:gr-qc/0007027, for the external claim recorded in *A neighbouring claim: the triplet from the electromagnetic potential*: the scalar-free part $N_{a0}=A_a$, $N_{ab}=\delta_{ab}A_0-i\sum_c\varepsilon_{abc}A_c$ of the biquaternion connection fixed linearly by the electromagnetic potential, its self-dual strength obeying the Yang–Mills equation as a Bianchi consequence, and the determinant relation by which the electromagnetic field strength is the modulus of the triplet. Cited as the programme's claim, not adopted.
