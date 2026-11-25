# __The Quantum Numbers Below the Breaking: Colour, $B-L$, Weak Isospin and the Electric Charge__

## Introduction

**The question.** Which charges survive the chain exactly, which survive only above a scale, and by what criterion? Is there one rule that decides all of them?

**The answer.**

$$
\boxed{\;
\text{a gauge charge is conserved}\iff\text{its generator annihilates the vacuum}
\iff\text{it is in }\mathfrak h
\iff\text{its boson is massless},
\;}
$$

$$
\boxed{\;
\underbrace{Q}_{\text{exact}},\quad
\underbrace{\text{colour}}_{\text{exact, confined}},\quad
\underbrace{B-L}_{\text{exact at every scale as a number}},\quad
\underbrace{T_{3L},T_{3R},Y}_{\text{broken at }M_W, M_R, M_W}.
\;}
$$

**The single idea.** Conservation and masslessness are the same condition. A generator that annihilates the vacuum gives a massless boson *and* a conserved charge, and a generator that does not gives a massive boson *and* a charge that is no longer a symmetry. So the table of conserved charges is the table of massless bosons read as quantum numbers, and there is nothing to compute twice. The one charge that escapes the criterion is $B-L$ below $M_R$: it stays exact while its boson has gone into the massive $Z_R$, because it is gauged above $M_R$ and only global below.

**What the article establishes.** The criterion and its proof; the table of charges with the scale at which each is lost; the two charges that survive — colour and the electric charge — with the different senses in which they survive; the exact status of $B-L$; the reason $B$ and $L$ separately are not symmetries and why the proton is stable anyway; the charges that are accidents of the field content; and the anomalous combination.

**What the article does not establish.** No dynamics and no decay rate. The proton's stability is treated in [The Leptoquarks of the Four Colours Left–Right Model: Six States, One Bound, and Why Proton Decay Does Not Bite](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html), and the sphaleron statement in [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html).

**Where the masses are.** [The Unbroken Subgroup of the Four Colours Left–Right Model: Nine Massless Generators, Twelve That Acquire Mass](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html) lists the bosons. This article is the same list read as charges.

## The Criterion

**One condition, four equivalent statements, one proof.**

**1.1 The statement.** Let $Q$ be a gauge generator and $\Phi_0$ the vacuum. Then $Q$ generates a symmetry of the vacuum if and only if $Q\Phi_0=0$.

**1.2 The proof.** A symmetry of the vacuum means $e^{i\theta Q}\Phi_0=\Phi_0$ for all $\theta$, which for infinitesimal $\theta$ is $Q\Phi_0=0$. Conversely $Q\Phi_0=0$ integrates to the finite statement.

**1.3 The equivalence with masslessness.** The mass matrix is $M^{2}_{XY}=\operatorname{tr}([X,\Phi_0]^\dagger[Y,\Phi_0])$, so $Q\Phi_0=0$ is exactly the vanishing of the row and column of $Q$. Same equation, two readings: a conserved charge and a massless boson.

**1.4 The converse, and its warning.** A charge that does not annihilate the vacuum is not conserved. That is a strong statement: it says the corresponding current has a divergence proportional to the Goldstone field, and the charge is not a well-defined operator on the physical Hilbert space. The charge is not "approximately conserved"; it is not defined.

**1.5 What the criterion does not cover.** It applies to gauge charges, and it is silent about global symmetries that are not gauged. Those are discussed in §*The Charges That Are Merely Accidental*, and their status is different in kind.

## The Table of Charges and Their Fates

**Six charges, three fates.**

| charge | generator | exact above | exact below | lost at | reason |
|---|---|---|---|---|---|
| electric, $Q$ | $T_{3L}+Y$ | below $M_W$ only | at every scale below $M_W$ | never below $M_W$ | it annihilates both vevs |
| colour | $\mathfrak{su}(3)$ | at every scale | at every scale | never | $X e_t=0$ |
| $B-L$ | the surviving $\mathrm{SU}(4)$ Cartan | as a factor above $M_R$ | as an accidental global charge below $M_R$ | never as a quantum number | no vev carries $B-L$ alone |
| $T_{3R}$ | $\sigma^{3}/2$ | above $M_R$ | no | $M_R$ | the right line is a $T_{3R}$ eigenstate, not an eigenstate of the other two |
| $Y$ | $T_{3R}+\tfrac12(B-L)$ | above $M_W$ | no | $M_W$ | the left line breaks it |
| $T_{3L}$ | $\tau^{3}/2$ | above $M_W$ | no | $M_W$ | the left line is a $T_{3L}$ eigenstate |

**2.1 The reading.** Above its breaking scale each charge is exact and its boson is massless. Below it, the charge is not a symmetry and the boson is massive. There is no intermediate status.

**2.2 The apparent exception of $Q$.** $Q$ is written as a combination of $T_{3L}$ and $Y$, both of which are broken at $M_W$, and yet $Q$ survives. That is not a contradiction: the combination is the one direction that annihilates the vacuum, and the two ingredients annihilate it only in that combination. A sum of two broken generators can be unbroken; a single one cannot be.

**2.3 The rank statement.** At each step the rank of the conserved charge lattice is the rank of $\mathfrak h$: $5\to5\to4\to3$. The number of independent conserved Cartan charges is that rank, and it is why there are three at the bottom and not more.

## Colour: Exact and Confined

**Three different senses of "survives", and colour has two of them.**

**3.1 Colour is exact.** $\mathfrak{su}(3)\subset\mathfrak h_i$ at every stage, so the eight colour charges are conserved at every scale. No step of the chain touches them.

**3.2 Colour is confined.** Conserved does not mean realised. The physical states are colour singlets, so no state carries a colour charge, and the conservation law is realised as the absence of coloured asymptotic states rather than as a selection rule among them.

**3.3 Why the two statements are compatible.** A conserved charge can be realised trivially on the physical spectrum. Colour is the standard example, and it is the reason "colour is conserved" and "there are no free quarks" are both true.

**3.4 The consequence for the model.** Because colour is a stabiliser at every scale, no step of the chain can make a coloured state light in a way that would show up as a free particle. The confinement statement is [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html).

## $B-L$: Exact as a Quantum Number at Every Scale

**The one charge the chain never removes, with a change of status in the middle.**

**4.1 Above $M_R$, it is gauged.** Between $M_C$ and $M_R$, $B-L$ is a factor, $\mathrm{U}(1)_{B-L}$, with its own boson and its own coupling. That is the content of the first step: $15-9=6$ generators are broken and no $B-L$ direction is among the six, so the charge is exact by the criterion of §*The Criterion*.

**4.2 Above $M_C$, it is a direction.** $B-L$ is a Cartan generator inside the simple $\mathrm{SU}(4)$ and carries no independent coupling. It becomes a charge of its own at the first step and not before.

**4.3 Below $M_R$, it is neither, and it survives anyway.** The second step absorbs $B-L$ into hypercharge, $Y=T_{3R}+\tfrac12(B-L)$, so below $M_R$ there is no $\mathrm{U}(1)_{B-L}$ in the gauge group. But no renormalisable operator violates $B-L$, because every field carries it and the only would-be violators — the leptoquarks — are gone. So below $M_R$ the charge is an *accidental* global symmetry: exact in perturbation theory, and exact because nothing is written that breaks it, not because a gauge invariance protects it. The distinction is the one in §*The Charges That Are Merely Accidental*, and it is the reason "the chain never breaks $B-L$" and "$B-L$ is gauged below $M_C$" are both true.

**4.4 The consequence, stated in three registers.** As a quantum number, exact at every scale. As a gauge symmetry, exact above $M_R$ only. As a protection, none below $M_R$: a non-renormalisable operator can violate it, and the leading one is of dimension six, suppressed by $1/M_C^{2}$ or by whatever scale closes the minimal content. Compare the Standard Model, where $B-L$ is a global symmetry from the start and never gauged; here the middle of the chain upgrades it to a gauge symmetry and the bottom of the chain hands it back as a global one.

## $B$ and $L$ Separately

**The charges that are not symmetries, and the reason the proton is stable anyway.**

**5.1 The violation.** Above $M_C$ the leptoquark vertex couples a quark to a lepton, and the gauge field that mediates it carries $B-L=\pm\tfrac43$ and no baryon number. So $B$ alone and $L$ alone are explicitly broken by the gauge coupling; only $B-L$ is a symmetry of the gauge sector.

**5.2 The size of the violation.** Below $M_C$ the mediator is gone and the violation appears as dimension-six operators suppressed by $1/M_C^{2}$. So $B$ and $L$ are violated at low energy by an amount that is small because $M_C$ is large, not because a symmetry protects them.

**5.3 Why there is no proton decay.** A proton decay operator needs a mediator that couples two quarks: a diquark. The gauge leptoquarks carry $B-L=\pm\tfrac43$, and a diquark coupling would need $B-L=\pm\tfrac23$, because two quarks have $B-L=\tfrac23$. The charge forbids the vertex, and the model contains no scalar with the right $B-L$ to supply it. The proton's stability is therefore a consequence of the charge of the leptoquarks, not of a baryon-number symmetry.

**5.4 The honest qualification.** "No proton decay" means no dimension-six gauge-mediated decay in the minimal content. Operators of higher dimension, or new scalars, could change it, and the bound on $M_C$ from the operators that do exist is in [The Leptoquarks of the Four Colours Left–Right Model: Six States, One Bound, and Why Proton Decay Does Not Bite](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html).

## The Charges That Are Merely Accidental

**Not every conserved number is a symmetry of the vacuum.** Three examples, and one warning.

**6.1 What "accidental" means.** A charge that is conserved because the renormalisable Lagrangian contains no operator violating it, given the field content and the gauge symmetries. It is not imposed; it follows.

**6.2 The examples.** Lepton number below $M_C$ is accidental: no renormalisable operator violates it once the leptoquarks are removed. Baryon number is accidental for the same reason. Both are violated by dimension-six operators, so both are approximate.

**6.3 The warning.** An accidental charge has no reason to survive a change of content, and a model that relies on one is relying on the absence of a term rather than on a symmetry. $B-L$ is not accidental here — it is gauged — and that is the difference that matters for the proton.

**6.4 The flavour charges.** The generation numbers are accidental in the same sense, and their violation is the Yukawa sector's business: [The Yukawa Sector of the $\mathrm{SU}(4)$ Model: One Matrix and Its Diagonalisation](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html).

## The Anomalous Combination

**One combination is violated by non-perturbative effects, and it is not $B-L$.**

**7.1 The statement.** In the Standard Model the combination $B+L$ is violated by sphalerons while $B-L$ is not. The same holds here below $M_C$, because the field content and the gauge group restricted to the Standard-Model factors are the same.

**7.2 Why $B-L$ escapes.** Its current has vanishing anomaly coefficients. The triangle coefficient of $B-L$ cancels inside a generation for the same reason every other anomaly does, the trace $\operatorname{tr}_{\mathbf4}(B-L)=0$ of [The Fermions After the Breaking: Three Colours and a Lepton Line, Two Weak Doublets, the Electric Charges](the-fermions-after-the-breaking-three-colours-and-a-lepton-line-two-weak-doublets-the-electric-charges.html). So the current is conserved even where it is only global, and the sphaleron has nothing to act on. Above $M_C$ the direction is inside a simple group and there is no separate current to discuss.

**7.3 Why it matters.** Sphaleron violation of $B+L$ with $B-L$ conserved is the mechanism that makes leptogenesis possible and that erases a $B+L$ asymmetry. Its absence for $B-L$ is what leaves an asymmetry to survive. The details are [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html).

## The Checks

**Five checks.**

| check | computation | result |
|---|---|---|
| the criterion | $Q\Phi_0=0$ | equivalent to a zero row of $M^{2}$ |
| the rank | $5\to5\to4\to3$ | one conserved Cartan charge lost at $M_R$, one at $M_W$ |
| the two steps at $M_W$ | $T_{3L}$ and $Y$ broken, $Q$ conserved | a sum of two broken generators can be unbroken |
| the $B-L$ of the leptoquarks | $\pm\tfrac43$ against $\pm\tfrac23$ for a diquark | the diquark vertex is forbidden |
| the $B-L$ status | gauged above $M_R$, global below | the quantum number never changes |
| the anomaly of $B-L$ | $\operatorname{tr}_{\mathbf4}(B-L)=0$ | no anomalous violation |

## Distinctions That Are Easy to Lose

**Three pairs.**

**8.1 Conserved and realised.** Colour is conserved and has no coloured asymptotic states. A charge can be exact and act trivially on the spectrum.

**8.2 Gauged and accidental.** $B-L$ is gauged and exact; $B$ and $L$ are accidental and violated at dimension six. The two statuses differ by more than a factor.

**8.3 Broken and violated.** A broken gauge charge is not defined on the physical Hilbert space. A violated global charge is defined and its non-conservation is a computable rate. The words are not interchangeable, and §*The Criterion* is where the difference is made.

## Summary

**The criterion.** A gauge charge is conserved exactly when its generator annihilates the vacuum — the same condition as a massless boson.

**The survivors.** $Q$, colour, and $B-L$ — the last as a quantum number at every scale, gauged only in the middle of the chain.

**The casualties.** $T_{3R}$ at $M_R$; $T_{3L}$ and $Y$ at $M_W$; $B$ and $L$ at every scale, as accidental charges only.

**The proton.** Stable because the leptoquarks carry $B-L=\pm\tfrac43$ and cannot couple two quarks, not because $B$ is a symmetry.

**The anomaly.** $B+L$ violated by sphalerons, $B-L$ not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q$ | the electric charge, $T_{3L}+Y$ |
| $B-L$ | baryon number minus lepton number, gauged below $M_C$ |
| $T_{3L}$, $T_{3R}$, $Y$ | the three broken Cartan charges |
| $\mathfrak h$ | the algebra of conserved charges at a given stage |
| $M^{2}_{XY}$ | the gauge mass matrix whose kernel is $\mathfrak h$ |
| $\Delta B$, $\Delta L$ | the changes a leptoquark vertex would produce |

## Further Reading

- [The Unbroken Subgroup of the Four Colours Left–Right Model: Nine Massless Generators, Twelve That Acquire Mass](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html). The same criterion read as a mass spectrum.
- [The Leptoquarks of the Four Colours Left–Right Model: Six States, One Bound, and Why Proton Decay Does Not Bite](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html). The $B-L$ of the leptoquarks and the absent diquark channel.
- [Charge Quantisation from the Fourth Colour: One Trace, One Third](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). Where the charge lattice comes from.
- [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html). The anomalous combination and its consequences.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html). Colour exact and confined.
- [The Fermions After the Breaking: Three Colours and a Lepton Line, Two Weak Doublets, the Electric Charges](the-fermions-after-the-breaking-three-colours-and-a-lepton-line-two-weak-doublets-the-electric-charges.html). The charges carried by each state.
