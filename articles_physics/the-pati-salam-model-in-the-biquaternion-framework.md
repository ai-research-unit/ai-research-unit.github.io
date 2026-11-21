# __The Pati–Salam Model in the Biquaternion Framework: Four Colours, $21$ Generators, One Coupling__

## Introduction

**The layer.** This is the frame article, so it carries both layers and labels them: **Layer A** is what the algebra does on its own carrier, and **Layer B** is $G_{PS}$ acting on a formal copy of that carrier. §“Where Each Factor Comes From, and How Firmly” is where each factor is assigned to one of the two, and the assignment is the article's main claim.

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
\dim_{\mathbb R}\mathfrak g_{PS}=15+3+3=21,
\qquad
\operatorname{rank}=3+1+1=5
\;}
$$

with the two-sided structure of the algebra supplying the second and third factors, and the carrier supplying the first.

**It opens the section, and it is the only article here that names a particular group.** The eighteen that follow are written for a general gauge group — the principle, the connection, the curvature, the path integral, the lattice — and every one of them reads correctly for $G_{PS}$. **This one says which group they are being read for**, and it is placed first for that reason.

**What is claimed.** That the twenty-one dimensions split as $15+3+3$ and the fifteen as $8+1+6$; that the two $\mathrm{SU}(2)$ factors arise from the algebra's own two-sided action and not from an import; that the fermion content is the sixteen of $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$; that one covariant derivative with one coupling covers all twenty-one; and that the group acts on a **formal copy** of the carrier's quartet, for the reason computed under *The Carrier Is a Copy*.

**What is not claimed.** That the algebra derives the group. It derives two of the three factors and the split of the third. **The identification of that split with the quark–lepton quartet is a declaration, with a price**, called (A) throughout and stated in *The Sixteen* and *Where Each Factor Comes From*. Nor that the group makes the theory chiral: it does not, and *The Chiral Wall, Restated for This Group* says why.

## Why the Corpus Adopts the Pati–Salam Model

**The corpus adopts an extension of the Standard Model.** The group it uses to describe the particles is Pati–Salam, $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$. **Call it a moderate extension with a specific structural motivation**: *moderate* against the alternatives, which are larger, and moderate against the Standard Model only in the fermion sector. **Nothing the Standard Model says is dropped**, which is the part unambiguously in its favour, and no measurement below the Pati–Salam scale distinguishes the two theories.

**The extension, in numbers.**

| | Standard Model | Pati–Salam model | the change, honestly |
|---|---|---|---|
| gauge generators | $12$ | $21$ | $+9$, a factor $1.75$ — not a rounding error |
| fermions per family | $15$ | $15$ | none: $\nu_R$ is the fourth component of the $\bar{\mathbf4}$, not an addition |
| families | $3$ | $3$ | none; no fourth generation |
| scalars | $4$ real degrees of freedom | $24$: eight and four complex components in a $(\mathbf4,\mathbf1,\mathbf2)$ and a $(\mathbf1,\mathbf2,\mathbf2)$ | a factor $6$, and the sector that genuinely costs |
| surviving scalars | one Higgs | twelve real: four from the bidoublet, eight from $\Phi$ | $24$ real components against $12$ broken generators, so twelve survive; **two neutral states mix, and the lighter is the $125$ GeV candidate**, and the cost is elsewhere — see below |
| scales | one | two | $M_{PS}\gtrsim250$ TeV, a ratio $M_{PS}/M_{Z}\gtrsim2.7\times10^{3}$ |
| hierarchy | the electroweak scale, unexplained | $M_{PS}$ and $M_{EW}$ both | the same problem, with a new gap to stabilise |

**Three of those rows are costs and this article does not soften them.** The scalar sector grows by a factor of six: twenty-four real components in place of the Standard Model's four, and twelve of them are eaten, because the chain breaks exactly twelve generators. **The minimal sector is not short of scalars, and the count is worth stating because it is the one place where a plausible reading goes wrong.** The $(\mathbf4,\mathbf1,\mathbf2)$ holds eight complex components, that is sixteen real ones; the breaking of $\mathrm{SU}(4)$ and of $\mathrm{SU}(2)_R$ removes eight of them as Goldstones and leaves eight — a colour triplet and one charged singlet, all $\mathrm{SU}(2)_L$ singlets. The bidoublet holds four complex components, eight real ones; the electroweak breaking removes four and leaves four, a charged pair and two neutral states, and the lighter neutral one is what a $125$ GeV resonance would be. **So the failure is not a shortage of scalars. It is a wrong mass relation.** One bidoublet couples the up-type and the down-type quarks through the same Yukawa matrix, so it predicts $m_d=m_e$ at $M_{PS}$, and the measured $m_d/m_e\simeq2.2$ contradicts it. That is what the corpus's ledger calls **F2**: a failure of content rather than of arithmetic, whose repair is a second bidoublet or a $(\mathbf{15},\mathbf2,\mathbf2)$ — and the $(\mathbf{15},\mathbf2,\mathbf2)$ brings colour-triplet scalars that can mediate proton decay at dimension six. The new scale brings the hierarchy question in a sharper form: the model must explain why $M_{PS}/M_{EW}$ is what it is. And the leptoquark bound *pushes that scale up*, which makes both problems worse, not better.

**What is genuinely small is the fermion sector, and what is genuinely cheap is the limit.** Break the larger group and the Standard Model comes out, with the same fields, the same couplings and the same Lagrangian, **so every measurement the Standard Model passes this model passes, and for the same reason.** A reader who wants the Standard Model back can have it by taking $M_{PS}\to\infty$. **The case for the extension therefore cannot rest on agreement with experiment, which it inherits; it has to rest on what the extension explains and on how it sits in the algebra.** That is what the six reasons below are about.

**A framework has to describe the particles with some group, and the choice is not free.** The corpus could have stayed with $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ and treated the algebra as a language for its equations: keep $G_{\mathrm{SM}}$ as the gauge group, ask nothing of the algebra beyond notation, and let the carrier, the two-sided product and the operators stay the vocabulary in which the equations are written. **Hypercharge would remain an imported number, quarks and leptons would remain separate representations, and there would be no fourth colour, no leptoquark and no $W_R$.** Nothing would be false under that choice, and nothing would be at risk.

**It is not a straw position, because it is the corpus's own default.** The $541$ articles outside this category are written that way, and so is the electromagnetic category entire: Maxwell's equations are exact at every scale and need no breaking scale to be stated. **The particle category is the only place where the question of the group arises at all**, and the reasons below are the reasons the answer there is not the Standard Model's group.

**What each choice costs, stated before the reasons are given.** Staying would leave five things unexplained that the model explains without a new field — the values of hypercharge, charge quantisation, the four anomaly cancellations, the existence of $\nu_R$, and custodial symmetry — and would leave the algebra's four-dimensional carrier a coincidence. **Adopting puts one declaration under load and predicts six states that have not been seen.** The reasons are not one-sided, and they are not presented as if they were.

**The six reasons, in descending order of strength**: the empirical, the structural, the compatibility with the algebra, the comparison with the competitors, the explanatory yield, and the falsifiability.

**1. No measurement contradicts it.** Every place where the model differs from the Standard Model sits at or above the Pati–Salam scale, and the scale is bounded from below, not from above. The six leptoquarks mediate $K_L\to\mu e$ at tree level with no CKM suppression, and the measured null result $\mathcal B(K_L\to\mu e)<4.7\times10^{-12}$ forces

$$
M_X\gtrsim 2.5\times10^{2}\ \mathrm{TeV},
$$

which is a lower bound on the new physics rather than a bound on the model's consistency. **Below that scale the two theories are the same theory**: the same group content, the same couplings, the same fields.

**The bound is not costless, and an earlier version of this section called the lower bound a statement with no cost, which was too generous.** Satisfying $K_L\to\mu e$ requires $M_{PS}$ above $250$ TeV, and every cost of the model grows with $M_{PS}$: the hierarchy $M_{PS}/M_{EW}$ grows, the running in *The Number That Fails* gets worse, and the leptoquarks recede from reach. **The honest statement is that the null result is satisfied for $M_{PS}\gtrsim250$ TeV and that this pushes the model into the region where its other problems are sharpest.** It is a lower bound on the new physics and a lower bound on the model's discomfort.

**Agreement with experiment is cheap** — any extension that reduces to the Standard Model agrees with it — so this reason is necessary and not sufficient. It is listed first because a candidate that failed it would need no further discussion, not because it is evidence.

**2. It is the smallest extension that can do the job.** The table above already says what grows and what does not; the reason is about the choice between candidates rather than the arithmetic. **No new fermion, no fourth generation, no new dimension, no change to spacetime** — and the nine new bosons are the minimum needed to gauge the fourth colour and the right-handed weak group. A larger group, $\mathrm{SO}(10)$ or $E_6$, would add structure that buys nothing the corpus can spend; a smaller one, the Standard Model itself or the left–right group, cannot do what a gauged fourth colour does. **Minimality is not a proof, but it is the right prior when the data cannot decide**, and the corpus is explicit that the data cannot decide.

**3. The Pati–Salam model is fully compatible with the biquaternion algebra formalism, much more than the Standard Model. This is the strongest reason.** *Compatible* here does not mean *not in conflict*, which is cheap and true of any extension. It means that **each of the model's three factors is a structure the algebra's carrier or product already supplies**, while one of the Standard Model's three factors is a group the algebra's own compact action provably cannot carry and another is a factor whose charge table is put in by hand.

**The reason is one of licensing and not of membership.** What matters is not what the algebra *contains* — that is an eight-dimensional space, and a group of twenty-one dimensions cannot be inside it. What matters is what the algebra *supplies*: a carrier of four complex dimensions, a canonical split of that carrier into a line and a three-space, and a two-sided action on it. The model is the group that those three structures license, acting on a formal copy of the carrier. **Stated as membership, the claim would be false; stated as licensing, it is the whole of the argument.**

| group | generators | what supplies it |
|---|---|---|
| $\mathrm{SU}(4)$ | $15$ | the unitary group of the carrier, on its four complex dimensions |
| $\mathrm{SU}(2)_L$ | $3$ | left multiplication, $\{L_{\vec e_a}\}$ — **endomorphisms whose parameter is $\vec e_a$** |
| $\mathrm{SU}(2)_R$ | $3$ | right multiplication, $\{R_{\vec e_a}\}$ — **endomorphisms whose parameter is $\vec e_a$** |

**The precision the slogan needs.** One of the twenty-one generators is **an element of the algebra** — the central phase, $\mathbb R(ie_t)$. The six sides are **endomorphisms of length one whose parameters are the imaginary units**: $L_{\vec e_a}$ acts on an element, and the element it multiplies by is $\vec e_a$. The other fifteen are **the unitary group of the carrier**, which is a group *of* the algebra's action and not *in* the algebra: $\dim_{\mathbb R}\mathbb B=8$, and fifteen does not fit inside eight. So the honest statement is not "twenty-one out of twenty-one live in the algebra" but **"every one of the twenty-one is a structure the algebra supplies; one is literally in the algebra, six are endomorphisms whose parameters are algebra elements, and fifteen are the unitary group of the carrier"** — which is still a stronger claim than the Standard Model can make, and it is stronger because it is precise. **The distinction matters because the fifteen are the factor that has to be declared**: the carrier is given, but that its four dimensions are colour is (A).

**The comparison factor by factor is the substance of the reason:**

| factor | in the Standard Model | in this model |
|---|---|---|
| colour, $8$ | a group the algebra's own compact action cannot host: $\dim\mathfrak{su}(3)=8>4=\dim\mathfrak{u}(2)$ | the stabiliser $\mathrm{Stab}_{\mathfrak{su}(4)}(e_t)$, that is $8=15-1-6$ of the carrier's group |
| weak isospin, $3$ | the algebra's left action — the one factor the corpus derives | the left half of the two-sided product |
| hypercharge, $1$ | the algebra has a $\mathrm{U}(1)$, but **which charge each field carries is chosen**: the step $q=6Y$ is selected to make the observed table integral | not a factor at all: $Y=T_{3R}+\tfrac12(B-L)$, with the quartet's eigenvalues fixed by $\operatorname{tr}_{\mathbf4}(B-L)=0$ |

**One of the Standard Model's three factors is a structure the algebra can host; all three of the model's are.** That is what *fully compatible* means here, and it is why the model is not a larger group laid on top of the algebra but the group the algebra's own objects were shaped for: the carrier supplies the fifteen, the two-sided action supplies the six, and the fourth colour is a direction the carrier already has. **Three of three by licensing, one of three by containment** — and the difference between the two counts is the difference the whole article turns on.

**None of this is a derivation, and the difference matters.** The algebra supplies the carrier, the stabiliser, the two-sided product and the traceless diagonal; the model supplies the names of the particles that sit in them, and the identification of the fourth direction with the lepton is **declared**, not derived. **Where the corpus had a four-dimensional complex carrier and needed a group, the model is the group that uses exactly that space** — and a group chosen for the space it acts on, rather than a space chosen for the group, is the only kind of match worth anything here. The price is stated in *The Carrier Is a Copy*: the group acts on a formal copy of the quartet, because $\mathfrak{su}(4)$ commutes with the Lorentz action only in $\mathfrak{su}(2)$.

**4. It is the best of the four candidates on the corpus's own criteria.** $\mathrm{SU}(5)$ puts quarks and leptons in one multiplet, has no $\nu_R$, and would need a five-dimensional carrier the algebra does not have.

**$\mathrm{SO}(10)$ needs a real answer, because it contains $G_{PS}$ and its sixteen *is* the Pati–Salam sixteen.** If the algebra points at $G_{PS}$ and $G_{PS}$ sits inside $\mathrm{SO}(10)$, a reader may ask whether the algebra secretly points at $\mathrm{SO}(10)$. **Three reasons it does not, and the first is the decisive one.** The carrier has four complex dimensions; $\mathrm{SO}(10)$'s smallest spinor is sixteen-dimensional and needs a Clifford module, so the algebra would have to supply a structure it does not have — **and "does not have" here is a theorem, not a taste**: the corpus uses biquaternions and not octonions or Clifford algebras for a reason, and the reason is that $\mathbb B\cong M_2(\mathbb C)$ has a four-dimensional carrier. Second, $\mathrm{SO}(10)$'s extra twenty-four generators act on a space the algebra's carrier is not, so they would be imported in exactly the way §4 refuses. Third, **$\mathrm{SO}(10)$ is rank $5$ and so is $G_{PS}$, so the rank argument that decides between two candidate groups here does not distinguish them** — the rank is evidence that the embedding exists, not evidence that it should be used. **The containment is real and it is not an argument:** $G_{PS}\subset\mathrm{SO}(10)$ says the smaller group is available inside the larger one, and the corpus takes the smaller one because the carrier is four-dimensional.

**The left–right group is the honest competitor**, and it is a closer call than $\mathrm{SO}(10)$: $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}$ gives the same physics below the scale, **with the $\mathrm{U}(1)$ charge put in by hand** where the model derives it from a tracelessness condition. *Why This Group and Not a Larger One* states the three refusals, and *The Carrier Is a Copy* states what the comparison costs. **Pati–Salam is what is left when the carrier is four-dimensional, the product is two-sided, and the fourth direction is gauged.**

**5. It answers five questions the Standard Model leaves open — given (A), and not for free.** Hypercharge stops being an imported number and becomes $Y=T_{3R}+\tfrac12(B-L)$. Charge quantisation stops being an observation about the electron and becomes $\operatorname{tr}_{\mathbf4}(B-L)=3\cdot\tfrac13-1=0$. The four anomaly conditions stop being conditions and become identities. $\nu_R$ stops being optional and becomes the fourth component of the $\bar{\mathbf4}$. Custodial symmetry stops being accidental and becomes the diagonal of a gauged pair.

**The qualifier is the same one every time, and it is not a detail.** The first two promotions need the eigenvalues of $B-L$ on the quartet to be $(1,-\tfrac13,-\tfrac13,-\tfrac13)$, and those are fixed **by the declaration that the fourth colour is the lepton**, not by the group. Without (A) the group still has a traceless diagonal; it does not know which direction is the lepton. **So the honest form of this reason is: five questions are answered given (A), and (A) is the model's one load-bearing declaration.** The anomaly cancellation is the one item that is genuinely structural — the sixteen is anomaly-free by construction, as a real multiplet of a complex group must be — but even that is a property of the multiplet the declaration chooses. **Five promotions for one assumption, not five for nothing.**

**6. It is falsifiable at a price the corpus can state.** Six states with fixed charge, fixed colour and a fixed mass ratio $M_X=\sqrt2\,M_{W_R}$, and a tree-level $K_L\to\mu e$. **A frame that predicts six states with no adjustable mass can be checked**, and the check has a shape: a leptoquark search, or a better bound. The angle is a different matter, and it is the one number in the frame that fails.

**The number that fails, quantified.** The frame gives $\sin^2\theta_W(M_{PS})=\tfrac38$, but that is **a boundary condition and not a prediction**: it says what the ratio of couplings must be at the scale where the group breaks, and the value at $M_{Z}$ is then a statement about the matter content in between. Run the measured couplings up with the Standard Model content, one loop, $b_{1}=\tfrac{41}{10}$ and $b_{2}=-\tfrac{19}{6}$:

| quantity | value | comment |
|---|---|---|
| $\sin^2\theta_W(M_{Z})$ | $0.2312$ | the measurement |
| $\sin^2\theta_W(250\ \mathrm{TeV})$ | $0.272$ | the minimal content run up to the leptoquark bound |
| $\mu$ at which $\sin^2\theta_W=\tfrac38$ | $1.0\times10^{13}\ \mathrm{GeV}$ | seven and a half decades above the bound |
| $\sin^2\theta_W(M_{Z})$ from $\tfrac38$ at $250$ TeV | $0.33$ | against $0.231$: $43\%$ too large |

**So the failure has a size, and the size is not small.** The model needs $\tfrac38$ at $250$ TeV, where the data give $0.272$: the model's value is $38\%$ high. Equivalently, the data reach $\tfrac38$ only at $10^{13}$ GeV, **seven and a half decades above the scale the leptoquark bound forces.** Three remedies exist — extra matter between the two scales, a scale close to the bound with threshold corrections, or supersymmetry — and all three change the matter content, which is to say **the failure is a statement about what lies between the scales and not a contradiction at any one scale.** But it is a failure, and the corpus records it as one.

What survives from this reason is the leptoquark prediction, which is sharp and has no free parameter beyond $M_{PS}$, and the statement that the angle is a boundary condition rather than a success. **A frame that presents $\tfrac38$ as a prediction of $0.231$ is trading on a coincidence of notation**, and this article does not.

**What adoption does not mean, and the corpus says so in the same breath.** It does not mean the algebra derives the model: one declaration is load-bearing, the fourth colour as the unit line, and *The Sixteen* and *Where Each Factor Comes From* state it with its price. It does not mean the model is confirmed: **six states that should exist and have not been seen is the weakest form of failure and the most persistent one.** And it does not mean the ledger is all gains: **four rows of the corpus's own accounting improve, four are unchanged, and two get worse** — (A) becomes load-bearing for everything downstream, and $\tfrac38$ lands at $0.33$ against $0.231$. **The register of open failures has four entries**, and two of them are the ones no amount of writing repairs: the wrong mass relation of the scalar sector, and six leptoquarks that have not been seen and whose diquark coupling could keep them unseeable. **The reasons above are why the corpus adopts the model; they are not a claim that the model is right.**

## The Three Factors, and What Each One Is

**The first factor is the carrier's own group.** $\mathrm{SU}(4)$ is the unitary group of the four-dimensional complex space on which $\mathbb B$ acts, fifteen real dimensions, defined by $M^{\dagger}M=\mathrm I$ and $\det M=1$. **The group is not an element of the algebra and not a corner of its endomorphisms; it is the whole group of the carrier.**

**The other two factors are the algebra's two-sided action.** Left and right multiplication by the imaginary units give two commuting $\mathfrak{su}(2)$'s inside $\mathfrak{so}(4)$:

$$
\mathfrak k_L=\{L_{\vec e_a}\},\qquad \mathfrak k_R=\{R_{\vec e_a}\},\qquad [L_{\vec e_a},R_{\vec e_b}]=0,\qquad \dim\mathfrak k_L=\dim\mathfrak k_R=3,
$$

so that $\exp\mathfrak k_L\times\exp\mathfrak k_R=\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, six dimensions. **Nothing is imported here: the two factors are the two ways the algebra multiplies.** They are endomorphisms of $\mathbb B$ and not elements of it — each is a length-one word whose parameter is an imaginary unit.

**The arithmetic, and it closes twice.**

$$
21=\underbrace{15}_{\mathrm{SU}(4)}+\underbrace{3}_{\mathrm{SU}(2)_L}+\underbrace{3}_{\mathrm{SU}(2)_R},
\qquad
15=\underbrace{8}_{\mathfrak{su}(3)}+\underbrace{1}_{\mathbb R\,iD}+\underbrace{6}_{\mathfrak m}.
$$

**The first equation is the frame; the second is the reason the frame can break to the Standard Model.** The $8$ will survive as colour, the $1$ will mix into hypercharge, and the $6$ will become the leptoquarks. **The ranks are $3+1+1=5$**, and the chain runs $5\to5\to4\to3$: the first step keeps the rank, because the six leptoquarks are off-diagonal and eat no Cartan direction, and the electroweak step removes one, the last step one more.

## The Sixteen

**The fermions are not a choice of the group; they are the smallest anomaly-free assignment, and the algebra's split selects it.**

$$
\mathbf{16}=(\mathbf 4,\mathbf 2,\mathbf 1)\oplus(\bar{\mathbf 4},\mathbf 1,\mathbf 2),
\qquad
4\cdot2+4\cdot2=16 .
$$

**Read the two terms as the two chiralities.** The first holds the left-handed doublet of the quartet — three quark colours and one lepton, each doubled by $SU(2)_L$. The second holds the right-handed partners as singlets of $SU(2)_L$ and doublets of $SU(2)_R$. **So $\nu_R$ is not added: it is the fourth component of the $\bar{\mathbf 4}$, and it is required the moment the lepton is a colour.**

**Why the split $15=8+1+6$ is what makes this work.** $B-L$ is a generator of the $\mathrm{SU}(4)$, with eigenvalues $(1,-\tfrac13,-\tfrac13,-\tfrac13)$ on the quartet, and $\mathbf 4\to\mathbf 3\oplus\mathbf 1$ under $\mathrm{SU}(3)$. **That is exactly the quark–lepton split**, and it is (A): the algebra supplies the split $\mathbb C e_t\oplus B_V$, and the declaration says the line is the lepton.

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

## One Covariant Derivative

**The whole gauge content is one line.**

$$
D_\mu=\partial_\mu-ig_4\sum_{a=1}^{15}A_{a,\mu}T_{a}
-ig_L\sum_{i=1}^{3}W_{L,i,\mu}\tau_i
-ig_R\sum_{i=1}^{3}W_{R,i,\mu}\tau_i .
$$

**Every index is low, because the metric is the identity.** The corpus has one metric, $\delta_{\mu\nu}=(1,1,1,1)$, so a raised index names the same index and the caret carries none. **The labels $a$ and $i$ are labels and not frame slots**: they count the fifteen $\mathrm{SU}(4)$ generators and the three of each $\mathrm{SU}(2)$, so they stand in the subscript like every other name. **The sums are written, because no index is summed by convention** — an index that appears twice is summed only where a $\sum$ names it and its range.

**Twenty-one gauge fields, and at the Pati–Salam scale one coupling.** The unification condition is not $\mathrm{SU}(5)$'s: there is no group above, only the statement that the three factors have a common origin at $M_{PS}$ in the sense that

$$
g_3=g_L=g_R=g_4\qquad\text{at }M_{PS},
$$

where $g_3$ is the coupling of the $\mathrm{SU}(3)$ that survives inside the $\mathrm{SU}(4)$. **Whether that is a unification or a coincidence is a question the corpus cannot answer**; what the frame supplies is that the three couplings have one boundary value if the frame is right.

**What the twenty-one fields are, in the frame's own labels.**

| block | count | $SU(3)$ | $SU(2)_L$ | $SU(2)_R$ | fate |
|---|---|---|---|---|---|
| $A_{a,\mu}$, $a$ in the $\mathfrak{su}(3)$ corner | $8$ | $\mathbf 8$ | $\mathbf 1$ | $\mathbf 1$ | the gluons |
| $A_{15,\mu}$ | $1$ | $\mathbf 1$ | $\mathbf 1$ | $\mathbf 1$ | the $B-L$ boson, mixes into $\gamma$ and $Z$ |
| $A_{a,\mu}$, $a$ in $\mathfrak m$ | $6$ | $\mathbf 3+\bar{\mathbf3}$ | $\mathbf 1$ | $\mathbf 1$ | the leptoquarks |
| $W_{L,i,\mu}$ | $3$ | $\mathbf 1$ | $\mathbf 3$ | $\mathbf 1$ | $W_{L,\pm}$, one neutral |
| $W_{R,i,\mu}$ | $3$ | $\mathbf 1$ | $\mathbf 1$ | $\mathbf 3$ | $W_{R,\pm}$, one neutral |

**The table is most of the boson spectrum.** Its three group columns are the reason the spectrum counts $9$ massless against $12$ massive: the eight gluons and the photon survive, and the six leptoquarks, $W_{L,\pm}$, $Z$, $W_{R,\pm}$ and $Z_R$ acquire mass. The two neutral entries in the last two rows join the $B$-$L$ boson in the mixing that produces the photon and the $Z$.

## Where Each Factor Comes From, and How Firmly

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

**The criterion of legitimacy, stated once, because every other article in this family quotes it.** The corpus carried an implicit test: **a gauge group is legitimate only if its generators are elements of the algebra**, $X\in\mathbb B$. **That test is the old habit, and under Pati–Salam it must go.** It is also refuted by the corpus's own later notes, which place $\mathfrak{su}(3)$ and $\mathfrak{su}(4)$ in the endomorphisms of $\mathbb B$ and never in $\mathbb B$.

**The replacement is the corpus's own, and it is an address rather than a filter.** A generator is an element of $\operatorname{End}_{\mathbb C}(\mathbb B)$, and the sixteen words $e_\mu[\,]e_\nu=L_{e_\mu}R_{e_\nu}$ are a basis of it. The **length** is the rank of the coefficient array, and **Conway's bound is $\ell\le4$**:

$$
M=\sum_{\mu,\nu}c_{\mu\nu}\,L_{e_\mu}R_{e_\nu},\qquad
\ell(M)=\operatorname{rank}\bigl(c_{\mu\nu}\bigr)\le4 .
$$

**The bound is four because a single two-sided product has a rank-one array.** $L_bR_c$ corresponds to $bc^{\mathsf T}$, so a sum of $k$ products has array of rank at most $k$ and every endomorphism of $\mathbb B$ is a sum of at most four. This is stated and verified in *The Meaning of $\mathrm{SU}(4)$ in the Endomorphisms of the Biquaternion Algebra*, §*The Carrier, the Six Words, and the Condition*; **the particle-physics articles have not been using it**, and that is the whole of what this section repairs.

**Why the rank and not the count of nonzero words.** The nonzero-word count is the finer measure and the corpus uses it where an element is diagonal. On a generic element the two differ sharply: fifteen words, four products. **The product count is the one quoted below**, because it is what "how far into the endomorphisms the generator sits" means; the word count is quoted where a generator's support is the point.

**The ladder, factor by factor.** Both entries that locate a generator are given: whether it is an element of the algebra, and its length.

| factor | in $\mathbb B$? | length | the words |
|---|---|---|---|
| central $\mathrm{U}(1)$ | **yes**, $\mathbb R(ie_t)$ | $1$ | $L_{e_t}R_{e_t}$ |
| $\mathrm{SU}(2)_L$ | no | $1$ | $L_{\vec e_a}R_{e_t}$, $a=x,y,z$ |
| $\mathrm{SU}(2)_R$ | no | $1$ | $L_{e_t}R_{\vec e_a}$ |
| $\mathrm{SU}(3)$ | no | $2$ on seven, $3$ on the Cartan direction $\operatorname{diag}(0,1,1,-2)$ | off-diagonal pairs of $B_V$, and the Cartan |
| $\mathrm{SU}(4)$ | no | $1$ on the six unscaled words; $2$ or $3$ on the other named generators (in the Gell-Mann basis, $2$ on thirteen and $3$ on two); $4$ generic | all fifteen |
| $B-L$ | no | $3$ | $i\sum_a L_{\vec e_a}R_{\vec e_a}$ |
| generic $\mathfrak{su}(4)$ element | no | $4$ | the bound, attained |

**The table is the argument, and it is an argument about addresses.** $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ is *not* in $\mathbb B$ — its generators are endomorphisms, which is what the old test got wrong even about the factors it thought it had passed. Only the central $\mathrm{U}(1)$ is in $\mathbb B$. **And $\mathrm{SU}(3)$ sits at length two, an address no worse than the diagonal phases'** — seven of its eight at two, the eighth at three. **The eighth is the concrete case of the limit stated above**: $\operatorname{diag}(0,1,1,-2)$ is $-\operatorname{diag}(0,1,-1,0)+2\operatorname{diag}(0,1,0,-1)$, a sum of two elements of length two, and its own length is three. The old test was not merely too strict; it was measuring the wrong space, and the only factor it passed is the one nobody disputes.

**The length is not a hierarchy, and this table must not be read as one.** A length belongs to a **named** generator and not to a group: $\mathfrak{su}(4)$ has a basis of fifteen elements of length one, so "the group $\mathrm{SU}(4)$ has length three" is not a statement, and neither is "colour is shorter than the leptoquarks". What the numbers record is how far each named generator — the one the physics identifies — sits from a single two-sided product. *Expressing Lie Algebras via Biquaternions*, §*The Third Sense: the Algebra as Endomorphisms*, states the limit and verifies it.

**What selects the group is the module, and this is where the frame's refusal of larger groups earns its keep.** The algebra supplies one four-dimensional complex module, its own carrier, so the largest compact simple group that can act faithfully on it is $\mathrm{SU}(4)$; $\mathrm{SU}(5)$ needs a five-dimensional module and $\mathrm{SO}(10)$ a sixteen-dimensional one, and the algebra supplies neither. **That is a statement about modules, and the length says only where the generators live.**

**What the criterion does not buy.** It grades the group's address in the endomorphisms; it does not make the theory chiral. **Chirality is a property of the module, and the endomorphisms of $\mathbb B$ supply no one-sided action** — no length, however short, produces a representation on which the group acts on one side only. **A reader who takes a short word as a chiral matter sector has read a fourth claim into the ladder.**

**The membership claim was corrected in this revision.** An earlier version of §*Why the Corpus Adopts the Pati–Salam Model* said that six of the twenty-one generators were elements of the algebra — a claim that was false, as the length ladder shows. The six sides are endomorphisms of length one, and their parameters are the imaginary units; only the central phase is in $\mathbb B$. Any article that quotes the old sentence should be read against the ladder.

## Why This Group and Not a Larger One

**Three competitors, and the corpus's reason for each refusal, stated in one line apiece.**

**$\mathrm{SU}(5)$.** Rank four, and its $\mathbf{10}+\bar{\mathbf5}$ has no $\nu_R$ and puts quarks and leptons in the same multiplet in a way the algebra's split does not suggest. **The corpus's $\mathfrak{su}(4)$ is the carrier's group; $\mathfrak{su}(5)$ would be a group with no carrier in the algebra at all.**

**$\mathrm{SO}(10)$.** Rank five, the same rank as $G_{PS}$, and it contains $G_{PS}$ — so it is the natural enlargement rather than a competitor. But its spinor is a $\mathbf{16}$ obtained by a Clifford algebra the corpus does not otherwise use, and **the rank-five coincidence is not an argument**: two rank-five groups contain one another for reasons of dimension, not of structure.

**$\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}$.** This is $G_{PS}$ after the $\mathrm{SU}(4)$ breaking, and it is the left–right model. **It is the honest alternative**: the difference is the six leptoquarks and the $\mathbb{CP}^{3}$ they generate, and the experiment that separates the two is a leptoquark search.

**The one-line reason the frame is $\mathrm{SU}(4)$ and not the left–right group.** The algebra's carrier is four-dimensional and its stabiliser is $\mathrm{SU}(3)$; **a three-colour group inside a four-dimensional carrier with one line removed is $\mathrm{SU}(4)$, not $\mathrm{SU}(3)\times\mathrm{U}(1)$.** Whether the fourth direction is gauged is the physics question, and the frame takes the answer that it is.

## The Carrier Is a Copy, and Here Is the Theorem

**The objection.** If $\mathrm{SU}(4)$ acts on the same four dimensions as the Lorentz action, the two must commute, and then colour must be inside the commutant of the Lorentz algebra.

**The computation.** Let $L_{\vec e_a}$ be left multiplication on $\mathbb C^4$ by the three imaginary units. Then

$$
\mathfrak{su}(4)\cap\bigl\{X:[X,L_{\vec e_a}]=0\ \text{for }a=x,y,z\bigr\}
=\operatorname{span}\{R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}\}\cong\mathfrak{su}(2),
\qquad \dim_{\mathbb R}=3 .
$$

**The proof, in three counts, because this is load-bearing and a sketch is not enough.**

**First, the commutant.** As a module for $L(\mathbb B)\cong M_2(\mathbb C)$, the carrier is two copies of the defining representation, $\mathbb C^4\cong\mathbb C^2\otimes\mathbb C^2$, with $L(\mathbb B)$ acting on the first factor only. By Schur's lemma the commutant is $\operatorname{End}_{\mathbb C}(\mathbb C^2)=M_2(\mathbb C)$, **complex dimension four, real dimension eight**, and that commutant is exactly $R(\mathbb B)$: right multiplications commute with left ones, and eight real dimensions is all there is.

**Second, Hermiticity inside it.** Of those eight dimensions, the anti-Hermitian part is four: $R_{\vec e_a}$ for $a=x,y,z$ (each anti-Hermitian, since $R_{\vec e_a}^{\dagger}=-R_{\vec e_a}$) together with $R_i=i\,\mathrm I_4$. The other four — $R_1=\mathrm I_4$ and $iR_{\vec e_a}$ — are Hermitian.

**Third, tracelessness.** $\operatorname{tr}R_i=4i\neq0$, so $R_i$ is excluded by $\operatorname{tr}X=0$. Each $R_{\vec e_a}$ is traceless, because the matrix of right multiplication by an imaginary unit is two copies of a traceless block. **What remains is exactly $\{R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}\}$, three real dimensions, and that is $\mathfrak{su}(2)$.**

So the count is $8\to4\to3$, each step a computation rather than a search, and the result is not a coincidence of the basis: **the two-sided product contributes a full $M_2(\mathbb C)$ to the commutant and the compact part of it is one $\mathfrak{su}(2)$.** The ceiling is three, and no choice of generators changes it.

**So the ceiling is $\mathrm{SU}(2)$, and the frame must be a tensor product.**

$$
(\text{internal }\mathbf 4)\otimes(\text{spinor}),
\qquad
\mathbf 4_{\text{int}}\cong\mathbb C e_t\oplus B_V ,
$$

where the internal quartet is a **formal copy** of the algebra's coordinate space: it inherits the split, because the split is canonical, and it does not inherit the Lorentz action, because it must not. **This is the same wall the corpus already knows from the chiral side**, met here from the colour side, and it is the same wall for the same reason: $M_4(\mathbb C)$ cannot host two large commuting compact groups.

**What this article therefore asserts, in one sentence.** *The frame is $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ acting on a formal copy of the carrier's quartet tensored with a spinor, and the copy is permitted by the canonical split and by nothing else.*

## The Chiral Wall, Restated for This Group

**The frame does not make the theory chiral, and no renaming will.** The algebra's product is two-sided; a chiral gauge theory needs an action that distinguishes left from right at the level of the *gauge* coupling. **In $G_{PS}$ that distinction is put in by the representation**: $\mathrm{SU}(2)_L$ acts on $(\mathbf4,\mathbf2,\mathbf1)$ and $\mathrm{SU}(2)_R$ on $(\bar{\mathbf4},\mathbf1,\mathbf2)$, and the assignment is a declaration, the fifth row of the table in *Where Each Factor Comes From*.

**What would count as the algebra supplying it.** A one-sided action of the algebra on a chiral spinor module — the corpus's open problem, unchanged. **What would be a fake solution, and is refused.** Writing the sixteen in a single multiplet of a larger group and calling the chirality derived, when the multiplet is real. **A real multiplet cannot be chiral**, and the sixteen is complex, which is why it works and why the algebra's own carrier, being self-conjugate, cannot supply it.

**The consequence for every article downstream.** The wall is quoted, not solved. [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$](quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html) says what the larger group moves and what it does not: one of three obstructions, and the one that moves is the dimension.

## The Checks

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
| the scalar count | $2(8+4)$ real components against $21-9$ broken generators | $12$ eaten, $12$ survive |
| the commutant ceiling | $\mathfrak{su}(4)\cap\operatorname{Comm}L(\mathbb H)$ | $\mathfrak{su}(2)$, $\dim 3$ |
| the sixteen Conway words are a basis of $\operatorname{End}_{\mathbb C}(\mathbb B)$ | rank of the $16\times16$ array of flattened words | $16$ |
| a single word is a rank-one product, so $\ell\le4$ | rank of every $4\times4$ coefficient array | never more than $4$ |
| the lengths of the ladder | the six rows of §*Where Each Factor Comes From* | $1$ on the central phase and the two sides, $2$ on seven of colour, $3$ on $B-L$ and on the eighth colour direction |
| the bound is attained | $300$ random $\mathfrak{su}(4)$ elements | $\ell=4$ on every draw |
| the six single words of $\mathfrak{su}(4)$ | $L_{e_t}R_{\vec e_a}$ and $L_{\vec e_a}R_{e_t}$, $a=x,y,z$ | $6$, and no other word qualifies |

## Summary

**The frame.** $G_{PS}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, $21=15+3+3$, rank $5$, one coupling at $M_{PS}$.

**The decompositions.** $15=8+1+6$; the sixteen $=(4,2,1)\oplus(\bar4,1,2)$; the eight of colour, the one that becomes $B-L$, the six leptoquarks.

**What is derived.** The two $SU(2)$'s from the two-sided action; the $\mathrm{SU}(4)$ from the carrier; the split $\mathbb C e_t\oplus B_V$, canonically.

**What is declared.** The identification of the split with the quark–lepton quartet (A); the chiral assignment; $g_3=g_L=g_R$ at the scale.

**The criterion.** A generator is an endomorphism of $\mathbb B$, measured by its length in the sixteen Conway words, $\ell=\operatorname{rank}c\le4$. **The old test — generators inside the algebra — is retired, and it is not merely too strict: it rejects the two-sided action along with colour.** On the ladder the two $\mathrm{SU}(2)$'s are length $1$ and colour is length $2$; the length addresses the named generators, it is not a grade of the group, and it buys no chirality.

**The ceiling.** $\mathfrak{su}(4)$ commutes with the Lorentz action only in $\mathfrak{su}(2)$; so the carrier is a formal copy, permitted by the split and by nothing else.

**The wall.** The frame does not make the theory chiral; the chirality is in the representation, and the representation is declared.

**The costs.** $21$ generators against $12$; twenty-four real scalars against four, of which twelve are eaten and twelve survive; a false prediction, $m_d=m_e$ at $M_{PS}$, whose repair needs a second bidoublet or a $(\mathbf{15},\mathbf2,\mathbf2)$; a second scale, $M_{PS}\gtrsim250$ TeV; and $\tfrac38$ as a boundary condition that does not run to $0.231$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $G_{PS}$ | $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, $21$ generators, rank $5$; the carrier stays $\mathbb C^4$, four complex dimensions |
| $T_{a}$ | the fifteen $\mathrm{SU}(4)$ generators, anti-Hermitian and traceless |
| $\tau_i$ | the three generators of each $\mathrm{SU}(2)$ |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the traceless diagonal of the $\mathrm{SU}(4)$; the abelian direction is $\mathbb R\,iD$ |
| $B-L$ | $-\tfrac13D$, the eigenvalues $(1,-\tfrac13,-\tfrac13,-\tfrac13)$ on the quartet |
| $T_{3L},T_{3R}$ | the two Cartan generators, one per $\mathrm{SU}(2)$ |
| $Y$ | $T_{3R}+\tfrac12(B-L)$, hypercharge as a combination |
| $g_4,g_L,g_R$ | the three couplings, equal at $M_{PS}$ |
| $M_{PS}$ | the $\mathrm{SU}(4)$ breaking scale, a parameter |
| $\mathfrak m$ | the six generators mixing $\mathbb C e_t$ with $B_V$, the leptoquark directions |
| $iD$ | $i\operatorname{diag}(-3,1,1,1)$, the diagonal generator of the $\mathrm{SU}(4)$ |
| $L_{\vec e_a},R_{\vec e_a}$ | left and right multiplication by the imaginary units |
| $\mathbf{16}$ | $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$, one family |
| (A) | the declaration that the fourth colour is the unit line |

## Further Reading

- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html). The general principle this frame is an instance of.
- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html). The connection, the curvature and the Yang–Mills action for a group of this size.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The ceiling on the algebra's own compact structure, which *Where Each Factor Comes From* and *The Carrier Is a Copy* meet again.
- [The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html). The two-sided action, before it is gauged.
- [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-in-the-biquaternion-framework-the-u2-ceiling-and-the-four-unbuilt-sectors.html). What the algebra's own action carries, and what it does not.
- [Grand Unification in the Biquaternion Framework: Where the Embedding Fails](grand-unification-in-the-biquaternion-framework-where-the-embedding-fails.html). The same ceiling read as a statement about unification, in both readings.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html). What the larger group moves of the colour obstruction and what it leaves standing.

**The traps, and each one is a place where a reader can be misled by a true sentence.**

**Do not read "the group of the carrier" as "the group acting on spacetime."** The two cannot be the same group, and the reason is a computation, not a preference: if $\mathrm{SU}(4)$ acted on the same four dimensions as the Lorentz action, it would have to sit in that action's commutant, and the compact part of the commutant is $\mathfrak{su}(2)$ of dimension three, not fifteen. **The tensor product is therefore forced**: an internal $\mathbf4$ tensored with a spinor, the internal factor being a formal copy of the carrier's quartet.

**Do not read the two $\mathrm{SU}(2)$'s as the Lorentz group.** They are gauged and internal: left and right multiplication by the imaginary units of the algebra, not the Lorentz action. **The Lorentz group does live in this framework, and it lives somewhere else** — it is the group of norm-preserving automorphisms of the algebra's Hermitian structure, the $SL(2,\mathbb C)$ acting on the spinor module. [The Lorentz Group as Biquaternion Norm Automorphisms](the-lorentz-group-as-biquaternion-norm-automorphisms.html) is where it is built, and the reader who wants to know which group is which should read that article beside this one. **Internal and spacetime factors are different factors of one tensor product; that is the whole architecture.**

**Do not read $g_3=g_L=g_R$ as a prediction at accessible energy.** It is a boundary condition at $M_{PS}$, and the one place where the boundary condition has been checked — the angle — fails.

**Do not read "the algebra supplies the two-sided action" as "the $\mathrm{SU}(2)$ generators are elements of $\mathbb B$."** The action is an endomorphism; its parameter is the element. **This is the Layer A / Layer B distinction again**: the algebra acts on its own carrier in Layer A, and the group acts on a formal copy in Layer B, and in neither layer is a generator of $\mathrm{SU}(2)$ an element of the algebra.

**Do not read the sixteen as evidence that the group is right.** It is evidence that the sixteen is the natural multiplet, and a natural multiplet is not a measurement. **The same multiplet appears in $\mathrm{SO}(10)$, which is how we know that a natural multiplet does not pick out a group.**
