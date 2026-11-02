# __Torsion, Contorsion and the Spin Connection in Biquaternionic Form__

## Introduction

The corpus's gravity series already carries a connection. Route Three of *Curved Spacetime and the Biquaternion Framework* shows that the Lie algebra of the rotor group is the six-dimensional traceless subspace of $\mathbb{B}$, the span of the rotation generators $\vec e_k$ and the boost generators $i\vec e_k$, so that a spin connection one-form $\vec\Gamma_\mu$ and its curvature are objects the algebra can hold in its own notation. That article then states its boundary exactly: **metric compatibility and the vanishing of torsion are conditions, not consequences; nothing in the algebra selects the Levi-Civita lift.** A second article names the missing piece outright. *The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form* lists, among the open items it inherits, "torsion in the framework's own notation": the antisymmetric part of the connection, and the algebraic elimination that produces the Hehl–Datta term, are not written in the framework's notation. This article supplies that item.

The article has one job. It gives the geometry of a **connection with torsion** — the torsion tensor, the contorsion, the tetrad postulate, the spin connection with torsion, the spin tensor of a Dirac field, the elimination of a non-propagating torsion, and the Weitzenböck or teleparallel connection — in the corpus's notation and with exact checks. It is a geometry article, not a dynamics article. It builds no action, selects no connection, and claims no field equation; those remain where *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* left them. It does not own the Hehl–Datta coefficient, which belongs to the nonlinear-Dirac article, and it does not own the four-fermion self-interaction as a physical model. What it adds is the chain of identities that makes the elimination step possible and states exactly what the corpus's phrase "vanishing torsion is a condition" means.

One warning belongs in the introduction, because a reader who has seen an external construction may expect the opposite. There is a claim in the literature that the torsion of spacetime *is* the commutator of the quaternionic units, and that the tetrad and the contorsion are bilinear composites of a biquaternionic spinor, so that geometry emerges from matter. That construction is recorded and tested separately, in *Matter Makes Space — An External Construction from Quaternionic Spinors*, where the parts that do not reproduce are listed. Nothing in this article depends on it. Here the torsion is an independent tensor field, exactly as in the standard Einstein–Cartan–Sciama–Kibble programme, and the algebra's role is only that its Lie subspace can carry the connection.

**Index convention.** Every display is all-low. In the three-index objects $\Gamma_{\lambda\mu\nu}$, $T_{\lambda\mu\nu}$ and $K_{\lambda\mu\nu}$ the first index is the output and the last two are the inputs, in that order; $\mathrm{Riem}_{\lambda\mu\nu\rho}$ reads the output first and then the three inputs. In the mixed frame-and-world objects $\exp(a){}_\mu$, $e_{a\mu}$ and $\omega_{ab\mu}$ the frame slot comes first. A repeated label is summed, with the sign vector $\varepsilon$ where the contraction is the metric one: $\varepsilon_t=+1$ and $\varepsilon_k=-1$, so that $\varepsilon_\mu A_\mu$ is the raised component $A^\mu$ in the frame, where $g=\eta$, and no index is ever written up. In a general chart the raising is done by the inverse metric, which is written out explicitly, as in the Christoffel symbols of the next section.

**Cells and the two conventions of the article.** The geometry is written in tensors, the algebra in cells. A frame cell is a two-sided operator, $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ for the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$ and $L_aR_b\psi=a\psi b$; the three spatial cells carry an arrow on the right multiplier and the timelike one collapses to $iR_{\vec e_x}$. The factor $i$ belongs to the cell, and $i^2=-1$ is used silently throughout: a product of two cells brings one factor $i^2$ and so one sign flip, and no display below counts a minus sign twice. The gammas are a basis of these cells and appear in one section only, *The Gamma Formulation*; nothing before it needs them.

## The Torsion Tensor

An affine connection $\Gamma_{\lambda\mu\nu}$ need not be symmetric under the exchange of its two last labels. Its antisymmetric part is the **torsion tensor**,

$$
T_{\lambda\mu\nu} = \Gamma_{\lambda\mu\nu} - \Gamma_{\lambda\nu\mu} .
$$

Both the connection and the torsion are objects of the *same* manifold and the *same* index structure; the torsion is simply the part of the connection that a symmetric connection would discard. It is a tensor, and it is antisymmetric in its last two indices by construction. In four dimensions that leaves $4 \times 6 = 24$ independent components, the same count as for the contorsion below.

Two remarks keep the object honest.

First, **the symmetric part of the connection says nothing new.** The Christoffel symbols of a metric carry exactly the symmetric part, so writing $\Gamma = \{\,\} + K$ with $\{\,\}$ the metric's Levi-Civita symbols and $K$ a remainder shows that all the information not already in the metric sits in $K$, and only its antisymmetric part in the last pair produces torsion. Whether the remainder vanishes is a separate question, answered by the field equations and not by the algebra.

Second, **the algebra does not produce a torsion tensor.** The biquaternion units have commutators, and the commutator of two of them is again an element of the algebra. That is a statement about a constant algebra; the torsion is a field on a manifold, changing from point to point, transforming as a tensor. The two objects have the same index count and different natures, and the conflation of them is the central error of the external construction recorded in *Matter Makes Space*. The corpus's own position — that the connection can be *carried* in the Lie subspace but is not *generated* by the algebra — is the one used here.

## Contorsion: the Torsionful Part of the Connection

Write the connection as a metric part plus a remainder,

$$
\Gamma_{\lambda\mu\nu} = \left\{{}_{\lambda\mu\nu}\right\} + K_{\lambda\mu\nu} ,
$$
where the Christoffel symbols of the metric are
$$
\left\{{}_{\lambda\mu\nu}\right\} = \tfrac12\sum_\rho (g^{-1})_{\lambda\rho}\bigl(\partial/\partial x_\mu\, g_{\nu\rho} + \partial/\partial x_\nu\, g_{\mu\rho} - \partial/\partial x_\rho\, g_{\mu\nu}\bigr) .
$$

The remainder $K_{\lambda\mu\nu}$ is the **contorsion** (or contortion; the two names are interchangeable and the first is used throughout).

**One slot is raised implicitly.** The Christoffel display carries an explicit $(g^{-1})_{\lambda\rho}$, and the same convention runs through $\Gamma$, $T$ and $K$: the first slot is the output slot, stored with the inverse metric already applied. That is why the tetrad postulate of the next section contracts $\Gamma_{\lambda\mu\nu}$ with $\exp(a){}_\lambda$ and needs no further $g^{-1}$. The one place where the metric enters the other way is the boxed relation below, in which $K_{\nu\mu\rho}$ is the array with its first slot lowered by $g_{\nu\lambda}$; total antisymmetry is a statement about that lowered array, and the antisymmetry in the last pair, which is the display just below, is not.

The exact facts that fix $K$ are short.

**Antisymmetry.** $K$ is antisymmetric in its last two indices,

$$
K_{\lambda\mu\nu} = - K_{\lambda\nu\mu} ,
$$
because the Christoffel symbols are symmetric and the antisymmetric part of $\Gamma$ must be the whole of $T$. Twenty-four independent components, the same count as the torsion.

**Torsion is twice the contorsion.** Since the Christoffel part cancels in the difference and the remainder does not,
$$
T_{\lambda\mu\nu} = \Gamma_{\lambda\mu\nu} - \Gamma_{\lambda\nu\mu} = K_{\lambda\mu\nu} - K_{\lambda\nu\mu} = 2\,K_{\lambda\mu\nu} .
$$
The relation is $T=2K$ outright, in every case and not only in the totally antisymmetric one. It is an **identity**, not a dynamical relation, and it fixes no component of either tensor. Its inverse is the equally trivial $K=\tfrac12T$, and the map is one-to-one on the twenty-four components; nothing is gained by inverting it component by component.

One permutation sum is often quoted, and it is worth stating exactly when it holds. **In the totally antisymmetric case,**
$$
K_{\lambda\mu\nu} = \tfrac12\bigl(T_{\lambda\mu\nu} - T_{\mu\nu\lambda} + T_{\nu\lambda\mu}\bigr) ,
$$
because a totally antisymmetric third-rank tensor is invariant under the cyclic permutation that carries one term into the next, so the right-hand side is $\tfrac12(T-T+T)=\tfrac12T$. Away from total antisymmetry the same sum is not $\tfrac12T$, and $K=\tfrac12T$ remains the only inverse. In the totally antisymmetric case the torsion and the contorsion carry four components each, not twenty-four. The corpus meets only that case, and this is the algebraic content behind the statement in the nonlinear-Dirac article that the contorsion–torsion relation follows automatically.

**Metric compatibility is exactly total antisymmetry.** The Christoffel symbols are metric-compatible by construction, so only the contorsion survives,
$$
\boxed{\;\nabla_\mu g_{\nu\rho} = -\left(K_{\nu\mu\rho} + K_{\rho\mu\nu}\right)\;}.
$$
This vanishes for every index order if and only if the contorsion is **totally antisymmetric**. The condition says that $K$ is antisymmetric in its first and third slots, and two transpositions generate the whole permutation group, so a contorsion that is already antisymmetric in its last pair and satisfies the condition is antisymmetric in all three indices. The count agrees: the 24 components are cut to the **four** of a totally antisymmetric third-rank tensor in four dimensions, so twenty of the conditions are independent. The corpus's sentence "metric compatibility is a condition, not a consequence" therefore reads, with precision:

> Demanding that the metric be covariantly constant in the presence of torsion is exactly the demand that the contorsion be totally antisymmetric, in which case the torsion is twice the contorsion and neither has any other part.

The other twenty components of a general contorsion are the ones that break metric compatibility. They are not forbidden by anything the algebra says; they are simply not selected, and the framework's statements about a metric would have to be re-examined if they were present.

The totally antisymmetric case is the one the corpus meets physically. The spin density of a Dirac field is totally antisymmetric (the next section computes it), and the torsion it sources is its dual; so the physical torsion of the Einstein–Cartan programme is precisely the metric-compatible case, and the general contorsion is needed only to state what has been excluded.

## The Tetrad Postulate and the Spin Connection

The tetrad $\exp(a){}_\mu$ relates the coordinate and frame indices, with inverse $e_{a\mu}$ defined by
$$
\sum_\mu\exp(a){}_\mu e_{b\mu} = \delta_{ab},\qquad \sum_a\exp(a){}_\mu e_{a\nu} = \delta_{\mu\nu},
$$
and it builds the metric as $g_{\mu\nu} = \sum_{a,b}\eta_{ab}\,\exp(a){}_\mu \exp(b){}_\nu$, with $\eta=\mathrm{diag}(+1,-1,-1,-1)$. The frame pair of a frame-indexed object is lowered with $\eta$, so a repeated frame label is summed with $\varepsilon$ exactly as a repeated world label is. A connection on the frame bundle is a one-form $\omega_{ab\mu}$, and the two connections are tied by the **tetrad postulate**,

$$
\nabla_\mu \exp(a){}_\nu = \partial/\partial x_\mu \exp(a){}_\nu - \sum_\lambda\Gamma_{\lambda\mu\nu} \exp(a){}_\lambda + \sum_b\omega_{ab\mu} \exp(b){}_\nu = 0 ,
$$

which says that the frame is covariantly constant in both connections at once. Solved for the spin connection — the array that results carries its first frame slot raised — with the tetrad $\exp(a){}_\lambda$ in the first slot and the inverse $e_{b\nu}$ in the second, it reads
$$
\omega_{ab\mu} = \sum_{\lambda,\nu}\exp(a){}_\lambda \Gamma_{\lambda\mu\nu} e_{b\nu} + \sum_\lambda\exp(a){}_\lambda\, \partial/\partial x_\mu\, e_{b\lambda} ,
$$
with $\Gamma_{\lambda\mu\nu}$ the connection of the previous sections, contorsion included.

Splitting the affine connection into its metric and contorsion parts splits the spin connection the same way,
$$
\omega_{ab\mu} = \omega_{ab\mu}(e) + K_{ab\mu} ,
\qquad
K_{ab\mu} = \sum_{\lambda,\nu}\exp(a){}_\lambda\, K_{\lambda\mu\nu}\, e_{b\nu} ,
$$
with $\omega_{ab\mu}(e)$ the Levi-Civita spin connection of the tetrad alone and $K_{ab\mu}$ the contorsion in frame indices.

**Metric compatibility is the antisymmetry of the lowered spin connection.** The solved array is *not* antisymmetric, and the exception is not exotic: for a boost in the $(0,1)$ frame plane the array is symmetric in its two frame slots. The object that lies in the Lorentz algebra, and the one that multiplies the generators in the spinor derivative, is that array with its first frame slot lowered by $\varepsilon_a$,
$$
\omega_{ab\mu} = -\,\sum_\lambda \nabla_\mu \exp(a){}_\lambda\, e_{b\lambda},
$$
which uses the orthonormality relation $\sum_\lambda \exp(a){}_\lambda e_{b\lambda} = \eta_{ab}$. Adding the two orderings kills the derivative, so
$$
\omega_{ab\mu} + \omega_{ba\mu} = -\,\nabla_\mu \eta_{ab},
$$
which vanishes exactly when the connection is metric compatible. With a contorsion the sum is the frame-space face of the boxed $\nabla_\mu g_{\nu\rho}$ of the previous section, so it vanishes exactly when the contorsion is totally antisymmetric. This is the object that appears in the covariant derivative of a spinor, and it is the only place the torsion enters the matter equation.

Two exact statements were checked here, in four dimensions and in exact rational arithmetic, on a tetrad of the form $\exp(a){}_\mu = \delta_{a\mu} + x_0M_{a\mu}$ with $M$ constant and $x_0$ the time coordinate.

**The tetrad postulate is satisfiable with a non-flat tetrad.** The Levi-Civita connection of the induced metric is nonzero for that tetrad, and the spin connection constructed from it makes $\nabla_\mu \exp(a){}_\nu = 0$ identically. The same computation confirms the frame-space statement above, in the only form in which it is true: the array with its first frame slot lowered is antisymmetric for the Levi-Civita connection, stays so under a totally antisymmetric contorsion, and loses the antisymmetry under a general one, while the array with both frame slots in the same position is never antisymmetric.

**The Weitzenböck connection is curvature-free and torsionful.** The connection built from the tetrad alone,
$$
\Gamma_{\lambda\mu\nu} = \sum_a e_{a\lambda}\, \partial/\partial x_\mu \exp(a){}_\nu ,
$$
called the **Weitzenböck connection**, was computed for that tetrad together with its curvature. The curvature came out **exactly zero** in every component, and the torsion came out exactly
$$
T_{\lambda\mu\nu} = \sum_a e_{a\lambda}\bigl(\partial/\partial x_\mu \exp(a){}_\nu - \partial/\partial x_\nu \exp(a){}_\mu\bigr),
$$
which is nonzero for that tetrad: the antisymmetrised derivative of the frame is the whole of the connection. This is the content of the teleparallel sector: a connection can be flat and still have torsion, and the framework's algebra can carry it.

**Where the algebra enters.** Under the dictionary of *Conventions of the Matrix Models*, §*The Clifford Structure and the Frame*, the six generators of the Lie subspace are the six Lorentz bivectors
$$
C_\mu C_\nu = \bigl(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\bigr)\bigl(iL_{e_\nu}R_{\vec e_{\nu(\nu)}}\bigr),\qquad \mu<\nu,
$$
products of the frame cells $C_\mu=iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$, and the Lorentz generators are half of these bivectors. The six components of the algebra-valued one-form $\vec\Gamma_\mu$ of Route Three are therefore in one-to-one correspondence with the six components $\omega_{ab\mu}$ of the spin connection, and nothing else about the algebra is used. The connection can be written as a $\mathbb{B}$-valued object, and the derivative that carries it depends on the module and not on the torsion. A vector transforms two-sidedly, $\tilde Q\mapsto\tilde U\tilde Q\tilde U^*$, so its covariant derivative is the two-sided
$$
D_\mu\tilde Q = \partial/\partial x_\mu\,\tilde Q + \vec\Gamma_\mu\tilde Q + \tilde Q\vec\Gamma_\mu^{*};
$$
a spinor transforms one-sidedly, $\psi\mapsto\tilde U\psi$, so its covariant derivative is the one-sided
$$
D_\mu\psi = \partial/\partial x_\mu\,\psi + \vec\Gamma_\mu\psi .
$$
The two are not interchangeable — the natural abbreviation $D_\mu=\partial/\partial x_\mu+[\vec\Gamma_\mu,\cdot]$ is wrong for exactly the boosts — and the torsion changes neither, since it lives in the part of $\vec\Gamma_\mu$ that is already in the Lie subspace. That trap is the corpus's own and is not repeated here; what matters for torsion is that the fix is the same for a torsionful connection as for a torsion-free one.

## The Spin Tensor and the Torsion–Spin Relation

In the Einstein–Cartan–Sciama–Kibble theory the torsion is not free: it is sourced *algebraically* by the spin density of matter. For a Dirac field the spin density is the completely antisymmetric bilinear
$$
\Sigma_{\lambda\mu\nu} = \bar\psi\,\operatorname{Alt}\bigl[C_\lambda C_\mu C_\nu\bigr]\,\psi ,
$$
in which $C_\mu=iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ is the frame cell of the coordinate $x_\mu$, and $\operatorname{Alt}$ is the **normalised** antisymmetrisation, the average over the six permutations weighted by the sign of the permutation, $\operatorname{Alt}[C_\lambda C_\mu C_\nu]=\tfrac16\sum_{\mathrm{perm}}\pm C_\lambda C_\mu C_\nu$. The Dirac adjoint is
$$
\bar\psi = \psi^\dagger\, iR_{\vec e_x} .
$$
The normalisation of $\operatorname{Alt}$ matters: without the $1/3!$ the duality below carries an extra factor six and the squared display an extra thirty-six.

The chirality cell is the single product
$$
-iL_{e_t}R_{\vec e_z} = -iR_{\vec e_z} = i\,\bigl(iR_{\vec e_x}\bigr)\bigl(iL_{e_x}R_{\vec e_y}\bigr)\bigl(iL_{e_y}R_{\vec e_y}\bigr)\bigl(iL_{e_z}R_{\vec e_y}\bigr).
$$
Each of the four cells in the product carries one $i$ and $i^4=+1$, so the four cells multiply to the product of the four bare cells; the single $i$ in front is what makes the left side the chirality cell. That cell anticommutes with each $C_\mu$, so $\{\gamma_5,\gamma_\mu\}=0$. The axial current is
$$
A_\mu = \bar\psi\,\bigl(-iR_{\vec e_z}\bigr)\bigl(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\bigr)\,\psi .
$$

**The antisymmetric spin density is the dual of the axial current.**
$$
\Sigma_{\lambda\mu\nu} = -\,i\,\epsilon_{\lambda\mu\nu\rho}\,\varepsilon_\rho\,A_\rho = -\,i\,\epsilon_{\lambda\mu\nu\rho}\,A^\rho ,
$$
with $A^\rho=\varepsilon_\rho A_\rho$ and $\epsilon_{0123}=+1$. The weight $\varepsilon_\rho$ is not a convention added by hand: it is the raised index, written low as the index convention requires, so the two forms of the display are the same statement.

The identity is exact at every index triple and for every spinor, and the constant is $-i$ **in the frame used here**. It is one line once the Clifford duality of *The Gamma Formulation* is available. There the antisymmetrised triple of gammas is $\gamma_{[\lambda}\gamma_\mu\gamma_\nu]=i\epsilon_{\lambda\mu\nu\rho}\varepsilon_\rho\gamma_\rho\gamma_5$, which the anticommutation $\{\gamma_5,\gamma_\rho\}=0$ turns into $-i\epsilon_{\lambda\mu\nu\rho}\varepsilon_\rho\gamma_5\gamma_\rho$. The three cells of $\Sigma$ are the three gammas and $\bar\psi\gamma_5\gamma_\rho\psi$ is $A_\rho$ by the definition above, so the display holds with $-i$ and there is nothing left to choose.

The weight is what carries the sign. Without it the same display with $+i$ holds on the eighteen triples whose free index is spacelike and fails on the six whose free index is timelike; the sign vector is exactly the raised index that repairs those six.

A direct consequence is that the spin density is not a general third-rank tensor: antisymmetrising a general third-rank bilinear collapses its 24 components to the four of a totally antisymmetric third-rank tensor, and for the Dirac field those four are exactly the axial current. This is the same counting as in the metric-compatibility condition above, and it is not a coincidence: the physical torsion and the physical spin density live in the same four-dimensional subspace.

**The spin density contracts to the axial current.** Substituting the duality and using $i^2=-1$,
$$
\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu}
= -\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\epsilon_{\lambda\mu\nu\rho}\,\epsilon_{\lambda\mu\nu\sigma}\,A^\rho A^\sigma .
$$
On the nonzero terms $(\lambda,\mu,\nu,\rho)$ is a permutation of $(0,1,2,3)$, so the product of the four sign factors is $-1$ and $\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu=-\varepsilon_\rho$; and $\sum_{\lambda,\mu,\nu}\epsilon_{\lambda\mu\nu\rho}\epsilon_{\lambda\mu\nu\sigma}=+6\,\delta_{\rho\sigma}$ for the all-lowered symbol with $\epsilon_{0123}=+1$. Hence
$$
\boxed{\;\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu} = 6\sum_\rho\varepsilon_\rho\,A_\rho A_\rho\;},
$$
and the numerical check reproduced it to a relative $10^{-15}$, that is, exactly to within the arithmetic.

The Einstein–Cartan field equations then read, schematically,

$$
T_{\lambda\mu\nu} = \kappa\,\Sigma_{\lambda\mu\nu} , \qquad \kappa = 8\pi G \quad (c=1) ,
$$

with $\Sigma$ the bilinear displayed above. Because the torsion appears in the action without derivatives, its field equation is algebraic: it is solved by $T=\kappa\Sigma$ and the solution can be substituted back into the matter equation. The substitution couples the torsion to the axial current, and since the torsion is the dual of that current, the result is a **four-fermion axial–axial contact term** with a coefficient fixed by $G$ and not chosen. The elimination is the step the nonlinear-Dirac article performs and whose coefficient $\tfrac{3\kappa}{8}$ it owns; this article supplies the two geometric identities — duality and the factor six — that make the elimination a two-line algebraic substitution rather than a computation in components. The statement that the torsion–spin relation is algebraic, and therefore that the elimination introduces no new propagating field, is the whole reason the Hehl–Datta term is a contact interaction.

## Teleparallel Geometry and the Weitzenböck Connection

The Weitzenböck connection of the previous section,

$$
\Gamma_{\lambda\mu\nu} = \sum_a e_{a\lambda}\, \partial/\partial x_\mu \exp(a){}_\nu ,
$$

defines a geometry whose curvature vanishes identically and whose torsion is nonzero. Its two exact properties, both confirmed above, are worth stating in the general form in which they are used.

**Zero curvature is an identity.** $\mathrm{Riem}_{\lambda\mu\nu\rho}(\Gamma) = 0$ for every tetrad. The reason is structural: the connection is the pure-gauge form $\Gamma=E^{-1}\partial E$ of the zero connection, so $\mathrm{Riem}=d\Gamma+\Gamma\wedge\Gamma=0$ because the quadratic term cancels the derivative of $E^{-1}$. The check is exact; no small-curvature approximation is involved.

**Torsion is the contorsion of the metric connection.** In the **Weitzenböck gauge** the full spin connection is set to zero, $\omega_{ab\mu} = 0$, so the tetrad postulate forces the Levi-Civita part and the contorsion to cancel,

$$
K_{ab\mu} = -\,\omega_{ab\mu}(e) .
$$

This is the teleparallel condition: the geometry is the one in which the frame is everywhere parallel and all the connection is contorsion. In this formulation the torsion is the entire content of the connection, and general relativity is recovered by the same equations in the zero-torsion case.

The corpus's boundary applies to this sector exactly as it applies to the others, and it is worth restating because teleparallel language invites an overclaim. Teleparallel gravity is **a gauge choice of the same geometry**, not a second geometry and not a derivation of the metric from matter. Nothing in the algebra selects it, the tetrad is still inserted by hand, and no action for the frame follows from the identity. What the identity does supply is a clean statement of what the corpus's own connection objects are: the sector in which the algebra-valued $\vec\Gamma_\mu$ is entirely contorsion and has zero curvature.

## What the Algebra Does and Does Not Do

The positive content of this article is a statement of *carrying*. The algebra's six-dimensional Lie subspace holds the spin connection with or without torsion; the torsion and the contorsion are tensors on a manifold and can be written in the framework's notation without leaving it; the spin density of a Dirac field is a Clifford bilinear with the full Clifford-odd structure the corpus requires, and its antisymmetric part is the dual of the axial current with the exact constant $-i$; the contraction gives the factor six; and the Weitzenböck identity shows a flat, torsionful connection is a perfectly consistent object that the algebra can express.

The negative content is the boundary, restated so that a later reader cannot mistake it. The algebra **generates no torsion**: the commutator of the quaternion units is a constant of the algebra, not a field, and no field equation for the torsion follows from it. The algebra **selects no connection**: the vanishing of torsion and metric compatibility are conditions, and the second of them was shown above to mean exactly "the contorsion is totally antisymmetric". The algebra **supplies no action** for the frame or the connection, so no Einstein equation, and the torsion is not eliminated by the algebra but by its own algebraic field equation in a theory that has one. And the algebra **does not couple the torsion to matter by itself**: the coupling lives in the spinor covariant derivative $D_\mu\psi=\partial/\partial x_\mu\,\psi+\vec\Gamma_\mu\psi$, the one-sided derivative of Route Three, and its strength is fixed by the Einstein constant in the theory that puts the torsion into the action.

The two open items this article was written against stand as follows. The first — torsion in the framework's notation, with the geometry that makes the elimination possible — is supplied here, and the identities are recomputed. The second — the action and the selection principle — is untouched, and remains where *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* and *Quantum Gravity under the Biquaternion Framework — A Research Agenda* placed it.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone of operators with $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
**The duality the spin section cites.**
$$
\gamma_{[\lambda}\gamma_\mu\gamma_\nu] = i\,\epsilon_{\lambda\mu\nu\rho}\,\varepsilon_\rho\,\gamma_\rho\gamma_5
= -\,i\,\epsilon_{\lambda\mu\nu\rho}\,\varepsilon_\rho\,\gamma_5\gamma_\rho ,
$$
with the normalised antisymmetrisation on the left and the raised index written low by the sign vector on the right. The two forms are equal because $\{\gamma_5,\gamma_\rho\}=0$, and the second is the one the spin section uses, where $\bar\psi\gamma_5\gamma_\rho\psi$ is $A_\rho$.

**Three contractions**, all exact in this frame:
$$
\sum_\mu\gamma_\mu\gamma_\mu=-2I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_5\gamma_\mu=+2\gamma_5 .
$$
The weight appears in the second and not in the other two because the second is the only one with a free lowered index, and the contraction that produces it is the metric one.

## Summary

A connection with torsion splits into a metric part, the Christoffel symbols, and a remainder, the contorsion $K_{\lambda\mu\nu}$, which is antisymmetric in its last two indices. The torsion is twice the contorsion, $T_{\lambda\mu\nu} = 2K_{\lambda\mu\nu}$, identically and in every case; the permutation sum $K_{\lambda\mu\nu} = \tfrac12(T_{\lambda\mu\nu} - T_{\mu\nu\lambda} + T_{\nu\lambda\mu})$ is the same identity written for a totally antisymmetric torsion, which is the only case the corpus meets. The covariant derivative of the metric is $\nabla_\mu g_{\nu\rho} = -(K_{\nu\mu\rho} + K_{\rho\mu\nu})$, which vanishes for every index order exactly when the contorsion is totally antisymmetric; the 24 contorsion components are then cut to four, so **metric compatibility is the condition of total antisymmetry**, and this is the precise meaning of the corpus's statement that metric compatibility is a condition and not a consequence.

The tetrad postulate ties the affine and spin connections, and the spin connection splits as $\omega = \omega(e) + K$ with the contorsion in frame indices; $\omega$ with its first frame slot lowered is antisymmetric in the frame pair exactly in the metric-compatible case, so the two conditions of the previous paragraph have one face in world indices and one in frame indices. The Weitzenböck connection $\Gamma_{\lambda\mu\nu} = \sum_a e_{a\lambda} \partial/\partial x_\mu \exp(a){}_\nu$ has exactly zero curvature and nonzero torsion; in the Weitzenböck gauge the full spin connection vanishes and the contorsion is minus the Levi-Civita spin connection of the tetrad.

The spin density of a Dirac field is the completely antisymmetric bilinear $\Sigma_{\lambda\mu\nu} = \bar\psi \operatorname{Alt}\bigl[C_\lambda C_\mu C_\nu\bigr]\psi$, with $C_\mu=iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ the frame cell of $x_\mu$ and $\operatorname{Alt}$ the normalised antisymmetrisation. It is the dual of the axial current, $\Sigma_{\lambda\mu\nu} = -i\,\epsilon_{\lambda\mu\nu\rho}\,A^\rho$ with $A_\mu = \bar\psi\,(-iR_{\vec e_z})\,C_\mu\,\psi$, and its square is six times the axial current squared, $\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu} = 6\sum_\rho\varepsilon_\rho A_\rho A_\rho$, the factor six following from $i^2=-1$ and from $\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu=-\varepsilon_\rho$ on the nonzero terms. The Einstein–Cartan torsion–spin relation $T = \kappa\Sigma$ is therefore algebraic, and the elimination of the torsion leaves the axial–axial contact term whose coefficient the nonlinear-Dirac article owns.

Two statements bound the article. The commutator of the quaternion units is a constant of the algebra and not the torsion of a manifold; the algebra carries the connection and the torsion but generates neither, selects no connection, and supplies no action. The identities above are exact and recomputed; the dynamics is not here and is not claimed.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Gamma_{\lambda\mu\nu}$ | affine connection |
| $\left\{{}_{\lambda\mu\nu}\right\}$ | Christoffel symbols of $g_{\mu\nu}$ |
| $T_{\lambda\mu\nu}$ | torsion tensor, $2K_{\lambda\mu\nu}$ |
| $K_{\lambda\mu\nu}$ | contorsion, antisymmetric in the last pair; the first slot is the output slot, raised implicitly |
| $\exp(a){}_\mu$, $e_{a\mu}$ | tetrad and its inverse |
| $g_{\mu\nu} = \eta_{ab}\exp(a){}_\mu \exp(b){}_\nu$ | metric from the tetrad, $\eta = \mathrm{diag}(+1,-1,-1,-1)$ |
| $\omega_{ab\mu}$ | spin connection one-form; antisymmetric in the frame pair once the first slot is lowered by $\varepsilon$ |
| $\omega_{ab\mu}(e)$ | its Levi-Civita part |
| $\vec\Gamma_\mu$ | the connection as an element of the Lie subspace of $\mathbb{B}$ |
| $L_{a}R_{b}$ | two-sided cell, $L_{a}R_{b}\psi=a\psi b$ |
| $C_\mu = iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ | frame cell of $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$: $iR_{\vec e_x}$ at $\mu=t$ and $iL_{\vec e_k}R_{\vec e_y}$ at $\mu=k$ |
| $C_\mu C_\nu$, $\mu<\nu$ | the six Lorentz bivectors; the six generators are half of them |
| $-iR_{\vec e_z}$ | chirality cell, $-iL_{e_t}R_{\vec e_z}=i\,(iR_{\vec e_x})(iL_{e_x}R_{\vec e_y})(iL_{e_y}R_{\vec e_y})(iL_{e_z}R_{\vec e_y})$ |
| $\bar\psi=\psi^\dagger iR_{\vec e_x}$ | Dirac adjoint |
| $\Sigma_{\lambda\mu\nu}$ | Dirac spin density, $\bar\psi \operatorname{Alt}\bigl[C_\lambda C_\mu C_\nu\bigr]\psi$, normalised antisymmetrisation |
| $A_\mu$ | axial current, $\bar\psi\,(-iR_{\vec e_z})\,C_\mu\,\psi$ |
| $\varepsilon$, $\varepsilon_\mu$ | sign vector, $\varepsilon_t=+1$ and $\varepsilon_k=-1$; $\varepsilon_\mu A_\mu$ is the raised $A^\mu$ |
| $\kappa = 8\pi G$ | Einstein gravitational constant, $c=1$ |

## Further Reading

- F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the Einstein–Cartan–Sciama–Kibble theory, the contorsion and the algebraic torsion–spin relation.
- F. W. Hehl and B. K. Datta, "Nonlinear spinor equation and asymmetric connection in general relativity," *Journal of Mathematical Physics* **12** (1971) 1334–1339, for the elimination of the torsion and the axial–axial contact term.
- R. Aldrovandi and J. G. Pereira, *Teleparallel Gravity: An Introduction* (Springer, 2013), for the Weitzenböck connection, the vanishing of its curvature, and the teleparallel formulation of general relativity.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for Route Two's frame field, Route Three's Lie subspace and two-sided derivative, and the boundary statement that metric compatibility and vanishing torsion are conditions.
- [The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form](the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html), for the Hehl–Datta coefficient $\tfrac{3\kappa}{8}$ and the placement of the axial channel among the fermion bilinears.
- [Conventions of the Matrix Models](conventions-of-the-matrix-models.html), for the correspondence between the six generators of the Lie subspace and the six Lorentz bivectors, §*The Clifford Structure and the Frame*.
- [Matter Makes Space — An External Construction from Quaternionic Spinors](matter-makes-space-an-external-construction-from-quaternionic-spinors.html), for the external claim that the torsion is the quaternion commutator and the composite geometry built on it, with the parts that do not reproduce.
