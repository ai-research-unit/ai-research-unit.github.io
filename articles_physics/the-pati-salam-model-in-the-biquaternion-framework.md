# __The Pati–Salam Model in the Biquaternion Framework: Four Colours, $21$ Dimensions, One Coupling__

## Introduction

**The model, in the form the literature states it.** Pati and Salam proposed in $1974$ that the lepton be read as a fourth colour: that quarks and leptons sit in one multiplet of an $\mathrm{SU}(4)$ acting on four colours, with lepton number the charge that distinguishes the fourth colour from the other three. The gauge group is

$$
G_{PS}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R ,
$$

and one family is the sixteen

$$
\mathbf{16}=(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2),
$$

which contains a right-handed neutrino without one being added, cancels its own anomalies, and gives a group-theoretic reason for the charge quantisation the Standard Model only records. **The price is six new gauge bosons** — the leptoquarks — which carry colour and lepton number at once and mediate proton decay unless they are heavy. The chain to the Standard Model runs in two steps,

$$
G_{PS}\ \longrightarrow\ \mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y\ \longrightarrow\ \mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}} ,
$$

so that colour survives the first step as a stabiliser, hypercharge is assembled at it, and the photon is the mixture that survives the second.

**The question this article answers.** Why this group, and where does each of its three factors come from in the biquaternion algebra? The algebra $\mathbb B\cong M_2(\mathbb C)$ is not an $\mathrm{SU}(4)$ and contains no colour of its own. **What it does contain is a carrier of four complex dimensions and a two-sided product**, and those two structures supply two of the three factors. This article says exactly how far that reaches and where the rest is declared — because the rest is declared, and a reader who is not told so will read the frame as a derivation.

**The answer in one line.**

$$
\boxed{\;
G_{PS}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R,
\qquad
\dim_{\mathbb R}=15+3+3=21,
\qquad
\operatorname{rank}=3+1+1=5
\;}
$$

with the two-sided structure of the algebra supplying the second and third factors, and the carrier supplying the first.

**It opens the section, and it is the only article here that names a particular group.** The eighteen that follow are written for a general gauge group — the principle, the connection, the curvature, the path integral, the lattice — and every one of them reads correctly for $G_{PS}$. **This one says which group they are being read for**, and it is placed first for that reason.

**What is claimed.** That the twenty-one dimensions split as $15+3+3$ and the fifteen as $8+1+6$; that the two $\mathrm{SU}(2)$ factors arise from the algebra's own two-sided action and not from an import; that the fermion content is the sixteen of $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$; that one covariant derivative with one coupling covers all twenty-one; and that the group acts on a **formal copy** of the carrier's quartet, for the reason computed in §6.

**What is not claimed.** That the algebra derives the group. It derives two of the three factors and the split of the third. **The identification of that split with the quark–lepton quartet is a declaration, with a price**, called (A) throughout and stated in §2 and §4. Nor that the group makes the theory chiral: it does not, and §7 says why the wall stands.

## 1. The Three Factors, and What Each One Is

**1.1 The first factor is the carrier's own group.** $\mathrm{SU}(4)$ is the unitary group of the four-dimensional complex space on which $\mathbb B$ acts, fifteen real dimensions, defined by $M^{\dagger}M=\mathrm I$ and $\det M=1$. **The group is not an element of the algebra and not a corner of its endomorphisms; it is the whole group of the carrier.**

**1.2 The other two factors are the algebra's two-sided action.** Left and right multiplication by the imaginary units give two commuting $\mathfrak{su}(2)$'s inside $\mathfrak{so}(4)$:

$$
\mathfrak k_L=\{L_{\vec e_a}\},\qquad \mathfrak k_R=\{R_{\vec e_a}\},\qquad [L_{\vec e_a},R_{\vec e_b}]=0,\qquad \dim\mathfrak k_L=\dim\mathfrak k_R=3,
$$

so that $\exp\mathfrak k_L\times\exp\mathfrak k_R=\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, six dimensions. **Nothing is imported here: the two factors are the two ways the algebra multiplies.**

**1.3 The arithmetic, and it closes twice.**

$$
21=\underbrace{15}_{\mathrm{SU}(4)}+\underbrace{3}_{\mathrm{SU}(2)_L}+\underbrace{3}_{\mathrm{SU}(2)_R},
\qquad
15=\underbrace{8}_{\mathfrak{su}(3)}+\underbrace{1}_{\mathbb R\,iD}+\underbrace{6}_{\mathfrak m}.
$$

**The first equation is the frame; the second is the reason the frame can break to the Standard Model.** The $8$ will survive as colour, the $1$ will mix into hypercharge, and the $6$ will become the leptoquarks. **The ranks are $3+1+1=5$**, and the chain takes $5\to4\to3$, one rank lost at each step.

## 2. The Sixteen

**The fermions are not a choice of the group; they are the smallest anomaly-free assignment, and the algebra's split selects it.**

$$
\mathbf{16}=(\mathbf 4,\mathbf 2,\mathbf 1)\oplus(\bar{\mathbf 4},\mathbf 1,\mathbf 2),
\qquad
4\cdot2+4\cdot2=16 .
$$

**Read the two terms as the two chiralities.** The first holds the left-handed doublet of the quartet — three quark colours and one lepton, each doubled by $SU(2)_L$. The second holds the right-handed partners as singlets of $SU(2)_L$ and doublets of $SU(2)_R$. **So $\nu_R$ is not added: it is the fourth component of the $\bar{\mathbf 4}$, and it is required the moment the lepton is a colour.**

**Why the split of §1.3 is what makes this work.** $B-L$ is a generator of the $\mathrm{SU}(4)$, with eigenvalues $(1,-\tfrac13,-\tfrac13,-\tfrac13)$ on the quartet, and $\mathbf 4\to\mathbf 3\oplus\mathbf 1$ under $\mathrm{SU}(3)$. **That is exactly the quark–lepton split**, and it is (A): the algebra supplies the split $\mathbb C e_t\oplus B_V$, and the declaration says the line is the lepton.

**The check that the assignment is forced, and not merely possible.** Three conditions have to hold at once, and each one is a trace:

| condition | evaluation | result |
|---|---|---|
| $\operatorname{tr}Y$ over the sixteen | $0$ | holds |
| $\operatorname{tr}Y^{3}$ | $-\tfrac29$ from $(\mathbf4,\mathbf2,\mathbf1)$, $+\tfrac29$ from $(\bar{\mathbf4},\mathbf1,\mathbf2)$ | $0$ |
| $SU(2)_L$ doublets per family | $4$ | even, so no Witten anomaly |

**The middle row is the one worth reading.** The left-handed quartet gives $-\tfrac29$, computed as

$$
6\cdot\Bigl(\tfrac16\Bigr)^{3}+2\cdot\Bigl(-\tfrac12\Bigr)^{3}=\tfrac{1}{36}-\tfrac14=-\tfrac29 ,
$$

and its conjugate gives $+\tfrac29$ with the signs reversed. **The cancellation is between the quartet and its own conjugate**, which is the structural statement: a real or vector-like assignment would cancel trivially, and this one cancels because the sixteen is built from a complex representation and its conjugate in equal measure.

## 3. One Covariant Derivative

**The whole gauge content is one line.**

$$
D_\mu=\partial_\mu-ig_4A^a_\mu T^{(4)a}-ig_LW^i_{L\mu}\tau^i-ig_RW^i_{R\mu}\tau^i ,
\qquad a=1,\dots,15,\quad i=1,2,3 .
$$

**Twenty-one gauge fields, and at the Pati–Salam scale one coupling.** The unification condition is not $\mathrm{SU}(5)$'s: there is no group above, only the statement that the three factors have a common origin at $M_{PS}$ in the sense that

$$
g_3=g_L=g_R=g_4\qquad\text{at }M_{PS},
$$

where $g_3$ is the coupling of the $\mathrm{SU}(3)$ that survives inside the $\mathrm{SU}(4)$. **Whether that is a unification or a coincidence is a question the corpus cannot answer**; what the frame supplies is that the three couplings have one boundary value if the frame is right.

**What the twenty-one fields are, in the frame's own labels.**

| block | count | $SU(3)$ | $SU(2)_L$ | $SU(2)_R$ | fate |
|---|---|---|---|---|---|
| $A^a$, $a$ in the $\mathfrak{su}(3)$ corner | $8$ | $\mathbf 8$ | $\mathbf 1$ | $\mathbf 1$ | the gluons |
| $A^{15}$ | $1$ | $\mathbf 1$ | $\mathbf 1$ | $\mathbf 1$ | the $B-L$ boson, mixes into $\gamma$ and $Z$ |
| $A^a$, $a$ in $\mathfrak m$ | $6$ | $\mathbf 3+\bar{\mathbf3}$ | $\mathbf 1$ | $\mathbf 1$ | the leptoquarks |
| $W_L^i$ | $3$ | $\mathbf 1$ | $\mathbf 3$ | $\mathbf 1$ | $W_L^{\pm}$, one neutral |
| $W_R^i$ | $3$ | $\mathbf 1$ | $\mathbf 1$ | $\mathbf 3$ | $W_R^{\pm}$, one neutral |

**The table is most of the boson spectrum.** Its last three columns are the reason the spectrum counts $9$ massless against $12$ massive, and the two neutral entries in the last two rows join the $B$-$L$ boson in the mixing that produces the photon and the $Z$.

## 4. Where Each Factor Comes From, and How Firmly

**Three different strengths of derivation, and the difference has to be stated or the frame overclaims.**

| factor | where it comes from | status |
|---|---|---|
| $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $\exp L(\mathfrak k)\times\exp R(\mathfrak k)$ | **derived** from the two-sided action, as an algebra statement |
| $\mathrm{SU}(4)$ | the unitary group of the carrier | **derived** as a group, given the carrier |
| the split $\mathbf 4=\mathbf 1\oplus\mathbf 3$ | $\mathbb C e_t\oplus B_V$ | **derived**; canonical, and the only canonical one |
| the identification with the quark–lepton quartet | — | **declared**, (A), phase $0$ |
| the chiral assignment $(4,2,1)\oplus(\bar4,1,2)$ | — | **declared**; the algebra does not choose a chirality |
| $g_3=g_L=g_R$ at $M_{PS}$ | — | **assumed**, and tested only by the consequence $\sin^2\theta_W=\tfrac38$ |

**The fourth row is the declaration (A) and the fifth is the chiral wall.** Neither is a defect of the frame; both are recorded so that no article downstream can quietly promote them.

## 5. Why This Group and Not a Larger One

**Three competitors, and the corpus's reason for each refusal, stated in one line apiece.**

**$\mathrm{SU}(5)$.** Rank four, and its $\mathbf{10}+\bar{\mathbf5}$ has no $\nu_R$ and puts quarks and leptons in the same multiplet in a way the algebra's split does not suggest. **The corpus's $\mathfrak{su}(4)$ is the carrier's group; $\mathfrak{su}(5)$ would be a group with no carrier in the algebra at all.**

**$\mathrm{SO}(10)$.** Rank five, the same rank as $G_{PS}$, and it contains $G_{PS}$ — so it is the natural enlargement rather than a competitor. But its spinor is a $\mathbf{16}$ obtained by a Clifford algebra the corpus does not otherwise use, and **the rank-five coincidence is not an argument**: two rank-five groups contain one another for reasons of dimension, not of structure.

**$\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}$.** This is $G_{PS}$ after the $\mathrm{SU}(4)$ breaking, and it is the left–right model. **It is the honest alternative**: the difference is the six leptoquarks and the $\mathbb{CP}^{3}$ they generate, and the experiment that separates the two is a leptoquark search.

**The one-line reason the frame is $\mathrm{SU}(4)$ and not the left–right group.** The algebra's carrier is four-dimensional and its stabiliser is $\mathrm{SU}(3)$; **a three-colour group inside a four-dimensional carrier with one line removed is $\mathrm{SU}(4)$, not $\mathrm{SU}(3)\times\mathrm{U}(1)$.** Whether the fourth direction is gauged is the physics question, and the frame takes the answer that it is.

## 6. The Carrier Is a Copy, and Here Is the Theorem

**The objection.** If $\mathrm{SU}(4)$ acts on the same four dimensions as the Lorentz action, the two must commute, and then colour must be inside the commutant of the Lorentz algebra.

**The computation.** Let $L_{\vec e_a}$ be left multiplication on $\mathbb C^4$ by the three imaginary units. Then

$$
\mathfrak{su}(4)\cap\bigl\{X:[X,L_{\vec e_a}]=0\ \text{for }a=x,y,z\bigr\}
=\operatorname{span}\{R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}\}\cong\mathfrak{su}(2),
\qquad \dim_{\mathbb R}=3 .
$$

**Verified**: the right multiplications commute with the left ones; each $R_{\vec e_a}$ is anti-Hermitian and traceless; $R_1$ is Hermitian and not traceless, so $iR_1$ is the only further anti-Hermitian element of the commutant and it is excluded. **The full commutant of $L(\mathbb H)$ in $M_4(\mathbb C)$ is $R(\mathbb B)$, eight real dimensions, of which exactly three lie in $\mathfrak{su}(4)$.**

**So the ceiling is $\mathrm{SU}(2)$, and the frame must be a tensor product.**

$$
(\text{internal }\mathbf 4)\otimes(\text{spinor}),
\qquad
\mathbf 4_{\text{int}}\cong\mathbb C e_t\oplus B_V ,
$$

where the internal quartet is a **formal copy** of the algebra's coordinate space: it inherits the split, because the split is canonical, and it does not inherit the Lorentz action, because it must not. **This is the same wall the corpus already knows from the chiral side**, met here from the colour side, and it is the same wall for the same reason: $M_4(\mathbb C)$ cannot host two large commuting compact groups.

**What this article therefore asserts, in one sentence.** *The frame is $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ acting on a formal copy of the carrier's quartet tensored with a spinor, and the copy is licensed by the canonical split and by nothing else.*

## 7. The Chiral Wall, Restated for This Group

**The frame does not make the theory chiral, and no renaming will.** The algebra's product is two-sided; a chiral gauge theory needs an action that distinguishes left from right at the level of the *gauge* coupling. **In $G_{PS}$ that distinction is put in by the representation**: $\mathrm{SU}(2)_L$ acts on $(\mathbf4,\mathbf2,\mathbf1)$ and $\mathrm{SU}(2)_R$ on $(\bar{\mathbf4},\mathbf1,\mathbf2)$, and the assignment is a declaration, the fifth row of §4's table.

**What would count as the algebra supplying it.** A one-sided action of the algebra on a chiral spinor module — the corpus's open problem, unchanged. **What would be a fake solution, and is refused.** Writing the sixteen in a single multiplet of a larger group and calling the chirality derived, when the multiplet is real. **A real multiplet cannot be chiral**, and the sixteen is complex, which is why it works and why the algebra's own carrier, being self-conjugate, cannot supply it.

**The consequence for every article downstream.** The wall is quoted, not solved. [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$](quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html) says what the larger group moves and what it does not: one of three obstructions, and the one that moves is the dimension.

## 8. The Checks

**Every number in this article, run again.**

| claim | check | result |
|---|---|---|
| $\dim G_{PS}$ | $15+3+3$ | $21$ |
| the $15$ | $8+1+6$ | $15$ |
| the rank | $3+1+1$ | $5$ |
| the sixteen | $4\cdot2+4\cdot2$ | $16$ |
| the sixteen's hypercharge trace | $3\cdot\tfrac16+3\cdot\tfrac16-\tfrac12-\tfrac12+3\cdot\tfrac23+3\cdot(-\tfrac13)+0-1$ | $0$ |
| the cubic, left-handed half | $6(\tfrac16)^{3}+2(-\tfrac12)^{3}$ | $-\tfrac29$ |
| the cubic, conjugate half | $3(-\tfrac23)^{3}+3(\tfrac13)^{3}+1$ | $+\tfrac29$ |
| the cubic, total | $-\tfrac29+\tfrac29$ | $0$ |
| $SU(2)_L$ doublets per family | $4$ | even |
| the commutant ceiling | $\mathfrak{su}(4)\cap\operatorname{Comm}L(\mathbb H)$ | $\mathfrak{su}(2)$, $\dim 3$ |

## Summary

**The frame.** $G_{PS}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, $21=15+3+3$, rank $5$, one coupling at $M_{PS}$.

**The decompositions.** $15=8+1+6$; the sixteen $=(4,2,1)\oplus(\bar4,1,2)$; the eight of colour, the one that becomes $B-L$, the six leptoquarks.

**What is derived.** The two $SU(2)$'s from the two-sided action; the $\mathrm{SU}(4)$ from the carrier; the split $\mathbb C e_t\oplus B_V$, canonically.

**What is declared.** The identification of the split with the quark–lepton quartet (A); the chiral assignment; $g_3=g_L=g_R$ at the scale.

**The ceiling.** $\mathfrak{su}(4)$ commutes with the Lorentz action only in $\mathfrak{su}(2)$; so the carrier is a formal copy, licensed by the split and by nothing else.

**The wall.** The frame does not make the theory chiral; the chirality is in the representation, and the representation is declared.

## Summary of Notation

| symbol | meaning |
|---|---|
| $G_{PS}$ | $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, dimension $21$, rank $5$ |
| $T^{(4)a}$ | the fifteen $\mathrm{SU}(4)$ generators, anti-Hermitian and traceless |
| $\mathfrak m$ | the six generators mixing $\mathbb C e_t$ with $B_V$, the leptoquark directions |
| $iD$ | $i\operatorname{diag}(-3,1,1,1)$, the diagonal generator of the $\mathrm{SU}(4)$ |
| $L_{\vec e_a},R_{\vec e_a}$ | left and right multiplication by the imaginary units |
| $\mathbf{16}$ | $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$, one family |
| (A) | the declaration that the fourth colour is the unit line |

## Further Reading

- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html). The general principle this frame is an instance of.
- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html). The connection, the curvature and the Yang–Mills action for a group of this size.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The ceiling on the algebra's own compact structure, which §4 and §6 meet again.
- [The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html). The two-sided action, before it is gauged.
- [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-in-the-biquaternion-framework-the-u2-ceiling-and-the-four-unbuilt-sectors.html). What the algebra's own action carries, and what it does not.
- [Grand Unification in the Biquaternion Framework: Where the Embedding Fails](grand-unification-in-the-biquaternion-framework-where-the-embedding-fails.html). The same ceiling read as a statement about unification, in both readings.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html). What the larger group moves of the colour obstruction and what it leaves standing.

**The traps.** Do not read "the group of the carrier" as "the group acting on spacetime"; §6 forbids it and the tensor product is the whole point. Do not read the two $\mathrm{SU}(2)$'s as the Lorentz group: in the frame they are gauged and internal, and the algebra supplies the mechanism, not the identification. Do not read $g_3=g_L=g_R$ as a prediction at accessible energy; it is a boundary condition at $M_{PS}$. Do not read the sixteen as evidence that the group is right: it is evidence that the sixteen is the natural multiplet, and a natural multiplet is not a measurement.
