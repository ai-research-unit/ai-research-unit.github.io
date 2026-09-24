# __The Neutrino and Majorana Fermions in Biquaternionic Form__

## Introduction

A **Dirac fermion** is a four-component field whose left- and right-handed parts are independent; a **Weyl fermion** is a two-component field of definite chirality; a **Majorana fermion** is a field that is its own charge conjugate, $\psi^{c}=\psi$. The three are not variants of a single object but three different answers to the question of what reality structure the spinor carries. The Majorana condition is the strongest: it identifies the field with its conjugate, halves the number of independent real components, forbids a vector (fermion-number) current, and yet permits a mass term. A Weyl fermion is chiral and, so long as its chirality is protected, exactly massless. A Dirac fermion is neither self-conjugate nor, in this sense, chiral.

The immediate physical application is the neutrino. In the Standard Model the neutrino is a left-handed Weyl fermion: the weak interaction couples only to its left-handed part, and no renormalisable mass term survives. Whether the neutrino is in fact Dirac or Majorana is one of the few places where the algebra of spinors meets experiment directly, and the answer is not settled. This article asks what the biquaternion framework, in the notation of the companion articles, supplies for that distinction.

The presentation is organized around one question — *which real structure on the spinor module is the charge conjugation, and does the algebra's own material/informational split supply it?* — and the answer is split, at the outset, into three categories.

- **Established, and recomputed below.** The Dirac module $\Delta=S\oplus\bar{S}$ of the read list is self-conjugate: it carries a conjugate-linear real structure $\mathcal{C}$ with $\mathcal{C}^2=1$ that commutes with the kinetic Dirac operator and **exchanges the two chiral halves**. Its fixed space is the Majorana spinor space, of real dimension four. A Majorana–Weyl structure would have to preserve each half and does not exist in this signature. The Majorana equation $i\gamma^\mu\partial_\mu\psi=m\psi^{c}$ is consistent with the constraint $\psi^{c}=\psi$, and the mass-shell condition $p^2=m^2$ is unchanged: the mass is permitted while the vector current vanishes.
- **Established from the read list, and sharpened here.** The framework's conjugations on $\mathbb{B}$ are the quaternion conjugate $\bar{\cdot}$, the coefficient complex conjugate ${}^{*}$, the Hermitian conjugate ${}^{\dagger}=\bar{\cdot}^{\,*}$, and the anti-Hermitian conjugation $\flat=-\dagger$, the algebra's real structure. Of these, only ${}^{*}$ is a conjugate-linear **algebra automorphism**; ${}^{\dagger}$ and $\flat$ reverse the order of products. Charge conjugation, which must be a module map compatible with left multiplication, is therefore tied to ${}^{*}$ — the real structure whose fixed points are $\mathbb{H}_{\mathbb{B}}$ — and not to the order-reversing real structure $\flat$.

- **Gap, left visible.** The two-sector split $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ is a decomposition of the *algebra* by $\dagger$, not a real structure of the *module*. Its anti-Hermitian summand $\mathbb{M}_-$ is the fixed space of $\flat$ and has real dimension four, superficially matching the Majorana count; but the Dirac operator does not preserve $\mathbb{M}_-$ (left multiplication by a spatial generator carries it out of the subspace), so the sector split cannot be the Majorana reality condition. An attempted identification of Majorana with $\mathbb{M}_-$ fails on the equation, not merely on taste.

The article is organized as follows. The next section fixes the three notions and their component counts. A section then constructs charge conjugation as a real structure on $\Delta$, states the basis and signature, and separates basis-independent existence from basis-dependent form. A section treats the Majorana condition, its consistency with the massive equation, and the surviving and vanishing bilinears. A section identifies which conjugation of the biquaternion algebra plays the role of charge conjugation. A section tests the sector split against the reality condition and reports the obstruction. A section states what in the neutrino's description is empirical input rather than a consequence of the framework, and a closing section separates what the framework supplies, transcribes, and does not supply. Open questions follow.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_1e_2=e_3$, and $i$ is the scalar imaginary, $i^2=-1$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the complex scalar subspace, the center of the algebra. The conjugations are the quaternion conjugate $\bar{\cdot}$, the complex conjugate ${}^{*}$ (conjugation of the coefficients) and the Hermitian conjugate ${}^{\dagger}=\bar{\cdot}^{\,*}$; the anti-Hermitian conjugate is $\tilde{Q}^{\flat}=-\tilde{Q}^{\dagger}$. The matrix realization is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, and $\Phi(\tilde{Q}^{\dagger})=\Phi(\tilde{Q})^{\dagger}$. The spinor module is $S=\mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, carrying the left-handed Weyl representation $(\tfrac12,0)$; its complex conjugate $\bar{S}=(0,\tfrac12)$ is the right-handed Weyl module, on which $\tilde{\Lambda}\in SL(2,\mathbb{C})$ acts by $\Phi(\tilde{\Lambda}^{*})$. The Dirac module is $\Delta=S\oplus\bar{S}$, and a Dirac spinor is written in blocks as $\Psi=(\psi_L,\psi_R)^{T}$ with $\psi_L\in S$, $\psi_R\in\bar{S}$. The chirality operator is $\gamma_5=\mathrm{diag}(-I_2,I_2)$, $\gamma_5^2=I_4$, and the chiral projectors are $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$.

For the matrix form of the Clifford algebra we use the **block (chiral) basis**

$$
\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad
\gamma^k=\begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},\qquad k=1,2,3,
$$

with **signature** $g=\mathrm{diag}(+,-,-,-)$, so that $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$ and $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{diag}(-I_2,I_2)$. This is the basis and signature of the read-list chirality article; the Clifford relations, the chirality operator and the projectors are all recomputed in it below. We record that the signature and the basis must be stated together, because the explicit form of charge conjugation depends on both. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## Dirac, Weyl and Majorana: The Three Notions

The three notions are three classes of element of the spinor module, distinguished by which representation of the Lorentz group they carry and by which reality structure they respect. The chiral decomposition itself was settled in the read list and is used here without re-derivation.

**Dirac.** A Dirac spinor is an element $\Psi\in\Delta=S\oplus\bar{S}$; it has four complex components, equivalently eight real components, and its two chiral halves are independent. It is the most general spinor of the module. On it the Lorentz group acts block-diagonally by $g\oplus\Phi(\tilde{\Lambda}^{*})$ with $g=\Phi(\tilde{\Lambda})$, and the chirality operator $\gamma_5$ labels the halves.

**Weyl.** A Weyl spinor is an element of one half, $\psi_L\in S$ or $\chi\in\bar{S}$; it has two complex, four real components, and carries a definite chirality. The two halves are not isomorphic as complex representations of $SL(2,\mathbb{C})$, as the read-list spinor article stresses: they are the conjugate pair $(\tfrac12,0)$ and $(0,\tfrac12)$. A Weyl spinor is therefore chiral in the representation-theoretic sense.

**Majorana.** A Majorana spinor is an element of a **real form** of $\Delta$: a spinor equal to its own charge conjugate, $\psi^{c}=\psi$, where $\psi^{c}$ is a conjugate-linear map of $\Delta$ to itself. The fixed space of an antilinear involution on an eight-real-dimensional space is four-real-dimensional, so a Majorana spinor has four real components — the same count as a Weyl spinor, but a different object: the Weyl spinor is chiral and its conjugate is the *other* half, whereas the Majorana spinor is self-conjugate and is not chiral.

The four notions satisfy the usual inclusions. In the Lorentzian signature $(1,3)$ the Dirac module is self-conjugate while the two Weyl halves are a conjugate pair, so **Majorana spinors exist and Majorana–Weyl spinors do not**. The reason is structural and is worth stating at once, because it is the point on which the biquaternion framework has something to say: the real structure that makes a spinor Majorana exchanges the two chiral halves, and a Majorana–Weyl spinor would require a real structure preserving them. The complex algebra $\mathbb{B}$, being simple, sees one simple module and cannot distinguish the halves at all; the exchange is a real-structure operation, and it is the same operation that pairs $S$ with $\bar{S}$ in the Dirac module. The classification of which signatures admit which type is governed by the signature modulo eight, and the corpus already records it; in $(1,3)$ the outcome is the one just stated.

| Notion | Carrier | $\dim_{\mathbb{R}}$ | Chiral? | Self-conjugate? |
|---|---|---|---|---|
| Dirac | $\Delta=S\oplus\bar{S}$ | $8$ | no (both halves) | no |
| Weyl | $S$ or $\bar{S}$ | $4$ | yes | no |
| Majorana | real form of $\Delta$ | $4$ | no (halves conjugate) | yes |
| Majorana–Weyl | real form of $S$ | — | yes | yes (does not exist in $(1,3)$) |

Two cautions belong here, both inherited from the read list and both relevant below. First, the chiral halves are **not** the two minimal left ideals $\mathbb{B}p$, $\mathbb{B}q$: those are both isomorphic to $S$ and carry the same defining representation, so the chirality distinction is invisible to $\mathbb{B}$ alone. Second, a biquaternion $\tilde{\Psi}\in\mathbb{B}$ is not a spinor; the spinor is an element of the module $S$, or of $\Delta$, and the algebra acts on it. The identification of an algebra element with a spinor is a separate step, and it is exactly where the reality conditions become delicate.

## Charge Conjugation as a Real Structure on the Spinor Module

Charge conjugation is a **conjugate-linear** map on the Dirac module. In four dimensions it is written with a charge-conjugation matrix $C$ acting on the Dirac conjugate,

$$
\psi^{c} \;=\; C\,\bar{\psi}^{\,T},
\qquad
\bar{\psi} \;=\; \psi^{\dagger}\gamma^0 ,
$$

and the matrix is fixed by the requirement that the kinetic term be preserved,

$$
C\,\gamma^{\mu\,T}\,C^{-1} \;=\; -\,\gamma^{\mu}.
$$

The transpose, not the inverse or the conjugate, appears because $C$ is the matrix of a bilinear pairing on the module. Two features of this definition must be stated before it is used, and they are the two traps of the subject.

**The matrix is basis-dependent, and the reality condition is basis-dependent in form.** A change of Clifford basis $\gamma^\mu\mapsto S\gamma^\mu S^{-1}$ sends $C\mapsto SCS^{T}$, so the explicit matrix changes with the basis even though the map it defines does not. In the block basis of the Conventions, with $g=\mathrm{diag}(+,-,-,-)$, the choice

$$
C \;=\; i\gamma^2\gamma^0 \;=\; \begin{pmatrix}\epsilon&0\\ 0&-\epsilon\end{pmatrix},
\qquad
\epsilon \;=\; i\sigma_2 \;=\; \begin{pmatrix}0&1\\ -1&0\end{pmatrix},
$$

is antisymmetric, $C^{T}=-C$, with $C^2=-I_4$ and $C^{\dagger}=C^{-1}$, and it satisfies $C\gamma^{\mu T}C^{-1}=-\gamma^\mu$ for $\mu=0,1,2,3$. The same map written in the Dirac basis $\gamma'^0=\mathrm{diag}(I_2,-I_2)$ has the charge-conjugation matrix $S C S^{T}$, which is a different matrix. The existence of a charge-conjugation matrix is a statement about the signature, not about the basis; its form is a statement about the basis. A calculation that fixes a sign by comparing "$C$" across two papers that use different Clifford bases is comparing two different matrices.

**The map is antilinear, and it is the antilinear map — not $C$ — that is the real structure.** Writing $\bar{\psi}^{\,T}=\gamma^{0T}\psi^{*}$ gives

$$
\psi^{c} \;=\; K\,\psi^{*},
\qquad
K \;=\; C\,\gamma^{0T} \;=\; \begin{pmatrix}0&\epsilon\\ -\epsilon&0\end{pmatrix},
\qquad
K K^{*} \;=\; I_4 .
$$

The relation $KK^{*}=I_4$ is the statement that $\mathcal{C}:\psi\mapsto\psi^{c}$ is an **involution**, $\mathcal{C}^2=1$; it is the real structure, and it is conjugate-linear by construction, $\mathcal{C}(\lambda\psi)=\lambda^{*}\mathcal{C}(\psi)$. The matrix $C$ itself has $C^2=-I_4$ and is not the real structure. The distinction matters below: the fixed points of $\mathcal{C}$ are the Majorana spinors, and no fixed points of $C$ are involved.

The consistency of this real structure with the Dirac operator is a second, independent condition. It is

$$
K\,\gamma^{\mu\,*}\,K^{-1} \;=\; -\,\gamma^{\mu},
$$

which holds for $\mu=0,1,2,3$ in the block basis. Because $\mathcal{C}$ is conjugate-linear, this is what makes $\mathcal{C}$ commute with the kinetic operator: for a constant matrix $M$, $\mathcal{C}(M\psi)=K M^{*}\psi^{*}$, so $\mathcal{C}(i\gamma^\mu\partial_\mu\psi)=i\gamma^\mu\partial_\mu(\mathcal{C}\psi)$ if and only if $K(i\gamma^\mu)^{*}K^{-1}=i\gamma^\mu$, which is exactly the displayed condition. In words: **charge conjugation commutes with the massless Dirac operator and anticommutes with the Clifford generators**. This is the property that makes the Majorana constraint consistent with the wave equation, and it is verified independently of any statement about a mass.

**Block form, and the exchange of the chiral halves.** In blocks $K$ is off-diagonal,

$$
K \;=\; \begin{pmatrix}0&\epsilon\\ -\epsilon&0\end{pmatrix},
\qquad\text{so}\qquad
\psi^{c} \;=\; \begin{pmatrix}\epsilon\,\psi_R^{*}\\ -\epsilon\,\psi_L^{*}\end{pmatrix}.
$$

Charge conjugation maps the left-handed half to the right-handed half and back. In particular it does not preserve the chirality projectors: in blocks $P_L\psi^{c}=(\epsilon\,\psi_R^{*},0)^{T}$ and $P_R\psi^{c}=(0,-\epsilon\,\psi_L^{*})^{T}$. The Majorana condition $\psi^{c}=\psi$ is therefore

$$
\psi_R \;=\; -\,\epsilon\,\psi_L^{*},
\qquad
\psi_L \;=\; \epsilon\,\psi_R^{*},
$$

a single pair of equations relating the two halves, not two independent real conditions. The fixed space is parametrised by $\psi_L$ alone: given any $\psi_L\in S$, the equations determine $\psi_R$, and the constraint is solved by four real parameters (two complex, conjugate-related). The fixed space is four-real-dimensional, as required for Majorana, and it is **not** the graph of a complex-linear identification of $S$ with $\bar{S}$ — such an identification would make the spinor Weyl and Majorana simultaneously, which does not exist here. This is the module-level content of the statement that the real structure exchanges the halves.

We collect the verified statements of this section in a table. Each entry was checked by exact computation in the block basis with $g=\mathrm{diag}(+,-,-,-)$; every Clifford and charge-conjugation identity was checked on all four $\mu$, not only on $\mu=0$.

| Statement | Verification |
|---|---|
| $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$, $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{diag}(-I_2,I_2)$ | all $16$ commutators and anticommutators, exact |
| $C^{T}=-C$, $C^2=-I_4$, $C^\dagger=C^{-1}$ | exact, $C=i\gamma^2\gamma^0$ |
| $C\gamma^{\mu T}C^{-1}=-\gamma^\mu$ | all $\mu=0,1,2,3$ |
| $K=C\gamma^{0T}=\begin{pmatrix}0&\epsilon\\ -\epsilon&0\end{pmatrix}$, $KK^{*}=I_4$ | exact |
| $K\gamma^{\mu*}K^{-1}=-\gamma^\mu$ | all $\mu=0,1,2,3$ |
| $\psi^{c}=K\psi^{*}$, $(\psi^{c})^{c}=\psi$ | all components |
| $\mathcal{C}$ exchanges $S$ and $\bar{S}$ | block structure of $K$ |
| $\dim_{\mathbb{R}}\{\psi:\psi^{c}=\psi\}=4$ | $\psi_L$ free, $\psi_R=-\epsilon\psi_L^{*}$ |

**A basis-independent caution.** The statement that a charge-conjugation matrix exists in a given signature is basis-independent, and it is not true in every dimension; it is governed by the signature modulo eight, as the corpus's spinor articles record. What is basis-independent is the existence of the real structure; what is basis-dependent is the matrix $K$ and the explicit form of the condition $\psi_R=-\epsilon\psi_L^{*}$. A reader who carries only the condition and forgets the basis will get signs wrong. A reader who carries only the basis and forgets that the map is antilinear will conclude, incorrectly, that the two halves are identified complex-linearly.

## The Majorana Condition and the Mass Term

The Majorana condition is the fixed-point equation $\psi^{c}=\psi$ of the real structure of the previous section,

$$
\psi_R \;=\; -\,\epsilon\,\psi_L^{*},
$$

and it determines $\psi_R$ from $\psi_L$. It is not an extra equation imposed on the field after the fact; it is a restriction of the spinor module to a real form, and the question that has to be answered is whether the restricted fields solve a sensible massive equation.

**The massive equation.** For a single self-conjugate field the mass term cannot be the Dirac term $m\bar{\psi}\psi$ of a Dirac field, because the two chiral halves are conjugate, not independent. The equation that carries a mass is the **Majorana equation**

$$
i\gamma^\mu\partial_\mu \psi \;=\; m\,\psi^{c}.
$$

If its solution also satisfies $\psi^{c}=\psi$, then it satisfies the ordinary massive Dirac equation $(i\gamma^\mu\partial_\mu-m)\psi=0$; conversely the massive Dirac equation restricted to the fixed space implies the Majorana equation. The content is therefore in the consistency of the constraint with the equation, and that consistency is a computation, not a convention.

**Consistency is verified, not assumed.** Apply the real structure $\mathcal{C}$ to the Majorana equation. Since $\mathcal{C}$ is conjugate-linear and commutes with $i\gamma^\mu\partial_\mu$ (the previous section, verified on all $\mu$), and since $\mathcal{C}^{2}=1$,

$$
\mathcal{C}\!\left(i\gamma^\mu\partial_\mu\psi\right)=i\gamma^\mu\partial_\mu\psi^{c},
\qquad
\mathcal{C}\!\left(m\psi^{c}\right)=m\,\psi .
$$

Applying $\mathcal{C}$ to the equation therefore returns $i\gamma^\mu\partial_\mu\psi^{c}=m\psi$, which is the same equation with $\psi$ and $\psi^{c}$ interchanged. Subtracting the two equations,

$$
i\gamma^\mu\partial_\mu\left(\psi-\psi^{c}\right) \;=\; -\,m\left(\psi-\psi^{c}\right),
$$

so the deviation $\chi=\psi-\psi^{c}$ satisfies the same form of equation as the field itself, and the subspace $\chi=0$ is preserved by the evolution. A field that is self-conjugate at one time stays self-conjugate; the constraint is consistent with the massive equation, not merely imposed on it. This is the point requested of every displayed identity: the consistency is checked by applying the real structure and using the anticommutation of $\mathcal{C}$ with the generators, and it does not hold for a generic conjugate-linear map — it uses the verified identity $K\gamma^{\mu*}K^{-1}=-\gamma^\mu$.

**A massive solution exists.** Nothing in the consistency argument forces $m=0$. The mode functions make that explicit. With $p^\mu=(E,\mathbf{p})$, $E=\sqrt{\mathbf{p}^2+m^2}$ and $\not{p}=\gamma^0E-\boldsymbol{\gamma}\cdot\mathbf{p}$, a positive-frequency Dirac spinor $u(p)$ solves $(\not{p}-m)u=0$, and its charge conjugate $v(p)=u^{c}(p)$ solves $(\not{p}+m)v=0$. The two are both nonzero for $m>0$, and $\bar{u}u$ is nonzero for $m>0$ (the normalisation is the one of the companion quantisation article). The mass-shell condition is $p^2=m^2$, unchanged from the Dirac case. So the Majorana restriction does not trivialise the spectrum: a massive plane wave exists for every $m>0$. What the restriction removes is not the mass but half the degrees of freedom.

**Which bilinears survive, and which vanish.** The physical statements are about the field, whose components anticommute. Writing the four components of the field as Grassmann variables and using $\psi=(\psi_L,-\epsilon\psi_L^{*})^{T}$ together with the Majorana condition, one finds the following, each computed exactly in the block basis.

| Bilinear | Grassmann Majorana field | Status |
|---|---|---|
| $\bar{\psi}\psi$ | nonzero | scalar mass term **permitted** |
| $\bar{\psi}\gamma^\mu\psi$ | $0$ for all $\mu$ | vector current **forbidden** |
| $\bar{\psi}\gamma^\mu\gamma_5\psi$ | nonzero | axial current permitted |
| $\psi^{T}C\psi$ | nonzero | the Majorana mass invariant |

The vanishing of the vector current is the statement that a self-conjugate field carries no fermion number; the surviving scalar and axial bilinears are what a Majorana field can couple to. Both properties follow from the same anticommutation: for the vector current the charge-conjugation flip of the bilinear and the self-conjugacy of the field combine to give $j^\mu=-j^\mu$; for the scalar the two contributions add rather than cancel.

**A caution that must be recorded.** The last paragraph is a statement about the Grassmann-valued field, and it is not true of a commuting c-number spinor that happens to satisfy the same algebraic condition. If the components are treated as ordinary complex numbers, the antisymmetric contractions that produced the mass term instead cancel, and the same computation gives the **opposite** pattern: $\bar{\psi}\psi=0$, the vector current *nonzero*, and the axial current zero. Every bilinear statement for a Majorana field is therefore a Grassmann statement; a purely classical c-number computation will not reproduce it, and the sign by which the physical statement differs is the anticommutativity of the components. This is recorded here rather than hidden, because the module-level construction above is classical and a reader may reasonably attempt the bilinears at that level. The module construction fixes the constraint and its consistency; the bilinear physics requires the Grassmann structure, which the framework supplies through the anticommuting mode operators of the companion quantisation article rather than through $\mathbb{B}$ itself.

**Contrast with the Weyl field.** A Weyl field of definite chirality has $\bar{\psi}\psi=0$ because the bilinear is chirality-odd (the read-list result), so it admits no Dirac mass. The only mass term a single chiral field can carry is a Majorana mass, which pairs $\psi_L$ with $\psi_L^{c}\in\bar{S}$; that term is allowed only when the field is not protected by a conserved charge. Where the chirality is protected by a complex gauge representation — the Standard-Model neutrino — the term is forbidden and the field is exactly massless; where the field is a gauge singlet, the term is allowed and the field, once massive, is Majorana and no longer Weyl. A Dirac fermion is the remaining case: it has independent halves, a Dirac mass, and neither the Weyl chirality nor the Majorana self-conjugacy.

## Which Conjugation of the Biquaternion Algebra Is the Charge Conjugation?

The module-level real structure $\mathcal{C}$ is abstract. The framework supplies concrete conjugations on $\mathbb{B}$, and the question is which of them realises $\mathcal{C}$. There are four operations in play, and they divide into two kinds.

| Operation | Action on coefficients | Type |
|---|---|---|
| $\bar{\cdot}$ quaternion | $e_0\mapsto e_0$, $e_k\mapsto -e_k$, $i\mapsto i$ | $\mathbb{C}$-linear antiautomorphism |
| ${}^{*}$ complex | coefficients conjugated, basis fixed | conjugate-linear **automorphism** |
| ${}^{\dagger}=\bar{\cdot}\circ{}^{*}$ Hermitian | coefficients conjugated, $e_k\mapsto -e_k$ | conjugate-linear antiautomorphism |
| $\flat=-\dagger$ | minus the Hermitian conjugate | conjugate-linear, order-reversing |

The distinction that decides the question is **automorphism versus antiautomorphism**. A real structure on a module has to commute with the module action; on the regular module $\mathbb{B}$, where the algebra acts by left multiplication, commuting with the action means respecting the order of products. Only ${}^{*}$ does:

$$
(Q R)^{*} = Q^{*}R^{*},
\qquad\text{whereas}\qquad
(Q R)^{\dagger}=R^{\dagger}Q^{\dagger},
\qquad
(Q R)^{\flat}=-R^{\flat}Q^{\flat}.
$$

Both relations were checked on random biquaternions in the matrix realisation. So of the framework's conjugations, ${}^{*}$ is the one that can serve as a charge-conjugation real structure on a module; $\dagger$ and $\flat$, being order-reversing, cannot. The fixed points of ${}^{*}$ are the real quaternions, $\mathbb{H}_{\mathbb{B}}=\{Q:Q^{*}=Q\}$; in this sense the real form that underlies charge conjugation is the real-quaternion real form, and the conjugate Weyl representation is produced by the coefficient conjugation, $\tilde{\Lambda}\mapsto\tilde{\Lambda}^{*}$, exactly as the read-list spinor article states for the action on $\bar{S}$. This is the identification the framework supplies, and it is clean: **charge conjugation is the fixed-point real structure of the coefficient complex conjugation, transported to the Dirac module by the identification of $S$ with $\bar{S}$.**

The map $\flat$ is a *different* conjugation, and the difference is exactly the order reversal. The parent articles retain $\flat$, $\tilde{\Psi}\mapsto\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$, as the algebra's real structure; it is antilinear and involutive, so it is a real structure on the algebra as a real vector space. But it is order-reversing, and its fixed space is the material sector $\mathbb{M}_-$, not a spinor real form. It is the map that pairs a field with its conjugate in a Majorana-type coupling; it is not the charge-conjugation map that identifies a field with its antiparticle, and it is not the parent's mass term, which is the linear chiral pair. Mixing the two is the natural error, and it is the one tested in the next section.

Finally, the passage from the algebra to the module is itself a real-structure step. The regular module is $\mathbb{B}\cong S\oplus S$ — two copies of the *same* defining representation — whereas the Dirac module is $\Delta=S\oplus\bar{S}$. Identifying an algebra element $\tilde{\Psi}\in\mathbb{B}$ with a Dirac spinor requires passing from $S\oplus S$ to $S\oplus\bar{S}$, and that passage uses precisely the coefficient conjugation. So the framework does contain the operation, but the operation is ${}^{*}$ together with the module identification, not the decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$.

## Does the Material/Informational Split Help or Obstruct?

The split $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ into anti-Hermitian and Hermitian parts is the algebra's own decomposition by $\dagger$. It is real,

$$
\mathbb{M}_-=\{Q:Q^{\dagger}=-Q\},
\qquad
\mathbb{M}_+=\{Q:Q^{\dagger}=Q\},
\qquad
\dim_{\mathbb{R}}\mathbb{M}_-=\dim_{\mathbb{R}}\mathbb{M}_+=4,
$$

and it has one property that makes it a genuine temptation for a Majorana construction: the flat map $\flat=-\dagger$ is an antilinear involution whose fixed space is exactly $\mathbb{M}_-$,

$$
Q^{\flat}=Q \iff Q^{\dagger}=-Q \iff Q\in\mathbb{M}_- .
$$

Both implications were checked on basis elements and on general elements. The dimension of $\mathbb{M}_-$ is four, the same as the Majorana count, and $\flat$ is the algebra's real structure, the map on which the framework's Majorana-type coupling is built. It is therefore natural to try the identification

$$
\text{``Majorana''} \;=\; \{\tilde{\Psi}\in\mathbb{B} : \tilde{\Psi}^{\flat}=\tilde{\Psi}\} \;=\; \mathbb{M}_- .
$$

The identification fails on the equation, and the failure is elementary. The biquaternionic Dirac operator is a sum of left multiplications,

$$
\nabla \;=\; e_0\,\partial_{ict} \;+\; \sum_{k=1}^{3} e_k\,\partial_k ,
$$

and left multiplication by the spatial generators $e_1,e_2,e_3$ does not preserve $\mathbb{M}_-$. The sharpest single instance is

$$
e_1\in\mathbb{M}_-,
\qquad
e_1\,e_1=-e_0\in\mathbb{M}_+ .
$$

So the spatial part of the Dirac operator does not preserve $\mathbb{M}_-$; more generally, for a generic $\tilde{\Psi}\in\mathbb{M}_-$ the products $e_k\tilde{\Psi}$ lie in neither sector. The time term fails for the same reason: $\partial_{ict}$ contributes a factor $-i$, and $i\,\tilde{\Psi}\in\mathbb{M}_+$ whenever $\tilde{\Psi}\in\mathbb{M}_-$. Hence $\nabla\tilde{\Psi}\notin\mathbb{M}_-$ for generic $\tilde{\Psi}\in\mathbb{M}_-$: **the Dirac operator does not preserve the material sector, so the sector cannot be a Majorana real form.** A Majorana reduction requires a subspace that the equation carries into itself, and $\mathbb{M}_-$ is not one.

The reason is structural rather than accidental. $\mathbb{M}_-$ is a real form of the *algebra* under the order-reversing map $\flat$, and as a vector space it is the four-dimensional material sector of the companion articles — the space of four-vectors and of the material field, on which the Lorentz group acts by $\tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^{\dagger}$. A Majorana spinor is a real form of the *spinor module*, on which the Lorentz group acts by one-sided multiplication. The two live in different representations and have different dimensions available to them (four real components each, but transforming differently). The sector split therefore does not help: it supplies a real form of the wrong object. If it is used as the reality condition it actively obstructs, because it makes the mass equation fail to close and would identify a spin-$\tfrac12$ field with a four-vector.

This is the same warning the parent chirality article issues in another guise. There, the chiral projectors $P_{L},P_{R}$ of the spinor module were distinguished from the sector projectors of the algebra: the two decompositions share no projector and the sector split does not see chirality. Here the sharpened statement is that the sector split does not see the Majorana reality condition either. The charge conjugation of the framework is the coefficient conjugation ${}^{*}$ of the previous section, acting on the module; the material/informational split is the algebra's decomposition by $\dagger$, and it is not a spinor real structure at all.

## The Neutrino: What the Framework Does and Does Not Derive

The reason the neutrino appears in this article at all is that it is the fermion for which the Dirac/Majorana distinction is an open experimental question. The framework has something to say about the *structures* that the question involves, and it must be stated plainly what it does **not** derive.

**The chiral coupling is empirical input.** The weak interaction couples to left-handed fermion fields and not to right-handed ones. This is a fact about the world, established by the observation of parity violation in weak decays and by the helicity of the neutrino; it is not a consequence of the biquaternion algebra. The parent gauge article makes the corresponding structural statement: the gauge group canonically attached to the algebra is the *vector-like* central phase $U(1)\subset\mathbb{C}_{\mathbb{B}}$, and a larger or chiral gauge structure requires an action that does not commute with the algebra, that is, a choice of representation. The framework therefore does not derive the Standard Model's chiral $SU(2)_L$ structure; it transcribes a chiral gauge theory onto the module, with the chiral assignment put in by hand, exactly as the read-list chirality article states for its abelian model. The left-handedness of the neutrino is, in this framework, an input.

**Which real structure a fermion uses is not selected by the algebra.** The algebra contains both structures. An unconstrained Dirac field $\Psi\in\Delta$ is what it is; imposing the fixed-point condition $\psi^{c}=\psi$ gives a Majorana field; and no internal principle of the biquaternion framework chooses one for the neutrino. A gauge-invariant Majorana mass requires the field to be a gauge singlet (or to lie in a real representation), while a Dirac mass requires a right-handed partner and a Higgs-type coupling; both are outside the algebra, and the choice between them is made by the measured spectrum, not by the framework.

**A Majorana pairing is genuinely antilinear, and it belongs to the real structure, not to the parent's mass term.** A genuine Majorana mass pairs the field with its conjugate, $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ with $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$, and because $\flat$ is $\mathbb{C}$-antilinear such a coupling is not invariant under the continuous central phase: a mass term that pairs the field with its conjugate breaks fermion number, which is the hall-mark of a Majorana-type coupling. That is a genuine structural resemblance, and it is the reason the framework is *compatible* with a Majorana neutrino. The parent's own massive equation is by contrast the linear chiral pair of the Dirac article, whose mass term is linear and through which the central $U(1)$ (fermion number) passes; only the axial symmetry is broken by it. The antilinear pairing belongs to the real structure $\flat$ and to the single-field equation built on it, which is a different equation, with central-phase plane waves on the spacelike locus. It is not a derivation. The equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$ does not impose $\tilde{\Psi}^{\flat}=\tilde{\Psi}$; whether its $\flat$-pairing should be read as charge conjugation or as a real-form presentation of a Dirac mass is an open question of the corpus, not a settled result. This article does not resolve it, and the distinction between the real structure $\flat$ and the charge-conjugation real structure $\mathcal{C}$ drawn in the previous two sections is precisely the reason the question is delicate.

**What is outside the framework entirely.** The value of the neutrino mass, the see-saw mechanism, lepton mixing, and the Majorana phases of the mixing matrix are not represented. The framework offers no prediction for any of them, and in particular no prediction for the rate of neutrinoless double beta decay, the process that would establish the Majorana nature experimentally. No expectation of that kind is claimed here.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| A charge-conjugation real structure on $\Delta$, with $\mathcal{C}^2=1$ and the constraint $\psi^{c}=\psi$ | **Supplied**, by the coefficient conjugation ${}^{*}$ transported to the module; verified |
| The Majorana component count $\dim_{\mathbb{R}}=4$ and the exchange of the chiral halves | **Supplied** |
| Existence of Majorana and non-existence of Majorana–Weyl in $(1,3)$ | **Transcribed** from the corpus's spinor article *Spinors* (§8); *Spinors categorization* takes the real structure to commute with the full Clifford action, under which $(1,3)$ is symplectic Majorana |
| The explicit charge-conjugation matrix $C$, its basis dependence, and the block form of the constraint | **Transcribed**; basis and signature stated |
| Consistency of the constraint with the massive equation | **Supplied** (through the verified $K\gamma^{\mu*}K^{-1}=-\gamma^{\mu}$) |
| The bilinear physics: no vector current, mass and axial current permitted | **Supplied at the level of the anticommuting field**; not visible in a commuting c-number spinor |
| A chiral gauge group, and the left-handedness of the neutrino | **Not supplied**; empirical input, transcribed |
| The material/informational split as the Majorana reality condition | **Not supplied**; it obstructs, as shown above |
| Whether the neutrino is Dirac or Majorana | **Not decided** by the framework |
| The neutrino mass value, the see-saw, mixing, and the Majorana phases | **Outside** |

## Open Questions

1. **The algebra-level form of the reality condition.** This article identifies the operation — the coefficient conjugation ${}^{*}$ — but works with the explicit matrix $K$ on the module. What is the biquaternion-valued rule that corresponds to $\psi\mapsto K\psi^{*}$ in the algebra, and how does it relate to the algebra's real structure $\flat$? The module real structure is the one that carries the Majorana condition; the parent's mass term is the linear chiral pair and is not at issue here.

2. **The status of the $\flat$-pairing.** Is the single-field equation $\tilde{\nabla}\tilde{\Psi}=m\tilde{\Psi}^{\flat}$, built on the algebra's real structure, a Majorana mass or an ordinary Dirac mass written on a real form? That equation is separate from the parent's linear chiral-pair mass term, whose fermion number is conserved. The present article sharpens the question: the real structure $\flat$ is an order-reversing conjugation whose fixed space is $\mathbb{M}_-$, so if it is a charge conjugation it is a different one from the module real structure constructed here.

3. **The sector split, in any other guise.** The obstruction above rules out the naive identification of Majorana with $\mathbb{M}_-$. Whether some other use of the split — a different module, a different pairing, or a combination of $\flat$ with the module identification — can carry a reality condition is not settled.

4. **Dimension-five operators.** Neutrino masses in the Standard Model are generated by a dimension-five operator after electroweak symmetry breaking. Whether the biquaternion framework can represent such an operator, and whether it has anything to say about the see-saw, is not attempted.

5. **CP and the Majorana phases.** The Majorana nature of a fermion is entangled with the reality properties of its mass matrix and with CP violation. A treatment belongs with the corpus's CP and CPT material; the CPT article is not yet written, and nothing is claimed here.

6. **Empirical contact.** The decisive experiment is neutrinoless double beta decay. The framework offers no rate and no prediction; the question of whether it can be brought into contact with one is open.

## Summary

A Dirac fermion is an arbitrary element of $\Delta=S\oplus\bar{S}$, with independent chiral halves and eight real components. A Weyl fermion is an element of one half, chiral and — while its chirality is protected — massless. A Majorana fermion is a fixed point of a conjugate-linear real structure $\mathcal{C}$ on $\Delta$ with $\mathcal{C}^2=1$, with four real components, no vector current, and a permitted mass. In the Lorentzian signature $(1,3)$ Majorana spinors exist and Majorana–Weyl spinors do not, because the real structure that makes a spinor Majorana exchanges the two chiral halves instead of preserving them.

The charge conjugation of the Dirac module was constructed explicitly in the block (chiral) basis with $g=\mathrm{diag}(+,-,-,-)$: the matrix $C=i\gamma^2\gamma^0$ satisfies $C\gamma^{\mu T}C^{-1}=-\gamma^\mu$ and defines an antilinear involution $\psi^{c}=K\psi^{*}$, $K=C\gamma^{0T}$, with $KK^{*}=I_4$ and $K\gamma^{\mu*}K^{-1}=-\gamma^\mu$. The last identity is what makes the Majorana constraint $\psi^{c}=\psi$ consistent with the massive equation $i\gamma^\mu\partial_\mu\psi=m\psi^{c}$, rather than merely imposed on it: the constraint is propagated, and a massive plane wave exists for every $m>0$. The vector current vanishes for a self-conjugate Grassmann field and the scalar and axial bilinears survive; those statements are properties of the anticommuting field, and a commuting c-number computation gives the opposite pattern.

In the biquaternion framework the charge conjugation is the real structure carried by the **coefficient complex conjugation** ${}^{*}$, the only one of the algebra's conjugations that is a conjugate-linear automorphism, with fixed points $\mathbb{H}_{\mathbb{B}}$; the Hermitian conjugate and the real structure $\flat$ are order-reversing and cannot serve as module real structures. The material/informational split is the algebra's decomposition by $\dagger$, and although $\mathbb{M}_-$ is the four-real-dimensional fixed space of the real structure $\flat$ and superficially matches the Majorana count, the Dirac operator does not preserve it ($e_1\in\mathbb{M}_-$ but $e_1e_1=-e_0\in\mathbb{M}_+$). The sector split therefore obstructs the reality condition and cannot be used as it stands; the Majorana real form lives on the spinor module, not on a subspace of the algebra. Finally, the left-handedness of the neutrino under the weak interaction is empirical input, the real structure $\flat$ carries a genuinely antilinear Majorana-type pairing that is compatible with but does not derive a Majorana neutrino, while the parent's own mass term is linear and conserves fermion number; the mass value and its consequences are outside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}} = \{Q:Q^{*}=Q\}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Complex scalar subspace; the center |
| $\bar{\cdot},\ {}^{*},\ {}^{\dagger}=\bar{\cdot}^{\,*}$ | Quaternion, complex and Hermitian conjugations |
| $\tilde{Q}^{\flat}=-\tilde{Q}^{\dagger}$ | Algebra's real structure; $\mathbb{C}$-antilinear involution, order-reversing; fixed space $\mathbb{M}_-$ |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ |
| $S = \mathbb{C}^2 = (\tfrac12,0)$ | Left-handed Weyl spinor module |
| $\bar{S} = (0,\tfrac12)$ | Right-handed Weyl spinor module (conjugate) |
| $\Delta = S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}\Delta=4$ |
| $\psi_L\in S,\ \psi_R\in\bar{S}$ | Left- and right-handed Weyl spinors |
| $\gamma_5 = \mathrm{diag}(-I_2,I_2)$ | Chirality operator |
| $g=\mathrm{diag}(+,-,-,-)$ | Clifford signature |
| $\epsilon = i\sigma_2$ | Invariant antisymmetric $2\times2$ tensor |
| $C = i\gamma^2\gamma^0$ | Charge-conjugation matrix, $C^{T}=-C$, $C^2=-I_4$ |
| $K = C\gamma^{0T} = \begin{pmatrix}0&\epsilon\\ -\epsilon&0\end{pmatrix}$ | The real structure on spinors; $KK^{*}=I_4$ |
| $\mathcal{C}:\psi\mapsto K\psi^{*}$ | Charge conjugation as an antilinear involution |
| $\psi^{c} = \mathcal{C}\psi$ | Charge conjugate; $\psi^{c}=\psi$ defines Majorana |
| $\psi_R=-\epsilon\psi_L^{*}$ | Majorana condition in the block basis |
| $i\gamma^\mu\partial_\mu\psi=m\psi^{c}$ | Majorana equation |
| $\bar{\psi}\gamma^\mu\psi$, $\bar{\psi}\psi$, $\bar{\psi}\gamma^\mu\gamma_5\psi$ | Vector, scalar and axial bilinears |
| $S C S^{T}$ | Charge-conjugation matrix in a basis $S\gamma^\mu S^{-1}$ |
| $\dim_{\mathbb{R}}\{\psi:\psi^{c}=\psi\}=4$ | Majorana component count |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- Ettore Majorana, "Teoria simmetrica dell'elettrone e del positrone", *Nuovo Cimento* **14** (1937) 171–184, the original symmetric theory of the electron and positron, where the self-conjugate spinor is introduced.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of Dirac, Weyl and Majorana fields, the charge-conjugation matrix, and the relation between the reality of the mass term and fermion-number conservation.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Dirac bilinears, charge conjugation in the chiral basis, and the Majorana mass term.
- Rabindra N. Mohapatra and Palash B. Pal, *Massive Neutrinos in Physics and Astrophysics* (World Scientific, 2004), for the Dirac/Majorana distinction, the see-saw mechanism, and neutrinoless double beta decay.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification of real structures on spinor modules by signature.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the relation between spinors, the charge-conjugation operation, and the Lorentz group in a real Clifford algebra.
- Companion articles: *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; *The Dirac Equation in Biquaternionic Form*; *Chiral Fermions in the Biquaternion Framework*; *Exercise: Chirality and the Weyl Spinors*; *The Electron in Biquaternionic Form*; *Canonical Quantization of the Biquaternion Dirac Field*; *The Gauge Principle in Biquaternionic Form*; *The Spin–Statistics Theorem in Biquaternionic Form*; *Spinors*; *Spinors categorization*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *Introduction to the Biquaternion Universe*.
