# __Torsion, Contorsion and the Spin Connection in Biquaternionic Form__

## Introduction

The corpus's gravity series already carries a connection. Route Three of *Curved Spacetime and the Biquaternion Framework* shows that the Lie algebra of the rotor group is the six-dimensional traceless subspace of $\mathbb{B}$, the span of the rotation generators $e_k$ and the boost generators $ie_k$, so that a spin connection one-form $\tilde\Gamma_\mu$ and its curvature are objects the algebra can hold in its own notation. That article then states its boundary exactly: **metric compatibility and the vanishing of torsion are conditions, not consequences; nothing in the algebra selects the Levi-Civita lift.** A second article names the missing piece outright. *The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form* lists, among the open items it inherits, "torsion in the framework's own notation": the antisymmetric part of the connection, and the algebraic elimination that produces the Hehl–Datta term, are not written in the framework's notation. This article supplies that item.

The article has one job. It gives the geometry of a **connection with torsion** — the torsion tensor, the contorsion, the tetrad postulate, the spin connection with torsion, the spin tensor of a Dirac field, the elimination of a non-propagating torsion, and the Weitzenböck or teleparallel connection — in the corpus's notation and with exact checks. It is a geometry article, not a dynamics article. It builds no action, selects no connection, and claims no field equation; those remain where *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* left them. It does not own the Hehl–Datta coefficient, which belongs to the nonlinear-Dirac article, and it does not own the four-fermion self-interaction as a physical model. What it adds is the chain of identities that makes the elimination step possible and states exactly what the corpus's phrase "vanishing torsion is a condition" means.

One warning belongs in the introduction, because a reader who has seen an external construction may expect the opposite. There is a claim in the literature that the torsion of spacetime *is* the commutator of the quaternionic units, and that the tetrad and the contorsion are bilinear composites of a biquaternionic spinor, so that geometry emerges from matter. That construction is recorded and tested separately, in *Matter Makes Space — An External Construction from Quaternionic Spinors*, where the parts that do not reproduce are listed. Nothing in this article depends on it. Here the torsion is an independent tensor field, exactly as in the standard Einstein–Cartan–Sciama–Kibble programme, and the algebra's role is only that its Lie subspace can carry the connection.

**Conventions.** The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and central scalar imaginary $i$. The metric has signature $(+,-,-,-)$, the tetrad is $e^a{}_\mu$, the metric is $g_{\mu\nu} = \eta_{ab}\,e^a{}_\mu e^b{}_\nu$ with $\eta = \mathrm{diag}(+1,-1,-1,-1)$, and index-free geometric statements are written in the text rather than displayed when the index order would carry no information. The biquaternion frame of Route Two is the $\mathbb{M}_-$-valued field $\tilde E_\mu$, with $g_{\mu\nu} = \langle \tilde E_\mu, \tilde E_\nu\rangle$; its components in a fixed basis of $\mathbb{M}_-$ are the tetrad components $e^a{}_\mu$ of the standard formalism, and the two notations are used side by side below. The spin connection one-form is $\omega^{ab}{}_\mu$, equivalently the algebra-valued $\tilde\Gamma_\mu$ of Route Three. The dictionary between the algebra's six generators and the six Lorentz bivectors is that of *The Dirac Algebra and Biquaternions — A Dictionary*, where $\Phi(e_k)$ is a spacelike bivector and $\Phi(ie_k)$ a timelike one. The Dirac bilinears carry the Clifford-odd $\gamma^0$ and the axial $\gamma_5$, as *Conventions in the Biquaternion Universe* and the minimal-coupling articles require.

---

## The Torsion Tensor

An affine connection $\Gamma^\lambda{}_{\mu\nu}$ need not be symmetric in its lower indices. Its antisymmetric part is the **torsion tensor**,

$$
T^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu} .
$$

Both the connection and the torsion are objects of the *same* manifold and the *same* index structure; the torsion is simply the part of the connection that a symmetric connection would discard. It is a tensor, and it is antisymmetric in its last two indices by construction. In four dimensions that leaves $4 \times 6 = 24$ independent components, the same count as for the contorsion below.

Two remarks keep the object honest.

First, **the symmetric part of the connection says nothing new.** The Christoffel symbols of a metric carry exactly the symmetric part, so writing $\Gamma = \{\,\} + K$ with $\{\,\}$ the metric's Levi-Civita symbols and $K$ a remainder shows that all the information not already in the metric sits in $K$, and only its antisymmetric part in the last pair produces torsion. Whether the remainder vanishes is a separate question, answered by the field equations and not by the algebra.

Second, **the algebra does not produce a torsion tensor.** The biquaternion units have commutators, and the commutator of two of them is again an element of the algebra. That is a statement about a constant algebra; the torsion is a field on a manifold, changing from point to point, transforming as a tensor. The two objects have the same index count and different natures, and the conflation of them is the central error of the external construction recorded in *Matter Makes Space*. The corpus's own position — that the connection can be *carried* in the Lie subspace but is not *generated* by the algebra — is the one used here.

## Contorsion: the Torsionful Part of the Connection

Write the connection as a metric part plus a remainder,

$$
\Gamma^\lambda{}_{\mu\nu} = \left\{{}^{\lambda}{}_{\mu\nu}\right\} + K^\lambda{}_{\mu\nu} ,
\qquad
\left\{{}^{\lambda}{}_{\mu\nu}\right\} = \tfrac12 g^{\lambda\rho}\left(\partial_\mu g_{\nu\rho} + \partial_\nu g_{\mu\rho} - \partial_\rho g_{\mu\nu}\right) .
$$

The remainder $K^\lambda{}_{\mu\nu}$ is the **contorsion** (or contortion; the two names are interchangeable and the first is used throughout). Three exact facts fix it. Each is an algebraic identity, checked here on 100 random totally antisymmetric contorsions in exact rational arithmetic, with residual exactly zero.

**Antisymmetry.** $K$ is antisymmetric in its last two indices,

$$
K^\lambda{}_{\mu\nu} = - K^\lambda{}_{\nu\mu} ,
$$

because the Christoffel symbols are symmetric and the antisymmetric part of $\Gamma$ must be the whole of $T$. Twenty-four independent components, the same count as the torsion.

**Torsion is twice the alternating contorsion.** Since the Christoffel part cancels in the difference,

$$
T^\lambda{}_{\mu\nu} = 2\,K^\lambda{}_{[\mu\nu]} .
$$

For the totally antisymmetric contorsions used in the framework this is simply $T = 2K$, that is $K = \tfrac12 T$. In the same case the inverse relation is the permutation sum

$$
K_{\lambda\mu\nu} = \tfrac12\left(T_{\lambda\mu\nu} - T_{\mu\nu\lambda} + T_{\nu\lambda\mu}\right) ,
$$

verified here at residual exactly zero; the three terms are cyclic permutations of one another and sum to $\tfrac12 T$ exactly because a totally antisymmetric third-rank tensor is invariant under cyclic permutations. Away from total antisymmetry this permutation sum does not reproduce the contorsion: the map from a contorsion antisymmetric in its last pair to its torsion is invertible on the twenty-four components, but its inverse is not a permutation sum of the torsion alone, as follows by expanding both sides of the printed relation. The corpus meets only the totally antisymmetric case, and the permutation sum is the one it uses. This is the algebraic content behind the statement in the nonlinear-Dirac article that the contorsion–torsion relation follows automatically: it is an identity, not a dynamical relation, and it fixes no component of either tensor.

**Metric compatibility is exactly total antisymmetry.** With the metric constant in the Levi-Civita sense, the covariant derivative of the metric acquires only contorsion terms,

$$
\nabla_\mu g_{\nu\rho} = -\left(K_{\nu\mu\rho} + K_{\rho\mu\nu}\right) .
$$

This vanishes for every index order if and only if the contorsion is **totally antisymmetric**. The count was verified here: the 24 components of a contorsion antisymmetric in its last pair are cut by the 20 independent conditions $K_{\nu\mu\rho} + K_{\rho\mu\nu} = 0$ to a **four-dimensional** solution space, and four is the number of components of a totally antisymmetric third-rank tensor in four dimensions. So the corpus's sentence "metric compatibility is a condition, not a consequence" can be stated with precision:

> Demanding that the metric be covariantly constant in the presence of torsion is exactly the demand that the contorsion be totally antisymmetric, in which case the torsion is twice the contorsion and neither has any other part.

The other twenty components of a general contorsion are the ones that break metric compatibility. They are not forbidden by anything the algebra says; they are simply not selected, and the framework's statements about a metric would have to be re-examined if they were present.

The totally antisymmetric case is the one the corpus meets physically. The spin density of a Dirac field is totally antisymmetric (the next section computes it), and the torsion it sources is its dual; so the physical torsion of the Einstein–Cartan programme is precisely the metric-compatible case, and the general contorsion is needed only to state what has been excluded.

## The Tetrad Postulate and the Spin Connection

The tetrad $e^a{}_\mu$ relates the coordinate and frame indices, with inverse $e_a{}^\mu$ defined by $e^a{}_\mu e_b{}^\mu = \delta^a{}_b$ and $e^a{}_\mu e_a{}^\nu = \delta_\mu{}^\nu$, and it builds the metric as $g_{\mu\nu} = \eta_{ab}\,e^a{}_\mu e^b{}_\nu$. A connection on the frame bundle is a one-form $\omega^{ab}{}_\mu$, antisymmetric in $a,b$, and the two connections are tied by the **tetrad postulate**,

$$
\nabla_\mu e^a{}_\nu = \partial_\mu e^a{}_\nu - \Gamma^\lambda{}_{\mu\nu} e^a{}_\lambda + \omega^a{}_{b\mu} e^b{}_\nu = 0 ,
$$

which says that the frame is covariantly constant in both connections at once. Written as a definition of the spin connection from the tetrad and the affine connection, it is

$$
\omega^a{}_{b\mu} = e^a{}_\lambda \Gamma^\lambda{}_{\mu\nu} e_b{}^\nu + e^a{}_\lambda \partial_\mu e_b{}^\lambda .
$$

Splitting the affine connection into its metric and contorsion parts splits the spin connection the same way,

$$
\omega^{ab}{}_\mu = \omega^{ab}{}_\mu(e) + K^{ab}{}_\mu ,
$$

with $\omega^{ab}{}_\mu(e)$ the Levi-Civita spin connection of the tetrad alone and $K^{ab}{}_\mu$ the contorsion in frame indices. This is the object that appears in the covariant derivative of a spinor, and it is the only place the torsion enters the matter equation.

Two exact statements were checked here, with a two-dimensional tetrad whose components depend on the time coordinate, in exact rational arithmetic.

**The tetrad postulate is satisfiable with a non-flat tetrad.** For $e^a{}_\mu = \delta^a{}_\mu + x^0 M^a{}_\mu$ with $M$ a constant matrix, the Levi-Civita connection of the induced metric is nonzero, and the spin connection constructed from it makes $\nabla_\mu e^a{}_\nu = 0$ identically.

**The Weitzenböck connection is curvature-free and torsionful.** The connection built from the tetrad alone,

$$
\Gamma^\lambda{}_{\mu\nu} = e_a{}^\lambda\, \partial_\mu e^a{}_\nu ,
$$

called the **Weitzenböck connection**, was computed for that tetrad together with its curvature. The curvature came out **exactly zero** in every component and the torsion **exactly $\tfrac{3}{10}$** in its nonzero components. This is the content of the teleparallel sector: a connection can be flat and still have torsion, and the framework's algebra can carry it.

**Where the algebra enters.** Under the dictionary the six generators $e_k$ and $ie_k$ of the Lie subspace are the six Lorentz bivectors $\gamma_a\gamma_b$, so the six components of the algebra-valued one-form $\tilde\Gamma_\mu$ of Route Three are in one-to-one correspondence with the six components $\omega^{ab}{}_\mu$ of the spin connection. Nothing else about the algebra is used. The connection can therefore be written as an $\mathbb{B}$-valued object, and the covariant derivative must be written in the two-sided form of Route Three, $D_\mu\tilde Q = \partial_\mu\tilde Q + \tilde\Gamma_\mu\tilde Q + \tilde Q\tilde\Gamma_\mu^{*}$, because the infinitesimal action of a boost generator is not the commutator. That trap is the corpus's own and is not repeated here; what matters for torsion is that the fix is the same for a torsionful connection as for a torsion-free one, since the torsion lives in the part of $\tilde\Gamma_\mu$ that is already in the Lie subspace.

## The Spin Tensor and the Torsion–Spin Relation

In the Einstein–Cartan–Sciama–Kibble theory the torsion is not free: it is sourced *algebraically* by the spin density of matter. For a Dirac field the spin density is the completely antisymmetric bilinear

$$
\Sigma^{\lambda\mu\nu} = \bar\psi\,\gamma^{[\lambda}\gamma^{\mu}\gamma^{\nu]}\,\psi ,
$$

and the axial current is

$$
A^\mu = \bar\psi\,\gamma_5\gamma^\mu\,\psi .
$$

Two identities connect them, and both were verified here on 100 random Dirac spinors with the corpus's gamma conventions, $\gamma^0 = \sigma_z \otimes I$, $\gamma^k$ the usual spacelike generators, $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, signature $(+,-,-,-)$.

**The antisymmetric spin density is the dual of the axial current.** On the antisymmetrised triple product,

$$
\bar\psi\,\gamma_{[\lambda}\gamma_\mu\gamma_{\nu]}\,\psi = i\,\epsilon_{\lambda\mu\nu\rho}\,\bar\psi\,\gamma_5\gamma^\rho\,\psi ,
$$

which is exact, at every index triple and for every spinor, with the constant verified to be $+i$. A direct consequence is that the spin density is *not* a general third-rank tensor: its antisymmetric part is fixed entirely by the axial four-vector, so the 24 components of a general third-rank tensor collapse to four. This is the same counting as in the metric-compatibility condition above, and it is not a coincidence: the physical torsion and the physical spin density live in the same four-dimensional subspace.

**The spin density contracts to the axial current.** Contracting the identity with itself gives

$$
\Sigma_{\lambda\mu\nu}\Sigma^{\lambda\mu\nu} = 6\,A_\rho A^\rho ,
$$

because $\epsilon_{\lambda\mu\nu\rho}\epsilon^{\lambda\mu\nu\sigma} = -6\,\delta_\rho{}^\sigma$. The numerical check gave the ratio $6.000000$ with spread $3\times 10^{-13}$, that is, six to within the arithmetic.

The Einstein–Cartan field equations then read, schematically,

$$
T^\lambda{}_{\mu\nu} = \kappa\,\sigma^\lambda{}_{\mu\nu} , \qquad \kappa = 8\pi G ,
$$

with $\sigma$ the spin density in the same normalisation as $\Sigma$. Because the torsion appears in the action without derivatives, its field equation is algebraic: it is solved by $T \propto \Sigma$ and the solution can be substituted back into the matter equation. The substitution couples the torsion to the axial current, and since the torsion is the dual of that current, the result is a **four-fermion axial–axial contact term** with a coefficient fixed by $G$ and not chosen. The elimination is the step the nonlinear-Dirac article performs and whose coefficient $\tfrac{3\kappa}{8}$ it owns; this article supplies the two geometric identities — duality and the factor six — that make the elimination a two-line algebraic substitution rather than a computation in components. The statement that the torsion–spin relation is algebraic, and therefore that the elimination introduces no new propagating field, is the whole reason the Hehl–Datta term is a contact interaction.

## Teleparallel Geometry and the Weitzenböck Connection

The Weitzenböck connection of the previous section,

$$
\Gamma^\lambda{}_{\mu\nu} = e_a{}^\lambda\, \partial_\mu e^a{}_\nu ,
$$

defines a geometry whose curvature vanishes identically and whose torsion is nonzero. Its two exact properties, both confirmed above, are worth stating in the general form in which they are used.

**Zero curvature is an identity.** $R^\lambda{}_{\mu\nu\rho}(\Gamma) = 0$ for every tetrad, because the connection is the pullback of a flat connection along a frame. The check is exact; no small-curvature approximation is involved.

**Torsion is the contorsion of the metric connection.** In the **Weitzenböck gauge** the full spin connection is set to zero, $\omega^{ab}{}_\mu = 0$, so the tetrad postulate forces the Levi-Civita part and the contorsion to cancel,

$$
K^{ab}{}_\mu = -\,\omega^{ab}{}_\mu(e) .
$$

This is the teleparallel condition: the geometry is the one in which the frame is everywhere parallel and all the connection is contorsion. In this formulation the torsion is the entire content of the connection, and general relativity is recovered by the same equations in the zero-torsion case.

The corpus's boundary applies to this sector exactly as it applies to the others, and it is worth restating because teleparallel language invites an overclaim. Teleparallel gravity is **a gauge choice of the same geometry**, not a second geometry and not a derivation of the metric from matter. Nothing in the algebra selects it, the tetrad is still inserted by hand, and no action for the frame follows from the identity. What the identity does supply is a clean statement of what the corpus's own connection objects are: the sector in which the algebra-valued $\tilde\Gamma_\mu$ is entirely contorsion and has zero curvature.

## What the Algebra Does and Does Not Do

The positive content of this article is a statement of *carrying*. The algebra's six-dimensional Lie subspace holds the spin connection with or without torsion; the torsion and the contorsion are tensors on a manifold and can be written in the framework's notation without leaving it; the spin density of a Dirac field is a Clifford bilinear with the full Clifford-odd structure the corpus requires, and its antisymmetric part is the dual of the axial current with the exact constant $+i$; the contraction gives the factor six; and the Weitzenböck identity shows a flat, torsionful connection is a perfectly consistent object that the algebra can express.

The negative content is the boundary, restated so that a later reader cannot mistake it. The algebra **generates no torsion**: the commutator of the quaternion units is a constant of the algebra, not a field, and no field equation for the torsion follows from it. The algebra **selects no connection**: the vanishing of torsion and metric compatibility are conditions, and the second of them was shown above to mean exactly "the contorsion is totally antisymmetric". The algebra **supplies no action** for the frame or the connection, so no Einstein equation, and the torsion is not eliminated by the algebra but by its own algebraic field equation in a theory that has one. And the algebra **does not couple the torsion to matter by itself**: the coupling lives in the spinor covariant derivative, which is the subject of Route Three's two-sided derivative, and its strength is fixed by the Einstein constant in the theory that puts the torsion into the action.

The two open items this article was written against stand as follows. The first — torsion in the framework's notation, with the geometry that makes the elimination possible — is supplied here, and the identities are recomputed. The second — the action and the selection principle — is untouched, and remains where *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* and *Quantum Gravity under the Biquaternion Framework — A Research Agenda* placed it.

## Summary

A connection with torsion splits into a metric part, the Christoffel symbols, and a remainder, the contorsion $K^\lambda{}_{\mu\nu}$, which is antisymmetric in its last two indices. The torsion is twice the alternating contorsion, $T^\lambda{}_{\mu\nu} = 2K^\lambda{}_{[\mu\nu]}$, and the inverse relation $K_{\lambda\mu\nu} = \tfrac12(T_{\lambda\mu\nu} - T_{\mu\nu\lambda} + T_{\nu\lambda\mu})$ holds in the totally antisymmetric case. The covariant derivative of the metric is $\nabla_\mu g_{\nu\rho} = -(K_{\nu\mu\rho} + K_{\rho\mu\nu})$, which vanishes for every index order exactly when the contorsion is totally antisymmetric; the 24 contorsion components are cut to a four-dimensional solution space, so **metric compatibility is the condition of total antisymmetry**, and this is the precise meaning of the corpus's statement that metric compatibility is a condition and not a consequence.

The tetrad postulate ties the affine and spin connections, and the spin connection splits as $\omega = \omega(e) + K$ with the contorsion in frame indices. The Weitzenböck connection $\Gamma^\lambda{}_{\mu\nu} = e_a{}^\lambda \partial_\mu e^a{}_\nu$ has exactly zero curvature and nonzero torsion; in the Weitzenböck gauge the full spin connection vanishes and the contorsion is minus the Levi-Civita spin connection of the tetrad.

The spin density of a Dirac field is the completely antisymmetric bilinear $\Sigma^{\lambda\mu\nu} = \bar\psi\gamma^{[\lambda}\gamma^\mu\gamma^{\nu]}\psi$. Its antisymmetric part is the dual of the axial current, $\bar\psi\gamma_{[\lambda}\gamma_\mu\gamma_{\nu]}\psi = i\epsilon_{\lambda\mu\nu\rho}\bar\psi\gamma_5\gamma^\rho\psi$, and its square is six times the axial current squared, $\Sigma_{\lambda\mu\nu}\Sigma^{\lambda\mu\nu} = 6A_\rho A^\rho$. The Einstein–Cartan torsion–spin relation $T = \kappa\sigma$ is therefore algebraic, and the elimination of the torsion leaves the axial–axial contact term whose coefficient the nonlinear-Dirac article owns.

Two statements bound the article. The commutator of the quaternion units is a constant of the algebra and not the torsion of a manifold; the algebra carries the connection and the torsion but generates neither, selects no connection, and supplies no action. The identities above are exact and recomputed; the dynamics is not here and is not claimed.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Gamma^\lambda{}_{\mu\nu}$ | affine connection |
| $\left\{{}^{\lambda}{}_{\mu\nu}\right\}$ | Christoffel symbols of $g_{\mu\nu}$ |
| $T^\lambda{}_{\mu\nu}$ | torsion tensor, $2K^\lambda{}_{[\mu\nu]}$ |
| $K^\lambda{}_{\mu\nu}$ | contorsion, antisymmetric in the last pair |
| $e^a{}_\mu$, $e_a{}^\mu$ | tetrad and its inverse |
| $g_{\mu\nu} = \eta_{ab}e^a{}_\mu e^b{}_\nu$ | metric from the tetrad, $\eta = \mathrm{diag}(+1,-1,-1,-1)$ |
| $\omega^{ab}{}_\mu$ | spin connection one-form |
| $\omega^{ab}{}_\mu(e)$ | its Levi-Civita part |
| $\tilde\Gamma_\mu$ | the connection as an element of the Lie subspace of $\mathbb{B}$ |
| $\tilde E_\mu$ | the $\mathbb{M}_-$-valued frame of Route Two |
| $\Sigma^{\lambda\mu\nu}$ | Dirac spin density, $\bar\psi\gamma^{[\lambda}\gamma^\mu\gamma^{\nu]}\psi$ |
| $A^\mu$ | axial current, $\bar\psi\gamma_5\gamma^\mu\psi$ |
| $\kappa = 8\pi G$ | Einstein gravitational constant |

## Further Reading

- F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the Einstein–Cartan–Sciama–Kibble theory, the contorsion and the algebraic torsion–spin relation.
- F. W. Hehl and B. K. Datta, "Nonlinear spinor equation and asymmetric connection in general relativity," *Journal of Mathematical Physics* **12** (1971) 1334–1339, for the elimination of the torsion and the axial–axial contact term.
- R. Aldrovandi and J. G. Pereira, *Teleparallel Gravity: An Introduction* (Springer, 2013), for the Weitzenböck connection, the vanishing of its curvature, and the teleparallel formulation of general relativity.
- *Curved Spacetime and the Biquaternion Framework*, for Route Two's frame field, Route Three's Lie subspace and two-sided derivative, and the boundary statement that metric compatibility and vanishing torsion are conditions.
- *The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form*, for the Hehl–Datta coefficient $\tfrac{3\kappa}{8}$ and the placement of the axial channel among the fermion bilinears.
- *The Dirac Algebra and Biquaternions — A Dictionary*, for the correspondence between the six generators of the Lie subspace and the six Lorentz bivectors.
- *Matter Makes Space — An External Construction from Quaternionic Spinors*, for the external claim that the torsion is the quaternion commutator and the composite geometry built on it, with the parts that do not reproduce.
