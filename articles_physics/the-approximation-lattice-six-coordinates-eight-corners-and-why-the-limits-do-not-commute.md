# __The Approximation Lattice: Six Coordinates, Eight Corners, and Why the Limits Do Not Commute__

## Introduction

**The claim.** [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html) writes the complete Lagrangian in eight lines. That expression is one point in a space of theories, and every calculable statement in physics is a different point, reached from it by shrinking one or more of six independent expansion parameters. A limit is legitimate when three things are said before the result: which coordinates were moved, how far, and what error the movement incurred.

**The answer.**

$$
\boxed{\;6\ \text{coordinates},\qquad 8\ \text{named corners},\qquad \text{at least }2\ \text{pairs of limits that do not commute}\;}
$$

**Why a lattice and not a list.** Approximations are usually presented as a list — non-relativistic quantum mechanics, the classical limit, the Fermi theory — with no relation between the entries and no statement of where one stops being usable. A list cannot answer the only question that matters when a calculation is quoted: is this number's error dominated by the approximation I just made, or by one I made three steps earlier? A lattice answers it, because a point in it carries its distance from the origin.

**What the origin is.** The complete Lagrangian, and nothing else. No corner of this section adds a term. Every one of them is reached by *discarding* — a loop, a component, a derivative, a non-perturbative sector — and discarding is the only operation that keeps the parameter count at nineteen. That is the structural claim of the section, and it is what makes the seven corners below a study of one theory rather than seven theories.

## The Six Coordinates

**Each is an independent small (or large) quantity, and each suppresses a different class of term.**

| # | Coordinate | Small when | What vanishes with it | Sectors touched |
|---|---|---|---|---|
| 1 | $\hbar$, or the loop order | tree level | loops, running, anomalies, vacuum polarisation, every width that is a loop effect | all |
| 2 | $v/c$, or $p^2/m^2$ | non-relativistic | antiparticles, pair production, and every relativistic correction including spin–orbit | $\tfrac12$, $0$, $1$ |
| 3 | $p/\Lambda$ | low energy | operators of dimension five and above, hence every contact term and every non-renormalisable coupling | all |
| 4 | $\alpha$, $\alpha_s$, $y$ | perturbative | solitons, instantons, monopoles, confinement, the whole non-perturbative sector | all |
| 5 | $1/N$ and the gradient | mean field | the quantum potential, fluctuations, the discrete spectrum | fluids, large-$N$ |
| 6 | $\hbar/\partial S$, or $\partial S$ large | adiabatic, eikonal | interference, the fringe contrast between separated amplitudes | $\tfrac12$ (WKB $\to$ BMT) |

**The numbers, so that the coordinates are not abstractions.** $\alpha=1/137.036$; $\alpha_s(m_Z)=0.118$ and rising below it; $v/c=Z\alpha=7.3\times10^{-3}$ for the electron in hydrogen, so $(v/c)^2=5.3\times10^{-5}$; $p/\Lambda$ equal to $1$ at the scale of the completions the corpus does not have a name for, and $10^{-3}$ at the electroweak scale in a process at $100$ MeV; $N=3$ for colour, which is why the large-$N$ coordinate is the weakest of the six here.

**The coordinate that is not a parameter of the list.** $\Lambda$ appears in no row of the forty-nine and in none of the nineteen. It is the scale at which the eight-line Lagrangian stops being the whole story, and the theory is silent about its value. Sending $p/\Lambda\to0$ therefore states something about the *process* and nothing about the theory — which is why [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) can exclude the dimension-six operators by dimension alone while [The Loop-Induced Pieces](the-loop-induced-pieces-the-tree-level-census-omits.html) still has to generate three of them.

## Why Six and Not One

**A single "small parameter" is a category error, and the numbers show it.** Four of the six are of order $10^{-3}$ to $10^{-1}$, one is $1/3$ at best, and one can be anything: a muon in a storage ring has $\gamma=29.3$, so $v/c=0.99942$ and the relativistic coordinate is not small at all while the quantum one is as small as ever. A calculation that quotes one error and means "the expansion parameter" has silently assumed that the six move together.

**They do not.** $\alpha_s$ grows as the other coordinates shrink; $v/c$ grows with energy while $p/\Lambda$ grows with it too, so an experiment that improves one makes the other worse; $1/N$ is stuck at $1/3$ and is not improvable by any experiment, which is the honest reason the mean-field corner is the least predictive of the seven.

**What the six have in common is only the origin.** Each coordinate is a ratio of a quantity the process supplies to a quantity the theory supplies — an energy to a mass, a coupling to $4\pi$, a wavelength to a curvature scale. That is why the lattice is finite-dimensional and why its corners can be enumerated.

## The Lattice Is Not a Line

**Two pairs of limits do not commute, and each non-commutation is a piece of physics rather than a technicality.**

### First pair: $\hbar$ and $v/c$, which is the Thomas precession

**The two orders.** Take $\hbar\to0$ first and then $v/c\to0$: the spin is still a relativistic object, its precession is the BMT equation, and expanding that equation in $v/c$ leaves a spin–orbit term whose coefficient is $\tfrac12$ of the value a naive substitution would give. Take $v/c\to0$ first and then $\hbar\to0$: the spin is a Galilean vector, it does not precess, and the $\tfrac12$ has nowhere to come from, because there is no comoving frame to rotate.

**So the commutator of the two limits is the Thomas term itself.** The naive coefficient is the one a scalar's angular momentum would have; the measured coefficient is half of it; and the difference is the Wigner rotation of the frame that carries the spin. A reader who takes the non-relativistic limit first and then wonders where the factor went has taken the limits in the wrong order, and no amount of care in the later step recovers it.

**This is the section's one exact demonstration.** It is exact in the sense that the two orders differ by a definite, computable term, not by a remainder of unknown size, and it is why [Thomas Precession as a Biquaternion Rotor Effect](thomas-precession-as-a-biquaternion-rotor-effect.html) is cited from both corners rather than from one.

### Second pair: $\hbar$ and $p/\Lambda$, which is the anomalous magnetic moment

**The two orders.** Take $p/\Lambda\to0$ first, keeping loops: the theory is the renormalisable Standard Model with its full quantum corrections, and the electron's magnetic moment is $g=2(1+\alpha/2\pi+\cdots)=2.00232\ldots$, which is measured. Take $\hbar\to0$ first: the tree-level theory, and $g=2$ exactly, with the anomaly zero.

**So the commutator is $a=(g-2)/2$ in its entirety.** The anomaly is a loop effect that exists in exactly one order of the two limits, and this is why it is quoted as an $\mathcal{O}(\alpha)$ quantity and never as a correction to a tree-level value: at tree level there is nothing to correct. The same structure produces the whole of the running of $\alpha$ and the whole of the $\mathrm{U}(1)$ anomaly, which is why coordinate 1 and coordinate 3 must be moved in the stated order whenever a coefficient is matched between them.

**The lesson in one line.** A limit is a path, not a projection, and the path is part of the result.

## The Eight Corners

**Case 1 is the origin and the other seven are the corners.**

| Case | Coordinates moved | Resulting theory | Observable that tests it |
|---|---|---|---|
| 1 | none | the complete Lagrangian | everything |
| 2 | $\hbar\to0$ | Klein–Gordon, Proca, Dirac, Madelung–Hamilton–Jacobi | Proca and KG polarisation; $g=2$ |
| 3 | $\hbar\to0$, then $v/c\to0$ | Pauli, then Schrödinger, with the Thomas factor | fine structure, partial |
| 4 | $v/c\to0$ alone | NRQED | Lamb shift, hyperfine, $a_e$ |
| 5 | $\hbar\to0$, $\partial S$ large | Hamilton–Jacobi with BMT and Thomas | spin precession in storage rings |
| 6 | $p/\Lambda\to0$ | Fermi theory, then the renormalisable Standard Model | muon lifetime, $\beta$ decay |
| 7 | $1/N\to0$, gradients | the relativistic spin fluid | the fluid equations |
| 8 | $\alpha$ large | solitons, instantons | none measured |

**Cases 2 to 7 introduce no new parameter.** Each is the complete Lagrangian with something discarded, and each of the seven articles that follow shows the discarded piece explicitly. Case 8 is the exception in both directions: it discards the expansion rather than a term, and it is the only corner whose error bar this section cannot supply.

## What a Point Means

**A case is a region, not a point.** Saying "non-relativistic" states a coordinate and not a distance. The distance must be given, and the three quantities that give it are the expansion parameter's value, the order at which the series was truncated, and the size of the first neglected term.

**Errors from independent coordinates add in quadrature; errors from one coordinate do not.** A calculation at $\mathcal{O}(\alpha)$ with the non-relativistic expansion at $\mathcal{O}(v^2/c^2)$ has two independent remainders and their sum in quadrature is the error; a calculation that keeps $\alpha^2$ but drops $\alpha^3$ has one remainder and no quadrature to do. The rule matters because the coordinates differ in size by orders of magnitude, and a budget that adds them linearly will be dominated by whichever is largest, correctly or not.

**The error bar is the deliverable.** [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html) states the four requirements a corner must satisfy, and the first of them is this one: a truncation without a size is a claim, and a claim is not a result.

## Checks

1. The count of coordinates. Six, and each suppresses a different class of term.
2. The count of corners. Eight, one of them the origin.
3. The first non-commutation. $\hbar$ before $v/c$ keeps the Thomas factor; the reverse order loses it, and the difference is the term.
4. The second non-commutation. $p/\Lambda$ before $\hbar$ gives $a=\alpha/2\pi$; the reverse gives $a=0$, and the difference is the anomaly.
5. The parameter count. No corner adds a number; case 8 adds none either, it only removes the expansion.
6. The values. $\alpha=1/137.036$; $(Z\alpha)^2=5.3\times10^{-5}$; $\alpha_s(m_Z)=0.118$; $N=3$.
7. The coordinate outside the list. $\Lambda$ is a scale of a completion and not a parameter of the forty-nine.
8. The independence. A muon at $\gamma=29.3$ has $v/c=0.99942$ while $\hbar$ is as small as ever, so the six do not move together.
9. The direction of every move. Each corner discards; none adds.
10. The deliverable. Every corner states its truncation and its error, and a corner that cannot is named as such.

## Summary

The complete Lagrangian is the origin of a six-dimensional lattice of approximation parameters: loop order, velocity, momentum over the cutoff, coupling, $1/N$ with gradients, and the adiabatic ratio. Eight named corners sit in it, and seven of them are reached from the origin by discarding something, which is why the parameter count does not move.

At least two pairs of limits do not commute, and each non-commutation is a measured quantity: the Thomas precession is the difference between taking the classical limit before and after the non-relativistic one, and the anomalous magnetic moment is the difference between taking the derivative cut before and after the loop cut. A limit is therefore a path, and a path must be stated.

The rest of this section is one article per corner, each with the four requirements of the discipline: the truncation with its error, the explicit arrow from the eight-line Lagrangian, the known result it must reproduce, and the statement of what it fails to reproduce.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| coordinate | one of the six expansion parameters |
| corner or case | a point of the lattice, specified by which coordinates moved |
| origin | case 1, the complete Lagrangian with nothing discarded |
| commutator of two limits | the difference between the two orders, which is a physical quantity |
| truncation | the order at which a series was stopped, with the size of the first neglected term |

## Further Reading

- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). The four requirements, applied to every corner.
- [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). The origin: the eight-line Lagrangian.
- [The Eight Corners in One Table](the-eight-corners-in-one-table.html). The whole lattice on one page, with errors.
- [Thomas Precession as a Biquaternion Rotor Effect](thomas-precession-as-a-biquaternion-rotor-effect.html). The first non-commutation, computed.
- [The Non-Relativistic Limit of Relativistic Mechanics](the-non-relativistic-limit-of-relativistic-mechanics-in-biquaternionic-form.html). The second coordinate, in the corpus's variables.
