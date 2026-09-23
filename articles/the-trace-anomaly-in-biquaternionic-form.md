# __The Trace Anomaly in Biquaternionic Form__

## Introduction

A theory that is classically invariant under a local rescaling of the metric has a stress tensor whose trace vanishes, and a quantised version of it generally does not. The equality $T^\mu{}_\mu = 0$ holds for the classical action of a massless field; the regulated one-loop effective action produces a non-vanishing trace, a **trace anomaly** (or **Weyl anomaly**), whose coefficient is fixed by the field content and whose form is fixed by the symmetries. The anomaly is not an artifact of a particular regulator: it is the obstruction to defining the regulated determinant in a way that preserves the classical symmetry, and it is the same obstruction that makes $\partial_\mu j^\mu_5 \neq 0$ for the axial current (Adler 1969; Bell and Jackiw 1969).

This article asks what the biquaternion framework contributes to that statement. The findings are the following.

1. **The quantum trace is a property of the determinant, not of the algebra.** The anomaly arises from the regularisation of $\log\det S''$, which is the object of *The Functional Determinant in Biquaternionic Form*. The divergence of that determinant is controlled by the heat-kernel coefficient $a_{d/2}$, and the anomalous trace is the conformal variation of the renormalised determinant. The algebra contributes neither the regularisation nor the divergence; it contributes the **operator on which the determinant is taken** and the **trace** that reads off the answer. This is the same division of labour the functional-integral and determinant articles record, and it is stated here at the outset so that the anomaly is not misattributed to the algebra.

2. **The framework's trace is a fixed pairing, and this is where the algebra enters.** The framework reads scalars off biquaternions with the trace pairing $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$, whose value on the unit is $\mathrm{Tr}(e_0)=2$. The anomaly coefficient counts the real components of the field, and the framework's component count is fixed by the algebra: a biquaternion field has four complex coefficients, hence eight real components, four per sector. The trace pairing and the level-1 norm form $\mathrm{diag}(+1,+1,+1,+1)$ are the two readings of that count, and they agree with each other exactly, as the verification below shows.

3. **The Weyl transformation is a level-1 statement, and it must not be confused with the $ict$ construction of the metric.** The framework obtains the Lorentzian signature from the level-1 form read on the material sector with the time coordinate written $ict$: the minus sign comes from $i^2 = -1$ alone, and the metric is an output rather than an input. A Weyl rescaling changes the level-1 form, and therefore changes the level-2 reading; it does not change the $ict$ assignment or the sector split. The anomaly is a statement about the level-1 form's variation under a rescaling, and it is the one place in this subcategory where a conformal rescaling of the primary convention is contemplated. The three levels are kept apart throughout.

4. **The anomaly's coefficient is multiplicity, and multiplicity is the only thing the algebra fixes.** For a free massless scalar the anomaly's coefficient is proportional to the number of real components; for the biquaternion scalar the count is fixed by the module and the sector split. This is a genuinely algebraic statement, and it is the same counting that the partition-function, functional-integral, and determinant articles make; it is *not* a claim that the biquaternion scalar is a multiplicity of complex scalars, for the reason those articles give.

5. **The anomaly and the $\theta$ vacuum are the two structural quantum effects of this group.** The trace anomaly is the failure of a *conformal* symmetry; the $\theta$ vacuum of the next article is the failure of a *topological* triviality. Both arise from the same place — the regularised determinant, and in particular its non-central part — and the determinant article's distinction between the central case (a determinant that factors) and the non-central case (a determinant with a phase) is what separates them. The trace anomaly is a central statement about a non-central operator; the $\theta$ vacuum is a statement about the phase that the non-central operator acquires.

The article proceeds as follows. The next section fixes what is meant by the trace and recalls the classical vanishing. A section derives the quantum trace from the conformal variation of the determinant, and a section evaluates the coefficient in two and four dimensions with the standard heat-kernel results. A section identifies the framework's trace pairing with the counting of components and verifies the agreement of the two readings. A section treats the Weyl transformation at the three metric levels and states what does and does not rescale. A section relates the anomaly to the renormalisation-group $\beta$ function of *The Renormalization Group in Biquaternionic Form*, and a section separates what is established from what is interpretation. The article closes with open questions.

**Conventions.** We use those of the companion articles, unchanged. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$; the cyclic products are $e_1e_2=e_3$ and its cyclic images. The sectors are $\mathbb{M}_-=\{ie_0,e_1,e_2,e_3\}_\mathbb{R}$ (anti-Hermitian, material) and $\mathbb{M}_+=\{e_0,ie_1,ie_2,ie_3\}_\mathbb{R}$ (Hermitian, informational), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ and $\mathbb{M}_-=i\mathbb{M}_+$. The trace is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ with $\mathrm{Sc}$ the real part of the $e_0$ coefficient, so that $\mathrm{Tr}(e_0)=2$. The material coordinate is $\tilde X=ict\,e_0+\mathbf{x}$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$; the d'Alembertian is the series $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial^2_{ict}+\Delta$. The level-1 norm form is the identity on $\mathbb{C}^4$, the primary convention; the Clifford metric $g$ is a level-3 tool and is not used here. These are the conventions of *Conventions in the Biquaternion Universe*, *The Functional Determinant in Biquaternionic Form*, and *The Generating Functional and the Effective Action in Biquaternionic Form*.

## The Classical Trace and Its Vanishing

The classical statement is fixed first, because the anomaly is the deviation from it.

**The stress tensor and its trace.** For a field theory with action $S[\Phi;g]$ on a background metric $g_{\mu\nu}$ the stress tensor is
$$
T^{\mu\nu} = \frac{2}{\sqrt{|g|}}\frac{\delta S}{\delta g_{\mu\nu}} ,
$$
and the trace is $T^\mu{}_\mu = g_{\mu\nu}T^{\mu\nu}$. A **Weyl transformation** is a local rescaling
$$
g_{\mu\nu}\;\longrightarrow\;e^{2\sigma(x)}g_{\mu\nu},
\qquad
\delta_\sigma g_{\mu\nu} = 2\sigma\,g_{\mu\nu},
$$
and the trace is exactly the response of the action to it:
$$
\delta_\sigma S = \int d^dx\,\sqrt{|g|}\;\sigma\,T^\mu{}_\mu .
$$
So $T^\mu{}_\mu=0$ is the statement that the classical action is Weyl invariant, and the anomaly is the statement that the quantum effective action is not.

**When the classical trace vanishes.** For a massless scalar with a conformal coupling, for the massless Dirac field in $d=4$, and for the Maxwell field, the classical action is Weyl invariant in the appropriate dimension, $T^\mu{}_\mu=0$ on shell. A mass term, a curvature coupling with non-critical coefficient, and a dimensionful coupling all break the invariance explicitly; those breakings are not anomalous, because they are already present classically and can be removed by a counterterm. The anomaly is the part that cannot.

**The improved tensor.** For a scalar in four dimensions the canonical tensor is not traceless even for the massless conformal action; adding the improvement term
$$
T^{\mu\nu}_{\mathrm{imp}} = T^{\mu\nu}_{\mathrm{can}} + \xi\big(\eta^{\mu\nu}\Box - \partial^\mu\partial^\nu\big)\phi^2 ,
\qquad
\xi=\tfrac16 ,
$$
produces $T^\mu{}_\mu=0$ classically. This is worth recording because it fixes the normalisation against which the quantum trace is measured: the anomaly is a statement about the improved tensor, and a calculation that omits the improvement term reports a classical trace instead of an anomaly.

**The $ict$ reading.** In the framework's coordinates the flat metric is the level-2 reading $\eta=\mathrm{diag}(-1,+1,+1,+1)$ of the level-1 form, obtained from $\tilde X=ict\,e_0+\mathbf{x}$ with the minus from $i^2$ alone. The trace $T^\mu{}_\mu$ is the contraction with $\eta$, and it is a level-2 object numerically while being a level-1 statement structurally. This is important for the Weyl transformation: a rescaling of the level-1 form is *not* a change of the $ict$ assignment, and the two operations are different. The section on the three levels makes this precise.

## The Quantum Trace as the Conformal Variation of the Determinant

The one-loop effective action is the determinant of the second variation, and the anomaly is its conformal variation.

**The one-loop trace.** From *The Generating Functional and the Effective Action in Biquaternionic Form* the one-loop effective action is
$$
\Gamma_1[\phi;g] = \tfrac12\,\mathrm{Tr}\log S''[\phi;g] ,
$$
with $S''$ the second variation of the classical action. Its response to a Weyl transformation is
$$
T^\mu{}_\mu\big|_{\text{one loop}} = \frac{1}{\sqrt{|g|}}g_{\mu\nu}\frac{\delta\Gamma_1}{\delta g_{\mu\nu}} ,
$$
and the anomaly is the statement that this is non-zero for a classically Weyl-invariant theory. In the path-integral language the same statement is that the measure $\mathcal{D}\Phi$ is not invariant under the rescaling, or equivalently that the regularised determinant is not; the two languages agree, and both are standard (Capper and Duff 1974; Deser, Duff, and Isham 1976; Duff 1994).

**The heat-kernel origin.** Regulating the determinant with a proper-time cutoff, the trace of the heat kernel has the small-$t$ expansion
$$
\mathrm{Tr}\,e^{-t\,S''}\;\sim\;\sum_{k\ge0} t^{(k-d)/2}\,a_k ,
$$
and the divergence that survives renormalisation is $a_{d/2}$, the Seeley–DeWitt coefficient of order $d/2$. The conformal variation of the regularised determinant is
$$
\delta_\sigma\Gamma_1 = \frac{1}{(4\pi)^{d/2}}\int d^dx\,\sqrt{|g|}\;\sigma\,a_{d/2} ,
$$
so that the anomalous trace is proportional to $a_{d/2}$. This is the standard heat-kernel account (DeWitt 2003; Vassilevich 2003), and it is the reason the anomaly is a one-loop, one-coefficient statement rather than a tower of terms: $a_{d/2}$ is local, and the higher coefficients are not.

**The algebra's role in the formula.** The heat kernel of $S''$ is taken on a space that the framework names. If $S''$ is a differential operator acting on a biquaternion-valued field, then the trace in $\mathrm{Tr}\,e^{-t S''}$ runs over the module, and the coefficient $a_{d/2}$ carries the module's multiplicity as an overall factor. The geometry of the operator supplies the curvature invariants; the algebra supplies the space on which the trace is taken. This is the same division as in the determinant article, and it is why the anomaly's *coefficient* — as opposed to its *form* — is the algebra's contribution.

## The Coefficients in Two and Four Dimensions

The standard values are recalled, and the multiplicity is exhibited.

**Two dimensions.** For a massless scalar field on a two-dimensional background the anomalous trace is
$$
T^\mu{}_\mu = \frac{c}{24\pi}\,R ,
$$
and the central charge is $c=1$ for a real scalar, $c=2$ for a complex scalar, and it is additive over decoupled fields. The value $c=1$ per real scalar is the standard one (Polyakov 1981), and it is proportional to the number of real components: the anomaly's coefficient counts components.

**Four dimensions.** In four dimensions the trace for a free field is a linear combination of the Euler density, the Weyl-square term, and $\Box R$:
$$
T^\mu{}_\mu = a\,E_4 + c\,W^2 + a'\,\Box R ,
$$
with $E_4$ the Euler density and $W$ the Weyl tensor. The coefficients $a$ and $c$ are fixed by the field content — the $a$-coefficient by the Euler term's contribution and the $c$-coefficient by the Weyl term's — and they too are additive over decoupled fields. For a scalar, a Dirac fermion, and a vector the standard values are tabulated (Duff 1994), and each is proportional to the field's internal multiplicity. The $\Box R$ term is scheme-dependent and is fixed by the choice of the renormalised coupling; the $a$ and $c$ terms are not.

**Multiplicity.** The pattern in both dimensions is that the anomaly coefficient is the sum over the field's internal components of each component's contribution, weighted by its spin. A field whose internal space is $n$-real-dimensional contributes $n$ times a single real component's coefficient, with a spin-dependent factor. The framework's task is therefore to fix $n$ for a biquaternion field and to say what the internal space is; that is the next section.

## The Framework's Trace and the Counting of Components

This is where the algebra enters, and it enters twice: through the trace pairing and through the norm form.

**The trace pairing.** The framework reads a number off a biquaternion with
$$
\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H),
\qquad
\mathrm{Tr}(e_0)=2 .
$$
The factor $2$ is the trace of the identity in the regular representation, and it is the algebraic origin of the "$2\,\mathrm{Sc}$" that recurs throughout the series. On the algebra regarded as a complex four-dimensional space the trace of the identity in the regular representation would be $4$; on the module $\mathbb{B}P_+(\hat{\boldsymbol\mu})\cong\mathbb{C}^2$, which is the space the determinant and the anomaly's trace are taken over, the trace is $2$. The two numbers are *not* interchangeable, and the anomaly's coefficient depends on which space the field is valued in; the determinant article's treatment of the module resolves which is meant in a given calculation.

**The level-1 norm form.** The primary convention is the norm form on $\mathbb{C}^4$,
$$
N(\tilde Q) = \sum_{\mu=0}^{3} Q_\mu^2 ,
\qquad
N = \mathrm{diag}(+1,+1,+1,+1),
$$
whose trace is $4$ over the complex four-dimensional algebra. This is the level-1 trace, and it counts the four complex coefficients. It is a *different* trace from the pairing above: one is the sum of the diagonal entries of the form on the complex four-dimensional algebra, the other is the trace of the identity in the regular representation on the module. They take the values $4$ and $2$ respectively, and their ratio is $\dim_\mathbb{C}\mathbb{B}/\dim_\mathbb{C}\text{module}=2$, which is the same $\mathrm{Tr}(e_0)=2$ read on the module. The two levels of counting are thus consistent and are not interchangeable, and the anomaly's coefficient uses the one appropriate to the space the field occupies.

**The component count.** A biquaternion field has four complex coefficients, equivalently eight real components, and the sector split assigns four real components to each sector. Two readings of that count are available, one on the module and one on the algebra, consistent through the ratio of the two dimensions:

- the regular-representation trace, $\mathrm{Tr}(e_0)=2$ on the module, with the module's complex dimension $2$;
- the level-1 norm form, whose trace over the algebra is $4$, with the algebra's complex dimension $4$.

The agreement is the identity $\dim_\mathbb{C}\mathbb{B} = 2\dim_\mathbb{C}\text{module}$, and it was checked below. The two readings are the two levels at which the framework counts, and the anomaly's coefficient uses the one appropriate to the space the field occupies.

**What the algebra does not fix.** The algebra fixes the multiplicity $n$ of the internal space; it does not fix the spin of the field, the background's curvature invariants, or the coefficients of $E_4$ and $W^2$. Those are the standard heat-kernel data and are transcribed. The framework's contribution is thus the identification of the internal space and its dimension, exactly as in the determinant article.

## The Weyl Transformation at the Three Metric Levels

The three levels of the word "metric" are the place where a spurious correction is most likely, and the Weyl transformation is where they interact.

**Level 1.** The norm form $N=\mathrm{diag}(+1,+1,+1,+1)$ on the complex coefficients is the framework's primary convention. A Weyl rescaling is a change of this form's normalisation, and the anomalous trace measures the response. The rescaling is *not* a change of the algebra, of the basis, or of the trace; it is a change of the one form, and it is the only object the anomaly's definition varies.

**Level 2.** The $ict$ coordinate metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$ is the level-1 form read on the material sector with the time coefficient written $ict$. A Weyl rescaling acts on this reading too — the level-2 metric is rescaled along with the level-1 form — but the $ict$ assignment is unchanged, and no minus sign in the anomaly formula is to be "corrected" on the basis of the level-1 form. The two levels are consistent by construction; the minus comes from $i^2$, not from the anomaly.

**Level 3.** The Clifford metric $g=\mathrm{diag}(+1,-1,-1,-1)$ of the $\gamma^\mu$ is a tool adopted where an article translates into gamma matrices. It enters the anomaly through the spin factor of a fermionic field's heat kernel — the Dirac operator's $a_{d/2}$ carries the spinor trace — and it does not dictate the framework's conventions. A calculation performed in the gamma-matrix language and a calculation performed with the biquaternion operators must agree on the anomaly, because the anomaly is a physical coefficient; where they appear to disagree it is the translation that is wrong, as the conventions article insists.

**What the transformation is not.** A Weyl rescaling is not a coordinate transformation (it changes distances without changing coordinates), not the Wick rotation (which is the identification of the material sector with the real-quaternion subspace and which changes the signature rather than the normalisation), and not a Lorentz transformation (which preserves the level-1 form). Keeping these apart is the content of the section.

## The Anomaly and the Renormalisation Group

The anomaly's coefficient and the running coupling's $\beta$ function are two readings of the same loop computation, and the corpus's renormalisation conventions fix how they are related.

**The relation.** For a coupling $g$ that multiplies a marginal operator, the anomalous trace is proportional to the $\beta$ function of the coupling:
$$
T^\mu{}_\mu \supset \frac{\beta(g)}{2g}\,O ,
$$
where $O$ is the operator multiplying the coupling. The relation is standard (the trace anomaly and the $\beta$ function are the same coefficient read in two ways), and it is the reason the anomaly is not removable by a counterterm: removing it would contradict the running that *The Renormalization Group in Biquaternionic Form* computes.

**Scheme dependence.** The $a$ and $c$ coefficients are scheme-independent in four dimensions; the coefficient of $\Box R$ is not, and it is adjusted by a finite local counterterm. The anomaly's scheme-independent part is therefore a genuine prediction of the field content, which is exactly what makes it a useful check on the framework's counting. A reader who finds a $\Box R$ coefficient differing between articles is looking at a scheme choice, not at a disagreement.

**The anomaly's one-loop exactness.** In a conformal theory the anomaly is one-loop exact: the higher loops do not add new terms of the anomalous form. This is the statement that $a_{d/2}$ is local and that the conformal variation of the determinant is exhausted by it, and it is standard. It is also the reason an anomaly computed at one loop in the framework is final, and it is worth stating because it is the exception rather than the rule for one-loop results.

**The non-central case.** Where the determinant does not factor — the chirality-off-diagonal Dirac mass, or any operator mixing the two minimal left ideals — the determinant acquires a phase, the eta invariant of the operator family, and the anomaly calculation acquires a topological contribution alongside the curvature one. That contribution is the subject of the next article, and the determinant article's central/non-central distinction is what separates them. The framework's statement is that the trace anomaly is the *central* statement (a scalar coefficient multiplying curvature invariants) while the $\theta$ vacuum is the *phase* statement, and that the two are read from the same determinant.

## The Proper-Time Expansion and the Coefficients

The anomaly's arithmetic comes from the heat-kernel expansion, and the framework's contribution is visible in it as a multiplicity.

**The one-loop effective action.** With $S''$ the second variation of the action about the background, the one-loop contribution is
$$
\Gamma_1 = \tfrac12\,\mathrm{Tr}\log S'' = -\tfrac12\int_0^\infty\frac{dt}{t}\,\mathrm{Tr}\,e^{-tS''}
$$
up to a divergent constant, the proper-time representation of the logarithm. The integrand is the heat kernel of $S''$, and its small-$t$ behaviour carries the anomaly.

**The heat-kernel expansion.** For a second-order operator on a $d$-dimensional manifold,
$$
\mathrm{Tr}\,e^{-tS''} \;\sim\; \frac{1}{(4\pi t)^{d/2}}\int d^dx\sqrt{g}\,\big(a_0+a_1t+a_2t^2+\cdots\big),
$$
with the Seeley–DeWitt coefficients $a_k$ built from the curvature and the operator's potential. The conformal transformation $g\to e^{2\Omega}g$ acts on the expansion through $\Omega$, and the term that survives in the trace is the one multiplying $a_{d/2}$: that is the origin of the anomalous trace,
$$
T^\mu{}_\mu = \frac{c}{24\pi}R \quad (d=2),
$$
with $c$ the central charge, and the corresponding combination of the curvature invariants in $d=4$. The identification $k=d/2$ is the exact reason the anomaly exists in even dimensions only.

**The coefficients, and the framework's multiplicity.** In $d=2$ the relevant coefficient is $a_1=R/6$, giving $c=1$ per real scalar; in $d=4$ the analogous coefficients give the standard $a$ and $c$ per field of each spin. The framework's contribution is the multiplicity: the trace runs over the module or the algebra, and the count is $\mathrm{Tr}(I)=2$ on the module and $4$ on the algebra, so a biquaternion-valued field contributes the corresponding multiple of the per-component coefficient. This is the same counting that the partition-function and harmonic-oscillator articles perform, and it is a count of components and not a multiplication of independent fields, for the reason those articles give. The finite-dimensional shadow of the whole construction was verified: for a complex $K$,
$$
\partial_s\log\det\big(e^{s}K\big)\big|_{s=0} = \dim ,
$$
obtained by finite differences as $3.99999\ldots$ for a $4\times4$ $K$ and $1.99999\ldots$ for a $2\times2$ $K$ — the dimension of the space is the coefficient of the conformal-like rescaling, which is the finite-dimensional image of "the anomaly's coefficient counts components".

**One-loop exactness.** The anomaly is not corrected beyond one loop: the Adler–Bardeen non-renormalisation theorem states that the anomalous coefficient is fixed by the one-loop result once the symmetry's breaking is fixed. This is standard and is recorded because it is what makes the anomaly a genuine structural quantity rather than a perturbative accident, and because it is the analogue, on the trace side, of the $\theta$ angle's topological exactness on the phase side.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**

- The Weyl transformation rescales the level-1 norm form and leaves the algebra, the basis, the $ict$ assignment, and the sector split unchanged; a rescaling is not the Wick rotation and not a Lorentz transformation.
- The framework's trace pairing is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ with $\mathrm{Tr}(e_0)=2$; the level-1 norm form has trace $4$ over the complex four-dimensional algebra; and the two readings are related by $\dim_\mathbb{C}\mathbb{B}/\dim_\mathbb{C}\text{module}=2$. Verified numerically: the trace of the identity in the module representation is exactly $2$, its trace in the regular representation on the algebra is exactly $4$, and for $\tilde Q=(0.7+0.2i,\,0.3-0.5i,\,-0.2+0.4i,\,0.1+0.6i)$ the $4\times4$ left-multiplication determinant is $0.0288000+0.0216000i$, equal to $N(\tilde Q)^2$ and to $(\det\Phi(\tilde Q))^2$.
- A biquaternion field has four complex coefficients, hence eight real components and four real components per sector; the anomaly's multiplicity is fixed by that count. This is a component count and not a multiplicity of complex scalars, for the reason *The Functional Integral in Biquaternionic Form*, *The Partition Function in Biquaternionic Form*, and *The Harmonic Oscillator in Biquaternionic Form* give.
- The conformal variation of a finite-dimensional Gaussian determinant is proportional to the dimension of the space, $\partial_s\log\det(e^{s}K)\big|_{s=0}=\dim$; verified by finite differences as $3.99999\ldots$ for a $4\times4$ complex $K$ and $1.99999\ldots$ for a $2\times2$ complex $K$, and the corresponding determinant derivative equals $\dim\cdot\det K$. This is the finite-dimensional shadow of the statement that the anomaly's coefficient counts components.

**Standard, and transcribed.**

- The definition of $T^{\mu\nu}$ as the metric variation of the action, the improvement term, and the classical vanishing of the trace.
- The one-loop trace as the conformal variation of $\log\det S''$; the heat-kernel expansion; the identification of $a_{d/2}$ as the anomalous coefficient.
- The values $c=1$ per real scalar in two dimensions and the four-dimensional $a$ and $c$ coefficients for scalar, fermion, and vector fields.
- The relation $T^\mu{}_\mu\supset\frac{\beta}{2g}O$, the scheme dependence of $\Box R$, and the one-loop exactness of the anomaly (Adler–Bardeen non-renormalisation).
- The proper-time representation $\Gamma_1=-\tfrac12\int_0^\infty\frac{dt}{t}\mathrm{Tr}\,e^{-tS''}$ and the small-$t$ expansion of the heat kernel, $\mathrm{Tr}\,e^{-tS''}\sim(4\pi t)^{-d/2}\int\sqrt g\,(a_0+a_1t+\cdots)$, with $k=d/2$ as the anomalous coefficient.

**Interpretation.**

- Reading the anomaly's coefficient as the algebra's multiplicity, with the geometry supplied by the heat kernel, is the framework's reading of the standard result; the standard result is not re-derived.
- Treating the trace anomaly and the $\theta$ vacuum as the two structural quantum effects of this subcategory is the organising reading of the anomaly-and-angle pair of this group.

**Open.**

- Whether the framework has a natural definition of the conformal coupling $\xi=\tfrac16$ beyond its transcription is not addressed here; the improvement term is used as in the standard theory.
- The anomaly of a genuinely non-central biquaternion operator, and whether its eta-invariant part has a framework-specific form, is left to the $\theta$-vacuum article.
- The scheme-independent coefficients of the biquaternion scalar and spinor fields are not computed here; only the counting that fixes them is identified.

## Summary

The trace anomaly in biquaternionic form is the standard anomaly with the framework's trace and component count. The classical trace vanishes for a Weyl-invariant action, and quantum mechanically the one-loop effective action $\Gamma_1=\tfrac12\mathrm{Tr}\log S''[\phi;g]$ has the conformal variation
$$
T^\mu{}_\mu\big|_{\text{one loop}} = \frac{1}{\sqrt{|g|}}g_{\mu\nu}\frac{\delta\Gamma_1}{\delta g_{\mu\nu}} = \frac{1}{(4\pi)^{d/2}}\,a_{d/2} ,
$$
proportional to the Seeley–DeWitt coefficient, which is local and one-loop exact. In two dimensions $T^\mu{}_\mu=\frac{c}{24\pi}R$ with $c$ counting real components; in four dimensions $T^\mu{}_\mu=aE_4+cW^2+a'\Box R$ with $a$ and $c$ fixed by the field content. The framework's contributions are the trace pairing $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ with $\mathrm{Tr}(e_0)=2$, the level-1 norm form with trace $4$, and the component count four complex and eight real; the two readings are related by $\dim_\mathbb{C}\mathbb{B}=2\dim_\mathbb{C}\text{module}$, verified numerically. The Weyl transformation rescales the level-1 form and nothing else, and the regularisation of the determinant, the curvature invariants, and the coefficients of $E_4$ and $W^2$ are standard and transcribed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | Level-1 norm form, $\mathrm{diag}(+1,+1,+1,+1)$; trace $4$ on $\mathbb{B}$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | Level-2 $ict$ metric; an output of $\tilde X=ict\,e_0+\mathbf{x}$ |
| $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial^2_{ict}+\Delta$ | Series d'Alembertian |
| $g_{\mu\nu}\to e^{2\sigma}g_{\mu\nu}$ | Weyl transformation; a level-1 rescaling |
| $T^{\mu\nu}=\frac{2}{\sqrt{\vert g\vert}}\frac{\delta S}{\delta g_{\mu\nu}}$ | Stress tensor |
| $\Gamma_1=\tfrac12\mathrm{Tr}\log S''$ | One-loop effective action whose variation is the anomaly |
| $a_{d/2}$ | Seeley–DeWitt coefficient controlling the anomalous trace |
| $c$, $a$ | Two- and four-dimensional anomaly coefficients |

## Further Reading

- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, for the axial anomaly and the origin of anomalous Ward identities.
- J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Il Nuovo Cimento A* **60** (1969) 47–61, for the independent discovery of the axial anomaly.
- D. M. Capper and M. J. Duff, "Trace anomalies in dimensional regularization," *Il Nuovo Cimento A* **23** (1974) 173–183, for the trace anomaly in dimensional regularisation.
- S. Deser, M. J. Duff, and C. J. Isham, "Non-local conformal anomalies," *Nuclear Physics B* **111** (1976) 45–55, for the structure of the conformal anomaly.
- M. J. Duff, "Twenty years of the Weyl anomaly," *Classical and Quantum Gravity* **11** (1994) 1387–1404, for the four-dimensional coefficients and their scheme independence.
- J. Wess and B. Zumino, "Consequences of anomalous Ward identities," *Physics Letters B* **37** (1971) 95–97, for the consistency conditions the anomaly satisfies.
- A. M. Polyakov, "Quantum geometry of bosonic strings," *Physics Letters B* **103** (1981) 207–210, for the two-dimensional anomaly and the central charge.
- B. S. DeWitt, *The Global Approach to Quantum Field Theory* (Oxford University Press, 2003), for the heat-kernel expansion and the Seeley–DeWitt coefficients.
- D. V. Vassilevich, "Heat kernel expansion: user's manual," *Physics Reports* **388** (2003) 279–360, for the heat-kernel coefficients used in the anomaly.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford University Press, 2002), for the renormalisation of the effective action and the trace anomaly.
- Companion articles: *The Functional Determinant in Biquaternionic Form*, for the regularised determinant whose variation is the anomaly; *The Generating Functional and the Effective Action in Biquaternionic Form*, for $\Gamma_1=\tfrac12\mathrm{Tr}\log S''$; *The Renormalization Group in Biquaternionic Form*, for the $\beta$ function the anomaly is read against; *Conventions in the Biquaternion Universe*, for the three metric levels and the trace pairing; *The Theta Vacuum in Biquaternionic Form*, for the phase of the non-central determinant; *The Partition Function in Biquaternionic Form* and *The Harmonic Oscillator in Biquaternionic Form*, for the sector reading of the component count.
