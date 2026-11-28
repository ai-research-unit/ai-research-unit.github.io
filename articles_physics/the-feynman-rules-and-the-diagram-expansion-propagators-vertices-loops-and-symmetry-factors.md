# __The Feynman Rules and the Diagram Expansion: Propagators, Vertices, Loops and Symmetry Factors__

## Introduction

**The claim.** Stage $4$ is a set of reading instructions. The series of stage $3$ is a sum of graphs, and four rules say what each piece of a graph contributes: the inverse of the quadratic operator for a line, the coefficient of a monomial for a vertex, an integral over each undetermined momentum, and the symmetry factor for the graph's automorphisms. Amputating the external lines and putting their momenta on the shell turns a correlator into an $S$-matrix element.

**Why the rules are not a mnemonic.** They are the reading of a computed series, and the computation is stages $2$ and $3$. The mnemonic is what a reader retains after forgetting the derivation, and calling it a mnemonic is honest about its retention and not about its status. [Stage $2$](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html) proves the line; [stage $3$](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html) proves the vertex and the symmetry factor; and this article collects the four into the form in which they are used.

**The strongest objection.** *Feynman rules are a calculational device with no content.* The objection mistakes the diagram for the physics. What the diagrams carry is the *order*: which processes contribute at which power of the coupling, which are tree and which are loop, and which are forbidden. That information is not in the density in any form a reader can see, and it is not in the equation of motion at all.

**Position.** Stage $4$ of the chain in [the hub](the-lagrangian-method-from-the-collected-lagrangian-to-the-feynman-diagram.html), and the article that hands the diagrams to [the classical limit](the-classical-limit-of-the-diagram-series-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html) and to [the failure modes](the-failure-modes-of-the-diagram-expansion-gauge-fixing-renormalisation-asymptotic-series-and-strong-coupling.html).

## The Four Rules

**Each rule reads one object of stages $2$ and $3$, and none of the four is optional.**

| rule | what it says | where it comes from |
|---|---|---|
| propagator | one line carries $\Delta=i/[-\mathcal M+i\epsilon]$, or the rung's numerator over that denominator | the inverse of $\mathcal L_{2}$'s operator |
| vertex | one vertex carries $i$ times the monomial's coefficient times its matching count | the coefficient of $\mathcal L_{\ge3}$ |
| loop momentum | integrate $\int\frac{\mathrm{d}^{4}k}{h^{4}}$ over every momentum the external data do not fix | the Fourier transform of an internal point |
| symmetry factor | multiply by $n!$ divided by the graph's automorphism count | the expansion's $\frac{1}{n!}$ |

**The loop measure is the corpus's own and it carries the action quantum.** The $\frac{\mathrm{d}^{4}k}{h^{4}}$ is $\frac{\mathrm{d}^{4}k}{(2\pi)^{4}}$ in the units $\frac{h}{2\pi}=1$, and every loop integral in the corpus's articles is written in one of the two. A reader who mixes the two measures across a computation gets a power of $2\pi$ per loop and nothing else, which is the kind of error that survives because it is invisible in a ratio.

**The rules are stated for a connected graph with external legs, and the disconnected ones follow.** The vacuum bubbles are the determinant's terms and divide out of every correlator; the connected diagrams are the logarithm of $Z$, and the one-particle-irreducible ones are the effective action's. [The Generating Functional and the Effective Action](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html) states the three generating functionals and what each one's diagrams are.

## The Diagrams Ordered by the Coupling

**Ordering by vertices is the organisation, and it is what makes a truncated computation meaningful.**

| diagram | vertices | order in $g$ | loops | what it is |
|---|---|---|---|---|
| a single line | $0$ | $1$ | $0$ | free propagation |
| two vertices joined by one line | $2$ | $g^{2}$ | $0$ | tree-level exchange |
| one vertex with one line closing | $1$ | $g$ | $1$ | the first correction to the two-point function |
| two vertices with one line closing | $2$ | $g^{2}$ | $1$ | the first correction to a four-point function |
| $n$ vertices, $L$ loops | $n$ | $g^{n}$ | $L=I-n+1$ | the general term |

**The loop number is not the order, and the table says so twice.** A one-loop diagram can be order $g$ or order $g^{2}$; a fixed order can contain several loop numbers. Truncating at fixed order and truncating at fixed loop number are different truncations of the same series, and [the sixth article](the-classical-limit-of-the-diagram-series-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html) is where the difference is used.

## The Tree Amplitude

**The running example's tree amplitude is one vertex and four external legs.** With the four legs on two components, [stage $3$'s vertex](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html) is $-2i\varpi_{\mathrm{cpl}}$, so the $s$-channel contribution is

$$
i\mathcal M_{s}=\bigl(-2i\varpi_{\mathrm{cpl}}\bigr)\times(\text{one external factor per leg})
\quad\Longrightarrow\quad
\mathcal M_{s}=-2\varpi_{\mathrm{cpl}},
$$

with the external factors equal to one after amputation and on-shell evaluation. The exchanged channel contributes the same with the legs crossed, and the two add for distinguishable components.

**Nothing in this line is an approximation beyond the truncation itself.** The vertex is exact at its order, the external legs are exact, and the amplitude is the coefficient of the monomial in the density, read once. That is what "exact at each order" means, and the phrase is used in the corpus in this sense only.

**The amplitude's dimensions follow from the vertex's, and the check is one line.** The density has dimension four and the quartic has dimension four, so $\varpi_{\mathrm{cpl}}$ carries dimension zero in units where the field is dimensionless, or dimension two where the field carries dimension one; the corpus's equation $(\Box_{\Phi}-4\pi^{2}\nu_{m}^{2})\tilde\Xi=\varpi_{\mathrm{cpl}}N\tilde\Xi$ fixes which, because both sides must carry the field's dimension over a length squared.

## The One-Loop Correction

**The first quantum correction is a line that closes on itself, and its integral is the first place the method meets a divergence.**

$$
\Gamma^{(2)}_{1}(p)\;\propto\;\varpi_{\mathrm{cpl}}\int\frac{\mathrm{d}^{4}k}{h^{4}}\;\Delta(k)
=\varpi_{\mathrm{cpl}}\int\frac{\mathrm{d}^{4}k}{h^{4}}\;\frac{i}{-\mathcal M(\tilde K_{\Phi})+i\epsilon}.
$$

**The integral is quadratically divergent and the divergence is not a technicality.** With a hard cutoff $\Lambda$ in the Euclidean region the integral is $\pi^{2}\bigl[\Lambda^{2}-m^{2}\log\bigl(1+\Lambda^{2}/m^{2}\bigr)\bigr]$, so $\int\Delta$ grows like $\Lambda^{2}$: on the corpus's units the ratio to $\Lambda^{2}$ approached $\pi^{2}$ as $9.7217$, $9.8472$, $9.8670$, $9.8693$, $9.8696$ at $\Lambda=10,30,100,300,1000$ with $m=\tfrac12$, and the residual tracked $-m^{2}\log$ to four figures. The number is quoted because "quadratically divergent" is a claim about a limit, and the limit was taken.

**The correction is absorbed, and the absorption is the renormalisation condition.** Writing the two-point function as the free propagator times a series, the divergent part is a constant times the free propagator and is removed by a counterterm of the same form as the mass term. That is the definition of mass renormalisation, and it works at every order for the theories the corpus writes. [The Renormalization Group](the-renormalization-group-in-biquaternionic-form.html) states the flow that the absorption defines, and [the last article of this section](the-failure-modes-of-the-diagram-expansion-gauge-fixing-renormalisation-asymptotic-series-and-strong-coupling.html) states why the absorption is a condition and not a derivation.

**The finite part is a prediction and the divergent part is not.** This is the sentence a reader should carry away from the one-loop computation: the divergence is removed by a choice, and the choice is a measurement. What survives is a number the theory did not have before the loop was drawn.

## The $S$-Matrix: Amputation and the Shell

**A correlator is not an amplitude, and the difference is four operations.** [The LSZ Reduction Formula](the-lsz-reduction-formula-in-biquaternionic-form.html) states them: Fourier transform each external leg with its plane-wave phase, amputate it by the wave operator, put every external momentum on the mass shell, and divide by $\sqrt Z$ per leg.

**Amputation is multiplication by $\mathcal M$, and it removes exactly the propagator the leg carried.** Off the pole,

$$
\mathcal M(\tilde Q_{\Phi})\,\Delta(\tilde Q_{\Phi})
=\frac{i\mathcal M}{-\mathcal M+i\epsilon}\;\longrightarrow\;-i ,
$$

and the residual is $\frac{\epsilon}{|\mathcal M|}$, which was computed on one hundred random off-shell values with $\epsilon=10^{-8}$ and never exceeded $2.0\times10^{-8}$. The overall $-i$ is the external-state convention that the corpus's LSZ article records: relative to the standard wave operator the amputation carries a factor $-1$ per leg, and the factor is a convention and not a discrepancy.

**The residue is the wave-function renormalisation, and it cancels out of the amplitude.** Writing the two-point function near the pole as $Z/\mathcal M$ plus a regular part, the residue $Z$ is what the leg's overlap contributes; the formula's $Z^{-1/2}$ per leg removes it, so no $Z$ survives. On the shell the amplitude is the amputated correlator with the external momenta at $N(\tilde Q_{\Phi})=-m^{2}c^{2}$.

**The four operations do not commute with a constraint, and the corpus's matrix rung is where that matters.** At the matrix rung the fifteen Gauss laws mean not every external leg is a physical state, so amputation and the on-shell condition do not commute with the constraint; [the LSZ article](the-lsz-reduction-formula-in-biquaternionic-form.html) states that the vector and matrix reductions are not written and why.

## The Rules the Corpus Already Wrote

**Four rule sets are collected in the corpus, and they stop at different places.**

| rule set | what the article actually writes | where |
|---|---|---|
| QED | the action and its two classical equations; it states in as many words that it has no propagator and no vertex | [QED](the-lagrangian-and-quantum-electrodynamics.html) |
| QCD | the quark, gluon and ghost propagators; the three- and four-gluon vertices and the ghost–gluon vertex | [QCD](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html) |
| $\mathrm{SU}(4)$ | the sixteen's propagators and the full vertex list: $120$ entries, $48+12$ per half | [the $\mathrm{SU}(4)$ rules](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html) |
| electroweak | the five propagators and the $R_{\xi}$ family, $\frac{P}{\Pi-M^{2}}+\frac{\zeta L}{\Pi-\zeta M^{2}}$, with the $\zeta$-cancellation | [$R_{\xi}$](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html) |

**Only the QCD and $\mathrm{SU}(4)$ articles carry vertex lists, and the table says so rather than pretending otherwise.** The QED article stops at the classical action; the $R_{\xi}$ article's subject is the propagator family and why the $\zeta$-dependent parts cancel, and its vertices appear only where the Ward identity needs them.

**The electroweak row is the one that shows the rules' dependence on stage $0$.** Its propagator is not the inverse of one operator but of a family, because the fixing term's parameter $\zeta$ is a choice; the physical answers do not depend on it, and the $\zeta$-dependent parts cancel between the Goldstone and the ghost because their poles coincide at $\Pi=\zeta M^{2}$. That is a statement about pole positions and it is [the $R_{\xi}$ article's](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html), not this one's.

**This section does not re-derive any of the four.** Each article transcribes a standard rule set into the corpus's notation with the imported half marked, and the QED article stops earlier and says so. A reader who needs a vertex checks it in the rule article, not here.

## What the Rules Do Not Give

**Four things are outside the rules, and naming them keeps the stage honest.**

**The interaction itself.** The rules read a density; they do not choose one. Every density beyond the corpus's scalar quartic is imported.

**The bound-state problem.** Two-quark states and their masses are not diagrams at any finite order; [Hadron Structure from QCD: The Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html) is the corpus's article on the gap.

**The sign of $i\epsilon$.** The algebra names the axis of the deformation and does not choose the orientation; the sign is a convention fixed by the vacuum.

**Convergence.** The rules produce a series; whether the series converges is not a rule's business, and the answer is no.

## Summary

**Stage $4$ reads the series by four rules.** A line is the inverse of the quadratic operator; a vertex is the coefficient of a monomial times the unit of the expansion and its matching count; every undetermined momentum is integrated with $\frac{\mathrm{d}^{4}k}{h^{4}}$; and the graph's automorphisms divide the expansion's $n!$. The result is a sum of diagrams ordered by the number of vertices.

**The tree amplitude of the running example is one vertex.** With the four legs on two components the $s$-channel amplitude is $\mathcal M_{s}=-2\varpi_{\mathrm{cpl}}$; the first quantum correction is a closed line whose integral grows like $\Lambda^{2}$ in four dimensions, with $\int\Delta/\Lambda^{2}\to\pi^{2}$ verified at five cutoffs.

**Amputation and the shell make the amplitude.** Multiplication by $\mathcal M$ returns $-i$ off the pole with residual $\frac{\epsilon}{|\mathcal M|}$, verified below $2.0\times10^{-8}$ on one hundred values; the residue is $Z$, and the formula's $Z^{-1/2}$ per leg cancels it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Delta$, $\mathcal M(\tilde Q_{\Phi})$ | the propagator and the mass-shell operator |
| $\mathcal M_{s}$ | the $s$-channel amplitude |
| $\Lambda$ | a momentum cutoff |
| $Z$ | the wave-function renormalisation, the residue at the pole |
| $P$, $L$ | the transverse and longitudinal projectors of the $R_{\xi}$ propagator |
| $\Pi$ | the positive momentum invariant |

## Further Reading

- [The LSZ Reduction Formula in Biquaternionic Form](the-lsz-reduction-formula-in-biquaternionic-form.html), the four operations that turn a correlator into an amplitude.
- [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), the three generating functionals and what each one's diagrams are.
- [The Feynman Rules of the $\mathrm{SU}(4)$ Model: The Vertices of the Fifteen and the Sixteen](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html), the corpus's largest rule set.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html), the three- and four-gluon and ghost rules.
- [Fixing the Representative in the Electroweak Theory: $R_{\xi}$ Conditions, Ghosts and the Goldstone Equivalence Theorem](fixing-the-representative-in-the-electroweak-theory-r-xi-conditions-ghosts-and-the-goldstone-equivalence-theorem.html), the propagator family and the $\zeta$ cancellation.
- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html), what the absorbed divergence defines.
