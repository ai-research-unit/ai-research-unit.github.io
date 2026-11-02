# __The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure__

## Introduction

An **electric dipole moment** (EDM) is a permanent separation of charge along the spin axis of a particle. For a spin-$\tfrac12$ particle the interaction is

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}\,d\;\bar{\psi}\,\sigma_{\mu\nu}\,-iR_{e_z}\,\psi\;F_{\mu\nu},
\qquad
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma},
$$

where $-iL_{e_t}R_{e_z}$ is the chirality cell, $\sigma_{\mu\nu}=\tfrac{i}{2}[iL_{e_\mu}R_{e_{\nu(\mu)}},iL_{e_\nu}R_{e_{\nu(\nu)}}]$ is the bivector of two frame generators, and $L_{a}R_{b}$ with $L_a\psi=a\psi$ and $R_b\psi=\psi b$; the five cells $iR_{e_x},\dots,iL_{e_z}R_{e_y},-iR_{e_z}$ are fixed below. So the particle gains an energy in an electric field that depends on the orientation of its spin. The EDM is the coefficient $d$; it has the dimensions of $e\cdot\mathrm{length}$ and it is the canonical **CP-odd** observable of a spin-$\tfrac12$ system. Its measurement is a search for physics beyond the Standard Model, and its present bounds are among the tightest in particle physics.

Here $iL_{e_\mu}R_{e_{\nu(\mu)}}$ is the generator cell of the coordinate $x_\mu$: $\nu(t)=x$ and $\nu(k)=y$, so that the time direction is carried by $iR_{e_x}=iL_{e_t}R_{e_x}$ and the three space directions by $iL_{e_k}R_{e_y}$ with $k=1,2,3$.

The biquaternion framework makes a structural statement about the EDM operator that is the subject of this article. The insertion $\sigma_{\mu\nu}\,-iR_{e_z}$ is **anti-Hermitian** in the field components that couple to $\vec E$, and it therefore belongs to the framework's material, anti-Hermitian sector $\mathbb{M}_-$; the magnetic-moment insertion $\sigma_{\mu\nu}$, which couples to $\vec B$, is Hermitian and belongs to the informational sector $\mathbb{M}_+$. The two are Hodge duals of each other, and the Hermiticity flips under the duality. The article establishes this and states what it does and does not buy.

- **Established, and recomputed below.** The Hermiticity of the insertions, the Hodge duality $\sigma_{\mu\nu}\,-iR_{e_z}=\tfrac{i}{2}\epsilon_{\mu\nu\rho\sigma}\sigma^{\rho\sigma}$, and the resulting sector placement. The $\vec E$-coupling insertion $\sigma_{0k}\,-iR_{e_z}$ is anti-Hermitian (recomputed), hence material; the $\vec B$-coupling insertion $\sigma_{ij}$ is Hermitian, hence informational. The EDM Lagrangian is Hermitian because the explicit $i$ compensates the anti-Hermiticity, and that $i$ is the framework's marker of the CP-odd coefficient.
- **Standard, transcribed.** The definition of the EDM, its $\mathbf{P}$-, $\mathbf{T}$-, and $\mathbf{CP}$-odd character, the nonrelativistic limit, the form-factor decomposition of the electromagnetic vertex, the Standard Model prediction (CKM-suppressed and tiny), the $\theta$-term contribution, and the experimental bounds are standard. They are stated in the framework's notation.
- **Gap, left visible.** The framework supplies the operator and its sector, and it does not supply the coefficient. It has no CP-violating phase of its own, no mechanism to generate one, and no prediction for the electron, neutron, or proton EDM. The value of $d$ is an empirical input, and the framework's statement is the structural one: a nonzero EDM is the presence of a coefficient on an anti-Hermitian, material-sector insertion.

The article is organised as follows. A section defines the EDM operator and its discrete symmetries. A section establishes the anti-Hermitian structure and the Hodge duality. A section gives the form-factor decomposition and contrasts the EDM with the magnetic moment. A section treats the origin of the CP-odd phase. A section collects the bounds and the scales they probe. A closing section separates what is supplied, transcribed, and missing.

The four cells $iR_{e_x}$ and $iL_{e_k}R_{e_y}$ carry the Clifford relations of $g=\operatorname{diag}(+1,-1,-1,-1)$; see the appendix.

With $-iR_{e_z}=i\omega$ and $\omega=iR_{e_x}\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}\,iL_{e_z}R_{e_y}$. The field strength is $F_{0i}=E_i$, $F_{ij}=-\epsilon_{ijk}B_k$, and $\epsilon_{0123}=+1$, with the metric form $\sigma_{\rho\sigma}=g_{\rho\mu}g_{\sigma\nu}\sigma_{\mu\nu}$. The mass terms are the linear Dirac pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$ (not a conjugation), and the antilinear real structure $\flat=-{}^{*}$ is a separate object. Natural units $\hbar=c=1$ are used, and the EDM unit conversion is $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$.

The framework results used here are those of the companion articles:

- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the Dirac module and the bilinears built on it.
- Companion article *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, for the identification of the Clifford generators with the biquaternion basis.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the mass-term conventions and the real structure $\flat$.
- Companion article *The Proton in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.
- Companion article *The Neutron in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.

## The EDM Operator and Its Discrete Symmetries

**The interaction.** The EDM is a CP-odd coupling of the electromagnetic field strength to the spin. Its Lorentz-covariant form and the nonrelativistic Hamiltonian are

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}\,d\,\bar{\psi}\sigma_{\mu\nu}\,-iR_{e_z}\psi F_{\mu\nu},
\qquad
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma},
$$

where $\boldsymbol{\sigma}$ are the Pauli matrices acting on the spin and the coefficient $d$ is the EDM. The explicit $i$ is required for a Hermitian Lagrangian, and it is the first appearance of the article's central point: the insertion is anti-Hermitian, and the coefficient must be multiplied by $i$ to give a real (Hermitian) interaction.

**Discrete symmetries.** Under parity $\mathbf{P}$, the electric field is a vector ($\vec E\to-\vec E$) and the spin vector is a pseudovector ($\boldsymbol{\sigma}\to+\boldsymbol{\sigma}$), so $\vec E\cdot\boldsymbol{\sigma}\to-\vec E\cdot\boldsymbol{\sigma}$: the EDM term is $\mathbf{P}$-odd. Under time reversal $\mathbf{T}$, the electric field is $\mathbf{T}$-even and the spin vector is $\mathbf{T}$-odd, so the term is again odd. Under $\mathbf{C}$ the term is even. Hence the EDM is $\mathbf{P}$- and $\mathbf{T}$-odd, and by the CPT theorem it is $\mathbf{CP}$-odd: a nonvanishing $d$ requires a source of CP violation. The magnetic-moment term, $-\vec\mu\cdot\vec B$, is $\mathbf{P}$-even and $\mathbf{T}$-even, and the contrast is exact: the two operators differ by the presence of the chirality cell $-iR_{e_z}$, which is the source of the parity and CP properties.

**The dimension and the size.** The EDM has the dimensions of electric charge times length. In natural units, $d$ is dimensionless times a length, i.e. $[\mathrm{GeV}^{-1}]$; the conversion is $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$. For a fermion of mass $m_f$ and a new-physics scale $\Lambda$, the standard dimensional estimate of a CP-violating contribution is

$$
d \sim \frac{e\,m_f}{\Lambda^2}\,\sin\varphi ,
$$

where $\varphi$ is the CP-odd phase. The estimate is the one that governs the reach of the experiments: the smaller the bound, the larger the scale probed, and the heavier the fermion, the larger the contribution. The numbers are used in the last section.

**The observable.** A permanent EDM precesses in an electric field, and the precession is what the experiments measure — in atoms and molecules, in stored neutrons, and in storage rings. The observable is the coefficient of $\vec E\cdot\boldsymbol{\sigma}$, and it is the only CP-odd coupling of a spin-$\tfrac12$ particle to the electromagnetic field up to dimension five. The framework's proton and neutron articles treat those composites and note that the framework supplies no value for their EDMs; this article treats the operator and its structure.

## The Anti-Hermitian Structure of $\sigma_{\mu\nu}\,-iR_{e_z}$

**The Hermiticity of the insertions.** With the block representation and $g=\mathrm{diag}(+1,-1,-1,-1)$, the generators of the Lorentz algebra split into the boosts and the rotations,

$$
\sigma_{0k} = \text{(anti-Hermitian)},\qquad \sigma_{ij} = \text{(Hermitian)},
$$

and the chirality insertion flips the two,

$$
\sigma_{0k}\,-iR_{e_z} = \text{(anti-Hermitian)},\qquad \sigma_{ij}\,-iR_{e_z} = \text{(Hermitian)}.
$$

The pattern is the standard one: $iR_{e_x}$ is Hermitian and $iL_{e_k}R_{e_y}$ anti-Hermitian; the boost generators $\sigma_{0k}$ therefore change sign under Hermitian conjugation while the rotation generators $\sigma_{ij}$ do not, and $-iR_{e_z}$, being Hermitian and anticommuting with each $iL_{e_\mu}R_{e_{\nu(\mu)}}$, commutes with the bilinear $\sigma_{\mu\nu}$ and so leaves its Hermiticity unchanged. **The $\vec E$-coupling insertion is the anti-Hermitian one.**

**The Hodge duality.** The two families of insertions are dual to each other. In terms of the totally antisymmetric symbol, with the sum over the raised pair,

$$
\boxed{\;\sigma_{\mu\nu}\,-iR_{e_z} = \frac{i}{2}\,\epsilon_{\mu\nu\rho\sigma}\,\sigma^{\rho\sigma},
\qquad\text{i.e.}\qquad
(\sigma_{\mathrm D})_{\mu\nu}:=\tfrac12\epsilon_{\mu\nu\rho\sigma}\sigma^{\rho\sigma} = -\,i\,\sigma_{\mu\nu}\,-iR_{e_z}\;},
$$

an identity that was recomputed for all pairs $(\mu,\nu)$ with residual exactly zero. The duality exchanges the electric and magnetic components: $\sigma_{0k}\,-iR_{e_z}$ is dual to a combination of the $\sigma_{ij}$, and vice versa. Since the duality factor is $i$, it exchanges Hermitian with anti-Hermitian, which is exactly the flip recorded above.

**The sector placement.** The even Clifford algebra generated by the products of pairs of the generators $iL_{e_\mu}R_{e_{\nu(\mu)}}$ — the unit, the $\sigma_{\mu\nu}$, and $-iR_{e_z}$ — is isomorphic to the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, and under this isomorphism the framework's sector split is the Hermiticity split: Hermitian generators lie in the informational sector $\mathbb{M}_+$ and anti-Hermitian generators in the material sector $\mathbb{M}_-$. The dictionary is that of the companion articles. Applied to the insertions:

| Insertion | Couples to | Hermiticity | Sector |
|---|---|---|---|
| $\sigma_{0k}$ | $\vec E$ (the boost part of the Pauli term) | anti-Hermitian | $\mathbb{M}_-$ |
| $\sigma_{0k}\,-iR_{e_z}$ | $\vec E$ (the EDM) | anti-Hermitian | $\mathbb{M}_-$ |
| $\sigma_{ij}$ | $\vec B$ (the magnetic moment) | Hermitian | $\mathbb{M}_+$ |
| $\sigma_{ij}\,-iR_{e_z}$ | $\vec B$ (the CP-odd partner) | Hermitian | $\mathbb{M}_+$ |

The EDM insertion is therefore the anti-Hermitian, material-sector insertion, and the magnetic-moment insertion is its Hermitian, informational-sector dual. This is the article's central structural statement; it was verified entry by entry in the block basis.

**The dictionary form of the EDM insertion.** The placement can be made exact rather than a Hermiticity match. Under the dictionary that carries the biquaternion basis to the Clifford generators, $\vec e_x\mapsto\,iL_{e_y}R_{e_y}\,iL_{e_z}R_{e_y}$, $\vec e_y\mapsto\,iL_{e_z}R_{e_y}\,iL_{e_x}R_{e_y}$, $\vec e_z\mapsto\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}$, the EDM insertion *is* the image of a basis element of the material sector:

$$
\boxed{\;\sigma_{0k}\,-iR_{e_z} = -\mathsf{M}_2(\vec e_k) = \mathsf{M}_2(-\vec e_k), \qquad -\vec e_k \in \mathbb{M}_-\;},
$$

verified for $k=1,2,3$ with residual exactly zero. The EDM insertion is thus not merely anti-Hermitian and therefore material; up to a sign it is the Clifford image of one of the three vector basis elements $\vec e_k$ of $\mathbb{M}_-$ — the same elements that carry the spatial directions of the material sector. The magnetic insertion corresponds to the informational element $i\vec e_k$, and since multiplication by the central $i$ exchanges the sectors, $i\mathbb{M}_-=\mathbb{M}_+$, the same $\vec e_k$ appears on both sides of the table. The correspondence is a statement about the objects the insertion represents, in the sense of the convention that reads the sectors on the fields; the sectors are real vector spaces on which the algebra acts rather than subalgebras, and a general element of the even Clifford algebra need not fall in one of them.

**The $i$ and the Hermiticity of the Lagrangian.** Because the EDM insertion is anti-Hermitian, the bilinear $\bar{\psi}\sigma_{0k}\,-iR_{e_z}\psi$ is anti-Hermitian as a classical bilinear, and the Lagrangian density $-\tfrac{i}{2}d\,\bar{\psi}\sigma_{\mu\nu}\,-iR_{e_z}\psi F_{\mu\nu}$ is Hermitian for real $d$ precisely because the explicit $i$ makes $i\times(\text{anti-Hermitian})$ Hermitian. The magnetic-moment Lagrangian has no such $i$, because its insertion is already Hermitian. **The factor of $i$ is the biquaternion signature of the EDM**: the operator is the CP-odd member of a dual pair, its material-sector placement is the anti-Hermiticity, and the Hermiticity of the action is restored by the central imaginary.

## The Nonrelativistic Reduction

**From the covariant operator to $-d\,\vec E\cdot\boldsymbol{\sigma}$.** The EDM coupling reduces to the nonrelativistic Hamiltonian by an identity that the block basis makes explicit. In the Dirac basis the spin operator is

$$
\Sigma_k = \mathrm{diag}(\sigma_k,\sigma_k),\qquad (\Sigma_k)^\dagger=\Sigma_k,\qquad
\sigma_{0k}\,-iR_{e_z} = i\,\Sigma_k ,
$$

which was verified entry by entry: $\sigma_{01}\,-iR_{e_z} = i\,\mathrm{diag}(\sigma_1,\sigma_1)$, and similarly for the other two components. The identity shows both facts at once — that $\sigma_{0k}\,-iR_{e_z}$ is $i$ times a Hermitian matrix (hence anti-Hermitian), and that the matrix it multiplies is the spin matrix.

Substituting into the Lagrangian, with $F_{0k}=E_k$ and the sum over $k$,

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}d\,\bar{\psi}\sigma_{\mu\nu}\,-iR_{e_z}\psi F_{\mu\nu}
\supset -\,i\,d\,E_k\,\bar{\psi}\sigma_{0k}\,-iR_{e_z}\psi
= -\,i\,d\,E_k\,\bar{\psi}\,(i\Sigma_k)\psi
= d\,E_k\,\bar{\psi}\Sigma_k\psi .
$$

On the upper (positive-energy) components the bilinear $\bar{\psi}\Sigma_k\psi$ reduces to the spin density $\psi^\dagger\sigma_k\psi$, so

$$
\mathcal{L}_{\mathrm{EDM}} \;\longrightarrow\; d\,\vec E\cdot(\psi^\dagger\boldsymbol{\sigma}\psi),
\qquad
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma},
$$

the stated nonrelativistic limit. The chain is a derivation of the limit from the covariant operator, and it exhibits the $i$ of the Lagrangian turning into the $i$ of $\sigma_{0k}\,-iR_{e_z}$. The magnetic-moment coupling reduces in the same way with $\sigma_{ij}$ and the field $\vec B$, but with a Hermitian insertion and no compensating $i$.

**The spin operator and the sector.** The spin operator $\Sigma_k$ is Hermitian and lies in the informational sector $\mathbb{M}_+$, and the EDM insertion is $i$ times it: the material-sector insertion is the central imaginary times the informational-sector spin. This is the algebraic statement of the CP-odd character of the EDM in the framework's language — the observable couples to the spin, and the coupling is made CP-odd by the central imaginary that moves the operator into the material sector.

## The Discrete Symmetries of the Insertions

**The bilinears and their transformation.** The four insertion families fall into two parity classes, and the classes determine the discrete symmetries of the observables. The bilinears

$$
\text{(vector)}\ \bar{\psi}\,iL_{e_\mu}R_{e_{\nu(\mu)}}\psi,\quad
\text{(axial)}\ \bar{\psi}\,iL_{e_\mu}R_{e_{\nu(\mu)}}\,-iR_{e_z}\psi,\quad
\text{(tensor)}\ \bar{\psi}\sigma_{\mu\nu}\psi,\quad
\text{(pseudotensor)}\ \bar{\psi}\sigma_{\mu\nu}\,-iR_{e_z}\psi
$$

transform under $\mathbf{P}$ and $\mathbf{T}$ in the standard way, and the electromagnetic couplings pick out the ones that are invariant:

| Observable | Bilinear | $\mathbf{P}$ | $\mathbf{T}$ | $\mathbf{CP}$ | Insertion |
|---|---|---|---|---|---|
| Charge | $\bar{\psi}\,iL_{e_\mu}R_{e_{\nu(\mu)}}\psi$ ($\mu=0$) | even | even | — | $iR_{e_x}$ (Hermitian) |
| Magnetic moment | $\bar{\psi}\sigma_{ij}\psi$ | even | even | even | $\sigma_{ij}$ (Hermitian) |
| EDM | $\bar{\psi}\sigma_{0k}\,-iR_{e_z}\psi$ | odd | odd | odd | $\sigma_{0k}\,-iR_{e_z}$ (anti-Hermitian) |
| CP-odd "magnetic" | $\bar{\psi}\sigma_{ij}\,-iR_{e_z}\psi$ | odd | odd | odd | $\sigma_{ij}\,-iR_{e_z}$ (Hermitian) |

The EDM sits in the antisymmetric tensor with the axial insertion, and the pattern is exactly the one demanded by the Hodge duality: the $\vec E$-coupling insertions ($\sigma_{0k}$, $\sigma_{0k}\,-iR_{e_z}$) are anti-Hermitian, the $\vec B$-coupling insertions ($\sigma_{ij}$, $\sigma_{ij}\,-iR_{e_z}$) are Hermitian, and the $-iR_{e_z}$ flips the parity and the CP character while the duality flips the Hermiticity.

**The framework's real structure and CP.** The framework's conjugation enters the bilinears through the module's real structure: a CP transformation is a charge conjugation accompanied by a parity reflection, and in the module language it uses the antilinear real structure $\mathcal{C}$. The EDM's bilinear is the one that changes sign under this operation, and the coefficient's reality is what makes the action invariant. The framework statement is therefore precise: the EDM is the coefficient of a CP-odd, anti-Hermitian, material-sector bilinear, and its measurement is the measurement of a central imaginary's coupling to the spin.

**The anapole, and the completeness of the pair.** The electromagnetic list is completed by the anapole and the charge-radius terms, which are CP-even and are not dipole moments. The dipole pair — the magnetic moment and the EDM — is the CP-even and CP-odd pair of the list, and it exhausts the CP-odd content of the dimension-five electromagnetic couplings of a spin-$\tfrac12$ particle. This is why the EDM is *the* CP-odd electromagnetic observable at leading order, and why its bound is the sharpest test of new CP violation in the fermion sector.

## The Form Factors and the Two Coefficients

**The electromagnetic vertex.** The most general gauge-invariant vertex of an on-shell spin-$\tfrac12$ particle with the electromagnetic field, at momentum transfer $k=p_2-p$, is

$$
\Gamma_\mu(p_2,p) = iL_{e_\mu}R_{e_{\nu(\mu)}} F_1(k^2) + \frac{i}{2m}\,\sigma_{\mu\nu}k_\nu\,F_2(k^2)
+ \frac{i}{2m}\,\sigma_{\mu\nu}k_\nu\,-iR_{e_z}\,F_3(k^2) + \cdots ,
$$

with $F_1$ the charge, $F_2$ the anomalous magnetic moment, and $F_3$ the EDM form factor; the ellipsis denotes the anapole and higher terms. In the nonrelativistic limit, $F_2$ and $F_3$ reduce to the magnetic and electric dipole couplings,

$$
H_{\mathrm{NR}} = -\,\mu\,\vec B\cdot\boldsymbol{\sigma} - d\,\vec E\cdot\boldsymbol{\sigma},
\qquad
\mu = \frac{e}{2m}\big(1+F_2(0)\big),\qquad d = \frac{e}{2m}F_3(0),
$$

so that the two coefficients are the form factors at zero momentum transfer, multiplied by the same dimensionful factor and distinguished by the $-iR_{e_z}$. The magnetic moment is the Hermitian member of the pair; the EDM is the anti-Hermitian member; and the two are Hodge duals of each other. This is the standard form-factor decomposition, and it is the reason the EDM is called the "dual" of the anomalous magnetic moment.

**Why the dual is the CP-odd one.** The form-factor pair $(F_2,F_3)$ is the framework's Hermitian/anti-Hermitian pair, and the two differ by the insertion of the volume element. The magnetic term has $F_2$ and no $-iR_{e_z}$; the EDM term has $F_3$ and one $-iR_{e_z}$. Under the Hodge duality $\sigma_{\mu\nu}\,-iR_{e_z}=\tfrac{i}{2}\epsilon_{\mu\nu\rho\sigma}\sigma^{\rho\sigma}$, the EDM insertion is the dual of the magnetic one with a factor of $i$; the factor is what makes the EDM's coefficient CP-odd and the magnetic moment's coefficient CP-even. The framework does not compute $F_3$; it places it in the anti-Hermitian sector, and the vanishing of $F_3$ leaves the pair $(F_2,F_3)$ wholly in the informational sector, which is the CP-even statement.

**The magnetic moment as the calibration.** The anomalous magnetic moment $F_2$ is measured to extraordinary precision, and its theoretical value is the framework's testing ground for the fermion sector; the companion article on the anomalous magnetic moment computes the framework's contribution. The EDM is the dual observable, and its bound is many orders of magnitude tighter in its own units than the magnetic moment's precision. The two together are the complete CP-even and CP-odd content of the dimension-five electromagnetic couplings of a spin-$\tfrac12$ particle.

## CP Violation and the Origin of the Phase

**Where a nonzero EDM comes from.** The EDM is CP-odd, so it can be generated only by a CP-violating interaction. The candidates are standard:

- **The CKM phase.** In the Standard Model the only CP-violating parameter of the quark sector is the phase of the Cabibbo–Kobayashi–Maskawa matrix; the companion article on the CKM matrix treats it. Its contribution to the neutron EDM arises only at the three-loop level and is of order $d_n\sim10^{-32}\ e\cdot\mathrm{cm}$, far below the present bound; the CKM phase is not the source of any measurable hadronic or atomic EDM.
- **The $\theta$ parameter.** Quantum chromodynamics admits a CP-odd topological term $\theta\,(\alpha_s/8\pi)\,\epsilon_{\mu\nu\rho\sigma}G_{a\mu\nu}G_{a\rho\sigma}$; its contribution to the neutron EDM is of order $d_n\sim\theta\times10^{-16}\ e\cdot\mathrm{cm}$, and the bound on $d_n$ forces $|\theta|\lesssim10^{-10}$. The $\theta$ parameter belongs to the corpus's general gauge apparatus and is not developed here; the fermion-sector statement is that the EDM is where the $\theta$ problem is measured.
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
| The EDM insertion $\sigma_{0k}\,-iR_{e_z}$ as anti-Hermitian, material-sector | **Supplied**, recomputed entry by entry |
| The magnetic-moment insertion $\sigma_{ij}$ as Hermitian, informational-sector | **Supplied**, recomputed |
| The Hodge duality $\sigma_{\mu\nu}\,-iR_{e_z}=\tfrac{i}{2}\epsilon_{\mu\nu\rho\sigma}\sigma^{\rho\sigma}$ | **Supplied**, recomputed for all pairs |
| The explicit $i$ in the EDM Lagrangian as the marker of the anti-Hermitian insertion | **Supplied** by the algebra |
| The definition of the EDM and its $\mathbf{P}$-, $\mathbf{T}$-, $\mathbf{CP}$-odd character | **Transcribed**; standard |
| The form-factor decomposition and the nonrelativistic limit | **Transcribed**; standard |
| The CKM and $\theta$-term contributions, and their smallness | **Standard**; the $\theta$ parameter belongs to the general gauge apparatus |
| The experimental bounds and the reach $\Lambda\gtrsim10^{3}$ TeV | **Transcribed**; standard, with the arithmetic recomputed |
| The value of $d$ for any particle | **Not supplied**; empirical |
| A CP-violating phase, and its origin | **Not supplied**; the framework has none |
| The electron, neutron, and proton EDMs as framework predictions | **Not supplied**; the composite articles state the same |

## Open Questions

1. **The dictionary's sharpness.** The identification of the Hermitian and anti-Hermitian insertions with the sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ is used here as the framework's stated dictionary. For the EDM insertion the placement is exact: $\sigma_{0k}\,-iR_{e_z}=-\mathsf{M}_2(\vec e_k)$ is the image of a basis element of $\mathbb{M}_-$, and the rotation insertions are the central imaginary times such an image, corresponding to the informational elements $i\vec e_k$. Whether the *full* even Clifford algebra, including the unit and $-iR_{e_z}$, decomposes into the two sectors, or only up to the central factor that changes Hermiticity, is a separate question of the algebra's presentation: the unit $e_t$ is Hermitian while $-iR_{e_z}$ is central, so neither is selected by the split, and a general Hermitian element of the even Clifford algebra need not be the image of an element of $\mathbb{M}_+$.

2. **The phase's sector.** A CP-odd phase multiplying the material-sector insertion is an imaginary coefficient. Whether the framework can distinguish phases that sit in the mass matrix from phases that sit in the dipole coefficients, and whether the abelian gauge-sector field strength of the framework supplies a $\theta$-like invariant, is not settled here and belongs partly to the general gauge apparatus.

3. **The composite EDMs.** The neutron and proton EDMs are matrix elements of quark and gluon CP-odd operators, and their computation is nonperturbative. The framework's proton and neutron articles supply no value; whether a biquaternion treatment of the bound-state problem can be given is open and lies outside the fermion sector.

4. **The duality at the level of the action.** The Hodge duality relates the EDM and magnetic insertions with a factor of $i$; whether the framework's action can be written so that the duality is manifest, pairing the two observables in a single Hermitian structure, is a question of the action's algebraic form.

## Summary

The electric dipole moment is the CP-odd, dimension-five coupling of a spin-$\tfrac12$ particle to the electromagnetic field, $-\tfrac{i}{2}d\,\bar{\psi}\sigma_{\mu\nu}\,-iR_{e_z}\psi F_{\mu\nu}$, whose nonrelativistic limit is $-d\,\vec E\cdot\boldsymbol{\sigma}$. In the biquaternion framework its insertion has a definite algebraic character: the $\vec E$-coupling insertion $\sigma_{0k}\,-iR_{e_z}$ is **anti-Hermitian** and therefore lies in the material sector $\mathbb{M}_-$, while the $\vec B$-coupling magnetic-moment insertion $\sigma_{ij}$ is **Hermitian** and lies in the informational sector $\mathbb{M}_+$; both statements were recomputed entry by entry in the block basis. The two are Hodge duals,

$$
\boxed{\;\sigma_{\mu\nu}\,-iR_{e_z}=\frac{i}{2}\epsilon_{\mu\nu\rho\sigma}\sigma^{\rho\sigma}\;},
$$

verified for all pairs $(\mu,\nu)$ with residual exactly zero, and the $i$ of the duality exchanges Hermiticity between the pair. The explicit $i$ in the EDM Lagrangian is what makes $i\times(\text{anti-Hermitian})$ Hermitian and is the algebra's marker of the CP-odd coefficient.

The form-factor decomposition $\Gamma_\mu=iL_{e_\mu}R_{e_{\nu(\mu)}} F_1+\tfrac{i}{2m}\sigma_{\mu\nu}k_\nu F_2+\tfrac{i}{2m}\sigma_{\mu\nu}k_\nu\,-iR_{e_z}F_3+\cdots$ exhibits the magnetic moment $F_2$ and the EDM $F_3$ as the Hermitian and anti-Hermitian members of one dimension-five pair, and the framework places them in the informational and material sectors. The framework does not supply the coefficient: it has no CP-violating phase, predicts no measurable EDM, and inherits the Standard Model's tiny CKM contribution and the $\theta$-term's constraint ($|\theta|\lesssim10^{-10}$ from $|d_n|\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$). The present electron bound $|d_e|\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$, combined with the dimensional estimate $d\sim e\,m_e\sin\varphi/\Lambda^2$, probes new-physics scales $\Lambda\gtrsim10^{3}$ TeV, and the framework's contribution is to state exactly where in the algebra such a coefficient would sit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\Delta=S\oplus\bar{S}$ | Dirac module; $S=\mathbb{C}^2=(\tfrac12,0)$ |
| $iL_{e_t}R_{e_x}$, $iL_{e_k}R_{e_y}$, $-iL_{e_t}R_{e_z}$ | Frame cells; $L_{a}R_{b}$, $L_{a}R_{b}\psi=a\psi b$ |
| $\sigma_{\mu\nu}=\tfrac{i}{2}[iL_{e_\mu}R_{e_{\nu(\mu)}},iL_{e_\nu}R_{e_{\nu(\nu)}}]$ | Lorentz generators |
| $-iR_{e_z}=i\omega$, $\omega=iR_{e_x}\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}\,iL_{e_z}R_{e_y}$ | Chirality cell and volume element |
| $\sigma_{\mu\nu}\,-iR_{e_z}=\tfrac{i}{2}\epsilon_{\mu\nu\rho\sigma}\sigma^{\rho\sigma}$ | Hodge duality of the insertions |
| $\sigma_{0k},\sigma_{0k}\,-iR_{e_z}$ | Anti-Hermitian, $\mathbb{M}_-$ (EDM insertion) |
| $\sigma_{ij},\sigma_{ij}\,-iR_{e_z}$ | Hermitian, $\mathbb{M}_+$ (magnetic insertion) |
| $-\tfrac{i}{2}d\,\bar{\psi}\sigma_{\mu\nu}\,-iR_{e_z}\psi F_{\mu\nu}$ | EDM Lagrangian |
| $H_{\mathrm{NR}}=-d\,\vec E\cdot\boldsymbol{\sigma}$ | EDM nonrelativistic Hamiltonian |
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

## Appendix — The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_tR_x,\quad \gamma_1=iL_xR_y,\quad \gamma_2=iL_yR_y,\quad \gamma_3=iL_zR_y,\quad \gamma_5=-iL_tR_z .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

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
The four contraction sums are frame statements, because a cell's square is. In the Euclidean frame, where every cell squares to $+I_4$, they are $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.
