# __The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure__

## Introduction

An **electric dipole moment** (EDM) is a permanent electric dipole along the spin axis of a particle. For a spin-$\tfrac12$ particle the interaction is

$$
\mathcal{L}_{\mathrm{EDM}}
= i\,d\sum_k E_k\;\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x
\;+\; i\,d\sum_k B_k\;\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_z\bigr)\vec e_x,
\qquad
H_{\mathrm{NR}} = -\,d\sum_k E_k\,i\vec e_k ,
$$

where $\tilde{Ξ}^{\mathrm{spn}}$ is a field of the biquaternion algebra $\mathbb{B}$, $d$ is the EDM, the three $\vec e_k$ are the spatial units of the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, and $i\vec e_k$ is twice the spin of *Special Element Conventions*, $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, the element that the magnetic and electric dipole couplings multiply by. The coefficient has the dimensions of charge times length, it is the canonical **CP-odd** observable of a spin-$\tfrac12$ system, and its measurement is a search for physics beyond the Standard Model: its present bounds are among the tightest in particle physics.

**The insertion is an element.** Every interaction of this article multiplies the field by an element of the algebra, and that element is the whole of the structure. An action that multiplies by $a$ on the left has the adjoint that multiplies by $a^{*}$ on the left, so the Hermiticity of the interaction is the class of one element under the star: the EDM insertion multiplies by $-\vec e_k$, the magnetic insertion multiplies by $i\vec e_k$, the spatial unit is anti-Hermitian and $i\vec e_k$ is Hermitian, and the two insertions therefore lie on opposite sides of the framework's split. The other two insertions of the article carry a right factor as well, $\vec e_z$, and the classes of the two factors under the star decide their class by the same rule.

**The chirality cell.** The chirality cell is the corpus's right multiplication by $-i\vec e_z$ (*Special Element Conventions*), and it is the object that carries one insertion of a pair into the other: composed after a bivector it returns the insertion of the EDM family, and composed after that insertion it returns the bivector. It is an involution, because $(-i)^2=-1$ and $\vec e_z\vec e_z=-e_t$ cancel, and it is Hermitian; its involution and the $(-i)^2$ of the dual are the two factors of the article's $\mathcal{D}^{2}=-1$.

**The structural statement.** The framework places the EDM operator in a definite half of its algebra. The EDM insertion multiplies by $-\vec e_k$, an **anti-Hermitian** element, and it therefore belongs to the material sector $\mathbb{M}_-$; the magnetic-moment insertion multiplies by $i\vec e_k$, a **Hermitian** element, and it belongs to the informational sector $\mathbb{M}_+$. The two are Hodge duals of each other: the dual exchanges the two insertions with the sign of the central $-i$, so it flips the Hermiticity class, and the $i$ of the exchange flips it back. That $i$ is the $i$ in front of $d$. The article establishes this and states what it does and does not buy.

- **Established, and recomputed below.** The Hermiticity of the four insertions, from the classes of their two factors under the star; the Hodge duality, as the exchange of the two families; and the resulting sector placement. The $\vec E$-coupling insertion multiplies by $-\vec e_k$ and is anti-Hermitian, hence material; the $\vec B$-coupling insertion multiplies by $i\vec e_k$ and is Hermitian, hence informational. The EDM Lagrangian is Hermitian because the explicit $i$ compensates the anti-Hermiticity, and that $i$ is the framework's marker of the CP-odd coefficient.
- **Standard, transcribed.** The definition of the EDM, its $\mathbf{P}$-, $\mathbf{T}$-, and $\mathbf{CP}$-odd character, the nonrelativistic limit, the form-factor decomposition of the electromagnetic vertex, the Standard Model prediction (CKM-suppressed and tiny), the $\theta$-term contribution, and the experimental bounds are standard. They are stated in the framework's notation.
- **Gap, left visible.** The framework supplies the operator and its sector, and it does not supply the coefficient. It has no CP-violating phase of its own, no mechanism to generate one, and no prediction for the electron, neutron, or proton EDM. The value of $d$ is an empirical input, and the framework's statement is the structural one: a nonzero EDM is the presence of a coefficient on an anti-Hermitian, material-sector insertion.

The sections that follow fix the operator, its dimension, and the size of the effect; establish the Hermiticity of the insertions and the Hodge duality that places them; derive the nonrelativistic limit; tabulate the discrete symmetries of the insertions; give the form-factor decomposition and the two coefficients; treat the CP-odd phase; and collect the bounds and the scales they probe. A closing section separates what the framework supplies from what it transcribes and what it lacks, and a list of open questions follows it. The array display is fixed in one section near the end, so that arrays appear in one place only.

**The signs and the field strength.** The frame signs and the components are

$$
\varepsilon=(1,-1,-1,-1),\qquad
\epsilon_{0123}=+1,\qquad
F_{0i}=E_i,\qquad
F_{ij}=-\epsilon_{ijk}B_k ,
$$

so that $\varepsilon_0=+1$ and $\varepsilon_k=-1$. The weight $\varepsilon_\rho$ is the corpus's plain weight (*Frame and Metric Conventions*): the sign with which the $\rho$-th unit squares. The two signs of $\varepsilon$ are not decoration: they are what turns a lower pair of indices into an upper pair, and the weighted contraction that reproduces the dual below uses them.

**The two Dirac equations.** The mass is the linear Dirac pair

$$
\tilde{\nabla}\tilde{Ξ}^{\mathrm{spn}}_R=m\tilde{Ξ}^{\mathrm{spn}}_L,
$$

$$
\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{spn}}_L=m\tilde{Ξ}^{\mathrm{spn}}_R,
$$

and the two displays are two equations, not one. Each is one-sided — the algebra acts by left multiplication on the field — and the pair is the chirality split of a single operator: the left-handed equation and the right-handed equation, coupled by the mass. The second member uses the conjugate gradient $\tilde{\nabla}^{\natural}$, a different element of the algebra; it is not the conjugate of the field, and the antilinear real structure $\flat=-{}^{*}$ is a third object, separate from both.

**Units.** Natural units $\hbar=c=1$ are used, and the EDM unit conversion is $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$.

The framework results used here are those of the companion articles:

- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the Dirac field and the bilinears built on it.
- Companion article *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, for the array display of the insertions.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the mass-term conventions and the real structure $\flat$.
- Companion article *The Proton in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.
- Companion article *The Neutron in Biquaternionic Form*, for the composite EDM and the framework's silence on its value.

## The EDM Operator and Its Dimension

**The interaction.** The EDM is a CP-odd coupling of the electromagnetic field strength to the spin. Its Lorentz-covariant form is

$$
\mathcal{L}_{\mathrm{EDM}}
= i\,d\sum_k E_k\;\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x
\;+\; i\,d\sum_k B_k\;\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_z\bigr)\vec e_x ,
$$

and its nonrelativistic limit is the Hamiltonian

$$
H_{\mathrm{NR}} = -\,d\sum_k E_k\,i\vec e_k ,
$$

the left multiplication by the element $-d\sum_kE_k\,i\vec e_k$ of $\mathbb{M}_+$. The explicit $i$ is required for a Hermitian Lagrangian, and it is the first appearance of the article's central point: the insertion multiplies by $-\vec e_k$, which is anti-Hermitian, and the coefficient must be multiplied by $i$ to give a real interaction.

**The dimension and the size.** The EDM has the dimensions of electric charge times length. In natural units, $d$ is dimensionless times a length, i.e. $[\mathrm{GeV}^{-1}]$, with the conversion given in the Introduction. For a fermion of mass $m_f$ and a new-physics scale $\Lambda$, the standard dimensional estimate of a CP-violating contribution is

$$
d \sim \frac{e\,m_f}{\Lambda^2}\,\sin\theta^{\mathrm{pha}} ,
$$

where $\theta^{\mathrm{pha}}$ is the CP-odd phase. The estimate is the one that governs the reach of the experiments: the smaller the bound, the larger the scale probed, and the heavier the fermion, the larger the contribution. The numbers are used in the last section.

**The observable.** A permanent EDM precesses in an electric field, and the precession is what the experiments measure — in atoms and molecules, in stored neutrons, and in storage rings. The observable is the coefficient of the spin along $\vec E$, the leading CP-odd electromagnetic coupling of a spin-$\tfrac12$ particle. The framework's proton and neutron articles treat those composites and note that the framework supplies no value for their EDMs; this article treats the operator and its structure.

## The Anti-Hermitian Structure of the EDM Insertion

**The adjoint of a two-sided multiplication.** An insertion acts as $Q\mapsto aQb$, with $b=e_t$ when it carries no right factor. Its adjoint is the action

$$
\bigl(Q\mapsto aQb\bigr)^{\dagger}=\bigl(Q\mapsto a^{*}Qb^{*}\bigr),
$$

because the star reverses the order of the three factors, $(aQb)^{*}=b^{*}Q^{*}a^{*}$, and the trace that defines the pairing is cyclic, so $b^{*}$ moves back to the right. The insertion is Hermitian exactly when the two factors are both fixed by the star or both reversed by it: $a^{*}=\lambda a$ and $b^{*}=\mu b$ with $\lambda\mu=1$. The rule is one line, it holds for every pair of multipliers, and it replaces the reading of an array.

**The four insertions.** The spatial unit is anti-Hermitian, $\vec e_k^{*}=-\vec e_k$, and the central imaginary is anti-Hermitian, $i^{*}=-i$; so $i\vec e_k$ is Hermitian, $(i\vec e_k)^{*}=i\vec e_k$, and $-\vec e_k$ is anti-Hermitian. The four insertions of the article, with the class the rule gives them:

| insertion | action | left factor | right factor | class | sector |
|---|---|---|---|---|---|
| magnetic moment | $Q\mapsto i\vec e_kQ$ | $i\vec e_k$, Hermitian | $e_t$, Hermitian | Hermitian | $\mathbb{M}_+$ |
| pseudotensor | $Q\mapsto \vec e_kQ\vec e_z$ | $\vec e_k$, anti-Hermitian | $\vec e_z$, anti-Hermitian | Hermitian | $\mathbb{M}_+$ |
| EDM | $Q\mapsto -\vec e_kQ$ | $-\vec e_k$, anti-Hermitian | $e_t$, Hermitian | anti-Hermitian | $\mathbb{M}_-$ |
| bare electric | $Q\mapsto i\vec e_kQ\vec e_z$ | $i\vec e_k$, Hermitian | $\vec e_z$, anti-Hermitian | anti-Hermitian | $\mathbb{M}_-$ |

**The bivectors.** The six bivectors are indexed by the six pairs of the basis, and each is an action of the same shape:

$$
\mathcal{G}_{0k}:\ Q\longmapsto i\,\vec e_k\,Q\,\vec e_z ,
\qquad
\mathcal{G}_{ij}:\ Q\longmapsto i\,\vec e_k\,Q ,
$$

with $k$ the spatial index complementary to the pair $(i,j)$. Each is $i$ times a left multiplication by a spatial unit, with the chirality factor present for the timelike pair and absent for the spatial pair. The glyph $\mathcal{G}_{\mu\nu}$ names the bivector of the pair and nothing else, and the two lines above are its definition.

**The Hodge duality.** The dual is this article's map on the insertions, and it is one line on each family: it exchanges the two members of a pair and it carries the sign of the central $-i$,

$$
\mathcal{D}\bigl(\mathcal{G}_{0k}\bigr)=+\,\mathcal{G}_{\lambda\mu},
\qquad
\mathcal{D}\bigl(\mathcal{G}_{\lambda\mu}\bigr)=-\,\mathcal{G}_{0k},
\qquad
\mathcal{D}\bigl(\mathcal{O}_{0k}\bigr)=+\,\mathcal{O}_{\lambda\mu},
\qquad
\mathcal{D}\bigl(\mathcal{O}_{\lambda\mu}\bigr)=-\,\mathcal{O}_{0k},
$$

where $(\lambda,\mu)$ is the spatial pair complementary to $k$, so that $(0,k,\lambda,\mu)$ is an even permutation of the frame. Each line is the chirality cell followed by the central $-i$, evaluated on the insertion, and the four together are the derived form of the Hodge dual on the bivectors and on the insertions. One evaluation, for the record: $\mathcal{D}(\mathcal{G}_{0k})(Q)=-i\,\mathcal{G}_{0k}(-iQ\vec e_z)=i\vec e_kQ=\mathcal{G}_{\lambda\mu}(Q)$; the second line is the same with one less factor, $\mathcal{D}(\mathcal{G}_{\lambda\mu})(Q)=-i\cdot i\vec e_k\,(-iQ\vec e_z)=-i\,\vec e_kQ\vec e_z=-\mathcal{G}_{0k}(Q)$. The dual therefore exchanges the two families and changes the sign of one of them, and two passages return minus the insertion,

$$
\mathcal{D}^{2}=-\,1 ,
$$

because the chirality cell is an involution and $(-i)(-i)=-1$: the familiar Lorentzian sign of the Hodge star on two-forms, here a consequence of the cell's square.

**The insertion is minus a spatial unit.** The composition of a bivector with the chirality cell is what the article means by the EDM insertion, and on the timelike pair it collapses to an element:

$$
\mathcal{O}_{0k}(Q)=i\,\vec e_k\,\bigl(-i\,Q\,\vec e_z\bigr)\vec e_z=i\,(-i)\,\vec e_k\,Q\,(\vec e_z\vec e_z)=-\,\vec e_k\,Q .
$$

The collapse spends the two factors of $\vec e_z$ and the two factors of $i$, and what survives is one spatial unit on the left. The EDM insertion is therefore the left multiplication by $-\vec e_k$, and the same composition on the spatial pair leaves the right factor standing,

$$
\mathcal{O}_{0k}:\ Q\longmapsto -\,\vec e_k\,Q ,
\qquad
\mathcal{O}_{ij}:\ Q\longmapsto \vec e_k\,Q\,\vec e_z .
$$

**The duality and the Hermiticity.** The dual alone does not preserve the class, and the factor $i$ is what restores it. The bare electric bivectors $\mathcal{G}_{0k}$ are anti-Hermitian and the rotations $\mathcal{G}_{ij}$ Hermitian, and the dual of a bare electric bivector is a rotation, $\mathcal{D}\bigl(\mathcal{G}_{0k}\bigr)=\mathcal{G}_{\lambda\mu}$, which is Hermitian: the bare dual has crossed to the other class. Composing with the chirality cell once more, which is what the EDM insertion is, gives $-\vec e_k$, anti-Hermitian again. In the magnetic family the same two steps run the other way, $\mathcal{D}\bigl(\mathcal{G}_{ij}\bigr)$ anti-Hermitian and $\mathcal{G}_{ij}$ after the chirality cell Hermitian, the pseudotensor of that family. The duality exchanges the families and flips the class; the $i$ flips it back, and it is the origin of the $i$ in the EDM Lagrangian.

**The weight and the contraction form.** The dual has a second writing, as a sum over the pair with the weight of *Frame and Metric Conventions*,

$$
\mathcal{D}\bigl(\mathcal{G}_{\mu\nu}\bigr)=\frac{1}{2}\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\,\varepsilon_\rho\varepsilon_\sigma\,\mathcal{G}_{\rho\sigma},
$$

and the two weights are what make the two writings agree; the sum was checked against the composition on all twelve ordered pairs. Dropping them gives the plain contraction, which is a different map: it takes the bare electric bivector to plus the rotation and the rotation to plus the bare electric bivector,

$$
\mathcal{G}_{0k}\longmapsto+\,\mathcal{G}_{\lambda\mu},\qquad
\mathcal{G}_{\lambda\mu}\longmapsto+\,\mathcal{G}_{0k},
$$

so it agrees with the dual on the bare electric family and differs by a sign on the rotations, and it squares to $+1$ where the dual squares to $-1$. The plain contraction is therefore not the duality; the weights are what turn it into one.

**The sector placement.** The four units and the central $i$ generate $\mathbb{B}$, and the insertions are built from them: a bivector adds $i\vec e_k$ on the left and, for the timelike pair, $\vec e_z$ on the right, and the chirality cell adds $\vec e_z$ on the right and the scalar $-i$. The sector split is the Hermiticity split of $\mathbb{B}$: Hermitian elements are the informational sector $\mathbb{M}_+$ and anti-Hermitian elements the material sector $\mathbb{M}_-$. Complexified, the algebra is $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, the two chiral halves, because the chirality cell commutes with every bivector and splits the algebra; the sector split is not that split, it is the split by Hermiticity. Applied to the insertions:

| Insertion | Term it carries | Hermiticity | Sector |
|---|---|---|---|
| $\mathcal{G}_{ij}$ | the magnetic moment, $\vec B$ | Hermitian | $\mathbb{M}_+$ |
| $\mathcal{O}_{ij}$, the bivector composed with the chirality cell | the pseudotensor, $i$ times the dual of the rotation | Hermitian | $\mathbb{M}_+$ |
| $\mathcal{O}_{0k}$, the bivector composed with the chirality cell | the EDM, $\vec E$ | anti-Hermitian | $\mathbb{M}_-$ |
| $\mathcal{G}_{0k}$ | the bare electric component | anti-Hermitian | $\mathbb{M}_-$ |

The EDM insertion is therefore the anti-Hermitian, material-sector insertion, and its Hermitian partner in the informational sector is the magnetic-moment insertion, one duality passage and one factor of $i$ away. This is the article's central structural statement. The bare electric bivector is anti-Hermitian as well, and it is listed only for completeness: it is not gauge invariant by itself, and only its contraction with $F$ is an operator.

**No dictionary is needed.** On the timelike pair the EDM insertion is not merely an operator that happens to be anti-Hermitian: it is the left multiplication by the element $-\vec e_k$, and $-\vec e_k$ is itself an element of the material sector. The placement is an identity, not a match. The rotation insertion is the left multiplication by $i\vec e_k$, an element of the informational sector; and since multiplication by the central $i$ exchanges the sectors, $i\mathbb{M}_-=\mathbb{M}_+$, the EDM insertion is the central imaginary times the rotation insertion about the same axis,

$$
\mathcal{O}_{0k}=i\,\mathcal{D}\bigl(\mathcal{G}_{0k}\bigr)=i\,\mathcal{G}_{\lambda\mu},
\qquad
-\,\vec e_k=i\,\bigl(i\vec e_k\bigr).
$$

The scalar $i$ and the element $i\vec e_k$ are different objects: $i$ is central and anti-Hermitian, $i\vec e_k$ is not central and is Hermitian, and the product $i\,(i\vec e_k)=-\vec e_k$ is what carries one sector into the other.

**The $i$ and the Hermiticity of the Lagrangian.** Because the EDM insertion is anti-Hermitian, the bilinear $\tilde{Ξ}^{\mathrm{spn}*}i(-\vec e_k\tilde{Ξ}^{\mathrm{spn}})\vec e_x$ is anti-Hermitian as a classical bilinear, and the Lagrangian density is Hermitian for real $d$ precisely because the explicit $i$ makes $i\times(\text{anti-Hermitian})$ Hermitian. The magnetic-moment Lagrangian has no such $i$, because its insertion is already Hermitian. **The factor of $i$ is the biquaternion signature of the EDM**: the operator is the CP-odd member of a dual pair, its material-sector placement is the anti-Hermiticity, and the Hermiticity of the action is restored by the central imaginary.

## The Nonrelativistic Reduction

**From the insertion to the spin.** The EDM insertion reduces to the nonrelativistic Hamiltonian through one identity,

$$
\mathcal{O}_{0k}=i\,\bigl(Q\mapsto i\vec e_kQ\bigr),
\qquad
(i\vec e_k)^{*}=i\vec e_k,
\qquad
(i\vec e_k)^{2}=e_t,
\qquad
\operatorname{tr}\bigl(Q\mapsto i\vec e_kQ\bigr)=0,
$$

$$
\{i\vec e_i,i\vec e_j\}=2\delta_{ij}e_t,
\qquad
[i\vec e_i,i\vec e_j]=2i\,\epsilon_{ijk}\,(i\vec e_k).
$$

The element $i\vec e_k$ is twice the spin of *Special Element Conventions*, $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$: Hermitian, of square one, traceless, and the three close on the commutator. The identity shows both facts at once — that the EDM insertion is $i$ times a Hermitian multiplication, hence anti-Hermitian, and that the multiplication it is $i$ times is the spin. The square $(i\vec e_k)^2=e_t$ is what gives $i\vec e_k$ the two eigenvalues $\pm1$; scaled by $\tfrac{\hbar}{2}$, they are the two values $\pm\tfrac{\hbar}{2}$ of a spin-$\tfrac12$ component.

**The factor of two and the sign.** The contraction of the insertion family with $F$ counts the electric pair twice, as $(0,k)$ and as $(k,0)$, and the two contributions are equal, because the bivector changes sign and $F$ changes sign together. With $F_{0k}=E_k$ the Lagrangian therefore contains

$$
\mathcal{L}_{\mathrm{EDM}} \supset -\,i\,d\,E_k\,\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\mathcal{O}_{0k}\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x
= -\,i\,d\,E_k\,\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(-\,\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x .
$$

Since $-\vec e_k=i(i\vec e_k)$ and $(-i)(i)=+1$, the insertion's minus and the coupling's $i$ spend to a plus, and the same term reads with the spin,

$$
-\,i\,d\,E_k\,\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(-\,\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x
= +\,d\,E_k\,\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl((i\vec e_k)\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x .
$$

For a positive-energy field normalized to one the bilinear is the spin density, the expectation of the spin $i\vec e_k$ on the field, whose two values are $\pm1$, so

$$
\mathcal{L}_{\mathrm{EDM}} \;\longrightarrow\; d\sum_k E_k\,\langle i\vec e_k\rangle ,
\qquad
H_{\mathrm{NR}} = -\,d\sum_k E_k\,i\vec e_k ,
$$

the stated nonrelativistic limit. The chain is a derivation of the limit from the covariant operator, and it exhibits the $i$ of the Lagrangian turning into the $i$ of the EDM insertion. The magnetic-moment coupling reduces in the same way with $\mathcal{G}_{ij}$ and the field $\vec B$, but with a Hermitian insertion and no compensating $i$.

**The spin operator and the sector.** The spin $i\vec e_k$ is Hermitian and lies in the informational sector $\mathbb{M}_+$, and the EDM insertion is $i$ times it: the material-sector insertion is the central imaginary times the informational-sector spin. This is the algebraic statement of the CP-odd character of the EDM in the framework's language — the observable couples to the spin, and the coupling is made CP-odd by the central imaginary that moves the operator into the material sector.

## The Discrete Symmetries of the Insertions

**The transformation of the two terms.** Under parity $\mathbf{P}$ the electric field is a vector, $\vec E\to-\vec E$, and the spin is a pseudovector, $i\vec e_k\to+i\vec e_k$, so the term $\vec E\cdot(\text{spin})\to-\vec E\cdot(\text{spin})$: the EDM term is $\mathbf{P}$-odd. Under time reversal $\mathbf{T}$ the electric field is even and the spin odd, so the term is odd again. Under charge conjugation $\mathbf{C}$ the field strength and the bilinear both change sign, and the term is even. The EDM is therefore $\mathbf{P}$- and $\mathbf{T}$-odd, and by the CPT theorem $\mathbf{CP}$-odd. The magnetic term $-\vec\mu\cdot\vec B$ is even under all three. The contrast is exact, and it is the chirality cell that carries it: the two operators differ by the composition with the chirality cell, and removing or restoring that cell is what flips the parity.

**The bilinears.** The sixteen bilinears fall into five shapes — scalar, vector, tensor, axial vector, pseudoscalar — and the chirality cell pairs the two that carry one free index and the two that carry two: the vector with the axial vector, the tensor with the pseudotensor. The four that enter here are

$$
\text{(vector)}\ \tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(i\,e_\mu\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_{\nu(\mu)}\bigr)\vec e_x,\qquad
\text{(tensor)}\ \tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\mathcal{G}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x,
$$

$$
\text{(axial)}\ \tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(i\,e_\mu\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_{\nu(\mu)}\vec e_z\bigr)\vec e_x,\qquad
\text{(pseudotensor)}\ \tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\mathcal{O}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x .
$$

Each is the field, the element the insertion multiplies it by, the unit $\vec e_{\nu(\mu)}$ that *Matrix Representations Conventions* attaches to the index, and the right factor $\vec e_x$ of the Dirac adjoint; the axial pair is the same product with the chirality factor appended, and in the last two the pair index decides which member of its family appears: the timelike pair gives the EDM insertion, the spatial pair the pseudotensor. A bilinear with free indices has no parity of its own, since its timelike and its spatial components transform oppositely; the parities are therefore those of the gauge-invariant operators, bilinear times field:

| Operator | Bilinear | $\mathbf{P}$ | $\mathbf{T}$ | $\mathbf{C}$ | $\mathbf{CP}$ | Insertion |
|---|---|---|---|---|---|---|
| $\tilde{Ξ}^{\mathrm{spn}*}i(i e_\mu\tilde{Ξ}^{\mathrm{spn}}\vec e_{\nu(\mu)})\vec e_x\,A_\mu$ (charge) | vector | even | even | even | even | $i\,e_\mu$ on the left, $i\vec e_{\nu(\mu)}$ on the right: Hermitian for $\mu=0$, anti-Hermitian for $\mu=k$ |
| $\tilde{Ξ}^{\mathrm{spn}*}i(\mathcal{G}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}})\vec e_x\,F_{\mu\nu}$ (magnetic) | tensor | even | even | even | even | $\mathcal{G}_{ij}$, Hermitian |
| $i\,\tilde{Ξ}^{\mathrm{spn}*}i(\mathcal{O}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}})\vec e_x\,F_{\mu\nu}$ (EDM) | pseudotensor | odd | odd | even | odd | $\mathcal{O}_{0k}$, anti-Hermitian |

The EDM is the pseudotensor bilinear, the tensor times the chirality cell, and the table is the parity bookkeeping of the Hodge duality: the chirality cell is what flips the parity and the CP character, and the factor $i$ that accompanies it is what keeps the Hermiticity class.

**Two operators, not four.** The list has two entries because the tensor and the pseudotensor are duals, not independent: the EDM insertion is $i$ times the dual of the tensor, and contracting a dual bivector with $F$ is the same as contracting the bivector with the dual of $F$. A Hermitian Lagrangian therefore carries two dimension-five couplings of different parity, and both coefficients are real: $\frac{1}{2}\mu\,\tilde{Ξ}^{\mathrm{spn}*}i(\mathcal{G}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}})\vec e_xF_{\mu\nu}$ and $\frac{1}{2}d\,\tilde{Ξ}^{\mathrm{spn}*}i\bigl(\mathcal{D}(\mathcal{G}_{\mu\nu})\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_xF_{\mu\nu}$. Written with the chirality cell instead of the dual, the second is $-i\,d$ times the insertion built on the bivector, and the $i$ of that writing is the duality's, not a separate phase. The other two combinations of bilinear and field are their conjugates. This is why the EDM is *the* CP-odd electromagnetic observable at this order, and why its bound is the sharpest test of new CP violation in the fermion sector. The anapole and the charge-radius terms join the list one dimension higher, are CP-even, and are not dipole moments.

**The framework's real structure and CP.** The framework's conjugation enters the bilinears through the real structure of the algebra: a CP transformation is a charge conjugation accompanied by a parity reflection, and it uses the antilinear real structure. The EDM's bilinear is the one that changes sign under this operation, and the coefficient that keeps the action invariant is the real number $d$ on the dual insertion, which is $-i\,d$ on the chirality-cell one. The framework statement is therefore precise: the EDM is the coefficient of a CP-odd, anti-Hermitian, material-sector bilinear, and its measurement is the measurement of a central imaginary's coupling to the spin.

## The Form Factors and the Two Coefficients

**The electromagnetic vertex.** The most general gauge-invariant vertex of an on-shell spin-$\tfrac12$ particle with the electromagnetic field, at momentum transfer $k=p_2-p_1$, is

$$
\Gamma_\mu(p_2,p_1)\,\tilde{Ξ}^{\mathrm{spn}}
= i\,e_\mu\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_{\nu(\mu)}\,F_1(k^2)
+ \frac{i}{2m}\,k_\nu\,\mathcal{G}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}}\,F_2(k^2)
+ \frac{i}{2m}\,k_\nu\,\mathcal{O}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}}\,F_3(k^2) + \cdots ,
$$

with $F_1$ the charge, $F_2$ the anomalous magnetic moment, and $F_3$ the EDM form factor; the ellipsis denotes the anapole and higher terms. In the nonrelativistic limit, $F_2$ and $F_3$ reduce to the magnetic and electric dipole couplings,

$$
H_{\mathrm{NR}} = -\,\mu\sum_k B_k\,i\vec e_k - d\sum_k E_k\,i\vec e_k ,
$$

$$
\mu = \frac{e}{2m}\big(1+F_2(0)\big),\qquad d = \frac{e}{2m}F_3(0),
$$

so that the two coefficients are the form factors at zero momentum transfer, multiplied by the same dimensionful factor and distinguished by the chirality cell. The magnetic moment is the Hermitian member of the pair; the EDM is the anti-Hermitian member; and the two are Hodge duals of each other. This is the standard form-factor decomposition, and it is the reason the EDM is called the "dual" of the anomalous magnetic moment.

**Why the dual is the CP-odd one.** The form-factor pair $(F_2,F_3)$ is the framework's Hermitian/anti-Hermitian pair, and the two differ by the chirality cell. The magnetic term has $F_2$ and no chirality cell; the EDM term has $F_3$ and one chirality cell. The chirality cell is what flips the parity and the CP character of the insertion, and the $i$ of the duality is what keeps the coefficient real, so both $F_2$ and $F_3$ are real and it is the parity that separates them. The framework does not compute $F_3$; it places it in the anti-Hermitian sector, and with $F_3=0$ only the Hermitian insertion survives, which is the CP-even statement.

**The magnetic moment as the calibration.** The anomalous magnetic moment $F_2$ is measured to extraordinary precision, and its theoretical value is the framework's testing ground for the fermion sector; the companion article on the anomalous magnetic moment computes the framework's contribution. The EDM is the dual observable, and its bound reaches scales that the magnetic moment cannot probe.

## CP Violation and the Origin of the Phase

**Where a nonzero EDM comes from.** The EDM is CP-odd, so it can be generated only by a CP-violating interaction. The candidates are standard:

- **The CKM phase.** In the Standard Model the only CP-violating parameter of the quark sector is the phase of the Cabibbo–Kobayashi–Maskawa matrix; the companion article on the CKM matrix treats it. Its contribution to the neutron EDM arises only at the three-loop level and is of order $d_n\sim10^{-32}\ e\cdot\mathrm{cm}$, far below the present bound; the CKM phase is not the source of any measurable hadronic or atomic EDM.
- **The $\theta$ parameter.** Quantum chromodynamics admits a CP-odd topological term

    $$
    \theta\,\frac{\alpha_s}{16\pi}\,\epsilon_{\mu\nu\rho\sigma}G_{a\mu\nu}G_{a\rho\sigma}
    \;=\;\theta\,\frac{g_s^{2}}{32\pi^{2}}\,G_{a\mu\nu}\tilde{G}_{a\mu\nu},
    \qquad \tilde{G}_{a\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}G_{a\rho\sigma},
    $$

    whose contribution to the neutron EDM is of order $d_n\sim\theta\times10^{-16}\ e\cdot\mathrm{cm}$; the bound on $d_n$ forces $|\theta|\lesssim10^{-10}$. The $\theta$ parameter belongs to the corpus's general gauge apparatus and is not developed here; the fermion-sector statement is that the EDM is where the $\theta$ problem is measured.
- **New physics.** Any new CP-violating phase in a theory of fermions and gauge fields contributes to the EDMs, usually at the one- or two-loop level, and the bounds constrain the scale of that physics. This is the sense in which the EDM searches probe beyond the Standard Model.

**The Standard Model prediction, and its smallness.** The Standard Model's CKM phase gives EDMs that are far below the current bounds; the electron EDM, in particular, is generated only at four loops and is unobservably small. The framework inherits this: its fermion sector carries the linear chiral mass and the antilinear real structure, neither of which contains a CP-odd phase, and the algebra's central objects are the volume element and the chirality cell, not a CP-violating angle. The framework therefore predicts no measurable EDM, and observes that any EDM would be evidence for a phase it does not contain.

**Where a phase could sit in the framework.** A CP-odd phase can be written on the algebra in more than one way: in the mass matrix, in a Yukawa coupling, or in a coefficient multiplying an anti-Hermitian insertion. The framework supplies the insertion — the anti-Hermitian, material-sector multiplication — and the phase is the coefficient's imaginary part in a real action. The algebraic statement is that a nonzero EDM is the presence of a nonzero coefficient on the material-sector insertion, and since the material sector is the anti-Hermitian one, the coefficient is the imaginary part of an otherwise real coupling. Where that phase originates is not answered by the algebra.

## The Bounds and the Scales They Probe

**The experimental bounds.** The strongest EDM bounds are on the electron and the neutron, with the atomic and molecular experiments providing orders of magnitude of leverage:

| System | Bound on $\lvert d\rvert$ | Method |
|---|---|---|
| Electron | $\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$ | polar molecule (ThO), Ramsey spectroscopy |
| Neutron | $\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$ | stored ultracold neutrons, magnetic resonance |
| Proton (indirect) | $\lesssim10^{-23}\ e\cdot\mathrm{cm}$ | atomic EDM, storage-ring proposals |
| Mercury-199 atom | $\lesssim7.4\times10^{-30}\ e\cdot\mathrm{cm}$ | atomic EDM |

The bounds have improved by many orders of magnitude over the decades and are the tightest CP-odd constraints in particle physics. The values are those of the standard reviews.

**The scales they probe.** The dimensional estimate $d\sim e\,m_f\sin\theta^{\mathrm{pha}}/\Lambda^2$ converts the bounds into a reach. Since $d$ is quoted in units of $e\cdot\mathrm{cm}$, the charge is factored out of the number and the estimate is used in the form

$$
\frac{d}{e} \sim \frac{m_f}{\Lambda^2}\,\sin\theta^{\mathrm{pha}} .
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
| The biquaternion algebra as the algebra of the insertions, and the Hermiticity sector split | **Supplied**; Hermitian is $\mathbb{M}_+$, anti-Hermitian is $\mathbb{M}_-$ |
| The EDM insertion $Q\mapsto-\vec e_kQ$ as anti-Hermitian, material-sector | **Supplied**, recomputed from the classes of the two factors under the star |
| The magnetic-moment insertion $Q\mapsto i\vec e_kQ$ as Hermitian, informational-sector | **Supplied**, recomputed |
| The Hodge duality of the insertions, $\mathcal{D}(\mathcal{G}_{0k})=+\mathcal{G}_{\lambda\mu}$ and $\mathcal{D}(\mathcal{G}_{\lambda\mu})=-\mathcal{G}_{0k}$, with $\mathcal{D}^{2}=-1$ on the six bivectors | **Supplied**, recomputed for all six |
| The EDM insertion $Q\mapsto-\vec e_kQ$ as the left multiplication by the element $-\vec e_k\in\mathbb{M}_-$ | **Supplied**, recomputed for the three spatial directions |
| The explicit $i$ in the EDM Lagrangian as the marker of the anti-Hermitian insertion | **Supplied** by the algebra |
| The definition of the EDM and its $\mathbf{P}$-, $\mathbf{T}$-, $\mathbf{CP}$-odd character | **Transcribed**; standard |
| The form-factor decomposition and the nonrelativistic limit | **Transcribed**; standard |
| The CKM and $\theta$-term contributions, and their smallness | **Standard**; the $\theta$ parameter belongs to the general gauge apparatus |
| The experimental bounds and the reach $\Lambda\gtrsim10^{3}$ TeV | **Transcribed**; standard, with the arithmetic recomputed |
| The value of $d$ for any particle | **Not supplied**; empirical |
| A CP-violating phase, and its origin | **Not supplied**; the framework has none |
| The electron, neutron, and proton EDMs as framework predictions | **Not supplied**; the composite articles state the same |

## Open Questions

1. **The placement's sharpness.** The identification of the Hermitian and anti-Hermitian insertions with the sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ is the framework's stated dictionary. For the EDM insertion the placement is exact: the insertion is the left multiplication by the element $-\vec e_k$ of $\mathbb{M}_-$, and nothing is compared. The rotation insertion is the left multiplication by $i\vec e_k$, and the central imaginary times it is read in the material sector through $i\mathbb{M}_-=\mathbb{M}_+$. The insertions that carry a right factor as well — the bare electric bivector and the pseudotensor — are placed by the rule on the two factors and not by an element of $\mathbb{B}$ alone; a sector assignment of a two-sided multiplication is a statement about the operator, and the article makes it as one.

2. **The phase's sector.** A CP-odd phase multiplying the material-sector insertion is an imaginary coefficient. Whether the framework can distinguish phases that sit in the mass matrix from phases that sit in the dipole coefficients, and whether the abelian gauge-sector field strength of the framework supplies a $\theta$-like invariant, is not settled here and belongs partly to the general gauge apparatus.

3. **The composite EDMs.** The neutron and proton EDMs are matrix elements of quark and gluon CP-odd operators, and their computation is nonperturbative. The framework's proton and neutron articles supply no value; whether a biquaternion treatment of the bound-state problem can be given is open and lies outside the fermion sector.

4. **The duality at the level of the action.** The Hodge duality relates the EDM and magnetic insertions with a factor of $i$; whether the framework's action can be written so that the duality is manifest, pairing the two observables in a single Hermitian structure, is a question of the action's algebraic form.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}^{\mathrm{spn}}=a\tilde{Ξ}^{\mathrm{spn}}$ and $R_b\tilde{Ξ}^{\mathrm{spn}}=\tilde{Ξ}^{\mathrm{spn}} b$.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The five are generators, not a basis: the basis is the sixteen cells $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$, one for each ordered pair of units, linearly independent over $\mathbb{C}$ and spanning the sixteen complex dimensions. A product of two cells is again a cell up to sign, and a general element is a complex linear combination of the sixteen.

$\gamma_5$ is the reference-frame cell of the chirality operator. The central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is $\mathbb{R}$-linear, not $\mathbb{C}$-linear; over $\mathbb{R}$ the sixteen products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, two real Clifford algebras of real dimension sixteen each.

**The identities.** With $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

**The normalisation of $\sigma_{\mu\nu}$.** The tensor is the Dirac one, $\sigma_{\mu\nu}=\frac{i}{2}[\gamma_\mu,\gamma_\nu]=i\gamma_\mu\gamma_\nu$ for $\mu\ne\nu$. The companion *Matrix Representations Conventions* writes the same symbol for the half bivector $\frac14[\gamma_\mu,\gamma_\nu]=\frac12\gamma_\mu\gamma_\nu$, which is $-\frac{i}{2}\sigma_{\mu\nu}$. The factor is complex rather than real, so the two symbols carry opposite Hermiticity: with the half-bivector convention the electric family is Hermitian and the magnetic family anti-Hermitian. The sector assignment stated in this article belongs to the Dirac tensor, the object that enters the bilinear.

**The four contractions.** The weight $\varepsilon$ is what carries the metric into the sum, and the anticommutation relations do the rest:

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\varepsilon_\alpha\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\rho\gamma_\mu=+2\gamma_\alpha\gamma_\beta\gamma_\rho .
$$

In the frame used here the weight is $\varepsilon=(1,-1,-1,-1)$, and the four sums read $4I_4$, $-2\gamma_\alpha$, $4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $+2\gamma_\alpha\gamma_\beta\gamma_\rho$. The unweighted sum $\sum_\mu\gamma_\mu\gamma_\mu$ equals $-2I_4$, one $+1$ and three $-1$; it is a different object and not one of the four.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.


## Summary

The electric dipole moment is the CP-odd, dimension-five coupling of a spin-$\tfrac12$ particle to the electromagnetic field,

$$
\mathcal{L}_{\mathrm{EDM}}
= i\,d\sum_k E_k\;\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\bigr)\vec e_x
\;+\; i\,d\sum_k B_k\;\tilde{Ξ}^{\mathrm{spn}*}i\,\bigl(\vec e_k\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_z\bigr)\vec e_x,
\qquad
H_{\mathrm{NR}} = -\,d\sum_k E_k\,i\vec e_k .
$$

In the biquaternion framework its insertion has a definite algebraic character: the $\vec E$-coupling insertion multiplies by $-\vec e_k$, an **anti-Hermitian** element, and it therefore lies in the material sector $\mathbb{M}_-$; the $\vec B$-coupling magnetic-moment insertion multiplies by $i\vec e_k$, a **Hermitian** element, and it lies in the informational sector $\mathbb{M}_+$. Both statements follow from the star-signs of the two factors of the insertion, and both were recomputed. The two are Hodge duals, the dual exchanging the two members of a pair with the sign of the central $-i$,

$$
\boxed{\;\mathcal{D}\bigl(\mathcal{G}_{0k}\bigr)=+\,\mathcal{G}_{\lambda\mu},\quad
\mathcal{D}\bigl(\mathcal{G}_{\lambda\mu}\bigr)=-\,\mathcal{G}_{0k},
\qquad
\mathcal{O}_{\mu\nu}=i\,\mathcal{D}\bigl(\mathcal{G}_{\mu\nu}\bigr),
\qquad
\mathcal{D}^{2}=-\,1\;}
$$

and the sign is the product of the cell's involution with $(-i)^2=-1$, verified for all six bivectors. The dual exchanges the two families with a sign, so two passages return minus the bivector; the EDM insertion is $i$ times the dual of the rotation, and that $i$ is what keeps the Hermiticity class while making the coefficient real. The explicit $i$ in the EDM Lagrangian is what makes $i\times(\text{anti-Hermitian})$ Hermitian, and it is the algebra's marker of the CP-odd coefficient; the collapse of the composition, $\mathcal{O}_{0k}(Q)=i\vec e_k(-iQ\vec e_z)\vec e_z=-\vec e_kQ$, makes the placement exact, the insertion being the left multiplication by the element $-\vec e_k$ of $\mathbb{M}_-$.

The form-factor decomposition

$$
\Gamma_\mu(p_2,p_1)\,\tilde{Ξ}^{\mathrm{spn}}
= i\,e_\mu\,\tilde{Ξ}^{\mathrm{spn}}\,\vec e_{\nu(\mu)}\,F_1
+ \frac{i}{2m}\,k_\nu\,\mathcal{G}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}}\,F_2
+ \frac{i}{2m}\,k_\nu\,\mathcal{O}_{\mu\nu}\tilde{Ξ}^{\mathrm{spn}}\,F_3 + \cdots
$$

exhibits the magnetic moment $F_2$ and the EDM $F_3$ as the Hermitian and anti-Hermitian members of one dimension-five pair, which the framework places in the informational and material sectors; they are the whole list, the pseudotensor being $i$ times the dual of the tensor. The framework does not supply the coefficient: it has no CP-violating phase, predicts no measurable EDM, and inherits the Standard Model's tiny CKM contribution and the $\theta$-term constraint, $|\theta|\lesssim10^{-10}$ from $|d_n|\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$. The present electron bound $|d_e|\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$, combined with the dimensional estimate $d/e\sim m_e\sin\theta^{\mathrm{pha}}/\Lambda^2$, probes new-physics scales $\Lambda\gtrsim10^{3}$ TeV, and the framework's contribution is to state exactly where in the algebra such a coefficient would sit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra of *Algebra and Element Conventions*; the even part of the frame's real algebra, the part generated by the six bivectors |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The four units of the basis (*Algebra and Element Conventions*); the star fixes $e_t$ and reverses the three spatial units |
| $i\vec e_k$ | Twice the spin (*Special Element Conventions*), $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$: Hermitian, of square $e_t$, traceless, the three closing on the commutator |
| $Q\mapsto aQb$ | A two-sided insertion; its adjoint multiplies by $a^{*}$ on the left and $b^{*}$ on the right |
| $Q\mapsto i\vec e_kQ$ | The magnetic-moment insertion, Hermitian, $\mathbb{M}_+$ |
| $Q\mapsto-\vec e_kQ$ | The EDM insertion, anti-Hermitian, $\mathbb{M}_-$ |
| the chirality cell | The corpus's right multiplication by $-i\vec e_z$ (*Special Element Conventions*); an involution, Hermitian |
| $\mathcal{G}_{0k}:\ Q\mapsto i\vec e_kQ\vec e_z$; $\mathcal{G}_{ij}:\ Q\mapsto i\vec e_kQ$ | The six bivectors; $k$ is the index complementary to the spatial pair $(i,j)$ |
| $\mathcal{O}_{0k}:\ Q\mapsto-\vec e_kQ$; $\mathcal{O}_{ij}:\ Q\mapsto\vec e_kQ\vec e_z$ | The six EDM insertions; each is the bivector of its pair composed with the chirality cell |
| $\mathcal{D}$ | The Hodge dual on the insertions; $\mathcal{D}(\mathcal{G}_{0k})=+\mathcal{G}_{\lambda\mu}$, $\mathcal{D}(\mathcal{G}_{\lambda\mu})=-\mathcal{G}_{0k}$, $\mathcal{D}^{2}=-1$, and $\mathcal{D}(\mathcal{G}_{\mu\nu})=\tfrac12\sum_{\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\varepsilon_\rho\varepsilon_\sigma\mathcal{G}_{\rho\sigma}$ |
| $\mathcal{O}_{\mu\nu}=i\,\mathcal{D}(\mathcal{G}_{\mu\nu})$ | The EDM insertion as $i$ times the dual of the bivector; on the timelike pair, $i\,(i\vec e_k)=-\vec e_k$ |
| $\varepsilon_\rho$ | The plain weight of *Frame and Metric Conventions*; with $\varepsilon=(1,-1,-1,-1)$, $\varepsilon_0=+1$ and $\varepsilon_k=-1$ |
| $F_{0i}=E_i$, $F_{ij}=-\epsilon_{ijk}B_k$ | The field strength components |
| $\mathcal{L}_{\mathrm{EDM}}=i\,d\sum_kE_k\tilde{Ξ}^{\mathrm{spn}*}i(\vec e_k\tilde{Ξ}^{\mathrm{spn}})\vec e_x + i\,d\sum_kB_k\tilde{Ξ}^{\mathrm{spn}*}i(\vec e_k\tilde{Ξ}^{\mathrm{spn}}\vec e_z)\vec e_x$ | EDM Lagrangian |
| $H_{\mathrm{NR}}=-d\sum_kE_k\,i\vec e_k$ | EDM nonrelativistic Hamiltonian |
| $F_1,F_2,F_3$ | Charge, anomalous magnetic moment, EDM form factors |
| $d=\tfrac{e}{2m}F_3(0)$, $\mu=\tfrac{e}{2m}(1+F_2(0))$ | EDM and magnetic moment |
| $d/e\sim m_f\sin\theta^{\mathrm{pha}}/\Lambda^2$ | Dimensional estimate, the charge factored out of the $e\cdot\mathrm{cm}$ unit |
| $1\ \mathrm{GeV}^{-1}=1.97327\times10^{-14}\ \mathrm{cm}$ | EDM unit conversion |
| $\lvert d_e\rvert\lesssim1.1\times10^{-29}\ e\cdot\mathrm{cm}$ | Electron EDM bound |
| $\lvert d_n\rvert\lesssim1.8\times10^{-26}\ e\cdot\mathrm{cm}$ | Neutron EDM bound |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- L. I. Schiff, "Measurability of nuclear electric dipole moments," *Physical Review* **132** (1963) 2194–2200, for the atomic-physics theorem on the screening of nuclear EDMs.
- W. Bernreuther and M. Suzuki, "The electric dipole moment of the electron," *Reviews of Modern Physics* **63** (1991) 313–340, for the electron EDM and its theory.
- I. B. Khriplovich and S. K. Lamoreaux, *CP Violation Without Strangeness* (Springer, 1997), for electric dipole moments of particles, atoms, and molecules.
- J. Engel, M. J. Ramsey-Musolf, and U. van Kolck, "Electric dipole moments of nucleons, nuclei, and atoms: the Standard Model and beyond," *Progress in Particle and Nuclear Physics* **71** (2013) 21–74, for the hadronic and nuclear EDMs and the $\theta$-term contribution.
- T. Chupp, P. Fierlinger, M. Ramsey-Musolf, and J. Singh, "Electric dipole moments of the nucleon and light nuclei," *Reviews of Modern Physics* **91** (2019) 015001, for the neutron and proton EDM bounds and their interpretation.
- V. Andreev *et al.* (ACME Collaboration), "Improved limit on the electric dipole moment of the electron," *Nature* **562** (2018) 355–360, for the polar-molecule electron EDM bound.
- C. Abel *et al.* (nEDM Collaboration), "Measurement of the permanent electric dipole moment of the neutron," *Physical Review Letters* **124** (2020) 081803, for the neutron EDM bound.
- E. D. Commins, "Electric dipole moments of leptons," *Advances in Atomic, Molecular, and Optical Physics* **40** (1998) 1–46, for the lepton EDM phenomenology.
- O. Lebedev, K. A. Olive, M. Pospelov, and A. Ritz, "Probing CP violation with the deuteron electric dipole moment," *Physical Review D* **70** (2004) 016003, for the relation between EDM bounds and new-physics scales.
