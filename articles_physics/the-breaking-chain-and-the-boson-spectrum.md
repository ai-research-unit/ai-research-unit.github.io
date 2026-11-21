# __The Breaking Chain and the Boson Spectrum: One Flag, Three Scales, Twenty-One Bosons__

## Introduction

**The layer.** The chain is a statement about a group breaking on a formal copy of the carrier, and the spectrum is a property of the resulting broken phase. Their Layer-A content is arithmetic at one step only: the six generators that leave at $M_{C}$ are the directions that move the canonical line, and that is why they carry no rank.

**The question.** In what order does $G_{4LR}$ break, at what scales, by which vacuum directions, and what becomes of each of the twenty-one gauge bosons on the way down?

**The answer in one line.**

$$
\boxed{\;
21=9+12,\qquad
9=\underbrace{8}_{\text{gluons}}+\underbrace{1}_{\gamma},
\qquad
12=\underbrace{6}_{\text{leptoquarks}}+\underbrace{2}_{W^{\pm}}+\underbrace{2}_{W_R^{\pm}}+\underbrace{1}_{Z}+\underbrace{1}_{Z_R}
\;}
$$

with the chain $21\to15\to12\to9$ in dimensions and $5\to5\to4\to3$ in rank, driven by one point of $\mathbb{CP}^{3}\times\mathbb{CP}^{1}\times\mathbb{CP}^{1}$, and with the photon emerging as the single null direction of a $3\times3$ neutral mass matrix whose ratios are exact.

**The single idea.** The chain is **not** three independent breakings. It is one object — a flag of three lines — and every step is the stabiliser of one line. **Written that way the chain has no free choices left except the scales**, and the scales are not tied to one another by anything this article states.

**What is claimed.** That each step is a stabiliser; that the dimension and rank budgets close; that the massless count equals the dimension of the unbroken group at every stage; that the neutral sector is three-dimensional throughout, of rank two, with one null vector; that the three matching relations are exact and mutually consistent; and that the angle at the equal-coupling threshold is fixed by the generators while the running down to $M_{Z}$ is where the model's quantitative tension lives. **The threshold statement itself — $g_4=g_L=g_R$ at one scale, and the number it fixes — is not in this article**: it is in [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html), with its failure.

**What is not claimed.** That the three scales are predicted. That the minimal matter content runs correctly — **it does not, and the flagged coupling article says so with the sign and the size of the failure**. That $M_{R}$ and $M_{C}$ are different: the minimal case sets them equal, and splitting them needs a second field.

**A word on the word "neutral", because two counts are in play in this model and they are not the same.** This article's **three** neutral states are **gauge** fields — $W^3_L$, $W^3_R$ and $B$, the fields that mix before the photon separates out. The scalar sector's **two** neutral states are real scalars, the $125$ GeV candidate and its heavier partner. **Three gauge, two scalar, and neither count constrains the other.** A reader who adds $3+2$ has added gauge bosons to scalars.

## 1. The Flag, Which Is the Chain

**Three lines, in three spaces, and the chain is the sequence of their stabilisers.**

**1.1 The first line is the unit line, and it lives in the carrier.** $\mathbb C e_t\subset\mathbb C^4$ is the only line every automorphism fixes, and the fibre over which $B-L$ takes its largest value. **Its stabiliser in $\mathrm{SU}(4)$ is $\mathrm{SU}(3)$**, and its stabiliser in the whole frame is $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}$:

$$
\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb C e_t)=\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L},
\qquad
15\to 8+1 .
$$

**1.2 The second line lives in the $SU(2)_R$ doublet.** The vacuum that breaks $\mathrm{SU}(4)$ does it with a field in the $(\mathbf 4,\mathbf 1,\mathbf 2)$: one $SU(2)_R$ doublet, and the breaking of $SU(2)_R$ is the choice of one of its two components. **A doublet has exactly one line up to phase, so there is nothing to choose**:

$$
\mathrm{Stab}_{\mathrm{SU}(2)_R}(\text{a line})=\mathrm{U}(1)_R,
\qquad
3\to 1 .
$$

**1.3 The third line lives in the $SU(2)_L$ doublet**, and it is the electroweak one. Its stabiliser is $\mathrm{U}(1)_{\mathrm{em}}$:

$$
\mathrm{Stab}_{\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y}(\text{a line})=\mathrm{U}(1)_{\mathrm{em}},
\qquad
3+1\to 1 .
$$

**1.4 Why that is one object and not three.** The three lines are nested in the sense that matters: each is a line in the module of the *unbroken* factor of the previous step. **The chain is therefore a point of**

$$
\mathbb{CP}^{3}_{\ \text{(the carrier)}}\times\mathbb{CP}^{1}_{\ \text{(the }R\text{ doublet)}}\times\mathbb{CP}^{1}_{\ \text{(the }L\text{ doublet)}},
$$

and each factor of that product is a choice of vacuum, not a choice of group. **The group is fixed; the vacuum is a point; the chain is the stabiliser of that point read off factor by factor.**

**The check that the flag is complete.** Rank $5=3+1+1$ at the top; rank $2+1+1+1=5$ after the first step; $2+1+1=4$ after the second; $2+1=3$ at the bottom. **One rank is lost at each of the last two steps and none at the first**, and §3 gives the reason.

## 2. The Dimension Budget, Read Three Ways

**Each step, with what leaves and what it costs.**

| step | group before | group after | dim | lost | massless after | newly massive |
|---|---|---|---|---|---|---|
| $M_{C}$ | $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $21\to15$ | $6$ | $15$ | the six leptoquarks |
| $M_{R}$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ | $15\to12$ | $3$ | $12$ | $W_R^{\pm}$, $Z_R$ |
| $M_{W}$ | $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}$ | $12\to9$ | $3$ | $9$ | $W^{\pm}$, $Z$ |

**Read it as masses.** Twelve of the twenty-one become massive, nine stay massless, and the nine are the eight gluons and the photon.

$$
6+3+3=12=21-9 .
$$

**A frame that predicted any other total would be wrong before any dynamics were computed.**

**Read it as rank.** $5\to5\to4\to3$: the first step loses six dimensions and no rank, the second loses three and one, the third loses three and one. **So each of the last two steps kills exactly one neutral boson and two charged ones**: one neutral and one pair of $W$'s at $M_{R}$, one neutral and one pair at $M_{W}$.

**Read it as a theorem, and this is the sense in which the count is not dynamics.** The number of massless gauge bosons equals the dimension of the unbroken group, always, because the Higgs mechanism eats exactly one Goldstone per broken generator. The last row's massless count is $9=8+1$, and $8+1$ is $\dim\bigl(\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}\bigr)$. **So $9+12$ is a statement about group dimensions, and it would be a scandal if it failed.**

**Why the count is still worth writing down.** Because the *assignment* is not a count: which six become massive at $M_{C}$, and which three at $M_{R}$, depends on which vacuum is chosen. **A frame could have the right totals and the wrong rows** — if a leptoquark stayed massless, colour would be broken and the chain would be a different chain. The rows of §4 are the content; the totals are the arithmetic check on them.

**Where the twelve Goldstones come from, and the one place the groupings differ.** Every massive state is one eaten real scalar, so the twelve massive states consume twelve of the scalar sector's twenty-four real numbers; **the other twelve survive as scalars, and $12+12=24$ is the scalar article's count stated in this article's language.** Grouped by broken generator the twelve are $6+2+4$ — six for the leptoquarks, two for the $W_R^{\pm}$, four for the $W^{\pm}$, the $Z$ and the $Z_R$. Grouped by the scale at which each state becomes massive they are $6+3+3$, as in the table. **The two groupings agree in total and differ only in where the $Z_R$ is placed**, because its eigenvector mixes the $R$-doublet direction with $B-L$: its mass is counted at $M_{R}$, while its Goldstone comes out of the bidoublet.

## 3. Why the First Step Is Different

**The six that leave at $M_{C}$ are all charged, and that is a structural fact worth stating.**

**3.1 They are the off-diagonal block of the fifteen.** The six generators mixing $\mathbb C e_t$ with the vector part carry $B-L=\pm\tfrac43$ and are $SU(2)_L\times SU(2)_R$ singlets, so

$$
Q=T_{3L}+T_{3R}+\tfrac12(B-L)=\pm\tfrac23 .
$$

**They are the leptoquarks**, and they are the only place in the whole chain where a *coloured* boson acquires a mass. **The gluons never do**, because $\mathrm{SU}(3)$ is a stabiliser at every scale.

**3.2 They carry no rank.** A Cartan generator is diagonal, and a generator with $B-L=\pm\tfrac43$ is off-diagonal by construction — it moves the unit line into the vector part. **So the first step is the only step that breaks a group without breaking a Cartan direction**, and that is why rank is untouched while six bosons get mass.

**3.3 Consequence for the neutral sector.** After the first step there are still **three** neutral gauge bosons in play — $W_L^3$, $W_R^3$, and the surviving $B-L$ field — and two of them must eventually become $Z$ and $Z_R$. **The three neutral states are a consequence of the first step not touching the Cartan**, which is why §5 is about them rather than about this step.

## 4. The Twenty-One, Classified

**Every gauge boson of the frame, with its representation under the groups that survive.**

| state | count | $SU(3)$ | $Q$ | mass at tree level | scale |
|---|---|---|---|---|---|
| gluon $g$ | $8$ | $\mathbf 8$ | $0$ | $0$ | exact |
| photon $\gamma$ | $1$ | $\mathbf 1$ | $0$ | $0$ | exact |
| leptoquark $X$ | $6$ | $\mathbf 3+\bar{\mathbf 3}$ | $\pm\tfrac23$ | $\propto v_R^2$ | $M_{C}$ |
| $W^{\pm}$ | $2$ | $\mathbf 1$ | $\pm1$ | $\tfrac14g_L^2v^2$ | $M_{W}$ |
| $Z$ | $1$ | $\mathbf 1$ | $0$ | $\propto v^2$ | $M_{W}$ |
| $W_R^{\pm}$ | $2$ | $\mathbf 1$ | $\pm1$ | $\propto v_R^2$ | $M_{R}$ |
| $Z_R$ | $1$ | $\mathbf 1$ | $0$ | $\propto v_R^2$ | $M_{R}$ |

**The two zeros in the mass column are zero for different reasons.** The gluons are zero because $\mathrm{SU}(3)$ is a stabiliser at every scale — an unbroken non-abelian group. **The photon is zero because $\mathrm{U}(1)_{\mathrm{em}}$ is the residual of the *whole* chain** — it is the one combination of three fields that annihilates every vacuum of §1, and that is a statement about eigenvectors, not about stabilisers.

**The six leptoquarks are the only coloured massive states in the theory.** Colour is never broken, and the objects that carry colour and mass at once are exactly the six that mix the unit line with the vector part.

**The charge column is the check, and no charge is put in by hand.**

$$
Q(X)=0+0+\tfrac12\cdot\tfrac43=+\tfrac23,
\qquad
Q(W^{\pm})=\pm1+0+0=\pm1,
\qquad
Q(\gamma)=0 .
$$

## 5. Why Three Neutral States

**The neutral sector is three-dimensional before the first breaking, and it stays three-dimensional until the last.**

**5.1 The counting.** Neutral gauge bosons are those with $Q=0$: $W_L^3$, $W_R^3$, and the $\mathrm{SU}(4)$ Cartan direction that survives the first breaking. **The other two $\mathrm{SU}(4)$ Cartans are the gluon directions $T_3$ and $T_8$**, which are neutral but are colour and never mix with anything, because colour is unbroken. **So the mixing sector is exactly three fields:**

$$
\{W^3_L,\ W^3_R,\ B\},\qquad B\equiv A^{15}.
$$

**All three are gauge fields, and none of them is one of the scalar sector's neutral states.**

**5.2 Why they mix at all.** Each of the two vacua is annihilated by a different combination. The first vacuum, along the unit line, is annihilated by $Y=T_{3R}+\tfrac12(B-L)$; the second, along the doublet direction, by $Q=T_{3L}+Y$. **Two conditions on three fields leave exactly one direction**, and that direction is the photon. **This is the whole of the neutral sector in one sentence.**

**5.3 The matrix.** With the two vacuum vectors $a_1,a_2\in\mathbb R^3$ written in the basis of couplings,

$$
\mathcal M^2=\sum_{i=1,2}v_i^2\,a_ia_i^{\mathsf T},
\qquad
a_1=\bigl(0,-\tfrac12,\sqrt{\tfrac38}\bigr)v_R,
\qquad
a_2=\bigl(\tfrac12,-\tfrac12,0\bigr)v ,
$$

where the entries are $(q_L,\,q_R,\,q_{15})$ in units of the three couplings, and the $B-L$ generator is normalised so that its eigenvalue on the unit line is $\sqrt{\tfrac38}$.

**5.4 The rank, and the theorem it is an instance of.** $\mathcal M^2$ is a sum of **two** rank-one matrices, so its rank is at most two, so it has at least one zero eigenvalue. **It has exactly one**, because $a_1$ and $a_2$ are independent: $a_1\cdot a_2=\tfrac14v_Rv\ne0$ and they are not parallel. **So: one massless neutral, two massive — always, for any two independent neutral vacua.** A frame with two neutral vacua and no massless neutral would violate this, and that is the structural reason the photon is not optional.

## 6. The Photon, Which Is a Mixture and Not a Factor

**One object, reached from the mass matrix alone, because the mass matrix is geometry and the couplings are not.**

**6.1 The field is not a gauge boson.** The unbroken abelian factor at the end of the chain is generated by $B$, the fifteenth $\mathrm{SU}(4)$ Cartan. **The photon is not $B$.** It is the combination of $W_L^3$, $W_R^3$ and $B$ that annihilates both neutral vacua, and its coefficients are the null vector of the neutral mass matrix:

$$
a_1\times a_2\ \propto\ \bigl(\sqrt{\tfrac38},\ \sqrt{\tfrac38},\ \tfrac12\bigr)
\qquad\Longrightarrow\qquad
A_\mu\ \propto\ W^3_{L\mu}+W^3_{R\mu}+\sqrt{\tfrac23}\,B_\mu .
$$

**The coefficients are $(1,\,1,\,\sqrt{2/3})$, and the $\sqrt{2/3}$ is a normalisation rather than a dynamical number.** It is the fifteenth Cartan's eigenvalue on the unit line, and it is fixed by $\operatorname{tr}(T^{15})^2=\tfrac12$ — the same identity that makes the $B-L$ generator proportional to $(1,-\tfrac13,-\tfrac13,-\tfrac13)$.

**6.2 Why the mixing is geometry.** The two vacua annihilate two different combinations of the three neutral generators, so the requirement that one combination survives both gives one null direction. **That is a rank statement about a sum of two rank-one matrices, and it holds for any couplings whatever** — the mixing pattern is fixed, and only the numerical size of each coefficient depends on how strongly each field couples.

**6.3 What the article therefore does not say.** It does not say what the couplings are, it does not evaluate the null vector at a particular point, and it does not state the angle that follows from it. **A reader who wants the angle will find it in the flagged coupling article**, which is the only place in this category where the coefficient values are written.

## 7. The Two Massive Neutrals

**Both eigenvalues, exactly, in the minimal vacuum.**

**7.1 The light one is the Standard Model $Z$, and it lands on the Standard Model relation.**

$$
M_Z^2=\tfrac14\bigl(g_L^2+g_Y^2\bigr)v^2 .
$$

**Verified**: at equal couplings the light eigenvalue of $\mathcal M^2$ is $0.4\,v^2$ against the predicted $\tfrac25\,v^2$. **So the frame reproduces the Standard Model's neutral mass structures relation, not merely its group.**

**7.2 The heavy one is $Z_R$, and its coefficient is $\tfrac58$.**

$$
M_{Z_R}^2=\tfrac58\,g^2v_R^2 .
$$

**Verified**: the heavy eigenvalue at $v\to0$ is $0.625\,g^2v_R^2=\tfrac58g^2v_R^2$, and the $\tfrac58$ is nothing but $|a_1|^2=\tfrac14+\tfrac38$: one quarter from $T_{3R}$ and three eighths from the $B-L$ normalisation. **The result is that the $Z_R$ is heavier than the $W_R$ by a fixed factor**, which §8 states.

## 8. The Coupling Block, Which Is Not Here

**Four things used to stand between §7 and §9 of this article, and all four are gone from it.** They are the tree-level mass ratios with $g_L=g_R=g_4$ imposed; the three scales with their bounds; the three matching relations; and the running that shows the boundary condition failing. **Every one of them is a coupling statement, and this category keeps its coupling statements in one flagged place**, [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html).

**Why they were removed rather than rewritten.** Each of the four carries a value that moves with a choice: the scale of the first breaking, the ratio $g_4/g_R$, the coefficient of the running. **A moving value printed in a geometric article reads as though the geometry produced it, and the geometry does not.** The chain fixes the count, the stabilisers, the dimension budget and the photon's composition. **It fixes no number that a scale can change.**

**What remains here, and why it is not a coupling statement.** The photon's composition is a mixture with coefficients *proportional to the couplings*; the coefficients are carried symbolically, and the article never substitutes a value for them. **That is the whole difference: the mixing is group theory, and the value of the mixing is the flagged article's business.**

**The one thing a reader should carry away from the deletion.** The statement that the minimal frame fails is *not* withdrawn — it is relocated, with its arithmetic, to §4 of the flagged article. **A reader who wants the failure will find it there, dated and computed. A reader who wants the chain will not trip over it.**

## 9. What Is Robust and What Is Not

**Four claims of very different strength, and they must not be blurred.**

**9.1 Robust: the count.** $9$ massless, $12$ massive, and the identity massless $=\dim$(unbroken group). **This holds for any vacuum, any scalar content, and any scale ordering.** It is group theory.

**9.2 Robust: the photon's composition.** A mixture of $W_L^3$, $W_R^3$ and $B$ with coefficients proportional to the couplings. **This holds whenever the three fields are present and two independent neutral vacua are chosen**, and it does not depend on the scalar content. **What the coefficients are is a coupling question, and it is not answered here.**

**9.3 Robust: the shape of the spectrum, as a list.** Six leptoquarks, two charged $W_R$, one $Z_R$, two light charged, one $Z$. **The list follows from the count of §2 and the groupings of §4, and it survives any choice of vacuum.** **The ratios among those masses are not robust and are not stated here.**

**9.4 Not robust at all: the absolute scale.** $v_R$ is bounded from below by the leptoquark bound and from above by nothing in the frame. **The spectrum's shape is predicted; its overall size is not.**

**9.5 And one loop changes all of it.** These are tree-level relations. The $\rho$ parameter, the $Z$–$W$ mass ratio and the $Z_R$ mass all take radiative corrections, and in a model with a bidoublet the tree-level $\rho=1$ is an alignment statement rather than a theorem. [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html) owns that question, and this article does not pre-empt it.

## 10. What the Chain and the Spectrum Buy

**Bought, in five lines.**

Colour is a stabiliser at every scale, so it is never broken and never needs explaining.

Hypercharge is a combination, $Y=T_{3R}+\tfrac12(B-L)$, so it is not imported.

The chain's three steps are three stabilisers of three lines, so the vacuum is a point of a product of projective spaces and the group is fixed.

The dimension budget $21=9+12$ and the rank budget $5\to5\to4\to3$ are exact, and they are the model's cheapest tests.

The three sections of the particle category become three rows of one table. **The strong section is the eight massless coloured states and why colour is a stabiliser. The electroweak section is the four states that get mass at $M_{W}$ and the mixing that produces them. The electromagnetic section is the one null direction and its composition.** None of the three can be written without the other two.

**Not bought, in five lines.**

The scales. $M_{C}$ and $M_{R}$ are parameters, bounded but not fixed.

The running of any coupling. Removed to the flagged coupling article, with the failure it produces.

The chiral assignment. The chain breaks a vector-like group; the chirality was declared before it, in the sixteen.

The scalar content. Which fields do the breaking is a choice, and the companion article prices it.

The absolute size of the spectrum, and the ratios among its masses, which move with the scales.

## 11. The Checks

| claim | check | result |
|---|---|---|
| dimensions | $21\to15\to12\to9$ | $15=8+3+3+1$; $12=8+3+1$; $9=8+1$ |
| the budget | $6+3+3$ | $12=21-9$ |
| ranks | $5\to5\to4\to3$ | $3{+}1{+}1$; $2{+}1{+}1{+}1$; $2{+}1{+}1$; $2{+}1$ |
| the total | $8+1+6+2+1+2+1$ | $21$ |
| the massless count | $8$ gluons $+$ photon | $9=\dim(\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}})$ |
| the massive count | $6+2+2+1+1$ | $12=21-9$ |
| the eaten Goldstones | $12$ of the scalar sector's $24$ real components | $12$ eaten $+$ $12$ survive $=24$ |
| the two groupings | $6+2+4$ by generator against $6+3+3$ by mass scale | both $12$; they differ at the $Z_R$ |
| the leptoquark charge | $0+0+\tfrac12\cdot\tfrac43$ | $\pm\tfrac23$ |
| the neutral fields | $\{W_L^3,W_R^3,B\}$ against the scalar sector's two | three gauge, two scalar, different objects |
| the neutral rank | sum of two rank-one matrices | $2$, so one zero eigenvalue |
| the photon ratios | null vector of $\mathcal M^2$ | $(1,1,0.816497)$ against $(1,1,\sqrt{2/3})$ |
| the light neutral | eigenvalue against $\tfrac14(1+\tfrac35)v^2$ | $0.4v^2$ against $0.4v^2$ |
| the heavy neutral | eigenvalue at $v\to0$ | $0.625\,g^2v_R^2=\tfrac58$ |
| proton decay | three leptoquark vertices per unit $B$ | dimension nine, so no proton-decay bound |

## Summary

**The chain.** $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\to\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\to\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y\to\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}$.

**The object.** One point of $\mathbb{CP}^{3}\times\mathbb{CP}^{1}\times\mathbb{CP}^{1}$; three stabilisers; three lines; the group fixed.

**The budget.** $21\to15\to12\to9$ dimensions, $5\to5\to4\to3$ rank, $6+3+3=12$ massive and $9$ massless.

**The spectrum.** $21=9+12$: eight gluons and one photon massless; six leptoquarks, $W^{\pm}$, $Z$, $W_R^{\pm}$, $Z_R$ massive.

**The neutral sector.** Three fields $\{W_L^3,W_R^3,B\}$, a $3\times3$ mass matrix of rank two, one null direction, two massive.

**The photon.** $W_L^3+W_R^3+\sqrt{2/3}\,B$, the null direction of the neutral mass matrix. **The $\sqrt{2/3}$ is the normalisation of the fifteenth Cartan, and it is the only coupling-adjacent number this article states.**

**The masses.** Each is a coupling squared times a vacuum expectation value squared, with the coefficients given by the vacuum: $\tfrac14$ for the light charged pair, $\tfrac14$ and $\tfrac58$ for the two heavy neutrals, $\tfrac12$ for the leptoquark. **The coefficients are structure; the couplings are not supplied here.**

**The ratios.** $M_{W_R}/M_W=v_R/v$, which is the ratio of the two vacua and carries no coupling. **The ratios involving $g_4$ and $g_R$ are in the flagged coupling article.**



**The failure.** Recorded in the flagged coupling article, not hidden and not here.

**The strength.** The count and the photon's composition are robust; the ratios are conditional on the minimal vacuum; the overall scale is bounded only from below.

## Summary of Notation

| symbol | meaning |
|---|---|
| $M_{C}$ | the scale of $\mathrm{SU}(4)\to\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}$ |
| $M_{R}$ | the scale of $\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}\to\mathrm{U}(1)_Y$; $=M_{C}$ in the minimal frame |
| $M_{W}$ | the electroweak scale, measured |
| $T^{15}$ | the $\mathrm{SU}(4)$ Cartan generator proportional to $(1,-\tfrac13,-\tfrac13,-\tfrac13)$ |
| $q,t$ | the expansion coefficients of $Y$ in the basis $\{T^{15},T_{3R}\}$, $q^{2}=\tfrac23$, $t=1$ |
| $B$ | the surviving $\mathrm{SU}(4)$ Cartan field, $A^{15}$, the $B-L$ boson |
| $\mathcal M^2$ | the $3\times3$ neutral mass matrix, a sum of two rank-one terms |
| $a_1,a_2$ | the two vacuum vectors in the neutral basis, in units of the couplings |
| $X$ | a leptoquark, one of the six, charge $\pm\tfrac23$, colour triplet |
| $v,v_R$ | the electroweak and colour-breaking vacuum expectation values |
| $\rho$ | $M_W^2/(M_Z^2\cos^2\theta_W)$, $1$ at tree level in the alignment limit |
| $\mathbb{CP}^{3}\times\mathbb{CP}^{1}\times\mathbb{CP}^{1}$ | the vacuum manifold: the three lines of §1 |

## Further Reading

- [The Fourth-Colour Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-fourth-colour-left-right-model.html). The group, the sixteen, the declaration (A) and the frame in which this chain runs.
- [The Scalar Sector and the Leptoquark Bounds](the-scalar-sector-and-the-leptoquark-bounds.html). Which fields do this breaking, how many real components they carry, and what their Goldstones cost.
- [The $W$ and $Z$ Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html). The two light neutral and charged states, before this article mixes them.
- [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). The matching relations this article used to derive, the angle they produce, and the failure that follows.
- [The Weinberg Angle, the Neutral Current and the $Z$ Coupling](the-weinberg-angle-the-neutral-current-and-the-z-coupling.html). The angle as a ratio of two couplings; **it stands inside the flagged section, beside the article above**.
- [Custodial Symmetry and the $\rho$ Parameter in Biquaternionic Form](custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html). The tree-level relation $\rho=1$ that §9.5 refuses to claim as a theorem.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html). Why colour is a stabiliser at every scale, which is the eight massless rows of §4.
- [Grand Unification in the Biquaternion Framework: Where the Embedding Fails](grand-unification-in-the-biquaternion-framework-where-the-embedding-fails.html). The same chain read as an embedding, and the point at which it stops being one.

**The traps.** Do not read $M_{C}$ as fixed by unification: nothing in this article fixes it, and the flagged coupling article shows that the running does not either. Do not read $\sin^{2}\theta_{W}=\tfrac38$ as a prediction of $0.2312$; it is a boundary condition, and the flagged article records how it fails. Do not read the three lines as three independent choices: two of the three have nothing to choose, and the only genuine choice is the first. Do not read "proton decay does not bound it" as "proton decay is absent": $B$ is violated, in thirds, and dimension-nine operators are there — they are simply unreachable. Do not read "the photon is the $U(1)$ boson": the $U(1)$ boson is $B$, and the photon is the mixture that survives — §6. Do not read the count as a dynamical achievement; it is $\dim G-\dim H$ and would be a scandal if it failed — §2. Do not read $M_X=\sqrt2M_{W_R}$ as a prediction: the $\sqrt2$ is the group's, and it is multiplied by $g_4/g_R$, which the group does not fix. **Do not read "three neutral states" as three scalars, or as two scalars and a gauge boson: all three are gauge fields, and the scalar sector's two neutral states are a separate object** — the Introduction and §5.1.
