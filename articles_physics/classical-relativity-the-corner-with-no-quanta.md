# __Classical Relativity: The Corner with No Quanta__

## Introduction

**The claim.** Move one coordinate, $\hbar\to0$, and nothing else. The complete Lagrangian becomes a set of classical field equations, one per sector: Yang–Mills and Maxwell for the gauge fields, Proca for the massive vectors, a nonlinear Klein–Gordon equation for the scalar, and the Dirac equation read as a classical spinning particle for the fermions. Relativity survives in full; spin survives; antiparticles survive. What dies is the loop.

**The answer.**

$$
\boxed{\;\hbar\to0,\ \text{tree level},\qquad \text{error}\ \frac{\alpha}{\pi}\approx2.3\times10^{-3}\ (\text{electroweak}),\qquad \frac{\alpha_s}{\pi}\approx4\%\ (\text{QCD})\;}
$$

**Why this corner is the one usually called "classical".** It is the corner in which the fields are $c$-numbers and the sources are currents. It is not the corner of Newtonian mechanics: $v/c$ has not moved, so the equations are still Lorentz invariant, the dispersion laws still carry $\sqrt{p^2+m^2}$, and a particle may still be created in pairs if the source supplies the energy. That is why the corner is named classical *relativistic*, and why [Classical Non-Relativistic](classical-non-relativistic-planck-first-then-velocity.html) is a second move and not the same one.

## The Arrow, Sector by Sector

**The arrow has three branches, and each starts at a row of the eight lines.**

### The gauge sector is already classical

**The curvature rows are classical actions.** $-\tfrac14G^a_{\mu\nu}G^{a\mu\nu}$ is a function of $c$-number fields, and varying it gives the Yang–Mills equation $D_\mu G^{a\mu\nu}=j^{a\nu}$ with no reference to $\hbar$. What the limit removes is not the equation but its corrections: the vacuum polarisation, the running of $g_s$, the $\mathrm{U}(1)$ anomaly, and the loop-induced vertices.

**The massive vectors keep their Proca form.** $-\tfrac14W^a_{\mu\nu}W^{a\mu\nu}+\tfrac12M_W^2W^+_\mu W^{-\mu}$ is the Proca Lagrangian, and its equation is $\partial_\mu W^{\mu\nu}+M_W^2W^\nu=j^\nu$, hence $\partial_\nu W^\nu=0$: four degrees of freedom, three of them physical. The mass term is a row of the list and it is not removed here, which is the statement that this corner is not the symmetric phase.

**One consequence worth stating.** In this corner the $W$ and $Z$ are ordinary massive vector fields with three polarisations each, and the Goldstone modes are already inside the longitudinal polarisation. Nothing in the corner remembers that they came from a doublet, which is why [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html) assigns them no ancestor term.

### The scalar sector becomes Hamilton–Jacobi

**The amplitude and the phase.** For a complex scalar, writing $\phi=\sqrt\rho\,e^{iS/\hbar}$ and separating real and imaginary parts of the Klein–Gordon equation gives two equations: the continuity equation $\partial_\mu(\rho\,\partial^\mu S)=0$ and the Hamilton–Jacobi equation $(\partial S)^2=m^2$ with a quantum potential $-\hbar^2\Box\sqrt\rho/\sqrt\rho$. Send $\hbar\to0$ and the quantum potential vanishes, leaving exactly Hamilton–Jacobi.

**In this category the scalar is real.** The single $h$ has no phase, so the branch above does not run through the $h$ row: the real scalar's classical equation is $\Box h+V'(h)=0$, a nonlinear Klein–Gordon equation with the cubic and quartic self-couplings. The Hamilton–Jacobi reading is a statement about the *complex* scalar, and in the corpus it belongs to [The Reverse Madelung Map](the-reverse-madelung-map-fluid-to-nonlinear-wave.html) and to the fluid articles. Stating this instead of pretending otherwise is the first requirement of [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html) applied to the article itself.

### The fermion sector becomes a spinning particle

**The Dirac equation survives; the interpretation changes.** $\bigl(i\slashed\partial-m\bigr)\psi=0$ is unchanged by $\hbar\to0$ — it is already a one-particle equation. What the limit does is remove the fermion loop, and what it leaves behind is a classical description in which the bilinears are the variables: the current $\bar\psi\gamma^\mu\psi$ is the four-velocity, the axial current $\bar\psi\gamma^\mu\gamma_5\psi$ is the spin four-vector, and the equation of motion for that spin is the BMT equation

$$
\frac{ds^\mu}{d\tau}=\frac{e}{m}\Bigl[F^{\mu\nu}s_\nu+\frac{g}{2}\bigl(s_\nu F^{\nu\rho}u_\rho\bigr)u^\mu\Bigr]+\cdots
$$

with $g=2$ exactly, because $g-2$ is a loop effect and the loop has been removed.

**Why $g=2$ exactly, and why that is the corner's signature.** The Dirac equation's magnetic moment is $g=2$ at the level of the classical bilinears: the Gordon decomposition of the current separates the convection from the magnetisation, and the magnetisation carries the coefficient $2$. Every departure from $2$ is a quantum correction, so a corner that sets $\hbar\to0$ and returns $g=2$ is internally consistent, and the measured $2.0023$ is the corner's first quantitative failure.

## What the Corner Keeps

**Four things that a reader might expect to lose and does not.**

| Kept | Because |
|---|---|
| Lorentz invariance | $v/c$ has not moved |
| spin and its precession | the BMT equation is a tree-level equation |
| antiparticles | $v/c$ has not moved, so the Dirac sea and pair creation remain |
| tree-level widths | the $W$, $Z$, $h$ and $t$ decay at tree level; those widths are in the corner |

**The fourth deserves emphasis.** It is common to describe the classical limit as "no decays", and that is wrong: a tree-level decay is a classical process in this sense, and its width is computable in the corner. What the corner cannot produce is a width that exists only because of a loop — the photon's, the gluon's, the neutrino's in the massless limit, and the entire $h\to\gamma\gamma$ channel.

## What the Corner Cannot Do

**Five failures, in descending order of size.**

**No anomalous magnetic moment.** $a_e=0$ against $1.1597\times10^{-3}$ measured. The relative error is $1.2\times10^{-3}$, which is $\alpha/2\pi$, and it is the corner's headline number.

**No running.** The couplings are constants here. A process at $100\ \mathrm{GeV}$ and the same process at $1\ \mathrm{GeV}$ are computed with the same $\alpha_s$, and the difference between them is a loop effect that the corner does not have. The error is $\alpha_s\log(Q_1/Q_2)/\pi$, which at a decade is about $9\%$ in $\alpha_s$ — an order of magnitude worse than the nominal $\alpha_s/\pi$.

**No $h\to\gamma\gamma$.** The decay is a loop process and the corner gives exactly zero for it, against a measured branching fraction of about $2.3\times10^{-3}$. This is the cleanest example in the section of a corner that is not merely imprecise but structurally silent: no order of the corner's own expansion produces the vertex.

**No Lamb shift.** The degeneracy of $2s_{1/2}$ and $2p_{1/2}$ is exact in the corner, and the measured splitting is $1057.845\ \mathrm{MHz}$.

**No vacuum polarisation, hence no charge screening.** The fine-structure constant is a number here, not a function of scale, and the muon's magnetic moment has no hadronic or electroweak contribution.

## The Error Bar, Stated

**Two numbers, and they differ by a factor of twenty.** For an electroweak observable the leading correction is $\mathcal{O}(\alpha/\pi)=2.3\times10^{-3}$; for a QCD observable it is $\mathcal{O}(\alpha_s/\pi)\approx3.8\%$. A process that involves both is a $4\%$ calculation, and quoting $10^{-3}$ for it would be false. The corner is therefore a $1\%$-level theory of the electroweak sector and a $4\%$-level theory of the strong sector, and the difference between those two statements is the whole content of the error budget.

**The corner's radius.** It is usable while the observable's loop correction is smaller than the effect being discussed. For a parity-violating asymmetry at tree level the correction is a few per cent and the corner is adequate; for a magnetic moment it is the entire signal and the corner is useless.

## Checks

1. The move. One coordinate, $\hbar$, and nothing else.
2. The gauge equations. Yang–Mills with a source, Proca with a mass, and no running.
3. The scalar equation. Nonlinear Klein–Gordon for the real $h$; Hamilton–Jacobi for the complex scalar, cited and not claimed.
4. The fermion equation. Dirac unchanged, with the bilinears as velocity and spin.
5. The magnetic moment. $g=2$ exactly, from the Gordon decomposition.
6. The antiparticles. Kept, because $v/c$ has not moved.
7. The widths. Tree-level widths kept; loop widths absent.
8. The failures. Five, and the largest is $\alpha/2\pi$.
9. The error. $2.3\times10^{-3}$ electroweak, $3.8\%$ QCD, and the smaller is not the one to quote.
10. The Goldstones. Inside the longitudinal polarisations, and not remembered.

## Summary

Setting $\hbar\to0$ and moving nothing else turns the eight-line Lagrangian into the classical field equations of its sectors: Yang–Mills and Proca for the gauge fields, a nonlinear Klein–Gordon equation for the real scalar, and the Dirac equation read as a classical spinning particle with $g=2$ exactly.

The corner is relativistic in full. It keeps Lorentz invariance, spin and its BMT precession, antiparticles, and every tree-level width. It loses every loop: the anomalous moment, the running, the vacuum polarisation, the Lamb shift, and the whole of $h\to\gamma\gamma$.

Its error is $\alpha/\pi$ for the electroweak sector and $\alpha_s/\pi$ for the strong one, which makes it a $1\%$ theory and a $4\%$ theory rather than a single thing. That split is the reason the next two corners exist: the non-relativistic one keeps the loop and drops the antiparticle, and the low-energy one drops the heavy field and keeps everything else.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g$ | the gyromagnetic ratio, $2$ in this corner and $2.0023$ measured |
| BMT | the Bargmann–Michel–Telegdi equation for spin precession |
| tree level | no loops, i.e. $\hbar\to0$ in the loop-order sense |
| $\alpha/\pi$ | the size of the leading electroweak loop correction |

## Further Reading

- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). The four requirements this article applies to itself.
- [Classical Non-Relativistic: $\hbar\to0$ First, Then $v/c\to0$](classical-non-relativistic-planck-first-then-velocity.html). The next move, and the one where the order matters.
- [The Approximation Lattice](the-approximation-lattice-six-coordinates-eight-corners-and-why-the-limits-do-not-commute.html). Why $g-2$ is the commutator of two corners.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html). The Gordon split and the non-relativistic limit, in the corpus's variables.
- [The Reverse Madelung Map](the-reverse-madelung-map-fluid-to-nonlinear-wave.html). The amplitude–phase split used above for the complex scalar.
