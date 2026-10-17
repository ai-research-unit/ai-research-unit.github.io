# __The Most Common Items with a Tilde__

**Scope: tilde glyphs only.** Every symbol in the tables carries a tilde. Four kinds of glyph are outside the scope and are not listed: a matrix, $I_n$, $\mathsf{M}_2$, $\mathsf{M}_4$; a pure element written with an arrow, $\vec Q$, $\vec q$, $\vec u$, $\vec U$, $\vec\Xi$, $\vec\Upsilon$; a mark that is not an element, $\tilde\cdot$, $\tilde\star$; and every glyph of the reduced, tilde-free layers, $\Pi_\pm$, $\Xi_\pm$, $\Upsilon_\pm$. The first is fixed by the rule that a matrix carries no tilde, §*The 2×2 Matrix Representation* of *Conventions in the Biquaternion Universe*; the others are elements of other layers or of no layer at all. The operator section states the rule that pairs the two marks; it is not a catalogue of arrowed glyphs.

The tilde marks a quaternionic factor. The last column of every table is the number of articles in which the symbol occurs, counted over the articles of `articles_maths/` and `articles_physics/` at the last scan. The list is triaged into three sections.

- **1. Allowed tilde** — the role is fixed by *Conventions in the Biquaternion Universe* and checked against the corpus. Cite these entries as they stand. The tables are ordered by theme, as the objects are.
- **2. To be tested** — one specific role, plausible but not yet verified. Test before citing. A symbol that is also wrongly generic keeps its role here and its generic claim in section 3.
- **3. Wrongly generic, to be rewritten** — one line per work item. It covers a generic claim outside the Q family and a tilde on an object that has no right to it. Do not cite.

The governing rule: **only the Q family is generic, and only an element carries the tilde.** $\tilde Q$ is the biquaternion or split-biquaternion element and $\tilde q$ the quaternion or split-quaternion element; numbered variants are allowed. A letter outside the family names an object, or an element bound where it is introduced. A matrix is the image of an element and takes no tilde.

## 1. Allowed tilde

### The Layer Glyphs

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde Q$ | General element of the algebra | $Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $Q_\mu\in\mathbb{C}$ | $\mathbb{B}$ | The only generic glyph; a second and a third are $\tilde Q_1,\tilde Q_2$ | 647 |
| $\tilde q$ | General element of the quaternion layer | $q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, $q_\mu\in\mathbb{R}$ | $\mathbb{H}_{\mathbb{B}}$ | The only generic glyph of that layer; a second is $\tilde q_1$ | 197 |
| $\tilde\Pi$ | Idempotent, projector | $\Pi_te_t+\vec\Pi$, with $\tilde\Pi^2=\tilde\Pi$ | $\mathbb{B}$; $\mathbb{M}_+$ when $\tilde\Pi^{*}=\tilde\Pi$ | A Hermitian idempotent is a pure state; $\mathbb{B}\tilde\Pi$ is the minimal left ideal, the state module | 267 |
| $\tilde\Xi$ | Root of a central value | $\Xi_te_t+\vec\Xi$, with $\tilde\Xi^2=\lambda e_t$, $\lambda$ central | $\mathbb{B}$; $\mathbb{M}_+$ for the roots $i\vec e_k$; $\mathbb{C}_{\mathbb{B}}$ for $\pm i$ | For a root of $1$ the idempotents are $\tfrac12(e_t\pm\tilde\Xi)$ | 56 |
| $\tilde\nu$ | Nilpotent of the quaternion layer | $\nu_te_t+\vec\nu$, with $\tilde\nu^2=0$ | The null cone, in neither sector | The biquaternion layer writes $\tilde\Upsilon$ | 8 |
| $\tilde U$ | Norm-one element | $U_te_t+\vec U$, with $\mathrm{Norm}(\tilde U)=e_t$; $\tilde U^{*}\tilde U=e_t$ in the unitary case | $\mathbb{B}$ | The rotor; the unitary group is $\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)$ | 167 |
| $\tilde u$ | Unit quaternion | $\cos(\theta/2)e_t+\sin(\theta/2)\vec u$, $\vec u$ a unit real vector | $\mathbb{H}_{\mathbb{B}}$, norm one | The rotor of $\mathrm{Sp}(1)\cong\mathrm{SU}(2)$; a pure unit quaternion is $\vec u$ | 60 |

### The Gradient and the Operators

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde\nabla$ | Biquaternionic gradient | $e_t\,\partial/\partial Q_t+\vec e_x\,\partial/\partial Q_x+\vec e_y\,\partial/\partial Q_y+\vec e_z\,\partial/\partial Q_z$ | Operator, $\mathbb{B}$-valued | Its conjugate $\tilde\nabla^{\natural}=e_t\partial_t-\vec e_k\partial_k$ is the second factor of $\Box$ | 203 |

An operator carries the mark of its element: the tilde when the element has a scalar part, the arrow when it is pure. The rule, the operator glyphs and the dagger are stated in §*The Operators* of *Conventions in the Biquaternion Universe* and of *Conventions in Mathematics*; the arrowed operators are outside this tilde-only catalogue.

### The Four-Vectors and the Currents

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde P$ | Four-momentum | $i(E/c)e_t+\vec p$ | $\mathbb{M}_-$ | $\tilde P=m\tilde V$; the letter is never generic | 465 |
| $\tilde V$ | Four-velocity | $\gamma(ic\,e_t+\vec v)$ | $\mathbb{M}_-$ | $\langle\tilde V\rangle_{\natural}=-c^2$ | 56 |
| $\tilde J$ | Four-current | $J^\nu e_\nu=ic\rho\,e_t+\vec J$ | $\mathbb{M}_-$ | $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J)=0$; the spatial part $\vec J$ is the current density | 56 |
| $\tilde A$ | Electromagnetic four-potential, abelian gauge connection | $\tilde A=i\phi/c\,e_t+\vec A\in\mathbb{M}_-$ | $\mathbb{M}_-$ | The potential of the minimal-coupling, hydrogen, Klein–Gordon, Hopf, quadrupole and self-dual articles; the tension biquaternion of the electro-gravimagnetic programme | 217 |

### The Fields

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde F$ | Field strength | $i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, scalar part zero | $\mathrm{Vect}(\mathbb{B})$ | Enters $\tilde\nabla\tilde F=-\tilde R$ | 107 |
| $\tilde\Psi$ | Dirac field | $\tilde\Psi_L+\tilde\Psi_R$ | $\mathbb{B}$ | An algebra-valued spinor field, with $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$ | 71 |

### The Observables, the States and the Quantum Objects

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde H$ | General Hermitian observable | $h_0e_t+ih_k\vec e_k$, $h_0,h_k\in\mathbb{R}$ | $\mathbb{M}_+$ | The Born pairing is $\mathrm{Tr}(\tilde\rho\tilde H)$; the tilde belongs to this object only | 225 |
| $\tilde S$ | Spin operators | $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | $\mathbb{M}_+$ | The vector slots of $\mathbb{M}_+$, with the total spin $\tilde S$ of a composite | 95 |

## 2. To be tested

One specific role per entry, not yet verified. The test is one pass over the articles that use the symbol, checking that every use matches the description.

| Symbol | Name | Formula | Note | Articles |
|---|---|---|---|---|
| $\tilde{\mathcal A}$ | Non-abelian gauge connection | $\tilde{\mathcal F}=\tilde\nabla\tilde{\mathcal A}+\tfrac12[\tilde{\mathcal A},\tilde{\mathcal A}]$ | The connection of the Yang–Mills, instanton, anomaly and path-integral articles | 7 |
| $\tilde{\mathcal A}$ | A-field, the dual field strength | $\tilde{\mathcal A}=\sqrt\epsilon\,\vec E+i\sqrt\mu\,\vec H=-i\tilde F$ | A complex three-vector and a biquaternion, not a connection; $D^+\tilde{\mathcal A}+\tilde J=0$ in the electro-gravimagnetic, Maxwell and Lorentz-force articles | 7 |
| $\tilde a$ | Annihilation operator | $\tilde a=\tfrac12(i\vec e_x-\vec e_y)$, $\tilde a^2=0$ | The harmonic-oscillator, Fock-space and quantized-field articles; the letter is also used generically in the scalar-product identities | 57 |
| $\tilde{\mathcal B}$ | Hypercharge field strength | $\tilde{\mathcal B}=\tilde\nabla\tilde B$ | In the electroweak article | 1 |
| $\tilde b$ | Bogoliubov-transformed annihilation operator | $\tilde b=u\tilde a+v\tilde a^{\dagger}$ | The Bogoliubov article; the letter is also a second real quaternion in the pairing $\mathrm{Sc}(\tilde a^{\natural}\tilde b)$ | 22 |
| $\tilde\chi$ | Spinor component | — | A component spinor of the algebra, as in $(\tilde\phi,\tilde\chi)^{\mathsf T}$ | 6 |
| $\tilde D$ | Gauge-covariant derivative | $\tilde D\tilde F=\tilde\nabla\tilde F+i\kappa[\tilde{\mathcal A},\tilde F]$ | The Yang–Mills and instanton articles; also a polynomial $\tilde D(s^2)$ in the Bhabha article | 23 |
| $\tilde\Delta\in\mathbb{M}_-$ | Gauge four-vector | $\delta\tilde E_\mu\mapsto\delta\tilde E_\mu-\partial_\mu\tilde\Delta$ | — | 4 |
| $\tilde{\not D}$ | Slashed Dirac operator | $\tilde{\not D}=\tilde E^\mu D_\mu$ | $\tilde{\not D}^2=\Box_g-\tfrac14R$ | 2 |
| $\tilde E$ | Element of the unitary slice | $\tilde E^{*}\tilde E=e_t$ | The slice $\cong U(2)$; an effect $\tilde E_y=\tilde M_y^{*}\tilde M_y$ | 46 |
| $\tilde{\mathbf E}$ | Normalised electric field | $\tilde{\mathbf E}=\sqrt{\epsilon}\,\vec E$ | A real three-vector | 2 |
| $\tilde\ell$ | Future null four-vector of a pure state | $\tilde\ell=i\tilde\Pi(u)\in\mathbb{M}_-$ | $\langle\tilde\ell\rangle_{\natural}=0$ | 1 |
| $\tilde\epsilon$ | Gauge parameter | $\tilde\Psi_\mu\mapsto\tilde\Psi_\mu+\tilde\nabla_\mu\tilde\epsilon$ | — | 2 |
| $\tilde\varepsilon_+$ | Primitive Hermitian idempotent | $\tilde\varepsilon_+=\tfrac12(e_t+i\vec e_z)$ | $\tilde\varepsilon_+^2=\tilde\varepsilon_+$ | 3 |
| $\tilde\eta$ | Fluctuation field | — | The one-loop fluctuation about the classical background in the Gaussian expansion $S[\tilde\phi+\tilde\eta]$, in the generating-functional, determinant and effective-potential articles | 3 |
| $\tilde{\mathcal F}$ | Non-abelian field strength | $\tilde{\mathcal F}=\tilde\nabla\tilde{\mathcal A}+\tfrac12[\tilde{\mathcal A},\tilde{\mathcal A}]$ | The curvature of the Yang–Mills, instanton, anomaly and path-integral articles; the non-abelian analogue of $\tilde F$ | 5 |
| $\tilde{\mathcal F}$ | Power–force biquaternion | $\tilde{\mathcal F}=-\tilde J\circ\tilde{\mathcal A}'$ | The scalar part is a power density and the vector part a force density; the Lorentz-force and electro-gravimagnetic articles | 5 |
| $\tilde f$ | Conjugate function | $\tilde f=\bar f$ | The conjugate function; a radiation field $\tilde f_{\mathrm{rad}}$ | 3 |
| $\tilde G$ | Algebra-valued Green kernel | $\tilde G=\tilde Q^{\natural}/\lVert\tilde Q\rVert_E^4$ | A function of the algebra | 25 |
| $\tilde{\mathcal G}$ | Gluon field strength | $\tilde{\mathcal G}=\tilde\nabla\tilde G+\tfrac{g_s}{2}[\tilde G,\tilde G]$ | — | 1 |
| $\tilde g$ | Group element | $\tilde g=\exp(\vec\alpha/2)\in\mathbb{H}^{1}_{\mathbb{B}}$ | The adjoint action $\tilde\pi\mapsto\tilde g\tilde\pi\tilde g^{-1}$ of the pion article | 5 |
| $\tilde\Gamma_\mu$ | Connection 1-form | $\tilde\Gamma_\mu\mapsto\tilde\Lambda\tilde\Gamma_\mu\tilde\Lambda^{-1}-(\partial_\mu\tilde\Lambda)\tilde\Lambda^{-1}$ | The curved-spacetime article; the covariant derivative is $D_\mu\tilde Q=\partial_\mu\tilde Q+\tilde\Gamma_\mu\tilde Q+\tilde Q\tilde\Gamma_\mu^{*}$ | 7 |
| $\tilde{\mathbf H}$ | Normalised magnetic field | $\tilde{\mathbf H}=\sqrt{\mu}\,\vec H$ | A real three-vector | 2 |
| $\tilde h$ | Element of the Hermitian half | — | An element of $\mathbb{M}_+$, as in the bracket $[\tilde h,\tilde h']$ | 6 |
| $\tilde j$ | Current density | $\tilde j=\vec j/\sqrt{\epsilon}$ | A normalised current density | 15 |
| $\tilde K$ | Cauchy kernel | — | The kernel of the biquaternion Cauchy integral | 84 |
| $\tilde{\mathcal K}$ | Retarded-time gradient coefficient | $\tilde{\mathcal K}=\tilde{\nabla}^{\natural}t_r=\frac{1}{c\kappa}(\vec u_R-ie_t)$ | — | 1 |
| $\tilde k$ | Wave four-vector | $\tilde k=ik^0e_t+\vec k\in\mathbb{M}_-$ | — | 35 |
| $\tilde\kappa_\epsilon$ | Unitary gate | — | A Hermitian-Pauli gate element | 1 |
| $\tilde L$ | Limit value or an angular-momentum element | $\tilde L_k=L_ke_t$ | The value a function tends to; the angular momentum | 19 |
| $\tilde{\mathbf L}$ | Angular-momentum vector | $\tilde{\mathbf L}=I\tilde{\boldsymbol\omega}$ | — | 1 |
| $\tilde\Lambda$ | Unit-norm element of the dagger sandwich | $X\mapsto\mathsf{M}_2(\tilde\Lambda)X\mathsf{M}_2(\tilde\Lambda)^{\dagger}$ | With $\langle\tilde\Lambda\rangle_{\natural}=1$ | 54 |
| $\tilde M$ | Kraus operator | $\tilde E_y=\tilde M_y^{*}\tilde M_y$ | The Kraus form of an effect | 10 |
| $\tilde m$ | Mass term | $\mathcal{D}=\tilde\nabla+\tilde m$ | The mass term of the biquaternion Dirac operator | 4 |
| $\tilde\mu$ | Magnetic moment | $\tilde\mu=\mu_k\vec e_k$ | The classical magnetic moment, a pure real quaternion | 1 |
| $\tilde{\boldsymbol\mu}$ | Bold form of the magnetic moment | $\tilde{\boldsymbol\mu}=\mu_k\vec e_k$ | The same object as $\tilde\mu$ | 2 |
| $\tilde N$ | Null vector or a number operator | — | A null vector whose ray is a boundary point; $\tilde N_{\mathrm{exc}}$ an excitation number | 18 |
| $\tilde{\mathcal N}$ | Retarded direction | $\tilde{\mathcal N}=\vec u_R-ie_t$ | In the field of a moving charge | 1 |
| $\tilde n$ | Outward unit normal | — | The biquaternion-valued outward unit normal of the Stokes theorem | 6 |
| $\tilde O$ | Observable element | — | An element paired in the trace formula $\mathrm{Tr}(\tilde\rho\tilde O)$ | 1 |
| $\tilde\Omega$ | Angular-velocity biquaternion | $\dot{\tilde\mu}=\tfrac12[\tilde\Omega,\tilde\mu]$ | A Larmor or Rabi element | 5 |
| $\tilde\omega$ | Angular velocity | $\dot{\tilde L}=\tfrac12[\tilde L,\tilde\omega_b]+\tilde\tau$ | A body-frame angular velocity | 7 |
| $\tilde{\boldsymbol\omega}$ | Bold form of the angular velocity | $\tilde{\boldsymbol\omega}=\omega_k\vec e_k$ | The same object as $\tilde\omega$ | 1 |
| $\tilde{\mathcal P}$ | Momentum biquaternion; also a matrix of biquaternions | $\tilde{\mathcal P}=\frac{E}{ic}e_t+\vec p$ | In the zero-divisor article; a generic array in $\mathsf{M}_2(\tilde{\mathcal P}\tilde{\mathcal Q})$ | 3 |
| $\tilde p$ | Canonical momentum | $\tilde p=p_te_t+\vec p$, $\tilde p=\partial L/\partial(d\tilde q/dt)$ | Real quaternion with four components, scalar $p_t$ and vector $\vec p$; the Legendre conjugate of $\tilde q$ | The mechanics and action-units articles; the momentum operator is $\vec p$ | 43 |
| $\tilde{\mathbf p}$ | Bold form of $\tilde p$ in the Euclidean dot product $\mathcal{W}=\tilde{\mathbf p}\cdot\tilde{\mathbf q}$ | — | — | 1 |
| $\tilde\Phi$ | Central algebra-valued scalar field | $\tilde\Phi=\varphi e_t$ | The scalar field of the Klein-Gordon and Higgs articles | 55 |
| $\tilde\phi$ | Field or source variable | $\tilde\Phi=\tilde\phi_-+\tilde\phi_+$ | A module-valued field | 8 |
| $\tilde\varphi$ | Field variable | $\tilde\varphi=\delta W/\delta\tilde J$ | The field of the effective potential | 2 |
| $\tilde\pi$ | Goldstone field | $\tilde\pi=\pi^a e_a\in\mathrm{SU}(2)\subset\mathbb{M}_-$ | The nonlinear sigma model and Skyrme articles; the idempotent is $\tilde\Pi$ | 38 |
| $\tilde\varpi$ | Canonical four-momentum | $\tilde\varpi=\tilde P+ϙ\tilde A$ | The canonical four-momentum | 1 |
| $\tilde\psi$ | Spinor of the state module | — | An element of the minimal left ideal $\mathbb{B}\tilde\Pi_+$ | 9 |
| $\tilde{\mathcal Q}$ | Matrix of biquaternions | $\tilde{\mathcal Q}=e_tQ_t+\vec e_xQ_x+\vec e_yQ_y+\vec e_zQ_z$ | The component writing, with $Q_\mu\in\mathbb{C}^{n\times m}$ | 1 |
| $\tilde{\mathbf q}$ | Bold form of $\tilde q$ in the Euclidean dot product $\mathcal{W}=\tilde{\mathbf p}\cdot\tilde{\mathbf q}$ | — | — | 1 |
| $\tilde R$ | Electric source biquaternion, or a rotation rotor | $\tilde R=\tfrac{i\rho}{\sqrt{\epsilon}}e_t+\sqrt{\mu}\,\vec J$; $\tilde R\tilde R^{\natural}=e_t$ for the rotor | The Maxwell and S-matrix articles; the two roles are to be separated | 219 |
| $\tilde{\mathcal R}$ | Combined electric-magnetic source | $\tilde{\mathcal R}=\tilde R_e+i\tilde R_m$ | — | 5 |
| $\tilde r$ | Position four-vector | $\tilde r=r_\mu\vec e_\mu\in\mathbb{H}_{\mathbb{B}}$ | As in $d\tilde r/dt=\vec\omega_T\times\tilde r$ and in the orbital product $\tilde r\tilde p$ | 19 |
| $\tilde\rho$ | State (density) element | $\tilde\rho=\tfrac12(e_t+i\vec r)$ | A state of the Bloch ball, $\lvert\vec r\rvert\le1$ | 104 |
| $\tilde\varrho$ | State | $\tilde\varrho=\tfrac12(e_t+i\vec r)$ | A state of the sesqualgebra, the ancestor of $\tilde\rho$ | 3 |
| $\tilde{\mathbf S}$ | Spin three-vector | $\tilde{\mathbf S}=S_k\vec e_k$ | A pure real quaternion | 2 |
| $\tilde{\mathcal S}$ | Bell operator | — | A Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$; its image is the CHSH operator | 2 |
| $\tilde s$ | Skew-Hermitian element | — | An element of $\mathbb{M}_-$, the unitary Lie algebra | 4 |
| $\tilde\Sigma$ | Root of $+1$ | $\tilde\Sigma^2=e_t$ | With $\tilde\Pi=\tfrac12(e_t+\tilde\Sigma)$ | 5 |
| $\tilde\sigma$ | State element | — | A second state, as in the relative entropy $S(\tilde\rho\\Vert\tilde\sigma)$ | 13 |
| $\tilde T$ | Kinetic energy | $\tilde T=-\tilde p^{\,2}/(2m)$ | In the free-particle and hydrogen articles | 40 |
| $\tilde\tau$ | Torque | $\dot{\tilde L}_b=\tfrac12[\tilde L_b,\tilde\omega_b]+\tilde\tau$ | The torque of Euler's equation | 1 |
| $\tilde\Upsilon$ | Nilpotent of the biquaternion layer | $\tilde\Upsilon^2=0$ | The quaternion layer writes $\tilde\nu$ | 23 |
| $\tilde{\mathbf V}$ | Pure vector | $\tilde\Omega=\tilde\Omega_0+\tilde{\mathbf V}$ | The vector part in a split such as | 1 |
| $\tilde v$ | Unit four-velocity | $\tilde v=\tilde V/c$ | The four-velocity in units of $c$ | 12 |
| $\tilde W$ | W-boson gauge field | $\tilde W=\sum_a\tilde W^aT^a$ | The electroweak article; its field strength is $\tilde{\mathcal W}=\tilde\nabla\tilde W+\tfrac{g}{2}[\tilde W,\tilde W]$ | 41 |
| $\tilde{\mathcal W}$ | Weak field strength or an energy density | $\tilde{\mathcal W}=\tilde\nabla\tilde W+\tfrac{g}{2}[\tilde W,\tilde W]$ | In the electroweak article; $\tilde{\mathcal W}=\tfrac12\tilde F\tilde F^*$ in the gauge article | 2 |
| $\tilde\xi$ | Root of $1$ of the quaternion layer | $\tilde\xi^2=e_t$ | The tilde-free layers write $\Xi$ | 19 |

## 3. Wrongly generic, to be rewritten

Two kinds of work item are collected here. The first is a **wrongly generic** claim: the entry asserts a generic element outside the Q family. The second is a **wrong scope**: the glyph names a real object, but the tilde does not belong to it. A symbol with a real role also appears in section 2 under that role and here under the defect.

| Symbol | Name | Formula | Note | Fix | Articles |
|---|---|---|---|---|---|
| $\tilde A$ | General element of the algebra | — | A second general element beside $\tilde Q$; also an inner derivation $\mathrm{ad}_{\tilde A}$ | Write $\tilde Q_k$ for the generic use; the potential $\tilde A$ keeps its tilde and is listed in section 1. | 217 |
| $\tilde B$ | General element of the algebra | — | A general element, as in the form $h(\tilde P\tilde B,\tilde R\tilde B)$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 126 |
| $\tilde C$ | General element of the algebra | — | A general element acting on the spinor module, $\mathfrak b_\mu(\tilde C\cdot s,\tilde C\cdot t)$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 46 |
| $\tilde c$ | General element of the quaternion layer | — | A general element of the quaternion layer, as in $L_{\tilde a}L_{\tilde c}=L_{\tilde a\tilde c}$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 12 |
| $\tilde d$ | General element of the quaternion layer | — | A general element beside $\tilde c$, as in $T_{\tilde c,\tilde d}$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 5 |
| $\tilde M$ | General element or a Kraus operator | $\tilde E_y=\tilde M_y^{*}\tilde M_y$ | A general element; the Kraus form of an effect | Write $\tilde Q_k$, or bind the letter where it is introduced. It also hides the Kraus role. | 10 |
| $\tilde p$ | General element of the quaternion layer | — | A general element, as in $L_{\tilde p},R_{\tilde p}$ | Write $\tilde Q_k$, or bind the letter where it is introduced. The corpus also uses the letter for the momentum operator, which is pure and written $\vec p$. | 43 |
| $\tilde R$ | General element or a velocity | — | A general element; the electric source and the rotation rotor | Write $\tilde Q_k$, or bind the letter where it is introduced. Two roles are mixed: electric source and rotation rotor. | 219 |
| $\tilde r$ | General element of the quaternion layer | $\tilde r\mapsto\tilde r^{\natural}$ | A general element; the reflection | Write $\tilde Q_k$, or bind the letter where it is introduced. The corpus also uses it as the position vector. | 19 |
| $\tilde T$ | General element of the algebra | — | A general element; a unit exactly when $\langle\tilde T\rangle_{\natural}\neq0$ | Write $\tilde Q_k$, or bind the letter where it is introduced. The physics articles also use it as the kinetic energy. | 40 |
| $\tilde W$ | General element of the algebra | — | A general element; a basis element of the spinor module | Write $\tilde Q_k$, or bind the letter where it is introduced. The physics articles also use it as the W-boson field. | 41 |
| $\tilde w$ | General element or unit quaternion | $\{L_{\tilde w}:\operatorname{Re}\tilde w=\operatorname{Re}\tilde q\}$ | A general element, as in the class | Write $\tilde Q_k$, or bind the letter where it is introduced. The LSZ article uses it as a constant amplitude. | 3 |
| $\tilde X$ | General element of the algebra | $\{\tilde X:\tilde P\tilde X=0\}$ | A general element, as in the annihilator | Write $\tilde Q_k$, or bind the letter where it is introduced. | 108 |
| $\tilde x$ | General element of the quaternion layer | — | A general element, as in $L_{\tilde x}(\tilde y)=\tilde x\tilde y$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 16 |
| $\tilde Y$ | General element of the algebra | — | A general element of the Peirce and sesqualgebra identities | Write $\tilde Q_k$, or bind the letter where it is introduced. | 90 |
| $\tilde y$ | General element of the quaternion layer | — | A general element, as in the plain form $\langle\tilde x,\tilde y\rangle$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 5 |
| $\tilde Z$ | General element of the algebra | $\{\tilde Z:\tilde P\tilde Z=0\}$ | A general element, as in the annihilator | Write $\tilde Q_k$, or bind the letter where it is introduced. | 43 |
| $\tilde z$ | General element of the quaternion layer | — | A general element paired with $\tilde y$ in the inner product, as in $\langle\tilde y,\tilde z\rangle$ | Write $\tilde Q_k$, or bind the letter where it is introduced. | 2 |
| $\tilde F$ | Placeholder | — | In the identity $\tilde\nabla\tilde F$ the letter stands for an arbitrary algebra-valued field. The letter is the field strength and is never generic | $\tilde\nabla\tilde Q$, or bind the field where it is introduced. | 107 |
| $\tilde H$ | Central Hamiltonian | $\tilde H=\bigl[-\frac{\hbar^2}{2m}\nabla^2+V\bigr]e_t=h_0e_t$ | In the Schrödinger, free-particle and scattering articles. A scalar is central; the tilde is not its mark | Drop the tilde, $H=h_0e_t$. | 225 |
| $\tilde H$ | Oscillator energy | $\tilde H=\omega(\tilde a^{\dagger}\tilde a+\tfrac12e_t)$ | It is Hermitian, but it is not the general Hermitian observable of section 1, and the rule keeps the tilde for that object alone | Drop the tilde, or write the energy as the section 1 observable when the statement is about the observable. | 225 |
| $\tilde H$ | Trace dummy | $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | No object is behind the letter, and the first slot $\tilde P$ is a dummy of the same kind | Write the pairing with the Q family, $\mathrm{Tr}(\tilde Q_1\tilde Q_2)$. | 225 |
| $\tilde P$ | Trace dummy | — | The first slot of the same formula. The letter is the four-momentum and is never generic | $\tilde Q_1$; the four-momentum keeps its tilde where it is the momentum. | 465 |
