# __The Conformal Anomaly in Biquaternionic Form__

## Introduction

A theory that is invariant under a local rescaling of its arena has an action that does not respond to the rescaling, and a quantised version of it generally does. The classical action of a massless field returns the same number when the arena is stretched point by point. The regulated one-loop action does not. The residue is the **conformal anomaly**: its coefficient is fixed by the field content, its form by the symmetries, and it is not an artifact of one regulator. It is the obstruction to defining the regulated determinant in a way that preserves the symmetry of the classical action.

**Two names circulate for it, and this article uses one.** *Conformal anomaly* names the symmetry that fails. *Trace anomaly* names the matrix operation that reads the failure, the diagonal sum of the matrix of components of the stress tensor. The two names denote one coefficient. This article writes the first, and writes the diagonal sum out in components, so that the word *trace* names a matrix and nothing else in these pages.

This article asks what the biquaternion framework contributes to the statement. The findings are the following.

1. **The response is a property of the determinant, not of the algebra.** The anomaly arises from the regulation of $\log\det S^{(2)}$, which is the object of *The Functional Determinant in Biquaternionic Form*. The divergence of that determinant is controlled by the heat-kernel coefficient $a_{d/2}$, and the response is the variation of the renormalised determinant under the rescaling. The algebra contributes neither the regulation nor the divergence. It contributes the operator on which the determinant is taken, and the dimension of the space on which that operator acts. The division of labour is the one the functional-integral and determinant articles record, and it is stated here at the outset so that the anomaly is not misattributed to the algebra.

2. **The coefficient counts the dimensions of the fibre, and the framework's state pairing is not that count.** A biquaternion field has four complex coefficients and eight real components, four in each sector, so the count is four complex or eight real. The pair of a state and an observable is a different object: it is the scalar part of a product, $2\,\mathrm{Sc}(\tilde{Ϛ}_\Psi\tilde H_\Psi)$, and it counts nothing and regulates nothing. *Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model: Four Conditions Become None* keeps the pairing and the determinant apart, and this article uses its separation.

3. **The rescaling is a level-1 statement, and it must not be confused with the $i r'_t$ construction of the coordinate.** The framework obtains the Lorentzian sign pattern from the level-1 form read on the material sector, with the time coordinate written $i r'_t$: the minus sign is one use of $i^2=-1$, and the signs are an output rather than an input. A rescaling changes the level-1 form, and therefore changes the level-2 reading. It does not change the $i r'_t$ assignment or the sector split. The three levels are kept apart throughout.

4. **The coefficient has a fixed shape, and the algebra contributes only its multiplicity.** In four dimensions the response is a linear combination of the Euler density, the Weyl square and the d'Alembertian of the curvature scalar, with rational coefficients additive over fields; the weights of a scalar, a Dirac fermion and a vector are $1:11:62$ and $1:6:12$. The algebra fixes how many copies of the per-component number a biquaternion field contributes. It fixes nothing else: not the weights, not the curvature invariants, not the scheme-dependent term. This is the same division the partition-function, functional-integral and determinant articles make. It is not a claim that the biquaternion scalar is a collection of independent complex scalars, for the reason those articles give.

5. **The conformal anomaly and the $\theta$ vacuum are the two structural quantum effects of this group.** The anomaly is the failure of a *conformal* symmetry; the $\theta$ vacuum of the next article is the failure of a *topological* triviality. Both arise from the regulated determinant, and in particular from its non-central part: the determinant article's distinction between the central case, where the determinant factors, and the non-central case, where it acquires a phase, is what separates them. The anomaly is a central statement about a non-central operator. The $\theta$ vacuum is a statement about the phase that the operator acquires.

The article proceeds as follows. The next section declares the arena, fixes the response and recalls the classical vanishing. A section derives the quantum response from the variation of the determinant and gives the heat-kernel origin of the coefficient. A section counts the fibre, and a section evaluates the coefficient in two and four dimensions. A section treats the rescaling at the three levels of the one metric. A section relates the anomaly to the $\beta$ function of *The Renormalization Group in Biquaternionic Form*. A section records the proper-time representation, the chiral pair and the mass. A section separates what is established from what is interpretation, and the summary, the notation table and the literature close the article.

## The Arena, the Rescaling, and the Response

The classical statement is fixed first, because the anomaly is the deviation from it.

### The One Metric and the Declared Arena

**The series has one metric.** It is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$ on the four $Q_\mu$, and it is the form of the algebra: the quaternionic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ is its quadratic form. *Frame and Metric Conventions* fixes it, and no article of the series introduces a second one.

**This article writes a second object, and declares it once.** A response to a local rescaling is a statement about a geometry that varies from point to point, and the unit metric is one geometry. The article therefore carries $g_{\mu\nu}$, the metric of the arena, written with no tilde and with both indices low. It enters the transcribed formulas and nothing else. It is not the algebra's form, it is not a second convention of the series, and no claim the framework makes in this article is a claim about $g$: every framework claim is a claim about the fibre of a biquaternion field or about the level-1 form. The declaration is the one *Conceptual Conventions* requires of an unpreferred object, and it is made here, before the first formula that carries $g$.

### The Response

**The response.** For an action $S[Ξ;g]$, a **rescaling** of the arena is a local stretch

$$
g_{\mu\nu}\;\longrightarrow\;\exp(2\sigma(x))\,g_{\mu\nu},
\qquad
\delta_\sigma g_{\mu\nu}=2\sigma\,g_{\mu\nu},
$$

and the response is the coefficient of the stretch in the variation of the action,

$$
\delta_\sigma S=\int d^dx\,\sqrt{|g|}\;\sigma\,\mathcal{A}_{\mathrm{cfa}},
\qquad
\mathcal{A}_{\mathrm{cfa}}=\sum_{\mu,\nu}g_{\mu\nu}T_{\mu\nu},
$$

with $T_{\mu\nu}$ the stress tensor, taken with both indices low and varying the components $g_{\mu\nu}$ with no index raised. On an arena whose metric is diagonal in the coordinates in use, the second display is the sum of the four diagonal entries, $\sum_\mu g_{\mu\mu}T_{\mu\mu}$, each carrying its own weight.

**The same number has a matrix name, and it is not used here.** The diagonal sum of the matrix of components $T_{\mu\nu}$ is what a text trained on matrices calls the trace of the stress tensor. That use is admitted by *Algebra and Element Conventions*, because the carrier there is a matrix of components and the matrix stands in the same formula. This article writes the sum instead: the object it varies is an action, the arena's metric is diagonal in the coordinates it uses, so the sum reduces to the four diagonal weights, and it names them. No trace of an element of $\mathbb{B}$ is written anywhere in these pages, nor of an operator, nor of a state: an element is read in $\mathrm{Sc}$, and the state pairing is written $2\,\mathrm{Sc}(\tilde{Ϛ}_\Psi\tilde H_\Psi)$.

**Weyl invariance is the vanishing of the response.** So $\mathcal{A}_{\mathrm{cfa}}=0$ is the statement that the classical action is invariant under the stretch, and the anomaly is the statement that the quantum effective action is not.

### The Classical Vanishing

**When the response vanishes.** For a massless scalar at the conformal coupling, for the massless Dirac field, and for the Maxwell field in $d=4$, the classical action is invariant and $\mathcal{A}_{\mathrm{cfa}}=0$ on shell. A mass term, a curvature coupling with non-critical coefficient and a dimensionful coupling break the invariance explicitly. Those breakings are not anomalous: they are present classically, and their coefficients are fixed by the action rather than by the regulator. The anomaly is the part that cannot be removed.

**The improvement term.** For a scalar the canonical tensor is not response-free even for the massless action at the conformal coupling, and the improvement term

$$
T_{\mathrm{imp},\mu\nu}=T_{\mathrm{can},\mu\nu}+\zeta\big(g_{\mu\nu}\Box_\Phi-\nabla_\mu\nabla_\nu\big)\xi^2,
\qquad
\zeta=\frac{d-2}{4(d-1)},
$$

produces $\mathcal{A}_{\mathrm{cfa}}=0$ on shell, the bracket reducing in flat coordinates to $\delta_{\mu\nu}\Box_\Phi-\partial^2/\partial R_\mu\partial R_\nu$, with $\Box_\Phi$ read on the flat arena. The arithmetic is short. The added response is $\zeta(d-1)\Box_\Phi\xi^2$, which on shell is $2\zeta(d-1)\sum_\mu(\partial\xi/\partial R_\mu)^2$, because $\Box_\Phi\xi^2=2\sum_\mu(\partial\xi/\partial R_\mu)^2+2\xi\,\Box_\Phi\xi$ and the second term vanishes for a massless field, while the canonical response is $-\tfrac{d-2}{2}\sum_\mu(\partial\xi/\partial R_\mu)^2$. The value $\zeta=(d-2)/(4(d-1))$ cancels the two, and gives $\zeta=\tfrac16$ at $d=4$.

**Why the improvement is recorded.** It fixes the normalisation against which the quantum response is measured. A calculation that omits the improvement reports the canonical value and calls it the anomaly, and the two differ by a term fixed by the action.

### The Material Reading of the Flat Arena

**The flat arena.** The flat metric is $\delta_{\mu\nu}=(1,1,1,1)$ on the four $Q_\mu$, and the level-2 reading of the level-1 form is the material one, $Q_t=i q'_t$ and $Q_\eta=q_\eta$, as *Frame and Metric Conventions* fixes. The response $\mathcal{A}_{\mathrm{cfa}}$ is then a level-2 number, four diagonal entries summed with their weights, while the statement it makes is level-1: the form was stretched.

**Two operations that are not one.** A rescaling of the level-1 form is not a change of the $i r'_t$ assignment. The first multiplies the form by a function of the point. The second writes the time coefficient on the material sector, once, and the minus of the interval is $i^2=-1$ in that coefficient. The section on the three levels makes the distinction precise, and it is the place where the two are most easily mixed.

## The Quantum Response as the Variation of the Determinant

The one-loop effective action is the determinant of the second variation, and the anomaly is its response to a stretch.

### The One-Loop Action

**The determinant.** From *The Generating Functional and the Effective Action in Biquaternionic Form*, and in the form of *The Functional Determinant in Biquaternionic Form*, the one-loop contribution is

$$
\Gamma_1[\xi;g]=\tfrac12\log\det S^{(2)}[\xi;g],
$$

with $S^{(2)}$ the second variation of the classical action about the background. The determinant of a fluctuation operator is a sanctioned name: *Norm and Pairing Conventions* lists the functional determinant of a path integral among the arrays that carry the word, and no determinant is taken of an element.

**The response of the one-loop action.** Its response to a stretch is

$$
\mathcal{A}_{\mathrm{cfa}}\big|_{\text{one loop}}=\frac{2}{\sqrt{|g|}}\sum_{\mu,\nu}g_{\mu\nu}\frac{\delta\Gamma_1}{\delta g_{\mu\nu}},
$$

and the anomaly is the statement that this is non-zero for a classically invariant theory. In the path-integral language the same statement is that the measure $\mathcal{D}Ξ$ is not invariant under the stretch, or equivalently that the regulated determinant is not. The two languages agree, and both are standard (Capper and Duff 1974; Deser, Duff and Isham 1976; Duff 1994).

### The Spectral Sum

**The determinant as a sum over the spectrum.** With $\lambda$ running over the spectrum of $S^{(2)}$ on the field space, each eigenvalue counted with its multiplicity,

$$
\Gamma_1=-\tfrac12\int_0^\infty\frac{d\tau}{\tau}\sum_{\lambda}\mathrm{e}^{-\tau\lambda},
$$

up to a divergent constant, the proper-time representation of the logarithm of a determinant. The sum names its index and its set, as *Operator and Calculus Conventions* requires of every sum in the series, and it needs no second symbol for the reading. A symbol that summed the spectrum would name the same operation, and the sum states it.

**What the sum makes visible.** The multiplicity sits in the sum and not in a factor to be looked up. Each eigenvalue of the scalar problem appears once per complex coordinate of the field, so the multiplicity of the field space is written where the eigenvalues are written.

### The Heat-Kernel Expansion

**The small-$\tau$ expansion.** Regulating the determinant with a proper-time cutoff, the heat kernel has the expansion

$$
\sum_{\lambda}\mathrm{e}^{-\tau\lambda}\;\sim\;\frac{1}{(4\pi\tau)^{d/2}}\sum_{k\ge0}\tau^{k}\int d^dx\,\sqrt{|g|}\,a_k,
$$

where $a_k$ is the Seeley–DeWitt coefficient of order $k$, the first being $a_0=1$ for the minimal operator. The term that survives renormalisation is $a_{d/2}$, because $\tau^{k-d/2}$ is logarithmically divergent exactly at $k=d/2$. The response of the regulated determinant is then

$$
\delta_\sigma\Gamma_1=\frac{1}{(4\pi)^{d/2}}\int d^dx\,\sqrt{|g|}\;\sigma\,a_{d/2},
$$

so that the response is local and proportional to the single coefficient $a_{d/2}$. This is the standard heat-kernel account (DeWitt 2003; Vassilevich 2003), and it is the reason the anomaly is a one-loop, one-coefficient statement rather than a tower of terms: $a_{d/2}$ is local, and the higher coefficients are not.

**The algebra's place in the expansion.** The coefficient $a_k$ of an operator on a biquaternion-valued field is the coefficient of the scalar problem times the dimension of the fibre on which the operator acts, when the operator is central. The geometry of the operator supplies the curvature invariants. The algebra supplies the dimension of the space the operator acts on. This is the same division as in the determinant article, and it is why the anomaly's multiplicity, as opposed to its form, is the algebra's contribution.

## The Multiplicity of the Fibre

The count is four, and it is the only number the algebra supplies to the coefficient.

### Four Complex, Eight Real

**The fibre.** A biquaternion field is an element of $\mathbb{B}$ at each point: four complex coefficients, hence eight real components, four in each sector. $\dim_{\mathbb{C}}\mathbb{B}=4$, and this dimension is the multiplicity of the field space.

**What the multiplicity means, and what it does not.** When the fluctuation operator is central, a scalar coefficient times the identity on the fibre, each eigenvalue of the scalar problem occurs once per complex coordinate, and the coefficient of the response is four times the scalar one, eight in a real counting. When the operator is not central, the four coordinates mix and each eigenvalue of the scalar problem is replaced by the four eigenvalues of a $4\times4$ matrix at each point; the coefficient is then read on the endomorphism of the fibre, and the counting of dimensions fixes only the leading term. The mass term of §*The Chiral Pair and the Mass* is such a case, and the section says so.

### What the Two-Sided Action Does to the Determinant

**Two derived forms, read from the multiplication of the units.** Let $L(a)$ and $R(b)$ be the left and the right multiplication by $a$ and $b$ on $\mathbb{B}$ taken as a complex vector space, matrices of size four. Then

$$
\det L(a)=\langle a\rangle_{\natural}^{2},
\qquad
\det\bigl(L(a)R(b)\bigr)=\langle a\rangle_{\natural}^{2}\,\langle b\rangle_{\natural}^{2},
\qquad
\det(c\,I_4)=c^{4},
$$

for $c$ central. Verified on $100$ random complex pairs: the residual is below $2\times10^{-11}$ on every pair, and the third is exact to machine precision. The first display is the statement that the regular determinant of a multiplier is the square of the quaternionic norm, the second is its multiplicativity, and the third is the count: the exponent four is the dimension of the fibre.

**What the forms do and do not say.** They say that a central multiplier acts on the fibre as one scalar, four times. They do not say that a general element acts as a scalar: the operator of a general two-sided action mixes the four coordinates, and its determinant is the product of the two norms, not a fourth power of one scalar part.

### The Finite-Dimensional Check

**The shadow of the count.** For a complex $K$ on a space of dimension $n$,

$$
\det\bigl(\mathrm{e}^{s}K\bigr)=\mathrm{e}^{ns}\det K,
\qquad
\frac{\partial}{\partial s}\log\det\bigl(\mathrm{e}^{s}K\bigr)\Big|_{s=0}=n,
\qquad
\frac{\partial}{\partial s}\det\bigl(\mathrm{e}^{s}K\bigr)\Big|_{s=0}=n\det K .
$$

The first identity is exact, so the second and the third are exact; a central difference with $h=10^{-6}$ returns the dimension to ten digits, and on a space of dimension four it returns $4$. The dimension of the space is the coefficient of the rescaling, which is the finite-dimensional image of the statement that the anomaly's coefficient counts components.

**The number two is not this field.** The value four is the dimension of the field space. The value two is the dimension of the $2\times2$ image, and it belongs to the reading of one element and not to the count of a field's components: $2\,\mathrm{Sc}\tilde Q$ is the scalar part of one element with the factor of that image, and a field space is not one element.

## The Coefficients in Two and Four Dimensions

The standard values are recalled, and the multiplicity is exhibited.

### Two Dimensions

**The response.** For a massless scalar field on a two-dimensional arena the response is

$$
\boxed{\;\mathcal{A}_{\mathrm{cfa}}=\frac{c_{\mathrm{2d}}}{24\pi}\,R\;},
$$

with $c_{\mathrm{2d}}=1$ for a real scalar, $c_{\mathrm{2d}}=2$ for a complex scalar, and the value additive over decoupled fields. The coefficient is the Seeley–DeWitt value $a_1=R/6$ of the minimal scalar, since $\frac{1}{4\pi}a_1=R/(24\pi)$, and the value $c_{\mathrm{2d}}=1$ per real scalar is the standard one (Polyakov 1981).

**The count.** The coefficient is proportional to the number of real components. A biquaternion scalar field carries eight, so it contributes eight times the per-component number. That is a count of components of one field, and not a claim that the field is eight independent scalars.

### Four Dimensions

**The response.** In four dimensions the response of a free field is a linear combination of the Euler density, the Weyl square and the d'Alembertian of the curvature scalar,

$$
\boxed{\;\mathcal{A}_{\mathrm{cfa}}=\frac{1}{(4\pi)^{2}}\bigl(c\,W^{2}-a\,E_{4}+b\,\Box_\Phi R\bigr)\;},
$$

with $E_4=\sum_{\mu,\nu,\rho,\sigma}R_{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}-4\sum_{\mu,\nu}R_{\mu\nu}R_{\mu\nu}+R^{2}$ the Euler density and $W^2=\sum_{\mu,\nu,\rho,\sigma}W_{\mu\nu\rho\sigma}W_{\mu\nu\rho\sigma}$ the Weyl square. The minus on the Euler density is the convention of Duff's review, and a text that writes $+aE_4$ defines $a$ with the opposite sign.

**The coefficients.** In that convention the coefficients are rational functions of the field content,

$$
a=\frac{1}{90}\bigl(n_s+11n_f+62n_v\bigr),
\qquad
c=\frac{1}{120}\bigl(n_s+6n_f+12n_v\bigr),
$$

for $n_s$ real scalars, $n_f$ Dirac fermions and $n_v$ vector fields. Both are additive over decoupled fields, and both are independent of the renormalised coupling.

### The Weights

The per-field values are read off the two displays above, with $n$ a single field of the kind.

| field | $n_s$ | $n_f$ | $n_v$ | $a$ | $c$ |
|---|---|---|---|---|---|
| real scalar | $1$ | $0$ | $0$ | $\tfrac{1}{90}$ | $\tfrac{1}{120}$ |
| Dirac fermion | $0$ | $1$ | $0$ | $\tfrac{11}{90}$ | $\tfrac{1}{20}$ |
| vector | $0$ | $0$ | $1$ | $\tfrac{62}{90}$ | $\tfrac{1}{10}$ |

**The ratio.** The weights stand in the ratio $1:11:62$ for $a$ and $1:6:12$ for $c$. Neither ratio is the algebra's: they are the spin weights of the standard heat kernel, and the algebra multiplies them by the dimension of its fibre.

**Two letters, one sign.** The symbol $c$ of the four-dimensional display is the Weyl-square coefficient, and it is not the two-dimensional central charge $c_{\mathrm{2d}}$ of the previous subsection. The two share a letter in the literature and nothing else, and this article labels the two-dimensional one so that the reader can tell them apart.

**Scheme dependence.** The $\Box_\Phi R$ term is the exception to scheme independence: its coefficient is moved by a finite local counterterm, so only $a$ and $c$ are predictions of the field content. A reader who finds a $\Box_\Phi R$ coefficient differing between articles is looking at a scheme choice and not at a disagreement.

## The Rescaling at the Three Levels of the One Metric

The one metric is read at three levels in the series, and the rescaling is where they are most easily mixed. The levels themselves are fixed in *Algebra and Element Conventions* and *Frame and Metric Conventions*; this section states only what the stretch does to each.

### Level 1

**The form.** The level-1 form is the biquaternion norm of *Frame and Metric Conventions*, whose metric is $\delta_{\mu\nu}$. A rescaling is a change of its normalisation, and the response measures the change. The stretch is not a change of the algebra, of the basis or of the sector split: it changes the one form, and that form is the only object the definition of the anomaly varies.

### Level 2

**The material reading.** The level-2 reading is the same form read on the material sector, with $Q_t=i q'_t$ and $Q_\eta=q_\eta$, which is the substitution *Frame and Metric Conventions* fixes. A stretch rescales the level-1 form and the level-2 coefficients with it, but it does not change the $i r'_t$ assignment or the sector split. The minus of the material $\Box_\Phi$ comes from $i^2=-1$ in $\partial/\partial i r'_t$ and from nothing else, and no sign in the coefficient above is to be corrected on the basis of the level-1 form.

### Level 3

**The legacy display.** The third level is the older display, the arrays in which the literature prints the same objects. It is a display and not a convention of this article: *Matrix Representations Conventions* fixes it, and *Operator and Calculus Conventions* states why it is legacy. The display enters the anomaly only as the standard transcription of the four-dimensional coefficients. A calculation in the display and a calculation with biquaternion elements must agree on the anomaly, because the anomaly is a physical coefficient; where they appear to disagree it is the transcription that is wrong.

### What the Rescaling Is Not

**Three operations that are not it.** A rescaling is not a coordinate transformation, since it changes distances without changing coordinates. It is not the Wick rotation, which in this series is either the exchange of the real and imaginary sectors or the continuation $r'_t\mapsto-i\tau$ of one coordinate, and which rotates rather than rescales. It is not a Lorentz transformation, which preserves the level-1 form. Keeping the four apart is the content of the section.

## The Anomaly and the Renormalisation Group

The coefficient of the response and the $\beta$ function of a running coupling are two readings of one loop computation, and the corpus's renormalisation conventions fix how they are related.

### The Relation

**Proportionality.** For a coupling $g$ that multiplies a marginal operator, the response is proportional to the $\beta$ function,

$$
\mathcal{A}_{\mathrm{cfa}}\supset\frac{\beta(g)}{2g}\,O,
$$

where $O$ is the operator multiplying the coupling. The relation is standard: the anomaly and the $\beta$ function are the same coefficient read in two ways. It is also the reason the anomaly is not removable by a counterterm, since removing it would contradict the running that *The Renormalization Group in Biquaternionic Form* computes.

### One-Loop Exactness

**Why one loop is final here.** In a conformal theory the anomaly is one-loop exact: higher loops add no new term of the anomalous form. This is the statement that $a_{d/2}$ is local and that the variation of the determinant is exhausted by it, and it is standard (Adler–Bardeen non-renormalisation). It is worth stating because it is the exception rather than the rule for one-loop results: a one-loop anomaly computed in the framework is not a first approximation.

### The Non-Central Case

**Where the determinant does not factor.** For a massive operator whose mass term carries one chirality value into the other, the determinant does not factor and acquires a phase, the eta invariant of the operator family. The anomaly remains the curvature statement; the phase is its topological partner, and the $\theta$ vacuum is what reads it. The distinction is the determinant article's, and it is what separates this article from the next one in the group.

## The Proper-Time Representation, the Chiral Pair and the Mass

Two details of the derivation and one structural fact about the mass are recorded here, and the cutoff that turns the divergence into a counterterm.

### The Chiral Pair

**The derivatives.** The gradient and its quaternion conjugate are fixed in *Operator and Calculus Conventions*, §*The Gradient*, and $\Box_\Phi$ is the scalar composition of the two. The massive dynamics is the chiral pair of *The Dirac Equation in Biquaternionic Form*, and its two letters are the two values of the chirality: $\tilde{Ξ}_{L}$ is the $-1$ part and $\tilde{Ξ}_{R}$ the $+1$ part. No one-field first-order massive equation stands beside the pair, because the square of the gradient is not scalar. In the coordinates $Q_\mu$ it is

$$
\tilde\nabla_\Phi^{2}=\frac{\partial^{2}}{\partial R_t^{2}}-\Delta_\Phi+2\sum_\eta\vec e_\eta\frac{\partial^{2}}{\partial R_t\,\partial R_\eta},
$$

where the mixed term survives because $e_t$ commutes with the spatial units, and $\Delta_\Phi$ is the convention's Laplacian. Only the composition with the conjugate is scalar, and that composition is the series' $\Box_\Phi$. Both identities are derived forms, read from the multiplication of the units.

### The Mass

**The mass term.** It is the right multiplication $\tilde{Ξ}\mapsto k_m\,\tilde{Ξ}(i\vec e_x)$, the frame's timelike basis operator up to the scalar $k_m=mc/\hbar$. The chirality basis operator multiplies on the right as well, and the two basis operators anticommute, because $\vec e_x\vec e_z=-\vec e_z\vec e_x$. The mass therefore carries $\tilde{Ξ}_{L}$ into a multiple of $\tilde{Ξ}_{R}$ and $\tilde{Ξ}_{R}$ into a multiple of $\tilde{Ξ}_{L}$: it exchanges the two values. This is a derived form, and it was checked on generic elements.

**What the mass does to the determinant, and to the count.** The gradient multiplies on the left, where it commutes with the chirality basis operator, so the free pair carries each value into itself and the free operator is central. The massive operator mixes the two values: it is not block-diagonal in them, its determinant is not the product of the two free determinants, and the fibre is not acted on by a scalar. The multiplicity of four is therefore exact for the free operator and for the leading term of the massive one, and the rest of the massive coefficient is read on the endomorphism of the fibre. This is the case §*What the Multiplicity Means* flags, and it is the reason the next article of the group has a phase to read.

### The Proper-Time Representation

**The cutoff and the counterterm.** A proper-time cutoff at $\tau=\Lambda^{-2}$ makes the term with $k=d/2$ of the expansion diverge logarithmically, and a local counterterm built from the curvature invariants absorbs the divergence. The subtraction does not remove the response, and the reason is the shape of the candidates: every local counterterm is an integral of a curvature invariant, and its own variation under the stretch is a local density of the same shape. What remains after the subtraction is the coefficient the field content fixes. In four dimensions the Euler density and the Weyl square are the two structures that survive, which is why $a$ and $c$ are predictions of the field content while the $\Box_\Phi R$ term is not.

**Where the framework's part is visible.** The integrand is the heat kernel of $S^{(2)}$, its small-$\tau$ expansion is the one of §*The Heat-Kernel Expansion*, and the term $a_{d/2}$ of that expansion is the anomalous coefficient. The framework's contribution appears in the sum over the spectrum, as the multiplicity with which the eigenvalues are counted.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**

- A rescaling of the arena rescales the level-1 biquaternion norm and leaves the algebra, the basis, the $i r'_t$ assignment and the sector split unchanged. A rescaling is not the Wick rotation and not a Lorentz transformation.
- The fibre of a biquaternion field has complex dimension four and real dimension eight, four per sector. The two-sided action scales a determinant by $\langle a\rangle_{\natural}^{2}\langle b\rangle_{\natural}^{2}$, so a central multiplier acts on the fibre as one scalar, four times. Both forms are derived from the multiplication of the units and were checked on $100$ random pairs with a residual below $2\times10^{-11}$.
- The conformal variation of a finite-dimensional determinant is proportional to the dimension of the space: $\partial/\partial s\,\log\det(\mathrm{e}^{s}K)|_{s=0}=\dim$. The identity is exact, and a central difference returns the dimension to ten digits, with the determinant derivative equal to $\dim\cdot\det K$. This is the finite-dimensional shadow of the statement that the coefficient counts components.
- The state pairing is not a determinant and not a count: it is $2\,\mathrm{Sc}(\tilde{Ϛ}_\Psi\tilde H_\Psi)$, the scalar part of a product with the factor of the $2\times2$ image, and no determinant is taken with it.

**Standard, and transcribed.**

- The definition of $T_{\mu\nu}$ as the variation of the action, the improvement term, and the classical vanishing of the response.
- The one-loop response as the variation of $\log\det S^{(2)}$; the heat-kernel expansion; the identification of $a_{d/2}$ as the anomalous coefficient.
- The values $c_{\mathrm{2d}}=1$ per real scalar in two dimensions, and the four-dimensional coefficients $a$ and $c$ for scalar, fermion and vector fields.
- The relation $\mathcal{A}_{\mathrm{cfa}}\supset\frac{\beta}{2g}O$, the scheme dependence of $\Box_\Phi R$, and the one-loop exactness of the anomaly.
- The proper-time representation and the small-$\tau$ expansion of the heat kernel, with $k=d/2$ as the anomalous coefficient.

**Interpretation.**

- Reading the coefficient of the anomaly as the multiplicity of the algebra's fibre, with the geometry supplied by the heat kernel, is the framework's interpretation of the standard result. The standard result is not re-derived here.
- Treating the conformal anomaly and the $\theta$ vacuum as the two structural quantum effects of this subcategory is the organising interpretation of the anomaly-and-angle pair of this group.

**Open.**

- Whether the framework has a natural definition of the conformal coupling $\zeta=\tfrac16$ beyond its transcription is not addressed here; the improvement term is used as in the standard theory.
- The anomaly of a genuinely non-central biquaternion operator, and whether its eta-invariant part has a framework-specific form, is left to the $\theta$-vacuum article.
- The scheme-independent coefficients of the biquaternion field are not computed here; only the counting that fixes them is identified.

## Summary

The conformal anomaly in biquaternionic form is the standard anomaly with the framework's count of the fibre. The classical response vanishes for an invariant action, and the one-loop effective action $\Gamma_1=\tfrac12\log\det S^{(2)}[\xi;g]$ has the conformal variation

$$
\boxed{\;\mathcal{A}_{\mathrm{cfa}}\big|_{\text{one loop}}=\frac{2}{\sqrt{|g|}}\sum_{\mu,\nu}g_{\mu\nu}\frac{\delta\Gamma_1}{\delta g_{\mu\nu}}=\frac{1}{(4\pi)^{d/2}}\,a_{d/2}\;},
$$

proportional to the Seeley–DeWitt coefficient, which is local and one-loop exact. In two dimensions the response is $\frac{c_{\mathrm{2d}}}{24\pi}R$ with $c_{\mathrm{2d}}$ counting real components; in four dimensions it is $\frac{1}{(4\pi)^2}(cW^2-aE_4+b\Box_\Phi R)$ with $a$ and $c$ fixed by the field content. The framework's contribution is the dimension of the fibre: four complex, eight real, four per sector, with the leading coefficient four times the scalar one and the count checked by $\partial/\partial s\,\log\det(\mathrm{e}^{s}K)|_{s=0}=\dim K$. A rescaling rescales the level-1 form and nothing else. The regulation of the determinant, the curvature invariants and the coefficients of $E_4$ and $W^2$ are standard and transcribed.

The response is written as a sum over the diagonal of the matrix of components of the stress tensor, never as a trace of an element. The factor two belongs to the reading of one element, $2\,\mathrm{Sc}\tilde Q$, and it is not the count of a field's components, which is four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\delta_{\mu\nu}=(1,1,1,1)$ | The unit metric, the one metric of the series |
| $g_{\mu\nu}$ | The arena's metric, declared once in this article; carried by the transcribed formulas and by nothing else |
| $\sigma$ | The local parameter of a rescaling, $g_{\mu\nu}\to\exp(2\sigma)g_{\mu\nu}$ |
| $\mathcal{A}_{\mathrm{cfa}}$ | The conformal response, the coefficient of $\sigma$ in the variation of the action |
| $T_{\mu\nu}=\frac{2}{\sqrt{|g|}}\frac{\delta S}{\delta g_{\mu\nu}}$ | Stress tensor, both indices low |
| $\mathcal{A}_{\mathrm{cfa}}\big|_{\text{class}}=\sum_{\mu,\nu}g_{\mu\nu}T_{\mu\nu}$ | The classical response, the diagonal sum of the matrix of components |
| $\Gamma_1=\tfrac12\log\det S^{(2)}$ | One-loop effective action whose variation is the anomaly |
| $\lambda$ | An eigenvalue of $S^{(2)}$ on the field space, counted with its multiplicity |
| $\sum_{\lambda}\mathrm{e}^{-\tau\lambda}$ | The heat kernel of $S^{(2)}$, as a sum over the spectrum |
| $a_{d/2}$ | Seeley–DeWitt coefficient controlling the anomalous response |
| $\zeta=(d-2)/(4(d-1))$ | Improvement coupling; $\zeta=1/6$ at $d=4$ |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | Quaternionic norm; $\dim_{\mathbb{C}}\mathbb{B}=4$ |
| $\det L(a)=\langle a\rangle_{\natural}^{2}$ | Determinant of the left regular matrix; the count of the fibre is the exponent four |
| $2\,\mathrm{Sc}(\tilde{Ϛ}_\Psi\tilde H_\Psi)$ | The state-and-observable pairing; a scalar part, not a determinant and not a count |
| $2\,\mathrm{Sc}\tilde Q=2Q_t$ | The scalar part of one element with the factor of the $2\times2$ image |
| $Q_t=i q'_t$, $Q_\eta=q_\eta$ | The material reading |
| $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ | Series d'Alembertian |
| $c_{\mathrm{2d}}$ | Two-dimensional central charge; a different letter from the four-dimensional $c$ |
| $a$, $c$ | Four-dimensional Euler and Weyl coefficients |
| $k_m=mc/\hbar$ | Mass wave number, the inverse of the mass length |

## Further Reading

- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, for the axial anomaly and the origin of anomalous Ward identities.
- J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Il Nuovo Cimento A* **60** (1969) 47–61, for the independent discovery of the axial anomaly.
- D. M. Capper and M. J. Duff, "Trace anomalies in dimensional regularization," *Il Nuovo Cimento A* **23** (1974) 173–183, for the anomaly in dimensional regularisation.
- S. Deser, M. J. Duff and C. J. Isham, "Non-local conformal anomalies," *Nuclear Physics B* **111** (1976) 45–55, for the structure of the conformal anomaly.
- M. J. Duff, "Twenty years of the Weyl anomaly," *Classical and Quantum Gravity* **11** (1994) 1387–1404, for the four-dimensional coefficients and their scheme independence.
- J. Wess and B. Zumino, "Consequences of anomalous Ward identities," *Physics Letters B* **37** (1971) 95–97, for the consistency conditions the anomaly satisfies.
- A. M. Polyakov, "Quantum geometry of bosonic strings," *Physics Letters B* **103** (1981) 207–210, for the two-dimensional anomaly and the central charge.
- B. S. DeWitt, *The Global Approach to Quantum Field Theory* (Oxford University Press, 2003), for the heat-kernel expansion and the Seeley–DeWitt coefficients.
- D. V. Vassilevich, "Heat kernel expansion: user's manual," *Physics Reports* **388** (2003) 279–360, for the heat-kernel coefficients used in the anomaly.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford University Press, 2002), for the renormalisation of the effective action and the anomaly.
- Companion articles: [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), for the regulated determinant whose variation is the anomaly; [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), for $\Gamma_1=\tfrac12\log\det S^{(2)}$; [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair and the two chirality values; [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html), for the $\beta$ function the anomaly is read against; [The Theta Vacuum in Biquaternionic Form](the-theta-vacuum-in-biquaternionic-form.html), for the phase of the non-central determinant; [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model: Four Conditions Become None](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html), for the axial current and the separation of the determinant from the state pairing.
- Conventions: [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the one metric, the scalar part of an element, and the rule that the word *trace* belongs to a matrix; [Norm and Pairing Conventions](norm-and-pairing-conventions.html), for $2\,\mathrm{Sc}\tilde Q=2Q_t$, the determinant of the $2\times2$ image, and the state pairing; [Matrix Representations Conventions](matrix-representations-conventions.html), for the two representations and the legacy display; [Frame and Metric Conventions](frame-and-metric-conventions.html), for the three levels of the one metric.
