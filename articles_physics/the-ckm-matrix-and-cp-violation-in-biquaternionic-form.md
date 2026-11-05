# __The CKM Matrix and CP Violation in Biquaternionic Form__

## Introduction

The **Cabibbo–Kobayashi–Maskawa (CKM) matrix** is the unitary matrix that relates the quark mass eigenstates to the weak-interaction eigenstates. It is the origin of quark mixing and, through its single complex phase, of CP violation in the quark sector. In the Standard Model it is a $3\times3$ unitary matrix with four physical parameters — three angles and one phase — and its measured entries and phase are among the most precisely known quantities in particle physics.

In the biquaternion framework the CKM matrix is a **flavour-factor operator**. The framework carries the generation as a label on the field: the field of type $t$ and generation $a$ is an element $\psi_{t,a}$ of $\mathbb{B}$, and the algebra acts on it without knowing $a$ (the companion article on the number of generations establishes this). The mixing is an operator on the labels alone, an element $V$ of the $*$-unitary group $\mathrm{U}(N_g)$ of the factor $\mathcal{F}=\mathbb{C}^{N_g}$. Its entries are complex numbers, and the complex numbers are central in $\mathbb{B}$, so the mixing multiplies the element by a number and leaves the algebra factor untouched: $\psi_{\mathrm d,b}\mapsto\sum_a V_{ab}\,\psi_{\mathrm u,a}$.

The framework's contribution is therefore the placement of the mixing on the generation label, and one structural fact that the counting alone does not give: the CP-violating phase cannot live in the algebra's centre, because the centre acts on every generation in the same way, and it must live in the flavour factor. The parameter count itself is the standard count of $\mathrm{U}(N_g)$. The article states these and is explicit that the framework does not determine the entries.

- **Established.** The CKM matrix as an operator on the generation label, with the algebra factor untouched; the non-centrality of the phase, from the structure of the multiplied algebra, hence the requirement that the CP phase sit on the generation label; the Jarlskog invariant as a commutator on the label factor; and the identical structure of the lepton sector's mixing matrix.
- **Standard, transcribed.** The parameter count of $\mathrm{U}(N_g)$ — $\tfrac12N_g(N_g-1)$ angles and $\tfrac12(N_g-1)(N_g-2)$ phases, and the requirement $N_g\ge3$ for a CP-violating phase — together with the quark-mass diagonalisation that produces $V$, the Wolfenstein parametrisation, the unitarity triangle, the measured parameters, the Jarlskog invariant and its value, and the standard CP-violating observables. The article recomputes the unitarity and the invariant.
- **Gap, left visible.** The framework does not produce the CKM angles, the CP phase, or the mass matrices that generate them. It has no flavour dynamics and no principle selecting the mixing pattern; the values are empirical.

The article is organised as follows. The next section defines the CKM matrix and places it on the flavour factor. Three sections then give the parameter count, explain why the phase cannot be central, and derive the mixing from the mass matrices. The Jarlskog invariant follows, with the condition for CP violation, then the Wolfenstein parametrisation and the measured values, then the area of the six unitarity triangles. Three short sections carry the structure to the leptons, to the running, and to baryogenesis. A table separates what is supplied, transcribed, and missing, and open questions close the physics. A closing section gives the older literature's names for the five generators; those names appear nowhere else.

The framework results used here are those of the companion articles:

- Companion article *The Neutrino and Majorana Fermions in Biquaternionic Form*, for the lepton mixing that parallels the quark mixing.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the label $L$ and the mass selection rule.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the field as an element of the algebra and for the generation factor.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the free field in its two forms — the one-sided chiral pair and the two-sided operator equation — and for its mass terms and bilinears.

## The CKM Matrix as a Flavour-Factor Operator

**The mixing.** Quarks are produced and interact in weak eigenstates and propagate in mass eigenstates. Writing the charged-current interaction in the mass basis introduces the mixing, and in the framework the term reads

$$
\mathcal{L}_{W}\supset
\frac{g}{\sqrt2}\,W^+_\mu\sum_{a,b}V_{ab}\;
\psi^{\dagger}_{\mathrm u,a}\,
i\Big(i\,e_\mu\,\psi_{\mathrm d,b,L}\,\vec e_{\nu(\mu)}\Big)\vec e_x
+\text{h.c.},
$$

with $a,b$ the generation labels and $V=X_u^\dagger X_d$ the relative rotation of the up- and down-type diagonalisations. Every factor of the term is an element or a product of elements — the two units, the two central $i$'s, the label $L$ on the down field, and the number $V_{ab}$ — and no array stands behind any of them.

**The generator of the coordinate.** The Lorentz structure of the charged current is the generator of the coordinate $x_\mu$, and a generator is what it does: it multiplies an element by $i e_\mu$ on the left and by $\vec e_{\nu(\mu)}$ on the right,

$$
X\longmapsto i\,e_\mu\,X\,\vec e_{\nu(\mu)},
$$

where $\vec e_{\nu(\mu)}$ is the unit the frame pairs with $x_\mu$ (*Frame and Metric Conventions*, §*The $\mathbb{M}_-$ Frame*, for the coordinate and the metric, and §*The Rules* for the index). The current carries the label $L$: only the $L$ part of the down field enters, and the label is the one of *Special Element Conventions*, §*The Chirality Convention*. The adjoint is the dagger of *Operator and Calculus Conventions*, §*The Operators*, and the current's factor $i\vec e_x$ sits after it, which is what the display writes.

**The two factors.** The vertex is therefore a product of two factors that do not mix: the generator above, read with the label $L$, and the mixing $V$. The framework supplies the first exactly — it is the algebra's own generator — and the second is an arbitrary $*$-unitary operator on $\mathcal{F}$. The only requirement is $V\in\mathrm{U}(N_g)$: it comes from the framework, because the flavour rotation must preserve the norm on $\mathcal{F}$, and it says nothing about which $V$. The companion articles write the same placement with the unit on the algebra factor, which states that the algebra factor is untouched; that is what the product with the number $V_{ab}$ says here. The gauge sector does not select the pattern.

**Why the mixing is a basis change.** The CKM matrix is a change of basis in flavour space, not a new interaction. In the framework this is transparent: the gauge interactions are the unit on the labels times the algebra's generator, so they are **generation-universal**, and the mixing arises only because the mass operators, which multiply by a number on the label and leave the element alone, are not diagonal in the same flavour basis. The framework's gauge sector is flavour-blind; the flavour structure is created by the mass operators. This is the algebraic form of the Glashow–Iliopoulos–Maiani mechanism: flavour-changing neutral currents are absent because the gauge vertex is the unit on the labels.

**The lepton sector, in parallel.** The same structure applies to the leptons, with the mixing matrix of the lepton sector playing the role of $V$ and the neutrino mass operators replacing the up-type quarks. The framework's structure on the labels is identical; the values differ because the mass matrices differ, and the two mixings are independent inputs. The companion article on the neutrino treats the lepton mixing; this article treats the quark sector and the framework features common to both.

## The Parameter Count and the CP Phase

**Counting the parameters.** A general $N_g\times N_g$ $*$-unitary matrix has $N_g^2$ real parameters. Of these, $N_g$ are removed by rephasing the $N_g$ up-type quarks and $N_g$ by rephasing the $N_g$ down-type quarks, except that one overall phase is unobservable, leaving

$$
\boxed{\;N_g^2-2N_g+1=(N_g-1)^2\;}
$$

physical parameters. They divide into

$$
\frac{N_g(N_g-1)}{2}\ \text{rotation angles},
\qquad
\frac{(N_g-1)(N_g-2)}{2}\ \text{CP-violating phases},
$$

the split of the $N_g^2$ coordinates of $\mathrm{U}(N_g)$ into the $\frac{N_g(N_g-1)}{2}$ angles of its $\mathrm{SO}(N_g)$ subgroup and the remaining $N_g(N_g+1)/2$ phases, of which the $2N_g-1$ rephasings remove all but $(N_g-1)(N_g-2)/2$. For $N_g=1$ there is nothing; for $N_g=2$ there is one angle and **no phase**; for $N_g=3$ there are three angles and **one phase**. The existence of a CP-violating phase in the quark sector therefore requires at least three generations, which is the content of the Kobayashi–Maskawa observation.

**The phase and CP violation.** The single phase of the three-generation CKM matrix is the source of CP violation in the quark sector. It appears in the charged-current interactions through the complex entries of $V$ and produces observable CP-violating asymmetries in meson decays and mixing. The phase is not by itself observable: the individual phases of the $V_{ij}$ change under a redefinition of the quark fields, and only the **rephasing-invariant combinations** — of which the Jarlskog invariant is the simplest — are unchanged. It is those combinations that the observables measure.

**Where the framework stands on the count.** The count $(N_g-1)^2$ is a property of the $*$-unitary group of the flavour factor, $\mathrm{U}(N_g)$, and the framework supplies that group as the norm-preserving group of the multiplicity factor. The framework therefore supplies the **arena** of the counting: the parameters are the coordinates of $\mathrm{U}(N_g)$, the angles and phases are its directions, and the CP phase is one of them. It does not supply a principle that fixes which point of $\mathrm{U}(N_g)$ the world occupies; that point is the measured CKM matrix.

## Why the CP Phase Is Not Central

**The centre acts on all generations alike.** The companion article on the number of generations establishes that the algebra acting on the $N_g$ fields is $\mathbb{B}\otimes M_{N_g}(\mathbb{C})\cong M_{2N_g}(\mathbb{C})$ and that its centre is $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}\cong\mathbb{C}$: a **single** central phase, acting on every generation with the same phase. A phase that distinguishes one generation from another — which is what a flavour-mixing phase does — cannot sit in the centre. It must sit in the flavour factor, the factor $M_{N_g}(\mathbb{C})$ of that algebra.

**The consequence for the CKM phase.** The CKM phase is therefore a **flavour-factor** phase: it is an entry of the $*$-unitary matrix on $\mathcal{F}$, and its CP-odd character is a property of that matrix, not of the algebra's central structure. This is a structural statement of the framework and one of its few definite contributions to the flavour sector: the algebra's centre is generation-blind, so the framework's own central phases — the vector phase and the volume element — are CP-even in the flavour sense, and the observed CP violation must be carried by the flavour factor. The companion article on the electric dipole moment draws the consequence: the CP-odd phase that the EDM would measure sits on the same factor, and the framework's algebra supplies no phase of its own.

**A contrast with the Dirac phase.** In the one-generation case the phase of the mass is unobservable: a rotation of the field that multiplies its $L$ part and its $R$ part by conjugate phases multiplies $m$ by a phase and leaves the kinetic term unchanged. That freedom is a redefinition of the field, not a central phase of the algebra — the central phase multiplies the field by a complex number and the adjoint by its conjugate, so the bilinear is unchanged — and it is generation-blind in any case. With $N_g$ generations the flavour rephasings are $N_g$ per quark type, $2N_g$ in all, and one overall phase is unobservable; what survives is the relative phase of the two diagonalisations, which no such rephasing can absorb. It exists precisely because the multiplicity factor is non-trivial. This is the algebraic version of the standard counting.

**The reality of the phase's location.** The framework thus makes a definite negative statement about where CP violation can come from: not from its algebra, its centre, or its real structure, all of which are generation-blind or generation-diagonal, but from the flavour factor. Any CP violation in the quark sector is a statement about the matrix on $\mathbb{C}^{N_g}$, and the framework hosts it without producing it.

## The Mass Matrices and the Origin of the Mixing

**The diagonalisation.** The mixing matrix arises from the mismatch between the up- and down-type mass matrices. In the framework a mass term multiplies the field by a central number, and with generations the number becomes a matrix on the labels: the mass operator leaves the element alone and mixes the generations,

$$
\psi_{\mathrm u,b}\longmapsto\sum_a M^{\mathcal{F}}_{u,ab}\,\psi_{\mathrm u,a},
\qquad
\psi_{\mathrm d,b}\longmapsto\sum_a M^{\mathcal{F}}_{d,ab}\,\psi_{\mathrm d,a},
$$

with the algebra factor common to the two types. The matrices $M_u^{\mathcal{F}},M_d^{\mathcal{F}}$ are general complex $N_g\times N_g$ matrices, so each factorises as $M^{\mathcal{F}}=XDY^\dagger$ with $X,Y$ unitary and $D$ diagonal and positive. The arrays of this article are the operators on $\mathcal{F}$ — the mass operators, $V$, and the Hermitian products below — because $\mathcal{F}$ is a complex vector space and no element of $\mathbb{B}$ stands behind them. The mixing depends on the left-handed unitaries alone, and the CP invariant on those and the masses, through the Hermitian products

$$
H_u=M_u^{\mathcal{F}}M_u^{\mathcal{F}\dagger}=X_uD_u^2X_u^\dagger,\qquad
H_d=M_d^{\mathcal{F}}M_d^{\mathcal{F}\dagger}=X_dD_d^2X_d^\dagger,\qquad
V=X_u^\dagger X_d ,
$$

with $D_u=\mathrm{diag}(m_u,m_c,m_t)$ and $D_d=\mathrm{diag}(m_d,m_s,m_b)$. The right-handed unitaries $Y_u,Y_d$ drop out of $V$, which is why two sets of masses and one relative rotation carry the information. The mixing is a measure of how differently the two Hermitian products are diagonalised, and it vanishes, $V=I$, when $X_u=X_d$; the eigenvalues of $H_u,H_d$ are the squared quark masses. The algebra factor is common to both, which is why the two diagonalisations are on the same label space and why the relative rotation is meaningful.

**The invariant content.** The two Hermitian products carry exactly the information of the six masses and of the mixing, up to the ordering of the eigenvalues. The framework's statement is that all of this information lives on $\mathcal{F}$, that the algebra factor contributes nothing to it, and that the gauge sector's flavour-universality is what makes the mixing observable in the charged current and not in the neutral current. This is the algebraic content of the GIM mechanism and it is exact in the framework.

**The absence of a dynamics.** The framework has no equation from which $M_u^{\mathcal{F}}$ or $M_d^{\mathcal{F}}$ follows. In a flavour model the matrices would be generated by a symmetry and its breaking, by a radiative mechanism, or by a higher-dimensional construction; the framework contains none of these, and its role is to state where the matrices sit and what they must respect. The companion article on the number of generations makes the analogous statement for the hierarchy of the eigenvalues; the present article makes it for the mixing.

## The Jarlskog Invariant and the Condition for CP Violation

**The rephasing invariant.** Because the individual phases of the CKM matrix are convention-dependent, CP violation is measured by rephasing-invariant combinations. The simplest one is the **Jarlskog invariant**,

$$
\boxed{\;\begin{aligned}
J &= \mathrm{Im}\big(V_{ud}V_{cs}V_{us}^{*}V_{cd}^{*}\big)\\
&= c_{12}\,c_{23}\,c_{13}^{2}\,s_{12}\,s_{23}\,s_{13}\,\sin\delta ,
\end{aligned}\;}
$$

where the second form uses the standard three-angle parametrisation with the phase $\delta$, and $c_{ij}=\cos\theta_{ij}$, $s_{ij}=\sin\theta_{ij}$. The invariant is the imaginary part of a quartet of matrix elements, and it vanishes if and only if the theory is CP-conserving with three generations. The same number is the imaginary part of the determinant of the commutator of the two Hermitian mass products, normalised by the six mass-squared differences:

$$
\boxed{\;J=\frac{\operatorname{Im}\det\big([H_u,H_d]\big)}
{2\prod_{i<j}\big(m_{ui}^{2}-m_{uj}^{2}\big)\big(m_{di}^{2}-m_{dj}^{2}\big)}\;}
$$

with $[H_u,H_d]=H_uH_d-H_dH_u$ and $H_u=M_u^{\mathcal{F}}M_u^{\mathcal{F}\dagger}$, $H_d=M_d^{\mathcal{F}}M_d^{\mathcal{F}\dagger}$. The product runs over the three up-type pairs and the three down-type pairs. Determinant and product change sign together when two masses are relabelled, so the ratio is labelling-independent; the overall sign is fixed by the quartet definition, and the identity was checked numerically with the measured masses and the measured $V$. **CP violation for three generations is the noncommutativity of the two mass-matrix products, measured by the Jarlskog invariant.**

**The values, recomputed.** With $\lambda=0.22500$, $A=0.826$, $\bar\rho=0.159$ and $\bar\eta=0.348$, the matrix reconstructed from the exact three-angle parametrisation satisfies

$$
\max\big|VV^\dagger-I_3\big| = 2.2\times10^{-16},
\qquad
J = 3.00\times10^{-5},
$$

so unitarity holds to machine precision, and the invariant agrees with the quoted $J\simeq3.1\times10^{-5}$ to the rounding of the four inputs. The magnitudes come out $|V_{ud}|\simeq0.974$, $|V_{us}|\simeq0.225$, $|V_{ub}|\simeq0.004$, $|V_{cb}|\simeq0.042$, $|V_{td}|\simeq0.009$, $|V_{tb}|\simeq0.999$. The leading-order Wolfenstein form $A^2\lambda^6\bar\eta$ gives $3.08\times10^{-5}$ at the same inputs; the exact invariant carries in addition the prefactor $c_{12}c_{23}c_{13}^{2}=1-\tfrac12(\lambda^2+A^2\lambda^4+\cdots)\simeq0.974$, which the truncated form omits, so the exact value lies about three per cent below the truncated one. The reconstruction used the exact three-angle parametrisation, because the truncated Wolfenstein form is $*$-unitary only to the order of the truncation and $J$ needs the untruncated phase structure.

**Why the commutator is the invariant.** The commutator of the mass matrices is the algebraic expression of the fact that CP violation requires two non-commuting matrices with a complex phase. If $H_u=M_u^{\mathcal{F}}M_u^{\mathcal{F}\dagger}$ and $H_d=M_d^{\mathcal{F}}M_d^{\mathcal{F}\dagger}$ commuted, they could be diagonalised simultaneously and the mixing matrix would be a permutation of phases — no CP violation. The determinant of the commutator is the simplest invariant of the two matrices that vanishes when they commute and changes sign when they are exchanged; its imaginary part is the Jarlskog invariant, up to the normalisation by the six mass-squared differences. In the framework the commutator is an operator on the labels alone, $[H_u^{\mathcal{F}},H_d^{\mathcal{F}}]$, and its nonvanishing is the statement that the two mass operators are misaligned in a CP-violating way.

## The Wolfenstein Parametrisation, the Unitarity Triangle, and the Data

**The Wolfenstein parametrisation.** The empirical pattern of the CKM matrix — nearly diagonal, with a small mixing — is captured by the expansion in $\lambda=\sin\theta_C\simeq0.225$, the Cabibbo angle. To order $\lambda^3$ the entries are

| entries | their value to $O(\lambda^3)$ |
|---|---|
| $V_{ud}$, $V_{cs}$ | $1-\tfrac12\lambda^2$ |
| $V_{tb}$ | $1$ |
| $V_{us}$ | $\lambda$ |
| $V_{cd}$ | $-\lambda$ |
| $V_{cb}$ | $A\lambda^2$ |
| $V_{ts}$ | $-A\lambda^2$ |
| $V_{ub}$ | $A\lambda^3(\bar\rho-i\bar\eta)$ |
| $V_{td}$ | $A\lambda^3(1-\bar\rho-i\bar\eta)$ |

with $A\simeq0.826$, $\bar\rho\simeq0.159$ and $\bar\eta\simeq0.348$. The two corners carry the barred pair, which is the standard placement at this order. The CP-violating parameter is the imaginary part $\bar\eta$. To this order the phase of the standard parametrisation is $\delta=\arctan(\bar\eta/\bar\rho)$, and the single CP-odd combination is the product $A^2\lambda^6\bar\eta$, which is the Jarlskog invariant at leading order. The hierarchy of the entries — the powers of $\lambda$ — is the observed structure; the framework supplies no reason for it.

**The unitarity triangle.** The orthogonality of the first and third columns of $V$ defines a triangle in the complex plane; rescaled by one of its sides it has vertices $(0,0)$, $(1,0)$ and $(\bar\rho,\bar\eta)$. The barred pair is the one the data are quoted in; it is related to the unbarred pair by $\bar\rho=\rho(1-\lambda^2/2+\cdots)$ and $\bar\eta=\eta(1-\lambda^2/2+\cdots)$. Its angles

$$
\alpha,\ \beta,\ \gamma
\qquad\text{with}\qquad
\sin2\beta = \frac{2(1-\bar\rho)\bar\eta}{(1-\bar\rho)^2+\bar\eta^2},\qquad
\gamma=\arctan\frac{\bar\eta}{\bar\rho},
$$

are measured by CP-violating asymmetries in $B$ decays; the kaon system measures the same invariant through $\epsilon_K$. With the standard parameters the recomputation gives

$$
\sin2\beta = 0.707,\qquad \beta\simeq22.5^\circ,\qquad \gamma\simeq65.4^\circ,\qquad
\alpha = 180^\circ-\beta-\gamma\simeq92^\circ,
$$

in agreement with the measured values. The triangle closes as a consequence of unitarity, and the closure is the statement that the three-generation mixing matrix is a point of $\mathrm{U}(3)$ — the framework's requirement on the flavour factor; the numerical closure is a property of the measured matrix.

**The measured entries and the one phase.** The magnitudes and the phase are measured to good precision, and the data are consistent with a single unitarity triangle. The framework's role is exhausted by the structure: it supplies the group $\mathrm{U}(N_g)$, the placement on the generation label, the non-centrality of the phase, and the counting; the numerical values are inputs. This is the flavour-sector analogue of the framework's position on the mass matrices and on the generation number, and the article states it without further claim.

**The CP-odd observables.** The invariant $J$ controls the CP-violating observables: the kaon parameter $\epsilon_K$, the $B$-decay asymmetries proportional to $\sin2\beta$, and the direct CP asymmetries. All are proportional to $J$ times products of hadronic matrix elements, and the consistency of the measurements with a single $J$ is the Standard Model's success in the flavour sector. The framework inherits the observables and the success; it adds the algebraic placement.

## The Jarlskog Area and the Six Triangles

**The triangles from unitarity.** The section above used one orthogonality relation of $V$, that of the first and third columns, already rescaled to the $(\bar\rho,\bar\eta)$ triangle. Unitarity gives six such relations — three from the columns and three from the rows — each of the form $V_{ij}V_{ik}^{*}+V_{lj}V_{lk}^{*}+V_{nj}V_{nk}^{*}=0$, and each defines a triangle in the complex plane. The unscaled sides of the one above are

$$
V_{ud}V_{ub}^{*}+V_{cd}V_{cb}^{*}+V_{td}V_{tb}^{*}=0 ,
$$

and the recomputation with the standard parameters confirmed that the three terms sum to zero to machine precision and that the triangle's area is

$$
A_{\triangle} = \tfrac12\,|J| = 1.499\times10^{-5}.
$$

The relation **area $=\tfrac12|J|$** is the geometric statement of the CP-violating invariant, and the computed area agreed with it to machine precision for all six triangles.

**The rescaled triangle.** Dividing the relation by the complex term $V_{cd}V_{cb}^{*}$, not by its modulus, sends that vertex to $1$ and brings the triangle to the standard form with vertices $(0,0)$, $(1,0)$, $(\bar\rho,\bar\eta)$ and angles $\alpha,\beta,\gamma$. Dividing by the modulus instead would leave a rotation of the whole triangle and move the apex off $(\bar\rho,\bar\eta)$. In the rescaled coordinates the area is $\bar\eta/2$, and the two areas are related by the squared side, $|V_{cd}V_{cb}^{*}|^{2}=A^{2}\lambda^{6}$. The framework's content is the closure: the sides are products of entries of a **$*$-unitary** matrix on the flavour factor, and unitarity is exactly the framework's requirement that the flavour rotation preserve the norm on $\mathcal{F}$. The closure of the triangle is the statement that $V$ is a point of $\mathrm{U}(N_g)$, and the nonzero area is the statement that the point is not real.

**The number of triangles and the number of phases.** The $\binom{N_g}{2}$ column pairs give as many triangles, the rows give as many again, and all of them have area $|J|/2$; for $N_g=3$ that is six triangles. The number of triangles is not the number of CP phases: for $N_g=3$ there are six triangles and one phase, and for $N_g=2$ the two triangles are degenerate and there is no phase. The equality of the six areas is a consistency condition of unitarity, not an independent input; the framework supplies the $*$-unitary structure, and the equality is a theorem of the group.

## CP Violation in the Lepton Sector

**The parallel structure.** The lepton sector has the same framework structure as the quark sector: a mixing operator $X_{\mathrm{PMNS}}=X_e^\dagger X_\nu$ on the labels, diagonalising the charged-lepton and neutrino mass operators, with the same placement and the same untouched algebra factor. The matrix is $*$-unitary and, for three generations, carries one CP-violating phase $\delta_{\mathrm{CP}}$ (and possibly two Majorana phases, which do not affect neutrino oscillations). The companion article on the neutrino and the seesaw article supply the neutrino mass matrices; this section records the parallel.

**The leptonic Jarlskog invariant.** The leptonic analogue of $J$ is

$$
J_{\mathrm{CP}} = \mathrm{Im}\big(X_{e1}X_{\mu2}X_{e2}^{*}X_{\mu1}^{*}\big)
= c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta_{\mathrm{CP}} ,
$$

the same expression with the leptonic angles and phase. The framework's structure is identical, and the two invariants are independent inputs. The experimental situation is the standard one: the leptonic angles are measured with the atmospheric and solar values, the phase is constrained but not yet precisely fixed, and the discovery of leptonic CP violation is a goal of the long-baseline experiments.

**The Majorana phases and the difference.** The leptonic sector differs from the quark sector in one framework-relevant way. If the neutrinos are Majorana, the mass matrix is symmetric and is diagonalised by a single unitary, $M_\nu=U^{*}DU^{\dagger}$, and two additional rephasing-invariant phases — the Majorana phases — survive; they do not affect neutrino oscillations. They are absent in the quark sector because the quark mass matrices are general complex matrices, whose diagonalisation uses two unitaries. The difference is a property of the flavour factor's reality structure, which the companion article on the neutrino treats. The article's structural point is that both sectors share the placement on the label, the unitarity, and the non-centrality of their CP phases, and that the framework supplies the structure and not the values.

## The Running of the CKM Parameters

**Scale dependence.** The CKM parameters, like the quark masses, are scale-dependent: the mass matrices acquire radiative corrections and the mixing angles and phase run with the renormalisation scale. The running is governed by the anomalous dimensions of the quark bilinears and is quantitatively important only at high scales; the framework inherits it, and the framework's own parameters — the algebra, its sectors, the trace — do not run, because they are finite-dimensional algebraic data. The statement is the same as elsewhere in the framework: the algebraic structure is scale-independent, and the flavour-factor data run.

**The framework's contribution to the running.** The framework's one-generation quantities — the mass term and its chiral structure — run with the standard anomalous dimensions of a Dirac fermion, and the companion article on the Dirac field records the free theory. The flavour-factor running is a matrix generalisation, and it does not involve the algebra. In the language of the article, the running multiplies the mass operators by a scale-dependent operator $Z(\mu)$ on the labels and rotates them; the mixing matrix runs because the rotations of the up and down sectors run differently. The framework hosts the running on the flavour factor, as it hosts everything else in the flavour sector.

## CP Violation and the Baryon Asymmetry

**The CKM phase is too small.** The observed baryon asymmetry of the universe requires CP violation beyond the Standard Model's CKM phase: the Jarlskog invariant $J\simeq3\times10^{-5}$ is far too small to generate the asymmetry through electroweak baryogenesis, and the electroweak phase transition in the Standard Model is not strongly first order. The framework inherits this quantitative statement and adds the structural one: the CKM phase is a flavour-factor phase (the previous sections), so any additional CP violation needed for baryogenesis must also live on the flavour factor or in new physics outside the framework's algebra.

**Where the framework leaves the question.** The framework's centre is generation-blind and CP-even in the flavour sense, and its algebra supplies no CP-odd invariant. A baryogenesis mechanism would therefore have to be an additional structure — new phases on the flavour factor, new particles, or a departure from the framework's present spectrum — and the framework neither supplies nor excludes it. The article records the electroweak-baryogenesis requirement as the standard motivation for CP violation beyond the CKM phase, with the framework's structural statement attached.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The CKM matrix as an operator on the generation label | **Supplied**; the algebra factor untouched |
| Gauge-sector flavour universality and the GIM mechanism | **Supplied**; the gauge vertex is the unit in flavour space |
| The count $(N_g-1)^2$, and $N_g\ge3$ for a CP phase | **Supplied** by the $*$-unitary group of the flavour factor; standard counting |
| The non-centrality of the CP phase | **Supplied**; the centre is $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}$ and acts on all generations alike |
| The Jarlskog invariant as a flavour-factor commutator | **Supplied** in form; standard in content |
| The mass-matrix origin of the mixing, $V=X_u^\dagger X_d$ | **Transcribed**; standard |
| The Wolfenstein parametrisation and the unitarity triangle | **Transcribed**; standard |
| The measured values of the angles, phase, and $J$ | **Transcribed**; standard, with unitarity and $J$ recomputed |
| The values of the CKM parameters, and the mass matrices | **Not supplied**; empirical |
| A flavour dynamics or symmetry that generates the pattern | **Not supplied**; the flavour factor is arbitrary |
| The relation of the quark mixing to the lepton mixing | **Not supplied**; they are independent inputs |

## Open Questions

1. **A flavour principle.** Whether a symmetry or a dynamics on the flavour factor can be formulated within the framework — a discrete family group, a radiative mechanism, or a structure on $\mathbb{C}^{N_g}$ — is open. The framework can host such a mechanism; it does not contain one.

2. **The phase's seat.** The article states that the CP phase must sit on the generation label because the centre is generation-blind. Whether the framework can say anything more — for instance whether a flavour-factor phase can be related to the real structure $\flat$ or to the central $i$ — is not settled.

3. **The quark–lepton connection.** In grand-unified extensions the quark and lepton mass matrices are related and the two mixing matrices are correlated. The framework has no unified structure, so it treats them as independent; whether a biquaternion unification can relate them is outside this article.

4. **The strong CP problem.** The CKM phase is not the only CP-odd parameter; the $\theta$ parameter is another, and its smallness is the strong CP problem. The $\theta$ parameter belongs to the corpus's general gauge apparatus; the fermion-sector statement is that the two phases are independent inputs in the framework.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The body of the article is written in elements: a generator is the action $X\mapsto ie_\mu X\vec e_{\nu(\mu)}$, the field carries the label $L$ or $R$, and the mixing is the number $V_{ab}$. The older literature writes the same five generators as arrays, and they are collected here — with the cells that display them — so that a reader who comes from the matrix literature can translate; they enter nowhere else in the article. The letter $\gamma$ of the unitarity triangle, in the section on the Wolfenstein parametrisation, is the triangle's angle and has nothing to do with $\gamma_\mu$.

**The frame and the signs.** The names below are the $\mathbb{M}_-$ frame, $\varepsilon=(1,-1,-1,-1)$, with the index low and $\epsilon_{0123}=+1$. The generator cell of the coordinate $x_\mu$ is $\gamma_\mu$, and $\gamma_5$ is the chirality cell:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The generator of the charged current of this article is $\gamma_\mu$ in these names, and the label $L$ of the body is what the older notation writes with the projector $P_L$; that projector is a named object of the older notation, and it needs no formula here.

**The squares.** Every square is a cell square, with $L_aR_bL_cR_d=L_{ac}R_{db}$, and the only sources of a sign are $i^2=-1$ and the squares of the imaginary units, $\vec e_k^2=-e_t$ and $e_t^2=e_t$:

$$
\gamma_5^2=(-i)^2L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=(-1)L_{e_t}^{\mathrm{pau}}R_{\vec e_z^2}^{\mathrm{pau}}=(-1)(-I_4)=I_4,
$$

The same identities in the axis-free display:

$$
\gamma_5^2=(-i)^2L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=(-1)L_{e_t}^{\mathrm{axf}}R_{\vec e_z^2}^{\mathrm{axf}}=(-1)(-I_4)=I_4,
$$

$$
\gamma_0^2=i^2L_{e_t^2}^{\mathrm{pau}}R_{\vec e_x^2}^{\mathrm{pau}}=(-1)L_{e_t}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=(-1)(-I_4)=I_4,\qquad
\gamma_k^2=i^2L_{\vec e_k^2}^{\mathrm{pau}}R_{\vec e_y^2}^{\mathrm{pau}}=(-1)(+I_4)=-I_4 ,
$$

Read in the axis-free display:

$$
\gamma_0^2=i^2L_{e_t^2}^{\mathrm{axf}}R_{\vec e_x^2}^{\mathrm{axf}}=(-1)L_{e_t}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=(-1)(-I_4)=I_4,\qquad
\gamma_k^2=i^2L_{\vec e_k^2}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=(-1)(+I_4)=-I_4 ,
$$

so a square spends $i^2=-1$ once, and it spends one quaternion square for $\gamma_0$ against two for $\gamma_k$: two minus signs give $(\gamma_0)^2=+I_4$, three give $(\gamma_k)^2=-I_4$.

**The fifth generator and the central sign.** $\gamma_5$ is the older notation's name for the fifth generator, the one it calls the chirality cell, and the label $L$ of the body is its minus part. The abstract central sign of the complexified algebra, $\chi=i\tilde\Xi_{\mathrm{ad}}$ of *Special Element Conventions*, §*The Root Convention*, is a different object; its representative on the array is $\gamma_5$.

**The identities.** In the frame declared above, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0 ,
\qquad \varepsilon=(1,-1,-1,-1),$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d] .
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

**The four contraction sums.** With the index $\mu$ summed over the frame and the summed index raised by $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, they are, for $A$ a product of $n$ distinct generators,

$$
\sum_\mu\gamma^\mu\gamma_\mu=-4I_4,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha,\qquad
\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4,
\qquad
\sum_\mu\gamma^\mu A\gamma_\mu=(-1)^{n+1}(4-2n)A .
$$

The metric sits in the raised index and nowhere else. With every index low the same sums read $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, $\sum_\mu\gamma_\mu\gamma_0\gamma_\mu=+4\gamma_0$, and the spatial sums vanish, $\sum_\mu\gamma_\mu\gamma_k\gamma_\mu=0$.

**Closure.** The sixteen products — $I_4$, the four $\gamma_\mu$, the six $\gamma_\mu\gamma_\nu$ with $\mu<\nu$, the four $\gamma_5\gamma_\mu$ and $\gamma_5$ — are a basis of $M_4(\mathbb{C})=\mathrm{Cl}_{1,3}(\mathbb{C})$, so no product of gammas leaves the algebra and the dictionary closes. The real algebras are smaller. The sixteen cells $L_aR_b$, whose product is again a cell, span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ over $\mathbb{R}$; the products of the gammas alone span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$. Both are sixteen-dimensional, and both complexify to $M_4(\mathbb{C})$. The chirality cell is not among the products with real coefficients:

$$
\gamma_5=i\,\gamma_0\gamma_1\gamma_2\gamma_3 ,
$$

so it enters with the central $i$, and the real algebra generated by the four $\gamma_\mu$ does not contain it. The chirality grading is the one place where the dictionary needs more than the four gammas.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The CKM matrix is a $*$-unitary operator on the framework's generation factor, multiplying the label and leaving the algebra factor untouched, and arising from the mismatch of the up- and down-type mass operators, $V=X_u^\dagger X_d$, both of which act on the labels while the algebra factor is common. The framework's gauge sector is flavour-universal, which is the algebraic form of the GIM mechanism: the charged-current term is the generator $X\mapsto ie_\mu X\vec e_{\nu(\mu)}$ read with the label $L$ and multiplied by the number $V_{ab}$, and the neutral currents are the unit on the labels and are flavour-diagonal. The parameter count is that of $\mathrm{U}(N_g)$: $(N_g-1)^2$ parameters, comprising $\tfrac12N_g(N_g-1)$ angles and $\tfrac12(N_g-1)(N_g-2)$ phases, so that a CP-violating phase requires $N_g\ge3$.

The framework's definite structural contribution is the location of the phase. The algebra acting on the multi-generation space is $\mathbb{B}\otimes M_{N_g}(\mathbb{C})$ with centre $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}\cong\mathbb{C}$, a single generation-blind central phase; a phase that distinguishes generations therefore cannot be central and must sit in the flavour factor, the factor $M_{N_g}(\mathbb{C})$ of that algebra. The framework's own central phases are CP-even in the flavour sense, and all quark-sector CP violation is a statement about the matrix on $\mathbb{C}^{N_g}$. The Jarlskog invariant, $J=\mathrm{Im}(V_{ud}V_{cs}V_{us}^{*}V_{cd}^{*})=c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta$, is the minimal rephasing-invariant measure of the CP violation and is the imaginary part of the determinant of the commutator of the two mass-matrix products, normalised by the six mass-squared differences; the recomputation with the standard parameters gave $J=3.00\times10^{-5}$, consistent with the quoted $3.1\times10^{-5}$ to the rounding of the inputs, with unitarity of the reconstructed matrix to machine precision, $\sin2\beta=0.707$, $\beta\simeq22.5^\circ$, and $\gamma\simeq65.4^\circ$. The framework places all of this on the flavour factor and supplies none of the values.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{C}_{\mathbb{B}}$ | Material sector (the frame of the closing section); centre |
| $\psi_{t,a}\in\mathbb{B}$ | The field of type $t$ and generation $a$; an element of the algebra |
| $X\mapsto ie_\mu X\vec e_{\nu(\mu)}$ | The generator of the coordinate $x_\mu$, written as the action it is |
| $\psi_L$, $\psi_R$ | The two parts of an element, by the label $L$ or $R$ |
| $\gamma_\mu$, $\gamma_5$ | The generators under their older names (closing section only) |
| $\mathcal{F}=\mathbb{C}^{N_g}$ | Generation (multiplicity) factor |
| $V\in \mathrm{U}(N_g)$, $V_{ab}$ | The CKM matrix, multiplying the generation label |
| $M_u^{\mathcal{F}},M_d^{\mathcal{F}}$ | Up- and down-type mass matrices on $\mathcal{F}$ |
| $H_u=M_u^{\mathcal{F}}M_u^{\mathcal{F}\dagger}$, $H_d=M_d^{\mathcal{F}}M_d^{\mathcal{F}\dagger}$ | Hermitian mass products; their eigenvalues are the squared masses |
| $V=X_u^\dagger X_d$ | CKM matrix from the diagonalisations |
| $\psi_{\mathrm u,a}$, $\psi_{\mathrm d,b}$; $\psi^{\dagger}$, with the factor $i\vec e_x$ | Up- and down-type quark fields, generation labels $a,b$; Dirac adjoint |
| $\psi^{\dagger}i(ie_\mu\psi_L\vec e_{\nu(\mu)})\vec e_x\,V_{ab}$ | The charged-current term |
| the unit on the labels | Gauge vertices; flavour universality (GIM) |
| $\mathbb{C}_{\mathbb{B}}\otimes I_{N_g}$ | Centre of the multiplied algebra; generation-blind |
| $\tfrac12N_g(N_g-1)$, $\tfrac12(N_g-1)(N_g-2)$ | Mixing angles; CP-violating phases |
| $J=\mathrm{Im}(V_{ud}V_{cs}V_{us}^{*}V_{cd}^{*})$ | Jarlskog invariant |
| $J=c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta$ | Jarlskog invariant, three-angle form |
| $\lambda,A,\bar\rho,\bar\eta$ | Wolfenstein parameters (barred values) |
| $\alpha,\beta,\gamma$ | Unitarity-triangle angles |
| $A_\triangle=\tfrac12|J|$ | Unitarity-triangle area |
| $X_{\mathrm{PMNS}}$, $\delta_{\mathrm{CP}}$, $J_{\mathrm{CP}}$ | Leptonic mixing matrix, phase, invariant |
| $J=3.00\times10^{-5}$; $A^2\lambda^6\bar\eta=3.08\times10^{-5}$ | Recomputed invariant; its leading-order form |
| $\sin2\beta=0.707$, $\gamma\simeq65.4^\circ$ | Recomputed CP observables |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
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
