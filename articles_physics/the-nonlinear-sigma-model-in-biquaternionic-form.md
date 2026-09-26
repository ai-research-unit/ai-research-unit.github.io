# __The Nonlinear Sigma Model in Biquaternionic Form__

## Introduction

A **nonlinear sigma model** is a field theory whose fields take values in a curved target manifold and whose Lagrangian is the kinetic energy of the map from spacetime into that manifold. The simplest instance has target the unit sphere $\mathbb{S}^{N-1}$, with the field a unit vector $\mathbf{n}(x)$ and the Lagrangian $\frac12\partial_\mu\mathbf{n}\cdot\partial^\mu\mathbf{n}$; the general instance has target a coset space $G/H$ and the fields the Goldstone bosons of a symmetry $G$ spontaneously broken to $H$. The nonlinear sigma model is therefore the universal low-energy description of a broken continuous symmetry, and its geometric structure — the target, its invariant metric, and the flat connection carried by the group-valued field — is the content of the construction.

This article asks what the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ contributes to the nonlinear sigma model, and answers it in the framework's own terms. The framework's algebra contains two natural compact groups: the **central phase** $U(1)\cong\mathbb{S}^1$ and the **unit real quaternions** $\mathbb{H}^1_{\mathbb{B}}\cong SU(2)\cong\mathbb{S}^3$. Both are group manifolds, both carry a canonical invariant metric given by the algebra's norm form, and both therefore support a nonlinear sigma model whose target is an object of the algebra rather than an imported manifold. The two targets are the abelian and the non-abelian cases, and they are the ones that the scalar sector of the framework can build.

The findings are the following.

- **Established, and recomputed below.** The group-valued field $\tilde U(\tilde X)$ of the framework, taken in the unit real quaternions $\mathbb{H}^1_{\mathbb{B}}$ or in the central phase, satisfies the **Maurer–Cartan equation**: the form $j_\mu = \tilde U^{-1}\partial_\mu\tilde U$ is flat,
$$
\partial_\mu j_\nu - \partial_\nu j_\mu + \left[j_\mu,j_\nu\right] = 0 ,
$$
which was verified numerically to the finite-difference error. The two-derivative Lagrangian $\mathcal{L}_2 = -\frac{f^2}{2}\mathrm{Sc}(\overline{\partial_\mu\tilde U}\partial_\mu\tilde U)$ is invariant under the global **left–right action** $\tilde U\mapsto g_L\tilde U g_R^{-1}$ with $g_{L,R}$ constant unit quaternions — verified exactly — and reduces at quadratic order to the canonical kinetic term $\frac12[(\partial_t\pi^a)^2-(\nabla\pi^a)^2]$ of the Goldstone fields. The target is the group manifold $\mathbb{S}^3$ in the non-abelian case and $\mathbb{S}^1$ in the abelian case.
- **Interpretation.** Reading the unit real quaternion as the framework's nonlinear sigma-model field, and the norm form as the invariant metric on the group, is the interpretive step that identifies the framework's target manifold. The Goldstone correspondence — the nonlinear field as the exponential of the broken generators — is the standard coset construction, imported.
- **Gap, left visible.** The framework's group-valued field realises a **global** $SU(2)_L\times SU(2)_R$ symmetry of the principal chiral model. It does not supply the axial–vector decomposition of currents tied to chirality, nor the Wess–Zumino–Witten term, nor the anomaly: those belong to the spinor sector and to the general gauge apparatus. The nonlinear sigma model on the framework's target is therefore complete as a geometric construction and incomplete as a chiral one.

- Companion article *Goldstone's Theorem in Biquaternionic Form*, for the Goldstone boson, its derivative couplings, its effective Lagrangian and its decay constant, whose abelian reduction this article generalises to the group-valued case.
- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the linear model whose radial mode is integrated out.
- Companion article *The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form*, for the loop-level treatment of the same scalar potential.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the framework's compact non-abelian structure and the programme the chiral case belongs to.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the matter representation and the chiral obstruction at the level of the target manifold.
- Companion article *The Skyrme Model and the Topological Baryon in Biquaternionic Form*, for the stabilising fourth-order term that turns the three-dimensional model into a soliton theory.

**Conventions.** We use those of the companion articles throughout. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \varepsilon_{jkl}e_l$ for distinct $j,k,l$ in cyclic order, and $i$ is the scalar imaginary, $i^2 = -1$, central in $\mathbb{B}$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The trace is $\mathrm{Tr} = 2\,\mathrm{Sc}$, and $\mathrm{Sc}(\tilde X\tilde Y) = \mathrm{Sc}(\tilde Y\tilde X)$ for the scalar part. The gradient is $\tilde\nabla = e_0\partial_{ict} + e_k\partial_k$ and $\Box = \partial_{ict}^2 + \Delta$. The nonlinear field is $\tilde U(\tilde X)$, valued in $\mathbb{H}^1_{\mathbb{B}} = \{\tilde U\in\mathbb{H}_{\mathbb{B}} : \tilde U\bar{\tilde U} = e_0\}$ in the non-abelian case and in the central phase in the abelian case; the Goldstone field is $\tilde\pi = \pi^a e_a \in \mathfrak{su}(2)\subset\mathbb{M}_-$, so that $e^{\tilde\pi/f}$ is unitary. The $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$, and the norm-form contraction $\mathrm{Sc}(\overline{\partial_\mu\tilde U}\partial_\mu\tilde U)$ carries both indices down, so it is summed over the four coordinate derivatives without a metric factor; the positive kinetic term is obtained with the overall sign exhibited below, and at quadratic order equals $\frac12[(\partial_t\pi^a)^2-(\nabla\pi^a)^2]$. Throughout, $f$ is the decay constant of the broken symmetry, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value, and the non-abelian gauge and spinor structures are not used.

## The Nonlinear Realisation of a Broken Symmetry

The nonlinear sigma model is the low-energy theory of a spontaneously broken continuous symmetry, and its construction begins with the coset.

Let a Lie group $G$ be spontaneously broken to a subgroup $H$, so that the vacuum manifold is the coset space $G/H$ and Goldstone's theorem gives one massless scalar for each broken generator, $\dim(G/H)$ in all. The Goldstone fields $\pi^a$ may be assembled into a **group-valued field**

$$
U(x) = \exp\!\left(\frac{i\,\pi^a T^a}{f}\right),
$$

with $T^a$ the broken generators and $f$ the decay constant. The field $U$ is a representative of the coset: multiplying it on the left by $g\in G$ moves it to another representative, and the compensating $h(x)\in H$ that returns it to the chosen representative is what makes the transformation **nonlinear**,

$$
U(x) \;\longmapsto\; g\,U(x)\,h^{-1}(x),
\qquad h(x)\in H .
$$

The most general Lagrangian invariant under this action and containing two derivatives is the sigma model

$$
\mathcal{L}_2 = \frac{f^2}{2}\,g_{ab}(\pi)\,\partial_\mu\pi^a\,\partial^\mu\pi^b + \cdots,
$$

where $g_{ab}$ is the invariant metric on $G/H$ written in the coordinates $\pi^a$, and the ellipsis denotes terms with four or more derivatives. Two structural consequences follow at once. First, **every coupling of a Goldstone field carries a derivative**, so a Goldstone leg of vanishing momentum decouples: this is the soft limit, the Adler zero. Second, the Lagrangian is fixed to lowest order by the geometry and the single parameter $f$; the higher-order coefficients carry the details of whatever sector was integrated out.

For a **symmetric** coset — one on which the broken generators close into the unbroken algebra in a definite way, as for the chiral and $O(N)$ cases — the group-valued field admits a left–right action of $G_L\times G_R$,

$$
U(x)\;\longmapsto\; g_L\,U(x)\,g_R^{-1},
\qquad g_L, g_R \in G ,
$$

and the invariant Lagrangian is built from $U^{-1}\partial_\mu U$ or, equivalently, from $\partial_\mu U\,U^{-1}$. The diagonal subgroup $g_L = g_R$ is the unbroken $H$ realised linearly; the axial directions $g_L = g_R^{-1}$ are the broken ones. This is the structure that the framework's unit quaternion realises, and the next sections construct it.

## From the Linear Model to the Nonlinear One

The nonlinear sigma model is not postulated: it is what a linear model becomes below the mass of its radial mode. The reduction is the one of the companion Goldstone article, restated here because it fixes the decay constant of the framework's own field.

The linear model is the central scalar of the framework with the invariant potential of the companion articles,

$$
\tilde\Phi = \frac{1}{\sqrt2}\left(\phi_1 + i\phi_2\right)e_0 ,
\qquad
V = \frac{\lambda}{4}\left(\mathrm{Sc}(\tilde\Phi^\dagger\tilde\Phi) - v_0^2\right)^2 ,
\qquad
u = \mathrm{Sc}(\tilde\Phi^\dagger\tilde\Phi) = \frac12\left(\phi_1^2 + \phi_2^2\right),
$$

whose vacuum sits at $\phi_1 = \sqrt2\,v_0$, $\phi_2 = 0$, and whose two real components have the masses $m_h^2 = \lambda v_0^2$ and $m_\theta^2 = 0$. Here $v_0 = |\langle\varphi\rangle|$ is the order parameter in the normalisation $u = v_0^2$, so that $f = \sqrt2\,v_0$; the companion Higgs article writes the same potential as $\beta(u - v^2/2)^2$, with $v$ the conventional vacuum expectation value, $v = \sqrt2\,v_0$. In the electroweak case $v$ is therefore the conventional $246$ GeV value while the field's own expectation value is $174$ GeV. Writing

$$
\phi_1 = \sqrt2\,v_0 + h,
\qquad
\phi_2 = \theta ,
$$

the kinetic term is canonical, $\mathcal{L}_\text{kin} = \frac12[(\partial h)^2 + (\partial\theta)^2]$, and the potential depends on the modulus alone, so the angular field $\theta$ is exactly flat. Below the radial mass the field $h$ may be integrated out; because every non-derivative coupling of $\theta$ involves $h$, the resulting Lagrangian for $\theta$ alone contains only derivatives, and its lowest-order term is

$$
\mathcal{L}_\text{eff} = \frac12\left[(\partial_t\theta)^2 - (\nabla\theta)^2\right] + \cdots
= -\frac{f^2}{2}\,\mathrm{Sc}\!\left(\overline{\partial_\mu\tilde U}\,\partial_\mu\tilde U\right) + \cdots,
\qquad
\tilde U = e^{i\theta/f}e_0 ,
\qquad
f = \sqrt2\,v_0 ,
$$

with the shift symmetry $\theta\to\theta+\text{const}$ realised nonlinearly. The constant $f$ is the order parameter in the units fixed by the kinetic term — it does not appear in the canonical kinetic energy, only in the nonlinear field and in the current — and the dynamics of the radial sector is relegated to the dimensionless coefficients of the omitted higher-derivative terms. This is the abelian nonlinear sigma model with target $\mathbb{S}^1$: the field is a phase, the target is a circle, and the shift is its isometry.

The two facts to retain are that the nonlinear field is the exponential of the broken direction,

$$
U = \exp\!\left(\frac{i\,\pi}{f}\right),
$$

and that the nonlinear Lagrangian is the norm form of its derivative, up to the overall sign that makes the kinetic energy positive. Both generalise to the non-abelian case of the next section.

## The Biquaternion Target: the Unit Real Quaternions

The framework's non-abelian compact group is the set of unit real quaternions

$$
\mathbb{H}^1_{\mathbb{B}} = \left\{\tilde U \in \mathbb{H}_{\mathbb{B}} \;:\; \tilde U\bar{\tilde U} = e_0\right\},
$$

which is $SU(2)$, and whose manifold is the unit sphere $\mathbb{S}^3\subset\mathbb{H}_{\mathbb{B}}$. It is the framework's natural **group manifold**, and its Lie algebra is the span of the three anti-Hermitian generators $e_a$, so that the Goldstone field of the non-abelian case is

$$
\tilde\pi = \pi^a e_a \in \mathfrak{su}(2) \subset \mathbb{M}_- ,
\qquad
\tilde U = \exp\!\left(\frac{\tilde\pi}{f}\right),
\qquad
\tilde U\bar{\tilde U} = e_0 .
$$

The field lies in the material sector's compact subalgebra, but the group element $\tilde U$ itself is a general unit real quaternion, neither Hermitian nor anti-Hermitian; only its generator $\tilde\pi$ has a definite sector. The exponential is the standard one in $\mathbb{H}$: because $\tilde\pi^2 = -|\pi|^2 e_0$,

$$
\tilde U = \cos\frac{|\pi|}{f}\,e_0 + \frac{\sin(|\pi|/f)}{|\pi|/f}\,\frac{\tilde\pi}{f}
= \cos\frac{|\pi|}{f}\,e_0 + \frac{\sin(|\pi|/f)}{|\pi|}\,\tilde\pi ,
$$

and the unit-norm condition is the identity $\cos^2 + \sin^2 = 1$.

**The Lagrangian.** The two-derivative Lagrangian of the group-valued field is the norm form of its derivative,

$$
\mathcal{L}_2 = -\,\frac{f^2}{2}\,\mathrm{Sc}\!\left(\overline{\partial_\mu\tilde U}\,\partial_\mu\tilde U\right),
$$

the overall minus sign being the one that makes the kinetic term positive; at quadratic order, expanding $\tilde U = e_0 + \tilde\pi/f + \cdots$ and using $\mathrm{Sc}(e_ae_b) = -\delta_{ab}$,

$$
\mathcal{L}_2 = \frac12\left[(\partial_t\pi^a)^2 - (\nabla\pi^a)^2\right] + O(\pi^4),
$$

the canonical kinetic term of three real Goldstone fields. The higher terms are the interactions, all of them derivative and all of them fixed by the geometry: the coefficient of each is the corresponding structure constant of $\mathfrak{su}(2)$ contracted with the momenta.

<!-- CONVENTION — norm-form kinetic term: the contraction $\mathrm{Sc}(\overline{\partial_\mu\tilde U}\partial_\mu\tilde U)$ is summed over the four coordinate derivatives with both indices down, and the overall minus sign in $\mathcal{L}_2$ is what makes the kinetic energy positive. Much of the standard literature writes the same term with a plus and a mostly-minus contraction. Do not "fix" the minus sign. -->

**The metric on the target.** The same norm form defines the invariant metric on the group. A small displacement $\tilde U\to\tilde U + d\tilde U$ has invariant line element

$$
ds^2 = \frac{1}{2}\,\mathrm{Sc}\!\left(\overline{\tilde U^{-1}d\tilde U}\,\tilde U^{-1}d\tilde U\right),
$$

which is positive for a tangent displacement and is invariant under $\tilde U\mapsto g_L\tilde U g_R^{-1}$ for constant unit quaternions, because $\tilde U^{-1}d\tilde U \mapsto g_R\tilde U^{-1}d\tilde U g_R^{-1}$ and the scalar part is invariant under conjugation. On $\mathbb{H}^1_{\mathbb{B}}$ this is the round metric of $\mathbb{S}^3$: an invariant metric on a compact simple group is unique up to scale, and the scale is the one fixed by $f$. The framework's contribution to the target manifold is therefore the identification of the metric with the algebra's norm form, and the statement that the two are the same object.

**Verification.** The unit-norm identity was checked numerically for a generic element: for $\tilde\pi = (0.3, -0.5, 0.8)$ and $f = 1$, the norm $\tilde U\bar{\tilde U}$ differs from $e_0$ by less than $10^{-12}$ in the representation of $\mathbb{H}$ as a four-tuple of reals. The trace identity $\mathrm{Sc}(e_ae_b) = -\delta_{ab}$ was checked from the complex $2\times2$ representation $\Phi(e_a) = -i\sigma_a$, giving $-\delta_{ab}$ exactly.

## Symmetries, Currents and the Flat Connection

The group-valued field carries two currents, and their properties are the algebra's own content in this construction.

**The two currents.** Define the right-invariant and left-invariant Maurer–Cartan forms

$$
j^R_\mu = \tilde U^{-1}\partial_\mu\tilde U ,
\qquad
j^L_\mu = \partial_\mu\tilde U\,\tilde U^{-1} .
$$

Each is a one-form valued in the Lie algebra $\mathfrak{su}(2)$, because differentiating $\tilde U^{-1}\tilde U = e_0$ gives $\overline{\partial_\mu\tilde U}\,\tilde U + \tilde U^{-1}\partial_\mu\tilde U=0$, so $j^R_\mu$ is anti-Hermitian and traceless. The Lagrangian is built from $j^R_\mu$,

$$
\mathcal{L}_2 = -\frac{f^2}{2}\,\mathrm{Sc}\!\left(\overline{j^R_\mu}\,j^R_\mu\right),
$$

and the **global symmetry** is the left–right action $\tilde U\mapsto g_L\tilde U g_R^{-1}$ under which

$$
j^R_\mu \;\longmapsto\; g_R\,j^R_\mu\,g_R^{-1},
\qquad
j^L_\mu \;\longmapsto\; g_L\,j^L_\mu\,g_L^{-1},
$$

so that $j^R_\mu$ is a singlet of $SU(2)_L$ and transforms in the adjoint of $SU(2)_R$, and conversely for $j^L_\mu$. The two commuting Noether currents are therefore the two adjoint currents of the chiral group $SU(2)_L\times SU(2)_R$, and their diagonal sum is the vector current of the unbroken $SU(2)_V$.

**Flatness.** The Maurer–Cartan form is flat: it satisfies the zero-curvature equation

$$
\partial_\mu j_\nu - \partial_\nu j_\mu + \left[j_\mu, j_\nu\right] = 0 ,
$$

for either current. The identity is algebraic, not dynamical: it is the statement that the components of $\tilde U^{-1}\partial_\mu\tilde U$ are a pure gauge connection, so the field strength of the connection vanishes, and the dynamics of the group-valued field is that of a connection constrained to be pure gauge. The equation of motion of the principal chiral model is the conservation of the flat current,
$$
\partial^\mu j^R_\mu = 0 ,
$$
and the two statements together are the content of the model: flatness is what distinguishes the group-valued field from a general algebra-valued gauge potential.

**Verification.** The left–right invariance of the Lagrangian was checked exactly: for a hedgehog-like field with profile $F(r) = \pi e^{-r^2/2}$ and constant unit quaternions $g_L, g_R$, the values of $\mathrm{Sc}(\overline{\partial_\mu\tilde U}\partial_\mu\tilde U)$ before and after $\tilde U\mapsto g_L\tilde U g_R^{-1}$ agreed to better than $10^{-9}$ at the sampled point, and the agreement is exact in exact arithmetic. The Maurer–Cartan flatness was checked by central differences: the maximum residual over the nine index pairs of $\partial_\mu j_\nu - \partial_\nu j_\mu + [j_\mu,j_\nu]$ was $2.8\times10^{-8}$ at the step $10^{-4}$ and $2.9\times10^{-10}$ at the step $10^{-5}$, the quadratic fall-off of a truncation error and not a residual of the identity. The fields were evaluated in the real four-dimensional representation of $\mathbb{H}$.

**What the framework does not supply here.** The two currents above are a left and a right adjoint current of $SU(2)$, but the framework's $SU(2)_V$ is realised on the group manifold and not on chirality. The axial current that a chiral Lagrangian pairs with the vector current — the $j^{\mu 5}$ whose conservation would tie the sigma model to the fermion sector — is not produced by the center, which is vector-like. The principal chiral model is therefore a global-symmetry construction available to the framework; the chiral current algebra is not. This is the same distinction that the companion articles on chiral fermions and on the Standard Model agenda record for the spinor sector, seen here at the level of the target manifold.

## The Abelian Target, the Compact Phase and the Axion

The other target the framework supplies is the center.

The central phase group is $U(1) = \{e^{i\alpha}e_0\}$, and its group-valued field is the exponential of a central Goldstone field,

$$
\tilde U = \exp\!\left(\frac{i\,\pi}{f}\right)e_0 \in \mathbb{C}_{\mathbb{B}} ,
\qquad
\tilde U\bar{\tilde U} = e_0 ,
$$

with $\pi$ a real central-valued scalar. The two-derivative Lagrangian is again the norm form,

$$
\mathcal{L}_2 = -\frac{f^2}{2}\,\mathrm{Sc}\!\left(\overline{\partial_\mu\tilde U}\,\partial_\mu\tilde U\right)
= \frac12\left[(\partial_t\pi)^2 - (\nabla\pi)^2\right],
$$

the equality being exact for the phase field, whose norm form carries no $\pi$-dependent factor: the abelian model is free. The target is the circle $\mathbb{S}^1$ of phases, with the shift symmetry $\pi\to\pi+\text{const}$ realised nonlinearly. The compactness of the phase is the statement $\pi\sim\pi+2\pi f$, so the target is a circle of circumference proportional to $f$ and the field's values are angles. This is the abelian sigma model of the Goldstone companion, and it is also the structure that the axion's shift symmetry requires: the axion is the pseudo-Goldstone boson of a broken global $U(1)$, and its low-energy Lagrangian is the abelian nonlinear sigma model with the shift symmetry broken only by the anomaly. The companion article on the axion and the Peccei–Quinn mechanism develops that case.

**Verification of the abelian current.** The Noether current of the shift symmetry is $j_\mu = f\partial_\mu\pi$ at lowest order in the normalisation $\tilde U = e^{i\pi/f}$, and its conservation is the equation of motion $\Box\pi = 0$. Both were checked on a **superposition** of two plane waves with $\omega = |k|$, $\pi(t,x) = 0.7\cos(3t-3x) + 0.4\cos(2.5t+2.5x)$, at the point $(t,x) = (0.31,-0.42)$: the on-shell condition $\Box\pi = -\partial_t^2\pi+\partial_x^2\pi$ evaluated to zero to machine precision at the step $10^{-4}$, and the divergence $\partial^\mu j_\mu = -\partial_t j_t+\partial_x j_x$ likewise. The superposition was used deliberately, since a single plane wave cannot distinguish the on-shell condition from a dispersion accident.

## Power Counting and the Effective-Field-Theory Reading

The nonlinear sigma model is an effective field theory, and the derivative expansion is what makes it one. This section states the bookkeeping and separates the standard part from the framework's.

**The derivative expansion.** The Lagrangian of a nonlinear sigma model is a sum of terms with an increasing number of derivatives,

$$
\mathcal{L} = \mathcal{L}_2 + \mathcal{L}_4 + \mathcal{L}_6 + \cdots ,
\qquad
\mathcal{L}_{2n} \sim \frac{f^2}{\Lambda^{2n-2}}\,\partial^{2n},
$$

where $\Lambda$ is the scale of the sector that was integrated out — in the framework, the radial mass $m_h = \sqrt{\lambda}\,v_0$ — and each term carries a coefficient of order one in units of $f$ and $\Lambda$. The two-derivative term fixes the target geometry and the decay constant; the four-derivative terms are the first corrections, and in three spatial dimensions the leading four-derivative term that stabilises a soliton is the Skyrme term. In four spacetime dimensions the nonlinear sigma model is nonrenormalizable in the power-counting sense, and it is used as a low-energy expansion, with the cutoff at $\Lambda$; the divergence structure is the standard one, and in the framework it is the same divergence structure written with the norm-form trace.

**The coset count.** Goldstone's theorem gives one massless scalar per broken generator, so the number of fields is $\dim(G/H)$. For the framework's abelian case $G = U(1)$, $H = \{1\}$ gives one field and target $\mathbb{S}^1$; for the non-abelian case $G = SU(2)_L\times SU(2)_R$, broken to the diagonal $H = SU(2)_V$, gives three fields and target the group manifold $\mathbb{S}^3$; and the $O(N)\to O(N-1)$ case, whose target is $\mathbb{S}^{N-1}$, gives $N-1$ fields. The framework's two targets are the $N=2$ and $N=4$ cases of this list, in the abelian and quaternion forms.

**The two-dimensional exception.** In two spacetime dimensions the $O(N)$ nonlinear sigma model is asymptotically free and its coupling grows in the infrared, so the model is a genuine interacting quantum field theory rather than only a low-energy expansion; the beta function is that of the companion renormalization-group article. The framework's sigma model inherits this statement in two dimensions, because the algebra's role in the computation is confined to the target metric and the trace, and the running is that of the coupling $1/f^2$. In four dimensions the model is the effective theory described above.

**What the framework adds.** The derivative expansion and the power counting are standard and are imported. The framework's contribution is that the target manifold, its invariant metric, and the flat connection of the group-valued field are all read off from the algebra: the target is the compact subgroup manifold, the metric is the norm form, and the Maurer–Cartan form is the algebra-valued one-form of the algebra's own commutators. No new mechanism is introduced, consistent with the absence of a native ladder in the scalar sector that the companion articles record.

## The Biquaternion Reading

**The target is a subgroup manifold.** The framework's nonlinear sigma models have targets $\mathbb{S}^1$ (the central phase) and $\mathbb{S}^3$ (the unit real quaternions). Both are objects of the algebra: $\mathbb{S}^1$ is the unit circle in the center and $\mathbb{S}^3$ is the unit sphere in the real-quaternion subspace. The framework therefore supplies the target spaces rather than borrowing them, which is the structural content of the construction.

**The metric is the norm form.** The invariant metric on the target is the algebra's norm form, $ds^2 = \frac12\mathrm{Sc}(\overline{\tilde U^{-1}d\tilde U}\tilde U^{-1}d\tilde U)$, and the two-derivative Lagrangian is the same form evaluated on the spacetime derivative, where the overall minus sign of the contraction converts the positive target norm into a positive kinetic energy. The identification of the kinetic energy with the norm form is the same identification that the free-field articles make for the scalar, and it is exact.

**The group element is a rotor.** A unit real quaternion is the framework's rotation element, and the nonlinear sigma model's field is therefore a spacetime-dependent rotor. The transformation $\tilde U\mapsto g_L\tilde U g_R^{-1}$ is the composition of a left and a right rotation, i.e. the rotor conjugation that the framework's Lorentz and gauge articles use; the diagonal subgroup is the unbroken rotation, and the coset directions are the Goldstone rotations. This is the geometric reading of the construction, and it is where the framework's algebra and the sigma model coincide.

**The anomaly and the Wess–Zumino–Witten term are not supplied.** The four-dimensional sigma model on a group manifold admits a topological term — the Wess–Zumino–Witten term, a five-dimensional integral whose variation is a four-dimensional total derivative — whose coefficient is quantised and whose presence is tied to the anomaly of the underlying fermions. The framework's center is vector-like and its group manifold carries no chirality, so the anomaly that fixes the Wess–Zumino–Witten level is not produced here; it belongs to the spinor and anomaly articles. The nonlinear sigma model on the framework's target is thus geometrically complete and anomalous-complete only as far as the framework's field content reaches.

## Open Questions

1. **Does the framework fix the normalisation of $f$?** The decay constant is the order parameter in units of the kinetic term; whether the framework's norm form or trace form fixes a preferred relation between $f$ and the vacuum value $v_0$, beyond the linear-model matching $f = \sqrt2\,v_0$, is not shown.

2. **Is the unit quaternion the only non-abelian target available?** The framework's compact group is $SU(2)$; whether higher-rank targets can be built inside $\mathbb{B}$ or one of its modules — and hence whether an $SU(3)$ flavour sigma model is available — is not settled. The Standard Model agenda's flavour discussion bears on this.

3. **The Wess–Zumino–Witten level.** Whether the framework's spinor sector, once its chirality is fixed, supplies the anomaly coefficient that quantises the Wess–Zumino–Witten level is the question that would promote the geometric sigma model to an anomalous one. It is not answered here.

4. **The Skyrme term's coefficient.** The four-derivative stabilising term is treated in the companion Skyrme article; whether the framework's norm form fixes its coefficient relative to $f$, or leaves it a free parameter, is the same quantisation question in a different guise.

5. **The $O(N)$ cases.** The framework's two targets are $N=2$ and $N=4$; whether the framework constrains the $N=3$ and large-$N$ cases, which would connect the sigma model to the $\mathbb{CP}^{N-1}$ construction, is open.

6. **Empirical contact.** As everywhere, the open question is whether the framework's sigma model differs from a standard nonlinear sigma model with the same target and decay constant. The framework's contribution is geometric, and no deviation has been exhibited.

## Summary

The nonlinear sigma model is the low-energy theory of a spontaneously broken continuous symmetry, with fields valued in a coset $G/H$, a Lagrangian built from the invariant metric of the target, and derivative couplings enforced by the non-linear realisation. The framework's algebra supplies two compact targets: the central phase $U(1)\cong\mathbb{S}^1$ and the unit real quaternions $\mathbb{H}^1_{\mathbb{B}}\cong SU(2)\cong\mathbb{S}^3$, the non-abelian one carrying the Goldstone field $\tilde\pi = \pi^a e_a\in\mathfrak{su}(2)\subset\mathbb{M}_-$ and the group-valued field $\tilde U = \exp(\tilde\pi/f)$.

The two-derivative Lagrangian is the norm form of the derivative,

$$
\mathcal{L}_2 = -\frac{f^2}{2}\,\mathrm{Sc}\!\left(\overline{\partial_\mu\tilde U}\,\partial_\mu\tilde U\right)
= \frac12\left[(\partial_t\pi^a)^2 - (\nabla\pi^a)^2\right] + O(\pi^4),
$$

with the invariant metric $ds^2 = \frac12\mathrm{Sc}(\overline{\tilde U^{-1}d\tilde U}\tilde U^{-1}d\tilde U)$ the same object. It is invariant under the global left–right action $\tilde U\mapsto g_L\tilde U g_R^{-1}$, whose diagonal is the unbroken subgroup and whose axial directions are the broken ones, and the Maurer–Cartan form $j^R_\mu = \tilde U^{-1}\partial_\mu\tilde U$ is flat,

$$
\partial_\mu j_\nu - \partial_\nu j_\mu + \left[j_\mu,j_\nu\right] = 0 .
$$

The left–right invariance was verified exactly and the flatness to the finite-difference error (maximum residual $2.8\times10^{-8}$ at step $10^{-4}$, falling quadratically with the step); the abelian current conservation was verified on a superposition of two plane waves with $\omega = |k|$, both the on-shell condition and the divergence vanishing at machine precision.

The framework's contribution to the construction is the target manifold, the invariant metric as the norm form, and the reading of the group element as a rotor; the coset construction, the derivative expansion, the power counting, the $O(N)$ counting and the two-dimensional asymptotic freedom are standard and imported. What the framework does not supply is the axial current tied to chirality and the Wess–Zumino–Witten term, both of which belong to the spinor and anomaly sectors; the sigma model on the framework's target is geometrically complete and anomalous-complete only as far as the framework's field content reaches.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \varepsilon_{jkl}e_l$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center; the abelian target's group |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{H}^1_{\mathbb{B}}$ | Real quaternions; unit real quaternions $\cong SU(2)\cong\mathbb{S}^3$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde U(\tilde X)$ | Group-valued sigma-model field |
| $\tilde\pi = \pi^a e_a \in \mathfrak{su}(2)\subset\mathbb{M}_-$ | Goldstone field (non-abelian) |
| $\tilde U = \exp(\tilde\pi/f)$ | Non-linear field; $\tilde U\bar{\tilde U} = e_0$ |
| $f$ | Decay constant of the broken symmetry |
| $u = \mathrm{Sc}(\tilde\Phi^\dagger\tilde\Phi)$, $V = \frac{\lambda}{4}(u-v_0^2)^2$ | Linear-model invariant and potential |
| $\phi_1 = \sqrt2 v_0 + h$, $\phi_2 = \theta$ | Radial and Goldstone components; $f = \sqrt2 v_0$ |
| $j^R_\mu = \tilde U^{-1}\partial_\mu\tilde U$, $j^L_\mu = \partial_\mu\tilde U\,\tilde U^{-1}$ | Maurer–Cartan currents |
| $\partial_\mu j_\nu - \partial_\nu j_\mu + [j_\mu,j_\nu] = 0$ | Flatness (zero curvature) of the group-valued field |
| $\tilde U\mapsto g_L\tilde U g_R^{-1}$ | Left–right global symmetry; diagonal $SU(2)_V$ unbroken |
| $\mathcal{L}_2 = -\frac{f^2}{2}\mathrm{Sc}(\overline{\partial_\mu\tilde U}\partial_\mu\tilde U)$ | Two-derivative sigma-model Lagrangian |
| $ds^2 = \frac12\mathrm{Sc}(\overline{\tilde U^{-1}d\tilde U}\tilde U^{-1}d\tilde U)$ | Invariant (round) metric on the target |
| $\mathrm{Sc}(e_ae_b) = -\delta_{ab}$ | Trace identity fixing the kinetic normalisation |
| $\mathcal{L}_4$ | Four-derivative term (Skyrme; companion article) |
| $\Lambda = m_h = \sqrt{\lambda}\,v_0$ | Cutoff of the effective theory (radial mass) |
| $\pi\sim\pi+2\pi f$ | Compact phase of the abelian target |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$ metric for index contractions |
| $\mathrm{Tr} = 2\,\mathrm{Sc}$ | Trace convention |

## Further Reading

- M. Gell-Mann and M. Lévy, "The axial vector current in beta decay," *Il Nuovo Cimento* **16** (1960) 705–726, for the linear sigma model and its nonlinear reduction.
- S. Weinberg, "Dynamical approach to current algebra," *Physical Review Letters* **18** (1967) 188–191, and "Nonlinear realizations of chiral symmetry," *Physical Review* **166** (1968) 1568–1577, for the nonlinear realisation and the derivative couplings.
- S. Coleman, J. Wess, and B. Zumino, "Structure of phenomenological Lagrangians. I," *Physical Review* **177** (1969) 2239–2247, and C. Callan, S. Coleman, J. Wess, and B. Zumino, "Structure of phenomenological Lagrangians. II," *Physical Review* **177** (1969) 2247–2250, for the coset construction and the invariant Lagrangian.
- J. Wess and B. Zumino, "Consequences of anomalous Ward identities," *Physics Letters B* **37** (1971) 95–97, and E. Witten, "Global aspects of current algebra," *Nuclear Physics B* **223** (1983) 422–432, for the Wess–Zumino–Witten term and its quantisation.
- A. M. Polyakov, "Interaction of Goldstone particles in two dimensions. Applications to ferromagnets and massive Yang–Mills fields," *Physics Letters B* **59** (1975) 79–81, for the asymptotic freedom of the two-dimensional $O(N)$ model.
- A. M. Polyakov and A. A. Belavin, "Metastable states of two-dimensional isotropic ferromagnets," *JETP Letters* **22** (1975) 245–248, for the instanton structure of the two-dimensional sigma model.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2: *Modern Applications* (Cambridge, 1996), for the effective-Lagrangian and power-counting treatment of the nonlinear sigma model.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the linear sigma model, the Goldstone bosons, and the $O(N)$ model.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the nonlinear sigma model, its renormalization, and the large-$N$ limit.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the coset construction and the current algebra.
- S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry* (Wiley, 1963), for the Maurer–Cartan equations and invariant metrics on Lie groups.
- T. Eguchi, P. B. Gilkey, and A. J. Hanson, "Gravitation, gauge theories and differential geometry," *Physics Reports* **66** (1980) 213–393, for the geometric reading of group-valued fields and topological terms.
- S. B. Treiman, R. Jackiw, B. Zumino, and E. Witten, *Current Algebra and Anomalies* (Princeton, 1985), for the anomaly and current-algebra context of the Wess–Zumino–Witten term.
