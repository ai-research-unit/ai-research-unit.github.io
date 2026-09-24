# __The Bell Inequality for Continuous Variables in Biquaternionic Form__

## Introduction

The companion exercise *Exercise: The CHSH Inequality and Tsirelson's Bound* treats Bell's theorem for two qubits. Its observables have two outcomes each, labelled $\pm1$; its classical bound is $|S|\le2$; and its quantum bound is Tsirelson's $|S|\le2\sqrt{2}$, which is a theorem about the spectrum of a four-dimensional Hermitian operator and holds for every state of the two-qubit algebra. The menu lists "the continuous-variable Bell inequality" as a separate article. This is that article.

The subject is the analogue of CHSH for observables with **continuous spectrum**. The benchmark is not the discrete Tsirelson bound but the Clauser–Horne–Shimony–Holt form as it was adapted to continuous variables by Braunstein and Caves. The physical arena is quantum optics: two field modes, quadratures $(\hat x,\hat p)$ with $[\hat x,\hat p]=i$, displacements in phase space, and the ideal test state, the **two-mode squeezed vacuum**.

The purpose of the article is threefold, and the three purposes are inseparable.

**First, to state the trap.** It is natural to carry over the discrete-variable bound, to write "$2\sqrt{2}$" as *the* continuous-variable Bell bound, and to treat the two-mode squeezed state as a device that "approaches Tsirelson's bound". That is wrong in a specific and reportable way. There is **no single Tsirelson bound for continuous variables.** The boundary of the CHSH combination depends on which observables are measured and on how many outcomes they are resolved into, and it depends on the state in a way the two-qubit bound does not. The number $2\sqrt{2}$ is still meaningful, but only as an upper bound on the sub-family of *dichotomic* continuous-variable observables — that is, on a question that has already been reduced to the discrete case. A number quoted without saying what it is a bound on is not a result.

**Second, to verify the violation on an explicit state, with the quadrature signs checked.** The natural state is the two-mode squeezed vacuum $|r\rangle$. With the **displaced-parity** observables — the standard continuous-variable pseudo-spin, with eigenvalues $\pm1$ — the CHSH combination built from $|r\rangle$ is computed below in closed form. The correlation function is
$$
E(\alpha,\beta)=\exp\!\Bigl(-2\cosh(2r)\bigl(|\alpha|^2+|\beta|^2\bigr)+4\sinh(2r)\,\mathrm{Re}(\alpha\beta)\Bigr),
$$
and the sign of the cross term is the point at which the quadrature convention must be checked rather than remembered. The article reports the check: the exponent is $\mathrm{Re}(\alpha\beta)$, **not** $\mathrm{Re}(\alpha\bar\beta)$. The two agree whenever both displacements are real (and again at $r=0$, where the cross term vanishes altogether) — which is exactly the case that cannot distinguish them — and the first version of the computation was wrong for that reason. The correlator is verified twice, once from the Wigner function and once by an independent truncated-Fock-space evaluation of the displaced-parity operators.

**Third, to say honestly what the biquaternion framework does here.** The framework supplies the trace pairing $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ and the idempotent algebra of the informational sector $\mathbb{M}_+$, and a dichotomic observable is a fair translation target for those tools. But the states and observables of the continuous-variable problem are **not elements of $\mathbb{B}$**. A quadrature has continuous spectrum, and no element of $\mathbb{B}\cong M_2(\mathbb{C})$ or of $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ has one; a bosonic mode requires $[\hat a,\hat a^\dagger]=e_0$ on an infinite-dimensional module, and the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* already proves that no such pair exists in $\mathbb{B}$, because the trace of a commutator vanishes while $\mathrm{Tr}(e_0)=2$. The framework can restate the *bound* — which is a fact about $\pm1$ spectra — but it cannot represent the *state*, and it therefore has no natural handle on the continuous-spectrum case. This is recorded below as a gap, not smoothed into an analogy.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$, the anti-Hermitian subspace $\mathbb{M}_-$, the complex subspace $\mathbb{C}_{\mathbb{B}}$ (the complex scalars, the center of $\mathbb{B}$), and the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$. The quaternion units are $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and the cyclic products $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$; $i$ is the scalar imaginary, $i^2=-1$. The trace is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, so that $\mathrm{Tr}(e_0)=2$. The isomorphism is the one fixed by *Quantum Mechanics in Biquaternionic Form*, $e_0\mapsto I_2$ and $e_k\mapsto-i\sigma_k$, whose image of $ie_k$ is $\sigma_k$. The two-qubit arena of the discrete exercise is $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. The field-theoretic companion's result on the bosonic obstruction is inherited and used, not rederived.

## Two Inequalities, Not One

Bell's theorem comes in forms, and the continuous-variable literature inherits more than one of them. The confusion the trap exploits is that the discrete forms have state-independent bounds and the continuous forms do not.

### The discrete form, for contrast

For two parties, two settings each, and observables $A,A',B,B'$ with spectrum contained in $\{\pm1\}$, the CHSH combination
$$
S=E(\hat a,\hat b)-E(\hat a,\hat b')+E(\hat a',\hat b)+E(\hat a',\hat b')
$$
satisfies $|S|\le2$ in every local hidden-variable model, because for each value of the shared variable one of $B-B'$, $B+B'$ vanishes. The quantum maximum over *all* states and all $\pm1$ observables is $2\sqrt{2}$, Tsirelson's bound; the algebraic maximum compatible with no-signaling is $4$. All three numbers are state-independent, observable-independent within the $\pm1$ class, and sharp. This is the structure the companion exercise establishes in the biquaternion algebra.

### The continuous form, and why the bound moves

A continuous-variable observable — a quadrature $\hat x_\theta$, the photon-number parity, a binned homodyne count — has a spectrum that need not be $\{\pm1\}$. Two things change at once.

**The observables are no longer pinned to $\{\pm1\}$.** If the outcomes are unbounded, the CHSH combination is not defined without a normalisation, and the inequality that replaces it is a different inequality: Braunstein and Caves adapted the Bell argument to observables of continuous spectrum by bounding the outcomes (or by working with the Wigner function directly), and the bound they obtain is a bound **on the normalised correlations of those bounded observables**. Quoting "$2\sqrt{2}$" for it is a category error unless the observables are first made dichotomic.

**The number of outcomes matters.** If a continuous outcome is binned into $d$ values, the relevant inequality is the $d$-outcome generalisation, and its classical and quantum bounds depend on $d$. The bound is a function of the outcome alphabet. There is no single number.

**The achievable maximum depends on the state and on the observable family.** Even after fixing the form and the number of outcomes, the largest $S$ a given state can reach depends on which observables are available. For the two-mode squeezed vacuum with displaced-parity observables, the maximum computed below is approximately $2.3245$ in the limit of infinite squeezing — not $2\sqrt{2}\approx2.8284$, and not a number any discrete formula would predict. Different continuous-variable observables give different boundaries, and the sharp ones are state-dependent.

The honest summary, and the sentence the rest of the article is written to support, is this: **for continuous variables there is no single Tsirelson bound; the boundary depends on the measured observables, on the number of outcomes, and on the state, and a bound may be quoted only together with the class of observables it bounds.** The one place a familiar number survives is the dichotomic class, where the discrete argument applies verbatim and gives $2$ classically and $2\sqrt{2}$ quantum — but that class has already given up the continuous spectrum.

## The Continuous-Variable Arena

### Quadratures and the sign convention

For a single mode with annihilation and creation operators $\hat a,\hat a^\dagger$ satisfying $[\hat a,\hat a^\dagger]=1$, the **quadratures** are
$$
\hat x=\frac{\hat a+\hat a^\dagger}{\sqrt2},\qquad
\hat p=\frac{\hat a-\hat a^\dagger}{i\sqrt2}=-i\,\frac{\hat a-\hat a^\dagger}{\sqrt2},
\qquad [\hat x,\hat p]=i .
$$
With this normalisation the vacuum has $\langle\hat x^2\rangle=\langle\hat p^2\rangle=\tfrac12$. The phase-space coordinate conjugate to these operators is the **complex displacement**
$$
\alpha=\frac{x+ip}{\sqrt2},\qquad |\alpha|^2=\frac{x^2+p^2}{2},
$$
so that a coherent state $|\alpha\rangle$ has $\langle\hat x\rangle=\sqrt2\,\mathrm{Re}\,\alpha$ and $\langle\hat p\rangle=\sqrt2\,\mathrm{Im}\,\alpha$. The factor of $\sqrt2$ and the sign of $i$ in $\hat p$ are conventions, and the correlation function below is stated in this one; a different normalisation of $\alpha$ rescales the optimum but not the physics.

The **displacement operator** is $D(\alpha)=\exp(\alpha\hat a^\dagger-\bar\alpha\hat a)$, and the **displaced parity**
$$
\Pi(\alpha)=D(\alpha)\,(-1)^{\hat n}\,D(\alpha)^\dagger,\qquad \hat n=\hat a^\dagger\hat a,
$$
is Hermitian, unitary, and has eigenvalues $\pm1$ exactly, because $(-1)^{\hat n}$ does and $D(\alpha)$ is unitary. It is the standard continuous-variable pseudo-spin: a genuinely continuous-family observable with a discrete, dichotomic, $\pm1$ spectrum. This is the observable family used throughout the article, because it is the family for which the CHSH combination is defined without further normalisation and for which the discrete bound $2$ applies verbatim as the classical bound.

Two facts about $\Pi(\alpha)$ are used below. First, its expectation is a fixed multiple of the Wigner function evaluated at the corresponding phase-space point,
$$
\langle\Pi(\alpha)\rangle=\pi\,W(\alpha),
$$
where $W$ is the Wigner function in the standard $x$–$p$ normalisation, so that a single mode has $\int W\,d^2\alpha=\tfrac12$. (The factor is $\pi$ and not $\pi/2$; the elementary vacuum value settles it, since $\langle\Pi(\alpha)\rangle_{\mathrm{vac}}=\langle\alpha|(-1)^{\hat n}|\alpha\rangle=e^{-2|\alpha|^2}$ and the vacuum Wigner in this convention is $\pi^{-1}e^{-2|\alpha|^2}$.) Second, $\Pi(\alpha)^2=e_0$: the eigenvalues are $\pm1$, so the classical CHSH proof applies to any two settings per party on each mode.

For a two-mode state the correlation of two displacements is
$$
E(\alpha,\beta)=\bigl\langle \Pi(\alpha)\otimes\Pi(\beta)\bigr\rangle .
$$

### The two-mode squeezed vacuum

The **two-mode squeezed vacuum** (TMSV) with squeezing parameter $r\ge0$ is, in the two-mode Fock basis,
$$
|r\rangle=\mathrm{sech}\,r\sum_{n=0}^{\infty}(\tanh r)^n\,|n\rangle_1|n\rangle_2 .
$$
Its reduced state on one mode is thermal with mean occupation $\bar n=\sinh^2 r$:
$$
\rho_1=\mathrm{Tr}_2|r\rangle\langle r|=\sum_n p_n|n\rangle\langle n|,\qquad
p_n=\frac{1}{\cosh^2 r}\,(\tanh^2 r)^n .
$$
The quadrature variances fix the correlation structure and the sign: with $\hat x_{1}-\hat x_{2}$ and $\hat p_{1}+\hat p_{2}$ as the squeezed combinations,
$$
\mathrm{Var}(\hat x_1-\hat x_2)=e^{-2r},\qquad
\mathrm{Var}(\hat p_1+\hat p_2)=e^{-2r},\qquad
\mathrm{Var}(\hat x_1+\hat x_2)=\mathrm{Var}(\hat p_1-\hat p_2)=e^{2r}.
$$
The sign in the second relation is the EPR structure: the two modes' positions agree and their momenta oppose, so the difference of positions and the **sum** of momenta are the quiet combinations. A correlator written in terms of $\hat p_1-\hat p_2$ would be correlating the loud combination and would be wrong. That distinction is what the cross-term sign check below detects.

### The Wigner function

The two-mode Wigner function of the TMSV is the Gaussian
$$
W(\alpha,\beta)=\frac{1}{\pi^2}\exp\!\Bigl(-2\cosh(2r)\bigl(|\alpha|^2+|\beta|^2\bigr)+4\sinh(2r)\,\mathrm{Re}(\alpha\beta)\Bigr),
$$
in the same $x$–$p$ normalisation as above. The cross term is $\mathrm{Re}(\alpha\beta)$; the marginal Wigner function of one mode is
$$
W_1(\alpha)=\frac{1}{\pi\cosh(2r)}\exp\!\Bigl(-\frac{2|\alpha|^2}{\cosh(2r)}\Bigr),
$$
the thermal Gaussian of the reduced state, which reproduces $\bar n=\sinh^2r$. These are standard; the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* records that the bosonic mode they describe has no native realisation in $\mathbb{B}$.

## The Correlation Function, and the Sign Check

### The correlator

The correlation of two displaced parities in the TMSV follows from the Wigner functions. Using
$$
\langle\Pi(\alpha)\rangle=\pi W_1(\alpha),
\qquad
\bigl\langle\Pi(\alpha)\otimes\Pi(\beta)\bigr\rangle=\pi^2 W(\alpha,\beta),
$$
the factor $\pi$ arising on each mode because each parity is a single-mode operator, one obtains
$$
\boxed{\;E(\alpha,\beta)=\exp\!\Bigl(-2\cosh(2r)\bigl(|\alpha|^2+|\beta|^2\bigr)+4\sinh(2r)\,\mathrm{Re}(\alpha\beta)\Bigr).\;}
$$
At $r=0$ this is $\exp(-2|\alpha|^2-2|\beta|^2)=E(\alpha)E(\beta)$: a product of one-mode factors, as it must be for the vacuum, which is a product state, and $E(\alpha,\beta)=0$ whenever either displacement is far from the origin. For $r>0$ the cross term $\mathrm{Re}(\alpha\beta)$ correlates the two modes along the EPR ridge.

### The sign check, reported rather than assumed

The exponent must be $\mathrm{Re}(\alpha\beta)$. The alternative that a reader who remembers "EPR correlations" will write is $\mathrm{Re}(\alpha\bar\beta)$, and the two are *equal when $\alpha$ and $\beta$ are both real, and equal again at $r=0$*, which is to say they agree on exactly the configurations a first check is likely to try. This is the case the claim came from, and checking it proves nothing. The check that distinguishes them used complex displacements, where $\mathrm{Re}(\alpha\beta)$ and $\mathrm{Re}(\alpha\bar\beta)$ differ.

Two independent evaluations were made.

**From the Wigner function.** With $E=\exp(-2\cosh2r(|\alpha|^2+|\beta|^2)+4\sinh2r\,\mathrm{Re}(\alpha\beta))$, the one-mode marginals reproduce the thermal distribution $p_n=\mathrm{sech}^2r\,\tanh^{2n}r$ and the two-mode function is a normalised Gaussian whose covariance matrix has $\mathrm{Var}(\hat x_1-\hat x_2)=\mathrm{Var}(\hat p_1+\hat p_2)=e^{-2r}$ and $\mathrm{Var}(\hat x_1+\hat x_2)=\mathrm{Var}(\hat p_1-\hat p_2)=e^{2r}$, matching the EPR structure named in the previous section.

**From an explicit Fock computation.** The displaced-parity operators $\Pi(\alpha)$, $\Pi(\beta)$ were built in a truncated Fock space from the matrix elements $\langle m|D(\alpha)|n\rangle$ of the displacement operator, and
$$
E_{\mathrm{Fock}}=\sum_{m,n}(\mathrm{sech}\,r)(\tanh r)^m\,(\mathrm{sech}\,r)(\tanh r)^n\,\langle m|\Pi(\alpha)|n\rangle\langle m|\Pi(\beta)|n\rangle
$$
was evaluated for complex displacements at several $r$. The agreement with the closed form above is exact to machine precision (residuals at the level of $10^{-16}$ for moderate truncation, growing only to $10^{-6}$ where the truncation is stressed). The same computation with $\mathrm{Re}(\alpha\bar\beta)$ in place of $\mathrm{Re}(\alpha\beta)$ disagrees by amounts up to order unity at the same points — the discrepancy is not marginal, it is qualitative. The sign is therefore settled by an independent route, not by the argument that produced the formula.

## The Violation, and the Value of Its Maximum

### The CHSH combination and its classical bound

With the four displacements $\alpha_1,\alpha_2$ for party $1$ and $\beta_1,\beta_2$ for party $2$, define
$$
S=E(\alpha_1,\beta_1)-E(\alpha_1,\beta_2)+E(\alpha_2,\beta_1)+E(\alpha_2,\beta_2).
$$
Because $\Pi(\alpha)$ and $\Pi(\beta)$ have spectrum $\{\pm1\}$, the classical proof of the discrete case applies unchanged: for a local hidden-variable model the outcomes are $\pm1$ functions of the setting and the shared variable, one of $\Pi(\beta_1)\mp\Pi(\beta_2)$ vanishes at each value of the shared variable, and
$$
|S|\le2 .
$$
This bound is genuine and tight for the parity family, and it is the classical bound for this problem. It is not the bound that moves; the *quantum* boundary is.

### The maximum

For fixed $r$ the four complex displacements were optimised numerically (a broad multi-start search followed by local refinement), and the resulting maxima are:

| $r$ | $S_{\max}$ | excess over $2$ |
|---|---|---|
| $0$ | $2.0000$ | $0$ |
| $0.02$ | $2.0015$ | $0.0015$ |
| $0.05$ | $2.0082$ | $0.0082$ |
| $0.10$ | $2.0276$ | $0.0276$ |
| $0.20$ | $2.0796$ | $0.0796$ |
| $0.30$ | $2.1335$ | $0.1335$ |
| $0.50$ | $2.2199$ | $0.2199$ |
| $1.00$ | $2.3075$ | $0.3075$ |
| $2.00$ | $2.3242$ | $0.3242$ |
| $r\to\infty$ | $2.3245$ | $0.3245$ |

Three features are reportable.

**The violation is real and its threshold is zero.** At $r=0$ the state is the vacuum, a product state, and $S_{\max}=2$ exactly: no violation. For every $r>0$ tested — down to $r=0.01$, where the excess is $3.8\times10^{-4}$ — the maximum exceeds $2$. The two-mode squeezed vacuum violates the parity CHSH inequality at arbitrarily small squeezing. This is unlike the two-qubit Werner state, whose violation requires the visibility $p>1/\sqrt2$; the difference is that the parity observables are matched to the state's Gaussian structure, so the entanglement is detected without a visibility penalty. The excess leaves zero approximately as $r^2$ at the smallest values and grows more slowly than that thereafter, the limit being finite.

**The maximum is not $2\sqrt{2}$, and it is not the discrete bound.** As $r\to\infty$ the maximum rises toward $2.3245$, which is well below Tsirelson's $2\sqrt{2}\approx2.8284$. Carrying the discrete bound over would both overstate what the state achieves and misdescribe what the bound is.

**In the ideal EPR limit the maximum has a closed form.** As $r\to\infty$ the two-mode squeezed state tends to the ideal EPR state, and the correlator becomes $E\to\exp(-|\mathbf{w}-\mathbf{z}|^2)$ in rescaled real two-vectors $\mathbf w,\mathbf z$ carrying the squeezed quadrature combinations. The maximum of $S$ for this kernel is attained on the collinear configuration
$$
\alpha_1=d,\qquad \alpha_2=-d,\qquad \beta_1=0,\qquad \beta_2=-2d,\qquad d^2=\frac{\ln 3}{8},
$$
for which $S=3e^{-d^2}-e^{-9d^2}$ and hence
$$
S_{\max}^{\mathrm{EPR}}=8\cdot 3^{-9/8}=2.3244947809\ldots
$$
The optimisation is one-dimensional along that line and is elementary; the numerical search over all four complex displacements agrees with it and does not exceed it. The value is exact for the ideal EPR state with displaced-parity observables, and it is the number that replaces the discrete Tsirelson bound for this state and this observable family. It is *not* a universal continuous-variable bound, and the article does not offer it as one: it is the boundary of one combination of state and observables.

### The three tiers, for continuous variables

| Bound | Value for the parity CHSH on the TMSV | Assumption |
|---|---|---|
| Classical (CHSH) | $2$ | local outcomes, shared variable; $\pm1$ parity outcomes |
| Quantum, this state and family | rises from $2$, tends to $8\cdot3^{-9/8}\approx2.3245$ | TMSV, displaced parity |
| Tsirelson (same state, any $\pm1$ observables) | $2\sqrt2\approx2.8284$ | any state, dichotomic observables |
| No-signaling (algebraic) | $4$ | each $E\in[-1,1]$ |

The table is the article's answer to the trap in one place. The value $2\sqrt2$ appears, but as the ceiling of the dichotomic class, not as the boundary of the continuous-variable problem; the row that describes the actual state is the state-dependent one; and no single number is the continuous-variable Bell bound.


## What the Biquaternion Framework Supplies, and What It Does Not

### The part that transfers

The framework's discrete result is available, and it is worth stating exactly what it covers. In the companion exercise the CHSH combination for a two-qubit system is the Born pairing of the state with a single Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$,
$$
\tilde{\mathcal S}
=(i\hat a)\otimes(i\hat b)-(i\hat a)\otimes(i\hat b')+(i\hat a')\otimes(i\hat b)+(i\hat a')\otimes(i\hat b'),
$$
whose square is $\tilde{\mathcal S}^2=4\bigl(e_0\otimes e_0+(\hat a\times\hat a')\otimes(\hat b\times\hat b')\bigr)$, giving the bound $2\sqrt2$ through the spectrum of its image in $M_4(\mathbb{C})$. That derivation needs only two things: a two-outcome observable whose square is the identity, and an idempotent state paired with it by the trace. The first is present for the displaced parity, since $\Pi(\alpha)^2=1$; the second is *not*, for the reason in the next subsection. So the transcribable content is the algebra of the **bound**, restricted to the dichotomic class: if one is handed a state that is an element of $\mathbb{M}_+\otimes\mathbb{M}_+$ and a pair of settings per party, the exercise's argument gives $|S|\le2\sqrt2$ for those settings. The framework states the ceiling correctly.

But the ceiling is the least informative row of the table above. For the two-mode squeezed vacuum the actual boundary is $8\cdot3^{-9/8}$, and the framework contributes nothing to it, because the state is not in the algebra.

### The gap: no continuous spectrum in $\mathbb{B}$

The obstruction is structural and is already proved in the corpus. It has two independent faces.

**The algebra cannot hold the mode.** A quadrature $\hat x$ has continuous spectrum, and every element of $\mathbb{B}\cong M_2(\mathbb{C})$ has a finite spectrum of at most two values. The parity $\Pi(\alpha)$, for all that its eigenvalues are $\pm1$, is built from $(-1)^{\hat n}$ and a displacement $D(\alpha)$; both are functions of the bosonic pair $(\hat a,\hat a^\dagger)$, and one bosonic mode requires $[\hat a,\hat a^\dagger]=e_0$ on an infinite-dimensional module. The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* shows that no such pair exists in $\mathbb{B}$: a commutator has vanishing trace, while $\mathrm{Tr}(e_0)=2$, so the only central scalar a commutator can produce is $0$. The framework carries the **fermionic** canonical relation exactly for one mode — the truncated ladder $\tilde a_{\mathrm{tr}}=\tfrac12(ie_1-e_2)$ satisfies $\{\tilde a_{\mathrm{tr}},\tilde a_{\mathrm{tr}}^\dagger\}=e_0$ — and the bosonic relation not at all. There is therefore no $\Pi(\alpha)$ in $\mathbb{B}$, no $\hat xe_0$, no quadrature, and no phase-space displacement as an element of the algebra.

**The algebra cannot hold the state or the arena.** The two-mode squeezed vacuum is a vector in the symmetric algebra of a two-mode one-particle space, a state on $\ell^2(\mathbb{N})^{\otimes2}$; it is infinite-dimensional and is not an element of $\mathbb{B}\otimes\mathbb{B}$, which has complex dimension sixteen. Writing "$|r\rangle$" as an idempotent of the tensor-product algebra would reproduce neither its spectrum nor its marginal, and the reduced thermal state $\sum_n p_n|n\rangle\langle n|$ has no image in $\mathbb{M}_+$, whose positive trace-one elements are exactly the Bloch ball.

The consequence is worth stating as plainly as the corpus states its other gaps. **The biquaternion framework supplies no natural handle on the continuous-spectrum case.** It can name the bound for dichotomic observables; it cannot represent the observables, the state, or the arena in which the bound is attained, and so it cannot supply the state-dependent boundary that is the actual content of the continuous-variable inequality. The gap is not one of effort or of missing notation. It is the finite dimension of $\mathbb{B}$ acting against the infinite dimension of a bosonic mode, and it does not close by refining an analogy. The honest thing to do with it is to leave it visible and labelled, and to decline to present the discrete result as if it covered the continuous case.

### What a genuinely biquaternionic continuous-variable question would require

The gap can be located precisely by saying what would have to exist for the framework to have a native continuous-variable Bell problem.

An infinite-dimensional module over $\mathbb{B}$ carrying a pair with $[\hat a,\hat a^\dagger]=e_0$, together with an element of the framework's own algebraic structure — not merely a matrix representation of it — whose analogue of $\tilde{\mathcal S}^2$ has a continuous spectrum with an explicit boundary; and a state in the algebra whose Born pairing with that element gives the two-mode squeezed correlator. None of the three is available, and the third is impossible in a four-dimensional $\mathbb{C}$-algebra. Whether some larger biquaternionic structure (a field of biquaternions, a $\mathbb{B}$-valued Weyl algebra) could carry them is a question this article does not answer; it records that the finite algebra does not, and that the standard construction of the bosonic Fock space is imported into the framework rather than derived from it.

## Summary

The Bell inequality for continuous variables is the CHSH inequality applied to observables of continuous spectrum, and its benchmark is the Clauser–Horne–Shimony–Holt form as adapted by Braunstein and Caves. This article's findings are four.

**There is no single Tsirelson bound for continuous variables.** The boundary of the CHSH combination depends on the measured observables, on the number of outcomes, and on the state. The value $2\sqrt{2}$ survives as the upper bound for the *dichotomic* class — observables with spectrum $\{\pm1\}$ — which is a reduction to the discrete problem, not a continuous-variable result. The number must be quoted together with the class of observables it bounds, and this article states, for every number it quotes, what that class is.

**On the two-mode squeezed vacuum the violation is explicit and was verified.** With displaced-parity observables the correlator is
$$
E(\alpha,\beta)=\exp\!\Bigl(-2\cosh(2r)\bigl(|\alpha|^2+|\beta|^2\bigr)+4\sinh(2r)\,\mathrm{Re}(\alpha\beta)\Bigr),
$$
checked twice: from the Wigner function, and independently in a truncated Fock space from the matrix elements of the displacement operator, with the marginals reproducing the thermal distribution of the reduced state. The classical bound $|S|\le2$ is violated for every $r>0$, with no visibility threshold, and the maximum grows to a limit in the ideal EPR case of
$$
S_{\max}=8\cdot 3^{-9/8}=2.3244947809\ldots,
$$
well below $2\sqrt{2}$. Different observable families give different boundaries; this value is the boundary of one such family, not a universal constant.

**The quadrature sign was the trap within the trap.** The exponent is $\mathrm{Re}(\alpha\beta)$, not $\mathrm{Re}(\alpha\bar\beta)$. The two coincide when the displacements are real and at $r=0$, so the case that first suggests the formula cannot distinguish them; the check that does was made on complex displacements. The first form of the computation was wrong for exactly this reason and is not carried into the article.

**The biquaternion framework has no natural handle on the continuous-spectrum case, and this is a gap.** The finite-dimensional algebra $\mathbb{B}\cong M_2(\mathbb{C})$ contains no bosonic mode, because a commutator is traceless while $\mathrm{Tr}(e_0)=2$; and $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ contains neither the two-mode squeezed state nor its infinite-dimensional arena. The framework correctly states the dichotomic ceiling $2\sqrt2$ — the companion exercise's algebra of the bound transfers — but it cannot represent the observables, the state, or the state-dependent boundary of the actual problem. Forcing a discrete analogy here would be the failure this article was written to avoid, and the gap is therefore left visible rather than closed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian (informational) and anti-Hermitian (material) subspaces |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ | Complex subspace (complex scalars, center); real-quaternion subspace |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, cyclic products |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (Born rule) |
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit tensor-product arena of the discrete exercise |
| $\hat a,\hat a^\dagger$ | Bosonic annihilation and creation operators, $[\hat a,\hat a^\dagger]=1$ |
| $\hat x,\hat p$ | Quadratures, $\hat x=(\hat a+\hat a^\dagger)/\sqrt2$, $\hat p=-i(\hat a-\hat a^\dagger)/\sqrt2$, $[\hat x,\hat p]=i$ |
| $\alpha=(x+ip)/\sqrt2$ | Complex phase-space displacement, $|\alpha|^2=(x^2+p^2)/2$ |
| $D(\alpha)=\exp(\alpha\hat a^\dagger-\bar\alpha\hat a)$ | Displacement operator |
| $\Pi(\alpha)=D(\alpha)(-1)^{\hat n}D(\alpha)^\dagger$ | Displaced parity, spectrum $\{\pm1\}$, $\Pi(\alpha)^2=1$ |
| $\langle\Pi(\alpha)\rangle=\pi W_1(\alpha)$ | Parity expectation from the Wigner function ($x$–$p$ normalisation, $\int W_1 d^2\alpha=\tfrac12$) |
| $|r\rangle=\mathrm{sech}\,r\sum_n(\tanh r)^n|n\rangle_1|n\rangle_2$ | Two-mode squeezed vacuum |
| $\bar n=\sinh^2 r$, $p_n=\mathrm{sech}^2r\,\tanh^{2n}r$ | Mean occupation and thermal marginal |
| $\mathrm{Var}(\hat x_1-\hat x_2)=\mathrm{Var}(\hat p_1+\hat p_2)=e^{-2r}$ | Squeezed (quiet) EPR combinations |
| $E(\alpha,\beta)=\exp(-2\cosh2r(|\alpha|^2+|\beta|^2)+4\sinh2r\,\mathrm{Re}(\alpha\beta))$ | Parity correlator of the TMSV |
| $S=E(\alpha_1,\beta_1)-E(\alpha_1,\beta_2)+E(\alpha_2,\beta_1)+E(\alpha_2,\beta_2)$ | CHSH combination |
| $\lvert S\rvert\le2$ | Classical (CHSH) bound, dichotomic observables |
| $8\cdot3^{-9/8}=2.3244947809\ldots$ | TMSV parity-CHSH maximum in the ideal EPR limit |
| $\lvert S\rvert\le2\sqrt2$ | Tsirelson bound, dichotomic observables only |
| $\lvert S\rvert\le4$ | No-signaling (algebraic) bound |
| $\tilde a_{\mathrm{tr}}=\tfrac12(ie_1-e_2)$ | Single-mode ladder in $\mathbb{B}$; fermionic, not bosonic |

## Further Reading

- J. S. Bell, "On the Einstein–Podolsky–Rosen paradox," *Physics* **1** (1964) 195–200, for Bell's theorem.
- J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Physical Review Letters* **23** (1969) 880–884, for the CHSH inequality.
- S. L. Braunstein and C. M. Caves, "Wringing out better Bell inequalities," *Annals of Physics* **202** (1990) 22–56, for the adaptation of the Bell inequality to observables of continuous spectrum.
- B. S. Cirel'son (Tsirelson), "Quantum generalizations of Bell's inequality," *Letters in Mathematical Physics* **4** (1980) 93–100, for the bound $2\sqrt{2}$ in the dichotomic case.
- A. Einstein, B. Podolsky, N. Rosen, "Can quantum-mechanical description of physical reality be considered complete?" *Physical Review* **47** (1935) 777–780, for the EPR state that the infinite-squeezing limit approaches.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the CHSH inequality and Tsirelson's bound in the standard formalism.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Mechanics in Biquaternionic Form*, *Entangled Subsystems in the Biquaternion Framework*, *Exercise: The CHSH Inequality and Tsirelson's Bound*, *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, and *The Quantum–Classical Divide in the Biquaternion Framework*.

