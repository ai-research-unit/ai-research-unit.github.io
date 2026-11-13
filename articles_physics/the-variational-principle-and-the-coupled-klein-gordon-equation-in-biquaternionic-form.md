# __The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Form__

## Introduction

This article writes the action of the coupled Klein–Gordon theory and reads what its variations deliver. It is the variational companion of *The Coupled Klein–Gordon Equation in Biquaternionic Form*, and it continues *The Variational Principle and the Klein–Gordon Equation in Biquaternionic Form*, whose free action, conjugation checks and pairing it inherits without change. The vector and spinor members of the series are the two coupled Proca articles and the two coupled Dirac articles.

**The action.**

$$
S\bigl[\tilde\Xi,\tilde\Xi^{*},\tilde A_\Phi\bigr]
=\int\mathrm{d}^{4}x\;\Bigl\{
\mathrm{Sc}\sum_\mu\Bigl[\bigl(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\Bigr]
-k_m^{2}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]
+\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde F\tilde F\bigr]
\Bigr\},
$$

with $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{iϙ}{\hbar}A_\mu$, $\tilde F=\mathrm{Vect}\big((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\big)$, and the sum over the four slots carrying the metric signs of the corpus's convention. The first two terms are the matter action; the third is the Maxwell article's field term. The coupling is not a separate term: it is inside the covariant derivative, and that placement is the article's first structural point.

**Four results.**

*First, one action has three variations and two equations.* Varying $\tilde\Xi^{*}$ gives the coupled Klein–Gordon equation; varying $\tilde A_\Phi$ gives the inhomogeneous Maxwell equation with the matter current as its source; the variation with respect to $\tilde\Xi$ gives the conjugate of the first. The two equations are one system because they are one action's, and the article states the identification of the source as a derivation rather than a definition.

*Second, the consistency of the two equations is the current's conservation, and it is automatic.* The Maxwell equation's scalar part must vanish, because the left side is the divergence of a pure vector; that vanishing is the continuity equation, and the matter equation supplies it. So the two variations cannot contradict each other, and the reason is the same one that makes the coupling possible at all.

*Third, the current lies entirely inside the algebra.* The free Klein–Gordon article's current is a bilinear of the field with its own Hermitian conjugate, and the coupling does not change its character: $\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi$ is one element times one element, and the current is its scalar part made real. There is no adjoint row, no $\gamma$-matrix insertion, and no bilinear that has to be repaired. This is the sharpest structural difference between the scalar case and the spinor case, where the variational article had to keep the naive bilinear and the polar article had to read it with a frame.

*Fourth, the field term is unproblematic, unlike the vector case.* The Maxwell term $\tfrac12\mathrm{Re\,Sc}(\tilde F\tilde F)$ is invariant under the central phase because the *connection* is real: the field strength is a pure vector with real coefficients on the material sector, and the phase never reaches it. The coupled Proca article records the opposite situation, where the potential is complex and the field strength is half of a complex bivector, and where the invariant pairing's normalisation is open. Here nothing is open about the field term, and the reason is that the scalar's charge is carried by the field and not by the connection.

**What is not claimed.** No new solution, no new prediction. The action is the standard scalar-electrodynamics action; the algebra's contribution is that the coupling is one derivative, that the current and the source are one object, and that the two equations' consistency is one line.

## The Action

**The matter term.** The free companion's action is the sum over the four slots of $\mathrm{Sc}\big[(\partial_\mu\tilde\Xi)^{*}\partial_\mu\tilde\Xi\big]$ with the metric signs of the display, minus the mass term. Covariantising the four slots gives

$$
S_{\mathrm{m}}=\int\mathrm{d}^{4}x\;\Bigl\{\sum_\mu\mathrm{Sc}\Bigl[\bigl(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\Bigr]-k_m^{2}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\Bigr\},
$$

and the only difference from the free action is the substitution of the derivative. Nothing was added to the action and nothing was rearranged: the interaction is the difference between the covariant and the ordinary kinetic terms, and it is bilinear in the field and linear in the connection.

**The kinetic term is real and non-negative, term by term.** For any element $Y=\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi$,

$$
\mathrm{Sc}\bigl(Y^{*}Y\bigr)=\sum_{\lambda}\lvert Y_\lambda\rvert^{2}\ge0 ,
$$

exactly, because $Y^{*}Y=\mathrm{nat}(\bar Y)Y$ has scalar part $\sum_\lambda\lvert Y_\lambda\rvert^{2}$. So each slot's contribution is real and non-negative and the sum is real and non-negative; the action's reality needs no antisymmetrisation and no boundary term. This is where the second-order scalar case is simpler than the first-order cases: the Schrödinger and Dirac actions are first order and their reality is bought by antisymmetrising $\tilde\Xi^{*}\partial\tilde\Xi$.

**The mass term is real.** $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=\sum_\lambda\lvert\Xi_\lambda\rvert^{2}$, the same computation with no derivative, so the mass term is real and positive for a nonzero field. The free companion's remark that the mass term's sign is fixed by the dispersion relation applies unchanged.

**The field term.** $\tfrac12\mathrm{Re\,Sc}(\tilde F\tilde F)$ is the Maxwell article's density; for a material field strength it is $\tfrac12(\epsilon\vec E^{2}-\vec B^{2}/\mu)$ and it is real. Its invariance under the central phase is trivial here: $\tilde F$ is built from the connection alone, the connection is real, and the phase is the field's. The article states this explicitly because the coupled Proca article's field term is not in this position, and the contrast is the difference between a charge carried by the field and a charge carried by the potential.

**The pairing.** The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout, the free companion's choice, and the reason is the free companion's: $\mathrm{Sc}(A^{\natural}A)=\sum_\mu a_\mu^{2}$ for complex coefficients is not real and does not give a real action, so the quaternionic pairing is unavailable. The polar companion uses the same pairing.

## The Variation in the Field

**The Euler–Lagrange equation.** Vary $\tilde\Xi$ and $\tilde\Xi^{*}$ independently, which is legitimate over the complex carrier and is the standard device for a complex field, and integrate by parts once per slot. The result is

$$
\Bigl(\Box_{\mathrm{gco}}-k_m^{2}\Bigr)\tilde\Xi=0,
\qquad
\Box_{\mathrm{gco}}=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2},
$$

which is the coupled equation of the element companion, with the overall sign fixed by the action's convention as in the free companion.

**Why the variation produces the squared operator.** The kinetic term is $\mathrm{Sc}\big[(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi)^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\big]$, and varying $\tilde\Xi$ acts on the second factor: $\delta\bigl(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr)=\tilde\nabla_{\mathrm{gco},\mu}\delta\tilde\Xi$, because the connection is held fixed and the variation commutes with a derivative whose coefficients are fixed functions. So

$$
\delta S_{\mathrm{m}}=2\,\mathrm{Re}\,\mathrm{Sc}\sum_\mu\Bigl[\bigl(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\mu}\delta\tilde\Xi\Bigr]+\text{(the conjugate variation)},
$$

and integrating by parts moves the derivative onto the first factor. The boundary term vanishes for a variation of compact support, and the operator that comes out squares one and the same covariant derivative, because the connection is central and the same in the two slots; the sign is the free companion's and no new sign has to be chosen.

**The two factors of a slot, and one exact bookkeeping point.** Write $c_\mu=\frac{iϙ}{\hbar}A_\mu$. The kinetic term carries $c_\mu$ in both factors of a slot, and the variation pairs them as $(\partial_\mu-\bar c_\mu)(\partial_\mu+c_\mu)$. That product is the square $\tilde\nabla_{\mathrm{gco},\mu}^{2}$ exactly when $\bar c_\mu=-c_\mu$, that is, when the slot's coefficient is purely imaginary. In the corpus's material convention $A_\eta$ is real, so the three spatial coefficients are purely imaginary and the three spatial slots pair into squares; and $A_t=i a'_t$ is imaginary, so the temporal coefficient is real and its slot pairs into $\partial_{R_t}^{2}-(ϙ a'_t/\hbar)^{2}$ rather than into $(\partial_{R_t}-ϙ a'_t/\hbar)^{2}$. For a constant potential the two differ by $-\frac{2ϙ a'_t}{\hbar}\partial_{R_t}+\frac{2ϙ^{2}a_t'^{2}}{\hbar^{2}}$: the first piece is the cross term through which the electric potential shifts the energy, the second the potential's square.

The article states the equation as $\Box_{\mathrm{gco}}\tilde\Xi=k_m^{2}\tilde\Xi$ and not as the adjoint-paired form, for three reasons: that is the equation the element companion states, it is the minimal-substitution form whose polar chart is the polar companion's pair, and it is the form whose mass shell carries the mechanical energy $E+ϙ c\,a'_t$. The variation reproduces it exactly for a magnetic connection and in the free limit, and for an electric one it reproduces it up to the cross term named above. The discrepancy is the single place where the corpus's convention for the temporal slot and the standard action's pairing part company, and it is recorded rather than absorbed: §*Open Questions* carries it.

**Why the variation does not produce the algebra's other equation.** The action's kinetic term is the sum over slots of the *squared moduli*, not the modulus of the algebra's gradient. The variation of $\mathrm{Sc}\big[(\tilde\nabla_{\mathrm{gco}}\tilde\Xi)^{*}\tilde\nabla_{\mathrm{gco}}\tilde\Xi\big]$ would produce $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde\Xi$, and the two functionals differ by the cross terms the element companion displays and measures. So the action is the arbiter, and it selects the component equation. The element companion states the same conclusion from the side of the equations; here it is the variation that decides.

**The count.** The equation is four complex equations for four complex coefficients, which is eight real equations for eight real functions. The action is real, so the variations with respect to $\tilde\Xi$ and with respect to $\tilde\Xi^{*}$ are not independent constraints: the pair gives the four complex equations and their four conjugates, and the conjugate set is the same set. The count is the free companion's, unchanged by the coupling.

## The Variation in the Connection

**The source.** Varying $A_\mu$ acts only inside the covariant derivatives, through $\delta\bigl(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr)=\frac{iϙ}{\hbar}\,\delta A_\mu\,\tilde\Xi$, and the connection's coefficient is central, so the variation does not have to choose a side. Hence

$$
\frac{\delta S_{\mathrm{m}}}{\delta A_\mu}
=-\frac{ϙ}{\hbar}\,J_\mu ,
\qquad
J_\mu=2\,\mathrm{Re}\,\mathrm{Sc}\Bigl[i\,\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\Bigr],
$$

with the sign from the two appearances of $A_\mu$ in the squared covariant derivative and the factor from $\partial/\partial A_\mu$ of a square. The object $J_\mu$ is real by construction, because it is twice the real part of a complex number, and it is the same current the element companion defines up to the constant $1/(2k_m)$: the companion's normalisation is chosen to match the free article's density and is a convention, the object is not.

**The connection's equation.** Adding the field term and varying it in the standard way — $\delta\tilde F=\mathrm{Vect}\big((\tilde\nabla_\Phi)^{\natural}\delta\tilde A_\Phi\big)$ and one integration by parts — gives

$$
\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\,\tilde J_\Phi^{\mathrm{(src)}},
\qquad
\tilde J_\Phi^{\mathrm{(src)}}\ \propto\ \frac{ϙ}{\hbar}J ,
$$

which is the Maxwell article's inhomogeneous equation with the matter current as its source. The proportionality is the field term's normalisation, which the Maxwell article fixes once; the sign is fixed by the relative sign of the two terms in the total action and is the sign that makes the source the current rather than minus the current. The article states the structure and the sign and does not re-derive the constant.

**The consistency, and why it is automatic.** The left side of the connection's equation is the divergence of a pure vector in the sense of the covariant-derivative article, and $\Box_\Phi$ is a scalar operator, so the scalar part of $\tilde\nabla_\Phi\tilde F$ vanishes identically. Therefore the source must satisfy

$$
\mathrm{Sc}\Bigl(\bigl(\tilde\nabla_\Phi\bigr)^{\natural}\tilde J_\Phi^{\mathrm{(src)}}\Bigr)=0 ,
$$

which is the free article's covariant form of the continuity equation. The matter equation supplies it: the identity

$$
\partial_\mu J_\mu=-2\,\mathrm{Im}\,\mathrm{Sc}\Bigl[\tilde\Xi^{*}\bigl(\Box_{\mathrm{gco}}-k_m^{2}\bigr)\tilde\Xi\Bigr]
$$

holds for the current as defined in this section, the companion's $J$ being this one divided by $2k_m$ and therefore carrying the same constant after the rescaling; the divergence vanishes on every solution, and the vanishing is the same statement as the scalar part of the connection's equation being zero. So the two variations of one action are mutually consistent, and the consistency is not a condition imposed on the system: it is the current's conservation, which is the matter equation read once more.

**What this establishes.** A coupling between a field and a connection exists exactly when the field has a conserved current, because the connection's equation must be integrable. For the scalar, the current is the phase symmetry's, the symmetry exists because the centre of the algebra is a $\mathrm{U}(1)$, and the coupling is the localization of that symmetry. The chain is the gauge principle article's, and the coupled Klein–Gordon variational article supplies the one computation the chain needs at second order.

## Gauge Invariance of the Total Action and What It Buys

**The matter term is invariant, exactly.** Under $\tilde\Xi\mapsto e^{iϙ\Lambda/\hbar}\tilde\Xi$ and $A_\mu\mapsto A_\mu-\partial_\mu\Lambda$ the covariant derivative is covariant — the computation is the element companion's and it is exact for a general element — so each slot's squared modulus is invariant and the mass term is invariant. The invariance is not up to a divergence; it is an identity.

**The field term is invariant, exactly.** $\tilde F$ is unchanged because the gauge transformation of the connection is a gradient and the field strength is the antisymmetrised gradient; the Maxwell article's argument applies verbatim.

**The interaction is not a separate term, and this is what the placement buys.** In the standard presentation the coupling is written as a term $A_\mu J^\mu$ added to the free action, and its gauge invariance has to be checked by integrating by parts and using the current's conservation. Here the coupling is inside the derivative, so the invariance is automatic and the current's conservation appears instead as the *consistency* of the connection's equation. The two presentations are the same theory, and the difference is which statement is a computation: the derivative placement makes the invariance manifest and the conservation derived, the term placement makes the conservation manifest and the invariance derived.

**What the invariance forces.** Nothing beyond the transformation laws, and that is the content of the second Noether theorem in this setting: the gauge symmetry is a symmetry of the action for every function $\Lambda$, so the variation of the action with respect to $\Lambda$ vanishes identically, and the identity that results is the current's conservation read off shell. The article does not need the theorem's general form; it needs the one line, and the one line is the previous section's consistency argument.

## The Noether Currents

**The phase symmetry: the charge.** The transformation $\tilde\Xi\mapsto e^{i\alpha}\tilde\Xi$, $\tilde\Xi^{*}\mapsto e^{-i\alpha}\tilde\Xi^{*}$ with $\alpha$ a constant real number leaves the Lagrangian invariant identically, because the central $i$ commutes with everything. The Noether current is

$$
J^{\mathrm{N}}_\mu=2\,\mathrm{Re}\,\mathrm{Sc}\Bigl[i\,\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\Bigr],
$$

which is the object of the previous section, and its conservation is the identity displayed there. The article records the coincidence as its third structural point: the current that the phase symmetry supplies and the current that the connection's equation needs are the same current, and they are the same because both are the derivative of the action with respect to the same object.

**The charge is gauge invariant.** Every derivative in $J^{\mathrm{N}}_\mu$ is covariant and the field's phase factor cancels between the two terms, so the current is unchanged by a gauge transformation. The free current is not — a shift of the phase by a function changes $\rho$ and $\vec j$ by gradient terms — and the coupling repairs it. What the coupling does not repair is the sign: on the negative-frequency branch the temporal component is negative, exactly as in the free article, because the sign is the sign of the energy and the connection does not enter the branch structure.

**The energy–momentum.** Under a translation $x_\mu\mapsto x_\mu+\epsilon_\mu$ with the connection held fixed, the matter action is invariant only when the connection is constant, because a varying connection is a set of functions and the Lagrangian depends on them. For a constant connection the Noether current is

$$
T_{\mu\nu}=\mathrm{Sc}\Bigl[\bigl(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\nu}\tilde\Xi
+\bigl(\tilde\nabla_{\mathrm{gco},\nu}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\Bigr]-\eta_{\mu\nu}\mathcal L ,
$$

which is real and symmetric in the index pair by construction: the two terms are each other's complex conjugates, and there is no antisymmetric piece to remove. This is a genuine difference from the free Proca case, where the symmetrisation had to be imposed.

**The matter tensor alone is not conserved when the connection varies.** For a varying connection the Lagrangian depends on the coordinates through $A_\mu$, so the translation is not a symmetry of the matter action, and the failure of conservation is the Lorentz force density,

$$
\partial_\mu T_{\mu\nu}=F_{\nu\mu}J_\mu ,
$$

up to the current's normalisation, with $F_{\nu\mu}=\partial_\nu A_\mu-\partial_\mu A_\nu$: the rate at which the field does work on the matter. The total tensor, matter plus field, is conserved, and that is the statement that the coupled system has no external source. The article states the matter identity and the total conservation and does not compute the field's tensor, which is the Maxwell article's.

**What the stress tensor does not need.** No improvement term for symmetry, because the tensor is already symmetric; no improvement term for the trace, because the trace of the matter tensor is the mass term and the mass term is what the trace is expected to be; and no gauge repair, because the tensor is built from covariant derivatives. The free companion's stress discussion carries over with the substitution of the derivative and one new identity, the Lorentz force.

## What the Principle Adds and What It Does Not

**Adds.**

- One action, three variations, two equations: the matter equation, the connection's equation and their consistency.
- The identification of the current as both the phase symmetry's charge and the connection's source, in one computation.
- The reality of the kinetic term as a one-line statement, $\mathrm{Sc}(Y^{*}Y)=\sum\lvert Y_\lambda\rvert^{2}$, with no antisymmetrisation to arrange.
- The action's arbitration between the two coupled equations: the component equation is the one the variation produces.
- The Lorentz force as the divergence of the matter tensor, which is the exact statement of what the coupling costs in energy–momentum.

**Does not add.**

- No new prediction. The action is the standard scalar-electrodynamics action.
- No new solution. The solutions are the standard charged scalar's.
- No repair of the density's sign, and no statement that the coupling changes the branch structure.
- No statement about the operator setting's renormalisation, which is the quantised scalar article's subject.

**The honest ledger.** The action is the standard one, written in the algebra, and the couplings are the standard ones. What the algebra contributes is the placement — one derivative, one element, no separate term — and the consequences of the placement: the invariance is manifest, the conservation is the consistency, the current is the source, and nothing in the current needs an adjoint.

## Open Questions

**The normalisation of the coupling to the field.** The constant relating $\frac{ϙ}{\hbar}J$ to the Maxwell source is the field term's normalisation, which the Maxwell article fixes on the material slice. Here the question is closed in principle — the connection is real and the field term is the free one — but the constant has not been recomputed in the coupled setting, and the article records it as carried over rather than derived.

**The fourfold multiplicity.** The action couples four coefficients to one connection with one charge, which is the fourfold structure of the free theory continued. Whether a variational principle can distinguish the four — by giving them different charges, or by adding a term that couples them to each other — and whether the framework would want to, is not answered by the standard action and is not answered here.

**The operator setting.** The action is classical and the connection is external. Whether the quantised version's current requires the normal ordering that the free quantised scalar article discusses, and whether the four copies' identical charge survives renormalisation as one charge or as four, is the quantisation's question and is not attempted.

**The temporal slot's pairing.** §*The Variation in the Field* records that the action's pairing of the two factors in the temporal slot is $\partial_{R_t}^{2}-(ϙa'_t/\hbar)^{2}$ while the article's equation carries $(\partial_{R_t}-ϙa'_t/\hbar)^{2}$, the two differing by the cross term through which the electric potential shifts the energy. The difference is a property of the corpus's convention $A_t=i a'_t$: the temporal coefficient of the covariant derivative is real, while the standard scalar action's minimal coupling pairs an imaginary one. Whether the convention should be read as the four-potential's time component being imaginary throughout — in which case the temporal slot's cross term belongs to the energy and not to the derivative — or whether the action for an electric connection should be written with the adjoint pairing in that slot, is not settled here. The magnetic case, the free limit, and the polar pair are unaffected; what is at stake is one bookkeeping choice, stated rather than absorbed.

## Summary

The action of the coupled scalar theory is

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\sum_\mu\bigl[(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi)^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr]-k_m^{2}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]+\tfrac12\mathrm{Re\,Sc}\bigl[\tilde F\tilde F\bigr]\Bigr\},
$$

with the coupling inside the derivative and not as a separate term. Varying the field gives $\bigl(\Box_{\mathrm{gco}}-k_m^{2}\bigr)\tilde\Xi=0$ — exactly for a magnetic connection and in the free limit, and up to the temporal slot's cross term for an electric one, the bookkeeping of §*The Variation in the Field* and one of the article's open questions — varying the connection gives $\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\tilde J_\Phi^{\mathrm{(src)}}$ with the matter current as the source; and the two are consistent because the matter current is conserved,

$$
\partial_\mu J_\mu=-2\,\mathrm{Im}\,\mathrm{Sc}\Bigl[\tilde\Xi^{*}\bigl(\Box_{\mathrm{gco}}-k_m^{2}\bigr)\tilde\Xi\Bigr]=0
\quad\text{on solutions},
$$

with $J_\mu=2\mathrm{Re\,Sc}\bigl[i\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr]$. The same object is the phase symmetry's Noether charge, the connection's source and the current whose conservation makes the connection's equation integrable. The current is gauge invariant and lies entirely inside the algebra, with no adjoint row and no bilinear to repair; the density's sign is not repaired and is the carrier's. The energy–momentum tensor is real and symmetric with no improvement term, and its divergence for a varying connection is the Lorentz force density.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}$, $\mathbb{B}_\Psi$, $\mathbb{B}_\Phi$ | The algebra and its two sectors |
| $\mathrm{Sc}$, $\mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part; trace |
| $^{*}$, $^{\natural}$ | Hermitian and quaternion conjugation |
| $\tilde\Xi$ | The field, a general element of $\mathbb{B}$ |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection, real on the material sector |
| $ϙ$ | The coupling |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{iϙ}{\hbar}A_\mu$ | The covariant derivative, central per slot |
| $\Box_{\mathrm{gco}}=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}$ | The covariant d'Alembertian |
| $\tilde F=\mathrm{Vect}\big((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\big)$ | The field strength |
| $S_{\mathrm{m}}$, $\mathcal L$ | The matter action; its density |
| $J_\mu=2\mathrm{Re\,Sc}\bigl[i\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\bigr]$ | The charge current; the Noether charge; the source |
| $\tilde J_\Phi^{\mathrm{(src)}}$ | The source of the connection's equation |
| $T_{\mu\nu}$ | The matter stress tensor; $\partial_\mu T_{\mu\nu}=F_{\nu\mu}J_\mu$ |
| $k_m=mc/\hbar$ | The mass wave number |

## Further Reading

- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the equation, the two writings and the current.
- [The Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the same theory in the chart.
- [The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the action in the chart.
- [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Form](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-form.html), for the free action and the conjugation checks.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator, the curvature and the second Noether theorem.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the field term and the inhomogeneous equation.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-form.html), for the contrast where the potential is complex and the field term's normalisation is open.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the contrast where the current needs an adjoint row.
- [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the operator reading of $T_{\mu\nu}$.
- [The Quantized Scalar Field in Biquaternionic Form](the-quantized-scalar-field-in-biquaternionic-form.html), for the field-theoretic reading of the four copies.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for scalar electrodynamics and its Ward identity.
- Emmy Noether, "Invariante Variationsprobleme", *Nachrichten der Königlichen Gesellschaft der Wissenschaften zu Göttingen* (1918), for the two theorems.
