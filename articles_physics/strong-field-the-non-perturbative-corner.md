# __Strong Field: The Non-Perturbative Corner and What It Refuses__

## Introduction

**The claim.** Every other corner is reached by sending a coordinate to zero. This one is reached by refusing to: the coupling is not small, so the expansion in $\alpha_s$ does not exist, and the objects that survive are the ones that cannot be expanded — solitons, instantons, condensates, and confinement. It is the only corner of the lattice whose error bar this section cannot supply, and it is also the only one where a total derivative becomes physical.

**The answer.**

$$
\boxed{\;\text{no expansion in }\alpha_s;\qquad \text{the instanton weight } e^{-8\pi^2/g^2}=e^{-2\pi/\alpha_s}\approx e^{-53}\ \text{at }m_Z\;}
$$

**What kind of corner this is.** The other seven are limits: a parameter is sent to zero and a term is discarded. Here nothing is discarded and nothing is sent to zero; the *method* is removed. The corner is therefore the complement of coordinate 4 rather than a point of the lattice, and calling it a corner is a deliberate abuse: it marks the region where the lattice's own expansion fails.

## What Survives Without the Expansion

**Four objects, and the first is the one that carries a number.**

**The instanton.** A finite-action solution of the Euclidean Yang–Mills equation with topological charge one. Its action is $S=8\pi^2/g^2=2\pi/\alpha_s$, so its weight in the path integral is $e^{-2\pi/\alpha_s}$, which at $\alpha_s(m_Z)=0.118$ is $e^{-53}\approx10^{-23}$. The exponential is invisible in every order of perturbation theory, which is exactly why the corner exists: $e^{-1/\alpha}$ has no Taylor series at $\alpha=0$.

**The $\theta$ term.** $(\theta g^2/32\pi^2)G\tilde G$ is a total derivative, and in the perturbative corners it can be integrated away. Here it cannot: an instanton is a configuration on which the integral of the total derivative is the winding number, so $\theta$ becomes a physical angle and the vacuum becomes a superposition of winding sectors. This is the structural surprise of the corner, and it is why [What the List Omits](what-the-list-omits-ghosts-the-theta-term-neutrino-mass-and-gravity.html) records $\theta$ as a parameter that is present and a row that is absent.

**Confinement, and with it the hadron spectrum.** The potential between a static quark and antiquark grows linearly at long distance with a string tension of about $1\ \mathrm{GeV/fm}$, so the asymptotic states are colour singlets. No order of perturbation theory produces this, and the mechanism is still not derived analytically. What exists is the lattice computation, which reproduces the hadron spectrum to a few per cent.

**The chiral condensate and the $\eta'$ mass.** The axial anomaly, which is exact at one loop, together with instantons, gives the $\eta'$ its large mass — the Witten–Veneziano relation. This is a case where a non-perturbative effect is computed from a perturbative anomaly plus a topological susceptibility.

## The Three Controlled Exceptions

**A corner with no expansion parameter is not automatically a corner with no error bar. There are three ways to get one.**

| Method | What supplies the error | What it costs |
|---|---|---|
| exact by symmetry or topology | none needed: the result is exact | the class of such results is small — anomalies, BPS bounds, index theorems |
| the lattice | the spacing $a$, extrapolated to zero, and the volume | a numerical error that shrinks as $a^2$, and no analytic formula |
| large $N$ | $1/N$, which is $1/3$ for colour | this is [the mean-field corner](mean-field-the-large-n-corner-and-the-fluid-that-comes-out.html) in disguise, with its $30\%$ |

**Everything else is uncontrolled.** A variational ansatz for a soliton gives an energy with no error bar unless one can bound the correction; a strong-coupling expansion gives a series with a finite radius that must be specified; a model of the QCD vacuum gives numbers whose relation to QCD is a hypothesis. The corner's discipline is therefore stricter than the others, not looser: a number computed here must be labelled with which of the three methods produced it.

## Dimensional Transmutation, and the Parameter Count

**This is where the category's central claim is tested most sharply.**

**The classical theory has a dimensionless coupling and no scale.** QCD at the classical level is scale invariant: $g_s$ is a number and there is no mass. The quantum theory is not: the coupling runs, and the running can be integrated to define a scale

$$
\Lambda=\mu\,\exp\!\Bigl(-\frac{2\pi}{b_0\,\alpha_s(\mu)}\Bigr),\qquad b_0=11-\tfrac23 n_f,
$$

which is independent of $\mu$ at one loop. A mass has appeared from a dimensionless number, and this is dimensional transmutation.

**Does that add a nineteenth parameter? No — and the distinction matters.** $\Lambda$ is not free: it is $\alpha_s$ read at a scale, and $\alpha_s$ is already one of the eighteen constants. The count is unchanged. What the corner adds is a *scale*, and a scale is not a parameter: it is the unit in which the parameters are expressed, and it can be changed by changing the renormalisation point.

**The arithmetic shows how little control there is.** At one loop with $n_f=5$ and $\alpha_s(m_Z)=0.118$, the formula gives $\Lambda\approx90\ \mathrm{MeV}$ against the measured $\Lambda_{\overline{\mathrm{MS}}}^{(5)}\approx210\ \mathrm{MeV}$. The factor of $2.4$ is the higher-order ambiguity of a series that is not converging, and it is the honest measure of the corner's precision when no lattice is available.

## What the Corner Cannot Do

**Four refusals, and the second is the one that matters for this section.**

**No Feynman expansion.** There is no diagrammatic series, so the vertex count of fifty-three is meaningless here. A reader who carries [the tally](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html) into this corner has carried an object that does not exist in it.

**No controlled error in general.** The three exceptions above are exceptions. A generic strong-coupling question has no error bar, and the honest answer is "unknown" rather than a number with a guess attached.

**No direct observation of the objects.** No soliton and no instanton has been observed as a particle. Their evidence is indirect: the $\eta'$ mass, the $\theta$ bound, the $\mathrm{U}(1)$ anomaly, the lattice spectrum.

**No derivation of confinement.** The lattice computes it; nobody derives it from the eight lines. This is the largest open problem attached to a corner of this section, and it is a problem about the theory and not about the approximation.

## Where the Corner Is Measured Indirectly

**Three places, and the first is the sharpest.**

**The hadronic vacuum polarisation in the muon $g-2$.** The muon's anomalous moment receives a contribution from a quark loop, which at the relevant momenta is entirely non-perturbative. It is computed either from $e^+e^-$ data or from the lattice, and the two disagree at the few-per-mille level — enough to change the significance of the measured discrepancy. This is the corner entering a precision measurement, and it is the cleanest example of a non-perturbative number being needed by a perturbative calculation.

**The running of $\alpha_s$ at low scales.** The measured $\alpha_s$ at $1\ \mathrm{GeV}$ is only reproduced once the quark thresholds and the higher orders are included, and the low-scale value is a strong-coupling quantity.

**The QCD contributions to $h\to gg$ and $h\to\gamma\gamma$.** The Higgs couplings to two gluons and two photons are loop-induced, and the gluon one is a strong-coupling matrix element over a perturbative coefficient. The measured rates are about $10\%$ and $3\%$ of the total width, and they are reproduced.

## Checks

1. The nature of the corner. No expansion, rather than a limit.
2. The instanton. $S=8\pi^2/g^2$, weight $e^{-2\pi/\alpha_s}\approx e^{-53}$ at $m_Z$.
3. The $\theta$ term. A total derivative that the corner makes physical.
4. Confinement. Linear potential, string tension about $1\ \mathrm{GeV/fm}$, and no derivation.
5. The $\eta'$. Massive through the anomaly plus instantons.
6. The three methods. Symmetry, lattice, large-$N$, and nothing else.
7. Dimensional transmutation. $\Lambda$ from $\alpha_s$, and no new parameter.
8. The arithmetic. One loop gives $90\ \mathrm{MeV}$ against $210\ \mathrm{MeV}$, which is the corner's precision.
9. The refusals. No diagrams, no generic error bar, no observed soliton, no derivation of confinement.
10. The indirect measurements. Hadronic vacuum polarisation, low-scale $\alpha_s$, $h\to gg$.

## Summary

The non-perturbative corner is not a limit but the absence of one. Instanton weights $e^{-2\pi/\alpha_s}$, a $\theta$ angle that stops being a total derivative, confinement with a linear potential, and a chiral condensate are the objects that live there, and none of them has a Taylor series in the coupling.

Error bars exist in exactly three ways: exact by symmetry, controlled by a lattice spacing, or organised by large $N$ with its $1/3$. Everything else is uncontrolled, and the honest label is "unknown".

The corner's structural contribution is dimensional transmutation: a scale emerges from a dimensionless coupling, which changes no parameter count but does introduce a unit. And its sharpest arithmetic — $90\ \mathrm{MeV}$ from one loop against $210\ \mathrm{MeV}$ measured — is the measure of how little the perturbative machinery can say here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| instanton | a finite-action Euclidean solution with unit topological charge |
| $\theta$ | the coefficient of $G\tilde G$; a total derivative that becomes physical here |
| $\Lambda$ | the transmuted scale, a function of $\alpha_s$ and not a new parameter |
| $b_0$ | the one-loop coefficient of the beta function, $11-\tfrac23n_f$ |
| string tension | the slope of the confining potential, about $1\ \mathrm{GeV/fm}$ |

## Further Reading

- [Mean Field: The Large-$N$ Corner](mean-field-the-large-n-corner-and-the-fluid-that-comes-out.html). The third of the controlled methods, and its $1/3$.
- [The Eight Corners in One Table](the-eight-corners-in-one-table.html). Where this corner sits, and why its error bar is missing.
- [What the List Omits](what-the-list-omits-ghosts-the-theta-term-neutrino-mass-and-gravity.html). $\theta$ as a parameter without a row.
- [Instantons and Solitons in Biquaternionic Form](instantons-and-solitons-in-biquaternionic-form.html). The objects, in the corpus's variables.
- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). The four requirements, and what happens when the first cannot be met.
