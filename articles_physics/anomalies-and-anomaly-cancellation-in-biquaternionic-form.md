# __Anomalies and Anomaly Cancellation in Biquaternionic Form__

## Introduction

An **anomaly** is a symmetry of a classical action that does not survive quantisation. The classical current is conserved by the equations of motion; the one-loop diagram that computes its divergence is not zero; and the discrepancy is not a calculational artefact but an exact, finite, one-loop effect that is not renormalised — the Adler–Bardeen theorem. Two anomalies matter for particle physics, and they play opposite roles.

- The **axial (Adler–Bell–Jackiw) anomaly** breaks a *global* symmetry that the classical theory has. It is physical: it is what makes the neutral pion decay to two photons and what makes the axial $\mathrm{U}(1)$ of quantum chromodynamics not a symmetry of the quantum theory.
- The **gauge anomaly** threatens a *local* symmetry. If the triangle diagram with three gauge currents does not vanish, the gauge theory is inconsistent: the current is not conserved, the longitudinal gauge modes do not decouple, and unitarity and renormalisability fail. A chiral gauge theory is therefore consistent only if the anomaly cancels, and the cancellation is a **condition on the matter spectrum**.

The framework's contribution is structural, and is stated at the outset.

- **Established; the density is recomputed below.** The axial anomaly is the failure of the chiral rotation to preserve the measure. Its density is built from the chirality cell, which is $i$ times the volume cell, and it is proportional to the **second invariant** $I_2=\vec E\cdot\vec B$ of the biquaternion field — the topological density computed in the companion article on instantons. The anomaly is therefore not foreign to the framework: its density is one of the framework's two field invariants.
- **Established, and recomputed below.** The anomaly coefficient of a gauge theory is the symmetrised trace $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ over the left-handed Weyl fermions. The framework's **own** gauge structure — the central $\mathrm{U}(1)$ and the $\mathrm{SU}(2)$ inside $\mathbb{M}_-$ — is anomaly-free: the central phase is vector-like, so its cubic trace cancels identically, and $\mathrm{SU}(2)$ has no cubic Casimir, so its triangle coefficient vanishes identically. The framework cannot be inconsistent by a gauge anomaly of the algebra's own gauge fields.
- **Standard, transcribed.** The anomaly cancellation conditions of the Standard Model's chiral spectrum — $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$, and the colour conditions — are standard, and the article verifies all of them generation by generation. They constrain the hypercharges and the colour assignments; they do not constrain the **number** of generations.
- **Gap, left visible.** The framework has no chiral gauge group of its own — the central phase is vector-like and the $\mathrm{SU}(2)$ acts vector-like on the algebra — so it cannot *derive* the Standard Model's chiral spectrum from which the cancellation conditions are read. It transcribes the conditions and hosts their solution; it does not select it.

**The order of the article.** A section states the anomaly as a quantum failure of a classical symmetry and fixes what the framework contributes to it and what it transcribes. A section gives the axial anomaly, its current, its density, and the identification of the density with $I_2$. A section sets out the triangle coefficient and computes the group factors. A section states the gauge cancellation conditions and verifies them on the Standard Model spectrum. A section proves the framework's own gauge structure anomaly-free. A section treats the anomaly as a topological density, a section the non-abelian consistency conditions, and a section the 't Hooft vertex. A section separates the two traces the article uses from the one it does not. A table collects what the framework supplies, transcribes, and does not supply; the closing sections are the legacy gamma section, the Summary, the Summary of Notation, and Further Reading.

**The objects, cited and not defined.** The state is an element of $\mathbb{B}$, written $\psi$. The four frame cells of the coordinates and the chirality cell of the frame are the five cells of *Matrix Representations Conventions*; the chirality cell is the one of *Special Element Conventions*, §*The Chirality Convention*, written $\mathsf{V}^{\mathrm{vol}}$, and its two values are carried by the subscript of the element, $\psi_L$ for the value $-1$ and $\psi_R$ for the value $+1$.

**The one symbol kept.** The **Dirac adjoint** $\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$ is a pairing of two states and not a cell of the frame; it is the one operator symbol the displays keep, and it is kept because a pairing has no action form.

**The derived form this article uses.** This article defines none of the cited objects. Where the body writes one of them, it writes what the cell does to an element, and that writing is the article's derived form. Written by what it does, the frame cell of the coordinate $x_\mu$ is the map $Q\mapsto i\,e_\mu Q\,\vec e_{\nu(\mu)}$, and the chirality cell is the map $Q\mapsto-i\,Q\,\vec e_z$. The two writings are one object read twice, and the rest of the article uses the second. The same objects under their gamma names are collected in the closing section *The Legacy Pauli Gamma Formulation*, and none of those names is used before it.

**The volume cell, written as an action.** The volume cell is the composite of the four frame cells, applied in the order $z,y,x,t$ with the cell of $z$ innermost. Written as actions, and with the four factors of $i$ reduced by $i^4=+1$, the composite is
$$
Q\ \xrightarrow{\ z\ }\ i\,e_zQ\,\vec e_y\ \xrightarrow{\ y\ }\ \vec e_xQ\ \xrightarrow{\ x\ }\ -i\,Q\,\vec e_y\ \xrightarrow{\ t\ }\ -Q\,\vec e_z ,
$$
the arrow labelled by a coordinate being the frame cell of that coordinate. The composite collapses to a single right multiplication, $Q\mapsto-Q\vec e_z$, and the chirality cell multiplies on the right by $-i\vec e_z$. So the chirality cell is $i$ times the volume cell, which is how the corpus states it (*Special Element Conventions*, §*The Chirality Convention*). That relation is what places the anomaly's density inside the framework rather than beside it.

**The field strength, in components.** For the abelian anomaly the field strength is $\tilde F=\tilde\nabla^{\natural}\tilde A$ in Heaviside–Lorentz units (the medium factors of *The Field-Strength Biquaternion and Its Invariants* are set to one). The alternating symbol has $\epsilon_{0123}=+1$, and in the real-time indices $t',x,y,z$ the components are

$$
F_{t'i}=E_i,
\qquad
F_{ij}=\epsilon_{ijk}B_k ,
$$

the magnetic sign being the one the field-strength article states explicitly, $F_{jk}=\epsilon_{jkl}B_l$. The only frame-dependent component is the time one: the algebra is written in the $ict'$ frame, where $Q_t=ict'$ and $F_{Q_t k}=iE_k/c$, and dropping the $i/c$ returns the real-time $F_{t'k}=E_k$. All densities below are evaluated in the real-time components. For the non-abelian factor the components are those of the companion article on non-abelian gauge fields,
$$
F_{\mu\nu}=\frac{\partial\mathcal{A}_\nu}{\partial Q_\mu}-\frac{\partial\mathcal{A}_\mu}{\partial Q_\nu}+i\kappa\,[\mathcal{A}_\mu,\mathcal{A}_\nu],
\qquad
\kappa=\frac{ϙ}{\hbar},
$$
of which
$$
\tilde F=\frac{1}{2}\sum_{\mu,\nu\in\{t,x,y,z\}}F_{\mu\nu}\,\bar e_\mu e_\nu
$$
is the biquaternion carrier, with $\bar e_\mu$ the quaternion conjugate of the unit ($\bar e_t=e_t$, $\bar e_k=-\vec e_k$). For the abelian factor the carrier is $\tilde\nabla^{\natural}\tilde A$ itself; for the non-abelian factor it is a definition read off from the components, since the commutator term is not a derivative of $\mathcal{A}$.

**The invariants.** With the field $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, the two real invariants of *The Field-Strength Biquaternion and Its Invariants* are $I_1=\vec E^2-c^2\vec B^2$ and $I_2=\vec E\cdot\vec B$, with $\vec B=\mu\vec H$, in the normalization of the instanton article. The informational trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is inherited unchanged; it is the pairing of the Hermitian sector, and the section *The Traces Involved, and the One That Is Not* keeps it apart from the two traces that compute an anomaly. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value, and the symbols $SU(3)$, $SU(2)_L$, $\mathrm{U}(1)_Y$, $Y$, $T_3$ are **standard-model notation, not framework objects**, used only where a standard structure is named.

The framework results used here are those of the companion articles:

- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological density and its identification with the invariant $I_2$.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength, the invariants $I_1$ and $I_2$, and the biquaternion norm.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral classification, the Dirac pair, and the gauge quantum numbers of the left- and right-handed fields.
- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the multiplet structure whose charge sums are the cancellation conditions.

## The Classical Symmetry and its Quantum Failure

**The mechanism, stated once.** A classical symmetry has a conserved current, $\langle\tilde\nabla,\tilde J\rangle_{\natural}=0$, by Noether's theorem. The quantum divergence is computed by inserting the current into a correlation function; at one loop the triangle diagram contributes, and the divergence receives a term that is finite as the regulator is removed. If that term is a total derivative — the divergence of a current built from the gauge field — then its integral over a closed region is a topological number, and a local counterterm, being a polynomial in the fields and their derivatives, cannot shift an integer. The symmetry is then genuinely broken, and no choice of regulator or subtraction restores it. This is the content of the Adler–Bardeen theorem: the anomaly is a one-loop effect and is exact.

**Two structural facts make the computation tractable.** First, in four dimensions the relevant diagram is a triangle with one axial and two vector currents (the axial anomaly) or three gauge currents (the gauge anomaly); higher-point diagrams do not add new anomalous terms. Second, the anomaly is a **trace** statement: the diagram's coefficient is a spinor trace times a trace of gauge generators, and each trace is computed once and for all.

**What the framework contributes here, and what it does not.** Every anomaly coefficient in the article carries $\epsilon_{\mu\nu\rho\sigma}$, and that tensor is the standard spinor trace, quoted from the standard calculation and written out under its gamma names in the closing legacy section. The framework contributes no new value for it. What it contributes is the identity of the object the trace is weighted by. The chirality that weights the anomaly is the algebra's own chirality cell $\mathsf{V}^{\mathrm{vol}}$, the same cell the mass term applies, and the density that comes out is the algebra's own invariant $I_2$. So the two ingredients of the anomaly — a chiral weight and a pseudoscalar density — are both elements of the algebra rather than objects attached to it from outside.

The chiral weight is settled by $\mathrm{tr}(\mathsf{V}^{\mathrm{vol}})=0$ in the section *The Traces Involved, and the One That Is Not*; the density is settled in the section that follows this one, where the axial current is exhibited as the insertion of the cell the mass uses.

## The Axial Anomaly

**The current and the equation it belongs to.** The corpus's Dirac pair is

$$
\tilde\nabla\psi_R=m\,\psi_L,
$$

$$
\tilde\nabla^{\natural}\psi_L=m\,\psi_R,
$$

one equation per chirality, both sides biquaternions; the first is the right-handed equation and the second is its quaternion conjugate. At $m=0$ the pair decouples,

$$
\tilde\nabla\psi_R=0,
$$

$$
\tilde\nabla^{\natural}\psi_L=0,
$$

and each equation is identical in form to the source-free Maxwell equation; the mass is what ties the two chiralities together, and it is the only term that does.

**The two-sided form, and why it is not a second dynamics.** The same physics has a two-sided representation, a single equation on the algebra,

$$
\tilde\nabla^{\natural}F=-i\,m\,\bar{F}\,\vec e_z ,
$$

for a biquaternion field $F$ — the two-sided Dirac field, not the component field strength $F_{\mu\nu}$ — with $\bar{F}$ its coefficient conjugate. The derivative acts on the left, the mass term is the chirality cell applied to $\bar{F}$, $m\,\mathsf{V}^{\mathrm{vol}}\bar{F}=-im\bar{F}\vec e_z$, and the conjugation supplies the antilinear part. The one-sided pair is the definition; the two-sided form is the representation in which the mass is a right multiplication, and the two are related by the dictionary of *The Dirac Equation in Biquaternionic Form* but are different operators: the pair is linear in the field, the two-sided equation is antilinear in its mass term. The anomaly below is read from the one-sided pair, because the axial current is a bilinear of the state and the measure is the measure of that state. What the two-sided form adds is the structural identity behind the current: the cell $\mathsf{V}^{\mathrm{vol}}$ that the mass applies is the cell the axial current inserts, so the mass term and the axial current are the two places where chirality enters.

**The currents.** For the one-sided pair, the common phase is a symmetry at every $m$, because the mass is central and passes through it, so the vector current

$$
j_{\mu}=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,\bigl(i\,e_\mu\,\psi\,\vec e_{\nu(\mu)}\bigr)
$$

is conserved at every $m$. An axial rotation assigns opposite phases to the two chiralities, so the mass term, which pairs them, is not invariant under it; the axial current therefore carries the chirality cell,

$$
j_{5\mu}=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,\bigl(e_\mu\,\psi\,\vec e_z\vec e_{\nu(\mu)}\bigr),
$$

where the $i$ of the frame cell and the $-i$ of the chirality cell have been reduced by $i(-i)=+1$. The surviving right multiplier is the product $\vec e_z\vec e_{\nu(\mu)}$, in that order: right multipliers compose in the order in which they act, and $\vec e_z\vec e_{\nu(\mu)}=-\vec e_{\nu(\mu)}\vec e_z$, so writing the pair the other way around flips the sign of the current. With $\nu(t)=x$ and $\nu(k)=y$ the product is $\vec e_y$ on the time coordinate and $-\vec e_x$ on the three space coordinates. The current is conserved only at $m=0$.

**The result.** For a Dirac fermion of electric charge $e$ in four dimensions, with $\tilde J_5=\sum_\mu j_{5\mu}e_\mu$ and with $\langle\tilde\nabla,\tilde J_5\rangle_{\natural}=\sum_\mu\partial j_{5\mu}/\partial Q_\mu$ the divergence — the plain sum, because the metric is already spent inside the frame cells, each of which squares to $\varepsilon_\mu$ times the identity, the plain weight of *Frame and Metric Conventions*, §*The Rules*, so an extra sign vector would apply it a second time —

$$
\boxed{\;\langle\tilde\nabla,\tilde J_5\rangle_{\natural} \;=\; 2m\,\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\bigl(\psi\,\vec e_z\bigr) \;-\; \frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\;}
$$

where the mass term has been reduced in the same way, $2im\,\mathsf{V}^{\mathrm{vol}}\psi=2im(-i\psi\vec e_z)=2m\,\psi\vec e_z$. The first term is the classical explicit breaking by the mass; the second is the anomaly, present even at $m=0$, and its coefficient is the standard Adler–Bell–Jackiw one, quoted from the standard literature rather than derived. The minus in front of it is bookkeeping, not physics: the standard statement carries the contraction with the upper-index symbol, and the corpus writes every index low. The next paragraph does that bookkeeping once.

**The density, with its sign and its coefficient.** With $F_{t'i}=E_i$ and $F_{ij}=\epsilon_{ijk}B_k$ the contraction evaluates exactly,

$$
\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=8\,\vec E\cdot\vec B ,
$$

so the anomaly term is

$$
-\frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=-\frac{e^2}{2\pi^2}\,\vec E\cdot\vec B ,
$$

a negative multiple of the framework's second field invariant:

$$
\boxed{\;\mathcal{A}(x)\;=\;-\frac{e^2}{2\pi^2}\,I_2\;}.
$$

**The sign, and the textbook minus.** The series writes the alternating symbol all-low, $\epsilon_{0123}=+1$, and raises no index, so its contraction of two field strengths is $+8\vec E\cdot\vec B$. The standard Adler–Bell–Jackiw equation is written with the upper-index symbol, and raising all four indices multiplies the symbol by $g^{00}g^{11}g^{22}g^{33}=-1$, so that contraction is $-8\vec E\cdot\vec B$. Term by term, then,

$$
-\frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=+\frac{e^2}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

so the boxed equation with its minus in the lower-index notation *is* the standard equation, with its plus in the upper-index notation. The density $-\frac{e^2}{2\pi^2}I_2$ is the textbook value, and what does not depend on the notation is the physics: the magnitude, the parity, and the proportionality to $I_2$ hold either way, and the overall sign is fixed by the convention that the chirality cell calls the value $+1$ right-handed.

**The biquaternion form of the density.** The companion article on instantons computes the same density and finds it a function of $I_2$ alone. Its quoted values are $\frac{2i}{c}I_2$ in the $ict'$ frame and $2I_2$ in the Euclidean continuation, for the quarter-density $\frac14\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$; the real-time value here is $2I_2$, and the $ict'$ value follows from it by the single factor $i/c$ that the substitution $F_{t'k}=iE_k/c$ contributes — each nonzero term of the contraction carries exactly one time index. The proportionality to $I_2$ is therefore the same statement in the three frames, and it is frame-independent: the anomalous divergence carries the axial current into the framework's own pseudoscalar invariant.

Three structural remarks follow. First, the density is a **pseudoscalar** — parity-odd, as $I_2$ is — which is why it can stand on the right-hand side of the divergence of an axial, parity-odd current. Second, it is a **total derivative** in the abelian case,

$$
\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=2\,\langle\tilde\nabla,\tilde J_{\mathrm{CS}}\rangle_{\natural},
\qquad
J_{\mathrm{CS},\mu}=\sum_{\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma},
$$

which is why it is not renormalised and why it is fixed by topology. Third, the axial rotation is generated by the chirality cell itself: $\psi\mapsto e^{i\alpha\mathsf{V}^{\mathrm{vol}}}\psi$. Because $i\mathsf{V}^{\mathrm{vol}}$ is the right multiplication by $\vec e_z$, the exponential is a right multiplication, $e^{i\alpha\mathsf{V}^{\mathrm{vol}}}\psi=\psi\,e^{\alpha\vec e_z}=\cos\alpha\,\psi+\sin\alpha\,\psi\vec e_z$, so the two imaginary units of $i\alpha\mathsf{V}^{\mathrm{vol}}$ reduce to a real parameter and a single right multiplier. That is why the axial current carries the chirality cell and not a separate object. The pseudoscalar character and the total-derivative form are standard; what the framework adds is that the density is the second invariant of its own field, and that the chirality cell is $i$ times the volume cell.

**The physical consequence, stated and not developed.** The anomaly makes $\pi^0\to\gamma\gamma$ possible at the observed rate and makes the axial $\mathrm{U}(1)$ of quantum chromodynamics explicitly broken at the quantum level; the $\mathrm{U}(1)_A$ problem and its resolution by the $\theta^{\mathrm{vac}}$ parameter and the axion belong to the corpus's other subcategories and are not treated here. The point for the fermion sector is the divergence identity itself: the axial current of any single massless Dirac fermion is not conserved quantum-mechanically, and no choice of regulator removes the term without moving the breaking elsewhere.

**Why the anomaly is exact.** The Adler–Bardeen theorem states that the coefficient of the anomaly is the one-loop value, unaffected by higher-order corrections. The modern reason is that the **integrated** anomaly is the index of the Dirac operator, an integer topological invariant; a continuous renormalisation cannot change an integer, so the coefficient is protected. The index statement is the subject of the general gauge apparatus and of the companion article on the Fujikawa method; here it is noted as the reason the coefficient above is stable.

## The Triangle Coefficient and the Group Factors

**Two traces, two names.** Throughout, $\mathrm{tr}$ is the trace of an operator of the algebra, in its four complex dimensions, and $\mathrm{Tr}_R$ the matrix trace over the gauge representation; the anomaly is their product. The subscript-free $\mathrm{Tr}$ appears only in the inherited informational formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, whose argument is a product of algebra elements rather than of matrices.

**The general anomaly coefficient.** For a gauge theory with generators $T_a$ acting on a left-handed Weyl fermion in a representation $R$, the coefficient of the triangle anomaly is the **symmetrised trace**

$$
A_{abc}(R) \;=\; \mathrm{Tr}_R\big[T_a\{T_b,T_c\}\big] .
$$

The anomaly is the sum over all left-handed Weyl fermions, with a right-handed Weyl fermion contributing the negative of a left-handed one — equivalently, a right-handed field in $R$ contributes as a left-handed field in the conjugate $\bar{R}$. The consistency condition for a chiral gauge theory is

$$
\sum_{\text{left-handed}} A_{abc}(R) \;-\; \sum_{\text{right-handed}} A_{abc}(R) \;=\; 0
\qquad\text{for all } a,b,c .
$$

For an abelian factor this reduces to $\sum Y^3=0$ over the charged left-handed content, with the right-handed sign. For a simple factor it reduces to the vanishing of the sum of the cubic Casimirs over the spectrum, $\sum A(R)=0$: trivial when the Casimir itself vanishes, as it does for $SU(2)$, and a genuine condition when it does not, as for $SU(3)$, where $A(3)=1$ and $A(\bar3)=-1$ in the usual normalisation. Both are standard.

**The $\mathrm{SU}(2)$ factor vanishes identically.** For $SU(2)$ in any representation the symmetrised trace of three generators is zero, because there is no cubic Casimir. For the doublet the proof is one line, and it uses only the algebra of the generators: the anticommutator of two of them is central,

$$
\{T_b,T_c\}=\tfrac12\delta_{bc}\,\mathrm I ,
$$

so

$$
T_a\{T_b,T_c\}=\tfrac12\delta_{bc}\,T_a ,
\qquad
\mathrm{Tr}_R\,\big[T_a\{T_b,T_c\}\big]=\tfrac12\delta_{bc}\,\mathrm{Tr}_R\,T_a = 0 ,
$$

the last step because every generator of $SU(2)$ is traceless. No array enters the argument.

The same conclusion holds for every $SU(2)$ representation: each is real or pseudoreal, the cubic invariant does not exist, and the triangle coefficient vanishes — verified on the spins $\tfrac12$, $1$, $\tfrac32$ and $2$. The step that makes this useful is the sign rule: because a left-handed doublet and a right-handed doublet contribute with opposite signs, and because each is separately anomalous only through a coefficient that is already zero, **$SU(2)$ is anomaly-free whatever its fermion content.** This is a property of the group, not of the model.

**The abelian factor.** For the central $\mathrm{U}(1)$ the coefficient is the cubic charge sum. The framework's own central phase acts as a **scalar** on the algebra: multiplication by $\exp(i\theta)$ multiplies every coefficient of a state by the same factor, so a state and its partner of the opposite chirality carry the *same* charge $ϙ$. The two contributions to the cubic sum are therefore $+ϙ^3$ and $-ϙ^3$, the sign being the left-minus-right rule and not a difference of charges,

$$
\boxed{\;\sum_{\text{L}} ϙ^3 - \sum_{\text{R}} ϙ^3 = 0\;},
$$

identically, for every state and every charge. This is the algebraic statement that the framework's abelian gauge factor is **vector-like**, and it is the reason that factor cannot be weak hypercharge: hypercharge is chiral, with independent left and right charges, and it is precisely the independent left and right charges that make the cubic sum a condition rather than a tautology. The companion articles on chiral fermions and on the Standard Model agenda make the same point.

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

The doublet sum carries the colour multiplicity of each doublet and the colour sum carries the weak multiplicity of each coloured state, so both run over all states of the multiplet. The remaining conditions vanish identically rather than by adjustment. $SU(3)_c^3$ vanishes because the colour content of the quarks is vector-like: writing $A$ for the cubic colour coefficient of a representation, the doublet supplies $2A(3)$ from its two components and the two right-handed quarks supply $-A(3)$ each, so the sum is $2A(3)-A(3)-A(3)=0$. $SU(2)_L^3$ vanishes because there is no cubic $SU(2)$ Casimir. Every mixed condition — two $SU(3)$ generators with one $SU(2)$, one of each, an $SU(3)$ generator with two $U(1)$ charges, and so on — contains a single trace of an $SU(3)$ or an $SU(2)$ generator as a factor, and both single traces are zero; the reason is the vanishing of a trace, not a property of any particular fermion's charges.

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

The arithmetic is instructive in one respect: the cubic sum does **not** vanish separately for left- and right-handed fields — for the left-handed content it is $-2/9$ and for the right-handed content it is also $-2/9$ — so the cancellation is a genuine left–right conspiracy and not a per-field accident. That is the sense in which anomaly cancellation *bites*: it relates an assignment to its own mirror image rather than to nothing, which is what makes the conditions restrictive rather than automatic.

**What the conditions constrain, and what they do not.** Anomaly cancellation constrains the hypercharges, the colours, and the weak representations. It does **not** fix the values uniquely, since four homogeneous equations on several charges have a family of solutions that only further input reduces to the observed spectrum; it does not fix the overall hypercharge normalisation; it says nothing about gauge singlets; and it does **not** constrain the number of generations, because each generation contributes the sums above independently and $N_g$ copies contribute $N_g$ times zero. The framework's position is the constraint itself: it can state and verify the conditions, and it cannot select the spectrum. The companion article on the number of generations takes up the counting.

**A consistency remark on the chiral assignment.** The conditions are statements about a **chiral** assignment of charges to a state, with independent charges on its two chiral parts: $ϙ_L$ on $\psi_L$ and $ϙ_R$ on $\psi_R$. The framework's own centre does not supply such an assignment; a chiral abelian symmetry can be *written* on a state by giving the two parts independent charges, and it is gauge covariant, with the companion article on chiral fermions deriving from the mass term the selection rule $ϙ_L=ϙ_R$; but it is not generated by the algebra. The Standard Model's hypercharge is therefore an input on the state, and the cancellation is verified on it rather than derived from it.

**A sterile fermion is unconstrained.** A right-handed neutrino, carrying $Y=0$ and no colour or weak charge, contributes zero to every one of the four sums. Anomaly cancellation therefore gives **no information** about the existence or the number of sterile fermions, and a gauge-singlet Majorana mass for such a field is not forbidden by any anomaly condition. This is the fermion-sector statement that makes the see-saw mechanism of the companion article possible at all: the heavy state whose mass suppresses the light neutrino mass carries no gauge quantum numbers, and the spectrum that cancels the anomalies is silent about it.

## The Framework's Own Gauge Structure is Anomaly-Free

Two statements, both exact, close the loop between the algebra and the consistency condition.

- **The central $\mathrm{U}(1)$ is vector-like and therefore anomaly-free.** The centre $\mathbb{C}_{\mathbb{B}}$ acts as a scalar; every coefficient of every state carries the same charge, the left and right spectra coincide, and $\sum_L ϙ^3-\sum_R ϙ^3=0$ identically. The framework's abelian factor cannot produce a gauge anomaly.
- **The $\mathrm{SU}(2)$ inside $\mathbb{M}_-$ is anomaly-free identically.** Its triangle coefficient vanishes for every representation by the computation above, and the sign rule makes the statement independent of the fermion content. The framework's non-abelian factor cannot produce a gauge anomaly either.

The consequence is worth stating plainly: **the biquaternion framework's own gauge fields pass the anomaly consistency test automatically.** A gauge anomaly is a failure mode the framework does not have. What the framework also does not have is a **chiral** gauge group — a factor assigning independent left and right charges — and it is exactly the chiral factors that make anomaly cancellation a nontrivial condition. So the framework is anomaly-free for the simple reason that it is not chiral where it is gauged, and the Standard Model's nontrivial cancellation lives in the part of its group that the framework does not generate.

**The global anomaly.** There is a second consistency condition, discrete rather than perturbative: Witten's global $SU(2)$ anomaly makes an $SU(2)$ gauge theory with an odd number of Weyl doublets inconsistent, because the fermion determinant changes sign under a large gauge transformation. For the framework's $\mathrm{SU}(2)$ the fermion content on the algebra is vector-like, so its Weyl doublets come in pairs and their number is even, and the condition is satisfied immediately; on the Standard Model's $SU(2)_L$ the number of doublets per generation is four — three colour copies of $Q_L$ and the lepton doublet $L_L$ — which is even, so the condition is satisfied by the spectrum. The statement is standard and is recorded here as the discrete counterpart of the triangle condition.

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
=-\frac{e^2}{16\pi^2}\int d^4x\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=-\frac{e^2}{8\pi^2}\,\Delta N_{\mathrm{CS}},
\qquad
N_{\mathrm{CS}}=\int d^3x\,J_{\mathrm{CS},t'} .
$$

The coefficient and the two minus signs are one chain: the boxed divergence carries the minus of the all-low notation, and $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=2\,\partial\cdot J_{\mathrm{CS}}$ turns the density into a divergence, so the axial charge is minus $\frac{e^2}{8\pi^2}$ times the change in Chern–Simons number. The magnitude is the standard one; only the sign of $J_{\mathrm{CS}}$ is a convention, and the article fixes it once here.

The axial charge therefore follows the Chern–Simons charge and changes only when the latter does — by a large gauge transformation, which in the Euclidean continuation is an instanton. This is the standard topological interpretation of the anomaly, and the companion article on instantons supplies the framework's form of the topological charge: its density is the invariant $I_2=\vec E\cdot\vec B$, whose integral over a configuration is the instanton number. In the biquaternion language the anomaly transports axial charge into the winding of the material-sector gauge field; both are framework objects, and neither needs an object beyond the algebra.

**The index.** The integrated anomaly is twice the index of the massless Dirac operator,

$$
\int d^4x\,\langle\tilde\nabla,\tilde J_5\rangle_{\natural} = 2\,\mathrm{ind}(D) ,
\qquad
\mathrm{ind}(D)=n_R-n_L ,
$$

where $D$ is the massless Dirac operator of the pair above, the representative of $\tilde\nabla$ on the state, taken on the Euclidean continuation so that the index is defined on a compact manifold, and $n_R$ and $n_L$ are the numbers of right- and left-handed zero modes of $D$ in the background. The general statement is the Atiyah–Singer theorem, and the zero-mode count and the index theorem belong to the corpus's general gauge apparatus rather than to the fermion sector. The two facts the fermion sector uses are immediate consequences and are all that is needed here: the **integrated** anomaly is an integer, which is why the coefficient cannot be renormalised — no continuous parameter interpolates between integers. The integer is the charge normalised with the coupling, $N=\frac{e^2}{32\pi^2}\int d^4x\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, which is what charge quantisation makes integral; the unnormalised Chern–Simons number above is related to it by $N=\frac{e^2}{16\pi^2}N_{\mathrm{CS}}$. The boxed coefficient then reads $\Delta Q_5=-2\Delta N$, so a unit of topological charge violates the axial charge by **two** units per fermion flavour — the factor two being the two chiralities the index counts as $n_R-n_L$. The divergence identity, the density, and the integer are one statement.

**The consistency of the picture.** The three interpretations of the anomaly — the triangle diagram with its trace, the Chern–Simons divergence with its boundary charge, and the index of the Dirac operator — are three faces of one object. The triangle gives the coefficient; the total-derivative form gives its topological character; the index gives its integrality. In the framework the coefficient is the standard spinor trace weighted by the chirality cell, the density is a field invariant ($I_2$), and the integral is a winding number of the material-sector connection. The article has stated the weight and the density and referred the integral to the general apparatus.

## The Non-Abelian Anomaly and Its Consistency

**The consistency problem.** For a non-abelian gauge theory the anomalous divergence is not simply $\langle\tilde\nabla,\tilde J_a\rangle_{\natural}\propto\sum_{b,c}A_{abc}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$; the current itself is defined only up to a local polynomial in the gauge field (the Bardeen counterterm), and the requirement is not just that the coefficient vanish but that the anomaly be expressible as the transformation of a local functional — the Wess–Zumino term — so that the gauge variation of the effective action is local and the theory remains consistent. The condition on the matter spectrum is the vanishing of the symmetrised trace $A_{abc}=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ used above; the finer statement is that the anomaly is a **consistent** (Bardeen) anomaly, whose form is fixed by the Wess–Zumino consistency condition rather than by the covariant triangle alone. Both are standard, and the corpus transcribes them; the fermion sector needs only the condition $A_{abc}=0$.

**The obstruction to a covariant current.** One structural point belongs here because it is easy to state wrongly. In four dimensions the anomaly is a total derivative, yet one cannot have a current that is simultaneously **covariant** and **conserved**: the covariant current has a nonzero divergence, the conserved current is not gauge covariant, and the two differ by the Chern–Simons term. The framework's gauge currents, built on the $\mathrm{SU}(2)$ connection of the companion articles, inherit this; there is nothing in the algebra that removes it, and the resolution is the standard Bardeen counterterm, not a biquaternion identity. The condition for consistency is the vanishing of $A_{abc}$, and the framework's own $A_{abc}$ vanishes identically, so the framework never has to face the obstruction for its own gauge fields.

**Anomaly matching.** A further standard consequence is 't Hooft's anomaly matching: the anomaly coefficients of the unbroken global symmetries must be the same in the ultraviolet and in the infrared, because the anomaly is one-loop-exact and cannot be generated or destroyed by the strong dynamics. For quantum chromodynamics this is one of the constraints on the spectrum of massless composite fermions. The framework has no confinement and no composite spectrum, so it cannot use the matching conditions; it records them as a property of the anomaly that survives any dynamics, and therefore as a constraint any future framework completion would have to satisfy.

## The 't Hooft Vertex and the $\mathrm{U}(1)_A$ Problem

**The vertex.** The axial anomaly can be written as an effective interaction. For $N_f$ massless flavours, a single instanton of the colour gauge field generates a $2N_f$-fermion vertex — the 't Hooft determinant — which is chirally non-invariant:

$$
\mathcal{L}_{\text{'t Hooft}} \;\propto\; \det_{f,f'}\big(\psi_{fL}^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\psi_{f'R}\big) + \text{h.c.},
$$

with one factor of each left- and each right-handed field, the determinant running over the flavour labels $f,f'$. The operator has the quantum numbers of the anomaly, it breaks the axial $\mathrm{U}(1)_A$, and it leaves the non-abelian chiral symmetry $SU(N_f)_L\times SU(N_f)_R$ intact. In the fermion sector this is the anomalous counterpart of the condensate: where the condensate breaks the axial symmetry **spontaneously**, the 't Hooft vertex breaks its axial $\mathrm{U}(1)$ subgroup **explicitly**, and the two together are what resolve the $\mathrm{U}(1)_A$ problem of quantum chromodynamics. The vertex is a six-fermion operator for $N_f=3$; the framework carries it as a product of the bilinears it already has, since each factor $\psi_{fL}^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\psi_{f'R}$ is the linear chiral pairing of the mass term.

**What is not treated.** The resolution of the $\mathrm{U}(1)_A$ problem in full involves the $\theta^{\mathrm{vac}}$ parameter, the vacuum angle, and — if it is a symmetry — the axion; the $\theta^{\mathrm{vac}}$ parameter belongs to the corpus's general gauge apparatus, and the axion to the spin-$0$ subcategory. This article states only the fermion-sector fact: the anomaly generates a chirally non-invariant multifermion vertex, and the divergence identity of the section *The Axial Anomaly* is its local form.

## The Traces Involved, and the One That Is Not

**Two traces, and only two.** Every anomaly coefficient in this article is a product of two independent traces: the **spinor trace**, over the four complex dimensions of the algebra, which supplies $\epsilon_{\mu\nu\rho\sigma}$, and the **gauge trace** over the representation, which supplies $A_{abc}=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$. In the abelian case the second is the cubic charge sum. The two are computed separately because they act on different indices, and the anomaly is their product.

**The chiral trace is a difference.** The chirality cell takes two values, and the trace of a composite with $\mathsf{V}^{\mathrm{vol}}$ is the trace on the part where the value is $-1$ minus the trace on the part where it is $+1$. The chirality-weighted trace is therefore a **difference** and not a sum, which is the algebraic origin of the left-minus-right rule: a left-handed state contributes with one sign and a right-handed one with the other, and the anomaly is their difference. On the identity action the two parts have the same dimension and the difference vanishes,

$$
\mathrm{tr}(\mathsf{V}^{\mathrm{vol}})=0 ,
$$

the identity that keeps the chirality-weighted trace free of an identity term, so that the anomaly is a total derivative rather than a shift of the vacuum energy.

**The trace that is not involved.** The framework's informational trace formula, $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, is the state-and-observable pairing of the Hermitian sector $\mathbb{M}_+$: it counts the scalar part of a product with the factor $\mathrm{Tr}(e_t)=2$. It is **not** the trace that computes an anomaly. The anomaly trace is the trace of an operator of the algebra together with the ordinary matrix trace over the gauge representation; neither is the scalar-part pairing, and substituting one for the other would be a category error. The formula of $\mathbb{M}_+$ is used in the companion articles for expectation values of observables; the anomaly uses the traces of the algebra. The distinction is stated here because both are called "the trace" in the series.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The $\epsilon_{\mu\nu\rho\sigma}$ of the anomaly | **Transcribed** from the standard spinor trace; written out under its gamma names in the legacy section, not re-derived |
| The anomaly's chiral weight as an element of the algebra: $\mathsf{V}^{\mathrm{vol}}$, the cell the mass applies and $i$ times the volume cell, with $\mathrm{tr}(\mathsf{V}^{\mathrm{vol}})=0$ | **Supplied** by the corpus's own display (*Special Element Conventions*, §*The Chirality Convention*); chirality is not an extra ingredient, and the vanishing trace is what makes the anomaly a total derivative |
| The axial anomaly density as a multiple of the framework's invariant $I_2=\vec E\cdot\vec B$ | **Supplied** (with the instanton article's normalization); the coefficient is standard, the density being $-\frac{e^2}{2\pi^2}I_2$ |
| The exactness of the anomaly coefficient (Adler–Bardeen) | **Transcribed**; the index-theoretic reason belongs to the general gauge apparatus |
| The Standard Model's cancellation conditions and their verification | **Transcribed** and recomputed exactly |
| Anomaly-freedom of the framework's own $\mathrm{U}(1)$ and $\mathrm{SU}(2)$ | **Supplied**; vector-like centre and no cubic Casimir |
| A chiral gauge group, and the spectrum it would constrain | **Not supplied**; the centre is vector-like and the $\mathrm{SU}(2)$ acts vector-like on the algebra |
| The $\theta^{\mathrm{vac}}$ parameter, the $\mathrm{U}(1)_A$ problem, and the axion | **Outside**; the $\theta^{\mathrm{vac}}$ parameter belongs to the general gauge apparatus, the axion to the spin-$0$ subcategory |
| The number of generations | **Not constrained** by cancellation; treated separately |

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The left and right multiplications act by $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and the five cells of the body become

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

$\gamma_5$ is the chirality cell of the frame under its gamma name; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The body's cells under their gamma names.** Because $L_{e_t}^{\mathrm{pau}}$ is the identity, $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$: the chirality cell of the body is the gamma-five cell itself, and the identity $\mathrm{tr}(\gamma_5)=0$ of the traces section is its vanishing signed trace. The generator cell of the coordinate $x_\mu$ is $\gamma_\mu$, and the volume cell is $\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5$. The single collapse behind every simplification in the body is

$$
i\,\gamma_\mu=-L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}} ,
$$

In the axis-free display:

$$
i\,\gamma_\mu=-L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}} ,
$$

so multiplying a generator cell by $i$ trades it for a plain one; four such cells therefore carry $i^4=+1$ and no residual unit. Under these names the five-index trace the anomaly needs is the one in the display below; the body does not state it, because its value is the standard one and this article does not re-derive it.

**The identities the body cites.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
\qquad \varepsilon=(1,-1,-1,-1),$$
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
The first display is the anticommutation relations the body's cells obey, together with the chirality cell's square and its anticommutation; the second gives the Lorentz generators $S_{cd}$ and their commutator with a generator; the last two give the traces the anomaly needs. All of them were recomputed on the module's explicit $4\times4$ representation, the five-index trace over all $4^4$ index assignments.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

An anomaly is a quantum breaking of a classical symmetry. The axial anomaly is the failure of the chiral rotation to preserve the measure; for a charged Dirac fermion its divergence is the standard Adler–Bell–Jackiw result,

$$
\langle\tilde\nabla,\tilde J_5\rangle_{\natural} = 2m\,\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\bigl(\psi\,\vec e_z\bigr) - \frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

where the two imaginary units of the mass term have been reduced by $i(-i)=+1$. The contraction in it evaluates to $+8\,\vec E\cdot\vec B$ all-low, so the anomaly density is $-\frac{e^2}{2\pi^2}\,I_2$, the textbook value, a fixed multiple of the framework's second field invariant $I_2=\vec E\cdot\vec B$: the anomaly's pseudoscalar density is the biquaternion field's own pseudoscalar invariant. The $\epsilon$ tensor of the anomaly is the standard spinor trace and is transcribed, not re-derived. What the framework supplies is the chirality of the algebra as the anomaly's chiral weight, $\mathsf{V}^{\mathrm{vol}}$ being the cell the mass applies and $i$ times the volume cell, so that the anomaly's pseudoscalar density is the algebra's own invariant $I_2$.

The gauge anomaly is the triangle coefficient $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$, and its vanishing is a consistency condition on the chiral spectrum. The article verified the Standard Model's four conditions — $\sum Y=0$, $\sum Y^3=0$, $\sum YT_3^2=0$, and the colour sum — exactly, for one generation, with a left-minus-right sign convention; the cubic sum does not vanish on either chirality alone — the raw sums are $-2/9$ for the left-handed content and $-2/9$ for the right-handed content — so it cancels only when the left-minus-right sign rule is applied.

The framework's **own** gauge structure is anomaly-free identically: the central $\mathrm{U}(1)$ is vector-like, so its cubic charge sum vanishes, and $\mathrm{SU}(2)\subset\mathbb{M}_-$ has no cubic Casimir, so its triangle coefficient vanishes for every representation. A gauge anomaly is therefore a failure mode the framework does not have — for the structural reason that the framework is not chiral where it gauges. The Standard Model's chiral spectrum, on which cancellation is nontrivial, is an input the framework hosts and constrains but does not select.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra; *Algebra and Element Conventions* |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}$ | The centre; the vector-like abelian factor |
| $\tilde\nabla$, $\Box$ | Gradient and d'Alembertian; the symbols are the conventions' (*Algebra and Element Conventions*, *Operator and Calculus Conventions*) |
| $L_{a}R_{b}$ | The two-sided cell, named only where the operator itself is the subject (*Operator Family Conventions*) |
| $Q\mapsto ie_\mu Q\vec e_{\nu(\mu)}$ | The frame cell of the coordinate $x_\mu$ by what it does; the cell is *Matrix Representations Conventions* |
| $\psi$, $\psi_L$, $\psi_R$ | The state and its two values under $\mathsf{V}^{\mathrm{vol}}$; *Special Element Conventions*, §*The Chirality Convention* |
| $\mathsf{V}^{\mathrm{vol}}:\ Q\mapsto-iQ\vec e_z$ | The chirality cell; $i$ times the volume cell |
| $\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$ | Dirac adjoint; a pairing of two states, not an action |
| $\mathrm{tr}(\mathsf{V}^{\mathrm{vol}})=0$ | The chirality-weighted trace of the identity vanishes |
| $\tilde\nabla\psi_R=m\psi_L$, $\tilde\nabla^{\natural}\psi_L=m\psi_R$ | The one-sided Dirac pair, one equation per chirality |
| $\tilde\nabla^{\natural}F=-im\bar{F}\vec e_z$ | Two-sided Dirac equation; the mass term is the chirality cell applied to $\bar{F}$ |
| $-R_{\vec e_z}^{\mathrm{axf}}$, the four frame cells composed in the order $z,y,x,t$ | The volume cell; the chirality cell is $i$ times it |
| $\mathrm{tr}$, $\mathrm{Tr}_R$ | Trace of an operator of the algebra in its four complex dimensions; matrix trace over the gauge representation |
| $\epsilon_{\mu\nu\rho\sigma}$ | Alternating symbol, written all-low with $\epsilon_{0123}=+1$; raising all four indices multiplies it by $g^{00}g^{11}g^{22}g^{33}=-1$, so the textbook's upper-index contraction is the negative of the all-low one, and the anomaly term carries an explicit minus in this notation |
| $j_{\mu}=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,(ie_\mu\psi\vec e_{\nu(\mu)})$, $j_{5\mu}=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,(e_\mu\psi\vec e_z\vec e_{\nu(\mu)})$ | Vector and axial currents; the axial current is the chirality cell inserted between the frame cell and the state, the right multiplier being $\vec e_z\vec e_{\nu(\mu)}$ in that order |
| $\langle\tilde\nabla,\tilde J_5\rangle_{\natural}=\sum_\mu\partial j_{5\mu}/\partial Q_\mu=2m\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}(\psi\vec e_z)-\dfrac{e^2}{16\pi^2}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Axial anomaly (ABJ), with the mass term reduced by $i(-i)=+1$; the minus is the lower-index notation, and the divergence is the plain sum, the metric being inside the frame cells |
| $F_{\mu\nu}=\partial \mathcal{A}_\nu/\partial x_\mu-\partial \mathcal{A}_\mu/\partial x_\nu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $\kappa=ϙ/\hbar$ | Non-abelian field strength, in components |
| $I_1=\vec E^2-c^2\vec B^2$, $I_2=\vec E\cdot\vec B$ | Biquaternion field invariants |
| $\tilde{F}=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Biquaternion field strength |
| $A_{abc}=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ | Triangle anomaly coefficient |
| $\sum_L-\sum_R$ | Left-handed minus right-handed anomaly sum |
| $T_a$ | $SU(2)$ generators; the symmetrised trace of three vanishes for every representation |
| $Y=ϙ-T_3$ | Hypercharge convention |
| $D$, $\mathrm{ind}(D)=n_R-n_L$ | Massless Dirac operator of the pair; representative of $\tilde\nabla$ on the state; its index, with $\int d^4x\,\langle\tilde\nabla,\tilde J_5\rangle_{\natural}=2\,\mathrm{ind}(D)$ |
| $N=\frac{e^2}{32\pi^2}\int d^4x\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, $N_{\mathrm{CS}}=\int d^3x\,J_{\mathrm{CS},t'}$ | Topological charge, integral by charge quantisation; $N=\frac{e^2}{16\pi^2}N_{\mathrm{CS}}$ and $\Delta Q_5=-2\Delta N$ |
| $SU(3)_c\times SU(2)_L\times \mathrm{U}(1)_Y$ | Standard-model gauge group (standard notation, not framework objects) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $a,b,c$; $\mu,\nu$ | Internal colour and spacetime indices, both written low; every contraction over them is an explicit sum |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
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
