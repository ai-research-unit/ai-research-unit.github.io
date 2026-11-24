# __The Fermions After the Breaking: Three Colours and a Lepton Line, Two Weak Doublets, the Electric Charges__

## Introduction

**The question.** One generation is sixteen states. After the chain has run, what are they — how many colours, how many doublets, which charges — and which of those numbers is read off the breaking and which is put in by hand?

**The answer.**

$$
\boxed{\;
(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)
\ \longrightarrow\
\underbrace{(Q_L)}_{\mathbf3,\ \text{six states}}
\oplus\underbrace{(u_R,d_R)}_{\bar{\mathbf3},\ \text{six states}}
\oplus\underbrace{(L_L)}_{\mathbf1,\ \text{two states}}
\oplus\underbrace{(\nu_R,e_R)}_{\mathbf1,\ \text{two states}},
\;}
$$

$$
\boxed{\;
6+6+2+2=16,
\qquad
Y=T_{3R}+\tfrac12(B-L),
\qquad
Q=T_{3L}+Y,
\qquad
\sum_{\text{generation}}Q=0,\quad \sum_{\text{generation}}(B-L)=0 .
\;}
$$

**The single idea.** The fermion quantum numbers are not an input list. They are the two Cartan eigenvalues the chain leaves behind — $B-L$ from the first step, $T_{3R}$ from the second — combined by one formula, and then the electric charge is a third combination on top. Every entry of the charge table follows from the value of $B-L$ on the quartet, which is itself fixed by declaring the fourth colour to be the lepton.

**What the article establishes.** The content of the sixteen at each stage of the chain; the split $\mathbf4\to\mathbf3\oplus\mathbf1$ and its reading as "three colours and a lepton line"; the assignment of $T_{3R}$ within the right doublet; hypercharge derived from $B-L$ and $T_{3R}$; the charge table with its two vanishing sums; why there is exactly one quark doublet and one lepton doublet per generation; and the anomaly arithmetic that makes the content consistent.

**What the article does not establish.** No mass and no mixing. The Yukawa sector, the one-matrix proportionality $M_d\propto M_e$ and its failure are [The Yukawa Sector of the Four Colours Left–Right Model: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-of-the-four-colours-left-right-model-fermion-mass-matrices-and-their-diagonalisation.html). The generation count is [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html).

**Where the content is owned.** The sixteen states, their $CP$ closure and the antiparticle tables are [Classification of the Fermions in the Four Colours Left–Right Model: One Generation, Sixteen Fields, Thirty-Two States, Closed Under $CP$ and Not Under $C$](classification-of-the-fermions-in-the-four-colours-left-right-model-one-generation-sixteen-fields-thirty-two-states-closed-under-cp-and-not-under-c.html). The hypercharge assignment as an anomaly problem is [The Electroweak Gauge Group and the Hypercharge Assignment in the Four Colours Left–Right Model: The Group and the Derived $Y$](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). This article owns the reading of the content after the breaking.

## The Sixteen and the Two Blocks

**Two blocks, because chirality is a choice of which factor acts.** The count is arithmetic before it is physics.

**1.1 The two blocks.** The left block is $(\mathbf4,\mathbf2,\mathbf1)$: eight states, the $\mathrm{SU}(4)$ index and the $L$ index live, the $R$ index trivial. The right block is $(\bar{\mathbf4},\mathbf1,\mathbf2)$: eight states, the conjugate quartet and the $R$ index live, the $L$ index trivial. Together

$$
4\cdot2\cdot1+4\cdot1\cdot2=8+8=16 .
$$

**1.2 Why the conjugate.** The right block carries $\bar{\mathbf4}$ and not $\mathbf4$. That single bar is what makes the sixteen anomaly-free in $\mathrm{SU}(4)$ and what makes the right-handed fields conjugates of quartet states rather than quartet states. It is also the reason $B-L$ has the sign it has on the right-handed leptons.

**1.3 The third factor is not parallel to the second.** The two blocks are not "the same eight twice". $(\mathbf4,\mathbf2,\mathbf1)$ and $(\mathbf4,\mathbf1,\mathbf2)$ are different modules, and the difference is which weak factor acts. Reading the pair as a $(\mathbf4,\mathbf2,\mathbf2)$ would give sixteen states with both weak factors live on all of them, which is the vector-like content the model does not have.

## The Split at $M_C$: Three Colours and a Lepton Line

**The first step divides the quartet.** One line out, three lines left.

**2.1 The branching.** Under $\mathrm{SU}(4)\to\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}$,

$$
\mathbf4\to\mathbf3_{+\frac13}\oplus\mathbf1_{-1},
\qquad
\bar{\mathbf4}\to\bar{\mathbf3}_{-\frac13}\oplus\mathbf1_{+1},
$$

the subscripts being $B-L$. The three are the colours; the one is the lepton line, the fourth colour.

**2.2 The two blocks, branched.** The left block becomes a colour triplet that is an $L$ doublet and a colour singlet that is an $L$ doublet:

$$
(\mathbf4,\mathbf2,\mathbf1)\to(\mathbf3,\tfrac13;\mathbf2,\mathbf1)\oplus(\mathbf1,-1;\mathbf2,\mathbf1).
$$

The right block becomes a colour antitriplet and a colour singlet, both $R$ doublets. So after $M_C$ the content is: a quark doublet, a lepton doublet, an antiquark doublet and an antilepton doublet, and $B-L$ is a good quantum number on all four.

**2.3 What the first step buys.** Before it, $B-L$ is a direction inside a simple group and there is no quantum number to assign. After it, every state has a definite $B-L$, and the two blocks differ by $\pm\tfrac13$ on the coloured states and by $\mp1$ on the singlet. That difference is the whole content of "three colours and a lepton line".

**2.4 Why the lepton is a colour.** The declaration is that the fourth colour is the lepton, and its consequence is the eigenvalue list $(-1,\tfrac13,\tfrac13,\tfrac13)$ on the quartet in the order $(e_t,\vec e_x,\vec e_y,\vec e_z)$. Charge quantisation follows from that list, because the trace $\operatorname{tr}_{\mathbf4}(B-L)=-1+1=0$ forces the three quark values once the lepton value is fixed. The argument is [Charge Quantisation from the Fourth Colour: One Trace, One Third](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html), and it is not repeated here.

## The Right Doublet at $M_R$: $T_{3R}$ Becomes a Label

**The second step splits each right doublet.** Two states, two labels, and one of them is new.

**3.1 The branching.** Under $\mathrm{SU}(2)_R\to\mathrm{U}(1)_R$ a doublet splits into its two components, which carry $T_{3R}=\pm\tfrac12$. Applied to the right block:

$$
(\bar{\mathbf3},-\tfrac13;\mathbf1,\mathbf2)\to
(\bar{\mathbf3},-\tfrac13)_{+\frac12}\oplus(\bar{\mathbf3},-\tfrac13)_{-\frac12},
$$

and the same for the singlet. So each right-handed species is resolved into two, and the resolution is what allows a mass term to be written for one member and not the other.

**3.2 The physical fields.** The states of the $\bar{\mathbf4}$ block are conjugates of the right-handed fields, so the sign of every charge flips when the block is read as $\{u_R,d_R,\nu_R,e_R\}$. That flip is the bookkeeping behind the $-\tfrac13$ and $+1$ in §*The Split at $M_C$* becoming $+\tfrac13$ and $-1$ on the physical states.

**3.3 Why the resolution matters.** Above $M_R$ the two members of a right doublet are degenerate: $\mathrm{SU}(2)_R$ rotates one into the other and no mass term distinguishes them. Below $M_R$ they carry different $T_{3R}$, hence different $Y$, hence different $Q$: an up-type and a down-type quark, a neutrino and an electron. The mass splitting of the members of a right doublet is therefore a consequence of the second breaking and not an input.

## Hypercharge, Derived

**One formula, and it needs both previous steps.** This is the section that answers where the numbers come from.

**4.1 The formula.**

$$
Y=T_{3R}+\tfrac12(B-L).
$$

**4.2 Why the coefficients are what they are.** The half in front of $B-L$ is the normalisation of the $\mathrm{SU}(4)$ generator that survives the first step: $B-L=\sqrt{8/3}\,T^{15}$, and the trace normalisation of $T^{15}$ is $\tfrac12$. The unit in front of $T_{3R}$ is the normalisation of the $\mathrm{SU}(2)$ Cartan. The two coefficients differ because the two groups enter the algebra with different trace normalisations, and that difference is the reason the weak mixing angle is not $\tfrac12$ at the breaking scale.

**4.3 The check on each species.**

| physical field | $T_{3R}$ | $B-L$ | $Y=T_{3R}+\tfrac12(B-L)$ | observed $Y$ |
|---|---|---|---|---|
| $u_R$ | $+\tfrac12$ | $+\tfrac13$ | $\tfrac12+\tfrac16=\tfrac23$ | $\tfrac23$ |
| $d_R$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac12+\tfrac16=-\tfrac13$ | $-\tfrac13$ |
| $\nu_R$ | $+\tfrac12$ | $-1$ | $\tfrac12-\tfrac12=0$ | $0$ |
| $e_R$ | $-\tfrac12$ | $-1$ | $-\tfrac12-\tfrac12=-1$ | $-1$ |
| $Q_L$ | $0$ | $+\tfrac13$ | $\tfrac16$ | $\tfrac16$ |
| $L_L$ | $0$ | $-1$ | $-\tfrac12$ | $-\tfrac12$ |

**4.4 What the table is not.** It is not a fit. The two inputs are $B-L$, fixed by the declaration of the fourth colour, and $T_{3R}$, fixed by which member of the doublet a field is. Both are discrete. Nothing in the table is adjusted.

## The Electric Charge and the Table

**The third combination, and the two sums that check it.**

**5.1 The formula.** $Q=T_{3L}+Y$. The left factor's Cartan is $\pm\tfrac12$ on a doublet and $0$ on a singlet.

**5.2 The generation.**

| field | multiplicity | colour | $T_{3L}$ | $T_{3R}$ | $B-L$ | $Y$ | $Q$ |
|---|---|---|---|---|---|---|---|
| $Q_L=(u_L,d_L)$ | $6$ | $\mathbf3$ | $\pm\tfrac12$ | $0$ | $+\tfrac13$ | $+\tfrac16$ | $+\tfrac23$, $-\tfrac13$ |
| $u_R$ | $3$ | $\mathbf3$ | $0$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ | $+\tfrac23$ |
| $d_R$ | $3$ | $\mathbf3$ | $0$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ | $-\tfrac13$ |
| $L_L=(\nu_L,e_L)$ | $2$ | $\mathbf1$ | $\pm\tfrac12$ | $0$ | $-1$ | $-\tfrac12$ | $0$, $-1$ |
| $\nu_R$ | $1$ | $\mathbf1$ | $0$ | $+\tfrac12$ | $-1$ | $0$ | $0$ |
| $e_R$ | $1$ | $\mathbf1$ | $0$ | $-\tfrac12$ | $-1$ | $-1$ | $-1$ |

Multiplicities: $6+3+3+2+1+1=16$.

**5.3 The charge sum.** $1+2-1-1+0-1=0$: the quark doublet contributes $3(\tfrac23-\tfrac13)=1$, the up singlets $3\cdot\tfrac23=2$, the down singlets $3\cdot(-\tfrac13)=-1$, the lepton doublet $0-1=-1$, the neutrino singlet $0$, the electron singlet $-1$. A generation is neutral.

**5.4 The $B-L$ sum.** $6\cdot\tfrac13+3\cdot\tfrac13+3\cdot\tfrac13+2\cdot(-1)+(-1)+(-1)=2+1+1-2-1-1=0$. The same vanishing, read on the other charge, and it is the same arithmetic as $\operatorname{tr}_{\mathbf4}(B-L)=0$ multiplied by the two chiralities.

**5.5 The proton's charge, as an example of the same identity.** $uud$ gives $\tfrac23+\tfrac23-\tfrac13=1$, and the electron gives $-1$: the hydrogen atom is neutral because $Q$ is a linear combination with the coefficient of $B$ fixed by the trace. This is what "charge quantisation" means here, and it is the reason the fourth colour had to be the lepton.

## The Two Weak Doublets

**Why exactly two, and why one of each kind.** The count is the module structure, not a convention.

**6.1 The count.** A left doublet needs an $L$ index; the left block has one; the left block is a $\mathbf4$ of $\mathrm{SU}(4)$, which branches to $\mathbf3\oplus\mathbf1$. So there is one doublet on the triplet and one on the singlet: a quark doublet and a lepton doublet, and no third.

**6.2 Why there is no right-handed doublet below $M_R$.** The right doublets exist above $M_R$ and are resolved by the second breaking. Below $M_R$ each of their members is a singlet of everything except $\mathrm{U}(1)_Y$, so the low-energy theory has only left doublets and right singlets. That is the observed structure, and here it is a consequence of the breaking rather than an axiom.

**6.3 The neutrino.** The right block contains a colour singlet with $B-L=-1$ and $T_{3R}=+\tfrac12$, whose conjugate is $\nu_R$: a Standard-Model singlet with zero charge and zero hypercharge. The model therefore has a right-handed neutrino without adding one, and the mass it can carry — a Majorana mass at $M_R$ — is the seesaw of [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html).

## Anomalies and the Trace

**Why the content is consistent, in one line and four checks.**

**7.1 The one line.** $\operatorname{tr}_{\mathbf4}(B-L)=0$.

**7.2 The four consequences.**

| anomaly | coefficient | why it vanishes |
|---|---|---|
| $[\mathrm{SU}(4)]^3$ | index of $\mathbf4$ minus index of $\bar{\mathbf4}$ | the two blocks are conjugates, so $1-1=0$ |
| $[\mathrm{SU}(4)]^2\,\mathrm{U}(1)_{B-L}$ | $2\operatorname{tr}_{\mathbf4}(B-L)$ | the trace is zero |
| $\mathrm{SU}(2)_{L,R}^2\,\mathrm{U}(1)_{B-L}$ | $\sum_{\text{doublets}}B-L$ | quark doublet $+2$, lepton doublet $-2$ |
| $\mathrm{U}(1)_{B-L}^3$ | $\sum(B-L)^3$ over the sixteen | $2(-1)+6(\tfrac1{27})$ against $2(+1)+6(-\tfrac1{27})$, and the blocks cancel |
| gravity | $\sum B-L$ over the sixteen | zero, as in §*The Electric Charge and the Table* |

**7.3 What this is not.** It is not a proof that the model is anomaly-free at every order. It is the statement that the cubic and mixed anomalies vanish because the sixteen is built from a quartet and its conjugate, and that the vanishing is a property of the trace rather than of a cancellation between unrelated multiplets. The full treatment is [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model: Four Conditions Become None](anomalies-and-anomaly-cancellation-in-the-four-colours-left-right-model.html).

**7.4 The $CP$ remark.** The sixteen is closed under $CP$ and not under $C$, and the exchange of the two weak factors is what closes it. That is not used anywhere above, and it is the reason the model is a left–right model rather than a vector-like one.

## What the Fermion Content Does Not Say

**Four silences.** Each is a different article.

**8.1 Masses.** Every entry in the table is a quantum number. None is a mass. The masses come from Yukawa couplings, and the minimal content's single bidoublet forces $M_d\propto M_e$: [The Yukawa Sector of the Four Colours Left–Right Model: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-of-the-four-colours-left-right-model-fermion-mass-matrices-and-their-diagonalisation.html).

**8.2 Mixing.** The table is diagonal in flavour by construction: one generation. The CKM and PMNS matrices are [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) and [The PMNS Matrix and Lepton Mixing](the-pmns-matrix-and-lepton-mixing.html).

**8.3 The number of copies.** Nothing above fixes three generations. The repetition is [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html).

**8.4 Which vacuum the quarks see.** The table is the content, not the spectrum: confinement, and with it the absence of free quarks, is [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html).

## The Checks

**Six checks.**

| check | computation | result |
|---|---|---|
| the count | $6+6+2+2$ | $16$ |
| the branching | $4\cdot2\cdot1$ and $\bar4\cdot1\cdot2$ | $8+8$ |
| hypercharge | $Y=T_{3R}+\tfrac12(B-L)$ on all six species | matches the observed table |
| the charge | $\sum Q$ over the generation | $0$ |
| $B-L$ | $\sum(B-L)$ over the generation | $0$ |
| the trace | $\operatorname{tr}_{\mathbf4}(B-L)=-1+3\cdot\tfrac13$ | $0$ |

## Distinctions That Are Easy to Lose

**Three pairs.**

**9.1 The block's labels and the physical fields.** The $\bar{\mathbf4}$ block's charges are the negatives of the physical right-handed fields' charges. A table that mixes the two conventions has the wrong sign on $u_R$ and on $e_R$ and is still internally consistent, which is why the error survives.

**9.2 Hypercharge and the weak hypercharge of the checklist.** The corpus writes $Y$; the reference tables often write $Y_W=2Y$. Both are consistent, and the factor two is a convention on the $\mathrm{U}(1)$ normalisation.

**9.3 Sixteen and fifteen.** The sixteen includes $\nu_R$. A content with fifteen states is the Standard Model's, and it has no $T_{3R}$ to build hypercharge from. The sixteenth state is what makes the derivation of §*Hypercharge, Derived* possible.

## Summary

**The content.** $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$, sixteen states, branching to a quark doublet, two up-type and down-type singlets, a lepton doublet and two lepton singlets.

**The colours.** Three, plus a lepton line: the split $\mathbf4\to\mathbf3\oplus\mathbf1$ at $M_C$.

**The doublets.** Two left doublets, one quark and one lepton; the right doublets are resolved at $M_R$.

**The charges.** $Y=T_{3R}+\tfrac12(B-L)$ and $Q=T_{3L}+Y$, both derived, both discrete, with $\sum Q=\sum(B-L)=0$ over a generation.

**The consistency.** The anomalies vanish because the sixteen is a quartet and its conjugate and because $\operatorname{tr}_{\mathbf4}(B-L)=0$.

**What is missing.** Masses, mixing, and the number of generations.

## Summary of Notation

| symbol | meaning |
|---|---|
| $(\mathbf4,\mathbf2,\mathbf1)$, $(\bar{\mathbf4},\mathbf1,\mathbf2)$ | the two blocks of the sixteen |
| $Q_L$, $L_L$ | the quark and lepton left doublets |
| $u_R$, $d_R$, $\nu_R$, $e_R$ | the right-handed singlets |
| $B-L$ | baryon number minus lepton number, the $\mathrm{SU}(4)$ Cartan that survives $M_C$ |
| $T_{3L}$, $T_{3R}$ | the Cartan eigenvalues of the two weak factors |
| $Y$, $Q$ | hypercharge and electric charge |
| $\operatorname{tr}_{\mathbf4}$ | the trace over the quartet, the source of every vanishing sum |
| $M_C$, $M_R$ | the scales of the colour and right-handed breakings |

## Further Reading

- [Classification of the Fermions in the Four Colours Left–Right Model: One Generation, Sixteen Fields, Thirty-Two States, Closed Under $CP$ and Not Under $C$](classification-of-the-fermions-in-the-four-colours-left-right-model-one-generation-sixteen-fields-thirty-two-states-closed-under-cp-and-not-under-c.html). The states, the antiparticle tables and the $CP$ closure.
- [The Electroweak Gauge Group and the Hypercharge Assignment in the Four Colours Left–Right Model: The Group and the Derived $Y$](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). The same assignments read as an anomaly problem, with the three rays and the one that survives.
- [Charge Quantisation from the Fourth Colour: One Trace, One Third](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). Why the trace fixes the eigenvalues $(-1,\tfrac13,\tfrac13,\tfrac13)$.
- [The Yukawa Sector of the Four Colours Left–Right Model: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-of-the-four-colours-left-right-model-fermion-mass-matrices-and-their-diagonalisation.html). What the content cannot say about masses.
- [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model: Four Conditions Become None](anomalies-and-anomaly-cancellation-in-the-four-colours-left-right-model.html). The anomaly arithmetic in full.
- [The Order of the Breaking in the Four Colours Left–Right Model: Nested Vacua and the Scale Order $M_C\ge M_R\ge M_W$](the-order-of-the-breaking-in-the-four-colours-left-right-model-nested-vacua-and-the-scale-order.html). Why $T_{3R}$ is a label only below $M_R$ and $B-L$ only below $M_C$.
