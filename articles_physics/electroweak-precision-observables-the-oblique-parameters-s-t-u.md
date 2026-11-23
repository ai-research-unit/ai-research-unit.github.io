# __Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$__

## Introduction

The material below is standard theory, written in the corpus's language. No number in it is derived from the biquaternion algebra, and §*What the Framework Supplies* separates the linear algebra the algebra can host from the part imported with the particle content. The two sources are Peskin and Takeuchi (1990), where the three parameters are defined, and the electroweak review of the Particle Data Group, where they are fitted.

Three numbers summarise what any heavy new sector does to the electroweak gauge bosons, and they exist because the vacuum polarisation of those bosons has more freedom than the three inputs of the theory can fix. The freedom is three-dimensional, and that dimension is a count, not a convention:

$$
8-2-3=3 .
$$

Four self-energy functions, each with a value and a slope at zero momentum, give eight numbers. Electromagnetic gauge invariance sets two of the values to zero. The three measured inputs $\alpha$, $G_F$ and $M_Z$ absorb three more. Three combinations survive, and they are called $S$, $T$ and $U$.

The definitions are these.

$$
S=\frac{4s_W^2c_W^2}{\alpha}\left[\Pi'_{ZZ}(0)-\frac{c_W^2-s_W^2}{s_Wc_W}\Pi'_{Z\gamma}(0)-\Pi'_{\gamma\gamma}(0)\right] ,
$$

$$
T=\frac{1}{\alpha}\left[\frac{\Pi_{WW}(0)}{M_W^2}-\frac{\Pi_{ZZ}(0)}{M_Z^2}\right] ,
\qquad
U=\frac{4s_W^2}{\alpha}\left[\Pi'_{WW}(0)-c_W^2\Pi'_{ZZ}(0)-2s_Wc_W\Pi'_{Z\gamma}(0)-s_W^2\Pi'_{\gamma\gamma}(0)\right] ,
$$

with $\Pi_{VV'}(q^2)$ the transverse part of the self-energy and the prime the derivative in $q^2$. All three are shifts: they are defined with the Standard Model of some reference top mass and reference Higgs mass subtracted, and that subtraction is the subject of §*The Scheme, Stated Once*.

Each measures one part of the custodial relation. $S$ measures the slope of the part of the self-energy that breaks weak isospin without breaking the custodial symmetry. $T$ measures the value of the part that breaks custodial symmetry, and it is the $\rho$ parameter written as a deviation. $U$ measures the slope of the part that breaks custodial symmetry, and it is the one the data constrain least, which is why the literature writes "$S$, $T$" more often than "$S$, $T$, $U$".

The measured values say what a non-zero value would mean.

| Parameter | Fitted value | Meaning of a non-zero value |
|---|---|---|
| $S$ | $0.00\pm0.07$ | new states with weak isospin that couple to the transverse modes |
| $T$ | $0.05\pm0.06$ | new states with a mass splitting inside an isospin multiplet |
| $U$ | $0.02\pm0.06$ | new states whose custodial violation is momentum-dependent |

The three are consistent with zero, and that is the sharpest statement in the sector: no new sector that couples obliquely to the gauge bosons sits at the electroweak scale. The sentence is weaker than it sounds, and §*What the Parameters Cannot See* says why.

$\rho$ appears elsewhere as the tree-level number $1$ and as the custodial invariant, and the statement "$\rho-1\approx\alpha T$" is used without the definition of $T$. Here are the definition, the count that produces it, and the numbers.

## The Self-Energy Functions

The one-particle-irreducible two-point function of two gauge fields, in momentum space, carries two Lorentz indices and is written

$$
i\Pi_{VV',\imath\jmath}(q)=i\left(\delta_{\imath\jmath}-\frac{q_{\imath} q_{\jmath}}{q^2}\right)\Pi_{VV'}(q^2)+\text{(terms proportional to }q_{\imath}\text{ or }q_{\jmath}\text{)} .
$$

The second piece never contributes to a physical amplitude: a conserved external current annihilates it. What matters is the transverse function $\Pi_{VV'}(q^2)$.

For the photon the transverse structure is forced. Electromagnetic gauge invariance requires $\sum_{\imath} q_{\imath}\Pi_{\gamma\gamma,\imath\jmath}=0$. With the projectors

$$
P_{\imath\jmath}=\delta_{\imath\jmath}+\frac{q_{\imath} q_{\jmath}}{\Pi} ,
\qquad
L_{\imath\jmath}=-\frac{q_{\imath} q_{\jmath}}{\Pi} ,
\qquad
\Pi\equiv-\sum_{\imath} q_{\imath} q_{\imath} ,
$$

the only symmetric tensor built from $\delta$ and $q$ that is annihilated by $q_{\imath}$ is $P_{\imath\jmath}$, since $\sum_{\imath} q_{\imath} P_{\imath\jmath}=0$ and $\sum_{\imath} q_{\imath} L_{\imath\jmath}=-q_{\jmath}$. So

$$
\Pi_{\gamma\gamma,\imath\jmath}(q)=P_{\imath\jmath}\,\Pi_{\gamma\gamma}(q^2) ,
$$

and the longitudinal projector is absent identically. "The photon self-energy is transverse" and "the longitudinal projector is invisible to a conserved current" are the same statement, and both are the Ward identity.

There are four functions: the three neutral pairs among $\gamma$ and $Z$, and the charged pair $WW$, which mixes with neither:

| Function | External legs | Vanishes at $q^2=0$? |
|---|---|---|
| $\Pi_{\gamma\gamma}$ | $\gamma\gamma$ | yes, and its value is zero |
| $\Pi_{Z\gamma}$ | $Z\gamma$ | yes, and its value is zero |
| $\Pi_{ZZ}$ | $ZZ$ | no |
| $\Pi_{WW}$ | $WW$ | no |

Two values are zero and two are not. The two that vanish do so by electromagnetic gauge invariance: a massless photon cannot mix with anything at zero momentum, because a mixing would give it a mass. The two that do not vanish are the masses themselves: $\Pi_{ZZ}(0)=M_Z^2$ and $\Pi_{WW}(0)=M_W^2$ in the reference theory, so the two non-zero values are not free but are fixed by the two measured masses.

Each function is expanded about $q^2=0$,

$$
\Pi_{VV'}(q^2)=\Pi_{VV'}(0)+q^2\,\Pi'_{VV'}(0)+\tfrac12 q^4\,\Pi''_{VV'}(0)+\cdots ,
$$

and the three parameters retain the first two terms only. That truncation is the definition of "oblique": the new physics is assumed heavy compared with $M_Z$, so that its contribution is a polynomial in $q^2/M^2$ of low order, and the terms beyond the first derivative are dropped.

Value and slope for four functions give eight numbers, which is the starting point of the count.

## Why Three and Not More

Eight numbers, less two, less three.

| Step | Removed | Reason |
|---|---|---|
| four functions, value and slope | $8$ remain | definition |
| $\Pi_{\gamma\gamma}(0)=0$ and $\Pi_{Z\gamma}(0)=0$ | $6$ remain | electromagnetic gauge invariance |
| $\alpha$, $G_F$, $M_Z$ as inputs | $3$ remain | they fix three normalisations |
| the survivors | $S$, $T$, $U$ | by definition |

The three inputs are three measurements of three combinations of the same eight numbers: $\alpha$ is the residue of the photon propagator, $G_F$ is the charged-current normalisation at zero momentum transfer, and $M_Z$ is the position of the neutral pole. Which combination each one removes depends on the basis in which the eight are written, so the assignment of inputs to numbers is not one-to-one; the dimension of what is left is.

$\alpha$ and $G_F$ together predict $M_W$ in the reference theory, and $M_Z$ is measured. What the three inputs cannot fix is the *relative* normalisation of the charged and neutral sectors, which is the combination appearing in $T$. The three inputs are three measurements against four normalisations, and the mismatch is one number; the derivatives supply two more.

The count is not a convention. A different set of three inputs would give a different basis for the same three-dimensional space, in the way that a different choice of axes gives different coordinates for the same vector. The dimension is invariant, and the invariance is the content of the statement "three parameters". A reader who doubts the count should try to construct a fourth: any addition would have to be a combination of the eight already counted, so it cannot be independent.

$\Pi_{WW}$ appears with both its value and its slope, and both are used: the value in $T$, the slope in $U$. The reason the $W$ enters two parameters and the $Z$ enters three is that the $Z$ mixes with the photon and the $W$ does not.

## What Each of the Three Measures

A sector that respects the custodial symmetry has the same two-point function in its charged direction and in the neutral direction of the same isospin multiplet,

$$
\Pi_{WW}(q^2)=\Pi_{W_3W_3}(q^2)\qquad\text{for all }q^2 ,
$$

each side being written in the mass eigenstates. At $q^2=0$ the photon pieces vanish and the relation reads $\Pi_{WW}(0)=c_W^2\Pi_{ZZ}(0)$, which is $M_W^2=M_Z^2c_W^2$. One relation, evaluated and differentiated, produces the zeros of $T$ and $U$.

The multiplet structure behind the relation is the display of $SU(2)$ — the compact factor, which in this algebra is $\mathrm{SU}(2)=\mathrm{Spin}(3)$: the left-handed fields are carried by a minimal left ideal, the right-handed by the conjugate, and the hypercharge is a circle inside the right action. The custodial group is then the diagonal rotor acting by the Hermitian pair, which is the spatial rotation, so the three oblique parameters have a one-line reading and no formula changes:

- $T=0$ when the vacuum is fixed by the diagonal rotor — that is, when the vacuum is rotation-invariant, which is the framework's statement of custodial symmetry.
- $U=0$ with $T$ when no further carrier splits off at the same order, since the rotor's tower is complete at spin one.
- $S$ measures how far the vacuum's carrier is from being the trivial one, which is why it is the one parameter that does not vanish for a degenerate heavy sector.

None of this computes a number. It names the objects whose failure to be symmetric the three parameters measure, and it is why the count is three: the rotor has three carriers, one per spin.

The three parameters are three ways of breaking it.

| Parameter | Which part of the relation fails |
|---|---|
| $T$ | the relation at $q^2=0$: the two masses are not in the custodial ratio |
| $U$ | the relation in its $q^2$ derivative: the two slopes are not in the custodial ratio |
| $S$ | neither: $S$ is the overall size of the isospin-breaking sector that the relation does not constrain |

With the definitions above, and at leading order in the deviations,

$$
\alpha T=\frac{M_W^2}{M_Z^2c_W^2}-1=\rho-1 .
$$

The verification is direct: $\rho-1$ is the mismatch of the two normalisations, and $T$ is that mismatch divided by $\alpha$ so as to be dimensionless and of order one for a typical heavy sector. $T$ is the oblique parameter of $\rho$, and $\rho$ is the tree-level value of $T$'s numerator. For the measured $T=0.05$, $\rho-1=3.6\times10^{-4}$: the custodial relation holds to four parts in ten thousand.

Written in the neutral self-energies the combination is a difference of slopes, and the subtraction is what removes the piece a pure isospin sector would contribute; what is left is the $W_3$–$B$ mixing. But $S$ is not the $W_3$–$B$ function alone. In the definition it appears with the coefficient $-(c_W^2-s_W^2)/(s_Wc_W)$ against $\Pi'_{Z\gamma}$ and with $-1$ against $\Pi'_{\gamma\gamma}$, so a sector whose $\Pi_{3Y}$ vanishes still contributes through $\Pi'_{ZZ}-\Pi'_{\gamma\gamma}$, which is proportional to $\Pi'_{33}-\Pi'_{YY}$. A vector-like singlet or doublet has equal left and right couplings, so those weights cancel and $S=0$; a chiral doublet does not, and it keeps $S=N_c/(6\pi)$ even when its two members are exactly degenerate. That number, $0.053$ for a lepton doublet and $0.16$ for a quark one, is the whole reason a fourth chiral generation is excluded, and it is the value at degeneracy, not away from it. What degeneracy removes is $\Pi_{3Y}$ — the trace $\sum_iT_{3,i}Y_i$ vanishes for any doublet with a common hypercharge — and with it the $Z\gamma$ mixing, not $S$.

$U$ is the same kind of difference, taken in the derivative. For a heavy sector it is suppressed relative to $S$ by $M_Z^2/M^2$, because the difference of the derivatives brings down a factor of the inverse mass squared. That is why the pairing $S$–$T$ carries nearly all the information and $U$ is quoted last, with the largest relative uncertainty.

## The Custodial Limit as the Zero of Two Parameters

A custodially invariant heavy sector has $T=0$ and $U=0$ exactly, and $S$ unconstrained. The first follows from the value of the custodial relation at $q^2=0$, the second from its derivative.

Take the tree-level masses, with $M_W=\tfrac12gv$ and $M_Z=\tfrac12\sqrt{g^2+g_{\mathrm Y}^2}\,v$,

$$
\frac{M_W^2}{M_Z^2c_W^2}=\frac{g^2v^2/4}{\frac{v^2}{4}\left(g^2+g_{\mathrm Y}^2\right)\cdot\frac{g^2}{g^2+g_{\mathrm Y}^2}}=1 ,
$$

identically, so $T=0$ at tree level in the reference theory. That is not a prediction of the framework; it is the custodial symmetry of the doublet, computed from the tree-level masses and interpreted in the custodial-symmetry article.

Hypercharge breaks the custodial symmetry explicitly, because it gauges one direction of $SU(2)_R$ and not the other two. The breaking is a loop effect in the reference theory and a tree-level effect for any new sector with a mass splitting inside a multiplet.

Five kinds of sector sit in this classification, and only one silence in it comes from degeneracy.

| Sector | $S$ | $T$ | $U$ |
|---|---|---|---|
| strictly degenerate chiral doublet, custodial | $N_c/(6\pi)$ | $0$ | $0$ |
| chiral doublet with a mass splitting | $N_c/(6\pi)$ at degeneracy, smaller as the splitting grows | $\delta\rho/\alpha$ | small |
| vector-like doublet, degenerate (left and right couplings equal) | $0$ | $0$ | $0$ |
| vector-like singlet | $0$ | $0$ | $0$ |
| state with hypercharge and no isospin | $0$ | $0$ | $0$ |

The rows are ordered by what survives. A vector-like singlet has no isospin, so it cannot break a relation about isospin, and it is invisible to all three parameters at leading order: it only renormalises the three inputs, which is to say it is absorbed into $\alpha$, $G_F$ and $M_Z$ and leaves no trace. The last row says the same about hypercharge alone: with no isospin there is nothing for the hypercharge to mix with. A vector-like doublet is invisible for the other reason — its left and right couplings are equal, so the weights that make $S$ cancel — and that is the row the word "degenerate" used to be attached to. Degeneracy is not silence. An exactly degenerate *chiral* doublet has $T=U=0$ by custodial symmetry and $S=N_c/(6\pi)$ at its full value, which is why a degenerate fourth generation is excluded by $S$ alone. $S$, $T$ and $U$ measure the vector-like or chiral character of a multiplet and the breaking of its custodial relation, not merely the existence of new particles. A sector can be heavy, chiral, present, and still consistent with $(0,0,0)$ only if it is vector-like, which is the sharpest thing that can be said about them.

## What a Heavy Sector Would Shift

For a heavy fermion doublet whose members have masses $m_1$ and $m_2$, the shift of the $\rho$ parameter is

$$
\delta\rho=\frac{N_cG_F}{8\sqrt{2}\,\pi^2}\,f(m_1,m_2) ,
\qquad
f(m_1,m_2)=m_1^2+m_2^2-\frac{2m_1^2m_2^2}{m_1^2-m_2^2}\ln\frac{m_1^2}{m_2^2} .
$$

The bracket $f$ vanishes identically at $m_1=m_2$, which is the check that it must pass: a degenerate pair is custodially invariant and cannot shift $\rho$. Both the formula and its limits are standard one-loop results.

The bracket has two regimes.

- One mass much lighter: with $m_2\to0$ the bracket tends to $m_1^2$, so $\delta\rho=N_cG_Fm_1^2/(8\sqrt2\pi^2)$. The top–bottom pair is in this regime, and the number is the classical one: with $m_t=172.69$ GeV the bracket is $2.98\times10^{4}$ GeV$^2$ and $\delta\rho=9.3\times10^{-3}$, that is $T=1.27$.
- Near-degenerate: with $m_2=m_1+\delta m$ the bracket tends to $(\delta m^2)^2/(3m^2)$ with $\delta m^2=m_2^2-m_1^2$, which is quadratic in $\delta m^2$ where the popular estimate is linear. A heavy pair is therefore far safer than the linear estimate suggests, and the popular formula $\delta\rho\simeq N_cG_F\delta m^2/(8\sqrt2\pi^2)$ is not valid here: it overestimates by more than two orders of magnitude in the near-degenerate regime.

The exact values sit beside the linear estimate.

| $m_1$, $m_2$ (GeV) | $N_c$ | $\delta\rho$ exact | $T$ exact | $T$ from the linear $\delta m^2$ estimate |
|---|---|---|---|---|
| $300/301$ | $3$ | $4.2\times10^{-7}$ | $0.00006$ | $0.026$ |
| $300/310$ | $3$ | $4.2\times10^{-5}$ | $0.006$ | $0.26$ |
| $300/400$ | $3$ | $4.2\times10^{-3}$ | $0.57$ | $3.0$ |
| $500/510$ | $3$ | $4.2\times10^{-5}$ | $0.006$ | $0.43$ |
| $172.69/4.18$ | $3$ | $9.3\times10^{-3}$ | $1.27$ | $1.28$ |

The last row is the reference, and that is the point of the whole scheme. The top–bottom contribution is not new physics: it sits inside the Standard Model prediction, and the reference top mass is defined so that it does. A reader who takes the $1.27$ of the last row as a discrepancy to be explained has forgotten what the subtraction means.

With $\sigma_T=0.06$ and a colour-triplet doublet at $300$ GeV, the near-degenerate bracket gives $\delta m\lesssim30$ GeV, and the exact bracket agrees: $300/325$ gives $T=0.036$ and $300/330$ gives $T=0.052$. The bound is on the splitting relative to the mass, not on the mass, which is why a heavy degenerate multiplet survives.

$S$ is the harder one to estimate, because it survives only through the mixing, so it is sensitive to the difference of the two loop functions rather than to their size, and the difference is what makes the estimates scheme- and splitting-dependent. The large-$N$ number $N_c/(6\pi)$ is $0.053$ per doublet, of the order of the experimental uncertainty, which is the quantitative reason this sector is called precision physics: a single chiral doublet at the electroweak scale would be visible, and none is. The exact one-loop value for a given mass splitting is a two-line computation from the definition, and the literature's tables differ in the third digit for that reason.

## The Measured Values

From the electroweak fit to the LEP and SLD data, $M_W$, $m_t$ and the $Z$-pole asymmetries, with the Higgs mass fixed at $125$ GeV:

| Parameter | Value | Uncertainty |
|---|---|---|
| $S$ | $0.00$ | $\pm0.07$ |
| $T$ | $0.05$ | $\pm0.06$ |
| $U$ | $0.02$ | $\pm0.06$ |

The third digit is not meaningful, and the numbers move in the third digit between editions of the review and between fits with different reference masses. What is stable is the size: a few hundredths, which is the same size as the standard estimate $N_c/(6\pi)$ for one chiral doublet.

The correlation is large and it matters. $S$ and $T$ are quoted with a correlation close to $+0.9$, and the correlations involving $U$ are smaller and negative. Two consequences follow, and both are routinely ignored.

- The errors are not independent. Adding $\pm0.07$ and $\pm0.06$ in quadrature is wrong. The ellipse is long and thin, and its axes are computable: with those two uncertainties and that correlation, the combination $S-1.2\,T$ is measured to $\pm0.020$ while the orthogonal one, $S+0.84\,T$, is measured only to $\pm0.090$ — a factor of four and a half.
- Which axis a sector sits on decides its bound, and the two axes are not the ones the individual numbers suggest. A heavy scalar doublet raises $S$ and lowers $T$, so it moves along $S-1.2T$: the *tight* direction, at $\pm0.020$. Such doublets are therefore among the most strongly constrained sectors in the classification, which is why the mass limits on them are tight. The direction that hides is the other one, $S$ and $T$ rising together, which is where a sector with both mixing and custodial violation of the same sign sits.

One direction in the $S$–$T$ plane is measured to $0.02$ and the other only to $0.09$, and the well-measured one is the combination the $Z$-pole couplings fix directly; the poorly measured one is where a sector can hide.

Some twenty quantities — $M_Z$, $\Gamma_Z$, $\sigma_{\mathrm{had}}$, the three $R_\ell$, the three $A_{FB}^{0,\ell}$, the three $A_\ell$ from SLD, $A_b$, $A_{FB}^{0,b}$, $A_c$, $A_{FB}^{0,c}$, $M_W$, $\Gamma_W$, $m_t$ — against three parameters. The over-determination is the test: a fit with three parameters to twenty numbers is a fit that can fail, and the fact that it does not is the evidence that the oblique approximation captures the data at the current precision.

The strongest objection is that twenty observables reduced to three numbers discards information. The discarded directions are not discarded but *tested*: a sector that couples directly to fermions would show up as a residual in the fit, and the residuals are consistent with zero. The oblique reduction is a hypothesis, and the fit tests it at the same time as it tests the parameters.

## The Higgs Mass and the Fit That Predicted It

In the Standard Model the Higgs contributes to $S$ logarithmically,

$$
\frac{dS}{d\ln M_H}=\frac{1}{6\pi}=0.053 ,
$$

so a factor of two in $M_H$ moves $S$ by $0.037$, about half the experimental uncertainty, and a factor of eight moves it by $0.11$. The sign is positive: a heavier Higgs pushes $S$ up.

With $S$ measured to be consistent with zero, a heavy Higgs was disfavoured, and the fit with $M_H$ free gave a central value near $90$ GeV with a 95 per cent upper bound near $160$ GeV. That bound was the sector's most-quoted number for a decade.

The Higgs was found at $125$ GeV, inside the window. This is the one place in the sector where a precision fit predicted a mass before the discovery, and it is worth stating what the prediction assumed: the Standard Model particle content, the oblique truncation, and the measured top mass. Under those three assumptions the bound was a bound on one number.

The same fit cannot predict the mass of a new sector, because a new sector enters with three unknown parameters rather than one. What the fit supplies for new physics is an allowed region in the $S$–$T$ plane, not a number.

The number to remember is $1/(6\pi)=0.053$ per unit of $\ln M_H$. The same factor appears as the large-$N$ estimate $N_c/(6\pi)$ for a chiral doublet's contribution to $S$, and the two are easy to confuse: one is a slope in the Higgs mass, the other an estimate of a finite mixing from a fermion loop. They enter different fits and they are not interchangeable.

## What the Parameters Cannot See

The three parameters describe new physics that couples to the Standard Model *only* through the gauge-boson self-energies. That is a strong assumption, and it fails in identifiable ways.

| What is invisible or misdescribed | Why | What is needed instead |
|---|---|---|
| a $Z'$ with direct fermion couplings | it produces four-fermion operators, not self-energies | a full four-fermion fit |
| leptoquarks with flavour structure | the couplings carry generation indices | flavour-specific observables |
| new physics lighter than $M_Z$ | the expansion in $q^2/M^2$ does not converge | a full momentum-dependent analysis |
| a sector coupling only to the Higgs | it shifts $M_H$ and the quartic, not the gauge functions | the Higgs couplings |
| anything with a large width | a broad resonance is not a heavy state | a line-shape analysis |

A $Z'$ is the standard example: it mixes with the $Z$, so it does shift $S$ and $T$, but it also couples to fermions directly, and the direct couplings dominate the $Z$-pole observables. A fit in $S$ and $T$ alone would attribute the shift to the wrong parameter and could miss the state entirely.

The oblique truncation drops terms of order $M_Z^2/M^2$ and higher. For a sector at $1$ TeV those terms are at the per-cent level, which is at the edge of the measurement; for a sector at $300$ GeV they are not small, and the three parameters are a poor summary.

If the oblique description were wrong, the fit to twenty observables with three parameters would leave residuals much larger than the quoted uncertainties. It does not, so the description holds at the current precision, and the statement has a date on it: it will fail when the $Z$-pole uncertainties improve by an order of magnitude, or when a $Z'$ is found.

## The Scheme, Stated Once

Three choices change the numbers.

| Choice | Options | Size of the effect |
|---|---|---|
| which $\alpha$ | $\alpha(M_Z)=1/127.95$ or $\alpha(0)=1/137.04$ | $7$ per cent on $S$ |
| reference $m_t$ | $172.69$ GeV, or the fitted value | shifts $T$ by the top contribution |
| reference $M_H$ | $125$ GeV, or free | shifts $S$ by $1/(6\pi)$ per unit $\ln$ |

The prefactor of $S$ is $4s_W^2c_W^2/\alpha$, which is $91.0$ with $\alpha(M_Z)$ and $97.4$ with $\alpha(0)$. The same physical self-energy therefore gives two different values of $S$, differing by $7$ per cent — about one standard deviation. $S$ without a statement of $\alpha$ is not a number, which is the lesson the Weinberg-angle article states about $\sin^2\theta_W$.

Moving the reference top mass by $1$ GeV moves $T$ by $0.0148$, since $\partial T/\partial m_t$ is the top's contribution to $\delta\rho$ differentiated. That is a quarter of the uncertainty, so the reference mass must be quoted to the GeV.

What does not depend on the scheme is the physical prediction: $M_W$, the $Z$-pole asymmetries and the cross sections. The parameters are coordinates on the space of heavy sectors, and coordinates move when the axes do, which is why the content article carries a scheme column.

Every number here is normalised with $\alpha(0)=1/137.036$, not $\alpha(M_Z)$. That is the convention the definitions were written in, and it is visible in two of the numbers above. $T=\delta\rho/\alpha$ at the top row gives $1.27$ with $\alpha(0)$ and $1.19$ with $\alpha(M_Z)$. And $\alpha T=\rho-1$ at $T=0.05$ gives $3.6\times10^{-4}$ with $\alpha(0)$ and $3.9\times10^{-4}$ with $\alpha(M_Z)$. Using $\alpha(M_Z)$ throughout would rescale $S$ and $T$ by $0.934$ — the $7$ per cent of the table, and nothing else changes.

The rest of the corpus uses $\alpha(M_Z)$: the Weinberg angle is stated at $M_Z$ in the $\overline{\mathrm{MS}}$ scheme, and the couplings are taken at $M_Z$. The oblique parameters are the exception, because their normalisation is inherited from Peskin and Takeuchi and is a statement about the reference theory rather than about the $Z$ pole. So the normalisation inside $S$, $T$ and $U$ is $\alpha(0)$ throughout, and a reader comparing with a table that used $\alpha(M_Z)$ must accept the $7$ per cent before comparing digits. A statement of the form "$S=0.00$" without an $\alpha$ is not a number, and neither is "$T=1.27$".

## What the Framework Supplies

What the algebra supplies and what is imported:

| Item | Status |
|---|---|
| Transversality of the self-energy from the Ward identity | the algebra's, via the gauge-fixing article's projector |
| The projector algebra $P^2=P$, $L^2=L$, $P+L=\delta$ | from the gauge-fixing article |
| The count $8-2-3=3$ | linear algebra; available to any framework |
| The custodial relation $\Pi_{WW}=\Pi_{W_3W_3}$ and its $q^2=0$ case | the algebra's group, the tree-level masses |
| The definitions of $S$, $T$, $U$ | imported, Peskin–Takeuchi |
| The measured values | imported, PDG |
| The one-loop Veltman bracket, and the estimate $N_c/(6\pi)$ for a degenerate chiral doublet | imported |
| The particle content that fixes $N_c$ and the multiplicities | imported; no framework route |

Two things the algebra contributes are not transcription.

- Transversality is structural. The self-energy must lie in the projector $P$, and $P$ is the object that makes the vector propagator invertible. So the same algebra that fixed the gauge produces the tensor structure of the vacuum polarisation, and no new machinery is needed.
- The count is a dimension. The three parameters are the dimension of a quotient of the eight Taylor coefficients by five constraints, and a dimension is exactly what a linear-algebra framework can state without knowing the dynamics.

What the algebra does not contribute is the numerical values, and the *existence* of the three parameters as measurements. The framework can say why three combinations survive; it cannot say what they are worth, because their worth is set by the particle content, and the particle content has no framework route.

Those two statements are what make the article consistent with the gauge-fixing article rather than merely adjacent to it: the same $P$ and $L$, the same Ward identity, the same $\Pi$.

The oblique parameters are a *summary* of heavy physics, not a theory of it. Nothing in the framework or in the algebra produces the heavy sector to be summarised, so the article's subject is what the Standard Model's precision data say about the absence of such a sector, and it is silent on what such a sector would be.

## Summary

Three numbers summarise heavy new physics in the gauge sector, and their number is forced: four self-energy functions with value and slope give eight numbers, two vanish by electromagnetic gauge invariance, three are absorbed by the measured inputs $\alpha$, $G_F$ and $M_Z$, and three survive. The count is $8-2-3=3$ and it is a dimension, not a convention.

$T$ is the $\rho$ parameter written as a deviation, $\alpha T=\rho-1$; with $T=0.05$ the custodial relation holds to $3.6\times10^{-4}$. $S$ is what survives the subtraction in the neutral sector — the $W_3$–$B$ mixing together with the difference $\Pi'_{ZZ}-\Pi'_{\gamma\gamma}$ — and it is largest for a degenerate chiral doublet, at $N_c/(6\pi)$; $U$ is the same kind of difference taken in the derivative, which is why $U$ is the smallest and the least measured. A custodially invariant sector has $T=U=0$ exactly, and the statement is the value and the derivative of one relation, $\Pi_{WW}(q^2)=\Pi_{W_3W_3}(q^2)$, whose $q^2=0$ case is $M_W=M_Zc_W$.

The measured values are $S=0.00\pm0.07$, $T=0.05\pm0.06$ and $U=0.02\pm0.06$, with an $S$–$T$ correlation near $+0.9$. The strong correlation is not a detail: it means the two uncertainties cannot be combined in quadrature and that a sector moving along the ellipse is less constrained than either bound suggests.

A mass splitting shifts $T$ through the Veltman bracket, which is quadratic in $\delta m^2$ for a near-degenerate pair and linear in the heavy mass for a hierarchical one; the popular linear estimate $\delta\rho\simeq N_cG_F\delta m^2/(8\sqrt2\pi^2)$ overestimates the near-degenerate case by more than two orders of magnitude, and the table above shows the exact values beside it. The top–bottom pair contributes $T=1.27$ and sits inside the reference, which is what the subtraction means. An exactly degenerate *chiral* pair has $T=U=0$ by custodial symmetry and $S=N_c/(6\pi)$ at full strength; it is the vector-like pair, with equal left and right couplings, that vanishes from all three. $S$ is therefore a meter of chiral versus vector-like structure, not of particle count.

The standard large-$N$ estimate for a chiral doublet's contribution to $S$, $N_c/(6\pi)=0.053$, is the size of the experimental uncertainty. That coincidence is what makes the sector a precision test: one chiral doublet at the electroweak scale would be visible, and none is. A vector-like singlet, and any state with no isospin, shifts nothing at leading order, so the parameters measure multiplet structure and its breaking rather than the presence of heavy states. The oblique description is itself a hypothesis, tested by the fit's residuals, with a date on it.

The framework supplies the transversality of the self-energy through the gauge-fixing article's projector, and the dimension count as linear algebra. It does not supply the definitions, the numbers, or the particle content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_{VV'}(q^2)$ | Transverse part of the $VV'$ self-energy |
| $\Pi'_{VV'}(0)$ | Its derivative in $q^2$ at zero momentum |
| $P_{\imath\jmath}$, $L_{\imath\jmath}$ | The transverse and longitudinal projectors |
| $\Pi$ | $-\sum_{\imath} q_{\imath} q_{\imath}$, the positive momentum invariant |
| $s_W$, $c_W$ | $\sin\theta_W$, $\cos\theta_W$ |
| $\alpha$ | $1/137.036$ inside $S$, $T$ and $U$ — the definitions' normalisation; $\alpha(M_Z)=1/127.95$ elsewhere in the corpus |
| $\rho$ | $M_W^2/(M_Z^2c_W^2)$, equal to $1+\alpha T$ at leading order |
| $\Pi_{33}$, $\Pi_{3Y}$, $\Pi_{YY}$ | The $W_3W_3$, $W_3B$ and $BB$ self-energies, in terms of which $\Pi_{ZZ}$, $\Pi_{Z\gamma}$ and $\Pi_{\gamma\gamma}$ are written |
| $q^2$ | The momentum transfer squared of the self-energy |
| $M_W$, $M_Z$ | $80.377$ and $91.1876$ GeV |
| $G_F$ | $1.1664\times10^{-5}$ GeV$^{-2}$ |
| $S$ | The $W_3$–$B$ mixing parameter |
| $T$ | The custodial-breaking value parameter, $\alpha T=\rho-1$ |
| $U$ | The custodial-breaking slope parameter |
| $\delta\rho$ | The shift of $\rho$, equal to $\alpha T$ at leading order |
| $f(m_1,m_2)$ | The Veltman bracket, vanishing at $m_1=m_2$ |
| $N_c$ | Colour multiplicity: $1$ for leptons, $3$ for quarks |
| $m_t$, $M_H$ | Reference top and Higgs masses of the subtraction |

## Further Reading

- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html). The tree-level masses and $\rho=1$ that the subtraction of this article refers to.
- [The Weinberg Angle and the Three Neutral States: $\tfrac38$ Conditional on $g_R=g_L$](the-weinberg-angle-and-the-three-neutral-states.html). The three angles and the scheme discipline that §*The Scheme, Stated Once* repeats.
- [Gauge Fixing in the Electroweak Theory: $R_\xi$ Gauges, Ghosts and the Goldstone Equivalence Theorem](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html). The projectors $P$ and $L$ and the Ward identity that force the self-energy to be transverse.
- [Custodial Symmetry and the Rho Parameter: From Accidental to Gauged](custodial-symmetry-and-the-rho-parameter.html). The group-theoretic content of the custodial relation, and the earlier use of $\alpha T\approx\rho-1$.
- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The parameter table and the scheme column that $S$, $T$ and $U$ are not in.
- [The Standard Model and the Lagrangian: Four Sectors in One Expression](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html). The sign rule that puts a corpus action beside a standard one.
- [The Standard Model as the Low-Energy Phase: The U(2) Ceiling and the Four Unbuilt Sectors](the-standard-model-as-the-low-energy-phase.html). The classification that the last section uses.

- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html). The strong sector that fixes $N_c$ in the bracket of §*What a Heavy Sector Would Shift*, and the colour factor that makes a quark doublet three times a leptonic one.
- [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html). The top mass that sets the reference subtraction, and the Higgs coupling whose scale dependence is the other half of the scheme question.
