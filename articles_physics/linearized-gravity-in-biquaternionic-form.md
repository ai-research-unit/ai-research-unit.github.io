# __Linearized Gravity in Biquaternionic Form__

## Introduction

Linearized gravity is general relativity's weak-field limit. The metric is written as the flat metric plus a small perturbation,

$$
g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \qquad |h_{\mu\nu}| \ll 1,
$$

and the field equations are expanded to first order in $h$. What results is a linear theory of a symmetric rank-two field $h_{\mu\nu}$ that has the shape of a gauge theory: a gauge freedom, a gauge-invariant field strength (the linearized Riemann tensor), a trace-reversal, a harmonic gauge in which the vacuum equations reduce to a wave equation, and two propagating polarizations. It is the gravitational analogue of Maxwell's theory, and it is the setting in which gravitational waves are computed.

The parent article, *Curved Spacetime and the Biquaternion Framework*, established that the biquaternion algebra can **carry** a curved metric by a frame field $\tilde{E}_\mu(x) \in \mathbb{M}_-$ with

$$
g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle,
$$

and that the algebra then supplies the pointwise $SL(2,\mathbb{C})$, its vector representation, and its Lie algebra. It established just as firmly that the algebra supplies none of the dynamics: no action, no field equation for $\tilde{E}_\mu$, and no counterpart of diffeomorphism invariance. Linearized gravity is the smallest setting in which those two statements can be tested against each other, because it linearizes the frame route into a definite kinematic structure and asks how much of the theory that structure actually contains.

The answer developed here is narrower than the title might suggest, and it is worth stating at the outset.

- **Established, and recomputed below.** A metric perturbation $h_{\mu\nu}$ is carried by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through
  $h_{\mu\nu} = \langle \varepsilon_\mu, \delta\tilde{E}_\nu\rangle + \langle \delta\tilde{E}_\mu, \varepsilon_\nu\rangle$,
  and every symmetric $h_{\mu\nu}$ arises this way. The sixteen frame components split as $16 = 10 + 6$, the six-dimensional kernel being the infinitesimal local Lorentz transformations. The linearized gauge transformation $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$ with $\tilde{\Xi} \in \mathbb{M}_-$ reproduces $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu$. The trace-reversal $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}h$ is carried by the frame shift $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac{1}{4}h\,\varepsilon_\mu$ with $h = 2\langle\varepsilon^\nu, \delta\tilde{E}_\nu\rangle$, and the linearized Riemann tensor is invariant under the gauge transformation. In harmonic gauge the linearized vacuum equation is $\Box\bar{h}_{\mu\nu} = 0$, and a transverse-traceless plane wave satisfies it with nonvanishing Riemann curvature.
- **The structural finding.** The metric perturbation is **not** an element of the material sector $\mathbb{M}_-$, and not a single biquaternion at all. The natural single-biquaternion carrier of a symmetric $h_{\mu\nu}$,
  $\sum_{\mu\nu} h_{\mu\nu}\,\varepsilon_\mu\bar{\varepsilon}_\nu$, equals $(\eta^{\mu\nu}h_{\mu\nu})\,e_0$: it is blind to the traceless part of $h$, which is exactly the part that carries the gravitational-wave polarizations. A biquaternion has eight real dimensions and a symmetric rank-two tensor in four dimensions has ten components, so no single biquaternion can be $h_{\mu\nu}$. The field lives in the frame perturbation — an $\mathbb{M}_-$-valued one-form — not in one algebra element.
- **Interpretation and gap, left visible.** The algebra supplies no action and no field equation, so the wave equation is transcribed, not derived; it supplies no representation of diffeomorphism invariance, so the gauge freedom's *origin* is outside the framework even though its *form* can be written in the framework's notation. The coupling to matter, whose source is the symmetric rank-two energy–momentum tensor, is not derived, and the coupling constant $8\pi G/c^4$ is not fixed by the algebra. These are labelled as gaps in the sections where they arise.

**What this article is and is not.** It is a computation of how the frame route of the parent article linearizes, and a comparison of the result with standard linearized gravity. It is not a derivation of general relativity from the biquaternion algebra, and it does not claim that the algebra predicts the linearized Einstein equation. The linear theory is transcribed into the framework's notation; the framework's contribution is the sector structure of the carrier and the form of the gauge transformation, both of which are checked, and neither of which is a dynamics.

**Conventions.** The conventions of the read-list articles are inherited without change. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = -\delta_{jk}e_0 + \epsilon_{jkm}e_m$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$.

Two further conventions are needed and are fixed once, here. First, the **material basis** of $\mathbb{M}_-$ is

$$
\varepsilon_0 = i\,e_0, \qquad \varepsilon_1 = e_1, \qquad \varepsilon_2 = e_2, \qquad \varepsilon_3 = e_3,
$$

which is the basis used in the parent article; its Gram matrix is $\eta_{\mu\nu} = \langle \varepsilon_\mu, \varepsilon_\nu\rangle = \mathrm{diag}(-1, 1, 1, 1)$. This is the metric of the material sector, and it is the flat background of the linearized theory. Second, the coordinates in which the components $h_{\mu\nu}$ are written are the **real** components of the frame, $x^\mu = (ct, x, y, z)$, so that a four-vector is $\tilde{X} = X^\mu\varepsilon_\mu$ and $X^0 = ct$. The framework's imaginary time is related to the same coordinate by $ict = i\,x^0$, so

$$
\partial_{ict} = -i\,\partial_0, \qquad \partial_0 = \frac{\partial}{\partial(ct)},
$$

and therefore

$$
\Box = \partial_{ict}^2 + \Delta = -\partial_0^2 + \Delta = \eta^{\mu\nu}\partial_\mu\partial_\nu .
$$

Both the biquaternionic d'Alembertian and the tensorial wave operator are the same operator in these coordinates; only the naming of the time variable differs. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## Linearized Gravity in Standard Form

This section fixes the target. It is the standard linear theory, written in the coordinate convention just fixed, and every formula displayed here is recomputed in the companion file. Nothing in the section is biquaternionic; it is the theory that the next sections try to write in the framework's notation.

### The Gauge Freedom

The linearized metric is $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$. A coordinate transformation $x^\mu \mapsto x^\mu + \xi^\mu$, with $\xi^\mu$ small, changes the perturbation by

$$
h_{\mu\nu} \;\longmapsto\; h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu, \qquad \xi_\nu = \eta_{\nu\lambda}\xi^\lambda .
$$

This is the **linearized gauge transformation**, and it is a diffeomorphism: it relabels the same physical spacetime. Two perturbations related this way describe the same geometry, so only gauge-invariant combinations of $h_{\mu\nu}$ are physical.

### Curvature

At linear order the Christoffel symbols are

$$
\Gamma^\lambda{}_{\mu\nu} = \tfrac{1}{2}\eta^{\lambda\rho}\left(\partial_\mu h_{\nu\rho} + \partial_\nu h_{\mu\rho} - \partial_\rho h_{\mu\nu}\right),
$$

and the Riemann tensor is

$$
R_{\mu\nu\rho\sigma} = \tfrac{1}{2}\left(\partial_\nu\partial_\rho h_{\mu\sigma} + \partial_\mu\partial_\sigma h_{\nu\rho} - \partial_\mu\partial_\rho h_{\nu\sigma} - \partial_\nu\partial_\sigma h_{\mu\rho}\right).
$$

Contraction gives the linearized Ricci tensor,

$$
R_{\mu\nu} = \tfrac{1}{2}\left(\partial_\mu\partial^\lambda h_{\lambda\nu} + \partial_\nu\partial^\lambda h_{\lambda\mu} - \Box h_{\mu\nu} - \partial_\mu\partial_\nu h\right), \qquad h = \eta^{\mu\nu}h_{\mu\nu},
$$

and the Ricci scalar is $R = \eta^{\mu\nu}R_{\mu\nu} = \partial^\mu\partial^\lambda h_{\lambda\mu} - \Box h$. The Riemann tensor is gauge invariant, and so therefore are $R_{\mu\nu}$ and $R$: they are constructed from the metric, which the relabelling does not change.

### The Trace-Reversal and the Field Equation

The **trace-reversed** perturbation is

$$
\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}h, \qquad \bar{h} = \eta^{\mu\nu}\bar{h}_{\mu\nu} = -h,
$$

so that the operation is an involution up to sign: $h_{\mu\nu} = \bar{h}_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}\bar{h}$. In terms of $\bar{h}_{\mu\nu}$ the linearized Einstein tensor takes the compact form

$$
G_{\mu\nu} = R_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}R = \tfrac{1}{2}\left(\partial_\mu\partial^\lambda\bar{h}_{\lambda\nu} + \partial_\nu\partial^\lambda\bar{h}_{\lambda\mu} - \Box\bar{h}_{\mu\nu} - \eta_{\mu\nu}\partial^\rho\partial^\sigma\bar{h}_{\rho\sigma}\right).
$$

The **harmonic gauge** is the condition

$$
\partial^\lambda\bar{h}_{\lambda\nu} = 0,
$$

which is four conditions on the ten components of $\bar{h}_{\mu\nu}$ and can always be imposed. In it $G_{\mu\nu} = -\tfrac{1}{2}\Box\bar{h}_{\mu\nu}$, and the linearized Einstein equation $G_{\mu\nu} = \tfrac{8\pi G}{c^4}T_{\mu\nu}$ becomes

$$
\Box\bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4}\,T_{\mu\nu}.
$$

In vacuum, $T_{\mu\nu} = 0$ and the equation reduces to the wave equation

$$
\Box\bar{h}_{\mu\nu} = 0 .
$$

The harmonic condition is preserved by the residual gauge transformations with $\Box\xi_\nu = 0$, exactly as the Lorenz condition of electromagnetism is preserved by residual gauge functions with $\Box\Gamma = 0$. The analogy with electromagnetism is close: $\bar{h}_{\mu\nu}$ plays the role of the potential, $R_{\mu\nu\rho\sigma}$ the role of the field strength, and the harmonic condition the role of the Lorenz gauge. It is not exact, and the differences are the subject of the rest of the article.

### The Plane Wave

A plane-wave solution of the vacuum equation is

$$
h_{\mu\nu} = A_{\mu\nu}\cos(k_\lambda x^\lambda), \qquad k^\mu k_\mu = 0,
$$

with a constant symmetric amplitude $A_{\mu\nu}$. The harmonic condition and the residual gauge freedom can be used to put it in **transverse-traceless** form, in which $k^\mu A_{\mu\nu} = 0$ and $\eta^{\mu\nu}A_{\mu\nu} = 0$. For propagation in the $+z$ direction, $k^\mu = (\omega/c)(1,0,0,1)$ in the coordinates $x^\mu = (ct, x, y, z)$, so that the phase is $\omega(z/c - t)$, and the two independent amplitudes are the **plus** polarization, $A_{11} = -A_{22} \ne 0$, and the **cross** polarization, $A_{12} = A_{21} \ne 0$, all other components zero. For such a wave $R_{\mu\nu} = 0$, while $R_{\mu\nu\rho\sigma} \ne 0$: the curvature is nonzero even though the Ricci tensor vanishes, which is what distinguishes a gravitational wave from a gauge artifact. The two polarizations are the physical, propagating degrees of freedom of the linear theory.

This is the theory that the framework's frame route will now be asked to contain.

## The Frame Route: Where the Perturbation Lives

The parent article's frame route writes the metric as $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle$ with $\tilde{E}_\mu \in \mathbb{M}_-$. Linearize it around the flat basis $\varepsilon_\mu$:

$$
\tilde{E}_\mu = \varepsilon_\mu + \delta\tilde{E}_\mu, \qquad \delta\tilde{E}_\mu \in \mathbb{M}_- .
$$

The perturbation $\delta\tilde{E}_\mu$ is a frame perturbation: four material-sector biquaternions, one for each coordinate index $\mu$. Expanding the Gram matrix to first order,

$$
g_{\mu\nu} = \langle \varepsilon_\mu + \delta\tilde{E}_\mu,\ \varepsilon_\nu + \delta\tilde{E}_\nu\rangle
= \eta_{\mu\nu} + \langle \varepsilon_\mu, \delta\tilde{E}_\nu\rangle + \langle \delta\tilde{E}_\mu, \varepsilon_\nu\rangle + O(\delta\tilde{E}^2),
$$

so the metric perturbation is

$$
\boxed{\;h_{\mu\nu} = \langle \varepsilon_\mu, \delta\tilde{E}_\nu\rangle + \langle \delta\tilde{E}_\mu, \varepsilon_\nu\rangle \;=\; \mathrm{Sc}\!\left(\varepsilon_\mu\,\bar{\delta\tilde{E}}_\nu\right) + \mathrm{Sc}\!\left(\delta\tilde{E}_\mu\,\bar{\varepsilon}_\nu\right).\;}
$$

The right-hand side is automatically symmetric in $\mu\nu$, because the bilinear form $\langle\cdot,\cdot\rangle$ is symmetric. The map is also surjective onto symmetric perturbations: given any symmetric $h_{\mu\nu}$, the choice

$$
\delta\tilde{E}_\mu = \tfrac{1}{2}h_{\mu\lambda}\,\varepsilon^\lambda, \qquad \varepsilon^\lambda = \eta^{\lambda\rho}\varepsilon_\rho,
$$

reproduces it exactly, since $\langle \varepsilon_\mu, \tfrac{1}{2}h_{\nu\lambda}\varepsilon^\lambda\rangle = \tfrac{1}{2}h_{\nu\mu}$ and the two terms add to $h_{\mu\nu}$. Both statements were checked by direct computation, the surjectivity on randomly generated symmetric perturbations rather than on the expression that suggested it.

### The Counting

The frame perturbation has $4 \times 4 = 16$ real components; a symmetric $h_{\mu\nu}$ has $10$. The difference is accounted for by the **local Lorentz transformations** of the frame. If $\tilde{\Lambda} = e_0 + \tilde{G}$ is an infinitesimal unit-norm biquaternion, the frame transforms as

$$
\tilde{E}_\mu \;\longmapsto\; \tilde{\Lambda}\tilde{E}_\mu\tilde{\Lambda}^\dagger
= \tilde{E}_\mu + \tilde{G}\tilde{E}_\mu + \tilde{E}_\mu\tilde{G}^\dagger + O(\tilde{G}^2),
$$

and at linear order, with $\tilde{E}_\mu$ replaced by $\varepsilon_\mu$ in the correction,

$$
\delta\tilde{E}_\mu \;\longmapsto\; \delta\tilde{E}_\mu + \tilde{G}\varepsilon_\mu + \varepsilon_\mu\tilde{G}^\dagger .
$$

The unit-norm condition $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ linearizes to $\tilde{G} + \bar{\tilde{G}} = 0$, which says that $\tilde{G}$ is a **complex pure vector**, $\tilde{G} \in \mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3, ie_1, ie_2, ie_3\}$. This is the six-dimensional traceless subspace that the parent article identifies with the Lorentz Lie algebra $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$, spanned by the rotation generators $J_k = e_k$ and the boost generators $K_k = ie_k$. Its elements leave the metric perturbation invariant:

$$
\langle \varepsilon_\mu, \tilde{G}\varepsilon_\nu + \varepsilon_\nu\tilde{G}^\dagger\rangle
+ \langle \tilde{G}\varepsilon_\mu + \varepsilon_\mu\tilde{G}^\dagger, \varepsilon_\nu\rangle = 0,
$$

because the infinitesimal rotor conjugation preserves the bilinear form. This is the kernel of the map $\delta\tilde{E}_\mu \mapsto h_{\mu\nu}$, and it has dimension $6$, so $16 - 6 = 10$, the dimension of the metric. A computation that included an $e_0$ component in $\tilde{G}$ — which the unit-norm condition forbids — gives a nonzero shift of $h$; the restriction to the complex pure vector part is what makes the kernel statement exact. Both the vanishing shift and the failure without the restriction were checked.

## The Graviton Is Not a Material Biquaternion

The perturbation $h_{\mu\nu}$ is a symmetric rank-two tensor. The parent article records the representation-theoretic bookkeeping: under the Lorentz group such objects sit in $(1,1)\oplus(0,0)$, of dimension $9 + 1 = 10$, while the framework's kinematical fields are four-vectors, $(\tfrac12,\tfrac12)$, of dimension $4$, and lie in $\mathbb{M}_-$. The companion article on the material space records in the same way that neither the antisymmetric field strength nor the symmetric energy–momentum tensor is an element of $\mathbb{M}_-$. The linearized graviton belongs to the same class of objects, and it is worth making the obstruction concrete for this case rather than inheriting it as a slogan.

**No single biquaternion can carry $h_{\mu\nu}$.** A biquaternion has four complex coefficients, that is eight real dimensions, while a symmetric rank-two tensor in four dimensions has ten independent components. The deficit of two is intrinsic: whatever identification is attempted, two components of $h$ have nowhere to go.

**The natural single-biquaternion carrier loses exactly the traceless part.** Suppose one tries the most obvious packaging, the biquaternion

$$
\tilde{H} = \sum_{\mu,\nu=0}^{3} h_{\mu\nu}\,\varepsilon_\mu\bar{\varepsilon}_\nu .
$$

For symmetric $h_{\mu\nu}$ this element is Hermitian, $\tilde{H}^\dagger = \tilde{H}$, and so lies in the informational sector $\mathbb{M}_+$ rather than the material sector $\mathbb{M}_-$. More importantly, it is not faithful. Computing the products $\varepsilon_\mu\bar{\varepsilon}_\nu$ from the multiplication rules gives

$$
\tilde{H} = \left(\eta^{\mu\nu}h_{\mu\nu}\right)e_0 = h\,e_0 ,
$$

a real multiple of the identity carrying only the **Lorentzian trace** $h = \eta^{\mu\nu}h_{\mu\nu}$. The off-diagonal contributions cancel in pairs by the symmetry of $h$, and the spatial-spatial contributions collapse to $\sum_k h_{kk}$; what survives is the trace and nothing else. The traceless part of $h_{\mu\nu}$ — nine of the ten components, and all of the transverse-traceless content that carries the two gravitational-wave polarizations — maps to zero. The same collapse occurs for the reverse ordering $\sum h_{\mu\nu}\bar{\varepsilon}_\mu\varepsilon_\nu$. The computation was performed on randomly generated symmetric perturbations, and the result was checked to be the Lorentzian trace in each case; the traceless diagonal case was checked separately and maps to zero.

This is the precise sense in which the graviton is not a material biquaternion, and the obstacle is sharper than the observation that $h$ is not in $\mathbb{M}_-$.

- It is not a four-vector, so there is no packaging of it as an element of the material sector: $\mathbb{M}_-$ is the four-vector representation $(\tfrac12,\tfrac12)$, of dimension $4$, while $h$ is a symmetric rank-two object, $(1,1)\oplus(0,0)$, of dimension $10$.
- The natural packaging that does land in an algebra sector lands in $\mathbb{M}_+$, not $\mathbb{M}_-$, and it retains only the trace.
- It is not any single element of $\mathbb{B}$: eight real dimensions cannot hold ten components.

The correct carrier is the frame perturbation. For each coordinate direction $\mu$, $\delta\tilde{E}_\mu$ is a material-sector biquaternion, i.e. a four-vector; the collection $\{\delta\tilde{E}_\mu\}$ is an **$\mathbb{M}_-$-valued one-form**, sixteen real components modulo the six-dimensional local Lorentz kernel. The potential of the linearized graviton lives in the same sector as the electromagnetic potential, but as a one-form of material four-vectors rather than as one material four-vector. This is the framework's version of the statement that the graviton is a spin-two field while the photon is spin-one: both potentials are valued in $\mathbb{M}_-$, and they differ in the index structure carried on top of it.

## Gauge Freedom as the Derivative of a Material Four-Vector

The linearized diffeomorphism of the standard theory has a definite image in the frame perturbation. Let $\tilde{\Xi} \in \mathbb{M}_-$ be a material four-vector and let

$$
\delta\tilde{E}_\mu \;\longmapsto\; \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}.
$$

Then the metric perturbation changes by

$$
h_{\mu\nu} \;\longmapsto\; h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu,
\qquad \xi_\nu = \langle \tilde{\Xi}, \varepsilon_\nu\rangle = \mathrm{Sc}\!\left(\tilde{\Xi}\,\bar{\varepsilon}_\nu\right),
$$

which is exactly the linearized gauge transformation of the standard theory. The check is direct: the two terms of $h_{\mu\nu}$ contribute $-\partial_\mu\langle\tilde{\Xi},\varepsilon_\nu\rangle$ and $-\partial_\nu\langle\tilde{\Xi},\varepsilon_\mu\rangle$, and summing gives $-\partial_\mu\xi_\nu - \partial_\nu\xi_\mu$. The result was checked with a randomly chosen smooth $\tilde{\Xi}$ and an independently generated $h$, and the frame-level transformation reproduced the metric-level transformation to machine precision.

**The shape of the transformation is the electromagnetic one.** The gauge article, *The Gauge Principle in Biquaternionic Form*, obtains the electromagnetic gauge transformation as the localization of a central phase, in the form

$$
\tilde{A} \;\longmapsto\; \tilde{A} - \tilde{\nabla}\Gamma,
$$

the biquaternionic gradient of a scalar $\Gamma$. The gravitational transformation above has the same shape: it is the exterior derivative of the gauge parameter, with the central scalar $\Gamma$ replaced by a material four-vector and the biquaternion potential $\tilde{A}$ replaced by the $\mathbb{M}_-$-valued one-form,

$$
\delta\tilde{E} \;\longmapsto\; \delta\tilde{E} - d\tilde{\Xi}, \qquad d\tilde{\Xi} = \partial_\mu\tilde{\Xi}\,dx^\mu,\qquad \delta\tilde{E} = \delta\tilde{E}_\mu\,dx^\mu .
$$

In both cases the transformation is the derivative of a lower object, and in both cases it generates a gauge redundancy of the potential that leaves the field strength invariant. What changes is the module the gauge parameter is valued in: the central scalars for electromagnetism, the material sector $\mathbb{M}_-$ for gravity.

**The origin of the transformation is not the electromagnetic one.** This must be said plainly, because the formal resemblance invites the opposite conclusion. The electromagnetic gauge freedom is the localization of a symmetry of the algebra's center — a genuine algebraic structure that the framework supplies. The linearized gravitational gauge freedom is a **diffeomorphism**, a relabelling of the points of the manifold. The parent article states the gap without qualification: the algebra $\mathbb{B}$ has no representation of $\mathrm{Diff}(M)$ and nothing in it corresponds to a coordinate change on the base. The transformation $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$ is written in the framework's notation, and it is the correct image of the linearized diffeomorphism in that notation, but the framework does not generate it. The resemblance to the gauge principle is a resemblance of form, not a common origin. This is the central qualification of the article, and it is not repaired anywhere below.

There is a second, smaller point carried by the frame language. The local Lorentz transformations of the previous section act on $\delta\tilde{E}_\mu$ but leave $h_{\mu\nu}$ unchanged; they are a redundancy of the frame, not of the metric. The diffeomorphism $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$ is the transformation that actually moves the metric. In tetrad gravity the two are independent gauges, and the framework sees the first as an algebraic symmetry and the second only as a transcription.

## The Gauge-Invariant Field Strength

The field strength of the linearized graviton is the linearized Riemann tensor, and its defining property is gauge invariance. Under $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu$ each of the four terms of $R_{\mu\nu\rho\sigma}$ is replaced by two terms, and the eight resulting third-derivative terms cancel in pairs. For example, the term $-\partial_\nu\partial_\rho\partial_\mu\xi_\sigma$ produced by $\partial_\nu\partial_\rho h_{\mu\sigma}$ cancels the term $+\partial_\mu\partial_\rho\partial_\nu\xi_\sigma$ produced by $-\partial_\mu\partial_\rho h_{\nu\sigma}$, because the two differ only by the order of the three derivatives. The other three components of $\xi$ cancel the same way, and the result is $\delta R_{\mu\nu\rho\sigma} = 0$. This was also checked numerically on a randomly generated $h$ and a randomly generated smooth $\xi$, with the four-index tensor agreeing before and after the gauge transformation to the accuracy of the finite differences.

The field strength is therefore gauge invariant, exactly as the electromagnetic $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is. It is also further from the algebra than $h$ is. The Riemann tensor has four indices; in four dimensions it has twenty independent components, and it is not a biquaternion, not a material four-vector, and not a rank-two object of any kind. The framework cannot hold it as a single element.

What the framework can do is hold its **bivector structure index by index**. For each antisymmetric pair $(\mu,\nu)$ on the base, the second pair $(\rho,\sigma)$ is antisymmetric and can be contracted with the basis to give an element of the Lie subspace,

$$
\tilde{R}_{\mu\nu} = \tfrac{1}{2}\sum_{\rho,\sigma} R_{\mu\nu\rho\sigma}\,\bar{\varepsilon}^\rho\varepsilon^\sigma .
$$

Because antisymmetrization in $\rho\sigma$ is antisymmetrization in the product of two material basis vectors, each $\tilde{R}_{\mu\nu}$ is a complex pure vector, hence an element of the six-dimensional bivector subspace that the parent article identifies with $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$. The gravitational field strength is thus a **Lie-algebra-valued two-form** on the manifold, and every value it takes sits inside $\mathbb{B}$. This is the exact structural analogue of the electromagnetic field strength: the gauge article records that the electromagnetic $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is a single bivector, the curvature of an abelian connection, while the gravitational $\tilde{R}_{\mu\nu}$ is a bivector-valued two-form, the curvature of a connection valued in the non-abelian Lorentz Lie algebra. The identification of $\tilde{R}_{\mu\nu}$ with the curvature of the torsion-free spin connection is the standard tetrad identification, and the parent article records that metric compatibility and the vanishing of torsion are conditions the algebra does not select. The algebra supplies the home for each bivector value; it does not supply the object, because the object is built from $h$, which is not in the algebra.

The physical, gauge-invariant content of the curvature is its **Weyl part**, the ten-component tensor obtained from $R_{\mu\nu\rho\sigma}$ by removing the Ricci and scalar traces. In vacuum the two coincide, because the Ricci part vanishes, and the propagating degrees of freedom are in the Weyl tensor. Its encoding in the biquaternion framework — through the self-dual and anti-self-dual bivectors, or through the five complex Newman–Penrose scalars $\Psi_0, \dots, \Psi_4$ — is a separate problem, and it is not attempted here; it is recorded among the open questions.

## The Field Equation and the Trace-Reversal Step

The field equation is where the framework's d'Alembertian enters directly, and where the trace-reversal has a clean biquaternionic image. Both are worth displaying.

### The Trace-Reversal as a Frame Shift

Let $h = \eta^{\mu\nu}h_{\mu\nu}$ be the trace of the metric perturbation. From the frame representation, the trace is itself a biquaternionic pairing,

$$
h = 2\,\langle\varepsilon^\nu, \delta\tilde{E}_\nu\rangle = 2\,\mathrm{Sc}\!\left(\varepsilon^\nu\,\bar{\delta\tilde{E}}_\nu\right).
$$

Define the **trace-reversed frame perturbation**

$$
\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac{1}{4}h\,\varepsilon_\mu .
$$

Then the metric perturbation it carries is the trace-reversed one,

$$
\langle\varepsilon_\mu, \bar{\delta\tilde{E}}_\nu\rangle + \langle\bar{\delta\tilde{E}}_\mu, \varepsilon_\nu\rangle
= h_{\mu\nu} - \tfrac{1}{2}\eta_{\mu\nu}h = \bar{h}_{\mu\nu},
$$

because $\langle\varepsilon_\mu, \tfrac{1}{4}h\,\varepsilon_\nu\rangle + \langle\tfrac{1}{4}h\,\varepsilon_\mu, \varepsilon_\nu\rangle = \tfrac{1}{2}h\,\eta_{\mu\nu}$. The trace-reversal is therefore not an operation that takes the graviton out of the framework: it is a shift of each $\delta\tilde{E}_\mu$ by a multiple of the corresponding basis vector $\varepsilon_\mu$, with the multiple fixed by the biquaternionic trace. The identity was checked on randomly generated $h$ with the two sides agreeing exactly, and it reproduces $\bar{h} = -h$ as it must. This is the natural place for a sign to be fitted to the case that suggested it, so it was checked on a random case and the $\bar{h} = -h$ contraction was verified independently.

### The Wave Equation

The biquaternionic d'Alembertian $\Box$ is a real operator built from the basis $e_0, e_1, e_2, e_3$ and the partial derivatives, so it commutes with the constant basis vectors $\varepsilon_\mu$ and acts componentwise on biquaternion-valued fields. Applying it to the trace-reversed frame perturbation and using the frame representation of $\bar{h}_{\mu\nu}$,

$$
\Box\bar{h}_{\mu\nu} = \langle\varepsilon_\mu, \Box\bar{\delta\tilde{E}}_\nu\rangle + \langle\Box\bar{\delta\tilde{E}}_\mu, \varepsilon_\nu\rangle .
$$

Consequently $\Box\bar{h}_{\mu\nu} = 0$ holds if and only if $\Box\bar{\delta\tilde{E}}_\mu$ lies in the local-Lorentz kernel of the map to $h$: a frame perturbation whose $\Box$ is a pure local Lorentz transformation produces no metric perturbation. If the local Lorentz freedom is fixed — for instance by demanding that $\delta\tilde{E}_\mu$ and $\varepsilon_\mu$ be related by a symmetric matrix, as in the surjectivity construction above — then the wave equation takes the direct form

$$
\Box\,\bar{\delta\tilde{E}}_\mu = 0 .
$$

The same structure appears in the electromagnetic analogue: without the Lorenz condition, $\Box\tilde{A}$ is a pure gauge gradient, and in Lorenz gauge it vanishes. Here the harmonic condition plays the role of the Lorenz condition and the local Lorentz transformations play the role of the residual gauge freedom. With a source, the linearized Einstein equation $\Box\bar{h}_{\mu\nu} = -\tfrac{16\pi G}{c^4}T_{\mu\nu}$ is transcribed componentwise; its right-hand side, the energy–momentum tensor, is the symmetric rank-two object whose biquaternion representation is studied in *Exercise: The Electromagnetic Energy–Momentum Tensor*, where it is built as a biquaternion bilinear because no single biquaternion can carry it. The gravitational source belongs to the same class, and the same obstruction applies to it.

**What is not derived.** The operator $\Box$ is inherited; the equation $\Box\bar{h}_{\mu\nu} = 0$ is the standard linearized vacuum equation, transcribed. The framework supplies no action whose variation would yield it, and no principle selecting the frame. The parent article's conclusion is unchanged at linear order: the kinematical fibre is present, the dynamics is absent. The wave equation is written correctly in the framework's notation, and that is all that is claimed.

## The Plane Wave and the Two Polarizations

The plane-wave case is the sharpest check that the transcription is faithful, and it is where the gauge-invariant and gauge-dependent parts separate cleanly. Take a transverse-traceless perturbation propagating in the $z$ direction,

$$
h_{11} = -h_{22} = A\cos\!\left(\omega\left(\tfrac{z}{c} - t\right)\right), \qquad h_{00} = h_{33} = h_{0\mu} = h_{3\mu} = 0,
$$

with the other off-diagonal components zero. The wave vector is null, $k^\mu k_\mu = 0$, and the amplitude is transverse, $k^\mu A_{\mu\nu} = 0$, and traceless, $\eta^{\mu\nu}A_{\mu\nu} = 0$. A direct computation gives

$$
R_{\mu\nu} = 0, \qquad R_{\mu\nu\rho\sigma} \ne 0,
$$

with, for example, $R_{0101} = -R_{0202} \ne 0$ while $R_{0303} = 0$. The curvature is nonzero, so the wave is not pure gauge; the Ricci tensor vanishes, so it solves the vacuum equation. This was checked numerically for both a plus-polarization amplitude ($A_{11} = -A_{22}$) and the corresponding cross-polarization amplitude ($A_{12} = A_{21}$), with the same qualitative result in each case: the Ricci tensor vanishes and the Riemann tensor does not.

The two independent amplitudes are the two polarizations of the linear theory. In the framework's variables they are carried entirely by the **traceless part** of $\delta\tilde{E}_\mu$; the trace part of the frame perturbation carries only the trace $h$, and, by the result of the section above, the trace is the only thing the natural single-biquaternion packaging can see. So the two propagating degrees of freedom of the graviton are precisely the components that a single biquaternion cannot represent. This is the clearest statement of the article's structural finding: the framework carries the graviton as a frame perturbation, and the algebra element into which one might try to compress it retains only the trace, which is not propagating in vacuum.

The detailed phenomenology of these waves — their generation, their interaction with matter, and the observational constraints on their polarizations — is not developed here. The linearized kinematics and the gauge structure are the subject of this article; the wave theory is a separate development.

## What the Algebra Supplies and What It Does Not

The boundary can be drawn as a list, in the manner of the parent article.

**Supplied by the algebra, and recomputed here.** The material basis $\varepsilon_\mu$ with its Gram matrix $\eta_{\mu\nu} = \mathrm{diag}(-1,1,1,1)$; the representation of a metric perturbation by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through $h_{\mu\nu} = \langle\varepsilon_\mu, \delta\tilde{E}_\nu\rangle + \langle\delta\tilde{E}_\mu, \varepsilon_\nu\rangle$, with every symmetric $h$ realized; the decomposition $16 = 10 + 6$ with the six-dimensional local Lorentz kernel, and the exact invariance of $h$ under the kernel; the gauge transformation $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$ with $\tilde{\Xi} \in \mathbb{M}_-$, reproducing $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu$; the trace-reversal as the frame shift $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac{1}{4}h\,\varepsilon_\mu$ with $h = 2\langle\varepsilon^\nu,\delta\tilde{E}_\nu\rangle$; the invariance of the linearized Riemann tensor under the gauge transformation; the bivector-valued two-form packaging of the curvature; and the reduction of the vacuum equation to $\Box\bar{h}_{\mu\nu} = 0$, hence to $\Box\bar{\delta\tilde{E}}_\mu = 0$ once the local Lorentz freedom is fixed.

**Interpretation, not derivation.** Reading $\delta\tilde{E}_\mu$ as a tetrad and $h_{\mu\nu}$ as the metric it carries is a geometric reading of the algebraic construction, exactly as in the parent article. The algebra is consistent with the reading, and the computations above make the consistency precise, but the algebra does not force the bundle-theoretic or geometric picture.

**Not supplied, and left as gaps.** An action principle and a field equation for the frame, and hence any derivation of the linearized Einstein equation. A representation of diffeomorphism invariance, which is the origin of the gravitational gauge freedom written above. A selection principle for the connection, and with it the identification of the bivector-valued curvature $\tilde{R}_{\mu\nu}$ as the curvature of any particular connection. A derivation of the coupling to matter, and of the constant $8\pi G/c^4$. A single-biquaternion or material-sector representative of the graviton; the natural one collapses to the trace. And, as always in this framework, empirical content: nothing here predicts a deviation from standard linearized gravity.

## Open Questions

1. **A biquaternion action whose linearization is linearized gravity.** Is there an action functional of $\tilde{E}_\mu$ and $\tilde{\Gamma}_\mu$, built from the algebra's own operations, whose linearized variation gives the linearized Einstein equation? The parent article states that none is known; the question is whether the linearized problem is any easier, and in particular whether the trace-reversal identity of this article points toward a natural quadratic action.

2. **The non-abelian curvature and the gauge article's gap.** The linearized gravitational field strength is a $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$-valued two-form. The gauge article records that the framework supplies non-commutativity but not a compactness or reality condition selecting a gauge algebra. Does the local Lorentz algebra, which is non-compact and selected by the metric, meet that gap, or is it a different structure that the electromagnetic case cannot use?

3. **A biquaternionic harmonic condition.** The harmonic condition $\partial^\lambda\bar{h}_{\lambda\nu} = 0$ is four conditions on the frame. Is there a distinguished biquaternionic differential operator — a divergence on $\mathbb{M}_-$-valued one-forms — that produces it naturally, in the way that $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A}) = 0$ produces the Lorenz condition for the electromagnetic potential?

4. **The Weyl tensor in the algebra.** The propagating content of linearized gravity is the Weyl tensor, and its natural biquaternionic encoding is through the self-dual and anti-self-dual bivectors. Can the five Newman–Penrose scalars be written as components of biquaternion objects, and does the algebra's decomposition into $\mathbb{M}_+$ and $\mathbb{M}_-$ organise them?

5. **The relation to the parent's local-scale route.** The parent article shows that the local scale factor $c = 1/\sqrt{\epsilon\mu}$, read as a metric, is a class in which Ricci-flatness forces flatness, so it carries no gravitational waves. Does linearizing that route reproduce the statement that its linearized Riemann tensor vanishes identically, and does the frame route's nonvanishing Riemann tensor make the two routes inequivalent already at linear order?

6. **The informational sector.** The natural Hermitian packaging of the metric perturbation is its trace, an element of $\mathbb{M}_+$. Is that a coincidence of the packaging, or does the two-sector structure constrain which perturbations are representable? The trace is not propagating in vacuum, which makes the coincidence worth understanding rather than dismissing.

7. **Empirical content.** As everywhere in the framework, the open question is whether any of this yields a prediction distinguishing it from standard linearized gravity. The transcription developed here does not.

## Summary

Linearized gravity in biquaternionic form is the linearization of the parent article's frame route. The metric perturbation is carried by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through $h_{\mu\nu} = \langle\varepsilon_\mu,\delta\tilde{E}_\nu\rangle + \langle\delta\tilde{E}_\mu,\varepsilon_\nu\rangle$, and every symmetric perturbation arises this way. The sixteen frame components split as $16 = 10 + 6$, the kernel being the infinitesimal local Lorentz transformations, which leave the metric perturbation exactly invariant.

The graviton is not a material biquaternion. It is not an element of $\mathbb{M}_-$, it is not a single element of $\mathbb{B}$ — eight real dimensions cannot hold ten components — and the natural single-biquaternion packaging $\sum h_{\mu\nu}\varepsilon_\mu\bar{\varepsilon}_\nu$ collapses to the Lorentzian trace $h\,e_0$, losing the traceless part that carries the two polarizations. The carrier is the frame perturbation, an $\mathbb{M}_-$-valued one-form: the graviton's potential lives in the same sector as the electromagnetic potential, but as a one-form of material four-vectors rather than as one material four-vector.

The gauge freedom is written as $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$ with $\tilde{\Xi} \in \mathbb{M}_-$, which reproduces $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu$. Its shape is the electromagnetic one — the exterior derivative of a gauge parameter — with a material four-vector replacing the central scalar; but its origin is a diffeomorphism, for which the algebra has no representation. The shape is transcribed; the origin is not supplied.

The field strength is the linearized Riemann tensor, gauge invariant under the transformation above, and further from the algebra than $h$: a rank-four tensor with twenty components, held by the framework only as a bivector-valued two-form whose values lie in the Lorentz Lie algebra. The trace-reversal has a clean biquaternionic image, the frame shift $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac14 h\,\varepsilon_\mu$ with $h = 2\langle\varepsilon^\nu,\delta\tilde{E}_\nu\rangle$. In harmonic gauge, with the local Lorentz freedom fixed, the vacuum equation is $\Box\bar{\delta\tilde{E}}_\mu = 0$, and a transverse-traceless plane wave satisfies it with nonvanishing curvature — the standard two-polarization result, carried by exactly the traceless components that a single biquaternion cannot hold.

What the algebra supplies is the kinematic fibre of linearized gravity and the form of its gauge structure. What it does not supply is the dynamics: no action, no derived field equation, no diffeomorphism invariance, no coupling to matter, no empirical content. The title names a form, and that is what has been written.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\varepsilon_\mu = (ie_0, e_1, e_2, e_3)$ | Material basis of $\mathbb{M}_-$ |
| $\eta_{\mu\nu} = \langle\varepsilon_\mu,\varepsilon_\nu\rangle = \mathrm{diag}(-1,1,1,1)$ | Flat metric of the material sector |
| $\langle\tilde{Q},\tilde{P}\rangle = \mathrm{Sc}(\tilde{Q}\bar{\tilde{P}})$ | Bilinear form on $\mathbb{M}_-$ |
| $x^\mu = (ct,x,y,z)$, $\partial_\mu$ | Real coordinates and their derivatives; $ict = i x^0$ |
| $\partial_{ict} = -i\partial_0$ | Relation of the framework's imaginary time derivative to $\partial_0$ |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}, \Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \eta^{\mu\nu}\partial_\mu\partial_\nu$ | Biquaternionic gradient, conjugate, d'Alembertian |
| $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ | Linearized metric |
| $\tilde{E}_\mu = \varepsilon_\mu + \delta\tilde{E}_\mu$ | Frame field and frame perturbation, $\delta\tilde{E}_\mu \in \mathbb{M}_-$ |
| $h_{\mu\nu} = \langle\varepsilon_\mu,\delta\tilde{E}_\nu\rangle + \langle\delta\tilde{E}_\mu,\varepsilon_\nu\rangle$ | Metric perturbation carried by the frame perturbation |
| $h = \eta^{\mu\nu}h_{\mu\nu} = 2\langle\varepsilon^\nu,\delta\tilde{E}_\nu\rangle$ | Trace of the metric perturbation |
| $\bar{h}_{\mu\nu} = h_{\mu\nu} - \tfrac12\eta_{\mu\nu}h$, $\bar{h} = -h$ | Trace-reversed perturbation |
| $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac14 h\,\varepsilon_\mu$ | Trace-reversed frame perturbation |
| $\tilde{G} \in \mathrm{span}_{\mathbb{R}}\{e_k, ie_k\}$ | Infinitesimal local Lorentz generator (complex pure vector) |
| $\tilde{\Xi} \in \mathbb{M}_-$ | Gauge four-vector, $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial_\mu\tilde{\Xi}$ |
| $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial_\mu\xi_\nu - \partial_\nu\xi_\mu$, $\xi_\nu = \langle\tilde{\Xi},\varepsilon_\nu\rangle$ | Linearized gauge transformation |
| $R_{\mu\nu\rho\sigma}$ | Linearized Riemann tensor (gauge-invariant field strength) |
| $R_{\mu\nu}$, $G_{\mu\nu}$ | Linearized Ricci tensor and Einstein tensor |
| $\tilde{R}_{\mu\nu} = \tfrac12\sum_{\rho\sigma}R_{\mu\nu\rho\sigma}\bar{\varepsilon}^\rho\varepsilon^\sigma$ | Curvature as a bivector-valued two-form |
| $\partial^\lambda\bar{h}_{\lambda\nu} = 0$ | Harmonic gauge |
| $\Box\bar{h}_{\mu\nu} = -\tfrac{16\pi G}{c^4}T_{\mu\nu}$ | Linearized Einstein equation |
| $A_{\mu\nu}$, plus/cross | Plane-wave amplitude; the two polarizations |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula of the informational sector |

## Further Reading

- Companion articles: *Curved Spacetime and the Biquaternion Framework*; *The Gauge Principle in Biquaternionic Form*; *Maxwell's Equations in the Biquaternionic Formulation*; *The Field-Strength Biquaternion and Its Invariants*; *Exercise: The Electromagnetic Energy–Momentum Tensor*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *Biquaternion Representation Theory*.
- Charles W. Misner, Kip S. Thorne, and John A. Wheeler, *Gravitation* (Freeman, 1973), for the linearized theory, the transverse-traceless gauge, and the two polarizations of a gravitational wave.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the linearized Einstein equation, the trace-reversal, and the harmonic gauge.
- Sean M. Carroll, *Spacetime and Geometry: An Introduction to General Relativity* (Cambridge, 2019), for a compact treatment of linearized gravity and its gauge structure.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spin-coefficient and bivector formulation of the curvature on which the Weyl-tensor encoding rests.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic treatment of gravity in the same rotor language used here.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra formulation of the tetrad and the curvature bivector.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the bivector structure of two-forms.
