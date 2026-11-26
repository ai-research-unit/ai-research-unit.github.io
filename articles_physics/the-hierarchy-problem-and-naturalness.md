# __The Hierarchy Problem and Naturalness__

## Introduction

This is standard physics, and one of the two places where the model is widely agreed to be incomplete from the inside. Nothing here is a framework result. The framework's contribution is stated in one section and consists of a *reason for silence*, which is worth having only because it is exact.

The Higgs mass is the only dimensionful parameter in the model that is not protected by a symmetry, so every heavy particle that couples to the Higgs shifts its mass by an amount proportional to the heavy particle's mass squared, and the measured value requires those shifts to cancel against the bare parameter to one part in $3.0\times10^{32}$ if the cutoff is the Planck scale.

Three claims are refused at the outset.

- The quadratic divergence is not the problem. The divergence is a regulator artefact: in dimensional regularisation the Standard Model has no quadratic divergence in the scalar mass at all, because there is no invariant dimension-two operator other than the $\mu^2$ term itself. The physical problem is sensitivity, not divergence, and the two are different statements. Section *The Divergence Is a Convention* separates them.
- The framework has no solution. It does not, and section *What the Algebra Says* gives the exact reason.
- Naturalness is not a theorem. It is a heuristic with one success and at least one conspicuous failure, and section *Naturalness Is Not a Theorem* states both.

**Units.** A mass in this article is written in kilograms. A cutoff, a compositeness scale and a running scale stay in joules: those are energies, and the joule is their unit.

Four claims are then established, each with a number.

- The sensitivity is real and it is quadratic. The one-loop shift is $\delta m_H^2=\frac{\Lambda^2}{16\pi^2}(2.49)$, the coefficient being the sum of a representative part $0.239$, a top part $1.476$ and a quartic part $0.774$. The top dominates, as it does everywhere in the scalar sector.
- The tuning is $\Lambda^2$-scaled and the stable window is narrow. $\Lambda=1.6\times10^{-7}\ \mathrm{J}$ costs nothing; $\Lambda=1.6\times10^{-6}\ \mathrm{J}$ costs a factor $10^2$; $\Lambda=M_{\mathrm{Pl}}$ costs $10^{32}$. Radiative stability requires new physics within about $8$ Higgs masses, that is around $1.6\times10^{-7}\ \mathrm{J}$.
- Three standard responses exist, and each has a measured cost. Supersymmetry needs stops below about $1.6\times10^{-7}\ \mathrm{J}$ to keep the tuning under $10\%$, and the LHC has not found them. Compositeness needs $f\lesssim1.6\times10^{-7}\ \mathrm{J}$ for the same, and has not been found either. The landscape needs no new physics and cannot be tested by the same means.
- The framework's answer is that it has no cutoff, and therefore no quadratic sensitivity, and therefore nothing to say. That is not a solution; it is a statement that the problem is imported whole. But it comes with one structural observation that is worth the section: a dimensionless algebra cannot generate a dimensionful parameter by itself, which is exactly the statement [the hadron article](hadron-structure-from-qcd-the-bound-state-problem.html) made about $\Lambda_{\mathrm{QCD}}$ — and there, the mechanism exists and is non-perturbative, while here it does not exist at all.

## The Quadratic Sensitivity

Couple the Higgs to a heavy state of mass $M$ with coupling $c$. The diagram that renormalises the Higgs mass gives

$$
\delta m_H^2=\frac{c}{16\pi^2}\left[\Lambda^2-2M^2\ln\frac{\Lambda}{M}+\dots\right] ,
$$

and the same result is obtained by computing the heavy state's contribution to the vacuum energy and differentiating twice with respect to the Higgs field. The quadratic term is the problem, and the logarithmic term is the part that survives in a cutoff-free scheme.

The Standard Model contributes through three sources.

| Source | Coupling | Coefficient $c$ | Share |
|---|---|---|---|
| Connections | $\tfrac94 g^2$ | $0.239$ | $9.6\%$ |
| Top quark | $3y_t^2$ | $1.476$ | $59.3\%$ |
| Higgs quartic | $6\varpi_{\mathrm{cpl}}$ | $0.774$ | $31.1\%$ |
| Total | — | $2.489$ | $100\%$ |

The coefficients use $g=0.652$, $y_t=m_t/v=3.079\times10^{-25}/4.3893\times10^{-25}=0.7014$ and $\varpi_{\mathrm{cpl}}=0.1291$. The top's contribution is $59\%$ of the total, which is the same fact as in the running of $\varpi_{\mathrm{cpl}}$ and in the vacuum stability condition: the top coupling dominates every question about the scalar sector.

The physical interpretation needs no cutoff. Take the Standard Model to be valid up to a scale $\Lambda$ and ask what happens to the Higgs mass when a state of mass $M\sim\Lambda$ is integrated out. The answer is a shift of order $\Lambda^2/16\pi^2$, whatever the regularisation. So the question "why is the Higgs mass so much smaller than the scale of whatever comes next" is a question about heavy states, not about infinities.

In the framework's language, a mass shift proportional to $\Lambda^2$ is a statement about a *cutoff*, and a cutoff is a property of a regularisation. The algebra has no measure on field space and therefore no cutoff. So the calculation above cannot be performed inside the framework at all. That is not an evasion: it means the framework is a language for the theory below the cutoff, and the problem lives in the relation between that theory and whatever is above it.

## The Divergence Is a Convention; the Sensitivity Is Not

Compute the one-loop scalar mass in dimensional regularisation:

$$
\delta m_H^2=\frac{c}{16\pi^2}M^2\left[\frac{2}{\epsilon}-\gamma+\ln\frac{4\pi\mu^2}{M^2}\right] ,
$$

with no $\Lambda^2$ term at all. The reason is structural: the only invariant operator of dimension two that can renormalise the Higgs mass is $\xi_{\mathrm{pot}}^{\dagger}\xi_{\mathrm{pot}}$ itself, so the divergence must be proportional to $\mu^2$ and not to a cutoff. In a cutoff scheme the quadratic term appears; in dim reg it does not; and the two schemes describe the same physics.

So what is the problem? Two things, and neither is the divergence.

- Sensitivity. If a heavy particle of mass $M$ couples to the Higgs with coupling $c$, the physical Higgs mass is $m_H^2=m_{H,0}^2+\frac{c}{16\pi^2}M^2+\dots$, and the heavy scale must cancel against the bare parameter. This statement is scheme-independent: it is about the *derivative* of the Higgs mass with respect to a heavy mass, and that derivative is legitimately large.
- The naturalness criterion. A theory is natural if $\delta m_H^2\lesssim m_H^2$ for all states that are actually integrated out. This is a criterion on the *spectrum*, not on a divergence.

The distinction matters here because the divergent form of the problem is refuted by a dim-reg calculation. The divergence is a convention, the sensitivity is a fact about heavy states, and that fact generates the tuning numbers below.

The cutoff reappears in one place. If gravity is included, the Planck scale is a physical cutoff, and the quadratic term becomes physical because Planck-scale states couple to the Higgs with gravitational strength. Then $\Lambda=M_{\mathrm{Pl}}$ is not a convention. This is why the problem is usually stated with the Planck scale rather than with an arbitrary $\Lambda$, and it is the version this article quotes.

With the total coefficient $2.489$,

$$
\delta m_H^2=\frac{2.489}{16\pi^2}\left(1.22\times10^{19}\right)^2=6.03\times10^{16}\ \mathrm{J^{2}} ,
$$

against $m_H^2/2=2.01\times10^{-16}\ \mathrm{J^{2}}$. The ratio is $3.0\times10^{32}$.

## The Fine Tuning, Stated Exactly

The tuning is defined by

$$
\mathcal{T}_{\mathrm{tune}}=\frac{\lvert\delta m_H^2\rvert}{m_H^2} ,
\qquad
\text{tuning fraction}=\frac{1}{\mathcal{T}_{\mathrm{tune}}} .
$$

The tuning scales with $\Lambda^2$.

| $\Lambda$ | $\Lambda^2$ (J$^2$) | $\delta m_H^2$ (J$^2$) | $\delta m_H^2/m_H^2$ | $1/\mathcal{T}_{\mathrm{tune}}$ |
|---|---|---|---|---|
| $1.6\times10^{-7}$ J | $2.57\times10^{-14}$ | $4.06\times10^{-16}$ | $1.01$ | $0.99$ |
| $3.2\times10^{-7}$ J | $1.03\times10^{-13}$ | $1.62\times10^{-15}$ | $4.03$ | $0.25$ |
| $8.0\times10^{-7}$ J | $6.42\times10^{-13}$ | $1.01\times10^{-14}$ | $25.2$ | $0.040$ |
| $1.6\times10^{-6}$ J | $2.57\times10^{-12}$ | $4.06\times10^{-14}$ | $101$ | $9.9\times10^{-3}$ |
| $1.6\times10^{-5}$ J | $2.57\times10^{-10}$ | $4.06\times10^{-12}$ | $1.01\times10^{4}$ | $9.9\times10^{-5}$ |
| $1.6\times10^{1}$ J | $2.57\times10^{2}$ | $4.06\times10^{0}$ | $1.01\times10^{16}$ | $9.9\times10^{-17}$ |
| $M_{\mathrm{Pl}}$ | $3.83\times10^{18}$ | $6.03\times10^{16}$ | $1.50\times10^{32}$ | $6.7\times10^{-33}$ |

The first row is the statement that new physics at $1.6\times10^{-7}\ \mathrm{J}$ costs nothing: the shift is the same size as the mass. The fourth row is the statement that new physics at $1.6\times10^{-6}\ \mathrm{J}$ costs one part in a hundred. The seventh is one part in $3\times10^{32}$.

The tuning is not a probability. A small $\mathcal{T}_{\mathrm{tune}}$ does not mean the value is unlikely; it means that a small change in the input produces a large change in the output, and that a theory which produces $m_H$ from a cancellation is one whose parameters must be tuned. The distinction matters for the landscape discussion below, where the same number is read as a selection effect.

The comparison with the cosmological constant takes one line: it requires $10^{120}$, where this requires $10^{32}$. Both are "fine tunings", and the two are recorded as different problems with different orders of magnitude rather than as one problem, because the mechanisms proposed for them are not the same.

## The Radiative Stability Criterion

At what $\Lambda$ does the shift equal the mass itself?

$$
\frac{2.489}{16\pi^2}\Lambda^2=m_H^2
\quad\Longrightarrow\quad
\Lambda=\sqrt{\frac{16\pi^2}{2.489}}\,m_H=8.0\,m_H=1.60\times10^{-7}\ \mathrm{J}=4.05\,v .
$$

The window is narrow.

| Criterion | $\Lambda$ | Physical statement |
|---|---|---|
| $\delta m_H^2=m_H^2/10$ | $5.05\times10^{-8}\ \mathrm{J}$ | Uncomfortably close to $m_H$ |
| $\delta m_H^2=m_H^2$ | $1.60\times10^{-7}\ \mathrm{J}$ | The stability edge |
| $\delta m_H^2=10\,m_H^2$ | $5.05\times10^{-7}\ \mathrm{J}$ | One part in ten tuning |
| $\delta m_H^2=100\,m_H^2$ | $1.60\times10^{-6}\ \mathrm{J}$ | One part in a hundred |

So the statement is: new physics should be within a factor of four of the weak scale, and a $10\%$ tuning allows at most a factor of thirteen.

The window is above the reach of LEP (which excluded new physics below $1.60\times10^{-8}\ \mathrm{J}$ by the $Z$ width) and below a few $10^{-6}$ J (which the LHC reaches). The LHC found the Higgs and found nothing else. The natural window is now closed, in the sense that no new state couples to the Higgs above about $1$–$3.2\times10^{-7}\ \mathrm{J}$, and that is the precise form of the hierarchy problem as it stands in 2026.

Something could still be there. States with small couplings to the Higgs — a hidden sector, a heavy singlet, a state whose coupling is suppressed by a symmetry — shift the mass less than the estimate and are not excluded. This is a real loophole and it is why the problem is stated as a tension rather than a refutation.

## Why Only the Scalar

Three field types, compared.

| Field type | Mass term | Protected by | Shift |
|---|---|---|---|
| Fermion | $m\barΞ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}$ | Chiral symmetry | $\delta m\propto m\ln\Lambda$ — proportional to the mass |
| Connection | $\tfrac12m^2\sum_{\imath}\varepsilon_{\imath} A_{\imath} A_{\imath}$ | Local symmetry | Forbidden while massless; protected after breaking |
| Scalar | $m^2\xi_{\mathrm{pot}}^{\dagger}\xi_{\mathrm{pot}}$ | Nothing | $\delta m^2\propto\Lambda^2$ |

A symmetry that forbids the mass term also forbids its radiative correction, because the correction must respect the symmetry of the Lagrangian. Chiral symmetry forbids $m\barΞ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}$ for a massless fermion, so the correction must be proportional to the mass — a fermion mass is *technically natural*: setting it to zero is stable under renormalisation. Local symmetry forbids $m^2A^2$, so a connection mass is natural in the same sense.

The scalar has no such protection. $\xi_{\mathrm{pot}}^{\dagger}\xi_{\mathrm{pot}}$ is a singlet under every symmetry of the Standard Model, so no symmetry forbids it, and no symmetry can forbid its correction. This is the whole content of the hierarchy problem: it is a statement about the absence of a symmetry, and it is exact in that form.

The framework's account is a real observation and a small one. The algebra distinguishes the three cases in a way that matches: the fermion mass is a parameter of a chiral pair's mixing, and the mixing is what chiral symmetry forbids; the vector mass is a parameter of the metric structure, and the massless case is the natural one; the scalar mass is a parameter of a potential, and a potential is the one object with no derivational origin in the algebra at all. So the framework exhibits the asymmetry — it does not explain it.

## Response One: Supersymmetry

Pair every Standard Model state with a superpartner of the opposite statistics. The scalar's quadratic shift from a loop of fermions is then cancelled by the loop of the corresponding scalars, because the coupling is the same and the sign is opposite.

For each multiplet the cancellation is exact:

$$
\delta m_H^2\propto\left(m_B^2-m_F^2\right) ,
$$

so the shift vanishes exactly when supersymmetry is unbroken. Breaking it at scale $M_{\mathrm{SUSY}}$ leaves $\delta m_H^2\sim\frac{c}{16\pi^2}\left(M_{\mathrm{SUSY}}^2-m_{\mathrm{SM}}^2\right)$: the tuning is now a tuning on the *superpartner* masses.

The numbers are these, and there are two problems.

| $m_{\tilde t}$ (kg) | $\delta m_H^2$ (J$^2$) | $\mathcal{T}_{\mathrm{tune}}$ | $1/\mathcal{T}_{\mathrm{tune}}$ |
|---|---|---|---|
| $8.915\times10^{-25}$ | $3.59\times10^{-16}$ | $0.89$ | $1.12$ |
| $1.337\times10^{-24}$ | $6.98\times10^{-16}$ | $1.74$ | $0.58$ |
| $1.782\times10^{-24}$ | $1.10\times10^{-15}$ | $2.75$ | $0.36$ |
| $3.565\times10^{-24}$ | $3.08\times10^{-15}$ | $7.69$ | $0.13$ |
| $8.915\times10^{-24}$ | $8.32\times10^{-15}$ | $20.7$ | $0.048$ |

So a stop below $1.78\times10^{-24}\ \mathrm{kg}$, that is a supersymmetry-breaking scale of $1.6\times10^{-7}$ J, keeps the tuning under $30\%$, and a stop at $8.90\times10^{-24}\ \mathrm{kg}$ costs a factor of twenty. The LHC's stop searches reach about $1.34$–$2.34\times10^{-24}\ \mathrm{kg}$, at scales of $1.2$–$2.1\times10^{-7}$ J, in favourable topologies and have found nothing, so the natural region is excluded for the simplest models.

The second problem is independent. In the minimal supersymmetric Standard Model the quartic is fixed by the connection couplings,

$$
m_h^2=M_Z^2\cos^2 2\beta
\quad\Longrightarrow\quad
m_h\le M_Z=1.6258\times10^{-25}\ \mathrm{kg}\ \text{at tree level},
$$

against a measured $m_h=2.230\times10^{-25}$ kg. So the model requires large loop corrections from heavy stops to reach the measured mass, and those corrections are exactly the ones that reintroduce the tuning. The two requirements pull in opposite directions: *raise* $m_h$ needs heavy stops, *naturalness* needs light ones. This tension, not the absence of a discovery by itself, is what has made minimal supersymmetry uncomfortable.

Split supersymmetry survives, with the scalars heavy and the fermionic partners light. It gives up naturalness for the scalar mass and keeps the connection coupling unification and the dark matter candidate. It is a coherent position, and it concedes the point.

## Response Two: Compositeness and the Pseudo-Goldstone

If the Higgs is not elementary but a bound state of a new strong interaction at scale $f$, then its mass is not a fundamental parameter: it is generated by the strong dynamics, in the same way that the pion mass is generated by the quark masses and the nucleon mass by $\Lambda_{\mathrm{QCD}}$. The quadratic sensitivity is then cut off at $f$, and the Higgs is a light composite because it is a pseudo-Goldstone boson of an approximate symmetry.

Pseudo-Goldstone is the load-bearing part. A generic composite scalar has mass of order $f$, which is too heavy. A Goldstone boson has mass exactly zero, protected by the shift symmetry; breaking the symmetry explicitly and weakly gives a mass suppressed by the breaking, and the Standard Model's $v/f$ plays the role of that suppression:

$$
m_H^2\sim\frac{g_{\mathrm{strong}}^2}{16\pi^2}f^2\times\left(\frac{v}{f}\right)^{2}\quad\text{in the little-Higgs form,}
\qquad
\mathcal{T}_{\mathrm{tune}}\sim\left(\frac{f}{v}\right)^{2} .
$$

The tuning follows from $f/v$.

| $f$ | $v/f$ | $\mathcal{T}_{\mathrm{tune}}=(f/v)^2$ | $1/\mathcal{T}_{\mathrm{tune}}$ |
|---|---|---|---|
| $8.01\times10^{-8}\ \mathrm{J}$ | $0.492$ | $4.1$ | $0.24$ |
| $1.28\times10^{-7}\ \mathrm{J}$ | $0.308$ | $10.6$ | $0.095$ |
| $1.6\times10^{-7}\ \mathrm{J}$ | $0.246$ | $16.5$ | $0.061$ |
| $4.8\times10^{-7}\ \mathrm{J}$ | $0.082$ | $148$ | $0.007$ |

So $f$ must be within a factor of two of the weak scale for a $10\%$ tuning, and the LHC's exclusion of vector-like quarks and of $W'$-like resonances below about $1.5$–$3.2\times10^{-7}\ \mathrm{J}$ pushes $f$ up. The same tension as supersymmetry: the natural region is the excluded region.

The connection to this corpus is exact. Compositeness is the mechanism [the hadron article](hadron-structure-from-qcd-the-bound-state-problem.html) described for the proton: a mass generated by strong dynamics, non-perturbatively, with no dimensionful parameter in the Lagrangian. The difference is that the QCD case has a known dynamics and the electroweak case does not. The framework hosts the QCD mechanism in principle and does not host a second strong sector, which is the subject of the next section.

## Response Three: The Landscape

If the underlying theory has many vacua with different values of the Higgs mass parameter, and if the value is selected by the requirement that structure forms, then the smallness is a selection effect and not a cancellation.

Weinberg's original version was for the cosmological constant: a universe with a much larger vacuum energy does not form galaxies, so observers find themselves in a small one. The Higgs version is the same: a much larger $m_H^2$ means a much larger $v$, and a $v$ far above the weak scale gives a universe with no stable nuclei or no atoms.

It predicts no new particles, so it cannot be tested by the LHC. The three responses are not three candidate theories competing on the same data: two predict new states and one does not. That asymmetry is why the disagreement in the field will not be settled by the next collider.

The assessment has three parts.

- The landscape is not excluded. If the string landscape exists, the number $10^{32}$ is not a tuning but a probability, and the corpus has no argument against it.
- The landscape is not a solution in the sense the other two are: it does not explain *why* $m_H$ has its value, it explains why we see it.
- The landscape requires the anthropic step, and the anthropic step requires a measure on the space of vacua. The measure is not known, and without it the argument does not make quantitative predictions that could fail.

It belongs here because the framework has no measure either, and for the same reason: a measure requires a space to integrate over, and neither the algebra nor the landscape argument supplies one. Two positions that share a defect are not thereby both right, but the parallel is worth stating: the framework's silence on $m_H$ and the landscape's answer to it come from the same missing object.

## A Fourth That Failed: the Veltman Condition

If the sum of the coefficients of the quadratic divergences vanishes, the quadratic sensitivity cancels among Standard Model states and no new physics is needed.

The condition is one equation on the measured couplings:

$$
\sum_i c_i=0 ,
$$

and from the table above the sum is $2.489$, which is not zero. The condition would be satisfied if the top's contribution were opposite and equal to the rest, which requires

$$
3y_t^2=0.239+0.774=1.013
\quad\Longrightarrow\quad
m_t=2.549\times10^{-25}\ \mathrm{kg},
$$

against a measured $m_t=3.079\times10^{-25}$ kg. The condition fails by $20\%$ in the mass, that is by $45\%$ in the squared coupling.

The failure is informative. The quadratic terms do not cancel accidentally in the Standard Model, so no hidden mechanism is already present. The condition is also a *fine tuning of a different kind*: one equation on the parameters, not satisfied. A framework that solved the hierarchy problem by a cancellation among Standard Model states would have to explain why this particular combination vanishes, and nothing does.

The lesson is that naturalness conditions are equations, and equations can be checked. The Veltman condition is the cleanest case of a naturalness proposal that is *arithmetically* refuted rather than merely unfound.

## What the Algebra Says

The framework says nothing about the tuning, and the reason it says nothing is exact: the quadratic sensitivity is a statement about a cutoff, a cutoff is a property of a regularisation, the algebra has no measure on field space, and therefore the framework has no cutoff to be sensitive.

The statement has three parts.

- There is no measure. [The symmetry group ceiling article](the-compact-sector-of-the-biquaternions-is-u2.html) and [the lattice article](lattice-connection-theory-and-the-biquaternion-path-integral.html) record between them that the path integral over $\mathbb{B}$-valued fields is a formal object, that the fermionic measure is not an algebraic operation, and that a cutoff is imposed from outside. So the framework's loop integrals are not defined and the quadratic term cannot be computed in it.
- There is no second strong sector. Compositeness requires a new confining dynamics at $f\sim1.6\times10^{-7}\ \mathrm{J}$. The framework has exactly one strong sector available — the imported $SU(3)$ — and no second one. [The ceiling](the-compact-sector-of-the-biquaternions-is-u2.html) is the reason: no compact algebra of dimension above four, so no second confining group.
- There is no vacuum selection. A landscape requires a space of vacua with a measure. The algebra has one vacuum, the identity of the field algebra, and no family of them.

One structural observation is not silence. A dimensionless algebra cannot generate a dimensionful parameter by itself. [The hadron article](hadron-structure-from-qcd-the-bound-state-problem.html) established this and then established the resolution: QCD generates $\Lambda_{\mathrm{QCD}}$ non-perturbatively, by dimensional transmutation, with an essential singularity at $\alpha_s=0$. The electroweak sector has the same logical gap and no such mechanism. The Higgs mass is a *parameter*, not an anomaly's matrix element, and no conformal anomaly generates it.

The contrast is the article's one real contribution:

| Sector | Dimensionful quantity | Origin | Framework's role |
|---|---|---|---|
| QCD | $\Lambda_{\mathrm{QCD}}=3.12\times10^{-11}\ \mathrm{J}$ | Dimensional transmutation, non-perturbative | Hosts the mechanism; cannot compute it |
| Electroweak | $v=3.94\times10^{-8}\ \mathrm{J}$ | A parameter of a potential, tuned | Hosts the potential; has no mechanism |

The two look like the same problem and are not. QCD's scale *is* generated and the generation is understood in principle. The electroweak scale is *not* generated, and the tuning is the statement that the model provides no generation. That is a sharper statement of the hierarchy problem than "the scalar mass is quadratically divergent", and the framework's structure is what makes it visible.

## Naturalness Is Not a Theorem

Naturalness is a heuristic: it asserts that dimensionless ratios should not be much smaller than the loop factors that generate them. It is not a theorem, it is not a symmetry, and it does not follow from any axiom.

One success is clear. [The closure article](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html) records it: GIM is a naturalness argument in a different guise. A loop of generation-universal couplings had to cancel, and the cancellation required a fourth quark with a specified coupling pattern. The prediction was right. This is the strongest evidence that the heuristic works.

One failure is equally clear. Supersymmetry at the weak scale was the prediction of the same heuristic applied to the scalar mass. The LHC did not find it. So the heuristic has been right once and wrong once, and the score is $1$–$1$ rather than decisive.

It could be wrong in two ways.

- Selection. If there are many vacua, a small ratio is not tuned, it is selected. The heuristic then has no force because the ensemble is not the one it assumes.
- Structure. The criterion assumes that the parameters are independent inputs. If the underlying theory relates them — if $m_H$ is a function of the same quantity that sets $M_{\mathrm{Pl}}$ — then the ratio is not tuned but computed, and the heuristic is measuring the wrong thing.

The corpus's position is to record the tension, to state the criterion's status, and not to use naturalness as evidence for or against anything. [The parameter-count article](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html) already established that the framework's defence is geometric rather than numerical; a naturalness argument would be a numerical defence, and the framework cannot mount one.

A reader who has been told that the hierarchy problem is "the deepest problem in physics" will read a framework that is silent on it as deficient. A heuristic is silent because it is a heuristic: it states no number for $m_H/v$, so there is no number to check.

## What a Solution Would Look Like

A solution would fall in one of three grades.

| Grade | Criterion | Would it settle the problem? |
|---|---|---|
| A mechanism | A symmetry, a dynamics or a selection principle that fixes $m_H/v$ | Yes |
| A relation | $m_H$ computed from another parameter | Yes, if the relation is measured |
| A cancellation | An arithmetic condition satisfied by the spectrum | Only if a reason for it is given |

Five candidates have been weighed.

| Mechanism | Predicts | Status |
|---|---|---|
| Supersymmetry | Superpartners below $\sim1.6\times10^{-7}\ \mathrm{J}$ | Not found; natural region excluded for minimal models |
| Compositeness | Resonances at $f\lesssim1.6\times10^{-7}\ \mathrm{J}$ | Not found; $f$ pushed above $1.5$–$3.2\times10^{-7}\ \mathrm{J}$ |
| Extra dimensions | Kaluza–Klein states | Not found |
| Landscape | Nothing | Untestable at colliders |
| Veltman | $m_t=2.549\times10^{-25}$ kg | Refuted, $m_t=3.079\times10^{-25}$ kg |

The corpus would accept a statement that makes $m_H/v$ a function of quantities already in the nineteen, at the second grade, with a measured consequence. No such statement exists, in the framework or outside it. The question is open, and it is neither to the framework's credit nor to its discredit.

Two things would change the picture. A new state coupled to the Higgs below a few $10^{-6}$ J would reopen the natural window. A demonstration that the landscape measure exists and is calculable would close the question in the other direction. Neither is in hand.

## What the Framework Supplies

The framework supplies two observations. The first is that the electroweak scale and the QCD scale are different *kinds* of problem: the first is generated and the second is not, and the framework's structure makes the distinction visible because it hosts the first mechanism (dimensional transmutation, per [the hadron article](hadron-structure-from-qcd-the-bound-state-problem.html)) and has no counterpart of it for the second. The second is that the scalar is the only field type whose mass term has no symmetry to forbid it, a fact the algebra's own organisation reproduces without explaining.

It supplies nothing else. No cutoff, because no measure. No second confining sector, because of the ceiling. No family of vacua, because the algebra has one. No mechanism relating $m_H$ to any other parameter.

The table gives each item and its provenance.

| Item | Status |
|---|---|
| $\delta m_H^2=\frac{c}{16\pi^2}\Lambda^2$ | Imported one-loop result |
| The coefficients $0.239$, $1.476$, $0.774$, sum $2.489$ | Computed here |
| The divergence-against-sensitivity distinction | This article's argument; the dim-reg statement imported |
| $\delta m_H^2=6.03\times10^{16}$ J$^2$ at $M_{\mathrm{Pl}}$ | Computed here |
| The tuning table, $10^{32}$ at $M_{\mathrm{Pl}}$ | Computed here |
| $\Lambda_{\mathrm{stable}}=1.60\times10^{-7}\ \mathrm{J}$ $=8.0\,m_H$ | Computed here |
| Chiral and representative protection of fermion and vector masses | Imported |
| The MSSM bound $m_h\le M_Z$ | Imported; the number $1.6258\times10^{-25}$ kg quoted |
| The stop-tuning table | Computed here |
| The composite tuning $(f/v)^2$ | Computed here |
| The landscape argument | Imported; its status assessed here |
| The Veltman condition and $m_t=2.549\times10^{-25}$ kg | Computed here |
| The QCD-versus-electroweak contrast | Framework result, resting on the hadron article |
| Naturalness as a heuristic, $1$–$1$ | This article's assessment |
| A mechanism for $m_H/v$ | Not available |

## Summary

The Higgs mass is the only dimensionful parameter with no symmetry to protect it. Every heavy state coupled to the Higgs shifts it by $\frac{c}{16\pi^2}\Lambda^2$, with coefficients $0.239$ from connections, $1.476$ from the top and $0.774$ from the quartic, summing to $2.489$.

The divergence is a convention — dimensional regularisation gives no quadratic term at all — but the sensitivity is not. It is a statement about heavy states, and it produces the tuning: $\Lambda=1.6\times10^{-7}\ \mathrm{J}$ costs nothing, $1.6\times10^{-6}\ \mathrm{J}$ costs one part in a hundred, $M_{\mathrm{Pl}}$ costs one part in $3.0\times10^{32}$.

Radiative stability requires new physics within $8.0$ Higgs masses, that is $1.60\times10^{-7}\ \mathrm{J}$ or $4.05\,v$, and the LHC's null results have closed that window for states with Standard-Model-like couplings.

Fermion and connection masses are protected because a symmetry forbids the mass term and hence its correction. The scalar has no such symmetry, and that is the whole content of the problem.

Three responses: supersymmetry needs stops below $1.6\times10^{-7}\ \mathrm{J}$ for $30\%$ tuning, and its tree-level bound $m_h\le1.6258\times10^{-25}$ kg pulls the other way; compositeness needs $f\lesssim1.6\times10^{-7}\ \mathrm{J}$, and its tuning is $(f/v)^2=16.5$ at $f=1.6\times10^{-7}\ \mathrm{J}$; the landscape needs no new physics and makes no collider prediction. A fourth, the Veltman condition, is arithmetically refuted: it requires $m_t=2.549\times10^{-25}$ kg against a measured $3.079\times10^{-25}$ kg.

The framework has no cutoff — no measure — so the quadratic term cannot be computed in it, and it has no second confining sector and no family of vacua. Its one contribution is the contrast between the two scales: $\Lambda_{\mathrm{QCD}}$ is generated non-perturbatively and $v$ is not, and the tuning is the statement that the electroweak sector has no counterpart of the mechanism the strong sector does have.

Naturalness is a heuristic with one success (GIM) and one failure (weak-scale supersymmetry). It is recorded as a heuristic, and the tension is recorded as open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda$ | Cutoff, or the scale of new physics |
| $\delta m_H^2$ | One-loop shift of the Higgs mass squared |
| $c_i$ | Coefficient of the quadratic divergence from source $i$ |
| $\mathcal{T}_{\mathrm{tune}}$ | Tuning, $\lvert\delta m_H^2\rvert/m_H^2$ |
| $\varpi_{\mathrm{cpl}}$ | Higgs quartic, $0.1291$ |
| $y_t$ | $m_t/v=0.7014$ in this article's convention, with $m_t=3.079\times10^{-25}$ kg and $v=4.3893\times10^{-25}$ kg; the $\sqrt2$-normalised Yukawa is $0.9919$ |
| $v$ | Higgs expectation value, $4.3893\times10^{-25}$ kg (an energy of $3.9449\times10^{-8}$ J) |
| $f$ | Compositeness scale |
| $M_{\mathrm{SUSY}}$, $m_{\tilde t}$ | Supersymmetry breaking scale, stop mass |
| $M_{\mathrm{Pl}}$ | Planck scale, $1.95\times10^{9}\ \mathrm{J}$ |
| $\Lambda_{\mathrm{QCD}}$ | Strong-interaction scale, $\approx3.12\times10^{-11}\ \mathrm{J}$ |

## Further Reading

- [Hadron Structure from QCD: the Bound-State Problem](hadron-structure-from-qcd-the-bound-state-problem.html). The other end of the contrast: a scale that *is* generated, non-perturbatively, with no dimensionful parameter in the Lagrangian.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Vector-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html). The potential whose two parameters carry the tuning.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html). What the framework does represent of the scalar sector, and what it does not.
- [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html). How the scalar mass and any new heavy state enter the fit, and why $T$ is the observable that measures them.
- [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html). Where $v$ and $M_H$ appear as two of the nineteen, both in the group with no arena.
- [Asymptotic Freedom and the Running of the Strong Force](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). The running that makes the QCD scale possible, and the contrast the framework's silence on $v$ is measured against.
- [The Compact Sector of the Biquaternions Is $\mathfrak{u}(2)$: No $\mathfrak{su}(3)$ Among the Operators](the-compact-sector-of-the-biquaternions-is-u2.html). Why no second confining sector is available, and hence why compositeness cannot be built here.
- [Meson Mixing, Rare Decays and the Unitarity Triangle as a Closure Test](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html). GIM as the naturalness argument that worked, and the standard for what "worked" means.
- [The Yukawa Sector of the $\mathrm{SU}(4)$ Model: One Matrix and Its Diagonalisation](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). The top Yukawa that dominates the coefficient.
