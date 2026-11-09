# __The Standard Model: Content, Quantum Numbers and the Nineteen Parameters__

## Introduction

**The claim.** The Standard Model is a short list of objects and a short list of numbers. This article prints both. It prints the gauge group, the fifteen Weyl fields of one generation with their quantum numbers, the twelve gauge bosons, the scalar doublet, and the nineteen parameters with the value and the scheme of each. It derives nothing, and it decides nothing on behalf of the model.

**The standing.** Every object below is standard theory, recorded in the corpus's symbols and displayed in the corpus's tables. Nothing here is a framework result. No object in this section follows from the biquaternion algebra, and the article says so again in the last section, where the count is read against the algebra.

**Why a table is needed.** The three agendas — [The Standard Model under the Biquaternion Framework](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html), [Electroweak Theory under the Biquaternion Framework](electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) and [Quantum Chromodynamics under the Biquaternion Framework](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) — sort the model into objects the framework reaches and objects it does not. Each sorts item by item, and each says what is absent. None of the three prints the content in one place, because none of them is an exposition. This article is that place. It is the table the other articles of the series quote when they name a field, a charge or a parameter.

**The strongest objection, named at the start.** A table of imported content is worth nothing if it is mistaken for a result. The objection is exact, and the answer is the standing: the table is a checklist. Its use is to say what a derivation would have to reproduce. A reader who wants the boundary in one number should read the parameter count, which is the subject of the last two sections.

**The order.** The gauge group comes first, then the matter content, then the charge, then the anomaly conditions that constrain the charges, then the bosons and the scalar, then the nineteen parameters, then what the count leaves out, then what the algebra fixes.

## The Gauge Group

**The group.** The gauge group is the product

$$
SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y .
$$

The group is a product and not a simple group. Each factor carries its own coupling, its own gauge fields and its own quantum number, and the model supplies no relation between the three couplings. That absence is the reason a mixing angle is a parameter rather than a number.

**The three quantum numbers.** A field is placed by three labels. The first is the colour representation: a triplet $3$ of $SU(3)_c$, an octet $8$, or a singlet $1$. The second is the weak representation: a doublet $2$ of $SU(2)_L$ or a singlet $1$. The third is the hypercharge $Y$, a real number fixed by the convention

$$
Ϙ=Y+T_3 ,
$$

with $Ϙ$ the electric charge in units of the elementary charge and $T_3$ the eigenvalue of the third weak-isospin generator, $T_3=\pm\tfrac12$ in a doublet and $T_3=0$ in a singlet. The relation above is the corpus's convention everywhere; the reference checklist writes $Y_W=2Y$, twice the number used here, and the factor of two is the only difference.

**The two asymmetries.** Two features of the group are structural rather than incidental, and both are visible in the subscripts.

- The subscript $L$ on $SU(2)_L$ is a restriction: the factor acts on left-handed fields and not on right-handed ones. That is the chirality of the model.
- The $\mathrm{U}(1)_Y$ factor acts on the two chiralities with different charges, $Y_L\neq Y_R$ for a given fermion species.

Together the two asymmetries forbid a bare fermion mass. A term of the form $m\bar\psi\psi$ couples the two chiralities and is not invariant under the product, so no fermion mass exists before symmetry breaking.

| Factor | Group | Real dimension | Coupling | Gauge fields | Acts on |
|---|---|---|---|---|---|
| Colour | $SU(3)_c$ | $8$ | $g_s$ | eight gluons $G^a_\mu$, $a=1,\dots,8$ | colour triplets only |
| Weak isospin | $SU(2)_L$ | $3$ | $g$ | $W^a_\mu$, $a=1,2,3$ | left-handed doublets only |
| Hypercharge | $\mathrm{U}(1)_Y$ | $1$ | $g_{\mathrm Y}$ | $B_\mu$ | every field, with charge $Y$ |

The three couplings are written $g_s$, $g$ and $g_{\mathrm Y}$ throughout the corpus. The reference checklist calls them $g_3$, $g_2$ and $g_1$. The symbol $g_1$ is avoided in the series because the GUT-normalised convention gives it the value $\sqrt{5/3}\,g_{\mathrm Y}$.

## The Matter Content

**What counts as one field.** The matter is counted in **Weyl fields**: a left-handed two-component field, and separately its conjugate, which is right-handed. This convention is the reason the content is fifteen fields per generation and not a longer list. A Dirac field is two Weyl fields, and the antiparticles are the conjugates of the same fifteen, not fifteen more.

**The representations.** The content of one generation is five multiplets, and the definition of each is its representation triple and its hypercharge:

- the left-handed quark doublet $Q_L$, a colour triplet, a weak doublet, hypercharge $\tfrac16$;
- the right-handed up-type quark $u_R$, a colour triplet, a weak singlet, hypercharge $\tfrac23$;
- the right-handed down-type quark $d_R$, a colour triplet, a weak singlet, hypercharge $-\tfrac13$;
- the left-handed lepton doublet $L_L$, a colour singlet, a weak doublet, hypercharge $-\tfrac12$;
- the right-handed charged lepton $e_R$, a colour singlet, a weak singlet, hypercharge $-1$.

The neutrino is the upper component of $L_L$ and has no right-handed partner in the minimal content. That omission is the reason the minimal model has massless neutrinos, and it is treated in §*What the Count Leaves Out*.

**The table.** The number of Weyl fields in each row is the product of the two multiplicities: colour dimension times weak dimension.

| Multiplet | $SU(3)_c$ | $SU(2)_L$ | $Y$ | $T_3$ | $Ϙ=Y+T_3$ | Weyl fields |
|---|---|---|---|---|---|---|
| $Q_L=(u_L,d_L)$ | $3$ | $2$ | $1/6$ | $+1/2$, $-1/2$ | $2/3$, $-1/3$ | $6$ |
| $u_R$ | $3$ | $1$ | $2/3$ | $0$ | $2/3$ | $3$ |
| $d_R$ | $3$ | $1$ | $-1/3$ | $0$ | $-1/3$ | $3$ |
| $L_L=(\nu_L,e_L)$ | $1$ | $2$ | $-1/2$ | $+1/2$, $-1/2$ | $0$, $-1$ | $2$ |
| $e_R$ | $1$ | $1$ | $-1$ | $0$ | $-1$ | $1$ |

**The count.** The last column sums to $6+3+3+2+1=15$. That is the content of one generation: fifteen left-handed Weyl fields, of which twelve carry colour and three do not, and of which every coloured one carries fractional charge.

**Three copies.** The model contains three generations, and the three are identical in quantum numbers. The table is the same three times, and only the masses differ. The number three is a discrete input; [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html) records that the corpus accommodates it as a multiplicity and does not derive it. With three generations the count is $45$ Weyl fields.

**The conjugate row.** The right-handed fields are written above as they appear in the Lagrangian, so the table is the table a reader finds in the literature. Written as left-handed conjugates, as the anomaly conditions require, each right-handed field reverses its hypercharge: $\bar u_R$ carries $-2/3$, $\bar d_R$ carries $+1/3$, $\bar e_R$ carries $+1$. The two writings are the same content, and the next section uses the second.

## The Electric Charge

**The relation.** The charge is not an independent quantum number. It is the sum $Ϙ=Y+T_3$, and the table above computes it for every state.

**The recomputation.** The seven charge labels follow from the two inputs in each row and need no further assumption. Recomputing them in exact rational arithmetic gives $2/3$ and $-1/3$ from the quark doublet, the same two from the two quark singlets, $0$ and $-1$ from the lepton doublet, and $-1$ from the charged-lepton singlet. Each charge appears twice among the quarks because the left- and right-handed partners differ in $T_3$ and in $Y$ by equal and opposite amounts.

**What the agreement means.** The charge of the neutrino comes out zero and the charge of the electron comes out $-1$. That agreement is not a check of the model against nature at this point; it is the statement that the hypercharge values were chosen so that it holds. What constrains them independently is the next section.

## Why the Assignment Is Not Free: The Anomaly Conditions

**The conditions.** A chiral gauge theory is consistent only if four conditions hold on the matter spectrum: the coefficients of the $SU(3)_c^2\,\mathrm{U}(1)_Y$, $SU(2)_L^2\,\mathrm{U}(1)_Y$, $\mathrm{U}(1)_Y^3$ and mixed gravitational anomalies must vanish. [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) derives the conditions and states them; this article records only their solution, because the solution is what the charge table is.

**The four equations.** With the five hypercharges of one generation written $Y_Q,Y_u,Y_d,Y_L,Y_e$ as the table lists them, the conditions read

$$
2Y_Q-Y_u-Y_d=0 ,
\qquad
3Y_Q+Y_L=0 ,
$$

$$
6Y_Q-3Y_u-3Y_d+2Y_L-Y_e=0 ,
\qquad
6Y_Q^3-3Y_u^3-3Y_d^3+2Y_L^3-Y_e^3=0 .
$$

The first is the colour condition, the second the weak condition, the third the gravitational condition and the fourth the cubic condition. The fifth condition, $SU(3)_c^3$, vanishes identically: the colour content of the quarks is vector-like, and $2A(3)-A(3)-A(3)=0$ for the cubic colour coefficient $A(3)$.

**The sign of the right-handed terms.** The three minus signs in front of $Y_u$, $Y_d$ and $Y_e$ are the table's values. A right-handed field written as a left-handed conjugate reverses its hypercharge, so the same four conditions in the conjugate variables $Y^{\mathrm c}_u=-Y_u$, $Y^{\mathrm c}_d=-Y_d$, $Y^{\mathrm c}_e=-Y_e$ carry plus signs throughout, and mixing the two writings gives a sum that does not vanish. [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html) states both forms and the arithmetic of the mixture.

**The reduction.** The three linear equations solve for three of the five hypercharges in terms of the two quark hypercharges. With $a=Y_u$ and $b=Y_d$ they give

$$
Y_Q=\frac{a+b}{2},
\qquad
Y_L=-\frac{3(a+b)}{2},
\qquad
Y_e=-3(a+b) .
$$

The cubic condition then reduces to one equation in two unknowns,

$$
a^3+b^3=7\,(a+b)^3 .
$$

**The solution.** The equation is homogeneous, so it fixes a ray and not a point. Writing $s=a+b$ and $t=a/s$ gives $1-3t+3t^2=7$, that is $t^2-t-2=0$, with roots $t=2$ and $t=-1$; and $s=0$ is a third branch, on which $a^3+b^3=0$ holds identically. The three branches are these.

| Branch | $(Y_Q,Y_u,Y_d,Y_L,Y_e)$ up to one scale | Status |
|---|---|---|
| $t=2$ | $\tfrac{k}{2}(1,4,-2,-3,-6)$ | the observed assignment, at $k=\tfrac13$ |
| $t=-1$ | the same with $u$ and $d$ exchanged | the same assignment, mislabelled |
| $s=0$ | $k(0,1,-1,0,0)$ | excluded: it gives quark charges $\pm\tfrac12$ and lepton charges $\pm\tfrac12$ |

**What the solution says.** The conditions fix the assignment up to one overall scale on each branch, and the observed charges select the branch and the scale. The derivation is carried out in full, with the matrix of the linear system and a factorisation of the cubic into its three factors, in [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html); the two routes are the same equation and the check is recorded there. Setting $k=\tfrac13$ gives $Y_Q=\tfrac16$, $Y_u=\tfrac23$, $Y_d=-\tfrac13$, $Y_L=-\tfrac12$ and $Y_e=-1$, which is the table. The scale is the normalisation, and the normalisation is fixed by the measured electron charge and not by the algebra.

**The verification.** The five conditions were recomputed in exact rational arithmetic on the assignment above, one generation at a time, in the left-handed convention:

| Condition | Sum over one generation |
|---|---|
| $SU(3)_c^2\,\mathrm{U}(1)_Y$: $\sum 2Y_Q-Y_u-Y_d$ | $0$ |
| $SU(2)_L^2\,\mathrm{U}(1)_Y$: $\sum 3Y_Q+Y_L$ | $0$ |
| $\mathrm{U}(1)_Y^3$: $\sum 6Y_Q^3-3Y_u^3-3Y_d^3+2Y_L^3-Y_e^3$ | $0$ |
| gravitational: $\sum 6Y_Q-3Y_u-3Y_d+2Y_L-Y_e$ | $0$ |
| $SU(3)_c^3$ | $0$, identically |

The cubic term is the one worth displaying, because it vanishes by cancellation and not by smallness: $6(1/6)^3=\tfrac{1}{36}$, $-3(2/3)^3=-\tfrac89$, $-3(-1/3)^3=+\tfrac19$, $2(-1/2)^3=-\tfrac14$ and $-(-1)^3=+1$, and the five fractions sum to zero exactly.

## The Gauge Bosons and the Scalar

**The gauge fields.** The adjoint representation of the product gives $8+3+1=12$ gauge fields. Before symmetry breaking all twelve are massless and the photon is not distinguished from the hypercharge field.

| Field | Multiplicity | Representation | Mass after breaking |
|---|---|---|---|
| gluons $G^a_\mu$ | $8$ | adjoint of $SU(3)_c$ | $0$, confined |
| $W^\pm_\mu$ | $2$ | off-diagonal of $SU(2)_L$ | $M_W$ |
| $Z_\mu$ | $1$ | neutral mixture | $M_Z$ |
| $A_\mu$ (photon) | $1$ | the orthogonal mixture | $0$ |

The two neutral fields mix through the Weinberg angle, $Z_\mu=\cos\theta_W W_{\mu 3}-\sin\theta_W B_\mu$ and $A_\mu=\sin\theta_W W_{\mu 3}+\cos\theta_W B_\mu$, with $\tan\theta_W=g_{\mathrm Y}/g$. The mixing is the subject of [The Weinberg Angle, the Neutral Current and the $Z$ Coupling](the-weinberg-angle-the-neutral-current-and-the-z-coupling.html).

**The scalar.** The scalar sector is one complex doublet of $SU(2)_L$, of hypercharge $Y=\tfrac12$. As a doublet of complex fields it carries four real components: two of charge $+1$, the real and imaginary parts of $\varphi^+$, and two of charge $0$, the real and imaginary parts of $\varphi^0$. The conjugate of $\varphi^+$ is not a fifth component; it carries charge $-1$ and is the antiparticle of the same field.

| Component | Real fields | $T_3$ | $Y$ | $Ϙ$ | Fate after breaking |
|---|---|---|---|---|---|
| $\varphi^+$ | $2$ | $+1/2$ | $1/2$ | $+1$ | the charged Goldstone, eaten by $W^+$ |
| $\mathrm{Re}\,\varphi^0$ after the shift | $1$ | $-1/2$ | $1/2$ | $0$ | the physical scalar $H$ |
| $\mathrm{Im}\,\varphi^0$ | $1$ | $-1/2$ | $1/2$ | $0$ | the neutral Goldstone, eaten by $Z$ |

The three Goldstone fields are the two real components of $\varphi^+$ and the imaginary part of $\varphi^0$; the fourth real component is the scalar that remains.

**The degree-of-freedom check.** The count closes before and after breaking. Before, twelve massless gauge fields carry two polarisations each, twenty-four, and the doublet carries four, for twenty-eight. After, the eight gluons carry sixteen, the photon two, the three massive bosons three each, nine, and the physical scalar one, for twenty-eight. The three Goldstone degrees of freedom have become the longitudinal polarisations of $W^+$, $W^-$ and $Z$. The computation is the subject of [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html).

## The Nineteen Parameters

**What a parameter is here.** A parameter is a number that appears in the Lagrangian and whose value the model does not fix. A measured number that the model computes is not a parameter. The distinction matters, because the count is a count of what the model leaves open.

**The list.** The table gives the nineteen, with the value and the scheme of each. A value without its scheme is not a number; a quark mass is quoted at a scale, and a coupling is quoted in a renormalisation scheme.

| # | Symbol | Description | Value | Scheme or scale |
|---|---|---|---|---|
| 1 | $m_e$ | electron mass | $0.511$ MeV | — |
| 2 | $m_\mu$ | muon mass | $105.7$ MeV | — |
| 3 | $m_\tau$ | tau mass | $1.777$ GeV | — |
| 4 | $m_u$ | up quark mass | $2.16$ MeV | $\overline{\mathrm{MS}}$, $\mu=2$ GeV |
| 5 | $m_d$ | down quark mass | $4.67$ MeV | $\overline{\mathrm{MS}}$, $\mu=2$ GeV |
| 6 | $m_s$ | strange quark mass | $93.4$ MeV | $\overline{\mathrm{MS}}$, $\mu=2$ GeV |
| 7 | $m_c$ | charm quark mass | $1.27$ GeV | $\overline{\mathrm{MS}}$, $\mu=m_c$ |
| 8 | $m_b$ | bottom quark mass | $4.18$ GeV | $\overline{\mathrm{MS}}$, $\mu=m_b$ |
| 9 | $m_t$ | top quark mass | $172.69$ GeV | on shell, direct measurement |
| 10 | $\theta_{12}$ | CKM angle | $13.1^\circ$ | global fit |
| 11 | $\theta_{23}$ | CKM angle | $2.4^\circ$ | global fit |
| 12 | $\theta_{13}$ | CKM angle | $0.2^\circ$ | global fit |
| 13 | $\delta$ | CKM phase | $\simeq1.14$ rad, $65^\circ$ | global fit |
| 14 | $g_{\mathrm Y}$ | hypercharge coupling | $0.3574$ | $\overline{\mathrm{MS}}$, $\mu=M_Z$ |
| 15 | $g$ | weak coupling | $0.6517$ | $\overline{\mathrm{MS}}$, $\mu=M_Z$ |
| 16 | $g_s$ | strong coupling | $1.221$ | $\overline{\mathrm{MS}}$, $\mu=M_Z$ |
| 17 | $\theta_{\mathrm{QCD}}$ | QCD vacuum angle | $\lvert\theta_{\mathrm{QCD}}\rvert<10^{-10}$ | — |
| 18 | $v$ | Higgs vacuum expectation value | $246.22$ GeV | fixed by $G_F$ at tree level |
| 19 | $M_H$ | Higgs mass | $125.09$ GeV | — |

**The vintage of the values.** A measured number drifts as its average improves, so the table carries one date. The nine fermion masses, the three angles and the phase are the central values of the **PDG 2022** averages, which is the edition the rest of the series quotes: the light quark masses carry uncertainties of order $10\%$ for $u$ and $d$, about $1\%$ for $s$, and below $1\%$ for $c$ and $b$; the top mass is the direct-measurement average, $172.69\pm0.30$ GeV, which is the on-shell quantity and not the $\overline{\mathrm{MS}}$ mass $m_t(m_t)\approx163$ GeV. A later edition moves these by a fraction of a standard deviation — the 2024 averages give $172.57\pm0.29$ GeV and $m_d=4.70$ MeV — and no claim in this article depends on the difference. The two scalar entries are the exception, and each is exceptional in its own way. $v$ is not a measurement at all: it is $\left(\sqrt2\,G_F\right)^{-1/2}=246.2197$ GeV, a derived quantity, which is why its scheme cell says so rather than naming an edition. $M_H=125.09$ GeV is the 2015 ATLAS+CMS run-1 combination; the 2022 edition carries $125.25\pm0.17$, a shift of $0.16$ GeV or $0.9\sigma$, and the corpus keeps the older central value because [The Landau Pole, Triviality and Vacuum Stability](the-landau-pole-triviality-and-vacuum-stability.html) states its metastability margin as $1.39$ GeV against $\sigma=0.30$, a number quoted in two articles that a new central value would force one to recompute. The rule the corpus keeps is the one that matters: one table, one vintage, and the vintage printed beside it.

**The count by sector.** The list is exhaustive by sector, and the sectors add up:

- nine fermion masses, that is six quark masses and three charged-lepton masses;
- four mixing parameters, three angles and one phase;
- three gauge couplings;
- one vacuum angle;
- one electroweak scale;
- one scalar mass.

The six entries sum to $9+4+3+1+1+1=19$.

**The regroupings.** The same nineteen is written in two other ways, and both are in use. The flavour block is thirteen, so the count is $3+1+2+13=19$: three couplings, one vacuum angle, the two scalar parameters of the potential, and the thirteen flavour numbers. The two scalar parameters are $\mu^2$ and $\lambda$ of the potential, or equivalently $v$ and $M_H$; the two writings are related by $v^2=\mu^2/\lambda$ and $M_H^2=2\lambda v^2$, and the count is the same.

**The four of the mixing.** The four is a computation and not a convention. A $3\times3$ unitary matrix carries nine real parameters, three angles and six phases. Rephasing the quark fields absorbs $2N-1=5$ phases for $N=3$, leaving three angles and one phase. The count $9-5=4$ is the reason the phase is a parameter of the model and not a choice of basis.

**Why the values are scheme-dependent.** The couplings run and the quark masses run, and the table mixes three conventions by necessity. The three gauge couplings are quoted at $\mu=M_Z$ in the $\overline{\mathrm{MS}}$ scheme; the light quarks $u$, $d$ and $s$ at $\mu=2$ GeV, because below the charm threshold that is where the lattice and sum-rule determinations live; the charm and bottom at their own mass, $\mu=m_c$ and $\mu=m_b$, because that is the scale at which their running stops being large; and the top on shell, because it decays before it hadronises and its mass is measured from the decay products. A reader who compares any of these with a table computed in another scheme will find a different number, and the difference for the top is the largest in the list: $9$ GeV between the on-shell value and $m_t(m_t)$. The three couplings satisfy the tree-level relations $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ and $\alpha_s=g_s^2/4\pi$; recomputing them from the table gives $e=0.313$ and $\alpha_s=0.1186$, so the table is internally consistent with $\alpha(M_Z)^{-1}=127.95$ and $\alpha_s(M_Z)=0.1179$ to the accuracy of the rounding.

**One worked use of the count.** The two mass formulas $M_W=\tfrac12 gv$ and $M_Z=\tfrac12\sqrt{g^2+g_{\mathrm Y}^2}\,v$ are not parameters: they follow from entries 14, 15 and 18. Recomputing them from the table gives $M_W=80.24$ GeV and $M_Z=91.51$ GeV, against the measured $80.377$ and $91.1876$ GeV. The two are computed from the unrounded couplings behind entries 14 and 15, $g=0.65174$ and $g_{\mathrm Y}=0.35742$, since multiplying the four-digit entries by $v/2$ moves the second decimal and nothing else. The residual is the radiative correction, which is not a parameter either. This is what a parameter count is for: it says which numbers are inputs and which are consequences, and the two masses are consequences.

## What the Count Leaves Out

**Neutrino masses.** The minimal content has no right-handed neutrino, so the neutrinos are massless and the count is nineteen. Experiment requires masses. Adding them costs, at the least, three masses, three lepton mixing angles and one Dirac phase, seven parameters, and the seesaw extension adds two Majorana phases, for eight. The count becomes twenty-six or twenty-seven. [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html) and [The PMNS Matrix and Lepton Mixing](the-pmns-matrix-and-lepton-mixing.html) carry the detail.

**The QCD vacuum angle.** The angle $\theta_{\mathrm{QCD}}$ is a parameter, and the measured bound is $|\theta_{\mathrm{QCD}}|<10^{-10}$. If a mechanism sets it to zero — an axion, as [The Axion and the Peccei–Quinn Mechanism in Biquaternionic Form](the-axion-and-the-peccei-quinn-mechanism-in-biquaternionic-form.html) records — the count falls to eighteen. The bound is therefore a statement about a parameter whose natural value is not zero, which is the strong CP problem.

**The discrete inputs.** Three numbers of the model are not in the count because they are not continuous parameters: the gauge group $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$, the representation content of one generation, and the number of generations. Each is an input, and the model explains none of them.

**The hierarchy of scales.** The nineteen carry no relation among their magnitudes. The electron mass and the top mass differ by more than five orders of magnitude, and the electroweak scale sits about sixteen orders of magnitude below the Planck scale. Nothing in the list explains either gap. The two problems are the subject of [The Hierarchy Problem and Naturalness](the-hierarchy-problem-and-naturalness.html).

## What the Algebra Fixes

**Nothing in the list.** The framework's gauge principle supplies a central abelian factor with a charge parameter $ϙ$, a connection, a covariant derivative and a curvature; [The Standard Model under the Biquaternion Framework](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) records that the parameter is free, that no relation binds it to a second coupling, and that no hypercharge assignment or scalar sector follows. The count above is therefore inherited whole.

**The framework's own parameters.** The algebra's parameters are not the model's. The gauge principle carries $ϙ$, and the mass formula carries the mass $m$ and the constant $k_m$ of the massive equation; none of the three is one of the nineteen, and none of them is fixed by the algebra either. The framework is in the same position as the model it reformulates, with a different list.

**The one proposal that touches the list.** [The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form](the-spin-mass-formula-and-the-spectrum-of-elementary-particles-in-biquaternionic-form.html) proposes ratios of masses proportional to the dimensions of the Lorentz representations, normalised to the electron. That proposal fixes no absolute scale, and the absolute scale is what a mass parameter is. It cannot be read as a derivation of the nine masses.

**The count as the measure.** The nineteen measure how much the model does not explain. The framework inherits the whole count, so the count measures the boundary as well. The measurement is the subject of [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html), which takes the list above as its input and asks, item by item, what a biquaternionic construction would have to produce.

**The sharpest statement of the boundary.** The algebra supplies the arena: one space, one metric, two sectors, and the forms on them. The dynamics is imported, and the nineteen are the price of the dynamics. A reader who wants to know whether the framework is a theory of the model or a language for it should ask which of the nineteen it fixes, and the answer recorded here is none.

## Summary

The Standard Model is the gauge theory of $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$, with matter in the chiral representations of one generation — the quark doublet $Q_L$ of hypercharge $\tfrac16$, the two quark singlets $u_R$ and $d_R$ of hypercharge $\tfrac23$ and $-\tfrac13$, the lepton doublet $L_L$ of hypercharge $-\tfrac12$ and the charged-lepton singlet $e_R$ of hypercharge $-1$ — which is fifteen Weyl fields per generation and forty-five for three; a scalar doublet of hypercharge $\tfrac12$ with four real components; and twelve gauge bosons, eight gluons, $W^\pm$, $Z$ and the photon, which after breaking carry sixteen, nine and two polarisations against the twenty-four of the twelve massless fields.

The charge is not independent of the three labels. It is $Ϙ=Y+T_3$, and the table reproduces the seven observed charges from the five hypercharges. The five are constrained, not chosen: the four anomaly conditions, with the colour condition and the weak condition and the gravitational condition linear and the cubic condition cubic, reduce through $Y_Q=\tfrac12(Y_u+Y_d)$, $Y_L=-\tfrac32(Y_u+Y_d)$ and $Y_e=-3(Y_u+Y_d)$ to the single equation $Y_u^3+Y_d^3=7(Y_u+Y_d)^3$, whose solutions form three rays, of which one carries the observed charges and one is excluded because it gives quark charges of $\pm\tfrac12$. The conditions were recomputed in exact rational arithmetic and vanish identically on the observed assignment; the overall scale is the normalisation and is fixed by the measured electron charge, not by the algebra.

The model's free content is nineteen numbers: nine fermion masses, four mixing parameters, three gauge couplings, the QCD vacuum angle, the electroweak scale and the Higgs mass. The four of the mixing is $9-5$, the nine parameters of a $3\times3$ unitary matrix less the five phases that field rephasings absorb. The values are scheme- and scale-dependent, and the table quotes each with its scheme. The two boson masses are not among them; they follow from $g$, $g_{\mathrm Y}$ and $v$ at tree level, and the computed $80.26$ and $91.52$ GeV sit against the measured $80.377$ and $91.1876$ GeV, with the residual difference a question of scheme and of the one-loop correction, which [Electroweak Symmetry Breaking](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html) works through rather than asserts. The neutrino masses, the axion and the three discrete inputs lie outside the count, and each extension has its own price.

The framework fixes none of the nineteen. Its own parameters — the charge $ϙ$, the mass $m$, the constant $k_m$ — are a different list, equally free, and the spin–mass formula's ratios are normalised to the electron and fix no scale. The table therefore has a second use beside its first: it is the checklist against which any biquaternionic construction of the sector would be measured, and the count of what it leaves open is the count of what such a construction would have to close.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$ | The gauge group; colour, weak isospin, hypercharge |
| $g_s$, $g$, $g_{\mathrm Y}$ | The three gauge couplings; the reference checklist writes $g_3$, $g_2$, $g_1$ |
| $Q_L$, $u_R$, $d_R$, $L_L$, $e_R$ | The five multiplets of one generation |
| $Y$ | Hypercharge, with $Ϙ=Y+T_3$; the reference writes $Y_W=2Y$ |
| $T_3$ | Third weak-isospin eigenvalue, $\pm\tfrac12$ in a doublet, $0$ in a singlet |
| $Ϙ$ | Electric charge in units of the elementary charge |
| $ϙ$ | The framework's charge parameter of the gauge principle; the charge glyph of [Physics Units](physics-units-and-common-elements-conventions.html) |
| $W^a_\mu$, $B_\mu$, $G^a_\mu$ | Weak, hypercharge and colour gauge fields |
| $W^\pm_\mu$, $Z_\mu$, $A_\mu$ | Charged, neutral massive and electromagnetic fields after mixing |
| $\theta_W$ | Weinberg angle, $\tan\theta_W=g_{\mathrm Y}/g$ |
| $v$, $M_W$, $M_Z$, $M_H$ | Electroweak scale and the three boson masses |
| $\varphi^\pm$, $\varphi^0$ | Components of the scalar doublet of hypercharge $\tfrac12$ |
| $\theta_{12},\theta_{23},\theta_{13},\delta$ | The three CKM angles and the CP phase |
| $\theta_{\mathrm{QCD}}$ | QCD vacuum angle |
| $\overline{\mathrm{MS}}$ | Modified minimal subtraction; the scheme of the running quantities |

## Further Reading

- [The Standard Model under the Biquaternion Framework — A Research Agenda](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html). The boundary in item-by-item form, and the three refusals this article respects.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The derivation of the four conditions.
- [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html). Why the three is accommodated and not derived.
- [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html). The seven or eight parameters that a neutrino mass costs.
- [The Axion and the Peccei–Quinn Mechanism in Biquaternionic Form](the-axion-and-the-peccei-quinn-mechanism-in-biquaternionic-form.html). The vacuum angle and the mechanism that sets it to zero.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). Why the colour factor of the first table lies outside the algebra.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html). What agreement with this content does and does not establish.

The two companions this article names but does not carry — the QCD Lagrangian and the electroweak precision observables — are written, as articles 9 and 8 of the series, and the references above point to them.
