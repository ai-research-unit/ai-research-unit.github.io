# __Linearized Gravity in Biquaternionic Form__

## Introduction

Linearized gravity is general relativity's weak-field limit. The metric is the flat interval plus a small perturbation,

$$
g_{\mu\nu}\,\mathrm{d}r_x^\mu\mathrm{d}r_x^\nu = -c^2\mathrm{d}r'_t^2+\mathrm{d}r_x^2+\mathrm{d}r_y^2+\mathrm{d}r_z^2+h_{\mu\nu}\,\mathrm{d}r_x^\mu\mathrm{d}r_x^\nu,\qquad |h_{\mu\nu}| \ll 1,
$$

and the field equations are expanded to first order in $h$. What results is a linear theory of a symmetric rank-two field $h_{\mu\nu}$ that has the shape of a gauge theory: a gauge freedom, a gauge-invariant field strength (the linearized Riemann tensor), a trace-reversal, a harmonic gauge in which the vacuum equations reduce to a wave equation, and two propagating polarizations. It is the gravitational analogue of Maxwell's theory, and it is the setting in which gravitational waves are computed.

The parent article, *Curved Spacetime and the Biquaternion Framework*, established that the biquaternion algebra can **carry** a curved metric by a frame field $\tilde{E}_\mu(x) \in \mathbb{M}_-$ with

$$
g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle_{\natural},
$$

and that the algebra then supplies the pointwise $SL(2,\mathbb{C})$, its vector representation, and its Lie algebra. It established just as firmly that the algebra supplies none of the dynamics: no action, no field equation for $\tilde{E}_\mu$, and no counterpart of diffeomorphism invariance. Linearized gravity is the smallest setting in which those two statements can be tested against each other, because it linearizes the frame route into a definite kinematic structure and asks how much of the theory that structure actually contains.

The answer developed here is narrower than the title might suggest, and it is worth stating at the outset.

- **Established, and recomputed below.** A metric perturbation $h_{\mu\nu}$ is carried by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through
  $h_{\mu\nu} = \langle \varepsilon_\mu, \delta\tilde{E}_\nu\rangle_{\natural} + \langle \delta\tilde{E}_\mu, \varepsilon_\nu\rangle_{\natural}$,
  and every symmetric $h_{\mu\nu}$ arises this way. The sixteen frame components split as $16 = 10 + 6$, the six-dimensional kernel being the infinitesimal local Lorentz transformations. The linearized gauge transformation $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}$ with $\tilde Q_{\mathrm d} \in \mathbb{M}_-$ reproduces $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu$. The trace-reversal $\bar{h}_{00}=h_{00}+\tfrac{1}{2}h$, $\bar{h}_{0k}=h_{0k}$ and $\bar{h}_{kl}=h_{kl}-\tfrac{1}{2}h\,\delta_{kl}$ is carried by the frame shift $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac{1}{4}h\,\varepsilon_\mu$ with $h = 2\sum_\nu\langle\hat\varepsilon_\nu, \delta\tilde{E}_\nu\rangle_{\natural}$, and the linearized Riemann tensor is invariant under the gauge transformation. In harmonic gauge the linearized vacuum equation is $\Box\bar{h}_{\mu\nu} = 0$, and a transverse-traceless plane wave satisfies it with nonvanishing Riemann curvature.
- **The structural finding.** The metric perturbation is **not** an element of the material sector $\mathbb{M}_-$, and not a single biquaternion at all. The natural single-biquaternion carrier of a symmetric $h_{\mu\nu}$,
  $\sum_{\mu\nu} h_{\mu\nu}\,\varepsilon_\mu\varepsilon_\nu^{\natural}$, equals $h\,e_t$, with $h$ the trace of $h_{\mu\nu}$: it is blind to the traceless part of $h$, which is exactly the part that carries the gravitational-wave polarizations. A biquaternion has eight real dimensions and a symmetric rank-two tensor in four dimensions has ten components, so no single biquaternion can be $h_{\mu\nu}$. The field lives in the frame perturbation — an $\mathbb{M}_-$-valued one-form — not in one algebra element.
- **Interpretation and gap, left visible.** The algebra supplies no action and no field equation, so the wave equation is transcribed, not derived; it supplies no representation of diffeomorphism invariance, so the gauge freedom's *origin* is outside the framework even though its *form* can be written in the framework's notation. The coupling to matter, whose source is the symmetric rank-two energy–momentum tensor, is not derived, and the coupling constant $8\pi G/c^4$ is not fixed by the algebra. These are labelled as gaps in the sections where they arise.

**What this article is and is not.** It is a computation of how the frame route of the parent article linearizes, and a comparison of the result with standard linearized gravity. It is not a derivation of general relativity from the biquaternion algebra, and it does not claim that the algebra predicts the linearized Einstein equation. The linear theory is transcribed into the framework's notation; the framework's contribution is the sector structure of the carrier and the form of the gauge transformation, both of which are checked, and neither of which is a dynamics.

The body is written in the biquaternion algebra. An action on an element is written as it acts, $\tilde Q\mapsto a\tilde Qb$, and a cell appears only where the operator itself is the subject, in *The Fermionic Coupling at First Order*. The gamma matrices appear only in the final section, *The Legacy Pauli Gamma Formulation*, which is a translation table and not a second formulation.

The framework's conventions are used here and are not restated. The material basis $\varepsilon_\mu$ of $\mathbb{M}_-$, the real coordinates $x_\mu=(c r'_{t},x,y,z)$ of the material frame and the biquaternionic d'Alembertian $\Box$ are those of *Frame and Metric Conventions* and *Operator and Calculus Conventions*, and every pairing written here is the quaternionic form $\langle\cdot,\cdot\rangle_{\natural}$ of *Norm and Pairing Conventions*. The plain form is a different pairing and is not used. There is one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$ on the four $Q_\mu$; the material interval is that form read on $Q_t=i c r'_t$, $-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$, and its one minus is the square of the $i$. The one symbol this article fixes for itself is the dual material basis $\hat\varepsilon_\lambda$, fixed by $\langle\hat\varepsilon_\lambda,\varepsilon_\rho\rangle_{\natural}=\delta_{\lambda\rho}$; it carries the trace and the surjectivity of the frame map below.

One derived form is needed repeatedly, and it is recorded once. The framework's imaginary time is $Q_t=ix_0$, so $\partial/\partial R_t=-i\,\partial/\partial x_0$ and the biquaternionic d'Alembertian is the tensorial wave operator,

$$
\Box = \partial^2/\partial R_t^2 + \Delta = -\frac{1}{c^2}\frac{\partial^2}{\partial r'_t^2}+\frac{\partial^2}{\partial r_x^2}+\frac{\partial^2}{\partial r_y^2}+\frac{\partial^2}{\partial r_z^2} .
$$

A product $k_\lambda x_\lambda$ below is the invariant contraction $-k_0x_0+k_1x_1+k_2x_2+k_3x_3$, not a sum of like components; its one minus is the square of the $i$ in $Q_t=i c r'_t$.

## Linearized Gravity in Standard Form

This section fixes the target. It is the standard linear theory, written in the coordinate convention named above, and every formula displayed here was checked by direct computation. Nothing in the section is biquaternionic; it is the theory that the next sections try to write in the framework's notation.

### The Gauge Freedom

The linearized metric is the flat interval plus $h_{\mu\nu}$. A coordinate transformation $x_\mu \mapsto x_\mu + \zeta_\mu$, with $\zeta_\mu$ small, changes the perturbation by

$$
h_{\mu\nu} \;\longmapsto\; h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu.
$$

This is the **linearized gauge transformation**, and it is a diffeomorphism: it relabels the same physical spacetime. Two perturbations related this way describe the same geometry, so only gauge-invariant combinations of $h_{\mu\nu}$ are physical.

### Curvature

At linear order the Christoffel symbols are

$$
\begin{aligned}
\Gamma_{0\mu\nu} &= -\tfrac{1}{2}\left(\partial/\partial x_\mu h_{\nu 0} + \partial/\partial x_\nu h_{\mu 0} - \partial/\partial x_0 h_{\mu\nu}\right),\\[2pt]
\Gamma_{k\mu\nu} &= +\tfrac{1}{2}\left(\partial/\partial x_\mu h_{\nu k} + \partial/\partial x_\nu h_{\mu k} - \partial/\partial x_k h_{\mu\nu}\right),
\end{aligned}
$$

where the first slot is the connection's upper slot, written low in the all-low labelling of this article; the two lines are the one contraction, with the minus of the interval on the time row. The Riemann tensor is

$$
\mathrm{Riem}_{\mu\nu\rho\sigma} = \tfrac{1}{2}\left(\partial^2/\partial x_\nu\partial x_\rho h_{\mu\sigma} + \partial^2/\partial x_\mu\partial x_\sigma h_{\nu\rho} - \partial^2/\partial x_\mu\partial x_\rho h_{\nu\sigma} - \partial^2/\partial x_\nu\partial x_\sigma h_{\mu\rho}\right).
$$

Contraction, with the sign convention used here, gives the linearized Ricci tensor,

$$
\begin{aligned}
\mathrm{Ric}_{\mu\nu} = \tfrac{1}{2}\Bigl(&\partial/\partial x_\mu\,D_\nu
+\partial/\partial x_\nu\,D_\mu
-\Box h_{\mu\nu}-\partial^2/\partial x_\mu\partial x_\nu h\Bigr),
\qquad D_\nu = -\partial/\partial x_0 h_{0\nu}+\sum_k\partial/\partial x_k h_{k\nu},\quad h = -h_{00}+h_{11}+h_{22}+h_{33},
\end{aligned}
$$

and the Ricci scalar is

$$
\mathrm{Ric} = -\mathrm{Ric}_{00}+\mathrm{Ric}_{11}+\mathrm{Ric}_{22}+\mathrm{Ric}_{33}
= \partial^2/\partial x_0^2\,h_{00}-\sum_k\left(\partial^2/\partial x_0\partial x_k\,h_{k0}+\partial^2/\partial x_k\partial x_0\,h_{0k}\right)+\sum_{k,l}\partial^2/\partial x_k\partial x_l\,h_{lk}-\Box h .
$$

The Riemann tensor is gauge invariant, and therefore so are $\mathrm{Ric}_{\mu\nu}$ and $\mathrm{Ric}$: they are constructed from the metric perturbation in a way that the relabelling leaves invariant.

### The Trace-Reversal and the Field Equation

The **trace-reversed** perturbation is

$$
\bar{h}_{00} = h_{00} + \tfrac{1}{2}h, \qquad \bar{h}_{0k} = h_{0k}, \qquad \bar{h}_{kl} = h_{kl} - \tfrac{1}{2}h\,\delta_{kl}, \qquad \bar{h} = -\bar{h}_{00}+\bar{h}_{11}+\bar{h}_{22}+\bar{h}_{33} = -h,
$$

so that the map is its own inverse, $\bar{\bar h}_{\mu\nu} = h_{\mu\nu}$, and only the trace changes sign: $h_{00} = \bar{h}_{00} - \tfrac{1}{2}\bar{h}$, $h_{0k}=\bar{h}_{0k}$ and $h_{kl} = \bar{h}_{kl} - \tfrac{1}{2}\bar{h}\,\delta_{kl}$. In terms of $\bar{h}_{\mu\nu}$ the linearized Einstein tensor takes the compact form

$$
\begin{aligned}
G_{00} = \mathrm{Ric}_{00} + \tfrac{1}{2}\mathrm{Ric} = \tfrac{1}{2}\Bigl(&\partial/\partial x_0\,\bar{D}_0+\partial/\partial x_0\,\bar{D}_0-\Box\bar{h}_{00}+\bar{S}\Bigr),\\[2pt]
G_{0k} = \mathrm{Ric}_{0k} = \tfrac{1}{2}\Bigl(&\partial/\partial x_0\,\bar{D}_k+\partial/\partial x_k\,\bar{D}_0-\Box\bar{h}_{0k}\Bigr),\\[2pt]
G_{kl} = \mathrm{Ric}_{kl} - \tfrac{1}{2}\delta_{kl}\mathrm{Ric} = \tfrac{1}{2}\Bigl(&\partial/\partial x_k\,\bar{D}_l+\partial/\partial x_l\,\bar{D}_k-\Box\bar{h}_{kl}-\delta_{kl}\bar{S}\Bigr).
\end{aligned}
$$

with $\bar{D}_\nu = -\partial/\partial x_0\bar{h}_{0\nu}+\sum_k\partial/\partial x_k\bar{h}_{k\nu}$ and $\bar{S} = \partial^2/\partial x_0^2\bar{h}_{00}-\sum_k(\partial^2/\partial x_0\partial x_k\bar{h}_{k0}+\partial^2/\partial x_k\partial x_0\bar{h}_{0k})+\sum_{k,l}\partial^2/\partial x_k\partial x_l\bar{h}_{lk}$; the minus on the time row of each contraction is the one minus of the interval.

The **harmonic gauge** is the condition

$$
-\partial/\partial x_0\bar{h}_{0\nu}+\partial/\partial x_1\bar{h}_{1\nu}+\partial/\partial x_2\bar{h}_{2\nu}+\partial/\partial x_3\bar{h}_{3\nu} = 0,
$$

which is four conditions on the ten components of $\bar{h}_{\mu\nu}$ and can always be imposed. In it $G_{\mu\nu} = -\tfrac{1}{2}\Box\bar{h}_{\mu\nu}$, and the linearized Einstein equation $G_{\mu\nu} = \tfrac{8\pi G}{c^4}T_{\mu\nu}$ becomes

$$
\Box\bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4}\,T_{\mu\nu}.
$$

In vacuum, $T_{\mu\nu} = 0$ and the equation reduces to the wave equation

$$
\Box\bar{h}_{\mu\nu} = 0 .
$$

The harmonic condition is preserved by the residual gauge transformations with $\Box\zeta_\nu = 0$, exactly as the Lorenz condition is preserved by gauge functions with $\Box\Gamma = 0$. That gives the count: ten components of $h_{\mu\nu}$, four removed by the harmonic condition, four more by the residual transformations, and two polarizations left. The analogy with electromagnetism is close — $\bar{h}_{\mu\nu}$ is the potential, $\mathrm{Riem}_{\mu\nu\rho\sigma}$ the field strength, and the harmonic condition the Lorenz gauge — and it is made precise in *The Field Equation and the Trace-Reversal Step*.

### The Plane Wave

A plane-wave solution of the vacuum equation is

$$
h_{\mu\nu} = A_{\mu\nu}\cos(k_\lambda x_\lambda), \qquad -k_0^2+k_1^2+k_2^2+k_3^2 = 0,
$$

with a constant symmetric amplitude $A_{\mu\nu}$. The harmonic condition and the residual gauge freedom can be used to put it in **transverse-traceless** form, in which $-k_0A_{0\nu}+k_1A_{1\nu}+k_2A_{2\nu}+k_3A_{3\nu} = 0$ and $-A_{00}+A_{11}+A_{22}+A_{33} = 0$. For propagation in the $+z$ direction, $k_\mu = (\omega/c)(1,0,0,1)$ in the coordinates $x_\mu = (c r'_{t}, x, y, z)$, so that the phase is $\omega(r_z/c - r'_t)$, and the two independent amplitudes are the **plus** polarization, $A_{11} = -A_{22} \ne 0$, and the **cross** polarization, $A_{12} = A_{21} \ne 0$, all other components zero. For such a wave $\mathrm{Ric}_{\mu\nu} = 0$, while $\mathrm{Riem}_{\mu\nu\rho\sigma} \ne 0$: the curvature is nonzero even though the Ricci tensor vanishes, which is what distinguishes a gravitational wave from a gauge artifact. The two polarizations are the physical, propagating degrees of freedom of the linear theory.

This is the theory that the framework's frame route will now be asked to contain.

## The Frame Route: Where the Perturbation Lives

The parent article's frame route writes the metric as $g_{\mu\nu} = \langle \tilde{E}_\mu, \tilde{E}_\nu\rangle_{\natural}$ with $\tilde{E}_\mu \in \mathbb{M}_-$. Linearize it around the flat basis $\varepsilon_\mu$:

$$
\tilde{E}_\mu = \varepsilon_\mu + \delta\tilde{E}_\mu, \qquad \delta\tilde{E}_\mu \in \mathbb{M}_- .
$$

The perturbation $\delta\tilde{E}_\mu$ is a frame perturbation: four material-sector biquaternions, one for each coordinate index $\mu$. Expanding the Gram matrix to first order,

$$
g_{\mu\nu} = \langle \varepsilon_\mu + \delta\tilde{E}_\mu,\ \varepsilon_\nu + \delta\tilde{E}_\nu\rangle_{\natural}
= \langle \varepsilon_\mu, \varepsilon_\nu\rangle_{\natural} + \langle \varepsilon_\mu, \delta\tilde{E}_\nu\rangle_{\natural} + \langle \delta\tilde{E}_\mu, \varepsilon_\nu\rangle_{\natural} + O(\delta\tilde{E}^2),
$$

so the metric perturbation is

$$
\boxed{\;h_{\mu\nu} = \langle \varepsilon_\mu, \delta\tilde{E}_\nu\rangle_{\natural} + \langle \delta\tilde{E}_\mu, \varepsilon_\nu\rangle_{\natural} \;=\; \mathrm{Sc}\!\left(\varepsilon_\mu^{\natural}\,\delta\tilde{E}_\nu\right) + \mathrm{Sc}\!\left(\delta\tilde{E}_\mu^{\natural}\,\varepsilon_\nu\right)\;}.
$$

The right-hand side is automatically symmetric in $\mu\nu$, because the general quaternionic bilinear form $\langle\cdot,\cdot\rangle_{\natural}$ is symmetric. The map is also surjective onto symmetric perturbations: given any symmetric $h_{\mu\nu}$, the choice

$$
\delta\tilde{E}_\mu = \tfrac{1}{2}\sum_\lambda h_{\mu\lambda}\,\hat\varepsilon_\lambda ,
$$

reproduces it exactly, since $\sum_\lambda\langle \varepsilon_\mu, \tfrac{1}{2}h_{\nu\lambda}\hat\varepsilon_\lambda\rangle_{\natural} = \tfrac{1}{2}h_{\nu\mu}$ and the two terms add to $h_{\mu\nu}$. Both statements were checked numerically: the symmetry on random perturbations, the surjectivity on random symmetric $h$, and the rank of the map on the sixteen frame directions, which is $10$ with a kernel of dimension $6$.

### The Counting

The frame perturbation has $4 \times 4 = 16$ real components; a symmetric $h_{\mu\nu}$ has $10$. The difference is accounted for by the **local Lorentz transformations** of the frame. If $\tilde{U} = e_t + \vec G$ is an infinitesimal unit-norm biquaternion, the frame transforms as

$$
\tilde{E}_\mu \;\longmapsto\; \tilde{U}\tilde{E}_\mu\tilde{U}^{*}
= \tilde{E}_\mu + \vec G\tilde{E}_\mu + \tilde{E}_\mu\vec G^{*} + O(\vec G^2),
$$

and at linear order, with $\tilde{E}_\mu$ replaced by $\varepsilon_\mu$ in the correction,

$$
\delta\tilde{E}_\mu \;\longmapsto\; \delta\tilde{E}_\mu + \vec G\varepsilon_\mu + \varepsilon_\mu\vec G^{*} .
$$

The unit-norm condition $\tilde{U}\tilde{U}^{\natural} = e_t$ linearizes to $\vec G + \vec G^{\natural} = 0$, which says that $\vec G$ is a **complex pure vector**, $\vec G \in \mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z, i\vec e_x, i\vec e_y, i\vec e_z\}$. This is the six-dimensional traceless subspace that the parent article identifies with the Lorentz Lie algebra $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$, spanned by the rotation generators $J_k = \vec e_k$ and the boost generators $K_k = i\vec e_k$. Its elements leave the metric perturbation invariant:

$$
\langle \varepsilon_\mu, \vec G\varepsilon_\nu + \varepsilon_\nu\vec G^{*}\rangle_{\natural}
+ \langle \vec G\varepsilon_\mu + \varepsilon_\mu\vec G^{*}, \varepsilon_\nu\rangle_{\natural} = 0,
$$

because the infinitesimal rotor conjugation preserves the bilinear form. This is the kernel of the map $\delta\tilde{E}_\mu \mapsto h_{\mu\nu}$, and it has dimension $6$, so $16 - 6 = 10$, the dimension of the metric. A real $e_t$ component in $\vec G$ — which the unit-norm condition forbids — shifts $h_{\mu\nu}$ by a multiple of $\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural}$, a rescaling of the trace and not a Lorentz transformation; the restriction to the complex pure-vector part is what makes the kernel statement exact. Both the vanishing shift and the failure without the restriction were checked.

### An External Variant: Frame Fields That Carry Their Own Connection

An external construction dispenses with the vierbein altogether, and it linearises onto exactly this section's frame perturbation. J. Fredsted (*Spinor fields without Lorentz frames in curved spacetime using complexified quaternions*, arXiv:0811.1357v4 [math-ph], 2009) takes as primitive not a frame field in a fixed background but four $\mathbb{M}_-$-valued fields $s_\mu$ that play the roles of basis, metric and connection data at once. In this paragraph the bar is the source's quaternion conjugate — the corpus's $\natural$ — not the corpus's complex conjugation, and $\langle\cdot,\cdot\rangle$ is the source's bilinear form. The metric is the polar form $g_{\mu\nu} = \langle s_\mu, s_\nu\rangle$, the local Lorentz freedom is the rotor conjugation $s_\mu \mapsto \Lambda s_\mu\bar{\Lambda}$ with $\Lambda$ in $Sp(1,\mathbb{C}) \cong SL(2,\mathbb{C})$, and — the part that has no counterpart in this article's frame route — the connection is **not inserted beside the frame but determined by it**, through the algebraic vielbein postulate $D_\rho s_\nu \equiv 0$ with $D_\rho s_\nu = \partial/\partial x_\rho s_\nu + \omega_\rho s_\nu + s_\nu\bar{\omega}_\rho^* - \Gamma_{\mu\nu\rho}s_\mu$. Solving for the coefficients gives

$$
\Gamma_{\mu\nu\rho} = \left\langle \hat s_\mu,\ \partial/\partial x_\rho s_\nu + \omega_\rho s_\nu + s_\nu\bar{\omega}_\rho^*\right\rangle ,
$$

with $\hat s_\mu$ the dual basis, $\langle \hat s_\mu, s_\nu\rangle = \delta_{\mu\nu}$. That $\Gamma_{\mu\nu\rho}$ is real-valued and that this $\Gamma$ indeed annihilates $D_\rho s_\nu$ were checked here, on random bases and random connection fields.

The relevance to this article is the linearisation. Expand the basis as $s_\mu = \varepsilon_\mu + \delta s_\mu$ with $\delta s_\mu \in \mathbb{M}_-$ and the flat $\varepsilon_\mu$. Then $\delta s_\mu$ **is** this article's frame perturbation $\delta\tilde{E}_\mu$, and the metric perturbation read off it is this section's own,

$$
h_{\mu\nu} = \langle \varepsilon_\mu, \delta s_\nu\rangle_{\natural} + \langle \delta s_\mu, \varepsilon_\nu\rangle_{\natural} ,
$$

with the exact expansion $g_{\mu\nu} = \langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural} + h_{\mu\nu} + \langle \delta s_\mu, \delta s_\nu\rangle_{\natural}$; both were checked. The local freedom and the counting are the same as above: the rotor conjugation of $s_\mu$ reproduces the six-dimensional kernel, $16 - 6 = 10$. So the external construction is not a rival to this section but a completion of it — it linearises to the same $h_{\mu\nu}$ and the same gauge count, and it supplies the connection that this article's frame route, as recorded, leaves as a separate inserted object. Two qualifications keep the comparison honest. The construction is in the source's own algebra conventions and the corpus does not adopt it; and it carries no action for $s_\mu$ either, so the boundary at the end of this article — no dynamics is derived for the frame — is unchanged by it.

### The Fermionic Coupling at First Order

The construction above is pure geometry: it linearizes the frame and reads the metric perturbation off it. Where matter attaches to that frame, the parent article's attachment is the one-sided covariant derivative $D_\mu\tilde{Ξ}^{\mathrm{sp}} = \partial/\partial x_\mu\,\tilde{Ξ}^{\mathrm{sp}} + \vec\Gamma_\mu\tilde{Ξ}^{\mathrm{sp}}$ on an element-valued Dirac field, with $\vec\Gamma_\mu$ the spin connection. An external source shows that this attachment has two inequivalent forms, and the difference is not a higher-order subtlety here.

For the standard vierbein coupling of a Dirac fermion to gravity, gauging the flat equation and varying the gauged action **do not commute**: the varied equation carries an anticommutator term between the generator cell of a coordinate and the Lorentz generator, which the substituted equation does not. The generator cell of the coordinate $x_\mu$ is the frame cell $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, with $\nu(t)=x$ and $\nu(k)=y$, and $S_{ab}$ is the Lorentz generator those cells build, the quarter-commutator displayed in *Matrix Representations Conventions*, §*The Clifford Structure*. The relevant commutator is, with $\varepsilon=(1,-1,-1,-1)$ the plain weight of the frame,

$$
\bigl[L_{e_c}R_{\vec e_{\nu(c)}}^{\mathrm{axf}},S_{ab}\bigr]
=\varepsilon_c\delta_{ca}\,L_{e_b}R_{\vec e_{\nu(b)}}^{\mathrm{axf}}
-\varepsilon_c\delta_{cb}\,L_{e_a}R_{\vec e_{\nu(a)}}^{\mathrm{axf}},
$$

which is nonzero whenever $c$ equals exactly one of $a,b$, rather than vanishing (J. Fredsted, arXiv:1906.12200v3 [physics.gen-ph], 2019; recorded, with its world-index repair, in *Curved Spacetime and the Biquaternion Framework*). Both the frame perturbation $\delta\tilde{E}_\mu$ and the spin connection $\vec\Gamma_\mu$ are **first order** in the perturbation of this article, and the discrepancy is linear in the connection, so it is first order as well: it does not disappear as the perturbation is taken small. A linearized system that couples a Dirac field to $h_{\mu\nu}$ therefore has to say which of the two forms it linearizes, and the corpus's own curved Dirac equation — the one-sided chirality pair displayed in *The Legacy Pauli Gamma Formulation* — is the substituted one.

This is recorded as an external caution and is not resolved here. Nothing constructed in this article changes, because the construction above contains no matter coupling at all; what changes is the interpretation of the article's own gap list, where "a derivation of the coupling to matter" has to be strengthened — the coupling is not merely underived, it is not unique in the standard formulation.

## The Graviton Is Not a Material Biquaternion

The perturbation $h_{\mu\nu}$ is a symmetric rank-two tensor. The parent article records the representation-theoretic bookkeeping: under the Lorentz group such objects sit in $(1,1)\oplus(0,0)$, of dimension $9 + 1 = 10$, while the framework's kinematical fields are four-vectors, $(\tfrac12,\tfrac12)$, of dimension $4$, and lie in $\mathbb{M}_-$. The companion article on the material space records in the same way that neither the antisymmetric field strength nor the symmetric energy–momentum tensor is an element of $\mathbb{M}_-$. The linearized graviton belongs to the same class of objects, and it is worth making the obstruction concrete for this case rather than inheriting it as a slogan.

**No single biquaternion can carry $h_{\mu\nu}$.** A biquaternion has four complex coefficients, that is eight real dimensions, while a symmetric rank-two tensor in four dimensions has ten independent components. The deficit of two is intrinsic: whatever identification is attempted, two components of $h$ have nowhere to go.

**The natural single-biquaternion carrier loses exactly the traceless part.** Suppose one tries the most obvious packaging, the biquaternion

$$
\tilde R_\psi = \sum_{\mu,\nu=0}^{3} h_{\mu\nu}\,\varepsilon_\mu\varepsilon_\nu^{\natural} .
$$

For symmetric $h_{\mu\nu}$ this element is Hermitian, $\tilde R_\psi^{*} = \tilde R_\psi$, and so lies in the informational sector $\mathbb{M}_+$ rather than the material sector $\mathbb{M}_-$. More importantly, it is not faithful. Computing the products $\varepsilon_\mu\varepsilon_\nu^{\natural}$ from the multiplication rules gives

$$
\boxed{\;\tilde R_\psi = h\,e_t\;},
$$

a real multiple of the identity carrying only the **trace** $h = -h_{00}+h_{11}+h_{22}+h_{33}$, one minus being the square of the $i$ in $Q_t=i c r'_t$. The off-diagonal contributions cancel in pairs by the symmetry of $h$, and the spatial-spatial contributions collapse to $\sum_k h_{kk}$; what survives is the trace and nothing else. The traceless part of $h_{\mu\nu}$ — nine of the ten components, and all of the transverse-traceless content that carries the two gravitational-wave polarizations — maps to zero. The same collapse occurs for the reverse ordering $\sum h_{\mu\nu}\varepsilon_\mu^{\natural}\varepsilon_\nu$. The computation was performed on randomly generated symmetric perturbations, and the result was checked to be the trace $h=-h_{00}+h_{11}+h_{22}+h_{33}$ in each case; the traceless diagonal case was checked separately and maps to zero.

This is the precise sense in which the graviton is not a material biquaternion, and the obstacle is sharper than the observation that $h$ is not in $\mathbb{M}_-$.

- It is not a four-vector, so there is no packaging of it as an element of the material sector: $\mathbb{M}_-$ is the four-vector representation $(\tfrac12,\tfrac12)$, of dimension $4$, while $h$ is a symmetric rank-two object, $(1,1)\oplus(0,0)$, of dimension $10$.
- The natural packaging that does land in an algebra sector lands in $\mathbb{M}_+$, not $\mathbb{M}_-$, and it retains only the trace.
- It is not any single element of $\mathbb{B}$: eight real dimensions cannot hold ten components.

The correct carrier is the frame perturbation. For each coordinate direction $\mu$, $\delta\tilde{E}_\mu$ is a material-sector biquaternion, i.e. a four-vector; the collection $\{\delta\tilde{E}_\mu\}$ is an **$\mathbb{M}_-$-valued one-form**, sixteen real components modulo the six-dimensional local Lorentz kernel. The potential of the linearized graviton lives in the same sector as the electromagnetic potential, but as a one-form of material four-vectors rather than as one material four-vector. This is the framework's version of the statement that the graviton is a spin-two field while the photon is spin-one: both potentials are valued in $\mathbb{M}_-$, and they differ in the index structure carried on top of it.

## Gauge Freedom as the Derivative of a Material Four-Vector

The linearized diffeomorphism of the standard theory has a definite image in the frame perturbation. Let $\tilde Q_{\mathrm d} \in \mathbb{M}_-$ be a material four-vector and let

$$
\delta\tilde{E}_\mu \;\longmapsto\; \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}.
$$

Then the metric perturbation changes by

$$
h_{\mu\nu} \;\longmapsto\; h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu,
\qquad \zeta_\nu = \langle \tilde Q_{\mathrm d}, \varepsilon_\nu\rangle_{\natural} = \mathrm{Sc}\!\left(\tilde Q_{\mathrm d}^{\natural}\,\varepsilon_\nu\right),
$$

which is exactly the linearized gauge transformation of the standard theory. The check is direct: the two terms of $h_{\mu\nu}$ contribute $-\partial/\partial x_\mu\,\langle\tilde Q_{\mathrm d},\varepsilon_\nu\rangle_{\natural}$ and $-\partial/\partial x_\nu\,\langle\tilde Q_{\mathrm d},\varepsilon_\mu\rangle_{\natural}$, and summing gives $-\partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu$. The result was checked with a randomly chosen smooth $\tilde Q_{\mathrm d}$ and an independently generated $h$, and the frame-level transformation reproduced the metric-level transformation to machine precision.

**The shape of the transformation is the electromagnetic one.** The gauge article, *The Gauge Principle in Biquaternionic Form*, obtains the electromagnetic gauge transformation as the localization of a central phase, in the form

$$
\tilde{A} \;\longmapsto\; \tilde{A} - \tilde{\nabla}\Gamma,
$$

the biquaternionic gradient of a scalar $\Gamma$. The gravitational transformation above has the same shape: it is the exterior derivative of the gauge parameter, with the central scalar $\Gamma$ replaced by a material four-vector and the biquaternion potential $\tilde{A}$ replaced by the $\mathbb{M}_-$-valued one-form,

$$
\delta\tilde{E} \;\longmapsto\; \delta\tilde{E} - d\tilde Q_{\mathrm d}, \qquad d\tilde Q_{\mathrm d} = \partial/\partial x_\mu\,\tilde Q_{\mathrm d}\,dx_\mu,\qquad \delta\tilde{E} = \delta\tilde{E}_\mu\,dx_\mu .
$$

In both cases the transformation is the derivative of a lower object, and in both cases it generates a gauge redundancy of the potential that leaves the field strength invariant. What changes is the module the gauge parameter is valued in: the central scalars for electromagnetism, the material sector $\mathbb{M}_-$ for gravity.

**The origin of the transformation is not the electromagnetic one.** This must be said plainly, because the formal resemblance invites the opposite conclusion. The electromagnetic gauge freedom is the localization of a symmetry of the algebra's centre — a genuine algebraic structure that the framework supplies. The linearized gravitational gauge freedom is a **diffeomorphism**, a relabelling of the points of the manifold. The parent article states the gap without qualification: the algebra $\mathbb{B}$ has no representation of $\mathrm{Diff}(M)$ and nothing in it corresponds to a coordinate change on the base. The transformation $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}$ is written in the framework's notation, and it is the correct image of the linearized diffeomorphism in that notation, but the framework does not generate it. The resemblance to the gauge principle is a resemblance of form, not a common origin. This is the central qualification of the article, and it is not repaired anywhere below.

There is a second, smaller point carried by the frame language. The local Lorentz transformations of the previous section act on $\delta\tilde{E}_\mu$ but leave $h_{\mu\nu}$ unchanged; they are a redundancy of the frame, not of the metric. The diffeomorphism $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}$ is the transformation that actually moves the metric. In tetrad gravity the two are independent gauges, and the framework sees the first as an algebraic symmetry and the second only as a transcription.

## The Gauge-Invariant Field Strength

The field strength of the linearized graviton is the linearized Riemann tensor, and its defining property is gauge invariance. Under $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu$ each of the four terms of $\mathrm{Riem}_{\mu\nu\rho\sigma}$ is replaced by two terms, and the eight resulting third-derivative terms cancel in pairs. For example, the term $-\partial^3/\partial x_\nu\partial x_\rho\partial x_\mu\,\zeta_\sigma$ produced by $\partial^2/\partial x_\nu\partial x_\rho h_{\mu\sigma}$ cancels the term $+\partial^3/\partial x_\mu\partial x_\rho\partial x_\nu\,\zeta_\sigma$ produced by $-\partial^2/\partial x_\mu\partial x_\rho h_{\nu\sigma}$, because the two differ only by the order of the three derivatives. The other three components of $\zeta$ cancel the same way, and the result is $\delta \mathrm{Riem}_{\mu\nu\rho\sigma} = 0$. This was also checked numerically on a randomly generated $h$ and a randomly generated smooth $\zeta$, with the four-index tensor agreeing before and after the gauge transformation to the accuracy of the finite differences.

The field strength is therefore gauge invariant, exactly as the electromagnetic $F_{\mu\nu} = \partial/\partial x_\mu A_\nu - \partial/\partial x_\nu A_\mu$ is. It is also further from the algebra than $h$ is. The Riemann tensor has four indices; in four dimensions it has twenty independent components, and it is not a biquaternion, not a material four-vector, and not a single rank-two algebra element. The framework cannot hold it as a single element.

What the framework can do is hold its **bivector structure index by index**. For each antisymmetric pair $(\mu,\nu)$ on the base, the second pair $(\rho,\sigma)$ is antisymmetric and can be contracted with the basis to give an element of the Lie subspace,

$$
\tilde C_{\mu\nu} = \tfrac{1}{2}\sum_{\rho,\sigma} \mathrm{Riem}_{\mu\nu\rho\sigma}\,\varepsilon_\rho^{\natural}\varepsilon_\sigma .
$$

The scalar part of $\varepsilon_\rho^{\natural}\varepsilon_\sigma$ is the symmetric pairing $\langle\varepsilon_\rho,\varepsilon_\sigma\rangle_{\natural}$, the material interval's coefficient, so the antisymmetrized sum has no scalar part: each $\tilde C_{\mu\nu}$ is a **complex pure vector**, hence an element of the six-dimensional bivector subspace that the parent article identifies with $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$. The gravitational field strength is thus a **Lie-algebra-valued two-form** on the manifold, and every value it takes sits inside $\mathbb{B}$. This is the exact structural analogue of the electromagnetic field strength: the gauge article records that the electromagnetic $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$ is a single bivector, the curvature of an abelian connection, while the gravitational $\tilde C_{\mu\nu}$ is a bivector-valued two-form, the curvature of a connection valued in the non-abelian Lorentz Lie algebra. The identification of $\tilde C_{\mu\nu}$ with the curvature of the torsion-free spin connection is the standard tetrad identification, and the parent article records that metric compatibility and the vanishing of torsion are conditions the algebra does not select. The algebra supplies the home for each bivector value; it does not supply the object, because the object is built from $h$, which is not in the algebra.

The propagating, gauge-invariant content of the curvature is its **Weyl part**, the ten-component tensor obtained from $\mathrm{Riem}_{\mu\nu\rho\sigma}$ by removing the Ricci and scalar traces. In vacuum the two coincide, because the Ricci part vanishes, and the propagating degrees of freedom are in the Weyl tensor. Its encoding in the biquaternion framework — through the self-dual and anti-self-dual bivectors, or through the five complex Newman–Penrose scalars $\tilde{Ξ}^{\mathrm{sp}}_0, \dots, \tilde{Ξ}^{\mathrm{sp}}_4$ — is a separate problem, and it is not attempted here; it is recorded among the open questions.

## The Field Equation and the Trace-Reversal Step

The field equation is where the framework's d'Alembertian enters directly, and where the trace-reversal has a clean biquaternionic image. Both are worth displaying.

### The Trace-Reversal as a Frame Shift

Let $h = -h_{00}+h_{11}+h_{22}+h_{33}$ be the trace of the metric perturbation. From the frame representation, the trace is itself a biquaternionic pairing,

$$
h = 2\sum_\nu\langle\hat\varepsilon_\nu, \delta\tilde{E}_\nu\rangle_{\natural} = 2\sum_\nu\mathrm{Sc}\!\left(\hat\varepsilon_\nu^{\natural}\,\delta\tilde{E}_\nu\right).
$$

Define the **trace-reversed frame perturbation**

$$
\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac{1}{4}h\,\varepsilon_\mu .
$$

Then the metric perturbation it carries is the trace-reversed one,

$$
\boxed{\;\langle\varepsilon_\mu, \bar{\delta\tilde{E}}_\nu\rangle_{\natural} + \langle\bar{\delta\tilde{E}}_\mu, \varepsilon_\nu\rangle_{\natural}
= h_{\mu\nu} - \tfrac{1}{2}h\,\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural} = \bar{h}_{\mu\nu}\;},
$$

because $\langle\varepsilon_\mu, \tfrac{1}{4}h\,\varepsilon_\nu\rangle_{\natural} + \langle\tfrac{1}{4}h\,\varepsilon_\mu, \varepsilon_\nu\rangle_{\natural} = \tfrac{1}{2}h\,\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural}$, which is $+\tfrac{1}{2}h$ when both indices are space indices, $-\tfrac{1}{2}h$ when both are the time index, and zero otherwise, the minus being the square of the $i$ in $\varepsilon_0=ie_t$. The trace-reversal is therefore not an operation that takes the graviton out of the framework: it is a shift of each $\delta\tilde{E}_\mu$ by a multiple of the corresponding basis vector $\varepsilon_\mu$, with the multiple fixed by the biquaternionic trace. The identity was checked on randomly generated $h$ with the two sides agreeing exactly, and it reproduces $\bar{h} = -h$ as it must. The sign is the natural place for an error, so the $\bar{h} = -h$ contraction was checked independently on a random case.

### The Wave Equation

The biquaternionic d'Alembertian $\Box$ is a real operator built from the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ and the partial derivatives, so it commutes with the constant basis vectors $\varepsilon_\mu$ and acts componentwise on biquaternion-valued fields. Applying it to the trace-reversed frame perturbation and using the frame representation of $\bar{h}_{\mu\nu}$,

$$
\Box\bar{h}_{\mu\nu} = \langle\varepsilon_\mu, \Box\bar{\delta\tilde{E}}_\nu\rangle_{\natural} + \langle\Box\bar{\delta\tilde{E}}_\mu, \varepsilon_\nu\rangle_{\natural} .
$$

Consequently $\Box\bar{h}_{\mu\nu} = 0$ holds if and only if $\Box\bar{\delta\tilde{E}}_\mu$ lies in the local-Lorentz kernel of the map to $h$: a frame perturbation whose $\Box$ is a pure local Lorentz transformation produces no metric perturbation. If the local Lorentz freedom is fixed — for instance by demanding that $\delta\tilde{E}_\mu$ and $\varepsilon_\mu$ be related by coefficients symmetric in their two indices, as in the surjectivity construction above — then the wave equation takes the direct form

$$
\boxed{\;\Box\,\bar{\delta\tilde{E}}_\mu = 0\;}.
$$

The slicing condition is linear with constant coefficients, so $\Box$ preserves it, and on that slice the map to $h$ is injective.

The same structure appears in the electromagnetic analogue, with the roles assigned carefully. There the potential obeys $\Box\tilde{A} = -\mu\tilde{J}$, the field strength $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$ is gauge invariant, and the Lorenz condition $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A}) = 0$ is preserved exactly by the gauge functions with $\Box\Gamma = 0$, because $S \mapsto S - \Box\Gamma$. The correspondence is then $\tilde{A} \leftrightarrow \delta\tilde{E}_\mu$, $\tilde{F} \leftrightarrow \mathrm{Riem}_{\mu\nu\rho\sigma}$, $S \leftrightarrow$ the harmonic divergence, and $\Gamma \leftrightarrow \zeta$. The local Lorentz freedom is the one piece with no counterpart in the abelian case: it is the kernel of the map from the frame to the metric, a redundancy of the carrier and not of the potential. With a source, the linearized Einstein equation $\Box\bar{h}_{\mu\nu} = -\tfrac{16\pi G}{c^4}T_{\mu\nu}$ is transcribed componentwise; its right-hand side, the energy–momentum tensor, is the symmetric rank-two object whose biquaternion representation is studied in *Exercise: The Electromagnetic Energy–Momentum Tensor*, where it is built as a bigeneral quaternionic bilinear because no single biquaternion can carry it. The gravitational source belongs to the same class, and the same obstruction applies to it.

**What is not derived.** The operator $\Box$ is inherited; the equation $\Box\bar{h}_{\mu\nu} = 0$ is the standard linearized vacuum equation, transcribed. The framework supplies no action whose variation would yield it, and no principle selecting the frame. The parent article's conclusion is unchanged at linear order: the kinematical fibre is present, the dynamics is absent. The wave equation is written correctly in the framework's notation, and that is all that is claimed.

## The Plane Wave and the Two Polarizations

The plane-wave case is the sharpest check that the transcription is faithful, and it is where the gauge-invariant and gauge-dependent parts separate cleanly. Take a transverse-traceless perturbation propagating in the $z$ direction,

$$
h_{11} = -h_{22} = A\cos\!\left(\omega\left(\tfrac{z}{c} - r'_t\right)\right), \qquad h_{0\mu}=0, \qquad h_{3\mu}=0,
$$

with the other components zero. The wave vector is null, $-k_0^2+k_1^2+k_2^2+k_3^2 = 0$, and the amplitude is transverse, $-k_0A_{0\nu}+k_1A_{1\nu}+k_2A_{2\nu}+k_3A_{3\nu} = 0$, and traceless, $-A_{00}+A_{11}+A_{22}+A_{33} = 0$. A direct computation gives

$$
\mathrm{Ric}_{\mu\nu} = 0, \qquad \mathrm{Riem}_{\mu\nu\rho\sigma} \ne 0,
$$

with, for example, $\mathrm{Riem}_{0101} = -\mathrm{Riem}_{0202} \ne 0$ while $\mathrm{Riem}_{0303} = 0$. The curvature is nonzero, so the wave is not pure gauge; the Ricci tensor vanishes, so it solves the vacuum equation. This was checked numerically for both a plus-polarization amplitude ($A_{11} = -A_{22}$) and the corresponding cross-polarization amplitude ($A_{12} = A_{21}$), with the same qualitative result in each case: the Ricci tensor vanishes and the Riemann tensor does not.

The two independent amplitudes are the two polarizations of the linear theory. A displacement of the frame along its own basis, $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu + c\,\varepsilon_\mu$, shifts $h_{\mu\nu}$ by $2c\,\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural}$ and by nothing else; the part of $h$ along $\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural}$ is thus exactly the part the frame carries along $\varepsilon_\mu$. A transverse-traceless wave has $h = 0$, so it has no such part at all, and its content sits entirely in the components of $\delta\tilde{E}_\mu$ orthogonal to $\varepsilon_\mu$ in this sense. By the result of *The Graviton Is Not a Material Biquaternion*, the trace is the only thing the natural single-biquaternion packaging can see — that packaging is $\tilde R_\psi = h\,e_t$, which vanishes identically for this wave. So the two propagating degrees of freedom of the graviton are precisely what a single biquaternion cannot represent. This is the clearest statement of the article's structural finding: the framework carries the graviton as a frame perturbation, and the algebra element into which one might try to compress it retains only the trace, which a gravitational wave does not have.

The detailed phenomenology of these waves — their generation, their interaction with matter, and the observational constraints on their polarizations — is not developed here. The linearized kinematics and the gauge structure are the subject of this article; the wave theory is a separate development.

## What the Algebra Supplies and What It Does Not

The boundary can be drawn as a list, in the manner of the parent article.

**Supplied by the algebra, and recomputed here.** The material basis $\varepsilon_\mu$ together with the natural form $\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural}$; the representation of a metric perturbation by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through $h_{\mu\nu} = \langle\varepsilon_\mu, \delta\tilde{E}_\nu\rangle_{\natural} + \langle\delta\tilde{E}_\mu, \varepsilon_\nu\rangle_{\natural}$, with every symmetric $h$ realized; the decomposition $16 = 10 + 6$ with the six-dimensional local Lorentz kernel, and the exact invariance of $h$ under the kernel; the gauge transformation $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}$ with $\tilde Q_{\mathrm d} \in \mathbb{M}_-$, reproducing $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu$; the trace-reversal as the frame shift $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac{1}{4}h\,\varepsilon_\mu$ with $h = 2\sum_\nu\langle\hat\varepsilon_\nu,\delta\tilde{E}_\nu\rangle_{\natural}$; the invariance of the linearized Riemann tensor under the gauge transformation; the bivector-valued two-form packaging of the curvature; and the reduction of the vacuum equation to $\Box\bar{h}_{\mu\nu} = 0$, hence to $\Box\bar{\delta\tilde{E}}_\mu = 0$ once the local Lorentz freedom is fixed.

**Interpretation, not derivation.** Reading $\delta\tilde{E}_\mu$ as a tetrad and $h_{\mu\nu}$ as the metric it carries is a geometric interpretation of the algebraic construction, exactly as in the parent article. The algebra is consistent with the interpretation, and the computations above make the consistency precise, but the algebra does not force the bundle-theoretic or geometric picture.

**Not supplied, and left as gaps.** An action principle and a field equation for the frame, and hence any derivation of the linearized Einstein equation. A representation of diffeomorphism invariance, which is the origin of the gravitational gauge freedom written above. A selection principle for the connection, and with it the identification of the bivector-valued curvature $\tilde C_{\mu\nu}$ as the curvature of any particular connection. (The external variant above fixes the coefficients $\Gamma_{\mu\nu\rho}$ from the basis once its $\omega_\mu$ is given, which is a partial determination; it leaves $\omega_\mu$ itself free, so this gap stands as stated.) A derivation of the coupling to matter, and of the constant $8\pi G/c^4$. A single-biquaternion or material-sector representative of the graviton; the natural one collapses to the trace. And, as always in this framework, empirical content: nothing here predicts a deviation from standard linearized gravity.

## Open Questions

1. **A biquaternion action whose linearization is linearized gravity.** Is there an action functional of $\tilde{E}_\mu$ and $\vec\Gamma_\mu$, built from the algebra's own operations, whose linearized variation gives the linearized Einstein equation? The parent article states that none is known; the question is whether the linearized problem is any easier, and in particular whether the trace-reversal identity of this article points toward a natural quadratic action.

2. **The non-abelian curvature and the gauge article's gap.** The linearized gravitational field strength is an $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$-Lie-algebra-valued two-form. The gauge article records that the framework supplies non-commutativity but not a compactness or reality condition selecting a gauge algebra. Does the local Lorentz algebra, which is non-compact and selected by the metric, meet that gap, or is it a different structure that the electromagnetic case cannot use?

3. **A biquaternionic harmonic condition.** The harmonic condition $-\partial/\partial x_0\bar{h}_{0\nu}+\partial/\partial x_1\bar{h}_{1\nu}+\partial/\partial x_2\bar{h}_{2\nu}+\partial/\partial x_3\bar{h}_{3\nu} = 0$ is four conditions on the frame. Is there a distinguished biquaternionic differential operator — a divergence on $\mathbb{M}_-$-valued one-forms — that produces it naturally, in the way that $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A}) = 0$ produces the Lorenz condition for the electromagnetic potential?

4. **The Weyl tensor in the algebra.** The propagating content of linearized gravity is the Weyl tensor, and its natural biquaternionic encoding is through the self-dual and anti-self-dual bivectors. Can the five Newman–Penrose scalars be written as components of biquaternion objects, and does the algebra's decomposition into $\mathbb{M}_+$ and $\mathbb{M}_-$ organise them?

5. **The relation to the parent's local-scale route.** The parent article shows that the local scale factor $c = 1/\sqrt{\epsilon\mu}$, read as a metric, is a class in which Ricci-flatness forces flatness, so it carries no gravitational waves. Does linearizing that route reproduce the statement that its linearized Riemann tensor vanishes identically, and does the frame route's nonvanishing Riemann tensor make the two routes inequivalent already at linear order?

6. **The informational sector.** The natural Hermitian packaging of the metric perturbation is its trace, an element of $\mathbb{M}_+$. Is that a coincidence of the packaging, or does the two-sector structure constrain which perturbations are representable? The trace is not propagating in vacuum, which makes the coincidence worth understanding rather than dismissing.

7. **Empirical content.** As everywhere in the framework, the open question is whether any of this yields a prediction distinguishing it from standard linearized gravity. The transcription developed here does not.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are the frame cells of the body. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}^{\mathrm{sp}}=a\tilde{Ξ}^{\mathrm{sp}}$ and $R_b\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. Every $i$ below is the central scalar, with $i^2=-1$, so each cell carries one factor of $i$ and each product of two cells carries $i^2=-1$.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The time cell simplifies at once, because $L_{e_t}^{\mathrm{pau}}$ is the identity: $\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$. The fifth gamma is not a fifth frame vector but their product,

$$
\gamma_5:=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=-iR_{\vec e_z}^{\mathrm{pau}}.
$$

In the axis-free display:

$$
\gamma_5:=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}.
$$

The four cells in the product carry $i^4=1$, so the single $i$ of the definition survives; the cell that results is $-iR_{\vec e_z}^{\mathrm{pau}}$, the chirality cell.

$\gamma_5$ is the reference-frame cell of the chirality operator. The central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, with $\tilde{Ζ}_{\mathrm{ad}}$ the central root of $-e_t$, is the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$. It is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and the real left–right products $L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$, without the central $i$, span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the body and the companions cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$ and in the frame of this section — not the body's full metric —

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

The sign change is the one convention change in the translation: the time cell has $\gamma_0^2=+I_4$, while the material time basis vector has $\langle\varepsilon_0,\varepsilon_0\rangle_{\natural}=-1$.

The contraction sums depend only on the squares of the cells, not on the representation, and they are fixed once the summed index is raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$:

$$
\sum_\mu\gamma^\mu\gamma_\mu=-4I_4,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha,
$$

$$
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha.
$$

For a product of $n$ distinct generators they are one rule, $\sum_\mu\gamma^\mu A\gamma_\mu=(-1)^{n+1}(4-2n)A$. With every index low only the first keeps a closed form, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$; the rest are index-dependent and are computed, not transcribed: $\sum_\mu\gamma_\mu\gamma_0\gamma_\mu=+4\gamma_0$ and $\sum_\mu\gamma_\mu\gamma_k\gamma_\mu=0$ for $k=1,2,3$.

**The two Dirac equations.** Two equations carry the name in this corpus: the one-sided chirality pair and Kravchenko's two-sided equation. They share the $\gamma$ frame and are related by the dictionary, but they are not the same equation and must not be read as one. The one-sided pair, which is the flat form of the equation meant in the body above, is

$$
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=m\tilde{Ξ}^{\mathrm{sp}}_L,\qquad
\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m\tilde{Ξ}^{\mathrm{sp}}_R,
$$

with both gradients acting from the left and the mass term pairing the two chiral halves off-diagonally. Kravchenko's two-sided equation, for a biquaternion field $F$ (in the source's units $c=1$), is

$$
\bigl(i\partial/\partial r'_t+D_3\bigr)F-m\,i\,\overline{F}\,\vec e_z=0,
\qquad
D_3=\sum_k\vec e_k\frac{\partial}{\partial R_k},
$$

with the spatial gradient acting from the left, the mass from the right through $\vec e_z$, and the mass term carrying the algebra's complex conjugation $\overline{\cdot}$. The first acts on a pair of chirality halves with a scalar mass; the second acts on one biquaternion with a directed, antilinear mass. They share the frame, not the operator.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Linearized gravity in biquaternionic form is the linearization of the parent article's frame route. The metric perturbation is carried by a frame perturbation $\delta\tilde{E}_\mu \in \mathbb{M}_-$ through $h_{\mu\nu} = \langle\varepsilon_\mu,\delta\tilde{E}_\nu\rangle_{\natural} + \langle\delta\tilde{E}_\mu,\varepsilon_\nu\rangle_{\natural}$, and every symmetric perturbation arises this way. The sixteen frame components split as $16 = 10 + 6$, the kernel being the infinitesimal local Lorentz transformations, which leave the metric perturbation exactly invariant.

The graviton is not a material biquaternion. It is not an element of $\mathbb{M}_-$, it is not a single element of $\mathbb{B}$ — eight real dimensions cannot hold ten components — and the natural single-biquaternion packaging $\sum h_{\mu\nu}\varepsilon_\mu\varepsilon_\nu^{\natural}$ collapses to the trace $h\,e_t$, losing the traceless part that carries the two polarizations. The carrier is the frame perturbation, an $\mathbb{M}_-$-valued one-form: the graviton's potential lives in the same sector as the electromagnetic potential, but as a one-form of material four-vectors rather than as one material four-vector.

The gauge freedom is written as $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}$ with $\tilde Q_{\mathrm d} \in \mathbb{M}_-$, which reproduces $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu$. Its shape is the electromagnetic one — the exterior derivative of a gauge parameter — with a material four-vector replacing the central scalar; but its origin is a diffeomorphism, for which the algebra has no representation. The shape is transcribed; the origin is not supplied.

The field strength is the linearized Riemann tensor, gauge invariant under the transformation above, and further from the algebra than $h$: a rank-four tensor with twenty components, held by the framework only as a bivector-valued two-form whose values lie in the Lorentz Lie algebra. The trace-reversal has a clean biquaternionic image, the frame shift $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac14 h\,\varepsilon_\mu$ with $h = 2\sum_\nu\langle\hat\varepsilon_\nu,\delta\tilde{E}_\nu\rangle_{\natural}$. In harmonic gauge, with the local Lorentz freedom fixed, the vacuum equation is $\Box\bar{\delta\tilde{E}}_\mu = 0$, and a transverse-traceless plane wave satisfies it with nonvanishing curvature — the standard two-polarization result, carried by the traceless part that a single biquaternion cannot hold.

What the algebra supplies is the kinematic fibre of linearized gravity and the form of its gauge structure. What it does not supply is the dynamics: no action, no derived field equation, no diffeomorphism invariance, no coupling to matter, no empirical content. The title names a form, and that is what has been written.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\varepsilon_\mu = (ie_t, \vec e_x, \vec e_y, \vec e_z)$ | Material basis of $\mathbb{M}_-$ |
| $\langle\varepsilon_\mu,\varepsilon_\nu\rangle_{\natural}$ | The natural form on the material basis: $+1$ on the three space rows and $-1$ on the time row, the minus being the square of the $i$ in $\varepsilon_0=ie_t$ |
| $\tilde Q^{\natural}$, $\bar{\tilde Q}$, $\tilde Q^{*}$ | Quaternion conjugation, complex conjugation, and Hermitian conjugation $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$ |
| $\hat\varepsilon_\nu$ | Dual material basis, $\langle\hat\varepsilon_\lambda,\varepsilon_\rho\rangle_{\natural}=\delta_{\lambda\rho}$ |
| $\varepsilon=(1,-1,-1,-1)$ | The plain weight of the frame, $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$; used in *The Fermionic Coupling at First Order* and *The Legacy Pauli Gamma Formulation* |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$ | General quaternionic bilinear form on $\mathbb{M}_-$, the interval |
| $x_\mu = (c r'_{t},x,y,z)$, $\partial/\partial x_\mu$ | Real coordinates and their derivatives; the framework's imaginary time is $i x_0$ |
| $\partial/\partial R_t = -i\partial/\partial x_0$ | Relation of the framework's imaginary time derivative to $\partial/\partial x_0$ |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \sum_\mu\partial^2/\partial R_\mu^2$ | Biquaternionic gradient, conjugate, d'Alembertian |
| $g_{\mu\nu}\,\mathrm{d}r_x^\mu\mathrm{d}r_x^\nu = -c^2\mathrm{d}r'_t^2+\mathrm{d}\vec r^2+h_{\mu\nu}\,\mathrm{d}r_x^\mu\mathrm{d}r_x^\nu$ | Linearized metric: the flat interval plus the perturbation $h_{\mu\nu}$ |
| $\tilde{E}_\mu = \varepsilon_\mu + \delta\tilde{E}_\mu$ | Frame field and frame perturbation, $\delta\tilde{E}_\mu \in \mathbb{M}_-$ |
| $h_{\mu\nu} = \langle\varepsilon_\mu,\delta\tilde{E}_\nu\rangle_{\natural} + \langle\delta\tilde{E}_\mu,\varepsilon_\nu\rangle_{\natural}$ | Metric perturbation carried by the frame perturbation |
| $h = -h_{00}+h_{11}+h_{22}+h_{33} = 2\sum_\nu\langle\hat\varepsilon_\nu,\delta\tilde{E}_\nu\rangle_{\natural}$ | Trace of the metric perturbation |
| $\bar{h}_{00}=h_{00}+\tfrac12h$, $\bar{h}_{kl}=h_{kl}-\tfrac12h\,\delta_{kl}$, $\bar{h} = -h$ | Trace-reversed perturbation; here the overbar marks trace reversal, not complex conjugation |
| $\bar{\delta\tilde{E}}_\mu = \delta\tilde{E}_\mu - \tfrac14 h\,\varepsilon_\mu$ | Trace-reversed frame perturbation |
| $\vec G \in \mathrm{span}_{\mathbb{R}}\{\vec e_k, i\vec e_k\}$ | Infinitesimal local Lorentz generator (complex pure vector) |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | The generator cell of the coordinate $x_\mu$, in the axis-free display of *Matrix Representations Conventions*; it is a cell, that is, an operator |
| $\tilde Q_{\mathrm d} \in \mathbb{M}_-$ | Gauge four-vector, $\delta\tilde{E}_\mu \mapsto \delta\tilde{E}_\mu - \partial/\partial x_\mu\,\tilde Q_{\mathrm d}$ |
| $h_{\mu\nu} \mapsto h_{\mu\nu} - \partial/\partial x_\mu\,\zeta_\nu - \partial/\partial x_\nu\,\zeta_\mu$, $\zeta_\nu = \langle\tilde Q_{\mathrm d},\varepsilon_\nu\rangle_{\natural}$ | Linearized gauge transformation |
| $\mathrm{Riem}_{\mu\nu\rho\sigma}$ | Linearized Riemann tensor (gauge-invariant field strength) |
| $\mathrm{Ric}_{\mu\nu}$, $G_{\mu\nu}$ | Linearized Ricci tensor and Einstein tensor |
| $\tilde C_{\mu\nu} = \tfrac12\sum_{\rho\sigma}\mathrm{Riem}_{\mu\nu\rho\sigma}\varepsilon_\rho^{\natural}\varepsilon_\sigma$ | Curvature as a bivector-valued two-form |
| $-\partial/\partial x_0\bar{h}_{0\nu}+\partial/\partial x_1\bar{h}_{1\nu}+\partial/\partial x_2\bar{h}_{2\nu}+\partial/\partial x_3\bar{h}_{3\nu} = 0$ | Harmonic gauge |
| $\Box\bar{h}_{\mu\nu} = -\tfrac{16\pi G}{c^4}T_{\mu\nu}$ | Linearized Einstein equation |
| $A_{\mu\nu}$, plus/cross | Plane-wave amplitude; the two polarizations |
| $\mathrm{Tr}(\tilde{R}_{\psi,1}\tilde{R}_{\psi,2}^{*})=2\,\mathrm{Sc}(\tilde{R}_{\psi,1}\tilde{R}_{\psi,2}^{*})$ | Trace reading of the Hermitian form on the informational sector |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Companion articles: [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html); [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html); [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html).
- Charles W. Misner, Kip S. Thorne, and John A. Wheeler, *Gravitation* (Freeman, 1973), for the linearized theory, the transverse-traceless gauge, and the two polarizations of a gravitational wave.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the linearized Einstein equation, the trace-reversal, and the harmonic gauge.
- Sean M. Carroll, *Spacetime and Geometry: An Introduction to General Relativity* (Cambridge, 2019), for a compact treatment of linearized gravity and its gauge structure.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spin-coefficient and bivector formulation of the curvature on which the Weyl-tensor encoding rests.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic treatment of gravity in the same rotor language used here.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra formulation of the tetrad and the curvature bivector.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the bivector structure of two-forms.
- V. V. Kravchenko, *Applied Quaternionic Analysis*, Research and Exposition in Mathematics 28 (Heldermann, 2003), for the two-sided quaternionic Dirac equation distinguished in *The Legacy Pauli Gamma Formulation*.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external caution recorded in *The Fermionic Coupling at First Order*: that the standard vierbein coupling of a Dirac fermion to gravity is not unique — the varied and substituted equations differ by a term linear in the spin connection — so the ambiguity is first order in the frame perturbation and a linearized fermion–gravity system must state which form it uses. Cited as an external claim; the construction is recorded in *Curved Spacetime and the Biquaternion Framework*.
- J. Fredsted, "Spinor fields without Lorentz frames in curved spacetime using complexified quaternions," arXiv:0811.1357v4 [math-ph] (2009), for the external variant recorded in *An External Variant: Frame Fields That Carry Their Own Connection*: $\mathbb{M}_-$-valued frame fields $s_\mu$ in place of a vierbein, with the connection derived from the algebraic vielbein postulate $D_\rho s_\nu = 0$ rather than inserted. Cited as an external construction in its own conventions, not adopted here.
