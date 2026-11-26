# __Gravitational Waves in Biquaternionic Form__

## Introduction

Gravitational radiation is the propagating content of the linearized theory of general relativity. The parent article, *Linearized Gravity in Biquaternionic Form*, established the kinematics of that theory inside the biquaternion framework: the metric perturbation is carried by a frame perturbation $\delta\tilde{E}_{\Phi,\imath} \in \mathbb{B}_{\Phi}$ through $h_{\imath\jmath} = \langle\varepsilon_{\imath},\delta\tilde{E}_{\Phi,\jmath}\rangle_{\natural} + \langle\delta\tilde{E}_{\Phi,\imath},\varepsilon_{\jmath}\rangle_{\natural}$, with every symmetric perturbation realized; the sixteen frame components split as $16 = 10 + 6$, the six-dimensional kernel being the infinitesimal local Lorentz transformations; the linearized diffeomorphism is written $\delta\tilde{E}_{\Phi,\imath} \mapsto \delta\tilde{E}_{\Phi,\imath} - \partial/\partial x_{\imath}\tilde Q_{\Phi,\mathrm d}$ with $\tilde Q_{\Phi,\mathrm d} \in \mathbb{B}_{\Phi}$, reproducing $h_{\imath\jmath} \mapsto h_{\imath\jmath} - \partial/\partial x_{\imath}\zeta_{\jmath} - \partial/\partial x_{\jmath}\zeta_{\imath}$; the trace-reversal is the frame shift $\bar{\delta\tilde{E}_{\Phi}}_{\imath} = \delta\tilde{E}_{\Phi,\imath} - \tfrac14 h\,\varepsilon_{\imath}$ with $h = 2\langle\varepsilon_{\jmath},\delta\tilde{E}_{\Phi,\jmath}\rangle_{\natural}$; and, in harmonic fixing condition, the vacuum equation is $\Box_\Phi\bar{h}_{\imath\jmath} = 0$, hence $\Box_\Phi\bar{\delta\tilde{E}_{\Phi}}_{\imath} = 0$ once the local Lorentz freedom is fixed. The parent displayed a transverse-traceless plane wave with vanishing Ricci tensor and nonvanishing Riemann tensor, and then stopped, deferring explicitly "the detailed phenomenology of these waves — their generation, their interaction with matter, and the observational constraints on their polarizations".

This article takes up that deferral, and only as far as the linearized approximation reaches. Its subject is the standard radiation theory: the trace-reversed perturbation and its wave equation, the harmonic (Lorenz) gauge and the residual redundancy that survives it, the counting of physical degrees of freedom from ten to two, the two transverse-traceless polarizations, and the quadrupole formula for the radiated power. Each of these is first written in its standard form, then asked what the biquaternion framework has to say about it.

The findings are worth separating at the outset, because one of them is negative and is easy to mistake for a defect of the exposition.

- **Established, and recomputed below.** The harmonic condition $-\partial/\partial x_0\bar{h}_{0\jmath}+\partial/\partial x_1\bar{h}_{1\jmath}+\partial/\partial x_2\bar{h}_{2\jmath}+\partial/\partial x_3\bar{h}_{3\jmath} = 0$ does not exhaust the redundancy: it is preserved by exactly those residual transformations with $\Box_\Phi\zeta_{\jmath} = 0$. Counting the physical content therefore requires the residual freedom, and with it the count $10 \to 6 \to 2$ is justified rather than asserted: the ten components of $h_{\imath\jmath}$ reduce to six under the four harmonic conditions, and the six-dimensional space is the direct sum of the two-dimensional transverse-traceless space and the four-dimensional image of the residual redundancy. The two polarizations are transverse-traceless, and both the transversality and the tracelessness are verified on an explicit plane-wave ansatz, together with $\mathrm{Ric}_{\imath\jmath} = 0$ and $\mathrm{Riem}_{\imath\jmath\rho\sigma} \ne 0$ for each of the plus and cross amplitudes. The quadrupole formula $P = \frac{G}{5c^5}\langle \,d^3\mathcal{Q}_{ij}/d{r'_{t}}^3 d^3\mathcal{Q}_{ij}/d{r'_{t}}^3\rangle$ is verified by matching it, on the equal-mass circular binary, to the standard result $\frac{32}{5}\frac{G^4}{c^5}\frac{(m_1m_2)^2(m_1+m_2)}{d^5}$; the radiation is quadrupole because the monopole and dipole moments are conserved, and the mass dipole's second derivative vanishes by momentum conservation.
- **The framework's contribution, and its limit.** The algebra supplies the wave operator $\Box_\Phi$ and the shape of the local transformation, both inherited from the parent, and it supplies the residual redundancy as the condition $\Box_\Phi\tilde Q_{\Phi,\mathrm d} = 0$ on a material four-vector. It supplies **no natural handle on the polarization count**: the step $6 \to 2$ is a dynamical statement about which of the harmonic-gauge components propagate, and the algebra does not generate it. The physical polarization amplitudes are carried by a symmetric traceless rank-two object, and the algebra's natural single-biquaternion packaging of that object collapses to its trace, which vanishes — so the two polarizations are precisely what a single biquaternion cannot hold. The quadrupole moment is the same kind of object, and the same collapse applies to it; the source $T_{\imath\jmath}$ belongs to the same class. Consequently the quadrupole formula is transcribed into the framework's notation, not derived from it, and the prefactor $G/5c^5$ is not fixed by the algebra.
- **What is not claimed.** Linearized general relativity is not derived from the biquaternion algebra. No action, no field equation, and no representation of diffeomorphism invariance is supplied here; these are the parent's gaps, and nothing in the radiation theory closes them. The framework predicts no deviation from standard gravitational-wave physics.

## The Trace-Reversed Perturbation and the Wave Equation

This section fixes the target. It is standard linearized gravity, written in the coordinate convention just fixed, and every formula displayed here was checked by direct computation.

The framework's conventions are used here and are not restated. The material basis $\varepsilon_{\imath}$ of $\mathbb{B}_{\Phi}$ and the real coordinates $x_{\imath}=(r'_{t}, r_x, r_y, r_z)$ of the material frame are those of *Frame and Metric Conventions*, and the biquaternionic d'Alembertian $\Box_\Phi$ is that of *Operator and Calculus Conventions*. There is one metric, the unit metric $\delta_{\imath\jmath}=(1,1,1,1)$ on the four $Q_{\imath}$; the material interval is that form read on $Q_t=i q'_t$, $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$, and its one minus is the square of the $i$. The linearized metric is the flat interval plus the perturbation $h_{\imath\jmath}$, with $|h_{\imath\jmath}| \ll 1$, and every contraction below is written out in the real coordinates, where the minus on the time row is that one minus. A product $\nu_{\Phi,k}x_{\imath}$ below is the invariant contraction $-\nu_t^{\prime}x_0+\nu_{\Phi x}x_1+\nu_{\Phi y}x_2+\nu_{\Phi z}x_3$, not a sum of like components. The **trace-reversed** perturbation is

$$
\bar{h}_{00} = h_{00} + \tfrac{1}{2}h, \qquad \bar{h}_{0k} = h_{0k}, \qquad \bar{h}_{\imath l} = h_{\imath l} - \tfrac{1}{2}h\,\delta_{\imath l}, \qquad \bar{h} = -\bar{h}_{00}+\bar{h}_{11}+\bar{h}_{22}+\bar{h}_{33} = -h,
$$

with $h = -h_{00}+h_{11}+h_{22}+h_{33}$, so that the operation is an involution up to sign, $h_{00} = \bar{h}_{00} + \tfrac{1}{2}\bar{h}$, $h_{0k}=\bar{h}_{0k}$ and $h_{\imath l} = \bar{h}_{\imath l} - \tfrac{1}{2}\bar{h}\,\delta_{\imath l}$. In these variables the linearized Einstein tensor is

$$
\begin{aligned}
G_{00} = \tfrac{1}{2}\Bigl(&\partial/\partial x_0\,\bar{D}_0+\partial/\partial x_0\,\bar{D}_0-\Box_\Phi\bar{h}_{00}+\bar{S}\Bigr),\\[2pt]
G_{0k} = \tfrac{1}{2}\Bigl(&\partial/\partial x_0\,\bar{D}_{\imath}+\partial/\partial x_{\imath}\,\bar{D}_0-\Box_\Phi\bar{h}_{0k}\Bigr),\\[2pt]
G_{\imath l} = \tfrac{1}{2}\Bigl(&\partial/\partial x_{\imath}\,\bar{D}_l+\partial/\partial x_l\,\bar{D}_{\imath}-\Box_\Phi\bar{h}_{\imath l}-\delta_{\imath l}\bar{S}\Bigr),
\end{aligned}
$$

with $\bar{D}_{\jmath} = -\partial/\partial x_0\bar{h}_{0\jmath}+\sum_{\imath\in\{x,y,z\}}\partial/\partial x_{\imath}\bar{h}_{k\jmath}$ and $\bar{S} = \partial^2/\partial x_0^2\bar{h}_{00}-\sum_{\imath\in\{x,y,z\}}(\partial^2/\partial x_0\partial x_{\imath}\bar{h}_{k 0}+\partial^2/\partial x_{\imath}\partial x_0\bar{h}_{0k})+\sum_{\imath,l}\partial^2/\partial x_{\imath}\partial x_l\bar{h}_{l\imath}$; the minus on the time row of each contraction is the one minus of the interval.

The **harmonic fixing condition** condition is

$$
-\partial/\partial x_0\bar{h}_{0\jmath}+\partial/\partial x_1\bar{h}_{1\jmath}+\partial/\partial x_2\bar{h}_{2\jmath}+\partial/\partial x_3\bar{h}_{3\jmath} = 0 .
$$

It is four conditions on the ten components of $\bar{h}_{\imath\jmath}$ and it can always be imposed. In it $G_{\imath\jmath} = -\tfrac{1}{2}\Box_\Phi\bar{h}_{\imath\jmath}$, so the linearized Einstein equation $G_{\imath\jmath} = \tfrac{8\pi G}{c^4}T_{\imath\jmath}$ becomes

$$
\Box_\Phi\bar{h}_{\imath\jmath} = -\frac{16\pi G}{c^4}\,T_{\imath\jmath},
\qquad\text{and in vacuum}\qquad
\Box_\Phi\bar{h}_{\imath\jmath} = 0 .
$$

The parent article's frame route carries all of this. The trace-reversed frame perturbation is

$$
\bar{\delta\tilde{E}_{\Phi}}_{\imath} = \delta\tilde{E}_{\Phi,\imath} - \tfrac{1}{4}h\,\varepsilon_{\imath},
\qquad
h = 2\langle\varepsilon_{\jmath},\delta\tilde{E}_{\Phi,\jmath}\rangle_{\natural},
$$

and it carries $\bar{h}_{\imath\jmath}$ exactly; the biquaternionic d'Alembertian acts componentwise, so $\Box_\Phi\bar{h}_{\imath\jmath} = \langle\varepsilon_{\imath},\Box_\Phi\bar{\delta\tilde{E}_{\Phi}}_{\jmath}\rangle_{\natural} + \langle\Box_\Phi\bar{\delta\tilde{E}_{\Phi}}_{\imath},\varepsilon_{\jmath}\rangle_{\natural}$, and with the local Lorentz freedom fixed the vacuum equation becomes

$$
\Box_\Phi\,\bar{\delta\tilde{E}_{\Phi}}_{\imath} = 0 .
$$

The operator is inherited, not derived: the framework supplies no action whose variation would produce $\Box_\Phi\bar{h}_{\imath\jmath} = 0$. That is the parent's conclusion, and it is unchanged by anything in this article.

## The Harmonic Fixing Condition and Its Residual Redundancy

The harmonic condition is the gravitational analogue of the Lorenz condition of electromagnetism — it is also called the De Donder fixing condition, and, by the analogy, the Lorenz fixing condition of linearized gravity. The analogy is worth stating because the residual freedom is the same in both cases, and this is the first place where a naive count goes wrong.

Under a coordinate transformation $x_{\imath} \mapsto x_{\imath} + \zeta_{\imath}$ the metric perturbation changes by

$$
h_{\imath\jmath} \;\longmapsto\; h_{\imath\jmath} - \partial/\partial x_{\imath}\zeta_{\jmath} - \partial/\partial x_{\jmath}\zeta_{\imath},
$$

and the trace-reversed perturbation changes by

$$
\begin{aligned}
\bar{h}_{00} &\;\longmapsto\; \bar{h}_{00} - 2\partial/\partial x_0\zeta_0 - D,\\[2pt]
\bar{h}_{0k} &\;\longmapsto\; \bar{h}_{0k} - \partial/\partial x_0\zeta_{\imath} - \partial/\partial x_{\imath}\zeta_0,\\[2pt]
\bar{h}_{\imath l} &\;\longmapsto\; \bar{h}_{\imath l} - \partial/\partial x_{\imath}\zeta_l - \partial/\partial x_l\zeta_{\imath} + \delta_{\imath l}D,
\end{aligned}
$$

with $D = -\partial/\partial x_0\zeta_0+\partial/\partial x_1\zeta_1+\partial/\partial x_2\zeta_2+\partial/\partial x_3\zeta_3$.

A direct computation, carried out on a general smooth $\zeta_{\imath}$ and not merely on a plane wave, gives

$$
\bar{D}_{\jmath} \;\longmapsto\; \bar{D}_{\jmath}-\Box_\Phi\zeta_{\jmath} .
$$

The harmonic condition is therefore preserved by precisely those local transformations with

$$
\boxed{\;\Box_\Phi\zeta_{\jmath} = 0\,\;}.
$$

Four functions satisfy this, one for each coordinate direction, so the redundancy is **not** exhausted by the harmonic condition. It is a residual redundancy of the same kind that the Lorenz condition leaves in electromagnetism, where the condition is preserved by $\Box_\Phi\Gamma = 0$. A count that imposes harmonic fixing condition and then declares the remaining six components physical has used the redundancy twice in the wrong order: the six components include the four that the residual freedom still moves.

For a plane wave there is an instructive simplification. Writing $\zeta_{\jmath} = a_{\jmath} \exp\big(ik_{\Phi,k}x_{\imath}\big)$, the preservation condition is $\nu_{\Phi}^2a_{\jmath} = 0$, and for a lightlike wave vector $\nu_{\Phi}^2 = -\nu_t^{\prime\,2}+\nu_{\Phi x}^2+\nu_{\Phi y}^2+\nu_{\Phi z}^2 = 0$ it holds for every $a_{\jmath}$; every residual phase function is available for a plane wave. This is the case on which the count below is computed.

## Counting the Physical Degrees of Freedom

The count is $10 \to 6 \to 2$, and it must be justified at each arrow. The first arrow is a choice of representative; the second is the division by the residual redundancy just exhibited.

**Ten.** The symmetric tensor $h_{\imath\jmath}$ has $\tfrac{1}{2}\cdot4\cdot5 = 10$ independent components.

**Six.** The four phase functions $\zeta_{\imath}$ are used to impose the four harmonic conditions $\bar{D}_{\jmath} = 0$. The space of perturbations satisfying them is six-dimensional. This is a fixing the representative, not yet a reduction to physical content.

**Two.** The residual redundancy acts inside that six-dimensional space. Restricting the residual transformations with $\Box_\Phi\zeta_{\jmath} = 0$ to the harmonic-gauge plane wave, the map from the four parameters $a_{\jmath}$ to the change it induces in the six harmonic components has rank four, and its image is complementary to the transverse-traceless amplitudes. The companion verifies exactly this: on the six-dimensional space, the transverse-traceless subspace has dimension two, the residual-gauge image has dimension four, their direct sum has dimension six, and their intersection is trivial. The count is therefore

$$
\boxed{\;10 \;\xrightarrow[\text{4 harmonic conditions}]{}\; 6 \;\xrightarrow[\text{4 residual phase functions}]{}\; 2\;},
$$

with the last quotient exactly the transverse-traceless amplitudes.

Two independent checks confirm the final number.

*Transverse-traceless tensor count.* A symmetric spatial amplitude $A_{ij}$ ($i,j = 1,2,3$) has six independent components; transversality $\sum_i \nu_{i}A_{ij} = 0$ imposes three conditions; tracelessness $\sum_i A_{ii} = 0$ imposes one. Six minus three minus one is two.

*Little-group count.* A massless field of spin $s$ in four dimensions carries two helicities, $\pm s$. For the graviton $s = 2$, so the helicities are $\pm 2$, again two. This is the representation-theoretic reason the number is independent of the details of the fixing the representative, and it is the count the algebra does not reproduce; that is the subject of the section *The Wave Operator, the Redundancy, and the Counting in the Framework*.

Two cautions belong with the count. First, the intermediate values $10$ and $6$ are properties of the potential and of a gauge slice, not of the physics; only the final two, and the invariant curvature that carries them, are invariant. Second, the quotient by the residual redundancy is a local statement about the field at a point; it counts local degrees of freedom and says nothing about global or boundary data. Both cautions are standard, and both matter for the framework comparison below, where the gauge slice is available but the dynamics that selects the two propagating components is not.

## The Two Polarizations

A vacuum plane wave is

$$
h_{\imath\jmath} = A_{\imath\jmath}\cos(2\pi\nu_{\Phi,k}x_{\imath}), \qquad -4\pi^{2}\nu_t^{\prime\,2}+4\pi^{2}\nu_{\Phi x}^2+4\pi^{2}\nu_{\Phi y}^2+4\pi^{2}\nu_{\Phi z}^2 = 0,
$$

with a constant symmetric amplitude $A_{\imath\jmath}$. The residual redundancy of the previous section can be used to put it in **transverse-traceless** form, in which

$$
-2\pi\nu_t^{\prime}A_{0\jmath}+k_1A_{1\jmath}+k_2A_{2\jmath}+k_3A_{3\jmath} = 0 \qquad\text{and}\qquad -A_{00}+A_{11}+A_{22}+A_{33} = 0 ,
$$

and in which, in addition, the components with a timelike index vanish, $A_{t\imath} = 0$. For propagation in the $+z$ direction, $2\pi\nu_{\Phi,\imath} = (\omega/c)(1,0,0,1)$ in the coordinates $x_{\imath} = (r'_{t}, r_x, r_y, r_z)$, so that the phase is $(\omega/c)(r_z - r'_t)$ and the plane transverse to the propagation is spanned by $x$ and $y$.

**The transversality and tracelessness are checked, not assumed.** For the two amplitudes

$$
\text{plus:}\quad A_{xx} = -A_{yy} \ne 0, \qquad
\text{cross:}\quad A_{xy} = A_{yx} \ne 0,
$$

with all other components zero, a direct check verifies $-\nu_t^{\prime\,2}+\nu_{\Phi x}^2+\nu_{\Phi y}^2+\nu_{\Phi z}^2 = 0$, $-2\pi\nu_t^{\prime}A_{0\jmath}+k_1A_{1\jmath}+k_2A_{2\jmath}+k_3A_{3\jmath} = 0$, and $-A_{00}+A_{11}+A_{22}+A_{33} = 0$, for each amplitude and for the general transverse-traceless solution. Solving the conditions $A_{t\imath} = 0$, $-2\pi\nu_t^{\prime}A_{0\jmath}+k_1A_{1\jmath}+k_2A_{2\jmath}+k_3A_{3\jmath} = 0$, $-A_{00}+A_{11}+A_{22}+A_{33} = 0$ on a general symmetric $A_{\imath\jmath}$ leaves

$$
\boxed{\;A_{xx} = -A_{yy}, \qquad A_{xy} = A_{yx}, \qquad \text{all other components zero}\;},
$$

a two-parameter family: the plus amplitude and the cross amplitude, and nothing else. The two are related by a rotation through $45^\circ$ in the transverse plane, and together they span the two-dimensional space of physical polarizations, whose helicity eigenstates are the two circular combinations $A_{xx}\pm iA_{xy}$.

**The curvature is nonzero, so the wave is not pure gradient.** A direct computation of the linearized Riemann tensor of the displayed ansatz, using

$$
\mathrm{Riem}_{\imath\jmath\rho\sigma} = \tfrac{1}{2}\left(\partial^2/\partial x_{\jmath}\partial x_\rho h_{\imath\sigma} + \partial^2/\partial x_{\imath}\partial x_\sigma h_{\jmath\rho} - \partial^2/\partial x_{\imath}\partial x_\rho h_{\jmath\sigma} - \partial^2/\partial x_{\jmath}\partial x_\sigma h_{\imath\rho}\right),
$$

gives, for the plus amplitude,

$$
R_{txtx} = -R_{tyty} = \frac{\omega^2}{2c^2}\cos\!\left(\frac{\omega}{c}(r_z - r'_{t})\right),
\qquad R_{tztz} = 0,
$$

and, for the cross amplitude,

$$
R_{txty} = R_{txyz} = \frac{\omega^2}{2c^2}\cos\!\left(\frac{\omega}{c}(r_z - r'_{t})\right),
\qquad R_{txtx} = R_{tyty} = R_{tztz} = 0 .
$$

In both cases the Ricci tensor vanishes,

$$
\mathrm{Ric}_{\imath\jmath} = 0, \qquad \mathrm{Riem}_{\imath\jmath\rho\sigma} \ne 0 ,
$$

so each amplitude solves the vacuum equation and carries nonzero curvature. The nonvanishing components with two timelike indices are the components a local observer measures as tidal stretching; in the plus case the stretching is along $x$ and the compression along $y$, in the cross case along the two diagonals. The two polarizations were verified separately, so the result is not an artefact of the symmetric combination.

Because the vacuum equations force the Ricci part of the curvature to vanish at linear order, the physical, invariant content of a wave is its **Weyl** part, the ten-component tensor obtained from $\mathrm{Riem}_{\imath\jmath\rho\sigma}$ by removing the Ricci and scalar traces. In vacuum the two coincide. The two polarizations are the two independent components of the Weyl tensor that a lightlike wave can carry, and they are the two helicities of the previous count. Encoding the Weyl tensor in the biquaternion framework — through self-dual and anti-self-dual bivectors, or through the five Newman–Penrose scalars — is a separate problem, and it is recorded among the open questions rather than attempted here.

## The Quadrupole Formula

The wave equation of the first section, $\Box_\Phi\bar{h}_{\imath\jmath} = -\tfrac{16\pi G}{c^4}T_{\imath\jmath}$, is inhomogeneous: matter radiates. The standard slowly-varying, weak-field solution is the quadrupole formula, and it is the point at which two numerical errors are commonly made — the prefactor, and the choice of moment. Both are checked below against an independent result.

**The amplitude.** For an isolated, slowly moving source, the far-field transverse-traceless perturbation is

$$
h_{ij}^{\mathrm{TT}}(r'_t, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \frac{2G}{c^4 r}\,\left(d^2\mathcal{Q}_{ij}^{\mathrm{TT}}/d{r'_{t}}^2\right)(r'_t - r/c), \qquad
\mathcal{Q}_{ij} = \int \rho(r_{2x}\,\vec e_x+r_{2y}\,\vec e_y+r_{2z}\,\vec e_z)\left(r_{2i}r_{2j} - \tfrac{1}{3}r_2^2\delta_{ij}\right)d^3r_2,
$$

where $r = |r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|$, $\mathcal{Q}_{ij}$ is the **traceless (reduced) quadrupole moment**, and the transverse-traceless projection removes the trace and the longitudinal parts. The field is proportional to the **second** time derivative of the quadrupole moment. The retarded argument makes the wave outgoing along the future light cone, the null cone of $\Box_\Phi$, which is the zero-divisor cone of $\mathbb{B}_{\Phi}$ inherited from the material sector.

**No monopole, no dipole.** The multipole expansion begins at the quadrupole, and the reason is conservation. The monopole moment $M = \int\rho\,d^3r$ is the total mass–energy; it is conserved, $dM/dr'_t = 0$, so there is no monopole radiation. The dipole moment $d_i = \int\rho\,x_i\,d^3r$ has $dd_{i}/dr'_t = \int\rho\,v_i\,d^3r = P_i$, the total momentum, which is conserved for an isolated source; hence $d^2d_{i}/d{r'_{t}}^2 = 0$ and there is no dipole radiation. The leading radiating moment is therefore the quadrupole. This is the sharpest structural difference from electromagnetism, where the dipole radiates; it is a consequence of momentum conservation, and it is why the gravitational-wave formula has three time derivatives on a quadrupole rather than two on a dipole.

**The power.** The radiated power, averaged over a period, is

$$
\boxed{\;P = \frac{G}{5c^5}\left\langle \,d^3\mathcal{Q}_{ij}/d{r'_{t}}^3\,d^3\mathcal{Q}_{ij}/d{r'_{t}}^3 \right\rangle\;},
$$

with the same traceless quadrupole moment. The power is quadratic in the **third** derivative; the field is linear in the second. An equivalent form uses the un-reduced moment $I_{ij} = \int\rho\,x_ix_j\,d^3r$,

$$
P = \frac{G}{5c^5}\left\langle \,d^3I_{ij}/d{r'_{t}}^3 d^3I_{ij}/d{r'_{t}}^3 - \tfrac{1}{3}\left(d^3I_{\imath\imath}/d{r'_{t}}^3\right)^2 \right\rangle,
$$

which reduces to the traceless form because $I_{ij} = \mathcal{Q}_{ij} + \tfrac13\delta_{ij}I_{\imath\imath}$.

**The prefactor, verified on the binary.** The equal-mass circular binary is the standard check. Two masses $m$ in a circular orbit of radius $R$ (separation $d = 2R$) at angular frequency $\omega$ have the traceless quadrupole

$$
\mathcal{Q}_{xx} = \frac{mR^2}{3} + mR^2\cos 2\omega r'_t/c, \qquad
\mathcal{Q}_{yy} = \frac{mR^2}{3} - mR^2\cos 2\omega r'_t/c, \qquad
\mathcal{Q}_{xy} = mR^2\sin 2\omega r'_t/c,
$$

whose third derivatives give $d^3\mathcal{Q}_{ij}/d{r'_{t}}^3 d^3\mathcal{Q}_{ij}/d{r'_{t}}^3 = 128\,m^2R^4\omega^6$, a constant. Then

$$
P = \frac{G}{5c^5}\cdot128\,m^2R^4\omega^6
= \frac{64}{5}\frac{G^4}{c^5}\frac{m^5}{d^5},
$$

on using Kepler's law $\omega^2 = 2Gm/d^3$ and $R = d/2$. The standard equal-mass form of the binary power is

$$
P = \frac{32}{5}\frac{G^4}{c^5}\frac{(m_1m_2)^2(m_1+m_2)}{d^5}
= \frac{64}{5}\frac{G^4}{c^5}\frac{m^5}{d^5} \quad (m_1 = m_2 = m),
$$

and the two agree. A direct check of both the traceless and the unreduced forms of the power obtains the same result from each, and also verifies the angular projection identity by which the flux integral over the sphere reduces to the traceless form, so the factor $\tfrac15$ is confirmed twice over rather than read off from one case.

**What the formula is and is not.** It is a weak-field, slow-motion, far-zone result; it is the leading term of a multipole expansion, not an exact statement. Its prefactor is fixed by the coupling constant $8\pi G/c^4$ in the field equation and by the angular structure of the transverse-traceless projection. Nothing in this article derives either from the biquaternion algebra.

## The Wave Operator, the Redundancy, and the Counting in the Framework

The radiation theory is built from four objects, and it is worth asking of each whether the framework contains it or merely names it.

**The wave operator.** $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural} = \sum_{\imath}\partial^2/\partial R_{\imath}^2$ is an element of the framework, inherited from the Maxwell article and the parent. It is the operator whose null cone is the zero-divisor cone of $\mathbb{B}_{\Phi}$ and whose retarded solution carries the outgoing wave. Nothing here is transcribed: $\Box_\Phi$ is the algebra's own differential operator, and the statement $\Box_\Phi\bar{\delta\tilde{E}_{\Phi}}_{\imath} = 0$ is written in the framework's notation exactly.

**The redundancy and its residual part.** The linearized diffeomorphism is $\delta\tilde{E}_{\Phi,\imath} \mapsto \delta\tilde{E}_{\Phi,\imath} - \partial/\partial x_{\imath}\tilde Q_{\Phi,\mathrm d}$ with $\tilde Q_{\Phi,\mathrm d} \in \mathbb{B}_{\Phi}$, inherited from the parent. The residual freedom of the previous sections has a clean image: the harmonic condition is preserved by exactly those material four-vectors with

$$
\Box_\Phi\tilde Q_{\Phi,\mathrm d} = 0 .
$$

The residual redundancy is therefore the kernel of the framework's own d'Alembertian acting on $\mathbb{B}_{\Phi}$, and the count of the previous section can be stated in the framework's variables as: four redundant directions in $\mathbb{B}_{\Phi}$ remove four of the six harmonic-gauge frame components, leaving the two transverse-traceless directions. This is a genuine, if modest, piece of framework content: the residual freedom is not an extra structure imposed from outside, and its condition uses only $\Box_\Phi$ and the material sector.

**The counting.** Here the framework reaches its limit, and it is better to say so than to force an analogy. The parent supplies the decomposition $16 = 10 + 6$, the six being the infinitesimal local Lorentz kernel of the map $\delta\tilde{E}_{\Phi,\imath} \mapsto h_{\imath\jmath}$. The four-component parameter $\tilde Q_{\Phi,\mathrm d}$ then removes four of the ten, leaving six. That is as far as the algebra's counting goes. The step $6 \to 2$ requires knowing which of the six harmonic-gauge components propagate; it is the residual redundancy, not the algebra, that makes four of them non-dynamical, and it is the transverse-traceless projection — governed by the wave vector and by the unit metric $\delta_{\imath\jmath}$, neither of them a *selection principle* — that identifies the remaining two. The algebra has no analogue of the little group of a null vector and no representation of helicity, so it has **no natural handle on the polarization count**. The number two is inherited from the transcribed theory. A reader who expects the biquaternion structure to produce $\pm2$ the way it produces the Lorentz group will not find it here, and the absence is recorded as an open question rather than papered over with a resemblance.

**The polarization amplitudes.** There is a sharp negative statement to be made about the physical content itself. The two amplitudes are the traceless transverse components $A_{ij}$, and the algebra's natural single-biquaternion packaging of a symmetric rank-two object is

$$
\tilde{A}_{\Phi} = \sum_{i,j=1}^{3} A_{ij}\,\varepsilon_i\bar{\varepsilon}_j .
$$

For a traceless $A_{ij}$ this vanishes identically, $\tilde{A}_{\Phi} = \big(\sum_i A_{ii}\big)e_t = 0$, by the same computation that makes the packaging of $h_{\imath\jmath}$ collapse to its trace in the parent article. The two polarizations are therefore **exactly the components that the algebra's natural packaging annihilates**. The same holds for a plus amplitude and a cross amplitude separately: each is scalar-free, each packages to zero. The framework carries the wave in the frame perturbation $\delta\tilde{E}_{\Phi,\imath}$, an $\mathbb{B}_{\Phi}$-valued one-form; every attempt to compress it into a single biquaternion retains only the trace, and in transverse-traceless fixing condition the trace is zero. This is sharper than the parent's statement that the graviton is not a material biquaternion: the polarization content is invisible not only to $\mathbb{B}_{\Phi}$ but to the natural packaging into *any* single algebra element.

**The field strength, and a trap.** The invariant field strength is the linearized Riemann tensor, packaged index by index as a bivector-valued two-form

$$
\tilde{Q}_{3,\imath\jmath} = \tfrac{1}{2}\sum_{\rho,\sigma} \mathrm{Riem}_{\imath\jmath\rho\sigma}\,\bar{\varepsilon}_\rho\varepsilon_\sigma .
$$

Because the antisymmetric part of $\bar{\varepsilon}_\rho\varepsilon_\sigma$ has no scalar component, each $\tilde{Q}_{3,\imath\jmath}$ is a **complex pure vector** — an element of the six-dimensional subspace $\mathrm{span}_{\mathbb{R}}\{\vec e_{\imath}, i\vec e_{\imath}\}$ that the parent identifies with the Lorentz Lie algebra $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$ — and so lies in neither $\mathbb{B}_{\Phi}$ nor $\mathbb{B}_{\Psi}$. This invites an analogy with the electromagnetic field strength $\tilde{F} = i\vec E - c\vec B$, which is also a complex pure vector with vanishing scalar part and is likewise not in $\mathbb{B}_{\Phi}$. The analogy is real but narrow, and it must not be pushed past the field strength. What the two cases share is that a **field strength** built from derivatives of a potential can leave the material sector; the electromagnetic potential $\tilde{A}_{\Phi}$ itself is a single material four-vector, whereas the gravitational potential is an $\mathbb{B}_{\Phi}$-valued one-form $\delta\tilde{E}_{\Phi,\imath}$, one material four-vector per coordinate direction. And the graviton is not the field strength: it is the symmetric rank-two perturbation $h_{\imath\jmath}$, or its frame carrier, or the two traceless amplitudes — an object of dimension ten that is not a bivector, not a four-vector, and not a single element of $\mathbb{B}$. Placing the graviton "in a sector" because $\tilde{F}$ is not in $\mathbb{B}_{\Phi}$ would be an inference the notation does not license; the honest statement is that the *field strength* sits in the bivector subspace, the *potential* sits in $\mathbb{B}_{\Phi}$, and the *graviton itself* sits in no sector of the algebra at all.

**The source and the quadrupole moment.** The radiating source is the symmetric energy–momentum tensor $T_{\imath\jmath}$, and the radiating moment is the symmetric traceless $\mathcal{Q}_{ij}$. Both are symmetric rank-two objects, the class the material-space article records as not lying in $\mathbb{B}_{\Phi}$ and that the energy–momentum exercise shows no single biquaternion can faithfully carry. For the quadrupole moment the collapse is exact and total: $\sum_{ij}\mathcal{Q}_{ij}\varepsilon_i\bar{\varepsilon}_j = (\sum_{i}\mathrm{Sd}_{ii})e_t = 0$ for traceless $\Theta$. The algebra therefore cannot hold the quantity that the quadrupole formula differentiates; the formula is transcribed into the framework's notation, not derived from it. In particular the coupling constant $8\pi G/c^4$, and with it the prefactor $G/5c^5$, is not fixed by the algebra.

## What the Algebra Supplies and What It Does Not

The boundary can be drawn as a list, in the manner of the parent article.

**Supplied by the algebra, and recomputed here.** The wave operator $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural} = \sum_{\imath}\partial^2/\partial R_{\imath}^2$ and the null cone it defines; the carrier of the wave as an $\mathbb{B}_{\Phi}$-valued one-form $\delta\tilde{E}_{\Phi,\imath}$, with the trace-reversed shift $\bar{\delta\tilde{E}_{\Phi}}_{\imath} = \delta\tilde{E}_{\Phi,\imath} - \tfrac14h\varepsilon_{\imath}$ and the vacuum equation $\Box_\Phi\bar{\delta\tilde{E}_{\Phi}}_{\imath} = 0$ once the local Lorentz freedom is fixed; the local transformation $\delta\tilde{E}_{\Phi,\imath} \mapsto \delta\tilde{E}_{\Phi,\imath} - \partial/\partial x_{\imath}\tilde Q_{\Phi,\mathrm d}$, whose residual part is the kernel of $\Box_\Phi$ on $\mathbb{B}_{\Phi}$; the decomposition $16 = 10 + 6$ and the removal of four further directions by $\tilde Q_{\Phi,\mathrm d}$, giving the six harmonic-gauge components in the framework's own counting; and the bivector-valued packaging $\tilde{Q}_{3,\imath\jmath}$ of the invariant curvature, whose values lie in the complex pure-vector subspace.

**Interpretation, not derivation.** Reading the transverse-traceless amplitudes as the physical polarizations, and the two helicities $\pm2$ as the content of those amplitudes, is an interpretation of the transcribed theory. The framework is consistent with the interpretation — the amplitudes can be written in the material basis, and their tracelessness is the statement that the packaging vanishes — but the algebra does not force the interpretation, and the little-group counting that makes $\pm2$ inevitable has no algebraic counterpart.

**Not supplied, and left as gaps.** An action and a field equation for the frame, and hence any derivation of the linearized Einstein equation and of the wave equation $\Box_\Phi\bar{h}_{\imath\jmath} = 0$. A representation of diffeomorphism invariance, which is the origin of the redundancy whose residual part the framework can describe. A principle selecting the two propagating components from the six harmonic-gauge ones — that is, any handle on the polarization count or on helicity. A faithful single-biquaternion carrier of the transverse-traceless amplitudes, of the quadrupole moment, or of the energy–momentum source; the natural packaging annihilates the first two and collapses the third to its trace. A derivation of the coupling constant, and with it of the quadrupole prefactor. And empirical content: nothing here predicts a deviation from standard gravitational-wave physics.

## Open Questions

1. **A biquaternionic handle on the polarization count.** The main text states plainly that the algebra supplies no natural handle on the reduction $6 \to 2$. The framework does, however, contain the Lorentz group and its representations, and a lightlike wave vector has a nonzero stabiliser in it. Is the little group of the null direction — together with the representations the framework's Lorentz-group structure already carries — enough to produce the helicity $\pm2$ algebraically, without importing the little-group argument from the standard theory? If it is, the count would be a framework result rather than a transcription; if it is not, the reason would be worth stating as sharply as the absence.

2. **A faithful biquaternion carrier of the quadrupole moment.** No single biquaternion carries the symmetric traceless $\mathcal{Q}_{ij}$: the natural packaging collapses it to its vanishing trace, exactly as it collapses $h_{\imath\jmath}$ to the trace that does not propagate. The electromagnetic energy–momentum tensor is carried not by a single biquaternion but by a bilinear, and the exercise on that object shows how. Is the same true of $\mathcal{Q}_{ij}$ — is there a bilinear of two $\mathbb{B}_{\Phi}$ elements, or of a matter field, whose symmetric traceless part is the quadrupole moment and whose transformation under the Lorentz group is correct? A positive answer would give the framework a place to stand in the generation problem; a negative answer would explain why the quadrupole formula resists transcription into a single algebra element.

3. **The retarded solution and the null cone.** The Maxwell article writes the retarded potential with a kernel supported on the past light cone. Does the same construction, applied to the $\mathbb{B}_{\Phi}$-valued one-form $\delta\tilde{E}_{\Phi,\imath}$ with a rank-two source, produce the retarded $\bar{h}_{\imath\jmath}$ and the far-field amplitude $h_{ij}^{\mathrm{TT}} \propto \,d^2\mathcal{Q}_{ij}^{\mathrm{TT}}/d{r'_{t}}^2$? The transverse-traceless projection of the far field is the step most likely to require structure the algebra does not have, but the retarded kernel itself may go through unchanged.

4. **The Weyl tensor, helicity, and the two sectors.** The invariant content of the wave is the Weyl tensor, naturally packaged through self-dual and anti-self-dual bivectors. The writing half of this question is answered in [The Newman–Penrose Formalism in Biquaternionic Form](the-newman-penrose-formalism-in-biquaternionic-form.html): the five scalars are the components of the self-dual Weyl spinor $\tilde{Ξ}_{ABCD}\in\mathrm{sym}^4 S$, and the two-sector split does not organise them, since $\mathrm{sym}^4 S$ is five complex dimensional against the four of $\mathbb{B}$. What remains is the generation question — which element of $\mathrm{sym}^4 S$ a given spacetime produces — and whether the algebra distinguishes the two circular polarisations of the radiation or sees only their sum.

5. **The coupling constant and the prefactor.** The linearized Einstein equation carries $8\pi G/c^4$, and the quadrupole power carries $G/5c^5$. Both are transcribed. Is there any normalisation intrinsic to the algebra — a trace identity, a preferred bilinear, a choice of inner product on $\mathbb{B}_{\Phi}$ — that fixes either? The parent left the constant as a gap; the radiation theory does not close it. It is worth asking whether the question is even well posed without an action.

6. **Back-reaction and the energy of the wave.** The radiated power is quadratic in the wave amplitude, and its standard derivation uses the Isaacson stress–energy tensor, itself a bilinear in the transverse-traceless field. The algebra's bilinear structure supplies the electromagnetic energy–momentum tensor; does it supply the Isaacson tensor with the same naturalness, or does the transverse-traceless projection again obstruct the packaging? This is the framework's analogue of the quadrupole formula's quadratic side.

7. **Empirical content.** As everywhere in the framework, the open question is whether any of this yields a prediction distinguishing it from standard linearized gravity. The transcription developed here does not.

## Summary

Gravitational radiation in the linearized theory has been written in the biquaternion framework, and each step has been identified as either framework content or transcribed standard theory.

The trace-reversed perturbation $\bar{h}_{00} = h_{00}+\tfrac12h$ and $\bar{h}_{\imath l} = h_{\imath l}-\tfrac12h\,\delta_{\imath l}$ satisfies $\Box_\Phi\bar{h}_{\imath\jmath} = -\tfrac{16\pi G}{c^4}T_{\imath\jmath}$ in harmonic fixing condition, the framework's image of the condition being $\Box_\Phi\bar{\delta\tilde{E}_{\Phi}}_{\imath} = 0$. The harmonic fixing condition is preserved by the residual transformations with $\Box_\Phi\zeta_{\jmath} = 0$ — a condition verified on a general parameter, not only on a plane wave — so the redundancy is not exhausted by the fixing condition. The physical count is $10 \to 6 \to 2$: ten components of the symmetric perturbation, four harmonic conditions leaving six, and a four-dimensional residual gauge image inside those six whose complement is the two-dimensional transverse-traceless subspace. The split was verified by rank computation, and the final two were confirmed independently by the transverse-traceless tensor count and by the helicity count. On an explicit plane-wave ansatz, both the plus and the cross amplitudes were verified to be transverse and traceless, to have vanishing Ricci tensor, and to have nonvanishing Riemann tensor, so both carry physical curvature and neither is pure gradient. The quadrupole formula $P = \tfrac{G}{5c^5}\langle\,d^3\mathcal{Q}_{ij}/d{r'_{t}}^3 d^3\mathcal{Q}_{ij}/d{r'_{t}}^3\rangle$ was verified by matching it, on the equal-mass circular binary, to $\tfrac{32}{5}\tfrac{G^4}{c^5}\tfrac{(m_1m_2)^2(m_1+m_2)}{d^5}$, and the absence of monopole and dipole radiation was traced to the conservation of mass–energy and momentum.

The framework's reach was drawn. It supplies the wave operator and its null cone; the carrier of the wave as an $\mathbb{B}_{\Phi}$-valued one-form; the local transformation whose residual part is the kernel of $\Box_\Phi$ on $\mathbb{B}_{\Phi}$; the count $16 = 10 + 6$ and the removal of the four redundant directions from the ten; and the bivector packaging of the curvature, whose values lie in the complex pure-vector subspace and so in neither sector. It does not supply the dynamics that selects two of the six harmonic-gauge components: the framework has no natural handle on the polarization count, and the number two is inherited. The physical polarization amplitudes are exactly the components the algebra's natural single-biquaternion packaging annihilates, as is the traceless quadrupole moment, and the energy–momentum source is the rank-two object no single biquaternion carries. The quadrupole formula, and the coupling constant within it, are therefore transcribed rather than derived. The distinction between the electromagnetic field strength, which is a bivector outside $\mathbb{B}_{\Phi}$ despite the material potential it comes from, and the graviton, which is a symmetric rank-two object belonging to no sector at all, has been kept explicit; the two are not to be identified by the accident that both field strengths leave the material sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_{\imath}^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\varepsilon_{\imath}$ | Material basis of $\mathbb{B}_{\Phi}$: $\varepsilon_0=ie_t$ and $\varepsilon_{\imath}=\vec e_{\imath}$; the natural form on it is $+1$ on the three space rows and $-1$ on the time row, the minus being the square of the $i$ |
| $\delta_{\imath\jmath}=(1,1,1,1)$ | The unit metric, the coefficient tuple of $\sum_{\imath} Q_{\imath}^2$; the material interval is that form read on $Q_t=i q'_t$, and its one minus is the square of the $i$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural} = \mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$ | General quaternionic bilinear form on $\mathbb{B}_{\Phi}$, the interval |
| $Q_{\imath}=q_{\imath}+iq'_{\imath}$; on $\mathbb{B}_{\Phi}$, $Q_t=i q'_t$ and $Q_{\imath}=q_{\imath}$; $x_{\imath}=(r'_{t}, r_x, r_y, r_z)$ | The coordinate, its material reading, and the real coordinates in which the contractions are written out |
| $\tilde\nabla_\Phi, (\tilde\nabla_\Phi)^{\natural}, \Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural} = \sum_{\imath}\partial^2/\partial R_{\imath}^2$ | Biquaternionic gradient, conjugate, d'Alembertian |
| $h_{\imath\jmath}$, $h = -h_{00}+h_{11}+h_{22}+h_{33}$ | Metric perturbation and its trace |
| $\bar{h}_{00}=h_{00}+\tfrac12h$, $\bar{h}_{0k}=h_{0k}$, $\bar{h}_{\imath l}=h_{\imath l}-\tfrac12h\,\delta_{\imath l}$, $\bar{h} = -h$ | Trace-reversed perturbation |
| $\delta\tilde{E}_{\Phi,\imath} \in \mathbb{B}_{\Phi}$ | Frame perturbation carrying $h_{\imath\jmath} = \langle\varepsilon_{\imath},\delta\tilde{E}_{\Phi,\jmath}\rangle_{\natural} + \langle\delta\tilde{E}_{\Phi,\imath},\varepsilon_{\jmath}\rangle_{\natural}$ |
| $\bar{\delta\tilde{E}_{\Phi}}_{\imath} = \delta\tilde{E}_{\Phi,\imath} - \tfrac14 h\,\varepsilon_{\imath}$ | Trace-reversed frame perturbation |
| $\tilde Q_{\Phi,\mathrm d} \in \mathbb{B}_{\Phi}$ | Gauge four-vector, $\delta\tilde{E}_{\Phi,\imath} \mapsto \delta\tilde{E}_{\Phi,\imath} - \partial/\partial x_{\imath}\tilde Q_{\Phi,\mathrm d}$ |
| $-\partial/\partial x_0\bar{h}_{0\jmath}+\partial/\partial x_1\bar{h}_{1\jmath}+\partial/\partial x_2\bar{h}_{2\jmath}+\partial/\partial x_3\bar{h}_{3\jmath} = 0$, $\Box_\Phi\zeta_{\jmath} = 0$ | Harmonic (Lorenz, de Donder) gauge and its residual redundancy |
| $\Box_\Phi\bar{h}_{\imath\jmath} = -\tfrac{16\pi G}{c^4}T_{\imath\jmath}$ | Linearized Einstein equation |
| $A_{\imath\jmath}$; $A_{xx} = -A_{yy}$, $A_{xy} = A_{yx}$ | Plane-wave amplitude; the plus and cross polarizations |
| $2\pi\nu_{\Phi,\imath} = (\omega/c)(1,0,0,1)$, $-\nu_t^{\prime\,2}+\nu_{\Phi x}^2+\nu_{\Phi y}^2+\nu_{\Phi z}^2 = 0$ | Wave vector along $+z$ and its null condition |
| $\mathrm{Riem}_{\imath\jmath\rho\sigma}$, $\mathrm{Ric}_{\imath\jmath}$, $G_{\imath\jmath}$ | Linearized Riemann, Ricci, and Einstein tensors |
| $\tilde{Q}_{3,\imath\jmath} = \tfrac12\sum_{\rho,\sigma}\mathrm{Riem}_{\imath\jmath\rho\sigma}\bar{\varepsilon}_\rho\varepsilon_\sigma$ | Curvature as a bivector-valued two-form |
| $\mathcal{Q}_{ij} = \int\rho(x_ix_j - \tfrac13r^2\delta_{ij})d^3r$ | Traceless (reduced) quadrupole moment |
| $h_{ij}^{\mathrm{TT}} = \tfrac{2G}{c^4r}d^2\mathcal{Q}_{ij}^{\mathrm{TT}}/d{r'_{t}}^2$, $P = \tfrac{G}{5c^5}\langle\,d^3\mathcal{Q}_{ij}/d{r'_{t}}^3 d^3\mathcal{Q}_{ij}/d{r'_{t}}^3\rangle$ | Quadrupole amplitude and power |
| $2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$ | Trace reading of the Hermitian form on the informational sector |

## Further Reading

- Companion articles: [Linearized Gravity in Biquaternionic Form](linearized-gravity-in-biquaternionic-form.html); [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html); [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html); [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html); [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html); [Four-Vectors and the Interval](four-vectors-and-the-interval.html); [States, Observables and the Born Weight](states-observables-and-the-born-weight.html); [The Minimal Coupling in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The Relativistic Two-Body Problem in Biquaternionic Form](the-relativistic-two-body-problem-in-biquaternionic-form.html); [Radiation from Accelerated Charges in Biquaternionic Form](radiation-from-accelerated-charges-in-biquaternionic-form.html); [Twistor Theory and Biquaternions](twistor-theory-and-biquaternions.html); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html).
- Charles W. Misner, Kip S. Thorne, and John A. Wheeler, *Gravitation* (Freeman, 1973), for the linearized theory, the transverse-traceless fixing condition, the two polarizations, and the quadrupole formula with its energy-loss interpretation.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the linearized Einstein equation, the trace-reversal, the harmonic fixing condition, and the counting of the physical degrees of freedom.
- Sean M. Carroll, *Spacetime and Geometry: An Introduction to General Relativity* (Cambridge, 2019), for a compact treatment of gravitational waves and the residual redundancy.
- Michele Maggiore, *Gravitational Waves*, Vol. 1 (Oxford, 2008), for the quadrupole formula, the binary inspiral power, and the derivation from the transverse-traceless amplitude.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spin-coefficient and bivector formulation of the curvature on which the Weyl-tensor encoding rests.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic treatment of gravity in the same rotor language used here.
