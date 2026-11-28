# __Local and Low Energy: The Derivative Cut and the Fermi Theory__

## Introduction

**The claim.** Move the derivative coordinate, $p/\Lambda\to0$, and keep everything else. Every operator of dimension five and above is suppressed by a power of $\Lambda$, so the theory reduces to the renormalisable one: the eight lines, forty-nine rows, nineteen parameters. This is the corner the category has been written in from the beginning, and saying so makes the census rule a truncation rather than a postulate.

**The answer.**

$$
\boxed{\;\mathcal{L}=\mathcal{L}^{(4)}+\sum_{d\ge5}\frac{C_i}{\Lambda^{d-4}}\,\mathcal{O}_i\;\xrightarrow{\ p/\Lambda\to0\ }\;\mathcal{L}^{(4)}\;\text{— and }\Lambda\ \text{is in none of the eight lines}\;}
$$

**Why this is the category's own corner.** [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) admits a piece when it is a Lorentz scalar, invariant under $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}}$, built from the broken-phase fields, and of mass dimension at most four. The fourth condition is this article's limit, stated once and applied to every row. That is why the category is a standard model effective field theory truncated at its leading order, and why the truncation should be named rather than left implicit.

## The Arrow

**The archetype is the Fermi theory, and it is the same arrow every threshold uses.**

**Step one: the $W$ propagator at low momentum.** The charged-current rows couple fermions to $W$ with strength $g/\sqrt2$. Exchanging a $W$ between two currents gives, at momentum transfer $q\ll M_W$,

$$
\frac{g^2/2}{q^2-M_W^2}\;\longrightarrow\;-\frac{g^2}{2M_W^2}\Bigl(1+\frac{q^2}{M_W^2}+\cdots\Bigr).
$$

**Step two: the contact term.** The leading piece is a four-fermion operator with no propagator, and its coefficient defines the Fermi constant:

$$
\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}=1.1663787\times10^{-5}\ \mathrm{GeV}^{-2}.
$$

**Step three: the corrections are the tower.** The terms in $q^2/M_W^2$ are the dimension-six operators of the local expansion, and they are the size of the error. The arrow has therefore produced both the leading term and its own error bar.

**The other thresholds are the same arrow.** Integrating out the $Z$ gives the neutral-current contact terms; integrating out the top gives the $W$ and $Z$ self-energies and the $h\gamma\gamma$, $hgg$ couplings; integrating out the Higgs gives the $W$ and $Z$ masses as matching conditions rather than as a condensate. Each is a coefficient, and none is a row.

## The Tower, and Where the Category Stops

**Dimension five, dimension six, and the reason the list ends at four.**

| Order | Examples | Status in the category |
|---|---|---|
| $d=4$ | the forty-seven rows | the list |
| $d=5$ | the Weinberg operator $\ell\ell HH$; $hF_{\mu\nu}F^{\mu\nu}$ | omitted, and the loop-induced ones are named in [The Loop-Induced Pieces](the-loop-induced-pieces-the-tree-level-census-omits.html) |
| $d=6$ | four-fermion contact terms, dipole moments, $H^\dagger H\,F^2$ | excluded by dimension in [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) |

**The size of the tower is the reason for the cut.** The dimension-six basis, counted with flavour, is thousands of operators and thousands of coefficients; the dimension-eight basis is larger again. A list that included them would have no end and no nineteen. The cut at four is the statement that the coefficients of the tower are unknown, and a theory with thousands of unknown coefficients is not a theory but a parametrisation.

**The cut is also a physical statement.** Every $d>4$ operator is suppressed by a power of a scale that has not been observed. The category's claim is that the eight lines describe the data at the accuracy the data has, and that claim is testable: a deviation from the eight lines at the $10^{-3}$ level in a four-fermion process would be a dimension-six coefficient.

## What the Corner Reproduces

**Four results, and the first is exact at leading order.**

**The muon lifetime.** $\tau_\mu=2.1969811\ \mu s$ measured, and the corner gives $192\pi^3/(G_F^2m_\mu^5)$ with phase-space and radiative corrections. The prediction uses no $W$ and no $M_W$: the corner has one number, $G_F$, and it is measured in the same decay. The check is therefore on the *corrections*, which are known to two loops.

**$\beta$ decay and the whole charged-current phenomenology.** Neutron decay, pion decay, kaon decay: each is a four-fermion process with a coefficient fixed by $G_F$ and a matrix element. The corner is the language in which nuclear and particle physics was written before the $W$ was seen.

**The $d\le4$ list itself.** The corner is the only one whose content is a finite list, and reproducing the list — that no other $d\le4$ piece exists — is the check performed in [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html).

**The running, as a matching condition.** $\alpha_s$ at $1\ \mathrm{GeV}$ and at $m_Z$ are related by integrating out the heavy quarks; the corner does not run, it *matches*, and the two descriptions agree at the threshold by construction.

## What the Corner Cannot Reproduce

**Four failures, and the third is a warning about the whole category.**

**The $W$ as a propagating field.** Above its threshold the $W$ is a degree of freedom with a width and a resonance shape. The corner has a contact term, and a contact term has no resonance. The $W$ width, $2.085\ \mathrm{GeV}$, is a matching condition here and a process in case 1.

**The logarithms above the threshold.** A process at $10\ \mathrm{TeV}$ in a theory matched at $m_Z$ has logs of $10\ \mathrm{TeV}/m_Z$ that the corner cannot generate; they must be resumed by the renormalisation group. A corner without resummation is accurate to one logarithm and no further.

**The loop-induced vertices are coefficients, not loops.** In the corner $h\to\gamma\gamma$ is a contact term whose coefficient was computed by matching. If that coefficient is set to its tree-level value, which is zero, the corner predicts zero. This is the failure that makes the derivative cut and the loop cut non-commuting, and it is the reason [The Approximation Lattice](the-approximation-lattice-six-coordinates-eight-corners-and-why-the-limits-do-not-commute.html) insists on the order.

**The parameter values are inputs.** The nineteen numbers are matching coefficients of the local expansion, and the corner says nothing about their values. A reader who expects the corner to explain why $m_\mu/m_e=206.77$ has mistaken the corner for the origin: the origin has the same nineteen numbers and does not explain them either.

## The Error Bar, Stated

**Two powers of the ratio, and one logarithm.**

| Source | Size | Note |
|---|---|---|
| the leading correction, $\mathcal{O}(m_\mu^2/M_W^2)$ | $1.7\times10^{-6}$ | the first dimension-six coefficient |
| the next order | $3\times10^{-12}$ | and negligible |
| the un-resummed logarithm | $\alpha_s\log(Q/m)$ | the real limitation at high $Q$ |

**The corner's radius is the threshold itself.** Below $M_W$ it is accurate to a part in $10^6$ in the muon sector and better elsewhere; above $M_W$ it is not a description at all, because the field it deleted is the one that is being produced. The radius is not a matter of accuracy; it is a matter of the field content.

## Checks

1. The move. $p/\Lambda\to0$, and nothing else.
2. The rule. The census condition $d\le4$ is this limit.
3. The archetype. $G_F/\sqrt2=g^2/8M_W^2$, from the $W$ propagator at low momentum.
4. The number. $G_F=1.1663787\times10^{-5}\ \mathrm{GeV}^{-2}$.
5. The lifetime. $2.1969811\ \mu s$, from $G_F$ and phase space.
6. The tower. $d=5$ omitted and named; $d=6$ excluded by dimension.
7. The size of the tower. Thousands of coefficients, which is why the cut is at four.
8. The failures. No $W$ resonance, no logs, no loop vertices, no parameter values.
9. The error. $1.7\times10^{-6}$ from $m_\mu^2/M_W^2$.
10. The radius. $M_W$, and beyond it the corner is silent.

## Summary

Sending $p/\Lambda\to0$ produces the renormalisable theory: the eight lines, forty-nine rows, nineteen parameters, and no scale $\Lambda$ anywhere in them. The census rule of this category is exactly this truncation, which is why the category is an effective field theory at its leading order.

The arrow is the integration of a heavy field, and the Fermi constant is its archetype: $G_F/\sqrt2=g^2/8M_W^2$ from the $W$ propagator at low momentum, with the corrections forming the tower that the category deliberately omits. The tower's size is the justification for the cut; its unobserved coefficients are the reason the cut is a physical statement rather than a convenience.

The corner reproduces the muon lifetime, the whole charged-current phenomenology, and the finite $d\le4$ list, to a part in $10^6$. It cannot produce a resonance, a resummed logarithm, a loop-induced vertex, or a parameter value, and above $M_W$ it is not a description of anything.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda$ | the scale of the omitted tower; not a parameter of the list |
| matching | fixing a coefficient by requiring agreement with the theory above the threshold |
| $G_F$ | the Fermi constant, a matching coefficient |
| the tower | the $d\ge5$ operators, ordered by dimension |
| radius of the corner | the threshold $M_W$, beyond which the deleted field is produced |

## Further Reading

- [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html). The $d\le4$ condition, which is this corner's truncation.
- [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html). Why the tower is excluded by dimension.
- [The Loop-Induced Pieces](the-loop-induced-pieces-the-tree-level-census-omits.html). The three $d=5$ operators the cut removes and the loops regenerate.
- [What the List Omits](what-the-list-omits-ghosts-the-theta-term-neutrino-mass-and-gravity.html). The omissions that are not the tower.
- [Quantum Non-Relativistic: $v/c\to0$ Alone](quantum-non-relativistic-velocity-alone-and-the-terms-that-survive.html). The other corner that works by deleting a field.
