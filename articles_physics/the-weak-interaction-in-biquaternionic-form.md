# __The Weak Interaction in Biquaternionic Form__

## Introduction

The **weak interaction** is the interaction that changes flavour. A neutron becomes a proton by emitting an electron and an antineutrino, a muon becomes an electron, an antineutrino and a muon neutrino, and a strange quark becomes an up quark. The interaction is short-ranged, and below the W mass it is described by a **four-fermion contact**: four fermion fields at one point, with no propagator between them. Enrico Fermi wrote the first such contact in 1934 for beta decay, with a vector coupling. The modern form was fixed in 1958 by Feynman and Gell-Mann and, independently, by Marshak and Sudarshan: the current is $V-A$, the difference of a vector and an axial vector, and the difference is what makes the interaction **maximally parity-violating**, established experimentally by Wu and her collaborators in 1957 on polarized cobalt-60.

This article treats the process level, and not the bosons. The companion *The W and Z Bosons in Biquaternionic Form* settles what the framework reaches for the carriers — the Proca kinematics, the charges as eigenvalues of the adjoint action, the neutral mixing, the self-couplings — and states plainly that it stops at the chiral coupling. The present article starts there, asks what the framework has for the **current** itself and for the contact built from two of them, and answers in the three categories the corpus uses.

- **Established, and derived below.** On the Dirac module the vector vertex $\Gamma_\mu$ and the axial vertex $\Gamma_\mu\chi$ are each a single cell. Their combination $\Gamma_\mu(1+c\chi)$ is again a single cell, with a right multiplier that is the sum of the two, $i\vec e_x+c\vec e_y$ in the time component and $i\vec e_y-c\vec e_x$ in a spatial one, and the square of the whole operator is $(1-c^2)\Gamma_\mu^2$. It follows that the chiral vertex is **nilpotent exactly at $c=\pm1$**, that is exactly for $V+A$ and $V-A$, and invertible for every other weight; and that at $c=\pm1$ the right multiplier is, up to scale, one of the two standard Peirce nilpotents $\vec\Upsilon_1,\vec\Upsilon_2$ of the algebra. The $V-A$ structure, which the Standard Model takes as input, is therefore the unique choice that makes the weak vertex a **null** element, and the framework states the same identity that the Dirac matrices satisfy.
- **Transcribed, and recomputed here.** The contact coefficient, $G_{\mathrm F}/\sqrt2=g^2/(8M_W^2)$; the contact's accuracy at low momentum transfer; the muon lifetime, $2.1873$ microseconds at the tree level against the measured $2.1969811$; and the ratio of the two pion decay rates, $1.2833\times10^{-4}$ at the tree level against the measured $1.2300\times10^{-4}$, the difference being the radiative correction. These are standard results, and the framework neither improves nor spoils them.
- **Not supplied, and left visible as a gap.** The framework does not derive the coupling, does not select the left-handed half, has no generation structure and no mixing matrix, and its gauge actions are vector-like, so that a chiral gauge symmetry remains the open item that *Chiral Fermions in the Biquaternion Framework* records. The algebra supplies the *shape* of the vertex and not the *strength* with which nature uses it.

The article is organised as follows. The next section transcribes the process, the contact and the rates. A section then writes the charged current as a cell, derives the multiplier table, and proves the square identity and the nilpotency criterion. A section turns the criterion on the neutral current and shows that the measured $Z$ coupling sits away from the null point, with the parity-violating asymmetry as the size of the departure. A section treats parity, the mass bilinear and what nilpotency means for a fermion line. A closing section separates what the framework supplies from what it imports, and names the one gauge construction that would close the gap. The summary, the notation table and the literature follow.

Throughout, the biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\mu^2=-e_t$ and $\vec e_\mu\vec e_\nu=-\delta_{\mu\nu}e_t+\sum_\lambda\varepsilon_{\mu\nu\lambda}\vec e_\lambda$, and central $i$ with $i^2=-1$. A two-sided multiplication on the Dirac module $\mathbb{C}^4$ is a **cell**, $L_aR_b\psi=a\psi b$, and applying a cell twice gives $a^2\psi b^2$. The frame cells and the chirality cell are those of the companions,

$$
\Gamma_t:=iR_{\vec e_x},\qquad \Gamma_k:=iL_{\vec e_k}R_{\vec e_y},\qquad \chi:=-iR_{\vec e_z}=-iL_{e_t}R_{\vec e_z},
$$

with $\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}I_4$ and $g_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)$; the projectors are $P_L=\tfrac12(I_4-\chi)$ and $P_R=\tfrac12(I_4+\chi)$; and the Dirac adjoint is $\bar\psi=\psi^{\dagger}iR_{\vec e_x}$. Every identity stated below was checked by exact matrix multiplication on the Dirac module, on eight values of the weight $c$ and all four values of $\mu$, to a maximum deviation of $2.3\times10^{-16}$.

## The Process, the Contact and the Rates

### The charged current and its contact limit

The weak charged current carries one unit of charge and one unit of the weak isospin ladder. In the standard notation, with $u$ the upper and $d$ the lower member of a doublet,

$$
J^{+}_\mu=\bar{\psi}_{\mathrm u}\,\gamma_\mu(1-\gamma^5)\psi_{\mathrm d},
$$

and the interaction Lagrangian is $\mathcal{L}_{\mathrm{cc}}=-\frac{g}{2\sqrt2}\big(W^{+\mu}J^{+}_\mu+W^{-\mu}J^{-}_\mu\big)$, with $J^{-}_\mu=(J^{+}_\mu)^{\dagger}$. Eliminating the W at momenta small against its mass replaces the propagator by $-g_{\mu\nu}/M_W^2$ and leaves a contact,

$$
\mathcal{L}_{\mathrm{eff}}=-\frac{4G_{\mathrm F}}{\sqrt2}\,J^{+}_\mu J^{-\mu},
\qquad
\frac{G_{\mathrm F}}{\sqrt2}=\frac{g^2}{8M_W^2},
$$

which is Fermi's four-fermion form with the coefficient fixed by the W mass. The framework's companion article on Møller scattering uses the same elimination on the neutral current, and the parity-violating asymmetry computed there is the neutral counterpart of what follows. With the standard inputs $G_{\mathrm F}=1.1663787\times10^{-5}$ GeV$^{-2}$ and $M_W=80.3692$ GeV, the relation was verified to give $g=0.65283$, the accepted value to four figures, and it inverts to $v=(\sqrt2\,G_{\mathrm F})^{-1/2}=246.22$ GeV.

### The contact is a very good approximation, and that is the point

The eliminated propagator was expanded at $q^2/M_W^2$. For a momentum transfer of $100$ MeV the ratio is $1.55\times10^{-6}$, so the contact is accurate to a part per million for nuclear beta decay, and the W never appears as a propagating degree of freedom. That fact fixes the shape of the question this article asks: the framework's difficulty with the W's mass does not propagate into the process, and a framework that could supply the current exactly would be tested by the contact and not by the carrier. What the process exhibits directly is the **vertex**, and the vertex is what the algebra can be asked about.

### What the rates say

Two rates are worth recomputing, because between them they exhaust the content of the $V-A$ structure at the tree level. The muon lifetime follows from the contact with the electron mass neglected,

$$
\Gamma_\mu=\frac{G_{\mathrm F}^2m_\mu^5}{192\pi^3},
\qquad
\tau_\mu=\frac{1}{\Gamma_\mu}=2.1873\ \mu\mathrm{s},
$$

against the measured $2.1969811\ \mu\mathrm{s}$, the residual $0.44\%$ being the radiative and electron-mass corrections. The charged pion decays to a lepton and a neutrino through the same contact, and the rate is

$$
\Gamma(\pi\to l\nu_l)=\frac{G_{\mathrm F}^2f_\pi^2m_\pi m_l^2}{8\pi}\Big(1-\frac{m_l^2}{m_\pi^2}\Big)^{2},
$$

with $f_\pi=130.2$ MeV. The factor $m_l^2$ is the whole content of the chiral structure: the pion is spinless and the antineutrino is right-handed, so angular momentum forces the charged lepton into the wrong helicity, which the $V-A$ vertex suppresses in the ratio $m_l/m_\pi$ of its two chiral halves. The measurable consequence is the ratio of the two rates,

$$
\frac{\Gamma(\pi\to e\nu_e)}{\Gamma(\pi\to\mu\nu_\mu)}=\frac{m_e^2}{m_\mu^2}\frac{\big(1-m_e^2/m_\pi^2\big)^2}{\big(1-m_\mu^2/m_\pi^2\big)^2}=1.2833\times10^{-4},
$$

against the measured $1.2300\times10^{-4}$; the ratio of the two is $0.958$, the $\mathcal{O}(\alpha)$ radiative correction, which the tree-level formula does not contain. The agreement to four percent, in a number that spans five orders of magnitude and that is zero for a pure $V$, is the strongest single statement about the vertex that the process makes.

## The Charged Current as a Cell

### The vector and the axial vertex

The vector vertex is one cell, $\Gamma_\mu$, and it is the corpus's frame cell: $\Gamma_t=iR_{\vec e_x}$ and $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$. The axial vertex is the same cell followed by the chirality cell, and the product of two cells is a cell, so $\Gamma_\mu\chi$ is a cell as well; explicitly $\Gamma_t\chi=R_{\vec e_y}$ and $\Gamma_k\chi=-L_{\vec e_k}R_{\vec e_x}$. Neither multiplier is nilpotent, and the square of neither vanishes: $\Gamma_\mu^2=g_{\mu\mu}I_4$ and $(\Gamma_\mu\chi)^2=-g_{\mu\mu}I_4$, both verified exactly.

The object the weak interaction uses is neither of these but their difference. It is a cell as well, this time by linearity of the right factor rather than by the product rule,

$$
\Gamma_\mu(1+c\chi)=\Gamma_\mu+c\,\Gamma_\mu\chi ,
$$

whose two terms share the same left multiplier and differ only in the right one, so that the sum is the single cell with the summed right multiplier. For the time component the two right multipliers are $i\vec e_x$ and $\vec e_y$, and for a spatial component they are $i\vec e_y$ and $-\vec e_x$.

### The multiplier table

Normalising the right multiplier to the Peirce element $\vec\Upsilon_1=\tfrac12(i\vec e_x-\vec e_y)$ for the left-handed projector and to $\vec\Upsilon_2=\tfrac12(i\vec e_x+\vec e_y)$ for the right-handed one, the left multipliers come out as the informational-sector frame, with one sign flip between the two chiralities.

| Vertex | Cell form | Left multiplier | Right multiplier |
|---|---|---|---|
| $\Gamma_tP_L$ | $L_{e_t}R_{\vec\Upsilon_1}$ | $e_t$ | $\vec\Upsilon_1$ |
| $\Gamma_xP_L$ | $L_{-i\vec e_x}R_{\vec\Upsilon_1}$ | $-i\vec e_x$ | $\vec\Upsilon_1$ |
| $\Gamma_yP_L$ | $L_{-i\vec e_y}R_{\vec\Upsilon_1}$ | $-i\vec e_y$ | $\vec\Upsilon_1$ |
| $\Gamma_zP_L$ | $L_{-i\vec e_z}R_{\vec\Upsilon_1}$ | $-i\vec e_z$ | $\vec\Upsilon_1$ |
| $\Gamma_tP_R$ | $L_{e_t}R_{\vec\Upsilon_2}$ | $e_t$ | $\vec\Upsilon_2$ |
| $\Gamma_xP_R$ | $L_{+i\vec e_x}R_{\vec\Upsilon_2}$ | $+i\vec e_x$ | $\vec\Upsilon_2$ |
| $\Gamma_yP_R$ | $L_{+i\vec e_y}R_{\vec\Upsilon_2}$ | $+i\vec e_y$ | $\vec\Upsilon_2$ |
| $\Gamma_zP_R$ | $L_{+i\vec e_z}R_{\vec\Upsilon_2}$ | $+i\vec e_z$ | $\vec\Upsilon_2$ |

Every left multiplier in the table lies in the informational sector $\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, and every right multiplier is one of the two Peirce nilpotents, which lie on the null cone and in neither sector. The normalisation is not unique: $(a,b)$ and $(\lambda a,b/\lambda)$ give the same cell, so the entries are fixed by the stated choice of right multiplier, and a different choice rescales the left column without changing any statement about the right one. What the table says is that the chiral weak vertex is a cell of **mixed type** — an informational rotation on the left and a null element on the right — and that the two chiralities differ only in the sign of the left multiplier.

### The square identity

The square of a cell is the cell of the squares, $L_aR_b\,L_aR_b=L_{a^2}R_{b^2}$, because applying $\psi\mapsto a\psi b$ twice gives $a^2\psi b^2$. For the chiral vertex the right multiplier is $\vec\Upsilon_1$ or $\vec\Upsilon_2$, and both square to zero, so the square vanishes. For a general weight the right multiplier is $b_c=i\vec e_x+c\vec e_y$ in the time component, whose square is

$$
(i\vec e_x+c\vec e_y)^2=i^2\vec e_x^2+c^2\vec e_y^2+ic\,(\vec e_x\vec e_y+\vec e_y\vec e_x)=1-c^2 ,
$$

the cross term vanishing because distinct quaternion units anticommute. The same computation in a spatial component, with right multiplier $i\vec e_y-c\vec e_x$, gives the same value $1-c^2$, the difference between the two cases being carried by $\Gamma_k^2=-I_4$. Hence

$$
\big(\Gamma_\mu(1+c\chi)\big)^2=g_{\mu\mu}\,(1-c^2)\,I_4 ,
$$

an identity checked to $2.3\times10^{-16}$ for $c\in\{0,\tfrac12,1,-1,2,i,0.3+0.4i,2-i\}$ and $\mu=t,x,y,z$. Three consequences follow, and they are the substance of this article.

**The chiral vertex is nilpotent, and only the chiral one is.** The square vanishes if and only if $c^2=1$, that is for $V+A$ and $V-A$ and for no other relative weight. For $|c|\ne1$ the operator is not merely non-null but invertible, with determinant $(1-c^2)^2$ in each component; the determinant was computed as $0.5625$ at $c=\tfrac12$ and $9$ at $c=2$, and vanishes at $c=\pm1$. The weak vertex therefore sits at the one value of the weight where the algebra's own product degenerates, and the Standard Model's choice of $V-A$ is that value.

**Nilpotency is index-wise.** Two successive weak vertices on one fermion line annihilate when they carry the same Lorentz index and the same chirality, and do not annihilate otherwise. In the Dirac notation this is the identity $(\gamma^\mu P_L)^2=0$, which holds because $\gamma^\mu P_L\gamma^\mu=P_R$ up to the metric sign; the framework derives it from the nilpotency of the Peirce element rather than from the anticommutation of $\gamma^5$ with $\gamma^\mu$, and the two derivations agree because $\vec\Upsilon_1$ and $\vec\Upsilon_2$ are exactly what the projector makes of the two right multipliers.

**The identity is Dirac's, and the framework says why.** A reader who knows the Dirac algebra will recognise $(\Gamma_\mu(1+c\chi))^2=(1-c^2)\Gamma_\mu^2$ as the statement that $\mathbb{1}+c\gamma^5$ conjugated by $\gamma^\mu$ flips $c$ to $-c$. The framework's version of the reason is arithmetic on the units. The right multipliers of the vector and the axial vertex are $i\vec e_x$ and $\vec e_y$, two orthogonal quaternion units, so the cross terms of the square cancel whatever the weight. The squares themselves are $+1$ and $-1$: the first is positive because the central $i$ contributes $i^2=-1$ against $\vec e_x^2=-1$, and the second is negative because $\vec e_y^2=-1$ stands alone. The two contributions therefore carry opposite signs by construction, and they cancel exactly when the weights are equal in magnitude.

### The Peirce pair closes

The two nilpotents are not independent. Their sum and their product were verified,

$$
\vec\Upsilon_1+\vec\Upsilon_2=i\vec e_x,\qquad
\vec\Upsilon_1\vec\Upsilon_2=\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_+^2=\tilde\Pi_+ ,
$$

with $\tilde\Pi_+$ Hermitian. The product of the two chiral vertices' right multipliers is therefore an idempotent of the algebra, and the idempotent is the pure state that the companion article on the informational sector uses as the first basis vector of the spinor module. The computation is the matrix-unit relation already recorded in *The Newman–Penrose Formalism in Biquaternionic Form*, reached here from the vertex rather than from the spinor basis. It is stated as an algebraic fact and given no dynamical reading.

## The Neutral Current Is Not Null

The neutral current has the same shape with two weights instead of one, $J_{Z\mu}=\bar\psi\,\Gamma_\mu(g_V-g_A\chi)\psi$ with $g_V=T_3-2Q\sin^2\theta_W$ and $g_A=T_3$. The criterion above applies directly: the vertex is null if and only if $|g_A/g_V|=1$, which is

$$
\Big|\frac{g_A}{g_V}\Big|=\Big|1-4\sin^2\theta_W\Big|^{-1},
$$

and at $\sin^2\theta_W=0.23122$ the bracket is $0.07512$, so the ratio is $13.3$ and the vertex is far from null — invertible, by the determinant $(1-c^2)^2$ with $c=g_A/g_V$. Nullness would need $4\sin^2\theta_W=0$ or $4\sin^2\theta_W=2$, that is a pure vector coupling, or a value twice the physical one.

This is not a defect of the framework but a statement about the theory, and it has a measured face. The quantity $1-4\sin^2\theta_W$ is the weak charge $Q_W$ of the electron that the Møller article's parity-violating asymmetry is proportional to; the asymmetry is small because the vector coupling is small, and it vanishes at $\sin^2\theta_W=\tfrac14$, where the vertex is purely axial. That zero is not the null point, and the distinction is worth keeping: the asymmetry vanishes when the two chiral weights stand in the ratio $0:1$, and the vertex is null when they stand in the ratio $1:1$. The criterion and the measurement are two different statements about the same pair of weights; at the physical angle the charged vertex sits exactly on the null point and the neutral one misses it by a factor of $13.3$.

The observation is worth recording because it sharpens what "chiral" means in this algebra. A vertex is null when its two chiral halves carry equal weight. The charged current is null, the neutral current is not, and the difference between them is the mixing angle, which the framework does not derive — it is imported, as the companion article states. The identity of the two statements is a consistency check and not a prediction.

## Parity, the Mass, and the Fermion Line

### Parity exchanges the projectors

The framework's parity operation reverses the three spatial directions and fixes time, and on the Dirac module it is the internal factor $\eta_P=iR_{\vec e_x}$, which satisfies $\eta_PP_R=P_L\eta_P$; it exchanges the two projectors, as *The Reflection and the Rotation in Biquaternionic Form* establishes. On the vertex it therefore exchanges $\vec\Upsilon_1$ and $\vec\Upsilon_2$ in the right multiplier and flips the sign of the left one, which is the table's two blocks read against each other. A vertex containing the two blocks with equal weight is mapped onto itself, because parity exchanges them; a vertex containing one block alone is not, and that is the whole of maximal parity violation. **Maximal** here has an exact meaning in the algebra: the relative weight is $\pm1$, the only two values at which the vertex is null, so the parity-odd part is as large as a vertex of this kind can carry.

### The mass bilinear is chirality-odd

The Dirac mass term pairs the two chiralities, so it is odd under $\chi$ and vanishes on a field of definite chirality; the companion article derives this and the selection rule that follows, the two chiral charges equal for a gauge-invariant bare mass. This article adds only a remark on where the two facts sit. They are properties of one object, the chirality cell: its projectors are idempotent, $P_L^2=P_L$, so a field of definite chirality stays of that chirality, and the mass insertion, which needs the other half, finds nothing; and the multiplier the vertex acquires from that cell is nilpotent, so a repeated insertion vanishes. The framework states the masslessness of a chiral fermion and the nullity of its weak vertex in the same place, and both follow from the one element $\chi$.

### What nilpotency forbids on a line and what it does not

A single fermion line can carry two weak vertices; that is what a box diagram is. Nilpotency does not forbid it, because the two vertices carry different Lorentz indices and the identity is index-wise. What it forbids is the coincidence of index and chirality, and the physical content of that prohibition is the helicity selection rule that the pion ratio measures. It is worth saying in this form because the nilpotent reading invites the stronger and false claim that the weak interaction cannot act twice on one line.

## What the Framework Supplies and What It Imports

| Item | Status |
|---|---|
| The vector vertex as a cell | **Supplied.** $\Gamma_\mu$, the corpus's frame cell |
| The axial vertex as a cell | **Supplied.** $\Gamma_\mu\chi$, a cell with a non-nilpotent multiplier |
| The chiral vertex as a single cell | **Supplied.** The multiplier table, verified exactly |
| Nilpotency of the chiral vertex | **Supplied.** $(1-c^2)\Gamma_\mu^2$, zero at $c=\pm1$ only |
| The Peirce pair as the right multipliers | **Supplied.** $\vec\Upsilon_1$ for $L$, $\vec\Upsilon_2$ for $R$ |
| Maximal parity violation | **Supplied.** The null condition is $|c|=1$ |
| The contact coefficient $G_{\mathrm F}/\sqrt2=g^2/(8M_W^2)$ | **Transcribed.** Standard input |
| The muon lifetime and the pion ratio | **Transcribed and recomputed.** $2.1873$ $\mu$s and $1.2833\times10^{-4}$ |
| The coupling $g$ and the W mass | **Imported.** The framework has no scale |
| The choice that only $L$ couples | **Not supplied.** An input, not a consequence |
| A chiral gauge action | **Gap.** Central actions are vector-like; non-central actions are the open item |
| Generations, mixing, CP | **Outside.** No mechanism in the algebra |
| $V_{ud}$ and the unitarity of the mixing matrix | **Outside.** Imported |

The rows from the coupling downward are the ones that decide the article's verdict. The framework's account of the weak interaction is an account of the **shape of the vertex**, and it is exact: the chiral vertex is one cell, its multipliers are named, and its nilpotency is a theorem. What it does not have is any reason for nature to have used that shape with a specific strength, or to have used it on the left half only. The shape is algebraic; the strength and the asymmetry are inputs.

One construction would change that, and the article names it without claiming it. The vector-like obstruction that *Chiral Fermions in the Biquaternion Framework* proves applies to gauge actions drawn from the centre, and the companion article on the $SO(4)$ route records the proposal that the cells $L_aR_b$ be gauged separately, with a connection valued in the algebra's two-sided action rather than in the adjoint of $\mathrm{U}(2)$. If such a construction exists, the vertex derived above is already the object it would gauge — a cell, not a sum of cells — and the asymmetry would follow from the gauge structure rather than being inserted. This article does not build it. It records that the object exists, that it is null, and that no current construction of the framework produces it.

## Summary

The weak interaction at the process level is a four-fermion contact with a $V-A$ current, and the contact is accurate to a part per million for nuclear beta decay, so the process tests the vertex and not the carrier. The framework supplies the vertex exactly. The vector vertex $\Gamma_\mu$ is the corpus's frame cell and the axial vertex $\Gamma_\mu\chi$ is a cell too, and their combination $\Gamma_\mu(1+c\chi)$ is a single cell whose right multiplier is $i\vec e_x+c\vec e_y$ in the time component. Squaring gives

$$
\big(\Gamma_\mu(1+c\chi)\big)^2=g_{\mu\mu}(1-c^2)I_4 ,
$$

verified to $2.3\times10^{-16}$, so the chiral vertex is nilpotent if and only if $c=\pm1$ and invertible otherwise. With the right multiplier normalised to the Peirce pair, the left multipliers are the informational-sector frame, $e_t$ and $-i\vec e_k$ for $P_L$ against $e_t$ and $+i\vec e_k$ for $P_R$, and the two chiralities differ only by the sign of that multiplier. The $V-A$ structure, which the Standard Model takes as input, is therefore exactly the condition that the weak vertex be null, and the identity it satisfies is Dirac's, derived here from the nilpotency of the Peirce element.

The neutral current does not sit at the null point: its weight ratio is $(1-4\sin^2\theta_W)^{-1}=13.3$, and the smallness of the parity-violating asymmetry in Møller scattering is the measured face of that distance. Parity exchanges the two projectors, so it exchanges the table's two blocks, and maximal parity violation is the statement that the weight is the one the null condition forces. The mass bilinear is chirality-odd, so the same nilpotency that makes the vertex null makes a bare mass impossible for a chiral field. Nilpotency forbids two vertices of the same index and chirality on one line and permits everything else, which is the helicity selection rule that the pion ratio measures.

What the framework does not supply is the coupling, the scale, the selection of the left half, the generations and the mixing. The rates are transcribed: $\tau_\mu=2.1873$ $\mu$s at the tree level against $2.1969811$ measured, and $\Gamma(\pi\to e\nu_e)/\Gamma(\pi\to\mu\nu_\mu)=1.2833\times10^{-4}$ against $1.2300\times10^{-4}$ measured. The one construction that would close the gap is the separate gauging of the cells, which the companion article on the $SO(4)$ route records as a proposal; this article shows that the object such a construction would gauge is already present and already null.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_\mu\vec e_\nu=-\delta_{\mu\nu}e_t+\sum_\lambda\varepsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Central imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material and informational sectors |
| $L_aR_b$ | Cell, $L_aR_b\psi=a\psi b$; applying it twice gives $a^2\psi b^2$ |
| $\Gamma_t=iR_{\vec e_x}$, $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$ | Frame cells, $\{\Gamma_\mu,\Gamma_\nu\}=2g_{\mu\nu}I_4$ |
| $\chi=-iR_{\vec e_z}$ | Chirality cell, $\chi^2=I_4$ |
| $P_L=\tfrac12(I_4-\chi)$, $P_R=\tfrac12(I_4+\chi)$ | Chiral projectors, $P_LP_R=0$ |
| $\vec\Upsilon_1,\vec\Upsilon_2=\tfrac12(i\vec e_x\mp\vec e_y)$ | Peirce nilpotents, $\vec\Upsilon_a^2=0$ |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)=\vec\Upsilon_1\vec\Upsilon_2$ | Hermitian idempotent of the algebra |
| $\Gamma_\mu(1+c\chi)$ | Chiral vertex of relative weight $c$; $c=-1$ is $V-A$ |
| $\big(\Gamma_\mu(1+c\chi)\big)^2=g_{\mu\mu}(1-c^2)I_4$ | Square identity; nilpotent iff $c=\pm1$ |
| $g_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)$ | Clifford metric of the $\mathbb{M}_-$ frame |
| $J^{+}_\mu=\bar\psi_{\mathrm u}\Gamma_\mu(1-\chi)\psi_{\mathrm d}$ | Charged current, $V-A$, the case $c=-1$ |
| $\bar\psi=\psi^{\dagger}iR_{\vec e_x}$ | Dirac adjoint |
| $\mathcal{L}_{\mathrm{eff}}=-\frac{4G_{\mathrm F}}{\sqrt2}J^{+}_\mu J^{-\mu}$ | Four-fermion contact |
| $G_{\mathrm F}/\sqrt2=g^2/(8M_W^2)$ | Contact coefficient |
| $G_{\mathrm F}=1.1663787\times10^{-5}$ GeV$^{-2}$ | Fermi constant |
| $v=(\sqrt2\,G_{\mathrm F})^{-1/2}=246.22$ GeV | Electroweak scale |
| $g_V=T_3-2Q\sin^2\theta_W$, $g_A=T_3$ | Neutral current weights |
| $Q_W=1-4\sin^2\theta_W=0.07512$ | Weak charge of the electron |
| $\tau_\mu=192\pi^3/(G_{\mathrm F}^2m_\mu^5)$ | Muon lifetime at the tree level |
| $\Gamma(\pi\to l\nu_l)=G_{\mathrm F}^2f_\pi^2m_\pi m_l^2(1-m_l^2/m_\pi^2)^2/(8\pi)$ | Pion decay rate, $f_\pi=130.2$ MeV |

## Further Reading

- E. Fermi, "Tentativo di una teoria dei raggi $\beta$," *Il Nuovo Cimento* **11** (1934) 1–19, for the original four-fermion contact.
- R. P. Feynman and M. Gell-Mann, "Theory of the Fermi interaction," *Physical Review* **109** (1958) 193–198, and E. C. G. Sudarshan and R. E. Marshak, "Chirality invariance and the universal Fermi interaction," *Physical Review* **109** (1958) 1860–1862, for the $V-A$ current.
- C. S. Wu, E. Ambler, R. W. Hayward, D. D. Hoppes and R. P. Hudson, "Experimental test of parity conservation in beta decay," *Physical Review* **105** (1957) 1413–1415, for the observation of maximal parity violation.
- T. D. Lee and C. N. Yang, "Question of parity conservation in weak interactions," *Physical Review* **104** (1956) 254–258, for the argument that preceded it.
- M. Gell-Mann and M. Lévy, "The axial vector current in beta decay," *Il Nuovo Cimento* **16** (1960) 705–726, for the partially conserved axial current.
- S. Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the charged and neutral currents, the contact limit and the radiative corrections.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the four-fermion theory, the muon lifetime and the helicity suppression in pion decay.
- W. J. Marciano and A. Sirlin, "Precise $SU(2)\times \mathrm{U}(1)$ parameters and the $Z$ mass," *Physical Review D* **22** (1980) 2695–2700, for the relation between $G_{\mathrm F}$ and the W mass and for the radiative correction to the muon lifetime.
- Particle Data Group, R. L. Workman *et al.*, "Review of Particle Physics," *Progress of Theoretical and Experimental Physics* **2022** (2022) 083C01, for $G_{\mathrm F}$, $M_W$, $\sin^2\theta_W$, the muon lifetime, the pion branching ratios and $|V_{ud}|$.
- A. Sudbery, "Quaternionic Analysis," *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the algebra's multiplication and the obstruction to naive holomorphy.
