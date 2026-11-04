# __Chiral Fermions in the Biquaternion Framework__

## Introduction

A **chiral fermion** is a fermion whose left- and right-handed components carry *inequivalent* representations of the gauge group. The **vector-like** alternative is a fermion whose two chiral components carry the same representation; a vector-like fermion may have a mass term that pairs the two components, and a chiral fermion may not. The distinction is not a technicality: the matter content of the Standard Model is chiral, with the left-handed quarks and leptons in $SU(2)$ doublets and their right-handed partners in singlets, and the immediate kinematic consequence is that no bare fermion mass is gauge invariant. The electron mass appears only after electroweak symmetry breaking, through the coupling of the two chiralities to the Higgs field, whose vacuum expectation value carries the charge that the mass term lacks.

This article asks what the biquaternion framework, in the notation of the companion articles, supplies for that structure. The presentation is organized around one question — *can the framework distinguish the two chiralities in a gauge interaction?* — and the answer is split, at the outset, into the three categories the corpus uses.

- **Established, and recomputed below.** The biquaternion Dirac field decomposes into two chiral halves; the chirality cell is $\chi:=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$, acting by $\chi\Psi=-i\,e_t\Psi\vec e_z$ and satisfying $\chi^2=I_4$, and the projectors $P_{L,R}=\tfrac12(I_4\mp\chi)$ are well defined, Lorentz invariant, idempotent, orthogonal and complete; the Dirac mass bilinear is chirality-odd and vanishes on a field of definite chirality. On the Dirac module a *chiral* abelian gauge symmetry with independent charges $ϙ_L,ϙ_R$ is consistent: the covariant derivative $D_\mu=\partial/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Ϙ$, $Ϙ=ϙ_LP_L+ϙ_RP_R$, is gauge covariant for arbitrary charges, with curvature $[D_\mu,D_\nu]=\tfrac{i}{\hbar}F_{\mu\nu}Ϙ$. The mass bilinear is gauge invariant if and only if $ϙ_L=ϙ_R$: a chiral fermion cannot carry a bare Dirac mass.
- **Established from the read list, and sharpened here.** The gauge group of the biquaternionic abelian gauge principle is the $*$-unitary part of the centre $\mathbb{C}_{\mathbb{B}}$, and a central element acts as a **scalar** on the algebra $M_2(\mathbb{C})$. A gauge group drawn from the centre therefore assigns every component the same charge: it is vector-like and cannot be chiral. Chirality requires a gauge action that is not scalar, hence non-central — the structure whose algebraic status the gauge article leaves open.
- **Gap, left visible.** The algebra's real structure $\flat=-{}^{*}$ supplies the shape of a conjugate pairing with the quantum numbers of a Majorana-type mass, but the single-field equation built on it is not a physical mass: its central-phase plane waves sit on the spacelike locus (the companion *Antilinear Structure and the Two Kinds of Mass* shows this). A physical Majorana pairing must be built on the module's charge conjugation $\mathcal C:S\leftrightarrow\bar S$. The parent's own mass term is the linear chiral pair, through which the continuous central phase passes and which preserves the vector $\mathrm{U}(1)$; it is not the antilinear pairing. Whether a given fermion uses the module's $\mathcal C$ is the question of the companion *The Neutrino and Majorana Fermions in Biquaternionic Form*. It is recorded here only for its consequence: the framework's vector-like gauge structure and the real structure's antilinear pairing do not naturally meet.

The article is organized as follows. The next section recalls the chiral decomposition of the biquaternion Dirac field and the projectors, and checks them against the mass term rather than only against the massless equation. The section after that writes the chiral gauge symmetry on the Dirac module and derives the mass selection rule. A section then determines what the algebra's centre supplies, and why it is vector-like; a section treats the mass term and the algebra's real structure; a section records an external reading of the Majorana condition and the spacetime signature; and a section separates chirality from the material/informational sector split, and what the framework supplies from what it only transcribes. Open questions close the argument, and a last section writes out the Clifford frame of the same module once, for comparison with the literature; the argument itself needs no frame.

## The Two Chiral Halves and the Projectors

The chiral decomposition is a property of the spinor module, and it is inherited unchanged from the read list. The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a single simple module $S$; the left-handed Weyl spinor is $(\tfrac12,0)$, carried by $S$, and the right-handed Weyl spinor is its complex conjugate $\bar{S}=(0,\tfrac12)$. Their direct sum

$$
\Delta \;=\; S\oplus\bar{S}\;=\;\left(\tfrac12,0\right)\oplus\left(0,\tfrac12\right),
\qquad \dim_{\mathbb{C}}\Delta = 4,
$$

is the **Dirac spinor module**. Written in blocks, a Dirac spinor is

$$
\Psi = \begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix}, \qquad \psi_L\in S,\quad \psi_R\in\bar{S},
$$

and $SL(2,\mathbb{C})$ acts block-diagonally, $\Psi\mapsto\big(g\,\psi_L,\ \mathsf{M}_2(\bar{\tilde U})\,\psi_R\big)$, where $g=\mathsf{M}_2(\tilde U)$; the bar is coefficient conjugation, so $\bar{\tilde U}=(\tilde U^{*})^{\natural}$, and for a unit-norm $\tilde U$ the second block is the inverse conjugate transpose of the first, $\mathsf{M}_2(\bar{\tilde U})=(g^{\dagger})^{-1}$. That last identity is what makes $\psi_L^{\dagger}\psi_R$ invariant, and with it the mass bilinear of the next section.

The **chirality cell** on $\Delta$ is the two-sided multiplier by $e_t$ on the left and by $\vec e_z$ on the right. With $L_a\Psi=a\Psi$, $R_b\Psi=\Psi b$ and $L_aR_b$,

$$
\chi \;:=\; -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} \;=\; -iR_{\vec e_z}^{\mathrm{axf}},
\qquad
\chi\Psi \;=\; -i\,e_t\,\Psi\,\vec e_z,
\qquad
\chi^{2} \;=\; I_4,
$$

where the last identity uses $i^2=-1$, $e_t=1$ and $\vec e_z^{\,2}=-e_t$. The **chiral projectors** are the cells

$$
P_L \;=\; \tfrac12\left(L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}+i\,L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\right) \;=\; \tfrac12\left(I_4-\chi\right),
\qquad
P_R \;=\; \tfrac12\left(L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}-i\,L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\right) \;=\; \tfrac12\left(I_4+\chi\right),
$$

or, on the module,

$$
P_L\Psi \;=\; \tfrac12\left(\Psi+i\,\Psi\vec e_z\right),
\qquad
P_R\Psi \;=\; \tfrac12\left(\Psi-i\,\Psi\vec e_z\right).
$$

Their elementary algebra is exact:

$$
P_L^2 = P_L, \qquad P_R^2 = P_R, \qquad P_LP_R = P_RP_L = 0, \qquad P_L+P_R = I_4, \qquad \chi = P_R-P_L,
$$

and each is Hermitian of trace $2$, so each projects onto a complex two-dimensional half: in the basis where the chirality cell is diagonal, $P_L\Psi=(\psi_L,0)$ and $P_R\Psi=(0,\psi_R)$. The four generator cells of the coordinate directions are $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ and $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, and they satisfy

$$
iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}} iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}} + iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}} iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}} = 2g_{\mu\nu}I_4,
$$

with $g=\mathrm{diag}(-,+,+,+)$. The chirality cell anticommutes with each generator,

$$
\chi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}+iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\chi=0,
$$

so $\chi$ grades the Clifford set of generator cells: it anticommutes with the generators and commutes with every even product of them. The commutation with the Lorentz action follows at once, because that action is generated by the bivector cells, products of two generator cells. (It is also immediate from the form of $\chi$: a right multiplier commutes with every left multiplier.) Hence $\chi$ commutes with each $P_{L,R}$.

Here $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}$ is the generator cell of the coordinate $x_\mu$, with $\tau(t)=x$ and $\tau(k)=y$; the companion articles denote the same map by $\nu$.

**Lorentz invariance, with or without a mass.** A projector is easy to check on the equation that suggested it, namely the massless Dirac equation, where the two halves decouple and the projector merely selects one of the two resulting Weyl equations. The claim that survives the mass term is different, and it is the one worth stating: chirality is carried by the cell $\gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}$, which commutes with every Lorentz generator, so it is **Lorentz-invariant** and not a property of the massless limit. The Lorentz generators are the bivector cells, products of two generator cells, $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}}$, and $\chi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}} iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}}=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}}\,\chi$ holds identically, with or without a mass. The mass does not enter the commutator that makes chirality Lorentz invariant; what the mass does is to make the two halves visible to each other, and that is a statement about the equation, not about the invariance of the label.

**What the mass term does to a chirality-definite state.** Let $\bar{\Psi} = \Psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}}$, the adjoint built with the time-like generator cell $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$. In a basis in which the chirality cell is diagonal and $iR_{\vec e_x}^{\mathrm{axf}}$ swaps the two blocks identically, $iR_{\vec e_x}^{\mathrm{axf}}(\psi_L,0)=(0,\psi_L)$ and $iR_{\vec e_x}^{\mathrm{axf}}(0,\psi_R)=(\psi_R,0)$,

$$
\bar{\Psi}\Psi = \Psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}}\Psi = \psi_L^{\dagger}\psi_R + \psi_R^{\dagger}\psi_L,
$$

the **Dirac mass bilinear**. Since $iR_{\vec e_x}^{\mathrm{axf}}$ anticommutes with $\chi$, it maps each chiral half into the other, and the bilinear is off-diagonal in the chiral blocks: it pairs $\psi_L$ with $\psi_R$ and never a half with itself. Under the discrete chirality transformation $\Psi\mapsto \chi\Psi$ one has $\bar{\Psi}\mapsto-\bar{\Psi}\chi$, since $\chi$ is Hermitian and $iR_{\vec e_x}^{\mathrm{axf}}\chi=-\chi\,iR_{\vec e_x}^{\mathrm{axf}}$, so

$$
\bar{\Psi}\Psi \;\longmapsto\; (-\bar{\Psi}\chi)(\chi\Psi) = -\bar{\Psi}\Psi :
$$

the mass bilinear is **chirality-odd**. Equivalently, if $\Psi$ has definite chirality, $\chi\Psi=\pm\Psi$, then the two blocks are $\Psi=( \psi_L,0)$ or $(0,\psi_R)$ and

$$
\bar{\Psi}\Psi = 0 .
$$

A field of definite chirality has no Dirac mass bilinear at all. This is the precise sense in which a lone Weyl field cannot carry a **Dirac** mass, and it is the algebra behind the Standard Model's chiral matter. It is not a statement that such a field is massless: a Majorana mass pairs the field with its own conjugate and needs no second chirality, which is why it is built on the charge conjugation below rather than on $\bar{\Psi}\Psi$.

**Framework caution.** Chirality is not visible to the algebra $\mathbb{B}$ alone. The algebra is simple, with one simple module; the element $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and it carries the two associated idempotents $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$, whose sum is $e_t$; the two minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$ and carry the *same* defining representation. The chiral halves are $S$ and $\bar{S}$, and the distinction between them is a **conjugation** distinction: it appears only when complex conjugation is taken into account, or when the algebra is complexified, where the central idempotents

$$
e_\pm=\tfrac12\left(e_t\pm\chi_{\mathrm{ad}}\right),
\qquad
\chi_{\mathrm{ad}}:=i\tilde\Xi_{\mathrm{ad}},
\qquad
\tilde\Xi_{\mathrm{ad}}^2=-e_t,
$$

split

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B} \;\cong\; M_2(\mathbb{C})\oplus M_2(\mathbb{C})
$$

into the two chiralities. Here $\chi_{\mathrm{ad}}$ is the abstract central sign of the complexification, the difference $e_+-e_-$; on the Dirac module it is represented by the frame cell $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$, so that $e_\pm$ correspond to $P_R$ and $P_L$. Which summand is called left is a labelling convention; the intrinsic statement is that the two are a conjugate pair.

**A biquaternion $\tilde{\Psi}\in\mathbb{B}$ therefore carries no chirality label of its own.** The chirality cell does act on $\mathbb{B}$, but it splits it into the two Peirce summands $\mathbb{B}\tilde\Pi_\pm$, which are two copies of $S$ and not $S$ and $\bar{S}$. It is the module object $\Psi\in\Delta$ that carries the label, and the operation that relates the two halves is the module's charge conjugation $\mathcal C$, an antilinear map — a real-form operation distinct from the parent's mass term (the linear off-diagonal chiral pair) and from the algebra's order-reversing real structure $\flat$.

Two things must be kept apart. The projectors themselves need no complexification: $R$ is complex-linear, so $iR_{\vec e_z}^{\mathrm{axf}}=R_{i\vec e_z}^{\mathrm{axf}}$ and

$$
P_L=\tfrac12\left(I_4+iR_{\vec e_z}^{\mathrm{axf}}\right)=R_{\tilde\Pi_+},
\qquad
P_R=R_{\tilde\Pi_-},
$$

right multiplications by elements of $\mathbb{B}$. What $\mathbb{B}$ does not contain is a non-trivial **central** idempotent, because it is simple; the central idempotents $e_\pm$ live in the complexification, and the same cells are their representatives on $\Delta$. Nothing below depends on which reading is taken.

## Chiral Gauge Symmetry on the Dirac Module

The gauge principle of the read list localizes a **central** phase: $\lambda=\exp(iϙ\Gamma(\tilde{Q})/\hbar)$, with $ϙ$ a single coupling, and it produces a covariant derivative $D=\tilde{\nabla}+\tfrac{iϙ}{\hbar}\tilde{A}$. A single coupling acts on the whole Dirac field; to make the gauge action *chiral* we must let the two halves carry independent charges. On the module this is elementary, and we write it out because the selection rule below is read off from it.

Introduce a real scalar gauge function $\Gamma(\tilde{Q})$ and two real charges $ϙ_L, ϙ_R$, and set

$$
Ϙ \;=\; ϙ_L P_L + ϙ_R P_R \;=\; \begin{pmatrix} ϙ_L I_2 & 0\\ 0 & ϙ_R I_2\end{pmatrix},
\qquad
\Lambda(\tilde{Q}) \;=\; \exp\!\left(\frac{i}{\hbar}\,\Gamma(\tilde{Q})\,Ϙ\right) \;=\; \begin{pmatrix} \exp(iϙ_L\Gamma/\hbar)I_2 & 0\\ 0 & \exp(iϙ_R\Gamma/\hbar)I_2\end{pmatrix}.
$$

The gauge transformation is $\Psi\mapsto\Lambda\Psi$, and the connection transforms as $A_{2,\mu}=A_\mu-\partial/\partial Q_\mu\Gamma$, exactly as in the abelian gauge principle. The covariant derivative is the module operator

$$
\boxed{\;D_\mu \;=\; \partial/\partial Q_\mu + \frac{i}{\hbar}\,A_\mu\,Ϙ\;}
$$

and it is covariant, $D_{2,\mu}(\Lambda\Psi)=\Lambda\,D_\mu\Psi$, for the derivative $D_2$ built from $A_{2,\mu}$. The check is a two-line computation:

$$
\begin{aligned}
D_{2,\mu}(\Lambda\Psi)
&= \partial/\partial Q_\mu(\Lambda\Psi) + \frac{i}{\hbar}A_{2,\mu} Ϙ\,\Lambda\Psi
= \frac{i}{\hbar}(\partial/\partial Q_\mu\,\Gamma)Ϙ\,\Lambda\Psi + \Lambda\,\partial/\partial Q_\mu\,\Psi + \frac{i}{\hbar}(A_\mu-\partial/\partial Q_\mu\,\Gamma)Ϙ\,\Lambda\Psi \\
&= \Lambda\,\partial/\partial Q_\mu\,\Psi + \frac{i}{\hbar}A_\mu Ϙ\,\Lambda\Psi
= \Lambda\,D_\mu\Psi,
\end{aligned}
$$

where the second step uses that $\Lambda$ is diagonal and $Ϙ$ is constant, so that $\partial/\partial Q_\mu\,\Lambda=\tfrac{i}{\hbar}(\partial/\partial Q_\mu\,\Gamma)Ϙ\Lambda$ and $Ϙ$ commutes with $\Lambda$. This holds for **arbitrary** $ϙ_L,ϙ_R$. The curvature is likewise weighted by the charge operator,

$$
[D_\mu,D_\nu] \;=\; \frac{i}{\hbar}\,F_{\mu\nu}\,Ϙ, \qquad F_{\mu\nu} = \partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu ,
$$

which is the abelian curvature of the one connection $A_\mu$, distributed between the two chiralities by $Ϙ$.

Two structural remarks belong here, because they distinguish this construction from the framework's own gauge principle.

1. **The chiral connection multiplies from the right, not from the left.** Writing $I_4=P_L+P_R$ and $\chi=P_R-P_L$ gives $Ϙ=\tfrac{ϙ_L+ϙ_R}{2}I_4+\tfrac{ϙ_R-ϙ_L}{2}\chi$. Both terms are right multiplications by biquaternions, $I_4=R_{e_t}^{\mathrm{axf}}$ and $\chi=R_{-i\vec e_z}^{\mathrm{axf}}$, so for real charges

$$
Ϙ=R_b,\qquad b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}\left(ϙ_R-ϙ_L\right)\vec e_z\in\mathbb{M}_+,
$$

and $A_\mu Ϙ=R_{A_\mu b}$. What fails is the **side**, not the algebra: the parent's derivative is $\tilde{\nabla}+\tfrac{iϙ}{\hbar}\tilde{A}$, a left multiplication, whereas this one is a right multiplication. The two agree only for a central multiplier, and $b$ is central only when the $\vec e_z$ term vanishes. So in this realization the chiral connection takes the parent's form $\tilde{\nabla}+\tfrac{iϙ}{\hbar}\tilde{A}$ with $\tilde{A}\in\mathbb{B}$ **exactly when $ϙ_L=ϙ_R$** — the same condition as the mass selection rule, which is no accident: the vector-like case is the one in which the charge is central and can be written without choosing a side, while the chiral case cannot. A right multiplier commutes with every left multiplier, so the chiral weighting never enters a left-multiplied equation, and the two structures sit on the field without interfering.
2. **The abelian chiral connection is genuinely scalar in the curvature.** Since $Ϙ$ is constant, the components commute in the abelian case, and the curvature is the ordinary $F_{\mu\nu}$; the chirality enters only through the charge weighting. A non-abelian chiral connection would additionally require $Ϙ$ to be replaced by generators that do not commute, which is the gap treated in the next section.

**The mass selection rule.** The scalar Dirac bilinear of the preceding section is the Lorentz-invariant pairing of the two halves available to a mass term. Under the chiral gauge transformation,

$$
\psi_L \longmapsto \exp(iϙ_L\Gamma/\hbar)\psi_L, \qquad \psi_R \longmapsto \exp(iϙ_R\Gamma/\hbar)\psi_R,
$$

so that the coefficient of $\psi_L^{\dagger}\psi_R$ acquires a position-dependent phase while its conjugate acquires the inverse phase. Since $\bar{\Psi}\Psi$ is real and equals $2\,\mathrm{Re}(\psi_L^{\dagger}\psi_R)$,

$$
\bar{\Psi}\Psi
\;\longmapsto\;
2\,\mathrm{Re}\!\left(\exp(\frac{i}{\hbar}(ϙ_R-ϙ_L)\Gamma)\,\psi_L^{\dagger}\psi_R\right),
$$

which is position dependent unless the phase is unity. The bilinear is gauge invariant for all gauge functions $\Gamma$ **if and only if**

$$
\boxed{\;ϙ_R = ϙ_L\;}
$$

This is the **mass selection rule**: a bare Dirac mass is compatible with the gauge symmetry exactly when the two chiralities carry the same charge, i.e. exactly when the fermion is vector-like. A genuinely chiral fermion, $ϙ_R\neq ϙ_L$, has no gauge-invariant bare mass; its mass must wait for a field carrying the compensating charge $ϙ_L-ϙ_R$ (the mass bilinear acquires the phase $\exp(i(ϙ_R-ϙ_L)\Gamma/\hbar)$), which is what the Higgs mechanism supplies. The rule was checked on both branches: it holds for all $\Gamma$ when $ϙ_L=ϙ_R$ (the vector-like case, including $ϙ_L=ϙ_R=0$), and it fails for the chiral case $ϙ_L\neq ϙ_R$, including the axial assignment $ϙ_R=-ϙ_L$. In particular the rule is not merely "some charge is preserved": an axial $\mathrm{U}(1)$, which carries opposite charges on the two halves and is the natural first guess for a chiral symmetry, does not preserve the mass either.

**No opposite-chirality partner.** A field of definite chirality has $\bar{\Psi}\Psi=0$ identically, so even before the gauge symmetry is imposed there is nothing for the mass to multiply. The two statements — the bilinear vanishes on a chiral state, and it is not gauge invariant when the charges differ — are the algebraic form of the single physical fact that a chiral fermion is massless in the unbroken phase.

## What the Centre Supplies: A Vector-Like Abelian Sector

The gauge group of the biquaternionic abelian gauge principle is not chosen; it is the **$*$-unitary part of the centre** of the algebra,

$$
\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t,\,ie_t\}, \qquad \mathrm{U}(1) = \{\exp(i\theta) : \theta\in\mathbb{R}\} \subset \mathbb{C}_{\mathbb{B}}.
$$

A central element commutes with every biquaternion, and this is what makes the construction abelian. Centrality is also where the two sides of the multiplication coincide, $L_\lambda=R_\lambda$ for $\lambda\in\mathbb{C}_{\mathbb{B}}$, while $L_a\neq R_a$ for a non-central $a$; only a central charge can ride on a left multiplication, which is the form the parent's connection takes. On the matrix algebra $M_2(\mathbb{C})$, left multiplication by a central element $\lambda$ is multiplication by a **scalar**,

$$
M \;\longmapsto\; \lambda M, \qquad \lambda = \exp(i\theta),
$$

so that every entry, and in particular every column of $M$, acquires the same factor. The two columns are the regular module's two copies of $S$. A gauge group drawn from the centre therefore acts by a scalar on the matter module: it assigns every component the **same** charge. Such a group cannot distinguish $\psi_L$ from $\psi_R$, and it cannot be the source of a chiral gauge interaction. The abelian sector of the framework is **vector-like**.

The converse statement is the useful one. A *chiral* gauge action has $ϙ_L\neq ϙ_R$; by the argument above it cannot be central, and a non-central gauge group is not supplied by the biquaternionic gauge principle, whose group is the centre. (The abelian chiral structure of the preceding section acts on the module, not by an element of $\mathbb{B}$ — structural remark 1.) The centre supplies a canonical abelian gauge group and nothing chiral; chirality requires a non-central, module-realised action whose algebraic status the read-list gauge article leaves open. There the gap is that the Lie algebra of $\mathbb{B}\cong M_2(\mathbb{C})$, read as an associative algebra, is $\mathfrak{gl}(2,\mathbb{C})$ — its traceless part $\mathfrak{sl}(2,\mathbb{C})$ is not compact — so that a reality and tracelessness condition must select a compact gauge algebra before a Yang–Mills structure can be claimed. The present article inherits that gap and sharpens its meaning: **without those conditions the framework has no chiral gauge group at all, because the only gauge group it supplies canonically is the scalar centre.**

**A qualification about the two interpretations of the phase.** The argument above is robust in one direction: a gauge group *drawn from the centre* is scalar and hence vector-like on the algebra. But the corpus does not settle how the biquaternion field is identified with the Dirac module, and the qualification is worth stating rather than hiding. The left regular module is $S\oplus S$, whose two columns both carry the defining representation; the Dirac module is $S\oplus\bar{S}$, whose second factor carries the conjugate action. The passage between them is **complex conjugation** — equivalently, the module's charge conjugation $\mathcal C$ — and under the Lorentz action the conjugate factor transforms by $\mathsf{M}_2(\bar{\tilde U})$. Applied to a central phase $\lambda=\exp(i\theta)$ this assignment would give $\exp(i\theta)$ on the left-handed half and $\mathsf{M}_2(\bar\lambda)=\exp(-i\theta)$ on the right-handed half — an **axial**, not vector-like, action. Which interpretation is the physical one is the same unsettled question as the module structure of the field (the "two-$i$" point), and the present article does not decide it. What is decided is the implication: the centre cannot supply *independent* left and right charges, whichever interpretation of the phase is adopted — under the vector-like interpretation the two charges are equal, and under the axial interpretation they are locked to the single ratio $ϙ_R=-ϙ_L$ — so the centre can act axially, but never with independent charges, and cannot be the source of a general chiral gauge group. (The centre is the complex line $\mathbb{C}e_t$: two real dimensions, one complex, and its $*$-unitary part is a circle.) The non-central gap is therefore a prerequisite for a general chiral gauge sector under either interpretation.

## The Mass Term and the Real Structure

The biquaternion Dirac equation of the parent is a pair of one-sided equations,

$$
L_{\tilde{\nabla}}\tilde{\Psi}_R=m\,\tilde{\Psi}_L,
\qquad
L_{\tilde{\nabla}^{\natural}}\tilde{\Psi}_L=m\,\tilde{\Psi}_R,
$$

with $\tilde{\Psi}_L\in S$, $\tilde{\Psi}_R\in\bar{S}$, and $L_{\tilde{\nabla}}\tilde{\Psi}=\tilde{\nabla}\tilde{\Psi}$. The first is the right-handed equation. The second carries $\tilde{\nabla}^{\natural}$ rather than $\tilde{\nabla}$ because the left-handed field is the conjugate of the right-handed one; $\natural$ is the order-reversing anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$, $\mathbb{C}$-linear, fixing $e_t$ and negating the spatial units. They are the two lines of one chiral pair, not two independent dynamics: eliminating one half gives the massive Klein–Gordon equation, and in the massless case the lines decouple into the Weyl equations $\tilde{\nabla}\tilde{\Psi}_R=0=\tilde{\nabla}^{\natural}\tilde{\Psi}_L$. The pair is complete as written; no second field is needed.

The same equation, read on the whole algebra rather than on the module, has the two-sided form

$$
L_{\tilde{\nabla}^{\natural}}F
= m\,L_{e_t}^{\mathrm{axf}}R_{-i\vec e_z}^{\mathrm{axf}}\bar{F}
= m\,\chi\bar{F},
$$

where $\bar{F}$ is the coefficient conjugate. The derivative acts on the left, the mass on the right through the chirality cell, and the conjugation supplies the antilinear part. This is the operator-theoretic content of the two-sidedness: the second field of the $\natural$-side equation is the conjugate of the first, $-i\bar{F}\vec e_z$. The one-sided pair is the definition; the two-sided form is the representation in which the mass is a right multiplication. The mass term in the two-sided display is antilinear in $F$, because it carries $\bar{F}$; the dictionary is $\mathbb{R}$-linear and the central phase acts on the right, so the $\mathrm{U}(1)$ statement below is read from the one-sided pair.

The **one-sided** mass term is linear in the field and off-diagonal in chirality. Because the one-sided form is linear, the central phase passes through it: under the global phase $\tilde{\Psi}\mapsto\lambda\tilde{\Psi}$ both sides acquire the same factor $\lambda$, so the continuous $\mathrm{U}(1)$ (fermion number) is conserved for the massive field, not only for the massless one. What the mass term breaks is the **axial** symmetry: for the spinor-module field,

$$
\sum_\mu \frac{\partial j_{5\mu}}{\partial Q_\mu}
= 2im\,\bar{\Psi}\,\chi\Psi,
\qquad
j_{5\mu}=\bar{\Psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\chi\,\Psi,
$$

and the right-hand side vanishes only at $m=0$. The vector current is conserved at every $m$, the axial current only at $m=0$. The mass term is also what distinguishes the massive biquaternionic equation from the massless one, which is identical in form to the source-free Maxwell equation.

The algebra carries, besides the conjugations used above, the **anti-Hermitian conjugation** $\flat=-{}^{*}$ and its role as the algebra's **real structure**:

$$
\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{*},
$$

a $\mathbb{C}$-**antilinear** involution, order-reversing with a sign, $\left(\tilde{Q}\tilde{Q}_3\right)^{\flat}=-\tilde{Q}_3^{\flat}\tilde{Q}^{\flat}$, fixing the anti-Hermitian sector $\mathbb{M}_-$ and negating the Hermitian sector $\mathbb{M}_+$; its fixed space is $\mathbb{M}_-$. A coupling built on $\flat$ pairs the algebra field with its **conjugate** rather than with an independent field of the same charge, and its phase behaviour is the opposite of a linear term's: since $\lambda^{\flat}=-\bar\lambda$ for a central phase, $(\lambda F)^{\flat}=\bar\lambda F^{\flat}$, so an antilinear piece of an equation transforms with $\bar\lambda$ while the derivative piece transforms with $\lambda$. The two match only when $\lambda=\bar\lambda$, that is $\lambda=\pm1$: the continuous central phase is broken to a sign. In the standard classification this has the quantum numbers of a **Majorana-type** mass: it is allowed only for a neutral fermion, and it breaks the continuous fermion-number $\mathrm{U}(1)$ to a sign. A mass that pairs $\psi_L$ with an independent $\psi_R$ of equal charge is a **Dirac** mass, and it preserves that $\mathrm{U}(1)$. The parent's mass is of the second type — the linear off-diagonal pair above, whose bilinear $\bar{\Psi}\Psi=\psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ carries the selection rule of the preceding section.

A coupling of the first type is a separate equation built on the real structure, $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$. The companion article *Antilinear Structure and the Two Kinds of Mass* shows that its central-phase plane waves sit on the spacelike locus rather than on the physical mass shell, so the single-field equation is not a physical mass. What $\flat$ supplies is the **shape** of a conjugate pairing on the algebra, not a fermion-number-breaking mass on the module. The operation that exchanges the two chiral halves is the module charge conjugation $\mathcal C:S\leftrightarrow\bar{S}$, not $\flat$: $\flat$ is order-reversing and acts with opposite signs on the two sectors $\mathbb{M}_\pm$, while $\mathcal C$ is the antilinear map between the halves. A physical Majorana mass must be built on $\mathcal C$.

**What remains open is not the algebra's pairing but its physical use.** The $\flat$-pairing has the quantum numbers of a Majorana mass; the single-field equation built on it does not describe a physical fermion. Whether a given fermion — the neutrino in particular — uses the module's $\mathcal C$ is the question of *The Neutrino and Majorana Fermions in Biquaternionic Form*, together with the parent Dirac article's open question 1, which asks what the real structure $\flat$ means in terms of the electroweak interaction. (The gauge article records the same pairing question inside its open question 5, alongside the axial symmetry.)

What this article adds is the connection to chirality, and it is the equation-side form of the vanishing of the Dirac bilinear: a physical Majorana coupling pairs the field with its module conjugate $\mathcal C\Psi$, not with the algebra conjugate $\tilde\Psi^\flat$, and the parent's mass term, being the linear off-diagonal pair, conserves the vector $\mathrm{U}(1)$ and fails exactly the axial one.

## An External Reading of the Majorana Condition and the Spacetime Signature

An external source reaches this article's own question — which mass terms the algebra allows, and on which signature — from a direction that shares none of the corpus's conventions, and it is worth recording because it exhibits the signature-dependence independently. D. J. Cirilo-Lombardo (*Algebraic structures, physics and geometry from a Unified Field Theoretical framework*, arXiv:1411.5493v3 [hep-th], 2015) performs Majorana's 1937 transformation on the structural group of his own unified field theory, and states his aim in the terms this article uses: to obtain a transformation for which the Dirac equation becomes real-coefficient and symmetric "for both: fermions and antifermions."

**What was verified, and what was not.** The transformation is the Weyl-basis charge conjugation $U = \tfrac{1}{\sqrt2}\left(\begin{smallmatrix}\sigma_0 & \sigma_2\\ \sigma_2 & -\sigma_0\end{smallmatrix}\right)$. It is $*$-unitary and involutive, $U^\dagger U = U^2 = I_4$, and it achieves its stated purpose: the transformed structural group $G_2 = UGU^{-1}$ is **real and symmetric**, because the source's transformed generators are purely imaginary while his own coefficients are purely imaginary too. That is a genuine Majorana condition, reached independently of this article's route. Three printed slips are recorded with it, and all three concern the source's own displays rather than the transformation: the generators of his Eq. (28) are not a Clifford set until a sign is restored, the time-like member being $\sigma_0\oplus(-\sigma_0)$; the diagonal block of his printed $G_2$ carries the wrong sign in its $(\sigma_3a_1\pm\sigma_1a_3)$ combination; and the sentence that $G_2$ and its transpose satisfy $G_2^{\mathsf T}G_2 = I_4$ does not reproduce — the identity that holds is the quaternionic one *before* the transformation. The full record is in *The Biquaternion Basis of a Unified-Field Fibre Bundle*.

**The signature dependence, and what it does not add.** The source asserts that the availability of a Majorana representation is tied to the spacetime signature, and here the corpus has already said more: in *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint* the reality type of the spinor module is a function of the signature modulo eight, the **internal** module $S$ is of complex type and carries no reality structure — it has the charge conjugate $\bar S$, but no Majorana partner inside itself — and the **ambient** four-dimensional module does carry a real structure in this signature, namely the module charge conjugation $\mathcal C$. That classification is what this article's third open question reflects: a Majorana-type coupling must be built on $\mathcal C$, on the ambient module, and cannot be manufactured inside the internal factor. The algebra's $\flat$-pairing has the right shape, but its single-field equation is not a physical mass, as recorded above. The source states the dependence and gives no table; the corpus's table is the contribution, and the source's Section V is an external worked instance of it.

**The non-Hermitian claim, kept apart.** The source also reports **non-Hermitian (CP) dynamic operators** as a structural feature. The corpus's translation separates two things: the source's own structural object is Hermitian — it is a biquaternion of $\mathbb{M}_+$ — and the non-Hermiticity the paper flags belongs to the *generalized momentum* of its second, $(2{+}2)$ sector, where the paper itself notes that $E^2+H^2$ can be negative. So the claim does not put a non-Hermitian generator into the chirality structure this article uses; the Born rule here is still the Hermitian form of a Hermitian idempotent, read through the trace, and the assertion is recorded as one about that other sector rather than about the algebra. Its algebraic engine is the split real form of the Pauli triple, $(\sigma_1,-i\sigma_2,\sigma_3)$: the middle generator squares to $-I_2$ while $\sigma_3$ squares to $+I_2$, so the source's unit-norm condition changes from $a_0^2+a_1^2+a_2^2+a_3^2=1$ to $a_0^2+a_1^2-a_2^2+a_3^2=1$, one sign flipped. Both are verified in the companion article. It is the same algebraic move that separates the algebra's real structure $\flat$ from its compact conjugations.

Nothing here changes this article's findings or its open questions. The source is recorded as an independent instance of the same signature-dependent classification, not as support for any interpretation of the framework.

## Chirality Is Not the Sector Split

Three decompositions of the framework are in play in this article and its parents, and they must not be conflated.

- The **chiral decomposition** is a decomposition of the spinor module $\Delta$ by the chirality cell $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, into $S$ and $\bar{S}$. Its projectors are $P_L,P_R$, and it is the subject of this article.
- The **sector decomposition** is a decomposition of the algebra $\mathbb{B}$ by Hermitian conjugation ${}^{*}$, into the anti-Hermitian $\mathbb{M}_-$ and the Hermitian $\mathbb{M}_+$. Its projectors are the maps $\tilde{Q}\mapsto\tfrac12(\tilde{Q}\mp\tilde{Q}^{*})$.
- The **ideal decomposition** is the Peirce decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ by the primitive idempotents $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$, $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$. Its two summands are *both* copies of $S$; it is not a chirality decomposition, as the read-list spinor article stresses.

The chiral projectors and the Peirce projectors are both right multiplications on $\mathbb{B}$ — indeed $P_L=R_{\tilde\Pi_+}$ — so as operators on the algebra they are the same decomposition; what separates them is what distinguishes the two summands. The Peirce idempotents are non-central, so their summands are two copies of one module $S$ and no conjugation tells them apart; the chirality cell is the representative of a **central** idempotent, and the two halves are then $S$ and its conjugate $\bar S$, related by the antilinear $\mathcal C$. The sector projectors are a third thing again: no chiral projector equals a sector projector. That is the precise sense of the electron article's two findings, "chirality is not the same as the sector split" and "the two decompositions share no projector", and this article inherits them unchanged. They are repeated only because a reader of the gauge principle might be tempted to identify the internal chirality with the material/informational split, and the temptation is without algebraic support.

## What the Framework Supplies, Transcribes, and Does Not Supply

**What it supplies.**

- *The two-chiral structure and its projectors.* The spinor module decomposes into $S\oplus\bar{S}$; the chirality cell $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ (with $\chi^2=I_4$) and $P_{L,R}$ are exact and Lorentz invariant, and the projectors are idempotent, orthogonal and complete. The algebra of the projectors has been checked, including the commutation with the even (Lorentz) generators that survives the mass term.
- *The chirality-oddness of the mass.* The Dirac bilinear is odd under $\chi$ and vanishes on a definite-chirality state; the parent's mass term is the linear off-diagonal chiral pair, while the operation that exchanges the chiral halves is the module charge conjugation $\mathcal C$. The algebra's real structure $\flat$ is order-reversing but preserves the sector split, so it does not by itself exchange the halves. This is established.
- *The chiral gauge covariant derivative on the module.* For independent charges $ϙ_L,ϙ_R$ the derivative $D_\mu=\partial/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Ϙ$ is covariant with $Ϙ=ϙ_LP_L+ϙ_RP_R$, and its curvature is $\tfrac{i}{\hbar}F_{\mu\nu}Ϙ$. This is the standard chiral abelian gauge structure, expressed on the biquaternion spinor module. The charge operator is the right multiplication $R_b$, so the parent's left-multiplied form is recovered only in the vector-like case.
- *The mass selection rule.* A bare Dirac mass is gauge invariant iff $ϙ_L=ϙ_R$; a chiral fermion is massless in the unbroken phase. This is established by direct computation and is the algebraic content of the Standard Model's need for a Higgs field.
- *The vector-like character of the centre.* The only canonically available abelian gauge group is the scalar centre, which cannot be chiral.

**What it only transcribes.**

- *The global-to-local gauge argument itself.* The localization of a phase and the appearance of a connection are the read-list gauge principle's; the chiral variation above is that argument run with a charge operator $Ϙ$ instead of a scalar charge $ϙ$.
- *The Higgs requirement.* That a chiral fermion needs a compensating scalar field is read off the selection rule; the mechanism by which the scalar acquires its expectation value is the subject of the companion *The Higgs Mechanism in Biquaternionic Form*, for the abelian case. The Yukawa coupling that would convert the vacuum value into a fermion mass is not constructed there either, so the fermion mass itself is not supplied.
- *The Weyl/Dirac split.* The two-component equations of the massless limit, and the helicity–chirality locking, are worked in the exercise articles of the read list; this article uses them and does not re-derive them.

**What it does not supply.**

- *A chiral gauge group.* The centre is scalar and vector-like; a non-central gauge structure, and with it the reality and compactness conditions that would select a compact gauge algebra, are not derived. This is the principal gap.
- *The value of the charges.* $ϙ_L$ and $ϙ_R$ are parameters, exactly as $ϙ$ is in the abelian gauge principle; the algebra does not fix them.
- *The resolution of the real structure's pairing.* The parent's mass term is the linear chiral pair and conserves fermion number. The algebra's $\flat$ supplies the shape of a conjugate pairing of Majorana type, but its single-field equation is not a physical mass; whether a given fermion uses the module's charge conjugation $\mathcal C$ is open, and is the pivot on which the framework's chiral sector turns.
- *Anomaly cancellation for a chiral spectrum.* The framework's own gauge structure is anomaly-free, and not by a nontrivial cancellation: it is vector-like, so the left and right spectra coincide and the triangle coefficients vanish identically. The axial density itself is computed from the chirality cell in the companion *Anomalies and Anomaly Cancellation in Biquaternionic Form*. What is not supplied here is a cancellation condition for a chiral non-central group, since no such group is supplied.
- *Empirical contact.* As everywhere in the framework, no prediction distinguishing it from the standard chiral gauge theory is offered.

## Open Questions

1. **Can the framework host a chiral gauge group?** The centre supplies only a scalar, vector-like abelian group. Chirality requires a non-central action, hence a gauge group beyond the scalar centre; the read-list gauge article's reality and tracelessness conditions are the prerequisite, and whether they admit a compact simple algebra in $\mathbb{B}\cong M_2(\mathbb{C})$ is not settled.

2. **Which interpretation of the phase is physical?** The centre acts as a scalar on the algebra (vector-like) but would act as $\exp(i\theta)$ on $S$ and $\exp(-i\theta)$ on $\bar{S}$ under the Lorentz-conjugate assignment (axial). The identification of the biquaternion field with $\Delta$ — the real-structure or "two-$i$" question — decides between them. This article does not.

3. **What is the physical status of the real structure's pairing?** The parent's mass term is the linear chiral pair, through which the continuous central phase passes, so the framework's fermion number is conserved by it. The algebra's $\flat=-{}^{*}$ gives the shape of a conjugate pairing of Majorana type, but the single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ has spacelike plane waves and is retired as a physical mass (the companion *Antilinear Structure and the Two Kinds of Mass*). The module operation that can carry a physical Majorana mass is the charge conjugation $\mathcal C:S\leftrightarrow\bar S$; whether a given fermion — the neutrino in particular — uses it is the companion's question. The parent Dirac article's open question 1 and the gauge article's open question 5 remain the loci.

4. **What is the biquaternion status of the chiral projectors?** The operators need no complexification: $P_L=R_{\tilde\Pi_+}$ and $P_R=R_{\tilde\Pi_-}$ are right multiplications by elements of $\mathbb{B}$. What has no representative in $\mathbb{B}$ is a non-trivial **central** idempotent, since $\mathbb{B}$ is simple; the central idempotents $e_\pm=\tfrac12(e_t\pm\chi_{\mathrm{ad}})$ live in $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}$. The open part is therefore not the embedding of the projectors but the one of question 2: which module structure, $S\oplus S$ or $S\oplus\bar{S}$, the physical field carries.

5. **Where does the Higgs field enter?** The selection rule identifies the quantum numbers a compensating scalar must carry, and the companion *The Higgs Mechanism in Biquaternionic Form* carries out the abelian mechanism: the central scalar, its circle of minima, and the gauge-boson mass from the scalar kinetic term. The Yukawa coupling of that scalar to the two chiral halves — the step that would give the fermion its mass — is not constructed there, and is the open end of this question.

6. **Anomalies.** The companion *Anomalies and Anomaly Cancellation in Biquaternionic Form* computes the axial density from the chirality cell and states the cancellation as a condition on the spectrum, and it shows that the framework's own gauge structure passes the test identically because it is vector-like. What remains open is the conditional: if a non-central chiral gauge group is ever supplied (question 1), whether the algebra's representation theory would make any of the cancellation conditions automatic.

7. **Chirality versus the sector split.** The chiral and the sector projectors are genuinely different operators — no chiral projector equals any sector projector. But the group acting on the module and the algebra's own structure are both built from $\mathbb{B}$: is there a deeper relation, or are they independent structures that happen to coexist in one algebra?

8. **Empirical contact.** Does any of the chiral structure above yield a prediction distinguishing the framework from standard chiral gauge theory? As always, this is the central unresolved question.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, not a different algebra. In cell notation,

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

$$
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\chi .
$$

In the axis-free display:

$$
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\chi .
$$

A single cell $L_aR_b$ is a pure tensor of $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, of tensor rank one; as an operator on $\Delta$ its rank is four whenever $a$ and $b$ are invertible, so the two ranks must not be confused. The pure cells form the seven-dimensional cone of rank at most one, and a general element is a sum of at most four of them. Two cells multiply by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order, and the products of the four frame cells $\gamma_0,\dots,\gamma_3$ give the usual sixteen-element Clifford basis. Every sign among them comes from $i^2=-1$ together with $\vec e_k^2=-e_t$: for instance $\gamma_0\gamma_1=i^2L_{e_t\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}$, and the same four steps give $\gamma_0\gamma_1\gamma_2\gamma_3=-i\chi$, that is $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$.

$\gamma_5$ is the reference-frame representative of the chirality operator. The abstract central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, with $\chi_{\mathrm{ad}}^2=e_t$ — is a different object; on the Dirac module it is represented by the frame cell $\gamma_5=\chi$. The distinction is the one between the abstract central sign and its representative.

The cell dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
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
The four contraction sums are

$$
\gamma_\mu\gamma^\mu=4I_4,\qquad
\gamma_\mu\gamma_\alpha\gamma^\mu=-2\gamma_\alpha,\qquad
\gamma_\mu\gamma_\alpha\gamma_\beta\gamma^\mu=4g_{\alpha\beta}I_4,\qquad
\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\delta\gamma^\mu=-2\gamma_\delta\gamma_\beta\gamma_\alpha.
$$

With all indices lowered, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$; the difference is the metric used to raise the contracted index. In the Euclidean frame, where $\gamma_\mu^2=+I_4$ for every $\mu$, the same sums read $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

A chiral fermion is one whose left- and right-handed components carry inequivalent gauge representations. In the biquaternion framework the chiral decomposition lives in the spinor module: the Dirac module is $\Delta=S\oplus\bar{S}$, the chirality cell is $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$, acting by $\chi\Psi=-i\,e_t\Psi\vec e_z$ with $\chi^2=I_4$, and the projectors are the cells

$$
P_L=\tfrac12(I_4-\chi)=\tfrac12(I_4+iR_{\vec e_z}^{\mathrm{axf}}),\qquad
P_R=\tfrac12(I_4+\chi)=\tfrac12(I_4-iR_{\vec e_z}^{\mathrm{axf}}),
$$

equivalently $P_L\Psi=\tfrac12(\Psi+i\Psi\vec e_z)$ and $P_R\Psi=\tfrac12(\Psi-i\Psi\vec e_z)$. They are idempotent, orthogonal, complete, of rank two, and Lorentz invariant, because $\chi$ commutes with the bivector cells that generate the Lorentz action — it anticommutes with the generator cells themselves. The Dirac mass bilinear $\bar{\Psi}\Psi=\psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ is chirality-odd and vanishes on a state of definite chirality.

A chiral abelian gauge symmetry with independent charges is consistent on the module: with $Ϙ=ϙ_LP_L+ϙ_RP_R$, the covariant derivative $D_\mu=\partial/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Ϙ$ satisfies $D_{2,\mu}(\Lambda\Psi)=\Lambda D_\mu\Psi$ for arbitrary $ϙ_L,ϙ_R$, and $[D_\mu,D_\nu]=\tfrac{i}{\hbar}F_{\mu\nu}Ϙ$. The charge operator is itself a right multiplication, $Ϙ=R_b$ with $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$, so it coincides with a left multiplication, and hence with the parent's connection, only when $ϙ_L=ϙ_R$. But under the gauge transformation $\bar{\Psi}\Psi$ acquires the position-dependent phase $\exp(\tfrac{i}{\hbar}(ϙ_R-ϙ_L)\Gamma)$, so it is gauge invariant **iff $ϙ_L=ϙ_R$**: a chiral fermion has no bare Dirac mass. This is the framework's form of the Standard Model's requirement that fermion masses arise through a compensating scalar. The two occurrences of the condition $ϙ_L=ϙ_R$ — one for the mass, one for the side of the connection — are the same statement seen twice.

The framework's *own* abelian gauge group is the $*$-unitary part of the centre $\mathbb{C}_{\mathbb{B}}$, and a central element acts as a scalar on $M_2(\mathbb{C})$, giving every component the same charge. The canonically available abelian sector is therefore **vector-like** and cannot be chiral; a chiral gauge group requires a non-central action beyond the scalar centre — precisely the structure the read-list gauge article leaves open. The framework's mass term is the linear chiral pair, through which the continuous central phase passes: the vector $\mathrm{U}(1)$ is conserved for the massive field, and what the mass breaks is the axial symmetry,

$$
\sum_\mu\frac{\partial j_{5\mu}}{\partial Q_\mu}
=2im\,\bar{\Psi}\,\chi\Psi,
$$

which vanishes only at $m=0$. The algebra's antilinear involution is the real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$: it pairs an algebra element with its conjugate, is not invariant under the continuous central phase, and has the quantum numbers of a conjugate-pairing (Majorana-type) term. It does not, however, exchange the two chiral halves; that exchange is the module charge conjugation $\mathcal C$. Its single-field equation is not a physical mass, because its plane waves are spacelike.

Two gaps are left visible. First, without a non-central gauge structure the framework has no chiral gauge group, and the reality and compactness conditions that would supply one are not derived. Second, the algebra's $\flat$ supplies the shape of a conjugate pairing of Majorana type, but its single-field equation is not a physical mass; whether a given fermion uses the module's charge conjugation $\mathcal C$ is open. The chiral structure itself — the halves, the projectors, the selection rule — is established and exact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_+, \mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Complex scalar subspace; the centre of the algebra |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i)=iI_2$ |
| $S = \mathbb{C}^2 = (\tfrac12,0)$ | Left-handed Weyl spinor module (unique simple module) |
| $\bar{S} = (0,\tfrac12)$ | Right-handed Weyl spinor module (conjugate); the parent Dirac article writes it $S^{\mathrm{c}}$ |
| $\Delta = S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}\Delta=4$ |
| $\psi_L\in S,\ \psi_R\in\bar{S}$ | Left- and right-handed Weyl spinors |
| $I_4$ | Identity operator on $\Delta$ |
| $L_a\Psi=a\Psi,\ R_b\Psi=\Psi b,\ L_{a}R_{b}$ | Left, right and two-sided multipliers; $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$ |
| $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, $\chi\Psi=-i\,e_t\Psi\vec e_z$, $\chi^2=I_4$ |
| $P_L=\tfrac12(I_4-\chi)=\tfrac12(I_4+iR_{\vec e_z}^{\mathrm{axf}})$, $P_R=\tfrac12(I_4+\chi)=\tfrac12(I_4-iR_{\vec e_z}^{\mathrm{axf}})$ | Chiral projectors |
| $\bar{\Psi} = \Psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}}$, $\bar{\Psi}\Psi = \psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ | Dirac adjoint and mass bilinear (chirality-odd) |
| $\mathcal C$ | Module charge conjugation, the antilinear map $S\leftrightarrow\bar S$; its fixed space is the Majorana spinor space |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}$ | Generator cells: $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, with $\tau(t)=x$, $\tau(k)=y$ |
| $g_{\mu\nu}=\mathrm{diag}(+,-,-,-)$ | Metric; the generator cells satisfy $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}} iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}}+iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\tau(\nu)}}^{\mathrm{axf}} iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}=2g_{\mu\nu}I_4$ |
| $ϙ_L, ϙ_R$ | Left and right charges (parameters) |
| $Ϙ = ϙ_LP_L+ϙ_RP_R$ | Chiral charge operator |
| $Ϙ=R_b$, $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$ | The same operator as a right multiplication by a Hermitian biquaternion; central iff $ϙ_L=ϙ_R$ |
| $\Lambda = \exp(\tfrac{i}{\hbar}\Gamma Ϙ)$ | Chiral gauge transformation |
| $D_\mu = \partial/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu Ϙ$ | Chiral covariant derivative |
| $A_{2,\mu} = A_\mu-\partial/\partial Q_\mu\,\Gamma$ | Transformation of the abelian connection |
| $F_{\mu\nu} = \partial/\partial Q_\mu A_\nu-\partial/\partial Q_\nu A_\mu$ | Abelian curvature |
| $[D_\mu,D_\nu]=\tfrac{i}{\hbar}F_{\mu\nu}Ϙ$ | Chiral curvature identity |
| $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{*}$ | Anti-Hermitian conjugation; the algebra's real structure ($\mathbb{C}$-antilinear, order-reversing; preserves $\mathbb{M}_\pm$, so it does not exchange the chiral halves) |
| $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$, $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ | Abstract central sign of the complexification; represented by $\chi$ on $\Delta$ |
| $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ | Complexification; the two chiral summands |
| $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\ \tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ | Primitive idempotents; $P_L=R_{\tilde\Pi_+}$, $P_R=R_{\tilde\Pi_-}$ |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, the Weyl spinors, and the chiral decomposition of the Dirac field.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Dirac spinor from two Weyl spinors, the chiral gauge interactions, and the Standard Model's need for a Higgs field to give mass to chiral fermions.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the $V-A$ structure, the mass selection rule, and the electroweak chiral assignments.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra construction of spinors from idempotents and the chirality operator.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- Walter Greiner and Berndt Müller, *Gauge Theory of Weak Interactions* (Springer, 2000), for the chiral structure of the electroweak theory and the generation of fermion masses.
- D. J. Cirilo-Lombardo, "Algebraic structures, physics and geometry from a Unified Field Theoretical framework," arXiv:1411.5493v3 [hep-th] (2015), for the external interpretation recorded in *An External Reading of the Majorana Condition and the Spacetime Signature*: Majorana's 1937 transformation applied to a structural group, the verified real-symmetric result, the assertion that a Majorana representation is tied to the signature, and the non-Hermitian operators of the source's separate $(2{+}2)$ sector. Cited for the independent instance of the signature-dependent classification, with the source's printed slips noted and its programme not endorsed.
- Companion articles: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html); [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html); [The Biquaternion Basis of a Unified-Field Fibre Bundle](the-biquaternion-basis-of-a-unified-field-fibre-bundle.html).
