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
\underbrace{B-L}_{\text{eigenvalue fixed, charge lost at }M_C},\quad
\underbrace{T_{3L},T_{3R},Y}_{\text{broken at }M_W,\ M_C,\ M_W}.
\;}
$$

**The single idea.** Conservation and masslessness are the same condition. A generator that annihilates the vacuum gives a massless boson *and* a conserved charge, and a generator that does not gives a massive boson *and* a charge that is no longer a symmetry. So the table of conserved charges is the table of massless bosons read as quantum numbers, and there is nothing to compute twice. **No charge escapes the criterion, and $B-L$ looks as though it does.** Its boson is the $Z_R$, and its eigenvalue never moves; that is why it is easy to write as though it survived the transition. The $B-L$ section below shows that it does not, and that what survives in its place is $B$, by accident of the content.

**What the article establishes.** The criterion and its proof; the table of charges with the scale at which each is lost; the two charges that survive — colour and the electric charge — with the different senses in which they survive; the exact status of $B-L$; the reason $B$ and $L$ separately are not symmetries and why the proton is stable anyway; the charges that are accidents of the field content; and the anomalous combination.

**What the article does not establish.** No dynamics and no decay rate. The proton's stability is treated in [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html), and the sphaleron statement in [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html).

**Where the masses are.** [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html) lists the bosons. This article is the same list read as charges.

## The Criterion

**One condition, four equivalent statements, one proof.**

**1.1 The statement.** Let $Q$ be a gauge generator and $Ξ_0$ the vacuum. Then $Q$ generates a symmetry of the vacuum if and only if $QΞ_0=0$.

**1.2 The proof.** A symmetry of the vacuum means $e^{i\theta Q}Ξ_0=Ξ_0$ for all $\theta$, which for infinitesimal $\theta$ is $QΞ_0=0$. Conversely $QΞ_0=0$ integrates to the finite statement.

**1.3 The equivalence with masslessness.** The mass matrix is $M^{2}_{XY}=\operatorname{tr}([X,Ξ_0]^\dagger[Y,Ξ_0])$, so $QΞ_0=0$ is exactly the vanishing of the row and column of $Q$. Same equation, two readings: a conserved charge and a massless boson.

**1.4 The converse, and its warning.** A charge that does not annihilate the vacuum is not conserved. That is a strong statement: it says the corresponding current has a divergence proportional to the Goldstone field, and the charge is not a well-defined operator on the physical Hilbert space. The charge is not "approximately conserved"; it is not defined.

**1.5 What the criterion does not cover.** It applies to gauge charges, and it is silent about global symmetries that are not gauged. Those are discussed in §*The Charges That Are Merely Accidental*, and their status is different in kind.

## The Table of Charges and Their Fates

**Six charges, three fates.**

| charge | generator | exact above | exact below | lost at | reason |
|---|---|---|---|---|---|
| electric, $Q$ | $T_{3L}+Y$ | below $M_W$ only | at every scale below $M_W$ | never below $M_W$ | it annihilates both vevs |
| colour | $\mathfrak{su}(3)$ | at every scale | at every scale | never | $X e_t=0$ |
| $B-L$ | the surviving $\mathrm{SU}(4)$ Cartan | as a direction of $\mathrm{SU}(4)$ above $M_C$ | no | $M_C$ | the lepton line carries $B-L=-1$, so $[B-L,Ξ_0]\neq0$ |
| $T_{3R}$ | $\sigma^{3}/2$ | above $M_C$ | no | $M_C$ | the right line is a $T_{3R}$ eigenstate, not an eigenstate of the other two |
| $Y$ | $T_{3R}+\tfrac12(B-L)$ | above $M_W$ | no | $M_W$ | the left line breaks it |
| $T_{3L}$ | $\tau^{3}/2$ | above $M_W$ | no | $M_W$ | the left line is a $T_{3L}$ eigenstate |

**2.1 The reading.** Above its breaking scale each charge is exact and its boson is massless. Below it, the charge is not a symmetry and the boson is massive. There is no intermediate status.

**2.2 The apparent exception of $Q$.** $Q$ is written as a combination of $T_{3L}$ and $Y$, both of which are broken at $M_W$, and yet $Q$ survives. That is not a contradiction: the combination is the one direction that annihilates the vacuum, and the two ingredients annihilate it only in that combination. A sum of two broken generators can be unbroken; a single one cannot be.

**2.3 The rank statement.** At each step the rank of the conserved charge lattice is the rank of $\mathfrak h$: $3\to5\to4\to3$. The number of independent conserved Cartan charges is that rank, and it is why there are three at the bottom and not more. **The rank rises at the first step**, because the two weak $\mathrm{SU}(2)$ factors arrive with the doublet index and bring their Cartans; it falls back to four in the same vacuum, because the right factor is broken there; and it falls to three at $v$, because a broken $\mathrm{SU}(2)_L$ leaves a single abelian direction. **Rank five exists at $M_C$ and has no width.**

## Colour: Exact and Confined

**Three different senses of "survives", and colour has two of them.**

**3.1 Colour is exact.** $\mathfrak{su}(3)\subset\mathfrak h_i$ at every stage, so the eight colour charges are conserved at every scale. No step of the chain touches them.

**3.2 Colour is confined.** Conserved does not mean realised. The physical states are colour singlets, so no state carries a colour charge, and the conservation law is realised as the absence of coloured asymptotic states rather than as a selection rule among them.

**3.3 Why the two statements are compatible.** A conserved charge can be realised trivially on the physical spectrum. Colour is the standard example, and it is the reason "colour is conserved" and "there are no free quarks" are both true.

**3.4 The consequence for the model.** Because colour is a stabiliser at every scale, no step of the chain can make a coloured state light in a way that would show up as a free particle. The confinement statement is [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html).

## $B-L$: A Fixed Eigenvalue at Every Scale, a Charge Broken at $M_C$

**The charge that is the article's hardest case, because its number never moves while its symmetry does.**

**4.1 Inside $\mathrm{SU}(4)$ it is a direction; the colour step promotes it to a factor with no interval attached.** $B-L$ is a Cartan generator of the simple group and carries no coupling of its own, so there is no scale above $M_C$ at which it is a separate gauge symmetry. The colour half of the transition leaves it in the residual group, $\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}$ at rank five and dimension fifteen ([Matching at $M_C$](matching-at-m-c-the-four-quantities-that-cross-and-where-the-masses-come-from.html)). **That group has no interval of scales**: the doublet half of the same vacuum breaks it at once (§4.2), so the factor is a statement about the residual algebra and never about a range of energies.

**4.2 The transition does two things to it, and they must be told apart.** The colour part of the vacuum, $iD$, commutes with $B-L$: the corner is in the stabiliser, so the six generators that become heavy do not include it, and the sextet's $\pm\tfrac43$ are eigenvalues of a generator the colour step leaves alone. **The doublet part of the same vacuum does not commute with it.** That vacuum lies on the lepton line, where $B-L=-1$ and $T_{3R}=+\tfrac12$, so $[B-L,Ξ_0]=-Ξ_0\neq0$. **By the criterion of §*The Criterion*, $B-L$ is not conserved below $M_C$** — and by §1.4 it is not approximately conserved either: it is not defined.

**4.3 What does annihilate the vacuum is hypercharge.** $Y=T_{3R}+\tfrac12(B-L)$ gives $\tfrac12-\tfrac12=0$ on that line, so $Y$ is the unbroken direction and $B-L$ alone is not. Below $M_C$ the exact gauge charges are colour, $Y$, and — below $v$ — $Q$. **The charge that survives in $B-L$'s place does so by accident**: $B$, because the renormalisable Lagrangian contains no operator that violates it once the leptoquarks are gone (§*The Charges That Are Merely Accidental*).

**4.4 The eigenvalue is what does not move, and it is a different statement.** $B-L$ takes the same values at every scale — $-1$ on the lepton line, $\tfrac13$ on the three colour lines — because an eigenvalue is a property of an array and not of the vacuum, and no mixing between $W^{3}_{L}$, $W^{3}_{R}$ and $B'$ changes a diagonal entry of $B'$. **"The chain never renormalises $B-L$" is true; "$B-L$ is conserved below $M_C$" is false**, and the two are easy to run together because both are sentences about a number that stays put.

**4.5 The breaking is wanted twice over, and it costs no Goldstone.** A Majorana mass for the right-handed neutrino carries $B-L=-2$, so it needs a vacuum that breaks the charge — and the transition supplies one. **That is the seesaw's licence, and it is the same vev that breaks $\mathrm{SU}(2)_R$** ([The Seesaw Mechanism](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html)). And because the broken direction was a direction of a *gauge* group above $M_C$, the would-be Goldstone is eaten: it is the longitudinal mode of the $Z_R$, whose mass $\tfrac58g^2v_C^2$ is the neutral sector's ([The Weak Sector Below $M_C$](the-weak-sector-below-m-c-three-neutrals-a-diagonal-charged-pair-and-the-bidoublet.html)).

**4.6 Compared with the Standard Model.** There $B-L$ is an accidental global symmetry from the start and is never gauged, and it is broken only by the Weinberg operator at dimension five. **Here it is a gauge direction above $M_C$, broken at $M_C$, and accidental below it** — the exact opposite order of statuses, with the same low-energy consequence, because the residual violation below $M_C$ is again of dimension five and suppressed by the same scale.

## $B$ and $L$ Separately

**The charges that are not symmetries, and the reason the proton is stable anyway.**

**5.1 The violation.** Above $M_C$ the leptoquark vertex couples a quark to a lepton, and the gauge field that mediates it carries $B-L=\pm\tfrac43$ and no baryon number. So $B$ alone and $L$ alone are explicitly broken by the gauge coupling; above $M_C$ only $B-L$ is a symmetry of the gauge sector — and the vacuum breaks even that one, at the same scale, by §4.2.

**5.2 The size of the violation.** Below $M_C$ the mediator is gone and the violation appears as dimension-six operators suppressed by $1/M_C^{2}$. So $B$ and $L$ are violated at low energy by an amount that is small because $M_C$ is large, not because a symmetry protects them.

**5.3 Why there is no proton decay.** A proton decay operator needs a mediator that couples two quarks: a diquark. The gauge leptoquarks carry $B-L=\pm\tfrac43$, and a diquark coupling would need $B-L=\pm\tfrac23$, because two quarks have $B-L=\tfrac23$. The charge forbids the vertex, and the model contains no scalar with the right $B-L$ to supply it. The proton's stability is therefore a consequence of the charge of the leptoquarks, not of a baryon-number symmetry.

**5.4 The honest qualification.** "No proton decay" means no dimension-six gauge-mediated decay in the minimal content. Operators of higher dimension, or new scalars, could change it, and the bound on $M_C$ from the operators that do exist is in [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html).

## The Charges That Are Merely Accidental

**Not every conserved number is a symmetry of the vacuum.** Three examples, and one warning.

**6.1 What "accidental" means.** A charge that is conserved because the renormalisable Lagrangian contains no operator violating it, given the field content and the gauge symmetries. It is not imposed; it follows.

**6.2 The examples, and one that is not one.** Baryon number below $M_C$ is accidental: no renormalisable operator violates it once the leptoquarks are removed, and the leading violation is of dimension six. **Lepton number is not accidental here.** The right-handed neutrino is a gauge singlet below $M_C$, its Majorana mass carries $B-L=-2$, and the vacuum has already broken the charge that forbade it — so $L$ is broken at dimension three, with no suppression at all. **That is the seesaw, and it is why the neutrino mass is the one place the framework's broken charge shows.**

**6.3 The warning.** An accidental charge has no reason to survive a change of content, and a model that relies on one is relying on the absence of a term rather than on a symmetry. **The proton's stability rests on one of these**, on $B$ below $M_C$, and §*$B$ and $L$ Separately* says why the resting is nevertheless firm: the forbidden vertex is forbidden by $B-L$, and $B-L$ is a direction of the gauge group above the scale that would supply a diquark.

**6.4 The flavour charges.** The generation numbers are accidental in the same sense, and their violation is the Yukawa sector's business: [The Yukawa Sector of the $\mathrm{SU}(4)$ Model: One Matrix and Its Diagonalisation](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html).

## The Anomalous Combination

**One combination is violated by non-perturbative effects, and it is not $B-L$.**

**7.1 The statement.** In the Standard Model the combination $B+L$ is violated by sphalerons while $B-L$ is not. The same holds here below $M_C$, because the field content and the gauge group restricted to the Standard-Model factors are the same. **The anomalous statement is about the coefficients of the currents, not about the vacuum**, so the breaking of §4.2 does not touch it: the triangle coefficient of $B-L$ vanishes whether or not a vev carries the charge. What the breaking does change is the *kind* of protection — accidental rather than gauge — and the leading explicit violation is the dimension-five Weinberg operator, suppressed by the transition scale.

**7.2 Why $B-L$ escapes.** Its current has vanishing anomaly coefficients. The triangle coefficient of $B-L$ cancels inside a generation for the same reason every other anomaly does, the trace $\operatorname{tr}_{\mathbf4}(B-L)=0$ over the four entries of the carrier. So the current is conserved even where it is only global, and the sphaleron has nothing to act on. Above $M_C$ the direction is inside a simple group and there is no separate current to discuss.

**7.3 Why it matters.** Sphaleron violation of $B+L$ with $B-L$ conserved is the mechanism that makes leptogenesis possible and that erases a $B+L$ asymmetry. Its absence for $B-L$ is what leaves an asymmetry to survive. **Below $M_C$ the conservation is exact at the level of the anomaly and approximate at the level of the operators**, and the second half is the qualification §4.2 puts on the first. The details are [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html).

## The Checks

**Six checks.**

| check | computation | result |
|---|---|---|
| the criterion | $QΞ_0=0$ | equivalent to a zero row of $M^{2}$ |
| the rank | $3\to5\to4\to3$ | two gained and one lost at $M_C$, one lost at $M_W$ |
| the two steps at $M_W$ | $T_{3L}$ and $Y$ broken, $Q$ conserved | a sum of two broken generators can be unbroken |
| the $B-L$ of the leptoquarks | $\pm\tfrac43$ against $\pm\tfrac23$ for a diquark | the diquark vertex is forbidden |
| the $B-L$ status | a gauge direction above $M_C$, broken at $M_C$ | the eigenvalue never changes; the charge is lost |
| the anomaly of $B-L$ | $\operatorname{tr}_{\mathbf4}(B-L)=0$ | no anomalous violation |

## Distinctions That Are Easy to Lose

**Three pairs.**

**8.1 Conserved and realised.** Colour is conserved and has no coloured asymptotic states. A charge can be exact and act trivially on the spectrum.

**8.2 Gauged, broken, accidental.** $B-L$ is gauged above $M_C$ and broken at $M_C$; $B$ is accidental below $M_C$ and violated at dimension six; $L$ is broken at dimension three by the right-handed neutrino's mass. **Three statuses, and the third is the one that produces a measured number**, because a dimension-three term is not suppressed (the seesaw article has it).

**8.3 Broken and violated.** A broken gauge charge is not defined on the physical Hilbert space. A violated global charge is defined and its non-conservation is a computable rate. The words are not interchangeable, and §*The Criterion* is where the difference is made.

## Summary

**The criterion.** A gauge charge is conserved exactly when its generator annihilates the vacuum — the same condition as a massless boson.

**The survivors.** $Q$ and colour, and with them $B$ by accident of the content. **$B-L$ is not one of them**: its eigenvalue is fixed at every scale, but the transition that breaks $\mathrm{SU}(2)_R$ breaks it, and the Majorana neutrino mass is the price and the payoff.

**The casualties.** $T_{3R}$ and $B-L$ at $M_C$; $T_{3L}$ and $Y$ at $M_W$; $L$ just below $M_C$, through the right-handed neutrino's mass. **$B$ is never one of them** — it is not broken at all, and it is accidental, which is a weaker thing than conserved.

**The proton.** Stable because the leptoquarks carry $B-L=\pm\tfrac43$ and cannot couple two quarks, not because $B$ is a symmetry.

**The anomaly.** $B+L$ violated by sphalerons, $B-L$ not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q$ | the electric charge, $T_{3L}+Y$ |
| $B-L$ | baryon number minus lepton number; a direction of $\mathrm{SU}(4)$, broken at $M_C$ |
| $T_{3L}$, $T_{3R}$, $Y$ | the three broken Cartan charges |
| $\mathfrak h$ | the algebra of conserved charges at a given stage |
| $M^{2}_{XY}$ | the gauge mass matrix whose kernel is $\mathfrak h$ |
| $\Delta B$, $\Delta L$ | the changes a leptoquark vertex would produce |

## Further Reading

- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The same criterion read as a mass spectrum.
- [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html). The $B-L$ of the leptoquarks and the absent diquark channel.
- [Charge Quantisation from the Fourth Colour: One Trace, One Third](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). Where the charge lattice comes from.
- [What the Standard Model Does Not Explain: Dark Matter, Baryogenesis and the Sphaleron](what-the-standard-model-does-not-explain-dark-matter-baryogenesis-and-the-sphaleron.html). The anomalous combination and its consequences.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$: The Colour Wall, Restated](quantum-chromodynamics-as-the-residual-of-su4.html). Colour exact and confined.
