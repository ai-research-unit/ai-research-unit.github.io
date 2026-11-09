# __The Parton Model and Deep Inelastic Scattering__

## Introduction

**The standing of this article.** Everything quantitative below is standard theory, written in the corpus's coordinates and notation. It is **standard input**, not a framework result.

**The one thing that is different about this article.** Elsewhere in this series the corpus imports *numbers*: the coupling at one scale, the value of $N_c$, the mass of the top. Here it imports *functions*. The parton densities $q(x,Q^2)$ and $g(x,Q^2)$ are not parameters of any Lagrangian and are not computable in perturbation theory; they are non-perturbative functions of one variable, and they are obtained by fitting data. That is a different kind of import, and it is the honest characterisation of the parton model: it is a factorisation statement, not a theory of the proton. [The article on confinement](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) already established that the partonic description is not a description of a hadron but a description at a resolution; this article works out what that description can predict once the resolution is fixed.

**The claim.** Deep inelastic scattering measures two dimensionless functions of two variables, and the whole of the parton model is the statement that at large $Q^2$ those two functions collapse to functions of one variable, which are sums of parton densities weighted by charge squared.

$$
F_2(x,Q^2)\;\longrightarrow\;\sum_f e_f^2\,x\left[q_f(x)+\bar q_f(x)\right] .
$$

Four things follow, and they organise the article.

- **Two structure functions reduce to one relation.** $F_2=2xF_1$ for spin-$\tfrac12$ constituents, and the derivation is three lines of Dirac trace. It is violated in proportion to how far the constituents depart from being massless, on-shell spin-$\tfrac12$ — by their transverse momentum and by the gluon's longitudinal coupling — and the measured violation is small.
- **The one-variable functions are densities.** They obey sum rules: momentum, baryon number, and the Gottfried relation. Two of the three hold; the third fails, and the failure is a measurement of $\bar d-\bar u$.
- **The residual two-variable dependence is the running coupling.** The breaking of scaling is not a new interaction. It is $\alpha_s(Q^2)$ appearing where the naive model put zero, and its coefficient is a computable anomalous dimension.
- **One sum rule measures the coupling directly.** The Gross–Llewellyn Smith sum rule is the cleanest instance in the whole of QCD where an integral over data returns $\alpha_s$.

**The order.** Kinematics, then the tensor decomposition, then scaling, then the parton model, then the spin relation and its violation, then the densities, then the sum rules and their two verdicts, then the gluon, then scaling violations with the anomalous dimensions computed and checked, then the coupling from the sum rule, then factorisation and the ledger.

## Kinematics: What Is Measured

**The metric, stated once.** $g_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)$ throughout, so a spacelike exchange has $q^2=-Q^2<0$ and the transverse projector below is the one this signature gives. No vertex is computed in this article, so the incoming-momentum convention of [the QCD article](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html) does not enter; where a trace is taken, it is the Dirac trace of a massless line and carries no sign ambiguity.

**The process and the variables.** An electron of momentum $k_\Phi$ scatters off a proton of momentum $p$ and emerges with momentum $k'$. The exchanged photon (or $Z$) carries

$$
q=k-k' ,
\qquad
Q^2=-q^2>0 ,
\qquad
\nu=\frac{p\cdot q}{M} ,
\qquad
x=\frac{Q^2}{2\,p\cdot q}=\frac{Q^2}{2M\nu} ,
\qquad
y=\frac{p\cdot q}{p\cdot k} .
$$

Two of these are independent. The pair $(x,Q^2)$ is the conventional choice; $(x,y)$ is the experimental one, since $y$ is the fractional energy loss of the lepton, and

$$
Q^2=s\,x\,y ,
$$

with $s$ the lepton–proton centre-of-mass energy squared: $s=2ME$ for a fixed target, with $M$ the proton mass and $E$ the beam energy, and $s=4E_eE_p$ for a collider. The fixed-target form is therefore $Q^2=2MExy$, and it is the one to use below only when the target is at rest. The relation is worth keeping in mind because it is why a fixed-$x$ scan is a scan in $y$: raising $Q^2$ at fixed $x$ means raising the energy loss, and the kinematic ceiling is $y\le1$, hence $Q^2\le sx$ — the collider number in the next paragraph, not the fixed-target one, and the two differ by the factor $2E_p/M$.

**Why $x$ is a fraction of null momentum.** Write the momenta in light-cone components, $p^\pm=(p^0\pm p^3)/\sqrt2$. A boost along the collision axis sends $p^+\to\lambda p^+$, $p^-\to\lambda^{-1}p^-$, and leaves $p\cdot q=p^+q^-+p^-q^+-\vec p_\perp\!\cdot\vec q_\perp$ unchanged. So $Q^2$ and the denominator $2p\cdot q$, and therefore $x$, are **invariant under the collinear boost**: $x$ does not care how fast the proton moves along the beam. That is the formal reason the parton picture is frame-independent, and the statement the parton model needs is that in a frame where $p^+$ is large, the struck parton carries a fraction $x$ of it,

$$
k^+=x\,p^+ ,
\qquad\text{with}\qquad k^2\approx0 ,
$$

so that $(k+q)^2=0$ reads $2xp\cdot q=Q^2$, which is the definition of $x$. The variable is not a bookkeeping device; it is the fraction of null momentum, and the elastic condition on a massless constituent fixes it uniquely.

**The measured range.** At HERA, $E_e=27.5$ GeV against $E_p=920$ GeV gives $s=4E_eE_p=1.01\times10^5$ GeV$^2$, that is $\sqrt s=318$ GeV, and the reach is $Q^2$ up to $s$ and $x$ down to $Q^2/s\approx10^{-5}$ at $Q^2=1$ GeV$^2$. The range matters: the small-$x$ region is where the gluon dominates and where the rise of $F_2$ is seen, and it is a region that only a collider reaches.

## The Hadronic Tensor and the Two Structure Functions

**The cross section factorises into a lepton tensor and a hadron tensor.** With $L_{\mu\nu}=2\left(k_\mu k'_\nu+k_\nu k'_\mu-g_{\mu\nu}k\cdot k'\right)$ for an unpolarised lepton, the cross section is the contraction of $L$ with $W$, and carrying out the contraction leaves two independent coefficients:

$$
\frac{d^2\sigma}{dx\,dQ^2}=\frac{4\pi\alpha^2}{xQ^4}\left[\left(1-y-\frac{M^2x^2y^2}{Q^2}\right)F_2(x,Q^2)+y^2x\,F_1(x,Q^2)\right] ,
$$

and the two coefficients are what the experiment separates. The combination in brackets is the reason a measurement at one $y$ cannot give both functions: two energies are needed, and that is why the Rosenbluth separation exists in elastic scattering and its analogue in deep inelastic scattering is a scan in $y$.

**The tensor decomposition.** Lorentz invariance and parity fix the hadronic tensor to two independent structures for an unpolarised target:

$$
W_{\mu\nu}=-W_1\left(g_{\mu\nu}-\frac{q_\mu q_\nu}{q^2}\right)+\frac{W_2}{M^2}\left(p_\mu-\frac{p\cdot q}{q^2}q_\mu\right)\left(p_\nu-\frac{p\cdot q}{q^2}q_\nu\right) ,
$$

with the two scalar functions $W_1$ and $W_2$. The reason there are exactly two is a count: the available vectors are $p$ and $q$, the metric is one more tensor, and the antisymmetric $\epsilon$ is excluded by parity for an unpolarised target. Two structures, two functions, and no more.

**The dimensionless versions.**

$$
F_1(x,Q^2)=M\,W_1 ,
\qquad
F_2(x,Q^2)=\nu\,W_2 ,
$$

and the factors of $M$ and $\nu$ are chosen so that both are dimensionless and, in the scaling limit, functions of $x$ alone. A third function $F_3$ exists and is measured with neutrinos; it is parity-odd and requires a weak exchange, which is [the neutral-current article's](the-weinberg-angle-the-neutral-current-and-the-z-coupling.html) territory rather than this one's.

## Bjorken Scaling

**The statement.** In the limit $Q^2\to\infty$ with $x$ fixed,

$$
F_1(x,Q^2)\to F_1(x) ,
\qquad
F_2(x,Q^2)\to F_2(x) ,
$$

with no residual $Q^2$ dependence at all. This is Bjorken scaling, and its content is that the probe resolves *pointlike, non-interacting* constituents: if the constituents were extended objects with a form factor, $F_2$ would fall with $Q^2$ the way the elastic form factor does, and if they interacted during the collision the impulse approximation would fail and the $Q^2$ dependence would be strong.

**The measured statement, stated carefully.** Scaling holds to within about ten per cent over the range $2\lesssim Q^2\lesssim 20$ GeV$^2$, and beyond that the deviation is resolved rather than absent — it grows, but it grows logarithmically. The word *logarithmically* is the whole of the next-to-last section: the violations are not power-law, they are slow, and a slow violation is the signature of a dimensionless coupling that runs rather than of a length scale that is being resolved.

**Why scaling is a statement about dimension counting and not about dynamics.** If the constituents are pointlike and free, the only scale in the problem is $Q$, so a dimensionless cross section can depend on $Q^2$ only through the ratio $Q^2/\mu^2$ with $\mu$ any other scale; with no other scale, there is nothing to form a ratio with, and the cross section must be $Q^2$-independent. The argument is dimensional analysis, and it is why scaling's failure *is* the discovery of a scale: the violations measure $\Lambda_{\mathrm{QCD}}$ in the same way that a form factor measures a radius.

## The Parton Model: The Impulse Approximation

**The three assumptions, named.** The parton model is not a theory; it is a truncation, and its content is three separate assumptions.

| Assumption | What it says | What it costs |
|---|---|---|
| Infinite momentum frame | A frame exists in which the proton's partons are frozen over the collision time | Corrections of order $M^2/Q^2$ |
| Impulse approximation | The struck parton is free during the hard collision | Corrections of order $\alpha_s$; these are the scaling violations |
| Coherence | The partons are incoherent, so probabilities add and amplitudes do not | Corrections of order $\alpha_s$; the same ones |

**The cross section as a convolution.** With $f_i(\xi)$ the probability density for parton $i$ to carry fraction $\xi$,

$$
F_2(x,Q^2)=\sum_i e_i^2\,x\,f_i(x)\quad\text{at leading order,}
$$

and the reason the struck parton's fraction equals $x$ is the elastic condition computed above: only a parton with $\xi=x$ can absorb the photon and remain on shell. The delta function $\delta(\xi-x)$ that the convolution would carry is what collapses the integral to a point, and that collapse is the origin of scaling.

**What the model predicts and what it does not.** It predicts the *shape* of $F_2$ in $x$ only in the sense of being consistent with any shape; it predicts the *relations* between different processes, which is where its power lies. Neutrino and antineutrino scattering, the $W$ asymmetry, the Drell–Yan cross section and the $Z$ pole all use the same densities, and the consistency of all of them with one set of functions is the evidence that the densities are real objects rather than fit parameters.

## Callan–Gross, Derived in Three Lines

**The partonic tensor.** For a massless spin-$\tfrac12$ parton of charge $e$ and momentum $k_\Phi$,

$$
W^{(0)}_{\mu\nu}=e^2\,\delta\!\left((k+q)^2\right)\mathrm{Tr}\!\left[\not k\,\gamma_\mu(\not k+\not q)\gamma_\nu\right] ,
$$

up to an overall constant. The trace is standard,

$$
\mathrm{Tr}\!\left[\not k\,\gamma_\mu\not l\,\gamma_\nu\right]=4\left[k_\mu l_\nu+k_\nu l_\mu-g_{\mu\nu}\,k\cdot l\right] ,
\qquad
l=k+q .
$$

**The three lines.** Contract with $q^\mu$, and use $k^2=l^2=0$ together with $l=k+q$:

$$
q\cdot k=\frac{l^2-k^2-q^2}{2}=\frac{Q^2}{2} ,
\qquad
q\cdot l=\frac{l^2+q^2-k^2}{2}=-\frac{Q^2}{2} ,
\qquad
k\cdot l=k\cdot q=\frac{Q^2}{2} ,
$$

so that

$$
q^\mu W^{(0)}_{\mu\nu}\propto 4\left[\frac{Q^2}{2}l_\nu-\frac{Q^2}{2}k_\nu-\frac{Q^2}{2}q_\nu\right]=\frac{4Q^2}{2}\left[l_\nu-k_\nu-q_\nu\right]=0 .
$$

**What the vanishing means.** The partonic tensor is transverse to $q$, so it contains no longitudinal structure, so the coefficient of the $q$-longitudinal projector vanishes, so the longitudinal structure function vanishes, $F_L=0$ — which is

$$
F_2(x)=2xF_1(x) ,
$$

the Callan–Gross relation. It is not an extra assumption about the proton. It is the Dirac trace of a massless spin-$\tfrac12$ line, and it holds whenever the struck object has spin $\tfrac12$, is massless, and is on shell. The relation is between the $F$'s and not between the $W$'s: with $F_1=MW_1$ and $F_2=\nu W_2$ as defined above, $F_2=2xF_1$ is $W_2=(2xM/\nu)W_1$, so the frequently quoted $W_2=2xW_1$ is the same relation in a different normalisation of $W$, not another one.

**The contrast with spin zero, which is the reason the relation is a spin measurement.** For a scalar constituent the electromagnetic vertex is $(2k+q)_\mu$ and the tensor is proportional to $(2k+q)_\mu(2k+q)_\nu$. That tensor has no transverse part at all — $W_1=0$ and $W_2\neq0$ — so $F_1=0$ and the Callan–Gross relation fails maximally. A measurement of the ratio of the two structure functions is therefore a measurement of the constituents' spin, and the fact that $2xF_1/F_2$ comes out one, where a scalar constituent would give zero, is the discovery that the charged constituents of the proton have spin $\tfrac12$.

## R, and What Its Nonzero Value Says

**The ratio.** The longitudinal-to-transverse ratio is

$$
R=\frac{\sigma_L}{\sigma_T}=\frac{F_2\left(1+\dfrac{4M^2x^2}{Q^2}\right)-2xF_1}{2xF_1} ,
$$

and the Callan–Gross relation is $R=0$. The kinematic factor $4M^2x^2/Q^2$ is the target-mass correction and is negligible over most of the measured range.

**The measurement.** $R$ is not zero. It is about $0.18$ at $Q^2\sim5$ GeV$^2$, roughly flat in $x$ up to $x\approx0.5$, rising beyond that where the higher-twist terms take over, and falling at fixed $x$ as $Q^2$ rises — which is the direction the $\alpha_s$ origin of the deviation predicts. The size is the content, and the two limits are not $0$ and $1$ but $0$ and $\infty$: $R=0$ is a massless on-shell spin-$\tfrac12$ constituent, and $R\to\infty$ is a scalar, because a scalar constituent has no transverse coupling at all and $\sigma_T$ vanishes rather than merely shrinking. A value of $0.18$ therefore says the spin-$\tfrac12$ picture is right and the deviation is a correction, and it says it without needing an upper end to compare against.

**Where the deviation comes from.** Two sources, and they are of different kinds. The first is order $\alpha_s$: a gluon in the proton can be resolved by the photon through $g\to q\bar q$, and the longitudinal part of that splitting is nonzero, so $R$ acquires a term proportional to $\alpha_s$ times the gluon density. The second is a power correction and not an $\alpha_s$ effect: the quarks' intrinsic transverse momentum gives the struck quark a virtuality of order $k_T^2/Q^2$, which breaks the on-shell condition the Callan–Gross derivation used. The first dominates at small $x$, the second at large $x$, and the fact that $R$ stays small is the quantitative statement that both are corrections rather than the leading description.

## The Parton Densities

**The definitions.** For each flavour,

$$
q_f(x,Q^2)\,\text{and}\, \bar q_f(x,Q^2) ,
\qquad
g(x,Q^2) ,
$$

with $q_f(x)dx$ the number of quarks of flavour $f$ carrying a fraction between $x$ and $x+dx$. Six flavours and the gluon, at a scale, and the scale is part of the definition: a density without a $Q^2$ is not a density.

**What is known and what is fitted.** The densities are not predicted. They are parameterised at a low scale — typically a form like $x^{a}(1-x)^{b}(1+c\sqrt x)$ with a normalisation — and the parameters are fitted to several thousand data points spanning many processes, then evolved to other scales with the equations of the next-to-last section. The procedure is the opposite of a derivation: the theory supplies the evolution, the data supply the input, and the fit is where the two meet.

**The gross shape, and why the shape is not arbitrary.** At $Q^2\sim$ few GeV$^2$ the valence distributions peak around $x\approx0.15$ and fall at both ends, for two different reasons: $x\to1$ because a single quark cannot carry all the momentum without the others being absent, which is kinematics, and $x\to0$ as a power of $x$ that the data fit and the theory does not predict, which is where the coherent part of the proton's wave function lives. The sea is concentrated at small $x$ and rises as $x$ falls. The gluon is concentrated at small $x$ more strongly than the sea. Those three statements are qualitative, they are what any sensible parameterisation must reproduce, and they are the whole of what can be said without data.

## The Sum Rules

**Three integrals, two verdicts.** Each sum rule is an exact statement of the parton model; two of the three are tests, and the third is a constraint imposed on the fit.

| Sum rule | Statement | Status |
|---|---|---|
| Momentum | $\displaystyle\int_0^1 x\Big[\sum_f\left(q_f+\bar q_f\right)+g\Big]dx=1$ | Holds, by construction of the fit |
| Baryon number | $\displaystyle\int_0^1\left(u-\bar u\right)dx=2,\quad \int_0^1\left(d-\bar d\right)dx=1$ | Holds to the accuracy of the fit |
| Gottfried | $\displaystyle\int_0^1\frac{dx}{x}\left(F_2^{p}-F_2^{n}\right)=\frac13$ | **Fails**: $0.235\pm0.026$ |

**The momentum sum rule is the one that is not a test.** It says that the momentum fractions add to one, and it is imposed on the fit rather than checked by it. What it does is fix the gluon's normalisation once the quark densities are known, which is why the gluon density at a low scale is determined indirectly: no leading-order process measures it directly, and the momentum sum rule is what pins it down.

**The Gottfried sum rule, and its failure.** In the naive parton model

$$
\int_0^1\frac{dx}{x}\left(F_2^{p}-F_2^{n}\right)=\frac13+\frac23\int_0^1\left(\bar u-\bar d\right)dx ,
$$

which equals $\tfrac13$ if the sea is flavour-symmetric, $\bar u=\bar d$. The measured value is $S_G=0.235\pm0.026$, so

$$
\int_0^1\left(\bar u-\bar d\right)dx=\frac32\left(S_G-\frac13\right)=-0.147\pm0.039 ,
$$

that is, there is an excess of $\bar d$ over $\bar u$ of about $0.147$. This is a real result and not a failure of QCD: the asymmetry is what pion cloud models predict, since the proton can emit a $\pi^+$ (giving $\bar d$) more readily than a $\pi^-$ (giving $\bar u$). What fails is the *assumption* that the sea is symmetric, and the sum rule is the measurement that assumption was never entitled to.

**What a failed sum rule is worth.** The Gottfried failure is the most useful kind of negative result: it does not weaken the framework, it measures a quantity the framework had assumed away. The article states it rather than quoting only the two sum rules that hold, because a list of confirmed predictions is not evidence unless the unconfirmed ones are listed beside them.

## The Gluon, Which the Photon Does Not See at Leading Order

**The problem.** The photon couples to charge, and the gluon carries none. So the gluon density enters no leading-order expression for $F_1$ or $F_2$ — the two structure functions at leading order in $\alpha_s$ are sums over charged constituents only — and yet the gluon carries about half the proton's momentum at $Q^2\sim$ few GeV$^2$. The qualification is not a quibble: $F_L$ is zero at zeroth order in $\alpha_s$ and is generated entirely by $g\to q\bar q$, which is the third route below. The gluon is the largest single component of the proton and is invisible to the cleanest probe of the proton's structure.

**The three ways it is reached.** Through the momentum sum rule, which fixes its normalisation. Through the scaling violations, since $\partial F_2/\partial\ln Q^2$ at small $x$ is dominated by $g\to q\bar q$ and is therefore proportional to the gluon density. And through processes where it couples at tree level: dijet and photon-plus-jet production in the hadron collider, and the longitudinal structure function $F_L$.

**Why this belongs in this article.** The gluon's invisibility at leading order is the sharpest example of a general point: a density is defined by the operator that measures it, and different processes measure different combinations. The parton model's power is that finitely many densities, measured in finitely many processes, describe infinitely many cross sections; the price is that some densities require indirect routes.

## Scaling Violations as the Running Coupling

**The equation.** At leading order the non-singlet density evolves by

$$
\frac{\partial q(x,Q^2)}{\partial\ln Q^2}=\frac{\alpha_s(Q^2)}{2\pi}\int_x^1\frac{dz}{z}\,P_{qq}(z)\,q\!\left(\frac{x}{z},Q^2\right) ,
\qquad
P_{qq}(z)=C_F\left(\frac{1+z^2}{1-z}\right)_+ ,
$$

which is the Dokshitzer–Gribov–Lipatov–Altarelli–Parisi equation for the quark-to-quark splitting, with $C_F=\tfrac43$ from [the QCD article](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html). The plus prescription is written here in the form that subtracts the value at $z=1$, so that $\int_0^1[g(z)]_+dz=0$ for any $g$; many texts carry an extra $+\tfrac32\delta(1-z)$ together with a subtraction defined differently. The two writings are the same distribution and give the same moments — the delta term is what the different subtraction supplies back — so they are a convention and not a choice of physics. What the test below decides is whether a written form is internally consistent: $A_1=0$ must come out, quark number does not run, and a formula that gives $A_1\neq0$ has the delta term and the subtraction mismatched.

**Its content in one sentence.** The right side is the statement that a quark which carried fraction $x/z$ can be found at fraction $x$ after radiating a gluon that took away fraction $1-z$, and the plus prescription is the statement that the radiation is a *loss*: the virtual term is what keeps the quark number fixed while moving the momentum.

**The moments, which are exact.** Define $q_n=\int_0^1x^{n-1}q(x)dx$. Multiplying the equation by $x^{n-1}$ and integrating (with $x=zy$ in the convolution) turns it into an ordinary differential equation,

$$
\frac{dq_n}{d\ln Q^2}=\frac{\alpha_s}{2\pi}\,A_n\,q_n ,
\qquad
A_n=\int_0^1dz\,z^{n-1}P_{qq}(z)=C_F\int_0^1dz\,\frac{1+z^2}{1-z}\left(z^{n-1}-1\right).
$$

The integral is elementary because $\frac{1+z^2}{1-z}=-(1+z)+\frac{2}{1-z}$, and the result is

$$
\boxed{\;A_n=C_F\left[\frac32-\frac1n-\frac1{n+1}-2\sum_{j=1}^{n-1}\frac1j\right]\;}
$$

with the empty sum at $n=1$ taken as zero.

**This formula was checked against direct quadrature.** Evaluating the integral numerically with four million points and the integrand $(z^{n-1}-1)(1+z^2)/(1-z)$, which is finite at $z=1$, reproduces the closed form for $n=1,\dots,7$ to within $5\times10^{-6}$ in absolute value, the residual growing slowly with $n$ — $1\times10^{-6}$ at $n=2$, $4\times10^{-6}$ at $n=7$ — which is the quadrature error of the near-singular integrand rather than a discrepancy.

**Two of its values carry the physics.**

$$
A_1=0\qquad\text{exactly, because}\qquad \frac32-1-\frac12-0=0 ,
$$

which is **quark number conservation**: the $n=1$ moment is the integral of the density, and it does not run. This is not an accident of the arithmetic; it is the statement that the plus prescription was built to conserve the number, and the formula reproduces that construction. And

$$
A_2=C_F\left[\frac32-\frac12-\frac13-2\right]=\frac43\times\left(-\frac43\right)=-\frac{16}{9}=-1.7778 ,
$$

which governs how fast the quarks' momentum fraction falls — the quark half of the momentum sum, whose full coefficient requires the gluon entry $P_{gq}$ as well. That $A_2$ is negative is the statement that a quark *loses* momentum to its own radiation; that $A_1$ vanishes and $A_2$ does not is the statement that the loss is a redistribution and not a disappearance.

**The solution, and the exponent that measures the coupling.** Solving the two equations together,

$$
q_n(Q^2)=q_n(Q_0^2)\left[\frac{\alpha_s(Q^2)}{\alpha_s(Q_0^2)}\right]^{d_n} ,
\qquad
d_n=-\frac{A_n}{b_0} ,
$$

with $b_0$ the coefficient of [the running article](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). So the violation of scaling is not a new effect with a new parameter: it is $\alpha_s$ appearing in a power, and the power is a number the splitting function computes.

**The numbers, with $N_f=4$ held fixed across the interval.**

| $n$ | $A_n$ | $d_n$ | $q_n$ change, $2\to20$ GeV$^2$ | $q_n$ change, $2\to100$ GeV$^2$ |
|---|---|---|---|---|
| $1$ | $0$ | $0$ | $0.0\%$ | $0.0\%$ |
| $2$ | $-1.7778$ | $0.2133$ | $-12.0\%$ | $-16.9\%$ |
| $3$ | $-2.7778$ | $0.3333$ | $-18.0\%$ | $-25.2\%$ |
| $4$ | $-3.4889$ | $0.4187$ | $-22.1\%$ | $-30.5\%$ |

Two of the exponents are exact rationals, and it is worth seeing them: $d_2=\tfrac{16}{75}$ and $d_3=\tfrac13$, both following from $A_2=-\tfrac{16}{9}$, $A_3=-\tfrac{25}{9}$ and $b_0=\tfrac{25}{3}$ at four flavours. The changes are computed from the one-loop coupling with $N_f=4$ held across the interval so that the comparison tests the exponent and not the threshold bookkeeping; changing $b_0$ at each threshold moves them by a few per cent.

**What the table says, and it says something a table of $F_2$ would not.** Every moment falls, and the higher moments fall faster. A distribution whose high moments fall faster than its low ones is a distribution whose large-$x$ region is being depleted and whose small-$x$ region is being filled: $x^n$ weights large $x$ more heavily as $n$ grows, so a faster fall at large $n$ is a faster loss where $x$ is large. That is the softening of the parton distribution, and it follows from the monotonicity of $A_n$ in $n$ alone, with no further computation.

**The singlet, which this section has avoided.** The measured $F_2$ does not fall at small $x$; it *rises*, by a large factor over the HERA range. That rise is not in the table, and the reason is that the table is the non-singlet sector. The full evolution mixes the quark singlet with the gluon, the mixing matrix has a positive eigenvalue, and the $g\to q\bar q$ feed at small $x$ beats the quark's own loss. The article states the mixing and does not compute it: the two-by-two matrix and its eigenvectors are a separate calculation, and the qualitative claim that the small-$x$ rise is a gluon effect is what the data actually establishes.

## The One Sum Rule That Measures the Coupling

**Gross–Llewellyn Smith.** For neutrino and antineutrino scattering on an isoscalar target, the first moment of the parity-odd structure function is predicted to all orders:

$$
\int_0^1F_3^{\nu N}(x,Q^2)\,dx=3\left[1-\frac{\alpha_s}{\pi}-c_2\left(\frac{\alpha_s}{\pi}\right)^2-\dots\right] ,
$$

with $N$ the isoscalar nucleon, and with the leading correction fixed and computable. The moment is of one structure function and not of the neutrino-plus-antineutrino sum: charge conjugation on an isoscalar target gives $F_3^{\bar\nu N}=F_3^{\nu N}$, so either measures the same number and adding them would double the right side against a measurement of $2.50$. The superscript is $N$ and not $p$: the measured target is isoscalar, and it is charge symmetry that lets the proton and neutron densities be combined into one object, so writing the moment for a proton target and the measurement for an isoscalar one would compare two different sums. The prefactor three is the number of valence quarks, that is $N_c$ read as a baryon number, and the correction is the same $\alpha_s$ that runs.

**The arithmetic, and the first thing it gets wrong if the scale is not matched.** The measured datum is the CCFR first moment, quoted at $Q^2=3$ GeV$^2$ — that is $Q=1.73$ GeV, not $3$ GeV, and the distinction is worth one sentence because the coupling moves by twenty per cent between the two. Interpolating [the running article's](asymptotic-freedom-and-the-running-of-the-strong-coupling.html) one-loop line between its $1.5$ and $2$ GeV entries gives $\alpha_s\approx0.28$ there, and the one-loop prediction is

$$
3\left(1-\frac{0.28}{\pi}\right)=3(1-0.0891)=2.733 ,
$$

against a measured $2.50\pm0.08$. The gap is $0.23$, and the one-loop term itself is $3\times0.0891=0.267$: it covers fifty-four per cent of the distance from $3$, not all of it and not a fixed fraction of the residual.

**The two-loop coefficient is known, and it does not close the gap.** $c_2=\tfrac{55}{12}-\tfrac13N_f=3.25$ at four flavours, positive and of order one. Including it,

$$
3\left(1-0.0891-3.25\times0.00794\right)=2.66 ,
$$

moves the prediction by a further sixteen per cent of the distance — $0.078$ of the $0.50$ — and leaves $0.16$ unexplained. Closing the gap with a coefficient of this shape would need $c_2\approx9.8$, three times the calculated value; so the residual is not a coefficient deficiency and cannot be argued away as one.

**What the residual is.** The $F_3$ moments are measured down to $Q^2\approx1.3$ GeV$^2$ and extrapolated to $x=1$, and at those scales the target-mass and higher-twist corrections — of order $M^2/Q^2$ and $\Lambda_{\mathrm{QCD}}^2/Q^2$ — are not small. The comparison above includes none of them, which is why it is a demonstration of the size of the truncation and not a determination. The controlled extraction is a global next-to-next-to-leading-order fit to the same data, and it returns $\alpha_s(M_Z)=0.119\pm0.005$, consistent with the $Z$-pole value of $0.1179$ of the running article.

**Why this is the cleanest coupling determination.** The first moment is protected against the parton densities: whatever the densities are, their integral is fixed by the valence count, so the sum rule has no density uncertainty. What is left is the coefficient, which is a pure perturbative calculation. Every other determination convolves a hard coefficient with densities that must be fitted; this one does not, and that is why it is quoted as a test of the coupling rather than a test of the densities.

## Factorisation and the Two Scales

**The theorem, stated and not proved.** The cross section factorises:

$$
F_2(x,Q^2)=\sum_i C_i\!\left(x,\frac{Q^2}{\mu_F^2},\alpha_s(\mu_R)\right)\otimes f_i\!\left(x,\mu_F^2\right) ,
$$

a convolution of a hard coefficient, computable in perturbation theory, with a density, which is not. The two scales $\mu_R$ and $\mu_F$ are the renormalisation and factorisation scales, both arbitrary, and the statement of the theorem is that the dependence cancels order by order.

**Why two scales and not one.** $\mu_R$ is where $\alpha_s$ is evaluated; $\mu_F$ is where the density is defined, that is, the boundary between "short distance, computed" and "long distance, fitted". They are conceptually distinct and are often set equal by convenience. The residual dependence on either, at a finite order, is the truncation error, and it is the reason every extracted $\alpha_s$ carries a scale as part of its specification — the same discipline [the running article](asymptotic-freedom-and-the-running-of-the-strong-coupling.html) imposes on $\alpha_s$ determinations at different scales.

**The scheme, in one line.** Changing the scheme moves a finite piece from the coefficient into the density, and leaves the product unchanged. So the densities are scheme-dependent objects, like $\Lambda$, and for the same reason: they are defined by a subtraction, not by a measurement.

**What factorisation does not say.** It does not say the densities exist as probability densities in a frame-independent sense — that reading is the parton model's extra assumption, valid at leading order and in the infinite-momentum frame. It does not apply to the whole cross section: hadrons in the final state, and the region where two hard scales compete, need generalised versions. And it is a theorem about the leading power in $1/Q^2$, with the corrections being the higher-twist terms this article does not compute.

## What the Framework Supplies

**Three things, and two of them are negative.**

**One: the null direction exists in the algebra.** The whole construction rests on a light-cone decomposition, and a light-cone decomposition rests on a null direction. In $\mathbb{B}$ the null objects are the nilpotent elements, $\vec\Upsilon^2=0$, and their exponentials are exact unipotent elements, $\exp(r_t\vec\Upsilon)=e_t+r_t\vec\Upsilon$ — the null rotations of [the photon article](the-photon-in-biquaternionic-form.html). So the algebra contains the collinear structure the parton model needs. The invariance of $x$ is a different element, though, and the distinction matters: $x$ is fixed by the collinear *dilation* $p^+\to\lambda p^+$, which is the exponential of a bivector and a boost in the ordinary sense, while a null rotation rescales neither null component and leaves $x$ alone for the trivial reason. The parton model needs the dilation; the algebra has both. This is a real statement and it is small: the algebra hosts the kinematics.

**Two, negative: it does not supply the constituents.** The triplet does not exist in $\mathbb{B}$, as [the ceiling article](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) established and the QCD article restated. So the partons whose densities this article fits are not objects of the algebra at all. The densities are functions on $x$ that describe the distribution of things the algebra cannot host.

**Three, negative: it does not supply the densities.** Nothing in $\mathbb{B}$ produces $q(x)$. The densities come from data, and no amount of algebra will replace them, for the same reason that no amount of algebra produces the proton mass: they are non-perturbative. The only framework object that touches them is the scale at which they are defined, and that scale is the running coupling's.

**The ledger.**

| Item | Status |
|---|---|
| $Q^2$, $x$, $y$, $\nu$ and their relations | **Standard kinematics**; $x$ invariant under the algebra's collinear dilation |
| The null direction and its unipotent exponential | **Derived in the algebra**; the light-cone structure's carrier |
| The two-structure decomposition of $W_{\mu\nu}$ | **Imported.** Lorentz invariance and parity |
| Bjorken scaling | **Imported.** Dimensional analysis plus pointlike constituents |
| The impulse approximation and the infinite-momentum frame | **Imported.** An approximation, with $\alpha_s$ corrections |
| $F_2=2xF_1$ | **Derived here** from the Dirac trace of a massless spin-$\tfrac12$ line |
| The parton densities $q_f$, $\bar q_f$, $g$ | **Imported from data.** Functions, not parameters |
| The momentum and baryon-number sum rules | **Imported**; imposed on the fit |
| The Gottfried sum rule and its failure | **Imported**, measured, and it fails: $\int(\bar d-\bar u)=0.147$ |
| $P_{qq}$ and $A_n$ | **Imported** splitting function; $A_n$ **derived** here and checked against quadrature |
| The DGLAP equation | **Imported**; its moment solution **derived here** |
| The exponents $d_n=-A_n/b_0$ | **Derived** here, with $b_0$ from the running article |
| The Gross–Llewellyn Smith sum rule | **Imported**, with its one-loop and two-loop arithmetic done here |
| Factorisation | **Imported theorem**, not proved |
| The triplet, the octet, the number three | **Not available in $\mathbb{B}$**, per the ceiling |

**What this article does not do.** It does not compute a cross section, does not fit a density, does not solve the singlet evolution, and does not prove factorisation. It states what is measured, derives the two relations that can be derived from a trace and an integral, and marks the rest.

## Summary

Deep inelastic scattering measures two functions of two variables, and the parton model is the statement that at large $Q^2$ they collapse to functions of one: $F_2(x)=\sum_fe_f^2x(q_f+\bar q_f)$. The collapse is dimensional analysis plus the elastic condition $2xp\cdot q=Q^2$, and the variable $x$ is the fraction of null momentum, invariant under the collinear boost because the denominator $2p\cdot q$ is.

The two structure functions are related by the Dirac trace. Contracting the massless spin-$\tfrac12$ partonic tensor with $q^\mu$ gives zero, using $q\cdot k=Q^2/2$, $q\cdot l=-Q^2/2$ and $k\cdot l=Q^2/2$, so the tensor is purely transverse and $F_2=2xF_1$. For a scalar constituent the tensor has no transverse part at all and $F_1=0$, so the ratio is a spin measurement. The measured $R\approx0.18$ says the spin-$\tfrac12$ picture is right, with one $\alpha_s$ source of violation and one power correction behind the residual.

The densities are functions, not numbers: this is the one place in the series where the corpus imports something it cannot even in principle compute. Three sum rules constrain them, and only two of the three are tests. Momentum is imposed rather than tested, and baryon number holds. Gottfried fails: $0.235\pm0.026$ against $\tfrac13$, which measures an excess of $\bar d$ over $\bar u$ of $0.147\pm0.039$.

The residual $Q^2$ dependence is the running coupling. The moment eigenvalues of the splitting function are $A_n=C_F[\tfrac32-\tfrac1n-\tfrac1{n+1}-2H_{n-1}]$, checked against four-million-point quadrature to $5\times10^{-6}$; $A_1=0$ exactly, which is quark number conservation; $A_2=-\tfrac{16}{9}$; and the moments evolve as $\alpha_s^{d_n}$ with $d_2=\tfrac{16}{75}$ and $d_3=\tfrac13$. Every moment falls and the higher ones fall faster, so the distribution softens, and the measured small-$x$ rise is the singlet and gluon sector that this article names and does not compute.

One sum rule measures the coupling without densities: Gross–Llewellyn Smith, $3(1-\alpha_s/\pi)=2.733$ at $\alpha_s=0.28$, the coupling at the datum's own scale $Q^2=3$ GeV$^2$, against a measured $2.50$. The known two-loop coefficient $c_2=3.25$ moves that to $2.66$ and needs to be $9.8$ to close the gap, so the residual is the low-$Q^2$ treatment and not an unknown coefficient; the controlled NNLO extraction gives $\alpha_s(M_Z)=0.119\pm0.005$.

The framework supplies the null direction, and with it the light-cone decomposition; the invariance of $x$ under the collinear dilation is a separate and ordinary fact about boosts. It does not supply the triplet, the constituents, or the densities, and the ledger says so line by line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $k'$ | Initial and final lepton momenta |
| $p$ | Target momentum; $M$ the target mass |
| $q=k-k'$ | Momentum transfer |
| $Q^2=-q^2$ | Virtuality of the exchange, positive |
| $\nu=p\cdot q/M$ | Energy transfer in the target rest frame |
| $x=Q^2/(2p\cdot q)$ | Bjorken variable; the parton's fraction of null momentum |
| $y=p\cdot q/(p\cdot k)$ | Inelasticity, $Q^2=sxy$; $s=2ME$ fixed target, $4E_eE_p$ collider |
| $e_f$ | Quark charge in units of $e$; the weight $e_f^2$ in $F_2$ |
| $L_{\mu\nu}$ | Lepton tensor, $2(k_\mu k'_\nu+k_\nu k'_\mu-g_{\mu\nu}k\cdot k')$ |
| $p^\pm=(p^0\pm p^3)/\sqrt2$ | Light-cone components; $x=k^+/p^+$ |
| $F_L=F_2\left(1+\tfrac{4M^2x^2}{Q^2}\right)-2xF_1$ | Longitudinal structure function; $R=F_L/(2xF_1)$, and $F_L=0$ for massless spin-$\tfrac12$ at leading order |
| $z$, $\xi$ | Momentum fraction in the splitting ($z$) and in the convolution ($\xi$) |
| $c_2$ | Two-loop coefficient of the Gross–Llewellyn Smith sum rule, $\tfrac{55}{12}-\tfrac13N_f$ |
| $g_{\mu\nu}$ | Metric, $\mathrm{diag}(1,-1,-1,-1)$ |
| $W_{\mu\nu}$ | Hadronic tensor |
| $W_1$, $W_2$ | Its two scalar coefficients |
| $F_1=MW_1$, $F_2=\nu W_2$ | Dimensionless structure functions |
| $F_3$ | Parity-odd structure function, measured with neutrinos |
| $N$ | Isoscalar nucleon, $(p+n)/2$; the target of the sum rule |
| $R=\sigma_L/\sigma_T$ | Longitudinal-to-transverse ratio; zero for spin-$\tfrac12$ |
| $q_f(x,Q^2)$, $\bar q_f$, $g$ | Parton densities |
| $P_{qq}(z)$, $P_{gq}(z)$ | Quark-to-quark and gluon-to-quark splitting functions, $C_F[(1+z^2)/(1-z)]_+$ and $C_F[1+(1-z)^2]/z$ |
| $A_n$ | Its $n$-th moment, $C_F[\tfrac32-\tfrac1n-\tfrac1{n+1}-2H_{n-1}]$ |
| $d_n=-A_n/b_0$ | Exponent of $\alpha_s$ in the moment's evolution |
| $\alpha_s(Q^2)$ | Strong coupling at the scale of the probe |
| $b_0=11-\tfrac23N_f$ | One-loop coefficient of the running, $\tfrac{25}{3}$ at four flavours |
| $C_F=\tfrac43$ | Quadratic Casimir of the triplet; the quark's colour charge |
| $q_n=\int_0^1x^{n-1}q(x)dx$ | The $n$-th moment whose evolution the exponent governs |
| $\alpha$ | Fine-structure constant; the cross section above carries $\alpha^2$ |
| $S_G$ | Gottfried sum, measured $0.235\pm0.026$ |
| $\mu_R$, $\mu_F$ | Renormalisation and factorisation scales |
| $s$ | Lepton–proton centre-of-mass energy squared; $2ME$ fixed target, $4E_eE_p$ collider |

## Further Reading

- [Asymptotic Freedom and the Running of the Strong Coupling](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). $b_0$, $\alpha_s(Q^2)$ and the numbers the exponents here are built from.
- [The QCD Lagrangian: Colour, the Triplet, the Octet and the Feynman Rules](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html). $C_F=\tfrac43$, the vertices the splitting functions are computed from.
- [Confinement and the Loss of Partonic Information in Biquaternionic Form](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html). Why the partonic description is a description at a resolution, and what confinement does to it.
- [The Proton in Biquaternionic Form](the-proton-in-biquaternionic-form.html). The spin-$\tfrac12$ carrier, and what the algebra does and does not say about compositeness.
- [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html). The null direction and the exact unipotent null rotations that the light-cone construction uses.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The reason the constituents are not objects of the algebra.
- [The Weinberg Angle, the Neutral Current and the $Z$ Coupling](the-weinberg-angle-the-neutral-current-and-the-z-coupling.html). The $Z$ exchange that corrects the photon-only cross section, and $F_3$'s parity-odd partner.
- [Lattice Gauge Theory and the Biquaternion Path Integral](lattice-gauge-theory-and-the-biquaternion-path-integral.html). The method that computes what the densities can only be fitted to.
