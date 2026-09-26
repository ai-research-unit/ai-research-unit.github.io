# __Anomalies and Anomaly Cancellation in Biquaternionic Form__

## Introduction

An **anomaly** is a symmetry of a classical action that does not survive quantisation. The classical current is conserved by the equations of motion; the one-loop diagram that computes its divergence is not zero; and the discrepancy is not a calculational artefact but an exact, finite, one-loop effect that is not renormalised — the Adler–Bardeen theorem. Two anomalies matter for particle physics, and they play opposite roles.

- The **axial (Adler–Bell–Jackiw) anomaly** breaks a *global* symmetry that the classical theory has. It is physical: it is what makes the neutral pion decay to two photons and what makes the axial $U(1)$ of quantum chromodynamics not a symmetry of the quantum theory.
- The **gauge anomaly** threatens a *local* symmetry. If the triangle diagram with three gauge currents does not vanish, the gauge theory is inconsistent: the current is not conserved, the longitudinal gauge modes do not decouple, and unitarity and renormalisability fail. A chiral gauge theory is therefore consistent only if the anomaly cancels, and the cancellation is a **condition on the matter spectrum**.

This article treats both in the biquaternion framework. The framework's contribution is structural and is stated at the outset.

- **Established, and recomputed below.** The axial anomaly is the failure of the chiral rotation $\tilde{\Psi}\mapsto e^{i\alpha\gamma_5}\tilde{\Psi}$ to be a symmetry of the measure. Its density is built from $\gamma_5$, which the Clifford isomorphism identifies with the volume element, $\gamma_5=i\omega$, and it is proportional to the **second invariant** $I_2=\mathbf{E}\cdot\mathbf{B}$ of the biquaternion field — the topological density computed in the companion article on instantons. The anomaly is therefore not foreign to the framework: its density is one of the framework's two field invariants.
- **Established, and recomputed below.** The anomaly coefficient of a gauge theory is the symmetrised trace $\mathrm{Tr}\,[T^a\{T^b,T^c\}]$ over the left-handed Weyl fermions. The framework's **own** gauge structure — the central $U(1)$ and the $\mathfrak{su}(2)$ inside $\mathbb{M}_-$ — is anomaly-free: the central phase is vector-like, so its cubic trace cancels identically, and $\mathfrak{su}(2)$ has no cubic Casimir, so its triangle coefficient vanishes identically. The framework cannot be inconsistent by a gauge anomaly of the algebra's own gauge fields.
- **Standard, transcribed.** The anomaly cancellation conditions of the Standard Model's chiral spectrum — $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$, and the colour conditions — are standard, and the article verifies all of them generation by generation. They constrain the hypercharges and the colour assignments; they do not constrain the **number** of generations.
- **Gap, left visible.** The framework has no chiral gauge group of its own — the central phase is vector-like and the $\mathfrak{su}(2)$ acts vector-like on the algebra's module — so it cannot *derive* the Standard Model's chiral spectrum from which the cancellation conditions are read. It transcribes the conditions and hosts their solution; it does not select it.

The article is organised as follows. A section states the anomaly as a quantum failure of a classical symmetry. A section gives the axial anomaly and its biquaternion density. A section sets out the triangle coefficient and computes the group factors. A section states the gauge cancellation conditions and verifies them on the Standard Model spectrum. A section proves the framework's own gauge structure anomaly-free. A closing section separates what is supplied, transcribed, and missing.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material), with basis $ie_0,e_1,e_2,e_3$, and $\mathbb{M}_+$ (Hermitian, informational), with basis $e_0,ie_1,ie_2,ie_3$; the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$. The Dirac module is $\Delta=S\oplus\bar{S}$, $S=\mathbb{C}^2$, with $\gamma_5=\mathrm{diag}(-I_2,I_2)$, projectors $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$, and block representation

$$
\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad
\gamma^k=\begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},\qquad
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\qquad g=\mathrm{diag}(+1,-1,-1,-1),
$$

with $\gamma_5=i\omega$ and $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ the volume element. For the abelian anomaly we use the field strength $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, the totally antisymmetric symbol with $\epsilon^{0123}=+1$, and the components $F_{0i}=E_i$, $F_{ij}=-\epsilon_{ijk}B_k$; for the non-abelian factor we use $\mathcal{A}_\mu\in\mathfrak{su}(2)$ and $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$, with $\kappa=q/\hbar$. The biquaternion field invariants are $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, with $\mathbf{B}=\mu\mathbf{H}$, in the normalization of the instanton article. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; the symbols $SU(3)$, $SU(2)_L$, $U(1)_Y$, $Y$, $T_3$ are **standard-model notation, not framework objects**, used only where a standard structure is named.

The framework results used here are those of the companion articles:

- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological density and its identification with the invariant $I_2$.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength, the invariants $I_1$ and $I_2$, and the norm form.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral classification and the gauge quantum numbers of the left- and right-handed fields.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the multiplet structure whose charge sums are the cancellation conditions.

## The Classical Symmetry and its Quantum Failure

**The mechanism, stated once.** A classical symmetry has a conserved current, $\partial_\mu j^\mu=0$, by Noether's theorem. The quantum divergence is computed by inserting the current into a correlation function; at one loop the triangle diagram contributes, and the divergence receives a term that is finite as the regulator is removed. If that term is a total derivative of a topological density it cannot be removed by a local counterterm, and the symmetry is genuinely broken quantum-mechanically. This is the content of the Adler–Bardeen theorem: the anomaly is a one-loop effect and is exact.

**Two kinematic facts make the computation dimensional.** First, in four dimensions the relevant diagram is a triangle with one axial and two vector currents (the axial anomaly) or three vector currents (the gauge anomaly); higher-point diagrams do not add new anomalous terms. Second, the anomaly is a **trace** statement: the diagram's coefficient is a trace of products of gamma matrices times a trace of gauge generators, and each trace is computed once and for all.

**The biquaternion entry point.** The framework's contribution is the identity of the gamma-matrix trace that produces the anomaly. In the block basis of the Conventions the Clifford trace is

$$
\mathrm{tr}\big(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\big) = -4i\,\epsilon^{\mu\nu\rho\sigma},
\qquad
\mathrm{tr}\big(\gamma_5\gamma^0\gamma^1\gamma^2\gamma^3\big) = -4i ,
$$

which was recomputed for all $4!=24$ permutations: the trace vanishes unless the four indices are distinct, and then it is $-4i$ times the sign of the permutation, with $\epsilon^{0123}=+1$. Every anomaly coefficient in the article is this single number multiplied by the appropriate trace of gauge generators.

## The Axial Anomaly

**The result.** For a massless Dirac fermion of electric charge $e$ in four dimensions, the axial current $j_5^\mu=\bar{\psi}\gamma^\mu\gamma_5\psi$ satisfies

$$
\partial_\mu j_5^\mu \;=\; 2im\,\bar{\psi}\gamma_5\psi \;+\; \frac{e^2}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

with the conventions stated above. The first term is the classical explicit breaking by the mass; the second is the anomaly, present even at $m=0$. The coefficient is the standard Adler–Bell–Jackiw one and is quoted from the standard literature. With $F_{0i}=E_i$ and $F_{ij}=-\epsilon_{ijk}B_k$ the density evaluates to $\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=-8\,\mathbf{E}\cdot\mathbf{B}$, so the anomaly density is, up to the conventional factor, the second field invariant

$$
\mathcal{A}(x) \;\propto\; \mathbf{E}\cdot\mathbf{B} \;=\; I_2 .
$$

**The biquaternion form of the density.** The framework's field is the biquaternion

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H},
$$

whose two real invariants of the norm form are $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$; the companion article on instantons computes the topological density $(1/4)\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ and finds it proportional to $I_2$, with the factor of $i$ that the $ict$ convention carries in the time components. The anomalous divergence is therefore the divergence of the axial current into the framework's own pseudoscalar invariant. Two structural remarks follow. First, the density is a **pseudoscalar**: it is parity-odd, which is why it can appear on the right-hand side of the divergence of an axial (parity-odd) current. Second, it is a **total derivative** in the abelian case, $\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=2\,\partial_\mu K^\mu$ with $K^\mu$ the Chern–Simons current of the companion article on instantons, which is why it is not renormalised and why it is fixed by topology. Both statements are standard; what the framework adds is that the density is not an alien object but the second invariant of its own field, and that $\gamma_5=i\omega$ is the volume element.

**The physical consequence, stated and not developed.** The anomaly makes $\pi^0\to\gamma\gamma$ possible at the observed rate and makes the axial $U(1)$ of quantum chromodynamics explicitly broken at the quantum level; the $U(1)_A$ problem and its resolution by the $\theta$ parameter and the axion belong to the corpus's other subcategories and are not treated here. The point for the fermion sector is the divergence identity itself: the axial current of any single massless Dirac fermion is not conserved quantum-mechanically, and no choice of regulator removes the term without moving the breaking elsewhere.

**Why the anomaly is exact.** The Adler–Bardeen theorem states that the coefficient of the anomaly is the one-loop value, unaffected by higher-order corrections. The modern reason is that the anomaly is the index of the Dirac operator, an integer topological invariant; a divergence of a current cannot have a non-integer coefficient, so the one-loop value is protected. The index statement is the subject of the general gauge apparatus and of the companion article on the Fujikawa method; here it is noted as the reason the coefficient above is stable.

## The Triangle Coefficient and the Group Factors

**The general anomaly coefficient.** For a gauge theory with generators $T^a$ acting on a left-handed Weyl fermion in a representation $R$, the coefficient of the triangle anomaly is the **symmetrised trace**

$$
A^{abc}(R) \;=\; \mathrm{Tr}_R\big[T^a\{T^b,T^c\}\big] .
$$

The anomaly is the sum over all left-handed Weyl fermions, with a right-handed Weyl fermion contributing the negative of a left-handed one (equivalently, a right-handed field in $R$ contributes as a left-handed field in the conjugate $\bar{R}$). The consistency condition for a chiral gauge theory is

$$
\sum_{\text{left-handed}} A^{abc}(R) \;-\; \sum_{\text{right-handed}} A^{abc}(R) \;=\; 0
\qquad\text{for all } a,b,c .
$$

For an abelian factor this reduces to $\sum Y^3=0$ over the charged left-handed content (with the right-handed sign); for a simple factor it reduces to the vanishing of the appropriate cubic Casimir. Both are standard.

**The $\mathfrak{su}(2)$ factor vanishes identically.** For $SU(2)$ in any representation the symmetrised trace of three generators is zero, because there is no cubic Casimir. For the doublet with $T^a=\tfrac12\sigma^a$ the proof is one line:

$$
\{T^b,T^c\}=\tfrac14\{\sigma^b,\sigma^c\}=\tfrac12\delta^{bc}I_2 ,
\qquad
T^a\{T^b,T^c\}=\tfrac14\delta^{bc}\sigma^a ,
\qquad
\mathrm{Tr}\,\big[T^a\{T^b,T^c\}\big]=\tfrac14\delta^{bc}\,\mathrm{Tr}\,\sigma^a = 0 .
$$

The same conclusion holds for every $SU(2)$ representation: each is real or pseudoreal, the cubic invariant does not exist, and the triangle coefficient vanishes. The step that makes this useful is the sign rule: because a left-handed doublet and a right-handed doublet contribute with opposite signs, and because each is separately anomalous only through a coefficient that is already zero, **$SU(2)$ is anomaly-free whatever its fermion content.** This is a property of the group, not of the model.

**The abelian factor and the trace pairing.** For the central $U(1)$ the coefficient is the cubic charge sum. The framework's own central phase, however, acts as a **scalar** on the algebra and its module: multiplication by $e^{i\theta}$ multiplies every component of the module by the same factor, so the left- and right-handed spectra carry the *same* charge $q$. The left-handed and right-handed contributions to $\sum Y^3$ therefore have equal magnitude and opposite sign,

$$
\sum_{\text{L}} q^3 - \sum_{\text{R}} q^3 = 0 ,
$$

identically, for every module and every charge. This is the algebraic statement that the framework's abelian gauge factor is **vector-like**, and it is the reason that factor cannot be weak hypercharge: hypercharge is chiral, with independent left and right charges, and it is precisely the independent left and right charges that make the cubic sum a condition rather than a tautology. The companion articles on chiral fermions and on the Standard Model agenda make the same point.

## Gauge Anomaly Cancellation on the Standard Model Spectrum

**The conditions.** For the Standard Model gauge group $SU(3)_c\times SU(2)_L\times U(1)_Y$, the vanishing of the triangle coefficients gives four independent conditions on the matter content of one generation, listed here with the left-handed minus right-handed convention:

$$
\sum Y = 0 \quad(\text{gravitational}/U(1)_Y),
\qquad
\sum Y^3 = 0 \quad(U(1)_Y^3),
\qquad
\sum_{\text{doublets}} Y = 0 \quad(SU(2)_L^2\,U(1)_Y),
\qquad
\sum_{\text{colour}} Y = 0 \quad(SU(3)_c^2\,U(1)_Y),
$$

while $SU(3)_c^3$ vanishes automatically because the colour sector is vector-like, and the mixed $SU(3)_c\,SU(2)_L$ conditions vanish automatically because no fermion carries both a nontrivial colour and a nontrivial weak-triplet index. All four are standard.

**The spectrum.** One generation, with hypercharge $Y=Q-T_3$:

| field | $SU(3)_c$ | $SU(2)_L$ | $Y$ | chirality |
|---|---|---|---|---|
| $Q_L=(u_L,d_L)$ | $3$ | $2$ | $1/6$ | L |
| $u_R$ | $3$ | $1$ | $2/3$ | R |
| $d_R$ | $3$ | $1$ | $-1/3$ | R |
| $L_L=(\nu_L,e_L)$ | $1$ | $2$ | $-1/2$ | L |
| $e_R$ | $1$ | $1$ | $-1$ | R |

**The verification.** Each condition was computed exactly in rational arithmetic, for one generation, with the left-handed minus right-handed sign convention:

| condition | value (recomputed) |
|---|---|
| $\sum_L Y-\sum_R Y$ | $0$ |
| $\sum_L Y^3-\sum_R Y^3$ | $0$ |
| $SU(2)_L^2U(1)_Y$ ($\sum_{\text{doublets}}Y$, colour-weighted) | $0$ |
| $SU(3)_c^2U(1)_Y$ ($\sum_{\text{colour}}Y$, weak-weighted) | $0$ |

The arithmetic is instructive in one respect: the cubic sum does **not** vanish separately for left- and right-handed fields — for the left-handed content it is $-2/9$ and for the right-handed content it is also $-2/9$ — so the cancellation is a genuine left–right conspiracy and not a per-field accident. That is the sense in which the hypercharges are *fixed* by anomaly cancellation: the condition is restrictive on the assignments.

**What the conditions constrain, and what they do not.** Anomaly cancellation constrains the hypercharges, the colours, and the weak representations. It does **not** constrain the number of generations: each generation contributes the sums above independently, so $N_g$ copies contribute $N_g$ times zero. It also does not fix the values uniquely — the conditions are four equations on the several charges, and their solution is the one-generation spectrum only together with other input. The framework's position is the constraint itself: it can state and verify the conditions, and it cannot select the spectrum. The companion article on the number of generations takes up the counting.

**A consistency remark on the module.** The conditions are statements about a **chiral** assignment of charges to the module $\Delta=S\oplus\bar{S}$ with independent left and right charges. The framework's own center does not supply such an assignment; a chiral abelian symmetry can be *written* on the module, $Q=q_LP_L+q_RP_R$, and it is gauge covariant and anomaly-constrained (the companion article on chiral fermions derives the mass selection rule $q_L=q_R$), but it is not generated by the algebra. The Standard Model's hypercharge is therefore an input on the module, and the cancellation is verified on it rather than derived from it.

**A sterile fermion is unconstrained.** A right-handed neutrino, carrying $Y=0$ and no colour or weak charge, contributes zero to every one of the four sums. Anomaly cancellation therefore gives **no information** about the existence or the number of sterile fermions, and a gauge-singlet Majorana mass for such a field is not forbidden by any anomaly condition. This is the fermion-sector statement that makes the see-saw mechanism of the companion article possible at all: the heavy state whose mass suppresses the light neutrino mass carries no gauge quantum numbers, and the spectrum that cancels the anomalies is silent about it.

**What the conditions do not fix.** Anomaly cancellation is a set of four homogeneous conditions on the charges. It constrains but does not determine the spectrum: it does not fix the overall hypercharge normalisation, it does not distinguish the assignments of the several multiplets beyond a small set of solutions, it says nothing about the number of generations, and it says nothing about gauge singlets. Its content is a consistency requirement that any chiral spectrum must meet, and the Standard Model's spectrum meets it; the framework's role is to state and check the requirement, not to select its solution.

## The Framework's Own Gauge Structure is Anomaly-Free

Two statements, both exact, close the loop between the algebra and the consistency condition.

- **The central $U(1)$ is vector-like and therefore anomaly-free.** The center $\mathbb{C}_{\mathbb{B}}$ acts as a scalar; every component of every module carries the same charge, the left and right spectra coincide, and $\sum_L q^3-\sum_R q^3=0$ identically. The framework's abelian factor cannot produce a gauge anomaly.
- **The $\mathfrak{su}(2)$ inside $\mathbb{M}_-$ is anomaly-free identically.** Its triangle coefficient vanishes for every representation by the computation above, and the sign rule makes the statement independent of the fermion content. The framework's non-abelian factor cannot produce a gauge anomaly either.

The consequence is worth stating plainly: **the biquaternion framework's own gauge fields pass the anomaly consistency test automatically.** A gauge anomaly is a failure mode the framework does not have. What the framework also does not have is a **chiral** gauge group — a factor assigning independent left and right charges — and it is exactly the chiral factors that make anomaly cancellation a nontrivial condition. So the framework is anomaly-free for the simple reason that it is not chiral where it is gauged, and the Standard Model's nontrivial cancellation lives in the part of its group that the framework does not generate.

**The global anomaly.** There is a second consistency condition, discrete rather than perturbative: Witten's global $SU(2)$ anomaly makes an $SU(2)$ gauge theory with an odd number of Weyl doublets inconsistent, because the fermion determinant changes sign under a large gauge transformation. For the framework's $\mathfrak{su}(2)$ the fermion content on the algebra's module is not chiral, so the condition is satisfied immediately; on the Standard Model's $SU(2)_L$ the doublet number per generation is even and the condition is satisfied by the spectrum. The statement is standard and is recorded here as the discrete counterpart of the triangle condition.

## The Anomaly as a Topological Density

**The density is a total derivative.** In four dimensions the abelian anomaly density is the divergence of a Chern–Simons current, in the normalisation of the companion article on instantons,

$$
\partial_\mu K^\mu = \tfrac12\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} ,
\qquad
K^\mu = \epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma} ,
$$

so the anomaly is invisible in the local equations of motion of the gauge field and is detected only by the charge it transports:

$$
\frac{d}{dt}\int d^3x\,j_5^0
= \frac{e^2}{16\pi^2}\int d^3x\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= \frac{e^2}{8\pi^2}\oint dS_i\,K^i .
$$

The axial charge of the vacuum therefore changes only through a boundary term — a large gauge configuration, an instanton. This is the standard topological reading of the anomaly, and the companion article on instantons supplies the framework's form of the topological charge: the density is proportional to $I_2=\mathbf{E}\cdot\mathbf{B}$, whose integral over a configuration is the instanton number. In the biquaternion language the anomaly transports axial charge into the winding of the material-sector gauge field; both are framework objects, and neither needs an object beyond the algebra.

**The index.** The integrated anomaly is twice the index of the Dirac operator,

$$
\int d^4x\,\partial_\mu j_5^\mu = 2\,\mathrm{ind}(D\!\!\!/ ) ,
$$

the difference between the number of right- and left-handed zero modes of the massless Dirac operator in the background; the general index statement is the Atiyah–Singer theorem, and the zero-mode count and the index theorem belong to the corpus's general gauge apparatus rather than to the fermion sector. The two facts the fermion sector uses are immediate consequences and are all that is needed here: the anomaly coefficient is an **integer** topological invariant, which is why it cannot be renormalised (no continuous parameter can interpolate between integers), and a single unit of topological charge therefore produces a net axial-charge violation by two units per fermion flavour. The divergence identity, the density, and the integer are one statement.

**The consistency of the picture.** The three readings of the anomaly — the triangle diagram with its trace, the Chern–Simons divergence with its boundary charge, and the index of the Dirac operator — are three faces of one object. The triangle gives the coefficient; the total-derivative form gives its topological character; the index gives its integrality. In the framework the coefficient is a Clifford trace ($\gamma_5=i\omega$), the density is a field invariant ($I_2$), and the integral is a winding number of the material-sector connection. The article has stated the first two and referred the third to the general apparatus.

## The Non-Abelian Anomaly and Its Consistency

**The consistency problem.** For a non-abelian gauge theory the anomalous divergence is not simply $\partial_\mu j^{a\mu}\propto A^{abc}\epsilon FF$; the current itself is defined only up to a local polynomial in the gauge field (the Bardeen counterterm), and the requirement is not just that the coefficient vanish but that the anomaly be expressible as the transformation of a local functional — the Wess–Zumino term — so that the gauge variation of the effective action is local and the theory remains consistent. The condition on the matter spectrum is the vanishing of the symmetrised trace $A^{abc}=\mathrm{Tr}[T^a\{T^b,T^c\}]$ used above; the finer statement is that the anomaly is a **consistent** (Bardeen) anomaly, whose form is fixed by the Wess–Zumino consistency condition rather than by the covariant triangle alone. Both are standard, and the corpus transcribes them; the fermion sector needs only the condition $A^{abc}=0$.

**The obstruction to a covariant current.** One structural point belongs here because it is easy to state wrongly. In four dimensions the anomaly is a total derivative, yet one cannot have a current that is simultaneously **covariant** and **conserved**: the covariant current has a nonzero divergence and the conserved current is not gauge covariant, and the two differ by the Chern–Simons term. The framework's gauge currents, built on the $\mathfrak{su}(2)$ connection of the companion articles, inherit this; there is nothing in the algebra that removes it, and the resolution is the standard Bardeen counterterm, not a biquaternion identity. The condition for consistency is the vanishing of $A^{abc}$, and the framework's own $A^{abc}$ vanishes identically, so the framework never has to face the obstruction for its own gauge fields.

**Anomaly matching.** A further standard consequence is 't Hooft's anomaly matching: the anomaly coefficients of the unbroken global symmetries must be the same in the ultraviolet and in the infrared, because the anomaly is one-loop-exact and cannot be generated or destroyed by the strong dynamics. For quantum chromodynamics this is one of the constraints on the spectrum of massless composite fermions. The framework has no confinement and no composite spectrum, so it cannot use the matching conditions; it records them as a property of the anomaly that survives any dynamics, and therefore as a constraint any future framework completion would have to satisfy.

## The 't Hooft Vertex and the $U(1)_A$ Problem

**The vertex.** The axial anomaly can be written as an effective interaction. For $N_f$ massless flavours, a single instanton of the colour gauge field generates a $2N_f$-fermion vertex — the 't Hooft determinant — which is chirally non-invariant:

$$
\mathcal{L}_{\mathrm{'t Hooft}} \;\propto\; \det_{f,f'}\big(\bar{\psi}_{fL}\psi_{f'R}\big) + \text{h.c.},
$$

with one factor of each left- and each right-handed field. The operator has the quantum numbers of the anomaly, it breaks the axial $U(1)_A$, and it leaves the non-abelian chiral symmetry $SU(N_f)_L\times SU(N_f)_R$ intact. In the fermion sector this is the anomalous counterpart of the condensate: where the condensate breaks the axial symmetry **spontaneously**, the 't Hooft vertex breaks its axial $U(1)$ subgroup **explicitly**, and the two together are what resolve the $U(1)_A$ problem of quantum chromodynamics. The vertex is a six-fermion operator for $N_f=3$; the framework carries it as a product of the bilinears it already has, since each factor $\bar{\psi}_{fL}\psi_{f'R}$ is the linear chiral pairing of the mass term.

**What is not treated.** The resolution of the $U(1)_A$ problem in full involves the $\theta$ parameter, the vacuum angle, and — if it is a symmetry — the axion; the $\theta$ parameter and the Witten effect belong to the corpus's general gauge apparatus, and the axion to the spin-$0$ subcategory. This article states only the fermion-sector fact: the anomaly generates a chirally non-invariant multifermion vertex, and the divergence identity of the first section is its local form.

## The Traces Involved, and the One That Is Not

**Two traces, and only two.** Every anomaly coefficient in this article is a product of two independent traces: the **Clifford trace** over the four-dimensional Dirac module, which supplies the $\epsilon^{\mu\nu\rho\sigma}$ through $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$, and the **gauge trace** over the representation, which supplies $A^{abc}=\mathrm{Tr}[T^a\{T^b,T^c\}]$. In the abelian case the second is the cubic charge sum. The two are computed separately because they act on different indices, and the anomaly is their product.

**The chiral trace is a difference of Weyl traces.** In the block decomposition $\Delta=S\oplus\bar{S}$ with $\gamma_5=\mathrm{diag}(-I_2,I_2)$, a trace with a chirality insertion splits:

$$
\mathrm{tr}\big(\gamma_5 X\big) = -\,\mathrm{tr}_S(X_{LL}) + \mathrm{tr}_S(X_{RR}) = \mathrm{tr}_S(X_{RR})-\mathrm{tr}_S(X_{LL}),
$$

so the chirality-weighted trace is the **difference** of the two Weyl traces. For $X=I_4$ both halves contribute their dimension and the difference vanishes, $\mathrm{tr}(\gamma_5)=2-2=0$, which is the recomputed identity that makes the anomaly compatible with Lorentz invariance. The same splitting is the algebraic origin of the left-minus-right rule: a left-handed Weyl fermion in $S$ contributes its Weyl trace with one sign and a right-handed one with the other, and the anomaly is their difference.

**The trace that is not involved.** The framework's informational trace formula, $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, is the state-and-observable pairing of the Hermitian sector $\mathbb{M}_+$; it counts the scalar part of a product with the factor $\mathrm{Tr}(e_0)=2$. It is **not** the trace that computes an anomaly. The anomaly trace is the ordinary matrix trace over the gauge representation and the ordinary Clifford trace over the module; neither is the scalar-part pairing, and substituting one for the other would be a category error. The trace formula of $\mathbb{M}_+$ is used in the companion articles for expectation values of observables; the anomaly uses the traces of the module. The distinction is stated here because the two are both called "the trace" in the series.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The gamma-matrix trace underlying every anomaly, $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$ | **Supplied**, recomputed for all permutations |
| The identification $\gamma_5=i\omega$ with the volume element | **Supplied** by the Clifford isomorphism |
| The axial anomaly density as the framework's invariant $I_2=\mathbf{E}\cdot\mathbf{B}$ | **Supplied** (with the instanton article's normalization); the coefficient is standard |
| The exactness of the anomaly coefficient (Adler–Bardeen) | **Transcribed**; the index-theoretic reason belongs to the general gauge apparatus |
| The Standard Model's cancellation conditions and their verification | **Transcribed** and recomputed exactly |
| Anomaly-freedom of the framework's own $U(1)$ and $\mathfrak{su}(2)$ | **Supplied**; vector-like center and no cubic Casimir |
| A chiral gauge group, and the spectrum it would constrain | **Not supplied**; the center is vector-like and the $\mathfrak{su}(2)$ acts vector-like on the module |
| The $\theta$ parameter, the $U(1)_A$ problem, and the axion | **Outside**; the $\theta$ parameter belongs to the general gauge apparatus, the axion to the spin-$0$ subcategory |
| The number of generations | **Not constrained** by cancellation; treated separately |

## Summary

An anomaly is a quantum breaking of a classical symmetry. The axial anomaly is the failure of the chiral rotation to preserve the measure; for a charged Dirac fermion its divergence is the standard Adler–Bell–Jackiw result,

$$
\partial_\mu j_5^\mu = 2im\,\bar{\psi}\gamma_5\psi + \frac{e^2}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

and the anomalous density is proportional to the framework's second field invariant $I_2=\mathbf{E}\cdot\mathbf{B}$: the anomaly's pseudoscalar density is the biquaternion field's own pseudoscalar invariant. The gamma-matrix identity behind every anomaly, $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$, and the identification $\gamma_5=i\omega$ of the chirality operator with the volume element, are supplied by the framework's Clifford structure and were recomputed.

The gauge anomaly is the triangle coefficient $\mathrm{Tr}[T^a\{T^b,T^c\}]$, and its vanishing is a consistency condition on the chiral spectrum. The article verified the Standard Model's four conditions — $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$, and the colour sum — exactly, for one generation, with a left-minus-right sign convention; the cubic sum cancels by a genuine left–right conspiracy rather than per field. The conditions constrain the hypercharges and colour assignments but not the number of generations, since each generation contributes a zero.

The framework's **own** gauge structure is anomaly-free identically: the central $U(1)$ is vector-like, so its cubic charge sum vanishes, and $\mathfrak{su}(2)\subset\mathbb{M}_-$ has no cubic Casimir, so its triangle coefficient vanishes for every representation. A gauge anomaly is therefore a failure mode the framework does not have — for the structural reason that the framework is not chiral where it gauges. The Standard Model's chiral spectrum, on which cancellation is nontrivial, is an input the framework hosts and constrains but does not select.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center; the vector-like abelian factor |
| $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$, $\Box=\partial_{ict}^2+\Delta$ | Gradient and d'Alembertian, series convention |
| $\Delta=S\oplus\bar{S}$, $\gamma_5=\mathrm{diag}(-I_2,I_2)$ | Dirac module and chirality operator |
| $\omega=\gamma^0\gamma^1\gamma^2\gamma^3=-i\gamma_5$ | Volume element; $\gamma_5=i\omega$ |
| $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$ | The Clifford trace behind the anomaly |
| $\epsilon^{\mu\nu\rho\sigma}$, $\epsilon^{0123}=+1$ | Totally antisymmetric symbol |
| $j_5^\mu=\bar{\psi}\gamma^\mu\gamma_5\psi$ | Axial current |
| $\partial_\mu j_5^\mu=2im\bar{\psi}\gamma_5\psi+\dfrac{e^2}{16\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Axial anomaly (ABJ) |
| $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$, $I_2=\mathbf{E}\cdot\mathbf{B}$ | Biquaternion field invariants |
| $\tilde{F}=i\sqrt{\epsilon}\mathbf{E}-\sqrt{\mu}\mathbf{H}$ | Biquaternion field strength |
| $A^{abc}=\mathrm{Tr}[T^a\{T^b,T^c\}]$ | Triangle anomaly coefficient |
| $\sum_L-\sum_R$ | Left-handed minus right-handed anomaly sum |
| $T^a=\tfrac12\sigma^a$ | $SU(2)$ generators; $T^a\{T^b,T^c\}=\tfrac14\delta^{bc}\sigma^a$ |
| $Y=Q-T_3$ | Hypercharge convention |
| $SU(3)_c\times SU(2)_L\times U(1)_Y$ | Standard-model gauge group (standard notation, not framework objects) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, for the axial anomaly and the triangle diagram.
- J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Nuovo Cimento A* **60** (1969) 47–61, for the anomaly and its physical consequence.
- S. L. Adler and W. A. Bardeen, "Absence of higher-order corrections in the anomalous axial-vector divergence equation," *Physical Review* **182** (1969) 1517–1536, for the exactness of the one-loop anomaly.
- W. A. Bardeen, "Anomalous Ward identities in spinor field theories," *Physical Review* **184** (1969) 1848–1857, for the non-renormalisation of the anomaly and the consistent anomaly.
- C. Bouchiat, J. Iliopoulos, and P. Meyer, "An anomaly-free version of Weinberg's model," *Physics Letters B* **38** (1972) 519–523, for the hypercharge assignments required by anomaly cancellation.
- D. J. Gross and R. Jackiw, "Effect of anomalies on quasi-renormalizable theories," *Physical Review D* **6** (1972) 477–493, for the consistency condition on a chiral gauge theory.
- E. Witten, "An $SU(2)$ anomaly," *Physics Letters B* **117** (1982) 324–328, for the global (discrete) anomaly.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the triangle calculation, the trace identities, and the Standard Model cancellation conditions.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the anomaly, its topological character, and the $U(1)_A$ problem.
- K. Fujikawa, "Path-integral measure for gauge-invariant fermion theories," *Physical Review Letters* **42** (1979) 1195–1198, for the path-integral derivation of the anomaly.
- M. F. Atiyah and I. M. Singer, "The index of elliptic operators: III," *Annals of Mathematics* **87** (1968) 546–604, for the index theorem that makes the anomaly coefficient topological.
