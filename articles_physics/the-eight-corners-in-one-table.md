# __The Eight Corners in One Table__

## Introduction

**The claim.** The section has eight corners, and each is specified by the same four things: the coordinates moved and how far, the theory that results, the result it reproduces, and the effect it cannot produce. Written in one table, the lattice becomes a lookup: a reader with an observable in hand can read off which corner computes it and how large that corner's error is.

**The answer.**

$$
\boxed{\;8\ \text{corners},\quad 3\ \text{of them exact or near-exact},\quad 1\ \text{without an error bar},\quad \text{and } 2\ \text{pairs of limits that do not commute}\;}
$$

**What the table is for.** Not for reference alone. Two of the numbers in the last section of this article — the proton radius and the hadronic vacuum polarisation — show that a single measured quantity can require three or four corners at once, and that the accuracy of the answer is set by the *worst* corner used, not by the best.

## The Table

| Case | Coordinates moved | Resulting theory | Reproduces | Error | Cannot reproduce |
|---|---|---|---|---|---|
| 1 | none | the eight-line Lagrangian | everything | the measurement's | — |
| 2 | $\hbar\to0$ | classical field equations; Dirac as a spinning particle | $g=2$; Proca and KG dispersion; tree widths | $\alpha/\pi\approx2.3\times10^{-3}$ | $a_e$; running; $h\to\gamma\gamma$ |
| 3 | $\hbar\to0$, then $v/c\to0$ | Newton with spin; Pauli then Schrödinger | Thomas factor $\tfrac12$; Bohr spectrum; $j$-splitting | $10^{-5}$ from $v^2/c^2$, $10^{-3}$ from the loop | Lamb shift; degeneracy breaking |
| 4 | $v/c\to0$ | NRQED | Lamb shift; hyperfine; $a_e$ to twelve digits | $(Z\alpha)^2$, beaten by $e^{-2mr}$ | pairs; positronium; running above $2m_e$ |
| 5 | $\hbar\to0$, $\partial S$ large | Hamilton–Jacobi with BMT; WKB; eikonal | Bohr–Sommerfeld; Born limit; storage-ring precession | $\epsilon\sim Z\alpha$ | tunnelling; non-stationary paths; caustics |
| 6 | $p/\Lambda\to0$ | the renormalisable theory: the eight lines | muon lifetime; $\beta$ decay; the $d\le4$ list | $m_\mu^2/M_W^2=1.7\times10^{-6}$ | $W$ resonance; logs; loop vertices |
| 7 | $1/N\to0$, gradients | the relativistic spin fluid | continuity; Euler; quantised circulation $h/m$ | $(\ell/L)^2$ and $1/3$ | interference; spectrum; tunnelling; fluctuations |
| 8 | $\alpha_s$ large | instantons, condensates, confinement | $8\pi^2/g^2$; the anomaly; the lattice spectrum | none in general | any diagrammatic expansion |

## Three Structural Lessons

**First: the lattice is not a line.** The eight corners are not ordered by accuracy, and the ordering that exists is partial. Case 4 is the most accurate corner in physics; case 7 is the least; case 2 is better than case 5 for spin and worse for interference. A reader who assumes a single ordering will use the wrong corner for the wrong observable.

**Second: the errors are of different kinds.** Case 2's error is a power of $\alpha$; case 4's is a power of $Z\alpha$ that is beaten by an exponential; case 7's is a power of a number that is $1/3$; case 8's does not exist. A table that puts these in one column is already doing violence, and the violence is worth naming: four different kinds of error bar share a column because they share a function.

**Third: the corners are used together.** Nothing in the section computes a real observable from one corner alone, and the two worked examples below are the demonstration.

## Worked Example One: The Hydrogen Spectrum

**Six contributions, four corners, and one matching coefficient.**

| Contribution | Size | Corner |
|---|---|---|
| the Bohr levels | $13.6\ \mathrm{eV}$ | 3 |
| fine structure, $2p_{3/2}$–$2p_{1/2}$ | $10.969\ \mathrm{GHz}$ | 3, or 4 for the loop-corrected version |
| the Lamb shift, $2s_{1/2}$–$2p_{1/2}$ | $1057.845\ \mathrm{MHz}$ | 4, and impossible in 3 |
| hyperfine, $1s$ | $1420.405751\ \mathrm{MHz}$ | 4, limited by the proton's magnetism |
| the proton charge radius | $0.84\ \mathrm{fm}$ | 6, a matching coefficient |
| finite nuclear size beyond the radius | $\mathcal{O}(r_p^2)$ corrections | 6, higher orders |

**The lesson is in the fifth row.** The proton radius is not computed by any corner of this lattice; it is measured, and it enters case 4 as an input. The muonic-hydrogen Lamb shift is measured to $202.37\ \mathrm{meV}$ and the theory is limited by this input, whose electronic and muonic determinations differ by about $4\%$. A prediction "to twelve digits" is therefore a prediction to twelve digits *given* a number that is known to four.

**The lesson generalises.** Every corner has such inputs, and they are always matching coefficients from a corner below. A calculation that does not say which coefficients it took as inputs has hidden its largest error.

## Worked Example Two: The Muon Anomalous Moment

**One number, four corners, and a disagreement that is itself the point.**

**The assembly.** $a_\mu$ is built from:

| Contribution | Corner | Size |
|---|---|---|
| the tree value $g=2$ | 2 | the baseline |
| the QED loops | 4 | $1.16\times10^{-3}$, the dominant term |
| the electroweak loops | 6, matched | $1.5\times10^{-9}$ |
| the hadronic vacuum polarisation | 8, matched into 6 | $6.9\times10^{-8}$ |
| the hadronic light-by-light | 8, matched into 6 | $9\times10^{-10}$ |

**The measured value is $a_\mu=116592059(22)\times10^{-11}$.** The prediction is $116591810(43)\times10^{-11}$ when the hadronic vacuum polarisation is taken from $e^+e^-$ data, which is a $4.2\sigma$ difference; and it moves towards the measurement when the same quantity is taken from the lattice, reducing the difference to about $1\sigma$.

**Why this is the section's closing example.** The disagreement is not between theory and experiment in any single corner. It is between two determinations of one non-perturbative quantity — the hadronic vacuum polarisation — which is case 8, the corner with no error bar. The most precise measurement in the section is therefore limited by the least controlled corner in it, and the four-corner assembly is what makes that visible. A reader who computes the QED loops to five loops and stops has computed the easy part.

## The Scoreboard

**Best accuracy achieved, by corner, against what sets it.**

| Corner | Accuracy achieved | Set by |
|---|---|---|
| 2 | $10^{-3}$ | $\alpha/\pi$ |
| 3 | $10^{-5}$ of the fine structure | $(Z\alpha)^2$ |
| 4 | $10^{-12}$ in $a_e$ | the $\alpha$ series, not the $1/m$ series |
| 5 | $10^{-2}$ in hydrogen | $\epsilon\sim Z\alpha$ |
| 6 | $10^{-6}$ | $m_\mu^2/M_W^2$ |
| 7 | $30\%$ | $1/N=1/3$ |
| 8 | no general statement | the absence of an expansion |
| 1 | the measurement's | the measurement |

**The table is not monotone in any coordinate.** That is the section's final structural claim, and it is why the lattice had to be drawn in six dimensions rather than one.

## Checks

1. The count. Eight corners, one of them the origin.
2. The four entries per corner. Coordinates, theory, check, failure.
3. The non-monotonicity. Accuracy is not ordered by any single coordinate.
4. The kinds of error. Four: a power of $\alpha$, a power of $Z\alpha$, $1/N$, and none.
5. Hydrogen. Six contributions from four corners, and the radius is an input.
6. The radius. $0.84\ \mathrm{fm}$, measured, and it limits a twelve-digit prediction.
7. The muon. Four corners in one number.
8. The hadronic vacuum polarisation. $6.9\times10^{-8}$, and the two determinations disagree.
9. The significance. $4.2\sigma$ with data-driven input, about $1\sigma$ with lattice input.
10. The conclusion. The worst corner sets the accuracy of the assembly.

## Summary

Eight corners, four kinds of error bar, and one origin. The table is the section in one page: what each corner discards, what it reproduces, and what it cannot.

The corners are not ordered by accuracy and are not used alone. The hydrogen spectrum needs four of them and is limited by a matching coefficient from the quark level; the muon's anomalous moment needs four and is limited by the one corner with no error bar at all.

That is the honest summary of the approximation lattice: the precision of a prediction is set by its worst input, and the lattice's purpose is to make the worst input visible rather than to hide it behind the best one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| assembly | a prediction built from several corners, matched at their shared thresholds |
| matching coefficient | a number taken from a corner below and used as an input above |
| scoreboard | the best accuracy achieved by each corner, and what sets it |
| non-monotonicity | the absence of any single ordering of the corners by accuracy |

## Further Reading

- [The Approximation Lattice](the-approximation-lattice-six-coordinates-eight-corners-and-why-the-limits-do-not-commute.html). The six coordinates, and the two pairs that do not commute.
- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). The four requirements, corner by corner.
- [Local and Low Energy: The Derivative Cut](local-and-low-energy-the-derivative-cut.html). Case 6, which supplies the matching coefficients the others use.
- [Strong Field: The Non-Perturbative Corner](strong-field-the-non-perturbative-corner.html). Case 8, and why its error bar is missing.
- [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). Case 1, the origin of every arrow.
