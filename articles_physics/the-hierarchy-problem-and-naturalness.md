# __The Hierarchy Problem and Naturalness__

## Introduction

**The standing of this article.** Standard physics, and one of the two places where the model is widely agreed to be incomplete from the inside. Nothing here is a framework result. The framework's contribution is stated in one section and consists of a *reason for silence*, which is worth having only because it is exact.

**The problem in one sentence.** The Higgs mass is the only dimensionful parameter in the model that is not protected by a symmetry, so every heavy particle that couples to the Higgs shifts its mass by an amount proportional to the heavy particle's mass squared, and the measured value requires those shifts to cancel against the bare parameter to one part in $3.0\times10^{32}$ if the cutoff is the Planck scale.

**Three things this article will not do.**

- It will not present the quadratic divergence as the problem. The divergence is a regulator artefact: in dimensional regularisation the Standard Model has no quadratic divergence in the scalar mass at all, because there is no gauge-invariant dimension-two operator other than the $\mu^2$ term itself. The physical problem is **sensitivity**, not divergence, and the two are different statements. Section *The Divergence Is a Convention* separates them.
- It will not claim the framework has a solution. It does not, and section *What the Algebra Says* gives the exact reason rather than a lament.
- It will not treat naturalness as a theorem. It is a heuristic with one success and at least one conspicuous failure, and section *Naturalness Is Not a Theorem* states both.

**The four results.**

- **The sensitivity is real and it is quadratic.** The one-loop shift is $\delta m_H^2=\frac{\Lambda^2}{16\pi^2}(2.49)$, the coefficient being the sum of a gauge part $0.239$, a top part $1.476$ and a quartic part $0.774$. The top dominates, as it does everywhere in the scalar sector.
- **The tuning is $\Lambda^2$-scaled and the stable window is narrow.** $\Lambda=1$ TeV costs nothing; $\Lambda=10$ TeV costs a factor $10^2$; $\Lambda=M_{\mathrm{Pl}}$ costs $10^{32}$. Radiative stability requires new physics within about $8$ Higgs masses, that is around $1$ TeV.
- **Three standard responses exist, and each has a measured cost.** Supersymmetry needs stops below about $1$ TeV to keep the tuning under $10\%$, and the LHC has not found them. Compositeness needs $f\lesssim1$ TeV for the same, and has not been found either. The landscape needs no new physics and cannot be tested by the same means.
- **The framework's answer is that it has no cutoff, and therefore no quadratic sensitivity, and therefore nothing to say.** That is not a solution; it is a statement that the problem is imported whole. But it comes with one structural observation that is worth the section: a dimensionless algebra cannot generate a dimensionful parameter by itself, which is exactly the statement [the hadron article](hadron-structure-from-qcd-the-bound-state-problem.html) made about $\Lambda_{\mathrm{QCD}}$ — and there, the mechanism exists and is non-perturbative, while here it does not exist at all.

**The order.** The sensitivity, then the divergence convention, then the tuning, then the stability window, then why only the scalar, then the three responses, then the fourth that failed, then what the algebra says, then the status of naturalness, then what a solution would look like, then the ledger.

## The Quadratic Sensitivity

**The one-loop result.** Couple the Higgs to a heavy state of mass $M$ with coupling $c$. The diagram that renormalises the Higgs mass gives

$$
\delta m_H^2=\frac{c}{16\pi^2}\left[\Lambda^2-2M^2\ln\frac{\Lambda}{M}+\dots\right] ,
$$

and the same result is obtained by computing the heavy state's contribution to the vacuum energy and differentiating twice with respect to the Higgs field. The quadratic term is the problem, and the logarithmic term is the part that survives in a cutoff-free scheme.

**The three contributions in the Standard Model, with coefficients.**

| Source | Coupling | Coefficient $c$ | Share |
|---|---|---|---|
| Gauge bosons | $\tfrac94 g^2$ | $0.239$ | $9.6\%$ |
| Top quark | $3y_t^2$ | $1.476$ | $59.3\%$ |
| Higgs quartic | $6\lambda$ | $0.774$ | $31.1\%$ |
| **Total** | — | $2.489$ | $100\%$ |

The coefficients use $g=0.652$, $y_t=m_t/v=172.7/246.22=0.7014$ and $\lambda=0.1291$. The top's contribution is $59\%$ of the total, which is the same fact as in the running of $\lambda$ and in the vacuum stability condition: the top coupling dominates every question about the scalar sector.

**The physical reading, without a cutoff.** Take the Standard Model to be valid up to a scale $\Lambda$ and ask what happens to the Higgs mass when a state of mass $M\sim\Lambda$ is integrated out. The answer is a shift of order $\Lambda^2/16\pi^2$, whatever the regularisation. So the question "why is the Higgs mass so much smaller than the scale of whatever comes next" is a question about **heavy states**, not about infinities.

**The statement in the framework's language, stated early so it is not mistaken for a result.** A mass shift proportional to $\Lambda^2$ is a statement about a *cutoff*, and a cutoff is a property of a regularisation. The algebra has no measure on field space and therefore no cutoff. So the calculation above cannot be performed inside the framework at all. That is not an evasion: it means the framework is a language for the theory below the cutoff, and the problem lives in the relation between that theory and whatever is above it.

## The Divergence Is a Convention; the Sensitivity Is Not

**The distinction, which popular accounts usually lose.** Compute the one-loop scalar mass in dimensional regularisation:

$$
\delta m_H^2=\frac{c}{16\pi^2}M^2\left[\frac{2}{\epsilon}-\gamma+\ln\frac{4\pi\mu^2}{M^2}\right] ,
$$

with **no $\Lambda^2$ term at all**. The reason is structural: the only gauge-invariant operator of dimension two that can renormalise the Higgs mass is $\phi^{\dagger}\phi$ itself, so the divergence must be proportional to $\mu^2$ and not to a cutoff. In a cutoff scheme the quadratic term appears; in dim reg it does not; and the two schemes describe the same physics.

**So what is the problem?** Two things, and neither is the divergence.

- **Sensitivity.** If a heavy particle of mass $M$ couples to the Higgs with coupling $c$, the physical Higgs mass is $m_H^2=m_{H,0}^2+\frac{c}{16\pi^2}M^2+\dots$, and the heavy scale must cancel against the bare parameter. This statement is scheme-independent: it is about the *derivative* of the Higgs mass with respect to a heavy mass, and that derivative is legitimately large.
- **The naturalness criterion.** A theory is natural if $\delta m_H^2\lesssim m_H^2$ for all states that are actually integrated out. This is a criterion on the *spectrum*, not on a divergence.

**Why the distinction matters for this article.** An article that presented the quadratic divergence as the problem would be making a statement that a dim-reg calculation refutes, and the corpus's discipline forbids that. The honest form is: the divergence is a convention, the sensitivity is a fact about heavy states, and the fact is what generates the tuning numbers below.

**The one place the cutoff reappears.** If gravity is included, the Planck scale is a physical cutoff, and the quadratic term becomes physical because Planck-scale states couple to the Higgs with gravitational strength. Then $\Lambda=M_{\mathrm{Pl}}$ is not a convention. This is why the problem is usually stated with the Planck scale rather than with an arbitrary $\Lambda$, and it is the version this article quotes.

**A note on the standard statement's size.** With the total coefficient $2.489$,

$$
\delta m_H^2=\frac{2.489}{16\pi^2}\left(1.22\times10^{19}\right)^2=2.35\times10^{36}\ \mathrm{GeV}^2 ,
$$

against $m_H^2/2=7.82\times10^{3}\ \mathrm{GeV}^2$. The ratio is $3.0\times10^{32}$.

## The Fine Tuning, Stated Exactly

**The definition.** With $\Delta$ the tuning,

$$
\Delta=\frac{\lvert\delta m_H^2\rvert}{m_H^2} ,
\qquad
\text{tuning fraction}=\frac{1}{\Delta} .
$$

**The table, which is the article's central computation.**

| $\Lambda$ | $\Lambda^2$ (GeV$^2$) | $\delta m_H^2$ (GeV$^2$) | $\delta m_H^2/m_H^2$ | $1/\Delta$ |
|---|---|---|---|---|
| $1$ TeV | $1.0\times10^{6}$ | $1.58\times10^{4}$ | $1.01$ | $0.99$ |
| $2$ TeV | $4.0\times10^{6}$ | $6.30\times10^{4}$ | $4.03$ | $0.25$ |
| $5$ TeV | $2.5\times10^{7}$ | $3.94\times10^{5}$ | $25.2$ | $0.040$ |
| $10$ TeV | $1.0\times10^{8}$ | $1.58\times10^{6}$ | $101$ | $9.9\times10^{-3}$ |
| $10^{5}$ GeV | $1.0\times10^{10}$ | $1.58\times10^{8}$ | $1.01\times10^{4}$ | $9.9\times10^{-5}$ |
| $10^{11}$ GeV | $1.0\times10^{22}$ | $1.58\times10^{20}$ | $1.01\times10^{16}$ | $9.9\times10^{-17}$ |
| $M_{\mathrm{Pl}}$ | $1.49\times10^{38}$ | $2.35\times10^{36}$ | $1.50\times10^{32}$ | $6.7\times10^{-33}$ |

**How to read it.** The first row is the statement that new physics at $1$ TeV costs nothing: the shift is the same size as the mass. The fourth row is the statement that new physics at $10$ TeV costs one part in a hundred. The seventh is one part in $3\times10^{32}$.

**What the tuning is not.** It is not a probability. A small $\Delta$ does not mean the value is unlikely; it means that a small change in the input produces a large change in the output, and that a theory which produces $m_H$ from a cancellation is one whose parameters must be tuned. The distinction matters for the landscape discussion below, where the same number is read as a selection effect.

**The comparison with the other fine tuning.** The cosmological constant requires $10^{120}$; this requires $10^{32}$. Both are "fine tunings", and the corpus records them as different problems with different orders of magnitude rather than as one problem, because the mechanisms proposed for the two are not the same.

## The Radiative Stability Criterion

**The question.** At what $\Lambda$ does the shift equal the mass itself?

$$
\frac{2.489}{16\pi^2}\Lambda^2=m_H^2
\quad\Longrightarrow\quad
\Lambda=\sqrt{\frac{16\pi^2}{2.489}}\,m_H=8.0\,m_H=996\ \mathrm{GeV}=4.05\,v .
$$

**The window, and its narrowness.**

| Criterion | $\Lambda$ | Physical statement |
|---|---|---|
| $\delta m_H^2=m_H^2/10$ | $315$ GeV | Uncomfortably close to $m_H$ |
| $\delta m_H^2=m_H^2$ | $996$ GeV | The stability edge |
| $\delta m_H^2=10\,m_H^2$ | $3.15$ TeV | One part in ten tuning |
| $\delta m_H^2=100\,m_H^2$ | $9.96$ TeV | One part in a hundred |

So the statement is: **new physics should be within a factor of four of the weak scale**, and a $10\%$ tuning allows at most a factor of thirteen.

**Why this is the number the LHC was built to test.** The window is above the reach of LEP (which excluded new physics below $100$ GeV by the $Z$ width) and below a few TeV (which the LHC reaches). The LHC found the Higgs and found nothing else. So the natural window is now *closed to the extent that no new state couples to the Higgs above about $1$–$2$ TeV*, and that is the precise form of the hierarchy problem as it stands in 2026.

**What could still be there.** States with small couplings to the Higgs — a hidden sector, a heavy singlet, a state whose coupling is suppressed by a symmetry — shift the mass less than the estimate and are not excluded. This is a real loophole and it is why the problem is stated as a tension rather than a refutation.

## Why Only the Scalar

**The three cases, compared.**

| Field type | Mass term | Protected by | Shift |
|---|---|---|---|
| Fermion | $m\bar\psi\psi$ | Chiral symmetry | $\delta m\propto m\ln\Lambda$ — proportional to the mass |
| Gauge boson | $\tfrac12m^2A_\mu A^\mu$ | Gauge symmetry | Forbidden while massless; protected after breaking |
| Scalar | $m^2\phi^{\dagger}\phi$ | Nothing | $\delta m^2\propto\Lambda^2$ |

**The mechanism of protection, stated once.** A symmetry that forbids the mass term also forbids its radiative correction, because the correction must respect the symmetry of the Lagrangian. Chiral symmetry forbids $m\bar\psi\psi$ for a massless fermion, so the correction must be proportional to the mass — a fermion mass is *technically natural*: setting it to zero is stable under renormalisation. Gauge symmetry forbids $m^2A^2$, so a gauge boson mass is natural in the same sense.

**The scalar has no such protection.** $\phi^{\dagger}\phi$ is a singlet under every symmetry of the Standard Model, so no symmetry forbids it, and no symmetry can forbid its correction. This is the whole content of the hierarchy problem: it is a statement about the absence of a symmetry, and it is exact in that form.

**The framework's reading, which is a real observation and a small one.** The algebra distinguishes the three cases in a way that matches: the fermion mass is a parameter of a chiral pair's mixing, and the mixing is what chiral symmetry forbids; the vector mass is a parameter of the metric structure, and the massless case is the natural one; the scalar mass is a parameter of a potential, and a potential is the one object with no derivational origin in the algebra at all. So the framework exhibits the asymmetry — it does not explain it.

## Response One: Supersymmetry

**The idea.** Pair every Standard Model state with a superpartner of the opposite statistics. The scalar's quadratic shift from a loop of fermions is then cancelled by the loop of the corresponding scalars, because the coupling is the same and the sign is opposite.

**The cancellation, in one line.** For each multiplet,

$$
\delta m_H^2\propto\left(m_B^2-m_F^2\right) ,
$$

so the shift vanishes exactly when supersymmetry is unbroken. Breaking it at scale $M_{\mathrm{SUSY}}$ leaves $\delta m_H^2\sim\frac{c}{16\pi^2}\left(M_{\mathrm{SUSY}}^2-m_{\mathrm{SM}}^2\right)$: the tuning is now a tuning on the *superpartner* masses.

**The numbers, and the two problems.**

| $m_{\tilde t}$ | $\delta m_H^2$ (GeV$^2$) | $\Delta$ | $1/\Delta$ |
|---|---|---|---|
| $500$ GeV | $1.40\times10^{4}$ | $0.89$ | $1.12$ |
| $750$ GeV | $2.72\times10^{4}$ | $1.74$ | $0.58$ |
| $1$ TeV | $4.30\times10^{4}$ | $2.75$ | $0.36$ |
| $2$ TeV | $1.20\times10^{5}$ | $7.69$ | $0.13$ |
| $5$ TeV | $3.24\times10^{5}$ | $20.7$ | $0.048$ |

So a stop below $1$ TeV keeps the tuning under $30\%$, and a stop at $5$ TeV costs a factor of twenty. The LHC's stop searches reach about $1.2$–$1.3$ TeV in favourable topologies and have found nothing, so the natural region is excluded for the simplest models.

**The second problem, which is independent.** In the minimal supersymmetric Standard Model the quartic is fixed by the gauge couplings,

$$
m_h^2=M_Z^2\cos^2 2\beta
\quad\Longrightarrow\quad
m_h\le M_Z=91.2\ \mathrm{GeV}\ \text{at tree level},
$$

against a measured $125.09$ GeV. So the model requires large loop corrections from heavy stops to reach the measured mass, and those corrections are exactly the ones that reintroduce the tuning. The two requirements pull in opposite directions: *raise* $m_h$ needs heavy stops, *naturalness* needs light ones. This tension, not the absence of a discovery by itself, is what has made minimal supersymmetry uncomfortable.

**What survives.** Split supersymmetry, in which the scalars are heavy and the gauginos light, gives up naturalness for the scalar mass and keeps the gauge-coupling unification and the dark matter candidate. It is a coherent position and it concedes the point.

## Response Two: Compositeness and the Pseudo-Goldstone

**The idea.** If the Higgs is not elementary but a bound state of a new strong interaction at scale $f$, then its mass is not a fundamental parameter: it is generated by the strong dynamics, in the same way that the pion mass is generated by the quark masses and the nucleon mass by $\Lambda_{\mathrm{QCD}}$. The quadratic sensitivity is then cut off at $f$, and the Higgs is a light composite because it is a pseudo-Goldstone boson of an approximate symmetry.

**Why pseudo-Goldstone is the load-bearing part.** A generic composite scalar has mass of order $f$, which is too heavy. A Goldstone boson has mass exactly zero, protected by the shift symmetry; breaking the symmetry explicitly and weakly gives a mass suppressed by the breaking, and the Standard Model's $v/f$ plays the role of that suppression:

$$
m_H^2\sim\frac{g_{\mathrm{strong}}^2}{16\pi^2}f^2\times\left(\frac{v}{f}\right)^{2}\quad\text{in the little-Higgs form,}
\qquad
\Delta\sim\left(\frac{f}{v}\right)^{2} .
$$

**The numbers.**

| $f$ | $v/f$ | $\Delta=(f/v)^2$ | $1/\Delta$ |
|---|---|---|---|
| $500$ GeV | $0.492$ | $4.1$ | $0.24$ |
| $800$ GeV | $0.308$ | $10.6$ | $0.095$ |
| $1$ TeV | $0.246$ | $16.5$ | $0.061$ |
| $3$ TeV | $0.082$ | $148$ | $0.007$ |

So $f$ must be within a factor of two of the weak scale for a $10\%$ tuning, and the LHC's exclusion of vector-like quarks and of $W'$-like resonances below about $1.5$–$2$ TeV pushes $f$ up. The same tension as supersymmetry: the natural region is the excluded region.

**The connection to this corpus, stated because it is exact.** Compositeness is precisely the mechanism [the hadron article](hadron-structure-from-qcd-the-bound-state-problem.html) described for the proton: a mass generated by strong dynamics, non-perturbatively, with no dimensionful parameter in the Lagrangian. The difference is that the QCD case has a known dynamics and the electroweak case does not. The framework hosts the QCD mechanism in principle and does not host a second strong sector, which is the subject of the next section.

## Response Three: The Landscape

**The idea.** If the underlying theory has many vacua with different values of the Higgs mass parameter, and if the value is selected by the requirement that structure forms, then the smallness is a selection effect and not a cancellation.

**The argument's form.** Weinberg's original version was for the cosmological constant: a universe with a much larger vacuum energy does not form galaxies, so observers find themselves in a small one. The Higgs version is the same: a much larger $m_H^2$ means a much larger $v$, and a $v$ far above the weak scale gives a universe with no stable nuclei or no atoms.

**What makes it different from the other two.** It predicts no new particles. So it cannot be tested by the LHC, and the three responses are not three candidate theories competing on the same data — two predict new states and one does not. That asymmetry is the reason the field's disagreement is not resolvable by the next collider alone.

**The honest assessment, in three parts.**

- The landscape is **not** excluded. If the string landscape exists, the number $10^{32}$ is not a tuning but a probability, and the corpus has no argument against it.
- The landscape is **not** a solution in the sense the other two are: it does not explain *why* $m_H$ has its value, it explains why we see it.
- The landscape requires the anthropic step, and the anthropic step requires a measure on the space of vacua. The measure is not known, and without it the argument does not make quantitative predictions that could fail.

**Why this belongs in a corpus about an algebra.** Because the framework has no measure either, and for the same reason: a measure requires a space to integrate over, and neither the algebra nor the landscape argument supplies one. Two positions that share a defect are not thereby both right, but the parallel is worth stating: the framework's silence on $m_H$ and the landscape's answer to it come from the same missing object.

## A Fourth That Failed: the Veltman Condition

**The idea.** If the sum of the coefficients of the quadratic divergences vanishes, the quadratic sensitivity cancels among Standard Model states and no new physics is needed.

**The condition and its value.**

$$
\sum_i c_i=0 ,
$$

and from the table above the sum is $2.489$, which is not zero. The condition would be satisfied if the top's contribution were opposite and equal to the rest, which requires

$$
3y_t^2=0.239+0.774=1.013
\quad\Longrightarrow\quad
m_t=143\ \mathrm{GeV},
$$

against a measured $172.7$ GeV. The condition fails by $20\%$ in the mass, that is by $45\%$ in the squared coupling.

**Why the failure is informative rather than embarrassing.** It shows that the quadratic terms do not cancel accidentally in the Standard Model, so there is no hidden mechanism already present. It also shows that the condition is a *fine tuning of a different kind*: it is one equation on the parameters, and it is not satisfied. A framework that wanted to solve the hierarchy problem by a cancellation among Standard Model states would have to explain why this particular combination vanishes, and nothing does.

**The general lesson.** Naturalness conditions are equations, and equations can be checked. The Veltman condition is the cleanest case in the corpus of a naturalness proposal that is *arithmetically* refuted rather than merely unfound, and it is worth keeping for that reason.

## What the Algebra Says

**The answer, in one sentence, then the reason.** It says nothing about the tuning, and the reason it says nothing is exact: the quadratic sensitivity is a statement about a cutoff, a cutoff is a property of a regularisation, the algebra has no measure on field space, and therefore the framework has no cutoff to be sensitive.

**The three parts of that statement, separated.**

- **No measure.** [The gauge-group ceiling article](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) and [the lattice article](lattice-gauge-theory-and-the-biquaternion-path-integral.html) record between them that the path integral over $\mathbb{B}$-valued fields is a formal object, that the fermionic measure is not an algebraic operation, and that a cutoff is imposed from outside. So the framework's loop integrals are not defined and the quadratic term cannot be computed in it.
- **No second strong sector.** Compositeness requires a new confining dynamics at $f\sim1$ TeV. The framework has exactly one strong sector available — the imported $SU(3)$ — and no second one. [The ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) is the reason: no compact gauge algebra of dimension above four, so no second confining group.
- **No vacuum selection.** A landscape requires a space of vacua with a measure. The algebra has one vacuum, the identity of the field algebra, and no family of them.

**The one structural observation that is not silence.** A dimensionless algebra cannot generate a dimensionful parameter by itself. [The hadron article](hadron-structure-from-qcd-the-bound-state-problem.html) established this and then established the resolution: QCD generates $\Lambda_{\mathrm{QCD}}$ non-perturbatively, by dimensional transmutation, with an essential singularity at $\alpha_s=0$. The electroweak sector has the same logical gap and no such mechanism. The Higgs mass is a *parameter*, not an anomaly's matrix element, and no trace anomaly generates it.

**Why the contrast is the article's one real contribution.**

| Sector | Dimensionful quantity | Origin | Framework's role |
|---|---|---|---|
| QCD | $\Lambda_{\mathrm{QCD}}=195$ MeV | Dimensional transmutation, non-perturbative | Hosts the mechanism; cannot compute it |
| Electroweak | $v=246$ GeV | A parameter of a potential, tuned | Hosts the potential; has no mechanism |

The two look like the same problem and are not. QCD's scale *is* generated and the generation is understood in principle. The electroweak scale is *not* generated, and the tuning is the statement that the model provides no generation. That is a sharper statement of the hierarchy problem than "the scalar mass is quadratically divergent", and it is the one the framework's structure makes visible.

## Naturalness Is Not a Theorem

**The status of the criterion.** Naturalness is a heuristic: it asserts that dimensionless ratios should not be much smaller than the loop factors that generate them. It is not a theorem, it is not a symmetry, and it does not follow from any axiom.

**The one clear success.** [The closure article](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html) records it: GIM is a naturalness argument in a different guise. A loop of generation-universal couplings had to cancel, and the cancellation required a fourth quark with a specified coupling pattern. The prediction was right. This is the strongest evidence that the heuristic works.

**The one clear failure.** Supersymmetry at the weak scale was the prediction of the same heuristic applied to the scalar mass. The LHC did not find it. So the heuristic has been right once and wrong once, and the score is $1$–$1$ rather than decisive.

**Two ways it could be wrong in principle.**

- **Selection.** If there are many vacua, a small ratio is not tuned, it is selected. The heuristic then has no force because the ensemble is not the one it assumes.
- **Structure.** The criterion assumes that the parameters are independent inputs. If the underlying theory relates them — if $m_H$ is a function of the same quantity that sets $M_{\mathrm{Pl}}$ — then the ratio is not tuned but computed, and the heuristic is measuring the wrong thing.

**The corpus's position.** Record the tension, state the criterion's status, and do not use naturalness as evidence for or against anything. [The parameter-count article](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html) already established that the framework's defence is geometric rather than numerical; a naturalness argument would be a numerical defence, and the framework cannot mount one.

**Why this section is necessary rather than decorative.** A reader who has been told that the hierarchy problem is "the deepest problem in physics" will read a framework that is silent on it as deficient. The honest answer is that a heuristic is silent because it is a heuristic, and that the corpus's own standard — state the number, state its error, do not narrate — applies to naturalness as much as to a rare-decay anomaly.

## What a Solution Would Look Like

**Three grades, matching the framework the parameter-count article established.**

| Grade | Criterion | Would it settle the problem? |
|---|---|---|
| A mechanism | A symmetry, a dynamics or a selection principle that fixes $m_H/v$ | Yes |
| A relation | $m_H$ computed from another parameter | Yes, if the relation is measured |
| A cancellation | An arithmetic condition satisfied by the spectrum | Only if a reason for it is given |

**The four candidate mechanisms, and their measured status.**

| Mechanism | Predicts | Status |
|---|---|---|
| Supersymmetry | Superpartners below $\sim1$ TeV | Not found; natural region excluded for minimal models |
| Compositeness | Resonances at $f\lesssim1$ TeV | Not found; $f$ pushed above $1.5$–$2$ TeV |
| Extra dimensions | Kaluza–Klein states | Not found |
| Landscape | Nothing | Untestable at colliders |
| Veltman | $m_t=143$ GeV | Refuted, $m_t=172.7$ GeV |

**What the corpus would accept as a solution.** A statement that makes $m_H/v$ a function of quantities already in the nineteen, at the second grade, with a measured consequence. No such statement exists, in the framework or outside it, and the article says so in the same register it uses for the $\varepsilon'/\varepsilon$ tension: this is open, it is not a scandal, and it is not the framework's fault or its merit.

**What would change the picture.** A new state coupled to the Higgs below a few TeV, which would reopen the natural window. Or a demonstration that the landscape measure exists and is calculable, which would close the question in the other direction. Neither is in hand.

## What the Framework Supplies

**One structural contrast and a declared silence.**

**Supplied.** The observation that the electroweak scale and the QCD scale are different *kinds* of problem: the first is generated and the second is not, and the framework's structure makes the distinction visible because it hosts the first mechanism (dimensional transmutation, per [the hadron article](hadron-structure-from-qcd-the-bound-state-problem.html)) and has no counterpart of it for the second. The observation that the scalar is the only field type whose mass term has no symmetry to forbid it, which the algebra's own organisation reproduces without explaining.

**Not supplied, by declaration.** No cutoff, because no measure. No second confining sector, because of the ceiling. No family of vacua, because the algebra has one. No mechanism relating $m_H$ to any other parameter.

**The ledger.**

| Item | Status |
|---|---|
| $\delta m_H^2=\frac{c}{16\pi^2}\Lambda^2$ | **Imported** one-loop result |
| The coefficients $0.239$, $1.476$, $0.774$, sum $2.489$ | **Computed** here |
| The divergence-against-sensitivity distinction | **This article's** argument; the dim-reg statement imported |
| $\delta m_H^2=2.35\times10^{36}$ GeV$^2$ at $M_{\mathrm{Pl}}$ | **Computed** here |
| The tuning table, $10^{32}$ at $M_{\mathrm{Pl}}$ | **Computed** here |
| $\Lambda_{\mathrm{stable}}=996$ GeV $=8.0\,m_H$ | **Computed** here |
| Chiral and gauge protection of fermion and vector masses | **Imported** |
| The MSSM bound $m_h\le M_Z$ | **Imported**; the number $91.2$ GeV quoted |
| The stop-tuning table | **Computed** here |
| The composite tuning $(f/v)^2$ | **Computed** here |
| The landscape argument | **Imported**; its status assessed here |
| The Veltman condition and $m_t=143$ GeV | **Computed** here |
| The QCD-versus-electroweak contrast | **Framework** reading, resting on the hadron article |
| Naturalness as a heuristic, $1$–$1$ | **This article's** assessment |
| A mechanism for $m_H/v$ | **Not available** |

**What this article does not do.** It does not compute a two-loop shift, does not survey supersymmetric models, does not evaluate a landscape measure, and does not propose a solution. It computes the tuning, states the criterion's status, and gives the exact reason for the framework's silence.

## Summary

The Higgs mass is the only dimensionful parameter with no symmetry to protect it. Every heavy state coupled to the Higgs shifts it by $\frac{c}{16\pi^2}\Lambda^2$, with coefficients $0.239$ from gauge bosons, $1.476$ from the top and $0.774$ from the quartic, summing to $2.489$.

The divergence is a convention — dimensional regularisation gives no quadratic term at all — but the sensitivity is not. It is a statement about heavy states, and it produces the tuning: $\Lambda=1$ TeV costs nothing, $10$ TeV costs one part in a hundred, $M_{\mathrm{Pl}}$ costs one part in $3.0\times10^{32}$.

Radiative stability requires new physics within $8.0$ Higgs masses, that is $996$ GeV or $4.05\,v$, and the LHC's null results have closed that window for states with Standard-Model-like couplings.

Fermion and gauge masses are protected because a symmetry forbids the mass term and hence its correction. The scalar has no such symmetry, and that is the whole content of the problem.

Three responses: supersymmetry needs stops below $1$ TeV for $30\%$ tuning, and its tree-level bound $m_h\le91.2$ GeV pulls the other way; compositeness needs $f\lesssim1$ TeV, and its tuning is $(f/v)^2=16.5$ at $f=1$ TeV; the landscape needs no new physics and makes no collider prediction. A fourth, the Veltman condition, is arithmetically refuted: it requires $m_t=143$ GeV against a measured $172.7$.

The framework has no cutoff — no measure — so the quadratic term cannot be computed in it, and it has no second confining sector and no family of vacua. Its one contribution is the contrast between the two scales: $\Lambda_{\mathrm{QCD}}$ is generated non-perturbatively and $v$ is not, and the tuning is the statement that the electroweak sector has no counterpart of the mechanism the strong sector does have.

Naturalness is a heuristic with one success (GIM) and one failure (weak-scale supersymmetry). It is recorded as a heuristic, and the tension is recorded as open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda$ | Cutoff, or the scale of new physics |
| $\delta m_H^2$ | One-loop shift of the Higgs mass squared |
| $c_i$ | Coefficient of the quadratic divergence from source $i$ |
| $\Delta$ | Tuning, $\lvert\delta m_H^2\rvert/m_H^2$ |
| $\lambda$ | Higgs quartic, $0.1291$ |
| $y_t$ | Top Yukawa, $0.7014$ |
| $v$ | Higgs expectation value, $246.22$ GeV |
| $f$ | Compositeness scale |
| $M_{\mathrm{SUSY}}$, $m_{\tilde t}$ | Supersymmetry breaking scale, stop mass |
| $M_{\mathrm{Pl}}$ | Planck mass, $1.22\times10^{19}$ GeV |
| $\Lambda_{\mathrm{QCD}}$ | Strong-interaction scale, $\approx195$ MeV |

## Further Reading

- [Hadron Structure from QCD: the Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html). The other end of the contrast: a scale that *is* generated, non-perturbatively, with no dimensionful parameter in the Lagrangian.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html). The potential whose two parameters carry the tuning.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html). What the framework does represent of the scalar sector, and what it does not.
- [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html). How the scalar mass and any new heavy state enter the fit, and why $T$ is the observable that measures them.
- [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html). Where $v$ and $M_H$ appear as two of the nineteen, both in the group with no arena.
- [Asymptotic Freedom and the Running of the Strong Coupling](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). The running that makes the QCD scale possible, and the contrast the framework's silence on $v$ is measured against.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). Why no second confining sector is available, and hence why compositeness cannot be built here.
- [Meson Mixing, Rare Decays and the Unitarity Triangle as a Closure Test](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html). GIM as the naturalness argument that worked, and the standard for what "worked" means.
- [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html). The top Yukawa that dominates the coefficient.
