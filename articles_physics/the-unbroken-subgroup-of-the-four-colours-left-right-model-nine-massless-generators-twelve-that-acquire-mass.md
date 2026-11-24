# __The Unbroken Subgroup of the Four Colours Left–Right Model: Nine Massless Generators, Twelve That Acquire Mass__

## Introduction

**The question.** When the vacuum of the Four Colours Left–Right Model is chosen, which of the twenty-one gauge generators survive it, which acquire mass, and why is the split $9+12$ a statement of group theory rather than of any coupling?

**The answer.**

$$
\boxed{\;
\left|\mathrm{Stab}_{G_{4LR}}(\text{vacuum})\right|=9,
\qquad
21=9+12,
\qquad
\underbrace{8+1}_{9\ \text{massless}}+\underbrace{6+2+2+1+1}_{12\ \text{massive}}=21 .
\;}
$$

The nine are the eight gluons and the photon. The twelve are six leptoquarks, $W^{\pm}_{L}$, $W^{\pm}_{R}$, the $Z$ and the $Z_R$.

**The single idea.** A gauge field is massless exactly when its generator annihilates the vacuum. That is not a dynamical statement and it is not approximate: the gauge mass matrix is bilinear in $[X,\Phi_0]$, so every generator in the stabiliser of $\Phi_0$ gives a zero row and a zero column, and no generator outside it does. The massless count is therefore the dimension of one subgroup, fixed before a Lagrangian is written.

**What the article establishes.** The definition of the unbroken subgroup; the mass matrix formula and the proof that its kernel is the stabiliser; the two lists of nine and twelve with the mass coefficient each carries; the count at each of the three stages of the chain; and what masslessness means above and below a threshold.

**What the article does not establish.** No mass value. Every mass below is a coupling squared times a vacuum squared, with the coupling symbolic. The coefficients — $\tfrac14$, $\tfrac12$, $\tfrac58$ — come from the vacuum and are the group's; the couplings are not. Which values the couplings take is [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html).

**Where the spectrum is.** The cells, the names in the cells and the neutral mixing are [Classification of the Bosons in the Four Colours Left–Right Model: Twenty-Four Cells, Twenty-One Generators, Nine Massless and Twelve Massive](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html). The chain that produces the vacuum is [The Breaking Chain of the Four Colours Left–Right Model: One Flag, Three Stabilisers, Three Scales](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html). This article owns only the stabiliser and its dimension.

## The Stabiliser, Which Is the Answer

**One subgroup decides everything.** The vacuum is a set of scalar values; the gauge group acts on them; the subgroup that leaves them fixed is the unbroken group.

**1.1 The definition.** Let $\Phi_0$ be the vacuum value of the scalar content, and let $G_{4LR}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$. Then

$$
H=\mathrm{Stab}_{G_{4LR}}(\Phi_0)=\{g\in G_{4LR}:\ g\cdot\Phi_0=\Phi_0\},
\qquad
\mathfrak h=\mathrm{Lie}(H).
$$

**1.2 The mass matrix.** For a gauge generator $X$ acting on the scalar multiplet in the representation $R$,

$$
M^2_{XY}=\operatorname{tr}\left([X,\Phi_0]^\dagger\,[Y,\Phi_0]\right),
$$

the trace taken over the scalar's components, the sum running over every scalar that takes a vacuum value. This is the gauge-field mass term of the Lagrangian after the shift $\Phi=\Phi_0+\varphi$, written in the basis of generators rather than in the basis of fields.

**The same matrix as the array articles.** [The AXF Matrices of the Twenty-One Generators: Fifteen for $\mathfrak{su}(4)$, Three for $\mathfrak{su}(2)_L$, Three for $\mathfrak{su}(2)_R$](the-axf-matrices-of-the-twenty-one-generators.html) and [The Adjoint Mass Matrix of the Fifteen: One Number per Plane, $32v^2$ on Six and Zero on Nine](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html) write $\Phi_0=vD$ with $D=\operatorname{diag}(-3,1,1,1)$ and use this same formula. The two differ only in the normalisation of the vacuum array, which rescales every entry of $M^{2}$ by one constant; the zero entries, the ranks and the counts are the same.

**1.3 The kernel is the stabiliser.** If $X\in\mathfrak h$ then $X\Phi_0=0$ by definition, so $[X,\Phi_0]=0$, so the whole row $M^2_{X\cdot}$ and the whole column $M^2_{\cdot X}$ vanish. Conversely a vanishing row means $[X,\Phi_0]=0$, which means $X$ annihilates the vacuum. Hence

$$
\ker M^2=\mathfrak h,
\qquad
\#\{\text{massless gauge fields}\}=\dim\mathfrak h .
$$

**1.4 What the identity is not.** It is not a prediction of $\dim\mathfrak h$ from dynamics. It is a restatement: whoever chooses the vacuum chooses the stabiliser, and the stabiliser *is* the massless count. The content of the identity is that no other generator can be massless and no stabiliser direction can be massive, at tree level, in any gauge, with any normalisation.

## The Nine

**The unbroken subgroup and its generators.** Nine dimensions, and every one of them annihilates the vacuum.

**2.1 The subgroup.** At the bottom of the chain,

$$
H_3=\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}},
\qquad
\dim H_3=8+1=9 .
$$

**2.2 The list.**

| boson | number | generator | why massless |
|---|---|---|---|
| gluons $G^{a}$ | $8$ | $\mathfrak{su}(3)$ on $\mathbb C^3\subset\mathbb C^4$ | colour is unbroken at every scale |
| photon $\gamma$ | $1$ | the null combination of $W^3_L$, $W^3_R$, $B$ | it is the one direction that annihilates both vevs |

**2.3 The photon is a direction, not a factor.** None of the three neutral generators is massless on its own. $W^3_L$ is broken at $M_W$, $W^3_R$ at $M_R$, and $B$ at $M_R$. The photon is the one linear combination left in the kernel of the two-by-two neutral block, and its existence is the statement that the block has rank two. The eigenvector, its normalisation and the angle that names it are in [The Photon as the Unbroken Mixture: One Null Direction, Three Parents](the-photon-as-the-unbroken-mixture.html) and [The Weinberg Angle and the Three Neutral States: One Mixture, Three Denominators](the-weinberg-angle-and-the-three-neutral-states.html).

**2.4 Why colour is the exception.** Colour survives every step because no scalar in the minimal content carries a colour index that the vacuum could use: $\Phi$ is a $\mathbf 4$ and the vacuum sits on its singlet component, and $H$ is colour-blind. A vacuum that pointed into the triplet would break colour, and no field in the minimal sector does.

## The Twelve

**The complement.** Twelve dimensions of the algebra, and each maps to one massive state.

**3.1 The list.** Every mass is a coefficient times a coupling squared times a vacuum squared. The last column names the vacuum, not the threshold: in the minimal content the two colour-breaking masses share $v_R$ and therefore one threshold.

| states | number | generator | mass | vev |
|---|---|---|---|---|
| leptoquarks $X^{r},X^{g},X^{b}$ and conjugates | $6$ | the mixed cells $\{t,a\}$ of $\mathrm{SU}(4)$ | $\tfrac12 g_4^2 v_R^2$ each | $v_R$ |
| $W^{\pm}_{R}$ | $2$ | the two off-diagonal $\mathrm{SU}(2)_R$ generators | $\tfrac14 g_R^2 v_R^2$ | $v_R$ |
| $W^{\pm}_{L}$ | $2$ | the two off-diagonal $\mathrm{SU}(2)_L$ generators | $\tfrac14 g_L^2 v^2$ | $v$ |
| $Z$ | $1$ | the heavy neutral combination at $v$ | $\tfrac14(g_L^2+g_Y^2)v^2$ | $v$ |
| $Z_R$ | $1$ | the heavy neutral combination at $v_R$ | $\tfrac14 g_R^2 v_R^2+\tfrac38 g_4^2 v_R^2$ | $v_R$ |

**3.2 The count.** $6+2+2+1+1=12$. The first step loses six; the second and third lose three each, and they lose them by the same arithmetic, four generators replaced by one:

$$
\mathfrak{su}(2)_R\oplus\mathfrak u(1)_{B-L}\longrightarrow\mathfrak u(1)_Y,
\qquad
\mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y\longrightarrow\mathfrak u(1)_{\mathrm{em}},
$$

each a drop of $(3+1)-1=3$. In each case the three massive states are two charged bosons and one neutral mixture.

**3.3 The leptoquarks are six and not three.** The mixed block $\{t,a\}$ of the $4\times4$ matrix is three complex entries, and a complex entry with its conjugate is two real directions, so six. That six is the sextet of [The Leptoquarks of the Four Colours Left–Right Model: Six States, One Bound, and Why Proton Decay Does Not Bite](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html), and it is the same six as the six eaten components of $\Phi$.

**3.4 The coefficients are the vacuum's.** $\tfrac14$ is $|T_{3R}|^{2}=\tfrac14$ on the right doublet. $\tfrac12$ is the $\mathrm{SU}(4)$ normalisation on the mixed cell, in the convention $\operatorname{tr}(X^{2})=\tfrac12$ for the generators. $\tfrac58$ is $|a_1|^{2}=\tfrac14+\tfrac38$: one quarter from $T_{3R}$ and three eighths from $B-L=\sqrt{8/3}\,T^{15}$ with $\operatorname{tr}(T^{15})^{2}=\tfrac12$. None of the three is adjustable, and none of them is a coupling.

**3.5 Two caveats on these numbers.** First, $\tfrac58$ carries the normalisation convention $\operatorname{tr}(T^{15})^{2}=\tfrac12$; the other two do not depend on a choice of normalisation, because a doublet and a mixed cell are fixed by the representation theory alone. Second, the bare coefficients are not by themselves a mass ratio: the $\mathrm{SU}(4)$ entries are multiplied by $g_4$ and the $\mathrm{SU}(2)_R$ entries by $g_R$, and the two couplings are independent above $M_C$ and equal only at it. The physical ratio carries the coupling ratio,

$$
\frac{M_X}{M_{W_R}}=\sqrt2\,\frac{g_4}{g_R},
$$

so it is a prediction only once the two couplings are matched, which is why §*The Twelve* gives coefficients and no masses.

**3.6 The $Z_R$ in full.** The $\tfrac58$ is the equal-coupling value of a sum with one term per generator the state contains:

$$
M_{Z_R}^{2}=\tfrac14\,g_R^{2}v_R^{2}+\tfrac38\,g_4^{2}v_R^{2},
\qquad
M_{Z_R}^{2}=\tfrac58\,g^{2}v_R^{2}\ \text{when}\ g_4=g_R=g .
$$

The first term is the $T_{3R}$ quarter and the second the $B-L$ three eighths. This is also the sense in which the neutral at $M_R$ is not a $\mathrm{U}(1)_R$ boson: it is the mixture that consumes the $B-L$ direction, and the paragraph on the differences in §*The Count at Every Stage* is the accounting for that consumption.

## The Count at Every Stage

**The same identity, read three times.** Above each threshold the massless set is larger, because fewer generators are broken.

| stage | unbroken group | dimension | massless bosons | broken at that step |
|---|---|---|---|---|
| top | $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $21$ | all $21$ | none |
| after $M_C$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $15$ | $8+1+3+3$ | $6$ leptoquarks |
| after $M_R$ | $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ | $12$ | $8+3+1$ | $W^{\pm}_{R}$, $Z_R$ |
| after $M_W$ | $\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}$ | $9$ | $8+1$ | $W^{\pm}_{L}$, $Z$ |

**Two readings of the middle row.** The $15$ is the stabiliser of the carrier line *alone*, so it is the description between the two steps only if the field carrying that line has no $R$ index — a $(\mathbf4,\mathbf1,\mathbf1)$ with the right line fixed by a separate $(\mathbf1,\mathbf1,\mathbf2)$. The minimal content's $(\mathbf4,\mathbf1,\mathbf2)$ carries both lines, so one vacuum fixes both and the first threshold lands on the $12$ row directly: the threshold count is $21\to12\to9$, and the $15$ is a factor count. [The Order of the Breaking in the Four Colours Left–Right Model: Nested Vacua and the Scale Order $M_C\ge M_R\ge M_W$](the-order-of-the-breaking-in-the-four-colours-left-right-model-nested-vacua-and-the-scale-order.html) owns that distinction.

**The differences, and why the second step costs three.** $21-15=6$, $15-12=3$, $12-9=3$, and $6+3+3=12$. The second step costs three and not the two one would assign to $\mathrm{SU}(2)_R\to\mathrm{U}(1)_R$ alone, because four generators are consumed and one survives: the triplet $\{W^{1}_R,W^{2}_R,W^{3}_R\}$ and the $B-L$ boson, which was massless after $M_C$, are replaced by the single hypercharge generator. The three states that acquire mass are $W^{\pm}_{R}$ and the neutral mixture $Z_R$; the dimension budget and the state count are the same number here, and the reason is that $B-L$ pays one of the three. The third step repeats the pattern exactly, with $\mathfrak{su}(2)_L\oplus\mathfrak u(1)_Y$ in place of $\mathfrak{su}(2)_R\oplus\mathfrak u(1)_{B-L}$.

**Why the rank does not fall at the first step.** The six leptoquark directions are non-Cartan, so $5\to5$ there and the rank falls only at the last two steps: $5\to5\to4\to3$. A reader who expects one rank drop per step will miscount the first.

## Why the Count Cannot Be Otherwise

**Four arguments, each independent.** They are worth stating separately because each fails in a different model.

**5.1 The kernel argument.** §*The Stabiliser, Which Is the Answer*: $\ker M^2=\mathfrak h$ identically.

**5.2 The coset argument.** The number of massive gauge fields equals the dimension of the coset $G/H$, because each broken generator contributes exactly one real degree of freedom to the would-be Goldstones, and each would-be Goldstone is eaten. At the bottom, with $\dim G=21$ and $\dim H=9$, the coset has dimension $12$.

**The coset count is the total, and the stage table is the sum of the stages.** Read against the final stabiliser alone, $21-9$ is one number. Read stage by stage, the same argument applies to each stabiliser in turn — $21-15$ for the first line, $15-12$ for the second, $12-9$ for the third — and the three telescope:

$$
(21-15)+(15-12)+(12-9)=6+3+3=21-9 .
$$

So the two counts do not compete. A reader who applies the final coset at an intermediate stage will get $12$ where the answer is $6$ or $3$, because the intermediate group is the stabiliser of the lines fixed so far and not of the full vacuum.

**The middle row is a factor, not a stage, in the minimal content.** The $15$ is the stabiliser of the carrier line alone, which requires the field carrying that line to have no $R$ index. The minimal content's $(\mathbf4,\mathbf1,\mathbf2)$ carries both lines, so its one vacuum has the dimension-$12$ stabiliser and the thresholds are $21\to12\to9$. The table is the factor count; §*The Count at Every Stage* above and the scales article state the difference.

**5.3 The eigenvalue argument.** In the neutral basis $\{W^{3}_L,W^{3}_R,B'\}$ the two vacuum directions are the vectors of eigenvalues of $(T_{3L},T_{3R},T^{15})$ on the fields that take the vevs:

$$
a_1=\bigl(0,\tfrac12,-\sqrt{\tfrac38}\bigr)v_R,
\qquad
a_2=\bigl(\tfrac12,-\tfrac12,0\bigr)v,
\qquad
\mathcal M^{2}=a_1a_1^{\mathsf T}+a_2a_2^{\mathsf T},
$$

the vectors carrying their own vacuum values. Then $\mathcal M^{2}$ is a sum of two rank-one matrices, so rank $\le2$ and at least one null direction; and $a_1\cdot a_2=-\tfrac14v_Rv\ne0$, so the two are independent and the rank is exactly two. Three neutral generators, one massless and two massive: $3=1+2$. The same vectors, with the same normalisation, are in [Classification of the Bosons in the Four Colours Left–Right Model: Twenty-Four Cells, Twenty-One Generators, Nine Massless and Twelve Massive](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html), §*The Neutral Sector*.

**5.4 The independence of content.** The identity $\#\{\text{massless}\}=\dim\mathrm{Stab}(\Phi_0)$ holds for any vacuum, any scalar content and any ordering of scales. What the content changes is *which* subgroup is the stabiliser, not whether the count is the stabiliser's dimension. A different multiplet list therefore moves the number only by moving the vacuum.

## What Masslessness Means at Each Scale

**One word, three regimes.** The phrase "the $W_R$ is massless" is false at low energy and true above $M_R$, and both statements are exact.

**6.1 Above a threshold.** The gauge field exists as a propagating degree of freedom and its mass is zero in the unbroken phase. The count at the top of the table is $21$ massless fields.

**6.2 Below a threshold.** The field is removed from the low-energy theory. It is not a massless field with a small mass; it is not present. The low-energy theory is written with nine gauge fields and no others, and the removal is the subject of [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html).

**6.3 At the threshold.** The matching is where the two descriptions meet, and it is not a physical transition of the gauge sector: the vacuum is a fact at every scale, and the description changes because the theory is truncated, not because the group changes. This is the distinction that [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html) turns into a statement about one derivative written in two bases.

**6.4 The scalar count is the same count.** Twelve broken generators, twelve eaten real scalars, twelve survivors of twenty-four. Three twelves, and only the first two are the same twelve. [The Scalar Sector of the Four Colours Left–Right Model: Twenty-Four Real Components, Twelve Eaten, Twelve Surviving](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html) owns that ledger.

## Tree Level, and Where a Loop Would Enter

**What the identity survives.** The kernel statement is exact at tree level and survives a renormalised vacuum: the stabiliser is a property of the vacuum's direction, and a loop that changes the vacuum's value without changing its orbit changes no stabiliser.

**What it does not survive unchanged.** The values in §*The Twelve* are tree-level. At one loop the coefficients shift, the neutral mixing angle runs, and the $\rho$ parameter departs from one by a finite amount. Those statements belong to [Custodial Symmetry and the Rho Parameter: From Accidental to Gauged](custodial-symmetry-and-the-rho-parameter.html) and to [The Effective Potential and the One-Loop Correction in Biquaternionic Form](the-effective-potential-and-the-one-loop-correction-in-biquaternionic-form.html).

**The honest boundary.** This article cannot say that the nine masses are zero to all orders. It says that the nine fields are the unbroken ones and that their masses vanish identically in the classical Lagrangian. A loop that generated a mass for a gluon or a photon would contradict gauge invariance, and none does.

## The Checks

**Seven checks, each independent.**

| check | computation | result |
|---|---|---|
| the totals | $9+12$ against $21$ | $21$ |
| the budget | $(21-15)+(15-12)+(12-9)$ | $6+3+3=12$ |
| the rank | $5\to5\to4\to3$ | the broken Cartan directions are $0+0+1+1$: the sextet is off-diagonal, so the first step costs no rank |
| the neutral block | three neutral generators, rank two | one massless, two massive |
| the eaten scalars | $12$ broken against $16+8=24$ real | $12$ eaten, $12$ survive |
| the leptoquark six | $3$ complex mixed cells | $6$ real |
| the identity | $\ker M^2=\mathfrak h$ | proved from $[X,\Phi_0]=0$ |

## Distinctions That Are Easy to Lose

**Three pairs.**

**8.1 Massless and light.** A field below its threshold is absent, not light. Writing that the $Z_R$ has a small coupling to the electron mixes the two regimes.

**8.2 The stabiliser and the low-energy gauge group.** They coincide here only because the minimal content uses one scalar per step. With two scalars the unbroken group is the intersection of the two stabilisers, and the intersection is what the low-energy theory carries.

**8.3 Nine massless gauge fields and one massless boson.** The nine are unbroken generators, hence gauge fields with zero mass. Eight of them are gluons, confined, and therefore absent from the asymptotic spectrum; one is the photon, which is the single massless asymptotic gauge boson. "Nine massless" is a statement about the mass matrix; "one massless" is a statement about the spectrum. Confinement is what separates them, and it is [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html).

## Summary

**The subgroup.** $H_3=\mathrm{SU}(3)\times\mathrm{U}(1)_{\mathrm{em}}$, dimension nine, the stabiliser of the vacuum.

**The identity.** $\ker M^2=\mathfrak h$; the massless count is the dimension of the stabiliser, exactly, at tree level.

**The nine.** Eight gluons and one photon, the photon being the null combination of $W^3_L$, $W^3_R$ and $B$. Nine massless gauge fields, of which eight are confined and so are not asymptotic states; one massless asymptotic boson, the photon.

**The twelve.** Six leptoquarks, $W^{\pm}_{L}$, $W^{\pm}_{R}$, $Z$ and $Z_R$, with coefficients $\tfrac12$, $\tfrac14$, $\tfrac14$, $\tfrac14(g_L^2+g_Y^2)$ and $\tfrac14 g_R^2+\tfrac38 g_4^2$ (the last written $\tfrac58g^2$ at $g_4=g_R=g$).

**The stages.** $21\to15\to12\to9$ in dimensions, with $6$, $3$, $3$ leaving at the three steps and the rank falling only at the last two.

**What is not here.** No mass value, no coupling value, no loop correction.

## Summary of Notation

| symbol | meaning |
|---|---|
| $G_{4LR}$ | $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ |
| $H$, $\mathfrak h$ | the unbroken subgroup and its Lie algebra |
| $\Phi_0$ | the vacuum value of the scalar content |
| $M^2_{XY}$ | the gauge mass matrix, $\operatorname{tr}([X,\Phi_0]^\dagger[Y,\Phi_0])$ |
| $X^{a}$, $\bar X^{a}$ | the leptoquark gauge fields, $a=r,g,b$ |
| $W^{\pm}_{L}$, $W^{\pm}_{R}$ | the charged gauge fields of the two weak factors |
| $Z$, $Z_R$ | the two massive neutral mass eigenstates |
| $v$, $v_R$ | the electroweak and colour-breaking vacuum expectation values |
| $T^{15}$, $B$ | the $\mathrm{SU}(4)$ Cartan direction and the $B-L$ boson |
| $g_4$, $g_L$, $g_R$, $g_Y$ | the four couplings, all symbolic here |

## Further Reading

- [Classification of the Bosons in the Four Colours Left–Right Model: Twenty-Four Cells, Twenty-One Generators, Nine Massless and Twelve Massive](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html). The cells, the names, the neutral sector and the same nine-and-twelve count read off the grids.
- [The Breaking Chain of the Four Colours Left–Right Model: One Flag, Three Stabilisers, Three Scales](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html). The three stabilisers this article's subgroup is the last of.
- [The Scalar Sector of the Four Colours Left–Right Model: Twenty-Four Real Components, Twelve Eaten, Twelve Surviving](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html). The fields that supply the vacuum, and the eaten count.
- [The Leptoquarks of the Four Colours Left–Right Model: Six States, One Bound, and Why Proton Decay Does Not Bite](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html). The six states of the first step.
- [The Photon as the Unbroken Mixture: One Null Direction, Three Parents](the-photon-as-the-unbroken-mixture.html). The null direction of the neutral block.
- [Custodial Symmetry and the Rho Parameter: From Accidental to Gauged](custodial-symmetry-and-the-rho-parameter.html). Where the tree-level coefficients of §*The Twelve* receive their one-loop correction.
- [The Threshold Scales: $M_C$, $M_R$, $M_W$, and What Would Fix Them](the-threshold-scales-mc-mr-mw-and-what-would-fix-them.html). The bound that fixes the first scale, and the parameters the chain leaves free.
