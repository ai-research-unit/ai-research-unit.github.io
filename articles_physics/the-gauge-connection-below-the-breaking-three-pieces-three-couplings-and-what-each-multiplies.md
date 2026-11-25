# __The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies__

## Introduction

**The question.** The model has one covariant derivative at the top and one coupling. After the chain, how many pieces does that derivative have, what does each piece multiply, and are the three low-energy couplings independent?

**The answer.**

$$
\boxed{\;
D_\mu=\partial_\mu
-i g_s\,G^{a}_{\mu}T^{a}
-i g\,\frac{\tau^{a}}{2}W^{a}_{\mu}
-i g_Y\,Y B_{\mu},
\qquad
a=1,\dots,8\ \text{for colour},\quad a=1,2,3\ \text{for isospin},
\;}
$$

$$
\boxed{\;
g_s=g_4,
\qquad
g=g_L,
\qquad
\frac{1}{g_Y^{2}}=\frac{1}{g_R^{2}}+\frac{1}{(2g_{B-L})^{2}},
\qquad
\frac{1}{e^{2}}=\frac{1}{g^{2}}+\frac{1}{g_Y^{2}},
\qquad
\tan\theta_W=\frac{g_Y}{g}.
\;}
$$

**The single idea.** The covariant derivative is not rewritten; it is *restricted*. Above $M_C$ it carries fifteen connections and one coupling, because there is one group. Below $M_R$ it carries twelve connections and three couplings, because the factors the chain leaves carry one each; below $M_W$, nine of those connections are massless and two couplings act on them. **The couplings belong to the factors, and the factors change exactly once: at $M_C$, where one group becomes four.** Hypercharge's coupling is then not a fourth coupling but a combination of two of them, and the factor of two in that combination is the same $\tfrac12$ that appears in $Y=T_{3R}+\tfrac12(B-L)$.

**What the article establishes.** The derivative at the top; its restriction at each step; the table of what each surviving piece multiplies; the two matching relations with their factors of two; the reason there are three couplings and not four; and where the heavy pieces go when they are removed.

**What the article does not establish.** No numerical value. $g_4$, $g_L$, $g_R$ are symbols here, and the running that would give them values at a scale is [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html). Whether the running succeeds is [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html).

**Where the algebras are.** [The Gauge Algebras of the Two Sectors: Colour on Three Dimensions, Weak Isospin on Two, the Photon on One](the-gauge-algebras-of-the-two-sectors-colour-on-three-dimensions-weak-isospin-on-two-the-photon-on-one.html) lists the algebras this derivative is built from. The generic construction of a covariant derivative in the algebra is [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html).

## One Derivative at the Top

**Fifteen connections, one coupling.** The count is the first thing to get right.

**1.1 The object.** Above $M_C$ there is one group and one derivative,

$$
D_\mu=\partial_\mu-i g_4\,A^{A}_{\mu}T^{A},
\qquad A=1,\dots,15,
$$

with $T^{A}$ the fifteen anti-Hermitian generators of $\mathfrak{su}(4)$. **No $W$, no $V$, no $\tau^{a}$, no $\sigma^{a}$: none of those exists above the transition.**

**1.2 Fifteen and one.** Fifteen connections, because there are fifteen generators. One coupling, because there is one simple factor. A simple group has one coupling by definition — the generators of $\mathrm{SU}(4)$ cannot carry different couplings without breaking the invariance that makes them a basis of one algebra.

**1.3 Why "fifteen and one" matters.** Any statement that separates couplings above $M_C$ — "the leptoquark coupling is different from the gluon coupling", "the weak coupling is a second parameter" — is false, because there is one parameter. **Below $M_C$ the four factors are not equal in status.** Colour and $B-L$ are subalgebras of the algebra that carried $g_4$, so their couplings are $g_4$ by inheritance, exactly. The weak pair is not a subalgebra: it is born at $M_C$ with the index, and its two couplings are free parameters whose equality to $g_4$ is the corpus's threshold assumption and not a derivation — [The Handover at $M_C$](the-handover-at-m-c-what-the-transition-hands-down-and-where-the-masses-come-from.html) says where that assumption fails.

**1.4 The reality condition.** Each connection is real, each generator anti-Hermitian in the physicists' convention or Hermitian with the $i$ absorbed, and the whole expression is anti-Hermitian: $D^\dagger=-D$. That is what makes $D_\mu$ a derivative rather than a field, and it is the reason the algebra's anti-Hermitian subspace is the one that carries the connection.

## The Same Derivative in the Residual Basis

**No new object: a change of basis, applied twice.** The derivative is restricted, and the restriction is exact.

**2.1 After $M_C$.** Split the fifteen into the eight $\mathfrak{su}(3)$ directions, the one $B-L$ direction and the six leptoquark directions:

$$
g_4A^{A}T^{A}\ \longrightarrow\
g_4\,G^{a}T^{a}+g_4\,B\,T^{15}+g_4\left(X^{a}_{\mu}\,T^{a}_{t}+\text{h.c.}\right),
$$

where $T^{a}_{t}$ are the six mixed generators. The colour piece and the $B-L$ piece are the residual ones; the mixed piece is heavy. Note that all three carry the same $g_4$: the split is a split of generators, not of couplings.

**The weak pieces are not a split of the fifteen.** They are new connections, and they appear because the two copies of $\mathrm{SU}(2)$ arrive at $M_C$ with the index that the breaking object carries — [The Weak Force Born as a Side Effect](the-weak-force-born-as-a-side-effect-a-condensate-index-five-ranks-from-three.html). **So the derivative below $M_C$ is the restriction of the one above it plus six connections whose couplings are not inherited:** $g_L$ and $g_R$ are free parameters, matched to $g_4$ only by the threshold assumption. The six mixed generators $T^{a}_{t}$ are a different object: they are inside the fifteen, they are the ones that became heavy, and their coupling is $g_4$ like the rest.

**2.2 After $M_R$.** The right triplet splits into the surviving $\mathrm{U}(1)_R$ and two heavy directions, and the neutral fields mix:

$$
g_4\,B\,T^{15}+g_R\,V^{3}\frac{\sigma^{3}}{2}\ \longrightarrow\
g_Y\,B'\,Y+g_R\,(\text{heavy neutral}),
$$

with $Y=T_{3R}+\tfrac12(B-L)$, $B'$ the hypercharge field, and the heavy neutral the combination orthogonal to it. The mixing angle is fixed by the two couplings, not chosen.

**2.3 After $M_W$.** The left triplet splits into the surviving $\mathrm{U}(1)$ and two heavy directions, and the neutral fields mix again:

$$
g\,W^{3}\frac{\tau^{3}}{2}+g_Y\,B'\,Y\ \longrightarrow\
e\,A\,Q+g\,(\text{heavy neutral}),
$$

with $Q=T_{3L}+Y$ and $A$ the photon. The angle here is $\theta_W$.

**2.4 The observation.** In all three lines the heavy field is written in the same bracket as the light one, because both come from the same derivative. The difference between them is not their origin but whether they annihilate the vacuum, and that is [The Death of the Primordial Force](the-death-of-the-primordial-force-the-id-condensate-and-the-six-carriers-it-eats.html).

## What Each Piece Multiplies

**Three pieces, three modules, and a table that is the whole content.** A coupling without a module is a number; a piece with a module is a physical statement.

| piece | coupling | algebra | multiplies | acts on |
|---|---|---|---|---|
| gluon | $g_s=g_4$ | $\mathfrak{su}(3)$ | the triplet index of every coloured field | $\mathbb C^3$ |
| weak | $g=g_L$ | $\mathfrak{su}(2)_L$ | the $L$ doublet index, and only on left fields | $\mathbb C^2_L$ |
| hypercharge | $g_Y$ | $\mathfrak u(1)_Y$ | the number $Y$ of every field | the whole generation |

**3.1 The colours.** The gluon piece multiplies nothing but the triplet index: it is blind to flavour, to chirality and to the lepton line. In indices, $(T^{a})^{i}_{\ j}$ with $i,j\in\{r,g,b\}$ and no other free index.

**3.2 The left piece.** The weak piece multiplies the doublet index and is absent on right-handed fields, because the right block has no $L$ index. That absence is what "the weak interaction is chiral" means at the level of the derivative: a right-handed singlet has no $\tau^{a}$ to multiply.

**3.3 The hypercharge piece.** It multiplies a number, not an index, and it acts on every field of the generation. That is why $Y$ can distinguish $u_R$ from $d_R$ while colour cannot, and why the two right-handed states that were degenerate above $M_R$ split below it.

**3.4 The three heavy pieces, for contrast.** The leptoquark piece multiplies a colour index and a lepton index at once; the $W_R$ piece multiplies only the $R$ index; the heavy neutral pieces multiply the two combinations orthogonal to $Y$ and to $Q$. None appears in the table because none survives.

## The Three Couplings and the Two Matching Relations

**Where the factors of two come from.** This is the section that most often goes wrong, and the factor has a visible origin.

**4.1 The one relation that is an equality.** $g_s=g_{B-L}=g_4$ at the matching scale, because $\mathfrak{su}(3)$ and the $B-L$ direction are subalgebras of $\mathfrak{su}(4)$: the generators are literally the same generators, so no normalisation enters. **The weak pair is not in this class.** $\mathrm{SU}(2)_L$ and $\mathrm{SU}(2)_R$ are not subalgebras of $\mathrm{SU}(4)$ — they arrive with the index — so $g=g_L$ below $M_C$ names a free parameter, and its equality to $g_4$ is the threshold assumption of §4.5.

**4.2 The second relation is a combination.** Hypercharge is $Y=T_{3R}+\tfrac12(B-L)$, so the field $B'$ is a unit vector in the plane of the two neutral fields, and its component along each is fixed by the coupling:

$$
A_R=\frac{g_Y}{g_R}B',
\qquad
A_{B-L}=\frac{g_Y}{2g_{B-L}}B',
\qquad
A_R^{2}+A_{B-L}^{2}=B'^{2}.
$$

Dividing through by $B'^{2}$ gives

$$
\frac{g_Y^{2}}{g_R^{2}}+\frac{g_Y^{2}}{(2g_{B-L})^{2}}=1
\quad\Longrightarrow\quad
\frac{1}{g_Y^{2}}=\frac{1}{g_R^{2}}+\frac{1}{(2g_{B-L})^{2}}.
$$

**4.3 The factor of two is the same $\tfrac12$.** It is the $\tfrac12$ in $Y=T_{3R}+\tfrac12(B-L)$, passing through the orthogonality of the two fields. A reader who writes $g_Y^{-2}=g_R^{-2}+g_{B-L}^{-2}$ has normalised $B-L$ by its half-charge; both conventions are in use, and the corpus states which one it uses in the notation table.

**4.4 The electromagnetic relation.** The same construction one step later gives

$$
\frac{1}{e^{2}}=\frac{1}{g^{2}}+\frac{1}{g_Y^{2}},
\qquad
e=g\sin\theta_W=g_Y\cos\theta_W,
\qquad
\tan\theta_W=\frac{g_Y}{g},
$$

and the angle is a rotation of the basis, not a coupling. The corpus's statement of this is [The Weinberg Angle and the Three Neutral States: One Mixture, Three Denominators](the-weinberg-angle-and-the-three-neutral-states.html).

**4.5 The unification statement.** The model's threshold assumption is $g_4=g_L=g_R$ at one scale. That single equation is what makes the chain a unification rather than a product of three independent theories, and it is also the assumption that the running fails to reproduce: [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html).

## Why the Couplings Are Not Independent

**One relation, one counting argument.** Both say the same thing.

**5.1 The relation.** $g_Y$ is determined by $g_R$ and $g_{B-L}$ at the matching scale, so one coupling is not carried below $M_R$: the low-energy theory has three where the intermediate theory had four.

**5.2 The counting statement.** The count of independent couplings runs $1\to4\to3\to2$:

| stage | factors | independent couplings |
|---|---|---|
| above $M_C$ | $\mathrm{SU}(4)$ | $g_4$ |
| between $M_C$ and $M_R$ | $\mathrm{SU}(3)$, $\mathrm{U}(1)_{B-L}$, $\mathrm{SU}(2)_L$, $\mathrm{SU}(2)_R$ | $g_s$, $g_{B-L}$, $g_L$, $g_R$ |
| between $M_R$ and $M_W$ | $\mathrm{SU}(3)$, $\mathrm{SU}(2)_L$, $\mathrm{U}(1)_Y$ | $g_s$, $g$, $g_Y$ |
| below $M_W$ | $\mathrm{SU}(3)$, $\mathrm{U}(1)_{\mathrm{em}}$ | $g_s$, $e$ |

The count jumps at $M_C$ and falls twice, and the jump is the point: one factor becoming four leaves four couplings where there was one. **They are four values at the threshold, not four independent inputs**, and two of them — $g_s$ and $g_{B-L}$ — are fixed by inheritance rather than assumed. A counting that reads the four factors back above $M_C$ gets the first step wrong, and gets it wrong in the direction of more parameters than the model has.

**5.3 The consequence for a fit.** A fit to the low-energy data determines $g$ and $g_Y$; the model then predicts $g_R$ and $g_{B-L}$ through the relation, given the scale. That prediction is the model's content, and it is the one the running tests.

## What Is Left Out, and Where It Goes

**The heavy pieces are removed, not deleted.** The distinction is the subject of the next article in the block.

**6.1 The removal.** Below $M_C$ the leptoquark piece is absent from the derivative. Fields coupled by it are no longer coupled: the lepton and the quark do not share a connection, and the gauge symmetry that would have related them is gone.

**6.2 What remains of it.** The removal leaves operators: four-fermion terms with coefficients $\sim g_4^{2}/M_X^{2}$, which is why the leptoquarks can be bounded without being produced. That is the effective-Lagrangian statement, and the bound is in [The Sextet Put Aside](the-sextet-put-aside-six-leptoquarks-above-m-c-and-why-they-are-not-seen.html).

**6.3 The correction to the light couplings.** The removal also shifts the light couplings by finite amounts, which is the matching computation of [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html). At tree level the shifts are zero; at one loop they are not.

**6.4 The exact statement.** Up to the matching corrections, the three pieces above are the whole gauge sector of the low-energy theory. Nothing else couples to a fermion through a derivative.

## The Checks

**Six checks.**

| check | computation | result |
|---|---|---|
| the connections | $15$ above, $8+1+3+3$ after $M_C$ | $15$, then $15$ |
| the couplings | one per simple factor | $1$ above; $4$ below $M_C$; $3$ below $M_R$; $2$ below $M_W$ |
| the orthogonality | $A_R^{2}+A_{B-L}^{2}=B'^{2}$ | gives $g_Y^{-2}=g_R^{-2}+(2g_{B-L})^{-2}$ |
| the electromagnetic limit | $1/e^{2}=1/g^{2}+1/g_Y^{2}$ | reproduces $\tan\theta_W=g_Y/g$ |
| the chirality | $L$ piece absent on right singlets | the $R$ block has no $L$ index |
| the colour blindness | gluon piece carries no flavour index | holds in every term |

## Distinctions That Are Easy to Lose

**Three pairs.**

**7.1 A coupling and a connection.** Fifteen connections, one coupling. Counting connections and calling the result the number of couplings is the commonest error in the subject, and it is the error the old frame made when it counted twenty-one.

**7.2 The mixing angle and a coupling.** $\theta_W$ is a rotation of the neutral basis, fixed by the ratio of two couplings. It is not a third coupling and it does not run independently.

**7.3 The intermediate stage and the bottom.** At the intermediate stage there are four couplings because $B-L$ is a factor; at the bottom there are three because $Y$ is a direction. A counting that ignores this will report four at every stage above $M_W$.

## Summary

**One derivative.** Fifteen connections and one coupling at the top; twelve connections, three pieces and three couplings below $M_R$; nine massless connections and two couplings below $M_W$.

**The three pieces.** Colour on the triplet, weak isospin on the left doublet, hypercharge on the number $Y$.

**The two relations.** $g_s=g_{B-L}=g_4$ by identity of generators; $g_Y^{-2}=g_R^{-2}+(2g_{B-L})^{-2}$ by orthogonality of fields. **And one assumption:** $g_4=g_L=g_R$ at $M_C$, which the running tests.

**The angle.** $\tan\theta_W=g_Y/g$, a rotation and not a coupling.

**The heavy pieces.** Removed below their thresholds, leaving four-fermion operators and finite shifts to the light couplings.

**What is assumed.** $g_4=g_L=g_R$ at one scale, which is the unification statement and the one the running fails.

## Summary of Notation

| symbol | meaning |
|---|---|
| $D_\mu$ | the covariant derivative |
| $g_4$, $g_L$, $g_R$ | the couplings of the three simple factors |
| $g_{B-L}$ | the coupling of the $B-L$ factor between $M_C$ and $M_R$ |
| $g_s$, $g$, $g_Y$, $e$ | the low-energy couplings of colour, isospin, hypercharge, electromagnetism |
| $T^{A}$, $T^{a}$ | the fifteen $\mathrm{SU}(4)$ generators and the eight colour ones |
| $\tau^{a}$, $\sigma^{a}$ | the left and right isospin generators |
| $Y$, $Q$ | hypercharge and electric charge |
| $\theta_W$ | the weak mixing angle, $\tan\theta_W=g_Y/g$ |

## Further Reading

- [The Gauge Algebras of the Two Sectors: Colour on Three Dimensions, Weak Isospin on Two, the Photon on One](the-gauge-algebras-of-the-two-sectors-colour-on-three-dimensions-weak-isospin-on-two-the-photon-on-one.html). The algebras and modules this derivative is built from.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html). The generic construction, before any model.
- [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html). What the removal of the heavy pieces costs.
- [The Weinberg Angle and the Three Neutral States: One Mixture, Three Denominators](the-weinberg-angle-and-the-three-neutral-states.html). The rotation $\theta_W$ and the neutral basis.
- [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html). The running of these three couplings, and where it fails.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html). The field strength built from $D_\mu$ once the photon is separated.
