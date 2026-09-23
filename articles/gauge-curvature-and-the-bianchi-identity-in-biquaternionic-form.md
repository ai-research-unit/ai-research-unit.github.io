# __Gauge Curvature and the Bianchi Identity in Biquaternionic Form__

## Introduction

The companion article *The Covariant Derivative and Gauge Connection in Biquaternionic Form* recorded the identity $[D_\mu, D_\nu] = \tfrac{iq}{\hbar}F_{\mu\nu}$ in the abelian sector and closed by naming the biquaternion form of that identity as the subject of a planned companion. The companion *Non-Abelian Gauge Fields in Biquaternionic Form* let the connection take values in the vector part of the material sector, $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\} = \mathfrak{su}(2)$, and recorded in a single section that the curvature is the commutator of covariant derivatives and that the Bianchi identity follows from the Jacobi identity. This article takes those two statements as its whole subject and develops them.

Two structural claims organise it.

- **The curvature is the failure of covariant derivatives to commute, and the commutator reduces to the algebra.** The object $[D_\mu,D_\nu]$ is a priori a commutator of first-order differential operators — equivalently, in a matrix representation, a commutator of matrices acting on a module. It is not an element of $\mathbb{B}$; the operators $D_\mu$ are not either. The content is that the commutator is first order with *no derivative at all*: it is multiplication by the single element $i\kappa F_{\mu\nu}$ of $\mathbb{B}$, whose non-abelian part is the algebra commutator $[\mathcal{A}_\mu,\mathcal{A}_\nu]$. An infinite-dimensional operator commutator localises on the finite-dimensional algebra. That is the reduction.
- **The Bianchi identity is a Jacobi identity.** The covariant derivatives are operators in an associative algebra, so they satisfy the Jacobi identity identically. Substituting the curvature identity into that Jacobi identity produces the Bianchi identity. This is not an analogy; it is a substitution, and the substitution is carried out below, not asserted.

The division between what is established and what is interpretation is kept explicit.

- **Established, and recomputed below.** The identity $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ with $F_{\mu\nu}$ a definite element of the algebra; that the commutator is zeroth order (multiplication); the antisymmetry $F_{\mu\nu}=-F_{\nu\mu}$; the Bianchi identity $D_\lambda F_{\mu\nu}+D_\mu F_{\nu\lambda}+D_\nu F_{\lambda\mu}=0$; its identification with the operator Jacobi identity; and the algebraic Jacobi identity used in the coordinate proof. All were recomputed exactly on $\mathfrak{su}(2)$ with generic non-commuting, position-dependent connections, on all index pairs and all index triples, and on two independent random families. The abelian case was also recomputed, and is reported as *not* evidence.
- **Scope limitation, reported rather than smoothed over.** The reduction "operator commutator $=$ algebra element" is exact. The stronger reading "the curvature *is* a single algebra commutator" is not: $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ contains the exterior-derivative term, which is not a commutator of algebra elements. It is a single commutator of the connection components only when the curl $\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu$ vanishes. This is stated where it arises and carried into the open questions.
- **Inherited, and not settled here.** The reality class of the connection in the $ict$ direction, and which compact gauge algebra the framework selects, are taken unchanged from the non-abelian article; nothing here resolves them.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The abelian potential and field strength are $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ and $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$. The gauge algebra of this article is the vector part of the material sector,
$$
\mathfrak{su}(2) = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\} \subset \mathbb{M}_-, \qquad [e_a,e_b] = 2\,\varepsilon_{abc}\,e_c,
$$
with normalised generators $T_a = \tfrac12 e_a$ obeying $[T_a,T_b] = \varepsilon_{abc}T_c$ and $\mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}$. The coupling is $\kappa = q/\hbar$, the indices are $\mu,\nu,\lambda \in \{0,1,2,3\}$ with $\partial_0 = \partial_{ict} = -i\partial_t$, so that $\partial_\mu = \partial_{x_\mu}$ raises and lowers no index and the sum $\sum_\mu$ is the Lorentz-invariant contraction. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged; the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$ is a different pairing and is not it. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum speed of light.

## The Covariant Derivative and the Curvature It Defines

Let the connection be a one-form with values in the compact factor of the material sector,
$$
\mathcal{A}_\mu(\tilde{X}) = \mathcal{A}_\mu^{a}(\tilde{X})\,e_a \in \mathfrak{su}(2), \qquad
\mathcal{A} = \sum_{\mu=0}^{3}\mathcal{A}_\mu\,e_\mu ,
$$
with real coefficient functions, and let the covariant derivative act on a matter field by left multiplication,
$$
D_\mu = \partial_\mu + i\kappa\,\mathcal{A}_\mu, \qquad
D_\mu\Psi = \partial_\mu\Psi + i\kappa\,\mathcal{A}_\mu\Psi ,
\qquad \kappa = \frac{q}{\hbar}.
$$
This is the formal statement of the connection, before any reality condition is imposed; the obstruction to a single Hermitian-conjugation eigenspace across all four components, a property of the $ict$ derivative and not of the gauge algebra, is inherited unchanged from the companion and is carried as open question 3 below.
This is the one-sided, non-abelian connection of the companion article; its transformation law under a local $U(\tilde{X}) \in SU(2)$ is
$$
\mathcal{A}'_\mu = U\,\mathcal{A}_\mu\,U^{-1} + \frac{i}{\kappa}\,(\partial_\mu U)\,U^{-1},
$$
and the curvature is defined, as in the abelian case, by the commutator of covariant derivatives.

**Computation.** The commutator of two components is
$$
[D_\mu,D_\nu]
= [\partial_\mu + i\kappa\mathcal{A}_\mu,\;\partial_\nu + i\kappa\mathcal{A}_\nu]
= i\kappa\left(\partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu\right) + (i\kappa)^2[\mathcal{A}_\mu,\mathcal{A}_\nu].
$$
The second-order terms $\partial_\mu\partial_\nu$ cancel because partial derivatives commute, and the two remaining terms combine, using $(i\kappa)^2 = i\kappa\cdot i\kappa$, into the single algebra element
$$
\boxed{\;[D_\mu,D_\nu] = i\kappa\,F_{\mu\nu}\;},
\qquad
F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa\,[\mathcal{A}_\mu,\mathcal{A}_\nu] \in \mathfrak{su}(2)\oplus i\,\mathfrak{su}(2) = \mathfrak{sl}(2,\mathbb{C}).
$$
Acting on any field, $[D_\mu,D_\nu]\Psi = i\kappa\,F_{\mu\nu}\Psi$. The commutator of the two first-order operators is therefore not a second-order operator and not even a first-order one: it has no derivative at all. It is **multiplication by an element of the finite-dimensional algebra** $\mathbb{B}$. This was recomputed exactly on generic non-commuting, position-dependent connections, for all six independent index pairs, with the residual identically zero; and the zeroth-order character was checked separately by verifying $[D_\mu,D_\nu](f\Psi) = f\,[D_\mu,D_\nu]\Psi$ for an arbitrary scalar function $f$.

Two immediate properties fix the index structure.

- **Antisymmetry.** $F_{\mu\nu} = -F_{\nu\mu}$, because both the derivative terms and the algebra commutator are antisymmetric in $\mu\nu$. The curvature is a two-form index pair carrying one adjoint (algebra) index; it is not a collection of independent numbers, and the antisymmetry is the statement that only six of the sixteen components are independent.
- **The non-abelian term is the whole of the difference.** In the abelian case the connection coefficients are central, $[\mathcal{A}_\mu,\mathcal{A}_\nu]=0$, the algebra element collapses to the curl $\partial_\mu A_\nu-\partial_\nu A_\mu$, and the curvature is a number evaluated at each point. Here the bracket survives and is an algebra element. Every non-abelian feature of the curvature is downstream of that one term.

## The Curvature as an Algebra Element, Not a Matrix Commutator

The identity $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ is where the framework's reading of the curvature lives, and it is worth separating what is reduced from what is not.

**What is reduced.** A commutator of two covariant derivatives is, before the computation, an operator: an element of the algebra of differential operators acting on fields, or — in a matrix representation $\mathbb{B}\cong M_2(\mathbb{C})$ — a matrix commutator of differential-operator-valued matrices. The computation shows that it closes back into $\mathbb{B}$ itself: it equals left multiplication by $i\kappa F_{\mu\nu}$, with $F_{\mu\nu}$ built from the algebra product. In this precise sense the curvature is a **commutator of the algebra** rather than a matrix commutator: the non-commutativity that the curvature measures is the non-commutativity of $\mathbb{B}$ under its own product, $[\mathcal{A}_\mu,\mathcal{A}_\nu]$, and no structure external to the algebra is required to express it.

**What is not reduced.** The curvature element itself is
$$
F_{\mu\nu} = \underbrace{\partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu}_{\text{abelian curl}} + i\kappa\underbrace{[\mathcal{A}_\mu,\mathcal{A}_\nu]}_{\text{algebra commutator}} .
$$
The first term is an exterior derivative, not a commutator of two algebra elements, so $F_{\mu\nu}$ is *not in general a single algebra commutator of the connection components*. It is a single commutator only when the first term vanishes, which happens in particular for a connection that is constant in $\tilde{X}$. In that case
$$
\mathcal{A}_\mu = \text{const} \quad\Longrightarrow\quad F_{\mu\nu} = i\kappa\,[\mathcal{A}_\mu,\mathcal{A}_\nu],
$$
a single algebra commutator, and one can compute it in closed form. For
$$
\mathcal{A}_1 = e_1+e_2, \qquad \mathcal{A}_2 = e_2+e_3, \qquad \mathcal{A}_3 = e_3+e_1,
$$
the rule $[e_a,e_b]=2\varepsilon_{abc}e_c$ gives
$$
F_{12} = i\left([e_1,e_2]+[e_1,e_3]+[e_2,e_3]\right)
= i\left(2e_3 - 2e_2 + 2e_1\right) = 2i\left(e_1 - e_2 + e_3\right),
$$
a genuinely non-abelian curvature, nonzero and non-central. The reduction to a single commutator is exact here; for a position-dependent connection it is not, and the honest statement is the operator-level one: **the operator commutator is multiplication by the single element $i\kappa F_{\mu\nu}$**, while the element $F_{\mu\nu}$ is the sum of a curl and a commutator. This is carried into the open questions as a scope limitation, not hidden.

**The curvature is not gauge invariant.** Under $\mathcal{A}_\mu \mapsto \mathcal{A}'_\mu$ with the transformation law above, direct computation gives the adjoint law
$$
F'_{\mu\nu} = U\,F_{\mu\nu}\,U^{-1},
$$
which was verified both for an infinitesimal local $U = e_0 + \varepsilon g$ with $g\in\mathfrak{su}(2)$ and for a finite constant $SU(2)$ element; in each case the residual vanished exactly. The trace $\mathrm{Tr}(F_{\mu\nu})$ is invariant — here it vanishes identically, since $\mathfrak{sl}(2,\mathbb{C})$ elements are traceless — but the component is not: it is rotated by the group, and only gauge-invariant polynomials in $F$ are observables. Here and below $\mathrm{Tr}$ is the matrix trace on the $\mathfrak{su}(2)$ factor, not the informational trace formula.

## The Covariant Derivative on the Curvature: Two-Sided, Not One-Sided

The curvature carries two gauge indices — in the matrix representation, two matrix indices — and the group acts on them two-sidedly, by conjugation. The same is true of the covariant derivative acting on the curvature: because $F_{\mu\nu}$ is an algebra element in the adjoint representation, and not a matter field in the defining representation, its covariant derivative is not the left multiplication used above.

For any algebra-valued field $X(\tilde{X})$, define
$$
D_\lambda X = \partial_\lambda X + i\kappa\,[\mathcal{A}_\lambda, X],
$$
which is the same as the operator commutator,
$$
[D_\lambda, X] = D_\lambda X ,
$$
where on the left $X$ is understood as multiplication by the algebra element $X$. The bracket is a **commutator**, $\mathcal{A}_\lambda X - X\mathcal{A}_\lambda$: the action is two-sided in the two matrix indices of $X$, and it cannot be collapsed to a one-sided multiplication. This is the first of the traps this article guards against, and the two actions are genuinely different:

$$
\underbrace{D_\mu\Psi = \partial_\mu\Psi + i\kappa\,\mathcal{A}_\mu\Psi}_{\text{matter field: one-sided (left)}},
\qquad
\underbrace{D_\lambda X = \partial_\lambda X + i\kappa\,[\mathcal{A}_\lambda, X]}_{\text{adjoint-valued curvature: two-sided}} .
$$

The distinction is not cosmetic. Replacing the two-sided covariant derivative of the curvature by the one-sided $\partial_\lambda F_{\mu\nu} + i\kappa\,\mathcal{A}_\lambda F_{\mu\nu}$ destroys the Bianchi identity: on a generic non-commuting connection the resulting cyclic sum is nonzero and of order unity, while the correct two-sided sum vanishes. This was checked as a negative control, not assumed.

Finally, this gauge connection must not be confused with the gravitational connection of the corpus. The gauge connection is **one-sided**: it acts on matter by left multiplication, and on the adjoint-valued curvature by the commutator. The gravitational connection of *Curved Spacetime and the Biquaternion Framework* is **two-sided in a different sense**,
$$
D_\mu\tilde{X} = \partial_\mu\tilde{X} + \tilde{\Gamma}_\mu\tilde{X} + \tilde{X}\tilde{\Gamma}_\mu^\dagger ,
$$
because the infinitesimal Lorentz action on $\mathbb{M}_-$ is $G\tilde{X} + \tilde{X}G^\dagger$, not the commutator; the two differ precisely for the boosts. The gauge connection lives in $\mathfrak{su}(2)\subset\mathbb{M}_-$ and is one-sided; the gravitational connection lives in the six-dimensional traceless subspace and is two-sided. They share a name and nothing else, and no relation between them is asserted.

## The Bianchi Identity

The field strength is built from the connection by differentiation, so it cannot be arbitrary: it satisfies a differential identity. With the adjoint covariant derivative defined above, the **Bianchi identity** is

$$
D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0
\qquad \text{for all } (\lambda,\mu,\nu).
$$

The cyclic order is part of the statement, so it is worth writing out in full:

$$
\partial_\lambda F_{\mu\nu} + i\kappa[\mathcal{A}_\lambda,F_{\mu\nu}]
\;+\;
\partial_\mu F_{\nu\lambda} + i\kappa[\mathcal{A}_\mu,F_{\nu\lambda}]
\;+\;
\partial_\nu F_{\lambda\mu} + i\kappa[\mathcal{A}_\nu,F_{\lambda\mu}]
= 0 .
$$

The derivative index is paired with the form pair whose first index is the same index, and the three terms are the cyclic rotations of $(\lambda,\mu,\nu)$ applied to both the derivative index and the pair at once. The order matters: the sum $D_\lambda F_{\mu\nu}+D_\mu F_{\lambda\nu}+D_\nu F_{\mu\lambda}$, in which the second and third pairs are not the cyclic rotations, is generically nonzero, and was checked as a negative control. The cyclic sum is totally antisymmetric in the three indices, so contraction with the totally antisymmetric symbol gives the compact form

$$
\varepsilon^{\lambda\mu\nu\rho}\,D_\lambda F_{\mu\nu} = 0 .
$$

The identity was recomputed for all $64$ ordered triples $(\lambda,\mu,\nu)$, on generic non-commuting, position-dependent connections, with residual identically zero.

## The Bianchi Identity as the Jacobi Identity

The derivation is short and complete, and the point is to display each substitution rather than name the result.

For any three operators $X,Y,Z$ in an associative algebra, the Jacobi identity holds:

$$
[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0 ,
$$

as a consequence of the associativity of composition, $(XY)Z = X(YZ)$. This is an identity of the *operator* algebra, and it applies to the covariant derivatives because they are operators. Take $X = D_\lambda$, $Y = D_\mu$, $Z = D_\nu$:

$$
[D_\lambda,[D_\mu,D_\nu]] + [D_\mu,[D_\nu,D_\lambda]] + [D_\nu,[D_\lambda,D_\mu]] = 0 .
$$

Now substitute the two identities established above, term by term:

$$
[D_\mu,D_\nu] = i\kappa\,F_{\mu\nu},
\qquad
[D_\lambda, F_{\mu\nu}] = D_\lambda F_{\mu\nu}.
$$

The first turns each inner commutator into multiplication by $i\kappa F$; the second is the definition of the adjoint covariant derivative. Therefore

$$
[D_\lambda,[D_\mu,D_\nu]]
= [D_\lambda, i\kappa F_{\mu\nu}]
= i\kappa\,[D_\lambda,F_{\mu\nu}]
= i\kappa\,D_\lambda F_{\mu\nu},
$$

and the operator Jacobi identity becomes

$$
i\kappa\left(D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu}\right) = 0 ,
$$

which is the Bianchi identity. This is the identification the title promises, and it is a substitution, not an analogy: **the Bianchi identity is the Jacobi identity of the operator algebra, with the curvature identity substituted into it.** The substitution was verified exactly on generic non-commuting connections for all independent triples: the operator Jacobi sum is $i\kappa$ times the Bianchi cyclic sum, term by term.

## Where Each Identity Enters: Operator Jacobi and Algebra Jacobi

There are two distinct Jacobi identities in this story, at two different levels, and conflating them hides the structure.

**Operator level.** The identity just used,
$$
[D_\lambda,[D_\mu,D_\nu]] + [D_\mu,[D_\nu,D_\lambda]] + [D_\nu,[D_\lambda,D_\mu]] = 0 ,
$$
is exact for arbitrary operators. It uses only associativity of operator composition; it does not use the compactness, the reality, or even the Lie-algebra character of the connection components. Given the curvature identity, it produces the Bianchi identity with no further input.

**Algebra level.** The coordinate route to the same identity differentiates $F$ and applies $D_\lambda$. Its terms group into three classes, and each class is killed by a different mechanism. Writing only the cyclic sum $D_\lambda F_{\mu\nu}+D_\mu F_{\nu\lambda}+D_\nu F_{\lambda\mu}$, the classes are:

- the **second-derivative terms** $\partial_\lambda\partial_\mu\mathcal{A}_\nu - \partial_\lambda\partial_\nu\mathcal{A}_\mu + \text{cyclic}$, which vanish because partial derivatives commute;
- the **derivative-of-commutator terms** $\partial_\lambda[\mathcal{A}_\mu,\mathcal{A}_\nu] + \text{cyclic}$ together with $[\mathcal{A}_\lambda,\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu] + \text{cyclic}$, which cancel in pairs by the Leibniz rule for the bracket — the derivative of a bracket is the sum of the brackets of the derivatives;
- the **nested commutators** $[\mathcal{A}_\lambda,[\mathcal{A}_\mu,\mathcal{A}_\nu]] + \text{cyclic}$, which vanish by the **algebra Jacobi identity**
$$
[\mathcal{A}_\lambda,[\mathcal{A}_\mu,\mathcal{A}_\nu]] + [\mathcal{A}_\mu,[\mathcal{A}_\nu,\mathcal{A}_\lambda]] + [\mathcal{A}_\nu,[\mathcal{A}_\lambda,\mathcal{A}_\mu]] = 0 .
$$

These three classes were separated and each was verified to vanish on generic connections, with the reconstruction of the full cyclic sum from them checked as well. The algebraic Jacobi identity is the statement, in *Lie Algebras: A General Introduction*, that makes the adjoint action $\mathrm{ad}_u = [u,\cdot]$ a derivation of the bracket,
$$
\mathrm{ad}_u[v,w] = [\mathrm{ad}_u v, w] + [v, \mathrm{ad}_u w],
$$
and it is that derivation property — equivalently the Leibniz rule for $D_\lambda$ acting on a bracket — that makes the middle class cancel. It is the genuinely non-abelian ingredient: the abelian case lacks it because it lacks the bracket altogether.

The two Jacobi identities are not the same statement. The operator identity is associativity of composition and is sufficient, on its own, to turn the curvature identity into the Bianchi identity; the algebra identity is the Lie-algebra axiom that controls the coordinate proof. Both are exact, and both are used, at their own level.

## Explicit Verification on a Non-Abelian Connection

Everything above was checked by explicit substitution on $\mathfrak{su}(2)$ with the non-commuting generators $e_1,e_2,e_3$ and the rule $[e_a,e_b]=2\varepsilon_{abc}e_c$, on connections with generic real polynomial coefficients in all four components. The following were confirmed.

- **The reduction.** $[D_\mu,D_\nu]\Psi = i\kappa F_{\mu\nu}\Psi$ for all six independent index pairs, and the commutator is zeroth order, $[D_\mu,D_\nu](f\Psi) = f[D_\mu,D_\nu]\Psi$.
- **The Bianchi identity.** The cyclic sum vanishes identically for all $64$ ordered triples, with individual terms of order unity, so the vanishing is a genuine cancellation and not a sum of zeros.
- **The Jacobi identification.** The operator Jacobi sum equals $i\kappa$ times the Bianchi cyclic sum identically, and the three term classes of the coordinate proof (second derivatives, derivative-of-commutator, nested commutators) each vanish for the stated reason.
- **The non-vacuity controls.** The wrong cyclic order is generically nonzero; the one-sided replacement $\partial_\lambda F_{\mu\nu}+i\kappa\mathcal{A}_\lambda F_{\mu\nu}$ gives a generically nonzero cyclic sum; and $F_{\mu\nu}$ differs from $i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ for position-dependent connections.

The checks were run on two independent random families with different seeds, over all index pairs and all index triples, precisely so that the identity is not verified only on the case that suggested it. A concrete constant-connection display makes the structure visible. For

$$
\mathcal{A}_1 = e_1+e_2, \qquad \mathcal{A}_2 = e_2+e_3, \qquad \mathcal{A}_3 = e_3+e_1,
$$

one has $F_{12}=2i(e_1-e_2+e_3)$, $F_{23}=2i(e_1+e_2-e_3)$, and $F_{31}=2i(-e_1+e_2+e_3)$. The three Bianchi terms for the triple $(1,2,3)$ are each nonzero — for instance $D_1F_{23}$ has entries of magnitude $4\sqrt2$ — while their sum is the zero matrix, and the algebraic ancestor $[[\mathcal{A}_1,\mathcal{A}_2],\mathcal{A}_3] + \text{cyclic}$ is likewise the zero matrix. The constant case is where the Bianchi identity is *literally* the algebra Jacobi identity, because the derivative of $F$ vanishes and $D_\lambda F_{\mu\nu} = i\kappa[\mathcal{A}_\lambda,F_{\mu\nu}] = -\kappa^2[\mathcal{A}_\lambda,[\mathcal{A}_\mu,\mathcal{A}_\nu]]$.

## The Abelian Case Is Not Evidence

If all the connection coefficients are central — $\mathcal{A}_\mu = a_\mu e_0$ with complex scalar functions $a_\mu$ — then $[\mathcal{A}_\mu,\mathcal{A}_\nu]=0$, the curvature reduces to $F_{\mu\nu} = \partial_\mu a_\nu - \partial_\nu a_\mu$, the adjoint covariant derivative reduces to the ordinary one, and the Bianchi identity becomes

$$
\partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0 ,
$$

which is automatic: it is $dF = d^2a = 0$, and it holds because $F$ is a curl, not because of any bracket. The individual terms are nonzero, but the sum vanishes by the symmetry of mixed partial derivatives, and no commutator term is present at all.

The abelian check therefore passes for a reason unrelated to the non-abelian statement, and **passing it is not evidence**. It was confirmed that the abelian case is trivially zero, and it is reported here for the opposite purpose — to mark the boundary of what the non-abelian verification shows. The evidence for the non-abelian identity is the non-commuting, position-dependent family of the previous section, where the commutator term is nonzero and the individual Bianchi terms cancel against each other only by the Jacobi structure.

## Can One Biquaternion Equation Carry the Bianchi Identity?

The gauge principle article left open "the sense in which a single biquaternion equation carries" the Bianchi identity, and the covariant-derivative article recorded the negative result that the one-line equation $\tilde{\nabla}\tilde{F}=0$ is the full source-free Maxwell system and not the Bianchi identity. That negative result is confirmed here by recomputation, and the reason is visible.

For the abelian field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H} = \mathbf{F} = \sum_k F_k e_k$, direct computation with the quaternion product gives the exact identities

$$
\bar{\tilde{\nabla}}\tilde{F}
= \mathrm{div}(\mathbf{F})\,e_0 + \partial_0\mathbf{F} - \mathrm{curl}\,\mathbf{F},
\qquad
\tilde{\nabla}\tilde{F}
= -\mathrm{div}(\mathbf{F})\,e_0 + \partial_0\mathbf{F} + \mathrm{curl}\,\mathbf{F},
$$

where $\mathbf{F} = \sum_k F_k e_k$ and $\mathrm{div},\mathrm{curl}$ are the three-dimensional operators acting on the coefficient triple, each exactly as displayed, with no residual. The zero set of either equation is eight real equations: a scalar constraint, which for $\tilde{\nabla}\tilde{F}=0$ reads $\mathrm{div}\,\mathbf{E} = 0$ and $\mathrm{div}\,\mathbf{H} = 0$, together with the six real components of a vector equation, $\partial_0\mathbf{F} = -\mathrm{curl}\,\mathbf{F}$. The Bianchi identity in the abelian sector, by contrast, is the four real equations $\mathrm{div}\,\mathbf{B} = 0$ and $\partial_t\mathbf{B} + \mathrm{curl}\,\mathbf{E} = 0$. Eight equations are not four, and the scalar constraint has no counterpart in a three-index antisymmetric identity; the parent's negative result — that the one-line equation $\tilde{\nabla}\tilde{F}=0$ is the source-free field system and not the Bianchi identity — therefore stands, and the recomputation here confirms the structural reason rather than merely inheriting the verdict.

The structural reason is that the Bianchi identity is a three-index antisymmetric statement — a $3$-form — whereas a biquaternion product of the gradient (one index) with the curvature (a two-index algebra element) contracts its indices through the algebra, producing the scalar and vector combinations displayed above rather than the cyclic sum over three distinct indices. Contracting the Bianchi identity with the totally antisymmetric symbol does convert it into a four-component vector equation, $\varepsilon^{\lambda\mu\nu\rho}D_\lambda F_{\mu\nu} = 0$, which one may then package as a biquaternion $\tilde{B} = \sum_\rho (\varepsilon^{\lambda\mu\nu\rho}D_\lambda F_{\mu\nu})\,e_\rho = 0$. But the antisymmetric symbol is extra structure: it is not contained in the algebra product, and this is a rewriting of the four contracted equations rather than an algebra-intrinsic one-line Bianchi. **This is a gap, and it is recorded as one:** the framework does not, without extra structure, supply a single biquaternion equation carrying the Bianchi identity.

## Open Questions

1. **The single-biquaternion Bianchi.** The gap above is the sharpest open question of this article. Is there an algebra-intrinsic operation — a projection or a product with the conjugate gradient — that extracts the cyclic three-index sum from a biquaternion expression, or is the antisymmetric symbol genuinely required? The parent's negative result for $\bar{\tilde{\nabla}}\tilde{F}$ and the recomputed forms of both products suggest the latter, but neither settles it.

2. **The curvature as one commutator.** The reduction "$[D_\mu,D_\nu] = $ multiplication by $i\kappa F_{\mu\nu}$" is exact, but $F_{\mu\nu}$ itself is a curl plus a commutator, and is a single algebra commutator only when the curl $\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu$ vanishes. Is there a gauge-covariant way to write the full $F_{\mu\nu}$ as a single commutator of algebra-valued objects, or is the split into curl and commutator intrinsic?

3. **The reality class of the connection.** Inherited from the non-abelian article, unchanged: because $\partial_0 = -i\partial_t$, no single Hermitian-conjugation eigenspace is preserved by the gauge transformation across all four components, and the consistent mixed assignment (time in $\mathfrak{su}(2)\subset\mathbb{M}_-$, space in $i\,\mathfrak{su}(2)\subset\mathbb{M}_+$) is not shown to be the intended one.

4. **Which compact gauge algebra.** Also inherited: the framework exhibits $\mathfrak{su}(2)$ in the vector part of $\mathbb{M}_-$, and the material sector decomposes as $\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$. Whether a larger compact algebra is available, and which the framework selects, is open.

5. **The matter representation.** The covariant derivative here acts on matter by left multiplication and on the curvature by the commutator. For a non-abelian connection the left and right actions on a matter field differ, and which representation the matter field carries is not fixed here.

6. **Topological charge.** The Bianchi identity and the invariant density are the ingredients of the topological charge $\int\mathrm{Tr}(F\wedge F)$. Whether this requires the antisymmetric symbol as extra structure, as the packaging discussion suggests, and what the biquaternion framework supplies for it, is left open.

7. **Empirical contact.** As everywhere in the framework: does any of this yield a prediction distinguishing it from standard non-abelian gauge theory? The construction is a reformulation, and this question is untouched by it.

## Summary

The gauge curvature of the biquaternionic framework is the commutator of covariant derivatives, and the commutator reduces to the algebra. For a connection $\mathcal{A}_\mu \in \mathfrak{su}(2) = \mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{M}_-$ and $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$, with $\kappa = q/\hbar$,

$$
[D_\mu,D_\nu] = i\kappa\,F_{\mu\nu},
\qquad
F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu] \in \mathfrak{su}(2)\oplus i\,\mathfrak{su}(2) = \mathfrak{sl}(2,\mathbb{C}),
$$

and the commutator is zeroth order: it is multiplication by the single algebra element $i\kappa F_{\mu\nu}$. That localisation of an operator commutator onto the finite-dimensional algebra is the content of the reduction, and it was verified exactly on generic non-commuting connections for all index pairs. The curvature is antisymmetric, $F_{\mu\nu}=-F_{\nu\mu}$, and transforms in the adjoint representation, $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$.

Because the curvature is adjoint-valued, its covariant derivative is the two-sided commutator $D_\lambda X = \partial_\lambda X + i\kappa[\mathcal{A}_\lambda,X]$, not the one-sided left multiplication used on a matter field; collapsing the two-sided action to a one-sided one destroys the Bianchi identity. This distinction is separate from, and not to be confused with, the two-sided gravitational connection of the curved-spacetime article.

The Bianchi identity is

$$
D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0 ,
$$

with the cyclic order as displayed, equivalently $\varepsilon^{\lambda\mu\nu\rho}D_\lambda F_{\mu\nu}=0$. It is the **operator Jacobi identity** with the curvature identity substituted into it: $[D_\lambda,[D_\mu,D_\nu]]+\text{cyclic}=0$ becomes $i\kappa(D_\lambda F_{\mu\nu}+\text{cyclic})=0$. In the coordinate proof a second, algebraic Jacobi identity $[\mathcal{A}_\lambda,[\mathcal{A}_\mu,\mathcal{A}_\nu]]+\text{cyclic}=0$ kills the nested-commutator terms, via the derivation property of the adjoint action. Both identities are exact and were verified on $\mathfrak{su}(2)$; the abelian case is trivially zero and is not evidence.

Two things are left visible. First, a **scope limitation**: the curvature is a curl plus an algebra commutator, and is a single algebra commutator only when the curl $\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu$ vanishes. Second, a **gap**: no single biquaternion equation carries the Bianchi identity without extra structure — the recomputed products $\bar{\tilde{\nabla}}\tilde{F} = \mathrm{div}(\mathbf{F})e_0+\partial_0\mathbf{F}-\mathrm{curl}\,\mathbf{F}$ and $\tilde{\nabla}\tilde{F} = -\mathrm{div}(\mathbf{F})e_0+\partial_0\mathbf{F}+\mathrm{curl}\,\mathbf{F}$ each carry a scalar constraint and a vector equation (eight real equations), not the three-index cyclic sum, and the contracted form $\varepsilon^{\lambda\mu\nu\rho}D_\lambda F_{\mu\nu}=0$ requires the antisymmetric symbol.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; center $\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$ | Biquaternionic gradient and its quaternion conjugate |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$ | Commutator on the vector part of $\mathbb{M}_-$ |
| $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$ | Gauge algebra inside $\mathbb{M}_-$ |
| $T_a=\tfrac12 e_a$ | Normalized generators, $[T_a,T_b]=\varepsilon_{abc}T_c$, $\mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab}$ |
| $U(\tilde{X}) \in SU(2)$ | Unit real quaternion, $U^{-1}=\bar U=U^\dagger$ |
| $\mathcal{A}_\mu = \mathcal{A}_\mu^a e_a \in \mathfrak{su}(2)$ | Non-abelian connection, $\mathcal{A}=\sum_\mu\mathcal{A}_\mu e_\mu$ |
| $\kappa = q/\hbar$ | Coupling |
| $D_\mu = \partial_\mu + i\kappa\mathcal{A}_\mu$ | Covariant derivative on matter (one-sided, left) |
| $\partial_0 = \partial_{ict} = -i\partial_t$ | $ict$ time derivative |
| $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Curvature components, antisymmetric |
| $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$ | Curvature as the commutator of covariant derivatives |
| $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$ | Adjoint transformation of the curvature |
| $D_\lambda X = \partial_\lambda X + i\kappa[\mathcal{A}_\lambda,X]$ | Adjoint covariant derivative, $[D_\lambda,X]=D_\lambda X$ |
| $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu}=0$ | Bianchi identity (cyclic order as shown) |
| $\varepsilon^{\lambda\mu\nu\rho}D_\lambda F_{\mu\nu}=0$ | Contracted form of the Bianchi identity |
| $\tilde{F}=i\sqrt{\epsilon}\mathbf{E}-\sqrt{\mu}\mathbf{H}$ | Abelian field-strength biquaternion, $\mathbf{F}=\sum_kF_ke_k$ |
| $\mathrm{div}(\mathbf{F}),\ \mathrm{curl}\,\mathbf{F}$ | Three-dimensional operators on the coefficient triple |
| $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ | Gauge-invariant Yang–Mills density (matrix trace) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula (distinct from the matrix trace) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the immediate parent; its abelian commutator identity $[D_\mu,D_\nu]=\tfrac{iq}{\hbar}F_{\mu\nu}$ and its deferral of the Bianchi identity to this article.
- *Non-Abelian Gauge Fields in Biquaternionic Form* — the non-abelian connection, the transformation law, the adjoint curvature, and the compactness gap this article inherits unchanged.
- *The Gauge Principle in Biquaternionic Form* — the origin of the connection, the covariant derivative, and the curvature; the source of the remark that the homogeneous equations are the Bianchi identity of the connection.
- *The Field-Strength Biquaternion and Its Invariants* — the abelian field strength, its pure-vector character, and the norm-form apparatus that the non-abelian extension does not yet reproduce.
- *Maxwell's Equations in the Biquaternionic Formulation* — the abelian field equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ whose homogeneous part is the Bianchi identity.
- *Lie Algebras: A General Introduction* — the Jacobi identity, the adjoint action as a derivation, and the commutator bracket on an associative algebra.
- *Curved Spacetime and the Biquaternion Framework* — the two-sided gravitational connection $D_\mu\tilde{X}=\partial_\mu\tilde{X}+\tilde{\Gamma}_\mu\tilde{X}+\tilde{X}\tilde{\Gamma}_\mu^\dagger$, distinct from the one-sided gauge connection of this article.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the sector basis, the imaginary-scalar/real-vector structure, and the Lie-algebra decomposition on which the gauge algebra rests.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector and the trace formula distinguished here from the matrix trace.
- *Biquaternion Algebra* and *Quaternion Algebra* — the multiplication rule, the conjugations, and the center used throughout.
