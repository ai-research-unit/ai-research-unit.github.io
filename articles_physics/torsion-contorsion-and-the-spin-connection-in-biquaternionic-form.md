# __Torsion, Contorsion and the Spin Connection in Biquaternionic Form__

## Introduction

The corpus's gravity series already carries a connection. Route Three of *Curved Spacetime and the Biquaternion Framework* shows that the Lie algebra of the rotor group is the six-dimensional traceless subspace of $\mathbb{B}$, the span of the rotation generators $\vec e_k$ and the boost generators $i\vec e_k$, so that a spin connection one-form $\vec\Gamma_\mu$ and its curvature are objects the algebra can hold in its own notation. That article then states its boundary exactly: **metric compatibility and the vanishing of torsion are conditions, not consequences; nothing in the algebra selects the Levi-Civita lift.** A second article names the missing piece outright. *The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form* lists, among the open items it inherits, "torsion in the framework's own notation": the antisymmetric part of the connection, and the algebraic elimination that produces the Hehl–Datta term, are not written in the framework's notation. This article supplies that item.

The article has one job. It gives the geometry of a **connection with torsion** — the torsion tensor, the contorsion, the tetrad postulate, the spin connection with torsion, the spin tensor of a Dirac field, the elimination of a non-propagating torsion, and the Weitzenböck or teleparallel connection — in the corpus's notation and with exact checks. It is a geometry article, not a dynamics article. It builds no action, selects no connection, and claims no field equation; those remain where *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* left them. It does not own the Hehl–Datta coefficient, which belongs to the nonlinear-Dirac article, and it does not own the four-fermion self-interaction as a physical model. What it adds is the chain of identities that makes the elimination step possible and states exactly what the corpus's phrase "vanishing torsion is a condition" means.

One warning belongs in the introduction, because a reader who has seen an external construction may expect the opposite. There is a claim in the literature that the torsion of spacetime *is* the commutator of the quaternionic units, and that the tetrad and the contorsion are bilinear composites of one biquaternion-valued field, so that geometry emerges from matter. That construction is recorded and tested separately, in *Matter Makes Space — An External Construction from Quaternionic Spinors*, where the parts that do not reproduce are listed. Nothing in this article depends on it. Here the torsion is an independent tensor field, exactly as in the standard Einstein–Cartan–Sciama–Kibble programme, and the algebra's role is only that its Lie subspace can carry the connection.

**Index convention.** Every display is all-low. In the three-index objects $\Gamma_{\lambda\mu\nu}$, $T_{\lambda\mu\nu}$ and $N_{\mathrm{cont},\lambda\mu\nu}$ the first index is the output, the second is the direction of the derivative and the third is the index of the differentiated object — which is why the tetrad postulate below reads $\partial/\partial x_\mu\exp(a){}_\nu-\Gamma_{\lambda\mu\nu}\exp(a){}_\lambda$, and why the torsion, the antisymmetric part in that pair, is the object of the first section. $\mathrm{Riem}_{\lambda\mu\nu\rho}$ reads the output first, then the index of the differentiated object, then the two derivative directions, and it is antisymmetric in those last two. In the mixed frame-and-world objects $\exp(a){}_\mu$, $e_{a\mu}$, $\omega^{a}{}_{b\mu}$ and its lowered form $\omega_{ab\mu}$, the frame slot comes first. In an identity the same label appears on both sides, so it names a free index and is not summed; a contraction is always written with an explicit $\sum$, and carries the sign vector $\varepsilon$ where the contraction is the metric one: $\varepsilon_t=+1$ and $\varepsilon_k=-1$, so that $\varepsilon_\mu A_\mu$ is the component $A^\mu$ in the frame, where $g=\eta$. A raised label appears only where the object is defined that way — $A^\rho$ for the axial current and $\omega^{a}{}_{b\mu}$ for the spin connection as solved — and each display that uses one gives the lowering beside it, $A^\rho=\varepsilon_\rho A_\rho$ and $\omega_{ab\mu}=\varepsilon_a\omega^{a}{}_{b\mu}$, so that no result depends on which of the two is written. In a general chart the raising is done by the inverse metric, which is written out explicitly, as in the Christoffel symbols of the next section.

**The two conventions of the article.** The geometry is written in tensors on a manifold, with the index convention above. The algebra enters in two places: the Lie subspace of §*The Tetrad Postulate and the Spin Connection*, which carries the connection, and the pairing of §*The Spin Tensor and the Torsion–Spin Relation*, which is built from four actions, the frame cells of the four coordinate directions. The frame cell of the coordinate $x_\mu$ is the action

$$
Q\ \longmapsto\ i\,e_\mu\,Q\,\vec e_{\nu(\mu)},\qquad \nu(t)=x,\qquad \nu(k)=y,
$$

on an element $Q$ of $\mathbb{B}$; the four are the frame cells of the axis-free display of *Conventions of the Matrix Models*. Each cell carries its own factor $i$, so a product of two of them brings one sign flip and no display below counts a minus sign twice. The timelike cell is the one-sided action $Q\mapsto iQ\vec e_x$, the three spatial cells are two-sided. No letter stands for a cell, the matrix conventions having retired the letter that once did, so none is introduced here: the action is written out where the operand is the subject, and the cells are written out again, on the element, where the spin density is read. The older display of the same four operators is printed once, in the gamma section below, and nothing before that section needs it.

## The Torsion Tensor

An affine connection $\Gamma_{\lambda\mu\nu}$ need not be symmetric under the exchange of its two last labels. Its antisymmetric part is the **torsion tensor**,

$$
T_{\lambda\mu\nu} = \Gamma_{\lambda\mu\nu} - \Gamma_{\lambda\nu\mu} .
$$

Both the connection and the torsion are objects of the *same* manifold and the *same* index structure; the torsion is simply the part of the connection that a symmetric connection would discard. It is a tensor, and it is antisymmetric in its last two indices by construction. In four dimensions that leaves $4 \times 6 = 24$ independent components, the same count as for the contorsion below.

Two remarks keep the object honest.

First, **the torsion sees only part of the connection.** Writing $\\Gamma=\\{\\,\\}+N_{\mathrm{cont}}$ with $\{\,\}$ the Christoffel symbols of the metric, the torsion is the antisymmetric part of $N_{\mathrm{cont}}$ in the last pair and nothing else, so the symmetric part of $N_{\mathrm{cont}}$ in that pair is invisible to it. Whether that part vanishes, and whether $N_{\mathrm{cont}}$ itself vanishes, are separate questions, answered by the field equations and not by the algebra.

Second, **the algebra does not produce a torsion tensor.** The biquaternion units have commutators, and the commutator of two of them is again an element of the algebra. That is a statement about a constant algebra; the torsion is a field on a manifold, changing from point to point, transforming as a tensor. The two objects have the same index count and different natures, and the conflation of them is the central error of the external construction recorded in *Matter Makes Space*. The corpus's own position — that the connection can be *carried* in the Lie subspace but is not *generated* by the algebra — is the one used here.

## Contorsion: the Torsionful Part of the Connection

Write the connection as a metric part plus a remainder,

$$
\Gamma_{\lambda\mu\nu} = \left\{{}_{\lambda\mu\nu}\right\} + N_{\mathrm{cont},\lambda\mu\nu} ,
$$
where the Christoffel symbols of the metric are
$$
\left\{{}_{\lambda\mu\nu}\right\} = \tfrac12\sum_\rho (g^{-1})_{\lambda\rho}\bigl(\partial/\partial x_\mu\, g_{\nu\rho} + \partial/\partial x_\nu\, g_{\mu\rho} - \partial/\partial x_\rho\, g_{\mu\nu}\bigr) .
$$

The remainder $N_{\mathrm{cont},\lambda\mu\nu}$ is the **contorsion** (or contortion; the two names are interchangeable and the first is used throughout).

**One slot is raised implicitly.** The Christoffel display carries an explicit $(g^{-1})_{\lambda\rho}$, and the same convention runs through $\Gamma$, $T$ and $N_{\mathrm{cont}}$: the first slot is the output slot, stored with the inverse metric already applied. That is why the tetrad postulate of the next section contracts $\Gamma_{\lambda\mu\nu}$ with $\exp(a){}_\lambda$ and needs no further $g^{-1}$. The place where the metric enters the other way is the metric-compatibility block below, and every display in that block — the boxed relation, the Einstein–Cartan contorsion and its properties — is read in the all-lowered way, with the first slot lowered by $g_{\lambda\sigma}$. Total antisymmetry is a statement about that lowered array, whereas antisymmetry in the last pair holds in either position, because the first slot is not involved.

The exact facts about $N_{\mathrm{cont}}$ are short.

**The torsion fixes only the antisymmetric part of the remainder.** Taking the antisymmetric part of the split in the last pair gives
$$
T_{\lambda\mu\nu} = \Gamma_{\lambda\mu\nu} - \Gamma_{\lambda\nu\mu} = N_{\mathrm{cont},\lambda\mu\nu} - N_{\mathrm{cont},\lambda\nu\mu} ,
$$
and that is the whole of what the torsion says about $N_{\mathrm{cont}}$: it fixes $\tfrac12(N_{\mathrm{cont},\lambda\mu\nu}-N_{\mathrm{cont},\lambda\nu\mu})$ and leaves $N_{\mathrm{cont},\lambda(\mu\nu)}$ free. A general connection has sixty-four components, of which twenty-four are that antisymmetric part and forty are a symmetric remainder, the non-metricity. The torsion is blind to the forty, and the Christoffel symbols alone do not exhaust them.

**Metric compatibility picks exactly one connection per torsion.** With the metric lowering the first slot,
$$
\boxed{\;\nabla_\mu g_{\nu\rho} = -\left(g_{\nu\lambda}N_{\mathrm{cont},\lambda\mu\rho} + g_{\rho\lambda}N_{\mathrm{cont},\lambda\mu\nu}\right)\;}
$$
is an identity for *any* $N_{\mathrm{cont}}$, symmetric remainder included, so metric compatibility is the single condition
$$
N_{\mathrm{cont},\lambda\mu\nu} = -\,N_{\mathrm{cont},\nu\mu\lambda} ,
$$
antisymmetry in the first and third slots. Two conditions on a sixty-four-component object — the twenty-four of the torsion and these — have a unique joint solution, and it is
$$
N_{\mathrm{cont},\lambda\mu\nu} = \tfrac12\bigl(T_{\lambda\mu\nu} - T_{\mu\nu\lambda} + T_{\nu\lambda\mu}\bigr) .
$$
This is the **contorsion of the Einstein–Cartan programme**, and it is exact for any torsion, totally antisymmetric or not. Three properties were checked on random torsions, with the first slot lowered: the antisymmetrised difference of the array returns $T$, the array is antisymmetric in its first and third slots so that $\nabla_\mu g_{\nu\rho}=0$, and it is the only array with both properties. The Weitzenböck connection of *Teleparallel Geometry* is the case that shows the formula is not merely formal: its contorsion, lowered, is exactly this array.

**The torsion is twice the contorsion exactly in the totally antisymmetric case.** Antisymmetry of $N_{\mathrm{cont}}$ in the last pair is a third condition, and the array above satisfies it exactly when the torsion is totally antisymmetric. Then the three cyclic terms in the display coincide, $T_{\lambda\mu\nu}=T_{\mu\nu\lambda}=T_{\nu\lambda\mu}$, the array collapses to
$$
N_{\mathrm{cont},\lambda\mu\nu} = \tfrac12 T_{\lambda\mu\nu} ,
$$
antisymmetric in all three slots, and the map between torsion and contorsion becomes one-to-one on twenty-four components. Away from total antisymmetry the inverse is the general display, not $\tfrac12T$, and $T=2N_{\mathrm{cont}}$ fails: it is an identity of the sector in which $N_{\mathrm{cont}}$ is antisymmetric in its last pair, not of connections in general.

**The sector the corpus uses.** Writing $T=2N_{\mathrm{cont}}$ throughout is the choice of the split in which the Christoffel symbols are the whole symmetric part of the connection, $N_{\mathrm{cont},\lambda(\mu\nu)}=0$; the article uses it from here on, and it is a choice, not a consequence of the torsion. Inside it, metric compatibility is one extra condition, and it can be read off the Einstein–Cartan display: the unique metric-compatible array must also be antisymmetric in the last pair, which forces the torsion to be totally antisymmetric. The count agrees: the 24 contorsion components are cut to the **four** of a totally antisymmetric third-rank tensor in four dimensions, so twenty of the conditions are independent, and the map from the 24 to $\nabla g$ has rank twenty. The corpus's sentence "metric compatibility is a condition, not a consequence" therefore reads, with precision:

> Demanding that the metric be covariantly constant, in the sector in which the torsion is twice the contorsion, is exactly the demand that the contorsion be totally antisymmetric; in that case neither object has any other part, and both carry four components.

The other twenty components are the ones that break metric compatibility, *within the sector*. They are not forbidden by anything the algebra says; they are simply not selected, and the framework's statements about a metric would have to be re-examined if they were present.

One qualifier holds the whole of this section together, because the literature reads the same words two ways. Outside the sector — with the symmetric remainder kept — metric compatibility and total antisymmetry **come apart**: every torsion has exactly one metric-compatible connection, and when the torsion is not totally antisymmetric that connection's contorsion carries a symmetric part. The Einstein–Cartan programme therefore lives on both sides of the boundary: its connection is always metric compatible, and its contorsion is antisymmetric in the last pair only for the totally antisymmetric torsions. That last case is the one the corpus meets physically, and in it every statement above agrees at once. The spin density of a Dirac field is totally antisymmetric (*The Spin Tensor and the Torsion–Spin Relation* computes it), and the torsion it sources is proportional to it, hence totally antisymmetric too, so for that source the contorsion is $\tfrac12T$, antisymmetric in all three slots, metric compatibility and total antisymmetry hold together, and the sector of this article is no restriction at all. The general contorsion is needed only to state what has been excluded, and why the exclusion is a condition rather than a consequence.

## The Tetrad Postulate and the Spin Connection

The tetrad $\exp(a){}_\mu$ relates the coordinate and frame indices, with inverse $e_{a\mu}$ defined by
$$
\sum_\mu\exp(a){}_\mu e_{b\mu} = \delta_{ab},\qquad \sum_a\exp(a){}_\mu e_{a\nu} = \delta_{\mu\nu},
$$
and it builds the metric as $g_{\mu\nu} = \sum_{a,b}\delta_{ab}\,\exp(a){}_\mu \exp(b){}_\nu$, which is the unit metric $\delta_{\mu\nu}$ for the identity tetrad. The frame pair of a frame-indexed object is lowered with $\varepsilon_a$, so a repeated frame label is summed with $\varepsilon$ exactly as a repeated world label is. A connection on the frame bundle is a one-form $\omega_{ab\mu}$, and the two connections are tied by the **tetrad postulate**,

$$
\nabla_\mu \exp(a){}_\nu = \partial/\partial x_\mu \exp(a){}_\nu - \sum_\lambda\Gamma_{\lambda\mu\nu} \exp(a){}_\lambda + \sum_b\omega_{ab\mu} \exp(b){}_\nu = 0 ,
$$

which says that the frame is covariantly constant in both connections at once. Solved for the spin connection — the array that results carries its first frame slot raised — with the tetrad $\exp(a){}_\lambda$ in the first slot and the inverse $e_{b\nu}$ in the second, it reads
$$
\omega^{a}{}_{b\mu} = \sum_{\lambda,\nu}\exp(a){}_\lambda \Gamma_{\lambda\mu\nu} e_{b\nu} + \sum_\lambda\exp(a){}_\lambda\, \partial/\partial x_\mu\, e_{b\lambda} ,
$$
with $\Gamma_{\lambda\mu\nu}$ the connection of the previous sections, contorsion included.

Splitting the affine connection into its metric and contorsion parts splits the spin connection the same way,
$$
\omega^{a}{}_{b\mu} = \omega^{a}{}_{b\mu}(e) + N_{\mathrm{cont}}{}^{a}{}_{b\mu} ,
\qquad
N_{\mathrm{cont}}{}^{a}{}_{b\mu} = \sum_{\lambda,\nu}\exp(a){}_\lambda\, N_{\mathrm{cont},\lambda\mu\nu}\, e_{b\nu} ,
$$
with $\omega^{a}{}_{b\mu}(e)$ the Levi-Civita spin connection of the tetrad alone and $N_{\mathrm{cont}}{}^{a}{}_{b\mu}$ the contorsion in frame indices.

**Metric compatibility is the antisymmetry of the lowered spin connection.** The solved array $\omega^{a}{}_{b\mu}$ is *not* antisymmetric. Even in the metric-compatible case, where the lowered array is antisymmetric, the two are related by $\omega^{a}{}_{b\mu}=-\varepsilon_a\varepsilon_b\,\omega^{b}{}_{a\mu}$, so the raw array is symmetric on the three boost pairs and antisymmetric on the three spatial pairs. The object that lies in the Lorentz algebra, and the one that multiplies the generators in the derivative of the field, is the antisymmetric part of the array with its first frame slot lowered. Write $\omega_{ab\mu}=\varepsilon_a\,\omega^{a}{}_{b\mu}$ for the lowered array, antisymmetric exactly in the metric-compatible case; from here on $\omega_{ab\mu}$ without a raised label means it. Write $E_{a\mu}=\varepsilon_a\exp(a){}_\mu$ for the lowered tetrad and $\mathrm{D}_\mu$ for the affine covariant derivative, which acts on the world label only and carries no frame rotation. Then
$$
\omega_{ab\mu} = -\,\sum_\lambda \mathrm{D}_\mu E_{a\lambda}\; e_{b\lambda},
$$
and the orthonormality relation it rests on is
$$
\sum_\lambda E_{a\lambda}\, e_{b\lambda} = \varepsilon_a\delta_{ab},
$$
in which the lowering matters: without the factor $\varepsilon_a$ the same sum is $\delta_{ab}$, and it is the two signs of the weight that the antisymmetry statement is about.

The sum $\omega_{ab\mu}+\omega_{ba\mu}$ is the frame-space carrier of the non-metricity, and it vanishes exactly when $\nabla_\mu g_{\nu\rho}$ does: the lowered array is antisymmetric in the frame pair exactly when the lowered contorsion is antisymmetric in the first and third world slots, which is the condition of the contorsion section. What does *not* follow outside that sector is the further step to total antisymmetry, and the Weitzenböck connection of *Teleparallel Geometry* is the case that shows it: the array vanishes there while the torsion is not totally antisymmetric. What it is *not* is the plain frame image of $\nabla_\mu g_{\nu\rho}$, $\sum_{\nu,\rho}\exp(a){}_\nu\exp(b){}_\rho\nabla_\mu g_{\nu\rho}$: that equality holds only in the metric-compatible case, where both sides vanish, and it fails as soon as a contorsion with a non-antisymmetric part is present, because the frame image carries weight factors that the interval does not. The implication is the one that is used, and it was checked on sixteen contorsions: the Levi-Civita one, seven metric-compatible ones built from axial and from general torsions, four confined to the sector and four with no symmetry at all. The sum vanished in exactly the eight metric-compatible cases and in none of the others — including the metric-compatible ones whose contorsion is *not* antisymmetric in its last pair, which is why the equivalence is with antisymmetry in the first and third slots and not with total antisymmetry. The tetrad used for the check is deliberately not symmetric, so that no index convention is degenerate. That antisymmetrised part $\tfrac12(\omega_{ab\mu}-\omega_{ba\mu})$ is the one place the torsion enters the matter equation, and it is why a contorsion with a non-antisymmetric part carries a piece, the symmetric part, that no field couples to.

Every check in this section was made in four dimensions, in exact rational arithmetic, on a tetrad of the form $\exp(a){}_\mu = \delta_{a\mu} + x_0M_{a\mu}$, with $x_0$ the time coordinate and $M$ the constant matrix whose only nonzero entries are $M_{01}=M_{10}=M_{12}=M_{13}=M_{21}=M_{23}=M_{32}=1$, evaluated at $x_0=\tfrac12$. The matrix is deliberately not symmetric in its $1$–$3$ entries, so that no check below can pass by mistaking a frame index for a world index.

**The tetrad postulate is satisfiable with a non-flat tetrad.** The Levi-Civita connection of the induced metric is nonzero for that tetrad, and the spin connection constructed from it makes $\nabla_\mu \exp(a){}_\nu = 0$ identically. The same computation confirms the frame-space statement above, in the only form in which it is true: the array with its first frame slot lowered is antisymmetric for the Levi-Civita connection, stays so under a totally antisymmetric contorsion, and is lost by a general contorsion — one not tied to the metric by the Einstein–Cartan formula, which for *any* torsion gives the metric-compatible array — so that the equivalence is with metric compatibility and not with a symmetry of the torsion. The array as solved, with one frame slot raised and one lowered, is not antisymmetric as it stands: its symmetry in the frame pair is $\varepsilon_a\varepsilon_b$, symmetric on the three boost pairs and antisymmetric on the three spatial ones. The lowering is therefore part of the statement and not a choice of notation.

**The Weitzenböck connection is curvature-free and torsionful.** The connection built from the tetrad alone,
$$
\Gamma_{\lambda\mu\nu} = \sum_a e_{a\lambda}\, \partial/\partial x_\mu \exp(a){}_\nu ,
$$
called the **Weitzenböck connection**, was computed for that tetrad together with its curvature. The curvature came out **exactly zero** in every component, and the torsion came out exactly
$$
T_{\lambda\mu\nu} = \sum_a e_{a\lambda}\bigl(\partial/\partial x_\mu \exp(a){}_\nu - \partial/\partial x_\nu \exp(a){}_\mu\bigr),
$$
which is nonzero for that tetrad: the antisymmetrised derivative of the frame is the whole of the connection. This is the content of the teleparallel sector: a connection can be flat and still have torsion, and the framework's algebra can carry it.

**Where the algebra enters.** The Lie subspace is spanned, as elements, by the three rotation generators $\vec e_k$ and the three boost generators $i\vec e_k$, so a connection is an element of that span and of nothing larger. The six components of the algebra-valued one-form $\vec\Gamma_\mu$ of Route Three are therefore in one-to-one correspondence with the six components $\omega_{ab\mu}$ of the spin connection, and nothing else about the algebra is used. The same six directions appear among the products of the frame cells: the six products of two distinct cells are independent and are the six Lorentz bivectors, of which the generators are the halves. *Conventions of the Matrix Models* records that correspondence, and the gamma section below prints it. The connection can be written as a $\mathbb{B}$-valued object, and the derivative that carries it depends on the module and not on the torsion. A vector transforms two-sidedly, $\tilde Q\mapsto\tilde U\tilde Q\tilde U^*$, so its covariant derivative is the two-sided
$$
D_\mu\tilde Q = \partial/\partial x_\mu\,\tilde Q + \vec\Gamma_\mu\tilde Q + \tilde Q\vec\Gamma_\mu^{*};
$$
the field $\tilde{Ξ}_{\mathrm{sp}}$ transforms one-sidedly, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde U\tilde{Ξ}_{\mathrm{sp}}$, so its covariant derivative is the one-sided
$$
D_\mu\tilde{Ξ}_{\mathrm{sp}} = \partial/\partial x_\mu\,\tilde{Ξ}_{\mathrm{sp}} + \vec\Gamma_\mu\tilde{Ξ}_{\mathrm{sp}} .
$$
The two are not interchangeable — the natural abbreviation $D_\mu=\partial/\partial x_\mu+[\vec\Gamma_\mu,\cdot]$ is wrong for exactly the boosts — and the torsion changes neither, since it lives in the part of $\vec\Gamma_\mu$ that is already in the Lie subspace. That trap is the corpus's own and is not repeated here; what matters for torsion is that the fix is the same for a torsionful connection as for a torsion-free one.

## The Spin Tensor and the Torsion–Spin Relation

In the Einstein–Cartan–Sciama–Kibble theory the torsion is not free: it is sourced *algebraically* by the spin density of matter.

**Every density of this section is a pairing.** The field is an element of $\mathbb{B}$, and a density is the scalar part of the product of the conjugate of the field, one element built out of the field, and the fixed element $i\vec e_x$,
$$
\operatorname{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\,i\,X\,\vec e_x\bigr),
$$
where $X$ is the element the density reads (*Norm and Pairing Conventions*, §*The Four Algebraic Norms and the Unitary Convention*). The fixed element $i\vec e_x$ is the timelike frame cell, written as the one multiplier it is: this is the Dirac adjoint of *Index and Notation Conventions*, §*The Upper and Low Marks*, with its operator spent, and it is the same factor in every density below. No column, no row and no matrix product is written anywhere in this section.

For the field $\tilde{Ξ}_{\mathrm{sp}}$ the spin density is the completely antisymmetric bilinear of three frame cells, read in that pairing. Written on the field, the element it reads is
$$
X_{\lambda\mu\nu}=\tfrac16\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,i\,e_{\lambda_{\sigma(1)}}\Bigl(i\,e_{\lambda_{\sigma(2)}}\bigl(i\,e_{\lambda_{\sigma(3)}}\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_{\nu(\lambda_{\sigma(3)})}\bigr)\vec e_{\nu(\lambda_{\sigma(2)})}\Bigr)\vec e_{\nu(\lambda_{\sigma(1)})},
$$
with $(\lambda_1,\lambda_2,\lambda_3)=(\lambda,\mu,\nu)$ and $\sigma$ running over the six permutations, and the density is
$$
\Sigma_{\lambda\mu\nu}=\operatorname{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\,i\,X_{\lambda\mu\nu}\,\vec e_x\bigr).
$$
The innermost factor is the action of the cell of $x_{\lambda_{\sigma(3)}}$ on the field, and each bracket around it is the action of the cell of the index outside it, so the display is the product of the three cells written on the element: no operator symbol, no letter for a cell and no matrix product appears in it. The normalisation is that of $\operatorname{Alt}$, the **normalised** antisymmetrisation: the average over the six permutations weighted by the sign of the permutation, which is what the sum above writes; without the $1/3!$ the duality below carries an extra factor six and the squared display an extra thirty-six.

**The chirality cell is the volume cell of the frame**, the corpus's glyph $\mathsf{V}_{\mathrm{vol}}$ of *Special Element Conventions*, §*The Chirality Convention*. In the axis-free frame its action is the pure right multiplication $Q\mapsto-iQ\vec e_z$, and it is $i$ times the product of the four cells of the frame, each of the four carrying one $i$ and $i^4=+1$. It anticommutes with each of the four cells, and that sign is what makes the four alternate. The axial current is the same pairing with the volume cell in place of a fourth cell,
$$
A_\mu=\operatorname{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\,i\,e_\mu\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_{\nu(\mu)}\,\vec e_z\,\vec e_x\bigr),
$$
where $i\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)}$ is the element the cell of $x_\mu$ makes of the field, the volume cell multiplies that on the right by $-i\vec e_z$, the adjoint supplies the $i$ and the $\vec e_x$ outside, and the two phases cancel: the single $i$ of the display is the cell's, and no second one survives.

**The antisymmetric spin density is the dual of the axial current.**
$$
\Sigma_{\lambda\mu\nu} = -\,i\,\epsilon_{\lambda\mu\nu\rho}\,\varepsilon_\rho\,A_\rho = -\,i\,\epsilon_{\lambda\mu\nu\rho}\,A^\rho ,
$$
with $A^\rho=\varepsilon_\rho A_\rho$ and $\epsilon_{0123}=+1$. The weight $\varepsilon_\rho$ is not a convention added by hand: it is the raised index, written low as the index convention requires, so the two forms of the display are the same statement.

The identity is exact, and the constant is $-i$. The cells carry the reason themselves: the antisymmetrised product of three of them is the volume cell times the fourth, as an identity on any element $Q$,
$$
\tfrac16\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,i\,e_{\lambda_{\sigma(1)}}\Bigl(i\,e_{\lambda_{\sigma(2)}}\bigl(i\,e_{\lambda_{\sigma(3)}}\,Q\,\vec e_{\nu(\lambda_{\sigma(3)})}\bigr)\vec e_{\nu(\lambda_{\sigma(2)})}\Bigr)\vec e_{\nu(\lambda_{\sigma(1)})}
=-\,i\,\epsilon_{\lambda\mu\nu\rho}\,\varepsilon_\rho\,e_\rho\,Q\,\vec e_{\nu(\rho)}\,\vec e_z .
$$
That is an identity of elements, exact at every index triple, and it accounts for its own unit. The phase is bookkeeping throughout: the three cells of the left side carry $i^3=-i$ between them, which is the constant, and the same identity with the cells written without their phase carries $+i$ instead. Read in the pairing, with $Q=\tilde{Ξ}_{\mathrm{sp}}$ and the adjoint's $i\vec e_x$ on the right, it gives $\Sigma$ on the left and $A_\rho$ on the right, so the display holds with $-i$ and there is nothing left to choose. The same identity in the older gamma display is printed in the gamma section below.

The weight is what carries the sign. Without it the same display with $+i$ holds on the eighteen triples whose free index is spacelike and fails on the six whose free index is timelike; the sign vector is exactly the raised index that repairs those six.

Because $\operatorname{Alt}$ is a total antisymmetrisation, the spin density is not a general third-rank tensor: its 24 components are the four of a totally antisymmetric third-rank tensor repeated with signs, and by the duality those four are exactly the axial current. This is the same counting as in the metric-compatibility condition above, and it is not a coincidence: the physical torsion and the physical spin density live in the same four-dimensional subspace.

**The contracted spin density is the axial current squared.** Substituting the duality and using $i^2=-1$,
$$
\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu}
= -\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\epsilon_{\lambda\mu\nu\rho}\,\epsilon_{\lambda\mu\nu\sigma}\,A^\rho A^\sigma
= -\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\lambda\mu\nu\rho}\,\epsilon_{\lambda\mu\nu\sigma}\,A_\rho A_\sigma ,
$$
the second form writing the two raised indices out with the sign vector, $A^\rho=\varepsilon_\rho A_\rho$. On the nonzero terms $(\lambda,\mu,\nu,\rho)$ is a permutation of $(0,1,2,3)$, so $\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\varepsilon_\rho=-1$ and the whole product of five sign factors is $-\varepsilon_\sigma$; the leading minus turns that into $+\varepsilon_\sigma$. With $\sum_{\lambda,\mu,\nu}\epsilon_{\lambda\mu\nu\rho}\epsilon_{\lambda\mu\nu\sigma}=+6\,\delta_{\rho\sigma}$ for the all-lowered symbol and $\epsilon_{0123}=+1$, the sum collapses to six. Hence
$$
\boxed{\;\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\,\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu} = 6\sum_\rho\varepsilon_\rho\,A_\rho A_\rho\;},
$$
and the numerical check reproduced it to a relative error of order $10^{-32}$, that is, at machine precision.

The Einstein–Cartan field equations then read, schematically,

$$
T_{\lambda\mu\nu} = \kappa\,\Sigma_{\lambda\mu\nu} , \qquad \kappa = 8\pi G \quad (c=1) ,
$$

with $\Sigma$ the density displayed above. Because the torsion appears in the action without derivatives, its field equation is algebraic: it is solved by $T=\kappa\Sigma$ and the solution can be substituted back into the matter equation. The substitution couples the torsion to the axial current, and since the torsion is the dual of that current, the result is a **four-fermion axial–axial contact term** with a coefficient fixed by $G$ and not chosen. The elimination is the step the nonlinear-Dirac article performs; its coefficient, $\tfrac{3\kappa}{16}$ in the Lagrangian and $\tfrac{3\kappa}{8}$ in the equation, is that article's to own, and the factor of two between them is the variation of the square; this article supplies the two geometric identities — duality and the factor six — that make the elimination a two-line algebraic substitution rather than a computation in components. The statement that the torsion–spin relation is algebraic, and therefore that the elimination introduces no new propagating field, is the whole reason the Hehl–Datta term is a contact interaction.

## Teleparallel Geometry and the Weitzenböck Connection

The Weitzenböck connection of the previous section,

$$
\Gamma_{\lambda\mu\nu} = \sum_a e_{a\lambda}\, \partial/\partial x_\mu \exp(a){}_\nu ,
$$

defines a geometry whose curvature vanishes identically and whose torsion is nonzero. Its exact properties, all confirmed above, are worth stating in the general form in which they are used.

**Zero curvature is an identity.** With
$$
\mathrm{Riem}_{\lambda\mu\nu\rho} = \partial \Gamma_{\lambda\mu\rho}/\partial x_\nu - \partial \Gamma_{\lambda\mu\nu}/\partial x_\rho + \Gamma_{\lambda\nu\sigma}\Gamma_{\sigma\mu\rho} - \Gamma_{\lambda\rho\sigma}\Gamma_{\sigma\mu\nu} ,
$$
one has $\mathrm{Riem}_{\lambda\mu\nu\rho}(\Gamma)=0$ for every tetrad. The reason is structural and exact: in the array $E$ of the tetrad the connection is the pure-gauge form $\Gamma_\mu=E^{-1}\partial E/\partial x_\mu$ of the zero connection, and $\partial/\partial x_\mu(EE^{-1})=0$ gives $\partial E^{-1}/\partial x_\mu=-E^{-1}(\partial E/\partial x_\mu)E^{-1}$, hence $d\Gamma=-\Gamma\wedge\Gamma$ and $\mathrm{Riem}=d\Gamma+\Gamma\wedge\Gamma=0$ identically. The check is exact; no small-curvature approximation is involved.

**The torsion is the contorsion relative to the Levi-Civita connection.** In the **Weitzenböck gauge** the full spin connection is set to zero, $\omega^{a}{}_{b\mu} = 0$, so the tetrad postulate forces the Levi-Civita part and the contorsion to cancel,

$$
N_{\mathrm{cont}}{}^{a}{}_{b\mu} = -\,\omega^{a}{}_{b\mu}(e) ,
$$

and the same statement holds with the first frame slot lowered on both sides.

This is the teleparallel condition: the geometry is the one in which the frame is everywhere parallel and all the connection is contorsion. In this formulation the torsion is the entire content of the connection, and general relativity is recovered by the same equations in the zero-torsion case.

**The Weitzenböck contorsion is antisymmetric in the frame pair and not in the world pair, and $T\\ne 2N_{\mathrm{cont}}$ for it.** This is the sharpest available test of the contorsion section, because every quantity is computed rather than assumed. With $K=\Gamma-\{\,\}$ the world-index contorsion, the exact relation is the antisymmetrised $T_{\lambda\mu\nu}=N_{\mathrm{cont},\lambda\mu\nu}-N_{\mathrm{cont},\lambda\nu\mu}$, and the collapse to $T=2N_{\mathrm{cont}}$ needs $N_{\mathrm{cont}}$ antisymmetric in its last pair, which it is not: the geometry that makes $N_{\mathrm{cont},ab\\mu}=-\omega_{ab\mu}(e)$ antisymmetric in $a,b$ leaves $N_{\mathrm{cont},\lambda\mu\nu}$ with a nonzero symmetric part in $\mu,\nu$. That is not an exception to the identities, it is the sector boundary: the connection is **metric compatible**, $\nabla_\mu g_{\nu\rho}=0$ exactly, so its contorsion is the Einstein–Cartan array of the earlier section, antisymmetric in the first and third slots, and its torsion is not totally antisymmetric. Hence metric compatibility here does not imply total antisymmetry, and the frame statement ($\omega_{ab\mu}$ antisymmetric) and the world statement ($N_{\mathrm{cont},\lambda\mu\nu}$ not) are both true of it.

The corpus's boundary applies to this sector exactly as it applies to the others, and it is worth restating because teleparallel language invites an overclaim. Teleparallel gravity is **a gauge choice of the same geometry**, not a second geometry and not a derivation of the metric from matter. Nothing in the algebra selects it, the tetrad is still inserted by hand, and no action for the frame follows from the identity. What the identity does supply is a clean statement of what the corpus's own connection objects are: the sector in which the algebra-valued $\vec\Gamma_\mu$ is entirely contorsion and has zero curvature.

## What the Algebra Does and Does Not Do

The positive content of this article is a statement of *carrying*. The algebra's six-dimensional Lie subspace holds the spin connection with or without torsion; the torsion and the contorsion are tensors on a manifold and can be written in the framework's notation without leaving it; the spin density of the field is a bilinear of three frame cells in total antisymmetrisation, and it is the dual of the axial current with the exact constant $-i$; the contraction gives the factor six; and the Weitzenböck identity shows a flat, torsionful connection is a perfectly consistent object that the algebra can express.

The negative content is the boundary, restated so that a later reader cannot mistake it. The algebra **generates no torsion**: the commutator of the quaternion units is a constant of the algebra, not a field, and no field equation for the torsion follows from it. The algebra **selects no connection**: the vanishing of torsion and metric compatibility are conditions, and the second of them was shown above to mean that the contorsion is antisymmetric in its first and third slots, $N_{\mathrm{cont},\lambda\mu\nu}=-N_{\mathrm{cont},\nu\mu\lambda}$, which total antisymmetry implies and does not follow from. The algebra **supplies no action** for the frame or the connection, so no Einstein equation, and the torsion is not eliminated by the algebra but by its own algebraic field equation in a theory that has one. And the algebra **does not couple the torsion to matter by itself**: the coupling lives in the derivative of the field, $D_\mu\tilde{Ξ}_{\mathrm{sp}}=\partial/\partial x_\mu\,\tilde{Ξ}_{\mathrm{sp}}+\vec\Gamma_\mu\tilde{Ξ}_{\mathrm{sp}}$, the one-sided derivative of Route Three, and its strength is fixed by the Einstein constant in the theory that puts the torsion into the action.

The two open items this article was written against stand as follows. The first — torsion in the framework's notation, with the geometry that makes the elimination possible — is supplied here, and the identities are recomputed. The second — the action and the selection principle — is untouched, and remains where *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* and *Quantum Gravity under the Biquaternion Framework — A Research Agenda* placed it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. With $L_a$ and $R_b$ the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, they are
$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

The sixteen words in the four gammas are a basis of $M_4(\mathbb{C})$, and each single one is invertible with determinant one: $L_a$ and $R_b$ with $|a|=|b|=1$ are invertible, and the scalar $i$ enters a $4\times4$ determinant as $i^4=+1$. A frame cell is therefore a full-rank operator, and the rank-one cone of "pure tensors" belongs to the sandwich family $M\Theta M^\dagger$, not here.

These are the frame cells of the earlier sections under their Clifford names, $\gamma_\mu$ for the cell of $x_\mu$ and $\gamma_5$ for the volume cell $\mathsf{V}_{\mathrm{vol}}$. The central grading of the complexified algebra is a different object: it is the difference $e_+-e_-$ of the two central idempotents, written $i\tilde{Ζ}_{\mathrm{ad}}$ with $\tilde{Ζ}_{\mathrm{ad}}^2=-e_t$, so that its own square is $+e_t$. It is not a cell of the frame, and $\gamma_5$ is its representative on the Dirac module.

The dictionary is complex-linear. Over $\mathbb{R}$ the products of the gammas close on a sixteen-dimensional algebra and reproduce $\{\gamma_a,\gamma_b\}=2g_{ab}I_4$ with $\varepsilon=(1,-1,-1,-1)$, so they span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$; the same four cells without their factor $i$, written $\beta_a$ in this block, anticommute the other way round, $\{\beta_a,\beta_b\}=2\eta'_{ab}I_4$ with $\eta'=\mathrm{diag}(-1,+1,+1,+1)$, and span the opposite real form $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

## Summary

A connection with torsion splits into a metric part, the Christoffel symbols, and a remainder, the contorsion $N_{\mathrm{cont},\lambda\mu\nu}$. The torsion fixes only the antisymmetric part of the remainder in its last pair, twenty-four of sixty-four components; the unique metric-compatible connection for a given torsion is the Einstein–Cartan contorsion $N_{\mathrm{cont},\lambda\mu\nu}=\tfrac12(T_{\lambda\mu\nu}-T_{\mu\nu\lambda}+T_{\nu\lambda\mu})$, exact for any torsion, antisymmetric in the first and third slots, and collapsing to $\tfrac12T$ exactly when the torsion is totally antisymmetric. Writing $T_{\lambda\mu\nu}=2N_{\mathrm{cont},\lambda\mu\nu}$ throughout is the further choice of the sector in which the Christoffel symbols are the whole symmetric part of the connection; inside it the covariant derivative of the metric, $\nabla_\mu g_{\nu\rho} = -(g_{\nu\lambda}N_{\mathrm{cont},\lambda\mu\rho} + g_{\rho\lambda}N_{\mathrm{cont},\lambda\mu\nu})$, vanishes for every index order exactly when the contorsion is totally antisymmetric, and the 24 components are cut to four. **Inside the sector, metric compatibility is the condition of total antisymmetry**, and that is the precise meaning of the corpus's statement that metric compatibility is a condition and not a consequence.

The tetrad postulate ties the affine and spin connections, and the spin connection splits as $\omega = \omega(e) + K$ with the contorsion in frame indices; $\omega$ with its first frame slot lowered is antisymmetric in the frame pair exactly in the metric-compatible case, so the two conditions of the previous paragraph have one face in world indices and one in frame indices. The Weitzenböck connection $\Gamma_{\lambda\mu\nu} = \sum_a e_{a\lambda} \partial/\partial x_\mu \exp(a){}_\nu$ has exactly zero curvature and nonzero torsion; in the Weitzenböck gauge the full spin connection vanishes and the contorsion is minus the Levi-Civita spin connection of the tetrad.

The spin density of the field is the completely antisymmetric bilinear of three frame cells, read in the pairing $\operatorname{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x)$ that spends the timelike cell once: $\Sigma_{\lambda\mu\nu}=\operatorname{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX_{\lambda\mu\nu}\vec e_x)$, with $X_{\lambda\mu\nu}$ the normalised antisymmetrisation of the three cell actions applied to the field. It is the dual of the axial current, $\Sigma_{\lambda\mu\nu} = -i\,\epsilon_{\lambda\mu\nu\rho}\,A^\rho$ with $A_\mu = \operatorname{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)}\vec e_z\vec e_x)$, and its full contraction is six times the contracted square of the axial current, $\sum_{\lambda,\mu,\nu}\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\Sigma_{\lambda\mu\nu}\Sigma_{\lambda\mu\nu} = 6\sum_\rho\varepsilon_\rho A_\rho A_\rho$, the factor six coming from $\sum_{\lambda,\mu,\nu}\epsilon_{\lambda\mu\nu\rho}\epsilon_{\lambda\mu\nu\sigma}=6\delta_{\rho\sigma}$ and the sign from $(-i)^2=-1$ together with $\varepsilon_\lambda\varepsilon_\mu\varepsilon_\nu\varepsilon_\rho=-1$ on the nonzero terms. The Einstein–Cartan torsion–spin relation $T = \kappa\Sigma$ is therefore algebraic, and the elimination of the torsion leaves the axial–axial contact term whose coefficient the nonlinear-Dirac article owns.

Two statements bound the article. The commutator of the quaternion units is a constant of the algebra and not the torsion of a manifold; the algebra carries the connection and the torsion but generates neither, selects no connection, and supplies no action. The identities above are exact and recomputed; the dynamics is not here and is not claimed.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Gamma_{\lambda\mu\nu}$ | affine connection |
| $\left\{{}_{\lambda\mu\nu}\right\}$ | Christoffel symbols of $g_{\mu\nu}$ |
| $T_{\lambda\mu\nu}$ | torsion tensor, $N_{\mathrm{cont},\lambda\mu\nu}-N_{\mathrm{cont},\lambda\nu\mu}$; equal to $2N_{\mathrm{cont},\lambda\mu\nu}$ in the sector used here |
| $N_{\mathrm{cont},\lambda\mu\nu}$ | contorsion; antisymmetric in the last pair in the sector used here; under metric compatibility, with the first slot lowered, it equals $\tfrac12(T_{\lambda\mu\nu}-T_{\mu\nu\lambda}+T_{\nu\lambda\mu})$; the first slot is the output slot, raised implicitly |
| $\exp(a){}_\mu$, $e_{a\mu}$ | tetrad and its inverse |
| $E_{a\mu}=\varepsilon_a\exp(a){}_\mu$ | tetrad with its frame slot lowered, the object whose affine derivative gives the spin connection |
| $\mathrm{D}_\mu$ | affine covariant derivative, acting on the world label only |
| $g_{\mu\nu} = \delta_{ab}\exp(a){}_\mu \exp(b){}_\nu$ | metric from the tetrad; the unit metric $\delta_{\mu\nu}$ for the identity tetrad |
| $\omega^{a}{}_{b\mu}$ | spin connection one-form as solved, with the first frame slot raised |
| $\omega_{ab\mu}=\varepsilon_a\omega^{a}{}_{b\mu}$ | the same array with the first frame slot lowered; antisymmetric in the frame pair exactly in the metric-compatible case |
| $\omega_{ab\mu}(e)$ | its Levi-Civita part |
| $\vec\Gamma_\mu$ | the connection as an element of the Lie subspace of $\mathbb{B}$ |
| the frame cell of $x_\mu$ | the action $Q\mapsto i\,e_\mu Q\,\vec e_{\nu(\mu)}$ with $\nu(t)=x$ and $\nu(k)=y$: $Q\mapsto iQ\vec e_x$ at $\mu=t$ and $Q\mapsto i\vec e_kQ\vec e_y$ at $\mu=k$; no letter stands for it |
| two distinct frame cells | their six products are the six Lorentz bivectors; the six generators are half of them |
| $\mathsf{V}_{\mathrm{vol}}$ | the chirality cell of the frame, the action $Q\mapsto-iQ\vec e_z$; it is $i$ times the product of the four cells and anticommutes with each of them |
| $\operatorname{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x)$ | every density of the spin section: the pairing of the field with the element $X$, the timelike action $Q\mapsto iQ\vec e_x$ spent in it |
| $X_{\lambda\mu\nu}$ | the element the spin density reads, the normalised antisymmetrisation of the three cell actions applied to the field |
| $\Sigma_{\lambda\mu\nu}$ | spin density of the field, $\operatorname{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX_{\lambda\mu\nu}\vec e_x)$; equal to $-i\,\epsilon_{\lambda\mu\nu\rho}A^\rho$ |
| $A_\mu$ | axial current, $\operatorname{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*i\,e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_{\nu(\mu)}\vec e_z\vec e_x)$ |
| $\varepsilon$, $\varepsilon_\mu$ | sign vector, $\varepsilon_t=+1$ and $\varepsilon_k=-1$; $\varepsilon_\mu A_\mu$ is the raised $A^\mu$ |
| $\kappa = 8\pi G$ | Einstein gravitational constant, $c=1$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the Einstein–Cartan–Sciama–Kibble theory, the contorsion and the algebraic torsion–spin relation.
- F. W. Hehl and B. K. Datta, "Nonlinear spinor equation and asymmetric connection in general relativity," *Journal of Mathematical Physics* **12** (1971) 1334–1339, for the elimination of the torsion and the axial–axial contact term.
- R. Aldrovandi and J. G. Pereira, *Teleparallel Gravity: An Introduction* (Springer, 2013), for the Weitzenböck connection, the vanishing of its curvature, and the teleparallel formulation of general relativity.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for Route Two's frame field, Route Three's Lie subspace and two-sided derivative, and the boundary statement that metric compatibility and vanishing torsion are conditions.
- [The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form](the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html), for the Hehl–Datta coefficient — $\tfrac{3\kappa}{16}$ in the Lagrangian, $\tfrac{3\kappa}{8}$ in the field equation — and the placement of the axial channel among the fermion bilinears.
- [Conventions of the Matrix Models](matrix-representations-conventions.html), for the correspondence between the six generators of the Lie subspace and the six Lorentz bivectors, §*The Clifford Structure*, and for the rule that a cell is written as its two multipliers and never as a letter.
- [Conventions of the Norms and the Pairings](norm-and-pairing-conventions.html), for the scalar part and the forms on which every density of the spin section is read.
- [Matter Makes Space — An External Construction from Quaternionic Spinors](matter-makes-space-an-external-construction-from-quaternionic-spinors.html), for the external claim that the torsion is the quaternion commutator and the composite geometry built on it, with the parts that do not reproduce.
