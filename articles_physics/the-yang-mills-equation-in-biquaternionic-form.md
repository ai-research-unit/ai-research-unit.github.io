# __The Yang–Mills Equation in Biquaternionic Form__

## Introduction

*Maxwell's Equations in the Biquaternionic Formulation* compresses the four Maxwell equations into a single biquaternion equation, $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, in which a biquaternionic field strength is sourced by a biquaternionic current. *Non-Abelian Gauge Fields in Biquaternionic Form* then lets the connection of the same framework take values in the compact factor $\mathrm{SU}(2) = \mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ of the material sector, obtains the non-abelian curvature

$$
F_{\mu\nu} = \partial/\partial Q_\mu \mathcal{A}_\nu - \partial/\partial Q_\nu \mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu],
\qquad [D_\mu,D_\nu] = i\kappa F_{\mu\nu},
$$

and records, in its discussion of the Yang–Mills action, that the source-free field equation is $D_\mu F^{\mu\nu} = 0$ "in place of the abelian $\partial/\partial Q_\mu F^{\mu\nu} = 0$". It does not develop that equation: the sourced equation, the current that appears on its right-hand side, and the conservation law that current obeys are all left open. This article takes them up.

The Yang–Mills equation is the non-abelian generalisation of the Maxwell source equation,

$$
D_\mu F^{\mu\nu} = J^\nu,
\qquad
\tilde D\tilde F = \tilde\nabla\tilde F + i\kappa\,[\mathcal{A}, \tilde F],
$$

with the covariant derivative $D_\mu = \partial/\partial Q_\mu + i\kappa\mathcal{A}_\mu$ acting on the curvature through the commutator, in the adjoint action of the gauge algebra. The subject of this article is what changes from the abelian case, and the answer is a short list.

- **The field equation itself acquires a term.** In the abelian case the connection coefficients commute (in the parent's $\mathrm{U}(1)$ case they are central), so $[\mathcal{A}_\mu,F^{\mu\nu}] = 0$ and the field equation is the ordinary divergence. In the non-abelian case the commutator term is present and cannot be dropped: the covariant derivative is not the ordinary one, and the source of a non-abelian gauge field is itself charged.
- **The current is covariantly conserved, not ordinarily conserved.** Taking the covariant divergence of the field equation gives $D_\mu J^\mu = 0$. This is *not* $\langle\tilde\nabla,\tilde J\rangle_{\natural} = 0$: the ordinary divergence of the current is $-i\kappa[\mathcal{A}_\mu,J^\mu]$, which is nonzero for a generic non-abelian field. Writing ordinary conservation here would be a defect, not a simplification.
- **The terms that vanish in the abelian limit do so because the abelian connection commutes.** Every commutator that distinguishes the non-abelian equation from Maxwell contains either $[\mathcal{A}_\mu,\mathcal{A}_\nu]$ or $[\mathcal{A}_\mu,\,\cdot\,]$; all of them vanish when the connection coefficients commute, and none of them cancels against a nonvanishing partner.

The division between what is established and what is interpretation is kept explicit.

- **Established, and recomputed below.** The curvature identity $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$; the Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$; the Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ with the commutator term $i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$; the covariant conservation $D_\mu J^\mu = 0$ and the failure of ordinary conservation; the reduction to Maxwell on a commuting generator set; and the adjoint transformation $J'_\nu = \tilde U J_\nu \tilde U^{-1}$ of the source. Each was recomputed on a generic, non-constant $\mathrm{SU}(2)$-valued connection — all three generators, non-commuting — at four generic points, by exact polynomial arithmetic; no claim below rests on the abelian case.
- **Interpretation.** Reading $D_\mu F^{\mu\nu}$ as the conserved current of a non-abelian gauge field, and the field equation as the Euler–Lagrange equation of $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$, is the standard interpretation of the algebra, placed in the framework's notation. It is labelled as interpretation where it occurs.
- **Gaps and defects, left visible.** The biquaternion packaging of the curvature that the parent articles use, $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$, does not inherit the adjoint transformation as a single algebra conjugation, and the naive product $\nabla\!\cdot\!(\sum_\nu F^{\mu\nu}e_\nu)$ is not the covariant divergence of the field equation; both are stated precisely and neither is smoothed over. The framework's inability to fix the gauge is inherited unchanged and bounds the whole construction; no gauge is chosen anywhere below.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\mu^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $\vec e_\mu$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ is the complex scalar subspace, which is the centre of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$. On the material sector, $\mathbb{M}_- = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$ with $\mathrm{SU}(2) = \mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, $[e_a,e_b] = 2\varepsilon_{abc}e_c$, and normalized generators $T_a = \tfrac12 e_a$ with $[T_a,T_b] = \varepsilon_{abc}T_c$ and $\mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}$. The gauge group is $SU(2)$, the unit real quaternions, $\tilde U^{-1} = \bar{\tilde U} = \tilde U^\dagger$. The connection and field strength of the non-abelian sector are $\mathcal{A}_\mu = \mathcal{A}_\mu^a e_a \in \mathrm{SU}(2)$ with $\mathcal{A} = \sum_\mu\mathcal{A}_\mu e_\mu$, and $F_{\mu\nu} = \partial/\partial Q_\mu\,\mathcal{A}_\nu - \partial/\partial Q_\nu\,\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, with $\kappa = ϙ/\hbar$ the coupling. The covariant derivative is $D_\mu = \partial/\partial Q_\mu + i\kappa\mathcal{A}_\mu$, $D = \tilde{\nabla} + i\kappa\mathcal{A}$, acting on a matter field by left multiplication. Indices run $\mu,\nu,\lambda \in \{t,x,y,z\}$ with $\partial/\partial Q_t = -i\partial/\partial t$; in the $ict$ convention $\partial/\partial Q_\mu = \partial/\partial x_\mu$ raises and lowers no index, so the coordinate sum $\sum_\mu$ is the Lorentz-invariant contraction and we may write $F^{\mu\nu}$ and $F_{\mu\nu}$ interchangeably. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is inherited unchanged; where the Yang–Mills density is written, the trace is the **matrix trace** on the $\mathrm{SU}(2)$ factor, which is a different operation. No gauge is fixed.

## The Non-Abelian Curvature and the Adjoint Covariant Derivative

The constructions of this article are those of its two parents, and they are recalled here only far enough to fix the conventions the field equation uses.

The connection is an $\mathrm{SU}(2)$-valued one-form, $\mathcal{A}_\mu$, and the covariant derivative is $D_\mu = \partial/\partial Q_\mu + i\kappa\mathcal{A}_\mu$, with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$. Under a local gauge transformation $\tilde U(\tilde{Q})\in SU(2)$ the connection and field strength transform in the adjoint representation,

$$
\mathcal{A}'_\mu = \tilde U\mathcal{A}_\mu \tilde U^{-1} + \frac{i}{\kappa}(\partial/\partial Q_\mu \tilde U)\tilde U^{-1},
\qquad
F'_{\mu\nu} = \tilde U F_{\mu\nu} \tilde U^{-1},
$$

and $F_{\mu\nu}$ is *not* gauge invariant: it is an algebra element rotated by the group. The covariance of the first-order operator is what forces the inhomogeneous term in the first law.

Two derived objects carry the rest of the article. The first is the **adjoint covariant derivative**, the action of the gauge connection on an algebra-valued field $\tilde{Q}$:

$$
D_\lambda \tilde{Q} = \partial/\partial Q_\lambda \tilde{Q} + i\kappa\,[\mathcal{A}_\lambda, \tilde{Q}].
$$

It is the unique first-order operator whose action on $\tilde{Q}$ is the commutator of the covariant derivative operator with multiplication by $\tilde{Q}$. Recomputing that commutator directly,

$$
[D_\lambda, \tilde{Q}]\Psi = D_\lambda(\tilde{Q}\Psi) - \tilde{Q}(D_\lambda\Psi)
= (\partial/\partial Q_\lambda \tilde{Q} + i\kappa[\mathcal{A}_\lambda,\tilde{Q}])\Psi,
$$

for every $\Psi$, so that as operators

$$
[D_\lambda, \tilde{Q}] = D_\lambda \tilde{Q},
$$

with $\tilde{Q}$ read as multiplication by the algebra element. (The notation table and the Bianchi discussion of *Non-Abelian Gauge Fields in Biquaternionic Form* print $[D_\lambda,\tilde{Q}] = i\kappa D_\lambda \tilde{Q}$; that line is not consistent with the definition $D_\lambda \tilde{Q} = \partial/\partial Q_\lambda \tilde{Q} + i\kappa[\mathcal{A}_\lambda,\tilde{Q}]$ given in the same article, and the factor $i\kappa$ is an evident slip — the operator commutator is first order in $\partial/\partial Q_\lambda$ and equal to multiplication by $D_\lambda \tilde{Q}$. The Bianchi identity itself is unaffected, because the substitution that produces it is the same either way once the identity is corrected. The recomputed identity $[D_\lambda,\tilde{Q}] = D_\lambda \tilde{Q}$ is the one used here, and it was checked numerically — see the companion.) The second is the **Bianchi identity**,

$$
D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0,
$$

where each $D$ is the adjoint covariant derivative. It is the statement that the exterior derivative of the curvature is a cycle, and it is automatic for a curvature built from a connection: it follows from the Jacobi identity for the operators $D_\mu$, $[D_\lambda,[D_\mu,D_\nu]] + \text{cyclic} = 0$, together with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$; equally, at the level of components, from the derivation property of the adjoint action.

The biquaternion packaging of the curvature, inherited from the parents, is the definition

$$
\mathcal{F} = \tfrac12\sum_{\mu,\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu \;\in\; \mathbb{B},
\qquad \bar{e}_t = e_t,\; \bar{e}_\mu = -\vec e_\mu .
$$

It collects the six independent curvature components against the quaternion-basis products $\bar{e}_\mu e_\nu$. What this object does and does not inherit under a gauge transformation is treated in its own section below; the reader should not assume that the componentwise transformation law $F_{\mu\nu}\mapsto \tilde UF_{\mu\nu}\tilde U^{-1}$ promotes to a single conjugation of $\mathcal{F}$.

## The Yang–Mills Equation

Let the current be the covariant divergence of the curvature,

$$
\tilde J := \tilde D\tilde F = \tilde\nabla\tilde F + i\kappa\,[\mathcal{A}, \tilde F], \qquad \tilde J \in \mathrm{SU}(2),
$$

summed over $\mu$. This is the definition of the source in this article; the equation

$$
\boxed{\,D_\mu F^{\mu\nu} = J^\nu\,}
$$

is the Yang–Mills equation, and the two terms of its expansion are the whole of its content.

- **The ordinary divergence $\partial/\partial Q_\mu F^{\mu\nu}$.** In the abelian limit this term alone is Maxwell's source equation. In the non-abelian case it is not gauge covariant on its own.
- **The commutator term $i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$.** The index $\mu$ of the connection is contracted with the *derivative* index of $F^{\mu\nu}$ — the first index — and the commutator is taken with that same $\mathcal{A}_\mu$. This is the only placement that makes the equation gauge covariant and the current covariantly conserved; it is the term most often got wrong. In the abelian case $\mathcal{A}_\mu$ commutes with the curvature (it is central in the parent's $\mathrm{U}(1)$ case, and lies on a single generator otherwise), so the term vanishes.

The two slots of the index structure are fixed. The derivative that acts is the one whose index is contracted, and it must be the same index that labels the connection inside the commutator; and the curvature is contracted in its first index by that derivative. Writing $[\mathcal{A}_\nu,F^{\mu\nu}]$ (connection index equal to the free index), or $[\mathcal{A}_\mu,F^{\nu\mu}]$ (curvature contracted in its second index), or reversing the sign of the commutator term, each destroys the conservation law derived in the next section. This was checked directly on a generic non-commuting connection: the correct placement gives $D_\nu(D_\mu F^{\mu\nu}) = 0$ to $3\times10^{-15}$, while the three alternatives and the ordinary divergence give residuals of order $10$ — order unity on the same field. The reader who is unsure of a sign convention should repeat that one computation rather than consult memory.

**Gauge covariance.** The equation is covariant without any gauge being chosen. With $F'_{\mu\nu} = \tilde UF_{\mu\nu}\tilde U^{-1}$ and the transformation of the connection, the covariant derivative satisfies $D'_\mu(\tilde U\Psi) = \tilde U D_\mu\Psi$, so the current transforms in the adjoint,

$$
J'^\nu = \tilde U J^\nu \tilde U^{-1},
$$

and $D'_\mu F'^{\mu\nu} = \tilde U(D_\mu F^{\mu\nu})\tilde U^{-1}$. The equation $D_\mu F^{\mu\nu} = J^\nu$ therefore holds in one gauge if and only if it holds in every gauge; no condition such as $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\mathcal{A}) = 0$, and no other gauge-fixing surface, is imposed or available. This point is worth stating because the framework's canonical-quantisation article records that it *cannot* fix the gauge; the Yang–Mills equation inherits that situation rather than relieving it. The adjoint transformation of the source was verified numerically on a generic connection with a generic (constant) group rotation; the covariance for a general local $\tilde U$ follows from the transformation laws above and was not separately rechecked.

**Biquaternionic form.** Pack the four components of the current into a biquaternion in the quaternion basis,

$$
\mathcal{J} = \sum_{\nu\in\{t,x,y,z\}} J_\nu e_\nu \;\in\; \mathbb{B}.
$$

Then the Yang–Mills equation is the single biquaternion equation

$$
\sum_{\nu\in\{t,x,y,z\}} \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J},
\qquad\text{equivalently}\qquad
\sum_{\nu\in\{t,x,y,z\}} \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \sum_{\nu\in\{t,x,y,z\}} J_\nu\, e_\nu ,
$$

in which the covariant derivative acts on the $\mathrm{SU}(2)$-valued curvature components by the adjoint action $D_\mu F_{\mu\nu} = \partial/\partial Q_\mu F_{\mu\nu} + i\kappa[\mathcal{A}_\mu,F_{\mu\nu}]$, and the sum over $\mu$ is the divergence. The left-hand side is the covariant divergence of the curvature, expanded in the quaternion basis; the right-hand side is the source biquaternion. This is the direct non-abelian analogue of the parent's $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$: the parent's source $\sqrt{\mu}\,\tilde{J}$, with $\tilde J$ the four-current, plays the role of $-\mathcal{J}$ up to the parent's normalisation of $\tilde{F}$ (the parent uses $R_0 = i\rho/\sqrt{\epsilon}$, $\vec R = \sqrt{\mu}\,\vec J$, and writes its equation with the opposite sign). The sign of the source is a convention, fixed here by defining $J^\nu$ through the field equation; what is not a convention is that the derivative on the left is covariant.

**The biquaternion packaging does not collapse.** It is tempting to write the left-hand side as $\sum_\mu D_\mu F^\mu$ with $F^\mu := \sum_\nu F^{\mu\nu}e_\nu$, and to advertise a one-line product. That is not correct, and the failure is instructive. Because the adjoint commutator does not pass through the quaternion basis,

$$
D_\mu\bigl(F_{\mu\nu}e_\nu\bigr) = \bigl(D_\mu F_{\mu\nu}\bigr)e_\nu + i\kappa\,F_{\mu\nu}\,[\mathcal{A}_\mu,e_\nu],
$$

the extra term $i\kappa\sum_{\mu\nu}F_{\mu\nu}[\mathcal{A}_\mu,e_\nu]$ is present whenever $\mathcal{A}_\mu$ fails to commute with the basis elements. It does not vanish for a generic non-abelian connection, and it was verified to be of order unity. The biquaternionic field equation is therefore the basis-expanded contraction written above, not a single adjoint-covariant product of a packaged curvature. This is the same lesson the parent article records about $\mathrm{Vect}(\tilde{\nabla}^{\natural}\mathcal{A})$: the quaternion packaging of a non-abelian curvature is a bookkeeping device, and products of packaged objects hide index mixing that must be checked.

## Covariant Conservation of the Current

The source defined by the field equation is not free. Applying the adjoint covariant derivative to the field equation and using the antisymmetry of the curvature,

$$
D_\nu J^\nu = D_\nu D_\mu F^{\mu\nu}
= \tfrac12\{D_\nu,D_\mu\}F^{\mu\nu} + \tfrac12[D_\nu,D_\mu]F^{\mu\nu}.
$$

The two pieces are handled separately.

- **The symmetric piece vanishes by antisymmetry.** The anticommutator $\{D_\nu,D_\mu\}$ is symmetric in $\mu\nu$, while $F^{\mu\nu}$ is antisymmetric; contracting the two gives zero. Explicitly, relabelling $\mu\leftrightarrow\nu$ in one half of the sum turns $\{D_\nu,D_\mu\}F^{\mu\nu}$ into its own negative.
- **The antisymmetric piece vanishes by antisymmetry and the curvature identity.** Since $[D_\nu,D_\mu] = i\kappa F_{\nu\mu}$ acts on $F^{\mu\nu}$ by commutation,
$$
\tfrac12[D_\nu,D_\mu]F^{\mu\nu} = \tfrac12 i\kappa\,[F_{\nu\mu},F^{\mu\nu}],
$$
and the summed commutator vanishes: relabelling $\mu\leftrightarrow\nu$ and using $F_{\nu\mu} = -F_{\mu\nu}$ shows the sum equals its own negative.

Hence

$$
\boxed{\,D_\nu J^\nu = 0\,}
$$

the current is **covariantly conserved**. Expanding the definition, this is

$$
\langle\tilde\nabla,\tilde J\rangle_{\natural} + i\kappa\,[\mathcal{A}, \tilde J] = 0,
\qquad\text{that is}\qquad
\langle\tilde\nabla,\tilde J\rangle_{\natural} = -\,i\kappa\,[\mathcal{A}, \tilde J].
$$

The ordinary divergence does not vanish. For a generic non-abelian connection it is of order unity, and only the covariant divergence is zero; the difference is exactly the commutator of the connection with the current. This was recomputed on a generic non-commuting connection: $D_\nu J^\nu$ vanishes to $3\times10^{-15}$ while $\langle\tilde\nabla,\tilde J\rangle_{\natural}$ has magnitude $\approx 7$. Writing $\langle\tilde\nabla,\tilde J\rangle_{\natural} = 0$ for the non-abelian current is false, and would drop the term that carries the adjoint action.

**What the conservation uses, and what it does not.** It is often said that the current is conserved "by the Bianchi identity". In this derivation the differential Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$ is *not* used. What is used is the field equation, the antisymmetry of $F_{\mu\nu}$, and the curvature identity $[D_\nu,D_\mu] = i\kappa F_{\nu\mu}$; the vanishing commutator $[F_{\nu\mu},F^{\mu\nu}] = 0$ is an algebraic consequence of antisymmetry, not the differential identity. (That algebraic identity is itself sometimes called a Bianchi identity, being the contracted statement that the curvature is an algebra element; the differential identity is a different object, and it is the differential one that is not needed here.) The differential Bianchi identity is the independent *homogeneous* half of the non-abelian system, treated in its own section below. The two are sometimes conflated because both are identities of the curvature and both trace back to the Jacobi identity at the level of operators; the reader is entitled to know which one does the work. The claim to be verified for the conservation is therefore field equation plus antisymmetry, and that is what was checked.

**Consistency, not an extra condition.** In the abelian case the analogous statement $\partial/\partial Q_\nu\,\partial/\partial Q_\mu F^{\mu\nu} = 0$ is automatic, and charge conservation is recovered from the field equation rather than imposed. In the non-abelian case the same logic gives the covariant law; the current defined by the field equation is covariantly conserved automatically, and no independent condition on $\rho$ and $\vec J$ is added. In this sense $D_\nu J^\nu = 0$ is the integrability condition of the Yang–Mills system, exactly as ordinary conservation is the integrability condition of Maxwell's system.

## The Abelian Limit

The abelian case is the case of a **commuting generator set**: the connection takes values in a one-dimensional subalgebra, so that all its coefficients commute. Two settings realise it in the framework. The parent's abelian connection lies in the centre $\mathbb{C}_{\mathbb{B}}$, whose imaginary scalar $ie_t$ commutes with every biquaternion; and any connection proportional to a single fixed generator, $\mathcal{A}_\mu = a_\mu(\tilde{Q})\,\vec e_x$, has commuting coefficients even though $\vec e_x$ is not central. The reduction to Maxwell is the same in both, and it is worth saying exactly which terms vanish and why.

Write $\mathcal{A}_\mu = a_\mu\,g$ for a fixed generator $g$ with $a_\mu$ scalar functions (for the centre, $g = ie_t$; for a single spatial generator, $g = \vec e_x$). Then

$$
[\mathcal{A}_\mu,\mathcal{A}_\nu] = a_\mu a_\nu\,[g,g] = 0,
$$

so the curvature loses its commutator,

$$
F_{\mu\nu} = \partial/\partial Q_\mu\,\mathcal{A}_\nu - \partial/\partial Q_\nu\,\mathcal{A}_\mu = (\partial/\partial Q_\mu a_\nu - \partial/\partial Q_\nu a_\mu)\,g,
$$

and the Yang–Mills equation loses its own commutator term for the same reason:

$$
[\mathcal{A}_\mu,F^{\mu\nu}] = a_\mu\,(\partial^\mu a^\nu - \partial^\nu a^\mu)\,[g,g] = 0 .
$$

The field equation is therefore

$$
\tilde D\tilde F = \tilde\nabla\tilde F = \tilde J,
$$

which is Maxwell's source equation, and the current is now a commuting biquaternion, invariant under the abelian gauge transformations that preserve the generator set. Correspondingly the conservation law degenerates,

$$
\langle\tilde\nabla,\tilde J\rangle_{\natural} + i\kappa\,[\mathcal{A},\tilde J] = \langle\tilde\nabla,\tilde J\rangle_{\natural} = 0,
$$

because $[\mathcal{A}_\nu,J^\nu] = a_\nu[g,g]J^\nu = 0$; the current is **ordinarily** conserved, and it is invariant under the abelian gauge transformations that preserve the commuting generator set, $J'^\nu = \tilde U J^\nu \tilde U^{-1} = J^\nu$ (in the centre case every central $\tilde U$ qualifies, since $\tilde U$ is central; on a single spatial generator, the qualifying $\tilde U$ are those of the abelian subgroup generated by $g$).

Nothing here cancels. Every non-abelian term vanishes because the abelian connection commutes — with itself, with the curvature it generates, and with the current — not because two nonzero contributions are arranged to cancel. This is the precise sense in which the abelian case is the degenerate one, and it is why agreement on a commuting generator set is a consistency check on normalisation and signs but *not* evidence for the non-abelian statement: every non-abelian identity above was checked on the full non-commuting $\mathrm{SU}(2)$ connection, where the commutators are nonzero, and the abelian reduction was checked separately.

## The Bianchi Identity and the Homogeneous Half

The Yang–Mills equation is half of the non-abelian system. The other half is the Bianchi identity,

$$
D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0,
\qquad\text{equivalently}\qquad
D_\mu {\star}F^{\mu\nu} = 0,
$$

where ${\star}F$ is the dual field strength. Unlike Maxwell's source equation, this identity is not an equation of motion: it is a consequence of building $F$ from $\mathcal{A}$, and it holds for every connection. It is the non-abelian analogue of "the homogeneous Maxwell equations are identities once the field strength is a curl". The index-mixing term displayed earlier is the kind of contribution that the naive one-line product leaves behind; the Bianchi identity is the statement that the corresponding antisymmetrised combination of covariant derivatives of $F$ vanishes, and it is the homogeneous half of the system.

The relation between the two halves is worth stating without overclaim. The field equation determines $J^\nu$ and implies its covariant conservation; the Bianchi identity constrains the curvature independently of the source and is what the dual equation $D_\mu{\star}F^{\mu\nu} = 0$ expresses. Neither implies the other: the conservation of the current is not the Bianchi identity, and the source-free Yang–Mills equation $D_\mu F^{\mu\nu} = 0$ is not the Bianchi identity either — a distinction the gauge-principle companion records explicitly for the abelian one-line equation $\tilde{\nabla}\tilde{F} = 0$, and which survives verbatim here.

## What the Biquaternion Packaging Does and Does Not Give

The framework's compact form of the abelian equations, $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, is a genuine one-line equation. For the non-abelian system the analogous packaging is more delicate, and this article records the limits of what the packaging delivers rather than presenting a formula that would not survive a recheck.

The curvature biquaternion is defined, as in the parent, by $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$. Its *components* transform in the adjoint, $F'_{\mu\nu} = \tilde UF_{\mu\nu}\tilde U^{-1}$, so $\mathcal{F}$ inherits the componentwise adjoint law

$$
\mathcal{F}' = \tfrac12\sum_{\mu\nu}\bigl(\tilde UF_{\mu\nu}\tilde U^{-1}\bigr)\bar{e}_\mu e_\nu .
$$

This is **not** the single algebra conjugation $\tilde U\mathcal{F}\tilde U^{-1}$, because $\tilde U^{-1}$ does not pass through the basis product $\bar{e}_\mu e_\nu$. The two agree only when the group element $\tilde U$ commutes with the basis product $\bar{e}_\mu e_\nu$, i.e. in the centre case. This was verified: with a generic constant unitary $\tilde U$, $\mathcal{F}' = \tfrac12\sum(\tilde UF_{\mu\nu}\tilde U^{-1})\bar{e}_\mu e_\nu$ holds to machine precision, while $\mathcal{F}' = \tilde U\mathcal{F}\tilde U^{-1}$ fails by order unity. The componentwise law is what makes the current transform as $J'_\nu = \tilde UJ_\nu \tilde U^{-1}$ and what keeps the field equation covariant; the packaged law is simply not available.

Two consequences follow, and both are stated as findings rather than repairs.

- **The source biquaternion $\mathcal{J} = \sum_\nu J_\nu e_\nu$ is a valid packaging.** Its components transform in the adjoint, and the equation $\sum_\nu \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J}$ is exact and covariant. This is the biquaternionic form of the Yang–Mills equation used here.
- **A single adjoint-covariant product of the curvature is not that equation.** As shown in the previous section, $\sum_\mu D_\mu(\sum_\nu F^{\mu\nu}e_\nu)$ differs from $\sum_{\mu,\nu} \bigl(D_\mu F^{\mu\nu}\bigr) e_\nu$ by the index-mixing term $i\kappa\sum_{\mu\nu}F_{\mu\nu}[\mathcal{A}_\mu,e_\nu]$, which is nonzero for a generic connection. Whether some other representative of the non-abelian curvature makes the field equation a one-line product, in the way the pure-vector Riemann–Silberstein representative does in the abelian case, is not settled here.

**A neighbouring claim: the triplet from the electromagnetic potential.** One external programme makes a stronger statement than anything above, and it is worth separating because it reverses the direction of dependence between the abelian and non-abelian fields. In Kassandrov's algebrodynamics (recorded in *The Algebrodynamical Programme*) the biquaternion connection is split into a trace part and a trace-free part, $\Gamma_\nu=\tfrac12A_\nu I+N_\nu$, and the trace-free part is prescribed **linearly** by the same complex four-vector that serves as the electromagnetic potential,

$$
N^a_{\ 0}=A_a, \qquad N^a_{\ b}=\delta_{ab}A_0-i\varepsilon_{abc}A_c .
$$

Its strength $L_{\mu\nu}=\partial_{[\mu}N_{\nu]}-[N_\mu,N_\nu]$ is self-dual on the solutions of the programme's primary equation, and the Bianchi identity then gives the Yang–Mills equation $\partial/\partial Q_\nu L^{\mu\nu}=[N_\nu,L^{\mu\nu}]$. The abelian–non-abelian link is a determinant: the curvature splits into a trace part proportional to the electromagnetic field strength $F^{\mathrm{em}}_{\mu\nu}=\partial/\partial Q_\mu A_\nu-\partial/\partial Q_\nu A_\mu$ and the trace-free $L_{\mu\nu}$, and $\det R_{\mu\nu}=0$ — which holds because the non-trivial spinor lies in its kernel — makes the electromagnetic field strength the **modulus of the triplet**, $\sum_a(L^a_{\ \mu\nu})^2\propto(F^{\mathrm{em}}_{\mu\nu})^2$ (the constant is convention-dependent and is not reconciled; the superscript marks the abelian quantity, to be read apart from this article's $F_{\mu\nu}$). Here the Yang–Mills field has **no independent existence**, being a function of the electromagnetic potential, which is a different relation between the two fields from any construction in this article. It is a claim of that programme, conditional on its nonlinear primary equation, recorded there and not adopted here.

## A Biwave Equation with a Vector Structural Coefficient

There is a second biquaternion equation in the literature whose matrix form has been called Yang–Mills-like, and it is worth separating from the construction above. In a four-part series on the differential algebra of biquaternions, L. A. Alexeyeva studies the wave equation

$$
\nabla^\pm B + F \circ B = G(\tau, x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
\qquad
\nabla^\pm = \partial_\tau \pm i\,\nabla ,
$$

where $\tau$ is time in units of length, $\circ$ the biquaternion product, $G$ a given biquaternionic source, and $F = f + \vec F$ a **constant** biquaternion — the *structural coefficient* — with scalar part $f$ and vector part $\vec F$ [Alexeyeva 2014]. The four papers are a sequence of specialisations of this one equation: the earlier ones treat the members equivalent to the biquaternionic Maxwell system ($F = 0$) and to the biquaternionic Dirac system ($F = f$, a complex scalar), with their generalisations, and the fourth takes the **vector-valued** coefficient $\vec F \neq 0$. The author's remark for that case is that the equation, written in matrix (tensor) form, belongs to the class of Yang–Mills equations. Recording the series here gives the corpus a single source for the Maxwell–Dirac–Yang–Mills web that the framework's own articles reach by separate routes.

**What the identification is, and what it is not.** The coefficient is constant, so the equation carries no non-constant connection, no commutator curvature and no covariant derivative of the kind $D_\mu$ above. "Belongs to the class of Yang–Mills equations" is a statement about the **matrix form of a linear first-order system with matrix coefficients** — the shape of the equation, not its gauge structure. The two constructions are therefore not competing derivations of one object: this article's equation is non-linear in a field-valued connection and its current is only covariantly conserved, while the biwave equation is linear with a fixed coefficient. That one route reaches a Yang–Mills-type matrix form from a constant coefficient, and the other from a connection, is a genuine difference of route, and the corpus records it as such rather than as an agreement.

**Second-order form and solution.** Composing the two mutual operators for constant $\vec F$ gives the single second-order operator

$$
\left(\nabla^- - \vec F\right)\circ\left(\nabla^+ + \vec F\right)
= \Box_A + (\vec F,\vec F) + 2i(\vec F,\nabla),
\qquad
\Box_A = \partial_\tau^2 - \Delta ,
$$

so each component of $B$ solves a Klein–Gordon–Fock-type equation whose mass is the norm $(\vec F,\vec F)$ of the coefficient, plus one first-order directional term. *The Klein–Gordon Equation in Biquaternionic Form* treats that operator and the sense in which the vector coefficient makes it factor into first-order operators, which is the point of contrast with its scalar-coefficient case. The inhomogeneous equation is solved by convolution with the fundamental solution

$$
\psi(\tau,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{\exp(i(\vec F,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))}{4\pi|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|}\left((1-a)\,\delta(\tau-|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|) + a\,\delta(\tau+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|)\right) + \psi^0(\tau,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
\qquad a \in \mathbb{C},
$$

with $\psi^0$ an arbitrary solution of the homogeneous scalar equation: a superposition of the retarded and advanced $\delta$-layers on the light cone carrying the exponential weight $\exp(i(\vec F,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$, the constant $a$ choosing the branch. The published form of the solution is $B = (\nabla^- - \vec F)(\psi * G) + B^0$, the homogeneous part $B^0$ being built from the same kernel and arbitrary biquaternionic fields. The weight is not decoration: the Fourier denominator is $(\vec\xi + \vec F, \vec\xi + \vec F) - \omega^2$, which is *linear* in the wave vector, and that is why the kernel is a $\delta$-layer on the cone rather than the Bessel-type kernel of the ordinary massive case.

**The characteristic surface, by case.** The homogeneous equation $\nabla^+ B + \vec F\circ B = 0$ has plane-wave solutions supported on

$$
S = \left\{(\omega,\vec\xi) : (\vec\xi + \vec F, \vec\xi + \vec F) = \omega^2\right\},
$$

with $(\cdot,\cdot)$ the complex-bilinear pairing. Writing $\vec F = -E - iH$ with $E, H$ real vectors, the surface degenerates according to which part of the coefficient is present:

| Coefficient | Surface $S$ | Interpretation |
|---|---|---|
| real, $\vec F = -E$ | cone in $\mathbb{R}^4$ with vertex $(\omega,\vec\xi) = (0,E)$ | the coefficient shifts the vertex of the light cone; the kernel carries the phase weight $\exp(-i(E,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$, a drift of the wave vector, not a curvature |
| imaginary, $\vec F = -iH$ | the plane $(\vec\xi,H) = 0$ with the disc $\|\vec\xi\| < \|H\|$ removed | real frequencies exist only off the disc; the weight is $\exp(-(H,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$, an exponential growth or decay along $H$ |
| complex, $\vec F = -E - iH$ | the plane through $\vec\xi^* = E$ perpendicular to $H$, with the disc $\|\vec\xi - E\| < \|H\|$ removed | both effects at once, on a cone translated by $E$ |

The separation of the two parts of the coefficient is the point of the exercise: its **real part** shifts the wave vector and appears as the phase of the fundamental solution, while its **imaginary part** makes the amplitude grow or decay off the surface, so a complex coefficient describes a driven or dissipative medium. When $\|\vec\xi - E\| \leq \|H\|$ the potentials become standing waves with exponentially growing or decaying amplitude, and the elementary solutions of that regime are the ones catalogued in *Twistor Theory and Biquaternions*. Separating a harmonic time dependence, $B = B(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\exp(-i\omega\tau)$, replaces the mutual bigradients by $\nabla^{\pm}_{\omega} = \omega \pm \nabla$ and gives the stationary surface

$$
S^{\omega} = \left\{\vec\xi : (\vec\xi + i\vec F, \vec\xi + i\vec F) = \omega^2\right\},
$$

with the same complex-bilinear pairing: the circle of radius $\sqrt{\omega^2 + \|A\|^2}$ centred at $B$ in the plane through $B$ perpendicular to $A$, where $\vec F = A + iB$ — a sphere of radius $|\omega|$ centred at $B$ when $A = 0$. Both characteristic surfaces are written here in the coefficient $\vec F$ itself, so they hold whatever identification it is given with the physical vectors. Letting $\omega \to 0$ gives the static solutions, and the elementary stationary potential is the plane wave of wave vector $K_F = H + \vec u_E\sqrt{\omega^2 + \|E\|^2}$ with $\vec u_E \perp E$, whose invariants are recorded in the twistor article.

**The stationary kernel and its Helmholtz provenance.** The stationary problem has a fundamental solution of its own, and its kernel is Helmholtz rather than d'Alembert, because a weight strips the directional term. For constant $\vec F$ the compensated operator satisfies the exact identity

$$
\left(\Delta + 2(\vec F,\nabla) + \omega^2 + (\vec F,\vec F)\right)\left(\exp(-(\vec F,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))\varphi\right)
= \exp(-(\vec F,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))\left(\Delta + \omega^2\right)\varphi ,
$$

and it holds for the **upper** sign alone: checked on random complex coefficients and random smooth amplitudes, the residual is $1.6\times10^{-6}$ at a finite-difference step of $3\times10^{-4}$ for the upper sign and $O(50)$ for the lower. The directional term is therefore not obstinate — it is removed by the weight — and the complex amplitude of the stationary solution solves the ordinary Helmholtz equation. The kernel is the Helmholtz Green function times that weight,

$$
\psi_\omega(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = -\,\frac{\exp(-(\vec F,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))}{4\pi\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|}\left(a\,\exp(i\omega\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|) + (1-a)\,\exp(-i\omega\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|)\right),
\qquad a \in \mathbb{C},
$$

the outgoing and incoming spherical waves dressed by the exponential weight, and the theorem's form is $B = (\nabla^{\mp}_{\omega} - \vec F)(\psi_\omega * G) + T_\omega$ with $T_\omega$ a solution of the homogeneous stationary equation. Two caveats go with the kernel before it is copied. The source prints $\psi_\omega$ with the sign its own Helmholtz formula $\chi = -\frac{1}{4\pi\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|}(a\exp(i\omega\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|) + (1-a)\exp(-i\omega\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|))$ does **not** carry, so the printed kernel is the negative of the one its own $(\Delta + \omega^2)\chi = \delta$ gives; and the source fixes $\vec F = -E - iH$ in section 4.2 and $\vec F = E + iH$ in section 4.3, so the letters $E$ and $H$ swap roles between the two, one carrying the phase and the other the exponential. Both the kernel and the surfaces above are written in $\vec F$ itself for that reason, and the mirror between the printed exponent and the printed Fourier denominator is the same one *The Biquaternion D'Alembertian and Its Green's Functions* records for the series' later paper.

## Open Questions

1. **A one-line biquaternion form.** The abelian parent compresses its four equations into $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$. Is there a representative of the non-abelian curvature, or a modified product, for which the Yang–Mills equation is a single adjoint-covariant biquaternion identity, or is the index-mixing obstruction of this article fatal to that program? The obstruction found here is sharp enough to state and not resolved.

2. **Which compact algebra, and how many factors.** The gauge algebra used here is the $\mathrm{SU}(2)$ factor of the material sector, with the abelian factor $\mathbb{R}(ie_t)$ beside it. Whether larger gauge algebras are available, and whether the framework selects one, is the gap recorded by the non-abelian parent and untouched here.

3. **The reality class of the connection.** The non-abelian parent shows that no single Hermitian-conjugation eigenspace accommodates the connection across all four components, with the obstruction sitting in the time direction because $\partial/\partial Q_t = -i\partial/\partial t$. The field equation and its conservation law are statements about the algebra and do not depend on resolving that, but the physical identification of $\mathcal{A}_\mu$ does.

4. **The matter representation.** The covariant derivative here acts by left multiplication, and the current is defined from the curvature alone. For coupled matter the representation carried by the matter field must be specified, and it is not fixed here; the chiral-fermion and minimal-coupling articles pose that question.

5. **Gauge fixing.** The framework cannot fix the gauge, and the Yang–Mills equation supplies no selection principle. The non-abelian case adds the Gribov question of whether a gauge orbit meets a gauge-fixing surface more than once; nothing here addresses it.

6. **Topological terms.** The Bianchi identity and the invariant density are the ingredients of $\int\mathrm{Tr}(F\wedge F)$ and of instanton solutions. The self-dual truncation of the field equation is treated elsewhere; its relation to the biquaternion packaging is open.

7. **Empirical contact.** As everywhere in the framework, whether any of this yields a prediction distinguishing it from standard non-abelian gauge theory is untouched. The construction is a reformulation.

8. **The matrix form called Yang–Mills-like.** Alexeyeva's vector-coefficient biwave equation is reported to belong to the class of Yang–Mills equations once written in matrix (tensor) form. Whether that form carries any of the structure this article's $D_\mu$ carries — a connection, a covariant conservation law, gauge covariance — or only the shape of a linear first-order system with a constant coefficient, is not settled by the source and is left open here. It is the one question on which the two routes might be made to meet.

## Summary

The Yang–Mills equation in biquaternionic form is the covariant divergence equation

$$
D_\mu F^{\mu\nu} = J^\nu,
\qquad
\tilde D\tilde F = \tilde\nabla\tilde F + i\kappa\,[\mathcal{A},\tilde F],
\qquad
J^\nu \in \mathrm{SU}(2),
$$

with $D_\mu = \partial/\partial Q_\mu + i\kappa\mathcal{A}_\mu$ and $F_{\mu\nu} = \partial/\partial Q_\mu\,\mathcal{A}_\nu - \partial/\partial Q_\nu\,\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$. Two things change from the abelian case, and both come from the single fact that the covariant derivative is not the ordinary one.

- The field equation acquires the commutator term $i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$, with the derivative index contracted with the first index of the curvature and with the connection of the same index inside the commutator. This is the only placement that makes the equation covariant and the current conserved; the three alternatives tested fail at order unity.
- The current is **covariantly** conserved, $D_\nu J^\nu = 0$, not ordinarily conserved: $\langle\tilde\nabla,\tilde J\rangle_{\natural} = -i\kappa[\mathcal{A}_\nu,J^\nu] \neq 0$. The conservation follows from the field equation and the antisymmetry of the curvature, through $\tfrac12[D_\nu,D_\mu]F^{\mu\nu} = \tfrac12 i\kappa[F_{\nu\mu},F^{\mu\nu}] = 0$; the differential Bianchi identity is the independent homogeneous half and is not what makes it true.

In the abelian limit — a commuting generator set, whether the centre $\mathbb{C}_{\mathbb{B}}$ of the parent or a single fixed generator — every commutator vanishes: $[\mathcal{A}_\mu,\mathcal{A}_\nu] = 0$ removes the curvature's commutator term, $[\mathcal{A}_\mu,F^{\mu\nu}] = 0$ removes the field equation's, and $[\mathcal{A}_\nu,J^\nu] = 0$ removes the one separating covariant from ordinary conservation. The equation reduces to Maxwell's, $\partial/\partial Q_\mu F^{\mu\nu} = J^\nu$, with an ordinarily conserved current that is invariant under the abelian gauge transformations preserving the generator set. Nothing cancels; the abelian connection commutes with everything it meets.

The biquaternionic packaging is exact for the current, $\mathcal{J} = \sum_\nu J_\nu e_\nu$ with $\sum_\nu \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J}$ and $J'_\nu = \tilde UJ_\nu \tilde U^{-1}$, and limited for the curvature: the representative $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ inherits the componentwise adjoint law, not a single conjugation, and the naive one-line product picks up an index-mixing term of order unity. That limitation is stated, not papered over.

A second, independent route to a biquaternion equation with a Yang–Mills-type matrix form is recorded from the literature: the biwave equation $\nabla^\pm B + F\circ B = G$ with a constant vector structural coefficient, whose homogeneous solutions are the algebraic twistors and whose second-order operator carries a mass $(\vec F,\vec F)$ and a directional term. It is linear, with a fixed coefficient, and therefore carries no connection and no covariant conservation law. The corpus keeps the two routes apart by name and records the matrix-form claim as a class statement, not an equivalence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; abelian gauge factor |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_\mu\partial/\partial Q_\mu$ | Biquaternionic gradient; $\partial/\partial Q_t = -i\partial/\partial t$ |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_\mu\partial/\partial Q_\mu$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$ | d'Alembertian |
| $[e_a,e_b] = 2\varepsilon_{abc}e_c$ | Commutator on the vector part of $\mathbb{M}_-$ |
| $\mathrm{SU}(2) = \mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | Compact gauge algebra inside $\mathbb{M}_-$ |
| $T_a = \tfrac12 e_a$, $\mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}$ | Normalized generators; matrix trace |
| $\tilde U(\tilde{Q}) \in SU(2)$ | Unit real quaternion, $\tilde U^{-1} = \bar{\tilde U} = \tilde U^\dagger$ |
| $\mathcal{A}_\mu = \mathcal{A}_\mu^a e_a \in \mathrm{SU}(2)$, $\mathcal{A} = \sum_\mu\mathcal{A}_\mu e_\mu$ | Non-abelian connection |
| $\kappa = ϙ/\hbar$ | Coupling |
| $D_\mu = \partial/\partial Q_\mu + i\kappa\mathcal{A}_\mu$, $D = \tilde{\nabla} + i\kappa\mathcal{A}$ | Covariant derivative (left multiplication on matter) |
| $\mathcal{A}'_\mu = \tilde U\mathcal{A}_\mu \tilde U^{-1} + \frac{i}{\kappa}(\partial/\partial Q_\mu \tilde U)\tilde U^{-1}$ | Adjoint gauge transformation of the connection |
| $F_{\mu\nu} = \partial/\partial Q_\mu\,\mathcal{A}_\nu - \partial/\partial Q_\nu\,\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian curvature |
| $F'_{\mu\nu} = \tilde UF_{\mu\nu}\tilde U^{-1}$ | Adjoint transformation of the curvature (not invariant) |
| $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$ | Curvature as commutator of covariant derivatives |
| $D_\lambda \tilde{Q} = \partial/\partial Q_\lambda \tilde{Q} + i\kappa[\mathcal{A}_\lambda,\tilde{Q}]$ | Adjoint covariant derivative; $[D_\lambda,\tilde{Q}] = D_\lambda \tilde{Q}$ |
| $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$ | Bianchi identity (homogeneous half) |
| $\tilde J = \tilde D\tilde F = \tilde\nabla\tilde F + i\kappa[\mathcal{A},\tilde F]$ | Yang–Mills current (source) |
| $D_\mu F^{\mu\nu} = J^\nu$ | Yang–Mills equation |
| $D_\nu J^\nu = 0$ | Covariant conservation of the current |
| $\langle\tilde\nabla,\tilde J\rangle_{\natural} = -i\kappa[\mathcal{A},\tilde J]$ | Failure of ordinary conservation |
| $J'_\nu = \tilde UJ_\nu \tilde U^{-1}$ | Adjoint transformation of the source |
| $\mathcal{J} = \sum_\nu J_\nu e_\nu$ | Source biquaternion |
| $\sum_\nu \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J}$ | Biquaternionic form of the field equation |
| $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ | Curvature biquaternion (componentwise adjoint law) |
| $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ | Gauge-invariant Yang–Mills density (matrix trace) |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Inherited informational trace formula (distinct from the matrix trace) |
| $\sqrt{\mu}\,\tilde{J}$, with $\tilde J=ic\rho\,e_t+\vec J$ | Parent's abelian source; plays the role of $-\mathcal{J}$ up to the parent's normalisation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\vec F = -E - iH$ | Constant complex-vector structural coefficient of the biwave equation (Alexeyeva); $E, H$ real vectors |
| $\nabla^\pm = \partial_\tau \pm i\nabla$, $\Box_A = \partial_\tau^2 - \Delta$ | Mutual bigradients and wave operator of the biwave equation; $\Box_A$ is minus this article's $\Box$ |
| $\psi$, $K_F$ | Fundamental solution of the biwave equation; wave vector of its elementary stationary solution |
| $\nabla^\pm_\omega = \omega \pm \nabla$ | Mutual bigradients of the time-harmonic reduction |
| $\psi_\omega$, $\chi$ | Stationary fundamental solution (Helmholtz kernel times the weight $\exp(-(\vec F,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$); the source's Helmholtz Green function |
| $T_\omega$ | Solution of the homogeneous stationary equation |

## Further Reading

- *Non-Abelian Gauge Fields in Biquaternionic Form* — the immediate parent; the $\mathrm{SU}(2)$ factor, the curvature with its commutator, the adjoint transformation, the Bianchi identity, and the source-free equation $D_\mu F^{\mu\nu} = 0$ that this article sources.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the abelian connection and covariant derivative, the curvature as a commutator that closes on the algebra, and the gap this article and its non-abelian companion take up.
- *Maxwell's Equations in the Biquaternionic Formulation* — the abelian field equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, the source biquaternion, and the conservation law whose non-abelian generalisation is the subject here.
- *The Gauge Principle in Biquaternionic Form* — the origin of the connection and the transformation law, and the preview of the non-abelian curvature used here.
- *The Field-Strength Biquaternion and Its Invariants* — the abelian invariants and the biquaternion norm, whose non-abelian extension remains open.
- *Chiral Fermions in the Biquaternion Framework* — the covariant derivative on the spinor module and the matter representation that the current of this article does not fix.
- *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — the left/right matter-representation question and the coupled Dirac equation.
- *Canonical Quantization of the Biquaternion Maxwell Field* — the framework's inability to fix the gauge, which bounds the non-abelian orbit.
- *Instantons and Solitons in Biquaternionic Form* — the self-dual truncation $D_\mu F^{\mu\nu} = 0$ and the topological charge built from the Bianchi identity.
- *Lie Algebras: A General Introduction* — the Jacobi identity, the adjoint action as a derivation, and the commutator bracket on an associative algebra.
- *Conventions in the Biquaternion Universe* and *Quaternion Algebra* — the multiplication rule, the conjugations and the centre used throughout.
- *The Material Sector: Four-Vectors, Interval and Lorentz Action* — the sector basis and the imaginary-scalar/real-vector structure on which the $\mathrm{SU}(2)$ gauge factor rests.
- *The Informational Sector: States, Observables and Probability* — the Hermitian sector and the trace formula distinguished here from the matrix trace.
- *Curved Spacetime and the Biquaternion Framework* — the two-sided gravitational connection, distinct from the one-sided gauge connection of this article.
- L. A. Alexeyeva, "Differential algebra of biquaternions. 4. Twistors and twistor fields," arXiv:1406.5347 [math-ph] (2014), *Mathematical Journal* **13** (2013), for the vector-coefficient biwave equation whose matrix form is identified with the Yang–Mills class, for its non-stationary and stationary fundamental solutions and characteristic surfaces, and for the interpretation of the homogeneous equation as a transformation of charges and currents in an external field — the last recorded in *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*.
- V. V. Kassandrov, "Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time", *Gravitation & Cosmology* **1** (1995) 216, arXiv:gr-qc/0007027, for the external claim recorded in *A neighbouring claim: the triplet from the electromagnetic potential*: the trace-free part $N^a_{\ 0}=A_a$, $N^a_{\ b}=\delta_{ab}A_0-i\varepsilon_{abc}A_c$ of the biquaternion connection fixed linearly by the electromagnetic potential, its self-dual strength obeying the Yang–Mills equation as a Bianchi consequence, and the determinant relation by which the electromagnetic field strength is the modulus of the triplet. Cited as the programme's claim, not adopted.
