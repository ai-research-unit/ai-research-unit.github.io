# __The Sixteen Above $M_C$: Massless, Vector-Like, and What That Costs__

## Introduction

This article is about a phase and not about a multiplet. *Classification of the Fermions* counts the sixteen, assigns $B-L$ off the grid and writes the conjugation as a permutation; *The $\mathrm{SU}(4)$ Model* declares the content and proves the anomaly cancels by counting. **Neither says what the sixteen does above $M_C$**, and the phase has three properties that no other article states together: the fields are massless, the content is vector-like in pairs, and both facts are consequences of the vacuum and not of the local symmetry.

**The three claims, and one of them is uncomfortable.**

- *Massless* is asserted by the phase and **not protected by the group.** The boson sector's masslessness is protected: a mass term $\tfrac12m^{2}A_{a,\imath}A_{a,\imath}$ is not invariant, so local invariance forbids it and the fifteen must be massless until a vacuum forms. **The sixteen has no such protection.** $\mathbf4\otimes\bar{\mathbf4}=\mathbf{15}\oplus\mathbf1$, the singlet is an invariant bilinear, and a mass term built from it is allowed at every scale. **So the fermions' masslessness above $M_C$ is a parameter set to zero and not a theorem.**
- *Vector-like* is a theorem: the content is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$, so each representation appears with its conjugate in equal number.
- *What it costs* is the whole of §*What the Phase Cannot Do*: a local vector-like sector cannot tell left from right, so the phase has no parity violation and no $CP$ violation from the sector, and the transition is what supplies both.

**Why the uncomfortable claim is written first.** A block that described the unbroken phase as though every masslessness were protected would be describing a theory that does not exist. The corpus's own scalar census refuses to write a potential because the group does not fix one; the same honesty applies to the fermion mass, and it is the sharper case because a mass term exists and is simply not used.

## Conventions

**The content.** Sixteen Weyl fields per generation, $\xi^{\alpha}_{i}$ with $\alpha$ the quartet index and $i$ the copy index, so that

$$
\mathbf{16}=2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4},
\qquad
4\cdot2+4\cdot2=16 .
$$

**The generators act on $\alpha$ and not on $i$**, so every array of the fifteen is $X\otimes\mathbb{1}_{2}$ on the sixteen: this is the two-index rule of *The Fermion–Connection vertex in the Quartet Basis*, and it is a consequence of the copy index being not made local.

**The coupling.** One $g_4$, in the covariant derivative $D_{\imath}=\partial_{\imath}-ig_4\sum_{a}A_{a,\imath}t_{a}$, with the normalisation of *The Lagrangian and the Primordial Force*.

**The phase.** Above $M_C$ the scalar's expectation value vanishes, $\langleΞ\rangle=0$, so no Yukawa vertex can dress a fermion line and no invariant mass is generated dynamically. **The phase is defined by that vanishing and by nothing else.**

**The indices.** All low, all sums weighted, as everywhere in the series. **The copy index $i$ is a label and not a frame slot**: it counts two and it never contracts with a spacetime index. **It is not a spinor index, not a index and not a generation index**: it doubles the content *within* one generation, and the number of generations is a separate input the corpus does not derive.

## What the Phase Asserts

**Four statements, and the fourth is the one that needs care.**

| statement | why it holds above $M_C$ |
|---|---|
| every fermion is massless | $\langleΞ\rangle=0$, so the Yukawa contributes nothing |
| every fermion is in a definite chirality | a Weyl field is, by construction, at every scale |
| no fermion mixes with its conjugate | no mass term is written |
| the connection action is the same on both copies | the generators are $X\otimes\mathbb{1}_{2}$ |

**The first three are statements about the vacuum; the fourth is a statement about the group.** The distinction matters because the fourth cannot change at the transition while the first three all do.

**The masslessness is a choice with a name.** Since $\mathbf4\otimes\bar{\mathbf4}$ contains a singlet, the local symmetry admits

$$
\mathcal{L}_{m}=-\sum_{i,j}m_{ij}\,\bar\xi^{\alpha}_{i}\xi_{\alpha,j}+\text{h.c.} ,
$$

with $m$ a $2\times2$ matrix in the copy index and the contraction over $\alpha$ the singlet of $\mathbf4\otimes\bar{\mathbf4}$. **Nothing in the group forbids it.** **The setting is more than one number and fewer than four.** $m$ carries four complex entries, but the copy index is not made local and rotates freely, so a rotation of the two $\mathbf4$ copies against the two $\bar{\mathbf4}$ copies brings $m$ to a diagonal with two positive entries — its singular values. **The physical content of $m=0$ is therefore two masses set to zero**, and no symmetry of the phase protects either of them.

The model sets $m=0$ above $M_C$, and the setting is of the same kind as $\mu_{\Phi}^{2}>0$ in the potential: **a coefficient the group does not fix, chosen so that the phase has the spectrum the block describes.**

**Why the choice is not arbitrary.** Three reasons, in order of strength.

- *The transition would be pointless.* If $m$ were nonzero, the sixteen would be massive at every scale, the lightest generation would weigh $m$, and the masses would not come from the vacuum that the other nine articles are about.
- *The observed spectrum is the constraint.* The electron's mass is $9.1\times10^{-31}\ \mathrm{kg}$, and a Dirac mass at the primordial scale would be at least fourteen orders of magnitude larger unless $m$ were tuned. **Tuning $m$ to zero is a choice; tuning it to $10^{-18}$ of the primordial scale is a coincidence**, and the model prefers the choice it can state.
- *The local symmetry does not care either way.* Because the content is vector-like, a mass term is a singlet and the theory is consistent with or without it. **A chiral theory would have forbidden it**, which is the one place where being vector-like costs nothing and buys nothing.

### The Bosons Are Protected and the Fermions Are Not

**The asymmetry, stated once, because it is easy to lose.**

| sector | mass term | invariant? | so the masslessness is |
|---|---|---|---|
| the fifteen | $\tfrac12m^{2}\sum_{a,\imath}A_{a,\imath}A_{a,\imath}$ | no | protected |
| the sixteen | $m_{ij}\bar\xi_{i}\xi_{j}$ | **yes** | assumed |
| the scalar | $m^{2}\operatorname{tr}Ξ^{2}$ | yes | assumed |

**Two of the three sectors have an assumed masslessness and only one has a protected one.** The boson sector is the exception because a connection's mass term breaks the symmetry that defines it, and that is the only structural protection in the model. **A reader who takes "all fifteen directions are massless above $M_C$" as a theorem should take "the sixteen are massless" as an assumption**, and the two sentences sit in the same paragraph of the declaration article without that distinction being drawn.

## Vector-Like, and What the Anomaly Count Buys

**The pairing is exact and the count is a cancellation.**

$$
2(+1)+2(-1)=0 ,
$$

the cubic index $+1$ on the $\mathbf4$ and $-1$ on the $\bar{\mathbf4}$, so the $\mathrm{SU}(4)^{3}$ triangle vanishes. **The cancellation costs no trace computation**, because it is a cancellation between a representation and its own conjugate rather than among three distinct charges. **And every mixed coefficient is absent**, since there is one factor and nothing to mix with: no $\mathrm{SU}(4)^{2}\mathrm{U}(1)$, no gravitational–$\mathrm{SU}(4)$, no $\mathrm{U}(1)^{3}$.

**What the count buys, item by item.**

- *No anomaly condition on the spectrum.* The content is fixed by the group and not by a cancellation requirement. **Compare the Standard Model**, where $\operatorname{tr}Y=0$, $\operatorname{tr}Y^{3}=0$ and the even doublet count are conditions on the hypercharges and a wrong assignment would break the theory. Here there is nothing to satisfy.
- *No global anomaly, and the reason is the group and not the count.* $\pi_{4}(\mathrm{SU}(4))=0$, so the Witten $\mathbb{Z}_{2}$ obstruction that an $\mathrm{SU}(2)$ with an odd number of doublets carries has nothing to attach to above $M_C$; below it the weak factor carries the Standard Model's even doublet count. **The sixteen is what cancels the triangle, and the group is what removes the global obstruction** — two different facts that a single word, anomaly-free, would run together.
- *No Green–Schwarz mechanism.* No axion, no Wess–Zumino term, no anomaly inflow. **The question does not arise**, and its absence is not a gap.
- *No constraint on the number of generations.* Three generations give $6(+1)+6(-1)=0$; so does any number. **The generation count is therefore unexplained by the anomaly**, which is the honest statement and the one the corpus makes about flavour generally.

**What the count does not buy.** It buys nothing for chirality, and the next section is why. **The same pairing that cancels the anomaly is the pairing that forbids a chiral connection coupling**, and the two statements have one cause: a representation and its conjugate are the same object twice.

## The Thirty-Two States

**Sixteen fields, thirty-two states, and the count does not distinguish the phases.**

| configuration | fields | states each | total |
|---|---|---|---|
| sixteen massless Weyl fields | $16$ | $2$ | $32$ |
| eight massive Dirac fields | $8$ | $4$ | $32$ |

**The arithmetic is the same and the physics is not.** A massless Weyl field has two helicities and no rest frame; a massive Dirac field has two spin states and two antiparticle states and always has a rest frame. **So the state count is not a test of masslessness**, and any argument that infers the phase from the multiplicity is wrong.

**What does distinguish them is the dispersion.** Above $M_C$ every mode has $\omega=\lvert\vec k\rvert$, so no mode can be brought to rest, no longitudinal polarisation exists, and the sixteen fields propagate at one speed. **Below $M_C$ the same sixteen fields split into eight massive Dirac fields and the dispersion acquires eight masses.** The count is invariant; the dispersion is not.

**Consequence for the thermal history, stated as a limit.** A phase with thirty-two massless fermionic states and thirty massless representative states is a radiation-dominated plasma with

$$
g_{*}=\underbrace{15\times2}_{\text{the fifteen}}+\underbrace{32}_{\text{the sixteen}}\times\tfrac78
=30+28=58 ,
$$

**counting the connections' two polarisations each and the fermions' factor $\tfrac78$** — the fifteen contribute the thirty states the table above counts, and the sixteen contribute thirty-two, so $g_*$ is $30+28$ and not $60+28$. That number is the phase's contribution to a thermal bath, it is stated here only because it is the one place the state count is a physical quantity, and **no cosmological use of it is made in this block**: the phase may never have been populated, and the corpus does not claim it was.

## What the Phase Cannot Do

**Six things, and each is a consequence of one fact: the local sector is vector-like.**

- *No parity violation.* A connection interaction that treats the two copies equally cannot produce a parity-odd rate. **Every tree-level process above $M_C$ is parity-symmetric**, and the asymmetry the weak sector shows below $M_C$ has no counterpart above it.
- *No $C$ violation from the connection.* The content is closed under $C$ as a permutation of the field set — $C$ carries $2\cdot\mathbf4$ to $2\cdot\bar{\mathbf4}$, **and the $\bar{\mathbf4}$ fields are already there, which is what vector-like means** — and a symmetry of the content that the interaction also respects gives no asymmetric rate.
- *No $CP$ violation above $M_C$.* With $C$ and $P$ each respected by the sector, the product is. **The observed $CP$ violation is therefore a statement about the phase below $M_C$**, and it is not in the primordial sector at all.
- *And the $\theta_4$ term does not reopen it.* $\theta_4\operatorname{tr}(F\tilde F)$ is $P$-odd and $C$-even, so the product argument does not reach it; **what removes it is the masslessness.** The axial rotation shifts $\theta_4$ and costs nothing above $M_C$, because no mass term is there to absorb the shift, so the angle is **redundant rather than merely suppressed** — [The $\mathrm{SU}(4)$ Instanton](the-su4-instanton-a-matrix-transcription-outside-the-algebra.html) carries that argument. **The statement is exact, and not an estimate at $e^{-S}$.**
- *No left–right asymmetry in the spectrum.* The two copies have the same mass, the same couplings and the same dispersion, because the only thing that could differ between them is the mass matrix $m_{ij}$, and it is zero.
- *No distinction between the copies at all.* Nothing in the connection Lagrangian refers to $i$ except the fermion's own label; **the mass term would, and it is set to zero.** **The copy index is invisible to every interaction above $M_C$**, and that invisibility is what makes the doubling exact rather than approximate.

**One thing the phase can do, and it is the reason the transition is a transition.** The copy index is not made local above $M_C$ and made local below it. **The index does not change; its status does.** At $M_C$ the two copies are separated — one couples to the $L$ factor and one to the $R$ — and the same sixteen fields, with the same labels, become chiral. **That separation is a postulate and not a derivation**: a single factor acting on the copy index would leave the content vector-like, since $(\mathbf4,\mathbf2)\oplus(\bar{\mathbf4},\mathbf2)$ is its own conjugate, so what a chiral content needs is the two copies acted on by **two different factors**, $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$. **That is one choice of representation, and [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html) carries it as the transition's single postulate and spends it there.** **What the transition supplies is therefore the status of the index and the mechanism that assigns the two factors; the assignment itself is declared.**

**Where the corpus says the same thing more sharply.** *The Chiral Wall* states it as a theorem: the model is not chiral where it fixing conditions, and the chirality sits entirely in a label. **This article's contribution is the ledger that goes with it** — what the non-chirality forbids, item by item, and why the forbiddance is a property of the phase rather than of the group.

## The Ledger: What It Costs

**Three costs, three benefits, and one item that is neither, side by side, so that none is read alone.**

| item | what it is | sign |
|---|---|---|
| no chiral connection coupling | parity and $CP$ respected above $M_C$ | cost |
| no anomaly condition | content fixed by the group alone | benefit |
| no generation constraint | three generations unexplained | **neither** |
| assumed fermion masslessness | two masses set to zero, not a theorem | cost |
| doubling exact | the copy index is invisible to every vertex | benefit |
| masses from one vacuum | one scale, one mechanism, no second source | benefit |
| chirality deferred | the transition must exist | cost |

**The generation row is neither because the benefit was never on offer.** A chiral theory does not explain three generations either — the Standard Model's anomaly conditions are satisfied generation by generation and fix nothing — so the absence of a constraint is a benefit *not collected* rather than a cost paid, and calling it a cost would overstate what vector-likeness took away.

**The last row is the ledger's sum.** A phase that is vector-like cannot be the whole theory, because the world is chiral. **So the transition is not an embellishment of the model; it is required by the phase's own symmetry structure**, and the requirement is quantitative: without it the sixteen would be parity-symmetric at every scale and the model would predict zero for every parity-odd observable.

**What the ledger is not.** It is not a criticism of the model. A vector-like high-scale sector with a chiral transition is a coherent structure, and it is the structure the corpus declares. **What the ledger establishes is which of its statements are theorems and which are choices**, so that a reader who wants to attack the model attacks the right ones. **The choice is $m=0$, that is two masses set to zero; the theorem is the pairing.**

## The Checks

**Nine numbers, each recomputed.**

| statement | value |
|---|---|
| the content | $2\cdot4+2\cdot4=16$ |
| the states | $16\times2=32$ |
| the cubic index on the $\mathbf4$ and the $\bar{\mathbf4}$ | $+1$, $-1$ |
| the $\mathrm{SU}(4)^{3}$ coefficient | $2(+1)+2(-1)=0$ |
| the mixed coefficients | none, one factor |
| the global anomaly | $\pi_{4}(\mathrm{SU}(4))=0$ | absent, and not by the count |
| the states as eight massive Dirac fields | $8\times4=32$ |
| $g_{*}$ of the phase, representative $15\times2$ and fermion $32\times\tfrac78$ | $30+28=58$ |
| the mass channel | the singlet of $\mathbf4\otimes\bar{\mathbf4}=\mathbf{15}\oplus\mathbf1$ |

**The last row is the article's technical point in one line**: the singlet that makes the mass term invariant is the same singlet that makes the anomaly cancel and the same one that made the coupling article's coefficient blind to the scalar's representation. **One decomposition, three consequences**, and a reader who has met all three in different articles has met one fact three times.

## Summary

Above $M_C$ the sixteen are massless, vector-like and parity-symmetric, and the three properties have three different grounds. **Masslessness is assumed**: $\mathbf4\otimes\bar{\mathbf4}$ contains a singlet, so an invariant mass exists and the model sets its two physical masses — the singular values of $m_{ij}$ — to zero, exactly as it sets $\mu_{\Phi}^{2}>0$. **Vector-like is a theorem**: the content is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$ and each representation appears with its conjugate in equal number. **Parity symmetry is a consequence of vector-likeness**: a sector that treats the copies equally cannot produce a parity-odd rate.

**The anomaly cancels by counting and costs nothing.** $2(+1)+2(-1)=0$, no mixed coefficient exists because there is one factor, and no condition is imposed on the spectrum, the hypercharges or the number of generations. **That is the benefit side of vector-likeness and it is real**, not a consolation.

**The cost side is that the phase cannot be the whole theory.** No parity violation, no $CP$ violation from the sector, no left–right asymmetry, no distinction between the copies at all. **The $CP$ statement is exact and not a truncation**: the $\theta_4$ term is the one sector operator that is $CP$-odd, and the masslessness makes it removable rather than merely suppressed. **The transition is required by the phase's own symmetry structure**, and what it changes is not the fields and not the labels but the status of the copy index: not made local above, made local below — with the split into two factors supplied by the transition's one postulate rather than by this phase.

**The state count is thirty-two either way.** Sixteen massless Weyl fields and eight massive Dirac fields give the same multiplicity and different dispersions, so no argument from multiplicity can tell the phases apart. What tells them apart is $\omega=\lvert\vec k\rvert$ above and eight masses below.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\xi^{\alpha}_{i}$, $\bar\xi^{\alpha}_{i}$ | Fermion field, quartet index $\alpha$, copy index $i$ |
| $\mathbf{16}$ | $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$ |
| $i$ | The copy index, $i=1,2$; a label, not made local above $M_C$ |
| $m_{ij}$ | The invariant mass matrix in the copy index; set to zero above $M_C$ |
| $T_{a}\otimes\mathbb{1}_{2}$ | Every generator's action on the sixteen; the two-index rule |
| $g_4$ | The one coupling, the same on both copies |
| $g_{*}$ | $58$ for the phase, from $30$ representative and $28$ fermionic states |
| $C$ | The conjugation carrying $2\cdot\mathbf4$ to $2\cdot\bar{\mathbf4}$ |
| $\mathbf4\otimes\bar{\mathbf4}$ | $\mathbf{15}\oplus\mathbf1$; the singlet is the mass channel |

## Further Reading

- [Classification of the Fermions in the $\mathrm{SU}(4)$ Model](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html). The count, the two octets, the $B-L$ assignment and the conjugation as a permutation.
- [The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, Rank Three](the-su4-model-four-lines-fifteen-generators-one-declaration.html). The declaration of vector-likeness and the anomaly count that this article reads as a phase statement.
- [The Chiral Wall, Which Is Now a Theorem](the-su4-model-four-lines-fifteen-generators-one-declaration.html). §*The Chiral Wall* of the declaration article: why the model is not chiral where the symmetry acts, and where the chirality is instead.
- [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). The transition's single postulate — the two copies acted on by two different factors — which is what turns the label into chirality.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The action these sixteen fields sit in, and the place where $m_{ij}$ would have been written.
- [The Fermion–Connection vertex in the Quartet Basis](the-fermion-connection-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The two-index rule $X\otimes\mathbb{1}_{2}$ that makes the copy index invisible.
- [The Primordial Coupling](the-primordial-coupling-g4-as-a-boundary-condition-and-what-runs-above-m-c.html). The coefficient whose fermion term counts the sixteen as eight Dirac fields, which is the pairing this article describes.
- [The $\mathrm{SU}(4)$ Instanton](the-su4-instanton-a-matrix-transcription-outside-the-algebra.html). Why $\theta_4$ is admissible, periodic, and redundant above $M_C$ — the argument that keeps this phase free of $CP$ violation.
- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). The vacuum whose vanishing makes the Yukawa contribute nothing.
