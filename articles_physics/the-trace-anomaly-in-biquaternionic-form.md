# __The Trace Anomaly in Biquaternionic Form__

## Introduction

A theory that is classically invariant under a local rescaling of the metric has a stress tensor whose trace vanishes, and a quantised version of it generally does not. The equality $T_\mu{}_\mu = 0$ holds for the classical action of a massless field; the regulated one-loop effective action produces a non-vanishing trace, a **trace anomaly** (or **Weyl anomaly**), whose coefficient is fixed by the field content and whose form is fixed by the symmetries. The anomaly is not an artifact of a particular regulator: it is the obstruction to defining the regulated determinant in a way that preserves the classical symmetry, and the axial current's $\langle\tilde\nabla,\tilde J_5\rangle_{\natural} \neq 0$ is the same failure of the measure read on the chiral current (Adler 1969; Bell and Jackiw 1969).

This article asks what the biquaternion framework contributes to that statement. The findings are the following.

1. **The quantum trace is a property of the determinant, not of the algebra.** The anomaly arises from the regularisation of $\log\det S^{(2)}$, which is the object of *The Functional Determinant in Biquaternionic Form*. The divergence of that determinant is controlled by the heat-kernel coefficient $a_{d/2}$, and the anomalous trace is the conformal variation of the renormalised determinant. The algebra contributes neither the regularisation nor the divergence; it contributes the **operator on which the determinant is taken** and the **trace** that reads off the answer. This is the same division of labour the functional-integral and determinant articles record, and it is stated here at the outset so that the anomaly is not misattributed to the algebra.

2. **The trace that computes an anomaly is the trace of the space the field lives in, and the framework's informational formula is that trace on the two-dimensional module.** The series defines the trace through the $2\times2$ image, $\operatorname{Tr}\tilde Q=\operatorname{tr}\mathsf M_2(\tilde Q)=2\,\mathrm{Sc}\,\tilde Q=2Q_t$, so that $\operatorname{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ and $\operatorname{Tr}(e_t)=2$. The trace of a biquaternion therefore sees only its scalar part, because the $2\times2$ image of a pure quaternion is traceless; that is a property of the trace and not a truncation of it. This is the trace on the module $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$, and it is the state-and-observable pairing of the Hermitian sector $\mathbb{M}_+$. A four-component Dirac field lives on the four-dimensional Dirac module, whose Clifford trace is $\operatorname{tr}L_aR_b=4\,\mathrm{Sc}(a)\,\mathrm{Sc}(b)$ with $\operatorname{tr}e_t=4$; that trace, not the informational one, is the trace the spinor anomaly uses. The anomaly coefficient counts the components of whichever space the trace runs over, and the count is fixed by the algebra: a biquaternion field has four complex coefficients, hence eight real components, four per sector, and the two module dimensions are related exactly by $\dim_\mathbb{C}\mathbb{B}=2\dim_\mathbb{C}\text{module}$. *Anomalies and Anomaly Cancellation in Biquaternionic Form* keeps the two traces apart; this article uses its separation.

3. **The Weyl transformation is a level-1 statement, and it must not be confused with the $ict'$ construction of the metric.** The framework obtains the Lorentzian signature from the level-1 form read on the material sector with the time coordinate written $ict'$: the minus sign is one use of $i^2=-1$, since $(ict')^2=-c^2t'^2$, and the metric is an output rather than an input. A Weyl rescaling changes the level-1 form, and therefore changes the level-2 interpretation; it does not change the $ict'$ assignment or the sector split. The anomaly is a statement about the level-1 form's variation under a rescaling, and it is the one place in this subcategory where a conformal rescaling of the primary convention is contemplated. The three levels are kept apart throughout.

4. **The coefficient has a fixed shape, and the algebra contributes only its multiplicity.** In four dimensions the trace is $(4\pi)^{-2}(cW^2-aE_4+b\Box R)$, with $a$ and $c$ rational and additive over fields; the spin weights of a scalar, a Dirac fermion, and a vector are $1:11:62$ for $a$ and $1:6:12$ for $c$. The algebra fixes how many copies of the per-component number a biquaternion field contributes, and it fixes nothing else: not the weights, not the curvature invariants, not the scheme-dependent $\Box R$. This is the same division the partition-function, functional-integral, and determinant articles make; it is *not* a claim that the biquaternion scalar is a multiplicity of complex scalars, for the reason those articles give.

5. **The anomaly and the $\theta$ vacuum are the two structural quantum effects of this group.** The trace anomaly is the failure of a *conformal* symmetry; the $\theta$ vacuum of the next article is the failure of a *topological* triviality. Both arise from the same place — the regularised determinant, and in particular its non-central part — and the determinant article's distinction between the central case (a determinant that factors) and the non-central case (a determinant with a phase) is what separates them. The trace anomaly is a central statement about a non-central operator; the $\theta$ vacuum is a statement about the phase that the non-central operator acquires.

The article proceeds as follows. The next section fixes what is meant by the trace and recalls the classical vanishing. A section derives the quantum trace from the conformal variation of the determinant and gives the heat-kernel origin of the coefficient, and a section evaluates the coefficient in two and four dimensions. A section identifies the trace of the space the field lives on with the counting of components, and a section treats the Weyl transformation at the three metric levels. A section relates the anomaly to the renormalisation-group $\beta$ function of *The Renormalization Group in Biquaternionic Form*, and a section records the proper-time representation and the finite-dimensional check of the counting. A section separates what is established from what is interpretation. *The Legacy Pauli Gamma Formulation* then records the Clifford dictionary used elsewhere in the series, and the summary, the notation table, and the literature close the article.

## The Classical Trace and Its Vanishing

The classical statement is fixed first, because the anomaly is the deviation from it.

**The stress tensor and its trace.** For a field theory with action $S[\Phi;g]$ on a background metric $g_{\mu\nu}$ the stress tensor is
$$
T_{\mu\nu} = \frac{2}{\sqrt{|g|}}\frac{\delta S}{\delta g_{\mu\nu}} ,
$$
with both indices low, the variation being taken in the components $g_{\mu\nu}$ and no index raised, and the trace is the contraction $T_\mu{}_\mu = g_{\mu\nu}T_{\mu\nu}$. A **Weyl transformation** is a local rescaling
$$
g_{\mu\nu}\;\longrightarrow\;\exp(2\sigma(x))g_{\mu\nu},
\qquad
\delta_\sigma g_{\mu\nu} = 2\sigma\,g_{\mu\nu},
$$
and the trace is exactly the response of the action to it:
$$
\delta_\sigma S = \int d^dx\,\sqrt{|g|}\;\sigma\,T_\mu{}_\mu .
$$
So $T_\mu{}_\mu=0$ is the statement that the classical action is Weyl invariant, and the anomaly is the statement that the quantum effective action is not.

**When the classical trace vanishes.** For a massless scalar with the conformal coupling $\xi=(d-2)/(4(d-1))$, for the massless Dirac field, and for the Maxwell field in $d=4$, the classical action is Weyl invariant, and $T_\mu{}_\mu=0$ on shell. A mass term, a curvature coupling with non-critical coefficient, and a dimensionful coupling all break the invariance explicitly; those breakings are not anomalous, because they are already present classically and their coefficients are fixed by the classical action rather than by the regulator. The anomaly is the part that cannot be removed.

**The improved tensor.** For a scalar the canonical tensor is not traceless even for the massless action at the conformal coupling; adding the improvement term
$$
T_{\mu\nu}^{\mathrm{imp}} = T_{\mu\nu}^{\mathrm{can}} + \xi\big(g_{\mu\nu}\Box - \nabla_\mu\nabla_\nu\big)\phi^2 ,
\qquad
\xi=\frac{d-2}{4(d-1)},
$$
produces $T_\mu{}_\mu=0$ on shell, the bracket reducing to $g_{\mu\nu}[\mathbb{M}_-]\partial^2-\partial^2/\partial x_\mu\partial x_\nu$ in flat coordinates. The arithmetic is short. The added trace is $\xi(d-1)\Box\phi^2$, which on shell is $2\xi(d-1)(\partial\phi)^2$ because $\Box\phi^2=2(\partial\phi)^2+2\phi\,\Box\phi$ and the second term vanishes for a massless field; the canonical trace is $-\tfrac{d-2}{2}(\partial\phi)^2$; and $\xi=(d-2)/(4(d-1))$ is exactly the value that cancels the two, giving $\xi=\tfrac16$ at $d=4$. This is worth recording because it fixes the normalisation against which the quantum trace is measured: the anomaly is a statement about the improved tensor, and a calculation that omits the improvement term reports a classical trace instead of an anomaly.

**The $ict'$ interpretation.** In the framework's coordinates the flat metric is the level-2 interpretation $g_{\mu\nu}[\mathbb{M}_-]$ of the level-1 form, obtained from $\tilde{R}=ict'\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, where $(ict')^2=i^2c^2t'^2=-c^2t'^2$. The trace $T_\mu{}_\mu$ is the contraction with $\eta$, and it is a level-2 object numerically while being a level-1 statement structurally. This is important for the Weyl transformation: a rescaling of the level-1 form is *not* a change of the $ict'$ assignment, and the two operations are different. The section on the three levels makes this precise.

## The Quantum Trace as the Conformal Variation of the Determinant

The one-loop effective action is the determinant of the second variation, and the anomaly is its conformal variation.

**The one-loop trace.** From *The Generating Functional and the Effective Action in Biquaternionic Form* the one-loop effective action is
$$
\Gamma_1[\phi;g] = \tfrac12\,\operatorname{Tr}\log S^{(2)}[\phi;g] ,
$$
with $S^{(2)}$ the second variation of the classical action. Its response to a Weyl transformation is
$$
T_\mu{}_\mu\big|_{\text{one loop}} = \frac{2}{\sqrt{|g|}}g_{\mu\nu}\frac{\delta\Gamma_1}{\delta g_{\mu\nu}} ,
$$
and the anomaly is the statement that this is non-zero for a classically Weyl-invariant theory. In the path-integral language the same statement is that the measure $\mathcal{D}\Phi$ is not invariant under the rescaling, or equivalently that the regularised determinant is not; the two languages agree, and both are standard (Capper and Duff 1974; Deser, Duff, and Isham 1976; Duff 1994).

**The heat-kernel origin.** Regulating the determinant with a proper-time cutoff, the trace of the heat kernel has the small-$t'$ expansion
$$
\operatorname{Tr}\,\exp(-t'\,S^{(2)})\;\sim\;\frac{1}{(4\pi t')^{d/2}}\sum_{k\ge0}{t'}^{k}\int d^dx\,\sqrt{|g|}\,a_k ,
$$
where $a_k$ is the Seeley–DeWitt coefficient of order $k$, the first being $a_0=1$. The term that survives renormalisation is $a_{d/2}$, because ${t'}^{k-d/2}$ is logarithmically divergent exactly at $k=d/2$. The conformal variation of the regularised determinant is
$$
\delta_\sigma\Gamma_1 = \frac{1}{(4\pi)^{d/2}}\int d^dx\,\sqrt{|g|}\;\sigma\,a_{d/2} ,
$$
so that the anomalous trace is proportional to $a_{d/2}$; the proportionality is what the boxed coefficients below encode. This is the standard heat-kernel account (DeWitt 2003; Vassilevich 2003), and it is the reason the anomaly is a one-loop, one-coefficient statement rather than a tower of terms: $a_{d/2}$ is local, and the higher coefficients are not.

**The algebra's role in the formula.** The heat kernel of $S^{(2)}$ is taken on a space that the framework names. If $S^{(2)}$ is a differential operator acting on a biquaternion-valued field, then the trace in $\operatorname{Tr}\,\exp(-t' S^{(2)})$ runs over the module, and the coefficient $a_{d/2}$ carries the module's multiplicity as an overall factor. The geometry of the operator supplies the curvature invariants; the algebra supplies the space on which the trace is taken. This is the same division as in the determinant article, and it is why the anomaly's *multiplicity* — as opposed to its *form* — is the algebra's contribution.

## The Coefficients in Two and Four Dimensions

The standard values are recalled, and the multiplicity is exhibited.

**Two dimensions.** For a massless scalar field on a two-dimensional background the anomalous trace is
$$
\boxed{\;T_\mu{}_\mu = \frac{c}{24\pi}\,R\;},
$$
and the central charge is $c=1$ for a real scalar, $c=2$ for a complex scalar, and it is additive over decoupled fields. The coefficient is the Seeley–DeWitt value $a_1=R/6$ of the minimal scalar, since $\frac{1}{4\pi}a_1=R/(24\pi)$; the value $c=1$ per real scalar is the standard one (Polyakov 1981), and it is proportional to the number of real components: the anomaly's coefficient counts components.

**Four dimensions.** In four dimensions the trace for a free field is a linear combination of the Euler density, the Weyl-square term, and $\Box R$:
$$
\boxed{\;T_\mu{}_\mu = \frac{1}{(4\pi)^2}\big(c\,W^2 - a\,E_4 + b\,\Box R\big)\;},
$$
with $E_4=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}-4R_{\mu\nu}R^{\mu\nu}+R^2$ the Euler density and $W^2=W_{\mu\nu\rho\sigma}W^{\mu\nu\rho\sigma}$ the Weyl-square term; the minus on the Euler density is the convention of Duff's review, and a text that writes $+aE_4$ defines $a$ with the opposite sign. In that convention the coefficients are rational functions of the field content,
$$
a=\frac{1}{90}\big(n_s+11n_f+62n_v\big),
\qquad
c=\frac{1}{120}\big(n_s+6n_f+12n_v\big),
$$
for $n_s$ real scalars, $n_f$ Dirac fermions, and $n_v$ vector fields: $a=\tfrac{1}{90},\tfrac{11}{90},\tfrac{62}{90}$ and $c=\tfrac{1}{120},\tfrac{1}{20},\tfrac{1}{10}$ for one field of each kind. Both are additive over decoupled fields, and both are independent of the renormalised coupling. The symbol $c$ here is the Weyl-square coefficient and is not the two-dimensional central charge of the previous paragraph; the two share a letter in the literature and nothing else. The $\Box R$ term is the exception to scheme independence: its coefficient is moved by a finite local counterterm, so only $a$ and $c$ are predictions of the field content.

**Multiplicity.** The pattern in both dimensions is that the anomaly coefficient is the sum over the field's internal components of each component's contribution, weighted by its spin. A field whose internal space is $n$-real-dimensional contributes $n$ times a single real component's coefficient, with the spin weight read off the ratios above: $1:11:62$ for $a$ and $1:6:12$ for $c$. The framework's task is therefore to fix $n$ for a biquaternion field and to say what the internal space is; that is the next section.

## The Framework's Trace and the Counting of Components

This is where the algebra enters, and it enters twice: through the operator trace of the space the field lives on and through the biquaternion norm.

**The trace of one element.** The series defines the trace of a single biquaternion through its $2\times2$ image:
$$
\operatorname{Tr}\tilde Q=\operatorname{Tr}\mathsf M_2(\tilde Q)=2\,\mathrm{Sc}\,\tilde Q=2Q_t,
\qquad
\operatorname{Tr}(e_t)=2,
$$
and applying it to a product gives the formula the corpus quotes,
$$
\boxed{\;\operatorname{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)\;}.
$$
The factor $2$ is forced by $\mathsf M_2(e_t)=I_2$ and cannot be divided out. The trace of any biquaternion sees only its scalar part, because the $2\times2$ image of a pure quaternion is traceless; that is a property of the matrix trace, not a truncation of the functional. On the module $\mathbb{B}\tilde\Pi(\vec u)\cong\mathbb{C}^2$, of complex dimension $2$, this *is* the operator trace, and it is the pairing used for expectation values in $\mathbb{M}_+$.

**The trace that computes an anomaly.** A four-component field lives on the four-dimensional Dirac module, and the trace that computes its anomaly is the Clifford trace there,
$$
\operatorname{tr}L_aR_b=4\,\mathrm{Sc}(a)\,\mathrm{Sc}(b),
\qquad
\operatorname{tr}e_t=4 .
$$
The contrast with the display above is the whole distinction: the informational formula is a trace over a two-dimensional space, the Clifford trace is a trace over a four-dimensional one, and each counts the components of its own space. Substituting one for the other is the category error *Anomalies and Anomaly Cancellation in Biquaternionic Form* names, and the determinant article's treatment of the module fixes which of the two a given calculation uses.

**The level-1 biquaternion norm.** The primary convention is the quaternionic norm on the four complex coefficients,
$$
\langle\tilde Q\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2 ,
\qquad
N = \mathrm{diag}(+1,+1,+1,+1),
$$
a bilinear form on the algebra $\mathbb{C}^4$, not a trace on a module. It has four complex coefficients, which is why the algebra has complex dimension $4$. It is a *different object* from the two traces above: those are traces of products of elements, and this is the diagonal of a form on the algebra. The dimensions are related by the algebra's action on the module, $\mathbb{B}\cong M_2(\mathbb{C})$ acting on $\mathbb{C}^2$, so that $\dim_\mathbb{C}\mathbb{B}=2\dim_\mathbb{C}\text{module}$ and the ratio $4/2$ is exactly $\operatorname{Tr}(e_t)$. The relation is an identity of dimensions, not a numerical coincidence, and the three objects remain distinct.

**The component count.** A biquaternion field has four complex coefficients, equivalently eight real components, and the sector split assigns four real components to each sector. Two traces of an identity are available, and the ratio of the two dimensions relates them:

- the trace on the module, $\operatorname{Tr}(e_t)=2$, with $\dim_\mathbb{C}\text{module}=2$;
- the Clifford trace on the Dirac module, $\operatorname{tr}e_t=4$, whose space has complex dimension $4$ — the same number as the algebra's dimension, because the algebra acts on it faithfully.

The relation $\dim_\mathbb{C}\mathbb{B}=2\dim_\mathbb{C}\text{module}$ is exact, and the finite-dimensional check below verifies the counting in the determinant language. The field's eight real components and the module's two complex dimensions are different counts: the first is the size of the field space, the second the size of the fibre on which the determinant is taken. The anomaly's coefficient uses the trace of the space the field occupies, and that is the whole of the algebra's contribution to it.

**What the algebra does not fix.** The algebra fixes the multiplicity $n$ of the internal space; it does not fix the spin of the field, the background's curvature invariants, or the coefficients of $E_4$ and $W^2$. Those are the standard heat-kernel data and are transcribed. The framework's contribution is thus the identification of the internal space and its dimension, exactly as in the determinant article.

## The Weyl Transformation at the Three Metric Levels

The three levels of the word "metric" are the place where a spurious correction is most likely, and the Weyl transformation is where they interact.

**Level 1.** The biquaternion norm $N=\mathrm{diag}(+1,+1,+1,+1)$ on the complex coefficients is the framework's primary convention. A Weyl rescaling is a change of this form's normalisation, and the anomalous trace measures the response. The rescaling is *not* a change of the algebra, of the basis, or of the trace; it is a change of the one form, and it is the only object the anomaly's definition varies.

**Level 2.** The $ict'$ coordinate metric $g_{\mu\nu}[\mathbb{M}_-]$ is the level-1 form read on the material sector with the time coefficient written $ict'$:
$$
\langle\tilde R\rangle_{\natural}=(ict')^2+x^2+y^2+z^2=-c^2t'^2+x^2+y^2+z^2 .
$$
The minus is one use of $i^2=-1$ and nothing else. A Weyl rescaling acts on this interpretation too — the level-2 metric is rescaled along with the level-1 form — but the $ict'$ assignment is unchanged, and no minus sign in the anomaly formula is to be "corrected" on the basis of the level-1 form. The two levels are consistent by construction; the minus comes from $i^2$, not from the anomaly.

**Level 3.** The Clifford tool, whose four generators carry the frame metric $\mathrm{diag}(-1,+1,+1,+1)$, is a translation of the algebra adopted where an article writes in a Clifford frame; it is set out once in *The Legacy Pauli Gamma Formulation* below and is not a convention of the body. The tool enters the anomaly through the spin factor of a fermionic field's heat kernel, where the Dirac operator's $a_{d/2}$ carries the spinor trace, and it does not dictate the framework's conventions. A calculation performed in the Clifford frame and a calculation performed with the biquaternion operators must agree on the anomaly, because the anomaly is a physical coefficient; where they appear to disagree it is the translation that is wrong, as the conventions article insists.

**What the transformation is not.** A Weyl rescaling is not a coordinate transformation, since it changes distances without changing coordinates; not the Wick rotation, which in this series is either the exchange of the real and imaginary sectors or the continuation $t'\mapsto-i\tau$ of one coordinate, and which rotates rather than rescales all of them; and not a Lorentz transformation, which preserves the level-1 form. Keeping these apart is the content of the section.

## The Anomaly and the Renormalisation Group

The anomaly's coefficient and the running coupling's $\beta$ function are two interpretations of the same loop computation, and the corpus's renormalisation conventions fix how they are related.

**The relation.** For a coupling $g$ that multiplies a marginal operator, the anomalous trace is proportional to the $\beta$ function of the coupling:
$$
T_\mu{}_\mu \supset \frac{\beta(g)}{2g}\,O ,
$$
where $O$ is the operator multiplying the coupling. The relation is standard (the trace anomaly and the $\beta$ function are the same coefficient read in two ways), and it is the reason the anomaly is not removable by a counterterm: removing it would contradict the running that *The Renormalization Group in Biquaternionic Form* computes.

**Scheme dependence.** The $a$ and $c$ coefficients are scheme-independent in four dimensions; the coefficient of $\Box R$ is not, and it is adjusted by a finite local counterterm. The anomaly's scheme-independent part is therefore a genuine prediction of the field content, which is exactly what makes it a useful check on the framework's counting. A reader who finds a $\Box R$ coefficient differing between articles is looking at a scheme choice, not at a disagreement.

**The anomaly's one-loop exactness.** In a conformal theory the anomaly is one-loop exact: the higher loops do not add new terms of the anomalous form. This is the statement that $a_{d/2}$ is local and that the conformal variation of the determinant is exhausted by it, and it is standard. It is also the reason an anomaly computed at one loop in the framework is final, and it is worth stating because it is the exception rather than the rule for one-loop results.

**The non-central case.** Where the determinant does not factor — the chirality-off-diagonal Dirac mass, or any operator mixing the two minimal left ideals — the determinant acquires a phase, the eta invariant of the operator family. The trace anomaly remains the curvature statement; the phase is its topological partner, and the $\theta$ vacuum is what reads it. The mass term is the one-sided pair
$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$
on the algebra, and the two-sided cell equation
$$
(\mathbb{D}-m)\psi=0,\qquad \mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial t'}-\sum_{k}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial Q_k},
$$
on the module. These are the two Dirac equations of the series: the pair is the one-sided statement, the cell equation is its two-sided representative, and only the second carries a chirality. The phase, and not the curvature coefficient, is the subject of the next article, and the determinant article's central/non-central distinction is what separates them. The framework's statement is that the trace anomaly is the *central* statement (a scalar coefficient multiplying curvature invariants) while the $\theta$ vacuum is the *phase* statement, and that the two are read from the same determinant.

## The Proper-Time Representation and the Finite-Dimensional Check

Two details of the derivation are recorded here: the proper-time form of the one-loop action and the finite-dimensional identity that isolates the component count.

**The one-loop effective action.** With $S^{(2)}$ the second variation of the action about the background, the one-loop contribution is
$$
\Gamma_1 = \tfrac12\,\operatorname{Tr}\log S^{(2)} = -\tfrac12\int_0^\infty\frac{dt'}{t'}\,\operatorname{Tr}\,\exp(-t'S^{(2)}),
$$
up to a divergent constant, the proper-time representation of the logarithm. The integrand is the heat kernel of $S^{(2)}$; its small-$t'$ expansion is the one given in the section on the quantum trace, and the term $a_{d/2}$ of that expansion is the anomalous coefficient. This is where the anomaly's arithmetic comes from, and the framework's contribution is visible in it as the multiplicity of the trace.

**The finite-dimensional shadow.** The counting that fixes the coefficient is visible in a Gaussian integral. For a complex $K$ on an $n$-dimensional space,
$$
\det\big(\exp(s)K\big)=e^{ns}\det K,
\qquad
\frac{\partial}{\partial s}\log\det\big(\exp(s)K\big)\Big|_{s=0}=n,
\qquad
\frac{\partial}{\partial s}\det\big(\exp(s)K\big)\Big|_{s=0}=n\det K .
$$
The first identity is exact, so the second and third are exact; a central difference with $h=10^{-6}$ returns $2$ for a $2\times2$ $K$ and $4$ for a $4\times4$ $K$ to ten digits. The dimension of the space is the coefficient of the conformal-like rescaling, which is the finite-dimensional image of "the anomaly's coefficient counts components". The count is $2$ on the module and $4$ on the algebra and on the Dirac module, and the numbers are related as in the section on the counting of components.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**

- The Weyl transformation rescales the level-1 biquaternion norm and leaves the algebra, the basis, the $ict'$ assignment, and the sector split unchanged; a rescaling is not the Wick rotation and not a Lorentz transformation.
- The trace of a biquaternion is the $2\times2$ trace, $\operatorname{Tr}\tilde Q=2\,\mathrm{Sc}\,\tilde Q$, so that $\operatorname{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ and $\operatorname{Tr}(e_t)=2$; it is the trace on the two-dimensional module, while the Clifford trace on the four-dimensional Dirac module is $\operatorname{tr}L_aR_b=4\,\mathrm{Sc}(a)\,\mathrm{Sc}(b)$ with $\operatorname{tr}e_t=4$. The two numbers are related by $\dim_\mathbb{C}\mathbb{B}=2\dim_\mathbb{C}\text{module}=4$, and neither trace is a truncation of the other: they run over spaces of different dimension.
- A field valued on the algebra has four complex coefficients, hence eight real components and four per sector; a field valued on the module has two complex coefficients, four real. The anomaly's multiplicity is the dimension of whichever of the two spaces the determinant is taken over, and it is a component count and not a multiplicity of complex scalars, for the reason *The Functional Integral in Biquaternionic Form*, *The Partition Function in Biquaternionic Form*, and *The Harmonic Oscillator in Biquaternionic Form* give.
- The conformal variation of a finite-dimensional Gaussian determinant is proportional to the dimension of the space, $\partial/\partial s\,\log\det(\exp(s)K)\big|_{s=0}=\dim$; the identity is exact, and a central difference returns $4$ for a $4\times4$ complex $K$ and $2$ for a $2\times2$ complex $K$ to ten digits, with the determinant derivative equal to $\dim\cdot\det K$. This is the finite-dimensional shadow of the statement that the anomaly's coefficient counts components.

**Standard, and transcribed.**

- The definition of $T_{\mu\nu}$ as the metric variation of the action, the improvement term, and the classical vanishing of the trace.
- The one-loop trace as the conformal variation of $\log\det S^{(2)}$; the heat-kernel expansion; the identification of $a_{d/2}$ as the anomalous coefficient.
- The values $c=1$ per real scalar in two dimensions and the four-dimensional $a$ and $c$ coefficients for scalar, fermion, and vector fields.
- The relation $T_\mu{}_\mu\supset\frac{\beta}{2g}O$, the scheme dependence of $\Box R$, and the one-loop exactness of the anomaly (Adler–Bardeen non-renormalisation).
- The proper-time representation $\Gamma_1=-\tfrac12\int_0^\infty\frac{dt'}{t'}\operatorname{Tr}\,\exp(-t'S^{(2)})$ and the small-$t'$ expansion of the heat kernel, $\operatorname{Tr}\,\exp(-t'S^{(2)})\sim(4\pi t')^{-d/2}\int\sqrt g\,(a_0+a_1t'+\cdots)$, with $k=d/2$ as the anomalous coefficient.

**Interpretation.**

- Reading the anomaly's coefficient as the algebra's multiplicity, with the geometry supplied by the heat kernel, is the framework's interpretation of the standard result; the standard result is not re-derived.
- Treating the trace anomaly and the $\theta$ vacuum as the two structural quantum effects of this subcategory is the organising interpretation of the anomaly-and-angle pair of this group.

**Open.**

- Whether the framework has a natural definition of the conformal coupling $\xi=\tfrac16$ beyond its transcription is not addressed here; the improvement term is used as in the standard theory.
- The anomaly of a genuinely non-central biquaternion operator, and whether its eta-invariant part has a framework-specific form, is left to the $\theta$-vacuum article.
- The scheme-independent coefficients of the biquaternion scalar and spinor fields are not computed here; only the counting that fixes them is identified.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gamma symbols are used only in this section; every other section writes the same objects as cells. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a separate algebra.

Here $L_a\psi=a\psi$ and $R_b\psi=\psi b$ are the left and right multiplications, and $L_aR_b$ is the two-sided cell, $L_aR_b\psi=a\psi b$. The five reference cells are
$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

**The squares are uses of $i^2=-1$.** Each generator carries two factors of $i$ when it is squared, and the sign is the product of those two with the signs of the two multiplications:
$$
(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})^2=i^2(L_{e_t}^{\mathrm{pau}})^2(R_{\vec e_x}^{\mathrm{pau}})^2=(-1)(+1)(-1)=+e_t,
$$

In the axis-free display:

$$
(iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}})^2=i^2(L_{e_t}^{\mathrm{axf}})^2(R_{\vec e_x}^{\mathrm{axf}})^2=(-1)(+1)(-1)=+e_t,
$$

$$
(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^2=i^2(L_{\vec e_k}^{\mathrm{pau}})^2(R_{\vec e_y}^{\mathrm{pau}})^2=(-1)(-1)(-1)=-e_t,
$$

The same identities in the axis-free display:

$$
(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=i^2(L_{\vec e_k}^{\mathrm{axf}})^2(R_{\vec e_y}^{\mathrm{axf}})^2=(-1)(-1)(-1)=-e_t,
$$

for $k=x,y,z$, so the four generators carry the metric $g_{\mu\nu}[\mathbb{M}_-]=\mathrm{diag}(-1,+1,+1,+1)$ and $\gamma_5[\mathbb{M}_-]^2=+e_t$. The anticommutators carry the same metric, $\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ with $I_4=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ the identity on the module, and $\gamma_5[\mathbb{M}_-]$ anticommutes with the four generators. The product of the four is a cell, and the chirality is its multiple,
\qquad \varepsilon=(1,-1,-1,-1),$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{pau}},
\qquad
\gamma_5[\mathbb{M}_-]=+i\,\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{pau}},
$$

Read in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{axf}},
\qquad
\gamma_5[\mathbb{M}_-]=+i\,\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{axf}},
$$

the sign convention in which $\gamma_5[\mathbb{M}_-]^2=+e_t$; the opposite sign is an equally good chirality and differs only by which of the two chiralities is called left.

**Chirality is the right multiplication.** Because $L_{e_t}^{\mathrm{pau}}$ is the identity, $\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=-iR_{\vec e_z}^{\mathrm{pau}}$: the chirality is a pure right multiplication, and it is the one cell the one-sided pair displayed above cannot contain, because that pair uses left multiplications only. The two-sided representative does contain it, and the chiral halves of the module decouple because it anticommutes with the operator:
$$
\{\gamma_5[\mathbb{M}_-],\mathbb{D}\}=0,\qquad \gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{pau}}.
$$

The same expressions, in the axis-free display:

$$
\{\gamma_5[\mathbb{M}_-],\mathbb{D}\}=0,\qquad \gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{axf}}.
$$

That anticommutator is the algebraic content of "only the two-sided equation carries a chirality": a cell built from left multiplications alone could not produce it.

**The trace.** The trace of a product is a linear functional on cells, $\operatorname{tr}L_aR_b=4\,\mathrm{Sc}(a)\,\mathrm{Sc}(b)$ on the four-dimensional module, so a spinor trace is a product of scalar parts and $\operatorname{tr}e_t=4$. On the two-dimensional module the same cell has trace $2\,\mathrm{Sc}(ab)$, which is the informational formula of the body; the numbers $2$ and $4$ are the dimensions of the two spaces, not two normalisations of one trace. The dictionary is complex-linear: over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The trace anomaly in biquaternionic form is the standard anomaly with the framework's trace and component count. The classical trace vanishes for a Weyl-invariant action, and quantum mechanically the one-loop effective action $\Gamma_1=\tfrac12\operatorname{Tr}\log S^{(2)}[\phi;g]$ has the conformal variation
$$
\boxed{\;T_\mu{}_\mu\big|_{\text{one loop}} = \frac{2}{\sqrt{|g|}}g_{\mu\nu}\frac{\delta\Gamma_1}{\delta g_{\mu\nu}} = \frac{1}{(4\pi)^{d/2}}\,a_{d/2}\;},
$$
proportional to the Seeley–DeWitt coefficient, which is local and one-loop exact. In two dimensions $T_\mu{}_\mu=\frac{c}{24\pi}R$ with $c$ counting real components; in four dimensions $T_\mu{}_\mu=\frac{1}{(4\pi)^2}(cW^2-aE_4+b\Box R)$ with $a$ and $c$ fixed by the field content. The framework's contributions are the trace on the module, $\operatorname{Tr}(e_t)=2$, the Clifford trace on the Dirac module, $\operatorname{tr}e_t=4$, the level-1 norm with $\dim_\mathbb{C}\mathbb{B}=4$, and the component count four complex and eight real; the two module dimensions are related exactly by $\dim_\mathbb{C}\mathbb{B}=2\dim_\mathbb{C}\text{module}$, and the counting is checked in finite dimension by $\frac{\partial}{\partial s}\log\det(e^sK)\big|_{s=0}=\dim K$. The Weyl transformation rescales the level-1 form and nothing else, and the regularisation of the determinant, the curvature invariants, and the coefficients of $E_4$ and $W^2$ are standard and transcribed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\operatorname{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace on the two-dimensional module; $\operatorname{Tr}(e_t)=2$; the $\mathbb{M}_+$ pairing |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | Level-1 quaternionic norm, $\mathrm{diag}(+1,+1,+1,+1)$; $\dim_\mathbb{C}\mathbb{B}=4$ |
| $g_{\mu\nu}[\mathbb{M}_-]$ | Level-2 $ict'$ metric; an output of $\tilde{R}=ict'\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial Q_t^2+\Delta$ | Series d'Alembertian |
| $g_{\mu\nu}\to \exp(2\sigma)g_{\mu\nu}$ | Weyl transformation; a level-1 rescaling |
| $T_{\mu\nu}=\frac{2}{\sqrt{\vert g\vert}}\frac{\delta S}{\delta g_{\mu\nu}}$ | Stress tensor |
| $\Gamma_1=\tfrac12\operatorname{Tr}\log S^{(2)}$ | One-loop effective action whose variation is the anomaly |
| $a_{d/2}$ | Seeley–DeWitt coefficient controlling the anomalous trace |
| $\xi=(d-2)/(4(d-1))$ | Improvement coupling; $\xi=1/6$ at $d=4$ |
| $\operatorname{tr}L_aR_b=4\,\mathrm{Sc}(a)\,\mathrm{Sc}(b)$ | Clifford trace on the Dirac module; $\operatorname{tr}e_t=4$ |
| $\mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\partial/\partial t'-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial Q_k$ | Cell Dirac operator of the module |
| $a$, $c$ | Four-dimensional Euler and Weyl coefficients; the two-dimensional central charge is a different $c$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
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
- Companion articles: [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), for the regularised determinant whose variation is the anomaly; [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), for $\Gamma_1=\tfrac12\operatorname{Tr}\log S^{(2)}$; [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html), for the $\beta$ function the anomaly is read against; [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the three metric levels and the trace of a biquaternion; [The Theta Vacuum in Biquaternionic Form](the-theta-vacuum-in-biquaternionic-form.html), for the phase of the non-central determinant; [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html) and [The Harmonic Oscillator in Biquaternionic Form](the-harmonic-oscillator-in-biquaternionic-form.html), for the sector interpretation of the component count.
