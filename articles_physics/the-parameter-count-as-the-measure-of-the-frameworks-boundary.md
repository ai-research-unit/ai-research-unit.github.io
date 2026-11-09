# __The Parameter Count as the Measure of the Framework's Boundary__

## Introduction

**The claim of this article, in one sentence.** The Standard Model has nineteen free parameters, the framework fixes none of them, and this article turns that sentence into a number, a classification and a test.

**Why a count is the right measure.** A framework can be judged in two ways: by what it derives, or by what it leaves open. The corpus has spent fifteen articles on the first question and has produced a short list. The second question has a precise answer, because "what is left open" is a finite list that someone else has already written down, and each entry can be examined one at a time.

**The three grades of "fixing", and why the distinction is not pedantry.** Saying that a framework "does not derive the electron mass" lumps together three very different failures:

- **A value.** A principle that returns $m_e=0.511$ MeV. No framework in existence does this for any fermion mass, so the failure is universal and uninformative.
- **A relation.** A principle that makes one parameter a function of another, reducing the count by one. This is a weaker claim and a much more interesting one, because it is achievable and because it is falsifiable.
- **A constraint.** A principle that forbids a region, such as $\theta_{\mathrm{QCD}}=0$ or $m_\nu=0$. Also achievable, and the corpus has two examples.

An article that reported only the first grade would be reporting a failure shared by every competitor. Reporting all three is what makes the count a measure rather than a complaint.

**The four results.**

- **Nineteen, and the list is robust.** Three conventions give $18$, $19$ and $19$; the differences are bookkeeping and the core is stable. One unit is arbitrary, so the physical content is **eighteen dimensionless numbers**.
- **A typology, and it is not uniform.** Eight of the nineteen are coordinates on a group the algebra supplies, nine are eigenvalues of an operator it represents but cannot diagonalise from first principles, and two — the electroweak scale and the scalar mass — it cannot represent at all.
- **The framework's own list is three, and it does not overlap.** The charge parameter, the mass, and the constant of the massive equation. So the honest total is twenty-two, of which the framework contributes none of the nineteen, and the imported share is $86.4\%$.
- **The count is a test that can be run on any proposal.** For any claimed derivation, ask which of the nineteen it fixes and by which of the three grades. The article ends with the table that question produces for the corpus's own proposals.

**The order.** The list, then the definition of fixing, then the typology, then the three groups, then the framework's own count, then the one unit and the eighteen ratios, then the neutrino addition, then the over-determination, then the test applied to the corpus, then what would have to be true for the count to fall, then the ledger.

## The Nineteen, Itemised

**The list, quoted from the source of record.** [The content article](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html) prints it with values and schemes; the table is repeated here without the values, because this article's argument is about kinds and not magnitudes.

| # | Symbol | Kind of object | Sector |
|---|---|---|---|
| 1–3 | $m_e$, $m_\mu$, $m_\tau$ | Charged-lepton masses | Flavour |
| 4–9 | $m_u$, $m_d$, $m_s$, $m_c$, $m_b$, $m_t$ | Quark masses | Flavour |
| 10–12 | $\theta_{12}$, $\theta_{23}$, $\theta_{13}$ | CKM angles | Flavour |
| 13 | $\delta$ | CKM phase | Flavour |
| 14 | $g_{\mathrm Y}$ | Hypercharge coupling | Gauge |
| 15 | $g$ | Weak coupling | Gauge |
| 16 | $g_s$ | Strong coupling | Gauge |
| 17 | $\theta_{\mathrm{QCD}}$ | Vacuum angle | Gauge |
| 18 | $v$ | Higgs expectation value | Scalar |
| 19 | $M_H$ | Higgs mass | Scalar |

**The sector sums.**

$$
\underbrace{13}_{\text{flavour}}+\underbrace{3}_{\text{couplings}}+\underbrace{1}_{\theta_{\mathrm{QCD}}}+\underbrace{2}_{\text{scalar}}=19 .
$$

The flavour block is $13$ of $19$, that is $68.4\%$. Two thirds of the model's freedom sits in the sector the framework says the least about, which is the first quantitative statement of this article: the boundary is not spread evenly, it is concentrated where the algebra is emptiest.

**The regrouping, and why it does not change the count.** The scalar pair can be written $(v,M_H)$ or $(\mu^2,\lambda)$, related by $v^2=\mu^2/\lambda$ and $M_H^2=2\lambda v^2$. Recomputing from the quoted values,

$$
\lambda=\frac{M_H^2}{2v^2}=\frac{(125.09)^2}{2(246.22)^2}=0.1291 ,
\qquad
\mu=\frac{M_H}{\sqrt2}=88.5\ \mathrm{GeV} .
$$

Two numbers either way. The count is invariant under the choice, which is what makes it a property of the model rather than of the notation.

**The conventions that give 18 or 19.**

| Convention | Count | Reason |
|---|---|---|
| $\theta_{\mathrm{QCD}}$ set to zero by a mechanism | $18$ | The axion removes one entry |
| Neutrinos massless, as in the minimal content | $19$ | The baseline |
| $\theta_{\mathrm{QCD}}$ retained as a parameter | $19$ | Baseline with the small bound |
| $v$ and $M_H$ counted as $\mu^2$ and $\lambda$ | $19$ | Regrouping only |

So the count is $18$ or $19$ depending on whether the strong CP problem is solved, and never $17$ or $20$ on any convention in use. That is a stable list.

**What the count is not.** It is not a count of measurements. The model predicts far more than nineteen numbers, so the count of parameters and the count of observables are different quantities — and the gap between them is the model's testability, taken up below.

## What "Fixing" a Parameter Would Mean

**Three grades, defined exactly.**

| Grade | Criterion | Reduces the count? | Falsifiable how? |
|---|---|---|---|
| Value | A principle returns the measured number | No | Any other number refutes it |
| Relation | One parameter becomes a function of another | Yes, by one | The relation is measured and can fail |
| Constraint | A region is forbidden | No, but it explains why a bound holds | The bound is measured and can fail |

**Why the grades must be kept apart.** A framework that fixes zero values but produces one relation has done something real: it has reduced the model's freedom by one, and it has made a statement that a measurement can contradict. A framework that produces no relation but does explain why $\theta_{\mathrm{QCD}}<10^{-10}$ has also done something real. An article that reported "zero of nineteen" without the grades would be accurate and uninformative, in the way that "zero of nineteen" is uninformative about any framework that is not a theory of everything.

**The measure this article will use.** Not "how many values are derived", which is zero everywhere, but:

$$
\text{arena}+\text{relations}+\text{constraints} ,
$$

three separate counts, each of which can be nonzero. The rest of the article computes them.

## The Typology: Five Kinds of Number

**The classification.** Each of the nineteen is one of five kinds of mathematical object, and the kinds are not interchangeable because they require different machinery to fix.

| Kind | What it is | Which entries | Count |
|---|---|---|---|
| Group coordinate | A point in a parameter space the algebra supplies | 10–13 | $4$ |
| Connection normalisation | The size of a coupling in a covariant derivative | 14–16 | $3$ |
| Central phase | The phase of a topological term | 17 | $1$ |
| Eigenvalue | A mass, that is a spectrum of an operator | 1–9, 19 | $10$ |
| Scale | The one dimensionful normalisation | 18 | $1$ |

**The counts add to nineteen,** and the classification is exhaustive: a number in a Lagrangian is a coupling, a phase, an eigenvalue, or a scale, and the mixing angles are coordinates with no other home.

**Why the kinds matter more than the sectors.** The sector split (flavour $13$, gauge $4$, scalar $2$) is about physics. The kind split is about **what would have to be built**. A group coordinate needs a group and a selection principle; a connection normalisation needs a connection and a normalisation principle; a central phase needs a topology and a value; an eigenvalue needs an operator and a spectral principle; a scale needs a mechanism that breaks dilatation invariance. Those are five different machines, and the framework has some of them and not others.

## Eight With an Arena, Nine With an Eigenvalue, Two With Nothing

**The three groups, by what the framework can represent.**

| Group | Entries | Count | What the framework has |
|---|---|---|---|
| **Arena** | 10–17 | $8$ | The group, the connection, the phase: represented, value free |
| **Eigenvalue only** | 1–9 | $9$ | A mass term, but no spectral principle |
| **Nothing** | 18, 19 | $2$ | No scale mechanism, no scalar mass principle |

The shares are $42.1\%$, $47.4\%$ and $10.5\%$.

**One entry is in two groups, and the reason is exact.** $M_H$ is an eigenvalue by kind, since a scalar mass is a spectrum of a mass operator, and it is in the "nothing" group by arena, because the operator it is a spectrum of belongs to a scalar sector the framework does not host. For entries 1–9 the framework does host the operator — the Dirac mass term and the Yukawa matrices — and lacks only the principle that picks the eigenvalues. For $M_H$ it lacks the operator as well. The kind and the arena are therefore two different questions, and $M_H$ is the one entry where the answers differ.

**The arena group, entry by entry.**

- **The four mixing parameters (10–13).** A $3\times3$ unitary matrix has nine real parameters; rephasing five away leaves four. The framework supplies $\mathrm{U}(3)$ as the norm-preserving group of the flavour factor and the elements on which it acts, so the *space* is supplied. [The CKM article](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) supplies the necessity of the phase not being removable. The point in the space is measured.
- **The three couplings (14–16).** Each is the normalisation of a connection in a covariant derivative. The framework's gauge principle produces exactly this object and records that its normalisation is a free parameter $ϙ$; a second coupling is a second free parameter with no relation to the first. So the arena is supplied — and supplied *with the same freedom*, which is why this is arena and not derivation.
- **The vacuum angle (17).** A phase of a central term, which [the theta-vacuum article](the-theta-vacuum-in-biquaternionic-form.html) constructs. The arena is supplied; the smallness is not explained.

**The eigenvalue group, and the precise gap.** A mass is an eigenvalue of a mass operator, and the framework represents the operator: the mass term in the Dirac equation, the mass matrices in the Yukawa sector. What it does not have is a principle that selects the eigenvalues. Two statements must be kept apart:

- The framework **represents** $m_e$ as a parameter of a mass term. True, and cheap.
- The framework **does not determine** $m_e$. Also true, and this is the gap.

The one proposal in the corpus that touches this group, [the spin–mass formula](the-spin-mass-formula-and-the-spectrum-of-elementary-particles-in-biquaternionic-form.html), makes masses proportional to representation dimensions normalised to the electron. That fixes **ratios**, not the scale, and a mass parameter *is* a scale. So it is a relation of a restricted kind — a relation among the nine holding one of them fixed — and not a value.

**The two with nothing, and why they are the hardest.** The electroweak scale $v$ and the scalar mass $M_H$ both require a mechanism that the algebra does not contain:

- $v$ is generated by a potential's curvature going negative, which is a statement about a *dynamical* choice of vacuum. [The strong-coupling article](hadron-structure-from-qcd-the-bound-state-problem.html) showed what such a generation looks like in QCD, where the scale is non-perturbative and no finite order produces it. The electroweak scale has the same logical shape and the framework has no counterpart of the mechanism.
- $M_H$ is a scalar mass, which is the quantity with the quadratic sensitivity that the next article takes up. Nothing in the algebra cuts off a quadratic divergence, because a cutoff is a property of a regularisation and the algebra has no measure.

So the two entries with no arena are the two that require machinery from outside both the model and the algebra, and that is not a coincidence: they are the entries whose values are set by the vacuum rather than by a structure.

## The Framework's Own Parameters, Counted the Same Way

**The list.** The corpus's own constructions carry three continuous parameters:

| Parameter | Where it appears | Fixed by the algebra? |
|---|---|---|
| $ϙ$ | The central charge of the gauge principle | No |
| $m$ | The mass in the massive field equation | No |
| $k_m$ | The constant of the massive equation | No |

**The honest total.** If a reader counts "framework plus Standard Model" as one theory, the count is

$$
19+3=22 ,
$$

and the imported share is $19/22=86.4\%$. So the framework is not more parsimonious than the model it reformulates. It has a different list, and it adds a short one to a long one.

**Why this comparison is the right one and not a rhetorical one.** A reformulation that added parameters without fixing any would be a strictly worse description on the counting measure, and saying so is the discipline the corpus has imposed on itself throughout. The defence of the reformulation is not that it is smaller; it is that its objects are *geometric* — that a coupling is a connection coefficient, that a mass is an eigenvalue, that a phase is a central term — and that geometry is worth something even when it fixes nothing.

**The one place the framework's parameters could bite.** If $ϙ$ were related to one of the three gauge couplings by a structural argument, the count would fall by one and the claim would be grade two — a relation. No such argument exists in the corpus, and the gauge article records that no relation binds $ϙ$ to a second coupling. So the relation count is zero, and this article states it as zero.

**The three counts, assembled.**

| Measure | Value |
|---|---|
| Values derived | $0$ of $19$ |
| Relations produced | $0$ |
| Constraints explained | $2$ of $2$ in scope: $\lvert\theta_{\mathrm{QCD}}\rvert<10^{-10}$ has a mechanism available (the axion), and $m_\nu=0$ is *excluded* by oscillation |
| Arena supplied | $8$ of $19$ |
| Own parameters added | $3$ |

The constraint row deserves a note. The framework does not *explain* why $\theta_{\mathrm{QCD}}$ is small; it constructs the angle and records that its smallness is a separate problem with a proposed solution. And the massless-neutrino constraint is not explained either — it is refuted, which is what [the PMNS article](the-pmns-matrix-and-lepton-mixing.html) records.

## One Unit and Eighteen Ratios

**The statement.** A parameter count is only meaningful once units are fixed. With $\hbar=c=1$ the model has one dimensionful unit, and choosing it removes one parameter from the physical content:

$$
19\ \text{parameters}-1\ \text{unit}=18\ \text{dimensionless numbers}.
$$

Any one of the nineteen can be taken as the unit; the eighteen ratios are what a measurement determines. This is not a bookkeeping trick, because the choice is unobservable: a universe with all masses doubled is the same universe.

**What survives the choice.** The eighteen dimensionless combinations include $\lambda=0.1291$, the mass ratios $m_\mu/m_e=206.8$ and $m_t/m_e=3.4\times10^{5}$, the three couplings, the four mixing parameters, and $\theta_{\mathrm{QCD}}$. Taking $v$ as the unit, the ratio $M_H/v=0.5080$ is one of the eighteen, and it is the one that sets the electroweak hierarchy problem's scale.

**Why the nineteen are not nineteen independent measurements.** Three of them are not measured directly at all: $\theta_{\mathrm{QCD}}$ is bounded rather than measured, the three couplings are extracted from a fit to many observables, and the mixing parameters are fit outputs. So the count of *directly measured* parameters is smaller than nineteen, and the count of *fitted* ones is larger. Both facts are worth stating before the count is used as a measure.

**The scale hierarchy, which the ratios expose.** Two ratios of the eighteen are the corpus's remaining embarrassments:

$$
\frac{m_t}{m_e}=3.4\times10^{5}\ (5.53\ \text{orders}) ,
\qquad
\frac{v}{M_{\mathrm{Pl}}}=2.0\times10^{-17}\ (-16.7\ \text{orders}) .
$$

The first is a flavour puzzle; the second is the hierarchy problem. Both are statements about the eighteen ratios, and neither has an explanation in the framework. They are the subject of the next two articles. [The precision-observables article](electroweak-precision-observables-the-oblique-parameters-s-t-u.html) records how the second is already visible in the fit.

## What a Neutrino Mass Costs

**The addition.** The minimal content has no right-handed neutrino, so the count is nineteen. Oscillation requires mass, and [the PMNS article](the-pmns-matrix-and-lepton-mixing.html) established the parameter count of the lepton mixing matrix:

| Addition | Count | Running total |
|---|---|---|
| Three neutrino masses | $3$ | $22$ |
| Three lepton mixing angles | $3$ | $25$ |
| One Dirac phase | $1$ | $26$ |
| Two Majorana phases, if Majorana | $2$ | $27$ |

**The convention and the two totals.**

| Case | Count | With $\theta_{\mathrm{QCD}}=0$ |
|---|---|---|
| Dirac neutrinos | $26$ | $25$ |
| Majorana neutrinos | $27$ | $26$ |

So the model's parameter count is $26$ or $27$, and the difference is exactly the question of the neutrino's nature. This is the sharpest case in the corpus where a *count* is a physical discriminator: the two numbers are not conventions, they are two different theories, and the measurement of $m_{\beta\beta}$ distinguishes them.

**What the addition costs the framework.** Nothing and everything. Nothing, because the framework already hosts the Majorana condition — [the neutrino article](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) constructs it — so no new algebraic machinery is needed. Everything, because seven or eight new numbers are added to a list the framework fixes none of, taking the imported share from $86.4\%$ to $19/25=76\%$ or $19/26=73\%$ *of the model's own count*, while the framework's three stay three.

**The right way to state the comparison.** Not "the framework fixes none of twenty-seven" but "the framework fixes none of nineteen, and the seven that the neutrino adds are also unfixed, and their number is itself an open question." The second sentence carries information the first does not.

## The Over-determination, Quantified

**The gap between parameters and observables.** Nineteen parameters, and the model survives a number of measurements far larger than nineteen. That gap is the model's testability, and it can be measured in a specific case: [the closure article](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html) used **five** independent measurements to determine **two** parameters $(\bar\rho,\bar\eta)$ of the unitarity triangle, leaving **three** degrees of freedom. Three over-determination is what made the closure test a test.

**The general shape.**

| Quantity | Count |
|---|---|
| Parameters of the model | $19$ |
| Parameters of the flavour block | $13$ |
| Independent measurements constraining them | several hundred |
| Degrees of over-determination | the difference |

**Why over-determination is the framework's problem and not the model's.** A model with more parameters than measurements is unfalsifiable. The Standard Model is the opposite: it has nineteen parameters and is constrained from every side, which is why a $0.3\%$ closure in $R_t$ is informative. Any framework that wants to replace it must do better on the same measurements, and "better" is measured in the same currency: a smaller count with the same predictions, or the same count with more predictions.

**The measure this article proposes.** For any candidate framework, print two numbers: how many parameters it has, and how many of its predictions are not shared with the Standard Model. The corpus's answer for the biquaternionic framework is uncomfortable and exact:

| Candidate | Parameters | Predictions not shared with the Standard Model |
|---|---|---|
| Standard Model | $19$ | — |
| Biquaternionic framework | $19+3=22$ | $0$ |

That table is the boundary in one line. The framework's value is not in the second column; it is in the *derivability structure* of the first, and a reader who wants a predictive rival will not find one here.

## The Test Applied to the Corpus's Own Proposals

**The question the article exists to make askable.** For every proposal in the corpus that touches a parameter, which of the nineteen does it fix, and at which grade?

| Proposal | Entry touched | Grade claimed | Grade justified |
|---|---|---|---|
| The spin–mass formula | 1–9 | Relation | Relation among ratios, scale free; not a value |
| The gauge principle's $ϙ$ | 14–16 | Arena | Arena; no relation to a second coupling |
| The theta-vacuum construction | 17 | Arena | Arena; no value, no mechanism for smallness |
| The CKM as a flavour-factor operator | 10–13 | Arena | Arena; the group and the phase's necessity, not the point |
| The PMNS as the same operator | 10–13 (leptons) | Arena | Arena; and the count $4$ or $6$ as a discriminator |
| The condensate and the trace anomaly | 18 | None | No scale mechanism; the QCD case is imported |
| The Skyrme soliton | 1–9 | None | Ratios within a truncation, not parameters |
| The ceiling | — | Constraint | Forbids a $\mathbb{B}$ colour triplet, which forbids nothing among the nineteen |

**What the table shows.** One relation, of a restricted kind. Five arenas. Zero values. And one constraint that constrains the framework rather than the model. The table is the honest answer to "what does the framework fix", and it is the table the three agendas could not print before the nineteen articles existed.

**The row that deserves a second look.** The ceiling row is the only one where the framework *forbids* something, and what it forbids is a representation, not a number. That is worth stating precisely, because a constraint that forbids no parameter is not a constraint on the model: the model's nineteen numbers are untouched by the absence of a $\mathbb{B}$ triplet. The ceiling is a statement about what the framework can build, and the building it forbids is one the model does not require.

## What Would Have to Be True for the Count to Fall

**The four machines, and which are missing.**

| Machine | Would fix | Present? |
|---|---|---|
| A spectral principle | Entries 1–9, 19 ($10$ of $19$) | No. The operators exist; the spectrum does not follow |
| A scale-generating mechanism | Entry 18 | No. The QCD case is imported and non-perturbative |
| A flavour principle | Entries 10–13 ($4$) | No. The group is supplied; the point is measured |
| A coupling relation | Entries 14–16 ($3$) | No. $ϙ$ is free and single |

**The largest prize is the spectral one.** A principle fixing the ten mass-like entries would take the count from $19$ to $9$ — a reduction of more than half — and it would be the single most consequential result available to any framework. It is also the hardest, for a reason the corpus has already established: a spectrum is a property of an operator on an infinite-dimensional space, and [the ceiling article](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) established that the algebra's modules have dimensions the physics does not use. A spectral principle would have to live somewhere the algebra does not reach.

**The cheapest prize is the coupling relation.** Three couplings, one of which is the algebra's own $ϙ$. A relation $g_{\mathrm Y}=f(g)$ would be grade two, would reduce the count by one, and would be testable at the per-mille level by the electroweak fit. No such relation exists in the corpus, and the gauge article states why: the central charge is free and nothing binds it to a second one.

**What the corpus should not claim.** That any of the four machines is "almost" there. The four are absent, and the honest form of the sentence is: the framework supplies the *arena* for four of the nineteen, the *operator* for nine more, and nothing for two, and the fixing of any of them requires machinery the articles have named and not built.

## What the Framework Supplies

**The arena, the operator, and the ledger.**

**Supplied.** The group $\mathrm{U}(3)$ on the flavour factor, with the count $4$ following from it. The connection and a free normalisation $ϙ$, which is the shape of a coupling. The central phase, which is the shape of $\theta_{\mathrm{QCD}}$. The mass operator and the mass matrices, which are the shape of an eigenvalue. Five arenas, and the count of arenas is the framework's one positive number in this article.

**Not supplied, by kind.** A spectral principle. A scale-generating mechanism. A flavour principle. A coupling relation. These are the four machines, and all four are missing.

**The ledger.**

| Item | Status |
|---|---|
| The nineteen, with values and schemes | **Imported** from the content article; regrouped and re-typed here |
| The sector split $13+3+1+2$ | **Computed** here |
| The share $13/19=68.4\%$ | **Computed** here |
| $\lambda=0.1291$, $\mu=88.5$ GeV | **Computed** here from $M_H$ and $v$ |
| The typology into five kinds | **This article's** classification |
| The counts $8$, $9$, $2$ and their shares | **Computed** here |
| The framework's three parameters | **Imported** from the gauge and massive-equation articles |
| $19+3=22$, imported share $86.4\%$ | **Computed** here |
| The one unit and the eighteen ratios | **This article's** counting argument |
| $m_t/m_e=3.4\times10^{5}$, $v/M_{\mathrm{Pl}}=2.0\times10^{-17}$ | **Computed** here |
| The neutrino addition, $26$ or $27$ | **Imported** count from the PMNS article; the totals computed here |
| The three grades of fixing | **This article's** framework of analysis |
| The over-determination, five measurements for two parameters | **Imported** from the closure article; the degrees of freedom counted here |
| The four machines | **This article's** classification |
| A spectral, scale, flavour or coupling principle | **Not available** |

**What this article does not do.** It does not derive a parameter, does not propose a mechanism for any of the four machines, and does not argue that the count should be different. It classifies, counts, and states the boundary in numbers that a reader can check against the source articles.

## Summary

The Standard Model has nineteen free parameters: nine fermion masses, four mixing parameters, three gauge couplings, the vacuum angle, the electroweak scale and the scalar mass. Three conventions give $18$, $19$, $19$; the list is stable. One unit is unobservable, so the physical content is **eighteen dimensionless ratios**.

The framework fixes **none** of the nineteen values, produces **one** relation of a restricted kind (ratios of masses, scale free), and supplies the **arena** for eight — the four mixing coordinates, the three coupling normalisations, the one central phase. Nine more are eigenvalues of operators it represents but cannot diagonalise, and two, $v$ and $M_H$, have no arena at all.

The shares are $42.1\%$ arena, $47.4\%$ eigenvalue, $10.5\%$ nothing. Flavour is $68.4\%$ of the count, so the boundary is concentrated where the algebra is emptiest.

The framework's own list is three — $ϙ$, $m$, $k_m$ — and it overlaps none of the nineteen. The total is twenty-two and the imported share $86.4\%$. A reformulation that adds parameters and fixes none is not more parsimonious; its defence is that its objects are geometric, not that its list is short.

A neutrino mass costs seven or eight, taking the count to $26$ or $27$, and that difference is a physical discriminator rather than a convention.

The model is over-determined — nineteen parameters against several hundred measurements, and a closure test with three degrees of freedom — which is why the frame can be tested at all. The framework's own score on the same measure is twenty-two parameters and zero predictions not shared with the model.

Four machines would reduce the count: a spectral principle (ten entries), a scale mechanism (one), a flavour principle (four), a coupling relation (three). All four are absent, and each has been named.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $v$ | Higgs expectation value, $246.22$ GeV |
| $M_H$ | Higgs mass, $125.09$ GeV |
| $\mu^2$, $\lambda$ | The two parameters of the scalar potential |
| $g_{\mathrm Y}$, $g$, $g_s$ | The three gauge couplings |
| $\theta_{\mathrm{QCD}}$ | The QCD vacuum angle |
| $\theta_{ij}$, $\delta$ | CKM angles and phase |
| $ϙ$ | The framework's central charge parameter |
| $m$, $k_m$ | Mass and constant of the massive field equation |
| $M_{\mathrm{Pl}}$ | Planck mass, $1.22\times10^{19}$ GeV |
| $\bar\rho$, $\bar\eta$ | The two parameters of the unitarity triangle |
| $m_{\beta\beta}$ | Effective Majorana mass |

## Further Reading

- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The table this article takes as its input, with values and schemes.
- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The arena for four of the nineteen, and why the phase cannot be removed.
- [The PMNS Matrix and Lepton Mixing](the-pmns-matrix-and-lepton-mixing.html). The seven or eight that a neutrino mass adds, and the count as a discriminator.
- [Meson Mixing, Rare Decays and the Unitarity Triangle as a Closure Test](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html). The over-determination measured: five measurements, two parameters.
- [The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form](the-spin-mass-formula-and-the-spectrum-of-elementary-particles-in-biquaternionic-form.html). The corpus's one attempt at the spectral machine, and its restriction to ratios.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). Why a spectral principle would have to live outside the algebra.
- [Hadron Structure from QCD: the Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html). What a scale-generation mechanism looks like, and why no finite order produces one.
- [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html). How the scalar mass enters a fit, and why $T$ is the parameter that measures the scale hierarchy.
- [Asymptotic Freedom and the Running of the Strong Coupling](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). What happens to a coupling at high scale, where the count meets its own consistency conditions.
- [The Theta Vacuum in Biquaternionic Form](the-theta-vacuum-in-biquaternionic-form.html). Entry 17 constructed, and why its smallness is a separate problem.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The conditions the content must satisfy, which constrain the entries the count does not contain.
