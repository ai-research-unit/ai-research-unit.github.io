# __Quantum Non-Relativistic: $v/c\to0$ Alone, and the Terms That Survive__

## Introduction

**The claim.** Move the velocity coordinate and leave the loop coordinate alone. The result is non-relativistic quantum electrodynamics: a theory of electrons, photons and nuclei in which the electron may still radiate, still carry an anomalous moment, and still be bound, but in which the positron has been integrated out. It is the corner in which the most precisely verified predictions in physics live.

**The answer.**

$$
\boxed{\;\mathcal{L}_{\mathrm{NRQED}}=\psi^\dagger\Bigl(iD_0+\frac{\mathbf D^2}{2m}+\frac{\mathbf D^4}{8m^3}+c_F\frac{e}{2m}\boldsymbol\sigma\cdot\mathbf B+c_D\frac{e}{8m^2}\nabla\cdot\mathbf E+\cdots\Bigr)\psi-\tfrac14F_{\mu\nu}F^{\mu\nu}\;}
$$

with $D_0=\partial_0+ieA_0$, $\mathbf D=\nabla-ie\mathbf A$, and the coefficients $c_F,c_D,\dots$ fixed by matching to QED at the electron mass.

**Why this corner is not the previous one.** [Classical Non-Relativistic](classical-non-relativistic-planck-first-then-velocity.html) also sends $v/c\to0$, but it sends $\hbar\to0$ first, and the difference is decisive: there the spin–orbit coefficient was a classical kinematic fact, here the $c_F$ that multiplies the magnetic moment is $1+\alpha/\pi+\cdots$ and the entire Lamb shift is a loop that survives the velocity limit. Same coordinate, different order, different theory.

## The Arrow

**Three routes, and they must agree.**

**Route one: Foldy–Wouthuysen.** Apply a unitary transformation that block-diagonalises the Dirac Hamiltonian in powers of $1/m$. The upper block becomes a two-component Hamiltonian with the kinetic correction $\mathbf p^4/8m^3$, the spin–orbit term, the Darwin term, and the magnetic coupling. The transformation is a series, and truncating it is the truncation of the corner.

**Route two: integrate out the antiparticle.** The Dirac field splits into a large and a small two-component part; the small part is solved for and substituted, which is the same transformation written as an elimination. The small component is *heavy* in the sense that its energy cost is $2m$, so removing it is an integration at the scale $2m$, and the price is a set of contact terms.

**Route three: match.** Write every operator allowed by the symmetries — Hermiticity, rotational invariance, parity, charge conjugation, and the residual $\mathrm{U}(1)$ — with arbitrary coefficients, and fix the coefficients by computing the same observable in full QED and in the corner. Route three is the one that makes the corner predictive beyond its leading terms, because it produces $c_F$ rather than assuming it.

**What the three routes share.** Each produces the same operator list, and each produces coefficients that are *not* free: they are functions of $\alpha$ and $\log(m/\mu)$. That is the structural statement — the corner has no new parameters, only matched ones.

## What the Corner Reproduces

**Five results, and the fourth is the one no other corner can produce.**

**The hydrogen spectrum to the fine structure.** The leading terms give the Bohr levels, the relativistic correction, the spin–orbit and the Darwin term, and the $j$-dependent fine structure follows. This is shared with the previous corner and is not the achievement.

**The Lamb shift, $1057.845\ \mathrm{MHz}$ for $n=2$.** The loop produces a $\log(m/\mu)$ that the corner's own operators carry as a coefficient; the physical prediction is independent of $\mu$. The corner reproduces the measured splitting, and it is the first corner in this section that can.

**The hyperfine splitting, $1420.405751\ \mathrm{MHz}$ for the $1s$ level.** The spin–spin interaction is a tree-level operator of the corner; its precision is limited by the proton's magnetic structure, which is a matching coefficient from the quark level and not an object of this theory.

**The electron's anomalous moment to twelve digits.** $a_e=1.15965218059(13)\times10^{-3}$ measured, and the corner's series in $\alpha$ reproduces it to the precision of the measurement. This is the corner's signature, because it requires the loop and forbids the pair: the leading term is $\alpha/2\pi$, and the next terms are known.

**The $1s$–$2s$ transition in hydrogen.** Measured to a relative $10^{-15}$, and predicted to that accuracy in the corner once the proton radius is supplied. The corner is not the limit: the limit is the radius.

## What the Corner Cannot Reproduce

**Four failures, and the first is a boundary rather than a defect.**

**No pairs, so no positronium and no $e^+e^-\to\ldots$.** The positron has been integrated out, and a bound state of an electron and a positron is a state of the deleted field. Any process above $2m_e$ is outside.

**No running of $\alpha$ above $2m_e$.** The corner has a fixed coupling and a matching scale. The logarithm that would be the running is inside $c_F$ and the other coefficients; a process at $10\ \mathrm{GeV}$ is not described here, it is described by the corner that integrates out the $W$.

**The proton radius is an input, not an output.** The muonic-hydrogen Lamb shift is measured to $202.37\ \mathrm{meV}$ and the theory is limited by the proton charge radius, whose two determinations — from electronic hydrogen and from muonic hydrogen — differ by about $4\%$ in the radius. That discrepancy is not a failure of this corner: it is the statement that the radius is a matching coefficient of a lower-energy theory, and the corner is exactly as precise as the number fed to it.

**The Uehling potential's long tail is a matching, not a derivation.** The vacuum-polarisation correction to the Coulomb potential is a loop of the deleted field; in the corner it appears as a contact term plus a series, valid only at distances longer than $1/m$. At distances of order $1/m$ the corner has nothing to say.

## The Error Bar, Stated

**The corner's own expansion parameter is $Z\alpha$, and the achieved accuracy is far better than it suggests.**

| Source | Size | Note |
|---|---|---|
| the non-relativistic expansion | $(Z\alpha)^2=5.3\times10^{-5}$ | the truncation of the $1/m$ series |
| the omitted pair terms | $\exp(-2mr)$ | exponentially small at atomic distances, and this is why the corner works so well |
| the matching coefficients | $\mathcal{O}(\alpha^n)$ | order by order in $\alpha$, known to high $n$ |
| external inputs | the proton radius | the actual limitation |

**The reason the corner beats its expansion parameter is the exponential.** The deleted field's effects are suppressed by $e^{-2mr}$, which at the Bohr radius is $e^{-2/\alpha}\approx e^{-274}$ — an astronomically small number. A corner that deletes a field heavier than the inverse distance of interest does not pay a power of the small parameter; it pays an exponential, and that is why the non-relativistic corner of QED is the most accurate corner in physics.

## Checks

1. The move. $v/c\to0$ alone, with the loop kept.
2. The operator list. Four leading operators, with coefficients fixed by matching.
3. The three routes. Foldy–Wouthuysen, elimination, matching, and they agree.
4. The Lamb shift. $1057.845\ \mathrm{MHz}$, reproduced, and impossible in the previous corner.
5. The hyperfine splitting. $1420.405751\ \mathrm{MHz}$, limited by the proton's structure.
6. The anomalous moment. Twelve digits, and it needs the loop.
7. The pairs. Deleted, and positronium is outside.
8. The running. Not in the corner; it is in the matching.
9. The proton radius. An input, and the actual limit of the prediction.
10. The exponential. $e^{-2mr}$, which is why the corner is the most accurate one available.

## Summary

Sending $v/c\to0$ while keeping the loop gives non-relativistic QED: electrons, photons and nuclei, with the positron integrated out and its effects compressed into matched coefficients.

The corner reproduces the Lamb shift, the hyperfine splitting, and the anomalous magnetic moment to twelve digits, and it does so because the deleted field costs an exponential rather than a power. It cannot produce a pair, a positronium state, or the running above the electron mass, and its sharpest prediction is limited by the proton radius, which is a matching coefficient from below rather than an object of the theory.

The corner's lesson for the lattice is that the size of an error is not the size of the expansion parameter: a field whose mass exceeds the inverse distance of interest is deleted at the cost of $e^{-2mr}$, and a corner that can make that deletion is more accurate than its coordinates suggest.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| NRQED | non-relativistic QED, this corner |
| $c_F$ | the coefficient of the magnetic moment operator, $1+\alpha/\pi+\cdots$ |
| $c_D$ | the coefficient of the Darwin operator |
| matching | fixing a coefficient by requiring two theories to agree on one observable |
| $e^{-2mr}$ | the exponential suppression of a deleted heavy field at distance $r$ |

## Further Reading

- [Classical Non-Relativistic: $\hbar\to0$ First, Then $v/c\to0$](classical-non-relativistic-planck-first-then-velocity.html). The same coordinate in the other order.
- [Local and Low Energy: The Derivative Cut](local-and-low-energy-the-derivative-cut.html). The other corner that works by deleting a field.
- [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html). The leading order of the arrow.
- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). Why the exponential changes the error budget.
- [The Twelve Fermion Kinetic Rows](the-twelve-fermion-kinetic-pieces-nine-massive-species-three-neutrinos-and-their-currents.html). The rows this corner expands.
