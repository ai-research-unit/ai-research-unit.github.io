# __Meson Mixing, Rare Decays and the Unitarity Triangle as a Closure Test__

## Introduction

**The standing of this article.** Standard physics, transcribed. But this is the article where the corpus stops reporting inputs and exhibits a **consistency check**, and that is a different kind of claim from everything in the four articles before it. Lattice QCD reproduces one number; the triangle reproduces a *shape* from three independent measurements that were each made for a different reason.

**What "closure" means here.** Take three quantities measured by three different physical processes: a ratio of semileptonic decay rates, measured in tree-level decays; a ratio of oscillation frequencies, measured in loop-induced mixing; and an angle measured in a decay that involves neither mixing nor loops. Unitarily, they must satisfy a relation. They do, at the degree level. No parameter was adjusted to make them, and no new particle was needed.

**The claim, in four parts.**

- **GIM is unitarity plus non-degeneracy, and that is a statement about the flavour factor.** The box amplitude sums $V_{id}V^{*}_{is}m_i^2$ over the internal quarks. The sum of the $V$ products vanishes because $V$ is unitary; what survives is the failure of the mass operator to be a multiple of the identity on the generation label. Written this way, the mechanism is not a trick about charm: it is the statement that a loop of a generation-universal coupling cancels unless the masses split.
- **The charm prediction was a genuine prediction.** $\delta m_K$ was measured before charm existed. The box formula, read backwards with the GIM mechanism, gave $m_c\approx1.5$ GeV. The $J/\psi$ came in at $3.1$ GeV, and the current mass relevant to the loop is $1.27$ GeV — the hadron mass was never the right number, and the prediction was right anyway.
- **The three mixing systems span fourteen orders of magnitude in $\delta m/m$ and their pattern is diagnostic.** $7.0\times10^{-15}$, $6.3\times10^{-14}$, $2.2\times10^{-12}$. The third is large enough that the $B_s$ oscillates essentially completely before it decays: $\chi_s=0.4993$, against a ceiling of $0.5$.
- **The triangle closes, with one number that does not.** Four of the five measurements land within a per cent of the fit; $\varepsilon'/\varepsilon$ does not, and the article says so rather than presenting a triumph.

**The order.** The two-level system, then the box and GIM, then the charm prediction, then the kaon system, then the two $B$ systems, then the rare decays, then the triangle, then the closure test itself, then what closure does and does not prove, then the ledger.

## The Neutral Meson as a Two-Level System

**The states.** A neutral meson that can turn into its antiparticle — $K^0$–$\bar K^0$, $B^0$–$\bar B^0$, $B_s^0$–$\bar B_s^0$, $D^0$–$\bar D^0$ — is a two-state system described by a non-Hermitian effective Hamiltonian,

$$
i\frac{d}{dt}\begin{pmatrix}\lvert P^0\rangle\ \lvert\bar P^0\rangle\end{pmatrix}
=\left[\begin{pmatrix}M&M_{12}\\M_{12}^{*}&M\end{pmatrix}-\frac{i}{2}\begin{pmatrix}\Gamma&\Gamma_{12}\Gamma_{12}^{*}&\Gamma\end{pmatrix}\right]
\begin{pmatrix}\lvert P^0\rangle\ \lvert\bar P^0\rangle\end{pmatrix},
$$

with $M_{12}$ and $\Gamma_{12}$ the dispersive and absorptive mixing amplitudes. The eigenvalues are

$$
\delta m=m_H-m_L=2\lvert M_{12}\rvert ,
\qquad
\delta\Gamma=\Gamma_H-\Gamma_L=2\lvert\Gamma_{12}\rvert\cos\phi ,
$$

where $\phi=\arg(M_{12}/\Gamma_{12})$. The two parameters that experiments quote are $\delta m$ and the decay-width difference, and the relevant dimensionless ratios are

$$
x=\frac{\delta m}{\Gamma},
\qquad
y=\frac{\delta\Gamma}{2\Gamma} .
$$

**The three systems, with numbers.**

| System | $\delta m$ | $x=\delta m/\Gamma$ | $\delta m/m$ | $\chi$ (wrong-sign fraction) |
|---|---|---|---|---|
| $K^0$ | $5.293\times10^{-3}\ \mathrm{ps}^{-1}$ | $0.474$ | $7.0\times10^{-15}$ | — ($K_S$, $K_L$ have different lifetimes) |
| $B^0_d$ | $0.5065\ \mathrm{ps}^{-1}$ | $0.769$ | $6.3\times10^{-14}$ | $0.1859$ |
| $B^0_s$ | $17.757\ \mathrm{ps}^{-1}$ | $26.8$ | $2.2\times10^{-12}$ | $0.4993$ |

The wrong-sign fraction is

$$
\chi=\frac{x^2}{2(1+x^2)} ,
$$

which is the probability that a meson produced as $P^0$ decays as $\bar P^0$ after the oscillation has been integrated over. Its ceiling is $\tfrac12$, reached when $x\gg1$.

**What the $B_s$ number says.** $\chi_s=0.4993$ against a ceiling of $0.5$: the $B_s$ oscillates so fast that by the time it decays it has, to three decimal places, forgotten which flavour it was born with. This is not a curiosity. It is why $B_s$ mixing is measured as a *frequency* rather than as a counting asymmetry, and why the measurement needs a vertex detector with proper-time resolution far below $1/\delta m_s\approx0.06$ ps.

**Why the mass difference ratio matters more than either mass difference.** The theoretical expression for $\delta m$ carries the hadronic matrix element — a decay constant and a bag parameter — and those are the quantities with the large uncertainties. Their ratio is much better known. Taking the ratio for the two $B$ systems cancels everything except a well-computed SU(3)-breaking factor $\xi$:

$$
\frac{\delta m_{B_s}}{\delta m_{B_d}}
=\frac{m_{B_s}}{m_{B_d}}\,\xi^2\left\lvert\frac{V_{ts}}{V_{td}}\right\rvert^2 ,
\qquad \xi=1.216 .
$$

Measured, the left side is $35.06$; with the mass ratio $1.0165$ and $\xi$, the right side gives

$$
\left\lvert\frac{V_{ts}}{V_{td}}\right\rvert=4.83 .
$$

Since $V_{ts}\approx V_{cb}$ and $V_{td}\approx A\lambda^3 R_t$, this is a measurement of $R_t$ that uses no tree-level decay at all.

## The Box Diagram and the GIM Mechanism

**The amplitude.** $M_{12}$ for a neutral meson comes from a box with two $W$ bosons and two internal quarks:

$$
M_{12}\propto\sum_{i,j}V_{id}V^{*}_{is}V_{jd}V^{*}_{js}\,
S\!\left(\frac{m_i^2}{m_W^2},\frac{m_j^2}{m_W^2}\right),
$$

with $S$ the Inami–Lim function, which grows like $m^2/m_W^2$ for a heavy internal quark and is logarithmically small for a light one.

**GIM, stated as an identity.** Expand $S$ in the degenerate limit. The leading term is a constant, and its coefficient is

$$
\sum_{i,j}V_{id}V^{*}_{is}V_{jd}V^{*}_{js}
=\left(VV^{\dagger}\right)_{ds}\left(VV^{\dagger}\right)_{ds}=0
\quad\text{for }d\neq s .
$$

So the constant cancels exactly, whatever the masses are, and the first surviving term is proportional to the mass splitting:

$$
M_{12}\propto\sum_{i,j}V_{id}V^{*}_{is}V_{jd}V^{*}_{js}\,
\frac{m_i^2-m_j^2}{m_W^2}\times(\text{logarithm}) .
$$

**The framework reading, and it is exact.** $V$ is a change of basis on the generation label — [the CKM article's](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) operator — so $VV^{\dagger}=1$ is not an assumption but the definition of a $*$-unitary change of frame. The vanishing of the constant term is therefore **unitarity**. And the surviving term is proportional to the failure of the mass operator to be a scalar on that label: if $m_i=m_j$ for all $i,j$, the mass operator is a multiple of the identity on $\mathcal{F}$ and the whole loop cancels, exactly and to all orders.

So the GIM mechanism, in the corpus's language, reads:

> A loop of a generation-universal coupling vanishes unless the mass operator fails to be central on the flavour factor.

That is a structural statement about the algebra, not a numerical accident, and it is the one place in this article where the framework contributes something to the physics rather than to the bookkeeping. It also explains why the mechanism needs *two* generations to work and why it becomes a suppression rather than a cancellation with three: with a single generation there is nothing to subtract, and with three the subtraction leaves the splittings of whichever pair dominates.

**Why this is a suppression and not a cancellation.** With $u$, $c$, $t$ in the loop, the constant cancels and what remains is

$$
M_{12}\propto\frac{m_c^2-m_u^2}{m_W^2}\quad\text{for the kaon},
$$

because the top's contribution is absorbed by the unitarity relation into the $(m_t^2-m_c^2)$ term that the kaon's small energy scale cannot resolve. Numerically,

$$
\frac{m_c^2}{m_W^2}=2.50\times10^{-4},
\qquad
\frac{m_t^2}{m_c^2}=1.85\times10^{4},
$$

so the same diagram that gives the kaon its $7\times10^{-15}$ relative splitting gives the $B_s$ its $2\times10^{-12}$: a factor $18{,}500$ from the internal mass alone, softened by the loop function.

## The Charm Prediction

**The situation in 1974.** $\delta m_K$ was measured. The box diagram with only the up quark in the loop gave an answer that diverged quadratically and had no business being finite, let alone correct. Glashow, Iliopoulos and Maiani proposed a fourth quark with a specific coupling pattern, and the constant term cancelled.

**Reading the formula backwards.** What remained was proportional to $(m_c^2-m_u^2)/m_W^2$. Setting the coefficient to the measured $\delta m_K$ gave

$$
m_c\approx1.5\ \mathrm{GeV} .
$$

**What was found, and what the number actually meant.** The $J/\psi$ was discovered at $3.1$ GeV, and the $D$ meson at $1.87$ GeV. Neither is $1.5$ GeV, and both are the wrong kind of number: the mass in the box is the **current** mass of the charm quark, which is $1.27$ GeV, and the hadron masses include the binding energy of a light quark and a gluon cloud. So the prediction was right to about $15\%$ and the two numbers that "disconfirmed" it were not the quantity being predicted.

**Why this is worth recording.** It is the cleanest case in the corpus of a prediction that is easy to mis-state. A reader who compares $1.5$ GeV with $1.87$ GeV concludes the prediction was wrong by $25\%$; a reader who compares with $1.27$ GeV concludes it was right to $18\%$ with the accuracy of a one-loop calculation with an uncomputed hadronic matrix element. The second comparison is the correct one, and the distinction is exactly the one [the hadron-structure article](hadron-structure-from-qcd-the-bound-state-problem.html) drew between current and constituent masses.

**The status today.** The charm loop is now a precision input rather than a prediction: the measured $\delta m_K$ and the lattice-computed matrix element determine a combination of $V_{td}$ and $V_{ts}$ that agrees with the tree-level determination. The prediction has become a test, which is what happens to a successful prediction.

## The Kaon System

**The two eigenstates, and why they are so different.** $K_S$ and $K_L$ differ in mass by $3.5\times10^{-12}$ MeV and in lifetime by a factor of $580$ ($0.0895$ ns against $51.2$ ns). The lifetime difference is not a small perturbation: it comes from the nearly complete cancellation of the $K^0\to\pi\pi$ amplitude by the GIM-suppressed box contribution, so $K_S$ decays to two pions and $K_L$ cannot (it is CP-forbidden) and must go to three.

**The three CP observables.**

| Observable | Value | What it measures |
|---|---|---|
| $\lvert\varepsilon_K\rvert$ | $2.228\times10^{-3}$ | CP violation in mixing: the mass eigenstates are not CP eigenstates |
| $\mathrm{Re}(\varepsilon'/\varepsilon)$ | $1.66\times10^{-3}$ | CP violation in the decay amplitude itself |
| $\delta m_K$ | $5.293\times10^{-3}\ \mathrm{ps}^{-1}$ | The mixing, and hence $\lvert V_{td}V_{ts}\rvert$ through the box |

**The ratio of the two, and what it says.** $\mathrm{Re}(\varepsilon'/\varepsilon)/\lvert\varepsilon_K\rvert=0.745$. Both are nonzero, so CP is violated both in mixing and in the decay amplitude — which is the statement that the phase of $V$ enters twice, once through the mixing and once through the penguin amplitude's interference with the tree.

**The number that does not close.** $\varepsilon'/\varepsilon$ is the one measurement in the triangle programme that does not agree with its lattice prediction. The measured $1.66\times10^{-3}$ sits well above the $1.4\times10^{-4}$ that the current lattice calculation gives for the Standard Model, a difference of a factor of twelve and about two standard deviations once the (large) hadronic uncertainty is included. The article records this as a live tension rather than a confirmed conflict, and records the reason for caution: the prediction depends on the cancellation of two penguin contractions, and a quantity that is the difference of two large numbers is the last place to trust a first lattice calculation.

**Why $\varepsilon_K$ is the one that measures $\eta$.** At leading order in the Wolfenstein parameters,

$$
\lvert\varepsilon_K\rvert\propto B_K\, f_K^2\, m_K\, \frac{m_t^2}{m_W^2}\,\eta\left(1-\rho\right)\times(\text{short-distance function}),
$$

so $\varepsilon_K$ is proportional to the **altitude of the triangle**. Its measurement is what first established that $\eta>0$, that is, that the triangle is not flat on the axis and CP is genuinely violated. Numerically $\lvert\varepsilon_K\rvert/\eta=6.3\times10^{-3}$, a constant of proportionality that absorbs $B_K$, $f_K$ and the short-distance function.

## The Two $B$ Systems

**What the numbers are, and what sets them.** The three systems' splittings differ by the internal quark mass squared and by the meson decay constant squared:

| System | Internal quarks | $f_P^2 B_P$ | $\delta m$ |
|---|---|---|---|
| $K^0$ | $u,c,t$ (charm dominates) | $f_K^2B_K$ | $5.3\times10^{-3}$ ps$^{-1}$ |
| $B^0_d$ | $t$ dominates | $f_{B_d}^2B_{B_d}$ | $0.507$ ps$^{-1}$ |
| $B^0_s$ | $t$ dominates | $f_{B_s}^2B_{B_s}$ | $17.76$ ps$^{-1}$ |

Read down the table: the kaon's small splitting is charm's, the $B$'s large splittings are the top's, and the ratio between the two $B$ systems is almost purely the SU(3) breaking of the decay constant, because both are top-dominated and the CKM factors $V_{tb}V_{td}$ and $V_{tb}V_{ts}$ differ by the known ratio $V_{td}/V_{ts}$.

**Why the $B_d$ measurement determines a side of the triangle and the kaon does not.** $\delta m_{B_d}\propto\lvert V_{td}\rvert^2$, and $\lvert V_{td}\rvert$ is the distance from the triangle's apex to the vertex at $(1,0)$ — the side $R_t$, in units of $A\lambda^3$. The kaon's $\delta m$ is dominated by the charm contribution, which carries no $\eta$ dependence at leading order, so it constrains a different combination. Hence: the kaon measures the height, the $B_d$ measures the right side.

**The $B_s$ and the width difference.** $\delta\Gamma_s/\Gamma_s\approx0.12$ is measured, and it is the largest width difference of any neutral meson system. It matters because the two mass eigenstates have different CP content, so a decay into a CP eigenstate can be used to tag the flavour at production — the "same-side" or "opposite-side" tagging that makes $\delta m_s$ measurable at all.

## Rare Decays

**Why loops are the interesting place.** A decay that is forbidden at tree level in the Standard Model and allowed at one loop is sensitive to anything that couples to the loop's internal particles. The two canonical cases are $b\to s\gamma$ and $B_s\to\mu\mu$.

**$b\to s\gamma$.**

| Quantity | Value |
|---|---|
| Measured $\mathcal{B}(B\to X_s\gamma)$ at $E_\gamma>1.6$ GeV | $(3.32\pm0.15)\times10^{-4}$ |
| Standard Model | $(3.36\pm0.23)\times10^{-4}$ |
| Ratio | $0.988$ |

The agreement to $1\%$ is not a null result. The prediction requires the $W$–$t$ loop, the QCD corrections to two loops, and the $b$-quark mass; a factor-of-two error in any of them would show. The measurement constrains the Wilson coefficients $C_7$ and $C_8$ to a few per cent, and that is the tightest constraint on new physics in the dipole operators.

**$B_s\to\mu\mu$.**

| Quantity | Value |
|---|---|
| Measured $\mathcal{B}(B_s\to\mu\mu)$ | $(3.34\pm0.27)\times10^{-9}$ |
| Standard Model | $(3.66\pm0.14)\times10^{-9}$ |
| Ratio | $0.913$ |

The ratio is $0.91$, which is $1.4$ standard deviations below the prediction. Worth one sentence and no more: a $1.4\sigma$ is not evidence, and the quantity is helicity-suppressed by $m_\mu^2/m_{B_s}^2$ and therefore intrinsically small, so the experimental error dominates the comparison.

**The anomalies that dissolved.** Between 2014 and 2021 the $b\to s\ell\ell$ angular observables and the lepton-universality ratios $R_K$ and $R_{K^*}$ showed a coherent pattern of deviations from the Standard Model, of a size that suggested a new vector coupling. The 2022 LHCb reanalysis, with a revised treatment of the charmed-hadron backgrounds, moved $R_K$ and $R_{K^*}$ onto the Standard Model prediction. The pattern is gone.

**What the dissolution teaches, and this article's use of it.** A closure test is only as good as its inputs, and a coherent pattern of $3\sigma$ deviations is not a discovery. The corpus records the episode because it is the strongest available argument for the discipline the articles have followed: state the number, state its error, and do not narrate the anomaly until it survives an independent dataset.

## The Unitarity Triangle

**The construction.** Unitarity of the CKM matrix gives nine relations among its entries. The most useful is the $b$–$d$ relation,

$$
V_{ud}V^{*}_{ub}+V_{cd}V^{*}_{cb}+V_{td}V^{*}_{tb}=0 ,
$$

which is a sum of three complex numbers equal to zero — three vectors that close, hence a triangle. Dividing by the middle term puts two vertices at $(0,0)$ and $(1,0)$ and the third at $(\bar\rho,\bar\eta)$:

$$
\bar\rho+i\bar\eta=-\frac{V_{ud}V^{*}_{ub}}{V_{cd}V^{*}_{cb}} .
$$

**The parameters.**

| Quantity | Value | Definition |
|---|---|---|
| $\lambda$ | $0.22650$ | $\lvert V_{us}\rvert$, the base of the triangle |
| $A$ | $0.826$ | $\lvert V_{cb}\rvert/\lambda^2$ |
| $\bar\rho$ | $0.1591$ | Real coordinate of the apex |
| $\bar\eta$ | $0.3523$ | Imaginary coordinate; the CP-violating height |
| $R_b$ | $0.3866$ | $\sqrt{\bar\rho^2+\bar\eta^2}$ |
| $R_t$ | $0.9117$ | $\sqrt{(1-\bar\rho)^2+\bar\eta^2}$ |

**The three angles.**

$$
\alpha=91.6^\circ ,
\qquad
\beta=22.7^\circ ,
\qquad
\gamma=65.7^\circ ,
\qquad
\alpha+\beta+\gamma=180.0^\circ .
$$

The sum is $180$ by construction — the triangle is drawn in a plane — so the sum alone is not a test. What is a test is that three *independent* measurements of the three angles give values consistent with one triangle.

**The area.** Heron's formula on the three sides gives $0.1762$, and $\bar\eta/2$ gives $0.1762$. The area is the CP violation: a flat triangle ($\bar\eta=0$) has no area and no CP violation, and the Jarlskog invariant is proportional to it,

$$
J=A^2\lambda^6\,\bar\eta\,(1-\bar\rho)=2.73\times10^{-5}
\quad\text{(leading order)} ,
$$

against $J=2.91\times10^{-5}$ computed exactly from the angles and $J=3.08\times10^{-5}$ from the global fit. The three agree at the few-per-cent level, the spread being the truncation of the Wolfenstein expansion.

## The Closure Test

**The five measurements, and what each uses.**

| Quantity | Measured by | Physics used | Value | Uncertainty |
|---|---|---|---|---|
| $R_b$ | $\lvert V_{ub}\rvert/\lambda\lvert V_{cb}\rvert$ | Tree-level semileptonic decays | $0.386$ | $3\%$ |
| $R_t$ | $\delta m_{B_d}/\delta m_{B_s}$ | Loop-level box diagrams | $0.911$ | $1.3\%$ |
| $\beta$ | $\sin2\beta$ in $B\to J/\psi K_S$ | Tree decay with mixing | $22.2^\circ$ | $0.7^\circ$ |
| $\gamma$ | $B\to DK$ | Pure tree, no mixing | $65.9^\circ$ | $3.5^\circ$ |
| $\alpha$ | $B\to\pi\pi,\rho\rho,\rho\pi$ | Isospin analysis of trees | $91.9^\circ$ | $1.5^\circ$ |

**Four different kinds of physics.** $R_b$ is a ratio of two tree-level rates, so it is as clean as a hadronic quantity gets. $R_t$ is a ratio of two loop-induced frequencies, so it depends on the top mass, on the box function and on a lattice matrix element — and the ratio cancels most of the last. $\gamma$ comes from interference between $b\to c\bar us$ and $b\to u\bar cs$, both trees, so it is sensitive to no loop at all and is the Standard Model's cleanest angle. $\beta$ comes from a decay that requires mixing to occur, so it is a loop quantity dressed as a tree measurement. $\alpha$ is extracted from three channels by isospin, and is the least clean of the three.

**The closure, in three equations.**

$$
R_t^2=1+R_b^2-2R_b\cos\gamma
\quad\Longrightarrow\quad
0.9117=0.9117 ,
$$

which is the law of cosines and it holds to four decimal places because both sides use the same $(\bar\rho,\bar\eta)$. That is a consistency check of the arithmetic, not of the physics. The physical test is the next two:

$$
R_t\ \text{from}\ \frac{\delta m_{B_s}}{\delta m_{B_d}}=0.914
\quad\text{against}\quad
R_t=0.9117\ \text{from the fit} ,
$$

a difference of $0.3\%$, and

$$
\sin2\beta=0.7128\ \text{from the fit}
\quad\text{against}\quad
0.699\pm0.017\ \text{measured} ,
$$

a difference of $0.8$ standard deviations. Neither difference is zero, and both are within the stated errors. That is what closure looks like: not exact agreement, but agreement at the accuracy of the inputs, with no parameter adjusted to produce it.

**The comparison with the alternative.** A four-generation model, or a model with a $Z'$ coupling to $b$ quarks, would move one or more of these five numbers. The closure is therefore a constraint: it excludes any new physics that would shift $R_t$ or $\gamma$ by more than a per cent while leaving the others alone.

## What Closure Does and Does Not Prove

**What it proves.** That the CKM picture is *self-consistent*: three angles and two sides, measured by five different experimental techniques spanning tree and loop physics, satisfy the unitarity relations of a $3\times3$ unitary matrix. That is a strong statement, because unitarity is a property of the group and not of any dynamical assumption, so the test has no adjustable content.

**What it does not prove.** It does not prove that the CKM matrix is the *origin* of CP violation rather than a description of it. It does not exclude new physics that respects the same unitarity relations — a heavy particle that couples in a flavour-universal way, or one whose contributions cancel in the five observables. And it does not explain the pattern: the values $\lambda=0.2265$, $A=0.826$, $\bar\rho=0.159$, $\bar\eta=0.352$ are measured, and the corpus has no principle that selects them.

**The distinction the corpus insists on.** There is a difference between "the model is consistent with all data" and "the model is the correct description". The closure test establishes the first. The second would require the model to be *unique* among consistent descriptions, and it is not, as the persistence of the flavour puzzle shows.

**What would break it.** A sixth measurement of the same triangle by a different route, disagreeing at more than $3\sigma$:

| Candidate | Currently | Would test |
|---|---|---|
| $\gamma$ from Belle II | $3.5^\circ$ | The one angle with no loop dependence |
| $B_K$ from lattice at $1\%$ | $\sim3\%$ | The height, hence $\eta$, independently of $B$ decays |
| $\xi$ from lattice at $1\%$ | $\sim2\%$ | $R_t$ without the SU(3)-breaking assumption |
| $\delta m_s$ at $0.1\%$ | $0.6\%$ | The top loop directly |
| $\varepsilon'/\varepsilon$ | factor $12$ from lattice | The penguin sector, and currently the outlier |

None of the first four is available yet, and the closure is therefore a check with four significant figures and no fifth. The last row is the one entry already in the table that does not close.

## What the Framework Supplies

**Two structural statements, and neither is a number.**

**GIM is a statement about the flavour factor.** As above: $VV^{\dagger}=1$ is the definition of a change of basis on the generation label, so the constant term in the loop vanishes by unitarity, and the surviving term measures the non-centrality of the mass operator. This is a genuine framework-level reading. It supplies no value, but it supplies the *reason* the mechanism has the form it has, and it explains in one sentence why one generation gives nothing and three give a suppression.

**The triangle is a statement about $\mathrm{U}(3)$.** The three-vector sum closing is the unitarity of the mixing group, and the area being CP violation is the statement that a $*$-unitary operator with one phase cannot be made real by rephasing. [The CKM article](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) derived both. What the framework supplies is therefore the *necessity* of a triangle, not its shape.

**What it transcribes.** Everything numerical: the box functions, the Inami–Lim results, the hadronic matrix elements, the measured frequencies, the rare-decay branching ratios, the five closure inputs and their errors.

**What it does not supply, declared.** No loop calculation. No measure on the space of field configurations over which a loop integral is defined. No lattice. No hadronic matrix element. No mechanism for the values of $\lambda$, $A$, $\bar\rho$, $\bar\eta$. No explanation of why there are three generations. Each of these is an import, and the articles that own them are named in the ledger.

**The ledger.**

| Item | Status |
|---|---|
| $K^0$–$\bar K^0$, $B^0$–$\bar B^0$, $B_s$–$\bar B_s$ as two-level systems | **Imported** formalism; the two-level structure representable in the spinor module |
| $\delta m=2\lvert M_{12}\rvert$, $x=\delta m/\Gamma$, $\chi=x^2/2(1+x^2)$ | **Imported**; recomputed here for three systems |
| The box diagram and the Inami–Lim functions | **Imported** |
| GIM as unitarity plus non-centrality of the mass operator | **Framework reading** of an imported mechanism |
| $m_c\approx1.5$ GeV from $\delta m_K$ | **Imported** history; the current-mass comparison computed here |
| $\lvert\varepsilon_K\rvert=2.228\times10^{-3}$, $\varepsilon'/\varepsilon=1.66\times10^{-3}$ | **Imported** |
| $\delta m_{B_d}$, $\delta m_{B_s}$, the ratio $35.06$ | **Imported**; $\lvert V_{ts}/V_{td}\rvert$ and $R_t$ computed here |
| $\mathcal{B}(B\to X_s\gamma)$, $\mathcal{B}(B_s\to\mu\mu)$ | **Imported**; the ratios computed here |
| $\lambda$, $A$, $\bar\rho$, $\bar\eta$ | **Imported** global fit |
| $R_b$, $R_t$, $\alpha$, $\beta$, $\gamma$, the area | **Computed** here from the fit |
| The law-of-cosines identity and the two closure pulls | **Computed** here |
| $J=2.73\times10^{-5}$ (leading), $2.91\times10^{-5}$ (angles), $3.08\times10^{-5}$ (fit) | **Computed** here, three routes |
| $\mathrm{U}(3)$ and the necessity of a closed triangle | **Framework**, per the CKM article |
| Loop integrals, lattice matrix elements, the values of the four Wolfenstein parameters | **Not available** |

**What this article does not do.** It does not compute a box diagram, a Wilson coefficient or a hadronic matrix element. It assembles the numbers, checks the arithmetic through the law of cosines, compares the two independent $R_t$ determinations and the one $\beta$ determination, and marks the boundary. The closure it reports is a closure of *numbers*, not of derivations.

## Summary

The neutral mesons are two-level systems with $\delta m=2\lvert M_{12}\rvert$. The three splittings are $5.29\times10^{-3}$, $0.507$ and $17.76$ ps$^{-1}$, giving $x=0.474$, $0.769$ and $26.8$ and wrong-sign fractions up to $\chi_s=0.4993$ against a ceiling of $0.5$ — the $B_s$ forgets its flavour before it decays.

GIM is unitarity plus non-degeneracy. The constant term in the box cancels because $VV^{\dagger}=1$, and what survives is proportional to the mass splitting: $(m_c/m_W)^2=2.50\times10^{-4}$ for the kaon, $(m_t/m_c)^2=1.85\times10^{4}$ between the charm and top loops. Read backwards against $\delta m_K$ in 1974, this gave $m_c\approx1.5$ GeV; the current mass is $1.27$ GeV, and the $D$ meson's $1.87$ GeV was never the right quantity to compare with.

The triangle has sides $R_b=0.3866$, $R_t=0.9117$, base $1$, and angles $91.6^\circ$, $22.7^\circ$, $65.7^\circ$. Its area is $0.1762$ by Heron and $0.1762$ by $\bar\eta/2$. $R_t$ from the $B$ mixing ratio is $0.914$ against $0.9117$ from the fit — $0.3\%$; $\sin2\beta$ from the fit is $0.7128$ against $0.699\pm0.017$ measured — $0.8\sigma$. Both close.

The rare decays agree: $b\to s\gamma$ at $0.988$ of prediction, $B_s\to\mu\mu$ at $0.913$. The one number that does not close is $\varepsilon'/\varepsilon$, measured at $1.66\times10^{-3}$ against a lattice value near $1.4\times10^{-4}$, and it is recorded as a live tension rather than a conflict.

Closure proves self-consistency, not uniqueness, and it does not explain the four Wolfenstein parameters. The framework supplies two structural statements — GIM as non-centrality of the mass operator on the flavour factor, and the closed triangle as the unitarity of $\mathrm{U}(3)$ — and imports every number in the article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_{12}$, $\Gamma_{12}$ | Dispersive and absorptive mixing amplitudes |
| $\delta m$, $\delta\Gamma$ | Mass and width differences of the two eigenstates |
| $x$, $y$ | $\delta m/\Gamma$ and $\delta\Gamma/(2\Gamma)$ |
| $\chi$ | Time-integrated wrong-sign fraction, $x^2/2(1+x^2)$ |
| $K_S$, $K_L$ | The two kaon mass eigenstates |
| $\varepsilon_K$ | CP violation in kaon mixing, $2.228\times10^{-3}$ |
| $\varepsilon'/\varepsilon$ | Direct CP violation in the decay amplitude |
| $B_K$ | The kaon bag parameter |
| $\xi$ | SU(3)-breaking ratio of $B$-meson decay constants, $1.216$ |
| $\lambda$, $A$, $\bar\rho$, $\bar\eta$ | Wolfenstein parameters |
| $R_b$, $R_t$ | The two non-trivial sides of the unitarity triangle |
| $\alpha$, $\beta$, $\gamma$ | The three angles |
| $J$ | Jarlskog invariant, $2.9\times10^{-5}$ |
| $\mathcal{B}$ | Branching ratio |
| $C_7$, $C_8$ | Dipole Wilson coefficients |

## Further Reading

- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The operator, the parameter count, the Jarlskog invariant and the non-centrality of the phase — the source of both structural statements this article uses.
- [The PMNS Matrix and Lepton Mixing](the-pmns-matrix-and-lepton-mixing.html). The same mixing structure in the lepton sector, where the angles are large and the CP violation is $850$ times stronger.
- [Hadron Structure from QCD: the Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html). Current against constituent masses, which is the distinction the charm prediction turns on.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). Why the loop integral is an import and not an algebraic operation.
- [Lattice Gauge Theory and the Biquaternion Path Integral](lattice-gauge-theory-and-the-biquaternion-path-integral.html). Where the hadronic matrix elements that appear in $\delta m$ actually come from.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The consistency conditions the fermion content must satisfy, which a fourth generation would break.
- [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). The flavour structure the CKM matrix acts on, and the coupling that makes the loop generation-universal.
- [The Theta Vacuum in Biquaternionic Form](the-theta-vacuum-in-biquaternionic-form.html). The other CP-violating parameter of QCD, and why its smallness is a separate question from the triangle's area.
