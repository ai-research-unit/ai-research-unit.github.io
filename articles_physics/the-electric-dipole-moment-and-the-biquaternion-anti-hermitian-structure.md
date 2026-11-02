# __The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure__

## Introduction

An **electric dipole moment** (EDM) is a permanent separation of charge along the spin axis of a particle. For a spin-$\tfrac12$ particle the interaction is

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}\,d\;\bar{\psi}\,\sigma_{\mu\nu}(-iR_{\vec e_z})\,\psi\;F_{\mu\nu},
\qquad
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma},
$$

where $\boldsymbol{\sigma}$ are the Pauli matrices acting on the spin and $d$ is the EDM. The coefficient has the dimensions of charge times length, it is the canonical **CP-odd** observable of a spin-$\tfrac12$ system, and its measurement is a search for physics beyond the Standard Model: its present bounds are among the tightest in particle physics.

**The frame and the insertion.** The insertion is a product of frame cells, and the product is written with parentheses throughout the article, so that the minus sign of the chirality cell is never read as a subtraction. With $L_a\psi=a\psi$ and $R_b\psi=\psi b$, the frame is the five cells

$$
iL_{e_t}R_{\vec e_x},\qquad
iL_{e_x}R_{\vec e_y},\qquad
iL_{e_y}R_{\vec e_y},\qquad
iL_{e_z}R_{\vec e_y},\qquad
-iR_{\vec e_z},
$$

the first timelike, the next three spatial, the last the chirality cell $-iR_{\vec e_z}=-iL_{e_t}R_{\vec e_z}$. The bivector of two of them is

$$
\sigma_{\mu\nu}=\tfrac{i}{2}\big[iL_{e_\mu}R_{\vec e_{\nu(\mu)}},\,iL_{e_\nu}R_{\vec e_{\nu(\nu)}}\big],
\qquad
\nu(t)=x,\quad \nu(k)=y ,
$$

so $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ is the frame cell of the coordinate $x_\mu$. The frame carries the Clifford relations of $g=\operatorname{diag}(+1,-1,-1,-1)$ and is fixed in §*The Gamma Formulation*.

**The structural statement.** The biquaternion framework places the EDM operator in a definite half of its algebra. The insertion $\sigma_{\mu\nu}(-iR_{\vec e_z})$ is **anti-Hermitian** in the field components that couple to $\vec E$, and it therefore belongs to the framework's material, anti-Hermitian sector $\mathbb{M}_-$; the magnetic-moment insertion $\sigma_{ij}$, which couples to $\vec B$, is Hermitian and belongs to the informational sector $\mathbb{M}_+$. The two are Hodge duals of each other, and the $i$ that the duality carries in each direction is what reconciles their Hermiticities. The article establishes this and states what it does and does not buy.

- **Established, and recomputed below.** The Hermiticity of the insertions, the Hodge duality $\frac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\varepsilon_\rho\varepsilon_\sigma\sigma_{\rho\sigma}=-\sigma_{\mu\nu}(-iR_{\vec e_z})$, the signature-weighted sum defined below, and the resulting sector placement. The $\vec E$-coupling insertion $\sigma_{0k}(-iR_{\vec e_z})$ is anti-Hermitian (recomputed), hence material; the $\vec B$-coupling insertion $\sigma_{ij}$ is Hermitian, hence informational. The EDM Lagrangian is Hermitian because the explicit $i$ compensates the anti-Hermiticity, and that $i$ is the framework's marker of the CP-odd coefficient.
- **Standard, transcribed.** The definition of the EDM, its $\mathbf{P}$-, $\mathbf{T}$-, and $\mathbf{CP}$-odd character, the nonrelativistic limit, the form-factor decomposition of the electromagnetic vertex, the Standard Model prediction (CKM-suppressed and tiny), the $\theta$-term contribution, and the experimental bounds are standard. They are stated in the framework's notation.
- **Gap, left visible.** The framework supplies the operator and its sector, and it does not supply the coefficient. It has no CP-violating phase of its own, no mechanism to generate one, and no prediction for the electron, neutron, or proton EDM. The value of $d$ is an empirical input, and the framework's statement is the structural one: a nonzero EDM is the presence of a coefficient on an anti-Hermitian, material-sector insertion.

The sections that follow fix the operator, its dimension, and the size of the effect. A section establishes the Hermiticity of the insertions, the Hodge duality, and the dictionary that makes the placement exact. A section derives the nonrelativistic limit. A section tabulates the discrete symmetries of the insertions. A section gives the form-factor decomposition and the two coefficients. A section treats the CP-odd phase. A section collects the bounds and the scales, and a closing section separates what the framework supplies from what it transcribes and what it lacks.

**The metric and the field strength.** The frame metric and the components are

$$
g=\mathrm{diag}(+1,-1,-1,-1),\qquad
\varepsilon_\rho=g_{\rho\rho},\qquad
\epsilon_{0123}=+1,\qquad
F_{0i}=E_i,\qquad
F_{ij}=-\epsilon_{ijk}B_k ,
$$

so that $\varepsilon_0=+1$ and $\varepsilon_k=-1$. The metric is its own inverse. The two signs of $\varepsilon$ are not decoration: they are what turns a lower pair of indices into an upper pair, and they appear in the duality of the insertions for that reason.

**The chirality cell and the volume element.** The chirality cell is the central imaginary times the volume element $\omega$, the ordered product of the four frame cells,

$$
-iR_{\vec e_z}=i\omega,\qquad
\omega=iR_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y},
$$

and the product collapses because four factors of $i$ multiply to $i^4=+1$, the four left multipliers to $-e_t$, and the four right multipliers to $\vec e_z$ in that order,

$$
\omega=-R_{\vec e_z},\qquad \omega^2=-e_t .
$$

The square $\omega^2=-e_t$ is the reason $\omega$ is called the volume element: it is the cell that plays the part of the scalar imaginary $i$, with $i^2=-1$.

**The two Dirac equations.** The mass is the linear Dirac pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R ,
$$

and the two lines are two equations, not one. Each is one-sided — the algebra acts by left multiplication on a field of the module — and the pair is the chirality split of a single operator: the left-handed equation and the right-handed equation, coupled by the mass. The second member uses the conjugate gradient $\tilde{\nabla}^{\natural}$, a different element of the algebra; it is not the conjugate of the field, and the antilinear real structure $\flat=-{}^{*}$ is a third object, separate from both.

**Units.** Natural units $\hbar=c=1$ are used, and the EDM unit conversion is $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$.

The framework results used here are those of the companion articles:

- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the Dirac module and the bilinears built on it.
- Companion article *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, for the identification of the Clifford generators with the biquaternion basis.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the mass-term conventions and the real structure $\flat$.
- Companion article *The Proton in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.
- Companion article *The Neutron in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.

## The EDM Operator and Its Dimension

**The interaction.** The EDM is a CP-odd coupling of the electromagnetic field strength to the spin. Its Lorentz-covariant form is

$$
\mathcal{L}_{\mathrm{EDM}} = -\frac{i}{2}\,d\,\bar{\psi}\sigma_{\mu\nu}(-iR_{\vec e_z})\psi F_{\mu\nu},
$$

and its nonrelativistic limit is the Hamiltonian

$$
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma}.
$$

The explicit $i$ is required for a Hermitian Lagrangian, and it is the first appearance of the article's central point: the insertion is anti-Hermitian, and the coefficient must be multiplied by $i$ to give a real (Hermitian) interaction.

**The dimension and the size.** The EDM has the dimensions of electric charge times length. In natural units, $d$ is dimensionless times a length, i.e. $[\mathrm{GeV}^{-1}]$, with the conversion given in the Introduction. For a fermion of mass $m_f$ and a new-physics scale $\Lambda$, the standard dimensional estimate of a CP-violating contribution is

$$
d \sim \frac{e\,m_f}{\Lambda^2}\,\sin\varphi ,
$$

where $\varphi$ is the CP-odd phase. The estimate is the one that governs the reach of the experiments: the smaller the bound, the larger the scale probed, and the heavier the fermion, the larger the contribution. The numbers are used in the last section.

**The observable.** A permanent EDM precesses in an electric field, and the precession is what the experiments measure — in atoms and molecules, in stored neutrons, and in storage rings. The observable is the coefficient of $\vec E\cdot\boldsymbol{\sigma}$, the leading CP-odd electromagnetic coupling of a spin-$\tfrac12$ particle. The framework's proton and neutron articles treat those composites and note that the framework supplies no value for their EDMs; this article treats the operator and its structure.

## The Anti-Hermitian Structure of $\sigma_{\mu\nu}(-iR_{\vec e_z})$

**The Hermiticity of the insertions.** With the block representation and $g=\mathrm{diag}(+1,-1,-1,-1)$, the generators of the Lorentz algebra split into the boosts and the rotations,

$$
\sigma_{0k}\ \text{(anti-Hermitian)},\qquad
\sigma_{ij}\ \text{(Hermitian)},
$$

and the chirality cell does not change the pattern, because it commutes with every bivector,

$$
\sigma_{0k}(-iR_{\vec e_z})\ \text{(anti-Hermitian)},\qquad
\sigma_{ij}(-iR_{\vec e_z})\ \text{(Hermitian)}.
$$

The pattern follows from three facts about the frame. The timelike cell $iR_{\vec e_x}$ is Hermitian, the three spatial cells $iL_{\vec e_k}R_{\vec e_y}$ are anti-Hermitian, and the chirality cell $-iR_{\vec e_z}$ is Hermitian and anticommutes with each of the four. Two anticommuting cells of the same class multiply to an anti-Hermitian matrix, and two of opposite classes to a Hermitian one, since $(AB)^\dagger=B^\dagger A^\dagger=-BA$ is $-AB$ in the first case and $+AB$ in the second. The product of the timelike cell with a spatial one is therefore Hermitian, and the product of two spatial cells anti-Hermitian; multiplying by the $i$ of $\sigma_{\mu\nu}$ gives $\sigma_{0k}$ anti-Hermitian and $\sigma_{ij}$ Hermitian. The chirality cell commutes with both bivectors, because it anticommutes with each cell and a bivector is a product of two, so multiplying by it leaves each Hermiticity unchanged. **The $\vec E$-coupling insertion is the anti-Hermitian one.**

**The Hodge duality.** The two families of insertions are dual to each other. With the totally antisymmetric symbol, the explicit sum over the pair, and the two signature signs that an upper pair carries,

$$
\boxed{\;\frac{1}{2}\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\,\varepsilon_\rho\varepsilon_\sigma\,\sigma_{\rho\sigma}
= -\,\sigma_{\mu\nu}(-iR_{\vec e_z})\;}
$$

an identity verified for all sixteen ordered pairs with residual exactly zero. The sum is the Hodge dual of the bivector, and on the two families it acts as

$$
\star\sigma_{0k}=\frac{1}{2}\sum_{\rho,\sigma}\epsilon_{0k\rho\sigma}\,\varepsilon_\rho\varepsilon_\sigma\,\sigma_{\rho\sigma} = -\,i\,\sigma_{\lambda\mu},
\qquad
\star\sigma_{\lambda\mu}=+\,i\,\sigma_{0k},
$$

where $(\lambda,\mu)$ is the spatial pair complementary to $k$, so that $(0,k,\lambda,\mu)$ is an even permutation of the frame; both statements were checked component by component. The two directions carry opposite factors $i$, so the sum is an involution, $\star\star=1$: the product $(-i)(+i)=+1$ is what makes the round trip the identity. The EDM insertion is minus the dual of the tensor, and the dual of the EDM insertion is minus the tensor.

**The duality and the Hermiticity.** Each single passage supplies the factor $i$ that reconciles the two classes, and that factor is the origin of the $i$ in the EDM Lagrangian. The electric bivectors $\sigma_{0k}$ are anti-Hermitian and the magnetic ones $\sigma_{ij}$ Hermitian; the dual of an electric bivector is $-i$ times a magnetic one, and $-i$ times a Hermitian matrix is anti-Hermitian, so the dual stays in the class of the bivector it came from. The dual of a magnetic bivector is $+i$ times an electric one, and $i$ times an anti-Hermitian matrix is Hermitian, the same statement in the other direction. The duality therefore exchanges the two families and keeps each class; the $i$ is what makes the two facts compatible.

**The two signature signs.** They are what make the identity exact. The plain contraction $\frac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\sigma_{\rho\sigma}$ agrees with the weighted one on the pairs with a timelike index and has the opposite sign on the pairs that are purely spatial, because the complementary pair is spatial in the first case and mixed in the second.

**The sector placement.** The insertions are even elements of the Clifford algebra: the unit, the six bivectors $\sigma_{\mu\nu}$ and the chirality cell $-iR_{\vec e_z}$. The companion *Matrix Representations Conventions* identifies the even Clifford algebra with the biquaternion algebra, $\mathrm{Cl}^{+}_{1,3}(\mathbb{R})\cong\mathbb{B}$, and under that dictionary the framework's sector split is the Hermiticity split: Hermitian elements are the informational sector $\mathbb{M}_+$ and anti-Hermitian elements the material sector $\mathbb{M}_-$. Complexified, it is $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, the two chiral halves, because the chirality cell commutes with every even element and splits the algebra; the sector split is not that split, it is the split by Hermiticity. Applied to the insertions:

| Insertion | Term it carries | Hermiticity | Sector |
|---|---|---|---|
| $\sigma_{ij}$ | the magnetic moment, $\vec B$ | Hermitian | $\mathbb{M}_+$ |
| $\sigma_{ij}(-iR_{\vec e_z})$ | its dual | Hermitian | $\mathbb{M}_+$ |
| $\sigma_{0k}(-iR_{\vec e_z})$ | the EDM, $\vec E$ | anti-Hermitian | $\mathbb{M}_-$ |
| $\sigma_{0k}$ | the bare tensor component | anti-Hermitian | $\mathbb{M}_-$ |

The EDM insertion is therefore the anti-Hermitian, material-sector insertion, and the magnetic-moment insertion is its Hermitian, informational-sector dual. This is the article's central structural statement; it was verified entry by entry in the block basis. The bare $\sigma_{0k}$ is anti-Hermitian as well, and it is listed only for completeness: it is not gauge invariant by itself, and only its contraction with $F$ is an operator.

**The dictionary form of the EDM insertion.** The placement can be made exact rather than a Hermiticity match. The dictionary that carries the biquaternion basis to the Clifford generators is $\mathbb{R}$-linear on the eight real units,

$$
e_t\mapsto L_{e_t}R_{e_t}=I_4,\qquad
\vec e_k\mapsto L_{\vec e_k}R_{e_t},\qquad
i\vec e_k\mapsto L_{\vec e_k}R_{\vec e_z},
$$

and each image of a spatial unit is itself a product of two frame cells, $\vec e_x\mapsto iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y}$ and cyclically. On this dictionary the EDM insertion *is* the image of a basis element of the material sector:

$$
\boxed{\;\sigma_{0k}(-iR_{\vec e_z}) = -\,L_{\vec e_k}R_{e_t}\;}
$$

verified for $k=1,2,3$ with residual exactly zero. The EDM insertion is thus not merely anti-Hermitian and therefore material; up to a sign it is the Clifford image of one of the three vector basis elements $\vec e_k$ of $\mathbb{M}_-$ — the same elements that carry the spatial directions of the material sector. The rotation insertions are the central imaginary times those same images, $\sigma_{ij}=iL_{\vec e_m}R_{e_t}$ with $m$ the third spatial index, and since multiplication by the central $i$ exchanges the sectors, $i\mathbb{M}_-=\mathbb{M}_+$, the insertion is read in the informational sector. The scalar $i$ and the cell $i\vec e_k$ are different objects: the dictionary is $\mathbb{R}$-linear, so the image of $i\vec e_k$ is the cell $L_{\vec e_k}R_{\vec e_z}$ and not $i$ times $L_{\vec e_k}R_{e_t}$. The correspondence is a statement about the objects the insertion represents, in the sense of the convention that reads the sectors on the fields; the sectors are real vector spaces on which the algebra acts rather than subalgebras, and a general element of the even Clifford algebra need not fall in one of them.

**The $i$ and the Hermiticity of the Lagrangian.** Because the EDM insertion is anti-Hermitian, the bilinear $\bar{\psi}\sigma_{0k}(-iR_{\vec e_z})\psi$ is anti-Hermitian as a classical bilinear, and the Lagrangian density $-\tfrac{i}{2}d\,\bar{\psi}\sigma_{\mu\nu}(-iR_{\vec e_z})\psi F_{\mu\nu}$ is Hermitian for real $d$ precisely because the explicit $i$ makes $i\times(\text{anti-Hermitian})$ Hermitian. The magnetic-moment Lagrangian has no such $i$, because its insertion is already Hermitian. **The factor of $i$ is the biquaternion signature of the EDM**: the operator is the CP-odd member of a dual pair, its material-sector placement is the anti-Hermiticity, and the Hermiticity of the action is restored by the central imaginary.

## The Nonrelativistic Reduction

**From the covariant operator to $-d\,\vec E\cdot\boldsymbol{\sigma}$.** The EDM coupling reduces to the nonrelativistic Hamiltonian through one identity of the frame,

$$
\sigma_{0k}(-iR_{\vec e_z}) = i\,\Sigma_k ,
\qquad
(\Sigma_k)^\dagger=\Sigma_k,
\qquad
(\Sigma_k)^2=I_4,
\qquad
\operatorname{tr}\Sigma_k=0,
$$

$$
\{\Sigma_i,\Sigma_j\}=2\delta_{ij}I_4,
\qquad
[\Sigma_i,\Sigma_j]=2i\,\epsilon_{ijk}\Sigma_k ,
$$

verified for the three components. The three $\Sigma_k$ are therefore a Pauli triplet on the module: Hermitian, traceless, unitary, pairwise anticommuting, and closing on $i\epsilon_{ijk}$. The identity shows both facts at once — that $\sigma_{0k}(-iR_{\vec e_z})$ is $i$ times a Hermitian matrix, hence anti-Hermitian, and that the matrix it multiplies is the spin. In the cell basis used here only the first of the three has the block form, $\Sigma_1=\mathrm{diag}(\sigma_2,\sigma_2)$; which Pauli matrix is attached to which spatial direction is a labelling of the frame, and the algebra above is the invariant statement.

**The factor of two and the sign.** The sum over the pair $(\mu,\nu)$ counts the electric pair twice, as $(0,k)$ and as $(k,0)$, and the two contributions are equal, because $\sigma_{k0}=-\sigma_{0k}$ and $F_{k0}=-F_{0k}$ change sign together. With $F_{0k}=E_k$ the Lagrangian therefore contains

$$
\mathcal{L}_{\mathrm{EDM}} \supset -\,i\,d\,E_k\,\bar{\psi}\,\sigma_{0k}(-iR_{\vec e_z})\psi .
$$

Substituting the spin identity and multiplying the two factors of $i$, with $i^2=-1$,

$$
-\,i\,d\,E_k\,\bar{\psi}\,(i\Sigma_k)\psi
= -\,i^2\,d\,E_k\,\bar{\psi}\Sigma_k\psi
= +\,d\,E_k\,\bar{\psi}\Sigma_k\psi .
$$

On the upper (positive-energy) components the bilinear $\bar{\psi}\Sigma_k\psi$ reduces to the spin density $\psi^\dagger\sigma_k\psi$, so

$$
\mathcal{L}_{\mathrm{EDM}} \;\longrightarrow\; d\,\vec E\cdot(\psi^\dagger\boldsymbol{\sigma}\psi),
\qquad
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma},
$$

the stated nonrelativistic limit. The chain is a derivation of the limit from the covariant operator, and it exhibits the $i$ of the Lagrangian turning into the $i$ of $\sigma_{0k}(-iR_{\vec e_z})$. The magnetic-moment coupling reduces in the same way with $\sigma_{ij}$ and the field $\vec B$, but with a Hermitian insertion and no compensating $i$.

**The spin operator and the sector.** The spin operator $\Sigma_k$ is Hermitian and lies in the informational sector $\mathbb{M}_+$, and the EDM insertion is $i$ times it: the material-sector insertion is the central imaginary times the informational-sector spin. This is the algebraic statement of the CP-odd character of the EDM in the framework's language — the observable couples to the spin, and the coupling is made CP-odd by the central imaginary that moves the operator into the material sector.

## The Discrete Symmetries of the Insertions

**The transformation of the two terms.** Under parity $\mathbf{P}$ the electric field is a vector, $\vec E\to-\vec E$, and the spin is a pseudovector, $\boldsymbol{\sigma}\to+\boldsymbol{\sigma}$, so $\vec E\cdot\boldsymbol{\sigma}\to-\vec E\cdot\boldsymbol{\sigma}$: the EDM term is $\mathbf{P}$-odd. Under time reversal $\mathbf{T}$ the electric field is even and the spin odd, so the term is odd again. Under charge conjugation $\mathbf{C}$ the field strength and the bilinear both change sign, and the term is even. The EDM is therefore $\mathbf{P}$- and $\mathbf{T}$-odd, and by the CPT theorem $\mathbf{CP}$-odd. The magnetic term $-\vec\mu\cdot\vec B$ is even under all three. The contrast is exact, and it is the chirality cell that carries it: the two operators differ by the cell $-iR_{\vec e_z}$, and removing or restoring that cell is what flips the parity.

**The bilinears.** The Dirac bilinears come in four shapes, and the chirality cell pairs them: the vector with the axial, the tensor with the pseudotensor. They are

$$
\text{(vector)}\ \bar{\psi}\,iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\psi,\qquad
\text{(tensor)}\ \bar{\psi}\sigma_{\mu\nu}\psi,
$$

$$
\text{(axial)}\ \bar{\psi}\,iL_{e_\mu}R_{\vec e_{\nu(\mu)}}(-iR_{\vec e_z})\psi,\qquad
\text{(pseudotensor)}\ \bar{\psi}\sigma_{\mu\nu}(-iR_{\vec e_z})\psi .
$$

A bilinear with free indices has no parity of its own, since its timelike and its spatial components transform oppositely; the parities are therefore those of the gauge-invariant operators, bilinear times field:

| Operator | Bilinear | $\mathbf{P}$ | $\mathbf{T}$ | $\mathbf{C}$ | $\mathbf{CP}$ | Insertion |
|---|---|---|---|---|---|---|
| $\bar{\psi}\,iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\psi\,A^\mu$ (charge) | vector | even | even | even | even | $iR_{\vec e_x}$ (Hermitian) |
| $\bar{\psi}\sigma_{\mu\nu}\psi\,F_{\mu\nu}$ (magnetic) | tensor | even | even | even | even | $\sigma_{ij}$ (Hermitian) |
| $i\,\bar{\psi}\sigma_{\mu\nu}(-iR_{\vec e_z})\psi\,F_{\mu\nu}$ (EDM) | pseudotensor | odd | odd | even | odd | $\sigma_{0k}(-iR_{\vec e_z})$ (anti-Hermitian) |

The EDM is the tensor bilinear with the axial factor, and the table is the parity bookkeeping of the Hodge duality: the chirality cell flips the parity and the CP character, and the factor $i$ that the duality carries is what keeps the Hermiticity class.

**Two operators, not four.** The list has two entries because the tensor and the pseudotensor are one operator up to the factor $i$ of the duality: the dual of $\bar{\psi}\sigma_{\mu\nu}\psi$ is $-\bar{\psi}\sigma_{\mu\nu}(-iR_{\vec e_z})\psi$, and contracting either with $F$ or with its dual reproduces the same pair of terms up to $i$. A Hermitian Lagrangian therefore carries two independent dimension-five couplings, the magnetic one with a real coefficient and the EDM one with a coefficient multiplied by $i$; the other two combinations are their conjugates. This is why the EDM is *the* CP-odd electromagnetic observable at this order, and why its bound is the sharpest test of new CP violation in the fermion sector. The anapole and the charge-radius terms join the list one dimension higher, are CP-even, and are not dipole moments.

**The framework's real structure and CP.** The framework's conjugation enters the bilinears through the module's real structure: a CP transformation is a charge conjugation accompanied by a parity reflection, and in the module language it uses the antilinear real structure. The EDM's bilinear is the one that changes sign under this operation, and the coefficient $id$ with real $d$ is what keeps the action invariant. The framework statement is therefore precise: the EDM is the coefficient of a CP-odd, anti-Hermitian, material-sector bilinear, and its measurement is the measurement of a central imaginary's coupling to the spin.

## The Form Factors and the Two Coefficients

**The electromagnetic vertex.** The most general gauge-invariant vertex of an on-shell spin-$\tfrac12$ particle with the electromagnetic field, at momentum transfer $k=p_2-p_1$, is

$$
\Gamma_\mu(p_2,p_1) = iL_{e_\mu}R_{\vec e_{\nu(\mu)}} F_1(k^2) + \frac{i}{2m}\,\sigma_{\mu\nu}k_\nu\,F_2(k^2)
+ \frac{i}{2m}\,\sigma_{\mu\nu}(-iR_{\vec e_z})k_\nu\,F_3(k^2) + \cdots ,
$$

with $F_1$ the charge, $F_2$ the anomalous magnetic moment, and $F_3$ the EDM form factor; the ellipsis denotes the anapole and higher terms. In the nonrelativistic limit, $F_2$ and $F_3$ reduce to the magnetic and electric dipole couplings,

$$
H_{\mathrm{NR}} = -\,\mu\,\vec B\cdot\boldsymbol{\sigma} - d\,\vec E\cdot\boldsymbol{\sigma},
$$

$$
\mu = \frac{e}{2m}\big(1+F_2(0)\big),\qquad d = \frac{e}{2m}F_3(0),
$$

so that the two coefficients are the form factors at zero momentum transfer, multiplied by the same dimensionful factor and distinguished by the chirality cell. The magnetic moment is the Hermitian member of the pair; the EDM is the anti-Hermitian member; and the two are Hodge duals of each other. This is the standard form-factor decomposition, and it is the reason the EDM is called the "dual" of the anomalous magnetic moment.

**Why the dual is the CP-odd one.** The form-factor pair $(F_2,F_3)$ is the framework's Hermitian/anti-Hermitian pair, and the two differ by the insertion of the chirality cell. The magnetic term has $F_2$ and no chirality cell; the EDM term has $F_3$ and one chirality cell. Under the Hodge duality the EDM insertion is minus the dual of the magnetic one, and the factor $i$ that the duality carries in each direction is what makes the EDM's coefficient CP-odd and the magnetic moment's coefficient CP-even. The framework does not compute $F_3$; it places it in the anti-Hermitian sector, and the vanishing of $F_3$ leaves the pair $(F_2,F_3)$ wholly in the informational sector, which is the CP-even statement.

**The magnetic moment as the calibration.** The anomalous magnetic moment $F_2$ is measured to extraordinary precision, and its theoretical value is the framework's testing ground for the fermion sector; the companion article on the anomalous magnetic moment computes the framework's contribution. The EDM is the dual observable, and its bound reaches scales that the magnetic moment cannot probe.

## CP Violation and the Origin of the Phase

**Where a nonzero EDM comes from.** The EDM is CP-odd, so it can be generated only by a CP-violating interaction. The candidates are standard:

- **The CKM phase.** In the Standard Model the only CP-violating parameter of the quark sector is the phase of the Cabibbo–Kobayashi–Maskawa matrix; the companion article on the CKM matrix treats it. Its contribution to the neutron EDM arises only at the three-loop level and is of order $d_n\sim10^{-32}\ e\cdot\mathrm{cm}$, far below the present bound; the CKM phase is not the source of any measurable hadronic or atomic EDM.
- **The $\theta$ parameter.** Quantum chromodynamics admits a CP-odd topological term

    $$
    \theta\,\frac{\alpha_s}{8\pi}\,\epsilon_{\mu\nu\rho\sigma}G_{a\mu\nu}G_{a\rho\sigma},
    $$

    whose contribution to the neutron EDM is of order $d_n\sim\theta\times10^{-16}\ e\cdot\mathrm{cm}$; the bound on $d_n$ forces $|\theta|\lesssim10^{-10}$. The $\theta$ parameter belongs to the corpus's general gauge apparatus and is not developed here; the fermion-sector statement is that the EDM is where the $\theta$ problem is measured.
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

**The scales they probe.** The dimensional estimate $d\sim e\,m_f\sin\varphi/\Lambda^2$ converts the bounds into a reach. Since $d$ is quoted in units of $e\cdot\mathrm{cm}$, the charge is factored out of the number and the estimate is used in the form

$$
\frac{d}{e} \sim \frac{m_f}{\Lambda^2}\,\sin\varphi .
$$

For the electron, $m_e=0.511\ \mathrm{MeV}=5.11\times10^{-4}\ \mathrm{GeV}$, and the conversion $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$ was used; the numbers were recomputed,

$$
\frac{m_e}{(1\ \mathrm{TeV})^2} = 5.11\times10^{-10}\ \mathrm{GeV}^{-1} = 1.0\times10^{-23}\ \mathrm{cm},
$$

where the length is also the number of $e\cdot\mathrm{cm}$ that the bound quotes, since $d/e$ is what that unit measures. A new-physics scale of $1$ TeV with an order-one CP phase would give an electron EDM some six orders of magnitude above the present bound. Reproducing the bound $1.1\times10^{-29}\ e\cdot\mathrm{cm}$ requires the scale to be larger by the square root of the ratio, $\sqrt{9\times10^{5}}\simeq950$, i.e.

$$
\Lambda \gtrsim 10^{3}\ \mathrm{TeV}
$$

for an order-one phase and no loop suppression. This is the standard statement that the electron EDM probes scales up to a few thousand TeV, which is why it is a leading constraint on new physics and why it is the target of the next generation of experiments. The neutron and proton bounds probe their own combinations of quark and gluon CP-odd operators, and the framework's proton and neutron articles state that no value is predicted.

**The magnetic moment for comparison.** The anomalous magnetic moment of the muon is measured to a precision of about half a part per million and its theoretical uncertainty is dominated by hadronic effects; the companion article treats it. The EDM bounds are in a different regime: the electron EDM bound corresponds to a dipole moment about $5.7\times10^{-19}$ of the electron's magnetic moment, since $\mu_e/e=1/(2m_e)=1.93\times10^{-11}\ \mathrm{cm}$ and $d_e/e\lesssim1.1\times10^{-29}\ \mathrm{cm}$. The two observables are the Hermitian and anti-Hermitian members of the same dimension-five pair, and the framework places them in the informational and material sectors respectively.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The even Clifford algebra as the biquaternion algebra, and the Hermiticity sector split | **Supplied**; Hermitian is $\mathbb{M}_+$, anti-Hermitian is $\mathbb{M}_-$ |
| The EDM insertion $\sigma_{0k}(-iR_{\vec e_z})$ as anti-Hermitian, material-sector | **Supplied**, recomputed entry by entry |
| The magnetic-moment insertion $\sigma_{ij}$ as Hermitian, informational-sector | **Supplied**, recomputed |
| The Hodge duality $\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\varepsilon_\rho\varepsilon_\sigma\sigma_{\rho\sigma}=-\sigma_{\mu\nu}(-iR_{\vec e_z})$, an involution exchanging the two families | **Supplied**, recomputed for all sixteen ordered pairs |
| The dictionary form $\sigma_{0k}(-iR_{\vec e_z})=-L_{\vec e_k}R_{e_t}$, the image of $-\vec e_k\in\mathbb{M}_-$ | **Supplied**, recomputed for the three spatial directions |
| The explicit $i$ in the EDM Lagrangian as the marker of the anti-Hermitian insertion | **Supplied** by the algebra |
| The definition of the EDM and its $\mathbf{P}$-, $\mathbf{T}$-, $\mathbf{CP}$-odd character | **Transcribed**; standard |
| The form-factor decomposition and the nonrelativistic limit | **Transcribed**; standard |
| The CKM and $\theta$-term contributions, and their smallness | **Standard**; the $\theta$ parameter belongs to the general gauge apparatus |
| The experimental bounds and the reach $\Lambda\gtrsim10^{3}$ TeV | **Transcribed**; standard, with the arithmetic recomputed |
| The value of $d$ for any particle | **Not supplied**; empirical |
| A CP-violating phase, and its origin | **Not supplied**; the framework has none |
| The electron, neutron, and proton EDMs as framework predictions | **Not supplied**; the composite articles state the same |

## Open Questions

1. **The dictionary's sharpness.** The identification of the Hermitian and anti-Hermitian insertions with the sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ is used here as the framework's stated dictionary. For the EDM insertion the placement is exact: $\sigma_{0k}(-iR_{\vec e_z})=-L_{\vec e_k}R_{e_t}$ is the image of a basis element of $\mathbb{M}_-$, and the rotation insertions are the central imaginary times the image of $\vec e_k$, read in the informational sector through $i\mathbb{M}_-=\mathbb{M}_+$. Whether the *full* even Clifford algebra, including the unit and the chirality cell, decomposes into the two sectors, or only up to the central factor that changes Hermiticity, is a separate question of the algebra's presentation: the unit $e_t$ is Hermitian while $-iR_{\vec e_z}$ is central, so neither is selected by the split, and a general Hermitian element of the even Clifford algebra need not be the image of an element of $\mathbb{M}_+$.

2. **The phase's sector.** A CP-odd phase multiplying the material-sector insertion is an imaginary coefficient. Whether the framework can distinguish phases that sit in the mass matrix from phases that sit in the dipole coefficients, and whether the abelian gauge-sector field strength of the framework supplies a $\theta$-like invariant, is not settled here and belongs partly to the general gauge apparatus.

3. **The composite EDMs.** The neutron and proton EDMs are matrix elements of quark and gluon CP-odd operators, and their computation is nonperturbative. The framework's proton and neutron articles supply no value; whether a biquaternion treatment of the bound-state problem can be given is open and lies outside the fermion sector.

4. **The duality at the level of the action.** The Hodge duality relates the EDM and magnetic insertions with a factor of $i$; whether the framework's action can be written so that the duality is manifest, pairing the two observables in a single Hermitian structure, is a question of the action's algebraic form.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\qquad
\gamma_1=iL_{\vec e_x}R_{\vec e_y},\qquad
\gamma_2=iL_{\vec e_y}R_{\vec e_y},\qquad
\gamma_3=iL_{\vec e_z}R_{\vec e_y},\qquad
\gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

The five are generators, not a basis: the basis is the sixteen products. A single product is a pure tensor, and the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$; a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$. A product of cells is again a cell, and that closure is why the sixteen products span the algebra.

$\gamma_5$ is the reference-frame cell of the chirality operator. The central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is $\mathbb{R}$-linear, not $\mathbb{C}$-linear; over $\mathbb{R}$ the sixteen products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, two real Clifford algebras of real dimension sixteen each.

**The identities.** With $\epsilon_{0123}=+1$,

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

**The four contractions.** They are frame statements, since a product of cells is again a cell, and the weight $\varepsilon$ is what carries the metric into the sum:

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4g_{\alpha\beta}I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\rho\gamma_\mu=-2\gamma_\rho\gamma_\beta\gamma_\alpha .
$$

In the $\mathbb{B}$ frame every cell squares to $+I_4$, the weight is $+1$, and the same four sums give $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\rho\gamma_\beta\gamma_\alpha$. The unweighted sum $\sum_\mu\gamma_\mu\gamma_\mu$ equals $-2I_4$ in the frame used here and $+4I_4$ in the $\mathbb{B}$ frame; it is a third object, not one of the four.

## Summary

The electric dipole moment is the CP-odd, dimension-five coupling of a spin-$\tfrac12$ particle to the electromagnetic field,

$$
\mathcal{L}_{\mathrm{EDM}} = -\,\frac{i}{2}\,d\,\bar{\psi}\,\sigma_{\mu\nu}(-iR_{\vec e_z})\,\psi\,F_{\mu\nu},
\qquad
H_{\mathrm{NR}} = -\,d\,\vec E\cdot\boldsymbol{\sigma}.
$$

In the biquaternion framework its insertion has a definite algebraic character: the $\vec E$-coupling insertion $\sigma_{0k}(-iR_{\vec e_z})$ is **anti-Hermitian** and therefore lies in the material sector $\mathbb{M}_-$, while the $\vec B$-coupling magnetic-moment insertion $\sigma_{ij}$ is **Hermitian** and lies in the informational sector $\mathbb{M}_+$; both statements were recomputed entry by entry in the block basis. The two are Hodge duals,

$$
\boxed{\;\frac{1}{2}\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\,\varepsilon_\rho\varepsilon_\sigma\,\sigma_{\rho\sigma}
=-\,\sigma_{\mu\nu}(-iR_{\vec e_z}),\qquad
\star\sigma_{0k}=-i\,\sigma_{\lambda\mu},\quad \star\sigma_{\lambda\mu}=+i\,\sigma_{0k}\;}
$$

verified for all sixteen ordered pairs with residual exactly zero. The duality is an involution that exchanges the two families with opposite factors $i$, so the EDM insertion is minus the dual of the tensor, and each passage carries the $i$ that keeps the Hermiticity class. The explicit $i$ in the EDM Lagrangian is what makes $i\times(\text{anti-Hermitian})$ Hermitian, and it is the algebra's marker of the CP-odd coefficient; the dictionary form $\sigma_{0k}(-iR_{\vec e_z})=-L_{\vec e_k}R_{e_t}$ makes the placement exact, the insertion being the image of $-\vec e_k\in\mathbb{M}_-$.

The form-factor decomposition

$$
\Gamma_\mu=iL_{e_\mu}R_{\vec e_{\nu(\mu)}}F_1+\frac{i}{2m}\sigma_{\mu\nu}k_\nu F_2+\frac{i}{2m}\sigma_{\mu\nu}(-iR_{\vec e_z})k_\nu F_3+\cdots
$$

exhibits the magnetic moment $F_2$ and the EDM $F_3$ as the Hermitian and anti-Hermitian members of one dimension-five pair, which the framework places in the informational and material sectors; they are the whole list, the pseudotensor being the tensor times $i$ under the duality. The framework does not supply the coefficient: it has no CP-violating phase, predicts no measurable EDM, and inherits the Standard Model's tiny CKM contribution and the $\theta$-term constraint, $|\theta|\lesssim10^{-10}$ from $|d_n|\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$. The present electron bound $|d_e|\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$, combined with the dimensional estimate $d/e\sim m_e\sin\varphi/\Lambda^2$, probes new-physics scales $\Lambda\gtrsim10^{3}$ TeV, and the framework's contribution is to state exactly where in the algebra such a coefficient would sit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$; the even Clifford algebra $\mathrm{Cl}^{+}_{1,3}(\mathbb{R})$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi=a\psi b$ | Two-sided cell: left multiplication by $a$, right by $b$ |
| $iL_{e_t}R_{\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}$, $-iL_{e_t}R_{\vec e_z}$ | Frame cells; the last is the chirality cell $-iR_{\vec e_z}$ |
| $\sigma_{\mu\nu}=\tfrac{i}{2}[iL_{e_\mu}R_{\vec e_{\nu(\mu)}},iL_{e_\nu}R_{\vec e_{\nu(\nu)}}]$ | Lorentz generators; $\nu(t)=x$, $\nu(k)=y$ |
| $\omega=-R_{\vec e_z}$, $\omega^2=-e_t$ | Volume element, the product of the four frame cells; $-iR_{\vec e_z}=i\omega$ |
| $\varepsilon_\rho=g_{\rho\rho}$ | Signature sign; with $g=\mathrm{diag}(+1,-1,-1,-1)$, $\varepsilon_0=+1$ and $\varepsilon_k=-1$ |
| $\sigma_{0k}$, $\sigma_{0k}(-iR_{\vec e_z})$ | Anti-Hermitian, $\mathbb{M}_-$; the second is the EDM insertion |
| $\sigma_{ij}$, $\sigma_{ij}(-iR_{\vec e_z})$ | Hermitian, $\mathbb{M}_+$; the magnetic insertion and its dual |
| $\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\varepsilon_\rho\varepsilon_\sigma\sigma_{\rho\sigma}=-\sigma_{\mu\nu}(-iR_{\vec e_z})$ | Hodge dual of the bivector; $\star\star=1$ |
| $\star\sigma_{0k}=-i\sigma_{\lambda\mu}$, $\star\sigma_{\lambda\mu}=i\sigma_{0k}$ | The dual on the two families; $(\lambda,\mu)$ is the pair complementary to $k$ |
| $e_t\mapsto I_4$, $\vec e_k\mapsto L_{\vec e_k}R_{e_t}$, $i\vec e_k\mapsto L_{\vec e_k}R_{\vec e_z}$ | The dictionary, $\mathbb{R}$-linear |
| $\sigma_{0k}(-iR_{\vec e_z})=-L_{\vec e_k}R_{e_t}$ | The EDM insertion as the image of $-\vec e_k\in\mathbb{M}_-$ |
| $-\tfrac{i}{2}d\,\bar{\psi}\sigma_{\mu\nu}(-iR_{\vec e_z})\psi F_{\mu\nu}$ | EDM Lagrangian |
| $H_{\mathrm{NR}}=-d\,\vec E\cdot\boldsymbol{\sigma}$ | EDM nonrelativistic Hamiltonian |
| $F_1,F_2,F_3$ | Charge, anomalous magnetic moment, EDM form factors |
| $d=\tfrac{e}{2m}F_3(0)$, $\mu=\tfrac{e}{2m}(1+F_2(0))$ | EDM and magnetic moment |
| $d/e\sim m_f\sin\varphi/\Lambda^2$ | Dimensional estimate, the charge factored out of the $e\cdot\mathrm{cm}$ unit |
| $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$ | EDM unit conversion |
| $|d_e|\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$ | Electron EDM bound |
| $|d_n|\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$ | Neutron EDM bound |

## Further Reading

- L. I. Schiff, "Measurability of nuclear electric dipole moments," *Physical Review* **132** (1963) 2194–2200, for the atomic-physics theorem on the screening of nuclear EDMs.
- W. Bernreuther and M. Suzuki, "The electric dipole moment of the electron," *Reviews of Modern Physics* **63** (1991) 313–340, for the electron EDM and its theory.
- I. B. Khriplovich and S. K. Lamoreaux, *CP Violation Without Strangeness* (Springer, 1997), for electric dipole moments of particles, atoms, and molecules.
- J. Engel, M. J. Ramsey-Musolf, and U. van Kolck, "Electric dipole moments of nucleons, nuclei, and atoms: the Standard Model and beyond," *Progress in Particle and Nuclear Physics* **71** (2013) 21–74, for the hadronic and nuclear EDMs and the $\theta$-term contribution.
- T. Chupp, P. Fierlinger, M. Ramsey-Musolf, and J. Singh, "Electric dipole moments of the nucleon and light nuclei," *Reviews of Modern Physics* **91** (2019) 015001, for the neutron and proton EDM bounds and their interpretation.
- V. Andreev *et al.* (ACME Collaboration), "Improved limit on the electric dipole moment of the electron," *Nature* **562** (2018) 355–360, for the polar-molecule electron EDM bound.
- C. Abel *et al.* (nEDM Collaboration), "Measurement of the permanent electric dipole moment of the neutron," *Physical Review Letters* **124** (2020) 081803, for the neutron EDM bound.
- E. D. Commins, "Electric dipole moments of leptons," *Advances in Atomic, Molecular, and Optical Physics* **40** (1998) 1–46, for the lepton EDM phenomenology.
- O. Lebedev, K. A. Olive, M. Pospelov, and A. Ritz, "Probing CP violation with the deuteron electric dipole moment," *Physical Review D* **70** (2004) 016003, for the relation between EDM bounds and new-physics scales.
