# __The Neutrino and Majorana Fermions in Biquaternionic Form__

## Introduction

A **Dirac fermion** is a four-component field whose left- and right-handed parts are independent; a **Weyl fermion** is a two-component field of definite chirality; a **Majorana fermion** is a field that is its own charge conjugate, $\psi^{c}=\psi$. The three are not variants of a single object but three different answers to the question of what reality structure the spinor carries. The Majorana condition is the strongest: it identifies the field with its conjugate, halves the number of independent real components, forbids a vector (fermion-number) current, and yet permits a mass term. A Weyl fermion is chiral and, so long as its chirality is protected, exactly massless. A Dirac fermion is neither self-conjugate nor, in this sense, chiral.

The immediate physical application is the neutrino. In the Standard Model the neutrino is a left-handed Weyl fermion: the weak interaction couples only to its left-handed part, and no renormalisable mass term survives. Whether the neutrino is in fact Dirac or Majorana is one of the few places where the algebra of spinors meets experiment directly, and the answer is not settled. This article asks what the biquaternion framework, in the notation of the companion articles, supplies for that distinction.

The dynamics in the algebra is the **chiral pair**,

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R .
$$

The two lines are one dynamics and not two: the second is the conjugate of the first under $\natural$, the anti-automorphism $(ab)^{\natural}=b^{\natural}a^{\natural}$ that exchanges the sides, so each line is the other read from the other side, and together they are the two-sided operator theorem on the two chiralities. On the spinor module the same pair is a single equation,

$$
(\mathbb{D}-m)\Psi=0,
\qquad
\mathbb{D}\Psi=\bigl(\tilde{\nabla}\Psi_R,\ \tilde{\nabla}^{\natural}\Psi_L\bigr),
$$

with $\mathbb{D}$ the **pair operator** of the conventions article and $\mathbb{D}^2=\Box I$; this is the form the sections below use. A third equation is not a third form of these: $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$, built on the algebra's order-reversing real structure $\flat$, is a single-field equation on $\mathbb{B}$, and it is kept separate — it is the subject of the section on which conjugation is the charge conjugation, and of open question 2. The equations below are the spinor-module representatives of the pair; the Majorana equation is the representative restricted to the real form $\psi^{c}=\psi$, and whether that restriction descends to the algebra is the question this article tests rather than assumes.

The presentation is organized around one question — *which real structure on the spinor module is the charge conjugation, and does the algebra's own material/informational split supply it?* — and the answer is split, at the outset, into three categories.

- **Established, and recomputed below.** The Dirac module $\Delta=S\oplus\bar{S}$ of the read list is self-conjugate: it carries a conjugate-linear real structure $\mathcal{C}$ with $\mathcal{C}^2=1$ that **commutes with the Dirac operator and exchanges the two chiral halves**. Its fixed space is the Majorana spinor space, of real dimension four. A Majorana–Weyl structure would have to preserve each half and does not exist in this signature. The Majorana equation $\mathbb{D}\,\psi=m\psi^{c}$ is consistent with the constraint $\psi^{c}=\psi$: the constraint is propagated, the mass-shell condition $p^2=m^2$ is unchanged, and the mass is permitted while the vector current vanishes. The consistency is not free — it rests on the frame cells being imaginary and the Dirac operator using the real cells, the two being related by $i^2=-1$.
- **Established from the read list, and sharpened here.** The framework's conjugations on $\mathbb{B}$ are the quaternion conjugate ${}^{\natural}$, the coefficient complex conjugate $\bar{\cdot}$, the Hermitian conjugate ${}^{*}=({}^{\natural})^{\,*}$, and the anti-Hermitian conjugation $\flat=-{}^{*}$, the algebra's real structure. Of these, only $\bar{\cdot}$ is a conjugate-linear **algebra automorphism**; ${}^{*}$ and $\flat$ reverse the order of products. Charge conjugation, which must be a module map compatible with left multiplication, is therefore tied to $\bar{\cdot}$ — the real structure whose fixed points are $\mathbb{H}_{\mathbb{B}}$ — and not to the order-reversing real structure $\flat$.
- **Gap, left visible.** The two-sector split $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ is a decomposition of the *algebra* by ${}^{*}$, not a real structure of the *module*. Its anti-Hermitian summand $\mathbb{M}_-$ is the fixed space of $\flat$ and has real dimension four, superficially matching the Majorana count; but the Dirac operator does not preserve $\mathbb{M}_-$ (left multiplication by a spatial generator carries it out of the subspace), so the sector split cannot be the Majorana reality condition. An attempted identification of Majorana with $\mathbb{M}_-$ fails on the equation, not merely on taste.

The article is organized as follows. The next section fixes the three notions and their component counts. A section then constructs charge conjugation as a real structure on $\Delta$, states the frame and signature, and separates frame-independent existence from frame-dependent form. A section treats the Majorana condition, its consistency with the massive equation, and the surviving and vanishing bilinears. A section identifies which conjugation of the biquaternion algebra plays the role of charge conjugation. A section tests the sector split against the reality condition and reports the obstruction. A section states what in the neutrino's description is empirical input rather than a consequence of the framework, and the next separates what the framework supplies, transcribes, and does not supply. A section then records the geometric use of Majorana pairs outside the framework, open questions follow, and the article closes with the gamma formulation, the summary and the notation table.

For the form of the Clifford algebra we use the **cell frame**

$$
iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad k=1,2,3,
$$

with $L_a\psi=a\psi$, $R_b\psi=\psi b$ and $L_{a}R_{b}\psi=a\psi b$. Each of the four is one factor of $i$ times a cell with real entries; throughout, $i$ is the central scalar with $i^2=-1$, and wherever two imaginary units meet in a product below they are multiplied to that $-1$ and the $-1$ is written, so no display carries a double $i$. With **signature** $g=\mathrm{diag}(+,-,-,-)$ they carry the Clifford relations of $g$, and the chirality operator is $\Gamma=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, which is $-1$ on the left-handed half $S$ and $+1$ on the right-handed half $\bar S$. This is the frame and signature of the read-list chirality article; the Clifford relations, the chirality operator and the projectors are all recomputed below. Signature and frame must be stated together, because the explicit form of charge conjugation depends on both. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The plain form, read as the trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, is inherited unchanged.

## Dirac, Weyl and Majorana: The Three Notions

The three notions are three classes of element of the spinor module, distinguished by which representation of the Lorentz group they carry and by which reality structure they respect. The chiral decomposition itself was settled in the read list and is used here without re-derivation.

**Dirac.** A Dirac spinor is an element $\Psi\in\Delta=S\oplus\bar{S}$; it has four complex components, equivalently eight real components, and its two chiral halves are independent. It is the most general spinor of the module. On it the Lorentz group acts block-diagonally by $M\oplus\mathsf{M}_2(\tilde{U}^{*})$ with $M=\mathsf{M}_2(\tilde{U})$, and the chirality operator $\Gamma$ labels the halves.

**Weyl.** A Weyl spinor is an element of one half, $\psi_L\in S$ or $\chi\in\bar{S}$; it has two complex, four real components, and carries a definite chirality. The two halves are not isomorphic as complex representations of $SL(2,\mathbb{C})$, as the read-list spinor article stresses: they are the conjugate pair $(\tfrac12,0)$ and $(0,\tfrac12)$. A Weyl spinor is therefore chiral in the representation-theoretic sense.

**Majorana.** A Majorana spinor is an element of a **real form** of $\Delta$: a spinor equal to its own charge conjugate, $\psi^{c}=\psi$, where $\psi^{c}$ is a conjugate-linear map of $\Delta$ to itself. The fixed space of an antilinear involution on an eight-real-dimensional space is four-real-dimensional, so a Majorana spinor has four real components — the same count as a Weyl spinor, but a different object: the Weyl spinor is chiral and its conjugate is the *other* half, whereas the Majorana spinor is self-conjugate and is not chiral.

The four notions stand in the following relation. In the Lorentzian signature $(1,3)$ the Dirac module is self-conjugate while the two Weyl halves are a conjugate pair, so **Majorana spinors exist and Majorana–Weyl spinors do not**. The reason is structural and is worth stating at once, because it is the point on which the biquaternion framework has something to say: the real structure that makes a spinor Majorana exchanges the two chiral halves, and a Majorana–Weyl spinor would require a real structure preserving them. The complex algebra $\mathbb{B}$, being simple, sees one simple module and cannot distinguish the halves at all; the exchange is a real-structure operation, and it is the same operation that pairs $S$ with $\bar{S}$ in the Dirac module. The classification of which signatures admit which type is governed by the signature modulo eight, and the corpus already records it; in $(1,3)$ the outcome is the one just stated.

| Notion | Carrier | $\dim_{\mathbb{R}}$ | Chiral? | Self-conjugate? |
|---|---|---|---|---|
| Dirac | $\Delta=S\oplus\bar{S}$ | $8$ | no (both halves) | no |
| Weyl | $S$ or $\bar{S}$ | $4$ | yes | no |
| Majorana | real form of $\Delta$ | $4$ | no (halves conjugate) | yes |
| Majorana–Weyl | real form of $S$ | $2$ | yes | yes (only where the real structure preserves $S$; not in $(1,3)$) |

Two cautions belong here, both inherited from the read list and both relevant below. First, the chiral halves are **not** the two minimal left ideals $\mathbb{B}\tilde\Pi_+$, $\mathbb{B}\tilde\Pi_-$: those are both isomorphic to $S$ and carry the same defining representation, so the chirality distinction is invisible to $\mathbb{B}$ alone. Second, a biquaternion $\tilde{\Psi}\in\mathbb{B}$ is not a spinor; the spinor is an element of the module $S$, or of $\Delta$, and the algebra acts on it. The identification of an algebra element with a spinor is a separate step, and it is exactly where the reality conditions become delicate.

## Charge Conjugation as a Real Structure on the Spinor Module

Charge conjugation is a **conjugate-linear** map on the Dirac module. In four dimensions it is written with a charge-conjugation cell $C$ acting on the Dirac conjugate,

$$
\psi^{c} \;=\; C\,\bar{\psi}^{\,T},
\qquad
\bar{\psi} \;=\; \psi^{\dagger}\,iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}} ,
$$

and the cell is fixed by the requirement that the kinetic term be preserved,

$$
C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T}C^{-1}=-\,iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad C\,(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^{T}C^{-1}=-\,iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}.
$$

The transpose, not the inverse or the conjugate, appears because $C$ is the cell of a bilinear pairing on the module. Two features of this definition must be stated before it is used, and they are the two traps of the subject.

**The cell is frame-dependent, and the reality condition is frame-dependent in form.** A linear change of frame $\Lambda$ sends $C\mapsto \Lambda C\Lambda^{T}$, so the explicit cell changes with the frame even though the map it defines does not. In the cell frame of the Conventions, with $g=\mathrm{diag}(+,-,-,-)$, the frame's timelike cell is $iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, and the charge-conjugation cell is that cell with its factor $i$ removed,

$$
C \;=\; L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}} \;=\; R_{\vec e_x}^{\mathrm{pau}} .
$$

It is real and antisymmetric, $C^{T}=-C$, with $C^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ (the square of $\vec e_x$ is $-1$) and $C^{\dagger}=C^{-1}$, and it satisfies the two transposition relations above for $\mu=0,1,2,3$. The same map written in another frame has the cell $\Lambda C\Lambda^{T}$, which is a different cell. The existence of a charge-conjugation operation is a statement about the signature, not about the frame; its form is a statement about the frame. A calculation that fixes a sign by comparing "$C$" across two papers that use different cell frames is comparing two different cells.

**The map is antilinear, and it is the antilinear map — not $C$ — that is the real structure.** Writing $\bar{\psi}^{\,T}=(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T}\psi^{*}$ and using $(R_{\vec e_x}^{\mathrm{pau}})^{T}=-R_{\vec e_x}^{\mathrm{pau}}$ gives

$$
\psi^{c} \;=\; K\,\psi^{*},
\qquad
K \;=\; C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T} \;=\; R_{\vec e_x}^{\mathrm{pau}}\,(-iR_{\vec e_x}^{\mathrm{pau}}) \;=\; -i(R_{\vec e_x}^{\mathrm{pau}})^{2} \;=\; i\,L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},
\qquad
K K^{*} \;=\; L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}} .
$$

The step $-i(R_{\vec e_x}^{\mathrm{pau}})^{2}=iL_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ is $i^2=-1$ read once, because $(R_{\vec e_x}^{\mathrm{pau}})^{2}=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$; and $KK^{*}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ is $i(-i)=1$ read as cells. The real structure is therefore carried by the **central imaginary**: $K=iL_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=i\,I_4$, one factor of $i$ and nothing else. The same relation is the statement that $\mathcal{C}:\psi\mapsto\psi^{c}$ is an **involution**, $\mathcal{C}^2=1$, and it is conjugate-linear by construction, $\mathcal{C}(\lambda\psi)=\lambda^{*}\mathcal{C}(\psi)$. The cell $C$ itself has $C^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and is not the real structure. The distinction matters below: the fixed points of $\mathcal{C}$ are the Majorana spinors, and no fixed points of $C$ are involved.

The consistency of this real structure with the Dirac operator is a second, independent condition, and it is where the factor $i$ of the frame cells earns its place. Each frame cell is one factor of $i$ times a cell with real entries, so the coefficient conjugate of every frame cell is its negative,

$$
\bigl(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\bigr)^{*}=-\,iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}},
\qquad
\mu=0,1,2,3,
$$

with $\nu(0)=x$ and $\nu(k)=y$, and the chirality cell obeys the same relation, $\Gamma^{*}=-\Gamma$. Since $K=iL_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ is central, conjugation by it changes nothing, so

$$
\boxed{\;K\,\bigl(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\bigr)^{*}K^{-1}=-\,\bigl(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\bigr),
\qquad
K\,\Gamma^{*}K^{-1}=-\,\Gamma\;}
$$

In words: **charge conjugation negates every frame cell**, since its coefficient conjugate is its negative. The Dirac operator is not a sum of frame cells, however; it is

$$
\mathbb{D}=-\sum_\mu\varepsilon_\mu\,L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\,\partial_\mu ,
\qquad
\varepsilon_\mu:=g_{\mu\mu},
$$

whose coefficients are the **real** cells, taken with the signs $\varepsilon_\mu$, and whose symbol on the positive-frequency factor is the $\mathbb{D}_p$ used below, because $\partial_\mu\mapsto-ip_\mu$ there and $-\varepsilon_\mu L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\,(-ip_\mu)=\varepsilon_\mu\,iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\,p_\mu$. The two forms differ by one factor of $i$, counted with $i^2=-1$:

$$
-i\,\bigl(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\bigr)=-\,\bigl(i^2\bigr)\,L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}=L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}} .
$$

Multiplying a real cell by $i$ makes it imaginary, and conjugating makes it negative; the operator carries no such factor, so its coefficients are fixed,

$$
\bigl(L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\bigr)^{*}=L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}},
$$

and $\mathcal{C}$ **commutes** with $\mathbb{D}$: a self-conjugate field stays self-conjugate under the evolution. The commutation holds because the frame cells are imaginary, not in spite of it, and it is verified on all four $\mu$ independently of any statement about a mass.

**What flips is the frequency, not the mass.** At fixed momentum the statement reads differently, and the two readings must not be confused. The symbol is purely imaginary, $\mathbb{D}_p^{*}=-\mathbb{D}_p$, so the antilinear map anticommutes with it,

$$
J\,\mathbb{D}_p=-\,\mathbb{D}_p\,J,
\qquad
J:v\mapsto K v^{*},
$$

and $\mathcal{C}$ maps the kernel of $\mathbb{D}_p-m$ to the kernel of $\mathbb{D}_p+m$. That is the standard statement that the charge conjugate of a positive-frequency amplitude is a negative-frequency amplitude. Commuting on functions and anticommuting on symbols are one fact, because coefficient conjugation reverses the frequency.

**Chiral halves, and the exchange between them.** The charge conjugation anticommutes with $\Gamma$, so in chiral blocks it is off-diagonal: it maps the left-handed half to the right-handed half and back. In particular it does not preserve the chirality projectors, $P_{\mp}\,\mathcal{C}=\mathcal{C}\,P_{\pm}$ with $P_{\pm}=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}\pm\Gamma)$. The Majorana condition $\psi^{c}=\psi$ is therefore a single relation between the two halves, not two independent real conditions; in the native form it is the one equation

$$
\psi \;=\; i\,\psi^{*},
$$

which determines $\psi_R$ from $\psi_L$ and conversely. The fixed space is four-real-dimensional, as required for Majorana, and it is **not** the graph of a complex-linear identification of $S$ with $\bar{S}$ — such an identification would make the spinor Weyl and Majorana simultaneously, which does not exist here. This is the module-level content of the statement that the real structure exchanges the halves.

We collect the verified statements of this section in a table. Each entry was checked by exact computation in the cell frame with $g=\mathrm{diag}(+,-,-,-)$; every Clifford and charge-conjugation identity was checked on all four $\mu$, not only on $\mu=0$.

| Statement | Verification |
|---|---|
| $iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ and $iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ carry the Clifford relations of $g$, $\Gamma=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, $\Gamma^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | all $16$ commutators and anticommutators, exact |
| $P_{\pm}=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}\pm\Gamma)$: idempotent, $P_{+}+P_{-}=I_4$, ranks $2$ and $2$, $P_{\pm}\Gamma=\pm P_{\pm}$, $\mathcal{C}P_{\mp}=P_{\pm}\mathcal{C}$ | exact |
| $C^{T}=-C$, $C^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $C^\dagger=C^{-1}$ | exact, $C=L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ |
| $C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T}C^{-1}=-\,iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ and $C\,(iL_{e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^{T}C^{-1}=-\,iL_{e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | all $\mu=0,1,2,3$ |
| $K=C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T}=i\,L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=iI_4$, $KK^{*}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | exact |
| $\bigl(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\bigr)^{*}=-\,iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$ for all $\mu$; the reversed cells are imaginary, the operator uses the real ones, so $\mathcal{C}$ commutes with $\mathbb{D}$; likewise for $\Gamma$ | all $\mu=0,1,2,3$ |
| $\psi^{c}=K\psi^{*}$, $(\psi^{c})^{c}=\psi$ | all components |
| $\mathcal{C}$ exchanges $S$ and $\bar{S}$ | $\Gamma$-anticommutation of $\mathcal{C}$ |
| $\dim_{\mathbb{R}}\{\psi:\psi^{c}=\psi\}=4$ | $\psi_L$ free, $\psi_R$ determined by $\psi=i\psi^{*}$ |

**A frame-independent caution.** The statement that a charge-conjugation operation exists in a given signature is frame-independent, and it is not true in every dimension; it is governed by the signature modulo eight, as the corpus's spinor articles record. What is frame-independent is the existence of the real structure; what is frame-dependent is the cell $C$ and the explicit form of the condition $\psi=i\psi^{*}$. A reader who carries only the condition and forgets the frame will get signs wrong. A reader who carries only the frame and forgets that the map is antilinear will conclude, incorrectly, that the two halves are identified complex-linearly.

## The Majorana Condition and the Mass Term

The Majorana condition is the fixed-point equation $\psi^{c}=\psi$ of the real structure of the previous section. In the native form of the frame it is $\psi=i\psi^{*}$, and written on the two halves it fixes each of them from the other:

$$
\psi=\begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix},
\qquad
\psi_L=i\psi_R^{*},
\qquad
\psi_R=i\psi_L^{*},
$$

so either half fixes the other and the fixed space is four-real-dimensional, as the Majorana count requires. It is not an extra equation imposed on the field after the fact; it is a restriction of the spinor module to a real form. The question that has to be answered is whether the restricted fields solve a sensible massive equation.

**The massive equation.** For a single self-conjugate field the mass term cannot be the Dirac term $m\bar{\psi}\psi$ of a Dirac field with independent halves, because the two chiral halves are conjugate. Here and below $\mathbb{D}$ is the pair operator of the conventions article, acting on the module in the chiral basis, with $\mathbb{D}^2=\Box I$. The equation that carries a mass is the **Majorana equation**

$$
\boxed{\;\mathbb{D} \psi \;=\; m\,\psi^{c},
\qquad
\psi^{c}=\mathcal{C}\psi\;}
$$

**The constraint is propagated.** Apply $\mathcal{C}$ to the two sides, using that it is conjugate-linear, that it commutes with $\mathbb{D}$ (previous section, verified), that $\mathcal{C}^{2}=1$, and that the mass is real:

$$
\mathcal{C}\!\left(\mathbb{D}\,\psi\right)=\mathbb{D}\,\psi^{c},
\qquad
\mathcal{C}\!\left(m\psi^{c}\right)=m\,\psi .
$$

The conjugate of the equation is therefore $\mathbb{D}\psi^{c}=m\psi$, the same equation with $\psi$ and $\psi^{c}$ exchanged, and the two lines are one system:

$$
\mathbb{D}\,\psi=m\,\psi^{c},
\qquad
\mathbb{D}\,\psi^{c}=m\,\psi .
$$

Subtracting them gives

$$
\mathbb{D}\,\bigl(\psi-\psi^{c}\bigr)=-\,m\,\bigl(\psi-\psi^{c}\bigr),
$$

so the deviation $\chi=\psi-\psi^{c}$ solves the Majorana equation with the sign of the mass reversed, and the same mass shell, $\mathbb{D}^{2}\chi=m^{2}\chi$. That equation is linear and of first order in the time derivative, so $\chi=0$ at one time implies $\chi=0$ at all times: a field that is self-conjugate at one time stays self-conjugate. Nothing forces $m=0$. Squaring the Majorana equation, $\mathbb{D}^{2}\psi=m^{2}\psi$, that is $\Box\psi=m^{2}\psi$, the mass shell $p^{2}=m^{2}$ of the Dirac case, unchanged.

**The mode is not self-conjugate, and the field is.** Propagation holds mode by mode, but no single mode is itself self-conjugate. At fixed momentum the antilinear map anticommutes with the symbol, so $\mathcal{C}$ sends the kernel of $\mathbb{D}_p-m$ to the kernel of $\mathbb{D}_p+m$: the conjugate of a positive-frequency mode is a negative-frequency mode. A mode that is both on shell and self-conjugate would have to lie in both kernels, which forces $m u=-m u$, hence $u=0$. Verified on the mass shell: the kernel of $\mathbb{D}_p-m$ is two complex dimensional and its intersection with the fixed space $\{\psi:\psi^{c}=\psi\}$ is $\{0\}$ for every $m>0$, while at $m=0$ the same intersection is two-real-dimensional. The obstruction is therefore exactly the mass and nothing else.

So the object that is self-conjugate is a field carrying both frequencies, with the negative-frequency amplitude the conjugate of the positive-frequency one,

$$
\psi \;=\; u\,e_{+} \;+\; u^{c}\,e_{-},
$$

where $e_{+}=e^{-ip\cdot Q}$ and $e_{-}=e^{+ip\cdot Q}$ are the two frequency factors, $e_{-}$ being the coefficient conjugate of $e_{+}$, where $\mathbb{D}$ acts on $e_{+}$ as the symbol $\mathbb{D}_p=\sum_\mu\varepsilon_\mu\,iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\,p_\mu$ and on $e_{-}$ as $-\mathbb{D}_p$ (the sign of $\partial_\mu$ reverses), and where $u$ solves

$$
\bigl(\mathbb{D}_p-m\bigr)u=0,
\qquad
p^{2}=m^{2}.
$$

Then $\psi^{c}=\psi$, because $\mathcal{C}$ conjugates the frequency factors as well as the amplitudes and $\mathcal{C}^{2}=1$; and $(\mathbb{D}-m)\psi=0$, because the first term solves with $u$ while $u^{c}$ solves the opposite-sign equation $\bigl(\mathbb{D}_p+m\bigr)u^{c}=0$, which is exactly what the second factor needs. One object meets both requirements, and each requirement is met by a different half of it. That is the module-level content of the two-sided statement that the mass couples a field to its conjugate. Verified: both residuals vanish to machine precision for every $m>0$ tested.

What the Majorana restriction removes is therefore not the mass but half the degrees of freedom. The bilinear $\bar{u}u$ is nonzero for $m>0$ (the normalisation is the one of the companion quantisation article), the mass shell $p^{2}=m^{2}$ is unchanged from the Dirac case, and the field carries four real parameters per momentum instead of eight.

**Which bilinears survive, and which vanish.** The physical statements are about the field, whose components anticommute. The Majorana condition turns $\bar\psi$ into a linear function of $\psi$: from $\psi^{c}=C\bar\psi^{T}$ and $\psi^{c}=\psi$, and with $C^{-1}=-C$,

$$
\bar{\psi} \;=\; -\,C\,\psi ,
$$

which for a commuting spinor of the fixed space is the same statement as $\bar\psi=\psi^{\dagger}iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, checked to all components. Every entry below follows from that one relation together with the anticommutation, and each was computed exactly in the cell frame on a Grassmann field of four generators.

| Bilinear | Grassmann Majorana field | Status |
|---|---|---|
| $\bar{\psi}\psi$ | nonzero | scalar mass term **permitted** |
| $j_0=\bar{\psi}\,iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}\psi$ and $j_k=\bar{\psi}\,iL_{e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\psi$ | $0$ for all $\mu$ | vector current **forbidden** |
| $j^{5}_0=\bar{\psi}\,iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}\Gamma\psi$ and $j^{5}_k=\bar{\psi}\,iL_{e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\Gamma\psi$ | nonzero | axial current permitted |
| $\psi^{T}C\psi=-\bar{\psi}\psi$ | nonzero | the Majorana mass invariant |

The vanishing of the vector current is the statement that a self-conjugate field carries no fermion number; the surviving scalar and axial bilinears are what a Majorana field can couple to. Both properties follow from the same anticommutation: for the vector current the charge-conjugation flip of the bilinear and the self-conjugacy of the field combine to give $j_\mu=-j_\mu$; for the scalar the two contributions add rather than cancel. The same four bilinears computed with commuting components on a spinor of the fixed space give the mirror pattern quoted in the caution below, and both computations were run in the frame of the Conventions.

**A caution that must be recorded.** The last paragraph is a statement about the Grassmann-valued field, and it is not true of a commuting c-number spinor that happens to satisfy the same algebraic condition. If the components are treated as ordinary complex numbers, the antisymmetric contractions that produced the mass term instead cancel, and the same computation gives the **opposite** pattern: $\bar{\psi}\psi=0$, the vector current *nonzero*, and the axial current zero. Every bilinear statement for a Majorana field is therefore a Grassmann statement; a purely classical c-number computation will not reproduce it, and the sign by which the physical statement differs is the anticommutativity of the components. This is recorded here rather than hidden, because the module-level construction above is classical and a reader may reasonably attempt the bilinears at that level. The module construction fixes the constraint and its consistency; the bilinear physics requires the Grassmann structure, which the framework supplies through the anticommuting mode operators of the companion quantisation article rather than through $\mathbb{B}$ itself.

**Contrast with the Weyl field.** A Weyl field of definite chirality has $\bar{\psi}\psi=0$ because the bilinear is chirality-odd (the read-list result), so it admits no Dirac mass. The only mass term a single chiral field can carry is a Majorana mass, which pairs $\psi_L$ with $\psi_L^{c}\in\bar{S}$; that term is allowed only when the field is not protected by a conserved charge. Where the chirality is protected by a complex gauge representation — the Standard-Model neutrino — the term is forbidden and the field is exactly massless; where the field is a gauge singlet, the term is allowed and the field, once massive, is Majorana and no longer Weyl. A Dirac fermion is the remaining case: it has independent halves, a Dirac mass, and neither the Weyl chirality nor the Majorana self-conjugacy.

## Which Conjugation of the Biquaternion Algebra Is the Charge Conjugation?

The module-level real structure $\mathcal{C}$ is abstract. The framework supplies concrete conjugations on $\mathbb{B}$, and the question is which of them realises $\mathcal{C}$. There are four operations in play, and they divide into two kinds.

| Operation | Action on coefficients | Type |
|---|---|---|
| ${}^{\natural}$ quaternion | $e_t\mapsto e_t$, $\vec e_\mu\mapsto -\vec e_\mu$, $i\mapsto i$ | $\mathbb{C}$-linear antiautomorphism |
| $\bar{\cdot}$ complex | coefficients conjugated, basis fixed | conjugate-linear **automorphism** |
| ${}^{*}={}^{\natural}\circ\bar{\cdot}$ Hermitian | coefficients conjugated, $\vec e_\mu\mapsto -\vec e_\mu$ | conjugate-linear antiautomorphism |
| $\flat=-{}^{*}$ | minus the Hermitian conjugate | conjugate-linear, order-reversing |

The distinction that decides the question is **automorphism versus antiautomorphism**. A real structure on a module has to commute with the module action; on the regular module $\mathbb{B}$, where the algebra acts by left multiplication, commuting with the action means respecting the order of products. Only $\bar{\cdot}$ does:

$$
\overline{Q R} = \overline{Q}\,\overline{R},
\qquad\text{whereas}\qquad
(Q R)^{*}=R^{*}Q^{*},
\qquad
(Q R)^{\flat}=-R^{\flat}Q^{\flat}.
$$

So of the framework's conjugations, $\bar{\cdot}$ is the one that can serve as a charge-conjugation real structure on a module; ${}^{*}$ and $\flat$, being order-reversing, cannot. The fixed points of $\bar{\cdot}$ are the real quaternions, $\mathbb{H}_{\mathbb{B}}=\{Q:\bar{Q}=Q\}$ — the fixed points of ${}^{*}$ are $\mathbb{M}_+$, a different space; in this sense the real form that underlies charge conjugation is the real-quaternion real form. The conjugate half $\bar{S}$ carries the action $\tilde{U}\mapsto\tilde{U}^{*}$, exactly as the read-list spinor article states, and that is the Hermitian conjugate; for a Lorentz transformation $\tilde{U}\tilde{U}^{*}=1$, so it is also the contragredient $\tilde{U}^{-1}$. The coefficient conjugation is the real structure, and the Hermitian conjugate is what the conjugate half transforms by: the two are different roles and neither replaces the other. This is the identification the framework supplies, and it is clean: **charge conjugation is the fixed-point real structure of the coefficient complex conjugation, transported to the Dirac module by the identification of $S$ with $\bar{S}$.**

The map $\flat$ is a *different* conjugation, and the difference is exactly the order reversal. The parent articles retain $\flat$, $\tilde{\Psi}\mapsto\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$, as the algebra's real structure; it is antilinear and involutive, so it is a real structure on the algebra as a real vector space. But it is order-reversing, and its fixed space is the material sector $\mathbb{M}_-$, not a spinor real form. It is the map that pairs a field with its conjugate in a Majorana-type coupling; it is not the charge-conjugation map that identifies a field with its antiparticle, and it is not the parent's mass term, which is the linear chiral pair. Mixing the two is the natural error, and it is the one tested in the next section. The four levels at which the corpus uses the name charge conjugation — the algebra's real structure $\flat$, the Clifford pseudoautomorphism, the module operation $C$, and the module real structure $\mathcal{C}$ — are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

Finally, the passage from the algebra to the module is itself a real-structure step. The regular module is $\mathbb{B}\cong S\oplus S$ — two copies of the *same* defining representation — whereas the Dirac module is $\Delta=S\oplus\bar{S}$. Identifying an algebra element $\tilde{\Psi}\in\mathbb{B}$ with a Dirac spinor requires passing from $S\oplus S$ to $S\oplus\bar{S}$, and that passage uses precisely the coefficient conjugation. So the framework does contain the operation, but the operation is $\bar{\cdot}$ together with the module identification, not the decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$.

## Does the Material/Informational Split Help or Obstruct?

The split $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ into anti-Hermitian and Hermitian parts is the algebra's own decomposition by ${}^{*}$. It is real,

$$
\mathbb{M}_-=\{Q:Q^{*}=-Q\},
\qquad
\mathbb{M}_+=\{Q:Q^{*}=Q\},
\qquad
\dim_{\mathbb{R}}\mathbb{M}_-=\dim_{\mathbb{R}}\mathbb{M}_+=4,
$$

and it has one property that makes it a genuine temptation for a Majorana construction: the flat map $\flat=-{}^{*}$ is an antilinear involution whose fixed space is exactly $\mathbb{M}_-$,

$$
Q^{\flat}=Q \iff Q^{*}=-Q \iff Q\in\mathbb{M}_- .
$$

Both implications were checked on basis elements and on general elements. The dimension of $\mathbb{M}_-$ is four, the same as the Majorana count, and $\flat$ is the algebra's real structure, the map on which the framework's Majorana-type coupling is built. It is therefore natural to try the identification

$$
\text{``Majorana''} \;=\; \{\tilde{\Psi}\in\mathbb{B} : \tilde{\Psi}^{\flat}=\tilde{\Psi}\} \;=\; \mathbb{M}_- .
$$

The identification fails on the equation, and the failure is elementary. The biquaternionic gradient is a sum of left multiplications,

$$
\tilde\nabla \;=\; e_t\,\partial/\partial Q_t \;+\; \sum_{k=1}^{3} \vec e_k\,\partial/\partial Q_k ,
$$

and left multiplication by the spatial generators $\vec e_x,\vec e_y,\vec e_z$ does not preserve $\mathbb{M}_-$. The sharpest single instance is

$$
\boxed{\;\vec e_x\in\mathbb{M}_-,
\qquad
\vec e_x \vec e_x=-e_t\in\mathbb{M}_+\;}.
$$

So the spatial part of the gradient does not preserve $\mathbb{M}_-$; more generally, for a generic $\tilde{\Psi}\in\mathbb{M}_-$ the products $\vec e_k\tilde{\Psi}$ lie in neither sector. The time term fails for the same reason: on a plane wave $\partial/\partial Q_t$ contributes a factor $\pm i$, and $i\,\tilde{\Psi}\in\mathbb{M}_+$ whenever $\tilde{\Psi}\in\mathbb{M}_-$. Hence $\tilde\nabla\tilde{\Psi}\notin\mathbb{M}_-$ for generic $\tilde{\Psi}\in\mathbb{M}_-$: **the Dirac operator does not preserve the material sector, so the sector cannot be a Majorana real form.** A Majorana reduction requires a subspace that the equation carries into itself, and $\mathbb{M}_-$ is not one.

The reason is structural rather than accidental. $\mathbb{M}_-$ is a real form of the *algebra* under the order-reversing map $\flat$, and as a vector space it is the four-dimensional material sector of the companion articles — the space of four-vectors and of the material field, on which the Lorentz group acts by $\tilde{U}\,\tilde{Q}\,\tilde{U}^{*}$. A Majorana spinor is a real form of the *spinor module*, on which the Lorentz group acts by one-sided multiplication. The two live in different representations and have different dimensions available to them (four real components each, but transforming differently). The sector split therefore does not help: it supplies a real form of the wrong object. If it is used as the reality condition it actively obstructs, because it makes the mass equation fail to close and would identify a spin-$\tfrac12$ field with a four-vector.

This is the same warning the parent chirality article issues in another guise. There, the chiral projectors $P_{L},P_{R}$ of the spinor module were distinguished from the sector projectors of the algebra: the two decompositions share no projector and the sector split does not see chirality. Here the sharpened statement is that the sector split does not see the Majorana reality condition either. The charge conjugation of the framework is the coefficient conjugation $\bar{\cdot}$ of the previous section, acting on the module; the material/informational split is the algebra's decomposition by ${}^{*}$, and it is not a spinor real structure at all.

## The Neutrino: What the Framework Does and Does Not Derive

The reason the neutrino appears in this article at all is that it is the fermion for which the Dirac/Majorana distinction is an open experimental question. The framework has something to say about the *structures* that the question involves, and it must be stated plainly what it does **not** derive.

**The chiral coupling is empirical input.** The weak interaction couples to left-handed fermion fields and not to right-handed ones. This is a fact about the world, established by the observation of parity violation in weak decays and by the helicity of the neutrino; it is not a consequence of the biquaternion algebra. The parent gauge article makes the corresponding structural statement: the gauge group canonically attached to the algebra is the *vector-like* central phase $\mathrm{U}(1)\subset\mathbb{C}_{\mathbb{B}}$, and a larger or chiral gauge structure requires an action that does not commute with the algebra, that is, a choice of representation. The framework therefore does not derive the Standard Model's chiral $SU(2)_L$ structure; it transcribes a chiral gauge theory onto the module, with the chiral assignment put in by hand, exactly as the read-list chirality article states for its abelian model. The left-handedness of the neutrino is, in this framework, an input.

**Which real structure a fermion uses is not selected by the algebra.** The algebra contains both structures. An unconstrained Dirac field $\Psi\in\Delta$ is what it is; imposing the fixed-point condition $\psi^{c}=\psi$ gives a Majorana field; and no internal principle of the biquaternion framework chooses one for the neutrino. A gauge-invariant Majorana mass requires the field to be a gauge singlet (or to lie in a real representation), while a Dirac mass requires a right-handed partner and a Higgs-type coupling; both are outside the algebra, and the choice between them is made by the measured spectrum, not by the framework.

**A Majorana pairing is genuinely antilinear, and it belongs to the real structure, not to the parent's mass term.** A genuine Majorana mass pairs the field with its conjugate, $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ with $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$, and because $\flat$ is $\mathbb{C}$-antilinear such a coupling is not invariant under the continuous central phase: a mass term that pairs the field with its conjugate breaks fermion number, which is the hallmark of a Majorana-type coupling. That is a genuine structural resemblance, and it is the reason the framework is *compatible* with a Majorana neutrino. The parent's own massive equation is by contrast the linear chiral pair of the Dirac article, whose mass term is linear and through which the central $\mathrm{U}(1)$ (fermion number) passes; only the axial symmetry is broken by it. The antilinear pairing belongs to the real structure $\flat$ and to the single-field equation built on it, which is a different equation, with central-phase plane waves on the spacelike locus. Resemblance is not derivation, and two qualifications keep it in place. The equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ does not impose $\tilde{\Psi}^{\flat}=\tilde{\Psi}$: it couples a field to its conjugate without identifying the two, which is what a mass term does, not what a reality condition does. And whether its $\flat$-pairing should be read as charge conjugation or as a real-form presentation of a Dirac mass is an open question of the corpus, not a settled result.

This article does not resolve it. The distinction between the real structure $\flat$ and the charge-conjugation real structure $\mathcal{C}$, drawn in the previous two sections, is precisely the reason the question is delicate: $\flat$ is order-reversing and its fixed space is the material sector, so if it is a charge conjugation it is a different one from the module real structure constructed above.

**What is outside the framework entirely.** The value of the neutrino mass, the see-saw mechanism, lepton mixing, and the Majorana phases of the mixing matrix are not represented. The framework offers no prediction for any of them, and in particular no prediction for the rate of neutrinoless double beta decay, the process that would establish the Majorana nature experimentally. No expectation of that kind is claimed here.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| A charge-conjugation real structure on $\Delta$, with $\mathcal{C}^2=1$ and the constraint $\psi^{c}=\psi$ | **Supplied**, by the coefficient conjugation $\bar{\cdot}$ transported to the module; verified |
| The Majorana component count $\dim_{\mathbb{R}}=4$ and the exchange of the chiral halves | **Supplied** |
| Existence of Majorana and non-existence of Majorana–Weyl in $(1,3)$ | **Transcribed** from *Real Spinors and Reality Conditions with Inner Conjugation*, which takes the real structure to commute with the full Clifford action, under which $(1,3)$ is symplectic Majorana |
| The explicit charge-conjugation cell $C$, its frame dependence, and the exchange of the chiral halves | **Transcribed**; frame and signature stated |
| Consistency of the constraint with the massive equation | **Supplied** (the frame cells are imaginary and the pair operator uses the real cells, so $\mathcal{C}$ commutes with $\mathbb{D}$; the constraint is propagated and what flips is the frequency) |
| The bilinear physics: no vector current, mass and axial current permitted | **Supplied at the level of the anticommuting field**; not visible in a commuting c-number spinor |
| A chiral gauge group, and the left-handedness of the neutrino | **Not supplied**; empirical input, transcribed |
| The material/informational split as the Majorana reality condition | **Not supplied**; it obstructs, as shown above |
| Whether the neutrino is Dirac or Majorana | **Not decided** by the framework |
| The neutrino mass value, the see-saw, mixing, and the Majorana phases | **Outside** |
| Majorana spinors as boundary states of a time-like surface in three-dimensional quantum gravity | **Not supplied**; external, cited below |

## Majorana Spinors in a Geometric Setting Outside the Framework

The Majorana spinor is treated in this article as the carrier of a fermion. It also has a modern **geometric** use, external to the framework, in which a pair of Majorana spinors models a surface in three-dimensional Minkowski space; the use is worth recording because it shows the pair — not a single Weyl spinor — in a role where its real structure is what makes the geometry work.

The setting is the spinfoam boundary of three-dimensional Lorentzian quantum gravity. A boundary triangle is labelled by a holonomy whose group depends on causal character: $SU(2)$ when the triangle and its tetrahedron are space-like, and $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$ — the double cover of $SO(1,2)$, and the oscillator's dynamical group — in the two time-like cases. The external paper cited below models the three homogeneous spaces of these groups on spinors of the defining module with the indefinite pairing $[w|v]=w^{\dagger}\sigma_3v$:

- the sphere $S^2$, from one Weyl spinor, $v_i=\langle z|\sigma_i|z\rangle$;
- the two-sheeted time-like hyperboloid $H^\pm$, from one Weyl spinor with the indefinite pairing, $v_i=\tfrac12\langle z|\sigma_3\varsigma_i|z\rangle$ with $\varsigma_1=\sigma_3$, $\varsigma_2=i\sigma_2$, $\varsigma_3=-i\sigma_1$;
- the one-sheeted hyperboloid $H^{sl}$, from a **pair** of Majorana spinors, $v_i=\langle z_2|\sigma_3\varsigma_i|z_1\rangle$, with a real structure that commutes with $SU(1,1)$ taking the place of the complex conjugation of the other two cases.

Two points connect this to the present article. First, the operation that appears here is the *same kind* of object as the module real structure $\mathcal{C}$ of the preceding sections — a conjugate-linear involution used to select a real form of a complex module — although it acts on the indefinite form rather than on the Dirac module, and it is required to commute with $SU(1,1)$ rather than with the full Clifford action. Second, the reason the one-sheeted case needs a *pair* is stated in the paper as a sign statement: a single Weyl spinor with either pairing forces one sign of the area spectrum, and only the pair carries the sign that a time-like surface requires. That is the same style of argument as the one used above for the Majorana mass, where it is the reality of the mass term, not the geometry, that selects the conjugate-linear structure.

None of this is derived by the framework. The hyperboloid models are a standard-theory result, the group $SU(1,1)$ appears here only as a subgroup of the rotor group and as the oscillator's dynamical group, and nothing in the preceding sections is changed by the citation. It is recorded because it is the one place outside the particle-physics literature where the Majorana pair is put to a geometric use, and because the surface it models — the time-like boundary — is exactly the case the framework's own two-sided rotor action is built for.

## Open Questions

1. **The algebra-level form of the reality condition.** This article identifies the operation — the coefficient conjugation $\bar{\cdot}$ — but works with the explicit cell frame and the central scalar $K=i$ on the module. What is the biquaternion-valued rule that corresponds to $\psi\mapsto K\psi^{*}$ in the algebra, and how does it relate to the algebra's real structure $\flat$? The module real structure is the one that carries the Majorana condition; the parent's mass term is the linear chiral pair and is not at issue here.

2. **The status of the $\flat$-pairing.** Is the single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$, built on the algebra's real structure, a Majorana mass or an ordinary Dirac mass written on a real form? That equation is separate from the parent's linear chiral-pair mass term, whose fermion number is conserved. The present article sharpens the question: the real structure $\flat$ is an order-reversing conjugation whose fixed space is $\mathbb{M}_-$, so if it is a charge conjugation it is a different one from the module real structure constructed here.

3. **The sector split, in any other guise.** The obstruction above rules out the naive identification of Majorana with $\mathbb{M}_-$. Whether some other use of the split — a different module, a different pairing, or a combination of $\flat$ with the module identification — can carry a reality condition is not settled.

4. **Dimension-five operators.** Neutrino masses in the Standard Model are generated by a dimension-five operator after electroweak symmetry breaking. Whether the biquaternion framework can represent such an operator, and whether it has anything to say about the see-saw, is not attempted.

5. **CP and the Majorana phases.** The Majorana nature of a fermion is entangled with the reality properties of its mass matrix and with CP violation. A treatment belongs with the corpus's CP and CPT material; the CPT article is not yet written, and nothing is claimed here.

6. **Empirical contact.** The decisive experiment is neutrinoless double beta decay. The framework offers no rate and no prediction; the question of whether it can be brought into contact with one is open.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. In cells they are

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of a cell $M$ in the basis of the sixteen products.

Each of these is one product of a left and a right multiplication, so its coefficient matrix $c(\gamma_\mu)$ is a pure tensor: the single products fill the seven-dimensional cone $\operatorname{rank}c(M)\le1$ inside the sixteen-dimensional cell algebra, a general element is a sum of at most four of them, and the least number of products needed is $\ell(M)=\operatorname{rank}c(M)$. The rank is that of $c(M)$ in the four-element basis of $\mathbb{B}$, not the rank of $M$ as a map of the module: $\gamma_0$ is invertible as a map and is still a single product.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_0)^2=I_4,\qquad
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
The four contraction sums depend on the frame through the squares of the cells, so no single list is canonical. In a frame in which all four cells square to $+I_4$ — the Euclidean frame — they are

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,
\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\delta\gamma_\mu=-2\gamma_\delta\gamma_\beta\gamma_\alpha .
$$

In the frame of this article, where one cell squares to $+I_4$ and three to $-I_4$, every index is a lower index and the metric enters the contraction itself, so the first two read

$$
\sum_\mu\gamma_\mu\gamma_\mu=-2I_4,
\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=2\bigl(1+g_{\alpha\alpha}\bigr)\gamma_\alpha ,
$$

the second sum being $4\gamma_0$ on the timelike cell and $0$ on the three spatial ones. Each of these values was computed in the frame stated and not carried over from another one.

## Summary

A Dirac fermion is an arbitrary element of $\Delta=S\oplus\bar{S}$, with independent chiral halves and eight real components. A Weyl fermion is an element of one half, chiral and — while its chirality is protected — massless. A Majorana fermion is a fixed point of a conjugate-linear real structure $\mathcal{C}$ on $\Delta$ with $\mathcal{C}^2=1$, with four real components, no vector current, and a permitted mass. In the Lorentzian signature $(1,3)$ Majorana spinors exist and Majorana–Weyl spinors do not, because the real structure that makes a spinor Majorana exchanges the two chiral halves instead of preserving them.

The charge conjugation of the Dirac module was constructed explicitly in the cell frame with $g=\mathrm{diag}(+,-,-,-)$: the cell $C=L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=R_{\vec e_x}^{\mathrm{pau}}$ satisfies $C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T}C^{-1}=-\,iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ and $C\,(iL_{e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^{T}C^{-1}=-\,iL_{e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and defines an antilinear involution $\psi^{c}=K\psi^{*}$ with $K=C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T}=i\,L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=i$ and $KK^{*}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. Every frame cell is $i$ times a real cell, so it is imaginary and charge conjugation negates it; the Dirac operator, however, is built from the real cells $L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$, whose coefficients conjugation fixes, and so $\mathcal{C}$ commutes with $\mathbb{D}$. The constraint $\psi^{c}=\psi$ is therefore propagated, the mass shell stays $p^{2}=m^{2}$, and the mass is permitted. What the antilinear map reverses is the frequency, not the mass: at fixed momentum it anticommutes with $\mathbb{D}_p$, so the conjugate of a positive-frequency amplitude is a negative-frequency one, and no single mode is self-conjugate. The field $\psi=u\,e_{+}+u^{c}\,e_{-}$ is both self-conjugate and massive, and the Majorana restriction removes half the degrees of freedom, not the mass. The vector current vanishes for a self-conjugate Grassmann field and the scalar and axial bilinears survive; those statements are properties of the anticommuting field, and a commuting c-number computation gives the opposite pattern.

In the biquaternion framework the charge conjugation is the real structure carried by the **coefficient complex conjugation** $\bar{\cdot}$, the only one of the algebra's conjugations that is a conjugate-linear automorphism, with fixed points $\mathbb{H}_{\mathbb{B}}$; the Hermitian conjugate and the real structure $\flat$ are order-reversing and cannot serve as module real structures. The material/informational split is the algebra's decomposition by ${}^{*}$, and although $\mathbb{M}_-$ is the four-real-dimensional fixed space of the real structure $\flat$ and superficially matches the Majorana count, the Dirac operator does not preserve it ($\vec e_x\in\mathbb{M}_-$ but $\vec e_x \vec e_x=-e_t\in\mathbb{M}_+$). The sector split therefore obstructs the reality condition and cannot be used as it stands; the Majorana real form lives on the spinor module, not on a subspace of the algebra. Finally, the left-handedness of the neutrino under the weak interaction is empirical input, the real structure $\flat$ carries a genuinely antilinear Majorana-type pairing that is compatible with but does not derive a Majorana neutrino, while the parent's own mass term is linear and conserves fermion number; the mass value and its consequences are outside the algebra.

Separately from this particle interpretation, the Majorana pair has a **geometric** use external to the framework: a pair of Majorana spinors with a real structure commuting with $SU(1,1)$ models a time-like surface of three-dimensional quantum gravity, and a sign of the area spectrum is what forces the pair rather than a single Weyl spinor. That construction is a standard-theory result; the framework does not derive it, and the citation changes nothing above it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}} = \{Q:\bar{Q}=Q\}$ | Real-quaternion subspace, fixed space of $\bar{\cdot}$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Complex scalar subspace; the centre |
| ${}^{\natural},\ \bar{\cdot},\ {}^{*}=({}^{\natural})^{\,*}$ | Quaternion, complex and Hermitian conjugations |
| $\tilde{Q}^{\flat}=-\tilde{Q}^{*}$ | Algebra's real structure; $\mathbb{C}$-antilinear involution, order-reversing; fixed space $\mathbb{M}_-$ |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$, $\mathsf{M}_2(i)=iI_2$ |
| $S = \mathbb{C}^2 = (\tfrac12,0)$ | Left-handed Weyl spinor module |
| $\bar{S} = (0,\tfrac12)$ | Right-handed Weyl spinor module (conjugate) |
| $\Delta = S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}\Delta=4$ |
| $\psi_L\in S,\ \psi_R\in\bar{S}$ | Left- and right-handed Weyl spinors |
| $\Gamma = -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | Chirality operator; $-1$ on $S$, $+1$ on $\bar{S}$, $\Gamma^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $P_{\pm}=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}\pm\Gamma)$ | Chirality projectors; $P_{+}+P_{-}=I_4$, $\mathcal{C}P_{\mp}=P_{\pm}\mathcal{C}$ |
| $iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$; $\nu(0)=x$, $\nu(1)=\nu(2)=\nu(3)=y$ | Frame cells; they carry the Clifford relations of $g$ |
| $L_a,R_b$, $L_{a}R_{b}$ | $L_a\psi=a\psi$, $R_b\psi=\psi b$; $L_{a}R_{b}\psi=a\psi b$ |
| $g=\mathrm{diag}(+,-,-,-)$, $\varepsilon_\mu=g_{\mu\mu}$ | Clifford signature and its sign vector, $\varepsilon_0=+1$, $\varepsilon_k=-1$ |
| $C = L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=R_{\vec e_x}^{\mathrm{pau}}$ | Charge-conjugation cell; $C^{T}=-C$, $C^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $K = C\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^{T} = i\,L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=i$ | The central imaginary that carries the real structure; $KK^{*}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $\mathcal{C}:\psi\mapsto K\psi^{*}$ | Charge conjugation as an antilinear involution; commutes with $\mathbb{D}$ |
| $\bar{\psi} = \psi^{\dagger}iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | Dirac bar on the module; on the fixed space $\bar{\psi}=-C\psi$ |
| $\psi^{c} = \mathcal{C}\psi$ | Charge conjugate; $\psi^{c}=\psi$ defines Majorana |
| $\psi=i\psi^{*}$ | Majorana condition |
| $\mathbb{D}\,\psi=m\psi^{c}$ | Majorana equation |
| $\mathbb{D}=-\sum_\mu\varepsilon_\mu L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\partial_\mu$ | Pair operator in real cells; symbol $\mathbb{D}_p$, $\mathbb{D}_p^2=p^2$ |
| $j_\mu=\bar{\psi}\,iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\psi$; $\bar{\psi}\psi$; $j^{5}_\mu=\bar{\psi}\,iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\Gamma\psi$ | Vector, scalar and axial bilinears |
| $\Lambda C \Lambda^{T}$ | Charge-conjugation cell under a linear change of frame $\Lambda$ |
| $\dim_{\mathbb{R}}\{\psi:\psi^{c}=\psi\}=4$ | Majorana component count |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form on the informational sector |
| $[w|v]=w^{\dagger}\sigma_3v$ | Indefinite $SU(1,1)$-invariant pairing (external geometric usage) |
| $v_i=\langle z_2|\sigma_3\varsigma_i|z_1\rangle$ | Majorana-pair bilinear modelling the one-sheeted hyperboloid $H^{sl}$ |

## Further Reading

- Ettore Majorana, "Teoria simmetrica dell'elettrone e del positrone", *Nuovo Cimento* **14** (1937) 171–184, the original symmetric theory of the electron and positron, where the self-conjugate spinor is introduced.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of Dirac, Weyl and Majorana fields, the charge-conjugation matrix, and the relation between the reality of the mass term and fermion-number conservation.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Dirac bilinears, charge conjugation in the chiral basis, and the Majorana mass term.
- Rabindra N. Mohapatra and Palash B. Pal, *Massive Neutrinos in Physics and Astrophysics* (World Scientific, 2004), for the Dirac/Majorana distinction, the see-saw mechanism, and neutrinoless double beta decay.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification of real structures on spinor modules by signature.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the relation between spinors, the charge-conjugation operation, and the Lorentz group in a real Clifford algebra.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the geometric use of a *pair* of Majorana spinors modelling a time-like surface in three-dimensional quantum gravity, with a real structure commuting with $SU(1,1)$ and the area-spectrum sign argument that distinguishes the pair from a single Weyl spinor. External; cited for the geometric use only.
- Companion articles: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html); *Spinors*; *Spinors categorization*; [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html).
