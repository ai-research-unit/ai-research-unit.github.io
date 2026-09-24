# __The CKM Matrix and CP Violation in Biquaternionic Form__

## Introduction

The **Cabibbo–Kobayashi–Maskawa (CKM) matrix** is the unitary matrix that relates the quark mass eigenstates to the weak-interaction eigenstates. It is the origin of quark mixing and, through its single complex phase, of CP violation in the quark sector. In the Standard Model it is a $3\times3$ unitary matrix with four physical parameters — three angles and one phase — and its measured entries and phase are among the most precisely known quantities in particle physics.

In the biquaternion framework the CKM matrix is a **flavour-factor object**. The framework carries a generation index as a multiplicity factor $\mathbb{C}^{N_g}$, on which the algebra acts trivially (the companion article on the number of generations establishes this), and the CKM matrix is a unitary operator on that factor,

$$
V \;\in\; U(N_g),\qquad
\text{acting as } I_\Delta\otimes V \text{ on } \Delta\otimes\mathbb{C}^{N_g}.
$$

The framework's contribution is therefore the tensor structure of the flavour sector, the counting of the parameters, and one structural fact that the counting alone does not give: the CP-violating phase cannot live in the algebra's center, because the center acts on every generation in the same way, and it must live in the flavour factor. The article states these and is explicit that the framework does not determine the entries.

- **Established.** The CKM matrix as a flavour-factor operator $I_\Delta\otimes V$; the parameter count $\tfrac12N_g(N_g-1)$ angles and $\tfrac12(N_g-1)(N_g-2)$ phases; the requirement $N_g\ge3$ for a CP-violating phase; the non-centrality of the phase from the structure of the multiplied algebra; the Jarlskog invariant as a flavour-factor determinant; and the identical structure of the lepton sector's mixing matrix.
- **Standard, transcribed.** The quark-mass diagonalisation that produces $V$, the Wolfenstein parametrisation, the unitarity triangle, the measured parameters, the Jarlskog invariant and its value, and the standard CP-violating observables. The article recomputes the unitarity and the invariant.
- **Gap, left visible.** The framework does not produce the CKM angles, the CP phase, or the mass matrices that generate them. It has no flavour dynamics and no principle selecting the mixing pattern; the values are empirical.

The article is organised as follows. A section defines the CKM matrix and places it on the flavour factor. A section gives the parameter count and the CP phase. A section explains why the phase is not central. A section gives the mass-matrix origin of the mixing. A section treats the Jarlskog invariant and the condition for CP violation. A section collects the Wolfenstein parametrisation, the unitarity triangle, and the measured values. A closing section separates what is supplied, transcribed, and missing.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$; $\mathbb{B}\cong M_2(\mathbb{C})$. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The Dirac module is $\Delta=S\oplus\bar{S}$, $\dim_{\mathbb{C}}\Delta=4$, with $P_L,P_R$ the chiral projectors. The generation space is $\mathcal{F}=\mathbb{C}^{N_g}$ and the $N_g$-generation fermion space is $\Delta\otimes\mathcal{F}$; the flavour operators are $I_\Delta\otimes X$ with $X\in M_{N_g}(\mathbb{C})$. The quark mass matrices are $M_u,M_d\in M_{N_g}(\mathbb{C})\otimes I_\Delta$ and are diagonalised by unitary rotations on $\mathcal{F}$. The **CKM matrix** is $V=U_u^\dagger U_d$; the parametrisation and the numerical values are the Particle Data Group's, with $\lambda=0.22500$, $A=0.826$, $\bar\rho=0.159$, $\bar\eta=0.348$ and $\delta$ the CP-violating phase. Natural units $\hbar=c=1$ are used.

The framework results used here are those of the companion articles:

- Companion article *The Neutrino and Majorana Fermions in Biquaternionic Form*, for the lepton mixing that parallels the quark mixing.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral module and the mass selection rule.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the module and the flavour factor.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the free field, its mass terms and the bilinears.

## The CKM Matrix as a Flavour-Factor Operator

**The mixing.** Quarks are produced and interact in weak eigenstates and propagate in mass eigenstates. Writing the charged-current interaction in the mass basis introduces the mixing matrix,

$$
\mathcal{L}_{W} \supset \frac{g}{\sqrt2}\,W^+_\mu\,
\bar{u}_{iL}\gamma^\mu V_{ij}\,d_{jL} + \text{h.c.},
\qquad V = U_u^\dagger U_d ,
$$

where $U_u$ and $U_d$ diagonalise the up- and down-type mass matrices. In the framework the mass matrices are flavour operators, $M_u=I_\Delta\otimes M_u^{\mathcal{F}}$ and $M_d=I_\Delta\otimes M_d^{\mathcal{F}}$, with the module factor common and the flavour factor carrying the generation dependence; the diagonalising matrices are unitary operators on $\mathcal{F}$, and $V$ is their relative rotation. The whole construction lives on $\mathcal{F}$.

**The tensor form.** The interaction vertex is therefore

$$
I_\Delta\otimes\big(\gamma^\mu P_L\,V\big)
$$

on $\Delta\otimes\mathcal{F}$, i.e. the framework's Lorentz-and-chirality structure on the module factor times the mixing operator on the flavour factor. The framework supplies the first factor exactly — the $\gamma^\mu P_L$ vertex of the charged current is the module's structure — and the second factor is an arbitrary unitary operator: gauge invariance requires only $V\in U(N_g)$, not any particular $V$. The requirement of unitarity is the framework's, because the flavour rotation must preserve the norm on $\mathcal{F}$; the pattern of $V$ is not.

**Why the mixing is a basis change.** The CKM matrix is a change of basis in flavour space, not a new interaction. In the framework this is transparent: the gauge interactions are $I_\Delta\otimes I_{\mathcal{F}}$ times the module structure, i.e. they are **generation-universal**, and the mixing arises only because the mass matrices, which are $I_\Delta\otimes M^{\mathcal{F}}$, are not diagonal in the same flavour basis. The framework's gauge sector is flavour-blind; the flavour structure is created by the mass matrices. This is the algebraic form of the Glashow–Iliopoulos–Maiani mechanism: flavour-changing neutral currents are absent because the gauge vertex is $I_{\mathcal{F}}$ in flavour space.

**The lepton sector, in parallel.** The same structure applies to the leptons, with the mixing matrix of the lepton sector playing the role of $V$ and the neutrino mass matrices replacing the up-type quarks. The framework's tensor structure is identical; the values differ because the mass matrices differ, and the two mixings are independent inputs. The companion article on the neutrino treats the lepton mixing; this article treats the quark sector and the framework features common to both.

## The Parameter Count and the CP Phase

**Counting the parameters.** A general $N_g\times N_g$ unitary matrix has $N_g^2$ real parameters. Of these, $N_g$ are removed by rephasing the $N_g$ up-type quarks and $N_g$ by rephasing the $N_g$ down-type quarks, except that one overall phase is unobservable, leaving

$$
N_g^2-2N_g+1=(N_g-1)^2
$$

physical parameters. They divide into

$$
\frac{N_g(N_g-1)}{2}\ \text{rotation angles},
\qquad
\frac{(N_g-1)(N_g-2)}{2}\ \text{CP-violating phases},
$$

a decomposition that follows by counting the antisymmetric and orthogonal generators. For $N_g=1$ there is nothing; for $N_g=2$ there is one angle and **no phase**; for $N_g=3$ there are three angles and **one phase**. The existence of a CP-violating phase in the quark sector therefore requires at least three generations, which is the content of the Kobayashi–Maskawa observation, and it was the first theoretical argument that the number of generations could not be fewer than three.

**The phase and CP violation.** The single phase of the three-generation CKM matrix is the source of CP violation in the quark sector. It appears in the charged-current interactions through the complex entries of $V$ and produces observable CP-violating asymmetries in meson decays and mixing. Its reality or otherwise is rephasing-invariant: although the individual phases of the $V_{ij}$ can be changed by redefining the quark fields, the **rephasing-invariant combinations** — of which the Jarlskog invariant is the simplest — cannot, and it is those that are observable.

**Where the framework stands on the count.** The count $(N_g-1)^2$ is a property of the unitary group of the flavour factor, $U(N_g)$, and the framework supplies that group as the symmetry group of the multiplicity factor of the companion article. The framework therefore supplies the **arena** of the counting: the parameters are the coordinates of $U(N_g)$, the angles and phases are its directions, and the CP phase is one of them. It does not supply a principle that fixes which point of $U(N_g)$ the world occupies; that point is the measured CKM matrix.

## Why the CP Phase Is Not Central

**The center acts on all generations alike.** The companion article on the number of generations establishes that the algebra acting on $\Delta\otimes\mathbb{C}^{N_g}$ is $\mathbb{B}\otimes M_{N_g}(\mathbb{C})\cong M_{2N_g}(\mathbb{C})$ and that its center is $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}\cong\mathbb{C}$: a **single** central phase, acting on every generation with the same phase. A phase that distinguishes one generation from another — which is what a flavour-mixing phase does — cannot sit in the center. It must sit in the non-central part $I_\Delta\otimes M_{N_g}(\mathbb{C})$, i.e. in the flavour factor.

**The consequence for the CKM phase.** The CKM phase is therefore a **flavour-factor** phase: it is an entry of the unitary matrix on $\mathcal{F}$, and its CP-odd character is a property of that matrix, not of the algebra's central structure. This is a structural statement of the framework and one of its few definite contributions to the flavour sector: the algebra's center is generation-blind, so the framework's own central phases — the vector phase and the volume element — are CP-even in the flavour sense, and the observed CP violation must be carried by the flavour factor. The companion article on the electric dipole moment draws the consequence: the CP-odd phase that the EDM would measure is also a flavour-factor object, and the framework's algebra supplies no phase of its own.

**A contrast with the Dirac phase.** The framework's Dirac mass has a central phase symmetry, which is why the phase of the mass can be rotated away in the one-generation case: the vector phase acts on the single generation and can remove its phase. With $N_g$ generations the flavor-factor rotations give $N_g$ independent rephasings per chirality, and the relative phase between the up and down sectors cannot be removed when $N_g\ge3$. The framework's statement is the algebraic version of the standard counting: the unremovable CP phase is the one that the flavour-factor rephasings cannot absorb, and it exists precisely because the multiplicity factor is non-trivial.

**The reality of the phase's location.** The framework thus makes a definite negative prediction about where CP violation can come from: not from its algebra, its center, or its real structure, all of which are generation-blind or generation-diagonal, but from the flavour factor. Any CP violation in the quark sector is a statement about the matrix on $\mathbb{C}^{N_g}$, and the framework hosts it without producing it.

## The Mass Matrices and the Origin of the Mixing

**The diagonalisation.** The mixing matrix arises from the mismatch between the up- and down-type mass matrices. In the framework,

$$
M_u^{\mathcal{F}} = U_u\,D_u\,U_u^\dagger,\qquad
M_d^{\mathcal{F}} = U_d\,D_d\,U_d^\dagger,\qquad
V = U_u^\dagger U_d ,
$$

with $D_u,D_d$ diagonal and positive. The mixing is a measure of how differently the two matrices are diagonalised, and it vanishes when $U_u=U_d$. The framework's module factor is common to both, which is why the two diagonalisations are on the same flavour space and why the relative rotation is meaningful. The mass matrices $M^{\mathcal{F}}$ are general complex $N_g\times N_g$ matrices, and the eigenvalues are the quark masses.

**The invariant content.** The mixing matrix and the mass eigenvalues contain the same information as the two mass matrices up to the rephasings. The framework's statement is that all of this information lives on $\mathcal{F}$, that the module factor contributes nothing to it, and that the gauge sector's flavour-universality is what makes the mixing observable in the charged current and not in the neutral current. This is the algebraic content of the GIM mechanism and it is exact in the framework.

**The absence of a dynamics.** The framework has no equation from which $M_u^{\mathcal{F}}$ or $M_d^{\mathcal{F}}$ follows. In a flavour model the matrices would be generated by a symmetry and its breaking, by a radiative mechanism, or by a higher-dimensional construction; the framework contains none of these, and its role is to state where the matrices sit and what they must respect. The companion article on the number of generations makes the analogous statement for the hierarchy of the eigenvalues; the present article makes it for the mixing.

## The Jarlskog Invariant and the Condition for CP Violation

**The rephasing invariant.** Because the individual phases of the CKM matrix are convention-dependent, CP violation is measured by rephasing-invariant combinations. The lowest-order one is the **Jarlskog invariant**,

$$
J = \mathrm{Im}\big(V_{ud}V_{cs}V_{us}^{*}V_{cd}^{*}\big)
= c_{12}\,c_{23}\,c_{13}^{2}\,s_{12}\,s_{23}\,s_{13}\,\sin\delta ,
$$

where the second form uses the standard three-angle parametrisation with the phase $\delta$, and $c_{ij}=\cos\theta_{ij}$, $s_{ij}=\sin\theta_{ij}$. The invariant is the imaginary part of a quartet of matrix elements and it vanishes if and only if the theory is CP-conserving (for three generations); it is the determinant

$$
J \propto \mathrm{Im}\,\det\big[M_uM_u^\dagger,\,M_dM_d^\dagger\big] ,
$$

the commutator of the two mass-matrix products, up to normalisation by the mass differences. **CP violation for three generations is exactly the noncommutativity of the two mass matrices.**

**The values, recomputed.** With the standard values, the invariant and the matrix were computed from the unitary parametrisation:

$$
J = 3.08\times10^{-5},
\qquad
V V^\dagger = I \text{ to } 1.1\times10^{-16},
$$

the unitarity residual being machine precision, and the magnitude of $J$ agreeing with the approximation $J\simeq A^2\lambda^6\bar\eta=3.08\times10^{-5}$ to the precision of the inputs. The matrix elements came out as $|V_{ud}|=0.9744$, $|V_{us}|=0.2250$, $|V_{ub}|=0.00370$, $|V_{cb}|=0.0418$, $|V_{td}|=0.00857$, $|V_{tb}|=0.9991$, in agreement with the measured values. The computation used the exact three-angle parametrisation, not the truncated Wolfenstein form; the truncated form is unitary only up to the order of the truncation, and the invariant $J$ requires the untruncated phase structure.

**Why the commutator is the invariant.** The commutator of the mass matrices is the algebraic expression of the fact that CP violation requires two non-commuting matrices with a complex phase. If $M_uM_u^\dagger$ and $M_dM_d^\dagger$ commuted, they could be diagonalised simultaneously and the mixing matrix would be a permutation of phases — no CP violation. The determinant is the minimal invariant antisymmetric in the two matrices, and its imaginary part is the Jarlskog invariant. In the framework the commutator is a flavour-factor operator, $I_\Delta\otimes[M_u^{\mathcal{F}}M_u^{\mathcal{F}\dagger},M_d^{\mathcal{F}}M_d^{\mathcal{F}\dagger}]$, and its nonvanishing is the statement that the two mass matrices are misaligned in a CP-violating way.

## The Wolfenstein Parametrisation, the Unitarity Triangle, and the Data

**The Wolfenstein parametrisation.** The empirical pattern of the CKM matrix — nearly diagonal, with a small mixing — is captured by the expansion in $\lambda=\sin\theta_C\simeq0.225$, the Cabibbo angle:

$$
V = \begin{pmatrix}
1-\tfrac12\lambda^2 & \lambda & A\lambda^3(\bar\rho-i\bar\eta)\\
-\lambda & 1-\tfrac12\lambda^2 & A\lambda^2\\
A\lambda^3(1-\bar\rho-i\bar\eta) & -A\lambda^2 & 1
\end{pmatrix} + O(\lambda^4),
$$

with $A\simeq0.826$ and the CP-violating parameter the imaginary part $\bar\eta\simeq0.348$. The phase of the standard parametrisation is related to the Wolfenstein parameters by $\delta=\arctan(\bar\eta/\bar\rho)$, and the single CP-odd combination is the product $A^2\lambda^6\bar\eta$, which is the Jarlskog invariant at leading order. The hierarchy of the entries — the powers of $\lambda$ — is the observed structure; the framework supplies no reason for it.

**The unitarity triangle.** The orthogonality of two columns of $V$ defines a triangle in the complex plane with vertices at $(0,0)$, $(1,0)$ and $(\bar\rho,\bar\eta)$, the barred Wolfenstein parameters, which are the ones the data are quoted in and are related to the unbarred pair by $\bar\rho=\rho(1-\lambda^2/2+\cdots)$ and $\bar\eta=\eta(1-\lambda^2/2+\cdots)$. Its angles

$$
\alpha,\ \beta,\ \gamma
\qquad\text{with}\qquad
\sin2\beta = \frac{2(1-\bar\rho)\bar\eta}{(1-\bar\rho)^2+\bar\eta^2},\qquad
\gamma=\arctan\frac{\bar\eta}{\bar\rho},
$$

are measured by CP-violating asymmetries in $B$ and $K$ decays. With the standard parameters the recomputation gives

$$
\sin2\beta = 0.707,\qquad \beta\simeq22.5^\circ,\qquad \gamma\simeq65.4^\circ,\qquad
\alpha = 180^\circ-\beta-\gamma\simeq92^\circ,
$$

in agreement with the measured values. The triangle closes as a consequence of unitarity, and the closure is the framework's content: unitarity is the framework's requirement on the flavour factor, and the closure is the statement that the three-generation mixing matrix is a point of $U(3)$.

**The measured entries and the one phase.** The magnitudes and the phase are measured to good precision, and the data are consistent with a single unitarity triangle. The framework's role is exhausted by the structure: it supplies the group $U(N_g)$, the tensor placement, the non-centrality of the phase, and the counting; the numerical values are inputs. This is the flavour-sector analogue of the framework's position on the mass matrices and on the generation number, and the article states it without further claim.

**The CP-odd observables.** The invariant $J$ controls the CP-violating observables: the kaon parameter $\epsilon_K$, the $B$-decay asymmetries proportional to $\sin2\beta$, and the direct CP asymmetries. All are proportional to $J$ times products of hadronic matrix elements, and the consistency of the measurements with a single $J$ is the Standard Model's success in the flavour sector. The framework inherits the observables and the success; it adds the algebraic placement.

## The Unitarity Triangle and the Jarlskog Area

**The triangles from unitarity.** The unitarity of $V$ gives six orthogonality relations, each of the form $V_{ij}V_{ik}^{*}+V_{lj}V_{lk}^{*}+V_{nj}V_{nk}^{*}=0$, and each defines a triangle in the complex plane. The six triangles have a common area, and the area is a rephasing-invariant measure of CP violation. For the triangle formed by the orthogonality of the first and third columns, the sides are

$$
V_{ud}V_{ub}^{*}+V_{cd}V_{cb}^{*}+V_{td}V_{tb}^{*}=0 ,
$$

and the recomputation with the standard parameters confirmed that the three terms sum to zero (to machine precision) and that the triangle's area is

$$
A_{\triangle} = \tfrac12\,|J| = 1.5419\times10^{-5},
$$

exactly half the Jarlskog invariant: $|J|/2 = 1.541866\times10^{-5}$, and the computed area matched it to the last digit. The relation **area $=\tfrac12|J|$** is the geometric statement of the CP-violating invariant, and it holds for all six triangles.

**The rescaled triangle.** Dividing the relation by $|V_{cd}V_{cb}^{*}|$ brings the triangle to the standard $(\bar\rho,\bar\eta)$ form with vertices $(0,0)$, $(1,0)$, $(\bar\rho,\bar\eta)$ and angles $\alpha,\beta,\gamma$; in those rescaled coordinates the area is $\bar\eta/2$, and the two area statements are related by the side lengths. The framework's content is the closure: the sides are products of entries of a **unitary** matrix on the flavour factor, and unitarity is exactly the framework's requirement that the flavour rotation preserve the norm on $\mathcal{F}$. The closure of the triangle is the statement that $V$ is a point of $U(N_g)$, and the nonzero area is the statement that the point is not real.

**The number of triangles and the number of phases.** For $N_g$ generations there are $\tfrac12N_g(N_g-1)$ independent triangles from the column (or row) orthogonality relations, and for $N_g=3$ there are three; all six (rows and columns) collapse to the same area $|J|/2$. The number of triangles exceeds the number of CP-violating phases by one for $N_g=3$ (three triangles, one phase), and the equality of their areas is a nontrivial consistency condition of the unitary structure. The framework supplies the unitary structure and the counting; the equality is a theorem of the group.

## CP Violation in the Lepton Sector

**The parallel structure.** The lepton sector has the same framework structure as the quark sector: a mixing matrix $U_{\mathrm{PMNS}}=U_e^\dagger U_\nu$ on the flavour factor, diagonalising the charged-lepton and neutrino mass matrices, with the same tensor placement $I_\Delta\otimes U_{\mathrm{PMNS}}$. The matrix is unitary and, for three generations, carries one CP-violating phase $\delta_{\mathrm{CP}}$ (and possibly two Majorana phases, which do not affect neutrino oscillations). The companion article on the neutrino and the seesaw article supply the neutrino mass matrices; this section records the parallel.

**The leptonic Jarlskog invariant.** The leptonic analogue of $J$ is

$$
J_{\mathrm{CP}} = \mathrm{Im}\big(U_{e1}U_{\mu2}U_{e2}^{*}U_{\mu1}^{*}\big)
= c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta_{\mathrm{CP}} ,
$$

the same expression with the leptonic angles and phase. The framework's structure is identical, and the two invariants are independent inputs. The experimental situation is the standard one: the leptonic angles are measured with the atmospheric and solar values, the phase is constrained but not yet precisely fixed, and the discovery of leptonic CP violation is a goal of the long-baseline experiments.

**The Majorana phases and the difference.** The leptonic sector differs from the quark sector in one framework-relevant way: if the neutrinos are Majorana, the mass matrix is symmetric and its diagonalisation admits two additional rephasing-invariant phases, the Majorana phases, which are absent in the quark sector because the quark mass matrices are general complex matrices. The difference is a property of the flavour factor's reality structure, which the companion article on the neutrino treats; the article's structural point is that both sectors share the tensor placement, the unitarity, and the non-centrality of their CP phases, and that the framework supplies the structure and not the values.

## The Running of the CKM Parameters

**Scale dependence.** The CKM parameters, like the quark masses, are scale-dependent: the mass matrices acquire radiative corrections and the mixing angles and phase run with the renormalisation scale. The running is governed by the anomalous dimensions of the quark bilinears and is quantitatively important only at high scales; the framework inherits it, and the framework's own parameters — the algebra, its sectors, the trace — do not run, because they are finite-dimensional algebraic data. The statement is the same as elsewhere in the framework: the algebraic structure is scale-independent, and the flavour-factor data run.

**The framework's contribution to the running.** The framework's one-generation quantities — the mass term and its chiral structure — run with the standard anomalous dimensions of a Dirac fermion, and the companion article on the Dirac field records the free theory. The flavour-factor running is a matrix generalisation, and it does not involve the algebra. In the language of the article, the running multiplies the mass matrices by a scale-dependent matrix $I_\Delta\otimes Z(\mu)$ and rotates them; the mixing matrix runs because the rotations of the up and down sectors run differently. The framework hosts the running on the flavour factor, as it hosts everything else in the flavour sector.

## CP Violation and the Baryon Asymmetry

**The CKM phase is too small.** The observed baryon asymmetry of the universe requires CP violation beyond the Standard Model's CKM phase: the Jarlskog invariant $J\simeq3\times10^{-5}$ is far too small to generate the asymmetry through electroweak baryogenesis, and the electroweak phase transition in the Standard Model is not strongly first order. The framework inherits this quantitative statement and adds the structural one: the CKM phase is a flavour-factor phase (the previous sections), so any additional CP violation needed for baryogenesis must also live on the flavour factor or in new physics outside the framework's algebra.

**Where the framework leaves the question.** The framework's center is generation-blind and CP-even in the flavour sense, and its algebra supplies no CP-odd invariant. A baryogenesis mechanism would therefore have to be an additional structure — new phases on the flavour factor, new particles, or a departure from the framework's present spectrum — and the framework neither supplies nor excludes it. The article records the electroweak-baryogenesis requirement as the standard motivation for CP violation beyond the CKM phase, with the framework's structural statement attached.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The CKM matrix as a flavour-factor operator $I_\Delta\otimes V$ | **Supplied**; the tensor placement |
| Gauge-sector flavour universality and the GIM mechanism | **Supplied**; the gauge vertex is $I_{\mathcal{F}}$ in flavour space |
| The count $(N_g-1)^2$, and $N_g\ge3$ for a CP phase | **Supplied** by the unitary group of the flavour factor; standard counting |
| The non-centrality of the CP phase | **Supplied**; the center is $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}$ and acts on all generations alike |
| The Jarlskog invariant as a flavour-factor commutator | **Supplied** in form; standard in content |
| The mass-matrix origin of the mixing, $V=U_u^\dagger U_d$ | **Transcribed**; standard |
| The Wolfenstein parametrisation and the unitarity triangle | **Transcribed**; standard |
| The measured values of the angles, phase, and $J$ | **Transcribed**; standard, with unitarity and $J$ recomputed |
| The values of the CKM parameters, and the mass matrices | **Not supplied**; empirical |
| A flavour dynamics or symmetry that generates the pattern | **Not supplied**; the flavour factor is arbitrary |
| The relation of the quark mixing to the lepton mixing | **Not supplied**; they are independent inputs |

## Open Questions

1. **A flavour principle.** Whether a symmetry or a dynamics on the flavour factor can be formulated within the framework — a discrete family group, a radiative mechanism, or a structure on $\mathbb{C}^{N_g}$ — is open. The framework can host such a mechanism; it does not contain one.

2. **The phase's seat.** The article states that the CP phase must be a flavour-factor object because the center is generation-blind. Whether the framework can say anything more — for instance whether a flavour-factor phase can be related to the real structure $\flat$ or to the central $i$ — is not settled.

3. **The quark–lepton connection.** In grand-unified extensions the quark and lepton mass matrices are related and the two mixing matrices are correlated. The framework has no unified structure, so it treats them as independent; whether a biquaternion unification can relate them is outside this article.

4. **The strong CP problem.** The CKM phase is not the only CP-odd parameter; the $\theta$ parameter is another, and its smallness is the strong CP problem. The $\theta$ parameter belongs to the corpus's general gauge apparatus; the fermion-sector statement is that the two phases are independent inputs in the framework.

## Summary

The CKM matrix is a unitary operator on the framework's generation (multiplicity) factor, acting on $\Delta\otimes\mathbb{C}^{N_g}$ as $I_\Delta\otimes V$, and arising from the mismatch of the up- and down-type mass matrices, $V=U_u^\dagger U_d$, both of which are flavour-factor operators while the module factor is common. The framework's gauge sector is flavour-universal, which is the algebraic form of the GIM mechanism: the charged-current vertex is $I_\Delta\otimes(\gamma^\mu P_LV)$, and the neutral currents carry $I_{\mathcal{F}}$ and are flavour-diagonal. The parameter count is that of $U(N_g)$: $(N_g-1)^2$ parameters, comprising $\tfrac12N_g(N_g-1)$ angles and $\tfrac12(N_g-1)(N_g-2)$ phases, so that a CP-violating phase requires $N_g\ge3$.

The framework's definite structural contribution is the location of the phase. The algebra acting on the multi-generation space is $\mathbb{B}\otimes M_{N_g}(\mathbb{C})$ with center $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}\cong\mathbb{C}$, a single generation-blind central phase; a phase that distinguishes generations therefore cannot be central and must sit in the flavour factor $I_\Delta\otimes M_{N_g}(\mathbb{C})$. The framework's own central phases are CP-even in the flavour sense, and all quark-sector CP violation is a statement about the matrix on $\mathbb{C}^{N_g}$. The Jarlskog invariant, $J=\mathrm{Im}(V_{ud}V_{cs}V_{us}^{*}V_{cd}^{*})=c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta$, is the minimal rephasing-invariant measure of the CP violation and is proportional to the imaginary part of the determinant of the commutator of the two mass-matrix products; the recomputation with the standard parameters gave $J=3.08\times10^{-5}$, unitarity of the reconstructed matrix to machine precision, $\sin2\beta=0.707$, $\beta\simeq22.5^\circ$, and $\gamma\simeq65.4^\circ$. The framework places all of this on the flavour factor and supplies none of the values.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+,\mathbb{C}_{\mathbb{B}}$ | Material, informational sectors; center |
| $\Delta=S\oplus\bar{S}$ | Dirac module, $\dim_{\mathbb{C}}=4$ |
| $\mathcal{F}=\mathbb{C}^{N_g}$ | Generation (multiplicity) factor |
| $\Delta\otimes\mathcal{F}$ | $N_g$-generation fermion space |
| $I_\Delta\otimes V$, $V\in U(N_g)$ | The CKM matrix as a flavour-factor operator |
| $M_u^{\mathcal{F}},M_d^{\mathcal{F}}$ | Up- and down-type mass matrices on $\mathcal{F}$ |
| $V=U_u^\dagger U_d$ | CKM matrix from the diagonalisations |
| $I_\Delta\otimes(\gamma^\mu P_LV)$ | Charged-current vertex |
| $I_\Delta\otimes I_{\mathcal{F}}$ | Gauge vertices; flavour universality (GIM) |
| $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}$ | Center of the multiplied algebra; generation-blind |
| $\tfrac12N_g(N_g-1)$, $\tfrac12(N_g-1)(N_g-2)$ | Mixing angles; CP-violating phases |
| $J=\mathrm{Im}(V_{ud}V_{cs}V_{us}^{*}V_{cd}^{*})$ | Jarlskog invariant |
| $J=c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta$ | Jarlskog invariant, three-angle form |
| $\lambda,A,\bar\rho,\bar\eta$ | Wolfenstein parameters (barred values) |
| $\alpha,\beta,\gamma$ | Unitarity-triangle angles |
| $A_\triangle=\tfrac12|J|$ | Unitarity-triangle area |
| $U_{\mathrm{PMNS}}$, $\delta_{\mathrm{CP}}$, $J_{\mathrm{CP}}$ | Leptonic mixing matrix, phase, invariant |
| $J=3.08\times10^{-5}$ | Measured Jarlskog invariant (recomputed) |
| $\sin2\beta=0.707$, $\gamma\simeq65.4^\circ$ | Recomputed CP observables |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- N. Cabibbo, "Unitary symmetry and leptonic decays," *Physical Review Letters* **10** (1963) 531–533, for the original mixing angle.
- M. Kobayashi and T. Maskawa, "CP violation in the renormalizable theory of weak interaction," *Progress of Theoretical Physics* **49** (1973) 652–657, for the three-generation mixing matrix and its CP-violating phase.
- S. L. Glashow, J. Iliopoulos, and L. Maiani, "Weak interactions with lepton–hadron symmetry," *Physical Review D* **2** (1970) 1285–1292, for flavour universality and the GIM mechanism.
- L. Wolfenstein, "Parametrization of the Kobayashi–Maskawa matrix," *Physical Review Letters* **51** (1983) 1945–1947, for the expansion in $\lambda$.
- C. Jarlskog, "Commutator of the quark mass matrices in the standard electroweak model and a measure of maximal CP nonconservation," *Physical Review Letters* **55** (1985) 1039–1042, for the invariant measure of CP violation.
- C. Jarlskog (ed.), *CP Violation* (World Scientific, 1989), for the collected theory and phenomenology.
- Y. Nir, "CP violation in meson decays," in *Lectures on Flavor Physics* (Springer, 2002), and the review literature, for the unitarity triangle and the CP observables.
- A. Ceccucci, Z. Ligeti, and Y. Sakai, "The CKM quark-mixing matrix," in *Review of Particle Physics*, for the measured parameters and the global fits.
- M. Battaglia *et al.*, "The CKM matrix and the unitarity triangle," *Physics Reports* (2003), for the experimental determination of the triangle.
- G. C. Branco, L. Lavoura, and J. P. Silva, *CP Violation* (Oxford, 1999), for the general theory of CP violation in the quark and lepton sectors.
- A. D. Sakharov, "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe," *JETP Letters* **5** (1967) 24–27, for the conditions for baryogenesis.
- V. A. Kuzmin, V. A. Rubakov, and M. E. Shaposhnikov, "On the anomalous electroweak baryon number nonconservation in the early universe," *Physics Letters B* **155** (1985) 36–42, for electroweak baryogenesis and the requirement of CP violation beyond the CKM phase.
- G. Isidori, Y. Nir, and G. Perez, "Flavor physics constraints for physics beyond the Standard Model," *Annual Review of Nuclear and Particle Science* **60** (2010) 355–379, for the flavour sector as a probe of new physics.
