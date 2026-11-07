# __The Weak Interaction in Biquaternionic Form__

## Introduction

The **weak interaction** is the interaction that changes flavour. A neutron becomes a proton by emitting an electron and an antineutrino, a muon becomes an electron, an antineutrino and a muon neutrino, and a strange quark becomes an up quark. The interaction is short-ranged, and below the W mass it is described by a **four-fermion contact**: four fermion fields at one point, with no propagator between them. Enrico Fermi wrote the first such contact in 1934 for beta decay, with a vector coupling. The modern form was fixed in 1958 by Feynman and Gell-Mann and, independently, by Marshak and Sudarshan: the current is $V-A$, the difference of a vector and an axial vector, and the difference is what makes the interaction **maximally parity-violating**, established experimentally by Wu and her collaborators in 1957 on polarized cobalt-60.

This article treats the process level, and not the bosons. The companion *The W and Z Bosons in Biquaternionic Form* settles what the framework reaches for the carriers — the Proca kinematics, the charges as eigenvalues of the adjoint action, the neutral mixing, the self-couplings — and states plainly that it stops at the chiral coupling. The present article starts there, asks what the framework has for the **current** itself and for the contact built from two of them, and answers in the three categories the corpus uses.

- **Established, and derived below.** On the Dirac module the vector vertex $\Gamma_\mu$ and the axial vertex $\Gamma_\mu\xi$ are each a single basis operator. Their combination $\Gamma_\mu(g_V-g_A\xi)$ is again a single basis operator, with a right multiplier that is the sum of the two, $g_Vi\vec e_x-g_A\vec e_y$ in the time component and $g_Vi\vec e_y+g_A\vec e_x$ in a spatial one, and the square of the whole operator is $(g_V^2-g_A^2)\Gamma_\mu^2$. It follows that the chiral vertex is **nilpotent exactly at $|g_A|=|g_V|$**, that is exactly for the two chiral mixtures $V-A$ and $V+A$, and invertible for every other pair of weights; and that at $g_A=+g_V$ and $g_A=-g_V$ the right multiplier is exactly $2\vec\Upsilon_1$ and $2\vec\Upsilon_2$, the two standard Peirce nilpotents of the algebra. The $V-A$ structure, which the Standard Model takes as input, is therefore one of the only two weight assignments that make the weak vertex a **null** element, the other being $V+A$, which differs from it only in the sign of the axial half; and the framework states the same identity that the Dirac matrices satisfy.
- **Transcribed, and recomputed here.** The contact coefficient, $G_{\mathrm F}/\sqrt2=g^2/(8M_W^2)$; the contact's accuracy at low momentum transfer; the muon lifetime, $2.1873$ microseconds at the tree level against the measured $2.1969811$; and the ratio of the two pion decay rates, $1.2833\times10^{-4}$ at the tree level against the measured $1.2300\times10^{-4}$, the difference being the radiative correction. These are standard results, and the framework neither improves nor spoils them.
- **Not supplied, and left visible as a gap.** The framework does not derive the coupling, does not select the left-handed half, has no generation structure and no mixing matrix, and its own gauge group, the $*$-unitary part of the centre, acts as a scalar and is therefore vector-like on the module, a chiral gauge group requiring a non-central action that *Chiral Fermions in the Biquaternion Framework* records as the gap. The algebra supplies the *shape* of the vertex and not the *strength* with which nature uses it.

The article is organised as follows. The next section transcribes the process, the contact and the rates. A section then writes the charged current as a basis operator, derives the multiplier table, and proves the square identity and the nilpotency criterion. A section turns the criterion on the neutral current and shows that the measured $Z$ coupling sits away from the null point, with the parity-violating asymmetry as the size of the departure. A section treats parity, the mass bilinear and what nilpotency means for a fermion line. A closing section separates what the framework supplies from what it imports, and names the one gauge construction that would close the gap. The summary, the notation table and the literature follow.

Throughout, the biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\sum_l\varepsilon_{jkl}\vec e_l$ on the three spatial units, and central $i$ with $i^2=-1$. A two-sided multiplication on the Dirac module $\mathbb{C}^4$ is a **basis operator**, $L_aR_b\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}} b$, and applying a basis operator twice gives $a^2\tilde{Ξ}_{\mathrm{sp}} b^2$. The frame basis operators and the chirality basis operator are those of the companions,

$$
\Gamma_t:=iR_{\mathrm{axf},\vec e_x},\qquad \Gamma_k:=iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y},\qquad \xi:=-iR_{\mathrm{axf},\vec e_z}=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z},
$$

the label $\mathrm{axf}$ naming the axis-free frame of the regular representation as in *Matrix Representations Conventions*. **The coordinate frame is $\mathbb{B}_{\Phi}$ throughout**, the material frame with $x_0=r'_{t}$, and no formula below crosses into the $\mathbb{B}$ frame. In that frame $\{\Gamma_\mu,\Gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ and $\xi^2=I_4$, with $\varepsilon=(1,-1,-1,-1)$ and $\xi$ anticommuting with every $\Gamma_\mu$. The projectors are $P_L=\tfrac12(I_4-\xi)$ and $P_R=\tfrac12(I_4+\xi)$, and the Dirac adjoint is $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\vec e_x}$. Where the Dirac matrices are named they are these same basis operators in this same frame, $\gamma_\mu=\Gamma_\mu$ and $\gamma_5=\xi$. Every identity stated below was checked by exact matrix multiplication on the Dirac module, on eight pairs $(g_V,g_A)$ and all four values of $\mu$, to a maximum deviation of $2.3\times10^{-16}$.

## The Process, the Contact and the Rates

### The charged current and its contact limit

The weak charged current carries one unit of charge and one unit of the weak isospin ladder. In the standard notation, read in the frame declared above, with $u$ the upper and $d$ the lower member of a doublet,

$$
J^{+}_\mu=\tilde{Ξ}_{\mathrm{sp},\mathrm u}^{\dagger}iR_{\vec e_x}\,\gamma_\mu(1-\gamma_5)\tilde{Ξ}_{\mathrm{sp},\mathrm d},
$$

and the interaction Lagrangian is $\mathcal{L}_{\mathrm{cc}}=-\frac{g}{2\sqrt2}\sum_\mu\varepsilon_\mu\big(W^{+}_\mu J^{+}_\mu+W^{-}_\mu J^{-}_\mu\big)$, with $J^{-}_\mu=(J^{+}_\mu)^{\dagger}$. Eliminating the W at momenta small against its mass replaces the propagator by $\varepsilon_\mu\delta_{\mu\nu}/M_W^2$ and leaves a contact,

$$
\mathcal{L}_{\mathrm{eff}}=-\frac{4G_{\mathrm F}}{\sqrt2}\sum_\mu\varepsilon_\mu J^{+}_\mu J^{-}_\mu,
\qquad
\frac{G_{\mathrm F}}{\sqrt2}=\frac{g^2}{8M_W^2},
$$

which is Fermi's four-fermion form with the coefficient fixed by the W mass. The framework's companion article on Møller scattering uses the same elimination on the neutral current, and the parity-violating asymmetry computed there is the neutral counterpart of what follows. With the standard inputs $G_{\mathrm F}=1.1663787\times10^{-5}$ GeV$^{-2}$ and $M_W=80.3692$ GeV, the relation was verified to give $g=0.65283$, the accepted value to four figures, and it inverts to $v=(\sqrt2\,G_{\mathrm F})^{-1/2}=246.22$ GeV.

### The contact is a very good approximation, and that is the point

The eliminated propagator was expanded at $q^2/M_W^2$. For a momentum transfer of $100$ MeV the ratio is $1.55\times10^{-6}$, so the contact is accurate to a part per million for nuclear beta decay, and the W never appears as a propagating degree of freedom. That fact fixes the shape of the question this article asks: whatever the framework does or does not supply for the W's mass, the process does not see it, so a framework that could supply the current exactly would be tested by the contact and not by the carrier. What the process exhibits directly is the **vertex**, and the vertex is what the algebra can be asked about.

### What the rates say

Two rates are worth recomputing, because between them they exhibit the two faces of the $V-A$ structure at the tree level: its normalization and its chirality flip. The muon lifetime follows from the contact with the electron mass neglected,

$$
\Gamma(\mu\to e\nu_e\bar\nu_\mu)=\frac{G_{\mathrm F}^2m_\mu^5}{192\pi^3},
\qquad
\tau_\mu=\frac{1}{\Gamma(\mu\to e\nu_e\bar\nu_\mu)}=2.1873\ \mu\mathrm{s},
$$

against the measured $2.1969811\ \mu\mathrm{s}$, the residual $0.44\%$ being the radiative and electron-mass corrections. The charged pion decays to a lepton and a neutrino through the same contact, and the rate is

$$
\Gamma(\pi\to l\nu_l)=\frac{G_{\mathrm F}^2f_\pi^2m_\pi m_l^2}{8\pi}\Big(1-\frac{m_l^2}{m_\pi^2}\Big)^{2},
$$

with $f_\pi=130.2$ MeV. The factor $m_l^2$ is the whole content of the chiral structure: the pion is spinless and the antineutrino is right-handed, so angular momentum forces the charged lepton into the wrong helicity, which the $V-A$ vertex meets with one power of the mass for the one chirality flip, hence a factor $m_l^2$ in the rate. The measurable consequence is the ratio of the two rates,

$$
\frac{\Gamma(\pi\to e\nu_e)}{\Gamma(\pi\to\mu\nu_\mu)}=\frac{m_e^2}{m_\mu^2}\frac{\big(1-m_e^2/m_\pi^2\big)^2}{\big(1-m_\mu^2/m_\pi^2\big)^2}=1.2833\times10^{-4},
$$

against the measured $1.2300\times10^{-4}$, which is $0.958$ times the tree-level value; the $4.3\%$ is the $\mathcal{O}(\alpha)$ radiative correction, which the tree-level formula does not contain. The agreement to four percent, in a number that spans five orders of magnitude and that is zero for a pure $V$, is the strongest single statement about the vertex that the process makes.

## The Charged Current as an Operator
### The vector and the axial vertex

The vector vertex is one basis operator, $\Gamma_\mu$, and it is the corpus's frame basis operator: $\Gamma_t=iR_{\vec e_x}$ and $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$. The axial vertex is the same basis operator followed by the chirality basis operator, and the product of two basis operators is a basis operator, so $\Gamma_\mu\xi$ is a basis operator as well; explicitly $\Gamma_t\xi=R_{\vec e_y}$ and $\Gamma_k\xi=-L_{\vec e_k}R_{\vec e_x}$. Neither multiplier is nilpotent, and the square of neither vanishes: $\Gamma_\mu^2=\varepsilon_\mu I_4$ and $(\Gamma_\mu\xi)^2=-\varepsilon_\mu I_4$, both verified exactly.

The object the weak interaction uses is neither of these but their difference. It is a basis operator as well, this time by linearity of the right factor rather than by the product rule,

$$
\Gamma_\mu(g_V-g_A\xi)=g_V\Gamma_\mu-g_A\,\Gamma_\mu\xi ,
$$

whose two terms share the same left multiplier and differ only in the right one, so that the sum is the single basis operator with the summed right multiplier, $g_Vi\vec e_x-g_A\vec e_y$ in the time component and $g_Vi\vec e_y+g_A\vec e_x$ in a spatial one.

### The multiplier table

Normalising the right multiplier to the Peirce element $\vec\Upsilon_1=\tfrac12(i\vec e_x-\vec e_y)$ for the left-handed projector and to $\vec\Upsilon_2=\tfrac12(i\vec e_x+\vec e_y)$ for the right-handed one, the left multipliers come out as the informational-sector frame, with one sign flip between the two chiralities.

| Vertex | Basis operator form | Left multiplier | Right multiplier |
|---|---|---|---|
| $\Gamma_tP_L$ | $L_{e_t}R_{\vec\Upsilon_1}$ | $e_t$ | $\vec\Upsilon_1$ |
| $\Gamma_xP_L$ | $L_{-i\vec e_x}R_{\vec\Upsilon_1}$ | $-i\vec e_x$ | $\vec\Upsilon_1$ |
| $\Gamma_yP_L$ | $L_{-i\vec e_y}R_{\vec\Upsilon_1}$ | $-i\vec e_y$ | $\vec\Upsilon_1$ |
| $\Gamma_zP_L$ | $L_{-i\vec e_z}R_{\vec\Upsilon_1}$ | $-i\vec e_z$ | $\vec\Upsilon_1$ |
| $\Gamma_tP_R$ | $L_{e_t}R_{\vec\Upsilon_2}$ | $e_t$ | $\vec\Upsilon_2$ |
| $\Gamma_xP_R$ | $L_{+i\vec e_x}R_{\vec\Upsilon_2}$ | $+i\vec e_x$ | $\vec\Upsilon_2$ |
| $\Gamma_yP_R$ | $L_{+i\vec e_y}R_{\vec\Upsilon_2}$ | $+i\vec e_y$ | $\vec\Upsilon_2$ |
| $\Gamma_zP_R$ | $L_{+i\vec e_z}R_{\vec\Upsilon_2}$ | $+i\vec e_z$ | $\vec\Upsilon_2$ |

Every left multiplier in the table lies in the informational sector $\mathbb{B}_{\Psi}=\mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, and every right multiplier is one of the two Peirce nilpotents, which lie on the null cone and in neither sector. The normalisation is not unique: $(a,b)$ and $(\lambda a,b/\lambda)$ give the same basis operator, so the entries are fixed by the stated choice of right multiplier, and a different choice rescales the left column without changing any statement about the right one. What the table says is that the chiral weak vertex is a basis operator of **mixed type** — an element of the informational sector on the left and a null element on the right — and that the two chiralities differ only in the sign of the left multiplier.

### The square identity

The square of a basis operator is the basis operator of the squares, $L_aR_b\,L_aR_b=L_{a^2}R_{b^2}$, because applying $\tilde{Ξ}_{\mathrm{sp}}\mapsto a\tilde{Ξ}_{\mathrm{sp}} b$ twice gives $a^2\tilde{Ξ}_{\mathrm{sp}} b^2$. For the chiral vertex the right multiplier is $\vec\Upsilon_1$ or $\vec\Upsilon_2$, and both square to zero, so the square vanishes. For general weights the right multiplier is $b=g_Vi\vec e_x-g_A\vec e_y$ in the time component, whose square is

$$
(g_Vi\vec e_x-g_A\vec e_y)^2=-g_V^2\vec e_x^2+g_A^2\vec e_y^2=g_V^2-g_A^2 ,
$$

the cross term vanishing because distinct quaternion units anticommute. The same computation in a spatial component, with right multiplier $g_Vi\vec e_y+g_A\vec e_x$, gives the same value $g_V^2-g_A^2$, the difference between the two cases being carried by $\Gamma_k^2=-I_4$. Hence

$$
\big(\Gamma_\mu(g_V-g_A\xi)\big)^2=\varepsilon_\mu\,(g_V^2-g_A^2)\,I_4 ,
$$

an identity checked to $2.3\times10^{-16}$ for $(g_V,g_A)\in\{(1,0),(1,\tfrac12),(1,1),(1,-1),(1,2),(1,i),(1,0.3+0.4i),(1,2-i)\}$ and $\mu=t,x,y,z$. Three things follow, and they are the substance of this article.

**The chiral vertex is nilpotent, and only the chiral one is.** The square vanishes if and only if $g_A^2=g_V^2$, that is for $V-A$ and $V+A$ and for no other ratio of the weights. For $g_A^2\ne g_V^2$ the operator is not merely non-null but invertible, with determinant $(g_V^2-g_A^2)^2$ in each component; the determinant was computed as $0.5625$ at $(g_V,g_A)=(1,\tfrac12)$ and $9$ at $(1,2)$, and vanishes at $g_A=\pm g_V$. The weak vertex therefore sits at one of the two ratios of the weights at which the algebra's own product degenerates, and the Standard Model's choice of $V-A$ is that value.

**Two adjacent vertices annihilate, and the index does not matter.** The square identity uses one index twice, but the vanishing is stronger than the square shows. Since $\xi$ anticommutes with every frame basis operator, $P_L\Gamma_\nu=\Gamma_\nu P_R$, and two adjacent weak vertices collapse for **every** pair of Lorentz indices,

$$
\Gamma_\mu P_L\,\Gamma_\nu P_L=\Gamma_\mu\Gamma_\nu P_RP_L=0 ,
$$

verified for all sixteen pairs $(\mu,\nu)$ and likewise for $P_R$. The index plays no part; what does the work is the chirality flip, one projector at each vertex. The prohibition is therefore about **adjacency**. Anything between the two vertices removes it, and a single propagator is enough, because the momentum basis operator $P=p_0\Gamma_t-\sum_kp_k\Gamma_k$ anticommutes with $\xi$ and turns the projector back: with $p=(1,0.3,-0.2,0.1)$ the chain was $1.1$ in every component. A box diagram is unaffected for that reason, its two vertices standing at the two ends of one propagator rather than beside each other. This is the helicity selection rule read on one line rather than on one decay, and it is the same flip that the pion ratio measures.

**The identity is Dirac's, and the framework says why.** A reader who knows the Dirac algebra will recognise $(g_V^2-g_A^2)\Gamma_\mu^2$ as the statement that the axial matrix anticommutes with the vector one, $\Gamma_\mu\xi=-\xi\Gamma_\mu$, so that $\Gamma_\mu(g_V-g_A\xi)=(g_V+g_A\xi)\Gamma_\mu$ and the axial half reverses its sign as the vector passes through it; the square then returns $g_V^2-g_A^2$ times $\Gamma_\mu^2$. The framework's version of the reason is arithmetic on the units. The right multipliers of the vector and the axial vertex are $i\vec e_x$ and $\vec e_y$, two orthogonal quaternion units, so the cross terms of the square cancel whatever the weight. The squares themselves are $+1$ and $-1$: the first is positive because the central $i$ contributes $i^2=-1$ against $\vec e_x^2=-1$, and the second is negative because $\vec e_y^2=-1$ stands alone. The two contributions therefore carry opposite signs by construction, and they cancel exactly when the weights are equal in magnitude.

### The Peirce pair closes

The two nilpotents are not independent. Their sum and their product were verified,

$$
\vec\Upsilon_1+\vec\Upsilon_2=i\vec e_x,\qquad
\vec\Upsilon_1\vec\Upsilon_2=\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_+^2=\tilde\Pi_+ ,
$$

with $\tilde\Pi_+$ Hermitian. The product of the two right multipliers, in the normalisation of the table, is therefore an idempotent of the algebra, and the idempotent is the pure state that the companion article on the informational sector uses as the first basis vector of the spinor module. The computation is the matrix-unit relation already recorded in *The Newman–Penrose Formalism in Biquaternionic Form*, reached here from the vertex rather than from the spinor basis. It is stated as an algebraic fact and given no dynamical reading.

## The Neutral Current Is Not Null

The neutral current has the same shape, $J_{Z\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\vec e_x}\,\Gamma_\mu(g_V-g_A\xi)\tilde{Ξ}_{\mathrm{sp}}$, with the weights the theory supplies, $g_V=T_3-2ϙ\sin^2\theta_W$ and $g_A=T_3$, in place of the equal $g_V=g_A=1$ of the charged current. The criterion above applies directly: the vertex is null if and only if $|g_A/g_V|=1$, which is

$$
\Big|\frac{g_A}{g_V}\Big|=\Big|1-4\sin^2\theta_W\Big|^{-1},
$$

and at $\sin^2\theta_W=0.23122$ the bracket is $Q_W^e=0.07512$, so the ratio is $1/|Q_W^e|=13.3$ and the vertex is far from null — invertible, with the determinant $(g_V^2-g_A^2)^2$ evaluated at that ratio. Nullness would need $4\sin^2\theta_W=0$ or $4\sin^2\theta_W=2$, that is $\sin^2\theta_W=0$, a pure vector coupling, or $\sin^2\theta_W=\tfrac12$, a pure axial one.

This is not a defect of the framework but a statement about the theory, and it has a measured face. The quantity $1-4\sin^2\theta_W$ is the weak charge $Q_W$ of the electron that the Møller article's parity-violating asymmetry is proportional to; the asymmetry is small because the vector coupling is small, and it vanishes at $\sin^2\theta_W=\tfrac14$, where the vertex is purely axial. That zero is not the null point, and the distinction is worth keeping: the asymmetry vanishes when the two chiral weights stand in the ratio $0:1$, and the vertex is null when they stand in the ratio $1:1$. The criterion and the measurement are two different statements about the same pair of weights; at the physical angle the charged vertex sits exactly on the null point and the neutral one misses it by a factor of $13.3$.

The observation is worth recording because it sharpens what "chiral" means in this algebra. A vertex is null when its two chiral halves carry equal weight. The charged current is null, the neutral current is not, and the difference between them is the mixing angle, which the framework does not derive — it is imported, as the companion article states. Neither is a prediction: the algebra supplies the criterion, and the mixing angle is an input.

## Parity, the Mass, and the Fermion Line

### Parity reverses the axial weight

The framework's parity operation reverses the three spatial directions and fixes time; on the Dirac module it is the internal factor $\eta_P=iR_{\vec e_x}$, which satisfies $\eta_PP_R=P_L\eta_P$ and so exchanges the two projectors, as *The Reflection and the Rotation in Biquaternionic Form* establishes. In the algebra the exchange is arithmetic on one unit: conjugation by $R_{\vec e_x}$ sends $\vec e_x\vec\Upsilon_1\vec e_x=-\vec\Upsilon_2$ and $\vec e_x\vec\Upsilon_2\vec e_x=-\vec\Upsilon_1$, hence $\eta_P\xi\eta_P=-\xi$, and each basis operator $L_aR_{\vec\Upsilon_1}$ becomes $L_aR_{\vec\Upsilon_2}$ with the left multiplier untouched. On a vertex of weights $(g_V,g_A)$ the effect is

$$
\eta_P\,\Gamma_t(g_V-g_A\xi)\,\eta_P=\Gamma_t(g_V+g_A\xi),
\qquad
\eta_P\,\Gamma_k(g_V-g_A\xi)\,\eta_P=-\Gamma_k(g_V+g_A\xi),
$$

both verified exactly. Parity **reverses the axial weight**, $g_A\mapsto-g_A$, and the sign on the spatial components is the vector's own sign flip, $\Gamma_t\mapsto+\Gamma_t$ and $\Gamma_k\mapsto-\Gamma_k$. It does not annihilate a chiral vertex; it exchanges $V-A$ with $V+A$.

A theory is parity invariant when its vertex is its own image, which requires $g_A=0$: the pure vector, which is Fermi's original coupling. Any $g_A\ne0$ is parity-odd, and **maximal** violation is the weight $|g_A|=|g_V|$, where the two halves enter with equal magnitude and opposite sign, so the parity-odd admixture is as large as the form admits. That weight is also the null one, and the coincidence is one fact rather than two: the squares of the two contributions, $+1$ and $-1$, are what make the magnitudes equal and what make them cancel.

### The mass bilinear is chirality-odd

The Dirac mass term pairs the two chiralities, so it is odd under $\xi$ and vanishes on a field of definite chirality; the companion article derives this and the selection rule that follows, the two chiral charges equal for a gauge-invariant bare mass. This article adds only where the two facts meet. Both are properties of the one element $\xi$. The projectors are idempotent, $P_L^2=P_L$, and the adjoint passes through them to the other side, $P_LR_{\vec e_x}=R_{\vec e_x}P_R$, verified, so the bilinear of two left-handed fields is

$$
\tilde{Ξ}_{\mathrm{sp},L}^{\dagger}iR_{\vec e_x}\tilde{Ξ}_{\mathrm{sp},L}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}P_L\,iR_{\vec e_x}P_L\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\vec e_x}P_RP_L\tilde{Ξ}_{\mathrm{sp}}=0 ,
$$

a mass term with nothing to pair. The same basis operator supplies the vertex its nilpotent multiplier. A field of definite chirality is therefore massless and its weak vertex is null, and both statements are read off one basis operator and its eigenvalue on the state the idempotent prepares.

### What nilpotency forbids on a line

The rule above is worth separating from two claims it does not make. It does not forbid a box diagram, whose vertices are not adjacent. And it does not forbid the weak interaction to act twice on one line, since a propagator or a mass between the two vertices removes the prohibition. It says exactly what the projector algebra says: two adjacent vertices on one line vanish.

## What the Framework Supplies and What It Imports

| Item | Status |
|---|---|
| The vector vertex as a basis operator | **Supplied.** $\Gamma_\mu$, the corpus's frame basis operator |
| The axial vertex as a basis operator | **Supplied.** $\Gamma_\mu\xi$, a basis operator with a non-nilpotent multiplier |
| The chiral vertex as a single basis operator | **Supplied.** The multiplier table, verified exactly |
| Nilpotency of the chiral vertex | **Supplied.** $(g_V^2-g_A^2)\Gamma_\mu^2$, zero at $|g_A|=|g_V|$ only |
| The Peirce pair as the right multipliers | **Supplied.** $\vec\Upsilon_1$ for $L$, $\vec\Upsilon_2$ for $R$ |
| Maximal parity violation | **Supplied.** The null condition is $|g_A|=|g_V|$ |
| The contact coefficient $G_{\mathrm F}/\sqrt2=g^2/(8M_W^2)$ | **Transcribed.** Standard input |
| The muon lifetime and the pion ratio | **Transcribed and recomputed.** $2.1873$ $\mu$s and $1.2833\times10^{-4}$ |
| The coupling $g$ and the W mass | **Imported.** The framework has no scale |
| The choice that only $L$ couples | **Not supplied.** An input, not a consequence |
| A chiral gauge action | **Gap.** The framework's own group is central and therefore vector-like; a non-central action is not built |
| Generations, mixing, CP | **Outside.** No mechanism in the algebra |
| $V_{ud}$ and the unitarity of the mixing matrix | **Outside.** Imported |

The rows from the coupling downward are the ones that decide the article's verdict. The framework's account of the weak interaction is an account of the **shape of the vertex**, and it is exact: the chiral vertex is one basis operator, its multipliers are named, and its nilpotency is a theorem. What it does not have is any reason for nature to have used that shape with a specific strength, or to have used it on the left half only. The shape is algebraic; the strength and the asymmetry are inputs.

One construction would change that, and the article names it without claiming it. The obstruction that *Chiral Fermions in the Biquaternion Framework* proves is that the framework's own gauge group is the $*$-unitary part of the centre, and a central element acts as a scalar, so the canonically available abelian sector is vector-like; a chiral group needs a **non-central** action. The companion article on the $SO(4)$ route records a proposal of exactly that shape, the separate gauging of the two factors of the basis operator $L_aR_b$, and is careful about its status there: the ceiling's obstruction is stated for left multiplication, so it does not apply to $L_aR_b$ as stated, but the anomaly conditions, the mass selection rule and the charge operator would all have to be redone, and none of that is done. This article adds only a word about what the table above does and does not supply. Its right multipliers are not invertible, $\vec\Upsilon_a^2=0$, and a nilpotent cannot be the value of a group element near the identity, so the table describes a vertex and not a symmetry. What it does show is the shape such a construction would need: a non-central factor on the right and an informational one on the left.

## Summary

The weak interaction at the process level is a four-fermion contact with a $V-A$ current, and the contact is accurate to a part per million for nuclear beta decay, so the process tests the vertex and not the carrier. The framework supplies the vertex exactly. The vector vertex $\Gamma_\mu$ is the corpus's frame basis operator and the axial vertex $\Gamma_\mu\xi$ is a basis operator too, and their combination $\Gamma_\mu(g_V-g_A\xi)$ is a single basis operator whose right multiplier is $g_Vi\vec e_x-g_A\vec e_y$ in the time component. Squaring gives

$$
\big(\Gamma_\mu(g_V-g_A\xi)\big)^2=\varepsilon_\mu(g_V^2-g_A^2)I_4 ,
$$

verified to $2.3\times10^{-16}$, so the chiral vertex is nilpotent if and only if $|g_A|=|g_V|$ and invertible otherwise. With the right multiplier normalised to the Peirce pair, the left multipliers are the informational-sector frame, $e_t$ and $-i\vec e_k$ for $P_L$ against $e_t$ and $+i\vec e_k$ for $P_R$, and the two chiralities differ only by the sign of that multiplier. The $V-A$ structure, which the Standard Model takes as input, is therefore exactly the condition that the weak vertex be null, and the identity it satisfies is Dirac's, derived here from the nilpotency of the Peirce element.

The neutral current does not sit at the null point: its weight ratio is $(1-4\sin^2\theta_W)^{-1}=13.3$, and the smallness of the parity-violating asymmetry in Møller scattering is the measured face of that distance. Parity reverses the sign of the axial weight, $g_A\mapsto-g_A$, so it exchanges $V-A$ with $V+A$ and leaves only the pure vector self-conjugate; maximal violation is $|g_A|=|g_V|$, where the two halves enter with equal magnitude. The mass bilinear is chirality-odd, and the identity $P_LR_{\vec e_x}=R_{\vec e_x}P_R$ is what makes it vanish on a field of definite chirality. Two adjacent weak vertices on one line annihilate for every pair of indices, and a propagator between them revives the product; that is the chirality flip, and the pion ratio measures the same flip on one decay.

What the framework does not supply is the coupling, the scale, the selection of the left half, the generations and the mixing. The rates are transcribed: $\tau_\mu=2.1873$ $\mu$s at the tree level against $2.1969811$ measured, and $\Gamma(\pi\to e\nu_e)/\Gamma(\pi\to\mu\nu_\mu)=1.2833\times10^{-4}$ against $1.2300\times10^{-4}$ measured. The one construction that would close the gap is the separate gauging of the basis operators, which the companion article on the $SO(4)$ route records as a proposal and not as a result. The table above does not supply it: a nilpotent multiplier is not a group element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\sum_l\varepsilon_{jkl}\vec e_l$ on the spatial units |
| $i$ | Central imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material and informational sectors |
| $L_aR_b$ | Basis operator, $L_aR_b\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}} b$; applying it twice gives $a^2\tilde{Ξ}_{\mathrm{sp}} b^2$ |
| $\Gamma_t=iR_{\vec e_x}$, $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$ | Frame basis operators, $\{\Gamma_\mu,\Gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ |
| $\xi=-iR_{\vec e_z}$ | Chirality basis operator, $\xi^2=I_4$, the image of $\gamma_5$ |
| $P_L=\tfrac12(I_4-\xi)$, $P_R=\tfrac12(I_4+\xi)$ | Chiral projectors, $P_LP_R=0$ |
| $\vec\Upsilon_1=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_2=\tfrac12(i\vec e_x+\vec e_y)$ | Peirce nilpotents, $\vec\Upsilon_a^2=0$; they are the canonical frame's $\vec\Upsilon_-$ and $\vec\Upsilon_+$ |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)=\vec\Upsilon_1\vec\Upsilon_2$ | Hermitian idempotent of the algebra |
| $\Gamma_\mu(g_V-g_A\xi)$ | Chiral vertex of weights $g_V,g_A$; $g_A=+g_V$ is $V-A$ |
| $\big(\Gamma_\mu(g_V-g_A\xi)\big)^2=\varepsilon_\mu(g_V^2-g_A^2)I_4$ | Square identity; nilpotent iff $\lvert g_A\rvert=\lvert g_V\rvert$ |
| $J^{+}_\mu=\tilde{Ξ}_{\mathrm{sp},\mathrm u}^{\dagger}iR_{\vec e_x}\Gamma_\mu(1-\xi)\tilde{Ξ}_{\mathrm{sp},\mathrm d}$ | Charged current, $V-A$, the case $g_A=+g_V$ |
| $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\vec e_x}$ | Dirac adjoint |
| $\mathcal{L}_{\mathrm{eff}}=-\frac{4G_{\mathrm F}}{\sqrt2}\sum_\mu\varepsilon_\mu J^{+}_\mu J^{-}_\mu$ | Four-fermion contact |
| $G_{\mathrm F}/\sqrt2=g^2/(8M_W^2)$ | Contact coefficient |
| $G_{\mathrm F}=1.1663787\times10^{-5}$ GeV$^{-2}$ | Fermi constant |
| $v=(\sqrt2\,G_{\mathrm F})^{-1/2}=246.22$ GeV | Electroweak scale |
| $g_V=T_3-2ϙ\sin^2\theta_W$, $g_A=T_3$ | Neutral current weights; the charged current has $g_V=g_A=1$ |
| $\eta_P=iR_{\vec e_x}$ | Internal parity factor, $\eta_P^2=I_4$, $\eta_PP_R=P_L\eta_P$, $\eta_P\xi\eta_P=-\xi$ |
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
