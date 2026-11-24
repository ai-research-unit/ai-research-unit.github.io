# __The Landau Pole, Triviality and Vacuum Stability__

## Introduction

**The claim.** Three questions about the Standard Model's validity at high energy have one common source: the running of $\varpi_{\mathrm{cpl}}$ and of $g_{\mathrm Y}$. Asked separately they look like three separate worries. Asked together they are one calculation, and the three answers have the same shape — a scale, a bound, and a lifetime.

**The answer.**

$$
\boxed{\;M_{\text{pole}}=2.884\times10^{31}\ \mathrm{J},\qquad
m_H\le2.567\times10^{-25}\ \text{kg},\qquad
\tau_{\text{vac}}=10^{649}\,t_{U}\;}
$$

**Units.** A mass in this article is written in kilograms. A cutoff, a running scale and a decay rate stay in joules, because those quantities are energies and the joule is their unit. The two are never mixed: a mass is a mass and a joule value is an energy.

**The three questions.**

| Question | Quantity | Answer's form | This article's value |
|---|---|---|---|
| Does the theory remain defined at arbitrarily high energy? | $g_{\mathrm Y}(\mu)$ | A pole scale | $2.884\times10^{31}\ \mathrm{J}$ |
| Can a fundamental scalar be both weakly coupled and UV-complete? | $\varpi_{\mathrm{cpl}}(\mu)$ | An upper bound on $m_H$ | $2.567\times10^{-25}$ kg at the Planck scale |
| What is the fate of the vacuum we live in? | $\varpi_{\mathrm{cpl}}(\mu)$ | A lifetime | Metastable, $10^{649}$ times the age of the universe |

**The standing.** Every equation below is standard. The framework's contribution is confined to one section and consists of two structural statements and one gap, and the gap is the more informative of the three.

**The four results.**

- The hypercharge Landau pole is at $2.884\times10^{31}\ \mathrm{J}$, which is $1.5\times10^{22}$ Planck masses. So it is not a problem for the Standard Model alone: gravity intervenes $22$ orders of magnitude first. But it is a statement about the *kind* of group $\mathrm{U}(1)_Y$ is, and that statement is structural.
- Triviality bounds the Higgs mass from above at every cutoff, and at the Planck scale the bound is $m_H=2.567\times10^{-25}$ kg. The measured $m_H=2.230\times10^{-25}$ kg is $86.8\%$ of it. That is a striking saturation and this article refuses to call it a hint.
- The vacuum is metastable, not unstable, and the distinction is $649$ orders of magnitude. The tunnelling exponent is $S_E\approx1880$ against a threshold of about $440$.
- We sit $\Delta m_t=2.48\times10^{-27}$ kg above the stability edge, which is $4.6$ standard deviations of the top mass. That is one of the sharpest statements of its kind in the model, and it is a statement about where we are, not about what the theory says.

One methodological warning, given early because it governs the whole article. The fate of $\varpi_{\mathrm{cpl}}$ is decided by a difference of terms of order one, so the answer is a *precision* statement: it needs two- and three-loop running and a careful conversion between the pole and $\overline{\mathrm{MS}}$ top mass. A one-loop estimate gets the *sign* right and the *scale* wrong, sometimes by many orders of magnitude. The corpus's rule — never print a number without its order and its scheme — is not a formality here; it is the difference between a correct and an incorrect answer.

**The order.** The three questions, then the hypercharge pole, then why abelian is different, then triviality, then the near miss of the three couplings, then the fate of $\varpi_{\mathrm{cpl}}$, then what "unstable" means, then the metastability window, then the renormalisation group input, then the two-sector question, then what the algebra says, then what would change the answer, then the ledger.

## Three Questions, One Calculation

Why they are one. Each is a question about the value of a coupling at a scale far from the weak scale, and each is answered by solving the same system of ordinary differential equations:

$$
\frac{dg_i}{d\ln\mu}=\frac{b_i}{16\pi^2}g_i^3 ,\qquad
\frac{dy_t}{d\ln\mu}=\frac{y_t}{16\pi^2}\left(\frac92y_t^2-8g_s^2-\frac94g^2-\frac{17}{12}g_{\mathrm Y}^2\right) ,
$$

$$
\frac{d\varpi_{\mathrm{cpl}}}{d\ln\mu}=\frac{1}{16\pi^2}\left[24\varpi_{\mathrm{cpl}}^2-6y_t^4+\frac38\left(2g^4+\left(g^2+g_{\mathrm Y}^2\right)^2\right)+\varpi_{\mathrm{cpl}}\left(12y_t^2-9g^2-3g_{\mathrm Y}^2\right)\right] .
$$

The one-loop coefficients, which decide the first question outright.

| Coupling | $b$ | Sign | Consequence |
|---|---|---|---|
| $g_{\mathrm Y}$ | $+\tfrac{41}{6}$ | Positive | Grows with energy: a Landau pole |
| $g$ | $-\tfrac{19}{6}$ | Negative | Falls: asymptotically free |
| $g_s$ | $-7$ | Negative | Falls fastest: strongly asymptotically free |

The signs are the whole content of the first two questions. A positive $b$ means the coupling grows, and a coupling that grows without bound reaches a pole in finite time. A negative $b$ means it shrinks, and a coupling that shrinks is free at short distances.

**What the three questions are not.** They are not three independent tests of the model. The model passes two of them trivially — a metastable vacuum with a lifetime $10^{649}$ times the age of the universe is not a problem — and the third is not a statement about the model at all but about the group. The article's value is in the arithmetic and in the distinctions, not in a verdict.

## The $\mathrm{U}(1)_Y$ Landau Pole

The computation, in three lines. With $\alpha_{\mathrm Y}=g_{\mathrm Y}^2/4\pi$ and $b_1=41/6$,

$$
\frac{1}{\alpha_{\mathrm Y}(\mu)}=\frac{1}{\alpha_{\mathrm Y}(M_Z)}-\frac{b_1}{2\pi}\ln\frac{\mu}{M_Z} ,
$$

so the pole is where the right-hand side vanishes:

$$
\ln\frac{\Lambda}{\mu}=\frac{2\pi}{b_1\,\alpha_{\mathrm Y}(\mu)}=\frac{6\pi\cdot98.41}{41}=90.48 .
$$

With $\mu=1.461\times10^{-8}\ \mathrm{J}$ at the $Z$ pole, $\Lambda=2.9\times10^{31}\ \mathrm{J}$.

Where that sits.

| Comparison | Value |
|---|---|
| $\Lambda_{\mathrm{Landau}}$ | $2.884\times10^{31}\ \mathrm{J}$ |
| Planck scale | $1.9\times10^{9}\ \mathrm{J}$ |
| Ratio | $1.5\times10^{22}$ |
| In Planck masses | $1.5\times10^{22}\,M_{\mathrm{Pl}}$ |

So the pole is not reached. Whatever replaces the Standard Model does so at or below the Planck scale, and the hypercharge coupling at that scale is still small.

The coupling along the way, which is the more useful table.

| $\mu$ | $g_{\mathrm Y}$ | Comment |
|---|---|---|
| $1.461\times10^{-8}\ \mathrm{J}$ ($Z$ pole) | $0.357$ | Input |
| $1.6\times10^{-7}$ J | $0.362$ | Barely moves |
| $1.6\times10^{-6}$ J | $0.367$ | — |
| $1.6\times10^{1}$ J | $0.407$ | $14\%$ above the input |
| $1.6\times10^{6}$ J | $0.446$ | $25\%$ |
| $M_{\mathrm{Pl}}$ | $0.476$ | $33\%$, still perturbative |

**The physical statement.** $g_{\mathrm Y}$ grows by a third over thirty-eight e-folds. That is not a crisis; it is the mark of an abelian factor with matter that carries hypercharge. The growth is slow because $b_1$ is small and because logarithms are logarithms.

Why the pole is nevertheless worth printing. Because it is the only place in the model where a coupling's growth is *unbounded*, and because the reason is structural rather than accidental. A non-abelian coupling has a negative $b$ because the gauge bosons themselves carry charge and screen the other way; an abelian coupling has no such self-interaction, so its $\beta$ function is the sum of matter contributions alone and is necessarily positive for the matter the model contains. Section *Why Abelian Is Different* makes that exact.

What the framework says about it, stated here so it is not repeated. The framework's gauge principle produces a *central* abelian factor — this is the ceiling's constructive half, recorded in [the gauge-group article](the-electroweak-gauge-group-and-the-hypercharge-assignment.html) — and a central factor has no self-interaction by definition. So the positive $b_1$ is not a choice the framework could have made differently. That is a real structural statement and it is the strongest thing this article has to say on the subject.

## Why Abelian Is Different

The diagrammatic reason. The $\beta$ function's sign is decided by the screening-versus-antiscreening competition:

| Contribution | Sign of $b$ | Present for |
|---|---|---|
| Matter loop (fermions, scalars) | Positive: screening | All couplings |
| Gauge-boson loop | Negative: antiscreening | Non-abelian only |
| Ghost loop | Negative: antiscreening | Non-abelian only |
| Scalar loop | Positive | All couplings with scalars |

The numbers, decomposed. For the Standard Model,

$$
b_1=+\frac{41}{6}\ \text{(matter only)},\qquad
b_2=-\frac{19}{6}=\underbrace{-\frac{22}{3}}_{\text{gauge+ghost}}+\underbrace{\frac{4}{3}N_g}_{\text{fermions}}+\underbrace{\frac16}_{\text{scalar}} ,
$$

where $N_g=3$. The non-abelian case has a large negative gauge term and a smaller positive matter term; the abelian case has no negative term at all.

**Why the framework's abelian factor cannot escape this.** A central element commutes with everything, so the field strength built from a central connection has no commutator term — the curvature is $dA$ and not $dA+A\wedge A$ — and there is no self-coupling. No self-coupling means no antiscreening loop. So the sign of $b_1$ is a theorem about central factors, not a numerical accident.

What this costs the framework's picture. It means that the one coupling the framework supplies most naturally — the central abelian one, whose parameter $ϙ$ [the parameter-count article](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html) counts as entry 14 — is precisely the one that cannot be UV-complete on its own. The framework's most native object is its least UV-safe one. That is an honest observation and it has no remedy inside the algebra.

The contrast with QCD, which is the corpus's reference case. [The asymptotic-freedom article](asymptotic-freedom-and-the-running-of-the-strong-coupling.html) records $b_3=-7$ and the resulting screening: $g_s$ falls from $1.221$ at $M_Z$ to $0.49$ at $M_{\mathrm{Pl}}$, a factor of $2.5$. The two couplings move in opposite directions from the same starting magnitude, and the difference is entirely the gauge self-interaction.

## Triviality: a Fundamental Scalar Cannot Be Both Weak and Complete

The statement. Take the quartic's own $\beta$ function, dominated by $24\varpi_{\mathrm{cpl}}^2$ when $\varpi_{\mathrm{cpl}}$ is the largest coupling:

$$
\frac{d\varpi_{\mathrm{cpl}}}{d\ln\mu}=\frac{24\varpi_{\mathrm{cpl}}^2}{16\pi^2}
\quad\Longrightarrow\quad
\frac{1}{\varpi_{\mathrm{cpl}}(\mu)}=\frac{1}{\varpi_{\mathrm{cpl}}(v)}-\frac{24}{16\pi^2}\ln\frac{\mu}{v} .
$$

The consequence. $\varpi_{\mathrm{cpl}}(\mu)$ diverges at

$$
\Lambda_{\mathrm{pole}}=v\exp\left(\frac{16\pi^2}{24\varpi_{\mathrm{cpl}}(v)}\right)=246.22\times e^{50.97}=5.45\times10^{14}\ \mathrm{J} .
$$

That pole is $2.8\times10^{5}$ Planck masses away, so it is not reached either. But the *bound* that follows from it is sharp, because it can be turned around: for a given cutoff $\Lambda$, $\varpi_{\mathrm{cpl}}$ must satisfy $1/\varpi_{\mathrm{cpl}}(\Lambda)>0$, that is

$$
\varpi_{\mathrm{cpl}}(v)<\frac{16\pi^2}{24\ln(\Lambda/v)}
\quad\Longrightarrow\quad
m_H<\sqrt{\frac{16\pi^2}{12\ln(\Lambda/v)}}\,v .
$$

The bound as a function of cutoff.

| Cutoff $\Lambda$ | $\varpi_{\mathrm{cpl},\max}$ | $m_H$ ceiling (kg) | $m_H^{\text{meas}}/m_H^{\max}$ |
|---|---|---|---|
| $1.6\times10^{-7}$ J | $4.69$ | $1.344\times10^{-24}$ | $0.166$ |
| $1.6\times10^{-6}$ J | $1.78$ | $8.270\times10^{-25}$ | $0.270$ |
| $1.6\times10^{-4}$ J | $0.792$ | $5.526\times10^{-25}$ | $0.404$ |
| $1.6\times10^{1}$ J | $0.332$ | $3.583\times10^{-25}$ | $0.624$ |
| $M_{\mathrm{Pl}}$ | $0.171$ | $2.567\times10^{-25}$ | $0.868$ |

The direction of the bound, which is the counter-intuitive part. A *larger* cutoff gives a *tighter* bound. At $1.6\times10^{-7}$ J a Higgs of $1.344\times10^{-24}$ kg is allowed; at the Planck scale only $2.567\times10^{-25}$ kg is. So triviality says: the further the theory is claimed to reach, the lighter the scalar must be.

Why it is called triviality. If $\varpi_{\mathrm{cpl}}(v)$ is held fixed while $\Lambda\to\infty$, then $1/\varpi_{\mathrm{cpl}}(\Lambda)\to-\infty$, which means the theory is not defined. The only way to take the cutoff to infinity is $\varpi_{\mathrm{cpl}}(v)\to0$, that is a free field — a trivial theory. Hence: a $\xi_{\mathrm{pot}}^4$ theory in four dimensions is at best an *effective* theory with a finite cutoff. This is a rigorous lattice result, not a perturbative artefact.

The saturation, and the corpus's refusal. The measured $2.230\times10^{-25}$ kg is $86.8\%$ of the ceiling at the Planck scale. One can say that the Standard Model is "just barely" a valid effective theory to $M_{\mathrm{Pl}}$. One can also say that any number is some percentage of some bound. The honest statement is the arithmetic: the margin is a factor $1.15$ in mass, and it is not evidence for or against anything. [The naturalness article](the-hierarchy-problem-and-naturalness.html) established the same discipline for tuning; it applies here.

**What the bound is not.** It is not a bound on the Higgs mass in the real world. If the Higgs is composite, $\varpi_{\mathrm{cpl}}$ is not a fundamental coupling and the argument does not apply. Triviality constrains a *fundamental* scalar, and whether the Higgs is fundamental is open.

## The Near Miss at the Planck Scale

The observation. Run the three gauge couplings to the Planck scale with the one-loop coefficients above and they almost meet:

| $\mu$ | $g_{\mathrm Y}$ | $g$ | $g_s$ | Spread |
|---|---|---|---|---|
| $M_Z$ | $0.357$ | $0.652$ | $1.221$ | $0.864$ |
| $1.6\times10^{-6}$ J | $0.367$ | $0.627$ | $0.959$ | $0.592$ |
| $1.6\times10^{1}$ J | $0.407$ | $0.560$ | $0.630$ | $0.223$ |
| $1.6\times10^{6}$ J | $0.446$ | $0.523$ | $0.532$ | $0.086$ |
| $M_{\mathrm{Pl}}$ | $0.476$ | $0.504$ | $0.490$ | $0.028$ |

The numbers. At the Planck scale the three couplings are $0.476$, $0.504$ and $0.490$ — a spread of $0.028$, which is $5.7\%$ of their mean $0.490$. They do not meet, but they come within $6\%$ of doing so, at the scale where the calculation stops.

Why this is worth a section. Because it is the strongest single hint that the Standard Model is a fragment of something larger, and because it is *quantitatively* strong: three couplings that start two orders of magnitude apart and converge to within $6\%$ at $1.6\times10^{9}$ J is not a coincidence that happens by chance. The standard reading is that a Grand Unified group completes the meeting at a scale near $1.6\times10^{6}$ J, and that the mismatch at the Planck scale is the footprint of the states that complete it.

**What the framework can say, which is nothing.** [The ceiling article](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) established that no compact gauge algebra of dimension above four fits inside $\mathbb{B}$, so no Grand Unified group is available and the near miss has no completion here. This is the cleanest case in the corpus where an empirical hint points at precisely the structure the algebra forbids.

What the near miss does not prove. That unification happens, that it happens at $1.6\times10^{6}$ J, or that a GUT exists. It says that the three couplings' trajectories converge, which is a fact about the spectrum the model happens to have. Supersymmetry changes the convergence point; a different matter content changes it too. The observation is robust; its interpretation is not.

## The Fate of $\varpi_{\mathrm{cpl}}$: a Difference of Terms of Order One

The $\beta$ function, term by term, at the weak scale. With $y_t=\sqrt2\,m_t/v=0.991$, $\varpi_{\mathrm{cpl}}=0.1291$, $g=0.652$ and $g_{\mathrm Y}=0.357$:

| Term | Origin | Value |
|---|---|---|
| $24\varpi_{\mathrm{cpl}}^2$ | Scalar self-coupling | $+0.400$ |
| $-6y_t^4$ | Top quark | $-5.81$ |
| $\tfrac38\left(2g^4+(g^2+g_{\mathrm Y}^2)^2\right)$ | Gauge bosons | $+0.250$ |
| $\varpi_{\mathrm{cpl}}\left(12y_t^2-9g^2-3g_{\mathrm Y}^2\right)$ | Mixed | $+0.98$ |
| **Sum** | | $-4.18$ |
| $\beta_{\varpi_{\mathrm{cpl}}}=\text{sum}/16\pi^2$ | | $-0.0265$ |

**The structure, which is the article's central methodological point.** One negative term of order five is cancelled by three positive terms summing to about $1.6$. The residual is a *difference of terms of order one*, and the sign of $\varpi_{\mathrm{cpl}}$'s fate depends on that difference.

Why that makes the answer a precision question.

- The residual is a large fraction of the largest term. $\lvert-4.18\rvert$ is $72\%$ of $\lvert-6y_t^4\rvert$, and the negative term exceeds the sum of the three positive ones by a factor $3.56$. So the sum is not a near-cancellation in the arithmetic sense — but it is a *difference*, and a $20\%$ correction to any one term changes it by $20$ to $35\%$, while the *scale* at which $\varpi_{\mathrm{cpl}}$ reaches zero depends exponentially on the sum.
- The running of $\beta$ matters as much as $\beta$. $y_t$ falls from $0.991$ at $M_Z$ to $0.42$ at $M_{\mathrm{Pl}}$, so $-6y_t^4$ falls from $-5.81$ to $-0.19$ — a factor of $30$. $\beta_{\varpi_{\mathrm{cpl}}}$ is therefore not the weak-scale number throughout: it shrinks by an order of magnitude, and once $\varpi_{\mathrm{cpl}}$ is small the $+0.25$ gauge term is comparable to what remains of the top term. A one-loop estimate that holds $\beta$ fixed at its weak-scale value gives the wrong crossing scale by many orders of magnitude.
- The scheme matters. $y_t$ is defined from the top mass, and the pole mass and the $\overline{\mathrm{MS}}$ mass differ by $\Delta m_t=1.427\times10^{-26}$ kg, which is a $5\%$ change in $y_t$ and a $20\%$ change in $y_t^4$. The instability scale is exponentially sensitive to precisely that.

So the article quotes the higher-order result and labels it. The three-loop computation with $m_H=2.230\times10^{-25}$ kg and $m_t=3.079\times10^{-25}$ kg gives

$$
\varpi_{\mathrm{cpl}}(\mu)=0\ \text{at}\ \mu\approx1.6\times10^{1}\ \mathrm{J},
\qquad
\varpi_{\mathrm{cpl}}(M_{\mathrm{Pl}})\approx-0.014 .
$$

Both numbers are imported. What this article computes is the structure above and the consequences below; what it does not do is re-derive the running to three loops.

Why the corpus prints the caveat rather than the number alone. Because [the closure article](meson-mixing-rare-decays-and-the-unitarity-triangle-as-a-closure-test.html) established the rule that a number without its order is not a number, and because this is the case where the rule has teeth: the qualitative conclusion — metastable or stable — has flipped more than once in the literature as loops and mass definitions were improved.

## What "Unstable" Means: the Tunnelling Calculation

Three distinct statements, which are constantly confused.

| Statement | Condition | Meaning |
|---|---|---|
| Absolute stability | $\varpi_{\mathrm{cpl}}(\mu)>0$ for all $\mu$ | The vacuum is the global minimum everywhere |
| Metastability | $\varpi_{\mathrm{cpl}}$ goes negative, but the tunnelling time exceeds the age | The vacuum is a local minimum, deep enough to be long-lived |
| Instability | $\varpi_{\mathrm{cpl}}$ goes negative and the tunnelling time is short | The vacuum does not survive |

The Standard Model is in the second case, and the difference between the second and the third is the whole of the next computation.

The bounce action. For a negative quartic of magnitude $\lvert\varpi_{\mathrm{cpl}}\rvert$, the Euclidean bounce action is

$$
S_E\approx\frac{8\pi^2}{3\lvert\varpi_{\mathrm{cpl}}\rvert} .
$$

With $\lvert\varpi_{\mathrm{cpl}}\rvert=0.014$ from the three-loop result at the Planck scale,

$$
S_E=\frac{8\pi^2}{3(0.014)}=1880 .
$$

The comparison with the age of the universe. The decay rate per unit volume is of order $R^{-4}e^{-S_E}$, and the requirement that the vacuum survive the age of the universe is $S_E\gtrsim440$. Writing both sides as powers of ten:

| Quantity | Value |
|---|---|
| $e^{S_E}$ | $10^{816}$ |
| $H_0^{-4}$ (the age, in J$^{-4}$) | $1.5\times10^{206}$ |
| Margin | $10^{649}$ |

**The reading.** The tunnelling exponent exceeds the threshold by a factor of about $4$, and in a quantity that appears in an exponent that factor becomes $649$ orders of magnitude in the rate. So the vacuum is metastable with an enormous margin. "The electroweak vacuum is unstable" is, taken literally, false; "the electroweak vacuum is not the global minimum" is true; and the difference between the two sentences is $10^{649}$.

What would make it short-lived. A lighter Higgs or a heavier top pushes $\lvert\varpi_{\mathrm{cpl}}\rvert$ at the Planck scale up, so $S_E$ falls. At $\lvert\varpi_{\mathrm{cpl}}\rvert\approx0.06$, $S_E=8\pi^2/(3\times0.06)=439$ and the lifetime is the age of the universe. So the margin is a factor $4.3$ in $\lvert\varpi_{\mathrm{cpl}}(M_{\mathrm{Pl}})\rvert$ — a shift of $0.046$. Since the metastability ceiling sits at $m_t\approx3.173\times10^{-25}$ kg against an edge at $3.054\times10^{-25}$ kg, that shift corresponds to about $1.25\times10^{-26}$ kg in the top mass, which is why the statement is a measurement and not a theorem.

## The Metastability Window, and Where We Sit

The window in the top mass. For $m_H=2.230\times10^{-25}$ kg:

| Top mass | Status |
|---|---|
| $m_t<3.054\times10^{-25}$ kg | Absolute stability: $\varpi_{\mathrm{cpl}}>0$ to $M_{\mathrm{Pl}}$ |
| $3.054\times10^{-25}<m_t<3.173\times10^{-25}$ kg | Metastable, lifetime exceeding the age |
| $m_t>3.173\times10^{-25}$ kg | Lifetime shorter than the age: effectively unstable |

And the measurement:

$$
m_t=3.079\times10^{-25}\pm5.3\times10^{-28}\ \mathrm{kg},
\qquad
m_t-m_t^{\mathrm{crit}}=2.48\times10^{-27}\ \mathrm{kg}=4.6\sigma .
$$

So the vacuum is metastable at four and a half standard deviations. Not marginally, and not by a wide margin either: the measurement sits $2.48\times10^{-27}$ kg into a window that is $1.19\times10^{-26}$ kg wide.

The same statement in the Higgs mass, which is the more striking form. Solving for the Higgs mass at the stability edge, with $m_t=3.079\times10^{-25}$ kg, gives $m_h^{\mathrm{crit}}\approx2.309\times10^{-25}$ kg. So

$$
m_h^{\mathrm{meas}}=2.230\times10^{-25}\ \mathrm{kg}=m_h^{\mathrm{crit}}-7.86\times10^{-27}\ \mathrm{kg} ,
$$

and the triviality ceiling is $2.567\times10^{-25}$ kg. The allowed window for absolute stability to the Planck scale is therefore about $[2.309,\,2.567]\times10^{-25}$ kg, and the measured value sits $7.86\times10^{-27}$ kg below it.

**The temptation, and the refusal.** The measured Higgs mass sits just below a stability bound and just below a triviality bound, in a window about $2.59\times10^{-26}$ kg wide out of a range spanning five orders of magnitude. It is tempting to read this as selection or design. The corpus records the numbers and declines the inference, for a reason [the naturalness article](the-hierarchy-problem-and-naturalness.html) already gave: the window is a bound from an *assumption* — that the Standard Model holds to $M_{\mathrm{Pl}}$ — and if new physics enters at $1.6\times10^{1}$ J, which is where $\varpi_{\mathrm{cpl}}$ crosses zero, the whole window moves.

The one legitimate inference. The crossing scale $1.6\times10^{1}$ J is below the Planck scale, so the Standard Model *as an effective theory* is self-consistent up to that scale and no further, and new physics between $10^{11}$ and $1.6\times10^{9}$ J is not merely allowed but required to prevent the vacuum from being the wrong one. That is a real constraint on model building, and it is the same constraint that makes the stability statement interesting.

## The Renormalisation Group Input

What [the renormalisation-group article](the-renormalization-group-in-biquaternionic-form.html) supplies, and what it does not. That article establishes three things this one uses:

- The flow equation is exact and the regulator is an input. The Wetterich equation holds for any admissible $R_{\imath}$, and $R_{\imath}$ is not determined by the theory. So the trajectory $\Gamma_{\imath}$ depends on the scheme, while the physics does not.
- The algebra supplies a canonical home for the regulator. The wave biquaternion's norm $\langle\tilde P_\Phi\rangle_\natural=N$ is a *central* element, so the shell variable $N$ has an algebraic home, which is the one constructive thing the framework contributes to the renormalisation group.
- The regulator cannot assign the sectors different scales. It is a sharp cutoff on the central norm, and it is diagonal in the two sectors but common to both.

**The consequence for this article, which is a defect rather than a feature.** The quantities computed here span an enormous range of scales in one sector and a different range in another:

| Quantity | Scale | Sector |
|---|---|---|
| The weak scale, $v$ | $4.3893\times10^{-25}\ \mathrm{kg}$ | Electroweak |
| $\Lambda_{\mathrm{QCD}}$ | $3.2\times10^{-11}\ \mathrm{J}$ | Strong |
| Instability of $\varpi_{\mathrm{cpl}}$ | $1.6\times10^{1}$ J | Electroweak |
| $\mathrm{U}(1)_Y$ Landau pole | $2.884\times10^{31}\ \mathrm{J}$ | Hypercharge |

The span is $42$ orders of magnitude, and a single central-norm cutoff serves all of it. That is not wrong — a common cutoff is exactly what a Wilsonian scheme does — but it means the framework's regulator cannot be the *physical* cutoff of any one sector, because the physical cutoffs are $42$ orders apart. [The RG article](the-renormalization-group-in-biquaternionic-form.html) already flagged this as an open question; this article gives it a number.

What is imported whole. The three $\beta$ functions, the coefficients, the two- and three-loop corrections, the pole-to-$\overline{\mathrm{MS}}$ mass conversion, the bounce action, and the lifetime criterion. Every one of those is standard field theory. The framework supplies the shell, the central norm that hosts it, and no coefficient.

## What the Algebra Says

Three statements, one of which is a structural result.

**First, and this is the real one: the Landau pole is structural.** The framework's gauge principle produces a central abelian factor. A central connection has no self-coupling, therefore no antiscreening, therefore $b_1>0$ for any matter content with the observed quantum numbers. So the hypercharge pole is not a numerical accident that a different model might avoid; it is what a central factor *is*. The consequence is uncomfortable: the framework's most native object, the abelian connection with its free parameter $ϙ$, is the one object that cannot be UV-complete alone. Nothing in the algebra repairs this, because the repair would require the abelian factor to become non-abelian, which is precisely what the ceiling forbids.

Second: triviality is imported. The bound comes from the $\xi_{\mathrm{pot}}^4$ $\beta$ function, and the framework has no potential of its own from which a quartic's running could be derived. [The electroweak-symmetry-breaking article](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html) records that the potential is standard input; so is its running.

Third: the tunnelling calculation cannot be done here. A bounce is a saddle point of a Euclidean functional integral, and [the path-integral article](the-path-integral-in-biquaternionic-form.html) established that the measure lies outside $\mathbb{B}$. So the metastability statement is imported whole, and the framework neither confirms nor contradicts it.

The gap, stated as the article's conclusion about the framework. These three questions are questions about the *space of couplings*. The framework's objects live in the algebra, and the space of couplings lives outside it. So on this subject the framework is not a partial language with a few missing pieces; it is a language that does not address the question. That is a sharper and more useful statement than "the framework does not solve it", and it is the same kind of statement [the parameter-count article](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html) made about the nineteen.

One thing the algebra does say, and it is small. The instability scale is the scale at which the *effective* potential's quartic changes sign. In the framework's language the scalar potential is the one object with no derivational origin, so its coupling's running has no algebraic shadow either. The absence is consistent: nothing about $\varpi_{\mathrm{cpl}}$ is algebraic, from its value to its fate.

## What Would Change the Answer

Four possibilities, with their consequences.

| Change | Effect on the three questions |
|---|---|
| New physics at $1.6\times10^{1}$ J | Vacuum stability restored; instability scale becomes a threshold, not a fate |
| A composite Higgs | Triviality moot: $\varpi_{\mathrm{cpl}}$ is not fundamental; the bound disappears |
| A GUT at $1.6\times10^{6}$ J | The near miss is completed; $g_{\mathrm Y}$ runs into a non-abelian group, so no pole |
| Supersymmetry | All three change: two Higgs doublets, a different quartic, and the couplings meet exactly |

**Which of these the framework can express.** The last two, no: [the ceiling](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) forbids both a GUT group and a second confining sector, so neither a GUT nor compositeness is available. The first, yes in principle — new physics at $1.6\times10^{1}$ J is not a statement about the algebra — but the framework offers no candidate for it. The second, no, for the ceiling's reason.

The honest position. Of the four standard escapes, two are forbidden by the framework's own structure and two it cannot populate. That is a stronger statement than silence, and it is worth stating plainly: the framework's ceiling costs it exactly the escape routes that this article's three problems require.

## What the Framework Supplies

One structural result, three imports, one gap.

Supplied. The structural origin of the hypercharge Landau pole: a central abelian factor has no self-coupling, hence no antiscreening, hence $b_1>0$ necessarily. The algebraic home for the regulator, as a central biquaternion norm, which [the RG article](the-renormalization-group-in-biquaternionic-form.html) constructs. The observation that the framework's single cutoff is $42$ orders of magnitude too coarse to be any one sector's physical cutoff.

Imported. The three $\beta$ functions and their coefficients. The two- and three-loop running that locates the instability at $1.6\times10^{1}$ J and gives $\varpi_{\mathrm{cpl}}(M_{\mathrm{Pl}})=-0.014$. The pole-to-$\overline{\mathrm{MS}}$ top mass conversion. The bounce action and the lifetime criterion. The stability edge $m_t^{\mathrm{crit}}=2.745\times10^{-8}\ \mathrm{J}$ and the metastability ceiling $2.85\times10^{-8}\ \mathrm{J}$.

The ledger.

| Item | Status |
|---|---|
| $b_1=41/6$, $b_2=-19/6$, $b_3=-7$ | **Imported** one-loop coefficients |
| $\Lambda_{\mathrm{Landau}}=2.9\times10^{31}$ J | **Computed** here |
| $g_{\mathrm Y}(M_{\mathrm{Pl}})=0.476$ | **Computed** here |
| $\Lambda_{\mathrm{pole}}(\varpi_{\mathrm{cpl}})=5.4\times10^{14}$ J | **Computed** here from $24\varpi_{\mathrm{cpl}}^2$ alone |
| The triviality ceiling table, $2.567\times10^{-25}$ kg at the Planck scale | **Computed** here; the criterion stated |
| $m_H^{\mathrm{meas}}/m_H^{\max}=0.868$ | **Computed** here |
| The three couplings at $M_{\mathrm{Pl}}$, spread $0.028$ | **Computed** here |
| $\beta_{\varpi_{\mathrm{cpl}}}$ decomposition, sum $-4.13$ | **Computed** here at one loop, convention stated |
| $\varpi_{\mathrm{cpl}}=0$ at $1.6\times10^{1}$ J, $\varpi_{\mathrm{cpl}}(M_{\mathrm{Pl}})=-0.014$ | **Imported**, three loops; the one-loop value differs and is not printed |
| $S_E=1880$, margin $10^{649}$ | **Computed** here from the imported $\varpi_{\mathrm{cpl}}$ |
| $m_t^{\mathrm{crit}}=3.054\times10^{-25}$ kg, metastability to $3.173\times10^{-25}$ kg | **Imported** |
| $2.48\times10^{-27}$ kg in $m_t$, equal to $4.6\sigma$ | **Computed** here |
| $m_h^{\mathrm{crit}}\approx2.309\times10^{-25}$ kg, window $[2.309,\,2.567]\times10^{-25}$ kg | **Imported** edge, window computed here |
| The structural origin of $b_1>0$ | **Framework** result |
| A UV completion, a GUT, a composite Higgs | **Not available**, by the ceiling |

**What this article does not do.** It does not re-derive the three-loop running, does not compute a two-loop bounce, does not survey the vacuum-stability literature, and does not propose new physics at $1.6\times10^{1}$ J. It collects three questions into one calculation, prints the arithmetic, and states what the algebra does and does not say about the space of couplings.

## Summary

Three questions about the Standard Model's high-energy behaviour share one calculation, and the answers have the same shape.

The hypercharge coupling grows, because an abelian factor has no self-coupling and therefore no antiscreening: $b_1=+41/6$, and the pole is at $2.884\times10^{31}\ \mathrm{J}$, which is $1.5\times10^{22}$ Planck masses. The pole is never reached, but it is structural — a central factor cannot be UV-complete alone — and it singles out as the framework's weakest coupling the very object the framework supplies most naturally.

The quartic's growth bounds the Higgs mass from above at every cutoff: $1.344\times10^{-24}$ kg at $1.6\times10^{-7}$ J, $5.526\times10^{-25}$ kg at $1.6\times10^{-4}$ J, $2.567\times10^{-25}$ kg at the Planck scale. A larger cutoff gives a tighter bound, and at infinity the theory is free. The measured $2.230\times10^{-25}$ kg is $86.8\%$ of the Planck-scale ceiling.

The three gauge couplings almost meet: $0.476$, $0.504$, $0.490$ at $M_{\mathrm{Pl}}$, a spread of $5.7\%$. They do not meet, and the framework cannot complete them, because the ceiling forbids any gauge algebra above dimension four.

The quartic itself turns negative, because $\beta_{\varpi_{\mathrm{cpl}}}$ is a difference of terms of order one: $-6y_t^4=-5.76$ against $+0.400+0.250+0.98$. That structure makes the answer a precision question, and the three-loop answer is $\varpi_{\mathrm{cpl}}=0$ at $1.6\times10^{1}$ J and $\varpi_{\mathrm{cpl}}(M_{\mathrm{Pl}})=-0.014$. A one-loop estimate gets the sign right and the scale wrong by orders of magnitude, which is why the corpus prints the order with the number.

The vacuum is metastable, not unstable. The bounce action is $S_E=1880$ against a threshold of about $440$, so $e^{S_E}=10^{816}$ against $H_0^{-4}=10^{167}$: a margin of $10^{649}$.

We sit $\Delta m_t=2.48\times10^{-27}$ kg above the stability edge, that is $4.6\sigma$ in the top mass, and $7.86\times10^{-27}$ kg below the equivalent edge in the Higgs mass, in a window $[2.309,\,2.567]\times10^{-25}$ kg wide out of a range spanning five orders of magnitude. The corpus records that and declines the inference, because the window is conditional on the Standard Model holding to the Planck scale, and $\varpi_{\mathrm{cpl}}$ crosses zero eight orders below it.

The framework supplies one structural result — the sign of $b_1$ — one regulator, and one observation about its own cutoff being $42$ orders of magnitude too coarse to serve any single sector. It imports the $\beta$ functions, the running, the bounce and the lifetime criterion. On the space of couplings it has nothing to say, and that is a statement about what the algebra is, not about how well it has been used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $b_i$ | One-loop coefficients: $41/6$, $-19/6$, $-7$ |
| $\alpha_{\mathrm Y}$ | $g_{\mathrm Y}^2/4\pi$ |
| $\Lambda_{\mathrm{Landau}}$ | Scale of the hypercharge pole |
| $\varpi_{\mathrm{cpl}}$ | Higgs quartic, $0.1291$ at $v$ |
| $\Lambda_{\mathrm{pole}}$ | Scale of the quartic's own pole |
| $y_t$ | Top Yukawa, $\sqrt2\,m_t/v=0.991$ |
| $S_E$ | Euclidean bounce action |
| $H_0$ | Hubble constant, $2.4\times10^{-52}\ \mathrm{J}$ |
| $m_t^{\mathrm{crit}}$ | Top mass at the stability edge, $3.054\times10^{-25}$ kg |
| $m_h^{\mathrm{crit}}$ | Higgs mass at the stability edge, $2.309\times10^{-25}$ kg |
| $M_{\mathrm{Pl}}$ | Planck scale, $1.95\times10^{9}\ \mathrm{J}$ |

## Further Reading

- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html). The exact flow equation, the regulator the algebra supplies, and the open question this article turns into a number.
- [Asymptotic Freedom and the Running of the Strong Force](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). $b_3=-7$ and the contrast with the abelian case.
- [The Hierarchy Problem and Naturalness](the-hierarchy-problem-and-naturalness.html). The other consequence of the scalar sector's couplings, and the same discipline about what a bound means.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html). The potential whose quartic is the subject of half this article.
- [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html). $g_{\mathrm Y}$, $\varpi_{\mathrm{cpl}}$ and $m_H$ among the nineteen, and what kind of number each is.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3): Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). Why neither a GUT nor a composite Higgs can be built here.
- [The Path Integral in Biquaternionic Form](the-path-integral-in-biquaternionic-form.html). Why a bounce cannot be computed inside the algebra.
- [The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form](the-effective-potential-and-the-coleman-weinberg-mechanism-in-biquaternionic-form.html). The object whose quartic changes sign, in the framework's language.
- [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model: Four Conditions Become None](anomalies-and-anomaly-cancellation-in-the-four-colours-left-right-model.html). The conditions on the matter content that the $\beta$ coefficients inherit.
