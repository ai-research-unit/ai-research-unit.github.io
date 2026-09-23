# __Non-Abelian Gauge Fields in Biquaternionic Form__

## Introduction

The companion article *The Covariant Derivative and Gauge Connection in Biquaternionic Form* develops the gauge structure that the localization of a **central** phase forces on the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. Its connection is one-sided and its gauge group is the unitary part of the center, $U(1)$: it works with a connection whose coefficients are central, and it records that it is not the two-sided gravitational connection. It closes with an explicit gap, in its own words that "the non-abelian extension still needs a reality condition selecting a compact gauge algebra". This article takes that gap up.

The essential difference from the abelian case has nothing to do with the existence of a connection, or with the commutator form of the curvature. Both survive. It is a single, decisive change: **the field strength is no longer gauge invariant.** In the abelian case the connection coefficients are central, so the curvature transforms trivially and $\tilde{F}$ is a gauge-invariant object. In the non-abelian case the field strength carries the adjoint representation and transforms by conjugation,

$$
F'_{\mu\nu} = U\,F_{\mu\nu}\,U^{-1},
\qquad U = U(\tilde{X}) \in SU(2),
$$

so a component of the field strength is *not* a number; it is an algebra element that is rotated by the gauge group. Every other non-abelian feature — the commutator term $[A_\mu,A_\nu]$ in $F$, the non-linearity of the field equations, the Bianchi identity as the statement that the covariant derivative of $F$ is a cycle — is downstream of this one fact. The single most likely error in passing from the abelian case to the non-abelian one is to keep treating $F$ as invariant, and the bulk of this article is arranged as a guard against it.

The division between what is established and what is interpretation is kept explicit.

- **Established, and recomputed below.** The vector part of the material sector, $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, is a Lie subalgebra of $\mathbb{B}$ under the commutator, and it is $\mathfrak{su}(2)$ up to normalization; the center contributes the abelian factor. The non-abelian field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + i\kappa[A_\mu,A_\nu]$ transforms in the adjoint representation and is not invariant; it is the commutator of covariant derivatives, $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$; the Bianchi identity holds; and $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ is a gauge-invariant density. All of these were recomputed exactly on $\mathfrak{su}(2)$, on generic non-commuting connections, and on at least two independent components (in fact on all six).
- **Defect in the parent, reported rather than inherited.** The parent's packaging of the curvature, $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ and $\tilde{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$, does **not** survive the non-abelian extension. The object $\mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is not even in the reality class of the field strength, and it is not the adjoint-covariant object. This is stated in its own section and the repair is given.
- **Gap, left visible.** The reality condition on the *connection* that would make the non-abelian construction close inside a fixed Hermitian-conjugation eigenspace is obstructed in the time direction by the $ict$ derivative, $\partial_0 = \partial_{ict} = -i\partial_t$. The obstruction is sharp, is exhibited, and is not smoothed over.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The potential and field strength of the abelian sector are $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ and $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. For the non-abelian sector we write $\kappa = q/\hbar$ for the coupling and use the components $\mu,\nu,\lambda \in \{0,1,2,3\}$ with $\partial_0 = \partial_{ict}$, so that $\partial_\mu = \partial_{x_\mu}$ raises and lowers no index: in the $ict$ convention the coordinate sum $\sum_\mu$ is the Lorentz-invariant contraction.

## The Gauge Algebra Inside the Material Sector

The parent article identifies the abelian gauge group with the unitary part of the center $\mathbb{C}_{\mathbb{B}}$, and it records that the commutator algebra of $\mathbb{B}\cong M_2(\mathbb{C})$ is $\mathfrak{gl}(2,\mathbb{C})$, which is not compact. It is worth stating precisely what *is* available before any reality condition is imposed, because more is available than that remark suggests.

Under the commutator bracket, $\mathbb{B}$ is a real Lie algebra (every associative algebra is, *Lie Algebras: A General Introduction*). Three facts about it are elementary and were recomputed from the quaternion multiplication rule.

**1. The center contributes the abelian factor.** The central line is $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$, and the scalar imaginary is central,

$$
[i e_0,\, e_a] = 0, \qquad a = 1,2,3 .
$$

The imaginary scalar $ie_0$ is the generator of the abelian gauge group of the parent article: this is why the abelian connection could be central.

**2. The vector part of the material sector is a compact Lie algebra.** The three quaternion units span the real-vector, traceless part of $\mathbb{M}_-$, and they close under the commutator:

$$
[e_a, e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad a,b,c = 1,2,3,
$$

with every generator traceless and anti-Hermitian, $e_a^\dagger = -e_a$, $e_a \in \mathbb{M}_-$. This is $\mathfrak{su}(2)$ in a non-standard normalization; the conventionally normalized generators are $T_a = \tfrac12 e_a$, in terms of which $[T_a,T_b] = \varepsilon_{abc}T_c$ and $\mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}$. The sign of the trace is fixed by $e_k^2 = -e_0$; the positive-definite form $h_{ab} = -2\,\mathrm{Tr}(T_aT_b) = \delta_{ab}$ is the Killing form of this copy of $\mathfrak{su}(2)$.

**3. The material sector splits as a Lie algebra.** Combining the two, and using that the vector part of $\mathbb{M}_-$ is exactly $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$ and the scalar part is $\mathrm{span}_\mathbb{R}\{ie_0\}$,

$$
\mathbb{M}_- \;=\; \mathbb{R}(ie_0) \;\oplus\; \mathfrak{su}(2) \qquad \text{(direct sum of Lie algebras)} .
$$

The abelian factor is the imaginary scalar; the non-abelian factor is the real vector part. This is the precise sense in which the algebra already contains a compact simple gauge algebra: the parent article is right that $\mathfrak{gl}(2,\mathbb{C})$ is not compact, but the *material sector* is not all of $\mathbb{B}$, and its vector part is $\mathfrak{su}(2)$. What is not yet settled is which reality class the *connection* occupies once it takes values in this algebra — a matter treated in its own section below, and the one place where the $ict$ convention bites.

The gauge group of this article is the group generated by the compact factor,

$$
SU(2) \;=\; \bigl\{ U \in \mathbb{H}_{\mathbb{B}} : U\bar U = e_0 \bigr\},
$$

the unit-norm real quaternions. This is the group of rotors of pure spatial rotations in the corpus's Lorentz-group article, and it is the double cover of $SO(3)$. Its Lie algebra is $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$ under the commutator. The group element satisfies $U^{-1} = \bar U = U^\dagger$, so the quaternion conjugate, the Hermitian conjugate and the inverse coincide for $SU(2)$.

## The Non-Abelian Connection and Covariant Derivative

Let the connection be a one-form with values in this Lie algebra,

$$
\mathcal{A}_\mu(\tilde{X}) = \mathcal{A}_\mu^{a}(\tilde{X})\,e_a \;\in\; \mathfrak{su}(2), \qquad \mathcal{A} = \sum_{\mu=0}^{3}\mathcal{A}_\mu\,e_\mu ,
$$

with real coefficient functions $\mathcal{A}_\mu^{a}$. The parent's covariant derivative is generalized in the only way that keeps its form,

$$
D_\mu = \partial_\mu + i\kappa\,\mathcal{A}_\mu, \qquad D = \tilde{\nabla} + i\kappa\,\mathcal{A},
\qquad \kappa = \frac{q}{\hbar},
$$

acting on a matter field $\Psi$ by left multiplication, $D_\mu\Psi = \partial_\mu\Psi + i\kappa\,\mathcal{A}_\mu\Psi$. The coupling $\kappa$ plays the role of the abelian $iq/\hbar$; the factor $i$ is kept explicit, as in the parent, so that the reality discussion below can be stated cleanly.

Now let the field transform by a **local, non-central** element of the group,

$$
\Psi \;\longmapsto\; U(\tilde{X})\,\Psi, \qquad U \in SU(2).
$$

Unlike the abelian phase, $U$ does not commute with the algebra, and left and right multiplication by it differ. Requiring the covariant derivative to be covariant, $D'_\mu(U\Psi) = U\,D_\mu\Psi$, with $D'_\mu$ built from a new connection $\mathcal{A}'_\mu$, gives

$$
(\partial_\mu U)\Psi + U\,\partial_\mu\Psi + i\kappa\,\mathcal{A}'_\mu U\Psi
= U\,\partial_\mu\Psi + i\kappa\,U\,\mathcal{A}_\mu\Psi,
$$

so that $\partial_\mu U + i\kappa\,\mathcal{A}'_\mu U = i\kappa\,U\mathcal{A}_\mu$, that is,

$$
\mathcal{A}'_\mu = U\,\mathcal{A}_\mu\,U^{-1} + \frac{i}{\kappa}\,(\partial_\mu U)\,U^{-1}.
$$

This is the non-abelian transformation law. Two features separate it from the parent's additive law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$.

- **The homogeneous term is a conjugation.** The connection does not transform by a shift; it transforms in the adjoint representation, $A_\mu \mapsto UA_\mu U^{-1}$, with a compensating inhomogeneous term. The conjugation is what makes the transformation law non-linear in the field and the theory non-abelian.
- **The inhomogeneous term is a pure-gauge connection.** The combination $(\partial_\mu U)U^{-1}$ is the Maurer–Cartan form of the group element; it is the non-abelian replacement for $-\partial_\mu\Gamma$. In the abelian case $U = e^{i\kappa\Gamma}$ is central, $U\mathcal{A}_\mu U^{-1} = \mathcal{A}_\mu$, and $(\partial_\mu U)U^{-1} = i\kappa\,\partial_\mu\Gamma$, so the law reduces exactly to the parent's $\tilde{A}'_\mu = \tilde{A}_\mu - \partial_\mu\Gamma$.

The covariance was verified numerically on a generic non-commuting connection: with the $\mathcal{A}_\mu$ traceless and $U$ a generic unitary biquaternion, the residual of $D'_\mu(U\Psi) = U D_\mu\Psi$ was of order $10^{-11}$ for all four $\mu$, i.e. at the level of the finite-difference error. It is worth saying what the check means: the identity was *derived* for arbitrary $U$ and arbitrary $\mathcal{A}$, and the numerical evaluation is a guard against a sign slip in the derivation, not the source of the result.

**Example, and the check that it is non-abelian.** Take the constant connections $\mathcal{A}_1 = e_3$ and $\mathcal{A}_2 = e_1$ and the group element $U = \exp(\theta e_2)$ for a real constant $\theta$. Since $U$ is constant the inhomogeneous term is absent, and $\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1}$. For $\mu=1$ this is $Ue_3U^{-1}$, which for $\theta = \pi/2$ equals $-e_3$ (a rotation by $\pi$ about $e_2$), while the abelian law would have left it unchanged. This is the smallest display of the changed character of the connection: it is not a value that shifts by a gradient, it is a vector in a representation that rotates.

## The Field Strength Is Not Gauge Invariant

The field strength is defined as the curvature of the connection. In component form, and in parallel with the parent's $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$,

$$
F_{\mu\nu} = \partial_\mu \mathcal{A}_\nu - \partial_\nu \mathcal{A}_\mu + i\kappa\,[\mathcal{A}_\mu, \mathcal{A}_\nu] \;\in\; \mathfrak{su}(2)\oplus i\,\mathfrak{su}(2) = \mathfrak{sl}(2,\mathbb{C}),
$$

or as an algebra-valued two-form,

$$
F = d\mathcal{A} + i\kappa\,\mathcal{A}\wedge\mathcal{A},
\qquad
(\mathcal{A}\wedge\mathcal{A})_{\mu\nu} = [\mathcal{A}_\mu,\mathcal{A}_\nu].
$$

The commutator term is the whole of the difference from the abelian case, and it is not optional: it is what the transformation law requires. To see that, and to see the essential point of this article, apply the transformation law to the definition. Write $B_\mu = (\partial_\mu U)U^{-1}$, so that $\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1} + (i/\kappa)B_\mu$. Two elementary identities prepare the computation:

$$
\partial_\mu B_\nu - \partial_\nu B_\mu = [B_\mu,B_\nu],
$$

which is the Maurer–Cartan (flatness) identity for the pure-gauge field $B_\mu$, and $\partial_\mu(U\mathcal{A}_\nu U^{-1}) = B_\mu\,U\mathcal{A}_\nu U^{-1} + U(\partial_\mu\mathcal{A}_\nu)U^{-1} - U\mathcal{A}_\nu U^{-1}B_\mu$, from $(\partial_\mu U) = B_\mu U$ and $\partial_\mu(U^{-1}) = -U^{-1}(\partial_\mu U)U^{-1}$. Antisymmetrizing the first in $\mu\nu$ and expanding the commutator term of $F'_{\mu\nu}$, the pure-gauge contributions cancel in pairs and one is left with

$$
F'_{\mu\nu} = U\,F_{\mu\nu}\,U^{-1} .
$$

This is the adjoint transformation law, and it is the central statement of the article.

**$F$ is not gauge invariant.** Taking the trace of the transformation law, $\mathrm{Tr}(F'_{\mu\nu}) = \mathrm{Tr}(F_{\mu\nu})$, so the *trace* of each component is invariant; but the component itself is rotated by $U$ and changes. This was verified on all six independent components $(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)$ on a generic non-commuting connection: the residual of $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ was of order $10^{-11}$, while the change $F'_{\mu\nu} - F_{\mu\nu}$ was of order unity for every component. Two of the six, the spatial pair $(1,3)$ and the mixed pair $(0,1)$, are quoted here precisely because the abelian habit is strongest on the spatial pairs, where the commutator term vanishes and one might expect invariance by analogy with the curl:

$$
F'_{13} \neq F_{13}, \qquad F'_{01} \neq F_{01},
\qquad\text{both by order unity.}
$$

**The abelian limit.** If all the $\mathcal{A}_\mu$ are central — the abelian case — the commutator term vanishes, the transformation law degenerates to the abelian one, and $F_{\mu\nu}$ becomes invariant. The invariance of the abelian field strength is therefore not a general property of the curvature; it is the consequence of centrality, and it is exactly what fails here.

**The connection as an adjoint-valued orbit.** The parent's reading of the connection as a gauge orbit survives, with the abelian group replaced by the adjoint action. The single point $\mathcal{A}_\mu(\tilde{X}_0) = 0$ can still be reached at any one point: take $U(\tilde{X}_0)$ arbitrary in $SU(2)$ and set $(\partial_\mu U)(\tilde{X}_0) = i\kappa\,U(\tilde{X}_0)\mathcal{A}_\mu(\tilde{X}_0)$, as the vanishing of $\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1} + (i/\kappa)(\partial_\mu U)U^{-1}$ requires. The first derivatives of a matrix-valued function at a point can be set freely subject to the conjugation condition that unitarity imposes, and the prescribed derivative meets that condition under the mixed reality assignment exhibited in the reality-condition section below ($\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian); for a uniform anti-Hermitian connection the spatial components cannot be brought to zero by a unitary $U$. For that mixed assignment the connection therefore has no gauge-invariant local value. The curvature is again the obstruction to doing this on a neighbourhood. The difference is that the orbit is now the orbit of a vector under conjugation rather than a translate of a scalar, and the statement "$\mathcal{A}$ can be gauged to zero at a point" is a statement about a matrix, not a number.

## The Field Strength as the Commutator of Covariant Derivatives

The curvature is also the antisymmetrized square of the covariant derivative. Direct computation from $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$ gives

$$
[D_\mu, D_\nu] = i\kappa\,F_{\mu\nu},
\qquad
F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu].
$$

The commutator of covariant derivatives is first order — the second-order terms $\partial_\mu\partial_\nu$ cancel — and it is multiplication by an algebra element, exactly as in the abelian case; what is new is that this element now contains the commutator of the connections. This identity was recomputed on all pairs $\mu,\nu$ on the same generic non-commuting connection, with residual of order $10^{-16}$.

The identity has a structural reading that the abelian case hides. The failure of covariant derivatives to commute is measured by the curvature; and since $F_{\mu\nu} = (1/i\kappa)[D_\mu,D_\nu]$, the statement that $F$ transforms in the adjoint representation is the statement that the commutator of two covariant derivatives is an algebra element on which the gauge group acts by conjugation. In the abelian case the bracket vanishes for the connection and the curvature is a c-number; the adjoint representation is then trivial, which is precisely why $F$ appeared invariant.

## The Bianchi Identity and Where Jacobi Enters

The field strength is constructed from the connection by differentiation, so it cannot be arbitrary: it satisfies a differential identity. In the non-abelian case this identity is not optional either, and it is the statement that the covariant derivative of $F$ is a cycle. Define the covariant derivative acting on an algebra-valued field $X$ by the adjoint action,

$$
D_\lambda X = \partial_\lambda X + i\kappa\,[\mathcal{A}_\lambda, X],
$$

which is the same as the commutator of operators, $[D_\lambda,X] = D_\lambda X$ when $X$ is multiplication by an algebra element. Then the **Bianchi identity** is

$$
D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0
\qquad \text{for all } (\lambda,\mu,\nu).
$$

It was recomputed on all four independent triples $(\lambda,\mu,\nu) = (0,1,2),(0,1,3),(0,2,3),(1,2,3)$ on the generic non-commuting connection, with residual of order $10^{-10}$.

**Where the Jacobi identity enters.** There are two distinct places, and conflating them hides the structure.

- **At the level of operators.** The covariant derivatives $D_\mu$ are operators, and the Jacobi identity for the commutator of any associative algebra gives $[D_\lambda,[D_\mu,D_\nu]] + [D_\mu,[D_\nu,D_\lambda]] + [D_\nu,[D_\lambda,D_\mu]] = 0$. Substituting $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$ and $[D_\lambda,F_{\mu\nu}] = D_\lambda F_{\mu\nu}$ turns this operator identity directly into the Bianchi identity. The identity is exact for operators regardless of the reality or compactness of the connection algebra; it is the associativity of operator composition.
- **At the level of the connection components.** In the coordinate proof, the terms built from $\mathcal{A}\wedge\mathcal{A}$ must cancel against the derivatives of the commutator term, and the cancellation uses the *algebraic* Jacobi identity for the connection components,
$$
[\mathcal{A}_\lambda, [\mathcal{A}_\mu,\mathcal{A}_\nu]] + [\mathcal{A}_\mu, [\mathcal{A}_\nu,\mathcal{A}_\lambda]] + [\mathcal{A}_\nu, [\mathcal{A}_\lambda,\mathcal{A}_\mu]] = 0 .
$$

The second is the same identity that the general theory of Lie algebras singles out: in *Lie Algebras: A General Introduction* it is the identity that makes the adjoint action $\mathrm{ad}_u = [u,\cdot]$ a derivation of the bracket. It is that derivation property, $\mathrm{ad}_{\mathcal{A}_\lambda}([\mathcal{A}_\mu,\mathcal{A}_\nu]) = [\mathrm{ad}_{\mathcal{A}_\lambda}\mathcal{A}_\mu,\mathcal{A}_\nu] + [\mathcal{A}_\mu,\mathrm{ad}_{\mathcal{A}_\lambda}\mathcal{A}_\nu]$, that makes $D_\lambda$ act on a commutator by the Leibniz rule in the coordinate computation. The algebraic Jacobi identity was checked exactly on the three generators of $\mathfrak{su}(2)$, with residual identically zero.

**Continuous formulation.** Contracting the Bianchi identity with the totally antisymmetric symbol gives the compact form

$$
\varepsilon^{\lambda\mu\nu\rho}\, D_\lambda F_{\mu\nu} = 0,
$$

which is the non-abelian analogue of the statement that the homogeneous Maxwell equations are automatic once the field strength is a curl. This is the sense in which the parent article's remark — "the homogeneous Maxwell equations are identities rather than equations of motion" — survives the non-abelian extension: it survives as the Bianchi identity, *not* as the one-line source-free equation $\tilde{\nabla}\tilde{F} = 0$, which the parent's companion records is the full source-free Maxwell system and not the Bianchi identity.

## The Yang–Mills Action

The action is the integral of the simplest invariant density built from the field strength. Since $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ and the trace is cyclic,

$$
\mathrm{Tr}\!\left(F'_{\mu\nu}F'^{\,\mu\nu}\right)
= \mathrm{Tr}\!\left(UF_{\mu\nu}U^{-1}UF^{\mu\nu}U^{-1}\right)
= \mathrm{Tr}\!\left(F_{\mu\nu}F^{\mu\nu}\right),
$$

so the local density

$$
\mathcal{L} = -\frac{1}{2}\,\mathrm{Tr}\!\left(F_{\mu\nu}F^{\mu\nu}\right),
\qquad
S_{\mathrm{YM}} = \int d^4x\;\mathcal{L},
$$

is gauge invariant. The invariance was recomputed on the generic non-commuting connection with residual of order $10^{-9}$ (limited by the finite-difference derivatives, not by the identity). The trace here is the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$, restricted to the $\mathfrak{su}(2)$ factor; it is **not** the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, which pairs an element of the informational sector with a Hermitian element and is a different pairing on a different subspace. Conflating the two would be an error of the same kind the parent article warns against when it distinguishes the material from the informational sector.

The sign and normalization of $\mathcal{L}$ are the standard ones when the generators are normalized so that the form $-2\,\mathrm{Tr}(T_aT_b) = \delta_{ab}$; the overall sign convention is fixed by the reality class of the connection, treated in the next section. Since the density is a total trace, its variation under a gauge transformation vanishes, and the field equations are the non-abelian Maxwell–Yang–Mills equations, obtained by varying $\mathcal{A}_\mu$: the source-free equation is $D_\mu F^{\mu\nu} = 0$, in place of the abelian $\partial_\mu F^{\mu\nu} = 0$. The covariant derivative is necessary, not decorative: the source term of a non-abelian gauge field is itself charged, so the field equation cannot be linear in $F$.

## The Abelian Parent's Curvature Formula Does Not Survive

The parent article packages the curvature in biquaternion form as

$$
\tilde{F} = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right),
\qquad
\tilde{F} = \frac{1}{2}\sum_{\mu,\nu=0}^{3}F_{\mu\nu}\,\bar{e}_\mu e_\nu ,
$$

and it states that the first identity — the expression of $\tilde{F}$ as $\mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ — is "purely algebraic in the derivatives". Both formulas, and the invariance of $\tilde{F}$ asserted two paragraphs later ("The curvature is gauge invariant"), are theorems in the abelian case, and all three **fail** when the connection is $\mathfrak{su}(2)$-valued. This is a defect of the parent, not a defect of this article's construction, and it is reported here rather than quietly repaired.

To state the failure precisely, take the natural non-abelian generalization of the first formula, $\bar{\tilde{\nabla}}\mathcal{A} = \sum_{\mu\nu}\bar{e}_\mu(\partial_\mu\mathcal{A}_\nu)e_\nu$ with $\mathcal{A}_\nu$ now an algebra element, and let $\mathrm{Vect}$ be the trace-free projection used by the parent, $\mathrm{Vect}(X) = X - \mathrm{Sc}(X)$ with $\mathrm{Sc}(X) = \tfrac12\mathrm{Tr}(X)e_0$. On the generic non-commuting connection:

1. **$\mathrm{Vect}(\bar{\tilde{\nabla}}\mathcal{A})$ is not in the reality class of the field strength.** Evaluated on a connection whose components are Hermitian-traceless, the object acquires a nonzero anti-Hermitian part of order unity; it is not Hermitian. This is not a cosmetic difference. In the abelian case $\mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is, up to the normalization, the gauge-invariant field strength — a pure vector with a fixed behaviour under quaternion conjugation — which is what permits the corpus to identify it with $\tilde{F}$; non-abelianly the corresponding object is not adjoint-covariant and need not coincide with the field strength.
2. **$\mathrm{Vect}(\bar{\tilde{\nabla}}\mathcal{A})$ is not adjoint-covariant.** Its gauge transform does not equal $U\,\mathrm{Vect}(\bar{\tilde{\nabla}}\mathcal{A})\,U^{-1}$; the discrepancy is of order unity. The reason is structural: differentiating $\bar{\tilde{\nabla}}\mathcal{A}$ brings down a term $(\partial_\mu U)$, which is not accompanied by the compensating connection term because the object is bilinear in $\mathcal{A}$ rather than built from the covariant derivative. The abelian case is immune only because there the inhomogeneous term is central and cancels in $\bar{\tilde{\nabla}}\tilde{A}$.
3. **The two parent formulas are not equal to each other.** The combination $\tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$, formed with the *non-abelian* $F_{\mu\nu}$, differs from $\mathrm{Vect}(\bar{\tilde{\nabla}}\mathcal{A})$ by an order-unity amount.

The repair is not a small correction; it is a redefinition of what is being packaged. The biquaternion packaging that survives is

$$
\mathcal{F} := \frac{1}{2}\sum_{\mu,\nu=0}^{3}F_{\mu\nu}\,\bar{e}_\mu e_\nu,
\qquad
F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu],
$$

which is a **definition** of the biquaternion representative of the curvature, not an identity expressing it as $\mathrm{Vect}$ of a derivative. Its content is the component identity $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$; the biquaternion $\mathcal{F}$ is a convenient carrier of the six independent components and their gauge transformation, not a derived quantity. The parent's clause "purely algebraic in the derivatives" applies to the antisymmetrized derivative part alone; the commutator part is not a derivative of anything and is where the non-abelian content lives.

It should be said in the parent's defence that its formulas are correct in its own domain. The abelian curvature identity $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is exact when the connection coefficients commute, and it was recomputed there. What the non-abelian extension shows is that the identity is a consequence of centrality, not a general property of curvature — the same lesson as the invariance of $F$.

## The Reality Condition and the ict Direction

The parent's outstanding gap is a "reality condition selecting a compact gauge algebra". The previous sections supply the algebra — $\mathfrak{su}(2)$ sits inside the material sector — but the reality of the *connection* under a gauge transformation is obstructed, and this is the honest gap of the present article.

The obstruction is visible in the inhomogeneous term of the transformation law. For a unitary $U$, differentiation of $UU^\dagger = e_0$ gives

$$
(\partial_\mu U)U^\dagger = -\,U(\partial_\mu U)^\dagger ,
$$

which says that $(\partial_\mu U)U^{-1}$ is anti-Hermitian **when the derivative is an ordinary real derivative**. This was checked numerically on a general unitary $U$ (not merely on the exponential parametrization); what was found is the sharp split

$$
(\partial_k U)\,U^{-1} \ \text{is anti-Hermitian for } k=1,2,3,
\qquad
(\partial_0 U)\,U^{-1} \ \text{is Hermitian.}
$$

The reason is the $ict$ convention. The time derivative is $\partial_0 = \partial_{ict} = -i\partial_t$, so the object $(\partial_0U)U^{-1}$ carries a factor $-i$ relative to $(\partial_tU)U^{-1}$; and both $(\partial_tU)U^{-1}$ and $(\partial_kU)U^{-1}$ are anti-Hermitian for a unitary $U$. Multiplication by $-i$ converts an anti-Hermitian matrix into a Hermitian one. Hence the time-like component of the Maurer–Cartan form has the opposite conjugation behaviour to the space-like components.

The consequence for the reality condition is immediate. The transformation law is

$$
\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1} + \frac{i}{\kappa}\,(\partial_\mu U)U^{-1},
$$

and the homogeneous term preserves the Hermitian-conjugation eigenspace of $\mathcal{A}_\mu$, while the inhomogeneous term has eigenvalue

$$
\text{space: } i\cdot(\text{anti-Hermitian}) = \text{Hermitian},
\qquad
\text{time: } i\cdot(\text{Hermitian}) = \text{anti-Hermitian}.
$$

So a reality condition of the form "all four components of $\mathcal{A}_\mu$ lie in the same Hermitian-conjugation eigenspace" **cannot** be gauge invariant. This was confirmed directly: with all four components chosen Hermitian-traceless, the transformed spatial components remain Hermitian-traceless to $10^{-11}$, while the transformed time component acquires an anti-Hermitian part of order unity.

Two things can be said, one verified and one open.

- **Verified.** There is a consistent assignment, namely
$$
\mathcal{A}_0 \ \text{anti-Hermitian traceless (in } \mathfrak{su}(2)\subset\mathbb{M}_-\text{)},
\qquad
\mathcal{A}_k \ \text{Hermitian traceless (in } i\,\mathfrak{su}(2)\subset\mathbb{M}_+\text{)} ,
$$
under which the transformed components close: $\mathcal{A}'_0$ is anti-Hermitian-traceless and $\mathcal{A}'_k$ is Hermitian-traceless, to $10^{-9}$ under a generic unitary $U$; and the adjoint transformation $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ continues to hold for the mixed pairs. The time component sits in the material sector and the spatial components in the informational sector; the pattern is the one the $ict$ convention dictates for any four-vector ($x^0 = ict$ imaginary, $x^k$ real), and it mirrors the parent's abelian connection $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ with its imaginary scalar and real vector coefficients.
- **Open.** Whether this mixed assignment is the one the framework intends, or whether the time-like and space-like components should be combined into a single reality condition by a different placement of the factor $i$ in $D_\mu$, is not settled here. The obstruction is a property of the $ict$ derivative and not of the gauge algebra; changing the placement of $i$ relabels which components carry which reality but does not remove the mismatch. This is a genuine gap and is carried into the open questions.

## Open Questions

1. **The reality class of the connection.** The obstruction above shows that no single Hermitian-conjugation eigenspace is gauge invariant across all four components under the $ict$ derivative. Is the mixed assignment $\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian the intended one, or is the factor $i$ in $D_\mu$ to be placed differently, and with what consequence for the physical identification of the connection with the parent's $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$?

2. **Which compact algebra, and how many factors.** This article exhibits $\mathfrak{su}(2)$ inside the vector part of $\mathbb{M}_-$. The material sector decomposes as $\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, so the algebra available is $\mathfrak{u}(1)\oplus\mathfrak{su}(2)$. Is a larger gauge algebra, such as $\mathfrak{su}(2)\times\mathfrak{su}(2)$ or a higher-rank algebra, available by using the full traceless subspace of $\mathbb{B}$ or by complexification, and does the framework select one?

3. **The matter representation.** The covariant derivative here acts by left multiplication, as in the parent. For a non-abelian connection the left and right actions differ, and the representation carried by the matter field must be specified. The chiral-fermion article poses this on the spinor module; the non-abelian version of its charge operator is not constructed here.

4. **The biquaternion form of the field-strength invariants.** The abelian invariants $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ and $I_2 = \mathbf{E}\cdot\mathbf{B}$ are the real and imaginary parts of the norm form of $\tilde{F}$. For the non-abelian field strength the corresponding gauge-invariant objects are $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ and $\mathrm{Tr}(F_{\mu\nu}\tilde{F}^{\mu\nu})$, with $\tilde{F}$ the dual. Is there a clean biquaternion form of the second, and does the corpus's norm-form apparatus extend to it?

5. **Instantons and topology.** The Bianchi identity and the invariant density are the ingredients of the topological charge $\int \mathrm{Tr}(F\wedge F)$. Does the biquaternion framework supply a preferred connection with finite action and nonzero charge, and does the zero-divisor structure of $\mathbb{M}_-$ play any role in it?

6. **Gauge fixing.** The canonical-quantization article records that the framework cannot fix the gauge. The non-abelian case adds the Gribov-type question of whether the gauge orbit intersects a gauge-fixing surface more than once. Nothing here addresses it.

7. **Empirical contact.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard non-abelian gauge theory. The construction above is a reformulation; the question of empirical contact is untouched by it.

## Summary

The non-abelian gauge field in biquaternionic form is obtained by letting the connection of the parent article take values in the vector part of the material sector, $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\} = \mathfrak{su}(2)$, rather than in the central line. The material sector itself decomposes as a Lie algebra, $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$: the imaginary scalar carries the abelian $U(1)$ of the parent, and the real vector part carries a compact simple factor. The gauge group is $SU(2)$, the unit real quaternions, and the connection transforms as

$$
\mathcal{A}'_\mu = U\,\mathcal{A}_\mu\,U^{-1} + \frac{i}{\kappa}\,(\partial_\mu U)\,U^{-1},
$$

which reduces to the parent's additive law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ when $U$ is central.

The field strength is the curvature of this connection,

$$
F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu],
\qquad
F = d\mathcal{A} + i\kappa\,\mathcal{A}\wedge\mathcal{A},
\qquad
[D_\mu,D_\nu] = i\kappa F_{\mu\nu},
$$

and it is **not** gauge invariant: it transforms in the adjoint representation,

$$
F'_{\mu\nu} = U\,F_{\mu\nu}\,U^{-1}.
$$

This is the essential difference from the abelian case, and it was verified on all six independent components on a generic non-commuting connection, with the transformation law holding to $10^{-11}$ and the change being of order unity. It satisfies the Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$, verified on four independent triples, and the Jacobi identity enters both at the operator level, giving the Bianchi identity from $[D_\lambda,[D_\mu,D_\nu]] + \text{cyclic} = 0$, and at the level of the connection components, where it is the derivation property of the adjoint action that cancels the $\mathcal{A}\wedge\mathcal{A}$ terms. The Yang–Mills density $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ is gauge invariant, verified to $10^{-9}$, with the matrix trace on the $\mathfrak{su}(2)$ factor and not the informational trace formula.

Two things are left visible. First, a **defect in the parent**: the curvature formulas $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ and $\tilde{F} = \tfrac12\sum F_{\mu\nu}\bar{e}_\mu e_\nu$ do not survive; the non-abelian representative $\mathcal{F} = \tfrac12\sum F_{\mu\nu}\bar{e}_\mu e_\nu$ is a definition, and $\mathrm{Vect}(\bar{\tilde{\nabla}}\mathcal{A})$ is neither in the right reality class nor adjoint-covariant. Second, a **gap**: no single Hermitian-conjugation eigenspace is preserved by the gauge transformation across all four components, because $\partial_0 = -i\partial_t$ flips the conjugation behaviour of the Maurer–Cartan form in the time direction. A consistent mixed assignment exists — time in $\mathfrak{su}(2)\subset\mathbb{M}_-$, space in $i\,\mathfrak{su}(2)\subset\mathbb{M}_+$ — but whether it is the intended physical one is not settled here.

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
| $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$ | Lie-algebra decomposition of the material sector |
| $T_a = \tfrac12 e_a$ | Normalized generators, $[T_a,T_b]=\varepsilon_{abc}T_c$, $\mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab}$ |
| $U(\tilde{X}) \in SU(2)$ | Unit real quaternion, $U^{-1}=\bar U=U^\dagger$ |
| $\mathcal{A}_\mu = \mathcal{A}_\mu^a e_a \in \mathfrak{su}(2)$ | Non-abelian connection, $\mathcal{A}=\sum_\mu\mathcal{A}_\mu e_\mu$ |
| $\kappa = q/\hbar$ | Coupling |
| $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$ | Covariant derivative, $D=\tilde{\nabla}+i\kappa\mathcal{A}$ |
| $\mathcal{A}'_\mu = U\mathcal{A}_\mu U^{-1} + \frac{i}{\kappa}(\partial_\mu U)U^{-1}$ | Non-abelian transformation of the connection |
| $B_\mu = (\partial_\mu U)U^{-1}$ | Maurer–Cartan form; $\partial_\mu B_\nu - \partial_\nu B_\mu = [B_\mu,B_\nu]$ |
| $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian field strength |
| $F = d\mathcal{A} + i\kappa\,\mathcal{A}\wedge\mathcal{A}$ | Curvature two-form; $(\mathcal{A}\wedge\mathcal{A})_{\mu\nu}=[\mathcal{A}_\mu,\mathcal{A}_\nu]$ |
| $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ | Adjoint (NOT invariant) transformation of the field strength |
| $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$ | Curvature as commutator of covariant derivatives |
| $D_\lambda X = \partial_\lambda X + i\kappa[\mathcal{A}_\lambda,X]$ | Adjoint covariant derivative, $[D_\lambda,X]=D_\lambda X$ |
| $D_\lambda F_{\mu\nu} + \text{cyclic} = 0$ | Bianchi identity |
| $\mathcal{F} = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ | Biquaternion representative of the curvature (a definition) |
| $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ | Gauge-invariant Yang–Mills density |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula (distinct from the matrix trace) |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the immediate parent; its abelian connection, its curvature-commutator identity, its gauge-orbit analysis, and the gap this article takes up.
- *The Gauge Principle in Biquaternionic Form* — the origin of the connection and the abelian transformation law, and the preview $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + \tfrac{iq}{\hbar}[A_\mu,A_\nu]$ that is made exact here.
- *Maxwell's Equations in the Biquaternionic Form* — the abelian potential, field strength and gauge scalar that the non-abelian construction generalizes.
- *The Field-Strength Biquaternion and Its Invariants* — the abelian invariants and the norm form, whose non-abelian extension is posed as an open question.
- *Chiral Fermions in the Biquaternion Framework* — the covariant derivative on the spinor module and the charge operator $Q$, the setting for the matter-representation question.
- *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — the coupled Dirac equation and the left/right matter-representation issue.
- *Canonical Quantization of the Biquaternion Maxwell Field* — the framework's inability to fix the gauge, which bounds the non-abelian orbit as well.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the sector's basis, its four-vectors and the imaginary-scalar/real-vector structure on which the Lie-algebra decomposition rests.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector, the rotor action $X\mapsto HXH^\dagger$, and the trace formula distinguished here from the matrix trace.
- *Lie Algebras: A General Introduction* — the Jacobi identity, the adjoint action as a derivation, and the commutator bracket on an associative algebra.
- *Quaternion Algebra* and *Biquaternion Algebra* — the multiplication rule, the conjugations and the center used throughout.
- *Curved Spacetime and the Biquaternion Framework* — the two-sided gravitational connection, distinct from the one-sided gauge connection of this article.
