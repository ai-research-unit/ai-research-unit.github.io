# __The Observables: Correlation Functions and Their Reduction__

## Introduction

**The claim.** The method produces one object, the generating functional, and every observable is obtained from it by a fixed sequence of reductions. The sequence is the *ladder*: differentiate to obtain a correlator, amputate the external lines, put the external momenta on the shell, and read the residue. Each rung is a definite algebraic operation, and each discards something. The article states the ladder once, because the commonest error in reading a perturbative result is a comparison made at the wrong rung.

**Why it belongs at the end of the section.** The four stages produce diagrams; the ladder converts diagrams into numbers that an experiment can compare with. Without the ladder the section would stop at a formal series, and a formal series is not an observable. The dependence that the ladder removes — the wave-function normalisation, the source, the off-shell continuation — is the dependence a reader must know is unphysical before he can interpret any number in the corpus.

**The strongest objection.** *The ladder is standard, and each of its rungs already has its own article.* It is standard, and the articles exist: [the functional integral](the-functional-integral-in-biquaternionic-form.html), [the generating functional](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), [the $S$-matrix](the-s-matrix-in-biquaternionic-form.html) and [the LSZ reduction](the-lsz-reduction-formula-in-biquaternionic-form.html). What none of them states is the *order* — which subtraction happens at which rung, and which of the discarded quantities is unphysical and which is physical but unmeasured. This article states the order and adds no derivation to the four.

**Position.** The section's last constructive article before [the limits](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html). It consumes the diagrams of [stage $4$](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html) and produces the quantities that the limits apply to.

## The Ladder

**Four rungs, one direction, and each rung is a stated operation.**

| rung | the operation | what it removes | what it leaves |
|---|---|---|---|
| $1$ | differentiate $Z[J]$ $n$ times, then set $J=0$ | the source | the $n$-point correlator, off shell |
| $2$ | multiply by the inverse propagators of the external legs | the external propagators | the amputated correlator |
| $3$ | put the external momenta on the shell | the off-shell continuation | the on-shell amplitude |
| $4$ | multiply by the residues | the field normalisation | the $S$-matrix element |

**Only the fourth rung is directly comparable with a cross-section.** Everything above it is a statement about a quantity that depends on how the field was normalised. This is the fact the ladder exists to make explicit, and it is why a reader comparing two loop amplitudes should first check that both were taken to the same rung.

**The order is not negotiable.** Amputating before differentiating removes the wrong object. Putting on the shell before amputating leaves the external propagators' poles uncancelled. Reading the residue before the shell is reached multiplies by the residue of something that is not yet on its pole. Each misordering produces a finite, plausible, wrong number.

## What Each Rung Discards

**Rung $1$ discards the source, and the discard is legitimate because the source was a device.** The generating functional is defined with a source so that differentiation is possible; no observable contains it. The correlator is therefore the first object in the ladder that is a property of the theory alone, and it is still not an observable, because it is off shell.

**Rung $2$ discards the external propagators, and they are not physical.** An external line of a diagram carries the propagator of a virtual particle, and an asymptotic state is not a virtual particle. Amputation removes the artefact. What remains is the sum of everything that can happen between the external points, and that is the object a vertex is a term of.

**Rung $3$ discards the off-shell continuation, and this is the rung that requires a physical assumption.** The correlator is defined at arbitrary external momenta; an asymptotic state has a definite one. Putting the momenta on the shell is legitimate when the asymptotic states are well separated, which is the assumption the $S$-matrix is defined under. Where the assumption fails — in a bound state, in a confining regime — the ladder does not produce an $S$-matrix, and that is a boundary of the method and not of the algebra. It is the fourth class of [the limits](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html).

**Rung $4$ discards the field normalisation, and the discard is the residue.** The residue at the pole is what converts a correlator, which depends on how the field was defined, into an $S$-matrix element, which does not. This is the rung at which a change of representation in [the dictionary](the-dictionary-field-redefinition-and-change-of-representation.html) stops mattering: two representations that differ by a field rescaling differ at rungs $1$ to $3$ and agree at rung $4$.

## The Dependence That Does Not Cancel

**Three dependences are removed by the ladder, and three are not.**

| dependence | removed at | what to do with it |
|---|---|---|
| the source | rung $1$ | nothing: it was a device |
| the external propagators | rung $2$ | nothing: they are artefacts |
| the field normalisation | rung $4$ | nothing: the residue absorbs it |
| the truncation label | never | quote it with the number |
| the scheme | never | quote it, or convert |
| the ordering parameter | never | quote the order |

**The lower three are the reason a number in the corpus is quoted with its order.** A result quoted without its truncation label, its scheme and its order is not a prediction; it is a number whose dependence has been hidden. The ladder removes exactly the dependences that are unphysical, and it is the community's recurring error to assume it removes more.

**The middle of the table is the subtle one.** A quantity that depends on the scheme but not on the label, or on the label but not on the scheme, is a quantity whose dependence is partly physical. [Renormalisation as an Operation](renormalisation-as-an-operation-the-arbitrary-scale.html) is the article that separates the two dependencies, and this one only records that the ladder does not.

## The Reduction and the Physical Assumption

**The ladder is algebraic up to rung $3$ and physical at rung $3$.** This asymmetry is worth stating plainly, because it is where the method's scope is decided.

- **Rungs $1$, $2$ and $4$ are algebraic.** They can be performed for any theory, at any coupling, at any order. Nothing about the regime enters.
- **Rung $3$ requires asymptotic separation.** It is where the method assumes that the states in and out are free at early and late times, and where a theory with no such states gives no $S$-matrix at all.

**The consequence is that a correlator is more general than an $S$-matrix element.** A correlator exists whenever the generating functional does; an $S$-matrix element exists only where the asymptotic assumption holds. A reader who identifies the two has restricted the method without saying so, and it is the identification that makes confinement look like a failure of the diagrams rather than a failure of rung $3$.

**The corpus's reduction articles state the assumption where they use it.** [The LSZ Reduction Formula](the-lsz-reduction-formula-in-biquaternionic-form.html) states the asymptotic condition as a hypothesis, and [The $S$-Matrix](the-s-matrix-in-biquaternionic-form.html) states what follows from it. This article only places them on the ladder.

## What the Algebra Supplies Here

**The algebra supplies the vertices and the propagators that the correlators are built from, and it supplies nothing about the ladder.** The rungs are operations on the generating functional, and they are the same operations in every transcription. What the corpus's representation changes is the *form* of the correlator at rung $1$ — the biquaternion field's components and their pairings — and by rung $4$ that difference has been divided out by the residues. This is the sense in which the corpus's $S$-matrix elements are the standard ones, and the sense in which its intermediate quantities are not.

## Summary

**Every observable is obtained from the generating functional by a ladder of four reductions: differentiate, amputate, put on the shell, read the residue.** Each rung is a stated operation; each discards something; and the order is not negotiable.

**The ladder removes the source, the external propagators and the field normalisation — and only those.** The truncation label, the scheme and the order survive to the end and must be quoted with any number.

**Rung $3$ is where the ladder stops being algebraic.** It assumes asymptotic separation, and where that assumption fails the method produces correlators and no $S$-matrix. That is a boundary of rung $3$ and not of the diagrams.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Z[J]$ | the generating functional with source $J$ |
| $G^{(n)}$ | the $n$-point correlator, $Z$ differentiated $n$ times |
| $\Gamma^{(n)}$ | the amputated correlator, the one-particle-irreducible functional |
| $\mathcal M$ | the on-shell amplitude |
| $\mathcal S$ | the $S$-matrix element, the amplitude times the residues |

## Further Reading

- [The Functional Integral in Biquaternionic Form](the-functional-integral-in-biquaternionic-form.html), the object the ladder starts from.
- [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), rung $1$ and the Legendre transform to $\Gamma$.
- [The $S$-Matrix in Biquaternionic Form](the-s-matrix-in-biquaternionic-form.html), rung $4$ and what follows from it.
- [The LSZ Reduction Formula in Biquaternionic Form](the-lsz-reduction-formula-in-biquaternionic-form.html), rung $3$ and the asymptotic hypothesis it assumes.
- [The Feynman Rules and the Diagram Expansion: Propagators, Vertices, Loops and Symmetry Factors](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html), the diagrams that the ladder reduces.
- [The Limits of the Expansion: Gauge Fixing, Asymptotic Series and Strong Coupling](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html), the boundaries that apply to the numbers the ladder produces.
