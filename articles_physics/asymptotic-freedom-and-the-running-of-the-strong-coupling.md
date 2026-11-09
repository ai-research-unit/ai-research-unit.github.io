# __Asymptotic Freedom and the Running of the Strong Coupling__

## Introduction

**The standing of this article.** Everything below is standard theory, written in the corpus's coordinates and notation. It is **standard input**, not a framework result. The one-loop coefficient is the formula of [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html), and it is not re-derived here; what this article adds is the arithmetic of the coefficient in terms of the colour factors of [the QCD article](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html), the solution of the running equation, the numbers at the scales where the coupling is measured, and the one parameter that replaces the coupling.

**The claim.** The strong coupling is not a constant, and its dependence on scale has a sign that makes the theory calculable. Three statements carry the article.

- **One coefficient decides everything.** $b_0=11-\tfrac23N_f$ is positive for every $N_f\le16$, and its positivity is the whole content of asymptotic freedom.
- **The running is a straight line.** At one loop $1/\alpha_s$ is linear in $\ln\mu$, with slope $b_0/2\pi$. Every number in this article follows from that line.
- **The coupling is traded for a scale.** The classical theory has a dimensionless coupling and no scale; the quantum theory has a scale $\Lambda$ and no free dimensionless coupling. That trade is dimensional transmutation, and it is why QCD can predict dimensionless ratios absolutely and cannot predict its own overall scale.

**Why this article is not the renormalization-group article.** The group article derives the beta function in its general form, treats the scalar quartic coupling beside the gauge coupling, and finds the Wilson–Fisher and Banks–Zaks fixed points. This article does none of that. It takes the coefficient as given, solves the equation, and follows the solution to the numbers — $\alpha_s(M_Z)=0.1179$, $\Lambda_5=87$ MeV, the coupling at every scale from $1.5$ GeV to $10$ TeV — and then states where the truncation stops being trustworthy. The division of labour is deliberate and the two articles should be read in that order.

## The Coefficient and Its Three Contributions

**The equation.** With $\mu$ the renormalisation scale and $g_s$ the coupling of the QCD article,

$$
\beta_{g_s}=\mu\frac{dg_s}{d\mu}=-\frac{g_s^3}{16\pi^2}\,b_0 ,
\qquad
b_0=\frac{11}{3}C_A-\frac{4}{3}T_RN_f ,
$$

and in terms of $\alpha_s=g_s^2/4\pi$ the same statement is

$$
\mu\frac{d\alpha_s}{d\mu}=-\frac{b_0}{2\pi}\alpha_s^2 .
$$

The conversion between the two is one line of algebra and is worth stating because the two forms are both in circulation: $d\alpha_s/d\ln\mu=(g_s/2\pi)\beta_{g_s}$, and $(g_s/2\pi)\left(-b_0g_s^3/16\pi^2\right)=-b_0g_s^4/32\pi^3=-b_0\alpha_s^2/2\pi$.

**The three contributions, named.** The coefficient is a sum of three diagram classes, and the colour factors $C_A=3$ and $T_R=1/2$ were computed from explicit Gell-Mann matrices in the QCD article.

| Contribution | Colour factor | Its term in $b_0$ | At $N_c=3$ |
|---|---|---|---|
| Gluon and ghost loops, together | $C_A$ | $\tfrac{11}{3}C_A$ | $+11$ |
| Quark loop | $T_R$ per flavour | $-\tfrac43T_RN_f$ | $-\tfrac23N_f$ |

**Why the gauge sector is one line and not two.** The gluon loop and the ghost loop are separate diagrams with separate signs, and only their sum is $\tfrac{11}{3}C_A$. Writing "$+11$ from the gluon" is a shorthand for that sum, not for either diagram. The reason the pair is worth keeping together is that their signs are opposite and their sizes are differently distributed between the transverse and longitudinal parts of the gluon propagator: the longitudinal mode of a gauge field is not a physical degree of freedom, the ghost is what removes it, and what survives is a coefficient larger than any naive scalar count would suggest. The split is a calculation, it is performed in the general derivation that [the group article](the-renormalization-group-in-biquaternionic-form.html) transcribes, and it is not repeated here because no number in this article needs it. What every number here needs is the total, and the total is $\tfrac{11}{3}C_A$.

**The two ways of counting the quarks.** The corpus's group article writes the matter term as $-\tfrac23\sum_{\text{Weyl}}T(r)$, summing over Weyl fermions. The QCD article writes it as $-\tfrac43T_RN_f$, counting Dirac flavours. The two agree because one Dirac flavour is two Weyl fermions and each has $T=\tfrac12$:

$$
\frac23\sum_{\text{Weyl}}T(r)=\frac23\times2N_f\times\frac12=\frac23N_f ,
\qquad
\frac43T_RN_f=\frac43\times\frac12\times N_f=\frac23N_f .
$$

The agreement is exact but the two bookkeepings diverge the moment a theory has a Weyl fermion with no Dirac partner, which is the case in the electroweak theory, so it is worth knowing which one a formula is using.

**The coefficient at each $N_f$.**

| $N_f$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $15$ | $16$ | $17$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $b_0$ | $11$ | $10.33$ | $9.67$ | $9$ | $8.33$ | $7.67$ | $7$ | $1$ | $0.33$ | $-0.33$ |

**The value used in practice.** At the $Z$ pole five flavours are active, so $b_0=7.667$; below the bottom threshold $b_0=8.333$; below the charm threshold $b_0=9$. The number $\tfrac{11}{3}=3.667$ per gluon is what makes the coefficient large, and the $\tfrac23$ per quark is what erodes it.

## Why the Sign Is Negative

**The count.** The gluon's antiscreening carries weight $11$ and each quark's screening carries $-\tfrac23$. Six quarks remove four units, leaving seven. Asymptotic freedom is the statement $11>\tfrac23N_f$, and at $N_f=6$ the margin is a factor of nearly three.

**The physical picture, and what it is worth.** A colour charge placed in the vacuum polarises it: virtual $q\bar q$ pairs screen the charge the way a dielectric screens an electric charge, which is the QED behaviour and would make the coupling grow with distance. The gluon carries colour itself, so the virtual gluons are not a dielectric but a paramagnet, and their contribution has the opposite sign: the charge appears to *grow* as the probe approaches, so the coupling falls with increasing $Q$. That is the picture, and it is correct as far as it goes. It is worth less than the calculation: the picture explains the sign but not the size, and the size — $11$ against $\tfrac23$ per flavour — is the content. The word *antiscreening* names a result; it does not produce one.

**What the sign actually says.** In the ultraviolet, $g_s\to0$ and the partonic description becomes exact. In the infrared, $g_s$ grows without bound in perturbation theory and the expansion dies. Both halves matter, and only the first is under control: asymptotic freedom is a statement about short distances that is *derived*, and confinement is a statement about long distances that is *not* derived from the same information, even though it is the natural continuation of the same sign. This article is about the derived half.

**The contrast with QED, in one number.** For QED with one Dirac fermion $b_0=-\tfrac43$, so $1/\alpha$ *decreases* with energy: from $137.036$ at the electron mass to $128.1$ at $10^{15}$ GeV. The two signs differ because the adjoint Casimir is absent in the abelian case, and that is a group-theoretic fact about the gauge group, not about the algebra $\mathbb{B}$ or about the coordinates. The group article's table states all four cases side by side.

## The Solution

**The one-loop solution, in the form that is exact.** The equation separates:

$$
\frac{d}{d\ln\mu}\left(\frac{1}{\alpha_s}\right)=\frac{b_0}{2\pi}
\quad\Longrightarrow\quad
\frac{1}{\alpha_s(\mu)}=\frac{1}{\alpha_s(\mu_0)}+\frac{b_0}{2\pi}\ln\frac{\mu}{\mu_0} ,
$$

so that in $1/\alpha_s$ the running is a **straight line** in $\ln\mu$, and the line's slope is the coefficient divided by $2\pi$.

**The same solution in the form that is used.** Inverting,

$$
\alpha_s(\mu)=\frac{\alpha_s(\mu_0)}{1+\dfrac{b_0\alpha_s(\mu_0)}{2\pi}\ln\dfrac{\mu}{\mu_0}} ,
$$

and the two are the same function. The first is the one to quote when checking a number, because the arithmetic is linear; the second is the one to quote when explaining why the coupling is small at short distance.

**The slope, checked from the numbers.** Within a fixed $N_f$ the solution must be exactly straight, and it is: between $5$ GeV and $30$ GeV, where five flavours are active, the tabulated values below give

$$
\frac{1/\alpha_s(30\,\mathrm{GeV})-1/\alpha_s(5\,\mathrm{GeV})}{\ln(30/5)}=\frac{7.125-4.939}{1.792}=1.220 ,
$$

against $b_0/2\pi=7.667/6.283=1.220$. The agreement is not a coincidence and not a check of QCD; it is a check that the table was computed from the equation it claims. The straight line is the whole of the one-loop content, and everything else in this article is an evaluation of it.

## The Coupling at Every Scale

**The table.** Running down from $\alpha_s(M_Z)=0.1179$ with the flavour number changed at each threshold — $m_t=172.69$, $m_b=4.18$, $m_c=1.27$ GeV — and matching $\alpha_s$ continuously at each, which is the leading-order matching condition:

| $Q$ (GeV) | $N_f$ | $1/\alpha_s$, one loop | $\alpha_s$, one loop | $\alpha_s$, two loops |
|---|---|---|---|---|
| $1.5$ | $4$ | $3.361$ | $0.2975$ | $0.3403$ |
| $2$ | $4$ | $3.743$ | $0.2672$ | $0.2959$ |
| $3$ | $4$ | $4.280$ | $0.2336$ | $0.2507$ |
| $5$ | $5$ | $4.939$ | $0.2025$ | $0.2120$ |
| $10$ | $5$ | $5.785$ | $0.1729$ | $0.1776$ |
| $30$ | $5$ | $7.125$ | $0.1403$ | $0.1417$ |
| $91.19$ | $5$ | $8.482$ | $0.1179$ | $0.1179$ |
| $200$ | $6$ | $9.440$ | $0.1059$ | $0.1055$ |
| $1000$ | $6$ | $11.404$ | $0.0877$ | $0.0868$ |
| $10000$ | $6$ | $14.214$ | $0.0704$ | $0.0694$ |

**What the table shows and what it does not.** It shows the coupling falling by a factor of four between $1.5$ GeV and $10$ TeV, and it shows the one- and two-loop columns converging as the scale rises: the difference is ten per cent at $2$ GeV and one per cent at $30$ GeV. What it does not show is an observable. $\alpha_s$ is a parameter of a renormalisation scheme, not a number that any detector reads; the section *Where Perturbation Theory Dies* returns to this.

**The measured values.** The world average at the $Z$ pole is $\alpha_s(M_Z)=0.1179\pm0.0009$, and the same coupling extracted at other scales is consistent with it once the running is applied: about $0.30$ at $2$ GeV, $0.331\pm0.013$ at the $\tau$ mass, and $0.088$ at $1$ TeV from the one-loop line. The agreement across three orders of magnitude, from $\tau$ decays to the $Z$ pole to jet production at the LHC, is the strongest quantitative evidence that the coefficient is what the group theory says it is. That it is *evidence* rather than *proof* matters: a different coefficient would have produced a different set of numbers, but the numbers are fitted at one scale and predicted at all others, which is the structure of the test.

**Why the thresholds are not optional.** Using $N_f=3$ at all scales instead of four at $2$ GeV gives $0.332$ rather than $0.267$, an error of a quarter. The reason is that $b_0$ sits in the exponent-like denominator: a change of $\tfrac23$ in a coefficient of $8$ to $9$ is a few per cent, but it accumulates over the whole logarithm. A heavy quark that is kinematically absent must be removed from the running, and the removal is not a detail.

## Lambda and Dimensional Transmutation

**The trade.** The classical QCD Lagrangian has a dimensionless parameter $g_s$ and no dimensionful parameter other than the quark masses, which come from elsewhere. The quantum theory has a dimensionful parameter and no free dimensionless one. The mechanism is that the integration constant of the running equation carries a dimension:

$$
\Lambda=\mu_0\exp\left(-\frac{2\pi}{b_0\alpha_s(\mu_0)}\right) ,
$$

in terms of which the coupling is

$$
\alpha_s(\mu)=\frac{2\pi}{b_0\ln(\mu/\Lambda)} .
$$

**The formula is scale-invariant by construction, and that was checked.** Evaluating $\Lambda$ at three different scales with the one-loop solution gives the same number to five digits: $0.087311$ GeV from $\mu=91.19$, from $\mu=50$ and from $\mu=200$ GeV. The check is trivial algebra — $\ln\Lambda=\ln\mu_0-2\pi/(b_0\alpha_s(\mu_0))$ and the right side is $\mu$-independent because that is exactly what the running equation says — but it is the property that makes $\Lambda$ a parameter at all, and it is worth seeing.

**The numbers.**

| $N_f$ | $\Lambda$ (MeV) | Where it is defined |
|---|---|---|
| $6$ | $42$ | Above the top mass |
| $5$ | $87$ | Between $m_b$ and $m_t$ |
| $4$ | $119$ | Between $m_c$ and $m_b$ |
| $3$ | $142$ | Below $m_c$ |

The four values differ because $\Lambda$ is not one number but one number per flavour number: the same physics written with a different set of active quarks. What is invariant is the coupling at a given scale, and the matching condition is what ties the four together.

**The parameter count, stated once.** Classical QCD: $g_s$, dimensionless, plus the six quark masses. Quantum QCD: $\Lambda$, dimensionful, plus the six quark masses. The dimensionful parameter and the dimensionless one have swapped; the total count is unchanged, and the theory has lost the ability to be rescaled. That loss is what makes QCD predictive: with no dimensionless free parameter, every dimensionless ratio — the ratio of the proton mass to $\sqrt{\sigma}$ where $\sigma$ is the string tension, the ratio of the $\rho$ mass to the proton mass, the whole hadron spectrum in units of one of them — is a prediction of the theory rather than a fit.

**Where the scale comes from, and the honest answer.** Nothing in QCD fixes the value of $\Lambda$. It is $87$ MeV because the world is that way; a universe with a different $\Lambda$ would be a different world with the same equations. The number must come from outside — from whatever theory lies above the Planck scale, or from nothing at all — and this corpus has no candidate. That is not a defect of the derivation; it is the correct statement of what a dimensionally transmuted theory can and cannot say.

## What Lambda Is Not

**It is not a mass.** $\Lambda$ is defined by the truncation of a series, and it moves when the truncation changes. At one loop with five flavours it is $87$ MeV; at two loops the position of the pole in the solution moves by a factor of a few; in a different scheme it moves by a calculable constant. The number $87$ MeV should never be quoted as the mass of anything. The proton mass is $938$ MeV and is a different kind of object: it is a property of a solution, not of a subtraction.

**It is not scheme-independent.** For a change of scheme the relation is $\Lambda'=\Lambda\,e^{c/2b_0}$ with $c$ a scheme-dependent constant that is computable order by order, so $\Lambda$ is not an observable. What *is* scheme-independent is the first two coefficients of the beta function: $b_0$ and $b_1$ are the same in every mass-independent scheme, and the third coefficient is the first that depends on the scheme. This is why the article quotes $b_0$ without apology and quotes $\Lambda$ with a subscript.

**It is not well determined.** Differentiating the definition,

$$
\frac{\partial\ln\Lambda}{\partial\alpha_s}=-\frac{2\pi}{b_0\alpha_s^2}
=-59 ,
$$

so the uncertainty $\delta\alpha_s(M_Z)=0.0009$ becomes $\delta\Lambda/\Lambda=5.3$ per cent, about $\pm5$ MeV on $87$. A one per cent error in the coupling at the $Z$ pole is a five per cent error in the only scale of the strong interaction, and that amplification is the reason $\alpha_s(M_Z)$ is measured as hard as it is.

**It is not the vacuum energy, though it sits in the same place.** The natural size of the QCD vacuum energy density is $\Lambda^4\approx4\times10^{-4}$ GeV$^4$. That is $1.6\times10^{43}$ times the observed dark-energy density of $2.5\times10^{-47}$ GeV$^4$. The two numbers are computed from the same theory and differ by forty-three orders of magnitude; the discrepancy is the cosmological constant problem, and this article names it and does not solve it.

## Where Perturbation Theory Dies

**The expansion parameter.** The one-loop correction to any quantity is weighted by $\alpha_s b_0/2\pi$, which is $0.14$ at $M_Z$ and $0.35$ at $2$ GeV. The series is asymptotic: each order is smaller than the last until the terms start to grow again, and the smallest term is reached at an order of about $2\pi/(b_0\alpha_s)$, which is $7$ at $M_Z$ and $3$ at $2$ GeV.

**The failure, measured.** Comparing the two columns of the table is the measurement. At $1.5$ and at $2$ GeV the one-loop value is short of the two-loop value by thirteen and ten per cent, and the three-loop value moves again. The pattern at $2$ GeV is

| Order | $\alpha_s(2\,\mathrm{GeV})$ |
|---|---|
| One loop | $0.267$ |
| Two loops | $0.296$ |
| Measured | $\approx0.30$ |

The two-loop value lands within two per cent of the measured one and the one-loop value misses by eleven. That is a good outcome and it must be read correctly: it says the series is converging at $2$ GeV, not that two loops are exact.

**The scale at which the expansion dies.** Setting $\alpha_s=1$ in the solution with three flavours gives $\mu=285$ MeV; with five flavours, $198$ MeV. Below about $300$ MeV the coupling is of order one, every term of the series is as large as the last, and the perturbative description of the vacuum has nothing to say. The calculated value of $\alpha_s$ at $1$ GeV is $0.357$, which is already large enough that a two-loop number there should be quoted with a warning.

**What replaces it, and what does not.** Below that scale the relevant description is the lattice, where the coupling is defined at a finite lattice spacing and the continuum limit is taken; the hadron spectrum is computed there to per cent accuracy. What is *not* available is a derivation of confinement from the beta function. The running was derived; the area law was not. The next article in this series starts from the partonic description that asymptotic freedom licenses, and the one after that returns to the infrared from the other side.

**The discipline this imposes.** Because $\alpha_s$ is scheme-dependent and the series is asymptotic, no $\alpha_s$ determination is quoted here without a scale and a scheme, and no comparison between two determinations is made without running both to a common scale. A number like "$\alpha_s$ measured in $\tau$ decays" is shorthand for a scheme, an order, and a scale; the shorthand is universal in the literature and it is worth knowing that it is one.

## The Edge of the Theory

**The sign change.** $b_0$ vanishes between $N_f=16$ and $N_f=17$: at $N_f=16$ it is $\tfrac13$ and at $N_f=17$ it is $-\tfrac13$. So QCD with seventeen Dirac flavours is not asymptotically free — the coupling grows in the ultraviolet — and the boundary is exactly $N_f=\tfrac{33}{2}$. Six flavours is comfortably inside; fifteen is barely inside, with $b_0=1$.

**The window below the boundary.** For $N_f$ just below the critical value the two-loop coefficient is negative, and the two terms of the beta function balance at a fixed point. The group article computed the case $N_f=16$: $b_0=\tfrac13$, $b_1=-\tfrac{302}{3}$, and

$$
\alpha_s^*=\frac{g^{*2}}{4\pi}\approx0.0416 ,
$$

a fixed point small enough for perturbation theory to be meaningful. For $N_f$ between about $8$ and $16$ the theory is believed to be conformal in the infrared — the *conformal window* — and the fixed point moves to stronger coupling as $N_f$ falls, until perturbation theory loses control and the window's lower edge is a lattice question.

**Why this matters for the real theory.** The Standard Model has six flavours, all of which are active above the top mass, and $b_0=7$ there. The theory is therefore far from the edge, and the large margin is what allows perturbation theory to be useful over four orders of magnitude in energy. A world with thirteen light flavours would have been a qualitatively different place: the coupling would have run slowly, $b_0$ would have been $\tfrac13$, and the confinement scale would have sat exponentially close to the ultraviolet rather than five orders of magnitude below it.

**The abelian contrast, in the same language.** QED has $b_0=-\tfrac43$ and no adjoint contribution, so there is no window and no fixed point at one loop: $1/\alpha$ falls steadily and would reach zero at $\exp(3\pi/2\alpha)\approx10^{277}$ GeV. That scale is called the Landau pole and is far beyond any physics that is meant to be described by QED; the point of quoting it is the order of magnitude, not the number. The sign of the beta function decides whether a theory has an ultraviolet problem or an infrared one, and QCD has the second.

## Two Routes to One Number

**The test, stated as a computation.** The running is a one-parameter family, so any two scales determine each other. If the parameter is right, running up from a low-scale determination must reproduce the high-scale one. This was done in both directions.

**Downward.** From $\alpha_s(M_Z)=0.1179$, with the thresholds at $m_b$ and $m_c$, the one-loop line gives $\alpha_s(2\,\mathrm{GeV})=0.2672$. The measured value there is about $0.30$, so the one-loop prediction is eleven per cent low.

**Upward.** From $\alpha_s(2\,\mathrm{GeV})=0.30$, running up through four flavours to $m_b$ and five to the $Z$ pole gives

$$
\frac{1}{\alpha_s(M_Z)}=\frac{1}{0.30}+1.326\ln\frac{4.18}{2}+1.220\ln\frac{91.19}{4.18}=3.333+0.977+3.761=8.072 ,
$$

so $\alpha_s(M_Z)=0.1239$ against the measured $0.1179$ — five per cent high.

**What the two numbers mean together.** The two routes miss the measured value in the same direction and by comparable amounts, and the size of the miss is the size of the truncation error at $2$ GeV, not a discrepancy between two measurements. Upward, the error is diluted by the logarithm: an eleven per cent error at $2$ GeV becomes five per cent at $M_Z$, because the same absolute error in $1/\alpha_s$ is a smaller fraction of a larger $1/\alpha_s$. That dilution is why a low-scale determination is worth having and why it must be quoted with its scale.

**The consistency statement, in one line.** Two determinations of $\alpha_s$ at different scales, run to a common scale and compared, test the coefficient; two determinations at the same scale, compared, test the measurements. This article has done the first and has not done the second, and the reason is that the second requires cross sections.

## The Trace Anomaly and the Proton Mass

**Where the mass comes from.** For massless quarks the energy–momentum tensor has a nonzero trace, and the trace is the beta function:

$$
T^\mu_{\ \ \mu}=\frac{\beta_{g_s}}{2g_s}\sum_{a,\mu,\nu}G^a_{\mu\nu}G^a_{\mu\nu}=-\frac{b_0\alpha_s}{8\pi}\sum_{a,\mu,\nu}G^a_{\mu\nu}G^a_{\mu\nu} ,
$$

so that a scale-free classical theory acquires a mass scale in the quantum theory through the same coefficient that governs the running. The proton mass is the matrix element of that trace:

$$
m_p=\frac{1}{2m_p}\langle p|T^\mu_{\ \ \mu}|p\rangle .
$$

**The number, and what it denies.** Lattice QCD gives about one per cent of the nucleon mass from the light quark masses and the remaining ninety-nine per cent from the gluon field energy, that is from the anomaly. The proton is not made of quark masses; it is made of the energy of the colour field that binds them, and the coefficient that converts that energy into a mass is $b_0$. This is why the proton mass is of order $\Lambda$ and not of order the quark masses, and why the ratio $m_p/\Lambda_3=938/142=6.6$ is a number the lattice computes rather than a coincidence.

**Why this belongs in this article rather than the next.** The running and the mass gap are two readings of one coefficient. The next article takes the partonic description that asymptotic freedom licenses and computes cross sections in it; this one closes by noting that the same coefficient which makes the partons free at short distance is the one that makes the proton heavy at long distance.

## What the Group Article Already Did

**The division, stated plainly.** [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html) established: the Wilsonian effective action and its flow equation; the regulator and the momentum shell; the one-loop bubble and its $1/8\pi^2$; the beta functions of the quartic, abelian and non-abelian couplings with their signs; the adjoint Casimir checked for $SU(2)$ and $SU(3)$; the threshold $N_f\le16$ verified on $N_f=16$ and $N_f=17$; and both non-trivial fixed points with their stability. It also recorded the framework-specific obstruction: the regulator the algebra most naturally hosts is a sharp cutoff on the biquaternion norm, and that regulator breaks gauge invariance, while the regulator that preserves it — dimensional regularisation — is not a four-dimensional biquaternion object. The running of a non-abelian coupling therefore has to be computed in a scheme the algebra does not supply.

**What this article adds.** The coefficient written in the colour factors rather than in the Casimirs, with the ghost split out of the eleven; the Dirac–Weyl conversion; the solution of the equation rather than its coefficient; the threshold matching; the numbers at the scales where the coupling is measured, at one and at two loops; $\Lambda$ with its scheme, order and flavour dependence; the sensitivity of $\Lambda$ to $\alpha_s$; the scale at which the expansion dies; and the parameter-count statement that turns the running into a prediction.

**What neither article does.** Neither derives the beta function from the algebra, and neither claims to. The coefficient is a computation in quantum field theory with a gauge-invariant regulator, and the algebra's own regulator is not gauge invariant. That is the same boundary the QCD article marks for the group and the triplet, met from a different side.

## What the Framework Supplies

**The ledger.**

| Item | Status |
|---|---|
| The beta function and its one-loop coefficient | **Imported.** Standard theory; the group article's formula, used here |
| The colours factors $C_A=3$, $T_R=1/2$ | **Derived** in the QCD article from explicit matrices, given $N_c=3$ |
| $N_f\le16$ | **Derived** from the coefficient, given the particle content |
| The solution of the running equation | **Derived here**, by separation of variables |
| $\Lambda$ and dimensional transmutation | **Imported** in concept, **evaluated** here |
| The measured $\alpha_s(M_Z)$ | **Imported.** A measurement, not a computation |
| The sign rule $\sum_\mu X_\mu Y_\mu=-X_\mu Y^\mu$ | **Derived in the algebra**, in article 2; it affects no number here |
| A gauge-invariant regulator | **Not supplied.** The algebra's natural regulator breaks gauge invariance |
| The value of $\Lambda$ | **Not supplied by anything.** The theory's one scale is an input |

**The one place the algebra touches the running, and it is a negative result.** The biquaternion norm is the natural cutoff: it is a real central scalar, it commutes with the projections onto the material and informational sectors, and it is therefore a legitimate regulator. It is also not gauge invariant, because it does not commute with the gauge transformations that act on the octet. The corpus has no $\epsilon$-deformed biquaternion algebra, so dimensional regularisation — the regulator the calculation actually needs — has no home here. The honest statement is that the running is transcribed, and that the transcription is not a weakness of the algebra but a boundary of what the algebra was built to do.

## Summary

The strong coupling runs, and one coefficient decides how. $b_0=11-\tfrac23N_f$ is positive for every $N_f\le16$, it is the sum of $+11$ from the gluon and ghost loops and $-\tfrac23$ per quark flavour, and its positivity is asymptotic freedom. The two ways of counting the quark term — $-\tfrac23\sum_{\text{Weyl}}T(r)$ and $-\tfrac43T_RN_f$ — agree exactly, and both were written out.

At one loop $1/\alpha_s$ is a straight line in $\ln\mu$ with slope $b_0/2\pi$, verified from the article's own table at $1.220$ against $1.220$. Every number follows from that line: $\alpha_s$ falls from $0.2975$ at $1.5$ GeV to $0.0704$ at $10$ TeV, with the flavour number changed at each quark threshold, and the one- and two-loop values converge from ten per cent apart at $2$ GeV to one per cent at $30$ GeV.

The coupling is traded for a scale. $\Lambda_5=87$ MeV, $\Lambda_4=119$ MeV, $\Lambda_3=142$ MeV, $\Lambda_6=42$ MeV, computed from the same coupling at different flavour numbers; $\Lambda$ is scale-invariant by construction, which was checked to five digits at three scales. It is not a mass, not scheme-independent, and not well determined: $\delta\alpha_s=0.0009$ becomes $\delta\Lambda/\Lambda=5.3$ per cent.

The expansion dies below about $300$ MeV, where $\alpha_s=1$. At $2$ GeV the one-loop value is $0.267$, the two-loop value $0.296$, the measured value about $0.30$ — the series is converging there and the honest reading is convergence, not exactness.

The theory has an edge at $N_f=16.5$ and a conformal window below it; the Standard Model sits far inside, with $b_0=7$ at six flavours, and that margin is why perturbation theory works over four orders of magnitude. QED sits on the other side of the same sign with a Landau pole, and the difference is the adjoint Casimir.

Two readings of the one coefficient close the article: the same $b_0$ that makes the partons free at short distance gives the proton its mass at long distance, through the trace anomaly, with $m_p=938$ MeV of which about one per cent comes from quark masses and the rest from colour-field energy.

The framework supplies the sign rule and the colour factors and nothing else. The beta function is imported, the regulator is imported, and the value of $\Lambda$ is supplied by nothing at all.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha_s=g_s^2/4\pi$ | Strong coupling |
| $b_0$ | One-loop coefficient, $11-\tfrac23N_f$ |
| $b_1$ | Two-loop coefficient, $102-\tfrac{38}{3}N_f$ |
| $\beta_{g_s}=\mu\,dg_s/d\mu$ | Beta function of the coupling |
| $C_A=3$ | Quadratic Casimir of the adjoint, the gluon's colour charge |
| $T_R=1/2$ | Dynkin index of the triplet, the quark loop's normalisation |
| $N_f$ | Number of active quark flavours at the scale $\mu$ |
| $\mu$ | Renormalisation scale; $Q$ the kinematic scale of a process |
| $\Lambda$ | The strong-interaction scale, $\Lambda_{N_f}$ for $N_f$ flavours |
| $m_t$, $m_b$, $m_c$ | Thresholds $172.69$, $4.18$, $1.27$ GeV |
| $\alpha_s^*$ | Fixed-point coupling of the conformal window |

## Further Reading

- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html). The beta functions, the regulator question and the fixed points that this article uses without repeating.
- [The QCD Lagrangian: Colour, the Triplet, the Octet and the Feynman Rules](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html). The colour factors $C_A=3$ and $T_R=1/2$, computed from explicit Gell-Mann matrices, and the vertices the loops are built from.
- [The Gluon: An Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html). The adjoint representation and the embedded $\mathrm{SU}(3)$ elements.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The dimension bound behind the ledger's first row.
- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). Where $\alpha_s$ sits among the parameters, and at which scale.
- [Lattice Gauge Theory and the Biquaternion Path Integral](lattice-gauge-theory-and-the-biquaternion-path-integral.html). The description that takes over below $300$ MeV.
- [Quantum Chromodynamics under the Biquaternion Framework: A Research Agenda](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html). The classification that the ledger follows.
