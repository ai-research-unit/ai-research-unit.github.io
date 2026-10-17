# __The Most Common Items with a Tilde__

**Scope: tilde glyphs only.** Every symbol in the tables carries a tilde. Four kinds of glyph are outside the scope and are not listed among the allowed uses: a matrix, $I_n$, $\mathsf{M}_2$, $\mathsf{M}_4$; a pure element written with an arrow, $\vec Q$, $\vec q$, $\vec u$, $\vec U$, $\vec\Xi$, $\vec\Upsilon$; a mark that is not an element, $\tilde\cdot$, $\tilde\star$; and every glyph of the reduced, tilde-free layers, $\Pi_\pm$, $\Xi_\pm$, $\Upsilon_\pm$. The first is fixed by the rule that a matrix carries no tilde, §*General Matrix Conventions* of *Conventions in the Biquaternion Universe*; the others are elements of other layers or of no layer at all. The operator section states the rule that pairs the two marks; it is not a catalogue of arrowed glyphs.

The tilde marks a quaternionic factor. The last column of every table is the number of articles in which the symbol occurs, counted over the articles of `articles_maths/` and `articles_physics/` at the last scan. The list is triaged into three sections.

- **1. Allowed tilde** — the role is fixed by *Conventions in the Biquaternion Universe* and checked against the corpus. Cite these entries as they stand. The tables are ordered by theme, as the objects are.
- **2. To be tested** — one specific role, plausible but not yet verified. Test before citing. A symbol that is also wrongly generic keeps its role here and its generic claim in section 3.
- **3. Wrongly generic, to be rewritten** — one line per work item. It covers a generic claim outside the Q family and a tilde on an object that has no right to it. Do not cite.

The governing rule: **only the Q family is generic, and only an element carries the tilde.** $\tilde Q$ is the biquaternion or split-biquaternion element and $\tilde q$ the quaternion or split-quaternion element; numbered variants are allowed. A generic element that is unitary is written $\tilde U$. A letter outside the family names an object, or an element bound where it is introduced. A matrix — the image of an element, an array of biquaternions, or a colour matrix — takes no tilde; a tilde on one is a defect of scope, corrected where it occurs and not catalogued here.

## 1. Allowed tilde

### The Layer Glyphs

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde Q$ | General element of the algebra | $Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $Q_\mu\in\mathbb{C}$ | $\mathbb{B}$ | The only generic glyph; a second and a third are $\tilde Q_1,\tilde Q_2$ | 646 |
| $\tilde q$ | General element of the quaternion layer | $q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, $q_\mu\in\mathbb{R}$ | $\mathbb{H}_{\mathbb{B}}$ | The only generic glyph of that layer; a second is $\tilde q_1$ | 197 |
| $\tilde\Pi$ | Idempotent, projector | $\Pi_te_t+\vec\Pi$, with $\tilde\Pi^2=\tilde\Pi$ | $\mathbb{B}$; $\mathbb{M}_+$ when $\tilde\Pi^{*}=\tilde\Pi$ | A Hermitian idempotent is a pure state; $\mathbb{B}\tilde\Pi$ is the minimal left ideal, the state module | 270 |
| $\tilde\Xi$ | Root of a central value | $\Xi_te_t+\vec\Xi$, with $\tilde\Xi^2=\lambda e_t$, $\lambda$ central | $\mathbb{B}$; $\mathbb{M}_+$ for the roots $i\vec e_k$; $\mathbb{C}_{\mathbb{B}}$ for $\pm i$ | For a root of $1$ the idempotents are $\tfrac12(e_t\pm\tilde\Xi)$ | 57 |
| $\tilde\xi$ | Root of $1$ of the quaternion layer | $\xi_te_t+\vec\xi$, with $\tilde\xi^2=e_t$ | $\mathbb{H}_{\mathbb{B}}$; the split-quaternion layer writes the same glyph | The tilde-free layers write $\Xi$ | 19 |
| $\tilde\nu$ | Nilpotent of the quaternion layer | $\nu_te_t+\vec\nu$, with $\tilde\nu^2=0$ | The null cone, in neither sector | The biquaternion layer writes $\tilde\Upsilon$ | 8 |
| $\tilde\Upsilon$ | Nilpotent of the biquaternion layer | $\Upsilon_te_t+\vec\Upsilon$, with $\tilde\Upsilon^2=0$ | The null cone, in neither sector | The quaternion layer writes $\tilde\nu$ | 23 |
| $\tilde U$ | Norm-one element | $U_te_t+\vec U$, with $\mathrm{Norm}(\tilde U)=e_t$; $\tilde U^{*}\tilde U=e_t$ in the unitary case | $\mathbb{B}$ | The rotor; the unitary group is $\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)$ | 168 |
| $\tilde u$ | Unit quaternion | $\cos(\theta/2)e_t+\sin(\theta/2)\vec u$, $\vec u$ a unit real vector | $\mathbb{H}_{\mathbb{B}}$, norm one | The rotor of $\mathrm{Sp}(1)\cong\mathrm{SU}(2)$; a pure unit quaternion is $\vec u$ | 60 |
| $\tilde U_{\mathrm b}$ | Hermitian positive boost | $\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | $\mathbb{M}_+$, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | The boost factor of the polar word, one exponential, three parameters; it is not unitary under ${}^{*}$, $\tilde U_{\mathrm b}^{*}\tilde U_{\mathrm b}\neq e_t$ | 8 |
| $\tilde u_{\mathrm r}$ | Unit real quaternion rotor | $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\mathbb{H}_{\mathbb{B}}$, norm one | The spatial rotation of the polar word; unitary under every product | 11 |
| $\tilde U_{\mathrm L}$ | Lorentz rotor | $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde U_{\mathrm L}\rangle_{\natural}=1$, $\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$ | The Lorentz transformation: factors $3$ and $4$ of the polar word multiplied, not the boost alone; $\tilde\Lambda$ of the physics articles, $\tilde U_{\mathrm L}$ where $\tilde\Lambda$ is the eigenspinor | 3 |

### The Gradient and the Operators

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde\nabla$ | Biquaternionic gradient | $e_t\,\partial/\partial Q_t+\vec e_x\,\partial/\partial Q_x+\vec e_y\,\partial/\partial Q_y+\vec e_z\,\partial/\partial Q_z$ | Operator, $\mathbb{B}$-valued | Its conjugate $\tilde\nabla^{\natural}=e_t\partial_t-\vec e_k\partial_k$ is the second factor of $\Box$ | 204 |

An operator carries the mark of its element: the tilde when the element has a scalar part, the arrow when it is pure. The rule, the operator glyphs and the dagger are stated in §*The Operators* of *Conventions in the Biquaternion Universe* and of *Conventions in Mathematics*; the arrowed operators are outside this tilde-only catalogue.

### The Four-Vectors and the Currents

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde P$ | Four-momentum | $i(E/c)e_t+\vec p$ | $\mathbb{M}_-$ | $\tilde P=m\tilde V$; the letter is never generic | 464 |
| $\tilde p$ | Canonical momentum quaternion | $\tilde p=p_te_t+\vec p$, $\tilde p=\partial L/\partial(d\tilde q/dt)$ | $\mathbb{H}_{\mathbb{B}}$ | Real quaternion with four components, scalar $p_t$ and vector $\vec p$; the Legendre conjugate of $\tilde q$ | 45 |
| $\tilde V$ | Four-velocity | $\gamma(ic\,e_t+\vec v)$ | $\mathbb{M}_-$ | $\langle\tilde V\rangle_{\natural}=-c^2$ | 56 |
| $\tilde{\mathcal L}$ | Future null four-vector of a pure state | $\tilde{\mathcal L}=i\tilde\Pi(u)\in\mathbb{M}_-$ | $\mathbb{M}_-$ | $\langle\tilde{\mathcal L}\rangle_{\natural}=0$; the scalar part $i/2$ is complex, so the majuscule, §*The Elements and their Coefficients* | 1 |
| $\tilde J$ | Four-current; the Maxwell source; also the Noether current of a continuous symmetry | $J^\nu e_\nu=ic\rho\,e_t+\vec J$, $\langle\tilde\nabla,\tilde J\rangle_{\natural}=0$ | $\mathbb{M}_-$ | $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J)=0$; enters Maxwell as $\sqrt{\mu}\,\tilde J$, so $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$; the spatial part $\vec J$ is the current density. The axial current is $\tilde J_5$; the lowercase form of the letter is not used | 93 |
| $\tilde A$ | Electromagnetic four-potential, abelian gauge connection | $\tilde A=i\phi/c\,e_t+\vec A\in\mathbb{M}_-$ | $\mathbb{M}_-$ | The potential of the minimal-coupling, hydrogen, Klein–Gordon, Hopf, quadrupole and self-dual articles; the tension biquaternion of the electro-gravimagnetic programme | 216 |
| $\tilde K_{\mathrm{ret}}$ | Retarded-time gradient coefficient, also the null retarded gradient | $\tilde K_{\mathrm{ret}}=\tilde\nabla^{\natural}t_r=\frac{1}{c\kappa}(\vec u_R-ie_t)$ | $\mathbb{M}_-$, null | The gradient of the retarded time: $\tilde\nabla^{\natural}\tilde Q=\tilde K_{\mathrm{ret}}\,d\tilde Q/dt_r$ for a source depending on $t_r$ alone. It is a zero divisor, $\langle\tilde K_{\mathrm{ret}}\rangle_{\natural}=0$, so it is null and not unitary at any $\kappa$ | 1 |

$\tilde j$ no longer occurs: the normalised current density it named is the same object as $\sqrt{\mu}\,\tilde J$, and it is written that way. The lowercase letter was a duplicate of $\tilde J$, not a distinct quantity.

### The Fields

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde F$ | Field strength | $i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, scalar part zero | $\mathrm{Vect}(\mathbb{B})$ | Enters $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$ | 109 |
| $\tilde\Psi$ | Dirac field | $\tilde\Psi_L+\tilde\Psi_R$ | $\mathbb{B}$ | An algebra-valued spinor field, with $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$ | 70 |

### The Observables, the States and the Quantum Objects

| Symbol | Name | Formula | Space | Meaning | Articles |
|---|---|---|---|---|---|
| $\tilde{Ϛ}$ | State (density) element | $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$, $\lvert\vec r\rvert\le1$ | $\mathbb{M}_+$ | The state of the Bloch ball: Hermitian, positive, $\mathrm{Tr}(\tilde{Ϛ})=1$. The glyph is the upper-case stigma, U+03DA, because the majuscule of rho is the four-momentum $\tilde P$; the older rho and varrho spellings are retired. Its matrix image $\mathsf{M}_2(\tilde{Ϛ})$ carries no tilde | 105 |
| $\tilde H$ | General Hermitian observable | $h_0e_t+ih_k\vec e_k$, $h_0,h_k\in\mathbb{R}$ | $\mathbb{M}_+$ | The Born pairing is $\mathrm{Tr}(\tilde{Ϛ}\tilde H)$; the tilde belongs to this object only | 223 |
| $\tilde S$ | Spin operators | $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | $\mathbb{M}_+$ | The vector slots of $\mathbb{M}_+$, with the total spin $\tilde S$ of a composite | 94 |
| $\tilde E$ | Effect of a measurement | $0\le\tilde E\le e_t$, $\tilde E\in\mathbb{M}_+$; $\tilde E_y=\tilde K_y^{*}\tilde K_y$ | $\mathbb{M}_+$ | The outcome of a POVM; a rank-one effect is the idempotent $\tilde\Pi$ | 41 |
| $\tilde K$ | Kraus operator of an instrument | $\tilde E_y=\tilde K_y^{*}\tilde K_y$, $\tilde K_y\in\mathbb{B}$; $\sum_y\tilde K_y^{*}\tilde K_y=e_t$ | $\mathbb{B}$ | The measurement operator of outcome $y$; the principal square root has $\mathrm{Sc}(\tilde K_y)>0$ and is never pure. The channel and dephasing articles write $\tilde K_l$. The same glyph is also the central kernel of the functional integral and the force biquaternion of the Lorentz-force article; those uses are bound. The retarded-time gradient is the subscripted $\tilde K_{\mathrm{ret}}$ of §*The Four-Vectors and the Currents* | 85 |

## 2. To be tested

One specific role per entry, not yet verified. The test is one pass over the articles that use the symbol, checking that every use matches the description. A glyph whose uses are all bound but span several roles is listed separately at the end of the section, with the pass recorded.

| Symbol | Name | Formula | Note | Articles |
|---|---|---|---|---|
| $\tilde\chi$ | Spinor component | — | A component spinor of the algebra, as in $(\tilde\phi,\tilde\chi)^{\mathsf T}$ | 6 |
| $\tilde D$ | Gauge-covariant derivative | $\tilde D\tilde F=\tilde\nabla\tilde F+i\kappa[\mathcal A,\tilde F]$ | The Yang–Mills and instanton articles; also a polynomial $\tilde D(s^2)$ in the Bhabha article | 24 |
| $\tilde\Delta\in\mathbb{M}_-$ | Gauge four-vector | $\delta\tilde E_\mu\mapsto\delta\tilde E_\mu-\partial_\mu\tilde\Delta$ | — | 4 |
| $\tilde{\not D}$ | Slashed Dirac operator | $\tilde{\not D}=\tilde E^\mu D_\mu$ | $\tilde{\not D}^2=\Box_g-\tfrac14R$ | 2 |
| $\tilde{\mathcal F}$ | Non-abelian field strength | $\tilde{\mathcal F}=\tilde\nabla\mathcal A+\tfrac12[\mathcal A,\mathcal A]$ | The curvature of the Yang–Mills, instanton, anomaly and path-integral articles; the non-abelian analogue of $\tilde F$ | 5 |
| $\tilde{\mathcal F}$ | Power–force biquaternion | $\tilde{\mathcal F}=i\tilde J_{\mathrm{eg}}\circ\tilde F'$ | The scalar part is a power density and the vector part a force density; the Lorentz-force and electro-gravimagnetic articles | 5 |
| $\tilde J_{\mathrm{eg}}$ | Combined electric–magnetic charge–current | $\tilde J_{\mathrm{eg}}=i\rho+\vec J$ | The electro-gravimagnetic programme; not the corpus four-current $\tilde J$ | 5 |
| $\tilde g$ | Group element | $\tilde g=\exp(\vec\alpha/2)\in\mathbb{H}^{1}_{\mathbb{B}}$ | The adjoint action $\tilde\pi\mapsto\tilde g\tilde\pi\tilde g^{-1}$ of the pion article | 5 |
| $\tilde\Gamma_\mu$ | Connection 1-form | $\tilde\Gamma_\mu\mapsto\tilde\Lambda\tilde\Gamma_\mu\tilde\Lambda^{-1}-(\partial_\mu\tilde\Lambda)\tilde\Lambda^{-1}$ | The curved-spacetime article; the covariant derivative is $D_\mu\tilde Q=\partial_\mu\tilde Q+\tilde\Gamma_\mu\tilde Q+\tilde Q\tilde\Gamma_\mu^{*}$ | 7 |
| $\tilde\Lambda$ | Unit-norm element of the dagger sandwich | $X\mapsto\mathsf{M}_2(\tilde\Lambda)X\mathsf{M}_2(\tilde\Lambda)^{\dagger}$ | With $\langle\tilde\Lambda\rangle_{\natural}=1$ | 54 |
| $\tilde m$ | Mass term | $\mathcal{D}=\tilde\nabla+\tilde m$ | The mass term of the biquaternion Dirac operator | 4 |
| $\tilde\mu$ | Magnetic moment | $\tilde\mu=\mu_k\vec e_k$ | The classical magnetic moment, a pure real quaternion | 1 |
| $\tilde N$ | Null vector on a boundary ray | $g(\tilde N,\tilde N)=0$, $\xi=[\tilde N]$ | One role only: the null vector of *Split-Biquaternions and Hyperbolic Geometry*, whose ray is a point of $\partial H^3$ and whose normalisation is fixed in the notation row of that article | 1 |
| $\tilde N$ | Number operator | $\tilde N=\tilde a^\dagger\tilde a$ | The algebra number operator of the oscillator and Fock articles, with the truncation $\tilde N_{\mathrm{tr}}=\tfrac12(e_t-i\vec e_z)$ and the Tavis–Cummings excitation number $\tilde N_{\mathrm{exc}}=a^\dagger a+\tilde J_3/\hbar+N/2$. Bound where introduced, never a free element | 15 |
| $\tilde{\mathcal N}$ | Retarded direction | $\tilde{\mathcal N}=\vec u_R-ie_t$ | In the field of a moving charge | 1 |
| $\tilde n$ | Outward unit normal | — | The biquaternion-valued outward unit normal of the Stokes theorem | 6 |
| $\tilde\omega$ | Angular velocity or its generator | $d\tilde\mu/dt=\tfrac12[\tilde\mu,\tilde\omega_L]$ | An angular velocity or the generator of a precession | 6 |
| $\tilde\Phi$ | Central algebra-valued scalar field | $\tilde\Phi=\varphi e_t$ | The scalar field of the Klein-Gordon and Higgs articles; complex scalar sector, hence the majuscule. The fluctuation about it is $\delta\tilde\Phi$, in the generating-functional, determinant and effective-potential articles | 53 |
| $\tilde\phi$ | Field or source variable | $\tilde\Phi=\tilde\phi_-+\tilde\phi_+$ | A module-valued field | 8 |
| $\tilde\varphi$ | Field variable | $\tilde\varphi=\delta W/\delta\tilde J$ | The field of the effective potential | 2 |
| $\tilde\pi$ | Goldstone field | $\tilde\pi=\pi^a e_a\in\mathrm{SU}(2)\subset\mathbb{M}_-$ | The nonlinear sigma model and Skyrme articles; the idempotent is $\tilde\Pi$ | 38 |
| $\tilde\psi$ | Spinor of the state module | — | An element of the minimal left ideal $\mathbb{B}\tilde\Pi_+$ | 9 |
| $\tilde{\mathcal R}$ | Combined electric-magnetic source | $\tilde{\mathcal R}=\sqrt{\mu}\,\tilde J_e+i\sqrt{\epsilon}\,\tilde J_m$ | — | 5 |
| $\tilde r$ | Position four-vector | $\tilde r=r_\mu\vec e_\mu\in\mathbb{H}_{\mathbb{B}}$ | As in $d\tilde r/dt=\vec\omega_T\times\tilde r$ and in the orbital product $\tilde r\tilde p$ | 19 |
| $\tilde{\mathcal S}$ | Bell operator | — | A Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$; its image is the CHSH operator | 2 |
| $\tilde s$ | Skew-Hermitian element | — | An element of $\mathbb{M}_-$, the unitary Lie algebra | 4 |
| $\tilde\Sigma$ | Root of $+1$ | $\tilde\Sigma^2=e_t$ | With $\tilde\Pi=\tfrac12(e_t+\tilde\Sigma)$ | 5 |
| $\tilde\sigma$ | State element | — | A second state, as in the relative entropy $S(\tilde{Ϛ}\\Vert\tilde\sigma)$ | 13 |
| $\tilde W$ | W-boson gauge field | $\tilde W=\sum_a\tilde W^aT^a$ | The electroweak article; the generators $T^a=\tfrac12e_a$ are algebra elements, so the gauge field is an element and not a matrix; its field strength is $\tilde{\mathcal W}=\tilde\nabla\tilde W+\tfrac{g}{2}[\tilde W,\tilde W]$ | 42 |
| $\tilde{\mathcal W}$ | Weak field strength or an energy density | $\tilde{\mathcal W}=\tilde\nabla\tilde W+\tfrac{g}{2}[\tilde W,\tilde W]$ | In the electroweak article; $\tilde{\mathcal W}=\tfrac12\tilde F\tilde F^*$ in the gauge article | 2 |

The wave four-vector and the unit four-velocity are written $\tilde P/\hbar$ and $\tilde V/c$. Each is a quotient of an object already in the list, so neither takes a glyph of its own, and the rows that stood for them are removed.

$\tilde\tau$ no longer occurs: its one use was the pure torque of *Rigid-Body Dynamics and the Biquaternion Rotor*, now written $\vec\tau$.

### The Bound Roles of $\tilde R$

$\tilde R$ is not a generic glyph. After the electric-source role was removed, its uses are bound where the letter is introduced, and they fall into two roles that do not co-occur in one article.

| Role | Formula | Occurrences | Articles |
|---|---|---|---|
| Rotation rotor | $\tilde R=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\vec u_{\mathrm r}\cdot\mathbf e$, $\tilde R\tilde R^{\natural}=e_t$ | 372 | 16 |
| Bound element at the point of use | $\tilde P,\tilde Q,\tilde R$ in a ternary identity; $h(\tilde P,\tilde R)$; a unit in $\operatorname{H}_{\tilde R}$ | 2629 | 163 |

The token counts are over `articles_maths/` and `articles_physics/`; the article counts are the articles in which the symbol occurs, whether or not they display the defining formula. The two rows account for all 3001 tokens in 179 articles.

**The electric source is written with $\tilde J$, not $\tilde R$.** The Maxwell source is the four-current $\tilde J=ic\rho\,e_t+\vec J$, and the field equation reads $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$. Since $c=1/\sqrt{\epsilon\mu}$,
$$
\sqrt{\mu}\,\tilde J=\sqrt{\mu}\left(ic\rho\,e_t+\vec J\right)=\frac{i\rho}{\sqrt{\epsilon}}e_t+\sqrt{\mu}\,\vec J ,
$$
so the normalised combination $i\rho/\sqrt{\epsilon}\,e_t+\sqrt{\mu}\,\vec J$ is $\sqrt{\mu}\,\tilde J$, not a second object. The factor $\sqrt{\mu}$ is the whole difference, and it is written explicitly in every article. In a magnetic medium the magnetic source is $\sqrt{\epsilon}\,\tilde J_m$. No article of the corpus now writes $\tilde R$ for a source.

**The rotation rotor is a unit real quaternion**, the $SU(2)$ factor of $\tilde S=\exp(i\theta)\tilde R$ in *The S-Matrix in Biquaternionic Form*; the generic unit quaternion of that layer is $\tilde u$, and the rotor is that object bound to a rotation.

**The second role is a bound element, not a generic one.** In the algebra articles $\tilde R$ is the third multiplicand beside $\tilde P$ and $\tilde Q$, or a unit in a sandwich, bound where it is introduced. The generic element is $\tilde Q_k$.

### A Removed Glyph

The discarded limit glyph no longer occurs in any article. The last use was the value a limit tends to; that value is an arbitrary element, so it belongs to the Q family and is now $\tilde Q_2$, with $\tilde Q_3$ for the second limit in the uniqueness proof and the algebra of limits. The logarithm value is $\tilde Q_{\log}$ ($17$ places, $4$ articles). The Lorentz rotor is $\tilde\Lambda$ in *The Lorentz Transformation as a Biquaternionic Rotation* and $\tilde U_{\mathrm L}$ in *The Eigenspinor*, where $\tilde\Lambda$ is the eigenspinor itself. The Lindblad jump operators are $\tilde K_k$ ($10$ places, $1$ article). The orbital operators are $L_k e_t$ ($75$ places, $3$ articles).

The quaternion-layer logarithm is $\tilde q_{\log}$ ($16$ places, $1$ article), the same symbol as the biquaternion layer. The body-frame angular momentum of *Rigid-Body Dynamics and the Biquaternion Rotor*, $37$ places, is a pure real quaternion and is now written $\vec L_b$; the same pass made that article's angular velocity and torque $\vec\omega_b$ and $\vec\tau$, since they are pure as well. The left-inverse dummy of *Norm and Invertibility in the General Quaternionic Algebra* is now $\tilde Q_3$. The generic uses — the bilinearity dummy of *The Born Rule as a Trace Formula*, the general identity of *Biquaternion Elementary Functions*, and the periodicity statement of *Split-Biquaternion Spectral Theory* — were rewritten to $\tilde Q$. The Noether bivector is pure and is now written $\vec L$; the field strength $\tilde F$ is pure as well and still carries a tilde, so that pair differs in mark and the field strength is the remaining work item of the pair.

## 3. Wrongly generic, to be rewritten

Two kinds of work item are collected here. The first is a **wrongly generic** claim: the entry asserts a generic element outside the Q family. The second is a **wrong scope**: the glyph names a real object, but the tilde does not belong to it. A symbol with a real role also appears in section 2 under that role and here under the defect.

| Symbol | Name | Formula | Note | Fix | Articles |
|---|---|---|---|---|---|
| $\tilde A$ | General element of the algebra | — | A second general element beside $\tilde Q$; also an inner derivation $\mathrm{ad}_{\tilde A}$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$ for the generic use; the potential $\tilde A$ keeps its tilde and is listed in section 1. | 216 |
| $\tilde B$ | General element of the algebra | — | A general element, as in the form $h(\tilde P\tilde B,\tilde R\tilde B)$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 125 |
| $\tilde C$ | General element of the algebra | — | A general element acting on the spinor module, $\mathfrak b_\mu(\tilde C\cdot s,\tilde C\cdot t)$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 46 |
| $\tilde a$ | Annihilation operator | $\tilde a=\tfrac12(i\vec e_x-\vec e_y)$, $\tilde a^2=0$ | A Fock operator carries the superscript $\mathrm{fop}$ and no tilde; its one-mode truncation as an element is the pure nilpotent $\vec\Upsilon_x$ | Write $a^{\mathrm{fop}}$ for the abstract operator and $\vec\Upsilon_x$ for the element; a bound real quaternion with a scalar part keeps its tilde. | 54 |
| $\tilde c$ | General element of the quaternion layer | — | A general element of the quaternion layer, as in $L_{\tilde a}L_{\tilde c}=L_{\tilde a\tilde c}$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 12 |
| $\tilde d$ | General element of the quaternion layer | — | A general element beside $\tilde c$, as in $T_{\tilde c,\tilde d}$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 5 |
| $\tilde M$ | General element in the Hadamard scheme | $\tilde M=M_0e_t+\dots+M_3\vec e_z$ | Two generic multiplicands beside the fixed corner products; *The Computational Cost of Biquaternion Arithmetic* now writes them $\tilde Q_1,\tilde Q_2$ | Write $\tilde Q_1,\tilde Q_2$; the bound uses (Thomas interval rotor, limit value, conjugating element) are not generic. | 8 |
| $\tilde p$ | General element of the quaternion layer | — | A general element, as in $L_{\tilde p},R_{\tilde p}$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. The corpus also uses the letter for the momentum operator, which is pure and written $\vec p$. | 45 |
| $\tilde R$ | General element or a velocity | — | A general element; the bound roles are the rotation rotor and the third multiplicand beside $\tilde P,\tilde Q$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. See §*The Bound Roles of $\tilde R$* for the two bound roles. | 179 |
| $\tilde r$ | General element of the quaternion layer | $\tilde r\mapsto\tilde r^{\natural}$ | A general element; the reflection | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. The corpus also uses it as the position vector. | 19 |
| $\tilde T$ | General element of the algebra | — | A general element; a unit exactly when $\langle\tilde T\rangle_{\natural}\neq0$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. The physics articles also use it as the kinetic energy, listed in the next row. | 40 |
| $\tilde T$ | Kinetic energy | $\tilde T=-\tilde p^{\,2}/(2m)=p^{\,2}/(2m)e_t$ | In the free-particle and hydrogen articles. The object is central, a multiple of $e_t$: the square of the pure momentum is scalar, so no quaternionic factor is left for the tilde to mark | Drop the tilde, $T=-\tilde p^{\,2}/(2m)=p^{\,2}/(2m)e_t$. | 40 |
| $\tilde W$ | General element of the algebra | — | A general element; a basis element of the spinor module | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. The physics articles also use it as the W-boson field. | 42 |
| $\tilde w$ | General element or unit quaternion | $\{L_{\tilde w}:\operatorname{Re}\tilde w=\operatorname{Re}\tilde q\}$ | A general element, as in the class | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$; write $\tilde U$ when the element is unitary. The LSZ article uses it as a constant amplitude. | 3 |
| $\tilde X$ | General element of the algebra | $\{\tilde X:\tilde P\tilde X=0\}$ | A general element, as in the annihilator | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 110 |
| $\tilde x$ | General element of the quaternion layer | — | A general element, as in $L_{\tilde x}(\tilde y)=\tilde x\tilde y$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 16 |
| $\tilde Y$ | General element of the algebra | — | A general element of the Peirce and sesqualgebra identities | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 90 |
| $\tilde y$ | General element of the quaternion layer | — | A general element, as in the plain form $\langle\tilde x,\tilde y\rangle$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 5 |
| $\tilde Z$ | General element of the algebra | $\{\tilde Z:\tilde P\tilde Z=0\}$ | A general element, as in the annihilator | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 43 |
| $\tilde z$ | General element of the quaternion layer | — | A general element paired with $\tilde y$ in the inner product, as in $\langle\tilde y,\tilde z\rangle$ | Write $\tilde Q$, $\tilde Q_1$ or $\tilde Q_2$, or bind the letter where it is introduced. | 2 |
| $\tilde F$ | Placeholder | — | In the identity $\tilde\nabla\tilde F$ the letter stands for an arbitrary algebra-valued field. The letter is the field strength and is never generic | $\tilde\nabla\tilde Q$, or bind the field where it is introduced. | 109 |
| $\tilde H$ | Central Hamiltonian | $\tilde H=\bigl[-\frac{\hbar^2}{2m}\nabla^2+V\bigr]e_t=h_0e_t$ | In the Schrödinger, free-particle and scattering articles. A scalar is central; the tilde is not its mark | Drop the tilde, $H=h_0e_t$. | 223 |
| $\tilde H$ | Oscillator energy | $\tilde H=\omega(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}+\tfrac12e_t)$ | It is Hermitian, but it is not the general Hermitian observable of section 1, and the rule keeps the tilde for that object alone | Drop the tilde, or write the energy as the section 1 observable when the statement is about the observable. | 223 |

The trace dummy is resolved: the general identity is written $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$ and the pairing $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ across the corpus. The physical pairing of a state and a Hamiltonian, $\mathrm{Tr}(\tilde P\tilde H)=\langle u|H|u\rangle$, keeps its letters.
