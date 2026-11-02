# __Anomalies and Anomaly Cancellation in Biquaternionic Form__

## Introduction

An **anomaly** is a symmetry of a classical action that does not survive quantisation. The classical current is conserved by the equations of motion; the one-loop diagram that computes its divergence is not zero; and the discrepancy is not a calculational artefact but an exact, finite, one-loop effect that is not renormalised — the Adler–Bardeen theorem. Two anomalies matter for particle physics, and they play opposite roles.

- The **axial (Adler–Bell–Jackiw) anomaly** breaks a *global* symmetry that the classical theory has. It is physical: it is what makes the neutral pion decay to two photons and what makes the axial $\mathrm{U}(1)$ of quantum chromodynamics not a symmetry of the quantum theory.
- The **gauge anomaly** threatens a *local* symmetry. If the triangle diagram with three gauge currents does not vanish, the gauge theory is inconsistent: the current is not conserved, the longitudinal gauge modes do not decouple, and unitarity and renormalisability fail. A chiral gauge theory is therefore consistent only if the anomaly cancels, and the cancellation is a **condition on the matter spectrum**.

The framework's contribution is structural, and is stated at the outset.

- **Established, and recomputed below.** The axial anomaly is the failure of the chiral rotation to preserve the measure. Its density is built from the chirality cell, which is $i$ times the volume cell, and it is proportional to the **second invariant** $I_2=\vec E\cdot\vec B$ of the biquaternion field — the topological density computed in the companion article on instantons. The anomaly is therefore not foreign to the framework: its density is one of the framework's two field invariants.
- **Established, and recomputed below.** The anomaly coefficient of a gauge theory is the symmetrised trace $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ over the left-handed Weyl fermions. The framework's **own** gauge structure — the central $\mathrm{U}(1)$ and the $\mathrm{SU}(2)$ inside $\mathbb{M}_-$ — is anomaly-free: the central phase is vector-like, so its cubic trace cancels identically, and $\mathrm{SU}(2)$ has no cubic Casimir, so its triangle coefficient vanishes identically. The framework cannot be inconsistent by a gauge anomaly of the algebra's own gauge fields.
- **Standard, transcribed.** The anomaly cancellation conditions of the Standard Model's chiral spectrum — $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$, and the colour conditions — are standard, and the article verifies all of them generation by generation. They constrain the hypercharges and the colour assignments; they do not constrain the **number** of generations.
- **Gap, left visible.** The framework has no chiral gauge group of its own — the central phase is vector-like and the $\mathrm{SU}(2)$ acts vector-like on the algebra's module — so it cannot *derive* the Standard Model's chiral spectrum from which the cancellation conditions are read. It transcribes the conditions and hosts their solution; it does not select it.

**The order of the article.** A section states the anomaly as a quantum failure of a classical symmetry and exhibits the Clifford trace behind it. A section gives the axial anomaly, its current, its density, and the identification of the density with $I_2$. A section sets out the triangle coefficient and computes the group factors. A section states the gauge cancellation conditions and verifies them on the Standard Model spectrum. A section proves the framework's own gauge structure anomaly-free. A section treats the anomaly as a topological density, a section the non-abelian consistency conditions, and a section the 't Hooft vertex. A section separates the two traces the article uses from the one it does not. A table collects what the framework supplies, transcribes, and does not supply; the closing sections are the Gamma Formulation, the Summary, the Summary of Notation, and Further Reading.

**Notation, once.** The imaginary unit has $i^2=-1$. It is the only imaginary unit in the article, and where two of them meet in a product they are reduced before the formula is read: the four generator cells of a four-fold product contribute $i^4=+1$, so such a product is a product of four plain cells and carries no residual $i$. The two-sided cells act by $L_{a}R_{b}\psi=a\psi b$; the generator cell of the coordinate $x_\mu$ is $iL_{e_\mu}R_{\vec e_{\tau(\mu)}}$ with $\tau(t)=x$ and $\tau(k)=y$ for $k=x,y,z$; the chirality cell is $-iR_{\vec e_z}$; the module spinor is $\psi=\psi_L+\psi_R$, with $\psi_L$ and $\psi_R$ its two chiral components; and the Dirac bar is $\bar{\psi}=\psi^{\dagger}iR_{\vec e_x}$. The four generator cells carry the Clifford relations of $g=\operatorname{diag}(+1,-1,-1,-1)$. The same objects, under their Clifford frame names, are collected in the closing section *The Gamma Formulation*, and none of those names is used before it.

The volume cell is the product of the four generator cells, taken in the order $t,x,y,z$, and the four factors of $i$ multiply to $i^4=+1$:
$$
\omega=iR_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y}
=i^4\bigl(R_{\vec e_x}L_{\vec e_x}R_{\vec e_y}L_{\vec e_y}R_{\vec e_y}L_{\vec e_z}R_{\vec e_y}\bigr)=-R_{\vec e_z},
$$
so that
$$
-iR_{\vec e_z}=i\omega .
$$
The chirality cell is therefore $i$ times the volume cell, and the two differ by that unit alone. This is the identity that places the anomaly's density inside the framework rather than beside it.

**The field strength, in components.** For the abelian anomaly the field strength is $\tilde F=\tilde\nabla^{\natural}\tilde A$, the alternating symbol has $\epsilon_{0123}=+1$, and the real-time components are $F_{t'i}=E_i$ and $F_{ij}=-\epsilon_{ijk}B_k$ in the indices $t',x,y,z$. The biquaternion carrier is written in the algebra's $ict'$ frame, where the time coordinate is $Q_t=ict'$ and the time component of the field strength is $F_{tx}=iE_x/c$; the density below is computed directly from the real-time components $F_{t'i}=E_i$ and $F_{ij}=-\epsilon_{ijk}B_k$. For the non-abelian factor the components are those of the companion article on non-abelian gauge fields,
$$
F_{\mu\nu}=\frac{\partial\mathcal{A}_\nu}{\partial Q_\mu}-\frac{\partial\mathcal{A}_\mu}{\partial Q_\nu}+i\kappa\,[\mathcal{A}_\mu,\mathcal{A}_\nu],
\qquad
\kappa=\frac{ϙ}{\hbar},
$$
of which
$$
\tilde F=\frac{1}{2}\sum_{\mu,\nu\in\{t,x,y,z\}}F_{\mu\nu}\,\bar e_\mu e_\nu
$$
is the biquaternion carrier, with $\bar e_\mu$ the quaternion conjugate of the unit ($\bar e_t=e_t$, $\bar e_k=-\vec e_k$). The second display is a **definition** of the carrier, not an identity expressing it as a derivative of $\mathcal{A}$; the commutator term is not a derivative of anything.

**The invariants.** With the field $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, the two real invariants are $I_1=\vec E^2-c^2\vec B^2$ and $I_2=\vec E\cdot\vec B$, with $\vec B=\mu\vec H$, in the normalization of the instanton article. The informational trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is inherited unchanged; it is the pairing of the Hermitian sector, and the section *The Traces Involved, and the One That Is Not* keeps it apart from the two traces that compute an anomaly. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value, and the symbols $SU(3)$, $SU(2)_L$, $\mathrm{U}(1)_Y$, $Y$, $T_3$ are **standard-model notation, not framework objects**, used only where a standard structure is named.

The framework results used here are those of the companion articles:

- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological density and its identification with the invariant $I_2$.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength, the invariants $I_1$ and $I_2$, and the biquaternion norm.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral classification, the Dirac pair, and the gauge quantum numbers of the left- and right-handed fields.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the multiplet structure whose charge sums are the cancellation conditions.

## The Classical Symmetry and its Quantum Failure

**The mechanism, stated once.** A classical symmetry has a conserved current, $\langle\tilde\nabla,\tilde J\rangle_{\natural}=0$, by Noether's theorem. The quantum divergence is computed by inserting the current into a correlation function; at one loop the triangle diagram contributes, and the divergence receives a term that is finite as the regulator is removed. If that term is a total derivative of a topological density it cannot be removed by a local counterterm, and the symmetry is genuinely broken quantum-mechanically. This is the content of the Adler–Bardeen theorem: the anomaly is a one-loop effect and is exact.

**Two kinematic facts make the computation tractable.** First, in four dimensions the relevant diagram is a triangle with one axial and two vector currents (the axial anomaly) or three gauge currents (the gauge anomaly); higher-point diagrams do not add new anomalous terms. Second, the anomaly is a **trace** statement: the diagram's coefficient is a trace of a product of frame cells times a trace of gauge generators, and each trace is computed once and for all.

**The biquaternion entry point.** The framework's contribution is an identity of the Clifford trace over the module. Every anomaly coefficient in the article is a multiple of it, so it is stated once and referred to afterwards as the boxed trace:
$$
\boxed{\;\mathrm{tr}\big(-iR_{\vec e_z}\,L_{e_\mu}R_{\vec e_{\tau(\mu)}}\,L_{e_\nu}R_{\vec e_{\tau(\nu)}}\,L_{e_\rho}R_{\vec e_{\tau(\rho)}}\,L_{e_\sigma}R_{\vec e_{\tau(\sigma)}}\big) = -4i\,\epsilon_{\mu\nu\rho\sigma}\;}
$$
The four generator cells have been reduced by $i^4=+1$, so the only imaginary unit left standing in the box is the $-i$ of the chirality cell; the display is the same trace as the one written with the generator cells $iL R$, with the four $i$'s removed. It vanishes unless the four indices are distinct, and then it is $-4i$ times the sign of the permutation, with $\epsilon_{0123}=+1$; it was recomputed on the $4!=24$ distinct index assignments; repeated indices vanish by the trace identity.

Three remarks make the box usable without recomputation. First, the reduction uses $i^2=-1$ and $i^4=+1$: the four generator cells of a four-fold product contribute one, so no second imaginary unit is hidden in the box. Second, at $\mu\nu\rho\sigma=0123$ the four plain cells multiply to the volume cell, so the box becomes $\mathrm{tr}(-iR_{\vec e_z}\,\omega)=-4i$: that is the number every anomaly coefficient in the article carries. Third, the box is a trace over the four-dimensional Dirac module, not the informational trace formula of the Hermitian sector; the section *The Traces Involved, and the One That Is Not* keeps the two apart.

## The Axial Anomaly

**The current and the equation it belongs to.** The corpus's Dirac pair is

$$
\tilde\nabla\psi_R=m\,\psi_L,
$$

$$
\tilde\nabla^{\natural}\psi_L=m\,\psi_R,
$$

one equation per chirality, on the module $\Delta=S\oplus\bar{S}$; the first is the right-handed equation and the second is its quaternion conjugate. At $m=0$ the pair decouples,

$$
\tilde\nabla\psi_R=0,
$$

$$
\tilde\nabla^{\natural}\psi_L=0,
$$

and each equation is identical in form to the source-free Maxwell equation; the mass is what ties the two chiralities together, and it is the only term that does.

**The two-sided form, and why it is not a second dynamics.** The same physics has a two-sided representation, a single equation on the algebra,

$$
\tilde\nabla^{\natural}F=m\,\chi\bar{F},
\qquad
\chi=-iR_{\vec e_z},
$$

for a biquaternion field $F$ — the two-sided Dirac field, not the component field strength $F_{\mu\nu}$ — with $\bar{F}$ its coefficient conjugate. The derivative acts on the left, the mass acts on the right through the chirality cell, and the conjugation supplies the antilinear part. The one-sided pair is the definition; the two-sided form is the representation in which the mass is a right multiplication, and the two are related by the dictionary of *The Dirac Equation in Biquaternionic Form* but are different operators: the pair is linear in the field, the two-sided equation is antilinear in its mass term. The anomaly below is read from the one-sided pair, because the axial current is a bilinear of the module field and the measure is the measure of that field. What the two-sided form adds is the structural identity behind the current: the cell $\chi$ that multiplies the mass on the right is the cell the axial current inserts, so the mass term and the axial current are the two places where chirality enters.

**The currents.** The common phase is a symmetry at every $m$, because the mass is central and passes through it, so the vector current

$$
j_{\mu}=\bar{\psi}\,iL_{e_\mu}R_{\vec e_{\tau(\mu)}}\,\psi
$$

is conserved at every $m$. An axial rotation assigns opposite phases to the two chiralities, so the mass term, which pairs them, is not invariant under it; the axial current therefore carries the chirality cell,

$$
j_{5\mu}=\bar{\psi}\,iL_{e_\mu}R_{\vec e_{\tau(\mu)}}\,(-iR_{\vec e_z})\,\psi
=\bar{\psi}\,L_{e_\mu}R_{\vec e_{\tau(\mu)}}\,R_{\vec e_z}\,\psi ,
$$

where the two imaginary units have been reduced by $i(-i)=+1$. It is conserved only at $m=0$.

**The result.** For a Dirac fermion of electric charge $e$ in four dimensions, with $\tilde J_5=\sum_\mu j_{5\mu}e_\mu$ and with $\langle\tilde\nabla,\tilde J_5\rangle_{\natural}=\sum_\mu\partial j_{5\mu}/\partial Q_\mu$ the divergence of the operator conventions — the unweighted sum, the sign vector sitting inside the norm and never in the divergence —

$$
\boxed{\;\langle\tilde\nabla,\tilde J_5\rangle_{\natural} \;=\; 2m\,\bar{\psi}\,R_{\vec e_z}\,\psi \;+\; \frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\;}
$$

where the mass term has been reduced in the same way, $2im(-iR_{\vec e_z})=2mR_{\vec e_z}$. The first term is the classical explicit breaking by the mass; the second is the anomaly, present even at $m=0$, and its coefficient is the standard Adler–Bell–Jackiw one, quoted from the standard literature rather than derived.

**The density, with its sign and its coefficient.** With $F_{t'i}=E_i$ and $F_{ij}=-\epsilon_{ijk}B_k$ the contraction evaluates exactly,

$$
\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=-8\,\vec E\cdot\vec B ,
$$

so the anomaly term is

$$
\frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=-\frac{e^2}{2\pi^2}\,\vec E\cdot\vec B ,
$$

a negative multiple of the framework's second field invariant:

$$
\boxed{\;\mathcal{A}(x)\;=\;-\frac{e^2}{2\pi^2}\,I_2\;}.
$$

The sign is a matter of the orientation $\epsilon_{0123}=+1$ and of the sign of the axial current; the proportionality to $I_2$ alone is not.

**The biquaternion form of the density.** The companion article on instantons computes the topological density and finds it a function of $I_2$ alone; in its $ict'$ frame and orientation the statement is

$$
\frac{1}{4}\sum_{\mu,\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=\frac{2i}{c}\,I_2 .
$$

In the real-time components used here the same contraction is $\frac14\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=-2I_2$; the two conventions differ by the $ict'$ factor and by the sign convention for $\vec B$, and only the proportionality is used below. What the anomaly uses is that proportionality, and it is frame-independent: the anomalous divergence is the divergence of the axial current into the framework's own pseudoscalar invariant.

Three structural remarks follow. First, the density is a **pseudoscalar** — parity-odd, as $I_2$ is — which is why it can stand on the right-hand side of the divergence of an axial, parity-odd current. Second, it is a **total derivative** in the abelian case,

$$
\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=2\,\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural},
\qquad
J_{\mathrm{CS},\mu}=\sum_{\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma},
$$

which is why it is not renormalised and why it is fixed by topology. Third, the generator of the axial rotation is the chirality cell up to a unit: $i\chi=i(-iR_{\vec e_z})=R_{\vec e_z}$, so the rotation $\psi\mapsto e^{i\alpha\chi}\psi=\psi e^{\alpha\vec e_z}=\cos\alpha\,\psi+\sin\alpha\,\psi\vec e_z$ is generated by $i$ times the chirality cell, the unit being the one the exponential absorbs. The pseudoscalar character and the total-derivative form are standard; what the framework adds is that the density is the second invariant of its own field, and that the chirality cell is $i\omega$.

**The physical consequence, stated and not developed.** The anomaly makes $\pi^0\to\gamma\gamma$ possible at the observed rate and makes the axial $\mathrm{U}(1)$ of quantum chromodynamics explicitly broken at the quantum level; the $\mathrm{U}(1)_A$ problem and its resolution by the $\theta$ parameter and the axion belong to the corpus's other subcategories and are not treated here. The point for the fermion sector is the divergence identity itself: the axial current of any single massless Dirac fermion is not conserved quantum-mechanically, and no choice of regulator removes the term without moving the breaking elsewhere.

**Why the anomaly is exact.** The Adler–Bardeen theorem states that the coefficient of the anomaly is the one-loop value, unaffected by higher-order corrections. The modern reason is that the **integrated** anomaly is the index of the Dirac operator, an integer topological invariant; a continuous renormalisation cannot change an integer, so the coefficient is protected. The index statement is the subject of the general gauge apparatus and of the companion article on the Fujikawa method; here it is noted as the reason the coefficient above is stable.

## The Triangle Coefficient and the Group Factors

**Two traces, two names.** Throughout, $\mathrm{tr}$ is the Clifford trace over the four-dimensional Dirac module and $\mathrm{Tr}_R$ the matrix trace over the gauge representation; the anomaly is their product. The subscript-free $\mathrm{Tr}$ appears only in the inherited informational formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, whose argument is a product of algebra elements rather than of matrices.

**The general anomaly coefficient.** For a gauge theory with generators $T_a$ acting on a left-handed Weyl fermion in a representation $R$, the coefficient of the triangle anomaly is the **symmetrised trace**

$$
A_{abc}(R) \;=\; \mathrm{Tr}_R\big[T_a\{T_b,T_c\}\big] .
$$

The anomaly is the sum over all left-handed Weyl fermions, with a right-handed Weyl fermion contributing the negative of a left-handed one — equivalently, a right-handed field in $R$ contributes as a left-handed field in the conjugate $\bar{R}$. The consistency condition for a chiral gauge theory is

$$
\sum_{\text{left-handed}} A_{abc}(R) \;-\; \sum_{\text{right-handed}} A_{abc}(R) \;=\; 0
\qquad\text{for all } a,b,c .
$$

For an abelian factor this reduces to $\sum Y^3=0$ over the charged left-handed content, with the right-handed sign; for a simple factor it reduces to the vanishing of the appropriate cubic Casimir. Both are standard.

**The $\mathrm{SU}(2)$ factor vanishes identically.** For $SU(2)$ in any representation the symmetrised trace of three generators is zero, because there is no cubic Casimir. For the doublet with $T_a=\tfrac12\sigma_a$ the proof is one line:

$$
\{T_b,T_c\}=\tfrac14\{\sigma_b,\sigma_c\}=\tfrac12\delta_{bc}I_2 ,
\qquad
T_a\{T_b,T_c\}=\tfrac14\delta_{bc}\sigma_a ,
\qquad
\mathrm{Tr}_R\,\big[T_a\{T_b,T_c\}\big]=\tfrac14\delta_{bc}\,\mathrm{Tr}_R\,\sigma_a = 0 .
$$

The same conclusion holds for every $SU(2)$ representation: each is real or pseudoreal, the cubic invariant does not exist, and the triangle coefficient vanishes — verified on the spins $\tfrac12$, $1$, $\tfrac32$ and $2$. The step that makes this useful is the sign rule: because a left-handed doublet and a right-handed doublet contribute with opposite signs, and because each is separately anomalous only through a coefficient that is already zero, **$SU(2)$ is anomaly-free whatever its fermion content.** This is a property of the group, not of the model.

**The abelian factor.** For the central $\mathrm{U}(1)$ the coefficient is the cubic charge sum. The framework's own central phase acts as a **scalar** on the algebra and on its module: multiplication by $\exp(i\theta)$ multiplies every component of the module by the same factor, so the left- and right-handed spectra carry the *same* charge $ϙ$. The two contributions to $\sum Y^3$ therefore have equal magnitude and opposite sign,

$$
\boxed{\;\sum_{\text{L}} ϙ^3 - \sum_{\text{R}} ϙ^3 = 0\;},
$$

identically, for every module and every charge. This is the algebraic statement that the framework's abelian gauge factor is **vector-like**, and it is the reason that factor cannot be weak hypercharge: hypercharge is chiral, with independent left and right charges, and it is precisely the independent left and right charges that make the cubic sum a condition rather than a tautology. The companion articles on chiral fermions and on the Standard Model agenda make the same point.

## Gauge Anomaly Cancellation on the Standard Model Spectrum

**The conditions.** For $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$ the vanishing of the triangle coefficients gives four independent conditions on the matter content of one generation, all read with the left-handed minus right-handed convention:

$$
\sum Y=0\quad(\text{gravitational}/\mathrm{U}(1)_Y),
\qquad
\sum Y^3=0\quad(\mathrm{U}(1)_Y^3),
$$

$$
\sum_{\text{doublets}} Y=0\quad(SU(2)_L^2\,\mathrm{U}(1)_Y),
\qquad
\sum_{\text{colour}} Y=0\quad(SU(3)_c^2\,\mathrm{U}(1)_Y).
$$

The doublet sum carries the colour multiplicity of each doublet and the colour sum carries the weak multiplicity of each coloured state, so both run over all states of the multiplet. The remaining conditions vanish identically rather than by adjustment. $SU(3)_c^3$ vanishes because the colour sector is vector-like, so the left- and right-handed quark contributions cancel; $SU(2)_L^3$ vanishes because there is no cubic $SU(2)$ Casimir. Every mixed condition — two $SU(3)$ generators with one $SU(2)$, one of each, an $SU(3)$ generator with two $U(1)$ charges, and so on — contains a single trace of an $SU(3)$ or an $SU(2)$ generator as a factor, and both single traces are zero; the reason is the vanishing of a trace, not a property of any particular fermion's charges.

**The spectrum.** One generation, with hypercharge $Y=ϙ-T_3$:

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
| $SU(2)_L^2\mathrm{U}(1)_Y$ ($\sum_{\text{doublets}}Y$, colour-weighted) | $0$ |
| $SU(3)_c^2\mathrm{U}(1)_Y$ ($\sum_{\text{colour}}Y$, weak-weighted) | $0$ |

The arithmetic is instructive in one respect: the cubic sum does **not** vanish separately for left- and right-handed fields — for the left-handed content it is $-2/9$ and for the right-handed content it is also $-2/9$ — so the cancellation is a genuine left–right conspiracy and not a per-field accident. That is the sense in which the hypercharges are *fixed* by anomaly cancellation: the condition is restrictive on the assignments.

**What the conditions constrain, and what they do not.** Anomaly cancellation constrains the hypercharges, the colours, and the weak representations. It does **not** fix the values uniquely, since four homogeneous equations on several charges have a family of solutions that only further input reduces to the observed spectrum; it does not fix the overall hypercharge normalisation; it says nothing about gauge singlets; and it does **not** constrain the number of generations, because each generation contributes the sums above independently and $N_g$ copies contribute $N_g$ times zero. The framework's position is the constraint itself: it can state and verify the conditions, and it cannot select the spectrum. The companion article on the number of generations takes up the counting.

**A consistency remark on the module.** The conditions are statements about a **chiral** assignment of charges to the module $\Delta=S\oplus\bar{S}$ with independent left and right charges. The framework's own centre does not supply such an assignment; a chiral abelian symmetry can be *written* on the module, $ϙ=ϙ_LP_L+ϙ_RP_R$, and it is gauge covariant, with the companion article on chiral fermions deriving from the mass term the selection rule $ϙ_L=ϙ_R$; but it is not generated by the algebra. The Standard Model's hypercharge is therefore an input on the module, and the cancellation is verified on it rather than derived from it.

**A sterile fermion is unconstrained.** A right-handed neutrino, carrying $Y=0$ and no colour or weak charge, contributes zero to every one of the four sums. Anomaly cancellation therefore gives **no information** about the existence or the number of sterile fermions, and a gauge-singlet Majorana mass for such a field is not forbidden by any anomaly condition. This is the fermion-sector statement that makes the see-saw mechanism of the companion article possible at all: the heavy state whose mass suppresses the light neutrino mass carries no gauge quantum numbers, and the spectrum that cancels the anomalies is silent about it.

## The Framework's Own Gauge Structure is Anomaly-Free

Two statements, both exact, close the loop between the algebra and the consistency condition.

- **The central $\mathrm{U}(1)$ is vector-like and therefore anomaly-free.** The centre $\mathbb{C}_{\mathbb{B}}$ acts as a scalar; every component of every module carries the same charge, the left and right spectra coincide, and $\sum_L ϙ^3-\sum_R ϙ^3=0$ identically. The framework's abelian factor cannot produce a gauge anomaly.
- **The $\mathrm{SU}(2)$ inside $\mathbb{M}_-$ is anomaly-free identically.** Its triangle coefficient vanishes for every representation by the computation above, and the sign rule makes the statement independent of the fermion content. The framework's non-abelian factor cannot produce a gauge anomaly either.

The consequence is worth stating plainly: **the biquaternion framework's own gauge fields pass the anomaly consistency test automatically.** A gauge anomaly is a failure mode the framework does not have. What the framework also does not have is a **chiral** gauge group — a factor assigning independent left and right charges — and it is exactly the chiral factors that make anomaly cancellation a nontrivial condition. So the framework is anomaly-free for the simple reason that it is not chiral where it is gauged, and the Standard Model's nontrivial cancellation lives in the part of its group that the framework does not generate.

**The global anomaly.** There is a second consistency condition, discrete rather than perturbative: Witten's global $SU(2)$ anomaly makes an $SU(2)$ gauge theory with an odd number of Weyl doublets inconsistent, because the fermion determinant changes sign under a large gauge transformation. For the framework's $\mathrm{SU}(2)$ the fermion content on the algebra's module is not chiral, so the condition is satisfied immediately; on the Standard Model's $SU(2)_L$ the number of doublets per generation is four — three colour copies of $Q_L$ and the lepton doublet $L_L$ — which is even, so the condition is satisfied by the spectrum. The statement is standard and is recorded here as the discrete counterpart of the triangle condition.

## The Anomaly as a Topological Density

**The density is a total derivative.** In four dimensions the abelian anomaly density is the divergence of a Chern–Simons current, in the normalisation of the companion article on instantons,

$$
\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural} = \tfrac12\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} ,
\qquad
J_{\mathrm{CS},\mu} = \sum_{\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma} ,
$$

so the anomaly is invisible in the local equations of motion of the gauge field and is detected only by the charge it transports. Integrating the divergence over a region whose spatial boundary carries no flux,

$$
\Delta Q_5=\int d^4x\,\langle\tilde\nabla,\tilde J_5\rangle_{\natural}
=\frac{e^2}{16\pi^2}\int d^4x\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=\frac{e^2}{8\pi^2}\,\Delta N_{\mathrm{CS}},
\qquad
N_{\mathrm{CS}}=\int d^3x\,J_{\mathrm{CS},t'} .
$$

The axial charge therefore follows the Chern–Simons charge and changes only when the latter does — by a large gauge transformation, which in the Euclidean continuation is an instanton. This is the standard topological interpretation of the anomaly, and the companion article on instantons supplies the framework's form of the topological charge: its density is the invariant $I_2=\vec E\cdot\vec B$, whose integral over a configuration is the instanton number. In the biquaternion language the anomaly transports axial charge into the winding of the material-sector gauge field; both are framework objects, and neither needs an object beyond the algebra.

**The index.** The integrated anomaly is twice the index of the massless Dirac operator,

$$
\int d^4x\,\langle\tilde\nabla,\tilde J_5\rangle_{\natural} = 2\,\mathrm{ind}(D) ,
\qquad
\mathrm{ind}(D)=n_R-n_L ,
$$

where $D$ is the massless Dirac operator of the pair above, the module representative of $\tilde\nabla$, taken on the Euclidean continuation so that the index is defined on a compact manifold, and $n_R$ and $n_L$ are the numbers of right- and left-handed zero modes of $D$ in the background. The general statement is the Atiyah–Singer theorem, and the zero-mode count and the index theorem belong to the corpus's general gauge apparatus rather than to the fermion sector. The two facts the fermion sector uses are immediate consequences and are all that is needed here: the **integrated** anomaly is an integer, which is why the coefficient cannot be renormalised — no continuous parameter interpolates between integers — and a single unit of topological charge therefore violates the axial charge by two units per fermion flavour. The divergence identity, the density, and the integer are one statement.

**The consistency of the picture.** The three interpretations of the anomaly — the triangle diagram with its trace, the Chern–Simons divergence with its boundary charge, and the index of the Dirac operator — are three faces of one object. The triangle gives the coefficient; the total-derivative form gives its topological character; the index gives its integrality. In the framework the coefficient is the boxed Clifford trace, the density is a field invariant ($I_2$), and the integral is a winding number of the material-sector connection. The article has stated the first two and referred the third to the general apparatus.

## The Non-Abelian Anomaly and Its Consistency

**The consistency problem.** For a non-abelian gauge theory the anomalous divergence is not simply $\langle\tilde\nabla,\tilde J_a\rangle_{\natural}\propto\sum_{b,c}A_{abc}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$; the current itself is defined only up to a local polynomial in the gauge field (the Bardeen counterterm), and the requirement is not just that the coefficient vanish but that the anomaly be expressible as the transformation of a local functional — the Wess–Zumino term — so that the gauge variation of the effective action is local and the theory remains consistent. The condition on the matter spectrum is the vanishing of the symmetrised trace $A_{abc}=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ used above; the finer statement is that the anomaly is a **consistent** (Bardeen) anomaly, whose form is fixed by the Wess–Zumino consistency condition rather than by the covariant triangle alone. Both are standard, and the corpus transcribes them; the fermion sector needs only the condition $A_{abc}=0$.

**The obstruction to a covariant current.** One structural point belongs here because it is easy to state wrongly. In four dimensions the anomaly is a total derivative, yet one cannot have a current that is simultaneously **covariant** and **conserved**: the covariant current has a nonzero divergence, the conserved current is not gauge covariant, and the two differ by the Chern–Simons term. The framework's gauge currents, built on the $\mathrm{SU}(2)$ connection of the companion articles, inherit this; there is nothing in the algebra that removes it, and the resolution is the standard Bardeen counterterm, not a biquaternion identity. The condition for consistency is the vanishing of $A_{abc}$, and the framework's own $A_{abc}$ vanishes identically, so the framework never has to face the obstruction for its own gauge fields.

**Anomaly matching.** A further standard consequence is 't Hooft's anomaly matching: the anomaly coefficients of the unbroken global symmetries must be the same in the ultraviolet and in the infrared, because the anomaly is one-loop-exact and cannot be generated or destroyed by the strong dynamics. For quantum chromodynamics this is one of the constraints on the spectrum of massless composite fermions. The framework has no confinement and no composite spectrum, so it cannot use the matching conditions; it records them as a property of the anomaly that survives any dynamics, and therefore as a constraint any future framework completion would have to satisfy.

## The 't Hooft Vertex and the $\mathrm{U}(1)_A$ Problem

**The vertex.** The axial anomaly can be written as an effective interaction. For $N_f$ massless flavours, a single instanton of the colour gauge field generates a $2N_f$-fermion vertex — the 't Hooft determinant — which is chirally non-invariant:

$$
\mathcal{L}_{\text{'t Hooft}} \;\propto\; \det_{f,f'}\big(\bar{\psi}_{fL}\psi_{f'R}\big) + \text{h.c.},
$$

with one factor of each left- and each right-handed field, the determinant running over the flavour labels $f,f'$. The operator has the quantum numbers of the anomaly, it breaks the axial $\mathrm{U}(1)_A$, and it leaves the non-abelian chiral symmetry $SU(N_f)_L\times SU(N_f)_R$ intact. In the fermion sector this is the anomalous counterpart of the condensate: where the condensate breaks the axial symmetry **spontaneously**, the 't Hooft vertex breaks its axial $\mathrm{U}(1)$ subgroup **explicitly**, and the two together are what resolve the $\mathrm{U}(1)_A$ problem of quantum chromodynamics. The vertex is a six-fermion operator for $N_f=3$; the framework carries it as a product of the bilinears it already has, since each factor $\bar{\psi}_{fL}\psi_{f'R}$ is the linear chiral pairing of the mass term.

**What is not treated.** The resolution of the $\mathrm{U}(1)_A$ problem in full involves the $\theta$ parameter, the vacuum angle, and — if it is a symmetry — the axion; the $\theta$ parameter belongs to the corpus's general gauge apparatus, and the axion to the spin-$0$ subcategory. This article states only the fermion-sector fact: the anomaly generates a chirally non-invariant multifermion vertex, and the divergence identity of the section *The Axial Anomaly* is its local form.

## The Traces Involved, and the One That Is Not

**Two traces, and only two.** Every anomaly coefficient in this article is a product of two independent traces: the **Clifford trace** over the four-dimensional Dirac module, which supplies $\epsilon_{\mu\nu\rho\sigma}$ through the boxed trace, and the **gauge trace** over the representation, which supplies $A_{abc}=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$. In the abelian case the second is the cubic charge sum. The two are computed separately because they act on different indices, and the anomaly is their product.

**The chiral trace is a difference of Weyl traces.** In the block decomposition $\Delta=S\oplus\bar{S}$ with $-iR_{\vec e_z}=\mathrm{diag}(-I_2,I_2)$, and with $\mathrm{tr}_S$ the trace over the two-dimensional Weyl module, a trace with a chirality insertion splits:

$$
\mathrm{tr}\big(-iR_{\vec e_z} M\big) = -\,\mathrm{tr}_S(M_{LL}) + \mathrm{tr}_S(M_{RR}),
$$

so the chirality-weighted trace is the **difference** of the two Weyl traces. For $M=I_4$ both halves contribute their dimension and the difference vanishes, $\mathrm{tr}(-iR_{\vec e_z})=2-2=0$ — the identity that keeps the chirality-weighted trace free of an identity term, so that the anomaly is a total derivative rather than a shift of the vacuum energy. The same splitting is the algebraic origin of the left-minus-right rule: a left-handed Weyl fermion in $S$ contributes its Weyl trace with one sign and a right-handed one with the other, and the anomaly is their difference.

**The trace that is not involved.** The framework's informational trace formula, $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, is the state-and-observable pairing of the Hermitian sector $\mathbb{M}_+$: it counts the scalar part of a product with the factor $\mathrm{Tr}(e_t)=2$. It is **not** the trace that computes an anomaly. The anomaly trace is the ordinary Clifford trace over the module together with the ordinary matrix trace over the gauge representation; neither is the scalar-part pairing, and substituting one for the other would be a category error. The formula of $\mathbb{M}_+$ is used in the companion articles for expectation values of observables; the anomaly uses the traces of the module. The distinction is stated here because both are called "the trace" in the series.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The Clifford trace underlying every anomaly, the boxed $\mathrm{tr}(-iR_{\vec e_z}\,L_{e_\mu}R_{\vec e_{\tau(\mu)}}\cdots)=-4i\epsilon_{\mu\nu\rho\sigma}$ | **Supplied**, recomputed on the $24$ distinct index assignments |
| The identification $-iR_{\vec e_z}=i\omega$ of the chirality cell with the volume cell | **Supplied** by the Clifford isomorphism |
| The axial anomaly density as the framework's invariant $I_2=\vec E\cdot\vec B$ | **Supplied** (with the instanton article's normalization); the coefficient is standard |
| The exactness of the anomaly coefficient (Adler–Bardeen) | **Transcribed**; the index-theoretic reason belongs to the general gauge apparatus |
| The Standard Model's cancellation conditions and their verification | **Transcribed** and recomputed exactly |
| Anomaly-freedom of the framework's own $\mathrm{U}(1)$ and $\mathrm{SU}(2)$ | **Supplied**; vector-like centre and no cubic Casimir |
| A chiral gauge group, and the spectrum it would constrain | **Not supplied**; the centre is vector-like and the $\mathrm{SU}(2)$ acts vector-like on the module |
| The $\theta$ parameter, the $\mathrm{U}(1)_A$ problem, and the axion | **Outside**; the $\theta$ parameter belongs to the general gauge apparatus, the axion to the spin-$0$ subcategory |
| The number of generations | **Not constrained** by cancellation; treated separately |

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The body's cells under their gamma names.** Because $L_{e_t}$ is the identity, $\gamma_5=-iR_{\vec e_z}$: the chirality cell of the body is the gamma-five cell itself, and the identity $\mathrm{tr}(\gamma_5)=0$ of the traces section is its vanishing signed trace. The generator cell of the coordinate $x_\mu$ is $\gamma_\mu$, and the volume cell is $\gamma_0\gamma_1\gamma_2\gamma_3=\omega=-i\gamma_5$. The single collapse behind every simplification in the body is

$$
i\,\gamma_\mu=-L_{e_\mu}R_{\vec e_{\tau(\mu)}} ,
$$

so multiplying a generator cell by $i$ trades it for a plain one; four such cells therefore carry $i^4=+1$ and no residual unit. Under these names the boxed trace of the body is the standard five-index trace of the block below.

**The identities the body cites.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
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
The four contraction sums depend on the frame only through the squares of the cells. In the Euclidean frame, where every cell squares to $+I_4$, they are $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. In the Minkowski frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.

## Summary

An anomaly is a quantum breaking of a classical symmetry. The axial anomaly is the failure of the chiral rotation to preserve the measure; for a charged Dirac fermion its divergence is the standard Adler–Bell–Jackiw result,

$$
\langle\tilde\nabla,\tilde J_5\rangle_{\natural} = 2m\,\bar{\psi}\,R_{\vec e_z}\,\psi + \frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

where the two imaginary units of the mass term have been reduced by $i(-i)=+1$. The contraction in it evaluates to $-8\,\vec E\cdot\vec B$, so the anomaly density is $-\frac{e^2}{2\pi^2}\,I_2$, a fixed multiple of the framework's second field invariant $I_2=\vec E\cdot\vec B$: the anomaly's pseudoscalar density is the biquaternion field's own pseudoscalar invariant. The Clifford identity behind every anomaly, the boxed trace, and the identification $-iR_{\vec e_z}=i\omega$ of the chirality cell with the volume cell, are supplied by the framework's Clifford structure; the trace was recomputed on the $24$ distinct index assignments and the identification is exact.

The gauge anomaly is the triangle coefficient $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$, and its vanishing is a consistency condition on the chiral spectrum. The article verified the Standard Model's four conditions — $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$, and the colour sum — exactly, for one generation, with a left-minus-right sign convention; the cubic sum cancels by a genuine left–right conspiracy rather than per field, each chirality contributing $-2/9$.

The framework's **own** gauge structure is anomaly-free identically: the central $\mathrm{U}(1)$ is vector-like, so its cubic charge sum vanishes, and $\mathrm{SU}(2)\subset\mathbb{M}_-$ has no cubic Casimir, so its triangle coefficient vanishes for every representation. A gauge anomaly is therefore a failure mode the framework does not have — for the structural reason that the framework is not chiral where it gauges. The Standard Model's chiral spectrum, on which cancellation is nontrivial, is an input the framework hosts and constrains but does not select.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ | Centre; the vector-like abelian factor |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\,\vec e_k\partial/\partial Q_k$, $\Box=\partial^2/\partial Q_t^2+\Delta$ | Gradient and d'Alembertian, series convention |
| $L_{a}R_{b}\psi=a\psi b$ | The two-sided cells |
| $iL_{e_\mu}R_{\vec e_{\tau(\mu)}}$, $\tau(t)=x$, $\tau(k)=y$ | Generator cell of the coordinate $x_\mu$; the four carry the Clifford relations of $g$ |
| $\psi=\psi_L+\psi_R$ | Module spinor; $\psi_L$ and $\psi_R$ are its two chiral components |
| $-iR_{\vec e_z}$ | Chirality cell; equals $i\omega$ |
| $\bar{\psi}=\psi^{\dagger}iR_{\vec e_x}$ | Dirac bar on the module |
| $\Delta=S\oplus\bar{S}$, $-iR_{\vec e_z}=\mathrm{diag}(-I_2,I_2)$ | Dirac module and chirality cell |
| $\tilde\nabla\psi_R=m\psi_L$, $\tilde\nabla^{\natural}\psi_L=m\psi_R$ | The one-sided Dirac pair, one equation per chirality |
| $\tilde\nabla^{\natural}F=m\chi\bar{F}$, $\chi=-iR_{\vec e_z}$ | Two-sided Dirac equation; mass by right multiplication |
| $\omega=iR_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y}=R_{\vec e_x}L_{\vec e_x}R_{\vec e_y}L_{\vec e_y}R_{\vec e_y}L_{\vec e_z}R_{\vec e_y}=-R_{\vec e_z}$ | Volume cell; $-iR_{\vec e_z}=i\omega$ |
| $\mathrm{tr}$, $\mathrm{Tr}_R$ | Clifford trace over the module; matrix trace over the gauge representation |
| $\mathrm{tr}(-iR_{\vec e_z}\,L_{e_\mu}R_{\vec e_{\tau(\mu)}}\,L_{e_\nu}R_{\vec e_{\tau(\nu)}}\,L_{e_\rho}R_{\vec e_{\tau(\rho)}}\,L_{e_\sigma}R_{\vec e_{\tau(\sigma)}})=-4i\epsilon_{\mu\nu\rho\sigma}$ | The boxed Clifford trace behind the anomaly; the four generator cells are reduced by $i^4=+1$, and the trace was recomputed on the $24$ distinct index assignments |
| $\epsilon_{\mu\nu\rho\sigma}$, $\epsilon_{0123}=+1$ | Alternating symbol |
| $j_{\mu}=\bar{\psi}\,iL_{e_\mu}R_{\vec e_{\tau(\mu)}}\psi$, $j_{5\mu}=\bar{\psi}\,L_{e_\mu}R_{\vec e_{\tau(\mu)}}R_{\vec e_z}\psi$ | Vector and axial currents; the axial current is the reduced form of $\bar\psi\,iL R(-iR_z)\psi$ |
| $\langle\tilde\nabla,\tilde J_5\rangle_{\natural}=\sum_\mu\partial j_{5\mu}/\partial Q_\mu=2m\bar{\psi}R_{\vec e_z}\psi+\dfrac{e^2}{16\pi^2}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Axial anomaly (ABJ), with the mass term reduced by $i(-i)=+1$; the unweighted divergence |
| $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $\kappa=ϙ/\hbar$ | Non-abelian field strength, in components |
| $I_1=\vec E^2-c^2\vec B^2$, $I_2=\vec E\cdot\vec B$ | Biquaternion field invariants |
| $\tilde{F}=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Biquaternion field strength |
| $A_{abc}=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ | Triangle anomaly coefficient |
| $\sum_L-\sum_R$ | Left-handed minus right-handed anomaly sum |
| $T_a=\tfrac12\sigma_a$ | $SU(2)$ generators; $T_a\{T_b,T_c\}=\tfrac14\delta_{bc}\sigma_a$ |
| $Y=ϙ-T_3$ | Hypercharge convention |
| $D$, $\mathrm{ind}(D)=n_R-n_L$ | Massless Dirac operator of the pair; module representative of $\tilde\nabla$; its index |
| $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$ | Standard-model gauge group (standard notation, not framework objects) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $a,b,c$; $\mu,\nu$ | Internal colour and spacetime indices, both written low; every contraction over them is an explicit sum |

## Further Reading

- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, for the axial anomaly and the triangle diagram.
- J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Nuovo Cimento A* **60** (1969) 47–61, for the anomaly and its physical consequence.
- S. L. Adler and W. A. Bardeen, "Absence of higher-order corrections in the anomalous axial-vector divergence equation," *Physical Review* **182** (1969) 1517–1536, for the exactness of the one-loop anomaly.
- W. A. Bardeen, "Anomalous Ward identities in spinor field theories," *Physical Review* **184** (1969) 1848–1857, for the non-renormalisation of the anomaly and the consistent anomaly.
- C. Bouchiat, J. Iliopoulos, and P. Meyer, "An anomaly-free version of Weinberg's model," *Physics Letters B* **38** (1972) 519–523, for the hypercharge assignments required by anomaly cancellation.
- D. J. Gross and R. Jackiw, "Effect of anomalies on quasi-renormalizable theories," *Physical Review D* **6** (1972) 477–493, for the consistency condition on a chiral gauge theory.
- E. Witten, "An $SU(2)$ anomaly," *Physics Letters B* **117** (1982) 324–328, for the global (discrete) anomaly.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the triangle calculation, the trace identities, and the Standard Model cancellation conditions.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the anomaly, its topological character, and the $\mathrm{U}(1)_A$ problem.
- K. Fujikawa, "Path-integral measure for gauge-invariant fermion theories," *Physical Review Letters* **42** (1979) 1195–1198, for the path-integral derivation of the anomaly.
- M. F. Atiyah and I. M. Singer, "The index of elliptic operators: III," *Annals of Mathematics* **87** (1968) 546–604, for the index theorem that makes the anomaly coefficient topological.
