# __The PMNS Matrix and Lepton Mixing__

## Introduction

**The standing of this article.** The mixing matrix itself, its parameterisation and its numbers are standard physics, transcribed. What the corpus contributes is the placement: the matrix is an operator on the generation label, and [the CKM article](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) already built that operator. This article uses the same construction for the leptons and then reports what the numbers do, which is not the same as what the quark numbers do.

**Why leptons are not the quarks again.** The two mixing matrices are the same kind of object and their values have almost nothing in common. The quark angles are small, $13^\circ$, $2.4^\circ$, $0.2^\circ$, and their phase is not small — it is about $66^\circ$ — yet the asymmetry it produces is one part in $10^{5}$ of the mixing, because the asymmetry is the three small angles multiplied together. The lepton angles are large, $33^\circ$, $49^\circ$, $8.6^\circ$, and the CP asymmetry is $850$ times larger. An article that presented the PMNS matrix as "the CKM matrix for leptons" would be describing the formalism and missing the phenomenon: the lepton sector mixes *maximally* where the quark sector mixes *hardly at all*, and nothing in the framework explains why.

**The claim, in four parts.**

- **The matrix is a change of basis, and it is the same operator as CKM.** The weak interaction is generation-universal, the mass operators are not, and the matrix is the relative rotation $U=U_e^{\dagger}U_\nu$. The framework supplies the arena $\mathrm{U}(3)$ and the label on which it acts; it does not supply the point in the arena.
- **Two angles are near maximal and one is not small.** $\theta_{23}=49^\circ$ is $4^\circ$ from maximal, $\theta_{12}=33.4^\circ$ is $12^\circ$ from maximal but only $2^\circ$ from the tribimaximal value, and $\theta_{13}=8.6^\circ$ — the reactor angle — is the one that broke the symmetrical patterns. Its measurement in 2012 is why the tribimaximal ansatz is dead, and why the only pattern that survives is the one that predicted a nonzero reactor angle from a charged-lepton rotation.
- **The CP asymmetry is large because the angles are large.** $J$ is a product of four angle factors — $c_{12}s_{12}$, $c_{13}^2$, $s_{13}$, $c_{23}s_{23}$ — and one sine of the phase. The quark sector has small angles, so $J$ is small whatever the phase does. Here $J=-0.026$ at the fit value, with a ceiling of $\pm0.033$ at maximal CP violation, which is $850$ times the quark value.
- **Two of the six parameters are invisible in oscillation.** Every oscillation probability is built from products $U_{\alpha i}U^{*}_{\beta i}U^{*}_{\alpha j}U_{\beta j}$, in which a column phase appears once and its conjugate once, so the Majorana phases cancel identically — not approximately, and not because oscillation "measures mass-squared differences", but because of the shape of the observable. They are visible only in lepton-number violation, where the amplitude carries $U_{ei}^2$ and the phases add rather than cancel, and that is why neutrinoless double beta decay is the experiment that decides whether the neutrino is its own antiparticle.

**The order.** The matrix and its placement, then the parameterisation and the count six rather than four, then the measured values, then why neutrinos oscillate at all, then the Jarlskog invariant, then what the angles say against the standard patterns, then the mass ordering and the absolute scale, then the Majorana phases, then CP violation and leptogenesis, then the ledger.

## The Matrix and Where It Sits

**The definition.** The charged-current interaction in the mass basis carries

$$
\mathcal{L}_{W}\supset\frac{g}{\sqrt2}W^-_\mu\,\bar e_{L}\gamma^\mu U_{\mathrm{PMNS}}\,\nu_{L}+\text{h.c.},
\qquad
U_{\mathrm{PMNS}}=U_e^{\dagger}U_\nu ,
$$

where $U_e$ and $U_\nu$ are the unitary matrices that diagonalise the charged-lepton and neutrino mass matrices. It is the same construction as CKM's $V=X_u^{\dagger}X_d$, with the neutrino playing the role of the up-type quark.

**The framework's placement.** [The CKM article](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) established that the mixing term factorises into the algebra's own charged-current generator and a $*$-unitary operator $V$ on the flavour factor $\mathcal{F}$; the generator is supplied exactly, the operator is an arbitrary element of $\mathrm{U}(N_g)$, and the only requirement is unitarity, which the norm-preserving group of the multiplicity factor provides. The leptonic case is the same term with the down-type field replaced by the neutrino field. The neutrino field's label structure — including the $L$ label on the charged current and the two values of the chirality — is [the Majorana article's](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) subject.

**Why the framework cannot give the values, stated precisely.** The gauge interactions are the unit on the labels; the mass operators multiply by a number on the label and leave the element alone. A basis change in flavour space therefore cannot be generated by the gauge sector, and it cannot be generated by the algebra either, because the algebra is simple and has one carrier. So $U_{\mathrm{PMNS}}$ is a coordinate on $\mathrm{U}(3)$ with no dynamical principle selecting it inside the framework. The article says this once and does not repeat it as a lament.

## The Parameterisation: Six Numbers, Not Four

**The counting.** A general $3\times3$ unitary matrix has $9$ real parameters. Rephasing the three charged-lepton fields removes three, and rephasing the three neutrino fields removes three more, except that one overall phase is unobservable. So the count is

$$
9-5=4
$$

physical parameters — **if** the neutrinos are Dirac. The $5$, not $6$, is the point. Six field rephasings are available, three on the charged leptons and three on the neutrinos, but the one combination that rephases all six by the *same* phase acts as the identity on $U$ and removes nothing, so five independent rephasings remove five parameters. The usual bookkeeping "$9-3-3+1$" arrives at the same number by subtracting six and adding one back; that is the same arithmetic written so that the compensating phase looks like a repair rather than what it is, the redundancy inside the six.

**What changes when they are Majorana.** A Majorana mass term $\bar\nu^c\nu$ is not invariant under an arbitrary rephasing: only the sign is free. Each neutrino field therefore loses one rephasing, and the count rises by two:

$$
4\ \text{Dirac}\quad\longrightarrow\quad 6\ \text{Majorana}
=
3\ \text{angles}+1\ \text{Dirac phase}+2\ \text{Majorana phases}.
$$

So the number of PMNS parameters depends on the neutrino's nature: six for Majorana, four for Dirac. That is a test only in the sense that a sixth number can exist; it is not a test oscillation can perform, because oscillation is blind to the two extra phases and counts four either way. What could count them is a lepton-number-violating process, and even there the count is indirect — the rate of $\beta\beta_{0\nu}$ is one number depending on both phases, so measuring it constrains the pair without resolving them. The parameter count is exact and the observables are fewer than the parameters.

**The standard form.** In the PDG convention,

$$
U_{\mathrm{PMNS}}=
\begin{pmatrix}
c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\theta_{\mathrm{cpk}}}\
-s_{12}c_{23}-c_{12}s_{23}s_{13}e^{i\theta_{\mathrm{cpk}}} & c_{12}c_{23}-s_{12}s_{23}s_{13}e^{i\theta_{\mathrm{cpk}}} & s_{23}c_{13}\
s_{12}s_{23}-c_{12}c_{23}s_{13}e^{i\theta_{\mathrm{cpk}}} & -c_{12}s_{23}-s_{12}c_{23}s_{13}e^{i\theta_{\mathrm{cpk}}} & c_{23}c_{13}
\end{pmatrix}
\times\mathrm{diag}\!\left(1,e^{i\theta_{\mathrm{mjr},21}/2},e^{i\theta_{\mathrm{mjr},31}/2}\right) .
$$

The three angles are written as $s_{ij}=\sin\theta_{ij}$, $c_{ij}=\cos\theta_{ij}$; the Dirac phase $\delta$ sits in one place and only one; and the two Majorana phases $\theta_{\mathrm{mjr},21}$, $\theta_{\mathrm{mjr},31}$ multiply the second and third columns, real because each is the argument of a unit complex number. The factor $\mathrm{diag}(1,\cdot,\cdot)$ is what makes the last two phases unobservable in oscillation and observable in $\beta\beta_{0\nu}$.

**A convention that matters.** The Majorana-phase normalisation is not universal: some texts write $e^{i\theta_{\mathrm{mjr}}}$ rather than $e^{i\theta_{\mathrm{mjr}}/2}$, which shifts every quoted $\alpha$ by a factor of two. This article uses the half-angle form and says so, and any comparison with a table elsewhere must check which is in use. The same discipline that [the parton-model article](the-parton-model-and-deep-inelastic-scattering.html) imposed on the plus prescription applies here: the convention belongs in the display, not in a footnote.

## The Measured Values

**The angles.**

| Parameter | Best fit | $1\sigma$ range | Maximal value | Comment |
|---|---|---|---|---|
| $\sin^2\theta_{12}$ | $0.303$ | $0.29$–$0.32$ | $0.5$ | Solar; $12^\circ$ from maximal, $2^\circ$ from tribimaximal |
| $\sin^2\theta_{13}$ | $0.0223$ | $0.021$–$0.024$ | $0.5$ | Reactor; the smallest, and the one that killed the patterns |
| $\sin^2\theta_{23}$ | $0.57$ | $0.43$–$0.61$ | $0.5$ | Atmospheric; octant unresolved |
| $\delta_{\mathrm{CP}}$ | $\approx-128^\circ$ | broad, CP conservation disfavoured at $2$–$3\sigma$ | $\pm90^\circ$ | The Dirac phase; $-128^\circ$ is $-2.23$ rad, the normal-ordering fit point |

**The angles in degrees, since degrees are what the comparison needs.**

$$
\theta_{12}=33.4^\circ ,
\qquad
\theta_{13}=8.58^\circ ,
\qquad
\theta_{23}=49.0^\circ .
$$

The atmospheric angle is $4^\circ$ above maximal; the solar angle is $12^\circ$ below maximal. The reactor angle is $8.6^\circ$, which is two thirds of the Cabibbo angle and, crucially, **not zero**.

**The magnitudes of the matrix itself,** which is what oscillation experiments actually constrain:

| | $\nu_1$ | $\nu_2$ | $\nu_3$ |
|---|---|---|---|
| $\nu_e$ | $0.825$ | $0.544$ | $0.149$ |
| $\nu_\mu$ | $0.312$ | $0.588$ | $0.747$ |
| $\nu_\tau$ | $0.470$ | $0.599$ | $0.648$ |

Each row and each column has unit norm to the accuracy of three printed digits, and the check is worth making explicit: the matrix was assembled from the four parameters above and $\max\lvert (UU^{\dagger}-1)_{ij}\rvert$ came out at $2.2\times10^{-16}$, which is one unit of double-precision rounding — the matrix is unitary to machine precision, not to a stated tolerance. A mixing matrix that fails this test has a missing or doubled phase.

**The mass-squared differences, which are the other half of the data.**

| Quantity | Value | What it sets |
|---|---|---|
| $\delta m^2_{21}$ | $7.42\times10^{-5}\ \mathrm{eV}^2$ | The solar oscillation length |
| $\lvert\delta m^2_{31}\rvert$ | $2.51\times10^{-3}\ \mathrm{eV}^2$ | The atmospheric oscillation length |
| Ratio | $33.8$ | Why two very different lengths appear |

The ratio is $33.8$, so the two oscillation lengths differ by a factor of thirty-four and can be separated experimentally. This is the reason a three-neutrino fit is possible at all: were the two differences comparable, no single experiment could separate the two oscillation lengths, and every fit would be degenerate.

## Why Neutrinos Oscillate

**The statement.** A neutrino produced in a flavour eigenstate is a superposition of mass eigenstates. Each mass eigenstate accumulates a phase $e^{-iE_it}$ at its own rate, so the superposition's flavour content changes with distance:

$$
P(\nu_\alpha\to\nu_\beta)=\delta_{\alpha\beta}-4\sum_{i>j}\mathrm{Re}\left(U_{\alpha i}U^{*}_{\beta i}U^{*}_{\alpha j}U_{\beta j}\right)\sin^2\frac{\delta m^2_{ij}L}{4E}
+2\sum_{i>j}\mathrm{Im}\left(\dots\right)\sin\frac{\delta m^2_{ij}L}{2E} .
$$

The $\sin^2$ term is CP-conserving, the $\sin$ term is not, and the coefficient of the latter is the Jarlskog invariant up to signs.

**The oscillation length, and its size.** The phase is

$$
\frac{\delta m^2L}{4E}=1.267\,\frac{\delta m^2[\mathrm{eV}^2]\,L[\mathrm{km}]}{E[\mathrm{GeV}]} ,
$$

and the numbers explain the whole experimental programme:

| Experiment | $L$ | $E$ | $\delta m^2$ | Phase $\delta m^2L/4E$ | Oscillation length |
|---|---|---|---|---|---|
| T2K | $295$ km | $0.6$ GeV | $2.51\times10^{-3}$ | $1.56$ rad $=89.6^\circ$ | $593$ km |
| NOvA | $810$ km | $2$ GeV | $2.51\times10^{-3}$ | $1.29$ rad $=73.8^\circ$ | $1976$ km |
| KamLAND | $180$ km | $3$ MeV | $7.42\times10^{-5}$ | $5.64$ rad | $100$ km |
| Solar | $1.5\times10^{8}$ km | $5$ MeV | $7.42\times10^{-5}$ | $2.8\times10^{6}$ rad | $167$ km |

The last column is one full cycle of the $\sin^2$, $L_{\mathrm{osc}}=\pi E/(1.267\,\delta m^2)=2.48\,E[\mathrm{GeV}]/\delta m^2[\mathrm{eV}^2]$ km, at which the phase advances by $\pi$. Two of its entries are worth reading against the baseline beside them: T2K's $295$ km is half an oscillation length, so its phase is $\pi/2$ and its $\sin^2$ is at the first maximum; KamLAND's $180$ km is $1.8$ oscillation lengths, phase $1.79\pi$, so the reactor experiment sits on the falling side of its second maximum.

**T2K's phase is $89.6^\circ$.** That is not a coincidence: the beamline and the off-axis energy were chosen so that the flux peaks at the first oscillation maximum, where the $\sin^2$ is one and the rate is most sensitive to the parameters. The design of a long-baseline experiment is the choice of $L/E$ such that the phase is $\pi/2$ for the $\delta m^2$ of interest, which is $L=L_{\mathrm{osc}}/2$ — and the T2K numbers sit there to half a per cent, $295$ against $593/2=296.5$. NOvA, at $810$ km and $2$ GeV, sits at $0.41$ of an oscillation length and $73.8^\circ$ — short of the maximum, which is what lets its flux cover both the rise toward the first peak and the fall beyond it, and that shape is what separates the octant and the phase.

**Why the solar case is different.** Its phase is $2.8\times10^{6}$ radians, so the oscillation is averaged out entirely and the survival probability is the average, which depends on $\theta_{12}$ alone. That averaging is what makes the solar measurement a measurement of one angle rather than of a phase. And the matter effect — coherent forward scattering off electrons, which the electron flavour feels and the others do not — makes the high-energy survival tend to the *other* composition:

$$
\bar P_{ee}^{\text{vacuum}}=1-\frac12\sin^2 2\theta_{12}=0.578 ,
\qquad
P_{ee}^{\text{matter}}\to\lvert U_{e2}\rvert^2=0.296 .
$$

Both numbers are measured: roughly $0.55$ for the low-energy $pp$ neutrinos and $0.30$ for the high-energy $^8$B ones. The measured difference between them is a measurement of the matter effect, and the fact that the two limits are $0.58$ and $0.30$ rather than, say, $0.5$ and $0.5$ is a measurement of $\theta_{12}$ being neither maximal nor zero.

**Why oscillation requires mass.** A massless neutrino has no $\delta m^2$ and therefore no phase difference, so the superposition is static. The observation of oscillation is therefore the observation that the neutrino has mass — the only direct evidence — and it does not give the mass itself, only the differences.

## The Jarlskog Invariant

**The invariant.** The rephasing-invariant measure of CP violation is

$$
J=\mathrm{Im}\left(U_{e2}U_{\mu3}U^{*}_{e3}U^{*}_{\mu2}\right)
=c_{12}s_{12}c_{13}^{2}s_{13}c_{23}s_{23}\sin\delta .
$$

Computed from the values above with $\delta=-128^\circ$,

$$
J=-0.0262 ,
$$

and with the phase at its CP-maximal value $\pm90^\circ$,

$$
J_{\max}=\pm0.0332 .
$$

**The range, and the sign.**

| $\delta$ | $J$ | CP violation? |
|---|---|---|
| $0$ | $0$ | None |
| $180^\circ$ | $0$ | None |
| $-90^\circ$ | $-0.0332$ | Maximal |
| $-128^\circ$ | $-0.0262$ | Fit value |
| $+90^\circ$ | $+0.0332$ | Maximal, opposite sign |

The invariant vanishes at both CP-conserving phases and is largest at $\pm90^\circ$, so the measurement of $\delta$ is a measurement of how far from $0$ or $180^\circ$ the phase sits, and the size of the asymmetry is set by the angles.

**The comparison that carries the article.** The quark Jarlskog invariant is $J_{\mathrm{CKM}}=3.08\times10^{-5}$. The ratio is

$$
\frac{\lvert J_{\mathrm{PMNS}}\rvert}{J_{\mathrm{CKM}}}=\frac{0.0262}{3.08\times10^{-5}}=850 .
$$

The lepton sector violates CP eight hundred and fifty times more strongly than the quark sector, at least in the Jarlskog measure. This is the single most important number in the article, because it says that whatever mechanism sets the mixing, it acts completely differently on the two sectors. The corpus has no mechanism, so it has no explanation for the factor $850$, and the honest statement is that the factor is measured and unexplained.

**Why large angles give large $J$.** $J$ is a product of four angle factors — $c_{12}s_{12}$, $c_{13}^2$, $s_{13}$, $c_{23}s_{23}$ — and one sine of the phase. The four are not alike, and the phrase that each is "largest at $45^\circ$ and vanishes at $0$ and $90^\circ$" is true of only two of them. $c_{12}s_{12}$ and $c_{23}s_{23}$ are of the $\sin\theta\cos\theta$ form, largest at $45^\circ$ where they reach $0.5$. $c_{13}^2=1-s_{13}^2$ is largest at $\theta_{13}=0$: it is $0.978$ here and $0.99999$ for quarks, so it suppresses nothing and is a normalisation. $s_{13}$ is a bare sine, monotone, vanishing only at zero — and for small angles it *is* the angle in radians, which is why the gap between $\theta_{13}=8.6^\circ$ and $0.2^\circ$ enters $J$ linearly rather than through a peak at $45^\circ$. For quarks the three are $c_{12}s_{12}=0.219$ — the Cabibbo factor, already at $44\%$ of the $0.5$ ceiling — $s_{13}=0.0037$, and $c_{23}s_{23}=0.0418$, with product $3.38\times10^{-5}$. For leptons they are $0.460$, $0.149$ and $0.495$: two within $8\%$ of the ceiling, one a seventh of its, product $0.0340$, which $c_{13}^2$ brings to the $0.0332$ that multiplies $\sin\delta$. The ratio of the products is $1006$, distributed over the three angles as $2.1\times40\times12$, and each of those three is a measured number with no explanation behind it. Then the phases and the lepton $c_{13}^2$: the quark phase that the quoted $J_{\mathrm{CKM}}$ implies is $\arcsin(3.08\times10^{-5}/3.38\times10^{-5})=66^\circ$, so $\sin128^\circ/\sin66^\circ=0.864$, and $0.864\times0.978\times1006=850$ is the measured ratio.

## What the Angles Say About the Patterns

**The three historical ansätze, and their verdicts.**

| Pattern | $\theta_{12}$ | $\theta_{23}$ | $\theta_{13}$ | Predicted $\sin^2\theta_{12}$ | Verdict |
|---|---|---|---|---|---|
| Bimaximal | $45^\circ$ | $45^\circ$ | $0$ | $0.5$ | Fails: $\theta_{12}$ is $33^\circ$ |
| Tribimaximal | $35.26^\circ$ | $45^\circ$ | $0$ | $0.333$ | Fails: $\theta_{13}\neq0$ |
| Trimaximal (TM1) | $35.26^\circ$ | $45^\circ$ | $\sin^{-1}(\sin\theta_C/\sqrt2)=9.2^\circ$ | $0.333$ | **Survives**: predicts $\theta_{13}\neq0$, within a degree of the measurement |

**What actually survived.** $\theta_{12}=33.41^\circ$ is within $2^\circ$ of the tribimaximal $35.26^\circ$, and $\sin^2\theta_{12}=0.303$ against tribimaximal's $0.333$. So the solar angle is *approximately* tribimaximal. The atmospheric angle is $4^\circ$ from maximal, so it is *approximately* bimaximal. The reactor angle is $8.6^\circ$, which is not approximately zero, and that is the end of the tribimaximal ansatz as an exact statement.

**The 2012 measurement, and why it mattered.** Before 2012, $\theta_{13}$ was bounded only as $\sin^2\theta_{13}<0.04$; the tribimaximal pattern set it to zero by symmetry. Daya Bay, RENO and Double Chooz measured it at $\sin^2\theta_{13}\approx0.022$, a nonzero value at high significance. The consequence is not that the pattern was "slightly broken". A prediction of exactly zero being measured as nonzero is a falsification, and the honest description is that the class of models which set $\theta_{13}=0$ by a discrete symmetry was excluded, not adjusted.

**What replaced it.** One of the three anticipated it, and the table's last row is the record: trimaximal mixing keeps the tribimaximal $\theta_{12}$ and $\theta_{23}$ and lets the charged-lepton Cabibbo rotation generate $\theta_{13}$, which lands at $9.2^\circ$ against the measured $8.6^\circ$. What it does not explain is why the Cabibbo angle should be the source, and it leaves $\theta_{12}$ at $35.26^\circ$ where the measurement is $33.4^\circ$. Beyond that, nothing canonical: the measured pattern is compatible with a class of models in which a discrete group fixes two angles and a small perturbation generates the third, and each has one or two free parameters. The corpus does not adjudicate between them, and the article records the situation rather than the fashion.

**The octant ambiguity.** $\sin^2\theta_{23}=0.57$ admits two solutions, $49.0^\circ$ and $41.0^\circ$, symmetric about maximal mixing. Current data prefer the upper octant weakly, and the distinction matters because a maximal $\theta_{23}$ would be a symmetry statement and a non-maximal one would not. The ambiguity is also correlated with $\delta_{\mathrm{CP}}$, which is why separating them is an experimental programme and not a fit.

## The Mass Ordering and the Absolute Scale

**What oscillation gives and what it does not.** Oscillation gives the magnitudes of the two differences. The sign of $\delta m^2_{21}$ does not stay unknown: the solar matter effect fixes it positive, because only one sign reproduces the observed energy-dependent suppression of the electron flavour, which is why the solar entry above has a definite $\delta m^2_{21}$ and not a modulus. What remains unknown is the sign of $\delta m^2_{31}$ — that is, the ordering — and it is accessible for the same reason, since the matter term adds to the electron flavour's Hamiltonian with a known sign and so shifts the oscillation of neutrinos and antineutrinos differently. The ordering is therefore in principle measurable, and currently unresolved.

**The two orderings, with their numbers.** Taking the lightest mass at zero, which is the minimum allowed:

| Ordering | $m_1$ | $m_2$ | $m_3$ | $\sum m$ | $m_{\beta\beta}$ range |
|---|---|---|---|---|---|
| Normal | $0$ | $8.6$ meV | $50.1$ meV | $59$ meV | $1.4$–$3.7$ meV |
| Inverted | $50.1$ meV | $50.8$ meV | $0$ | $101$ meV | $19$–$49$ meV |

The masses follow from the differences alone once the lightest is fixed, which is why the table has no third independent quantity in it.

**The three frontiers, and what each measures.**

| Probe | Quantity | Current bound | Reaches |
|---|---|---|---|
| Cosmology | $\sum m_i$ | $<0.12$ eV | The ordering, if $\sum m<0.1$ eV |
| Tritium $\beta$ decay (KATRIN) | $m_\beta=\sqrt{\sum\lvert U_{ei}\rvert^2m_i^2}$ | $<0.8$ eV | The absolute scale, if degenerate |
| Neutrinoless $\beta\beta$ | $m_{\beta\beta}=\lvert\sum U_{ei}^2m_i\rvert$ | $<0.03$–$0.16$ eV (isotope dependent) | **Majorana nature**, and the ordering |

**Why the ordering matters to the corpus.** It is the difference between two theories' predictions for a number the framework does not contain. Neither ordering is preferred by any principle in the algebra, and the weak current preference for the normal ordering ($\delta\chi^2\approx2.7$) is a fit result and not a discovery. The article states the preference and states its weakness, because a $2.7$ is not evidence.

**Why the absolute scale is a separate question.** Neutrino oscillation determines differences to a few per cent and the absolute scale not at all. The cosmological bound is now within a factor of two of the normal-ordering sum, so the next generation of surveys will either measure the sum or exclude the inverted ordering, and that is the most consequential near-term test in the sector.

## The Two Majorana Phases

**The statement.** The two extra phases multiply the second and third columns of $U$. Every oscillation probability is a product $U_{\alpha i}U^{*}_{\beta i}U^{*}_{\alpha j}U_{\beta j}$, which is invariant under multiplying column $i$ by a phase and taking the conjugate from column $j$: the phases cancel between a column and its complex conjugate. So **the Majorana phases are invisible in oscillation**, exactly and at every order.

**The check.** Recomputing the matrix with $\theta_{\mathrm{mjr},21}=180^\circ$ and $\theta_{\mathrm{mjr},31}=90^\circ$ changes no magnitude at all — the phases have unit modulus and enter each probability as $e^{i\theta_{\mathrm{pha}}}e^{-i\theta_{\mathrm{pha}}}$, with $\theta_{\mathrm{pha}}$ the real phase of an entry — and leaves the Jarlskog invariant at $-0.0262$ *exactly*, not to a stated number of figures, because $J$ does not involve $\theta_{\mathrm{mjr},21}$ or $\theta_{\mathrm{mjr},31}$: their columns enter it with their conjugates. That is not an approximation; it is a symmetry of the observables, and the arithmetic to confirm it is a multiplication by $1$.

**Where they are visible.** In any amplitude that is not of the form $UU^{\dagger}$, and the canonical one is neutrinoless double beta decay, whose rate is proportional to

$$
\lvert m_{\beta\beta}\rvert=\left\lvert\sum_i U_{ei}^2\,m_i\right\rvert ,
$$

with the squares. The squares do not cancel the column phases; they add them, so the rate depends on $\theta_{\mathrm{mjr},21}$ and $\theta_{\mathrm{mjr},31}$ through interference between the three terms.

**Why the range matters more than the value.** For the normal ordering the three terms nearly cancel whatever the phases do, and $\lvert m_{\beta\beta}\rvert$ lies between $1.4$ and $3.7$ meV — an order of magnitude below any planned experiment. For the inverted ordering the first two terms add coherently and the range is $19$–$49$ meV, within reach. So a positive signal at $20$ meV would say two things at once: the neutrino is Majorana, and the ordering is inverted. A null result at $20$ meV would say the ordering is normal or the neutrino is Dirac, and would not distinguish those.

**The one thing this article will not do.** It will not claim the phases are measured. They are constrained only through $\lvert m_{\beta\beta}\rvert$, which is a single number depending on both, so even a measurement of the rate would not determine two phases. The count of six parameters is exact; the measurement of four of them is good; the measurement of the last two is not yet.

## CP Violation in the Lepton Sector and Leptogenesis

**The asymmetry, in the oscillation channel.** For $\nu_\mu\to\nu_e$ against $\bar\nu_\mu\to\bar e$, the difference is proportional to $J$ times a product of three $\sin$ factors:

$$
\delta P\equiv P(\nu_\mu\to\nu_e)-P(\bar\nu_\mu\to\bar e)=-16J\sin\frac{\delta m^2_{21}L}{4E}\sin\frac{\delta m^2_{31}L}{4E}\sin\frac{\delta m^2_{32}L}{4E} ,
$$

and this is an identity, not a parametrisation: it follows from the interference term above with $\sin(2x)=2\sin x\cos x$ and the three-mass-difference closure $\delta m^2_{31}=\delta m^2_{32}+\delta m^2_{21}$. The argument is $\delta m^2L/(4E)$ in all three factors — the same argument the $\sin^2$ term carries — and writing it as $\delta m^2L/(2E)$ as well would square the wrong function. So the asymmetry requires three nonzero mass differences, three nonzero angles, and a phase. All four conditions hold, and the asymmetry is at the per-cent to per-ten-cent level for a well-chosen baseline. That is why the current generation of long-baseline experiments is designed around it.

**Why the phase is not central, again.** [The CKM article](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) established that a $*$-unitary operator's phase cannot be removed by a central redefinition, so it lives on the flavour factor and not on the algebra. The argument is identical here, and the conclusion is identical: the CP phase is a coordinate of $\mathrm{U}(3)$ and the framework does not fix it.

**The link to baryogenesis.** The observed matter excess requires CP violation, and the Standard Model's quark-sector CP violation is too small by many orders of magnitude. Leptogenesis supplies the missing asymmetry by generating a lepton number excess in the decay of heavy Majorana neutrinos, which the sphaleron then converts partly into baryon number. Two ingredients are needed and both are outside this article's data: a heavy Majorana mass scale, which is [the seesaw article's](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html) subject, and CP violation in the heavy sector's couplings, which need not be the same $\delta$ as the light sector's.

**What the measured $\delta$ does and does not imply.** A large $\delta$ in the light sector is *compatible* with leptogenesis and says nothing about it directly: the light phases and the heavy phases are related through the same matrices but not determined by each other. The article records the compatibility and refuses the inference, because the inference is the one most often made.

## What the Framework Supplies

**One thing, and it is the arena.**

**The arena.** The mixing is a $*$-unitary operator on the flavour factor, so the matrix is an element of $\mathrm{U}(3)$; its four physical parameters are coordinates of the orbit space $\mathrm{U}(3)/\mathrm{U}(1)^{5}$, of dimension $9-5=4$ — the same subtraction as the count above — with three angles playing the role of the $\mathrm{SO}(3)$ directions and one relative phase the role of the coordinate that no rephasing removes. The framework supplies $\mathrm{U}(N_g)$ as the norm-preserving group of the multiplicity factor, and it supplies the label on which the operator acts. What it supplies is therefore the *space of possible mixing matrices*, not the point.

**What it transcribes.** The parameterisation, the measured angles, the mass-squared differences, the Jarlskog invariant and its value, the pattern comparison, the ordering, the $\lvert m_{\beta\beta}\rvert$ ranges, the oscillation formulae and the matter effect. None of these is derived; all are standard, and each is computed here where an arithmetic step exists.

**What it does not supply, declared.**

- No mechanism for the values. The angles are measured, not predicted, and the framework has no flavour dynamics.
- No explanation for the factor $850$ between the two sectors' CP violation.
- No selection of the mass ordering.
- No Majorana mass. The condition and its consequences are [the neutrino article's](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) and [the seesaw article's](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html); the framework hosts the condition and does not generate the scale.
- No leptogenesis. The sphaleron is [the theta-vacuum article's](the-theta-vacuum-in-biquaternionic-form.html) territory, and the sphaleron that would convert it is a saddle point of that structure.

**The ledger.**

| Item | Status |
|---|---|
| $U_{\mathrm{PMNS}}=U_e^{\dagger}U_\nu$ | **Imported** structure; **placed** on the flavour factor by the CKM article |
| The charged-current term with $U$ | **Framework**: the generator is exact, $U$ is a $*$-unitary element |
| $\mathrm{U}(3)$ and its parameter count $4$ or $6$ | **Framework supplies the group**; the count is group theory |
| The three angles and $\delta$ | **Imported** measurements |
| The two Majorana phases | **Imported**; their invisibility in oscillation is exact, since no probability contains them — checked, not measured |
| The $\lvert U\rvert$ matrix | **Computed** here; unitarity checked at $2.2\times10^{-16}$ |
| The oscillation formula and the matter effect | **Imported** |
| The oscillation lengths and phases | **Computed** here for four experiments |
| $J=-0.0262$, $J_{\max}=\pm0.0332$, ratio $850$ | **Computed** here |
| The bimaximal, tribimaximal and trimaximal verdicts | **Imported**; the comparisons and the TM1 relation computed here |
| $\delta m^2_{21}$, $\lvert\delta m^2_{31}\rvert$ | **Imported** |
| The ordering and the mass sums | **Imported**; the sums computed here |
| $m_{\beta\beta}$ ranges | **Computed** here by scanning both phases |
| The Majorana condition, the seesaw | **Framework**, each in its own article |
| A principle fixing the mixing | **Not available** |

**What this article does not do.** It does not fit the parameters, does not simulate an experiment, does not compute a cross section, and does not adjudicate between models of the mixing pattern. It assembles the matrix, checks it, computes every derived number it quotes, and marks the boundary.

## Summary

The PMNS matrix is the lepton analogue of CKM and the same kind of object: a $*$-unitary operator on the generation label, $U=U_e^{\dagger}U_\nu$, placed by the same construction. The framework supplies the arena $\mathrm{U}(3)$, and it does not supply the point.

The parameter count depends on the neutrino's nature: four if Dirac, six if Majorana, the difference being two phases that only a lepton-number-violating process can see. Oscillation cannot tell the two cases apart, so the count is a statement about the matrix and not an observable.

The measured angles are large: $\theta_{12}=33.4^\circ$, $\theta_{13}=8.58^\circ$, $\theta_{23}=49.0^\circ$, with $\delta_{\mathrm{CP}}\approx-128^\circ$ and the CP-conserving values disfavoured at two to three sigma. The magnitudes are $0.825$, $0.544$, $0.149$ in the first row, and the matrix is unitary to $2.2\times10^{-16}$, one rounding unit.

Neutrinos oscillate because the mass eigenstates are not the flavour eigenstates, with phase $1.267\,\delta m^2L/E$. T2K's baseline sits at $89.6^\circ$ by design; the solar phase is $2.8\times10^{6}$ radians and averages to $\bar P_{ee}=0.578$ in vacuum and $0.296$ in matter, and both numbers are measured.

CP violation is $850$ times stronger here than in the quark sector, in the Jarlskog measure: $J=-0.0262$ at the fit phase, $\pm0.0332$ at maximal. The size follows from the angles: $J$ is $c_{12}s_{12}$, $s_{13}$ and $c_{23}s_{23}$ times a normalisation $c_{13}^2$, and the products differ by $1006$ because $s_{13}$ is $40$ times larger here; the angle pattern itself is unexplained.

Two of the historical patterns are dead: bimaximal and tribimaximal both predicted $\theta_{13}=0$, and the 2012 measurement of $\sin^2\theta_{13}=0.022$ falsified them, with $\theta_{12}$ surviving only as approximately tribimaximal. The third anticipated the measurement: trimaximal mixing generates $\theta_{13}=\sin^{-1}(\sin\theta_C/\sqrt2)=9.2^\circ$ from the charged-lepton rotation, within a degree of the value found.

The mass ordering is unresolved, and the lightest-mass-zero table gives sums of $59$ and $101$ meV against a cosmological bound of $120$ meV. The Majorana phases are invisible in oscillation exactly, not to a tolerance, and visible only in $\lvert m_{\beta\beta}\rvert$, whose normal-ordering range of $1.4$–$3.7$ meV is out of reach while the inverted range of $19$–$49$ meV is not, so a signal would say Majorana and inverted at once.

The framework supplies the arena and transcribes the rest: no mechanism for the values, no explanation for the factor $850$, no ordering, no Majorana scale, no leptogenesis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U_{\mathrm{PMNS}}$ | The lepton mixing matrix, $U_e^{\dagger}U_\nu$ |
| $U_e$, $U_\nu$ | Diagonalisations of the charged-lepton and neutrino mass matrices |
| $\theta_{12}$ | Solar angle, $33.4^\circ$ |
| $\theta_{13}$ | Reactor angle, $8.58^\circ$ |
| $\theta_{23}$ | Atmospheric angle, $49.0^\circ$ |
| $\delta$ | Dirac CP phase, $\approx-128^\circ$ ($-2.23$ rad) |
| $\theta_{\mathrm{mjr},21}$, $\theta_{\mathrm{mjr},31}$ | Majorana phases, in the half-angle convention |
| $s_{ij}$, $c_{ij}$ | $\sin\theta_{ij}$, $\cos\theta_{ij}$ |
| $J$ | Jarlskog invariant, $-0.0262$ at the fit phase |
| $\delta m^2_{21}$ | $7.42\times10^{-5}$ eV$^2$ |
| $\delta m^2_{31}$ | $2.51\times10^{-3}$ eV$^2$, magnitude |
| $L$, $E$ | Baseline and energy |
| $L_{\mathrm{osc}}$ | One full cycle of the $\sin^2$, $\pi E/(1.267\delta m^2)$ |
| $\delta m^2_{32}$ | $\delta m^2_{31}-\delta m^2_{21}$, the third argument of the CP asymmetry |
| $\theta_C$ | Cabibbo angle, $13.0^\circ$, used by the trimaximal relation |
| $P_{ee}$ | Electron-neutrino survival probability |
| $\bar P_{ee}$ | The same, averaged over rapid oscillations, as the solar data are |
| $m_{\beta\beta}$ | Effective Majorana mass for $\beta\beta_{0\nu}$ |
| $m_\beta$ | Effective mass in tritium decay |
| $\mathrm{U}(3)$ | The group of $*$-unitary mixing operators |

## Further Reading

- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The same construction for quarks: the operator on the flavour factor, the parameter count, the non-centrality of the phase.
- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html). The field, its two values, the charge conjugation, and the Majorana condition.
- [The Seesaw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html). Where a heavy scale would come from, and what it would do to the light masses.
- [The Majorana Equation in Biquaternionic Form](the-majorana-equation-in-biquaternionic-form.html). The equation whose solutions are their own conjugates.
- [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). The lepton doublet and singlet, and the hypercharge assignment the charged current acts on.
- [The Theta Vacuum in Biquaternionic Form](the-theta-vacuum-in-biquaternionic-form.html). The vacuum angle, and the phase structure a baryon-number-violating saddle point would have to sit in.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The anomaly conditions the lepton and quark content must satisfy, and where a count of free parameters begins.
- [The Parton Model and Deep Inelastic Scattering](the-parton-model-and-deep-inelastic-scattering.html). The convention discipline this article applies to the Majorana-phase normalisation.
