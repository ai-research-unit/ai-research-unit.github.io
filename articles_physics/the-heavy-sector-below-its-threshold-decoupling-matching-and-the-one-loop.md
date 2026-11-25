# __The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop__

## Introduction

**The question.** The chain removes twelve gauge fields and a scalar sector at two thresholds. Is the removal exact, or is it an approximation? What happens to the effects of the fields that are removed, and what is computed when one says "the couplings are matched at one loop"?

**The answer.**

$$
\boxed{\;
\mathcal L_{\text{eff}}\big|_{\mu<M}=\mathcal L_{\text{light}}+\sum_{n\ge 4}\frac{1}{M^{n-4}}\,c_n\,\mathcal O_n,
\qquad
g_i^{\text{light}}(M)=g_i^{\text{heavy}}(M)+\frac{1}{16\pi^{2}}\,\Delta_i+\dots
\;}
$$

**The single idea.** Two operations are at work and only one of them is an approximation. The breaking is exact: the vacuum is a fact, and the group below a scale is the stabiliser, not an approximation to the group above it. The truncation is approximate: removing a field of mass $M$ costs powers of $E/M$. Matching is where the two descriptions are made to agree, and it is exact order by order in the loop expansion — the approximation is in the truncation, never in the matching.

**What the article establishes.** The distinction between breaking and truncation; the form of the decoupling expansion; the inventory of what leaves at each threshold; the structure of tree-level and one-loop matching; the way the truncation's error is estimated; and the reason the minimal content's running fails.

**What the article does not establish.** No numerical result of the running. The failure of the minimal content is stated here and computed in [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html), which owns every number.

**Where the neighbours are.** The derivative that is matched is [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html). The scales are [The Threshold Scales: One Transition at $M_C$, One Measured Weak Scale, and What Would Fix $M_C$](the-threshold-scales-mc-mw-and-what-would-fix-them.html). The one-loop machinery in the algebra is [The Effective Potential and the One-Loop Correction in Biquaternionic Form](the-effective-potential-and-the-one-loop-correction-in-biquaternionic-form.html).

## Two Operations That Are Often Confused

**A fact and an approximation.** The whole article turns on keeping them apart.

**1.1 The breaking.** The vacuum takes a value; the group that leaves it fixed is the unbroken group; the fields whose generators do not annihilate it acquire mass. This is exact. It holds whether or not anyone computes a correction, and no power of $E/M$ enters it.

**1.2 The truncation.** At energies far below $M$, a field of mass $M$ cannot be produced, so it is removed from the list of dynamical fields. This is approximate: the removal changes the predictions by terms of order $E^{2}/M^{2}$, and the expansion in those terms is the effective Lagrangian.

**1.3 The confusion.** "Below $M_C$ the group is $\mathrm{SU}(3)\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$" is exact. "Below $M_C$ a leptoquark does not exist" is shorthand for "the leptoquark is not a dynamical field of the truncated description". The first is a statement about the vacuum; the second about the description. Merging them produces the false claim that the breaking is approximate.

**1.4 Why the distinction has teeth.** If breaking were an approximation, the low-energy theory would be a fit with the breaking scale as a parameter. It is not: the low-energy group is fixed by the vacuum, and the only free parameters are the two scales and the couplings.

## What Decoupling Says, Exactly

**One theorem, one expansion, one caveat.**

**2.1 The statement.** Take a renormalisable theory with a heavy field of mass $M$ and a light sector. At energies $E\ll M$ every Green's function of light fields is reproduced, to any fixed order in $E/M$, by a local Lagrangian built from light fields only, with coefficients that depend on $M$ and on the heavy couplings.

**2.2 The form.** The coefficients are $c_n/M^{n-4}$ for an operator of dimension $n$. Dimension six gives $1/M^{2}$: the four-fermion terms left by the leptoquarks. Dimension five gives $1/M$: the Majorana mass of the neutrino, from the right doublet's vacuum at $M_C$.

**2.3 The caveat.** Decoupling as stated requires that the heavy mass comes from a vacuum and not from a hierarchy of couplings. Here it does: every heavy mass is a coupling times a vacuum value. A theory whose heavy mass came from a small coupling at a high scale would not decouple in this form, and that is the trap the phrase "the heavy fields decouple" hides.

**2.4 The third scale is different in kind.** At $M_W$ the removed fields are the $W$, the $Z$ and the top. Their masses are not all much greater than the energies of interest — the top is heavier than the $W$ by a factor of two — so the expansion in $E/M$ converges slowly and the top is often kept. The practice is standard and it is a truncation with a small parameter, not a breaking.

## The Three Thresholds and What Leaves at Each

**An inventory, with the operator each removal leaves behind.**

| threshold | what leaves | what remains of it | status of the removal |
|---|---|---|---|
| $M_C$ | six leptoquarks, the coloured components of $Ξ$; $\nu_R$'s Majorana mass | four-fermion operators with $\Delta B=\Delta L=\pm1$; the dimension-five operator for neutrino mass; the $1/M_C^{2}$ corrections to $W$ couplings | one breaking at one scale, truncated effects |
| $M_W$ | $W^{\pm}$, $Z$, the top, the Higgses | the four-fermion charged-current and neutral-current operators of the Fermi theory | exact breaking, slowly converging truncation |

**3.1 The transition.** The leptoquarks leave and their exchange becomes contact interactions. The same vacuum removes the six leptoquarks, and the neutrino's Majorana mass becomes a dimension-five operator — the seesaw. The bound on $M_C$ is the bound on those coefficients, and the diquark channel is the one that would give proton decay — with a suppression that makes it harmless, as [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html) shows.

**3.2 Why one removal and not two.** The leptoquarks and the Majorana mass leave at $M_C$ and not at a scale of their own, because the vacuum that gives them their mass is the vacuum that breaks the colour. **A reader who expects two removals will look for a second threshold that the content does not have.**

**3.3 The electroweak threshold.** The bosons leave and the theory becomes Fermi's. The removal is the most familiar and the least clean, because the top is close in mass.

**3.4 The order of the thresholds is the order of the chain.** The removals are nested: what leaves at $M_C$ is gone at $v$ too, and the description at $v$ is built from what survived the first removal. This nesting is why the chain reads as a descent and not as two parallel truncations.

## Matching: Tree Level and One Loop

**Where the two descriptions are made to agree.** Three statements of increasing precision.

**4.1 Tree level.** The couplings are equated at the threshold. At $M_C$ the single $\mathrm{SU}(4)$ coupling becomes two, the colour one and the $B-L$ one, both equal to $g_4$:

$$
g_s(M_C)=g_4(M_C),
\qquad
g_{B-L}(M_C)=g_4(M_C),
\qquad
g(M_C)=g_L(M_C).
$$

At the same scale the two neutral couplings combine into hypercharge by the orthogonality relation of [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html). **Both steps are at $M_C$: the colour factor and the hypercharge factor are made by the same vacuum.** No correction, no logarithm: at tree level a coupling passes through a threshold unchanged.

**4.2 One loop.** The equality acquires a finite shift,

$$
g_i^{\text{light}}(M)=g_i^{\text{heavy}}(M)+\frac{g_i^{3}}{16\pi^{2}}\,\Delta_i ,
$$

where $\Delta_i$ is computed from the heavy fields' contribution to the two-point function at zero external momentum. It is finite, it is a number, and it is not a logarithm: the logarithms live in the running below the threshold and cancels across it.

**4.3 What "the running" then means.** Between thresholds the couplings evolve with the beta functions of the fields present. The beta coefficients are the content of the thresholds: at each stage the coefficient changes when a field leaves. The one-loop coefficients are

$$
\beta(g)=-\frac{b\,g^{3}}{16\pi^{2}},\qquad b=\tfrac{11}{3}C_2(G)-\tfrac{4}{3}T_F n_f-\tfrac{1}{6}T_S n_s,
$$

with $n_f$ and $n_s$ the number of Dirac fermions and real scalars in the representation, and $C_2(G)$ the Casimir of the group.

**4.4 The composition.** Running from $M_W$ to $M_C$ with the Standard Model's coefficients, matching at $M_C$, running above it with the $\mathrm{SU}(4)$ content: the composition is the prediction. Each of the three steps is exact at its order, and the prediction's accuracy is limited by the order kept, not by the truncations.

**4.5 The assumption that is not a computation.** $g_4=g_L=g_R$ at one scale is an assumption of the model, not a result of the matching. It is what turns three independent couplings into one, and it is the statement the running then tests.

## What the Truncation Costs

**The error budget, stated before the result.** A prediction without an error estimate is not a prediction.

**5.1 The two truncations.** The decoupling expansion in $E/M$, and the loop expansion. The first is controlled by the ratio of the energy to the lowest removed mass; the second by the coupling.

**5.2 The size.** At the $Z$ pole, $E/M_W\approx1$, so the electroweak truncation is not a small expansion; at $M_C$, $E/M_C\ll1$, so the leptoquark truncation is excellent. The model's predictions at low energy are therefore mostly insensitive to $M_C$, which is exactly why $M_C$ has to be bounded by a rare process rather than by a precision observable.

**5.3 What the truncation cannot hide.** A mismatch of the *slopes* between thresholds is not a truncation effect: it is a statement about the content. If the content is wrong, the running misses by an amount that does not shrink as the truncation is improved. This is the failure of §*The Failure of the Minimal Content*.

**5.4 The honest summary.** Truncation errors are powers of $E/M$; content errors are not powers of anything. A model is tested by the second, and the second is what the corpus reports.

## The Failure of the Minimal Content

**One statement, no numbers.** The numbers are elsewhere by design.

**6.1 The failure.** With the minimal content — one $(\mathbf{15}\oplus\mathbf1)$ and the Standard Model fermions — the running from $M_C$ down to $M_W$ does not reproduce the measured $\sin^{2}\theta_W$ and the measured $\alpha_s$ simultaneously. The size and the sign are computed in [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html).

**6.2 Why the minimal content is the hardest case.** It has the fewest fields above $M_W$ and the fewest thresholds, so it has the least freedom to bend the slopes. Adding content adds freedom and also adds constraints, because every new field changes both $\alpha_s$ and $\sin^{2}\theta_W$.

**6.3 What the failure is not.** It is not evidence against the chain. The chain's content — the stabilisers, the budget and the massless count — is independent of any coupling. The failure is a statement about the field list above $M_W$, and it is the one open quantitative problem of the model.

**6.4 What the article claims and does not.** It claims that the machinery of matching is in place and that the minimal content fails within it. It does not claim that some other content succeeds. That would require a scan, and the scan is not in the corpus.

## The Checks

**Five checks.**

| check | computation | result |
|---|---|---|
| the tree matching | a coupling through a threshold | unchanged |
| the one-loop shift | finite, no logarithm | the logarithm cancels across the threshold |
| the beta coefficient | $b$ changes at each threshold | one value per stage |
| the operator dimensions | $1/M$ from the right vacuum, $1/M^{2}$ from the sextet, both at $M_C$ | dimension five and six |
| the error estimate | $E/M$ at each threshold | small at $M_C$, of order one at $M_W$ |

## Distinctions That Are Easy to Lose

**Three pairs.**

**7.1 Breaking and truncation.** The first is exact and sets the group; the second is approximate and sets the field list. Everything in §*Two Operations That Are Often Confused* is one instance of this.

**7.2 Matching and running.** Matching compares two theories at one scale; running moves within one. A prediction is a composition of both, and quoting one without the other is incomplete.

**7.3 The cancellation of logarithms.** The logarithm of the matching scale must cancel between the two theories' contributions; if it does not, the matching is wrong or the content is. This is the sharpest diagnostic the machinery has, and it is why the one-loop matching is worth the trouble at all.

## Summary

**Two operations.** Breaking, exact, a fact about the vacuum; truncation, approximate, a statement about the field list.

**Decoupling.** Removed fields become local operators of dimension five (the right vacuum) and six (the sextet), both at $M_C$.

**Two thresholds.** $M_C$: the leptoquarks, the Majorana mass. $M_W$: $W$, $Z$, the top.

**Matching.** Tree level equalities; one-loop finite shifts; logarithms cancel.

**The failure.** The minimal content does not reproduce the measured couplings, and the size of the failure is in the coupling article.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal L_{\text{eff}}$ | the low-energy Lagrangian |
| $\mathcal O_n$, $c_n$ | an operator of dimension $n$ and its coefficient |
| $\Delta_i$ | the finite one-loop matching shift of coupling $i$ |
| $b$ | the one-loop beta coefficient |
| $n_f$, $n_s$ | the numbers of Dirac fermions and real scalars |
| $C_2(G)$, $T_F$, $T_S$ | the Casimir and the index factors |
| $M_C$, $M_W$ | the two thresholds |

## Further Reading

- [The One Coupling That Returns the Standard Model: One Equation, One Scale, One Content Statement](the-one-coupling-that-returns-the-standard-model.html). The running, the failure and its size.
- [The Threshold Scales: One Transition at $M_C$, One Measured Weak Scale, and What Would Fix $M_C$](the-threshold-scales-mc-mw-and-what-would-fix-them.html). The scales this article matches at.
- [The Gauge Connection Below the Breaking: Three Pieces, Three Couplings, and What Each Multiplies](the-gauge-connection-below-the-breaking-three-pieces-three-couplings-and-what-each-multiplies.html). The couplings that are matched.
- [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html). The dimension-six operators of the first threshold.
- [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html). The dimension-five operator made at $M_C$.
- [The Effective Potential and the One-Loop Correction in Biquaternionic Form](the-effective-potential-and-the-one-loop-correction-in-biquaternionic-form.html). The loop machinery used here, in the algebra.
