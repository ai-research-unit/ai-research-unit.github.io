# __The Breaking Chain and the Boson Spectrum: One Flag, Three Scales, Twenty-One Bosons__

## Introduction

**The layer.** The chain is a statement about a group breaking on a formal copy of the carrier, and the spectrum is a property of the resulting broken phase. Its Layer-A content is arithmetic at one step only: the six generators that leave at $M_{C}$ are the directions that move the canonical line, and that is why they carry no rank.

**The question.** In what order does $G_{4LR}$ break, at what scales, by which vacuum directions, and what becomes of each of the twenty-one gauge bosons on the way down?

**The answer.**

$$
\boxed{\;
21=9+12,\qquad
9=\underbrace{8}_{\text{gluons}}+\underbrace{1}_{\gamma},
\qquad
12=\underbrace{6}_{\text{leptoquarks}}+\underbrace{2}_{W^{\pm}}+\underbrace{2}_{W_R^{\pm}}+\underbrace{1}_{Z}+\underbrace{1}_{Z_R}
\;}
$$

with the chain $21\to15\to12\to9$ in dimensions and $5\to5\to4\to3$ in rank, driven by one point of $\mathbb{CP}^{3}\times\mathbb{CP}^{1}\times\mathbb{CP}^{1}$, and with the photon emerging as the single null direction of a $3\times3$ neutral mass matrix whose ratios are exact.

**The single idea.** The chain is not three independent breakings. It is one object — a flag of three lines — and every step is the stabiliser of one line. Written that way the chain has no free choices left except the scales, and the scales are not tied to one another by anything this article states.

**What the article establishes.** That each step is a stabiliser; that the dimension and rank budgets close; that the massless count equals the dimension of the unbroken group at every stage; that the neutral sector is three-dimensional throughout, of rank two, with one null vector; that the three matching relations are exact and mutually consistent; and that the angle at the equal-coupling threshold is fixed by the generators while the running down to $M_{Z}$ is where the model's quantitative tension lies. The threshold statement itself — $g_4=g_L=g_R$ at one scale, and the number it fixes — is not in this article: it is in [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html), with its failure.

**Not established.** The three scales are not predicted. The minimal matter content does not run correctly: it fails, and the size and sign of the failure are in the coupling article. $M_{R}$ and $M_{C}$ are equal in the minimal case; splitting them needs a second field.

**Two meanings of "neutral".** Two counts are in play in this model and they are not the same. This article's three neutral states are gauge fields — $W^3_L$, $W^3_R$ and $B$, the fields that mix before the photon separates out. The scalar sector's two neutral states are real scalars, the $125$ GeV candidate and its heavier partner. Three gauge, two scalar, and neither count constrains the other; adding $3+2$ adds gauge bosons to scalars.

## The Flag, Which Is the Chain

**Three lines.** In three spaces, and the chain is the sequence of their stabilisers.

**1.1 The first line.** It is the unit line, and it lives in the carrier. $\mathbb C e_t\subset\mathbb C^4$ is the only line every automorphism fixes, and the fibre over which $B-L$ takes its largest value. Its stabiliser in $\mathrm{SU}(4)$ is $\mathrm{SU}(3)$, and its stabiliser in the whole frame is $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}$:

$$
\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb C e_t)=\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L},
\qquad
15\to 8+1 .
$$

**1.2 The second line.** It lives in the $SU(2)_R$ doublet. The vacuum that breaks $\mathrm{SU}(4)$ does it with a field in the $(\mathbf 4,\mathbf 1,\mathbf 2)$: one $SU(2)_R$ doublet, and the breaking of $SU(2)_R$ is the choice of one of its two components. A doublet has exactly one line up to phase, so there is nothing to choose:

$$
\mathrm{Stab}_{\mathrm{SU}(2)_R}(\text{a line})=\mathrm{U}(1)_R,
\qquad
3\to 1 .
$$

**1.3 The third line.** It lives in the $SU(2)_L$ doublet, and it is the electroweak one. Its stabiliser is $\mathrm{U}(1)_{\mathrm{em}}$:

$$
\mathrm{Stab}_{\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y}(\text{a line})=\mathrm{U}(1)_{\mathrm{em}},
\qquad
3+1\to 1 .
$$

**1.4 One object, not three.** The three lines are nested in the sense that matters: each is a line in the module of the unbroken factor of the previous step. The chain is therefore a point of

$$
\mathbb{CP}^{3}_{\ \text{(the carrier)}}\times\mathbb{CP}^{1}_{\ \text{(the }R\text{ doublet)}}\times\mathbb{CP}^{1}_{\ \text{(the }L\text{ doublet)}},
$$

and each factor of that product is a choice of vacuum, not a choice of group. The group is fixed; the vacuum is a point; the chain is the stabiliser of that point read off factor by factor. The word *flag* is used for that nesting of stabilisers and not for its geometric namesake: a geometric flag is a chain of subspaces of one vector space, and these three lines live in three different spaces, each a line in the module of the previous unbroken factor.

**Completeness.** Rank $5=3+1+1$ at the top; rank $2+1+1+1=5$ after the first step; $2+1+1=4$ after the second; $2+1=3$ at the bottom. One rank is lost at each of the last two steps and none at the first, and *Why the First Step Is Different* gives the reason.

## The Dimension Budget, Read Three Ways

**The three steps.**

| step | group before | group after | dim | lost | massless after | newly massive |
|---|---|---|---|---|---|---|
| $M_{C}$ | $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $21\to15$ | $6$ | $15$ | the six leptoquarks |
| $M_{R}$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ | $15\to12$ | $3$ | $12$ | $W_R^{\pm}$, $Z_R$ |
| $M_{W}$ | $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}$ | $12\to9$ | $3$ | $9$ | $W^{\pm}$, $Z$ |

**As masses.** Twelve of the twenty-one become massive, nine stay massless, and the nine are the eight gluons and the photon.

$$
6+3+3=12=21-9 .
$$

A frame that predicted any other total would be wrong before any dynamics were computed.

**As rank.** $5\to5\to4\to3$: the first step loses six dimensions and no rank, the second loses three and one, the third loses three and one. So each of the last two steps kills exactly one neutral boson and two charged ones: one neutral and one pair of $W$'s at $M_{R}$, one neutral and one pair at $M_{W}$.

**As a theorem.** This is the sense in which the count is not dynamics. The number of massless gauge bosons equals the dimension of the unbroken group, always, because the Higgs mechanism eats exactly one Goldstone per broken generator. The last row's massless count is $9=8+1$, and $8+1$ is $\dim\bigl(\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}\bigr)$. So $9+12$ is a statement about group dimensions, and it would be a scandal if it failed.

**Why the count matters.** Because the assignment is not a count: which six become massive at $M_{C}$, and which three at $M_{R}$, depends on which vacuum is chosen. A frame could have the right totals and the wrong rows — if a leptoquark stayed massless, colour would be broken and the chain would be a different chain. The rows of *The Twenty-One, Classified* are the content; the totals are the arithmetic check on them.

**The Goldstones.** Every massive state is one eaten real scalar, so the twelve massive states consume twelve of the scalar sector's twenty-four real numbers; the other twelve survive as scalars, and $12+12=24$ is [the scalar article](the-scalar-sector-and-the-leptoquark-bounds.html)'s count stated in this article's language. Grouped by broken generator the twelve are $6+2+4$ — six for the leptoquarks, two for the $W_R^{\pm}$, four for the $W^{\pm}$, the $Z$ and the $Z_R$ — and two of those four are neutral, because they are eaten by the $Z$ and the $Z_R$ and are not the scalar sector's two physical neutral states. Grouped by the scale at which each state becomes massive they are $6+3+3$, as in the table. The two groupings agree in total and differ only in where the $Z_R$ is placed, because its eigenvector mixes the $R$-doublet direction with $B-L$: its mass is counted at $M_{R}$, while its Goldstone comes out of the bidoublet.

## Why the First Step Is Different

**The structural fact.** The six that leave at $M_{C}$ are all charged, and that is worth stating.

**3.1 The off-diagonal block.** They are the off-diagonal block of the fifteen. The six generators mixing $\mathbb C e_t$ with the vector part carry $B-L=\pm\tfrac43$ and are $SU(2)_L\times SU(2)_R$ singlets, so

$$
Q=T_{3L}+T_{3R}+\tfrac12(B-L)=\pm\tfrac23 .
$$

They are the leptoquarks, and they are the only place in the whole chain where a coloured boson acquires a mass. The gluons never do, because $\mathrm{SU}(3)$ is a stabiliser at every scale.

**3.2 No rank.** A Cartan generator is diagonal, and a generator with $B-L=\pm\tfrac43$ is off-diagonal by construction — it moves the unit line into the vector part. So the first step is the only step that breaks a group without breaking a Cartan direction, and that is why rank is untouched while six bosons get mass.

**3.3 The neutral sector.** After the first step there are still three neutral gauge bosons in play — $W_L^3$, $W_R^3$, and the surviving $B-L$ field — and two of them must eventually become $Z$ and $Z_R$. The three neutral states are a consequence of the first step not touching the Cartan, which is why *Why Three Neutral States* is about them rather than about this step.

## The Twenty-One, Classified

**The full list.** Every gauge boson of the frame, with its representation under the groups that survive.

| state | count | $SU(3)$ | $Q$ | mass at tree level | scale |
|---|---|---|---|---|---|
| gluon $g$ | $8$ | $\mathbf 8$ | $0$ | $0$ | exact |
| photon $\gamma$ | $1$ | $\mathbf 1$ | $0$ | $0$ | exact |
| leptoquark $X$ | $6$ | $\mathbf 3+\bar{\mathbf 3}$ | $\pm\tfrac23$ | $\propto v_R^2$ | $M_{C}$ |
| $W^{\pm}$ | $2$ | $\mathbf 1$ | $\pm1$ | $\tfrac14g_L^2v^2$ | $M_{W}$ |
| $Z$ | $1$ | $\mathbf 1$ | $0$ | $\propto v^2$ | $M_{W}$ |
| $W_R^{\pm}$ | $2$ | $\mathbf 1$ | $\pm1$ | $\propto v_R^2$ | $M_{R}$ |
| $Z_R$ | $1$ | $\mathbf 1$ | $0$ | $\propto v_R^2$ | $M_{R}$ |

**Two zeros, two reasons.** The gluons are zero because $\mathrm{SU}(3)$ is a stabiliser at every scale — an unbroken non-abelian group. The photon is zero because $\mathrm{U}(1)_{\mathrm{em}}$ is the residual of the whole chain: it is the one combination of three fields that annihilates every vacuum of *The Flag, Which Is the Chain*, and that is a statement about eigenvectors, not about stabilisers.

**The only coloured massive states.** The six leptoquarks are the only coloured massive states in the theory. Colour is never broken, and the objects that carry colour and mass at once are exactly the six that mix the unit line with the vector part.

### The nine that fix the line, the six that move it

**A second sorting of the same fifteen, by what each generator does to the canonical line.** The line is $\mathbb C e_t$, and in the algebra's own form it is the time-like direction: the Krein norm is $\lvert Q_t\rvert^2-\lvert\vec Q\rvert^2$, signature $(1,3)$. Sorting the fifteen by their action on that line therefore sorts them by a signature the carrier already carries.

| action on $\mathbb C e_t$ | count | generators | class |
|---|---|---|---|
| annihilate it, $X e_t=0$ | $8$ | $\mathfrak{su}(3)$ | gluons |
| act on it as a phase | $1$ | $iD$ | $B-L$ |
| have a nonzero entry in row $0$ or column $0$, off the diagonal | $6$ | $\mathfrak m$ | leptoquarks |

$8+1+6=15$. The $8+1=9$ is the stabiliser of the split $\mathbb C e_t\oplus B_V$ and is a subgroup; the six are not, and that is the same statement as the first step losing dimension and no rank.

**The third row must be worded exactly, because the loose form is false.** Only three of the six take $e_t$ out of its line; the other three annihilate $e_t$ and bring a colour direction in. What all six share is a nonzero entry in row $0$ or column $0$, which is why they leave the *split* and not the *line*: the stabiliser of the line alone is the larger parabolic, of dimension $12=8+1+3$.

**The six split three and three, and the split is the $B-L$ grading.** With $D=\operatorname{diag}(3i,-i,-i,-i)$,

$$
[D,E_{0i}]=4i\,E_{0i},\qquad [D,E_{i0}]=-4i\,E_{i0},
$$

so three raise the line into a colour direction and three lower it back, carrying $B-L=\pm\tfrac43$ — the $\pm\tfrac23$ of the leptoquark charge once the $T_{3R}$ half is added. The $3+3$ is the particle–antiparticle pairing of the six, not a relabelling of one list.

**And the weak pair sits at forty-five degrees to both blocks.** Projecting $L_{\vec e_a}$ onto $\mathfrak m$ gives $\sqrt2$ against a total norm of $2$, and the projection of $R_{\vec e_a}$ onto $\mathfrak m$ is *the same vector*. Two consequences: $L_{\vec e_a}-R_{\vec e_a}$ carries no leptoquark part at all, so it is pure colour; and the six weak generators reach only a three-dimensional subspace of the six-dimensional $\mathfrak m$. A weak generator is not a colour direction plus a leptoquark direction — it is an equal mixture of the two.

> **Shape, not identity.** Leptoquarks and Lorentz boosts are both directions that mix the time line with a space line. That is a statement about the shape of these generators inside one matrix algebra, not a claim that leptoquarks are boosts. A boost is a spacetime transformation and the six are internal gauge directions. The four coordinates are read twice: once as time and space by the algebra's own form, and once as colour by the declaration (A).

**The charge check.** No charge is put in by hand.

$$
Q(X)=0+0+\tfrac12\cdot\tfrac43=+\tfrac23,
\qquad
Q(W^{\pm})=\pm1+0+0=\pm1,
\qquad
Q(\gamma)=0 .
$$

## Why Three Neutral States

**The dimension of the sector.** The neutral sector is three-dimensional before the first breaking, and it stays three-dimensional until the last.

**5.1 The counting.** Neutral gauge bosons are those with $Q=0$: $W_L^3$, $W_R^3$, and the $\mathrm{SU}(4)$ Cartan direction that survives the first breaking. The other two $\mathrm{SU}(4)$ Cartans are the gluon directions $T_3$ and $T_8$, which are neutral but are colour and never mix with anything, because colour is unbroken. So the mixing sector is exactly three fields:

$$
\{W^3_L,\ W^3_R,\ B\},\qquad B\equiv A^{15}.
$$

All three are gauge fields, and none of them is one of the scalar sector's neutral states.

**5.2 Why they mix.** Each of the two vacua is annihilated by a different combination. The first vacuum, along the unit line, is annihilated by $Y=T_{3R}+\tfrac12(B-L)$; the second, along the doublet direction, by $Q=T_{3L}+Y$. Two conditions on three fields leave exactly one direction, and that direction is the photon. That is the whole of the neutral sector in one sentence.

**5.3 The matrix.** With the two vacuum vectors $a_1,a_2\in\mathbb R^3$ written in the basis of couplings,

$$
\mathcal M^2=\sum_{i=1,2}v_i^2\,a_ia_i^{\mathsf T},
\qquad
a_1=\bigl(0,\tfrac12,-\sqrt{\tfrac38}\bigr)v_R,
\qquad
a_2=\bigl(\tfrac12,-\tfrac12,0\bigr)v ,
$$

where the entries are the eigenvalues of $(T_{3L},\,T_{3R},\,T^{15})$ on the field that takes the vev, with $T^{15}$ the Cartan normalised by $\operatorname{tr}(T^{15})^{2}=\tfrac12$ and hence $B-L=\sqrt{8/3}\,T^{15}$. So $a_1$ is the lepton line of the $(\mathbf4,\mathbf1,\mathbf2)$ — $T_{3R}=+\tfrac12$, $B-L=-1$, hence $T^{15}=-\sqrt{3/8}$ — and $a_2$ is the upper component of the bidoublet. Two annihilations fix the relative signs. Hypercharge is unbroken on the first vacuum, $Y=T_{3R}+\tfrac12(B-L)=0$, and both vacua must leave the photon massless, $Q=T_{3L}+T_{3R}+\tfrac12(B-L)$, which in this normalisation is the vector $(1,1,\sqrt{2/3})$: it gives $0+\tfrac12+\sqrt{2/3}\cdot(-\sqrt{3/8})=0$ on $a_1$ and $\tfrac12-\tfrac12+0=0$ on $a_2$. Only the products $a_ia_i^{\mathsf T}$ enter $\mathcal M^2$, so the overall sign of each $a_i$ is free; the relative signs are not, and the two tests above are what fixes them.

**5.4 The rank.** $\mathcal M^2$ is a sum of two rank-one matrices, so its rank is at most two, so it has at least one zero eigenvalue. It has exactly one, because $a_1$ and $a_2$ are independent: $a_1\cdot a_2=-\tfrac14v_Rv\ne0$ and they are not parallel. So there is one massless neutral and two massive, always, for any two independent neutral vacua. A frame with two neutral vacua and no massless neutral would violate this, and that is the structural reason the photon is not optional.

## The Photon, Which Is a Mixture and Not a Factor

**The object.** One object, reached from the mass matrix alone, because the mass matrix is geometry and the couplings are not.

**6.1 Not a gauge boson.** The unbroken abelian factor at the end of the chain is generated by $B$, the fifteenth $\mathrm{SU}(4)$ Cartan. The photon is not $B$. It is the combination of $W_L^3$, $W_R^3$ and $B$ that annihilates both neutral vacua, and its coefficients are the null vector of the neutral mass matrix:

$$
a_1\times a_2\ \propto\ -\bigl(\sqrt{\tfrac38},\ \sqrt{\tfrac38},\ \tfrac12\bigr)
\qquad\Longrightarrow\qquad
A_{\imath}\ \propto\ W^3_{L\imath}+W^3_{R\imath}+\sqrt{\tfrac23}\,B_{\imath} .
$$

The coefficients are $(1,\,1,\,\sqrt{2/3})$ up to the overall sign, which is free because a photon is a line. The $\sqrt{2/3}$ is a normalisation rather than a dynamical number. It is the fifteenth Cartan's eigenvalue on the unit line, and it is fixed by $\operatorname{tr}(T^{15})^2=\tfrac12$ — the same identity that makes the $B-L$ generator proportional to $(-1,\tfrac13,\tfrac13,\tfrac13)$.

**6.2 Geometry.** The two vacua annihilate two different combinations of the three neutral generators, so the requirement that one combination survives both gives one null direction. That is a rank statement about a sum of two rank-one matrices, and it holds for any couplings whatever: the mixing pattern is fixed, and only the numerical size of each coefficient depends on how strongly each field couples.

**6.3 What the article does not say.** It does not say what the couplings are, it does not evaluate the null vector at a particular point, and it does not state the angle that follows from it. The angle is in the coupling article, which is the only place in this category where the coefficient values are written. **The mixture itself has its own article**, [The Photon as the Unbroken Mixture](the-photon-as-the-unbroken-mixture.html), which derives the direction three ways and shows it to be the coefficient vector of $Q$.

## The Two Massive Neutrals

**Both eigenvalues.** Exactly, in the minimal vacuum.

**7.1 The light neutral.** It lands on the Standard Model relation.

$$
M_Z^2=\tfrac14\bigl(g_L^2+g_Y^2\bigr)v^2 .
$$

At equal couplings, with $g_Y^2=\tfrac35g^2$ from the matching relation, the predicted value is $\tfrac14(g_L^2+g_Y^2)v^2=\tfrac25g^2v^2$, and the light eigenvalue of $\mathcal M^2$ is $0.4\,g^2v^2$. The two are the same number, and that is the check: the normalisations entering $a_1$ and $a_2$ are consistent with the Standard Model's relation $M_Z^2=\tfrac14(g_L^2+g_Y^2)v^2$ and not merely with its group. The agreement is the leading term in $v/v_R$ — the eigenvalue is $0.3994\,g^2v^2$ at $v/v_R=10^{-1}$ — which is the sense in which the Standard Model is recovered below $M_{R}$, at tree level.

**7.2 The heavy neutral.** Its coefficient is $\tfrac58$.

$$
M_{Z_R}^2=\tfrac58\,g^2v_R^2 .
$$

The heavy eigenvalue at $v\to0$ is $0.625\,g^2v_R^2=\tfrac58g^2v_R^2$, and the $\tfrac58$ is nothing but $|a_1|^2=\tfrac14+\tfrac38$: one quarter from $T_{3R}$ and three eighths from the $B-L$ normalisation. At $v=0$ the matrix is rank one, so the other two eigenvalues vanish there: the $Z_R$ mass is entirely $M_{R}$'s, and the light neutral's comes entirely from $v$. The $Z_R$ is therefore heavier than the $W_R$ by the ratio of the two coefficients, $\sqrt{(5/8)/(1/4)}=\sqrt{5/2}\simeq1.58$ at equal couplings; with the couplings split the squared ratio is $1+\tfrac32(g_4/g_R)^2$, which carries $g_4/g_R$ and is the coupling article's business.

## The Coupling Statements and Where They Live

**One home.** The tree-level mass ratios with $g_L=g_R=g_4$ imposed, the three scales with their bounds, the three matching relations, and the running that shows the boundary condition failing are all coupling statements. This category keeps its coupling statements in one place, [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html).

**Why they are not restated here.** Each of the four carries a value that moves with a choice: the scale of the first breaking, the ratio $g_4/g_R$, the coefficient of the running. A moving value printed in a geometric article reads as though the geometry produced it, and the geometry does not. The chain fixes the count, the stabilisers, the dimension budget and the photon's composition. It fixes no number that a scale can change.

**What stays.** The photon's composition is a mixture with coefficients proportional to the couplings; the coefficients are carried symbolically, and the article never substitutes a value for them. The mixing is group theory, and the value of the mixing is the coupling article's business.

**The failure.** The equal-coupling condition implies two numbers at once, $\sin^2\theta_W=\tfrac38$ and $g_4=g_L$, and they are met four decades apart — $10^{13}$ GeV and $10^{17}$ GeV — so no single threshold satisfies both. That is the failure; *The Twenty-One, Classified* of the coupling article gives the arithmetic, and it is neither weakened here nor repeated.

## What Is Robust and What Is Not

**Four strengths.** They must not be blurred.

**9.1 The count.** $9$ massless, $12$ massive, and the identity massless $=\dim$(unbroken group). This holds for any vacuum, any scalar content, and any scale ordering. It is group theory.

**9.2 The photon's composition.** A mixture of $W_L^3$, $W_R^3$ and $B$ with coefficients proportional to the couplings. This holds whenever the three fields are present and two independent neutral vacua are chosen, and it does not depend on the scalar content. What the coefficients are is a coupling question, and it is not answered here.

**9.3 The list.** Six leptoquarks, two charged $W_R$, one $Z_R$, two light charged, one $Z$. The list follows from the count of *The Dimension Budget, Read Three Ways* and the groupings of *The Twenty-One, Classified*, and it survives any choice of vacuum. The ratios among those masses are not robust and are not stated here.

**9.4 The absolute scale.** $v_R$ is bounded from below by the leptoquark bound and from above by nothing in the frame. The spectrum's shape is predicted; its overall size is not.

**9.5 One loop.** These are tree-level relations. The $\rho$ parameter, the $Z$–$W$ mass ratio and the $Z_R$ mass all take radiative corrections, and in a model with a bidoublet the tree-level $\rho=1$ is an alignment statement rather than a theorem. [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html) owns that question, and this article does not pre-empt it.

## What the Chain and the Spectrum Establish

**Fixed, in five lines.**

Colour is a stabiliser at every scale, so it is never broken and never needs explaining.

Hypercharge is a combination, $Y=T_{3R}+\tfrac12(B-L)$, so it is not imported.

The chain's three steps are three stabilisers of three lines, so the vacuum is a point of a product of projective spaces and the group is fixed.

The dimension budget $21=9+12$ and the rank budget $5\to5\to4\to3$ are exact, and they are the model's cheapest tests.

The three sections of the particle category become three rows of one table. The strong section is the eight massless coloured states and why colour is a stabiliser. The electroweak section is the four states that get mass at $M_{W}$ and the mixing that produces them. The electromagnetic section is the one null direction and its composition. None of the three can be written without the other two.

**Not fixed, in five lines.**

The scales. $M_{C}$ and $M_{R}$ are parameters, bounded but not fixed.

The running of any coupling. It is in the coupling article, with the failure it produces.

The chiral assignment. The chain breaks a vector-like group; the chirality was declared before it, in the sixteen.

The scalar content. Which fields do the breaking is a choice, and the companion article counts what it requires.

The absolute size of the spectrum, and the ratios among its masses, which move with the scales.

## The Checks

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
| the light neutral | eigenvalue against $\tfrac14(g_L^2+g_Y^2)v^2$ with $g_Y^2=\tfrac35g^2$ | $0.4\,g^2v^2$ against $\tfrac25g^2v^2$, same number |
| the heavy neutral | eigenvalue at $v\to0$ | $0.625\,g^2v_R^2=\tfrac58g^2v_R^2$ |
| proton decay | three leptoquark vertices per unit $B$ | dimension nine, so no proton-decay bound |

## Distinctions That Are Easy to Lose

$M_{C}$ is not fixed by unification: nothing in this article fixes it, and the coupling article shows that the running does not either.

$\sin^{2}\theta_{W}=\tfrac38$ is a boundary condition, not a prediction of $0.2312$, and the coupling article records how it fails.

The three lines are not three independent choices: two of the three have nothing to choose, and the only genuine choice is the first.

"Proton decay does not bound it" does not mean "proton decay is absent": $B$ is violated, in thirds, and dimension-nine operators are there — they are simply unreachable.

The photon is not the $\mathrm{U}(1)$ boson: the $\mathrm{U}(1)$ boson is $B$, and the photon is the mixture that survives (*The Photon, Which Is a Mixture and Not a Factor*).

The count is not a dynamical achievement; it is $\dim G-\dim H$ and would be a scandal if it failed (*The Dimension Budget, Read Three Ways*).

$M_X=\sqrt2M_{W_R}$ is not a prediction: the $\sqrt2$ is the group's, and it is multiplied by $g_4/g_R$, which the group does not fix.

The three neutral states are not three scalars, and not two scalars and a gauge boson: all three are gauge fields, and the scalar sector's two neutral states are a separate object (Introduction, *Why Three Neutral States*).

## Summary

**The chain.** $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\to\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\to\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y\to\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}$.

**The object.** One point of $\mathbb{CP}^{3}\times\mathbb{CP}^{1}\times\mathbb{CP}^{1}$; three stabilisers; three lines; the group fixed.

**The budget.** $21\to15\to12\to9$ dimensions, $5\to5\to4\to3$ rank, $6+3+3=12$ massive and $9$ massless.

**The spectrum.** $21=9+12$: eight gluons and one photon massless; six leptoquarks, $W^{\pm}$, $Z$, $W_R^{\pm}$, $Z_R$ massive.

**The neutral sector.** Three fields $\{W_L^3,W_R^3,B\}$, a $3\times3$ mass matrix of rank two, one null direction, two massive.

**The photon.** $W_L^3+W_R^3+\sqrt{2/3}\,B$, the null direction of the neutral mass matrix. The $\sqrt{2/3}$ is the normalisation of the fifteenth Cartan, and it is the only coupling-adjacent number this article states.

**The masses.** Each is a coupling squared times a vacuum expectation value squared, with the coefficients given by the vacuum: $\tfrac14$ for the light charged pair and for the heavy charged pair, $\tfrac12$ for each leptoquark, and at equal couplings $\tfrac25$ for the $Z$ and $\tfrac58$ for the $Z_R$. The first three hold for any couplings; the last two move with $g_4/g_R$. The coefficients are structure; the couplings are not supplied here.

**The ratios.** $M_{W_R}/M_W=(g_R/g_L)(v_R/v)$: the ratio of the two vacua, times the coupling ratio that the chain does not fix. At equal couplings it reduces to $v_R/v$, and the ratios involving $g_4$ and $g_R$ are in the coupling article.

**The failure.** Recorded in the coupling article, in *The Twenty-One, Classified*.

**The strength.** The count and the photon's composition are robust; the ratios are conditional on the minimal vacuum; the overall scale is bounded only from below.

## Summary of Notation

| symbol | meaning |
|---|---|
| $M_{C}$ | the scale of $\mathrm{SU}(4)\to\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}$ |
| $M_{R}$ | the scale of $\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}\to\mathrm{U}(1)_Y$; $=M_{C}$ in the minimal frame |
| $M_{W}$ | the electroweak scale, measured |
| $T^{15}$ | the $\mathrm{SU}(4)$ Cartan generator proportional to $(-1,\tfrac13,\tfrac13,\tfrac13)$ |
| $q,t$ | the expansion coefficients of $Y$ in the basis $\{T^{15},T_{3R}\}$, $q^{2}=\tfrac23$, $t=1$ |
| $B$ | the surviving $\mathrm{SU}(4)$ Cartan field, $A^{15}$, the $B-L$ boson |
| $\mathcal M^2$ | the $3\times3$ neutral mass matrix, a sum of two rank-one terms |
| $a_1,a_2$ | the two vacuum vectors, the charges of the two vevs in the neutral basis $(T_{3L},T_{3R},B-L)$ |
| $X$ | a leptoquark, one of the six, charge $\pm\tfrac23$, colour triplet |
| $v,v_R$ | the electroweak and colour-breaking vacuum expectation values |
| $\rho$ | $M_W^2/(M_Z^2\cos^2\theta_W)$, $1$ at tree level in the alignment limit |
| $\mathbb{CP}^{3}\times\mathbb{CP}^{1}\times\mathbb{CP}^{1}$ | the vacuum manifold: the three lines of *The Flag, Which Is the Chain* |

## Further Reading

- [The Four Colours Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-four-colours-left-right-model.html). The group, the sixteen, the declaration (A) and the frame in which this chain runs.
- [Charge Quantisation from the Fourth Colour: One Trace, One Third, and Where the Twenty-One Generators Go](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). The trace that fixes the $B-L$ eigenvalues, and the ledger of where each of the twenty-one generators goes.
- [The Photon as the Unbroken Mixture: One Null Direction, Three Parents](the-photon-as-the-unbroken-mixture.html). *The Photon, Which Is a Mixture and Not a Factor*'s statement of the mixture in full: the three routes to the direction, why it is null, and the boundary against the coupling article.
- [The Scalar Sector and the Leptoquark Bounds](the-scalar-sector-and-the-leptoquark-bounds.html). Which fields do this breaking, how many real components they carry, and what their Goldstones require.
- [The $W$ and $Z$ Bosons in Biquaternionic Form](the-w-and-z-bosons-in-biquaternionic-form.html). The two light neutral and charged states, before this article mixes them.
- [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). The matching relations, the angle they produce, and the failure that follows.
- [The Weinberg Angle, the Neutral Current and the $Z$ Coupling](the-weinberg-angle-and-the-three-neutral-states.html). The angle as a ratio of two couplings.
- [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model](anomalies-and-anomaly-cancellation-in-the-four-colours-left-right-model.html). The four hypercharge conditions, which hold identically on the sixteen and are not restated here.
- [Custodial Symmetry and the $\rho$ Parameter in Biquaternionic Form](custodial-symmetry-and-the-rho-parameter.html). The tree-level relation $\rho=1$ that *What Is Robust and What Is Not* does not claim as a theorem.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html). Why colour is a stabiliser at every scale, which is the eight massless rows of *The Twenty-One, Classified*.
- [Grand Unification in the Biquaternion Framework: Where the Embedding Fails](grand-unification-in-the-biquaternion-framework-where-the-embedding-fails.html). The same chain read as an embedding, and the point at which it stops being one.
