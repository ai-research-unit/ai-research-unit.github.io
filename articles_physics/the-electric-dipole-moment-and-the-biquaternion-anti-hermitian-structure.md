# __The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure__

## Introduction

An **electric dipole moment** (EDM) is a permanent separation of charge along the spin axis of a particle. For a spin-$\tfrac12$ particle the interaction is

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}\,d\;\bar{\psi}\,\sigma^{\mu\nu}\gamma_5\,\psi\;F_{\mu\nu},
\qquad
H_{\mathrm{NR}} = -\,d\,\mathbf{E}\cdot\boldsymbol{\sigma},
$$

so that the particle gains an energy in an electric field that depends on the orientation of its spin. The EDM is the coefficient $d$; it has the dimensions of $e\cdot\mathrm{length}$ and it is the canonical **CP-odd** observable of a spin-$\tfrac12$ system. Its measurement is a search for physics beyond the Standard Model, and its present bounds are among the tightest in particle physics.

The biquaternion framework makes a structural statement about the EDM operator that is the subject of this article. The insertion $\sigma^{\mu\nu}\gamma_5$ is **anti-Hermitian** in the field components that couple to $\mathbf{E}$, and it therefore belongs to the framework's material, anti-Hermitian sector $\mathbb{M}_-$; the magnetic-moment insertion $\sigma^{\mu\nu}$, which couples to $\mathbf{B}$, is Hermitian and belongs to the informational sector $\mathbb{M}_+$. The two are Hodge duals of each other, and the Hermiticity flips under the duality. The article establishes this and states what it does and does not buy.

- **Established, and recomputed below.** The Hermiticity of the insertions, the Hodge duality $\sigma^{\mu\nu}\gamma_5=\tfrac{i}{2}\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma}$, and the resulting sector placement. The $\mathbf{E}$-coupling insertion $\sigma^{0k}\gamma_5$ is anti-Hermitian (recomputed), hence material; the $\mathbf{B}$-coupling insertion $\sigma^{ij}$ is Hermitian, hence informational. The EDM Lagrangian is Hermitian because the explicit $i$ compensates the anti-Hermiticity, and that $i$ is the framework's marker of the CP-odd coefficient.
- **Standard, transcribed.** The definition of the EDM, its $\mathbf{P}$-, $\mathbf{T}$-, and $\mathbf{CP}$-odd character, the nonrelativistic limit, the form-factor decomposition of the electromagnetic vertex, the Standard Model prediction (CKM-suppressed and tiny), the $\theta$-term contribution, and the experimental bounds are standard. They are stated in the framework's notation.
- **Gap, left visible.** The framework supplies the operator and its sector, and it does not supply the coefficient. It has no CP-violating phase of its own, no mechanism to generate one, and no prediction for the electron, neutron, or proton EDM. The value of $d$ is an empirical input, and the framework's statement is the structural one: a nonzero EDM is the presence of a coefficient on an anti-Hermitian, material-sector insertion.

The article is organised as follows. A section defines the EDM operator and its discrete symmetries. A section establishes the anti-Hermitian structure and the Hodge duality. A section gives the form-factor decomposition and contrasts the EDM with the magnetic moment. A section treats the origin of the CP-odd phase. A section collects the bounds and the scales they probe. A closing section separates what is supplied, transcribed, and missing.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The Dirac module is $\Delta=S\oplus\bar{S}$ with $S=\mathbb{C}^2=(\tfrac12,0)$, $\bar{S}=(0,\tfrac12)$, and

$$
\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\quad
\gamma^k=\begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},\quad
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\quad g=\mathrm{diag}(+1,-1,-1,-1),
$$

with $\gamma_5=i\omega$, $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$, and $\sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$. The field strength is $F_{0i}=E_i$, $F_{ij}=-\epsilon_{ijk}B_k$, and $\epsilon^{0123}=+1$; indices are raised and lowered with $g$, so that $\sigma_{\rho\sigma}=g_{\rho\mu}g_{\sigma\nu}\sigma^{\mu\nu}$. The mass terms are the linear Dirac pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$ (not a conjugation), and the antilinear real structure $\flat=-\dagger$ is a separate object. Natural units $\hbar=c=1$ are used, and the EDM unit conversion is $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$.

The framework results used here are those of the companion articles:

- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the Dirac module and the bilinears built on it.
- Companion article *The Dirac Algebra and Biquaternions — A Dictionary*, for the identification of the Clifford generators with the biquaternion basis.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the mass-term conventions and the real structure $\flat$.
- Companion article *The Proton in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.
- Companion article *The Neutron in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.

## The EDM Operator and Its Discrete Symmetries

**The interaction.** The EDM is a CP-odd coupling of the electromagnetic field strength to the spin. Its Lorentz-covariant form and the nonrelativistic Hamiltonian are

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}\,d\,\bar{\psi}\sigma^{\mu\nu}\gamma_5\psi F_{\mu\nu},
\qquad
H_{\mathrm{NR}} = -\,d\,\mathbf{E}\cdot\boldsymbol{\sigma},
$$

where $\boldsymbol{\sigma}$ are the Pauli matrices acting on the spin and the coefficient $d$ is the EDM. The explicit $i$ is required for a Hermitian Lagrangian, and it is the first appearance of the article's central point: the insertion is anti-Hermitian, and the coefficient must be multiplied by $i$ to give a real (Hermitian) interaction.

**Discrete symmetries.** Under parity $\mathbf{P}$, the electric field is a vector ($\mathbf{E}\to-\mathbf{E}$) and the spin is a pseudovector ($\boldsymbol{\sigma}\to+\boldsymbol{\sigma}$), so $\mathbf{E}\cdot\boldsymbol{\sigma}\to-\mathbf{E}\cdot\boldsymbol{\sigma}$: the EDM term is $\mathbf{P}$-odd. Under time reversal $\mathbf{T}$, the electric field is $\mathbf{T}$-even and the spin is $\mathbf{T}$-odd, so the term is again odd. Under $\mathbf{C}$ the term is even. Hence the EDM is $\mathbf{P}$- and $\mathbf{T}$-odd, and by the CPT theorem it is $\mathbf{CP}$-odd: a nonvanishing $d$ requires a source of CP violation. The magnetic-moment term, $-\boldsymbol{\mu}\cdot\mathbf{B}$, is $\mathbf{P}$-even and $\mathbf{T}$-even, and the contrast is exact: the two operators differ by the presence of $\gamma_5$, which is the chirality operator and the source of the parity and CP properties.

**The dimension and the size.** The EDM has the dimensions of electric charge times length. In natural units, $d$ is dimensionless times a length, i.e. $[\mathrm{GeV}^{-1}]$; the conversion is $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$. For a fermion of mass $m_f$ and a new-physics scale $\Lambda$, the standard dimensional estimate of a CP-violating contribution is

$$
d \sim \frac{e\,m_f}{\Lambda^2}\,\sin\varphi ,
$$

where $\varphi$ is the CP-odd phase. The estimate is the one that governs the reach of the experiments: the smaller the bound, the larger the scale probed, and the heavier the fermion, the larger the contribution. The numbers are used in the last section.

**The observable.** A permanent EDM precesses in an electric field, and the precession is what the experiments measure — in atoms and molecules, in stored neutrons, and in storage rings. The observable is the coefficient of $\mathbf{E}\cdot\boldsymbol{\sigma}$, and it is the only renormalisable CP-odd coupling of a spin-$\tfrac12$ particle to the electromagnetic field up to dimension five. The framework's proton and neutron articles treat those composites and note that the framework supplies no value for their EDMs; this article treats the operator and its structure.

## The Anti-Hermitian Structure of $\sigma^{\mu\nu}\gamma_5$

**The Hermiticity of the insertions.** With the block representation and $g=\mathrm{diag}(+1,-1,-1,-1)$, the generators of the Lorentz algebra split into the boosts and the rotations,

$$
\sigma^{0k} = \text{(anti-Hermitian)},\qquad \sigma^{ij} = \text{(Hermitian)},
$$

and the chirality insertion flips the two,

$$
\sigma^{0k}\gamma_5 = \text{(anti-Hermitian)},\qquad \sigma^{ij}\gamma_5 = \text{(Hermitian)}.
$$

Both statements were recomputed in the block basis. The pattern is the standard one: $\gamma^0$ is Hermitian and $\gamma^k$ anti-Hermitian; the boost generators $\sigma^{0k}$ therefore change sign under Hermitian conjugation while the rotation generators $\sigma^{ij}$ do not, and $\gamma_5$, being Hermitian and anticommuting with the $\gamma^\mu$, conjugates the same way as $\gamma_5^2$ would suggest. **The $\mathbf{E}$-coupling insertion is the anti-Hermitian one.**

**The Hodge duality.** The two families of insertions are dual to each other. In terms of the totally antisymmetric symbol,

$$
\sigma^{\mu\nu}\gamma_5 = \frac{i}{2}\,\epsilon^{\mu\nu\rho\sigma}\,\sigma_{\rho\sigma},
\qquad\text{i.e.}\qquad
\tilde{\sigma}^{\mu\nu}:=\tfrac12\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma} = -\,i\,\sigma^{\mu\nu}\gamma_5 ,
$$

an identity that was recomputed for all pairs $(\mu,\nu)$ with residual exactly zero. The duality exchanges the electric and magnetic components: $\sigma^{0k}\gamma_5$ is dual to a combination of the $\sigma^{ij}$, and vice versa. Since the duality factor is $i$, it exchanges Hermitian with anti-Hermitian, which is exactly the flip recorded above.

**The sector placement.** The even Clifford algebra generated by the products of pairs of $\gamma$'s — the unit, the $\sigma^{\mu\nu}$, and $\gamma_5$ — is isomorphic to the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, and under this isomorphism the framework's sector split is the Hermiticity split: Hermitian generators lie in the informational sector $\mathbb{M}_+$ and anti-Hermitian generators in the material sector $\mathbb{M}_-$. The dictionary is that of the companion articles. Applied to the insertions:

| Insertion | Couples to | Hermiticity | Sector |
|---|---|---|---|
| $\sigma^{0k}$ | $\mathbf{E}$ (the boost part of the Pauli term) | anti-Hermitian | $\mathbb{M}_-$ |
| $\sigma^{0k}\gamma_5$ | $\mathbf{E}$ (the EDM) | anti-Hermitian | $\mathbb{M}_-$ |
| $\sigma^{ij}$ | $\mathbf{B}$ (the magnetic moment) | Hermitian | $\mathbb{M}_+$ |
| $\sigma^{ij}\gamma_5$ | $\mathbf{B}$ (the CP-odd partner) | Hermitian | $\mathbb{M}_+$ |

The EDM insertion is therefore the anti-Hermitian, material-sector insertion, and the magnetic-moment insertion is its Hermitian, informational-sector dual. This is the article's central structural statement; it was verified entry by entry in the block basis.

**The dictionary form of the EDM insertion.** The placement can be made exact rather than a Hermiticity match. Under the dictionary that carries the biquaternion basis to the Clifford generators, $e_1\mapsto\gamma^2\gamma^3$, $e_2\mapsto\gamma^3\gamma^1$, $e_3\mapsto\gamma^1\gamma^2$, the EDM insertion *is* the image of a basis element of the material sector:

$$
\sigma^{0k}\gamma_5 = -\Phi(e_k) = \Phi(-e_k), \qquad -e_k \in \mathbb{M}_- ,
$$

verified for $k=1,2,3$ with residual exactly zero. The EDM insertion is thus not merely anti-Hermitian and therefore material; up to a sign it is the Clifford image of one of the three vector basis elements $e_k$ of $\mathbb{M}_-$ — the same elements that carry the spatial directions of the material sector. The magnetic insertion corresponds to the informational element $ie_k$, and since multiplication by the central $i$ exchanges the sectors, $i\mathbb{M}_-=\mathbb{M}_+$, the same $e_k$ appears on both sides of the table. The correspondence is a statement about the objects the insertion represents, in the sense of the convention that reads the sectors on the fields; the sectors are real vector spaces on which the algebra acts rather than subalgebras, and a general element of the even Clifford algebra need not fall in one of them.

**The $i$ and the Hermiticity of the Lagrangian.** Because the EDM insertion is anti-Hermitian, the bilinear $\bar{\psi}\sigma^{0k}\gamma_5\psi$ is anti-Hermitian as a classical bilinear, and the Lagrangian density $-\tfrac{i}{2}d\,\bar{\psi}\sigma^{\mu\nu}\gamma_5\psi F_{\mu\nu}$ is Hermitian for real $d$ precisely because the explicit $i$ makes $i\times(\text{anti-Hermitian})$ Hermitian. The magnetic-moment Lagrangian has no such $i$, because its insertion is already Hermitian. **The factor of $i$ is the biquaternion signature of the EDM**: the operator is the CP-odd member of a dual pair, its material-sector placement is the anti-Hermiticity, and the Hermiticity of the action is restored by the central imaginary.

## The Nonrelativistic Reduction

**From the covariant operator to $-d\,\mathbf{E}\cdot\boldsymbol{\sigma}$.** The EDM coupling reduces to the nonrelativistic Hamiltonian by an identity that the block basis makes explicit. In the Dirac representation the spin operator is

$$
\Sigma^k = \mathrm{diag}(\sigma^k,\sigma^k),\qquad (\Sigma^k)^\dagger=\Sigma^k,\qquad
\sigma^{0k}\gamma_5 = i\,\Sigma^k ,
$$

which was verified entry by entry: $\sigma^{01}\gamma_5 = i\,\mathrm{diag}(\sigma^1,\sigma^1)$, and similarly for the other two components. The identity shows both facts at once — that $\sigma^{0k}\gamma_5$ is $i$ times a Hermitian matrix (hence anti-Hermitian), and that the matrix it multiplies is the spin.

Substituting into the Lagrangian, with $F_{0k}=E_k$ and the sum over $k$,

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}d\,\bar{\psi}\sigma^{\mu\nu}\gamma_5\psi F_{\mu\nu}
\supset -\,i\,d\,E_k\,\bar{\psi}\sigma^{0k}\gamma_5\psi
= -\,i\,d\,E_k\,\bar{\psi}\,(i\Sigma^k)\psi
= d\,E_k\,\bar{\psi}\Sigma^k\psi .
$$

On the upper (positive-energy) components the bilinear $\bar{\psi}\Sigma^k\psi$ reduces to the spin density $\psi^\dagger\sigma^k\psi$, so

$$
\mathcal{L}_{\mathrm{EDM}} \;\longrightarrow\; d\,\mathbf{E}\cdot(\psi^\dagger\boldsymbol{\sigma}\psi),
\qquad
H_{\mathrm{NR}} = -\,d\,\mathbf{E}\cdot\boldsymbol{\sigma},
$$

the stated nonrelativistic limit. The chain is a derivation of the limit from the covariant operator, and it exhibits the $i$ of the Lagrangian turning into the $i$ of $\sigma^{0k}\gamma_5$. The magnetic-moment coupling reduces in the same way with $\sigma^{ij}$ and the field $\mathbf{B}$, but with a Hermitian insertion and no compensating $i$.

**The spin operator and the sector.** The spin operator $\Sigma^k$ is Hermitian and lies in the informational sector $\mathbb{M}_+$, and the EDM insertion is $i$ times it: the material-sector insertion is the central imaginary times the informational-sector spin. This is the algebraic statement of the CP-odd character of the EDM in the framework's language — the observable couples to the spin, and the coupling is made CP-odd by the central imaginary that moves the operator into the material sector.

## The Discrete Symmetries of the Insertions

**The bilinears and their transformation.** The four insertion families fall into two parity classes, and the classes determine the discrete symmetries of the observables. The bilinears

$$
\text{(vector)}\ \bar{\psi}\gamma^\mu\psi,\quad
\text{(axial)}\ \bar{\psi}\gamma^\mu\gamma_5\psi,\quad
\text{(tensor)}\ \bar{\psi}\sigma^{\mu\nu}\psi,\quad
\text{(pseudotensor)}\ \bar{\psi}\sigma^{\mu\nu}\gamma_5\psi
$$

transform under $\mathbf{P}$ and $\mathbf{T}$ in the standard way, and the electromagnetic couplings pick out the ones that are invariant:

| Observable | Bilinear | $\mathbf{P}$ | $\mathbf{T}$ | $\mathbf{CP}$ | Insertion |
|---|---|---|---|---|---|
| Charge | $\bar{\psi}\gamma^\mu\psi$ ($\mu=0$) | even | even | — | $\gamma^0$ (Hermitian) |
| Magnetic moment | $\bar{\psi}\sigma^{ij}\psi$ | even | even | even | $\sigma^{ij}$ (Hermitian) |
| EDM | $\bar{\psi}\sigma^{0k}\gamma_5\psi$ | odd | odd | odd | $\sigma^{0k}\gamma_5$ (anti-Hermitian) |
| CP-odd "magnetic" | $\bar{\psi}\sigma^{ij}\gamma_5\psi$ | odd | odd | odd | $\sigma^{ij}\gamma_5$ (Hermitian) |

The EDM sits in the antisymmetric tensor with the axial insertion, and the pattern is exactly the one demanded by the Hodge duality: the $\mathbf{E}$-coupling insertions ($\sigma^{0k}$, $\sigma^{0k}\gamma_5$) are anti-Hermitian, the $\mathbf{B}$-coupling insertions ($\sigma^{ij}$, $\sigma^{ij}\gamma_5$) are Hermitian, and the $\gamma_5$ flips the parity and the CP character while the duality flips the Hermiticity.

**The framework's real structure and CP.** The framework's conjugation enters the bilinears through the module's real structure: a CP transformation is a charge conjugation accompanied by a parity reflection, and in the module language it uses the antilinear real structure $\mathcal{C}$. The EDM's bilinear is the one that changes sign under this operation, and the coefficient's reality is what makes the action invariant. The framework statement is therefore precise: the EDM is the coefficient of a CP-odd, anti-Hermitian, material-sector bilinear, and its measurement is the measurement of a central imaginary's coupling to the spin.

**The anapole, and the completeness of the pair.** The electromagnetic list is completed by the anapole and the charge-radius terms, which are CP-even and are not dipole moments. The dipole pair — the magnetic moment and the EDM — is the CP-even and CP-odd pair of the list, and it exhausts the CP-odd content of the dimension-five electromagnetic couplings of a spin-$\tfrac12$ particle. This is why the EDM is *the* CP-odd electromagnetic observable at leading order, and why its bound is the sharpest test of new CP violation in the fermion sector.

## The Form Factors and the Two Coefficients

**The electromagnetic vertex.** The most general gauge-invariant vertex of an on-shell spin-$\tfrac12$ particle with the electromagnetic field, at momentum transfer $q$, is

$$
\Gamma^\mu(p',p) = \gamma^\mu F_1(q^2) + \frac{i}{2m}\,\sigma^{\mu\nu}q_\nu\,F_2(q^2)
+ \frac{i}{2m}\,\sigma^{\mu\nu}q_\nu\gamma_5\,F_3(q^2) + \cdots ,
$$

with $F_1$ the charge, $F_2$ the anomalous magnetic moment, and $F_3$ the EDM form factor; the ellipsis denotes the anapole and higher terms. In the nonrelativistic limit, $F_2$ and $F_3$ reduce to the magnetic and electric dipole couplings,

$$
H_{\mathrm{NR}} = -\,\mu\,\mathbf{B}\cdot\boldsymbol{\sigma} - d\,\mathbf{E}\cdot\boldsymbol{\sigma},
\qquad
\mu = \frac{e}{2m}\big(1+F_2(0)\big),\qquad d = \frac{e}{2m}F_3(0),
$$

so that the two coefficients are the same form factor at zero momentum transfer, multiplied by the same dimensionful factor and distinguished by the $\gamma_5$. The magnetic moment is the Hermitian member of the pair; the EDM is the anti-Hermitian member; and the two are Hodge duals of each other. This is the standard form-factor decomposition, and it is the reason the EDM is called the "dual" of the anomalous magnetic moment.

**Why the dual is the CP-odd one.** The form-factor pair $(F_2,F_3)$ is the framework's Hermitian/anti-Hermitian pair, and the two differ by the insertion of the volume element. The magnetic term has $F_2$ and no $\gamma_5$; the EDM term has $F_3$ and one $\gamma_5$. Under the Hodge duality $\sigma^{\mu\nu}\gamma_5=\tfrac{i}{2}\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma}$, the EDM insertion is the dual of the magnetic one with a factor of $i$; the factor is what makes the EDM's coefficient CP-odd and the magnetic moment's coefficient CP-even. The framework does not compute $F_3$; it places it in the anti-Hermitian sector and shows that its vanishing is the parity of the informational sector.

**The magnetic moment as the calibration.** The anomalous magnetic moment $F_2$ is measured to extraordinary precision, and its theoretical value is the framework's testing ground for the fermion sector; the companion article on the anomalous magnetic moment computes the framework's contribution. The EDM is the dual observable, and its bound is many orders of magnitude tighter in its own units than the magnetic moment's precision. The two together are the complete CP-even and CP-odd content of the dimension-five electromagnetic couplings of a spin-$\tfrac12$ particle.

## CP Violation and the Origin of the Phase

**Where a nonzero EDM comes from.** The EDM is CP-odd, so it can be generated only by a CP-violating interaction. The candidates are standard:

- **The CKM phase.** In the Standard Model the only CP-violating parameter of the quark sector is the phase of the Cabibbo–Kobayashi–Maskawa matrix; the companion article on the CKM matrix treats it. Its contribution to the neutron EDM arises only at the three-loop level and is of order $d_n\sim10^{-32}\ e\cdot\mathrm{cm}$, far below the present bound; the CKM phase is not the source of any measurable hadronic or atomic EDM.
- **The $\theta$ parameter.** Quantum chromodynamics admits a CP-odd topological term $\theta\,(\alpha_s/8\pi)\,\epsilon^{\mu\nu\rho\sigma}G^a_{\mu\nu}G^a_{\rho\sigma}$; its contribution to the neutron EDM is of order $d_n\sim\theta\times10^{-16}\ e\cdot\mathrm{cm}$, and the bound on $d_n$ forces $|\theta|\lesssim10^{-10}$. The $\theta$ parameter and the Witten effect belong to the corpus's general gauge apparatus and are not developed here; the fermion-sector statement is that the EDM is where the $\theta$ problem is measured.
- **New physics.** Any new CP-violating phase in a theory of fermions and gauge fields contributes to the EDMs, usually at the one- or two-loop level, and the bounds constrain the scale of that physics. This is the sense in which the EDM searches probe beyond the Standard Model.

**The Standard Model prediction, and its smallness.** The Standard Model's CKM phase gives EDMs that are far below the current bounds; the electron EDM, in particular, is generated only at four loops and is unobservably small. The framework inherits this: its fermion sector carries the linear chiral mass and the antilinear real structure, neither of which contains a CP-odd phase, and the algebra's central imaginaries are the volume element and the vector phase, not a CP-violating angle. The framework therefore predicts no measurable EDM, and observes that any EDM would be evidence for a phase it does not contain.

**Where a phase could sit in the framework.** A CP-odd phase can be written on the module in more than one way: in the mass matrix, in a Yukawa coupling, or in a coefficient multiplying an anti-Hermitian insertion. The framework supplies the insertion — the anti-Hermitian, material-sector operator — and the phase is the coefficient's imaginary part in a real action. The algebraic statement is that a nonzero EDM is the presence of a nonzero coefficient on the material-sector insertion, and since the material sector is the anti-Hermitian one, the coefficient is the imaginary part of an otherwise real coupling. Where that phase originates is not answered by the algebra.

## The Bounds and the Scales They Probe

**The experimental bounds.** The strongest EDM bounds are on the electron and the neutron, with the atomic and molecular experiments providing orders of magnitude of leverage:

| System | Bound on $|d|$ | Method |
|---|---|---|
| Electron | $\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$ | polar molecule (ThO), Ramsey spectroscopy |
| Neutron | $\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$ | stored ultracold neutrons, magnetic resonance |
| Proton (indirect) | $\lesssim10^{-23}\ e\cdot\mathrm{cm}$ | atomic EDM, storage-ring proposals |
| Mercury-199 atom | $\lesssim7.4\times10^{-30}\ e\cdot\mathrm{cm}$ | atomic EDM |

The bounds have improved by many orders of magnitude over the decades and are the tightest CP-odd constraints in particle physics. The values are those of the standard reviews.

**The scales they probe.** The dimensional estimate $d\sim e\,m_f\sin\varphi/\Lambda^2$ converts the bounds into a reach. For the electron, $m_e=0.511\ \mathrm{MeV}=5.11\times10^{-4}\ \mathrm{GeV}$; the conversion $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$ was used, and the numbers recomputed:

$$
\frac{e\,m_e}{(1\ \mathrm{TeV})^2} = 5.11\times10^{-10}\ \mathrm{GeV}^{-1} = 1.0\times10^{-23}\ e\cdot\mathrm{cm},
$$

so that a new-physics scale of $1$ TeV with an order-one CP phase would give an electron EDM some six orders of magnitude above the present bound. Reproducing the bound $1.1\times10^{-29}\ e\cdot\mathrm{cm}$ requires the scale to be larger by the square root of the ratio, $\sqrt{9\times10^{5}}\simeq950$, i.e.

$$
\Lambda \gtrsim 10^{3}\ \mathrm{TeV}
$$

for an order-one phase and no loop suppression. This is the standard statement that the electron EDM probes scales up to a few thousand TeV, which is why it is a leading constraint on new physics and why it is the target of the next generation of experiments. The neutron and proton bounds probe their own combinations of quark and gluon CP-odd operators, and the framework's proton and neutron articles state that no value is predicted.

**The magnetic moment for comparison.** The anomalous magnetic moment of the muon is measured to a precision of about two parts in $10^{7}$ and its theoretical uncertainty is dominated by hadronic effects; the companion article treats it. The EDM bounds are in a different regime: the electron EDM bound corresponds to a dipole moment about $5.7\times10^{-19}$ of the electron's magnetic moment. The two observables are the Hermitian and anti-Hermitian members of the same dimension-five pair, and the framework places them in the informational and material sectors respectively.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The even Clifford algebra as the biquaternion algebra, and the Hermiticity sector split | **Supplied**; the identification of Hermitian with $\mathbb{M}_+$ and anti-Hermitian with $\mathbb{M}_-$ |
| The EDM insertion $\sigma^{0k}\gamma_5$ as anti-Hermitian, material-sector | **Supplied**, recomputed entry by entry |
| The magnetic-moment insertion $\sigma^{ij}$ as Hermitian, informational-sector | **Supplied**, recomputed |
| The Hodge duality $\sigma^{\mu\nu}\gamma_5=\tfrac{i}{2}\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma}$ | **Supplied**, recomputed for all pairs |
| The explicit $i$ in the EDM Lagrangian as the marker of the anti-Hermitian insertion | **Supplied** by the algebra |
| The definition of the EDM and its $\mathbf{P}$-, $\mathbf{T}$-, $\mathbf{CP}$-odd character | **Transcribed**; standard |
| The form-factor decomposition and the nonrelativistic limit | **Transcribed**; standard |
| The CKM and $\theta$-term contributions, and their smallness | **Standard**; the $\theta$ parameter belongs to the general gauge apparatus |
| The experimental bounds and the reach $\Lambda\gtrsim10^{3}$ TeV | **Transcribed**; standard, with the arithmetic recomputed |
| The value of $d$ for any particle | **Not supplied**; empirical |
| A CP-violating phase, and its origin | **Not supplied**; the framework has none |
| The electron, neutron, and proton EDMs as framework predictions | **Not supplied**; the composite articles state the same |

## Open Questions

1. **The dictionary's sharpness.** The identification of the Hermitian and anti-Hermitian insertions with the sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ is used here as the framework's stated dictionary. For the EDM insertion the placement is exact: $\sigma^{0k}\gamma_5=-\Phi(e_k)$ is the image of a basis element of $\mathbb{M}_-$, and the rotation insertions are the central imaginary times such an image, corresponding to the informational elements $ie_k$. Whether the *full* even Clifford algebra, including the unit and $\gamma_5$, decomposes into the two sectors, or only up to the central factor that changes Hermiticity, is a separate question of the algebra's presentation: the unit $e_0$ is Hermitian while $\gamma_5$ is central, so neither is selected by the split, and a general Hermitian element of the even Clifford algebra need not be the image of an element of $\mathbb{M}_+$.

2. **The phase's sector.** A CP-odd phase multiplying the material-sector insertion is an imaginary coefficient. Whether the framework can distinguish phases that sit in the mass matrix from phases that sit in the dipole coefficients, and whether the abelian gauge-sector field strength of the framework supplies a $\theta$-like invariant, is not settled here and belongs partly to the general gauge apparatus.

3. **The composite EDMs.** The neutron and proton EDMs are matrix elements of quark and gluon CP-odd operators, and their computation is nonperturbative. The framework's proton and neutron articles supply no value; whether a biquaternion treatment of the bound-state problem can be given is open and lies outside the fermion sector.

4. **The duality at the level of the action.** The Hodge duality relates the EDM and magnetic insertions with a factor of $i$; whether the framework's action can be written so that the duality is manifest, pairing the two observables in a single Hermitian structure, is a question of the action's algebraic form.

## Summary

The electric dipole moment is the CP-odd, dimension-five coupling of a spin-$\tfrac12$ particle to the electromagnetic field, $-\tfrac{i}{2}d\,\bar{\psi}\sigma^{\mu\nu}\gamma_5\psi F_{\mu\nu}$, whose nonrelativistic limit is $-d\,\mathbf{E}\cdot\boldsymbol{\sigma}$. In the biquaternion framework its insertion has a definite algebraic character: the $\mathbf{E}$-coupling insertion $\sigma^{0k}\gamma_5$ is **anti-Hermitian** and therefore lies in the material sector $\mathbb{M}_-$, while the $\mathbf{B}$-coupling magnetic-moment insertion $\sigma^{ij}$ is **Hermitian** and lies in the informational sector $\mathbb{M}_+$; both statements were recomputed entry by entry in the block basis. The two are Hodge duals,

$$
\sigma^{\mu\nu}\gamma_5=\frac{i}{2}\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma},
$$

verified for all pairs $(\mu,\nu)$ with residual exactly zero, and the $i$ of the duality exchanges Hermiticity between the pair. The explicit $i$ in the EDM Lagrangian is what makes $i\times(\text{anti-Hermitian})$ Hermitian and is the algebra's marker of the CP-odd coefficient.

The form-factor decomposition $\Gamma^\mu=\gamma^\mu F_1+\tfrac{i}{2m}\sigma^{\mu\nu}q_\nu F_2+\tfrac{i}{2m}\sigma^{\mu\nu}q_\nu\gamma_5F_3+\cdots$ exhibits the magnetic moment $F_2$ and the EDM $F_3$ as the Hermitian and anti-Hermitian members of one dimension-five pair, and the framework places them in the informational and material sectors. The framework does not supply the coefficient: it has no CP-violating phase, predicts no measurable EDM, and inherits the Standard Model's tiny CKM contribution and the $\theta$-term's constraint ($|\theta|\lesssim10^{-10}$ from $|d_n|\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$). The present electron bound $|d_e|\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$, combined with the dimensional estimate $d\sim e\,m_e\sin\varphi/\Lambda^2$, probes new-physics scales $\Lambda\gtrsim10^{3}$ TeV, and the framework's contribution is to state exactly where in the algebra such a coefficient would sit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\Delta=S\oplus\bar{S}$ | Dirac module; $S=\mathbb{C}^2=(\tfrac12,0)$ |
| $\sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$ | Lorentz generators |
| $\gamma_5=i\omega$, $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | Chirality operator and volume element |
| $\sigma^{\mu\nu}\gamma_5=\tfrac{i}{2}\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma}$ | Hodge duality of the insertions |
| $\sigma^{0k},\sigma^{0k}\gamma_5$ | Anti-Hermitian, $\mathbb{M}_-$ (EDM insertion) |
| $\sigma^{ij},\sigma^{ij}\gamma_5$ | Hermitian, $\mathbb{M}_+$ (magnetic insertion) |
| $-\tfrac{i}{2}d\,\bar{\psi}\sigma^{\mu\nu}\gamma_5\psi F_{\mu\nu}$ | EDM Lagrangian |
| $H_{\mathrm{NR}}=-d\,\mathbf{E}\cdot\boldsymbol{\sigma}$ | EDM nonrelativistic Hamiltonian |
| $F_1,F_2,F_3$ | Charge, anomalous magnetic moment, EDM form factors |
| $d=\tfrac{e}{2m}F_3(0)$, $\mu=\tfrac{e}{2m}(1+F_2(0))$ | EDM and magnetic moment |
| $d\sim e\,m_f\sin\varphi/\Lambda^2$ | Dimensional estimate of the EDM |
| $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$ | EDM unit conversion |
| $|d_e|\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$ | Electron EDM bound |
| $|d_n|\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$ | Neutron EDM bound |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- L. I. Schiff, "Measurability of nuclear electric dipole moments," *Physical Review* **132** (1963) 2194–2200, for the atomic-physics theorem on the screening of nuclear EDMs.
- W. Bernreuther and M. Suzuki, "The electric dipole moment of the electron," *Reviews of Modern Physics* **63** (1991) 313–340, for the electron EDM and its theory.
- I. B. Khriplovich and S. K. Lamoreaux, *CP Violation Without Strangeness* (Springer, 1997), for electric dipole moments of particles, atoms, and molecules.
- J. Engel, M. J. Ramsey-Musolf, and U. van Kolck, "Electric dipole moments of nucleons, nuclei, and atoms: the Standard Model and beyond," *Progress in Particle and Nuclear Physics* **71** (2013) 21–74, for the hadronic and nuclear EDMs and the $\theta$-term contribution.
- T. Chupp, P. Fierlinger, M. Ramsey-Musolf, and J. Singh, "Electric dipole moments of the nucleon and light nuclei," *Reviews of Modern Physics* **91** (2019) 015001, for the neutron and proton EDM bounds and their interpretation.
- V. Andreev *et al.* (ACME Collaboration), "Improved limit on the electric dipole moment of the electron," *Nature* **562** (2018) 355–360, for the polar-molecule electron EDM bound.
- C. Abel *et al.* (nEDM Collaboration), "Measurement of the permanent electric dipole moment of the neutron," *Physical Review Letters* **124** (2020) 081803, for the neutron EDM bound.
- E. D. Commins, "Electric dipole moments of leptons," *Advances in Atomic, Molecular, and Optical Physics* **40** (1998) 1–46, for the lepton EDM phenomenology.
- K. F. Smith *et al.*, "Search for a permanent electric dipole moment of the electron," *Journal of Physics G* **45** (2018) 085001, for the experimental methods.
- O. Lebedev, K. A. Olive, M. Pospelov, and A. Ritz, "Probing CP violation with the deuteron electric dipole moment," *Physical Review D* **70** (2004) 016003, for the relation between EDM bounds and new-physics scales.
