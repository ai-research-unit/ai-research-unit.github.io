# __The Renormalization Group in Biquaternionic Form__

## Introduction

The **renormalization group** (RG) is the statement that the parameters of a quantum field theory are not constants but functions of the scale at which the theory is probed. Integrating out a shell of field modes between two momentum scales changes the effective action; the change is a flow in the space of couplings; and the zeros of that flow — the fixed points — organize the theory's behaviour at long and short distances. This article asks what, if anything, the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ adds to that structure.

The question is a fair one to ask of this framework, because the three read-list articles on which the RG rests have each already been written, and each has already located the algebra's contribution narrowly. *The Path Integral in Biquaternionic Form* found that the measure and the space of paths lie outside $\mathbb{B}$, while the central scalar imaginary supplies the phase and the Wick rotation supplies the Euclidean weight. *The Feynman Propagator in Biquaternionic Form* found that the algebra names the axis of the $i\epsilon$ deformation — the $ict$ direction of the material sector $\mathbb{M}_-$ — but does not choose its orientation. *The Partition Function in Biquaternionic Form* found that the trace is a scalar extraction, $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, and that the imaginary-time circle lies along the $\mathbb{M}_-$ time axis. The RG asks for the next thing: the dependence of all of this on a scale.

The finding is stated at the outset, and it has the same shape as the parents'.

- **What the algebra supplies.** A canonical home for the regulator. The **wave biquaternion** $\tilde{k} = iE\,e_0 + \mathbf{p}$ of the propagator article has the **norm form** $N(\tilde{k}) = \tilde{k}\bar{\tilde{k}} = -E^2 + \mathbf{p}^2 = -k^2$, which is a *central* element of $\mathbb{B}$ — a complex scalar times $e_0$ — and which becomes the Euclidean momentum squared $k_E^2 \ge 0$ under the Wick rotation of the path-integral article. A cutoff is therefore naturally a condition on a central scalar, $|\tilde{k}\bar{\tilde{k}}| \le \Lambda^2$, which in Euclidean signature is the real scalar $k_E^2 \le \Lambda^2$. Because it is *real* central — an element of $\mathbb{R}e_0$, the only central direction that commutes with the projections onto $\mathbb{M}_+$ and $\mathbb{M}_-$ (the imaginary central direction $ie_0$ instead exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, $i\mathbb{M}_-=\mathbb{M}_+$) — the natural regulator is **sector-blind** and does not mix the two sectors. The RG scale, the couplings, and the beta functions are likewise central scalars, and the whole flow is a flow of central elements.
- **What it does not supply, and what is therefore transcribed.** The effective action itself. None of the read-list articles supplies a biquaternionic action, a biquaternionic measure, or a biquaternionic regulator; the path-integral article says explicitly that the measure is an analytic construction outside the finite-dimensional algebra. The shell integration, the regularisation scheme, the one-loop coefficients, and the fixed points developed below are standard field theory, written in the biquaternion notation. They are **not** derived from $\mathbb{B}$.
- **The gap, left visible.** Whether the framework's regulator *respects* the two-sector structure is a framework-specific question with no inherited answer. The honest answer is partial: the central norm-form cutoff is diagonal in the two sectors and so does not mix them, which is one sense of respect; but it cannot assign the sectors different scales, and it is a sharp cutoff, which breaks gauge invariance. The gauge-safe regulator — dimensional regularisation — is not a four-dimensional biquaternion construct at all. The two requirements are met by two different regulators, and no regulator supplied by the algebra meets both. This is stated as a gap, not smoothed over.

The article is organized as follows. The next section fixes what the RG is and states the exact flow equation, taking care to distinguish the *functional* trace from the biquaternion trace. The following section describes the regulator and the shell, and what each costs. Two sections then perform the shell integration explicitly — the scalar quartic coupling, and the non-abelian gauge coupling — and fix the **sign** of each beta function. A section checks the fixed points against the flow equation on independent cases. A section addresses the two-sector question directly. A section separates what the algebra supplies from what it only transcribes. The article closes with open questions.

**Conventions.** We use those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The wave biquaternion is $\tilde{k} = iE\,e_0 + \mathbf{p}$ (natural units $\hbar = c = 1$), with norm form $\tilde{k}\bar{\tilde{k}} = -p^2$ and mass shell $\tilde{k}\bar{\tilde{k}} = -m^2$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. Euclidean momenta are denoted $k_E$, with $k_E^2 \ge 0$; the Wick rotation is the identification $\mathbb{M}_- \to \mathbb{H}_{\mathbb{B}}$ of the path-integral and Wick-rotation articles. Throughout, $\mathrm{Tr}$ in a **functional** expression is the trace over field space, not the biquaternion trace $2\,\mathrm{Sc}(\cdot)$; the distinction is flagged where it matters.

## The Scale Dependence of the Effective Action

The **effective action** $\Gamma[\phi]$ is the generating functional of one-particle-irreducible correlation functions: with $Z[J] = \int\mathcal{D}\phi\, e^{-S[\phi] + \int J\phi}$ and $W[J] = \log Z[J]$ (Euclidean signature throughout this article), $\Gamma$ is the Legendre transform of $W$. Its expansion in powers of the field and of derivatives defines the couplings of the theory. In this article we work with the **Wilsonian** effective action $\Gamma_k$, defined at a sliding scale $k$: $\Gamma_k$ is obtained from the microscopic action by integrating out all modes with Euclidean momenta larger than $k$. The dependence of $\Gamma_k$ on $k$ is what the RG computes.

The exact statement of that dependence is the **Wetterich equation**,

$$
\partial_t \Gamma_k[\phi] = \frac{1}{2}\,\mathrm{Tr}\!\left[\Big(\Gamma_k^{(2)}[\phi] + R_k\Big)^{-1}\,\partial_t R_k\right],
\qquad t = \log\frac{k}{\Lambda},
$$

where $\Gamma_k^{(2)}$ is the second functional derivative of $\Gamma_k$ with respect to $\phi$, $R_k$ is a **regulator** that suppresses modes with $|p| < k$, and $\Lambda$ is the microscopic scale at which the flow is initialized. Two features of this equation are the whole subject of the article.

1. **The trace is a functional trace.** The symbol $\mathrm{Tr}$ here is the trace over the infinite-dimensional field space: it stands for $\int \frac{d^4p}{(2\pi)^4}\sum_{\text{internal indices}}$ with the argument evaluated on the field configuration. It is **not** the biquaternion trace $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ of the read list. The biquaternion trace is taken over the two-dimensional fiber of $\mathbb{B}$; the functional trace is taken over the space of modes. They must not be conflated, and when the flow equation is read in the biquaternion framework the two appear side by side: the *fiber* trace is the algebra's, and the *mode* trace is analytic.
2. **The regulator is an input.** The equation is exact for any admissible $R_k$, but $R_k$ is not determined by the theory. Different choices give different *trajectories* $\Gamma_k$ and the same *physics* at the fixed point, up to scheme-dependent redefinitions of the couplings. The regulator is the analytic datum the algebra does not supply.

If $\Gamma_k$ is expanded in a basis of local operators with couplings $g_i(k)$,

$$
\Gamma_k[\phi] = \int d^4x \sum_i g_i(k)\, \mathcal{O}_i[\phi],
$$

then the flow equation is equivalent to a set of ordinary differential equations,

$$
\mu\frac{d g_i}{d\mu} = \beta_i(g),
$$

for the **beta functions**, where $\mu$ is the renormalization scale. A **fixed point** $g^*$ is a simultaneous zero, $\beta_i(g^*) = 0$, at which the couplings stop running. Linearizing about it, $\beta_i \approx \sum_j M_{ij}(g_j - g^*_j)$ with $M_{ij} = \partial\beta_i/\partial g_j|_{g^*}$, the eigenvalues of $M$ classify the directions as **relevant** (negative, growing toward the infrared), **irrelevant** (positive, shrinking toward the infrared), or **marginal**. The fixed points and their stability, not the trajectories, are the scheme-independent content of the RG.

**The scale is a central scalar.** In the biquaternion framework everything in the last two displays is a real number: the scale $\mu$, the couplings $g_i$ of a scalar or gauge theory, and the beta functions are ordinary scalars, that is, real multiples of $e_0$, hence elements of the center $\mathbb{C}_{\mathbb{B}}$ and, being real, of the informational sector $\mathbb{M}_+$. The flow therefore acts trivially on the algebra: it rescales central coefficients and does not by itself rotate one sector into the other. This is the first place the two-sector question arises, and it is treated on its own in a later section.

## The Regulator and the Shell

### The shell in the biquaternion norm form

The propagation of a biquaternion field is organized by the wave biquaternion $\tilde{k} = iE\,e_0 + \mathbf{p}$ and its **norm form**

$$
N(\tilde{k}) = \tilde{k}\bar{\tilde{k}} = (iE)^2 + \mathbf{p}^2 = -E^2 + \mathbf{p}^2 = -p^2 .
$$

This is the object on which the mass shell is the single condition $\tilde{k}\bar{\tilde{k}} = -m^2$, as the propagator article records. It has a property that matters here and is verified in the companion: for a general biquaternion $\tilde{k} = k_0e_0 + k_1e_1 + k_2e_2 + k_3e_3$ with complex coefficients, the product $\tilde{k}\bar{\tilde{k}} = k_0^2 + k_1^2 + k_2^2 + k_3^2$ is a **complex scalar times $e_0$** — it has no vector part — and therefore lies in the center and commutes with every element of $\mathbb{B}$. The norm form is central.

Under the Wick rotation $E \to i k_E^0$ (equivalently the identification $\mathbb{M}_- \to \mathbb{H}_{\mathbb{B}}$ of the companion article), the norm form becomes

$$
\tilde{k}\bar{\tilde{k}} \;\longrightarrow\; (k_E^0)^2 + \mathbf{p}^2 = k_E^2 \;\ge\; 0 .
$$

A **sharp cutoff** at scale $\Lambda$ is therefore naturally written as the algebraic condition

$$
\tilde{k}\bar{\tilde{k}} \le \Lambda^2 \qquad(\text{Euclidean}), 
$$

a condition on a central scalar. Integrating out a shell means restricting the internal momentum of a loop to

$$
\frac{\Lambda}{b} < \sqrt{\tilde{k}\bar{\tilde{k}}} < \Lambda,
\qquad \log b = \delta\ell > 0,
$$

where $b > 1$ is the shell ratio and $\delta\ell$ is the RG step. This is the biquaternion transcription of the standard momentum shell, and it is exact: the norm form is the Euclidean momentum squared, and a shell in $k_E$ is a shell in $\tilde{k}\bar{\tilde{k}}$.

### What the sharp cutoff costs

A sharp momentum cutoff is the easiest regulator to justify for a scalar theory, because the shell integration can be performed in closed form (the next section does so). Its cost is that it is **not gauge invariant**. A gauge transformation of the gauge field is non-local in momentum space: it mixes modes of different $|p|$, so a condition of the form "retain only modes with $|p| < \Lambda$" is not preserved by the transformation, and the regulated action is not invariant. The Ward and Slavnov–Taylor identities that protect the gauge-invariant structure of the theory are violated at the cutoff scale, and the violations must be cancelled by counterterms that themselves break the symmetry. For the abelian case the breaking can be controlled; for the non-abelian case the cutoff is not a practical regulator.

The gauge-safe alternative is **dimensional regularisation** (DR): the loop integrals are evaluated in $d = 4 - \epsilon$ dimensions, continued analytically, and the ultraviolet divergences appear as poles $1/\epsilon$. DR respects gauge invariance because it acts on the *dimension of the loop measure* and not on the mode content of the fields: there is no momentum threshold to violate the identity. Its divergences are logarithmic for the marginal couplings treated here, and the renormalization scale $\mu$ enters through the 't Hooft unit of mass, $\mu^{\epsilon}$, so that a dimensionless coupling runs as $\mu\, dg/d\mu = \beta(g)$. DR does not preserve supersymmetry and does not regulate power divergences; neither limitation matters for the couplings computed below.

**The framework-specific point.** Both regulators are external to the algebra in an important sense. The sharp cutoff is external because it lives on the **mode measure**, which the path-integral article already records as being outside finite-dimensional $\mathbb{B}$; the algebra supplies only the invariant $\tilde{k}\bar{\tilde{k}}$ on which the cutoff is imposed. Dimensional regularisation is external because it continues the dimension away from $d = 4$, whereas $\mathbb{B}$ is a four-real-dimensional algebra with a fixed quaternion basis; there is no $d = 4-\epsilon$ biquaternion algebra in the corpus. The algebra hosts the invariant; it does not host the regulator. This is the same division the parents found for the measure and the $i\epsilon$, and it recurs in every section below.

## Integrating Out a Shell: The Scalar Quartic Coupling

The cleanest case is a single real scalar with a quartic self-interaction,

$$
S[\phi] = \int d^4x\left[\tfrac12(\partial\phi)^2 + \tfrac12 m^2\phi^2 + \frac{\lambda}{4!}\phi^4\right],
$$

whose coupling $\lambda$ is marginal in $d = 4$ and whose beta function is the textbook one. The point of redoing it here is to show the shell integration explicitly, since a beta function stated without it is exactly the failure mode this subject invites.

Split the field into slow and fast modes, $\phi = \phi_< + \phi_>$, where $\phi_>$ carries only momenta in the shell $\Lambda/b < |k| < \Lambda$. Integrating out $\phi_>$ at one loop gives the correction to the four-point function from the bubble diagram: with two vertices $-(\lambda)$ from $(\lambda/4!)\phi^4$, the one-loop 1PI four-point function in the $s$, $t$, and $u$ channels is

$$
\Gamma^{(4)}_{\text{1-loop}}(p) = \frac{1}{2}\cdot 3\,(-\lambda)^2\, I_>(p),
\qquad
I_>(p) = \int_{\text{shell}}\!\frac{d^4k}{(2\pi)^4}\,\frac{1}{\big(k^2+m^2\big)\big((k+p)^2+m^2\big)},
$$

where the factor $3$ counts the channels and $1/2$ is the symmetry factor of the bubble. At zero external momentum the shell integral is elementary. Using $\int d^4k = 2\pi^2 k^3\,dk$ and $u = k^2$,

$$
I_>(0) = \frac{1}{16\pi^2}\int_{\Lambda^2/b^2}^{\Lambda^2} \frac{u\,du}{(u+m^2)^2}
= \frac{1}{16\pi^2}\left[\log\frac{\Lambda^2 + m^2}{\Lambda^2/b^2 + m^2} + m^2\!\left(\frac{1}{\Lambda^2 + m^2} - \frac{1}{\Lambda^2/b^2 + m^2}\right)\right].
$$

In the deep ultraviolet, $m^2 \ll \Lambda^2$, and the mass-dependent terms are suppressed:

$$
I_>(0) = \frac{1}{8\pi^2}\log b \;+\; O\!\left(\frac{m^2}{\Lambda^2}\right).
$$

The coefficient $1/(8\pi^2)$ of the logarithm is the whole content of the one-loop renormalization of the quartic coupling, and it is **mass-independent**: the mass appears only in the power-suppressed terms. This is why the beta function of the marginal coupling is universal and why it is insensitive to the detailed spectrum.

The effective coupling, defined from the 1PI function by $\lambda_{\text{eff}} = -\Gamma^{(4)}(0)$, therefore shifts by

$$
\delta\lambda = -\frac{3}{2}\,\lambda^2\, I_>(0) = -\frac{3\lambda^2}{16\pi^2}\,\log b .
$$

Writing $\delta\ell = \log b$ and reading the equation as the change of $\lambda$ as the cutoff is lowered from $\Lambda$ to $\Lambda/b$ — that is, toward the infrared — the flow is

$$
\frac{d\lambda}{d\ell} = -\frac{3\lambda^2}{16\pi^2},
\qquad\text{equivalently}\qquad
\beta_\lambda = \mu\frac{d\lambda}{d\mu} = +\frac{3\lambda^2}{16\pi^2} .
$$

The relative sign is fixed by $\ell = \log(\Lambda_0/\Lambda)$: increasing $\ell$ lowers the cutoff, so $\mu\,d/d\mu = -d/d\ell$. The sign of the beta function is therefore **positive**, and its consequences are immediate. For $\lambda > 0$, the coupling *grows* toward the ultraviolet and *shrinks* toward the infrared; the Gaussian fixed point $\lambda^* = 0$ is infrared-attractive, and the coupling reaches a Landau pole at a finite ultraviolet scale, at $\ell = \ell_0 - 16\pi^2/(3\lambda_0)$ measured from any reference point $\ell_0$. The one-loop formula is not to be continued past that pole toward the ultraviolet, and the companion records the artifact that a careless continuation through it produces; toward the infrared the coupling decreases monotonically to zero, which is the same statement as the infrared-attractiveness of the Gaussian fixed point.

The same coefficient is obtained from **dimensional regularisation**, which is a useful cross-check of the regulator: the massless bubble in $d = 4-\epsilon$ is

$$
\int\!\frac{d^dk}{(2\pi)^d}\frac{1}{(k^2)^2}
= \frac{\Gamma(2-d/2)}{(4\pi)^{d/2}\Gamma(2)}
= \frac{1}{8\pi^2}\cdot\frac{1}{\epsilon} + O(\epsilon^0),
$$

so the $1/\epsilon$ pole carries the same coefficient $1/(8\pi^2)$ as the sharp-cutoff logarithm $\log b$. The two regulators agree on the universal part, as they must.

### The beta function in $d = 4-\epsilon$

In $d = 4 - \epsilon$ the coupling acquires a classical scaling dimension $[\lambda] = \epsilon$, and the beta function acquires a term $-\epsilon\lambda$ from the engineering dimension:

$$
\beta_\lambda = -\epsilon\lambda + \frac{3\lambda^2}{16\pi^2} + O(\lambda^3).
$$

Besides the Gaussian fixed point $\lambda^* = 0$, this beta function has the **Wilson–Fisher fixed point**

$$
\lambda^* = \frac{16\pi^2}{3}\,\epsilon ,
$$

at which the two competing terms balance. We check this in the next section, rather than assert it.

## The Non-Abelian Gauge Coupling

The second case is the running of a non-abelian gauge coupling, which is the independent case with the opposite sign. It must be treated with a gauge-invariant regulator, so we use dimensional regularisation and the standard one-loop coefficient; a sharp cutoff cannot be used here for the reason given above.

The one-loop beta function of a Yang–Mills theory with gauge group $G$ and matter in representations $r$ is

$$
\beta_g = \mu\frac{dg}{d\mu} = -\frac{g^3}{16\pi^2}\,b_0,
\qquad
b_0 = \frac{11}{3}\,C_2(G) - \frac{2}{3}\sum_{\text{Weyl}} T(r),
$$

where $C_2(G)$ is the quadratic Casimir of the adjoint representation and $T(r)$ the Dynkin index of the matter representation. The **sign is negative** for a non-abelian gauge group with sufficiently little matter: the coupling *decreases* toward the ultraviolet, which is asymptotic freedom. This is the opposite sign to the scalar quartic coupling, and the contrast is the point of computing both.

The group-theory ingredient is the adjoint Casimir, and it is worth checking rather than quoting. For $SU(N)$ the structure constants satisfy

$$
\sum_{c,d} f^{acd}f^{bcd} = C_2(G)\,\delta^{ab} = N\,\delta^{ab}.
$$

This was recomputed explicitly in the companion: from the antisymmetric symbol for $SU(2)$ one gets $2\,\delta^{ab}$, and from the Gell-Mann structure constants $f^{abc} = -\frac{i}{4}\mathrm{Tr}([\lambda^a,\lambda^b]\lambda^c)$ for $SU(3)$ one gets $3\,\delta^{ab}$. The two cases $N = 2$ and $N = 3$ agree with $C_2(G) = N$; the $SU(3)$ value is the one that motivates the formula in QCD, and the $SU(2)$ value was computed as an independent check, so that the formula is not tested only on the case that suggested it.

For pure $SU(N)$ Yang–Mills, $b_0 = \frac{11}{3}N > 0$, so

$$
\beta_g = -\frac{11N}{3}\frac{g^3}{16\pi^2} < 0 ,
$$

and the Gaussian fixed point $g^* = 0$ is **ultraviolet-attractive**: the theory is asymptotically free and the coupling is weak at short distances. For $SU(3)$ with $N_f$ Dirac quark flavours, each flavour contributes two Weyl fermions of index $T = \frac12$, so $b_0 = 11 - \frac{2}{3}N_f$, and asymptotic freedom requires

$$
N_f < \frac{33}{2} = 16.5,
\qquad\text{that is}\qquad N_f \le 16 .
$$

The beta function changes sign at $N_f = 16.5$: below it the theory is asymptotically free, above it the coupling grows in the ultraviolet and the theory is infrared-free. This threshold is verified in the companion directly from the formula for $b_0$, on the values $N_f = 16$ and $N_f = 17$, not on the threshold itself.

The abelian case is the third sign, and it falls on the scalar side. For quantum electrodynamics with one Dirac fermion, $b_0 = -\frac{4}{3}$ in the same normalization, so $\beta_e = +e^3/(12\pi^2) > 0$: the abelian gauge coupling grows in the ultraviolet, like the scalar quartic coupling and unlike the non-abelian one. The distinction is a property of the gauge group's adjoint Casimir, not of the algebra $\mathbb{B}$: nothing in the biquaternion framework selects $SU(N)$ over $U(1)$, and the beta-function signs are those of the gauge groups one chooses to write down.

## Fixed Points and the Flow Equation

The fixed points must be checked against the flow equation, not asserted. We do it on the two independent cases just computed.

**Wilson–Fisher.** With $\beta_\lambda = -\epsilon\lambda + 3\lambda^2/(16\pi^2)$, substituting the candidate fixed point gives

$$
\beta_\lambda\!\left(\frac{16\pi^2}{3}\epsilon\right)
= -\epsilon\cdot\frac{16\pi^2}{3}\epsilon + \frac{3}{16\pi^2}\left(\frac{16\pi^2}{3}\epsilon\right)^2
= -\frac{16\pi^2}{3}\epsilon^2 + \frac{16\pi^2}{3}\epsilon^2 = 0 .
$$

The candidate is a fixed point. Its stability is fixed by the derivative, $\beta_\lambda'(\lambda^*) = -\epsilon + 6\lambda^*/(16\pi^2) = +\epsilon > 0$: because the eigenvalue is positive, the Wilson–Fisher fixed point is **infrared-attractive** in $d = 4-\epsilon$, while the Gaussian fixed point has eigenvalue $-\epsilon < 0$ and is ultraviolet-attractive. In exactly $d = 4$, $\epsilon = 0$, the Gaussian eigenvalue vanishes at one loop and the only fixed point of the one-loop flow is the Gaussian one, which is infrared-attractive for $\lambda > 0$; this is the statement of triviality of $\phi^4$ in four dimensions.

**Banks–Zaks.** At two loops the gauge beta function is

$$
\beta_g = -\frac{b_0}{16\pi^2}g^3 - \frac{b_1}{(16\pi^2)^2}g^5,
$$

with the standard coefficients. For $SU(3)$ with $N_f$ Dirac flavours, $b_0 = 11 - \frac{2}{3}N_f$ and $b_1 = 102 - \frac{38}{3}N_f$. In the window where $b_0 > 0$ and $b_1 < 0$ — which includes $N_f = 16$, for which $b_0 = \frac13$ and $b_1 = -\frac{302}{3}$ — the two terms balance at

$$
g^{*2} = -16\pi^2\frac{b_0}{b_1} = \frac{8\pi^2}{151},
\qquad
\alpha^* = \frac{g^{*2}}{4\pi} \approx 0.0416 ,
$$

a perturbatively small fixed point. Substitution confirms

$$
\beta_g(g^*) = -\frac{b_0}{16\pi^2}g^{*3} - \frac{b_1}{(16\pi^2)^2}g^{*5}
= g^{*3}\left(-\frac{b_0}{16\pi^2} - \frac{b_1}{(16\pi^2)^2}g^{*2}\right)
= g^{*3}\left(-\frac{b_0}{16\pi^2} + \frac{b_0}{16\pi^2}\right) = 0 ,
$$

where the last equality uses $g^{*2} = -16\pi^2 b_0/b_1$; the cancellation is exact in this two-loop truncation, and for $N_f = 16$ the slope $\beta_g'(g^*) > 0$ makes the Banks–Zaks fixed point infrared-attractive, matching its standard role as the infrared end of the conformal window. The companion verified the cancellation symbolically for general $b_0, b_1$ and evaluated the $N_f = 16$ case numerically.

A zero of the beta function is a fixed point in the strong sense that $g(\mu) = g^*$ is a scale-independent solution of $\mu\,dg/d\mu = \beta(g)$, not merely a stationary point of a numerical iteration; what the loop truncation controls is the accuracy of the *location* of $g^*$, not the existence of the constant solution. Two independent beta functions, then, with opposite signs and two different non-trivial fixed-point mechanisms: the scalar quartic in $d = 4-\epsilon$ and the non-abelian gauge coupling in four dimensions. Both fixed points satisfy the flow equation by direct substitution, and the Gaussian fixed points — the third case — satisfy it trivially, $\beta(0) = 0$, in every theory.

| Theory | One-loop beta function | Gaussian fixed point | Non-trivial fixed point |
|---|---|---|---|
| $\phi^4$, $d=4$ | $\beta_\lambda = +\dfrac{3\lambda^2}{16\pi^2}$ | $\lambda^*=0$, IR-attractive | none (Landau pole in UV) |
| $\phi^4$, $d=4-\epsilon$ | $\beta_\lambda = -\epsilon\lambda + \dfrac{3\lambda^2}{16\pi^2}$ | $\lambda^*=0$, UV-attractive | $\lambda^* = \dfrac{16\pi^2}{3}\epsilon$, IR-attractive |
| $U(1)$ gauge | $\beta_e = +\dfrac{e^3}{12\pi^2}$ | $e^*=0$, IR-attractive | none at one loop |
| non-abelian $SU(N)$ | $\beta_g = -\dfrac{11N}{3}\dfrac{g^3}{16\pi^2}$ | $g^*=0$, UV-attractive (asymptotically free) | Banks–Zaks at two loops |

The signs in the table are the physical content: a scalar quartic coupling and an abelian gauge coupling grow toward the ultraviolet, a non-abelian gauge coupling shrinks toward it, and the difference is a group-theoretic fact about the adjoint representation.

## Does the Regulator Respect the Two Sectors?

This is the framework-specific question, and it deserves a direct answer rather than an inherited one. The decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ means that every biquaternionic field has a material part and an informational part. A regulator **respects** the decomposition if its mode suppression is diagonal in the two sectors, that is, if it commutes with the projections $P_\pm$ onto $\mathbb{M}_\pm$; a regulator that mixed $\mathbb{M}_+$ with $\mathbb{M}_-$ would violate it.

**The natural cutoff does respect it, trivially.** The sharp cutoff is the condition $\tilde{k}\bar{\tilde{k}} \le \Lambda^2$ on the norm form, and the norm form of a general biquaternion is central — verified in the companion, where $\tilde{k}\bar{\tilde{k}}$ was shown to have vanishing vector part and to commute with $e_0, e_1, e_2, e_3$. The elements of the algebra that commute with the projections $P_\pm$ are exactly the **real** central scalars $\mathbb{R}e_0$: the imaginary central direction $ie_0$ exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$ and $i\mathbb{M}_-=\mathbb{M}_+$. The cutoff is of this real kind after the Wick rotation, where the norm form becomes $k_E^2 \ge 0$, so the cutoff acts as the same real scalar factor on both sectors and the regulated mode measure factorizes as (sector-blind suppression) $\times$ (free sum over the fibers). In this minimal sense the framework's natural regulator respects the two-sector structure: it does not mix the sectors. Dimensional regularisation respects it in the same minimal sense, since it acts on the loop measure and not on the algebra.

**But respecting is not distinguishing.** A real central cutoff is the *same* cutoff for both sectors; it cannot assign $\mathbb{M}_-$ a scale $\Lambda_-$ and $\mathbb{M}_+$ a scale $\Lambda_+$ with $\Lambda_- \ne \Lambda_+$, because the only elements of the algebra that commute with $P_\pm$ are the real central scalars $\mathbb{R}e_0$, and these multiply both sectors by the same scalar; a regulator with unequal weights on the two sectors — for example $\Lambda_+^2P_+ + \Lambda_-^2P_-$, which is diagonal but not multiplication by an algebra element — would have to be an operator construction outside the algebra-as-multiplication picture used here. So the two-sector structure admits a *sector-blind* regulator but not one supplied by the algebra as a *sector-sensitive* multiplier, and the framework supplies no reason to want one. Whether the effective theory should have two independent scales is not answerable from the read-list articles, and we do not answer it here.

**The tension with gauge invariance.** The sharp norm-form cutoff is the regulator the algebra most naturally hosts, and it is the one that is sector-blind. It is also the one that breaks gauge invariance. The regulator that preserves gauge invariance, dimensional regularisation, is not a four-dimensional biquaternion object: it continues $d = 4 - \epsilon$, and there is no $\epsilon$-deformed biquaternion algebra in the corpus. The two desirable properties — living in the algebra's central structure and preserving gauge invariance — are therefore met by two different regulators, and no single regulator supplied by the framework meets both. A third possibility, a Pauli–Villars regulator, is gauge invariant and lives in field space, but it too is external to the algebra and introduces auxiliary fields whose sector assignment is again a choice. The honest statement is that the framework's regulator is **sector-blind but not sector-distinguishing, and its algebraically natural choice conflicts with gauge invariance**; a genuinely biquaternionic, gauge-invariant regulator is an open problem, not a result.

There is one further framework-specific remark worth recording as a question rather than a claim. The framework makes the complex structure local: $c = 1/\sqrt{\epsilon\mu}$ varies with the medium, and the $ict$ direction varies with it. The RG scale $\mu$ is also a local structure in the sense of being a function of the probe. Whether the medium-dependent local complex structure and the RG scale are related — whether a renormalization of $c$ or of the local complex structure is even meaningful — is not addressed by any read-list article, and enters the open questions below. The suggestion is recorded as a question because that is what it is.

## What the Algebra Adds and What It Does Not

**Standard field theory, transcribed.** The Wilsonian effective action and its exact flow equation; the regulator and the shell; the one-loop four-point bubble and its $1/(8\pi^2)$ logarithm; the one-loop beta functions of the quartic, abelian, and non-abelian couplings; the adjoint Casimir and the asymptotic-freedom threshold; the Wilson–Fisher and Banks–Zaks fixed points and their stability. None of this is derived from $\mathbb{B}$, and none of it would change if the algebra were replaced by any other notation for complexified four-dimensional spacetime.

**What the biquaternion notation provides.**

- **A central invariant for the cutoff.** The norm form $\tilde{k}\bar{\tilde{k}}$ is central, and the sharp cutoff $\tilde{k}\bar{\tilde{k}} \le \Lambda^2$ is a condition on a central scalar. Because it is a real central scalar it is diagonal in the $\mathbb{M}_\pm$ decomposition. This is the one place where the framework gives the regulator a canonical algebraic home.
- **The Euclidean direction.** The Wick rotation $\mathbb{M}_- \to \mathbb{H}_{\mathbb{B}}$ is what turns the Lorentzian norm form into the Euclidean one, $k_E^2 \ge 0$, on which the cutoff is imposed. The regulator thus inherits the same complex structure that the parents located.
- **A clean statement of where the flow acts.** The scale, the couplings, and the beta functions are central scalars; the flow rescales central coefficients and does not rotate the sectors. The two-sector question therefore has the sharp form given in the previous section.
- **A distinction that prevents an error.** The functional trace of the flow equation is not the biquaternion trace $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$; the two appear side by side and must be kept apart. Writing the functional trace as $2\,\mathrm{Sc}$ would be a category error, and the notation of the corpus makes the error visible.

**What it does not provide.**

- **An action.** No read-list article supplies a biquaternionic action, so no biquaternionic beta function can be derived. Everything computed above is the standard flow of a standard action written in the algebra's notation.
- **A measure or a regulator.** The path-integral article records that the measure is analytic and outside finite-dimensional $\mathbb{B}$, and the same is true of the cutoff. The algebra supplies the invariant on which the cutoff is imposed, not the cutoff.
- **A scale or a spectrum.** The RG scale $\mu$, the number of fields, the gauge group, the matter content, and the values of the couplings are all inputs. The algebra fixes none of them.
- **A selection among fixed points.** A fixed point is a property of a flow, and a flow is a property of an action and a regulator. The algebra does not select the flow, so it does not select the fixed point.

**What is interpretation.** Reading the RG scale as a central scalar and the cutoff as a condition on the norm form is a reading of the algebra; the algebra is consistent with it and even suggests it, but it does not force it. The claim that the framework "explains" the renormalization group is not made and is not supported: the RG as presented here is a transcription, and the only algebraic content is the centrality of the invariant on which the cutoff is imposed. If that is all it adds, the article says so.

## Open Questions

1. **A biquaternionic action.** Does the framework admit a $\mathbb{B}$-valued action whose effective action has a beta function not obtainable from any scalar action? The path-integral article leaves the possibility of an $\mathbb{M}_+$-valued action open; without an action, the question cannot be posed.

2. **A biquaternionic gauge-invariant regulator.** The natural central cutoff respects the two-sector decomposition but breaks gauge invariance, and dimensional regularisation is external to the four-dimensional algebra. Is there a regulator that lives in $\mathbb{B}$, preserves gauge invariance, and is diagonal in the sectors?

3. **Sector-sensitive scales.** May the material and informational sectors renormalize at different rates, with $\Lambda_+ \ne \Lambda_-$? Any such regulator must be non-central, which would mix the sectors; whether the framework can accommodate that, and what it would mean, is unresolved.

4. **The local complex structure and the RG scale.** The framework's $c = 1/\sqrt{\epsilon\mu}$ makes the complex structure local. Is there a meaningful renormalization of $c$ or of the local complex structure, and is it related to the RG scale? No read-list article addresses this.

5. **The mass and the cosmological-constant problems.** The shell integration produces quadratic divergences in the mass and, in a gravitational setting, in the vacuum energy. The biquaternion reading does not address them here; whether the central norm form gives any purchase on them is unknown.

6. **The functional trace and the fiber trace.** The flow equation's trace is over field space and the algebra's trace is over the two-dimensional fiber. Is there an intrinsic construction that pairs them — for instance a biquaternion-valued effective action whose fiber trace reduces to the functional trace — or are they irreducibly different? The parents leave the corresponding question for their own traces.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard field theory. The beta functions and fixed points above are the standard ones; nothing here changes them.

## Summary

The renormalization group describes how the effective action depends on scale. Integrating out a shell of modes, $\Lambda/b < \sqrt{\tilde{k}\bar{\tilde{k}}} < \Lambda$, produces a flow in the couplings, $\mu\,dg_i/d\mu = \beta_i(g)$, whose zeros are the fixed points. In the biquaternion framework the **wave biquaternion** $\tilde{k} = iE\,e_0 + \mathbf{p}$ carries the norm form $\tilde{k}\bar{\tilde{k}} = -p^2$, which is central and which the Wick rotation turns into the Euclidean momentum squared $k_E^2$. The natural regulator is therefore the central condition $\tilde{k}\bar{\tilde{k}} \le \Lambda^2$, and because the regulator is a real central scalar it is diagonal in the two-sector decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$: the framework's regulator is **sector-blind**, respects the decomposition in the minimal sense of not mixing the sectors, but cannot assign them different scales.

The beta functions are standard, and their signs are checked on independent cases. For the scalar quartic coupling, the explicit shell integration gives

$$
I_>(0) = \frac{1}{8\pi^2}\log b + O\!\left(\frac{m^2}{\Lambda^2}\right),
\qquad
\delta\lambda = -\frac{3\lambda^2}{16\pi^2}\log b,
\qquad
\beta_\lambda = +\frac{3\lambda^2}{16\pi^2} > 0,
$$

so the Gaussian fixed point is infrared-attractive and the ultraviolet flow ends at a Landau pole. Dimensional regularisation gives the same $1/(8\pi^2)$ coefficient from the $1/\epsilon$ pole, a cross-check of the regulator. In $d = 4-\epsilon$ the beta function acquires $-\epsilon\lambda$, and the **Wilson–Fisher** fixed point $\lambda^* = 16\pi^2\epsilon/3$ satisfies $\beta_\lambda(\lambda^*) = 0$ by direct substitution, with $\beta'_\lambda(\lambda^*) = +\epsilon > 0$ making it infrared-attractive. For a non-abelian gauge coupling the one-loop beta function is

$$
\beta_g = -\frac{g^3}{16\pi^2}\,b_0,
\qquad
b_0 = \frac{11}{3}C_2(G) - \frac{2}{3}\sum_{\text{Weyl}}T(r),
$$

which is **negative** for pure $SU(N)$, where $C_2(G) = N$ was recomputed from the structure constants for $SU(2)$ and $SU(3)$. The Gaussian fixed point is then ultraviolet-attractive — asymptotic freedom — with the threshold $N_f < 33/2$ for $SU(3)$, and the two-loop **Banks–Zaks** fixed point $g^{*2} = -16\pi^2 b_0/b_1$ satisfies $\beta_g(g^*) = 0$ exactly, giving $\alpha^* \approx 0.0416$ for $N_f = 16$. The scalar quartic and the abelian gauge coupling have one sign; the non-abelian coupling has the other.

Three gaps are left visible. First, the framework supplies no action, so the beta functions are transcribed rather than derived. Second, the regulator is external to the algebra: the algebra hosts the central invariant $\tilde{k}\bar{\tilde{k}}$ on which the cutoff is imposed, but not the cutoff, and dimensional regularisation leaves the four-dimensional algebra altogether. Third, the algebraically natural cutoff respects the two-sector decomposition but breaks gauge invariance, while the gauge-safe regulator does not live in the algebra; a biquaternionic gauge-invariant regulator, and the question of whether the two sectors may run at different rates, are open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; home of the scale, couplings, and beta functions |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace; image of the Wick rotation |
| $\tilde{k} = iE\,e_0 + \mathbf{p}$ | Wave biquaternion |
| $\tilde{k}\bar{\tilde{k}} = -p^2$ | Norm form; central; cutoff invariant |
| $k_E^2 = \tilde{k}\bar{\tilde{k}}$ (Euclidean) | Euclidean momentum squared |
| $\Lambda$, $b$, $\delta\ell = \log b$ | Cutoff, shell ratio, RG step toward the IR |
| $\mu$ | Renormalization scale |
| $\Gamma_k[\phi]$, $\Gamma_k^{(2)}$ | Wilsonian effective action and its second functional derivative |
| $R_k$ | Regulator function |
| $\partial_t\Gamma_k = \tfrac12\mathrm{Tr}[(\Gamma_k^{(2)}+R_k)^{-1}\partial_t R_k]$ | Wetterich exact flow equation; $\mathrm{Tr}$ is the functional trace |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Biquaternion trace (fiber trace), distinct from the functional trace |
| $\beta_i = \mu\,dg_i/d\mu$ | Beta function |
| $g^*$ | Fixed point, $\beta(g^*) = 0$ |
| $\lambda$ | Scalar quartic coupling, $(\lambda/4!)\phi^4$ |
| $\epsilon = 4-d$ | Dimensional-regularisation parameter |
| $g$ | Non-abelian gauge coupling |
| $b_0 = \tfrac{11}{3}C_2(G) - \tfrac{2}{3}\sum T(r)$ | One-loop gauge coefficient |
| $b_1 = 102 - \tfrac{38}{3}N_f$ (QCD) | Two-loop gauge coefficient |
| $C_2(G) = N$ for $SU(N)$ | Adjoint quadratic Casimir |
| $N_f$ | Number of Dirac quark flavours |
| $\lambda^* = 16\pi^2\epsilon/3$ | Wilson–Fisher fixed point |
| $g^{*2} = -16\pi^2 b_0/b_1$ | Banks–Zaks fixed point |

## Further Reading

- K. G. Wilson and J. Kogut, "The renormalization group and the $\epsilon$ expansion," *Physics Reports* **12** (1974) 75–199, for the momentum-shell RG and the $\epsilon$ expansion.
- K. G. Wilson, "The renormalization group: critical phenomena and the Kondo problem," *Reviews of Modern Physics* **47** (1975) 773–840, for the conceptual foundations.
- J. Polchinski, "Renormalization and effective Lagrangians," *Nuclear Physics B* **231** (1984) 269–295, for the exact Wilsonian flow equation and the role of the regulator.
- C. Wetterich, "Exact evolution equation for the effective potential," *Physics Letters B* **301** (1993) 90–94, for the exact flow equation used in the text.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the one-loop beta functions, dimensional regularisation, and the RG.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the renormalization of gauge theories and the scheme dependence of the running couplings.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the Wilson–Fisher fixed point and the renormalization group in $d = 4-\epsilon$.
- D. J. Gross and F. Wilczek, "Ultraviolet behavior of non-abelian gauge theories," *Physical Review Letters* **30** (1973) 1343–1346, and H. D. Politzer, "Reliable perturbative results for strong interactions?," *Physical Review Letters* **30** (1973) 1346–1349, for asymptotic freedom.
- T. Banks and A. Zaks, "On the phase structure of vector-like gauge theories with massless fermions," *Nuclear Physics B* **196** (1982) 189–204, for the two-loop fixed point.
- W. E. Caswell, "Asymptotic behavior of non-abelian gauge theories to two-loop order," *Physical Review Letters* **33** (1974) 244–246, for the two-loop coefficients.
- G. 't Hooft and M. Veltman, "Regularization and renormalization of gauge fields," *Nuclear Physics B* **44** (1972) 189–213, for dimensional regularisation.
- J. Cardy, *Scaling and Renormalization in Statistical Physics* (Cambridge, 1996), and N. Goldenfeld, *Lectures on Phase Transitions and the Renormalization Group* (Addison-Wesley, 1992), for the momentum-shell method used in the scalar computation.
- Companion articles: *The Path Integral in Biquaternionic Form*; *The Feynman Propagator in Biquaternionic Form*; *The Partition Function in Biquaternionic Form*; *The S-Matrix in Biquaternionic Form*; *The Gauge Principle in Biquaternionic Form*; *The Covariant Derivative and Gauge Connection in Biquaternionic Form*; *The Klein–Gordon Equation in Biquaternionic Form*; *The Wick Rotation in the Biquaternion Universe*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *The KMS Condition and the Biquaternion Framework*.
