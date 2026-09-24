# __Chiral Fermions in the Biquaternion Framework__

## Introduction

A **chiral fermion** is a fermion whose left- and right-handed components carry *inequivalent* representations of the gauge group. The **vector-like** alternative is a fermion whose two chiral components carry the same representation; a vector-like fermion may have a mass term that pairs the two components, and a chiral fermion may not. The distinction is not a technicality: the matter content of the Standard Model is chiral, with the left-handed quarks and leptons in $SU(2)$ doublets and their right-handed partners in singlets, and the immediate kinematic consequence is that no bare fermion mass is gauge invariant. The electron mass appears only after electroweak symmetry breaking, through the coupling of the two chiralities to the Higgs field, whose vacuum expectation value carries the charge that the mass term lacks.

This article asks what the biquaternion framework, in the notation of the companion articles, supplies for that structure. The presentation is organized around one question — *can the framework distinguish the two chiralities in a gauge interaction?* — and the answer is split, at the outset, into the three categories the corpus uses.

- **Established, and recomputed below.** The biquaternion Dirac field decomposes into two chiral halves; the chirality operator $\gamma_5$ is an involution, $\gamma_5^2=I_4$, and the projectors $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$ are well defined and Lorentz invariant, and are idempotent, orthogonal and complete; the Dirac mass bilinear is chirality-odd and vanishes on a field of definite chirality. On the Dirac module a *chiral* abelian gauge symmetry with independent charges $q_L,q_R$ is consistent: the covariant derivative $D_\mu=\partial_\mu+\tfrac{i}{\hbar}A_\mu Q$, $Q=q_LP_L+q_RP_R$, is gauge covariant for arbitrary charges, with curvature $[D_\mu,D_\nu]=\tfrac{i}{\hbar}F_{\mu\nu}Q$. The mass bilinear is gauge invariant if and only if $q_L=q_R$: a chiral fermion cannot carry a bare Dirac mass.
- **Established from the read list, and sharpened here.** The gauge group of the biquaternionic abelian gauge principle is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$, and a central element acts as a **scalar** on the algebra $M_2(\mathbb{C})$. A gauge group drawn from the center therefore assigns every component the same charge: it is vector-like and cannot be chiral. Chirality requires a gauge action that is not scalar, hence non-central — the structure whose algebraic status the gauge article leaves open.
- **Gap, left visible.** Whether the algebra's real structure $\flat=-\dagger$ carries a physical Majorana-type pairing, or whether its conjugate equation is the real-form expression of an ordinary Dirac mass, is not settled here. The parent's own mass term is the linear chiral pair, through which the continuous central phase passes and which preserves the vector $U(1)$; the antilinear fermion-number-breaking pairing is the separate equation built on $\flat$. This is the read-list gauge article's open question, and the companion on the neutrino and Majorana fermions is where it belongs. It is recorded here only for its consequence: the framework's vector-like gauge structure and the real structure's antilinear pairing do not naturally meet.

The article is organized as follows. The next section recalls the chiral decomposition of the biquaternion Dirac field and the projectors, and checks them against the mass term rather than only against the massless equation. The section after that writes the chiral gauge symmetry on the Dirac module and derives the mass selection rule. A section then determines what the algebra's center supplies, and why it is vector-like; a section treats the mass term and the algebra's real structure; a section separates chirality from the material/informational sector split; and a closing section separates what the framework supplies from what it only transcribes.

Open questions follow.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The conjugations are the quaternion conjugate $\bar{\cdot}$, the complex conjugate ${}^{*}$ (conjugation of the coefficients) and the Hermitian conjugate ${}^{\dagger} = \bar{\cdot}^{\,*}$; the anti-Hermitian conjugate is $\tilde{Q}^{\flat} = -\tilde{Q}^{\dagger}$. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The matrix realization is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$; the spinor module is $S=\mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, carrying the left-handed Weyl representation $(\tfrac12,0)$, and its complex conjugate $\bar{S}=(0,\tfrac12)$ is the right-handed Weyl module. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Two Chiral Halves and the Projectors

The chiral decomposition is a property of the spinor module, and it is inherited unchanged from the read list. The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a single simple module $S$; the left-handed Weyl spinor is $V_1=(\tfrac12,0)$, carried by $S$, and the right-handed Weyl spinor is its complex conjugate $\bar{S}=(0,\tfrac12)$. Their direct sum

$$
\Delta \;=\; S\oplus\bar{S}\;=\;\left(\tfrac12,0\right)\oplus\left(0,\tfrac12\right),
\qquad \dim_{\mathbb{C}}\Delta = 4,
$$

is the **Dirac spinor module**. Written in blocks, a Dirac spinor is

$$
\Psi = \begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix}, \qquad \psi_L\in S,\quad \psi_R\in\bar{S},
$$

and $SL(2,\mathbb{C})$ acts block-diagonally by $S(\tilde{\Lambda}) = \mathrm{diag}\big(g,\ \Phi(\tilde{\Lambda}^{*})\big)$, $g=\Phi(\tilde{\Lambda})$.

The **chirality operator** on $\Delta$ is

$$
\gamma_5 = \begin{pmatrix}-I_2 & 0\\ 0 & I_2\end{pmatrix},
\qquad \gamma_5^2 = I_4,
$$

and the **chiral projectors** are

$$
P_L = \tfrac12\left(I_4-\gamma_5\right) = \begin{pmatrix}I_2&0\\0&0\end{pmatrix},
\qquad
P_R = \tfrac12\left(I_4+\gamma_5\right) = \begin{pmatrix}0&0\\0&I_2\end{pmatrix}.
$$

Their elementary algebra is exact:

$$
P_L^2 = P_L, \qquad P_R^2 = P_R, \qquad P_LP_R = P_RP_L = 0, \qquad P_L+P_R = I_4, \qquad \gamma_5 = P_R-P_L,
$$

and each is Hermitian of trace $2$, so each projects onto a complex two-dimensional half. In the block basis with

$$
\gamma^0 = \begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},
$$

the chirality operator anticommutes with every generator, $\{\gamma_5,\gamma^\mu\}=0$, and therefore commutes with every even product of generators, the biquaternion algebra among them: $[\gamma_5,\gamma^\mu\gamma^\nu]=0$. Since the Lorentz action is generated by the even elements, it commutes with $\gamma_5$ and with each $P_{L,R}$.

**The check that is not the massless case.** A projector is easy to check on the equation that suggested it, namely the massless Dirac equation, where the two halves decouple and the projector merely selects one of the two resulting Weyl equations. The claim that survives the mass term is different, and it is the one worth stating: chirality is a **Lorentz-invariant** label, not a property of the massless limit. The Lorentz generators are the bivectors $\gamma^\mu\gamma^\nu$, and $[\gamma_5,\gamma^\mu\gamma^\nu]=0$ holds identically, with or without a mass. The mass does not enter the commutator that makes chirality Lorentz invariant; what the mass does is to make the two halves visible to each other, and that is a statement about the equation, not about the invariance of the label.

**What the mass term does to a chirality-definite state.** Let $\bar{\Psi} = \Psi^{\dagger}\gamma^0$. In the block basis,

$$
\bar{\Psi}\Psi = \Psi^{\dagger}\gamma^0\Psi = \psi_L^{\dagger}\psi_R + \psi_R^{\dagger}\psi_L,
$$

the **Dirac mass bilinear**. It is off-diagonal in the chiral blocks: it pairs $\psi_L$ with $\psi_R$ and never a half with itself. Under the discrete chirality transformation $\Psi\mapsto\gamma_5\Psi$ one has $\bar{\Psi}\mapsto-\bar{\Psi}\gamma_5$, so

$$
\bar{\Psi}\Psi \;\longmapsto\; (-\bar{\Psi}\gamma_5)(\gamma_5\Psi) = -\bar{\Psi}\Psi :
$$

the mass bilinear is **chirality-odd**. Equivalently, if $\Psi$ has definite chirality, $\gamma_5\Psi=\pm\Psi$, then the two blocks are $\Psi=( \psi_L,0)$ or $(0,\psi_R)$ and

$$
\bar{\Psi}\Psi = 0 .
$$

A field of definite chirality has no Dirac mass bilinear at all. This is the precise sense in which a lone Weyl field cannot carry a mass, and it is the algebra behind the Standard Model's chiral matter.

**Framework caution.** Chirality is not visible to the algebra $\mathbb{B}$ alone. The algebra is simple, with one simple module; the two minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$, $p=\tfrac12(e_0+ie_3)$, $q=\tfrac12(e_0-ie_3)$, are both isomorphic to $S$ and carry the *same* defining representation. The chiral halves are $S$ and $\bar{S}$, and the distinction between them is a real-structure distinction: it appears only when complex conjugation is taken into account, or when the algebra is complexified, where the central idempotents $\tfrac12(1\pm\gamma_5)$ split

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B} \;\cong\; M_2(\mathbb{C})\oplus M_2(\mathbb{C})
$$

into the two chiralities. **A biquaternion $\tilde{\Psi}\in\mathbb{B}$ is therefore never chiral by itself.** It is the module object $\Psi\in\Delta$ that carries the chirality label, and the operation that relates the two halves is the conjugation $\tilde{\Psi}\mapsto\tilde{\Psi}^{*}$ — a real-form operation distinct from the parent's mass term (the linear off-diagonal chiral pair) and from the algebra's order-reversing real structure $\flat$.

The read-list articles record that the embedding of the projectors in $\mathbb{B}$ (as opposed to in its complexification) is not settled; nothing below requires such an embedding.

## Chiral Gauge Symmetry on the Dirac Module

The gauge principle of the read list localizes a **central** phase: $\lambda=e^{iq\Gamma(\tilde{X})/\hbar}$, with $q$ a single coupling, and it produces a covariant derivative $D=\tilde{\nabla}+\tfrac{iq}{\hbar}\tilde{A}$. A single coupling acts on the whole Dirac field; to make the gauge action *chiral* we must let the two halves carry independent charges. On the module this is elementary, and we write it out because the selection rule below is read off from it.

Introduce a real scalar gauge function $\Gamma(\tilde{X})$ and two real charges $q_L, q_R$, and set

$$
Q \;=\; q_L P_L + q_R P_R \;=\; \begin{pmatrix} q_L I_2 & 0\\ 0 & q_R I_2\end{pmatrix},
\qquad
\Lambda(\tilde{X}) \;=\; \exp\!\left(\frac{i}{\hbar}\,\Gamma(\tilde{X})\,Q\right) \;=\; \begin{pmatrix} e^{iq_L\Gamma/\hbar}I_2 & 0\\ 0 & e^{iq_R\Gamma/\hbar}I_2\end{pmatrix}.
$$

The gauge transformation is $\Psi\mapsto\Lambda\Psi$, and the connection transforms as $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$, exactly as in the abelian gauge principle. The covariant derivative is the module operator

$$
D_\mu \;=\; \partial_\mu + \frac{i}{\hbar}\,A_\mu\,Q ,
\qquad\text{so that}\qquad
D_\mu'(\Lambda\Psi) \;=\; \Lambda\,D_\mu\Psi
$$

for the derivative $D'$ built from $A_\mu'=A_\mu-\partial_\mu\Gamma$. The covariance is a two-line computation:

$$
\begin{aligned}
D_\mu'(\Lambda\Psi)
&= \partial_\mu(\Lambda\Psi) + \frac{i}{\hbar}A_\mu' Q\,\Lambda\Psi
= \frac{i}{\hbar}(\partial_\mu\Gamma)Q\,\Lambda\Psi + \Lambda\,\partial_\mu\Psi + \frac{i}{\hbar}(A_\mu-\partial_\mu\Gamma)Q\,\Lambda\Psi \\
&= \Lambda\,\partial_\mu\Psi + \frac{i}{\hbar}A_\mu Q\,\Lambda\Psi
= \Lambda\,D_\mu\Psi,
\end{aligned}
$$

where the second step uses $\Lambda$ diagonal with constant $Q$, so that $\partial_\mu\Lambda=\tfrac{i}{\hbar}(\partial_\mu\Gamma)Q\Lambda$ and $Q$ commutes with $\Lambda$. This holds for **arbitrary** $q_L,q_R$. The curvature is likewise weighted by the charge operator,

$$
[D_\mu,D_\nu] \;=\; \frac{i}{\hbar}\,F_{\mu\nu}\,Q, \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu ,
$$

which is the abelian curvature of the one connection $A_\mu$, distributed between the two chiralities by $Q$.

Two structural remarks belong here, because they distinguish this construction from the framework's own gauge principle.

1. **The chiral connection is a module operator, not a biquaternion.** The object $A_\mu Q$ acts on the Dirac module $\Delta$; it is not a single element of $\mathbb{B}$ multiplying the field from the left. Writing $I_4=P_L+P_R$ and $\gamma_5=P_R-P_L$ gives $Q=\tfrac{q_L+q_R}{2}I_4+\tfrac{q_R-q_L}{2}\gamma_5$: the first term is central and lies in $\mathbb{B}$, the second is the chiral part and is proportional to $\gamma_5$, which is a central idempotent combination of the complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}$, not an element of $\mathbb{B}$. So the chiral gauge structure does not fit the form $\tilde{\nabla}+\tfrac{iq}{\hbar}\tilde{A}$ with $\tilde{A}\in\mathbb{B}$; it is a connection valued in the algebra of module endomorphisms.
2. **The abelian chiral connection is genuinely scalar in the curvature.** Since $Q$ is constant, the components commute in the abelian case, and the curvature is the ordinary $F_{\mu\nu}$; the chirality enters only through the charge weighting. A non-abelian chiral connection would additionally require $Q$ to be replaced by generators that do not commute, which is the gap treated in the next section.

**The mass selection rule.** The scalar Dirac bilinear of the preceding section is the Lorentz-invariant pairing of the two halves available to a mass term. Under the chiral gauge transformation,

$$
\psi_L \longmapsto e^{iq_L\Gamma/\hbar}\psi_L, \qquad \psi_R \longmapsto e^{iq_R\Gamma/\hbar}\psi_R,
$$

so that the coefficient of $\psi_L^{\dagger}\psi_R$ acquires a position-dependent phase while its conjugate acquires the inverse phase. Since $\bar{\Psi}\Psi$ is real and equals $2\,\mathrm{Re}(\psi_L^{\dagger}\psi_R)$,

$$
\bar{\Psi}\Psi
\;\longmapsto\;
2\,\mathrm{Re}\!\left(e^{\frac{i}{\hbar}(q_R-q_L)\Gamma}\,\psi_L^{\dagger}\psi_R\right),
$$

which is position dependent unless the phase is unity. The bilinear is gauge invariant for all gauge functions $\Gamma$ **if and only if**

$$
q_R = q_L .
$$

This is the **mass selection rule**: a bare Dirac mass is compatible with the gauge symmetry exactly when the two chiralities carry the same charge, i.e. exactly when the fermion is vector-like. A genuinely chiral fermion, $q_R\neq q_L$, has no gauge-invariant bare mass; its mass must wait for a field carrying the compensating charge $q_L-q_R$ (the mass bilinear acquires the phase $e^{i(q_R-q_L)\Gamma/\hbar}$), which is what the Higgs mechanism supplies. The rule was checked on both branches: it holds for all $\Gamma$ when $q_L=q_R$ (the vector-like case, including $q_L=q_R=0$), and it fails for the chiral case $q_L\neq q_R$, including the axial assignment $q_R=-q_L$. In particular the rule is not merely "some charge is preserved": an axial $U(1)$, which carries opposite charges on the two halves and is the natural first guess for a chiral symmetry, does not preserve the mass either.

**No opposite-chirality partner.** A field of definite chirality has $\bar{\Psi}\Psi=0$ identically, so even before the gauge symmetry is imposed there is nothing for the mass to multiply. The two statements — the bilinear vanishes on a chiral state, and it is not gauge invariant when the charges differ — are the algebraic form of the single physical fact that a chiral fermion is massless in the unbroken phase.

## What the Center Supplies: A Vector-Like Abelian Sector

The gauge group of the biquaternionic abelian gauge principle is not chosen; it is the **unitary part of the center** of the algebra,

$$
\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,\,ie_0\}, \qquad U(1) = \{e^{i\theta} : \theta\in\mathbb{R}\} \subset \mathbb{C}_{\mathbb{B}}.
$$

A central element commutes with every biquaternion, and this is what makes the construction abelian. It also fixes the way the group can act on matter. On the matrix algebra $M_2(\mathbb{C})$, left multiplication by a central element $\lambda$ is multiplication by a **scalar**,

$$
M \;\longmapsto\; \lambda M, \qquad \lambda = e^{i\theta},
$$

so that every entry, and in particular every column of $M$, acquires the same factor. The two columns are the regular module's two copies of $S$. A gauge group drawn from the center therefore acts by a scalar on the matter module: it assigns every component the **same** charge. Such a group cannot distinguish $\psi_L$ from $\psi_R$, and it cannot be the source of a chiral gauge interaction. The abelian sector of the framework is **vector-like**.

The converse statement is the useful one. A *chiral* gauge action has $q_L\neq q_R$; by the argument above it cannot be central, and a non-central gauge group is not supplied by the biquaternionic gauge principle, whose group is the center. (The abelian chiral structure of the preceding section acts on the module, not by an element of $\mathbb{B}$ — structural remark 1.) The center supplies a canonical abelian gauge group and nothing chiral; chirality requires a non-central, module-realised action whose algebraic status the read-list gauge article leaves open. There the gap is that $\mathbb{B}\cong M_2(\mathbb{C})$ has commutator algebra $\mathfrak{gl}(2,\mathbb{C})$, not a compact simple algebra, so that a reality and tracelessness condition must select a compact gauge algebra before a Yang–Mills structure can be claimed. The present article inherits that gap and sharpens its meaning: **without those conditions the framework has no chiral gauge group at all, because the only gauge group it supplies canonically is the scalar center.**

**A qualification about the two readings of the phase.** The argument above is robust in one direction: a gauge group *drawn from the center* is scalar and hence vector-like on the algebra. But the corpus does not settle how the biquaternion field is identified with the Dirac module, and the qualification is worth stating rather than hiding. The left regular module is $S\oplus S$, whose two columns both carry the defining representation; the Dirac module is $S\oplus\bar{S}$, whose second factor carries the conjugate action. The passage between them is the real structure, complex conjugation, and under the Lorentz action the conjugate factor transforms by $\Phi(\tilde{\Lambda}^{*})$. Applied to a central phase $\lambda=e^{i\theta}$ this assignment would give $e^{i\theta}$ on the left-handed half and $\Phi(\lambda^{*})=e^{-i\theta}$ on the right-handed half — an **axial**, not vector-like, action. Which reading is the physical one is the same unsettled question as the embedding of the projectors (the "two-$i$" point), and the present article does not decide it. What is decided is the implication: the center cannot supply *independent* left and right charges, whichever reading of the phase is adopted — under the vector-like reading the two charges are equal, and under the axial reading they are locked to the single ratio $q_R=-q_L$ — so the center is chiral only in that locked ratio and cannot be the source of a general chiral gauge group. (The center is a complex line, one-dimensional over $\mathbb{C}$, not over $\mathbb{R}$.) The non-central gap is therefore a prerequisite for a general chiral gauge sector under either reading.

## The Mass Term and the Real Structure

The biquaternion Dirac equation of the parent is

$$
\tilde{\nabla}\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\,\tilde{\Psi}_R
$$

for mass $m$, and $\tilde{\nabla}\tilde{\Psi}=0$ in the massless case. The mass term is **linear** in the field and off-diagonal in chirality. Because it is linear, the central phase passes through it: under the global phase $\tilde{\Psi}\mapsto\lambda\tilde{\Psi}$ both sides acquire the same factor $\lambda$, so the continuous $U(1)$ (fermion number) is conserved for the massive field, not only for the massless one. What the mass term breaks is the **axial** symmetry: for the spinor-module field, $\partial_\mu j_5^\mu = 2im\,\bar{\psi}\gamma_5\psi$, which vanishes only at $m=0$. The vector current is conserved at every $m$, the axial current only at $m=0$. The mass term is also what distinguishes the massive biquaternionic equation from the massless one, which is identical in form to the source-free Maxwell equation.

The algebra carries, besides the conjugations used above, the **anti-Hermitian conjugation** $\flat=-\dagger$ and its role as the algebra's **real structure**:

$$
\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger},
$$

a $\mathbb{C}$-**antilinear** involution, order-reversing with a sign, $\left(\tilde{A}\tilde{B}\right)^{\flat}=-\tilde{B}^{\flat}\tilde{A}^{\flat}$, acting as $+1$ on $\mathbb{M}_-$ and $-1$ on $\mathbb{M}_+$, with fixed space the anti-Hermitian sector $\mathbb{M}_-$. A coupling built on $\flat$ pairs the field with its **conjugate** rather than with an independent field of the same charge, and because $\flat$ is antilinear such a coupling is not invariant under the continuous central phase. In the standard classification this is a **Majorana-type** mass: it is allowed only for a neutral fermion, and it breaks the continuous fermion-number $U(1)$ to a sign. A mass that pairs $\psi_L$ with an independent $\psi_R$ of equal charge is a **Dirac** mass, and it preserves that $U(1)$. The parent's mass is of the second type — the linear off-diagonal pair above, whose bilinear $\bar{\Psi}\Psi=\psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ carries the selection rule of the preceding section. A coupling of the first type is a *separate* equation built on the real structure, $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$, whose central-phase plane waves sit on the spacelike locus rather than on the physical mass shell.

**The real structure's pairing is left open, and it is genuinely Majorana-type.** Whether the framework intends the $\flat$-pairing as a physical Majorana coupling, or whether it is the real-form expression of an ordinary Dirac mass whose $U(1)$ is realized differently on the module, is not decided here. The question's locus is the companion on the neutrino and Majorana fermions, together with the parent Dirac article's open question 1, which asks what the real structure $\flat$ means in terms of the electroweak interaction. (The gauge article recorded this question as its open question 5; with the mass now linear, that slot carries the axial symmetry as the live item, and it retains the pairing question alongside it as a re-attribution.)

What this article adds is the connection to chirality: the real structure $\flat$ is order-reversing and maps the two chiral ideals into one another, so a coupling built on it couples the field to its own chirality conjugate. That is the genuine Majorana statement, and it belongs to $\flat$, not to the parent's mass term. The parent's mass term, by contrast, is off-diagonal in the chiral blocks and preserves the vector $U(1)$; it is the axial current, not the vector one, that it fails to conserve. This is the equation-side form of the vanishing of the Dirac bilinear on a definite-chirality state.

## Chirality Is Not the Sector Split

Three decompositions of the framework are in play in this article and its parents, and they must not be conflated.

- The **chiral decomposition** is a decomposition of the spinor module $\Delta$ by the operator $\gamma_5$, into $S$ and $\bar{S}$. Its projectors are $P_L,P_R$, and it is the subject of this article.
- The **sector decomposition** is a decomposition of the algebra $\mathbb{B}$ by Hermitian conjugation $\dagger$, into the anti-Hermitian $\mathbb{M}_-$ and the Hermitian $\mathbb{M}_+$. Its projectors are the maps $\tilde{Q}\mapsto\tfrac12(\tilde{Q}\mp\tilde{Q}^{\dagger})$.
- The **ideal decomposition** is the Peirce decomposition $\mathbb{B}=\mathbb{B}p\oplus\mathbb{B}q$ by the primitive idempotents $p=\tfrac12(e_0+ie_3)$, $q=\tfrac12(e_0-ie_3)$. Its two summands are *both* copies of $S$; it is not a chirality decomposition, as the read-list spinor article stresses.

The chiral projectors act on the module; the sector projectors act on the algebra; the Peirce projectors act on the algebra by right multiplication and produce two identical modules. The first two act on different spaces and compose to nothing; the first and third are different decompositions of different objects and, in particular, $P_L$ is not $p$ or $q$. The electron article of the corpus reaches the same conclusion from the physical side and records that "chirality is not the same as the sector split" and that "the two decompositions share no projector". This article inherits that finding unchanged; it is repeated here only because a reader of the gauge principle might be tempted to identify the internal chirality with the material/informational split, and the temptation is without algebraic support.

## What the Framework Supplies, Transcribes, and Does Not Supply

**What it supplies.**

- *The two-chiral structure and its projectors.* The spinor module decomposes into $S\oplus\bar{S}$; $\gamma_5$ (with $\gamma_5^2=I_4$) and $P_{L,R}$ are exact and Lorentz invariant, and the projectors are idempotent, orthogonal and complete. The algebra of the projectors has been checked, including the commutation with the even (Lorentz) generators that survives the mass term.
- *The chirality-oddness of the mass.* The Dirac bilinear is odd under $\gamma_5$ and vanishes on a definite-chirality state; the parent's mass term is the linear off-diagonal chiral pair, while the algebra's real structure $\flat$ is the order-reversing conjugation that exchanges the chiral ideals. This is established.

- *The chiral gauge covariant derivative on the module.* For independent charges $q_L,q_R$ the derivative $D_\mu=\partial_\mu+\tfrac{i}{\hbar}A_\mu Q$ is covariant with $Q=q_LP_L+q_RP_R$, and its curvature is $\tfrac{i}{\hbar}F_{\mu\nu}Q$. This is the standard chiral abelian gauge structure, expressed on the biquaternion spinor module.
- *The mass selection rule.* A bare Dirac mass is gauge invariant iff $q_L=q_R$; a chiral fermion is massless in the unbroken phase. This is established by direct computation and is the algebraic content of the Standard Model's need for a Higgs field.
- *The vector-like character of the center.* The only canonically available abelian gauge group is the scalar center, which cannot be chiral.

**What it only transcribes.**

- *The global-to-local gauge argument itself.* The localization of a phase and the appearance of a connection are the read-list gauge principle's; the chiral variation above is that argument run with a charge operator $Q$ instead of a scalar charge $q$.
- *The Higgs requirement.* That a chiral fermion needs a compensating scalar field is read off the selection rule; the mechanism by which the scalar acquires its expectation value is the subject of the planned companion on the Higgs mechanism, and is not derived here.
- *The Weyl/Dirac split.* The two-component equations of the massless limit, and the helicity–chirality locking, are worked in the exercise articles of the read list; this article uses them and does not re-derive them.

**What it does not supply.**

- *A chiral gauge group.* The center is scalar and vector-like; a non-central gauge structure, and with it the reality and compactness conditions that would select a compact gauge algebra, are not derived. This is the principal gap.
- *The value of the charges.* $q_L$ and $q_R$ are parameters, exactly as $q$ is in the abelian gauge principle; the algebra does not fix them.
- *The resolution of the real structure's pairing.* The parent's mass term is the linear chiral pair and conserves fermion number; whether the separate antilinear pairing built on $\flat$ is Majorana-type or a real-form Dirac mass is open, and is the pivot on which the framework's chiral sector turns.

- *Anomaly cancellation.* A chiral gauge theory with independent left and right charges must satisfy consistency conditions on the spectrum; no biquaternion formulation of the anomaly is attempted here. The planned companion on instantons and solitons is the natural place for it.
- *Empirical contact.* As everywhere in the framework, no prediction distinguishing it from the standard chiral gauge theory is offered.

## Open Questions

1. **Can the framework host a chiral gauge group?** The center supplies only a scalar, vector-like abelian group. Chirality requires a non-central action, hence a gauge group beyond the scalar center; the read-list gauge article's reality and tracelessness conditions are the prerequisite, and whether they admit a compact simple algebra in $\mathbb{B}\cong M_2(\mathbb{C})$ is not settled.

2. **Which reading of the phase is physical?** The center acts as a scalar on the algebra (vector-like) but would act as $e^{i\theta}$ on $S$ and $e^{-i\theta}$ on $\bar{S}$ under the Lorentz-conjugate assignment (axial). The identification of the biquaternion field with $\Delta$ — the real-structure or "two-$i$" question — decides between them. This article does not.

3. **Is the real structure's pairing Majorana-type or a real-form Dirac mass?** The parent's mass term is the linear chiral pair, through which the continuous central phase passes, so the framework's fermion number is conserved by it. The separate antilinear pairing built on $\flat$ is carried by the parent Dirac article's open question 1 and by the neutrino article; it was the gauge article's open question 5, which now records the axial symmetry as the live item and keeps the pairing alongside it as a re-attribution. Its answer determines whether that pairing is physical and whether the vector-like reading of the center is the correct one.

The neutrino and Majorana article is the natural locus.

4. **What is the biquaternion status of the chiral projectors?** The projectors $\tfrac12(1\pm\gamma_5)$ are central idempotents of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}$, not of $\mathbb{B}$. Whether there is a natural $P_{L,R}$ inside $\mathbb{B}$ is not settled; the electron article records the same doubt.

5. **Where does the Higgs field enter?** The selection rule identifies the quantum numbers a compensating scalar must carry, but the framework's realisation of the scalar, of spontaneous symmetry breaking, and of the Yukawa coupling is the planned companion's subject.

6. **Anomalies.** A chiral gauge theory's consistency is a statement about its spectrum. Is there a biquaternion form of the anomaly cancellation conditions, and does the framework's representation theory make any of them automatic?

7. **Chirality versus the sector split.** The two decompositions share no projector; but the group acting on the module and the algebra's own structure are both built from $\mathbb{B}$. Is there a deeper relation, or are they independent structures that happen to coexist in one algebra?

8. **Empirical contact.** Does any of the chiral structure above yield a prediction distinguishing the framework from standard chiral gauge theory? As always, this is the central unresolved question.

## Summary

A chiral fermion is one whose left- and right-handed components carry inequivalent gauge representations. In the biquaternion framework the chiral decomposition lives in the spinor module: the Dirac module is $\Delta=S\oplus\bar{S}$, the chirality operator is $\gamma_5$ with $\gamma_5^2=I_4$, and the projectors

$$
P_L = \tfrac12(I_4-\gamma_5), \qquad P_R = \tfrac12(I_4+\gamma_5)
$$

are idempotent, orthogonal, complete, of rank two, and Lorentz invariant, because $\gamma_5$ anticommutes with the generators and commutes with every even element. The Dirac mass bilinear $\bar{\Psi}\Psi=\psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ is chirality-odd and vanishes on a state of definite chirality.

A chiral abelian gauge symmetry with independent charges is consistent on the module: with $Q=q_LP_L+q_RP_R$, the covariant derivative $D_\mu=\partial_\mu+\tfrac{i}{\hbar}A_\mu Q$ satisfies $D_\mu'(\Lambda\Psi)=\Lambda D_\mu\Psi$ for arbitrary $q_L,q_R$, and $[D_\mu,D_\nu]=\tfrac{i}{\hbar}F_{\mu\nu}Q$. But under the gauge transformation $\bar{\Psi}\Psi$ acquires the position-dependent phase $e^{\frac{i}{\hbar}(q_R-q_L)\Gamma}$, so it is gauge invariant **iff $q_L=q_R$**: a chiral fermion has no bare Dirac mass. This is the framework's form of the Standard Model's requirement that fermion masses arise through a compensating scalar.

The framework's *own* abelian gauge group is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$, and a central element acts as a scalar on $M_2(\mathbb{C})$, giving every component the same charge. The canonically available abelian sector is therefore **vector-like** and cannot be chiral; a chiral gauge group requires a non-central action beyond the scalar center — precisely the structure the read-list gauge article leaves open. The framework's mass term is the linear chiral pair, through which the continuous central phase passes: the vector $U(1)$ is conserved for the massive field, and what the mass breaks is the axial symmetry, $\partial_\mu j_5^\mu=2im\bar{\psi}\gamma_5\psi$ (which vanishes only at $m=0$). The algebra's anti-linear object is the real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$: a coupling built on it pairs the field with its conjugate, is not invariant under the continuous central phase, and has the signature of a conjugate-pairing (Majorana-type) term. The real structure is order-reversing and exchanges the two chiral ideals; whether its pairing is the intended physical reading is left open below.

Two gaps are left visible. First, without a non-central gauge structure the framework has no chiral gauge group, and the reality and compactness conditions that would supply one are not derived. Second, whether the real structure's antilinear pairing is Majorana-type or a real-form Dirac mass is open, and it decides whether the vector-like reading of the center is the physical one. The chiral structure itself — the halves, the projectors, the selection rule — is established and exact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Complex scalar subspace; the center of the algebra |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ |
| $S = \mathbb{C}^2 = (\tfrac12,0)$ | Left-handed Weyl spinor module (unique simple module) |
| $\bar{S} = (0,\tfrac12)$ | Right-handed Weyl spinor module (conjugate) |
| $\Delta = S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}\Delta=4$ |
| $\psi_L\in S,\ \psi_R\in\bar{S}$ | Left- and right-handed Weyl spinors |
| $\gamma_5 = \mathrm{diag}(-I_2, I_2)$ | Chirality operator, $\gamma_5^2=I_4$ |
| $P_L = \tfrac12(I_4-\gamma_5),\ P_R = \tfrac12(I_4+\gamma_5)$ | Chiral projectors |
| $\bar{\Psi}\Psi = \psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ | Dirac mass bilinear (chirality-odd) |
| $\gamma^\mu$ | Generators, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$, $g=\mathrm{diag}(+,-,-,-)$ |
| $q_L, q_R$ | Left and right charges (parameters) |
| $Q = q_LP_L+q_RP_R$ | Chiral charge operator |
| $\Lambda = \exp(\tfrac{i}{\hbar}\Gamma Q)$ | Chiral gauge transformation |
| $D_\mu = \partial_\mu+\tfrac{i}{\hbar}A_\mu Q$ | Chiral covariant derivative |
| $A_\mu' = A_\mu-\partial_\mu\Gamma$ | Transformation of the abelian connection |
| $F_{\mu\nu} = \partial_\mu A_\nu-\partial_\nu A_\mu$ | Abelian curvature |
| $[D_\mu,D_\nu]=\tfrac{i}{\hbar}F_{\mu\nu}Q$ | Chiral curvature identity |
| $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger}$ | Anti-Hermitian conjugation; the algebra's real structure ($\mathbb{C}$-antilinear, order-reversing) |
| $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ | Complexification; the two chiral summands |
| $p=\tfrac12(e_0+ie_3),\ q=\tfrac12(e_0-ie_3)$ | Primitive idempotents (Peirce, not chirality) |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, the Weyl spinors, and the chiral decomposition of the Dirac field.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Dirac spinor from two Weyl spinors, the chiral gauge interactions, and the Standard Model's need for a Higgs field to give mass to chiral fermions.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the $V-A$ structure, the mass selection rule, and the electroweak chiral assignments.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra construction of spinors as minimal left ideals and the chirality operator.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- Walter Greiner and Berndt Müller, *Gauge Theory of Weak Interactions* (Springer, 2000), for the chiral structure of the electroweak theory and the generation of fermion masses.
- Companion articles: *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; *The Dirac Equation in Biquaternionic Form*; *The Gauge Principle in Biquaternionic Form*; *Exercise: Chirality and the Weyl Spinors*; *Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation*; *The Electron in Biquaternionic Form*; *The Lorentz Group in Biquaternionic Form — Structure and Representations*; *Biquaternion Representation Theory*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
