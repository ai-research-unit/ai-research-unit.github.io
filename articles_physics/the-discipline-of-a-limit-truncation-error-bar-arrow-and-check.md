# __The Discipline of a Limit: Truncation, Error Bar, Arrow and Check__

## Introduction

**The claim.** Every corner of [The Approximation Lattice](the-approximation-lattice-six-coordinates-eight-corners-and-why-the-limits-do-not-commute.html) is reached by discarding something from the eight-line Lagrangian, and every discard costs a known amount. Four requirements make the cost explicit, and a calculation that omits any of them is a claim rather than a result. The requirements are not stylistic. Each one closes a way in which a limit can be wrong while looking right.

**The answer.**

$$
\boxed{\;\text{truncation with error}\;\to\;\text{arrow}\;\to\;\text{known check}\;\to\;\text{named failure}\;}
$$

**Why four and not one.** An error bar alone says how wrong the answer might be; it does not say what the answer is. The arrow says what was discarded and therefore what the answer should be. The check says whether the arrow was drawn correctly, by comparing against a case that is already known independently. The failure says where the corner ends, which is the information a reader needs in order to know whether the corner applies to the problem in front of them.

## The Four Requirements

**Each requirement, and the failure mode it excludes.**

| # | Requirement | What it forces | What its absence looks like |
|---|---|---|---|
| 1 | the truncation and its error | a number and a size, e.g. "to $\mathcal{O}(v^2/c^2)$, tree level, error $\approx10^{-5}$" | a limit quoted as exact, with the first neglected term larger than the effect being discussed |
| 2 | the arrow | an explicit derivation from the eight-line Lagrangian to the corner | a corner asserted as a separate theory, with no statement of what was dropped |
| 3 | the known check | a result already established independently, reproduced | a formalism validated only against itself |
| 4 | the named failure | the effect the corner cannot produce, stated | a corner presented as universal, and an unexplained discrepancy later |

**The fourth is the one that distinguishes a systematic study from a collection of claims.** A corner that reproduces five known results and silently misses a sixth has been validated on the five; the sixth is where the reader learns the boundary.

## Requirement One: The Truncation and Its Error

**The statement has a fixed form.** *"To $\mathcal{O}(x^n)$ in the coordinate $x$, with the other coordinates at the stated values, the error is the size of the first neglected term."* Nothing shorter is usable, because the reader cannot reconstruct which coordinate dominated.

**A worked example, in hydrogen.** The electron's speed is $v=Z\alpha c$, so the non-relativistic coordinate is $Z\alpha=7.3\times10^{-3}$ and its square is $5.3\times10^{-5}$. A calculation that keeps terms to $\mathcal{O}(v^2/c^2)$ therefore carries a relative error of order $10^{-5}$ from that coordinate alone, and the honest statement is "error $\approx10^{-5}$, dominated by the relativistic expansion". The fine structure is itself of order $(Z\alpha)^2$, which means a leading-order calculation and a fine-structure calculation differ by an amount comparable to the error of the leading one — the truncation order must be quoted together with the term being discussed, not separately.

**Dominance and quadrature.** Errors from independent coordinates add in quadrature; errors from the same coordinate do not. A calculation at $\mathcal{O}(\alpha)$ and $\mathcal{O}(v^2/c^2)$ has two independent remainders, of order $2.3\times10^{-3}$ and $5.3\times10^{-5}$, and the sum in quadrature is $2.3\times10^{-3}$ — the electroweak one dominates by a factor of forty, and quoting $10^{-5}$ as "the" error would be false. The budget is not a decoration; it decides which correction is worth computing.

**One coordinate can swamp another completely.** A tree-level width and the same width with one loop differ by $\mathcal{O}(\alpha)$; a matching coefficient computed to $\mathcal{O}(p^2/\Lambda^2)$ but used at $p/\Lambda=1$ has no error bar at all, because the expansion has no small parameter where it is being used. In that case the requirement is to say so and to change corner, not to quote a number.

## Requirement Two: The Arrow

**An arrow is a derivation, and there are only three ways to draw one.**

| Technique | What is done | Where it is used |
|---|---|---|
| substitute an ansatz | write the field as an amplitude times a phase, $e^{iS/\hbar}$, and read the real and imaginary parts | case 2 and case 5, the classical and adiabatic corners |
| integrate out a heavy field | solve the heavy field's equation of motion and substitute, or expand the propagator at low momentum | case 6, the Fermi theory and every threshold |
| expand in a basis | project on a complete set of operators of increasing dimension or increasing powers of $1/m$ | case 4, the non-relativistic expansion |

**Every arrow starts at a row of the complete Lagrangian.** The scalar's kinetic row produces the phase and therefore the Hamilton–Jacobi function of case 2; the $W$ mass row and the charged-current rows together produce the four-fermion operator of case 6; the fermion kinetic row, expanded in $1/m$, produces the Pauli terms of case 4. An arrow that cannot be traced to a row is not an arrow, and an approximation that needs a term the eight lines do not contain is not a corner of this lattice.

**The arrow also fixes what is not dropped.** Integrating out the $W$ does not merely delete it; the deletion generates a contact term with a coefficient fixed by the mass and the coupling that were removed. A corner with no generated term is a truncation, not an integration, and the difference matters as soon as a loop is computed inside the corner.

## Requirement Three: The Known Check

**Each corner has a result it must reproduce, and reproducing it validates the arrow.**

| Case | Corner | The check | What success means |
|---|---|---|---|
| 2 | classical relativistic | Hamilton–Jacobi from the phase; the Proca and Klein–Gordon dispersion laws; $g=2$ | the classical limit is the correct one and the spin is relativistic |
| 3 | classical non-relativistic | the Thomas factor $\tfrac12$ in the spin–orbit term; the Bohr spectrum | the order of the two limits was taken correctly |
| 4 | quantum non-relativistic | the Lamb shift, the hyperfine splitting, $a_e$ | loops and bound states coexist without antiparticles |
| 5 | WKB and eikonal | Bohr–Sommerfeld quantisation; the Born amplitude from the eikonal phase | the stationary-phase approximation has the right leading term |
| 6 | local and low energy | the muon lifetime from $G_F$; $\beta$ decay | the matching at the $W$ threshold is correct |
| 7 | mean field | the Euler equation and the continuity equation of a perfect fluid; quantised circulation $h/m$ | the hydrodynamic variables are the right ones |
| 8 | strong field | the instanton action $8\pi^2/g^2$; the $\mathrm{U}(1)$ anomaly | the non-perturbative sector is being described at all |

**The check is independent or it is nothing.** Reproducing a result that was used to construct the corner proves only consistency. The Thomas factor is a genuine check because it is measured, not assumed; the muon lifetime is a genuine check because $G_F$ is measured at low energy and the lifetime follows; the instanton action is a genuine check because the exponential is not visible in any order of perturbation theory.

## Requirement Four: The Named Failure

**Every corner fails somewhere, and the failure is part of its specification.**

**Case 2 has no anomalous moment.** At tree level $g=2$ exactly, so the corner predicts $a_e=0$ against a measured $1.16\times10^{-3}$. A reader who uses case 2 for a magnetic moment gets an answer wrong in the third digit and has no way to know it from within the corner.

**Case 3 loses the Lamb shift, and it loses it twice.** The fine structure it produces has the correct $j$-dependence and the correct Thomas factor, and it keeps the $2s_{1/2}$–$2p_{1/2}$ degeneracy that the Dirac spectrum has. The Lamb shift breaks that degeneracy by $1057.845\ \mathrm{MHz}$, and it is a loop effect, so the corner that sets $\hbar\to0$ cannot produce it at any order of its own expansion. This is why the corner is described as fine structure *partial* and not fine structure complete.

**Case 4 loses pair production, and therefore positronium.** The non-relativistic corner keeps the electron and the photon and deletes the positron; a bound state of an electron and a positron is outside it, and so is every process above the pair threshold. The running of $\alpha$ above $2m_e$ is likewise outside: the corner has a fixed $\alpha$ and the logarithm must be put in by matching.

**Case 5 fails at a turning point.** The WKB wavefunction diverges where the momentum vanishes, and the region around the turning point has to be replaced by an Airy function with connection formulas. The failure is localised and repairable, which is what makes the corner useful; a failure that is not localised would make it useless.

**Case 6 cannot produce the $W$'s own width.** The $W$ has been integrated out, so its decay is a matching condition on the four-fermion coefficient and not a process of the corner. Any question about a $W$ resonance is a question for case 1.

**Case 7 has no quantum potential.** The mean-field corner drops the term $\hbar^2\nabla^2\sqrt\rho/\sqrt\rho$, which is exactly the term that produces interference between separated packets. It reproduces the Euler equation and the quantised circulation and it cannot reproduce the double slit.

**Case 8 has no error bar.** This is the honest failure of the non-perturbative corner: in general there is no expansion parameter, and a number computed there is either exact by a symmetry, controlled by a lattice spacing, or uncontrolled. [Strong Field: The Non-Perturbative Corner](strong-field-the-non-perturbative-corner.html) states the three exceptions.

## The Failure Ledger

**One table, and it is the most useful page of the section.**

| Case | Reproduces | Cannot reproduce |
|---|---|---|
| 2 | classical field equations, $g=2$, tree widths | $a_e$, running, anomalies, $h\to\gamma\gamma$ |
| 3 | Thomas factor, Bohr spectrum, spin–orbit | Lamb shift, degeneracy breaking, $a_e$ |
| 4 | Lamb shift, hyperfine, $a_e$ | pairs, positronium, running above $2m_e$ |
| 5 | Bohr–Sommerfeld, eikonal phase, spin precession | tunnelling, turning points, exact spectra beyond two cases |
| 6 | muon lifetime, $\beta$ decay, the $d\le4$ list | the $W$ as a propagating field, logs above the threshold |
| 7 | Euler, continuity, quantised circulation | quantum potential, double slit, discrete spectrum |
| 8 | instanton action, anomaly, confinement | anything with a controlled error bar in general |

**The ledger is the section's summary in advance.** A reader who knows which row their problem is in knows which corner to use and which of its failures will bite.

## Checks

1. The count. Four requirements, and each closes a distinct failure mode.
2. The truncation form. A number, a size, and the coordinate that dominates.
3. The quadrature rule. Independent coordinates add in quadrature; a single coordinate does not.
4. The dominance example. $\alpha/2\pi=1.2\times10^{-3}$ against $(Z\alpha)^2=5.3\times10^{-5}$: forty to one.
5. The arrows. Three techniques, and every arrow traces to a row of the eight lines.
6. The integration rule. Removing a field generates a contact term; it does not merely delete.
7. The checks. Seven corners, seven independent results.
8. The failures. Seven failures named, and one corner with none available.
9. The Lamb shift. $\hbar\to0$ cannot produce it at any order, which is why case 3 is partial.
10. The ledger. Every corner appears once in each column.

## Summary

A corner of the approximation lattice is specified by four statements: the truncation with its error, the arrow from the complete Lagrangian, the known result it reproduces, and the effect it cannot produce.

The error is a budget and not a decoration. Independent coordinates add in quadrature, the largest coordinate dominates, and a corner used outside its radius has no error bar at all. The arrow is one of three techniques and always begins at a row of the eight lines, which is what keeps the parameter count at nineteen.

The named failure is the requirement most often omitted and most useful when present: it tells a reader where the corner stops, and it converts a discrepancy into a boundary rather than a puzzle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| truncation | the order at which the expansion was stopped, with the size of the first neglected term |
| arrow | the explicit derivation from the eight-line Lagrangian to the corner |
| check | an independently known result the corner must reproduce |
| named failure | the effect the corner provably cannot produce |
| radius of a corner | the coordinate value beyond which the truncation error exceeds the effect being computed |

## Further Reading

- [The Approximation Lattice](the-approximation-lattice-six-coordinates-eight-corners-and-why-the-limits-do-not-commute.html). The six coordinates and why the limits do not commute.
- [The Eight Corners in One Table](the-eight-corners-in-one-table.html). Every corner with its error and its failure, on one page.
- [Classical Relativity: The Corner with No Quanta](classical-relativity-the-corner-with-no-quanta.html). Requirement three, worked in full.
- [Quantum Non-Relativistic: $v/c\to0$ Alone](quantum-non-relativistic-velocity-alone-and-the-terms-that-survive.html). The corner where the failure ledger is shortest.
- [Strong Field: The Non-Perturbative Corner](strong-field-the-non-perturbative-corner.html). The corner with no error bar.
