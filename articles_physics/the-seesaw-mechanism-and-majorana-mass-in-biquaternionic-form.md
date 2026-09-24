# __The Seesaw Mechanism and Majorana Mass in Biquaternionic Form__

## Introduction

The **seesaw mechanism** explains why the neutrinos are so light: a neutrino of Dirac mass $m_D$ mixes with a heavy state of Majorana mass $M_R$, and the light eigenvalue of the resulting mass matrix is suppressed by the ratio of the two,

$$
m_\nu \;\simeq\; \frac{m_D^2}{M_R} ,
$$

so that a Dirac mass of the electroweak scale and a heavy mass near $10^{14}$–$10^{15}$ GeV produce a light mass of order $0.05$ eV. The mechanism is not a model of the light mass alone but a statement about two masses of different kinds: the **Dirac mass**, which pairs two independent chiralities and conserves fermion number, and the **Majorana mass**, which pairs a field with its own conjugate and violates fermion number by two units. The seesaw is the mixing of the two.

The biquaternion framework has already separated the two kinds, and that separation is the reason this article can be written at all. The framework's Dirac mass is the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$, through which the vector central phase passes; the framework's antilinear object is the real structure $\flat=-\dagger$, and the genuinely conjugate pairing built on it is a separate equation. The companion articles on antilinear structure and on the neutrino establish the distinction and the module reality condition $\mathcal{C}:\psi\mapsto K\psi^{*}$ with $\mathcal{C}^2=1$. This article asks what the framework supplies for the seesaw, and states the answer in the corpus's three categories.

- **Established, and recomputed below.** The seesaw requires both masses, and the framework has both: the Dirac block of the mass matrix is the linear chiral pair, and the heavy Majorana block is the conjugate pairing on the module's real structure (or, for the single-field equation, on the algebra's real structure $\flat$). The light eigenvalue of the one-generation mass matrix is $m_\nu=-m_D^2/M_R$ to leading order in $m_D/M_R$, and the heavy one is $M_R$; the mixing is of order $m_D/M_R$. The $2\times2$ eigenvalues were computed exactly, and the light-mass suppression was verified.
- **Standard, transcribed.** The type-I seesaw matrix and its block diagonalisation, the general formula $m_\nu\simeq-m_DM_R^{-1}m_D^{T}$, the dimension-five Weinberg operator, and the scale $v^2/\Lambda$ are standard. They are stated in the framework's notation and the one-generation and diagonal cases are verified.
- **Gap, left visible.** The framework does not fix $m_D$, $M_R$, or $\Lambda$, and therefore does not predict $m_\nu$; it has no leptogenesis mechanism, no scalar triplet for the type-II seesaw (the scalar sector belongs to the spin-$0$ subcategory), and no derivation of why a heavy singlet should exist. What it supplies is the algebraic distinction between the two masses that the seesaw mixes, and the fact — established in the companion article on anomalies — that a gauge-singlet heavy state is unconstrained by anomaly cancellation.

The article is organised as follows. A section recalls the two kinds of mass and why the seesaw needs both. A section sets out the type-I mass matrix, diagonalises it, and verifies its numbers. A section gives the biquaternion form of the mechanism. A section treats the effective dimension-five operator and the scale. A short section records the type-II and type-III variants and their scope. A closing section separates what is supplied, transcribed, and missing.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ and $\Box=\partial_{ict}^2+\Delta$. The Dirac module is $\Delta=S\oplus\bar{S}$ with $S=\mathbb{C}^2=(\tfrac12,0)$, $\bar{S}=(0,\tfrac12)$, $\gamma_5=\mathrm{diag}(-I_2,I_2)$, and projectors $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$. The mass terms are: the **linear Dirac pair** $\tilde{\nabla}\tilde{\Psi}_R=m_D\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_D\tilde{\Psi}_R$, which conserves fermion number; the **Majorana pairing** $m_M\,(\text{conjugate pairing})$, built on the module reality condition $\psi^{c}=K\psi^{*}$ with $KK^{*}=I_4$; and the algebra's real structure $\flat=-\dagger$, kept separate. The spinor representation of a neutrino is written $\nu_L\in S$ and $N_R$ for the singlet; the charge-conjugate of a left-handed field is written $\nu_R^{c}=\mathcal{C}\nu_L$. The Higgs doublet and its vacuum expectation value $v=174$ GeV, the Weinberg operator, and the see-saw scales are **standard-model notation, not framework objects**, used where standard physics is named. Natural units $\hbar=c=1$ are used in the mass-matrix section.
<!-- CONVENTION — two kinds of mass: the Dirac mass is the linear chirality-off-diagonal pair and conserves fermion number; the Majorana mass is the antilinear pairing on the spinor module's real structure (or, separately, on the algebra's real structure flat = -dagger). Do not identify the framework's mass with the antilinear pairing, and do not identify flat with the module real structure. -->

The framework results used here are those of the companion articles:

- Companion article *The Neutrino and Majorana Fermions in Biquaternionic Form*, for the Majorana condition, the reality structure $\mathcal{C}$ on the module, and its fixed space.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the distinction between the linear chiral pair and the antilinear mass.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the module, its conjugate and the Lorentz action.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral decomposition of the Dirac module.

## The Two Kinds of Mass, and Why the Seesaw Needs Both

**The Dirac mass is the linear chiral pair.** The framework's massive Dirac fermion is

$$
\tilde{\nabla}\tilde{\Psi}_R = m_D\tilde{\Psi}_L , \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m_D\tilde{\Psi}_R ,
$$

which couples the two independent chiral halves and conserves the vector (fermion-number) central phase: the phase $e^{i\alpha}$ passes through $m_D$ because it is central, and the mass is invariant. In the module language the Dirac mass is a bilinear pairing $S$ with $\bar{S}$, and the fermion number $L-R$ is conserved.

**The Majorana mass is a self-conjugate pairing.** A Majorana mass pairs a field with its own charge conjugate, $\psi^{c}=\mathcal{C}\psi$, which is an antilinear involution on the module with $\mathcal{C}^2=1$; its fixed space has real dimension four. Such a mass term is permitted — the module's real structure commutes with the kinetic operator — but it violates fermion number by two units, because it converts a fermion into an antifermion. In the framework the antilinear object is the real structure, and the companion articles keep it strictly separate from the linear chiral pair; the present article does not conflate them.

**Why the seesaw needs both.** The mechanism has three ingredients, and each is a different object.

- A **Dirac mass** $m_D$ connecting the left-handed neutrino $\nu_L$ to a right-handed state $\nu_R^{c}$, which is the linear chiral pair.
- A **Majorana mass** $M_R$ for the right-handed singlet, $\tfrac12M_R\,\nu_R^{c\,T}C^{-1}\nu_R^{c}+\text{h.c.}$, which is the self-conjugate pairing and requires the singlet to be its own conjugate.
- The **absence of a direct Majorana mass for $\nu_L$** at the renormalisable level, which is the statement that the left-handed neutrino is part of an $SU(2)_L$ doublet and no renormalisable operator gives it a mass. This is standard.

The framework supplies the first two as different objects and the third as a statement about the module's gauge quantum numbers, and it is precisely the *difference* of the two masses that produces the suppression.

**The singlet is anomaly-silent.** A right-handed neutrino is a gauge singlet: vanishing colour and weak charge and vanishing hypercharge. As the companion article on anomalies records, it therefore contributes zero to every anomaly cancellation condition, and a Majorana mass for it is forbidden by no consistency requirement. The heavy state that the seesaw needs is thus invisible to the anomaly constraints that fix the rest of the spectrum — the fermion-sector reason the mechanism is available at all.

## The Type-I Seesaw: Mass Matrix and Diagonalisation

**The matrix.** In the basis $(\nu_L,\ \nu_R^{c})$, the mass terms of one generation are

$$
-\mathcal{L}_{\mathrm{mass}} = \tfrac12
\begin{pmatrix}\nu_L & \nu_R^{c}\end{pmatrix}
\begin{pmatrix} 0 & m_D \\ m_D & M_R \end{pmatrix}
\begin{pmatrix}\nu_L \\ \nu_R^{c}\end{pmatrix} + \text{h.c.},
$$

where the matrix is **symmetric** (both entries are Majorana-type couplings in the $(\nu_L,\nu_R^{c})$ basis, so the off-diagonal entries are equal) rather than Hermitian, and $m_D$ is the Dirac mass and $M_R$ the heavy Majorana mass. The zero in the upper-left corner is the statement that $\nu_L$ has no direct Majorana mass. This matrix is standard.

**Exact eigenvalues.** A real symmetric $2\times2$ matrix has eigenvalues

$$
\lambda_\pm = \frac{M_R\pm\sqrt{M_R^2+4m_D^2}}{2},
$$

and for $m_D\ll M_R$ the roots are

$$
\lambda_- = -\frac{2m_D^2}{M_R+\sqrt{M_R^2+4m_D^2}} \simeq -\frac{m_D^2}{M_R},
\qquad
\lambda_+ \simeq M_R + \frac{m_D^2}{M_R} .
$$

The light eigenvalue is suppressed by the ratio, and the heavy one is essentially the Majorana mass. The exact form of $\lambda_-$ was used to avoid the cancellation in $(M_R-\sqrt{M_R^2+4m_D^2})/2$, and the values were recomputed:

| $m_D$ (GeV) | $M_R$ (GeV) | heavy $\lambda_+$ (GeV) | light $\lambda_-$ (GeV) | $-m_D^2/M_R$ (GeV) |
|---|---|---|---|---|
| $100$ | $10^{15}$ | $10^{15}$ | $-10^{-11}$ | $-10^{-11}$ |
| $100$ | $10^{12}$ | $10^{12}$ | $-10^{-8}$ | $-10^{-8}$ |
| $100$ | $10^{6}$ | $10^{6}$ | $-10^{-2}$ | $-10^{-2}$ |

The third row is a check of the exact formula against the approximation at a resolvable scale: the exact light eigenvalue is $-0.01$ GeV and $-m_D^2/M_R=-0.01$ GeV. The first row is the physical regime: a Dirac mass of the electroweak scale and a heavy mass of $10^{15}$ GeV give a light mass of $10^{-11}$ GeV $=0.01$ eV.

**The mixing, and the decoupling.** The matrix is diagonalised by a rotation of angle $\theta$ with

$$
\tan 2\theta = \frac{2m_D}{M_R},
\qquad
\theta \simeq \frac{m_D}{M_R} \ll 1 .
$$

The heavy state is therefore almost purely $\nu_R^{c}$ and the light state almost purely $\nu_L$, with the admixture of order $m_D/M_R\sim10^{-13}$ for the physical scales. This is the technical statement of decoupling: the heavy state is inaccessible, which is why the mechanism predicts nothing directly at laboratory energies, and it is also why a high scale is needed for any cosmological consequence.

**More than one generation.** For $N_g$ generations $m_D$ becomes a $3\times3$ matrix and $M_R$ a symmetric $3\times3$ Majorana matrix; the mass matrix is $6\times6$, and block diagonalisation gives the light neutrino mass matrix

$$
m_\nu \;\simeq\; -\,m_D\,M_R^{-1}\,m_D^{T} ,
$$

a complex symmetric $3\times3$ matrix whose eigenvalues are the light masses. This is the standard type-I seesaw formula; the leading term is exact to relative order $(m_D/M_R)^2$. The formula requires only that $M_R$ be invertible and heavy; it is basis-independent in the sense that the light masses are the eigenvalues, whatever basis the blocks are written in. The diagonal case, $m_D=\mathrm{diag}(a_1,a_2,a_3)$ and $M_R=\mathrm{diag}(b_1,b_2,b_3)$, was checked to reproduce the per-generation suppression $\lambda_i\simeq-a_i^2/b_i$, and it is the only multi-generation case that is safely resolvable in double precision at physical scale ratios; the general non-diagonal formula is quoted from the standard literature.

**The two suppressions.** The seesaw is often described as one suppression, $m_D/M_R$ squared. It is worth separating the two factors. The light mass is small because (i) the Dirac mass is at the electroweak scale while the Majorana mass is heavy, and (ii) the light state has only a small admixture of the heavy state through which to feel the Majorana mass. The first is a hierarchy of scales; the second is the mixing angle $\theta\simeq m_D/M_R$; and the product of $m_D$ with $\theta$ is the light mass. The framework distinguishes the two masses, and the suppression is the statement that the linear chiral pairing is fed into the light state only through the small mixing with the self-conjugate pairing.

## The Biquaternion Form of the Seesaw

**The mass matrix in the framework's objects.** The three blocks of the seesaw matrix are three different framework objects.

- The **upper-left zero** is the absence of a renormalisable Majorana pairing for $\nu_L\in S$; the module's gauge quantum numbers forbid it at the renormalisable level.
- The **off-diagonal $m_D$** is the linear chiral pair, the coefficient of $\tilde{\nabla}\tilde{\Psi}_R=m_D\tilde{\Psi}_L$, with the central phase passing through it.
- The **lower-right $M_R$** is the conjugate self-pairing on the singlet, the Majorana mass built on the real structure; it is the object that violates fermion number by two and that the companion articles keep separate from the linear pair.

The seesaw is therefore not a single biquaternion equation but a **mixing of the two kinds of mass**; the framework's separation of the two is what makes the mixing expressible. The light eigenvalue is the double suppression of the linear pairing by the conjugate pairing.

**Fermion number and the heavy state.** The Dirac block conserves fermion number and the Majorana block violates it by two units. The mass eigenstates are therefore not states of definite fermion number: the light state is mostly the Dirac-like $\nu_L$ but has a tiny admixture of the self-conjugate heavy state. In the limit $M_R\to\infty$ the mixing vanishes, fermion number is restored, and the light state is a massless Weyl fermion. This is the framework's form of the statement that lepton number is violated by the seesaw, and that the violation is suppressed by $m_D/M_R$.

**Sector placement.** The Dirac mass coefficient is central and lies on the scalar line $\mathbb{C}_{\mathbb{B}}$; the light mass generated by the seesaw is likewise a coefficient of the linear chiral pair, hence central. The Majorana pairing is the antilinear object, and its sector placement is the module's reality structure rather than the algebra's sector split; the companion article on the neutrino shows that the naive identification of the Majorana condition with the material sector $\mathbb{M}_-$ fails, because the Dirac operator does not preserve $\mathbb{M}_-$. This article uses the module reality condition and does not place the Majorana mass in a sector of the algebra.

**What the algebra does not decide.** The algebra distinguishes the two masses and supplies the carrier of each; it does not select the heavy scale, does not forbid or require a heavy singlet, and does not relate $m_D$ to the electroweak scale. The companion article on the condensate makes the analogous point for the dynamical mass: the framework supplies the carrier, and the coefficient is empirical. Here it supplies the distinction, and both coefficients are empirical.

## The Majorana Condition and the Counting of States

**The condition halves the components.** A four-component Dirac spinor carries four complex components, and charge conjugation maps it to a different spinor. The Majorana condition $\psi^{c}=\mathcal{C}\psi$ identifies a spinor with its conjugate, and the fixed space of the antilinear involution $\mathcal{C}$ on $\Delta$ has real dimension four, i.e. the Majorana spinor carries **two** independent complex components — one Weyl spinor. The counting is the framework's own: the real structure on the module has a real fixed space of half the real dimension, and the companion article on the neutrino establishes the algebra of $\mathcal{C}$ on $\Delta$.

**Two Majorana fields are one Dirac field.** A Dirac field is equivalent to two Majorana fields of equal mass, and the equivalence is the statement that the module splits, through the real structure, into two copies of the fixed space. The type-I seesaw is a precise realisation of this counting. When the self-conjugate mass vanishes, $M_R=0$, the mass matrix is $\begin{pmatrix}0&m_D\\ m_D&0\end{pmatrix}$, whose eigenvalues are $\pm m_D$: the light and heavy Majorana states are degenerate and reassemble into one Dirac field of mass $m_D$. A nonzero $M_R$ splits the degeneracy and separates the pair into a light and a heavy Majorana state, which is the seesaw. The reassembly works exactly when the self-conjugate mass vanishes, because the degeneracy is what permits the pair to be combined into a single four-component field.

**Degrees of freedom across the spectrum.** For one generation the seesaw replaces a Dirac neutrino of four components by two Majorana neutrinos of two components each: the count is preserved. The heavy Majorana state is its own antiparticle, which is why it is invisible to the vector current and why its decays can violate lepton number — the fermion-sector facts the companion articles record and the mechanism uses. Nothing here is peculiar to the biquaternion algebra; the algebra's role is to carry the real structure $\mathcal{C}$ whose fixed space does the counting.

## Why the Light Neutrino Cannot be Massive at the Renormalisable Level

**The operator analysis.** A renormalisable mass term for $\nu_L$ would be a dimension-four operator of the form $\nu_L^T C^{-1}\nu_L$, i.e. a Majorana pairing of a field in the left-handed doublet with itself. It transforms as a component of a **triplet** of $SU(2)_L$ with hypercharge $-1$ (in the convention $Y=Q-T_3$), and the Standard Model contains no such field and no triplet with which to form a gauge-invariant product; the operator is therefore forbidden. This is the standard dimension counting that opens the seesaw. The framework states it as the module's gauge quantum numbers: the field $\nu_L$ sits in a doublet with $T_3=+\tfrac12$ and $Y=-\tfrac12$, and the symmetric product $(\nu_L\nu_L)$ carries $T_3=+1$ and $Y=-1$.

**The doublet and the singlet.** The same analysis explains why the heavy state need not be a doublet. The right-handed neutrino is a total gauge singlet; the mass operator $\nu_R^{c\,T}C^{-1}\nu_R^{c}$ transforms trivially, is dimension four, and is therefore allowed. The asymmetry of the two cases — forbidden for $\nu_L$, allowed for $\nu_R$ — is the whole of the seesaw's group theory. The framework's contribution is to place the two statements on the same footing: both are statements about which of the two fields has the quantum numbers under which a symmetric self-pairing is invariant.

**The Higgs route.** The left-handed case can be made gauge invariant by multiplying by two Higgs doublets, which is exactly the dimension-five Weinberg operator of the next section. The operator analysis is therefore a tower: dimension four for the singlet, dimension five for the doublet, and nothing below. The seesaw's scale is the price of the missing triplet, and the price is the operator's inverse power of the heavy scale.

## The Stability of the Small Ratio

**The singlet mass is unprotected.** A Dirac mass and the Higgs mass are protected by chiral and gauge symmetries respectively, and their smallness requires an explanation. The Majorana mass of a gauge singlet is protected by nothing: no gauge symmetry forbids it, and the only symmetry that would force it to zero is lepton number. Setting $M_R\to0$ increases the symmetry — lepton number becomes exact — and 't Hooft's naturalness criterion therefore does **not** require $M_R$ to be small; a large $M_R$, even a scale far above the electroweak scale, is technically natural. Conversely, the smallness of $m_D$ relative to $M_R$ is protected by the same chiral symmetry that protects the electron mass.

**Why the ratio is stable.** The ratio $m_D/M_R$ is stable against radiative corrections: the chiral symmetry keeps $m_D$ small and the absence of a symmetry does not make $M_R$ run to a small value; the two scales renormalise multiplicatively without the quadratic sensitivity that afflicts the Higgs mass. The smallness of the light neutrino mass is therefore not a fine-tuning problem in the same sense as the electroweak hierarchy — it is the natural consequence of a heavy singlet. The framework records the argument but does not add to it; the protection is a statement about symmetry, and the framework's symmetries are those of its module, not of lepton number.

**What the argument does not do.** It does not explain *why* the scale is $10^{14}$–$10^{15}$ GeV rather than any other value; naturalness permits any large $M_R$. The size of the scale is fixed only by matching the observed light mass, which is the empirical relation $m_\nu\sim v^2/M_R$ of the next section, and observed neutrino oscillation data. The framework supplies no relation among $m_D$, $M_R$, and $v$, and therefore does not predict the scale.

## The Weinberg Operator and the Scale

**The effective operator.** Below the scale of the heavy state, the seesaw is described by the unique dimension-five operator of the Standard Model, the **Weinberg operator**,

$$
\mathcal{L}_5 = \frac{c_5}{\Lambda}\,(LH)(LH) + \text{h.c.},
$$

where $L$ is the lepton doublet, $H$ the Higgs doublet, and $\Lambda$ the scale of the new physics. After electroweak symmetry breaking, with the Higgs doublet at its expectation value $\langle H\rangle=v=174$ GeV and a coefficient $c_5\sim1$, it generates a Majorana mass for the light neutrino,

$$
m_\nu = \frac{c_5\,v^2}{\Lambda} .
$$

The operator violates lepton number by two units, it is the lowest-dimensional operator that does so, and it is the model-independent statement of the seesaw. Its coefficient was recomputed for the electroweak vacuum expectation value $v=174$ GeV:

| $\Lambda$ (GeV) | $m_\nu=v^2/\Lambda$ (GeV) | $m_\nu$ (eV) |
|---|---|---|
| $10^{14}$ | $3.03\times10^{-10}$ | $0.30$ |
| $10^{15}$ | $3.03\times10^{-11}$ | $0.030$ |
| $10^{16}$ | $3.03\times10^{-12}$ | $0.0030$ |

The observed light neutrino mass scale, inferred from the atmospheric and solar mass-squared differences of order $2.5\times10^{-3}\ \mathrm{eV}^2$ and $7.5\times10^{-5}\ \mathrm{eV}^2$, is of order $0.05$ eV, so a scale $\Lambda$ of order $10^{14}$–$10^{15}$ GeV reproduces the observed magnitude with a coefficient of order one. This is the standard argument for a high seesaw scale, and it is a statement about the size of the object, not a derivation of it.

**The relation between the two descriptions.** The effective operator and the seesaw are the same physics at different scales: matching them gives $c_5/\Lambda \sim m_D^2/(M_R v^2)$, so that $m_\nu\sim m_D^2/M_R$ when $m_D\sim v$. In the framework's terms the dimension-five operator is a product of four module elements — two lepton doublets and two Higgs fields — and its coefficient is the ratio that mixes the linear chiral pairing with the heavy self-conjugate pairing. The framework does not derive the operator's uniqueness (that is standard effective-field-theory counting) and does not fix $\Lambda$; it gives the algebraic reading of the product as a pairing of the module with itself through the Higgs.

**What is not derived.** The seesaw scale, the Yukawa couplings that produce $m_D$, and the heavy Majorana matrix $M_R$ are inputs. The light neutrino masses and mixing angles therefore are not predicted; the mechanism relates them to inputs that the framework does not supply. The companion article on the CKM matrix makes the analogous statement for the quark sector.

## Integrating Out the Heavy State

**The tree-level matching.** The light mass can be derived rather than diagonalised. Take the renormalisable Lagrangian of one generation with a singlet $N_R$,

$$
\mathcal{L} = y\,\bar{L}\tilde{H}N_R + \text{h.c.} + \frac{M_R}{2}\,\overline{N_R^{c}}N_R + \cdots ,
$$

where $y$ is the Yukawa coupling, $\tilde{H}=i\sigma^2H^{*}$ the charge-conjugate doublet, and $L$ the lepton doublet. The field $N_R$ is heavy and has no kinetic term in the low-energy description; its classical equation of motion is

$$
\overline{N_R^{c}} = -\frac{y}{M_R}\,\bar{L}\tilde{H} ,
$$

which is algebraic, so the heavy field can be eliminated exactly at tree level. Substituting it back gives a dimension-five operator among the light fields alone,

$$
\mathcal{L}_5 = -\frac{y^2}{M_R}\,(\bar{L}\tilde{H})(\tilde{H}^{T}L^{c}) + \text{h.c.},
$$

the Weinberg operator, with coefficient $c_5/\Lambda = y^2/M_R$. After electroweak symmetry breaking the operator generates the light Majorana mass

$$
m_\nu = \frac{y^2 v^2}{M_R} = \frac{m_D^2}{M_R},
\qquad m_D = y\,v,
$$

which is the leading result of the matrix diagonalisation, obtained now by elimination rather than by block rotation. The two routes agree, as they must: the matching computes the same operator the diagonalisation computes, and the identification $m_D=yv$ is the standard relation between the Dirac mass and the Yukawa coupling, with $v=\langle H\rangle$. This is the sense in which the seesaw is a *renormalisable* origin for a *non-renormalisable* operator: the heavy field is the ultraviolet completion of the dimension-five term.

**Why the operator is the whole story at low energy.** Below $M_R$ the heavy field cannot be produced, and its only trace is the operator it generates; the Appelquist–Carazzone theorem states that the heavy field's effects decouple into local operators suppressed by powers of $M_R$. The leading one is the dimension-five term above, and the next corrections are suppressed by $1/M_R^2$. The light neutrino sector therefore probes the dimension-five operator, and through it the ratio $m_D^2/M_R$ and no more; the heavy field's other properties are inaccessible. The framework states the operator's product structure — two lepton doublets and two Higgs doublets — and the decoupling theorem supplies the suppression.

**The two suppressions again.** The elimination makes the double suppression explicit. The single insertion of the heavy field gives one power of $1/M_R$ and one factor of the Yukawa coupling from each end; squaring the coupling and drawing the two insertions together gives $y^2/M_R$. The mixing angle $\theta\simeq m_D/M_R$ is the amplitude for the light state to contain the heavy one, and the mass is $m_D$ times that amplitude. The elimination and the diagonalisation are two readings of the same small parameter.

## The Seesaw and the Observed Neutrino Masses

**What oscillation data fix.** Neutrino oscillations measure the two mass-squared differences, $\Delta m^2_{\mathrm{atm}}\simeq2.5\times10^{-3}\ \mathrm{eV}^2$ and $\Delta m^2_{\mathrm{sol}}\simeq7.5\times10^{-5}\ \mathrm{eV}^2$, and the mixing angles of the leptonic matrix; they do not measure the absolute mass scale, because an overall shift of the squared masses is invisible to oscillation. The two differences fix the spacings of the three light masses but leave the lightest mass free, and therefore leave open the **mass ordering**: the normal hierarchy, in which the lightest state is largely the electron neutrino, and the inverted hierarchy, in which two states are nearly degenerate and the third is lighter. The seesaw predicts a hierarchical light spectrum for a hierarchical $m_D$ and $M_R$ but does not fix which ordering.

**The absolute scale.** The absolute scale is bounded from above by cosmology, which constrains the sum of the light neutrino masses to be below of order $0.1$ eV, and from below only by the oscillation data, which require the heaviest state to be at least $\sqrt{\Delta m^2_{\mathrm{atm}}}\simeq0.05$ eV. The seesaw's relation $m_\nu\sim v^2/M_R$ then translates the level of the scale into a range for the heavy mass: masses of order $0.05$ eV correspond to $M_R$ near $10^{14}$–$10^{15}$ GeV for a coefficient of order one. This is the standard estimate, and it is an estimate and not a prediction: the unknown Yukawa and the unknown heavy matrix sit between the observed mass and the scale.

**What the framework adds here.** Nothing quantitative. The framework supplies the two kinds of mass and their mixing, and it inherits the standard-model translation of the light mass into the heavy scale; it does not relate the leptonic mixing to the heavy sector, does not select the ordering, and does not predict the absolute scale. The companion article on the number of generations treats the counting of the light states; the present article states the mechanism and its scale, and stops.

## The Type-II and Type-III Seesaws, and Their Scope

**Type II.** A scalar $SU(2)_L$ triplet with hypercharge one can couple directly to the lepton doublets and, once it acquires an expectation value, generate a light Majorana mass for $\nu_L$ without any heavy fermion. The mechanism is standard, but its agent is a scalar in a triplet representation, and the scalar sector — the doublet, the triplet, the potential, and the symmetry breaking — belongs to the spin-$0$ subcategory of this series and is not developed here. The framework's contribution to a type-II seesaw would be the same as to any scalar: the field is not supplied, and the representation is not a $\mathbb{B}$-module of the required kind. It is recorded for completeness.

**Type III.** A fermionic $SU(2)_L$ triplet can play the role of the heavy state, with the Dirac mass connecting the lepton doublet to the triplet. The mechanism is standard and is closest in structure to the type-I case: the heavy state is again a Majorana fermion, its mass is a self-conjugate pairing, and the light-mass suppression is the same $m_D^2/M_R$. What the framework can say about it is what it can say about type I — the two kinds of mass and their mixing — with the heavy state in a weak triplet rather than a singlet. Nothing in the algebra selects between the types; the selection is a statement about the gauge representations, which the framework does not generate.

**Scope.** All three types share the fermion-sector content of this article: a light state, a heavy self-conjugate state, and a Dirac mixing whose smallness is the source of the suppression. The differences are in the gauge representations of the heavy agent, and those representations are standard-model input. The framework's contribution is the same in all three cases, and this article does not use the variants beyond noting them.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The Dirac mass as the linear chiral pair | **Supplied**; the off-diagonal block of the seesaw matrix |
| The Majorana mass as the self-conjugate pairing on the module's real structure | **Supplied**; the heavy block; distinct from the linear pair |
| The charge-conjugation real structure $\mathcal{C}^2=1$ on $\Delta$ | **Supplied**; from the companion article on the neutrino |
| The absence of a renormalisable mass for $\nu_L\in S$ | **Standard** (gauge quantum numbers); transcribed |
| The singlet's anomaly-silence and the availability of $M_R$ | **Supplied** by the anomaly article's conditions |
| The type-I matrix, its exact $2\times2$ eigenvalues, and $m_\nu\simeq-m_D^2/M_R$ | **Supplied** at leading order; the $2\times2$ eigenvalues recomputed |
| The general formula $m_\nu\simeq-m_DM_R^{-1}m_D^{T}$ | **Transcribed**; standard |
| The dimension-five Weinberg operator and $m_\nu=v^2/\Lambda$ | **Transcribed**; standard, with the scale verified |
| The values of $m_D$, $M_R$, and $\Lambda$ | **Not supplied**; empirical |
| Leptogenesis, and the cosmological consequence of the heavy state | **Outside**; not treated here |
| A scalar triplet (type II) or fermion triplet (type III) | **Outside**; the scalar sector belongs to the spin-$0$ subcategory |

## Open Questions

1. **The module reality condition in the algebra.** The Majorana pairing is built on the module's real structure, which the companion article on the neutrino identifies with the coefficient conjugation ${}^{*}$; its algebra-level form, and its relation to the algebra's real structure $\flat$, remain open there. The type-I seesaw uses the module form only.

2. **The origin of the heavy scale.** Nothing in the framework fixes $M_R$ or explains why a heavy gauge singlet should exist. Whether the framework can relate the scale to a geometric or algebraic quantity is open.

3. **The $\flat$-pairing and the see-saw.** Whether the separate single-field equation built on the algebra's real structure $\flat$ — whose $\flat$-pairing is compatible with, but does not derive, a Majorana mass — can be brought into the seesaw is not settled. The present article uses the module reality condition of the companion article and leaves the $\flat$ equation to one side.

4. **Leptogenesis and the matter asymmetry.** The heavy Majorana state can generate a lepton asymmetry through its CP-violating decays, and the asymmetry is converted to the baryon asymmetry. The framework has no CP-violating phase for the heavy sector and no Boltzmann machinery; the question is outside this article.

## Summary

The seesaw generates a light neutrino mass from the mixing of two masses of different kinds. In biquaternionic form the two are exactly the framework's two objects: the **Dirac mass** is the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R=m_D\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_D\tilde{\Psi}_R$, which conserves fermion number; the **Majorana mass** is the self-conjugate pairing on the spinor module's antilinear real structure $\mathcal{C}$ with $\mathcal{C}^2=1$, which violates fermion number by two units. The type-I mass matrix in the $(\nu_L,\nu_R^{c})$ basis is the symmetric matrix $\begin{pmatrix}0&m_D\\ m_D&M_R\end{pmatrix}$, whose exact eigenvalues are $\lambda_\pm=\tfrac12(M_R\pm\sqrt{M_R^2+4m_D^2}\,)$; the light one is $\lambda_-\simeq-m_D^2/M_R$ and the heavy one is $\lambda_+\simeq M_R$, with mixing $\theta\simeq m_D/M_R$. The values were recomputed: $m_D=100$ GeV and $M_R=10^{15}$ GeV give $m_\nu=-10^{-11}$ GeV $=0.01$ eV, and at the resolvable scale $M_R=10^6$ GeV the exact eigenvalue reproduces $-m_D^2/M_R$ exactly. For several generations the light matrix is $m_\nu\simeq-m_DM_R^{-1}m_D^{T}$, which is standard and whose diagonal case was verified.

The right-handed singlet that the mechanism needs is a gauge singlet and contributes nothing to any anomaly cancellation condition, so the heavy state is unconstrained by the consistency of the spectrum. Below the heavy scale the mechanism is the unique dimension-five Weinberg operator $(LH)(LH)/\Lambda$, which gives $m_\nu=v^2/\Lambda$; with $v=174$ GeV this is $0.03$ eV at $\Lambda=10^{15}$ GeV, the observed order of magnitude. The framework supplies the distinction between the two masses and the carrier of each, and thereby the possibility of the mixing; it does not fix $m_D$, $M_R$, or $\Lambda$, does not select among the type-I, type-II, and type-III variants (whose differences are gauge representations it does not generate, and the type-II agent belongs to the spin-$0$ subcategory), and does not predict the light masses.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\Delta=S\oplus\bar{S}$, $S=\mathbb{C}^2=(\tfrac12,0)$ | Dirac module; left-handed Weyl module |
| $\nu_L\in S$, $\nu_R^{c}=\mathcal{C}\nu_L$ | Left-handed neutrino and its conjugate |
| $\mathcal{C}:\psi\mapsto K\psi^{*}$, $KK^{*}=I_4$ | Module real structure; charge conjugation |
| $\psi^{c}=\psi$ | Majorana condition (fixed space, real dimension four) |
| $\tilde{\nabla}\tilde{\Psi}_R=m_D\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_D\tilde{\Psi}_R$ | Linear Dirac mass pair |
| $m_D$, $M_R$ | Dirac mass and heavy Majorana mass |
| $\begin{pmatrix}0&m_D\\ m_D&M_R\end{pmatrix}$ | Type-I mass matrix in $(\nu_L,\nu_R^{c})$ |
| $\lambda_\pm=\tfrac12(M_R\pm\sqrt{M_R^2+4m_D^2})$ | Exact eigenvalues |
| $m_\nu=\lambda_-\simeq-m_D^2/M_R$ | Light mass (type-I, one generation) |
| $m_\nu\simeq-m_DM_R^{-1}m_D^{T}$ | Light mass matrix (type-I, $N_g$ generations) |
| $\theta\simeq m_D/M_R$ | Light–heavy mixing angle |
| $c_5(LH)(LH)/\Lambda$ | Dimension-five Weinberg operator |
| $m_\nu=c_5v^2/\Lambda$, $v=174$ GeV | Light mass from the Weinberg operator |
| $\flat=-\dagger$ | The algebra's real structure (separate object) |
| $Y=0$, $SU(3)_c$ singlet | Quantum numbers of the heavy state |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- P. Minkowski, "$\mu\to e\gamma$ at a rate of one out of $10^9$ muon decays?", *Physics Letters B* **67** (1977) 421–428, for the first appearance of the heavy-neutrino seesaw.
- T. Yanagida, "Horizontal gauge symmetry and masses of neutrinos," in *Proceedings of the Workshop on the Baryon Number of the Universe and Unified Theories* (KEK, 1979), for the type-I seesaw.
- M. Gell-Mann, P. Ramond, and R. Slansky, "Complex spinors and unified theories," in *Supergravity* (North-Holland, 1979), for the seesaw in grand unification.
- R. N. Mohapatra and G. Senjanović, "Neutrino mass and spontaneous parity nonconservation," *Physical Review Letters* **44** (1980) 912–915, for the seesaw and lepton-number violation.
- S. Weinberg, "Baryon- and lepton-nonconserving processes," *Physical Review Letters* **43** (1979) 1566–1570, for the dimension-five operator that generates the light neutrino mass.
- R. N. Mohapatra and P. B. Pal, *Massive Neutrinos in Physics and Astrophysics* (World Scientific, 2004), for the type-I, type-II, and type-III seesaws and their phenomenology.
- M. Fukugita and T. Yanagida, "Baryogenesis without grand unification," *Physics Letters B* **174** (1986) 45–47, for leptogenesis from the heavy Majorana state.
- K. Nakamura and S. T. Petcov, "Neutrino masses, mixing, and oscillations," in *Review of Particle Physics*, for the observed mass-squared differences and the light mass scale.
- E. Majorana, "Teoria simmetrica dell'elettrone e del positrone," *Nuovo Cimento* **14** (1937) 171–184, for the self-conjugate spinor and the Majorana mass.
- A. Zee, "A theory of lepton number violation and neutrino Majorana masses," *Physics Letters B* **93** (1980) 389–393, for the radiatively generated Majorana mass and the scalar-triplet variant.
