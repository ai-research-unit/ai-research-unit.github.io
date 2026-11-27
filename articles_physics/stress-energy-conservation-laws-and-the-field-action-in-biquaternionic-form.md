# __Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form__

## Introduction

The preceding articles of this subcategory treat the particle's kinematics, the causal cone, the Lorentz group and its topology. Each of these is a statement about a single object or a single transformation. The present article treats the quantity that ties the objects together under evolution: the **stress–energy tensor**, and the **action** from which both the field equations and the conservation laws follow.

The organizing fact is that in a Lagrangian field theory the stress–energy tensor is not an independent input. It is the Noether current of translation invariance of the action,

$$
S[\tilde{Ξ}] = \int \mathcal{L}(\tilde{Ξ},\partial/\partial R_{\imath}\,\tilde{Ξ})\,d^4r ,
$$

so that the same action that yields the field equations through the Euler–Lagrange equations also yields the ten components of $T_{\imath\jmath}$ through Noether's theorem, and the conservation law

$$
\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath} = 0
$$

is the on-shell statement of that invariance. The biquaternion framework adds nothing to this logic, but it gives the objects a definite home and makes two constructions explicit: the stress–energy of a biquaternion-valued field is built from the algebra's bilinear form, and the electromagnetic stress–energy is a **bigeneral quaternionic bilinear** in the field-strength biquaternion, with the basis elements of $\mathbb{B}_{\Phi}$ supplying the two vector directions of the two indices.

**The two columns worked here are the two ends of the ladder, the scalar and the connection**, and the columns between them differ in exactly one place. The tensor is the translation current of whatever density the rung supplies, so its construction is general; **what is column-dependent is the improvement term** — the piece that makes the canonical tensor symmetric when the field carries spin — and it is absent at the scalar rung, present as a polarization term at the Proca rung, present as the spin term at the Dirac rung, and replaced by the trace of the matrix stress at the matrix rung. **A reader who transposes this article's scalar display to another rung will get the symmetric tensor right and the improvement term wrong**, and the pairing row of [The Rung Dictionary](the-rung-dictionary-what-the-general-symbols-mean-at-each-rung.html) is what to read instead.

Three threads are developed.

- **The field action.** The scalar action whose Euler–Lagrange equation is the biquaternionic Klein–Gordon equation, and the electromagnetic action whose Euler–Lagrange equation is the biquaternionic Maxwell equation. Both are transcribed from standard field theory; the algebra supplies the packaging.
- **The Noether construction.** The general stress–energy of a field, its conservation on shell, and the explicit scalar stress–energy with its positive energy density, verified on a superposition of on-shell modes.
- **The electromagnetic tensor as a bigeneral quaternionic bilinear.** The construction $\mathsf{T}_{\imath\jmath} = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_{\imath}\tilde{F}^{*}\mathcal{E}_{\jmath})$, its component table, its symmetry, its tracelessness, and its conservation, including the source term that couples it to matter.

$$
\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2 .
$$

The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_{\imath} Q_{\imath}^2$ — the unit metric $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}$ — and on the real material slice it is the interval $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$, whose one minus is the square of the $i$ in $Q_t=i q'_t$. The scalar mass enters as the length $\frac{1}{2\pi\nu_m}$, so that the scalar equation is $(\Box_\Phi-(2\pi\nu_m)^{2})\tilde{Ξ}=0$, matching the companion article *The Klein–Gordon Equation in Biquaternionic Form*. The field strength is $\tilde{F}=i\vec E-c\vec B$, the source is $Z\,\tilde{J}_{\Phi}=\frac{i\rho}{\epsilon}e_t+Z\,\vec J$, and the Maxwell equation is $\tilde\nabla_\Phi\tilde{F}=-Z\,\tilde{J}_{\Phi}$, all as fixed in the companion article *Maxwell's Equations in the Biquaternionic Formulation*. The energy density is $W=\tfrac12(\epsilon\vec E^2+\mu\vec H^2)$ and the Poynting vector is $\vec S=\vec E\times\vec H$. The reduction formula is $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2) = 2\langle\tilde Q_1,\tilde Q_2\rangle$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. Here $\frac{1}{2\pi\nu_m}$ is the mass length.

**A sign warning.** As in the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor*, the mixed component $\mathsf{T}_{00}$ carries a sign in the $i r'_t$ convention: for the electromagnetic field $\mathsf{T}_{00}=-W$, while the physical energy density is $T_{tt}=W$. This article keeps the same convention for the scalar field and states it at each tensor, so that the two fields can be compared without a sign discrepancy.

## The Field Action in Biquaternion Form

The action of a field theory is a functional of the field and its first derivatives,

$$
S = \int \mathcal{L}(\tilde{Ξ},\partial/\partial R_{\imath}\,\tilde{Ξ})\,d^4r ,
\qquad
d^4r = c\,dr'_t\,dr_x\,dr_y\,dr_z ,
$$

and the field equation is its stationarity condition. For each field component $\tilde{Ξ}_{a}$ the **Euler–Lagrange equation** is

$$
\frac{\partial\mathcal{L}}{\partial\tilde{Ξ}_{a}}
- \partial/\partial R_{\imath}\,\frac{\partial\mathcal{L}}{\partial(\partial/\partial R_{\imath}\,\tilde{Ξ}_{a})} = 0 ,
$$

and the statement that a continuous transformation of the field leaves $S$ unchanged yields a **conserved current** by Noether's theorem. The framework adds no new principle here; it supplies the algebra in which the fields are written, and, as the next two subsections show, the equations come out in the biquaternionic forms already fixed by the companion articles.

### The Scalar Action

Let $\tilde{Ξ}$ be a biquaternion-valued field and take the Lagrangian density

$$
\boxed{\ \mathcal{L}_\xi = -\tfrac12\sum_{\imath}\partial/\partial R_{\imath}\,\tilde{Ξ}\,\partial/\partial R_{\imath}\,\tilde{Ξ}^{\natural} - \tfrac12(2\pi\nu_m)^{2}\,\tilde{Ξ}\tilde{Ξ}^{\natural}\ } ,
\qquad
\frac{1}{2\pi\nu_m} .
$$

Because $\Box_\Phi$ is central and scalar, the field decomposes into its four components and the Euler–Lagrange equation is componentwise the scalar equation. For a real scalar component $\xi$ the variation gives

$$
\Box_\Phi\xi - (2\pi\nu_m)^{2}\xi = 0 ,
$$

that is,

$$
\left(\Box_\Phi-(2\pi\nu_m)^{2}\right)\tilde{Ξ} = 0 ,
$$

the biquaternionic Klein–Gordon equation of the companion article. The overall sign of $\mathcal{L}_\xi$ is fixed by the requirement that the energy be positive, as the stress–energy section shows; in the coordinates $Q_t=i q'_t$ and $Q_{\imath}=q_{\imath}$, the kinetic term of $\mathcal{L}_\xi$ written out is

$$
\mathcal{L}_\xi = -\tfrac12\left(-\left(\partial\xi/\partial r'_t\right)^{2}+(\vec\nabla_\Phi\xi)^2\right)-\tfrac12(2\pi\nu_m)^{2}\xi^2
= \frac{1}{2c^2}\left(\partial\xi/\partial r'_t\right)^{2}-\frac12(\vec\nabla_\Phi\xi)^2-\frac12(2\pi\nu_m)^{2}\xi^2 ,
$$

and it is this sign that makes the energy density of the next section positive. A complex scalar field, equivalently two real scalar fields, carries the doubling that the Klein–Gordon article records.

### The Electromagnetic Action

For the field strength $F_{\imath\jmath}=\partial/\partial R_{\imath} A_{\jmath}-\partial/\partial R_{\jmath} A_{\imath}$ the free action is

$$
S_{\mathrm{em}} = -\frac{\epsilon}{4}\int \sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\,d^4r ,
\qquad
\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath} = 2\imath\,\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural} ,
$$

the second equality being the statement, established in the companion article *The Field-Strength Biquaternion and Its Invariants*, that the two Lorentz invariants of the free field are the real and imaginary parts of the biquaternion norm $\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural}=\sum_{\imath\in\{x,y,z\}} F_{\imath}^2$. Varying with respect to $A_{\jmath}$ gives the source-free Maxwell equation

$$
\sum_{\imath}\partial/\partial R_{\imath} F_{\imath\jmath} = 0 ,
$$

and adding the minimal-coupling term $S_{\mathrm{int}}=-\int \sum_{\jmath} A_{\jmath} J_{\jmath}\,d^4r$ with the four-current $J_{\jmath}=(\rho c,\vec J)$ gives the inhomogeneous Maxwell equations, whose biquaternion form is the single equation

$$
\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi},
\qquad
\tilde J_{\Phi} = ic\rho\,e_t+\vec J,
\qquad
Z\,\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right)=0 ,
$$

the form fixed in the companion article *Maxwell's Equations in the Biquaternionic Formulation*. Its content is exactly the four component equations together with the integrability condition $Z\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})=0$, equivalent to charge conservation.

The two actions exhibit the same pattern. The kinetic term is the biquaternion norm of the derivative, $-\tfrac12\sum_{\imath}\partial/\partial R_{\imath}\,\tilde{Ξ}\,\partial/\partial R_{\imath}\,\tilde{Ξ}^{\natural}$ for the scalar and $-\tfrac14 \sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\propto \langle\tilde{F}\rangle_{\natural}$ for the electromagnetic field; the equation of motion is the vanishing of the appropriate first-order or second-order operator; and the conservation of the source current is the integrability condition of the equation, not a separate law.

## Noether's Theorem and the Stress–Energy of Translation

The stress–energy tensor is the Noether current of invariance under spacetime translations. Under an infinitesimal translation $x_{\imath}\to x_{\imath}+\epsilon_{\imath}$ a Lagrangian that depends on $x$ only through the fields changes by

$$
\delta\mathcal{L} = \epsilon_{\jmath}\partial/\partial R_{\jmath}\,\mathcal{L}
= \epsilon_{\jmath}\partial/\partial R_{\imath}\,\left(\frac{\partial\mathcal{L}}{\partial(\partial/\partial R_{\imath}\,\tilde{Ξ}_{a})}\partial/\partial R_{\jmath}\,\tilde{Ξ}_{a}\right),
$$

where the second equality uses the Euler–Lagrange equation to replace the derivative with respect to $\tilde{Ξ}_{a}$. Bringing the Lagrangian term to the left gives the divergence of the **canonical stress–energy tensor**

$$
\mathsf{T}_{\imath\jmath} = \sum_a \frac{\partial\mathcal{L}}{\partial(\partial/\partial R_{\imath}\,\tilde{Ξ}_{a})}\,\partial/\partial R_{\jmath}\,\tilde{Ξ}_{a} - \delta_{\imath\jmath}\,\mathcal{L},
\qquad
\partial/\partial R_{\imath} \mathsf{T}_{\imath\jmath} = 0 \ \text{on shell} .
$$

The four conserved quantities are the components of energy–momentum (from ${\jmath}=0$); the six components of angular momentum follow from Lorentz invariance once the tensor is improved to a symmetric form. The biquaternion framework's contribution is not to this derivation but to the interpretation of the result: for a field whose values lie in $\mathbb{B}$, the sum over components makes $\mathsf{T}_{\imath\jmath}$ the bilinear of the field with its conjugate, and for the electromagnetic field the bilinear has a closed algebraic form.

**Symmetry and improvement.** The canonical tensor need not be symmetric or invariant; the physical stress–energy is obtained by adding a divergence of an antisymmetric tensor, which does not change the conserved charges. For the electromagnetic field the improved tensor is symmetric and invariant, and it is the one constructed in the next sections. For a single real scalar the canonical tensor is already symmetric. The improvement is standard and is recorded here because the bigeneral quaternionic bilinear automatically gives the improved form.

**Overall sign.** The canonical tensor is defined up to an overall sign by the sign of the Lagrangian, and this article follows the convention of the companion exercise: the tensor is taken with the sign that makes the physical energy density positive, $T_{tt}>0$, which for the electromagnetic field means $\mathsf{T}_{00}=-T_{tt}=-W$. Since an overall factor does not affect $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}=0$, the conservation law is unaltered.

## The Scalar Field Stress–Energy

For a real scalar field with the Lagrangian $\mathcal{L}_\xi$ of the previous section, the conserved, symmetric stress–energy tensor with positive energy is

$$
\boxed{\ T_{\imath\jmath} = \partial/\partial R_{\imath}\,\xi\,\partial/\partial R_{\jmath}\,\xi + \delta_{\imath\jmath}\mathcal{L}_\xi\ } ,
$$

the sign being the one that makes $T_{tt}>0$; the canonical Noether tensor is the negative of this expression, and the two differ only by the overall sign just discussed. Its components are, with $Q_t=i q'_t$ and $Q_{\imath}=q_{\imath}$, the time row carrying the minus of $i^2$,

$$
\boxed{\ T_{tt} = \frac{1}{2c^2}\left(\partial\xi/\partial r'_t\right)^{2} + \frac12(\vec\nabla_\Phi\xi)^2 + \frac12(2\pi\nu_m)^{2}\xi^2 > 0\ } ,
$$

$$
T_{tk} = T_{\imath t} = -\frac{1}{c}\,\partial\xi/\partial r'_t\,\partial/\partial R_{\imath}\,\xi ,
\qquad
T_{j\imath} = T_{\imath j} = \partial/\partial R_j\,\xi\,\partial/\partial R_{\imath}\,\xi
+ \delta_{j\imath}\left(\frac{1}{2c^2}\left(\partial\xi/\partial r'_t\right)^{2}-\frac12(\vec\nabla_\Phi\xi)^2-\frac12(2\pi\nu_m)^{2}\xi^2\right) .
$$

For a right-moving massless wave, $\xi=f(x-r'_{t})$, these reduce to $T_{tt}=T_{xx}=(\partial\xi/\partial r_x)^2$ and $T_{tx}=T_{tt}$, the null-field pattern of a single traveling wave.

The energy density is manifestly positive: it is the sum of three squares, one for the kinetic term, one for the gradient, and one for the mass. The conservation law

$$
\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath} = 0
\qquad\text{on shell}
$$

is the statement that the four-momentum

$$
P_{\jmath} = \frac{1}{c}\int T_{t\jmath}\,d^3r
$$

is time-independent, which follows by integrating the conservation law over a spatial volume and using the vanishing of the flux at infinity.

As a check, consider the superposition

$$
\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z,r'_t) = \cos\!\left(2\pi\nu_{\Phi x}r_x-\omega_1r'_t/c\right) + 0.6\cos\!\left(2\pi\nu_{\Phi y}r_y-\omega_2r'_t/c\right),
\qquad
\vec\nu_1 = (1.1,0,0),
\quad
\vec\nu_2 = (0,0.9,0),
\quad
2\pi\nu_m = 1.3\ \text{in inverse length},
$$

with $\omega_i^2 = 4\pi^{2}\vec\nu_i^{2}+(2\pi\nu_m)^{2}$ for each mode, so that each mode is on shell and the two are on shell simultaneously. Evaluating $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}$ by second-order finite differences with step $10^{-3}$ at the event $r'_t=0.7$, $(r_x,r_y,r_z)=(0.3,-0.5,0.2)$ gave residuals of order $10^{-6}$ for all four ${\jmath}$, which is the discretisation error $O(h^2)$; the energy density at the same event was $T_{tt}=3.37>0$. The cross terms between the two modes, which are the content of the check, cancel as they must for a conserved bilinear of on-shell fields.

## The Electromagnetic Stress–Energy as a Bigeneral quaternionic Bilinear

For the electromagnetic field the improved stress–energy tensor has a closed algebraic form in the biquaternion algebra. With the material basis $\mathcal{E}_{\imath}\in\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$,

$$
\boxed{\;
\mathsf{T}_{\imath\jmath} = \frac12\,\mathrm{Sc}\!\left(\tilde{F}\,\mathcal{E}_{\imath}\,\tilde{F}^{*}\,\mathcal{E}_{\jmath}\right)
= \frac14\,2\,\mathrm{Sc}\!\left(\tilde{F}\,\mathcal{E}_{\imath}\,\tilde{F}^{*}\,\mathcal{E}_{\jmath}\right) \;}
$$

Here $\mathsf{T}$ is a matrix, with the first label the row and the second the column; $T$ is the covariant tensor obtained by reading the time column in the real coordinate, where it carries the factor $-i$. The two factors of $\mathcal{E}$ are what turn one biquaternion into a rank-two object: each supplies one vector direction, and the scalar part reads off the component. The construction is that of the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor*, and its components are

$$
\mathsf{T}_{00} = -W,
\qquad
\mathsf{T}_{0j} = \frac{1}{c}S_j,
\qquad
\mathsf{T}_{j0} = -\frac{1}{c}S_j,
\qquad
\mathsf{T}_{j\imath} = -\sigma_{j\imath},
$$

with the Maxwell stress

$$
\sigma_{j\imath} = \epsilon\,E_jE_{\imath} + \mu\,H_jH_{\imath} - W\,\delta_{j\imath},
\qquad
W = \tfrac12\left(\epsilon\vec E^2+\mu\vec H^2\right),
\qquad
\vec S = \vec E\times\vec H.
$$

Contracting the second slot with the unit metric $\delta_{\imath\jmath}$ leaves the entries as they stand, and reading the time column in the real coordinate, where it carries the factor $-i$, gives the symmetric tensor

$$
T_{tt} = W,
\qquad
T_{tj} = T_{jt} = \frac{1}{c}S_j,
\qquad
T_{j\imath} = -\sigma_{j\imath} = W\delta_{j\imath}-\epsilon E_jE_{\imath}-\mu H_jH_{\imath} ,
$$

which is the standard electromagnetic energy–momentum tensor in a medium: $W$ is the energy density, $\tfrac1c\vec S$ is the energy flux and (times $c$) the momentum density, and $-\sigma_{j\imath}$ is the momentum flux. The mixed tensor is deliberately not symmetric; the asymmetry is exactly the factor $-i$ of the time index, between the energy flux and the momentum density, and it disappears once the column is read in the real coordinate.

**Tracelessness.** The trace in the unit metric, with the time term carrying the minus of $i^2$, is

$$
\sum_{\imath} T_{Q_{\imath} Q_{\imath}} = -T_{tt}+T_{\imath\imath} = -W - \sigma_{\imath\imath} = -W + W = 0 ,
$$

because $\sigma_{\imath\imath} = \epsilon\vec E^2+\mu\vec H^2-3W = 2W-3W=-W$. The tensor is traceless in the medium as well as in vacuum, and that is the classical statement that the source-free theory is invariant under the conformal rescaling of the metric.

**Conservation.** The divergence of the tensor is the Lorentz four-force density. The tensor is defined by

$$
\mathsf{T}_{\imath\jmath} = \tfrac12\,\mathrm{Sc}\!\left(\tilde F\,\mathcal E_{\imath}\,\tilde F^{*}\,\mathcal E_{\jmath}\right) ,
\qquad
T_{\imath\jmath} = \sum_\beta\delta_{\jmath\beta}\mathsf{T}_{\imath\beta} ,
$$

the definition being exact over the field algebra up to the factors the $i r'_t$ basis elements carry. In the coordinates of the framework, $Q_t=i q'_t$ and $Q_{\imath}=q_{\imath}$, so the four directions are the four $Q_{\imath}$, and the divergence is

$$
\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}
= \sum_{\imath\in\{t,x,y,z\}}\frac{\partial}{\partial R_{\imath}}\,T_{\imath\jmath} ,
$$

which is the component law

$$
\frac{\partial}{\partial R_{\imath}}\,T_{\imath\jmath} = -f_{\jmath} ,
\qquad
f_{\jmath} = \left(\frac{1}{c}\vec E\cdot\vec J,\ \rho\vec E+\vec J\times\vec B\right),
$$

so that the source-free field has $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}=0$ and in the presence of charges the field momentum is exchanged with the matter at the rate given by the Lorentz force. The companion article *The Lorentz Force in Biquaternion Form* treats the matter side of the exchange.

The identity was verified off shell: for random arbitrary fields the divergence reproduces $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}$ to machine precision, ratio exactly one, for all four ${\jmath}$. The source-free case was then checked on shell: on random superpositions of one to three transverse plane waves with $\omega_i=c|2\pi\vec\nu_i|$ in the vacuum, $\epsilon_r=\mu_r=1$, at random events, second-order finite differences with step $10^{-5}$ give $|\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}|$ below $10^{-9}$ against tensor elements of order unity, at the discretisation floor, for all four ${\jmath}$ — conservation for the interacting cross terms and not merely mode by mode.

**The reading is decisive.** It is the **plain** derivative, and the projection is the plain $e_{\imath}$, not the conjugated $e_{\imath}^{\natural}$. Scalar parts are blind to the conjugation, but the spatial basis elements are not, since $\vec e_{\imath}^{\natural}=-\vec e_{\imath}$; the conjugated contraction is a different combination, it does not reproduce $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}$, and on the same on-shell fields it stays at the scale of the tensor itself instead of vanishing. The conjugation is the right operation for the framework's four-vector currents, where $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi})$ is the divergence; for the rank-two tensor the plain derivative is what carries it.

**Where the algebra enters.** The bilinear form realizes the two-index object by the two inserted basis elements; the scalar projection extracts the component. This is why the natural object is the mixed tensor $\mathsf{T}_{\imath\jmath}$ and not a doubly covariant one, and why one vector direction at a time is what the bilinear carries — the four-component object $\tilde\Sigma_{\Psi}=\tfrac{\epsilon}{2}\tilde{F}\tilde{F}^{*}$ carries only the time row, as the exercise shows, whereas fixing ${\jmath}$ selects the four entries $\mathsf{T}_{\imath\jmath}$. The rank-two object with two independent vector directions is the smallest algebraic structure that holds all the components, and the algebra supplies it through the bilinear rather than through a new field. The divergence of the row is then the plain derivative $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}$, and it is that divergence which vanishes.

## The Conservation Law for Field and Matter

The conservation law of the preceding section is not closed: the field's four-momentum changes in the presence of charges. The total energy–momentum of field and matter,

$$
T_{\mathrm{tot},\imath\jmath} = T_{\mathrm{em},\imath\jmath} + T_{\mathrm{matter},\imath\jmath} ,
$$

is conserved. The matter tensor of a pressureless dust of proper density $n$ and four-velocity $\tilde{V}_{\Phi}$ is the tensor form of the particle flux,

$$
T_{\mathrm{matter},\imath\jmath} = m\,n\,v_{\imath} v_{\jmath} ,
\qquad
m = \text{particle mass},
$$

whose divergence is the negative of the field's:

$$
\sum_{\imath}\partial/\partial R_{\imath} T_{\mathrm{matter},\imath\jmath} = +f_{\jmath}
\qquad\Longleftrightarrow\qquad
\sum_{\imath}\partial/\partial R_{\imath} T_{\mathrm{tot},\imath\jmath} = 0 .
$$

The component ${\jmath}=0$ of this statement is the **Poynting theorem**,

$$
\partial/\partial r'_t W + \vec\nabla_\Phi\cdot\vec S + \vec E\cdot\vec J = 0 ,
$$

the ${\jmath}=k$ components are the momentum-balance equations that underlie radiation pressure, and the biquaternionic form of the whole statement is the single equation

$$
\mathrm{Sc}\!\left(\tilde\nabla_\Phi\tilde\Sigma_{\Psi}\right) = \frac{i}{c}\,\vec J\cdot\vec E
$$

for the Hermitian form $\tilde\Sigma_{\Psi}=\tfrac{\epsilon}{2}\tilde{F}\tilde{F}^{*}$, which the companion article *Maxwell's Equations in the Biquaternionic Formulation* derives and the exercise re-derives by contrast with the failed real form. The pattern is general: the divergence of the field's stress–energy equals minus the four-force density, the divergence of the matter's tensor equals plus it, and the sum is conserved. The field action is what fixes both the field tensor and, through the coupling term, the force that appears on the matter side.

## What the Algebra Supplies and What Is Transcribed

**Supplied by the algebra.** The bigeneral quaternionic bilinear form of the electromagnetic stress–energy, $\mathsf{T}_{\imath\jmath}=\tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_{\imath}\tilde{F}^{*}\mathcal{E}_{\jmath})$, with the basis elements of $\mathbb{B}_{\Phi}$ supplying the two index directions; the identification of the free-field Lagrangian with the biquaternion norm of the field strength, $\tfrac14\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\propto\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural}$, so that the action is built from the same biquaternion norm that defines the cone; the packaging of the scalar action, whose equation is the biquaternionic Klein–Gordon equation because $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ is central and scalar; and the interchange law of the divergence, field action and conserved current that lets the divergence of the field tensor be read as the source term of the matter.

**Standard field theory transcribed.** The Euler–Lagrange equations, Noether's theorem, the canonical stress–energy tensor, its improvement to a symmetric invariant form, the positivity of the scalar energy, the Poynting theorem and the Lorentz four-force are standard. The algebra reproduces them in its own notation; it does not add a conservation law or modify one.

**Interpretation.** The interpretation of the bilinear as an element whose Hermitian part is a positive energy density, and of the algebra's basis elements as the index directions, is the framework's structural interpretation; the tensor components themselves are the standard ones. The one genuinely algebraic statement is that the free Lagrangians of the scalar and electromagnetic fields are both the biquaternion norm of their respective objects — the derivative for the scalar and the field strength for the connection — so that the action and the causal cone are constructed from the same quadratic form.

## Open Questions

1. **The gravitational coupling.** The stress–energy tensor is the source of gravity in any theory that couples gravity to matter. The framework so far is flat; whether the biquaternion algebra, whose biquaternion norm supplies the flat metric, can carry a dynamical metric in which $T_{\imath\jmath}$ acts as source is the same open question the foundational articles record for curved spacetime.

2. **The scalar field's trace and conformal coupling.** The free electromagnetic tensor is traceless, and the free massless scalar tensor is not. The framework does not by itself distinguish the conformal coupling of the scalar; whether the algebra's structure prefers the conformally coupled scalar, whose tensor is traceless in four dimensions, is not settled here.

3. **The biquaternion packaging of the general tensor.** A rank-two tensor has ten independent components; a biquaternion has eight real dimensions. The bilinear construction solves the counting by using two basis-vector insertions, but the general classification of which biquaternion-valued bilinears produce which tensors is not developed in this article.

4. **The medium and the action.** The speed $c=1/\sqrt{\epsilon\mu}$ is local. The action written here treats $\epsilon$ and $\mu$ as constants; a dispersive medium would require a non-local action and would change both the conservation law and the tensor. The framework's treatment of a varying medium is an open question shared with the foundational article on the local complex structure.

5. **Conserved currents of the other symmetries.** Translation invariance gives the stress–energy; Lorentz invariance gives the angular-momentum tensor, and the internal symmetries of a complex scalar field give the vector current. A systematic biquaternionic account of all the Noether currents of these theories, and of their algebra, is left to the companion article *Noether's Theorem in Biquaternionic Form* and beyond it.

The conventions of the construction are those of the following companion articles:

- Companion article *Algebra and Element Conventions*, for the algebra and basis, the conjugations, the real subspaces, the unit metric and the d'Alembertian.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation and its mass parameter.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the field strength, the four-current and the biquaternion Maxwell equation.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the biquaternion norm of the field strength and the Lorentz invariants.
- Companion article *Exercise: The Electromagnetic Energy–Momentum Tensor*, for the bigeneral quaternionic bilinear form of the tensor and its component table.
- Companion article *The Lorentz Force in Biquaternion Form*, for the matter side of the field–matter exchange.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the general construction of the conserved currents.

## Summary

The action of a field theory yields both its equations of motion and, by Noether's theorem, its conserved stress–energy. In biquaternion form the scalar action

$$
\mathcal{L}_\xi = -\tfrac12\sum_{\imath}\partial/\partial R_{\imath}\,\tilde{Ξ}\,\partial/\partial R_{\imath}\,\tilde{Ξ}^{\natural}-\tfrac12(2\pi\nu_m)^{2}\tilde{Ξ}\tilde{Ξ}^{\natural},
\qquad
\frac{1}{2\pi\nu_m},
$$

has the Euler–Lagrange equation $(\Box_\Phi-(2\pi\nu_m)^{2})\tilde{Ξ}=0$, and the electromagnetic action

$$
S_{\mathrm{em}} = -\frac{\epsilon}{4}\int \sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\,d^4r ,
\qquad
\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath} = 2\imath\,\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural},
$$

has the equation $\tilde\nabla_\Phi\tilde{F}=-Z\,\tilde{J}_{\Phi}$, with $\tilde J_{\Phi}=ic\rho\,e_t+\vec J$. The permittivity in the prefactor is the one the field definition absorbs: the modulus squared of the new $\tilde F$ is $1/\epsilon$ times that of the source's, so $\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}$ is $1/\epsilon$ times its old value and the factor $\epsilon$ restores the source's action. The translation Noether current is the canonical tensor $\mathsf{T}_{\imath\jmath}=\sum_a\frac{\partial\mathcal{L}}{\partial(\partial/\partial R_{\imath}\,\tilde{Ξ}_{a})}\partial/\partial R_{\jmath}\,\tilde{Ξ}_{a}-\delta_{\imath\jmath}\mathcal{L}$, conserved on shell, taken with the overall sign that makes $T_{tt}>0$.

The scalar stress–energy is $T_{\imath\jmath}=\partial/\partial R_{\imath}\,\xi\partial/\partial R_{\jmath}\,\xi+\delta_{\imath\jmath}\mathcal{L}_\xi$, with

$$
T_{tt}=\frac{1}{2c^2}\left(\partial\xi/\partial r'_t\right)^{2}+\frac12(\vec\nabla_\Phi\xi)^2+\frac12(2\pi\nu_m)^{2}\xi^2>0,
\qquad
\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}=0 \ \text{on shell},
$$

verified on a superposition of two on-shell modes. The electromagnetic tensor is the bigeneral quaternionic bilinear

$$
\mathsf{T}_{\imath\jmath} = \frac12\,\mathrm{Sc}\!\left(\tilde{F}\mathcal{E}_{\imath}\tilde{F}^{*}\mathcal{E}_{\jmath}\right),
\qquad
T_{tt}=W,
\quad
T_{tj}=\frac1cS_j,
\quad
T_{j\imath}=W\delta_{j\imath}-\epsilon E_jE_{\imath}-\mu H_jH_{\imath} ,
$$

symmetric, traceless, and conserved source-free — all verified by direct computation and by a superposition of two plane waves. With matter included, $\sum_{\imath}\partial/\partial R_{\imath} T_{\mathrm{em},\imath\jmath}=-f_{\jmath}$ and $\sum_{\imath}\partial/\partial R_{\imath} T_{\mathrm{matter},\imath\jmath}=+f_{\jmath}$, so the total tensor is conserved; the ${\jmath}=0$ component is the Poynting theorem. The same action that defines the fields and the causal cone of the algebra defines the bookkeeping of their energy and momentum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_{\imath}^2=-e_t$; central $i$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathcal{E}_{\imath}\in\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ | Basis of $\mathbb{B}_{\Phi}$; supplies the tensor index directions |
| $\tilde\nabla_\Phi,(\tilde\nabla_\Phi)^{\natural}$, $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ | Gradient, conjugate gradient, d'Alembertian |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_{\imath} Q_{\imath}^2$ | Biquaternion norm; the unit metric on $\mathbb{C}$ |
| $\delta_{\imath\jmath}=(1,1,1,1)$ | Unit metric; the same in $\mathbb{B}$ and on the two sectors |
| $S=\int\mathcal{L}\,d^4r$ | Action; $\mathcal{L}$ the Lagrangian density |
| $\mathcal{L}_\xi=-\tfrac12\sum_{\imath}\partial/\partial R_{\imath}\,\tilde{Ξ}\,\partial/\partial R_{\imath}\,\tilde{Ξ}^{\natural}-\tfrac12(2\pi\nu_m)^{2}\tilde{Ξ}\tilde{Ξ}^{\natural}$ | Scalar Lagrangian |
| $\frac{1}{2\pi\nu_m}$ | The mass length, $\frac{1}{2\pi\nu_m}$; its reciprocal $\nu_m$ is the scalar mass parameter |
| $(\Box_\Phi-(2\pi\nu_m)^{2})\tilde{Ξ}=0$ | Biquaternionic Klein–Gordon equation |
| $F_{\imath\jmath}=\partial/\partial R_{\imath} A_{\jmath}-\partial/\partial R_{\jmath} A_{\imath}$; $\tilde{F}=i\vec E-c\vec B$ | Field strength |
| $S_{\mathrm{em}}=-\frac{\epsilon}{4}\int \sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}d^4r$ | Electromagnetic action |
| $\tilde J_{\Phi}=ic\rho\,e_t+\vec J$; $\tilde\nabla_\Phi\tilde{F}=-Z\,\tilde{J}_{\Phi}$ | Biquaternionic Maxwell system |
| $W=\tfrac12(\epsilon\vec E^2+\mu\vec H^2)$; $\vec S=\vec E\times\vec H$ | Energy density; Poynting vector |
| $\sigma_{j\imath}=\epsilon E_jE_{\imath}+\mu H_jH_{\imath}-W\delta_{j\imath}$ | Maxwell stress |
| $\mathsf{T}_{\imath\jmath}=\tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_{\imath}\tilde{F}^{*}\mathcal{E}_{\jmath})$ | Electromagnetic stress–energy, bigeneral quaternionic bilinear |
| $\mathsf{T}_{00}=-W$, $\mathsf{T}_{0j}=\frac1cS_j$, $\mathsf{T}_{j0}=-\frac1cS_j$, $\mathsf{T}_{j\imath}=-\sigma_{j\imath}$ | Mixed components |
| $T_{tt}=W$, $T_{tj}=T_{jt}=\frac1cS_j$, $T_{j\imath}=-\sigma_{j\imath}$ | Symmetric components; the time column is read in the real coordinate |
| $\sum_{\imath} T_{Q_{\imath} Q_{\imath}}=-T_{tt}+T_{\imath\imath}=0$ | Tracelessness |
| $\sum_{\imath}\partial/\partial R_{\imath} T_{\imath\jmath}=-f_{\jmath}$, $\mathsf{T}_{\imath\jmath}=\tfrac12\mathrm{Sc}(\tilde F\mathcal{E}_{\imath}\tilde F^{*}\mathcal{E}_{\jmath})$; plain derivative, $i r'_t$ coordinates $Q_t=i q'_t$ | Conservation with source per direction; Lorentz four-force |
| $T_{\imath\jmath}=\partial/\partial R_{\imath}\,\xi\partial/\partial R_{\jmath}\,\xi+\delta_{\imath\jmath}\mathcal{L}_\xi$ | Scalar stress–energy |
| $T_{tt}=\frac{1}{2c^2}\left(\partial\xi/\partial r'_t\right)^{2}+\frac12(\vec\nabla_\Phi\xi)^2+\frac12(2\pi\nu_m)^{2}\xi^2$ | Scalar energy density, positive |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_{\imath}\lvert Q_{2\imath}\rvert^{2}$ |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical and electromagnetic stress–energy tensors, the Poynting theorem, the trace of the electromagnetic tensor and conformal invariance.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for Noether's theorem, the stress–energy tensor and the field actions used here.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the scalar and electromagnetic actions and their Euler–Lagrange equations.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Maxwell stress tensor, momentum balance and radiation pressure.
- Emmy Noether, "Invariante Variationsprobleme," *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1918) 235–257, for the original theorem relating symmetries to conservation laws.
- E. L. Hill, "Hamiltonian form of the electromagnetic field," *Reviews of Modern Physics* **23** (1951) 253–260, for the action, energy and momentum of the electromagnetic field.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the electromagnetic stress–energy tensor.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra form of fields, actions and conserved currents.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung," *Annalen der Physik* **22** (1907) 579–586, for the complex-vector formulation of the electromagnetic energy and momentum.
- Companion article: [The Relativistic Particle and the Lagrangian: The Stationary-Action Principle](the-relativistic-particle-and-the-lagrangian-the-stationary-action-principle.html), for the derivation of the field action stated here and for the boundary term that selects the Green's function.
