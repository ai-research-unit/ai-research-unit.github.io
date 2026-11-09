# __Jets, the QCD Cross Section and the Infrared Structure__

## Introduction

**The standing of this article.** Everything below is standard theory, written in the corpus's coordinates and notation. It is **standard input**, not a framework result. Colour is the sharpest boundary in this corpus: by [The Gauge Group Ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html), no compact gauge algebra inside $\mathbb{B}$ has real dimension above four and no $\mathbb{B}$-module has odd complex dimension, so neither $SU(3)$ nor a triplet is available. The strong sector is transcribed, and this article is the one where the transcription has to confront the fact that its own perturbation series is divergent term by term.

**Why this article is different from its neighbours.** The previous three computed quantities that were finite. This one computes quantities whose individual terms are infinite. Every real-emission diagram at order $\alpha_s$ diverges when a gluon is soft or collinear, and every virtual diagram diverges at the same points; only their sum is finite. The article's subject is that cancellation, why it is guaranteed, what it costs, and what happens when it does not happen.

**The claim.** Four statements carry the article.

- **The total cross section is computable and blind.** $R=3\sum_fQ_f^2(1+\alpha_s/\pi+\dots)$ is the cleanest QCD prediction and the bluntest coupling determination, because the correction is only four per cent.
- **A jet is a definition, and the definition is part of the prediction.** Change the resolution and you change the number; a prediction without a stated algorithm is not a prediction.
- **The divergences cancel because the measurement is inclusive.** Bloch–Nordsieck for the soft ones, Kinoshita–Lee–Nauenberg for the collinear ones, and the physical statement behind both is that a hard process is unobservable in isolation: it is always accompanied by an indeterminate number of soft quanta.
- **What survives the cancellation is a logarithm, and the logarithms must be summed.** The leading double log is $\frac{2\alpha_sC_F}{\pi}\ln^2$, it is $0.84$ at a $5$ GeV resolution and passes unity at about $3$ GeV, which is where the cutoffs sit, and the sum of all orders is an exponential — the Sudakov form factor — which is the parton shower.

**The order.** $R$, then jets and why their definition matters, then the three-jet rate, then the two divergences, then their cancellation, then the splitting functions with their sum rules computed, then the double logarithm, then the Sudakov exponent, then the shower, then hadronisation, then the definition of an infrared-safe observable, then the ledger.

## The Total Cross Section and R

**The ratio.** The cleanest strong-interaction observable is a ratio in which the electroweak coupling cancels,

$$
R=\frac{\sigma(e^+e^-\to\text{hadrons})}{\sigma(e^+e^-\to\mu^+\mu^-)}=N_c\sum_fQ_f^2\left[1+\frac{\alpha_s}{\pi}+c_2\left(\frac{\alpha_s}{\pi}\right)^2+\dots\right] ,
$$

with $N_c=3$ from [the QCD article](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html) and the sum over the flavours that are kinematically open.

**The staircase.** The Born-level values are exact rationals, since the charges are:

| Flavour content | $\sum_fQ_f^2$ | $R_0=3\sum_fQ_f^2$ | Threshold |
|---|---|---|---|
| $u$, $d$, $s$ | $2/3$ | $2$ | — |
| $+\,c$ | $10/9$ | $10/3=3.333$ | $2m_c$ |
| $+\,b$ | $11/9$ | $11/3=3.667$ | $2m_b$ |
| $+\,t$ | $5/3$ | $5$ | $2m_t$ |

**What the staircase tests, and what it does not.** Each step is a threshold: as the energy passes twice a quark mass, a new colour triplet switches on and $R$ jumps by $3Q_f^2$. The steps are separate measurements of $N_c$ — the $11/3$ plateau is the one that excludes $N_c=1$ and $N_c=4$ by a wide margin. What the staircase does *not* test is the coupling: the correction is a few per cent, and it does not move the plateaus.

**The corrections, evaluated.** With $\alpha_s$ run from $\alpha_s(M_Z)=0.1179$ by [the running article](asymptotic-freedom-and-the-running-of-the-strong-coupling.html)'s one-loop line, and taking the second coefficient in its $N_f$-dependent form, $c_2=1.4092-0.0781N_f$ — that is $1.097$ at four flavours and $1.019$ at five, not the $1.41$ that is often quoted for the constant term alone:

| $\sqrt s$ | $N_f$ | $\alpha_s$ | $R_0$ | $R$ at order $\alpha_s$ | $R$ at order $\alpha_s^2$ |
|---|---|---|---|---|---|
| $34$ GeV | $4$ | $0.1374$ | $3.333$ | $3.479$ | $3.486$ |
| $34$ GeV | $5$ | $0.1374$ | $3.667$ | $3.827$ | $3.835$ |
| $M_Z$ | $5$ | $0.1179$ | $3.667$ | $3.804$ | $3.810$ |

The measured value on the $b$-inclusive plateau below the $Z$ is about $3.9$, and the third row's $3.81$ is within two and a half per cent of it, against a number that also carries electroweak and radiative corrections of that size. The two $34$ GeV rows are not two measurements: the coupling is not re-run between them, only the flavour content of the sum changes, and that is what isolates the threshold step. The agreement is good; it is not a precision test, and the next paragraph says why.

**Why $R$ is a blunt instrument.** The correction is $\alpha_s/\pi\approx0.04$. A two per cent measurement of $R$ is therefore a two per cent measurement of a four per cent effect, and in coupling units

$$
\delta\alpha_s=\pi\,\frac{\delta R}{R_0}=\pi\times\frac{0.078}{3.667}\approx\pi\times0.021\approx0.067 ,
$$

which is half the value of $\alpha_s$ itself. Inverting the leading formula against $R=3.9$ with $R_0=3.667$ gives $\alpha_s=0.20$, against the $0.14$ that the running demands — a factor of $1.45$ out, from a two per cent discrepancy in $R$. The lesson is not that the formula is wrong; it is that a quantity whose leading correction is four per cent cannot determine a coupling that enters at that order, and that $R$'s role is to count colour and to confirm the size of the correction, not to measure $\alpha_s$ well. The precision determinations use the $Z$ lineshape, which is sensitive at the per-mille level, and event shapes, which are sensitive at the per-cent level through a coefficient larger than one.

## What a Jet Is, and Why the Definition Enters the Prediction

**The physical statement.** A quark does not reach a detector. It fragments into a collimated spray of hadrons, and the spray's direction and energy are the quark's, approximately. A jet is the algorithm that recovers the quark's four-momentum from the spray, and the algorithm is a choice.

**The two families of algorithm, and their difference.**

| Family | Criterion | Consequence |
|---|---|---|
| Cone | The jet is a cone of fixed opening angle containing the deposited energy | Intuitive; the boundary is set by a geometric parameter $R$ |
| Sequential recombination | Particles are combined pairwise in order of a distance measure, until none is close enough | Infrared and collinear safe by construction; the ordering variable is the resolution |

**The distance measure, written once.** In the generalised $k_T$ family,

$$
d_{ij}=\min\left(k_{Ti}^{2p},k_{Tj}^{2p}\right)\frac{\Delta R_{ij}^2}{R^2} ,
\qquad
d_{iB}=k_{Ti}^{2p} ,
$$

with $\Delta R_{ij}^2=\Delta\eta_{ij}^2+\Delta\phi_{ij}^2$. The exponent $p$ selects the algorithm: $p=1$ is $k_T$, $p=0$ is Cambridge–Aachen, $p=-1$ is anti-$k_T$, and the last is the default at the LHC because it produces geometrically regular jets.

**Why the definition is part of the prediction.** The number of jets in an event is not a property of the event. It is a property of the event and the resolution: at a coarse resolution any event is two-jet, at a fine one every event is many-jet. So a cross section "for three jets" is meaningless until the resolution is given, and the resolution is a number that must be stated and, ideally, varied to show that the dependence is under control. This is not a technicality of experimental practice. It is the same statement as [the confinement article's](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) that the parton picture is a description at a resolution, made quantitative.

## The Three-Jet Rate

**Where the third jet comes from.** At order $\alpha_s$ the process $e^+e^-\to q\bar qg$ contributes, and it is the whole of the three-jet rate at that order. The rate is

$$
\frac{\sigma_{3}}{\sigma_0}=\frac{2\alpha_sC_F}{\pi}\ln^2\frac{1}{y}\left[1+O\left(\frac{1}{\ln(1/y)}\right)\right] ,
$$

at leading logarithm in the resolution $y$, with $C_F=\tfrac43$ from the QCD article. The first subleading term inside the bracket is $-\tfrac32\ln(1/y)$, negative and of one power of the log lower; it is shown separately in the table so that no entry is a mixture of two orders.

**The numbers, and where the formula breaks.** With $\alpha_s=0.1179$,

| $y$ | $\ln(1/y)$ | Leading log | Correction | Two-term sum | Status |
|---|---|---|---|---|---|
| $0.20$ | $1.609$ | $0.259$ | $-0.242$ | $0.018$ | Usable |
| $0.10$ | $2.303$ | $0.531$ | $-0.346$ | $0.185$ | Usable, corrections large |
| $0.05$ | $2.996$ | $0.898$ | $-0.450$ | $0.448$ | Marginal |
| $0.02$ | $3.912$ | $1.532$ | $-0.587$ | $0.944$ | **Meaningless: leading log exceeds one** |

The correction column is $-\tfrac32\ln(1/y)$ multiplied by the same prefactor, and the last column is their sum. The last row is the point of the table, and the columns say different things. The leading logarithm alone exceeds one, which is already impossible for a rate. The subleading term is not a small correction — at $y=0.02$ it is $-0.59$ against a leading term of $1.53$ — and it pulls the sum down to $0.94$, still of order one and still far above the measured fraction at that resolution. A series whose second term is forty per cent of its first has not been truncated anywhere useful. So the leading-logarithmic calculation is not merely imprecise at the resolutions of interest; no truncation of it is trustworthy there, and what must be done is to sum the logarithms to all orders. That is the subject of the next five sections, and it is the reason the parton shower exists.

**Why the logarithms are squared.** One logarithm comes from the energy integration over a soft gluon, $\int dE/E$; the other from the angle integration over a collinear emission, $\int d\theta/\theta$. Each runs over a range fixed by the resolution, and the two ranges are independent, so the emission probability is a product of two logs — a double logarithm. The physics is that a gluon is soft *and* collinear at once, and both limits are singular.

## Two Divergences, Named

**Soft.** A gluon emitted with energy $E\to0$ has an amplitude proportional to $1/E$, because the emission is a classical radiation field and the field of a slowly moving charge is the Coulomb field. The squared amplitude is therefore $1/E^2$, and the three-body phase space carries a factor $E$ from $d^3k/2E$, so the rate goes as $dE/E$: one power cancels and the other survives as the logarithm. The integral

$$
\int_0^{E_{\max}}\frac{dE}{E}
$$

is logarithmically divergent at the lower end. The divergence is *not* an artefact of perturbation theory; it is the statement that the number of soft gluons is indeterminate, and any measurement that counts them is ill-defined.

**Collinear.** A gluon emitted at angle $\theta\to0$ to a massless fermion has an amplitude proportional to $1/\theta$, because the emission is coherent over a transverse distance that grows as the angle falls. The rate goes as $d\theta/\theta$, and the integral diverges as $\theta\to0$. The divergence reflects the fact that a massless particle's splitting is degenerate: the two collinear partons have the same direction and the same invariant mass as the parent, so no measurement of four-momenta can tell whether the splitting occurred.

**The one sentence that covers both.** A divergence appears whenever a configuration with $n$ partons is physically indistinguishable from a configuration with $n+1$, because the extra parton is infinitely soft or exactly collinear. The divergence is the volume of the indistinguishable region, and it is infinite because the region is a lower-dimensional surface in a three-dimensional emission phase space.

**Where the masses go, and what that means.** Give the fermion a mass $m$ and the collinear divergence becomes $\ln(Q^2/m^2)$; give the gluon a mass and the soft one becomes $\ln(Q^2/m_g^2)$. In both cases the divergence is regulated by a physical scale and becomes a large logarithm. QCD has no such masses, so the logarithms are large — which is why the strong interaction's perturbation theory is a theory of logarithms rather than of powers.

## Why They Cancel

**Bloch–Nordsieck, for the soft ones.** The total cross section for a process that does not resolve soft quanta is finite, because the emission of a soft quantum of energy below the resolution is indistinguishable from no emission, and the sum over all such emissions — including the virtual correction in which the quantum is emitted and reabsorbed — is finite. The cancellation is between real emission and virtual correction at the same order, and it happens because both are proportional to the same eikonal factor with opposite signs.

**Kinoshita–Lee–Nauenberg, for the collinear ones.** The same statement, formulated for the degenerate configurations: a cross section summed over all final states that are degenerate with a given one is finite, order by order. The degeneracy is the collinear splitting, and the sum is over the unresolved splittings.

**The physical content, stated without the theorem names.** A hard process is never observed in isolation. An electron and a positron that annihilate into a quark pair always produce, in addition, an indeterminate number of soft gluons; the quark pair alone is not a state that any apparatus can prepare. So the quantity that is computable is not "the rate for $q\bar q$" but "the rate for anything that looks like $q\bar q$ at a given resolution", and that quantity is finite because the resolution cuts off the divergence at both ends: the soft ones below the energy resolution, the collinear ones below the angular resolution.

**The consequence for the total cross section.** $\sigma(e^+e^-\to\text{hadrons})$ is fully inclusive, so it is finite — and it is finite for exactly the reason above, not because the individual diagrams are. The order-$\alpha_s$ correction to $R$ is the sum of a real term $\int(1+z^2)/(1-z)$ and a virtual term with the opposite divergence, and the finite remainder is the coefficient that multiplies $\alpha_s/\pi$, which is one. That one is the residue of a cancellation, and a reader who wonders where the correction's coefficient comes from has the answer: it is what is left after two infinities are subtracted. The Born term — the $1$ that stands alone in $1+\alpha_s/\pi$ — is not a residue of anything; it is the tree-level rate, and reading the two as the same number is the commonest way to misread the formula.

**What cancellation does not give.** It does not make the *distribution* finite. The thrust distribution, the jet mass distribution and the energy–energy correlation all have logarithms that survive the cancellation, because the measurement is not inclusive enough to remove them. Those logarithms are the subject of the rest of the article, and the difference between an inclusive and a differential observable is exactly the difference between a cancelled divergence and a summed logarithm.

## The Splitting Functions and Their Sum Rules

**The four kernels.** The collinear limit of QCD is described by four splitting functions, and they are the same objects that drive the evolution of [the parton densities](the-parton-model-and-deep-inelastic-scattering.html):

$$
P_{qq}(z)=C_F\left[\frac{1+z^2}{1-z}\right]_+ ,
\qquad
P_{gq}(z)=C_F\frac{1+(1-z)^2}{z} ,
\qquad
P_{qg}(z)=T_R\left[z^2+(1-z)^2\right] ,
$$

with $P_{gg}$ the gluon's own kernel; $z$ is the fraction of the parent's momentum carried by the emitted parton's sibling. The plus prescription in $P_{qq}$ is on the whole kernel, which is the convention of [the parton-model article](the-parton-model-and-deep-inelastic-scattering.html), where the two ways of writing the subtraction are shown to give identical moments.

**Why they are the same objects.** The splitting function $P_{ba}(z)$ is the probability density for $a\to b$ with momentum fraction $z$, and it appears twice: once in the DGLAP equation, where it describes the evolution of a density with scale, and once in the shower, where it describes the branching of a parton. That the two are the same function is the content of factorisation, and it is why a shower can be built out of measured splitting functions.

**The sum rules, computed.** The integrals below were evaluated with a four-million-point quadrature using the plus prescription as $\int[F]_+h=\int F(z)[h(z)-h(1)]$, which makes each integrand finite.

| Identity | Value | What it says |
|---|---|---|
| $\int_0^1P_{qq}(z)\,dz$ | $0$ (exact) | Quark number is conserved by the splitting |
| $\int_0^1z\,P_{qq}(z)\,dz$ | $-16/9$ | The quark loses momentum to its own radiation |
| $\int_0^1z^2\,P_{qq}(z)\,dz$ | $-25/9$ | The loss is larger for the higher moment |
| $\int_0^1z\,P_{gq}(z)\,dz$ | $+16/9$ | Exactly what the quark lost |
| $\int_0^1P_{qg}(z)\,dz$ | $1/3$ | Two quarks per splitting, weighted by $T_R$ |
| $\int_0^1z\,P_{qg}(z)\,dz$ | $1/6$ | The momentum the gluon hands over |
| $\int_0^1z\left[P_{qq}+P_{gq}\right]dz$ | $0$ (exact; $1.4\times10^{-14}$ on the grid) | **Energy conservation on the quark line** |

The last row is the one to look at. It is the statement that the momentum a quark loses is exactly the momentum a gluon gains, and it is not imposed: it follows from the two kernels. Both moments are exact rationals, $\mp\tfrac{16}{9}$, and what a quadrature returns is its own rounding — here $1.4\times10^{-14}$ on the four-million-point grid. That is much tighter than the $5\times10^{-6}$ the same kind of check reports in [the parton-model article](the-parton-model-and-deep-inelastic-scattering.html), and the difference is the integrand: the plus prescription turns $\int z[P_{qq}+P_{gq}]$ into a quadratic polynomial, which the grid integrates to machine precision, whereas the moment check there keeps a near-singular integrand. A pair of splitting functions that failed this sum rule would describe a splitting that created or destroyed energy, and the check is cheap enough that there is no excuse for not making it.

**Why $\int P_{qq}=0$ is the deepest of them.** It says a quark that radiates is still one quark. In the DGLAP equation it is what keeps the baryon number fixed while the density moves; in the shower it is what makes the branching a redistribution of momentum rather than a creation of partons. And it is where the two ways of writing the kernel are seen to be the same distribution rather than two: with the delta term written explicitly the subtraction is defined differently, and the difference between the two integrals is exactly the delta's coefficient, so the first moment is zero in both and agrees identically. That is why the first moment is a test of a written formula's internal consistency and not a test that discriminates between conventions — the arithmetic that shows it is in [the parton-model article](the-parton-model-and-deep-inelastic-scattering.html), and the conclusion here is the one that follows from it: a first moment that came out nonzero would mean the formula is miswritten, not that the convention is unusual.

## The Eikonal and the Double Logarithm

**The emission probability.** For a soft gluon of energy $E$ emitted at angle $\theta$ from a massless fermion of energy $Q$, the probability is

$$
dw=\frac{\alpha_sC_F}{\pi}\,\frac{dE}{E}\,\frac{d\theta}{\theta} ,
$$

the eikonal, and it is the double-logarithmic kernel. It factorises: the energy and the angle integrals are independent, which is why the logs come in pairs.

**The integration, with its limits stated.** The energy runs from a resolution scale $Q_0$ to $Q$, and the angle from $Q_0/Q$ to $1$ — the lower limit on the angle is not zero but the angle at which the emission's transverse momentum falls below the resolution, and it is precisely this correlation that the naive leading-log treatment ignores. Taking both logs over the same range,

$$
W=\frac{2\alpha_sC_F}{\pi}\ln^2\frac{Q}{Q_0} ,
$$

where the factor two counts the two fermions of the dipole. This is the mean number of emissions above the resolution, and it is the exponent of the no-emission probability.

**The number, and why it matters.** At $Q=M_Z$ with $\alpha_s=0.118$ and $Q_0=5$ GeV, $\ln(91.19/5)=2.903$ and

$$
W=\frac{2\times0.1179\times\frac43}{\pi}\times2.904^2=0.844 .
$$

$W$ is of order one. That is the whole reason the truncation fails: the expansion parameter of the logarithmic series is not $\alpha_s$ but $\alpha_s\ln^2$, and at the scales where the data are taken the second is of order unity while the first is $0.118$.

**What the two logs are, physically.** The energy log says a soft emission is likely; the angle log says a collinear one is likely; and their product says that a *simultaneously* soft and collinear emission is likely with the product of two large numbers. That is why the double logarithm dominates and why the single logarithms, though present, are a correction.

## The Sudakov Form Factor

**The exponentiation.** The probability of no emission above the resolution is the exponential of minus the mean number,

$$
\Delta(Q,Q_0)=\exp\left[-\frac{2\alpha_sC_F}{\pi}\ln^2\frac{Q}{Q_0}\right] ,
$$

the Sudakov form factor. It is not an approximation to a sum; it *is* the sum of the leading double logarithms to all orders, and the reason the sum exponentiates is that independent emissions multiply probabilities.

**The numbers.**

| $Q_0$ | $\ln(Q/Q_0)$ | $W$ | $\Delta$ | $\langle n\rangle=-\ln\Delta$ | $1-\Delta$ |
|---|---|---|---|---|---|
| $3$ GeV | $3.414$ | $1.167$ | $0.311$ | $1.167$ | $0.689$ |
| $5$ GeV | $2.904$ | $0.844$ | $0.430$ | $0.844$ | $0.570$ |
| $10$ GeV | $2.210$ | $0.489$ | $0.613$ | $0.489$ | $0.387$ |
| $20$ GeV | $1.517$ | $0.230$ | $0.794$ | $0.230$ | $0.206$ |
| $40$ GeV | $0.824$ | $0.068$ | $0.934$ | $0.068$ | $0.066$ |

**What the table says.** At a resolution of $5$ GeV, only $43$ per cent of $Z$ events are two-jet; at $20$ GeV, $79$ per cent are. Both numbers are of the order of what is seen, and neither is a prediction of the measured two-jet fraction, because the leading-log exponent is only the first term of the exponent. The table's real content is the trend: the two-jet fraction is not a constant of nature but a function of the resolution, falling as the resolution tightens, and the fall is the exponential of a squared logarithm.

**The improvement that matters.** Replacing one of the two logs by $\ln(Q/\Lambda_{\mathrm{eff}})$, which is what the modified leading-log approximation does, changes the exponent from $0.844$ to $1.779$ at $Q_0=5$ GeV, and the no-emission probability from $0.43$ to $0.17$. The scale here is $\Lambda_{\mathrm{eff}}=0.2$ GeV, $\ln(Q/\Lambda_{\mathrm{eff}})=6.122$, and it is not $\Lambda_5$ of the running article, which is $87$ MeV: the MLLA logarithm absorbs a constant, so its argument carries an effective scale larger than any of the $\Lambda_{N_f}$. That factor of two is the size of the leading correction to the leading logarithm, and it is why a shower that used only the double log would put the two-jet fraction at $0.43$ where the improved exponent gives $0.17$ — a factor of two and a half, from one power of the logarithm. The article states the improved numbers rather than hiding the gap:

| $Q_0$ | $W$ (double log) | $W$ (one log improved) | $\Delta$ (double log) | $\Delta$ (improved) |
|---|---|---|---|---|
| $3$ GeV | $1.167$ | $2.092$ | $0.311$ | $0.123$ |
| $5$ GeV | $0.844$ | $1.779$ | $0.430$ | $0.169$ |
| $10$ GeV | $0.489$ | $1.354$ | $0.613$ | $0.258$ |
| $20$ GeV | $0.230$ | $0.930$ | $0.794$ | $0.395$ |

## The Parton Shower

**What a shower is.** An algorithm that generates, event by event, a sequence of branchings $a\to bc$ with probabilities given by the splitting functions and an ordering variable, terminating when the resolution is reached. It is the numerical evaluation of the resummation, and it is the bridge between a partonic calculation and a hadronic final state.

**The one structure that makes it work.** The no-branching probability between two scales is

$$
\Delta(t_1,t_2)=\exp\left[-\int_{t_2}^{t_1}\frac{dt}{t}\int dz\,\frac{\alpha_s}{2\pi}P(z)\right] ,
$$

and the shower's step is: draw a random number, solve $\Delta(t,t_1)=r$ for the next scale $t$, and if $t$ is above the cutoff, branch. The exponent is the integral of the splitting function, so the shower is the splitting functions plus a random number generator, and nothing else.

**Why the ordering variable is not optional.** A shower must order its emissions in a variable that is monotonic along the branching, or it will double-count. The candidates are the virtuality, the transverse momentum, and the angle; the last is the one that gets the coherence right, because a soft gluon emitted at a large angle cannot resolve the individual partons of a collinear pair. That coherence is the angular ordering, and it is what turns the naive double log into the correct one. It is also where the algebra's own structure is closest to the physics: the coherence is an interference effect between amplitudes, and the interference is the same one that [the photon article](the-photon-in-biquaternionic-form.html) found in the two helicity halves of a null field.

**What the shower does not do.** It does not compute a cross section; it needs the hard process as input. It does not include the interference between emissions at the same order beyond what the ordering allows. It does not hadronise, and it stops at a cutoff where a non-perturbative model takes over. Its accuracy is leading-logarithmic with the coherence built in, and next-to-leading-logarithmic accuracy requires either a matching to a fixed-order calculation or a different formalism.

## Hadronisation and the Size of the Correction

**The non-perturbative part.** Below a cutoff of order $1$ GeV the coupling is of order one, the shower stops, and a model converts partons into hadrons: string fragmentation, cluster fragmentation, or a combination. The model has parameters that are fitted, and its output is a set of hadrons whose momenta are then clustered into jets by the same algorithm as the data.

**The size, in the observable that matters.** For event shapes the hadronisation correction is approximately $0.5$ GeV divided by the hard scale, so

$$
\langle1-T\rangle_{\text{had}}\approx\frac{0.5\ \mathrm{GeV}}{Q} :
\qquad
0.036\text{ at }14\ \mathrm{GeV},\quad
0.015\text{ at }34\ \mathrm{GeV},\quad
0.0055\text{ at }M_Z .
$$

At $M_Z$ the perturbative value is about $0.05$, so the hadronisation correction is roughly ten per cent. At $14$ GeV the perturbative value is not $0.05$ but about $0.07$: the coupling there is $0.167$ against $0.118$, and an event shape scales roughly with $\alpha_s$, so the correction is about half the perturbative value rather than seventy per cent of a fixed one. Holding both numbers fixed while moving the energy would be the wrong comparison, and half is still large enough to matter — which is why low-energy event-shape fits to $\alpha_s$ are unreliable and why the precision determinations are done at the $Z$.

**Why the $1/Q$ scaling is not an accident.** The hadronisation correction scales as a power because it is a non-perturbative mass scale divided by the hard scale — the same dimensional argument that makes a form factor fall as $1/Q^2$. So the correction vanishes in the limit, which is the statement that QCD's predictions become exact at short distances; and it vanishes slowly, as the first power, which is why a ten per cent correction survives at $91$ GeV.

**The honest accounting, and the LEP number.** Fits to LEP event shapes with resummation and hadronisation corrections give $\alpha_s(M_Z)$ around $0.12$, consistent with the $Z$ lineshape value and with the $0.119$ of [the Gross–Llewellyn Smith analysis](the-parton-model-and-deep-inelastic-scattering.html). The consistency of three methods with different systematics — a lineshape ratio, a first moment, and a shape distribution with a fitted non-perturbative correction — is the real evidence that $\alpha_s$ is a parameter of QCD rather than of one analysis.

## Infrared Safety

**The definition.** An observable is *infrared safe* if its value on an $n$-parton configuration equals its value on any $(n+1)$-parton configuration obtained by adding an infinitely soft parton or by splitting one collinearly. Equivalently: the observable must be insensitive to the divergences, so that the KLN cancellation applies to it.

**The test, in the form that gets used.** Compute the observable on a configuration, then on the same configuration with one parton split collinearly, and compare. If the two differ, the observable is not safe, and its perturbative expansion has divergences that do not cancel — which means its coefficients are infinite and the expansion is meaningless, not merely inaccurate.

**What is safe and what is not.**

| Observable | Safe? | Why |
|---|---|---|
| Total cross section | Yes | Fully inclusive |
| Thrust, $C$-parameter, jet broadening | Yes | Defined by momenta, insensitive to splitting |
| Jet rates with a sequential algorithm | Yes | The algorithm is a distance measure that vanishes for collinear pairs |
| Jet rates with a fixed cone and no seedless procedure | Not always | The boundary can depend on a soft parton |
| Number of charged particles | No | A collinear splitting changes the count |
| $b$-tagged jet multiplicity at fixed parton level | No | Flavour is not infrared safe |

**Why the last two rows matter.** The charged multiplicity is the cleanest example: it is a perfectly good measured quantity, and it has no perturbative expansion, because the number of partons is not a perturbative concept. The article states this rather than fitting it, because it is the sharpest available illustration that a computation and a measurement need not live in the same space.

**The lesson for the corpus.** An infrared-safe observable is one whose definition is a functional on the *final state* rather than on the partonic description. That is the same distinction [the confinement article](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) draws between the asymptotic algebra and the partonic labels: the safe observables are those the asymptotic algebra can see, and the unsafe ones are those that refer to labels it does not contain.

## What the Framework Supplies

**Two things, and both are kinematic.**

**The null structure, again.** The eikonal and the collinear factorisation both rest on a light-cone decomposition, and $\mathbb{B}$'s null objects — the nilpotent elements and their exact unipotent exponentials — host that decomposition, as [the parton-model article](the-parton-model-and-deep-inelastic-scattering.html) recorded. The unipotent element is a null rotation and not a boost: it rescales neither null component, so it is the carrier of the light-cone structure and not the dilation that makes $x$ scale invariant. The angular ordering is an interference effect between amplitudes emitted at different angles, and interference is what the algebra's two-sector structure is built to describe. So the algebra hosts the *kinematics of the emission* and the *form of the interference*, and nothing more.

**The limitation, stated plainly.** The divergences are properties of a gauge theory's phase space, and the cancellation is a theorem about that phase space. Neither the phase space nor the theorem is an object of $\mathbb{B}$: the algebra has no $SU(3)$, no triplet, and no measure that would make $\int d^3k/2E$ an algebraic operation. So the whole of this article is transcription.

**The ledger.**

| Item | Status |
|---|---|
| $R=3\sum Q_f^2$ and its staircase | **Imported**, with $N_c=3$ from the QCD article |
| The $\alpha_s/\pi$ and $(\alpha_s/\pi)^2$ corrections | **Imported**; evaluated here |
| Jet algorithms and their distance measures | **Imported**; a definition, not a theorem |
| The three-jet rate at leading log | **Imported**; evaluated here at four resolutions |
| Soft and collinear divergences | **Imported.** Properties of the phase space |
| Bloch–Nordsieck and KLN | **Imported theorems**, not proved |
| $P_{qq}$, $P_{gq}$, $P_{qg}$ | **Imported**; their sum rules **computed** here |
| $\int z[P_{qq}+P_{gq}]dz=0$ | **Computed**: exact as rationals; grid residual $1.4\times10^{-14}$ |
| The eikonal and the double log | **Imported**; the exponent evaluated here |
| The Sudakov form factor | **Imported**; the two tables computed here |
| Angular ordering | **Imported**; it is the coherence the algebra's interference structure resembles |
| Hadronisation models | **Imported**, fitted, non-perturbative |
| Infrared safety | **Imported** definition; the classification is standard |
| The null direction and its unipotent exponential | **Derived in the algebra**; the only row the framework owns |

**What this article does not do.** It does not compute a shower, does not resum beyond the leading double logarithm, does not fit a hadronisation model, and does not prove any of the theorems it uses. It states the divergences, states the cancellation, and computes every number it quotes.

## Summary

The total cross section into hadrons is computable and blind. $R=3\sum_fQ_f^2(1+\alpha_s/\pi+\dots)$ gives the staircase $2$, $10/3$, $11/3$, $5$ at the quark thresholds, and the correction is only $4$ per cent, so a two per cent measurement of $R$ is a two per cent measurement of a four per cent effect — which in coupling units is an uncertainty of $0.067$, half the value of $\alpha_s$. $R$ counts colour and confirms the size of the correction; it does not measure the coupling well.

A jet is a definition. Fixed cones and sequential recombination differ, and sequential algorithms are infrared safe by construction. The three-jet rate at leading log is $\frac{2\alpha_sC_F}{\pi}\ln^2(1/y)$, it is $0.53$ at $y=0.10$ and $1.53$ at $y=0.02$ — and a rate above one is not a rate, which is why the logarithms must be summed rather than truncated.

Two divergences exist, soft ($dE/E$) and collinear ($d\theta/\theta$), and they cancel in any inclusive sum over degenerate states: Bloch–Nordsieck for the soft ones, KLN for the collinear ones. The physical statement is that a hard process is never observed in isolation. The coefficient of $\alpha_s/\pi$ is what is left after two infinities are subtracted, and the logarithms that survive the cancellation are what a differential observable measures.

The splitting functions satisfy sum rules that were computed here: $\int P_{qq}=0$ exactly (quark number), $\int zP_{qq}=-\tfrac{16}{9}$, $\int zP_{gq}=+\tfrac{16}{9}$, $\int P_{qg}=\tfrac13$, and $\int z[P_{qq}+P_{gq}]=0$ exactly — energy conservation on the quark line, which no one imposed, with the grid residual at $1.4\times10^{-14}$.

The double logarithm $\frac{2\alpha_sC_F}{\pi}\ln^2(Q/Q_0)$ is $0.84$ at $M_Z$ with $Q_0=5$ GeV, and its exponential is the Sudakov form factor: the two-jet fraction falls from $0.93$ at a $40$ GeV resolution to $0.43$ at $5$ GeV. Improving one logarithm to $\ln(Q/\Lambda_{\mathrm{eff}})$ moves the exponent from $0.84$ to $1.78$ — a factor of two in the exponent, which is the size of the leading correction. The parton shower is that exponent plus a random number generator, ordered in angle so that the coherence is right, cut off at a scale where a fitted hadronisation model takes over; the hadronisation correction to an event shape is $0.5$ GeV$/Q$, ten per cent at $M_Z$ and about half at $14$ GeV, where the perturbative value itself has grown.

An infrared-safe observable is one whose value does not change under a soft emission or a collinear splitting, and the safe ones are exactly those the asymptotic algebra can see.

The framework supplies the null direction and the form of the interference, and nothing else: it has no $SU(3)$, no triplet, and no phase space on which the theorems would act.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | $\sigma(e^+e^-\to\text{hadrons})/\sigma(e^+e^-\to\mu^+\mu^-)$ |
| $R_0=3\sum_fQ_f^2$ | Born-level value |
| $\sigma_0$ | Born cross section for $e^+e^-\to q\bar q$ |
| $\sigma_3$ | Cross section for three-jet events at resolution $y$ |
| $c_2$ | Second-order coefficient, $1.4092-0.0781N_f$: $1.097$ at $N_f=4$, $1.019$ at $N_f=5$ |
| $y$ | Jet resolution parameter |
| $d_{ij}$, $d_{iB}$ | Pairwise and beam distances in a sequential algorithm |
| $k_T$, $\eta$, $\phi$ | Transverse momentum, pseudorapidity, azimuth |
| $T$ | Thrust; $\langle1-T\rangle$ an event shape |
| $P_{qq},P_{gq},P_{qg},P_{gg}$ | Splitting functions |
| $z$ | Momentum fraction in a splitting |
| $P_{qq}=C_F[(1+z^2)/(1-z)]_+$ | Quark kernel, plus on the whole kernel |
| $W$ | $\frac{2\alpha_sC_F}{\pi}\ln^2(Q/Q_0)$, the double-log exponent |
| $\Delta(Q,Q_0)$ | Sudakov form factor, $e^{-W}$ |
| $Q_0$ | Resolution or cutoff scale |
| $\Lambda_{\mathrm{eff}}$ | Effective scale of the MLLA logarithm, $0.2$ GeV; not $\Lambda_{N_f}$ |
| $C_F=4/3$ | Quadratic Casimir of the triplet; the quark's colour charge |
| $N_c=3$ | Number of colours |
| $N_f$ | Number of flavours kinematically open at the scale |
| $T_R=1/2$ | Normalisation of the gluon-to-quark kernel |
| $\alpha_s$ | Strong coupling; quoted with its scale, as in the running article |

## Further Reading

- [The Parton Model and Deep Inelastic Scattering](the-parton-model-and-deep-inelastic-scattering.html). The splitting functions, their moments, and the convention that fixes their first moment.
- [Asymptotic Freedom and the Running of the Strong Coupling](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). $\alpha_s$ at every scale, and the discipline that every coupling carries a scale.
- [The QCD Lagrangian: Colour, the Triplet, the Octet and the Feynman Rules](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html). $C_F$, $C_A$ and the vertices the real-emission diagrams are built from.
- [Confinement and the Loss of Partonic Information in Biquaternionic Form](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html). Why the parton description is a description at a resolution, and what the asymptotic algebra can and cannot see.
- [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html). The null direction and the interference between the two helicity halves that the angular ordering resembles.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The bound behind every row of the ledger.
- [Lattice Gauge Theory and the Biquaternion Path Integral](lattice-gauge-theory-and-the-biquaternion-path-integral.html). The method that replaces the shower below the cutoff.
