# __Connection Curvature and the Bianchi Identity in Biquaternionic Form__

## Introduction

The companion article *The Covariant Derivative and Connection in Biquaternionic Form* recorded the identity $[D_{\imath}, D_{\jmath}] =i\kappa F_{\imath\jmath}$ in the abelian sector and closed by naming the biquaternion form of that identity as the subject of a planned companion. The companion *Non-Abelian Connections in Biquaternionic Form* let the connection take values in the vector part of the material sector, the real Lie algebra $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, and recorded in a single section that the curvature is the commutator of covariant derivatives and that the Bianchi identity follows from the Jacobi identity. This article takes those two statements as its whole subject and develops them.

Two structural claims organise it.

- **The curvature is the failure of covariant derivatives to commute, and the commutator reduces to the algebra.** The object $[D_{\imath},D_{\jmath}]$ is a priori a commutator of first-order differential operators — equivalently, in a matrix representation, a commutator of matrices acting on a module. It is not an element of $\mathbb{B}$; the operators $D_{\imath}$ are not either. The content is that the commutator is first order with *no derivative at all*: it is multiplication by the single element $i\kappa F_{\imath\jmath}$ of $\mathbb{B}$, whose non-abelian part is the algebra commutator $[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$. An infinite-dimensional operator commutator localises on the finite-dimensional algebra. That is the reduction.
- **The Bianchi identity is a Jacobi identity.** The covariant derivatives are operators in an associative algebra, so they satisfy the Jacobi identity identically. Substituting the curvature identity into that Jacobi identity produces the Bianchi identity. This is not an analogy; it is a substitution, and the substitution is carried out below, not asserted.

The division between what is established and what is interpretation is kept explicit.

- **Established, and recomputed below.** The identity $[D_{\imath},D_{\jmath}]=i\kappa F_{\imath\jmath}$ with $F_{\imath\jmath}$ a definite element of the algebra; that the commutator is zeroth order (multiplication); the antisymmetry $F_{\imath\jmath}=-F_{\jmath\imath}$; the Bianchi identity $D_{k} F_{\imath\jmath}+D_{\imath} F_{\jmath k}+D_{\jmath} F_{k\imath}=0$; its identification with the operator Jacobi identity; and the algebraic Jacobi identity used in the coordinate proof. All were recomputed exactly on $\mathfrak{su}(2)$ with generic non-commuting, position-dependent connections, on all index pairs and all index triples, and on two independent random families. The abelian case was also recomputed, and is reported as *not* evidence.
- **Scope limitation, reported rather than smoothed over.** The reduction "operator commutator $=$ algebra element" is exact. The stronger interpretation "the curvature *is* a single algebra commutator" is not: $F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}+i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$ contains the exterior-derivative term, which is not a commutator of algebra elements. It is a single commutator of the connection components only when the curl $\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}$ vanishes. This is stated where it arises and carried into the open questions.
- **Inherited, and not settled here.** The reality class of the connection in the $i r'_t$ direction, and which compact algebra the framework selects, are taken unchanged from the non-abelian article; nothing here resolves them.

## The Covariant Derivative and the Curvature It Defines

Let the connection be a one-form with values in the compact factor of the material sector,
$$
\mathcal{A}_{\imath}(\tilde{Q}) = \sum_a\mathcal{A}_{\imath a}(\tilde{Q})\,\vec e_a \in \mathfrak{su}(2), \qquad
\mathcal{A} = \sum_{\imath\in\{t,x,y,z\}}\mathcal{A}_{\imath}\,e_{\imath} ,
$$
with real coefficient functions, and let the covariant derivative act on a matter field by left multiplication,
$$
D_{\imath} = \partial/\partial R_{\imath} + i\kappa\,\mathcal{A}_{\imath}, \qquad
D_{\imath}\tilde{Ξ} = \partial/\partial R_{\imath}\,\tilde{Ξ} + i\kappa\,\mathcal{A}_{\imath}\tilde{Ξ} .
$$

The number $\kappa$ is the coupling. It is a parameter of the connection, not something the algebra supplies, and the conversion from a charge to it belongs to the rung where the action quantum is declared.
This is the formal statement of the connection, before any reality condition is imposed; the obstruction to a single Hermitian-conjugation eigenspace across all four components, a property of the $i r'_t$ derivative and not of the algebra, is inherited unchanged from the companion and is carried as open question 3 below.
This is the one-sided, non-abelian connection of the companion article; its transformation law under a local $\tilde U(\tilde{Q}) \in SU(2)$ is
$$
\mathcal{A}_{\mathrm g,\imath} = \tilde U\,\mathcal{A}_{\imath}\,\tilde U^{-1} + \frac{i}{\kappa}\,(\partial/\partial R_{\imath} \tilde U)\,\tilde U^{-1},
$$
and the curvature is defined, as in the abelian case, by the commutator of covariant derivatives.

**Computation.** The commutator of two components is
$$
[D_{\imath},D_{\jmath}]
= [\partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath},\;\partial/\partial R_{\jmath} + i\kappa\mathcal{A}_{\jmath}]
= i\kappa\left(\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}\right) + (i\kappa)^2[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}].
$$
The second-order terms $\partial^2/\partial R_{\imath}\partial R_{\jmath}$ cancel because partial derivatives commute, and the two remaining terms combine, using $(i\kappa)^2 = i\kappa\cdot i\kappa$, into the single algebra element
$$
\boxed{\;[D_{\imath},D_{\jmath}] = i\kappa\,F_{\imath\jmath}\;},
\qquad
F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath} + i\kappa\,[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}] \in \mathfrak{su}(2)\oplus i\,\mathfrak{su}(2) = \mathfrak{sl}(2,\mathbb{C}).
$$

**On the notation.** The direct sum in that display is a decomposition of *real Lie algebras*, not of groups: every traceless complex matrix is anti-Hermitian-traceless plus Hermitian-traceless, and those two spaces are $\mathfrak{su}(2)$ and $i\,\mathfrak{su}(2)$. The second is not a group — it does not contain the identity — so $\mathrm{SU}(2)\oplus i\,\mathrm{SU}(2)$ has no group meaning. Throughout, $\mathfrak{su}(2)$ is the span $\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, which the companion articles write $\mathrm{SU}(2)$; the group of unit quaternions is the separate object $\tilde U$ of the transformation law, and only $\tilde U$ and finite group elements are groups.

Acting on any field, $[D_{\imath},D_{\jmath}]\tilde{Ξ} = i\kappa\,F_{\imath\jmath}\tilde{Ξ}$. The commutator of the two first-order operators is therefore not a second-order operator and not even a first-order one: it has no derivative at all. It is **multiplication by an element of the finite-dimensional algebra** $\mathbb{B}$. This was recomputed exactly on generic non-commuting, position-dependent connections, for all six independent index pairs, with the residual identically zero; and the zeroth-order character was checked separately by verifying $[D_{\imath},D_{\jmath}](f\tilde{Ξ}) = f\,[D_{\imath},D_{\jmath}]\tilde{Ξ}$ for an arbitrary scalar function $f$.

Two immediate properties fix the index structure.

- **Antisymmetry.** $F_{\imath\jmath} = -F_{\jmath\imath}$, because both the derivative terms and the algebra commutator are antisymmetric in $\imath\jmath$. The curvature is a two-form index pair carrying one adjoint (algebra) index; it is not a collection of independent numbers, and the antisymmetry is the statement that only six of the sixteen components are independent.
- **The non-abelian term is the whole of the difference.** In the abelian case the connection coefficients are central, $[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]=0$, the algebra element collapses to the curl $\partial/\partial R_{\imath} A_{\jmath}-\partial/\partial R_{\jmath} A_{\imath}$, and the curvature is a number evaluated at each point. Here the bracket survives and is an algebra element. Every non-abelian feature of the curvature is downstream of that one term.

## The Curvature as an Algebra Element, Not a Matrix Commutator

The identity $[D_{\imath},D_{\jmath}]=i\kappa F_{\imath\jmath}$ is where the framework's interpretation of the curvature lives, and it is worth separating what is reduced from what is not.

**What is reduced.** A commutator of two covariant derivatives is, before the computation, an operator: an element of the algebra of differential operators acting on fields, or — in a matrix representation $\mathbb{B}\cong M_2(\mathbb{C})$ — a matrix commutator of differential-operator-valued matrices. The computation shows that it closes back into $\mathbb{B}$ itself: it equals left multiplication by $i\kappa F_{\imath\jmath}$, with $F_{\imath\jmath}$ built from the algebra product. In this precise sense the curvature is a **commutator of the algebra** rather than a matrix commutator: the non-commutativity that the curvature measures is the non-commutativity of $\mathbb{B}$ under its own product, $[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$, and no structure external to the algebra is required to express it.

**What is not reduced.** The curvature element itself is
$$
F_{\imath\jmath} = \underbrace{\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}}_{\text{abelian curl}} + i\kappa\underbrace{[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]}_{\text{algebra commutator}} .
$$
The first term is an exterior derivative, not a commutator of two algebra elements, so $F_{\imath\jmath}$ is *not in general a single algebra commutator of the connection components*. It is a single commutator only when the first term vanishes, which happens in particular for a connection that is constant in $\tilde{Q}$. In that case
$$
\mathcal{A}_{\imath} = \text{const} \quad\Longrightarrow\quad F_{\imath\jmath} = i\kappa\,[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}],
$$
a single algebra commutator, and one can compute it in closed form. For
$$
\mathcal{A}_1 = \vec e_x+\vec e_y, \qquad \mathcal{A}_2 = \vec e_y+\vec e_z, \qquad \mathcal{A}_3 = \vec e_z+\vec e_x,
$$
the rule $[\vec e_a,\vec e_b]=2\varepsilon_{abc}\vec e_c$ gives
$$
F_{12} = i\left([\vec e_x,\vec e_y]+[\vec e_x,\vec e_z]+[\vec e_y,\vec e_z]\right)
= i\left(2\vec e_z - 2\vec e_y + 2\vec e_x\right) = 2i\left(\vec e_x - \vec e_y + \vec e_z\right),
$$
a genuinely non-abelian curvature, nonzero and non-central. The reduction to a single commutator is exact here; for a position-dependent connection it is not, and the honest statement is the operator-level one: **the operator commutator is multiplication by the single element $i\kappa F_{\imath\jmath}$**, while the element $F_{\imath\jmath}$ is the sum of a curl and a commutator. This is carried into the open questions as a scope limitation, not hidden.

**The curvature is not invariant.** Under $\mathcal{A}_{\imath} \mapsto \mathcal{A}_{\mathrm g,\imath}$ with the transformation law above, direct computation gives the adjoint law
$$
F_{\mathrm g,\imath\jmath} = \tilde U\,F_{\imath\jmath}\,\tilde U^{-1},
$$
which was verified both for an infinitesimal local $\tilde U = e_t + \varepsilon g$ with $g\in\mathfrak{su}(2)$ and for a finite constant group element $\tilde U$; in each case the residual vanished exactly. The trace $\mathrm{Tr}(F_{\imath\jmath})$ is invariant — here it vanishes identically, since the curvature is valued in the derived algebra — but the component is not: it is rotated by the group, and only invariant polynomials in $F$ are observables. Here and below $\mathrm{Tr}$ is the matrix trace on the $\mathrm{SU}(2)$ factor, not the informational pairing formula.

## The Covariant Derivative on the Curvature: Two-Sided, Not One-Sided

The curvature carries two fixing condition indices — in the matrix representation, two matrix indices — and the group acts on them two-sidedly, by conjugation. The same is true of the covariant derivative acting on the curvature: because $F_{\imath\jmath}$ is an algebra element in the adjoint representation, and not a matter field in the defining representation, its covariant derivative is not the left multiplication used above.

For any algebra-valued field $\tilde{Q}$, define
$$
D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa\,[\mathcal{A}_{\imath}, \tilde{Q}],
$$
which is the same as the operator commutator,
$$
[D_{\imath}, \tilde{Q}] = D_{\imath} \tilde{Q} ,
$$
where on the left $\tilde{Q}$ is understood as multiplication by the algebra element $\tilde{Q}$. The bracket is a **commutator**, $\mathcal{A}_{\imath} \tilde{Q} - \tilde{Q}\mathcal{A}_{\imath}$: the action is two-sided in the two matrix indices of $\tilde{Q}$, and it cannot be collapsed to a one-sided multiplication. This is one of the traps this article guards against — the other is the repeated index in the Jacobi substitution — and the two actions are genuinely different:

$$
\underbrace{D_{\imath}\tilde{Ξ} = \partial/\partial R_{\imath}\,\tilde{Ξ} + i\kappa\,\mathcal{A}_{\imath}\tilde{Ξ}}_{\text{matter field: one-sided (left)}},
\qquad
\underbrace{D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa\,[\mathcal{A}_{\imath}, \tilde{Q}]}_{\text{adjoint-valued curvature: two-sided}} .
$$

The distinction is not cosmetic. Replacing the two-sided covariant derivative of the curvature by the one-sided $\partial/\partial R_{\imath} F_{\imath\jmath} + i\kappa\,\mathcal{A}_{\imath} F_{\imath\jmath}$ destroys the Bianchi identity: on a generic non-commuting connection the resulting cyclic sum is nonzero and of order unity, while the correct two-sided sum vanishes. This was checked as a negative control, not assumed.

Finally, this connection must not be confused with the gravitational connection of the corpus. The connection is **one-sided**: it acts on matter by left multiplication, and on the adjoint-valued curvature by the commutator. The gravitational connection of *Curved Spacetime and the Biquaternion Framework* is **two-sided in a different sense**,
$$
D_{\imath}\tilde{Q} = \partial/\partial R_{\imath}\,\tilde{Q} + \vec\Gamma_{\imath}\tilde{Q} + \tilde{Q}\vec\Gamma_{\imath}^{*} ,
$$
because the infinitesimal Lorentz action on $\mathbb{B}_{\Phi}$ is $G\tilde{Q} + \tilde{Q}G^{*}$, not the commutator; the two differ precisely for the boosts. The connection lives in $\mathfrak{su}(2)\subset\mathbb{B}_{\Phi}$ and is one-sided; the gravitational connection lives in the six-dimensional scalar-free subspace and is two-sided. They share a name and nothing else, and no relation between them is asserted.

## The Bianchi Identity

The field strength is built from the connection by differentiation, so it cannot be arbitrary: it satisfies a differential identity. With the adjoint covariant derivative defined above, the **Bianchi identity** is

$$
\boxed{\;D_{k} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0
\qquad \text{for all } (k,\imath,\jmath)\;}.
$$

Three distinct indices appear, $k,\imath,\jmath$, each carried once by a derivative and once inside a form pair. Writing it out in full, with each term split into its derivative and its commutator,

$$
\partial/\partial R_{k} F_{\imath\jmath} + i\kappa[\mathcal{A}_{k},F_{\imath\jmath}]
\;+\;
\partial/\partial R_{\imath} F_{\jmath k} + i\kappa[\mathcal{A}_{\imath},F_{\jmath k}]
\;+\;
\partial/\partial R_{\jmath} F_{k\imath} + i\kappa[\mathcal{A}_{\jmath},F_{k\imath}]
= 0 .
$$

**The index pattern.** The three terms are the cyclic rotations of the triple $(k,\imath,\jmath)$: the derivative carries the first index of the rotation and the form pair carries the remaining two, in order. So $(k,\imath,\jmath)$ gives $D_kF_{\imath\jmath}$, the rotation $(\imath,\jmath,k)$ gives $D_\imath F_{\jmath k}$, and $(\jmath,k,\imath)$ gives $D_\jmath F_{k\imath}$. Equivalently $D_{[k}F_{\imath\jmath]}=0$: the standard $D_{[\lambda}F_{\mu\nu]}=0$ with $\lambda=k$, $\mu=\imath$, $\nu=\jmath$, antisymmetrised over all three. The order is part of the statement: the sum $D_k F_{\imath\jmath}+D_\imath F_{k\jmath}+D_\jmath F_{\imath k}$, in which the second and third pairs are not the cyclic rotations, is generically nonzero, and was checked as a negative control. Because the cyclic sum is totally antisymmetric in the three indices, contraction with the antisymmetric symbol gives the compact form

$$
\varepsilon^{k\imath\jmath\rho}\,D_{k} F_{\imath\jmath} = 0
\qquad \text{(one equation for each } \rho\text{)},
$$

with $\varepsilon^{k\imath\jmath\rho}$ the Levi-Civita symbol, $\varepsilon^{0123}=+1$; the lower-index symbol is the same array as the raised one, so the contraction is unchanged. The identity was recomputed for all $64$ ordered triples $(k,\imath,\jmath)$, on generic non-commuting, position-dependent connections, with residual identically zero.

## The Bianchi Identity as the Jacobi Identity

The derivation is short and complete, and the point is to display each substitution rather than name the result.

For any three operators $X,Y,Z$ in an associative algebra, the Jacobi identity holds:

$$
[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0 ,
$$

as a consequence of the associativity of composition, $(XY)Z = X(YZ)$. This is an identity of the *operator* algebra, and it applies to the covariant derivatives because they are operators. Take $X = D_k$, $Y = D_{\imath}$, $Z = D_{\jmath}$, three **distinct** indices:

$$
[D_k,[D_{\imath},D_{\jmath}]] + [D_{\imath},[D_{\jmath},D_k]] + [D_{\jmath},[D_k,D_{\imath}]] = 0 .
$$

The distinctness is not decoration. With $X=Y=D_{\imath}$ and $Z=D_{\jmath}$ the identity collapses to $0=0$ — the third term vanishes because $[D_\imath,D_\imath]=0$, and the first two are negatives of each other — and substituting the curvature identity into it returns $i\kappa(D_\imath F_{\imath\jmath}-D_\imath F_{\jmath\imath})=0$, which is the antisymmetry of $F$ over again and not the Bianchi identity. A repeated index produces a tautology.

Now substitute, term by term:

$$
[D_{\imath},D_{\jmath}] = i\kappa\,F_{\imath\jmath},
\qquad
[D_{k}, F_{\imath\jmath}] = D_{k} F_{\imath\jmath}.
$$

The first turns each inner commutator into multiplication by $i\kappa F$; the second is the definition of the adjoint covariant derivative. Therefore

$$
[D_k,[D_{\imath},D_{\jmath}]]
= [D_k, i\kappa F_{\imath\jmath}]
= i\kappa\,[D_k,F_{\imath\jmath}]
= i\kappa\,D_k F_{\imath\jmath},
$$

and the other two terms follow by rotating $(k,\imath,\jmath)$, so the operator Jacobi identity becomes

$$
i\kappa\left(D_k F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath}\right) = 0 ,
$$

which is the Bianchi identity. This is the identification the title promises, and it is a substitution, not an analogy: **the Bianchi identity is the Jacobi identity of the operator algebra, with the curvature identity substituted into it.** The substitution was verified exactly on generic non-commuting connections for all independent triples: the operator Jacobi sum is $i\kappa$ times the Bianchi cyclic sum, term by term.

## Where Each Identity Enters: Operator Jacobi and Algebra Jacobi

There are two distinct Jacobi identities in this story, at two different levels, and conflating them hides the structure.

**Operator level.** The identity just used,
$$
[D_k,[D_{\imath},D_{\jmath}]] + [D_{\imath},[D_{\jmath},D_k]] + [D_{\jmath},[D_k,D_{\imath}]] = 0 ,
$$
is exact for arbitrary operators. It uses only associativity of operator composition; it does not use the compactness, the reality, or even the Lie-algebra character of the connection components. Given the curvature identity, it produces the Bianchi identity with no further input.

**Algebra level.** The coordinate route to the same identity differentiates $F$ and applies $D_{\imath}$. Its terms group into three classes, and each class is killed by a different mechanism. Writing only the cyclic sum $D_k F_{\imath\jmath}+D_\imath F_{\jmath k}+D_\jmath F_{k\imath}$, the classes are:

- the **second-derivative terms** $\partial^2/\partial R_{k}\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial^2/\partial R_{k}\partial R_{\jmath}\,\mathcal{A}_{\imath} + \text{cyclic}$, which vanish because partial derivatives commute;
- the **derivative-of-commutator terms** $\partial/\partial R_{k}[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}] + \text{cyclic}$ together with $[\mathcal{A}_{k},\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}] + \text{cyclic}$, which cancel in pairs by the Leibniz rule for the bracket — the derivative of a bracket is the sum of the brackets of the derivatives;
- the **nested commutators** $[\mathcal{A}_{k},[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]] + \text{cyclic}$, which vanish by the **algebra Jacobi identity**
$$
[\mathcal{A}_k,[\mathcal{A}_\imath,\mathcal{A}_\jmath]] + [\mathcal{A}_\imath,[\mathcal{A}_\jmath,\mathcal{A}_k]] + [\mathcal{A}_\jmath,[\mathcal{A}_k,\mathcal{A}_\imath]] = 0 .
$$

These three classes were separated and each was verified to vanish on generic connections, with the reconstruction of the full cyclic sum from them checked as well. The algebraic Jacobi identity is the statement, in *Lie Algebras: A General Introduction*, that makes the adjoint action $\mathrm{ad}_{q_x} = [q_x,\cdot]$ a derivation of the bracket,
$$
\mathrm{ad}_{q_x}[q_y,q_z] = [\mathrm{ad}_{q_x}q_y, q_z] + [q_y, \mathrm{ad}_{q_x}q_z],
$$
and it is that derivation property — equivalently the Leibniz rule for $D_{\imath}$ acting on a bracket — that makes the middle class cancel. It is the genuinely non-abelian ingredient: the abelian case lacks it because it lacks the bracket altogether.

The two Jacobi identities are not the same statement. The operator identity is associativity of composition and is sufficient, on its own, to turn the curvature identity into the Bianchi identity; the algebra identity is the Lie-algebra axiom that controls the coordinate proof. Both are exact, and both are used, at their own level.

## Explicit Verification on a Non-Abelian Connection

Everything above was checked by explicit substitution on $\mathfrak{su}(2)$ with the non-commuting generators $\vec e_x,\vec e_y,\vec e_z$ and the rule $[\vec e_a,\vec e_b]=2\varepsilon_{abc}\vec e_c$, on connections with generic real polynomial coefficients in all four components. The following were confirmed.

- **The reduction.** $[D_{\imath},D_{\jmath}]\tilde{Ξ} = i\kappa F_{\imath\jmath}\tilde{Ξ}$ for all six independent index pairs, and the commutator is zeroth order, $[D_{\imath},D_{\jmath}](f\tilde{Ξ}) = f[D_{\imath},D_{\jmath}]\tilde{Ξ}$.
- **The Bianchi identity.** The cyclic sum vanishes identically for all $64$ ordered triples, with individual terms of order unity, so the vanishing is a genuine cancellation and not a sum of zeros.
- **The Jacobi identification.** The operator Jacobi sum equals $i\kappa$ times the Bianchi cyclic sum identically, and the three term classes of the coordinate proof (second derivatives, derivative-of-commutator, nested commutators) each vanish for the stated reason.
- **The non-vacuity controls.** The wrong cyclic order is generically nonzero; the one-sided replacement $\partial/\partial R_{\imath} F_{\imath\jmath}+i\kappa\mathcal{A}_{\imath} F_{\imath\jmath}$ gives a generically nonzero cyclic sum; and $F_{\imath\jmath}$ differs from $i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$ for position-dependent connections.

The checks were run on two independent random families with different seeds, over all index pairs and all index triples, precisely so that the identity is not verified only on the case that suggested it. A concrete constant-connection display makes the structure visible. For

$$
\mathcal{A}_1 = \vec e_x+\vec e_y, \qquad \mathcal{A}_2 = \vec e_y+\vec e_z, \qquad \mathcal{A}_3 = \vec e_z+\vec e_x,
$$

one has $F_{12}=2i(\vec e_x-\vec e_y+\vec e_z)$, $F_{23}=2i(\vec e_x+\vec e_y-\vec e_z)$, and $F_{31}=2i(-\vec e_x+\vec e_y+\vec e_z)$. The three Bianchi terms for the triple $(1,2,3)$ are each nonzero — for instance $D_1F_{23}$ has entries of magnitude $4\sqrt2$ — while their sum is the zero matrix, and the algebraic ancestor $[[\mathcal{A}_1,\mathcal{A}_2],\mathcal{A}_3] + \text{cyclic}$ is likewise the zero matrix. The constant case is where the Bianchi identity is *literally* the algebra Jacobi identity, because the derivative of $F$ vanishes and $D_{k} F_{\imath\jmath} = i\kappa[\mathcal{A}_{k},F_{\imath\jmath}] = -\kappa^2[\mathcal{A}_{k},[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]]$. The numbers in this display take $\kappa=1$.

## The Abelian Case Is Not Evidence

If all the connection coefficients are central — $\mathcal{A}_{\imath} = a_{\imath} e_t$ with complex scalar functions $a_{\imath}$ — then $[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]=0$, the curvature reduces to $F_{\imath\jmath} = \partial/\partial R_{\imath} a_{\jmath} - \partial/\partial R_{\jmath} a_{\imath}$, the adjoint covariant derivative reduces to the ordinary one, and the Bianchi identity becomes

$$
\partial/\partial R_{k} F_{\imath\jmath} + \partial/\partial R_{\imath} F_{\jmath k} + \partial/\partial R_{\jmath} F_{k\imath} = 0 ,
$$

which is automatic: it is $dF = d^2a = 0$, and it holds because $F$ is a curl, not because of any bracket. The individual terms are nonzero, but the sum vanishes by the symmetry of mixed partial derivatives, and no commutator term is present at all.

The abelian check therefore passes for a reason unrelated to the non-abelian statement, and **passing it is not evidence**. It was confirmed that the abelian case is trivially zero, and it is reported here for the opposite purpose — to mark the boundary of what the non-abelian verification shows. The evidence for the non-abelian identity is the non-commuting, position-dependent family of the previous section, where the commutator term is nonzero and the individual Bianchi terms cancel against each other only by the Jacobi structure.

Nor is a single family enough on its own. The strongest evidence is an *independent* derivation of the same statement, and the coordinate proof of §*Where Each Identity Enters* is exactly that: it reaches the identity by differentiating $F$ directly, splits the result into three term classes, and kills each class for a stated reason — commuting partials, the Leibniz rule for the bracket, the algebra Jacobi identity — with no use of the operator Jacobi identity at all. The substitution proof and the coordinate proof are independent routes to one equation. Either alone would be a check; together they are what makes the identity established rather than merely verified.

## Can One Biquaternion Equation Carry the Bianchi Identity?

The minimal coupling article left open "the sense in which a single biquaternion equation carries" the Bianchi identity, and the covariant-derivative article recorded the negative result that the one-line equation $\tilde\nabla_\Phi\tilde{F}=0$ is the full source-free Maxwell system and not the Bianchi identity. That negative result is confirmed here by recomputation, and the reason is visible.

For the abelian field-strength biquaternion $\tilde{F} = i\vec E - c\vec B = \vec F = \sum_{\imath\in\{x,y,z\}} F_{\imath} \vec e_{\imath}$, direct computation with the quaternion product gives the exact identities

$$
(\tilde\nabla_\Phi)^{\natural}\tilde{F}
= \mathrm{div}(\vec F)\,e_t + \partial/\partial R_t\,\vec F - \mathrm{curl}\,\vec F,
\qquad
\tilde\nabla_\Phi\tilde{F}
= -\mathrm{div}(\vec F)\,e_t + \partial/\partial R_t\,\vec F + \mathrm{curl}\,\vec F,
$$

where $\vec F = \sum_{\imath\in\{x,y,z\}} F_{\imath} \vec e_{\imath}$ and $\mathrm{div},\mathrm{curl}$ are the three-dimensional operators acting on the coefficient triple, each exactly as displayed, with no residual. The zero set of either equation is eight real equations: a scalar constraint, which for $\tilde\nabla_\Phi\tilde{F}=0$ reads $\mathrm{div}\,\vec E = 0$ and $\mathrm{div}\,\vec H = 0$, together with the six real components of a vector equation, $\partial/\partial R_t\,\vec F = -\mathrm{curl}\,\vec F$. The Bianchi identity in the abelian sector, by contrast, is the four real equations $\mathrm{div}\,\vec B = 0$ and $\partial/\partial r'_t\vec B + \mathrm{curl}\,\vec E = 0$. Eight equations are not four, and the scalar constraint has no counterpart in a three-index antisymmetric identity; the parent's negative result — that the one-line equation $\tilde\nabla_\Phi\tilde{F}=0$ is the source-free field system and not the Bianchi identity — therefore stands, and the recomputation here confirms the structural reason rather than merely inheriting the verdict.

The structural reason is that the Bianchi identity is a three-index antisymmetric statement — a $3$-form — whereas a biquaternion product of the gradient (one index) with the curvature (a two-index algebra element) contracts its indices through the algebra, producing the scalar and vector combinations displayed above rather than the cyclic sum over three distinct indices. Contracting the Bianchi identity with the totally antisymmetric symbol does convert it into a four-component vector equation, $\varepsilon^{k\imath\jmath\rho}D_{k} F_{\imath\jmath} = 0$, one component for each $\rho$. But the antisymmetric symbol is extra structure: it is not contained in the algebra product, and this is a rewriting of the four contracted equations rather than an algebra-intrinsic one-line Bianchi. **This is a gap, and it is recorded as one:** the framework does not, without extra structure, supply a single biquaternion equation carrying the Bianchi identity.

## Open Questions

1. **The single-biquaternion Bianchi.** The gap above is the sharpest open question of this article. Is there an algebra-intrinsic operation — a projection or a product with the conjugate gradient — that extracts the cyclic three-index sum from a biquaternion expression, or is the antisymmetric symbol genuinely required? The parent's negative result for $(\tilde\nabla_\Phi)^{\natural}\tilde{F}$ and the recomputed forms of both products suggest the latter, but neither settles it.

2. **The curvature as one commutator.** The reduction "$[D_{\imath},D_{\jmath}] = $ multiplication by $i\kappa F_{\imath\jmath}$" is exact, but $F_{\imath\jmath}$ itself is a curl plus a commutator, and is a single algebra commutator only when the curl $\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}$ vanishes. Is there a covariant way to write the full $F_{\imath\jmath}$ as a single commutator of algebra-valued objects, or is the split into curl and commutator intrinsic?

3. **The reality class of the connection.** Inherited from the non-abelian article, unchanged: because $\partial/\partial R_t = -i\partial/\partial r'_t$, no single Hermitian-conjugation eigenspace is preserved by the local transformation across all four components, and the consistent mixed assignment (time in $\mathfrak{su}(2)\subset\mathbb{B}_{\Phi}$, space in $i\,\mathfrak{su}(2)\subset\mathbb{B}_{\Psi}$) is not shown to be the intended one.

4. **Which compact algebra.** Also inherited: the framework exhibits $\mathfrak{su}(2)$ in the vector part of $\mathbb{B}_{\Phi}$, and the material sector decomposes as $\mathbb{R}(ie_t)\oplus\mathfrak{su}(2)$. Whether a larger compact algebra is available, and which the framework selects, is open.

5. **The matter representation.** The covariant derivative here acts on matter by left multiplication and on the curvature by the commutator. For a non-abelian connection the left and right actions on a matter field differ, and which representation the matter field carries is not fixed here.

6. **Topological charge.** The Bianchi identity and the invariant density are the ingredients of the topological charge $\int\mathrm{Tr}(F\wedge F)$, which is the second Chern number $c_2$ of the bundle: an integer, unchanged by continuous deformation, and the reason instanton sectors exist in the first place. The concrete question is therefore narrow and answerable: does the biquaternion framework supply a natural representative of $c_2$ — an antisymmetric object built from the algebra product rather than from $\varepsilon$ — or does the invariant have to be written with the symbol inserted by hand? The packaging discussion above suggests the second, but does not prove it.

7. **Empirical contact.** The construction is a reformulation of standard Yang–Mills theory in the algebra's notation, and no empirical distinction is expected from it at this level: the identity proved here holds in both, for the same reason, and nothing in the proof refers to a quantity a measurement could separate. A distinction would have to come from elsewhere in the corpus — the connection's reality class, the representation of matter, or the compactness question above — and none of those is advanced by this article.

## Summary

The connection curvature of the biquaternionic framework is the commutator of covariant derivatives, and the commutator reduces to the algebra. For a connection $\mathcal{A}_{\imath} \in \mathfrak{su}(2) = \mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}\subset\mathbb{B}_{\Phi}$ and $D_{\imath} = \partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath}$, with $\kappa =\kappa$,

$$
[D_{\imath},D_{\jmath}] = i\kappa\,F_{\imath\jmath},
\qquad
F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath} - \partial/\partial R_{\jmath}\,\mathcal{A}_{\imath} + i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}] \in \mathfrak{su}(2)\oplus i\,\mathfrak{su}(2) = \mathfrak{sl}(2,\mathbb{C}),
$$

and the commutator is zeroth order: it is multiplication by the single algebra element $i\kappa F_{\imath\jmath}$. That localisation of an operator commutator onto the finite-dimensional algebra is the content of the reduction, and it was verified exactly on generic non-commuting connections for all index pairs. The curvature is antisymmetric, $F_{\imath\jmath}=-F_{\jmath\imath}$, and transforms in the adjoint representation, $F_{\mathrm g,\imath\jmath} = \tilde UF_{\imath\jmath}\tilde U^{-1}$.

Because the curvature is adjoint-valued, its covariant derivative is the two-sided commutator $D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa[\mathcal{A}_{\imath},\tilde{Q}]$, not the one-sided left multiplication used on a matter field; collapsing the two-sided action to a one-sided one destroys the Bianchi identity. This distinction is separate from, and not to be confused with, the two-sided gravitational connection of the curved-spacetime article.

The Bianchi identity is

$$
\boxed{\;D_{k} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath} = 0\;},
$$

on three distinct indices, the cyclic order as displayed — $D_{[k}F_{\imath\jmath]}=0$ — and equivalently $\varepsilon^{k\imath\jmath\rho}D_{k}F_{\imath\jmath}=0$, one equation for each $\rho$. It is the **operator Jacobi identity** with the curvature identity substituted into it: $[D_k,[D_\imath,D_\jmath]]+[D_\imath,[D_\jmath,D_k]]+[D_\jmath,[D_k,D_\imath]]=0$ becomes $i\kappa(D_kF_{\imath\jmath}+D_\imath F_{\jmath k}+D_\jmath F_{k\imath})=0$. In the coordinate proof a second, algebraic Jacobi identity $[\mathcal{A}_k,[\mathcal{A}_\imath,\mathcal{A}_\jmath]]+\text{cyclic}=0$ kills the nested-commutator terms, via the derivation property of the adjoint action. Both identities are exact and were verified on $\mathfrak{su}(2)$; the abelian case is trivially zero and is not evidence.

Two things are left visible. First, a **scope limitation**: the curvature is a curl plus an algebra commutator, and is a single algebra commutator only when the curl $\partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}$ vanishes. Second, a **gap**: no single biquaternion equation carries the Bianchi identity without extra structure — the recomputed products $(\tilde\nabla_\Phi)^{\natural}\tilde{F} = \mathrm{div}(\vec F)e_t+\partial/\partial R_t\,\vec F-\mathrm{curl}\,\vec F$ and $\tilde\nabla_\Phi\tilde{F} = -\mathrm{div}(\vec F)e_t+\partial/\partial R_t\,\vec F+\mathrm{curl}\,\vec F$ each carry a scalar constraint and a vector equation (eight real equations), not the three-index cyclic sum, and the contracted form $\varepsilon^{k\imath\jmath\rho}D_{k}F_{\imath\jmath}=0$ requires the antisymmetric symbol.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_{\imath}^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}, \mathbb{B}_{C}$ | Real-quaternion subspace; centre $\mathrm{span}_\mathbb{R}\{e_t,ie_t\}$ |
| $\tilde\nabla_\Phi, (\tilde\nabla_\Phi)^{\natural}$ | Biquaternionic gradient and its quaternion conjugate |
| $[\vec e_a,\vec e_b]=2\varepsilon_{abc}\vec e_c$ | Commutator on the vector part of $\mathbb{B}_{\Phi}$ |
| $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ | Real Lie algebra inside $\mathbb{B}_{\Phi}$; written $\mathrm{SU}(2)$ in the companion articles |
| $\mathfrak{su}(2)\oplus i\,\mathfrak{su}(2)=\mathfrak{sl}(2,\mathbb{C})$ | Real Lie-algebra decomposition of the traceless part; $i\,\mathfrak{su}(2)$ is not a group |
| $T_a=\tfrac12 \vec e_a$ | Normalized generators, $[T_a,T_b]=\varepsilon_{abc}T_c$, $2\,\mathrm{Sc}(T_aT_b)=-\tfrac12\delta_{ab}$ |
| $\tilde U(\tilde{Q}) \in SU(2)$ | Unit real quaternion, $\tilde U^{-1}=\bar{\tilde U}=\tilde U^\dagger$ |
| $\mathcal{A}_{\imath} = \sum_a\mathcal{A}_{\imath a} \vec e_a \in \mathfrak{su}(2)$ | Non-abelian connection, $\mathcal{A}=\sum_{\imath}\mathcal{A}_{\imath} e_{\imath}$ |
| $\kappa$ | Coupling, not fixed by the algebra |
| $D_{\imath} = \partial/\partial R_{\imath} + i\kappa\mathcal{A}_{\imath}$ | Covariant derivative on matter (one-sided, left) |
| $\partial/\partial R_t = -i\partial/\partial r'_t$ | $i r'_t$ time derivative |
| $F_{\imath\jmath} = \partial/\partial R_{\imath}\,\mathcal{A}_{\jmath}-\partial/\partial R_{\jmath}\,\mathcal{A}_{\imath}+i\kappa[\mathcal{A}_{\imath},\mathcal{A}_{\jmath}]$ | Curvature components, antisymmetric, valued in $\mathfrak{sl}(2,\mathbb{C})$ as a real Lie algebra |
| $[D_{\imath},D_{\jmath}] = i\kappa F_{\imath\jmath}$ | Curvature as the commutator of covariant derivatives |
| $F_{\mathrm g,\imath\jmath} = \tilde UF_{\imath\jmath}\tilde U^{-1}$ | Adjoint transformation of the curvature |
| $a,b$ | adjoint index of the algebra, written low |
| $D_{\imath} \tilde{Q} = \partial/\partial R_{\imath} \tilde{Q} + i\kappa[\mathcal{A}_{\imath},\tilde{Q}]$ | Adjoint covariant derivative, $[D_{\imath},\tilde{Q}]=D_{\imath} \tilde{Q}$ |
| $D_{k} F_{\imath\jmath} + D_{\imath} F_{\jmath k} + D_{\jmath} F_{k\imath}=0$ | Bianchi identity, three distinct indices, cyclic order as shown |
| $D_{[k}F_{\imath\jmath]}=0$ | The same identity as the antisymmetric part of $DF$ |
| $\varepsilon^{k\imath\jmath\rho}D_{k} F_{\imath\jmath}=0$ | Contracted form, one equation for each $\rho$ |
| $\tilde{F}=i\vec E-c\vec B$ | Abelian field-strength biquaternion, $\vec F=\sum_{\imath\in\{x,y,z\}} F_{\imath}\vec e_{\imath}$ |
| $\mathrm{div}(\vec F),\ \mathrm{curl}\,\vec F$ | Three-dimensional operators on the coefficient triple |
| $-\tfrac12\sum_{\imath,\jmath}\varepsilon_{\imath}\varepsilon_{\jmath}\,\mathrm{Tr}(F_{\imath\jmath}F_{\imath\jmath})$ | Invariant Yang–Mills density (matrix trace) |
| $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Inherited plain trace reading (distinct from the matrix trace) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- [The Covariant Derivative and Connection in Biquaternionic Form](the-covariant-derivative-and-connection-in-biquaternionic-form.html) — the immediate parent; its abelian commutator identity $[D_{\imath},D_{\jmath}]=i\kappa F_{\imath\jmath}$ and its deferral of the Bianchi identity to this article.
- [Non-Abelian Connections in Biquaternionic Form](non-abelian-connections-in-biquaternionic-form.html) — the non-abelian connection, the transformation law, the adjoint curvature, and the compactness gap this article inherits unchanged.
- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html) — the origin of the connection, the covariant derivative, and the curvature; the source of the remark that the homogeneous equations are the Bianchi identity of the connection.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the abelian field strength, its pure-vector character, and the biquaternion-norm apparatus that the non-abelian extension does not yet reproduce.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the abelian field equation $\tilde\nabla_\Phi\tilde{F}=-Z\tilde{J}_{\Phi}$ whose homogeneous part is the Bianchi identity.
- [Lie Algebras: A General Introduction](../articles_maths/lie-algebras-a-general-introduction.html) — the Jacobi identity, the adjoint action as a derivation, and the commutator bracket on an associative algebra.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html) — the two-sided gravitational connection $D_{\imath}\tilde{Q}=\partial/\partial R_{\imath}\,\tilde{Q}+\vec\Gamma_{\imath}\tilde{Q}+\tilde{Q}\vec\Gamma_{\imath}^{*}$, distinct from the one-sided connection of this article.
- [Four-Vectors and the Interval](four-vectors-and-the-interval.html) — the sector basis, the imaginary-scalar/real-vector structure, and the Lie-algebra decomposition on which the algebra rests.
- [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) — the Hermitian sector and the pairing formula distinguished here from the matrix trace.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) and [Quaternion Algebra](../articles_maths/quaternion-algebra.html) — the multiplication rule, the conjugations, and the centre used throughout.
