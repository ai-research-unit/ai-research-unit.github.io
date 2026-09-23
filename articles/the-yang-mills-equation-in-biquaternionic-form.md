# __The Yang–Mills Equation in Biquaternionic Form__

## Introduction

*Maxwell's Equations in the Biquaternionic Formulation* compresses the four Maxwell equations into a single biquaternion equation, $\tilde{\nabla}\tilde{F} = -\tilde{R}$, in which a biquaternionic field strength is sourced by a biquaternionic current. *Non-Abelian Gauge Fields in Biquaternionic Form* then lets the connection of the same framework take values in the compact factor $\mathfrak{su}(2) = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$ of the material sector, obtains the non-abelian curvature

$$
F_{\mu\nu} = \partial_\mu \mathcal{A}_\nu - \partial_\nu \mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu],
\qquad [D_\mu,D_\nu] = i\kappa F_{\mu\nu},
$$

and records, in its discussion of the Yang–Mills action, that the source-free field equation is $D_\mu F^{\mu\nu} = 0$ "in place of the abelian $\partial_\mu F^{\mu\nu} = 0$". It does not develop that equation: the sourced equation, the current that appears on its right-hand side, and the conservation law that current obeys are all left open. This article takes them up.

The Yang–Mills equation is the non-abelian generalisation of the Maxwell source equation,

$$
D_\mu F^{\mu\nu} = J^\nu,
\qquad
D_\mu F^{\mu\nu} = \partial_\mu F^{\mu\nu} + i\kappa\,[\mathcal{A}_\mu, F^{\mu\nu}],
$$

with the covariant derivative $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$ acting on the curvature through the commutator, in the adjoint action of the gauge algebra. The subject of this article is what changes from the abelian case, and the answer is a short list.

- **The field equation itself acquires a term.** In the abelian case the connection coefficients commute (in the parent's $U(1)$ case they are central), so $[\mathcal{A}_\mu,F^{\mu\nu}] = 0$ and the field equation is the ordinary divergence. In the non-abelian case the commutator term is present and cannot be dropped: the covariant derivative is not the ordinary one, and the source of a non-abelian gauge field is itself charged.
- **The current is covariantly conserved, not ordinarily conserved.** Taking the covariant divergence of the field equation gives $D_\mu J^\mu = 0$. This is *not* $\partial_\mu J^\mu = 0$: the ordinary divergence of the current is $-i\kappa[\mathcal{A}_\mu,J^\mu]$, which is nonzero for a generic non-abelian field. Writing ordinary conservation here would be a defect, not a simplification.
- **The terms that vanish in the abelian limit do so because the abelian connection commutes.** Every commutator that distinguishes the non-abelian equation from Maxwell contains either $[\mathcal{A}_\mu,\mathcal{A}_\nu]$ or $[\mathcal{A}_\mu,\,\cdot\,]$; all of them vanish when the connection coefficients commute, and none of them cancels against a nonvanishing partner.

The division between what is established and what is interpretation is kept explicit.

- **Established, and recomputed below.** The curvature identity $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$; the Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$; the Yang–Mills equation $D_\mu F^{\mu\nu} = J^\nu$ with the commutator term $i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$; the covariant conservation $D_\mu J^\mu = 0$ and the failure of ordinary conservation; the reduction to Maxwell on a commuting generator set; and the adjoint transformation $J'_\nu = U J_\nu U^{-1}$ of the source. Each was recomputed on a generic, non-constant $\mathfrak{su}(2)$-valued connection — all three generators, non-commuting — at four generic points, by exact polynomial arithmetic; no claim below rests on the abelian case.
- **Interpretation.** Reading $D_\mu F^{\mu\nu}$ as the conserved current of a non-abelian gauge field, and the field equation as the Euler–Lagrange equation of $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$, is the standard reading of the algebra, placed in the framework's notation. It is labelled as interpretation where it occurs.
- **Gaps and defects, left visible.** The biquaternion packaging of the curvature that the parent articles use, $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$, does not inherit the adjoint transformation as a single algebra conjugation, and the naive product $\nabla\!\cdot\!(\sum_\nu F^{\mu\nu}e_\nu)$ is not the covariant divergence of the field equation; both are stated precisely and neither is smoothed over. The framework's inability to fix the gauge is inherited unchanged and bounds the whole construction; no gauge is chosen anywhere below.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. On the material sector, $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$ with $\mathfrak{su}(2) = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, $[e_a,e_b] = 2\varepsilon_{abc}e_c$, and normalized generators $T_a = \tfrac12 e_a$ with $[T_a,T_b] = \varepsilon_{abc}T_c$ and $\mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}$. The gauge group is $SU(2)$, the unit real quaternions, $U^{-1} = \bar U = U^\dagger$. The connection and field strength of the non-abelian sector are $\mathcal{A}_\mu = \mathcal{A}_\mu^a e_a \in \mathfrak{su}(2)$ with $\mathcal{A} = \sum_\mu\mathcal{A}_\mu e_\mu$, and $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, with $\kappa = q/\hbar$ the coupling. The covariant derivative is $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$, $D = \tilde{\nabla} + i\kappa\mathcal{A}$, acting on a matter field by left multiplication. Indices run $\mu,\nu,\lambda \in \{0,1,2,3\}$ with $\partial_0 = \partial_{ict}$; in the $ict$ convention $\partial_\mu = \partial_{x_\mu}$ raises and lowers no index, so the coordinate sum $\sum_\mu$ is the Lorentz-invariant contraction and we may write $F^{\mu\nu}$ and $F_{\mu\nu}$ interchangeably. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged; where the Yang–Mills density is written, the trace is the **matrix trace** on the $\mathfrak{su}(2)$ factor, which is a different operation. No gauge is fixed.

## The Non-Abelian Curvature and the Adjoint Covariant Derivative

The constructions of this article are those of its two parents, and they are recalled here only far enough to fix the conventions the field equation uses.

The connection is an $\mathfrak{su}(2)$-valued one-form, $\mathcal{A}_\mu$, and the covariant derivative is $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$, with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$. Under a local gauge transformation $U(\tilde{X})\in SU(2)$ the connection and field strength transform in the adjoint representation,

$$
\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1} + \frac{i}{\kappa}(\partial_\mu U)U^{-1},
\qquad
F'_{\mu\nu} = U F_{\mu\nu} U^{-1},
$$

and $F_{\mu\nu}$ is *not* gauge invariant: it is an algebra element rotated by the group. The covariance of the first-order operator is what forces the inhomogeneous term in the first law.

Two derived objects carry the rest of the article. The first is the **adjoint covariant derivative**, the action of the gauge connection on an algebra-valued field $X$:

$$
D_\lambda X = \partial_\lambda X + i\kappa\,[\mathcal{A}_\lambda, X].
$$

It is the unique first-order operator whose action on $X$ is the commutator of the covariant derivative operator with multiplication by $X$. Recomputing that commutator directly,

$$
[D_\lambda, X]\Psi = D_\lambda(X\Psi) - X(D_\lambda\Psi)
= (\partial_\lambda X + i\kappa[\mathcal{A}_\lambda,X])\Psi,
$$

for every $\Psi$, so that as operators

$$
[D_\lambda, X] = D_\lambda X,
$$

with $X$ read as multiplication by the algebra element. (The notation table and the Bianchi discussion of *Non-Abelian Gauge Fields in Biquaternionic Form* print $[D_\lambda,X] = i\kappa D_\lambda X$; that line is not consistent with the definition $D_\lambda X = \partial_\lambda X + i\kappa[\mathcal{A}_\lambda,X]$ given in the same article, and the factor $i\kappa$ is an evident slip — the operator commutator is first order in $\partial_\lambda$ and equal to multiplication by $D_\lambda X$. The Bianchi identity itself is unaffected, because the substitution that produces it is the same either way once the identity is corrected. The recomputed identity $[D_\lambda,X] = D_\lambda X$ is the one used here, and it was checked numerically — see the companion.) The second is the **Bianchi identity**,

$$
D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0,
$$

where each $D$ is the adjoint covariant derivative. It is the statement that the exterior derivative of the curvature is a cycle, and it is automatic for a curvature built from a connection: it follows from the Jacobi identity for the operators $D_\mu$, $[D_\lambda,[D_\mu,D_\nu]] + \text{cyclic} = 0$, together with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$; equally, at the level of components, from the derivation property of the adjoint action. Both routes were recomputed.

The biquaternion packaging of the curvature, inherited from the parents, is the definition

$$
\mathcal{F} = \tfrac12\sum_{\mu,\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu \;\in\; \mathbb{B},
\qquad \bar{e}_0 = e_0,\; \bar{e}_k = -e_k .
$$

It collects the six independent curvature components against the quaternion-basis products $\bar{e}_\mu e_\nu$. What this object does and does not inherit under a gauge transformation is treated in its own section below; the reader should not assume that the componentwise transformation law $F_{\mu\nu}\mapsto UF_{\mu\nu}U^{-1}$ promotes to a single conjugation of $\mathcal{F}$.

## The Yang–Mills Equation

Let the current be the covariant divergence of the curvature,

$$
J^\nu := D_\mu F^{\mu\nu} = \partial_\mu F^{\mu\nu} + i\kappa\,[\mathcal{A}_\mu, F^{\mu\nu}], \qquad J^\nu \in \mathfrak{su}(2),
$$

summed over $\mu$. This is the definition of the source in this article; the equation

$$
\boxed{\,D_\mu F^{\mu\nu} = J^\nu\,}
$$

is the Yang–Mills equation, and the two terms of its expansion are the whole of its content.

- **The ordinary divergence $\partial_\mu F^{\mu\nu}$.** In the abelian limit this term alone is Maxwell's source equation. In the non-abelian case it is not gauge covariant on its own.
- **The commutator term $i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$.** The index $\mu$ of the connection is contracted with the *derivative* index of $F^{\mu\nu}$ — the first index — and the commutator is taken with that same $\mathcal{A}_\mu$. This is the only placement that makes the equation gauge covariant and the current covariantly conserved; it is the term most often got wrong. In the abelian case $\mathcal{A}_\mu$ commutes with the curvature (it is central in the parent's $U(1)$ case, and lies on a single generator otherwise), so the term vanishes.

The two slots of the index structure are fixed. The derivative that acts is the one whose index is contracted, and it must be the same index that labels the connection inside the commutator; and the curvature is contracted in its first index by that derivative. Writing $[\mathcal{A}_\nu,F^{\mu\nu}]$ (connection index equal to the free index), or $[\mathcal{A}_\mu,F^{\nu\mu}]$ (curvature contracted in its second index), or reversing the sign of the commutator term, each destroys the conservation law derived in the next section. This was checked directly on a generic non-commuting connection: the correct placement gives $D_\nu(D_\mu F^{\mu\nu}) = 0$ to $3\times10^{-15}$, while the three alternatives and the ordinary divergence give residuals of order $10$ — order unity on the same field. The reader who is unsure of a sign convention should repeat that one computation rather than consult memory.

**Gauge covariance.** The equation is covariant without any gauge being chosen. With $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ and the transformation of the connection, the covariant derivative satisfies $D'_\mu(U\Psi) = U D_\mu\Psi$, so the current transforms in the adjoint,

$$
J'^\nu = U J^\nu U^{-1},
$$

and $D'_\mu F'^{\mu\nu} = U(D_\mu F^{\mu\nu})U^{-1}$. The equation $D_\mu F^{\mu\nu} = J^\nu$ therefore holds in one gauge if and only if it holds in every gauge; no condition such as $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{\mathcal{A}}) = 0$, and no other gauge-fixing surface, is imposed or available. This point is worth stating because the framework's canonical-quantisation article records that it *cannot* fix the gauge; the Yang–Mills equation inherits that situation rather than relieving it. The adjoint transformation of the source was verified numerically on a generic connection with a generic (constant) group rotation; the covariance for a general local $U$ follows from the transformation laws above and was not separately rechecked.

**Biquaternionic form.** Pack the four components of the current into a biquaternion in the quaternion basis,

$$
\mathcal{J} = \sum_{\nu=0}^{3} J_\nu e_\nu \;\in\; \mathbb{B}.
$$

Then the Yang–Mills equation is the single biquaternion equation

$$
\sum_{\nu=0}^{3} \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J},
\qquad\text{equivalently}\qquad
\sum_{\nu=0}^{3} \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \sum_{\nu=0}^{3} J_\nu\, e_\nu ,
$$

in which the covariant derivative acts on the $\mathfrak{su}(2)$-valued curvature components by the adjoint action $D_\mu F_{\mu\nu} = \partial_\mu F_{\mu\nu} + i\kappa[\mathcal{A}_\mu,F_{\mu\nu}]$, and the sum over $\mu$ is the divergence. The left-hand side is the covariant divergence of the curvature, expanded in the quaternion basis; the right-hand side is the source biquaternion. This is the direct non-abelian analogue of the parent's $\tilde{\nabla}\tilde{F} = -\tilde{R}$: the parent's source biquaternion $\tilde{R}$ plays the role of $-\mathcal{J}$ up to the parent's normalisation of $\tilde{F}$ and $\tilde{R}$ (the parent uses $R_0 = i\rho/\sqrt{\epsilon}$, $\mathbf{R} = \sqrt{\mu}\,\mathbf{J}$, and writes its equation with the opposite sign). The sign of the source is a convention, fixed here by defining $J^\nu$ through the field equation; what is not a convention is that the derivative on the left is covariant.

**The biquaternion packaging does not collapse.** It is tempting to write the left-hand side as $\sum_\mu D_\mu F^\mu$ with $F^\mu := \sum_\nu F^{\mu\nu}e_\nu$, and to advertise a one-line product. That is not correct, and the failure is instructive. Because the adjoint commutator does not pass through the quaternion basis,

$$
D_\mu\bigl(F_{\mu\nu}e_\nu\bigr) = \bigl(D_\mu F_{\mu\nu}\bigr)e_\nu + i\kappa\,F_{\mu\nu}\,[\mathcal{A}_\mu,e_\nu],
$$

the extra term $i\kappa\sum_{\mu\nu}F_{\mu\nu}[\mathcal{A}_\mu,e_\nu]$ is present whenever $\mathcal{A}_\mu$ fails to commute with the basis elements. It does not vanish for a generic non-abelian connection, and it was verified to be of order unity. The biquaternionic field equation is therefore the basis-expanded contraction written above, not a single adjoint-covariant product of a packaged curvature. This is the same lesson the parent article records about $\mathrm{Vect}(\bar{\tilde{\nabla}}\mathcal{A})$: the quaternion packaging of a non-abelian curvature is a bookkeeping device, and products of packaged objects hide index mixing that must be checked.

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
\partial_\nu J^\nu + i\kappa\,[\mathcal{A}_\nu, J^\nu] = 0,
\qquad\text{that is}\qquad
\partial_\nu J^\nu = -\,i\kappa\,[\mathcal{A}_\nu, J^\nu].
$$

The ordinary divergence does not vanish. For a generic non-abelian connection it is of order unity, and only the covariant divergence is zero; the difference is exactly the commutator of the connection with the current. This was recomputed on a generic non-commuting connection: $D_\nu J^\nu$ vanishes to $3\times10^{-15}$ while $\partial_\nu J^\nu$ has magnitude $\approx 7$. Writing $\partial_\nu J^\nu = 0$ for the non-abelian current is false, and would drop the term that carries the adjoint action.

**What the conservation uses, and what it does not.** It is often said that the current is conserved "by the Bianchi identity". In this derivation the differential Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$ is *not* used. What is used is the field equation, the antisymmetry of $F_{\mu\nu}$, and the curvature identity $[D_\nu,D_\mu] = i\kappa F_{\nu\mu}$; the vanishing commutator $[F_{\nu\mu},F^{\mu\nu}] = 0$ is an algebraic consequence of antisymmetry, not the differential identity. (That algebraic identity is itself sometimes called a Bianchi identity, being the contracted statement that the curvature is an algebra element; the differential identity is a different object, and it is the differential one that is not needed here.) The differential Bianchi identity is the independent *homogeneous* half of the non-abelian system, treated in its own section below. The two are sometimes conflated because both are identities of the curvature and both trace back to the Jacobi identity at the level of operators; the reader is entitled to know which one does the work. The claim to be verified for the conservation is therefore field equation plus antisymmetry, and that is what was checked.

**Consistency, not an extra condition.** In the abelian case the analogous statement $\partial_\nu\partial_\mu F^{\mu\nu} = 0$ is automatic, and charge conservation is recovered from the field equation rather than imposed. In the non-abelian case the same logic gives the covariant law; the current defined by the field equation is covariantly conserved automatically, and no independent condition on $\rho$ and $\mathbf{J}$ is added. In this sense $D_\nu J^\nu = 0$ is the integrability condition of the Yang–Mills system, exactly as ordinary conservation is the integrability condition of Maxwell's system.

## The Abelian Limit

The abelian case is the case of a **commuting generator set**: the connection takes values in a one-dimensional subalgebra, so that all its coefficients commute. Two settings realise it in the framework. The parent's abelian connection lies in the center $\mathbb{C}_{\mathbb{B}}$, whose imaginary scalar $ie_0$ commutes with every biquaternion; and any connection proportional to a single fixed generator, $\mathcal{A}_\mu = a_\mu(\tilde{X})\,e_1$, has commuting coefficients even though $e_1$ is not central. The reduction to Maxwell is the same in both, and it is worth saying exactly which terms vanish and why.

Write $\mathcal{A}_\mu = a_\mu\,g$ for a fixed generator $g$ with $a_\mu$ scalar functions (for the center, $g = ie_0$; for a single spatial generator, $g = e_1$). Then

$$
[\mathcal{A}_\mu,\mathcal{A}_\nu] = a_\mu a_\nu\,[g,g] = 0,
$$

so the curvature loses its commutator,

$$
F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu = (\partial_\mu a_\nu - \partial_\nu a_\mu)\,g,
$$

and the Yang–Mills equation loses its own commutator term for the same reason:

$$
[\mathcal{A}_\mu,F^{\mu\nu}] = a_\mu\,(\partial^\mu a^\nu - \partial^\nu a^\mu)\,[g,g] = 0 .
$$

The field equation is therefore

$$
D_\mu F^{\mu\nu} = \partial_\mu F^{\mu\nu} = J^\nu,
$$

which is Maxwell's source equation, and the current is now a commuting biquaternion, invariant under the abelian gauge transformations that preserve the generator set. Correspondingly the conservation law degenerates,

$$
D_\nu J^\nu = \partial_\nu J^\nu + i\kappa\,[\mathcal{A}_\nu,J^\nu] = \partial_\nu J^\nu = 0,
$$

because $[\mathcal{A}_\nu,J^\nu] = a_\nu[g,g]J^\nu = 0$; the current is **ordinarily** conserved, and it is invariant under the abelian gauge transformations that preserve the commuting generator set, $J'^\nu = U J^\nu U^{-1} = J^\nu$ (in the center case every central $U$ qualifies, since $U$ is central; on a single spatial generator, the qualifying $U$ are those of the abelian subgroup generated by $g$).

Nothing here cancels. Every non-abelian term vanishes because the abelian connection commutes — with itself, with the curvature it generates, and with the current — not because two nonzero contributions are arranged to cancel. This is the precise sense in which the abelian case is the degenerate one, and it is why agreement on a commuting generator set is a consistency check on normalisation and signs but *not* evidence for the non-abelian statement: every non-abelian identity above was checked on the full non-commuting $\mathfrak{su}(2)$ connection, where the commutators are nonzero, and the abelian reduction was checked separately.

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

The framework's compact form of the abelian equations, $\tilde{\nabla}\tilde{F} = -\tilde{R}$, is a genuine one-line equation. For the non-abelian system the analogous packaging is more delicate, and this article records the limits of what the packaging delivers rather than presenting a formula that would not survive a recheck.

The curvature biquaternion is defined, as in the parent, by $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$. Its *components* transform in the adjoint, $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$, so $\mathcal{F}$ inherits the componentwise adjoint law

$$
\mathcal{F}' = \tfrac12\sum_{\mu\nu}\bigl(UF_{\mu\nu}U^{-1}\bigr)\bar{e}_\mu e_\nu .
$$

This is **not** the single algebra conjugation $U\mathcal{F}U^{-1}$, because $U^{-1}$ does not pass through the basis product $\bar{e}_\mu e_\nu$. The two agree only when the group element $U$ commutes with the basis product $\bar{e}_\mu e_\nu$, i.e. in the center case. This was verified: with a generic constant unitary $U$, $\mathcal{F}' = \tfrac12\sum(UF_{\mu\nu}U^{-1})\bar{e}_\mu e_\nu$ holds to machine precision, while $\mathcal{F}' = U\mathcal{F}U^{-1}$ fails by order unity. The componentwise law is what makes the current transform as $J'_\nu = UJ_\nu U^{-1}$ and what keeps the field equation covariant; the packaged law is simply not available.

Two consequences follow, and both are stated as findings rather than repairs.

- **The source biquaternion $\mathcal{J} = \sum_\nu J_\nu e_\nu$ is a valid packaging.** Its components transform in the adjoint, and the equation $\sum_\nu \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J}$ is exact and covariant. This is the biquaternionic form of the Yang–Mills equation used here.
- **A single adjoint-covariant product of the curvature is not that equation.** As shown in the previous section, $\sum_\mu D_\mu(\sum_\nu F^{\mu\nu}e_\nu)$ differs from $\sum_{\mu,\nu} \bigl(D_\mu F^{\mu\nu}\bigr) e_\nu$ by the index-mixing term $i\kappa\sum_{\mu\nu}F_{\mu\nu}[\mathcal{A}_\mu,e_\nu]$, which is nonzero for a generic connection. Whether some other representative of the non-abelian curvature makes the field equation a one-line product, in the way the pure-vector Riemann–Silberstein representative does in the abelian case, is not settled here.

## Open Questions

1. **A one-line biquaternion form.** The abelian parent compresses its four equations into $\tilde{\nabla}\tilde{F} = -\tilde{R}$. Is there a representative of the non-abelian curvature, or a modified product, for which the Yang–Mills equation is a single adjoint-covariant biquaternion identity, or is the index-mixing obstruction of this article fatal to that program? The obstruction found here is sharp enough to state and not resolved.

2. **Which compact algebra, and how many factors.** The gauge algebra used here is the $\mathfrak{su}(2)$ factor of the material sector, with the abelian factor $\mathbb{R}(ie_0)$ beside it. Whether larger gauge algebras are available, and whether the framework selects one, is the gap recorded by the non-abelian parent and untouched here.

3. **The reality class of the connection.** The non-abelian parent shows that no single Hermitian-conjugation eigenspace accommodates the connection across all four components, with the obstruction sitting in the time direction because $\partial_0 = \partial_{ict} = -i\partial_t$. The field equation and its conservation law are statements about the algebra and do not depend on resolving that, but the physical identification of $\mathcal{A}_\mu$ does.

4. **The matter representation.** The covariant derivative here acts by left multiplication, and the current is defined from the curvature alone. For coupled matter the representation carried by the matter field must be specified, and it is not fixed here; the chiral-fermion and minimal-coupling articles pose that question.

5. **Gauge fixing.** The framework cannot fix the gauge, and the Yang–Mills equation supplies no selection principle. The non-abelian case adds the Gribov question of whether a gauge orbit meets a gauge-fixing surface more than once; nothing here addresses it.

6. **Topological terms.** The Bianchi identity and the invariant density are the ingredients of $\int\mathrm{Tr}(F\wedge F)$ and of instanton solutions. The self-dual truncation of the field equation is treated elsewhere; its relation to the biquaternion packaging is open.

7. **Empirical contact.** As everywhere in the framework, whether any of this yields a prediction distinguishing it from standard non-abelian gauge theory is untouched. The construction is a reformulation.

## Summary

The Yang–Mills equation in biquaternionic form is the covariant divergence equation

$$
D_\mu F^{\mu\nu} = J^\nu,
\qquad
D_\mu F^{\mu\nu} = \partial_\mu F^{\mu\nu} + i\kappa\,[\mathcal{A}_\mu,F^{\mu\nu}],
\qquad
J^\nu \in \mathfrak{su}(2),
$$

with $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$ and $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$. Two things change from the abelian case, and both come from the single fact that the covariant derivative is not the ordinary one.

- The field equation acquires the commutator term $i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$, with the derivative index contracted with the first index of the curvature and with the connection of the same index inside the commutator. This is the only placement that makes the equation covariant and the current conserved; the three alternatives tested fail at order unity.
- The current is **covariantly** conserved, $D_\nu J^\nu = 0$, not ordinarily conserved: $\partial_\nu J^\nu = -i\kappa[\mathcal{A}_\nu,J^\nu] \neq 0$. The conservation follows from the field equation and the antisymmetry of the curvature, through $\tfrac12[D_\nu,D_\mu]F^{\mu\nu} = \tfrac12 i\kappa[F_{\nu\mu},F^{\mu\nu}] = 0$; the differential Bianchi identity is the independent homogeneous half and is not what makes it true.

In the abelian limit — a commuting generator set, whether the center $\mathbb{C}_{\mathbb{B}}$ of the parent or a single fixed generator — every commutator vanishes: $[\mathcal{A}_\mu,\mathcal{A}_\nu] = 0$ removes the curvature's commutator term, $[\mathcal{A}_\mu,F^{\mu\nu}] = 0$ removes the field equation's, and $[\mathcal{A}_\nu,J^\nu] = 0$ removes the one separating covariant from ordinary conservation. The equation reduces to Maxwell's, $\partial_\mu F^{\mu\nu} = J^\nu$, with an ordinarily conserved current that is invariant under the abelian gauge transformations preserving the generator set. Nothing cancels; the abelian connection commutes with everything it meets.

The biquaternionic packaging is exact for the current, $\mathcal{J} = \sum_\nu J_\nu e_\nu$ with $\sum_\nu \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J}$ and $J'_\nu = UJ_\nu U^{-1}$, and limited for the curvature: the representative $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ inherits the componentwise adjoint law, not a single conjugation, and the naive one-line product picks up an index-mixing term of order unity. That limitation is stated, not papered over.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; abelian gauge factor |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient; $\partial_0 = \partial_{ict} = -i\partial_t$ |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | d'Alembertian |
| $[e_a,e_b] = 2\varepsilon_{abc}e_c$ | Commutator on the vector part of $\mathbb{M}_-$ |
| $\mathfrak{su}(2) = \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Compact gauge algebra inside $\mathbb{M}_-$ |
| $T_a = \tfrac12 e_a$, $\mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}$ | Normalized generators; matrix trace |
| $U(\tilde{X}) \in SU(2)$ | Unit real quaternion, $U^{-1} = \bar U = U^\dagger$ |
| $\mathcal{A}_\mu = \mathcal{A}_\mu^a e_a \in \mathfrak{su}(2)$, $\mathcal{A} = \sum_\mu\mathcal{A}_\mu e_\mu$ | Non-abelian connection |
| $\kappa = q/\hbar$ | Coupling |
| $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$, $D = \tilde{\nabla} + i\kappa\mathcal{A}$ | Covariant derivative (left multiplication on matter) |
| $\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1} + \frac{i}{\kappa}(\partial_\mu U)U^{-1}$ | Adjoint gauge transformation of the connection |
| $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian curvature |
| $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ | Adjoint transformation of the curvature (not invariant) |
| $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$ | Curvature as commutator of covariant derivatives |
| $D_\lambda X = \partial_\lambda X + i\kappa[\mathcal{A}_\lambda,X]$ | Adjoint covariant derivative; $[D_\lambda,X] = D_\lambda X$ |
| $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$ | Bianchi identity (homogeneous half) |
| $J^\nu = D_\mu F^{\mu\nu} = \partial_\mu F^{\mu\nu} + i\kappa[\mathcal{A}_\mu,F^{\mu\nu}]$ | Yang–Mills current (source) |
| $D_\mu F^{\mu\nu} = J^\nu$ | Yang–Mills equation |
| $D_\nu J^\nu = 0$ | Covariant conservation of the current |
| $\partial_\nu J^\nu = -i\kappa[\mathcal{A}_\nu,J^\nu]$ | Failure of ordinary conservation |
| $J'_\nu = UJ_\nu U^{-1}$ | Adjoint transformation of the source |
| $\mathcal{J} = \sum_\nu J_\nu e_\nu$ | Source biquaternion |
| $\sum_\nu \bigl(D_\mu F_{\mu\nu}\bigr) e_\nu = \mathcal{J}$ | Biquaternionic form of the field equation |
| $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ | Curvature biquaternion (componentwise adjoint law) |
| $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ | Gauge-invariant Yang–Mills density (matrix trace) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula (distinct from the matrix trace) |
| $\tilde{R} = R_0+\mathbf{R}$ | Parent's abelian source biquaternion; plays the role of $-\mathcal{J}$ up to the parent's normalisation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- *Non-Abelian Gauge Fields in Biquaternionic Form* — the immediate parent; the $\mathfrak{su}(2)$ factor, the curvature with its commutator, the adjoint transformation, the Bianchi identity, and the source-free equation $D_\mu F^{\mu\nu} = 0$ that this article sources.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the abelian connection and covariant derivative, the curvature as a commutator that closes on the algebra, and the gap this article and its non-abelian companion take up.
- *Maxwell's Equations in the Biquaternionic Formulation* — the abelian field equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, the source biquaternion, and the conservation law whose non-abelian generalisation is the subject here.
- *The Gauge Principle in Biquaternionic Form* — the origin of the connection and the transformation law, and the preview of the non-abelian curvature used here.
- *The Field-Strength Biquaternion and Its Invariants* — the abelian invariants and the norm form, whose non-abelian extension remains open.
- *Chiral Fermions in the Biquaternion Framework* — the covariant derivative on the spinor module and the matter representation that the current of this article does not fix.
- *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — the left/right matter-representation question and the coupled Dirac equation.
- *Canonical Quantization of the Biquaternion Maxwell Field* — the framework's inability to fix the gauge, which bounds the non-abelian orbit.
- *Instantons and Solitons in Biquaternionic Form* — the self-dual truncation $D_\mu F^{\mu\nu} = 0$ and the topological charge built from the Bianchi identity.
- *Lie Algebras: A General Introduction* — the Jacobi identity, the adjoint action as a derivation, and the commutator bracket on an associative algebra.
- *Biquaternion Algebra* and *Quaternion Algebra* — the multiplication rule, the conjugations and the center used throughout.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the sector basis and the imaginary-scalar/real-vector structure on which the $\mathfrak{su}(2)$ gauge factor rests.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector and the trace formula distinguished here from the matrix trace.
- *Curved Spacetime and the Biquaternion Framework* — the two-sided gravitational connection, distinct from the one-sided gauge connection of this article.
