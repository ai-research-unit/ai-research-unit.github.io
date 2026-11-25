# __The Primordial Potential: One Symmetric Minimum Above $M_C$__

## Introduction

**The question.** What must the potential of the unbroken phase look like for the group to be exact, and what does the same potential do when the sign of its quadratic term flips?

**The answer.** With $\mu_{\Phi}^{2}>0$, $\mu_{2}^{2}>0$ and a bounded quartic, the minimum is at $Ξ=0$; all sixteen real components are massive, fifteen at $\mu_{\Phi}^{2}$ and the trace at $\mu_{\Phi}^{2}+4\mu_{2}^{2}$; no direction is eaten; and the group is exact. **The symmetric phase is not a fine-tuned point but a region of parameter space**, and the article states its boundaries.

**One result of this article is a condition and it is stated first.** The corpus's declared vacuum, $D=\operatorname{diag}(-3,1,1,1)$ up to scale, **is the minimum of the potential in the branch $\lambda_{1}<0$ with $\mu_{2}^{2}>0$, and it is not the minimum in the branch $\lambda_{1}>0$.** No cubic is needed; two signs are, one for the shape and one for the trace, and §*The Declared Vacuum, and the Branch Where It Is the Minimum* states both.

**What this article does.** It writes the potential, derives the condition for the symmetric minimum, computes the mass spectrum there, derives the boundedness cone, and then confronts the potential with the vacuum the transition assumes.

**What it does not do.** It does not run the potential, does not compute the one-loop correction — [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html) does — and does not fix any coefficient. **Six coefficients and the group fixes none of them.**

## The Potential

**Two quadratics, four quartics, and no odd term at the level the group requires.**

$$
V(Ξ)=\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}
+\mu_{2}^{2}\bigl(\operatorname{tr}Ξ\bigr)^{2}
+\lambda_{1}\operatorname{tr}Ξ^{4}
+\lambda_{2}\bigl(\operatorname{tr}Ξ^{2}\bigr)^{2}
+\lambda_{3}\bigl(\operatorname{tr}Ξ\bigr)^{2}\operatorname{tr}Ξ^{2}
+\lambda_{4}\bigl(\operatorname{tr}Ξ\bigr)^{4},
$$

with $Ξ$ the Hermitian $4\times4$ matrix of [The Scalar's Two Indices](the-scalars-two-colour-indices-and-the-count-sixteen.html), the trace taken over colour, and no copy index on $Ξ$: one Hermitian matrix, sixteen real parameters.

**The field carries no condition.** $\operatorname{tr}Ξ$ is a gauge singlet and a dynamical mode, and the sixteen components are sixteen. **"Fifteen generators, so fifteen scalar directions" is the count that deletes it, and it is wrong**: a generator is traceless because $\mathfrak{su}(4)$ removes the trace, and that is a property of the algebra and not of a field. **A constraint on a field is not a convention**, for the reason a Proca field keeps its fourth component: a condition that removes a mode follows from an equation of motion, or nothing removes it. **Tracelessness in this model is a property of the vacuum** — the second sign below — and the article never constrains the field to get it.

**Why two quartics and not one, in the traceless channel.** $\operatorname{tr}(Ξ^{2})^{2}$ and $(\operatorname{tr}Ξ^{2})^{2}$ are different contractions of four matrix indices. **Neither is a function of the other**, and a vector-valued scalar would admit only one of them. [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html) tabulates the count.

**Why two more quartics carry the trace.** Keeping $\operatorname{tr}Ξ$ turns four matrix indices into many more contractions, and $(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}$ and $(\operatorname{tr}Ξ)^{4}$ are the two the display writes. **The price is stated and not hidden**: six coefficients where the traceless reading had three, and [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) carries the same display with the same count. **A fifth quartic, $\operatorname{tr}Ξ^{3}\operatorname{tr}Ξ$, is allowed and set to zero**: it is the only quartic that needs an odd power of the matrix, and this potential uses $Ξ$ only through $Ξ^{2}$ and through $\operatorname{tr}Ξ$. **The omission is a declaration about coefficients and not a symmetry**, since no group property forbids the term; on the hyperplane $\operatorname{tr}Ξ=0$ it vanishes identically, so neither vacuum below depends on it.

**Why no cubic, yet.** $\operatorname{tr}Ξ^{3}$ is invariant when $Ξ\to UΞ U^{\dagger}$ and real for Hermitian $Ξ$, so the group allows it and the term is legitimate. **It is omitted because neither phase needs it**: the symmetric minimum is at $Ξ=0$ without it, and the declared vacuum is selected by $\lambda_{1}<0$ with $\mu_{2}^{2}>0$ without it. §*The Declared Vacuum, and the Branch Where It Is the Minimum* shows what its absence costs.

**Why no term of degree six.** It is irrelevant for the questions this article asks, and its omission is a truncation of the potential stated as one.

## The Symmetric Minimum

**The condition is one sign, and it is not a tuning.**

$$
\frac{\partial V}{\partialΞ^{\dagger}}\bigg\rvert_{Ξ=0}=\mu_{\Phi}^{2}Ξ=0
\quad\Longleftrightarrow\quad
Ξ=0 ,
$$

which is a minimum and not a saddle when $\mu_{\Phi}^{2}>0$ and $\mu_{2}^{2}>0$. **The stationarity is unaffected by the trace term**, because $\partial(\operatorname{tr}Ξ)^{2}/\partial Ξ=2(\operatorname{tr}Ξ)\,\mathbb 1$ vanishes at the origin; what the trace term decides is the curvature, and it decides it in one direction only. **So the quadratic form is two blocks and not one**: $\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}+\mu_{2}^{2}(\operatorname{tr}Ξ)^{2}$, diagonal in the decomposition $\mathbf{15}\oplus\mathbf 1$.

**The mass spectrum at the origin, and where the degeneracy goes.**

$$
m^{2}_{ab}=\mu_{\Phi}^{2}\ \ (15\text{ traceless directions}),
\qquad
m^{2}_{\mathrm{tr}}=\mu_{\Phi}^{2}+4\mu_{2}^{2}\ \ (\text{the trace}),
$$

**and the trace is heavier by $4\mu_{2}^{2}$.** Along the trace direction $Ξ=c\,\mathbb 1$ the ratio $(\operatorname{tr}Ξ)^{2}/\operatorname{tr}Ξ^{2}$ is $(\operatorname{tr}\mathbb 1)^{2}/\operatorname{tr}\mathbb 1^{2}=16/4=4$, so the trace's Hessian exceeds the traceless one by $4\mu_{2}^{2}$. **In this normalisation the Hessian is the mass squared**: the kinetic term is $\operatorname{tr}(\partial Ξ)^{2}$, which on generators with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$ is $\tfrac12\sum_{a}(\partial\chi_{a})^{2}$, already canonical, so no factor of two enters.

**The degeneracy is not an accident of the group, and it is not what it was.** At $Ξ=0$ with $\mu_{2}^{2}=0$ the quadratic part is invariant under all of $\mathrm{O}(16)$, because every component enters through the same sum of squares, $\operatorname{tr}Ξ^{2}$. **The trace term breaks that accidental $\mathrm{O}(16)$ to $\mathrm{U}(4)$**, since $(\operatorname{tr}Ξ)^{2}$ is a $\mathrm{U}(4)$ invariant and not an $\mathrm{O}(16)$ one. **The quartics break nothing further**: every term in $V$ is a function of the eigenvalues of $Ξ$ and of $\operatorname{tr}Ξ$, so all of them are $\mathrm{U}(4)$ invariants. **The breaking to $\mathrm{SU}(4)$ is the vacuum's and not the potential's**: $D$ has little group $\mathrm{U}(1)\times\mathrm{U}(3)$ in $\mathrm{U}(4)$, whose intersection with the gauged $\mathrm{SU}(4)$ is the $\mathrm{U}(3)$ of the last three lines, nine generators.

**Consequences, stated as counts.**

| statement | reason | value |
| --- | --- | --- |
| the number of Goldstone bosons | no generator is broken | $0$ |
| the number of eaten directions | no vector is massive | $0$ |
| the number of massive scalars | all components | $16$ |
| the number of massless vectors | no vacuum | $15$ |
| the leptoquark sextet's mass | no vacuum | $0$ |

**The last two rows are the phase's defining property.** Fifteen massless vectors, sixteen massive scalars, and no scale in the gauge sector at all: **the unbroken phase has no $M_C$ in it**, and $M_C$ is the scale at which the vacuum forms. **The second row is the consequence a reader is likeliest to forget: the six leptoquarks are among the fifteen**, so in this phase they are massless — exactly, and not approximately — and the mass $32v^{2}$ they carry below $M_C$ is made by the vacuum and by nothing else.

## The Boundedness Cone

**A quartic that is not bounded below makes every statement above empty, so the condition is derived and not assumed.**

Write $A=Ξ^{\dagger}Ξ$, a positive semi-definite Hermitian matrix with eigenvalues $a_{1},\dots,a_{4}\ge0$, and let $x=\operatorname{tr}A$ and $s_{2}=\operatorname{tr}A^{2}$. The quartic is

$$
V_{4}=\lambda_{1}s_{2}+\lambda_{2}x^{2} .
$$

**Both ends of the ratio bind, one for each sign.** For $a_{i}\ge0$ with $\sum a_{i}=x$ the ratio $s_{2}/x^{2}$ runs over $[\tfrac14,1]$, the lower end at four equal eigenvalues and the upper at a single nonzero one, because $\frac14x^{2}\le\sum a_{i}^{2}\le x^{2}$.

- *If $\lambda_{1}\ge0$*, $V_{4}$ is smallest at the four equal eigenvalues, so boundedness needs $\lambda_{1}+4\lambda_{2}\ge0$.
- *If $\lambda_{1}<0$*, $V_{4}$ is smallest at the single nonzero eigenvalue, where $s_{2}=x^{2}$, so boundedness needs $\lambda_{1}+\lambda_{2}\ge0$.

$$
\boxed{\;\lambda_{1}+\lambda_{2}\ge0\quad\text{and}\quad\lambda_{1}+4\lambda_{2}\ge0 .\;}
$$

**The two conditions are one cone, and neither half suffices.** The rank-one direction $A=rE_{11}$ gives $s_{2}=x^{2}$ and binds when $\lambda_{1}<0$; the identity gives $s_{2}=x^{2}/4$ and binds when $\lambda_{1}>0$, the ratio $4$ being $\operatorname{tr}\mathbb{1}$ for $\mathrm{SU}(4)$. **A quartic bounded on the rank-one directions alone still sinks along the identity when $\lambda_{1}>0$, and one bounded on the identity alone still sinks along a single entry when $\lambda_{1}<0$.** The frequently quoted bound $\lambda_{1}+\lambda_{2}>0$ is one half of the cone; $\lambda_{1}\ge0$ is neither half, and it excludes a region the cone allows.

### The Trace Channel, in the Cone

**These are the conditions of the potential with $\lambda_{5}=0$, and the scope is stated because it is not automatic.** The fifth quartic $\operatorname{tr}Ξ^{3}\operatorname{tr}Ξ$ is allowed by the group and set to zero by declaration, so it is absent from every row below; **a nonzero $\lambda_{5}$ would need its own row, and the four conditions here would not bound the potential on their own.** On the traceless hyperplane it vanishes identically, so nothing in the vacuum comparison depends on the omission.

**The two conditions above are the traceless slice, and the trace channel adds two more.** Write $y=\operatorname{tr}Ξ$ and $x=\operatorname{tr}Ξ^{2}$. **$y$ is not a function of $Ξ^{2}$**, since $\operatorname{tr}Ξ$ and $\operatorname{tr}Ξ^{2}$ are independent invariants, so the quartic

$$
V_{4}=\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}x^{2}+\lambda_{3}y^{2}x+\lambda_{4}y^{4}
$$

must be checked on the directions where $y\neq0$, and there are two that bind. Cauchy–Schwarz on the four eigenvalues gives $y^{2}\le4x$, with equality at the identity; a single nonzero entry attains $y^{2}=x$.

| direction | $Ξ$ | $\operatorname{tr}Ξ^{4}/x^{2}$ | $y^{2}/x$ | quartic coefficient |
| --- | --- | --- | --- | --- |
| the identity | $c\,\mathbb 1$ | $\tfrac14$ | $4$ | $\tfrac14\lambda_{1}+\lambda_{2}+4\lambda_{3}+16\lambda_{4}$ |
| a single entry | $rE_{11}$ | $1$ | $1$ | $\lambda_{1}+\lambda_{2}+\lambda_{3}+\lambda_{4}$ |

**Both coefficients must be non-negative, and both are attained**, so neither row can be dropped; the identity is the harder of the two, because it multiplies $\lambda_{3}$ by four and $\lambda_{4}$ by sixteen. **At $y=0$ the two trace terms vanish and the traceless cone above is recovered exactly**, which is why the corpus's earlier two-condition statement was not wrong, only narrower than the field it described.

**This is the shape the trace term was written for.** $\mu_{2}^{2}>0$ gives the trace a mass at the origin, so the vacuum sits at $y=0$; a positive quartic in the trace channel keeps it from escaping to large $y$; and a negative $\lambda_{3}$ is allowed only as far as the identity row above permits. **The identity row is therefore the one place the trace channel bites**, and it is the row a reader should check before quoting a negative $\lambda_{3}$.

## The Declared Vacuum, and the Branch Where It Is the Minimum

**Flip the sign and compare the directions at fixed $\operatorname{tr}Ξ^{2}=X$.** The comparison is drawn on the hyperplane $\operatorname{tr}Ξ=0$, and it is drawn there because $\mu_{2}^{2}>0$ puts the minimum of the trace direction on it: the $\mathbf1$ part of $Ξ$ is not a direction the vacuum takes when the trace carries a positive mass.

| direction | $Ξ$ | $R=\operatorname{tr}Ξ^{4}/X^{2}$ | quartic coefficient $c$ |
| --- | --- | --- | --- |
| the declared vacuum | $r\operatorname{diag}(-3,1,1,1)$, $r^{2}=X/12$ | $\tfrac{7}{12}$ | $\tfrac{7}{12}\lambda_{1}+\lambda_{2}$ |
| the even split | $\tfrac{\sqrt X}{2}\operatorname{diag}(1,1,-1,-1)$ | $\tfrac14$ | $\tfrac14\lambda_{1}+\lambda_{2}$ |

**The ratio is bounded by $\tfrac14$ and $\tfrac{7}{12}$ on the hyperplane $\operatorname{tr}Ξ=0$, and both ends are attained.** The lower end is $\operatorname{diag}(1,1,-1,-1)$ by Cauchy–Schwarz, the upper is $\operatorname{diag}(-3,1,1,1)$ and its permutations. **The declared shape is the maximum of $\operatorname{tr}Ξ^{4}$ at fixed $\operatorname{tr}Ξ^{2}$**, which is exactly the direction a negative $\lambda_{1}$ selects.

**So the sign of $\lambda_{1}$ decides between two vacua, and the corpus's is the one the negative sign gives.** With $V=-\mu^{2}X+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}X^{2}$ and $\mu^{2}>0$:

- *If $\lambda_{1}<0$*, the minimum at fixed $X$ is $D$, its depth is $-\mu^{4}/(4c)$ with $c=\tfrac{7}{12}\lambda_{1}+\lambda_{2}>0$ on the cone, and **no cubic is needed**.
- *If $\lambda_{1}>0$*, the minimum is the even split, of depth $-\mu^{4}/(4c)$ with $c=\tfrac14\lambda_{1}+\lambda_{2}$.

**The even split breaks $\mathrm{SU}(4)$ to $\mathrm{SU}(2)\times\mathrm{SU}(2)\times\mathrm{U}(1)$.** Its stabiliser is $S(\mathrm{U}(2)\times\mathrm{U}(2))$, eight generators broken and rank three: not $\mathrm{U}(3)$, and not nothing.

**The trace is a sign, and the potential enforces it.** The identity direction is a competing minimum of its own, with $R=\tfrac14$ and no breaking at all. **$\mu_{2}^{2}(\operatorname{tr}Ξ)^{2}$ is what removes it**: the term is non-negative, it is stationary at $\operatorname{tr}Ξ=0$, and it lifts every direction with a nonzero trace. **So the restriction to the hyperplane $\operatorname{tr}Ξ=0$ is a consequence of $\mu_{2}^{2}>0$ and not a declaration**, and the four vacua of the unconstrained reading become two.

| $\lambda_{1}$ | with $\mu_{2}^{2}>0$ | with $\mu_{2}^{2}=0$ |
| --- | --- | --- |
| $<0$ | $D$, stabiliser $\mathrm{U}(3)$, six eaten | $D$ at every trace, degenerate |
| $>0$ | the even split, $\mathrm{SU}(2)^{2}\times\mathrm{U}(1)$ | the even split at every trace, degenerate |

**A negative $\mu_{2}^{2}$ is a third case and not a fourth vacuum**: the trace then runs to the minimum of the trace channel, and every state above it is shifted by a multiple of the identity. **That shift breaks nothing**, because $\mathbb 1$ commutes with all fifteen generators, so the stabiliser and the mass spectrum are unchanged — which is why the corpus's numbers never depended on the trace and why the correction costs them nothing.

**The corpus's vacuum is the top-left entry, and it needs the sign $\lambda_{1}<0$ and the sign $\mu_{2}^{2}>0$.** Neither is written where the vacuum is declared, and both are consistent with the shape the lepton line, the trace condition and the Yukawa ratio fix.

**The cubic is neither needed nor forbidden.** $\operatorname{tr}Ξ^{3}$ is real for Hermitian $Ξ$, since $\bigl(\operatorname{tr}M^{3}\bigr)^{*}=\operatorname{tr}M^{3}$ on a Hermitian $M$, so the term is $c_{3}\operatorname{tr}Ξ^{3}$ with $c_{3}$ real and **no Hermitian conjugate is needed**; the group allows it, and it lowers $D$ against the even split because $\operatorname{tr}D^{3}<0$. **In the $\lambda_{1}<0$ branch $D$ already wins, so the cubic adds nothing.** In the $\lambda_{1}>0$ branch the quartic gap is $\tfrac13\lambda_{1}X^{2}$; the even split's cubic vanishes, so the cubic must supply the whole of it and $c_{3}\sqrt X\gtrsim0.577\,\lambda_{1}$, while against the identity the threshold is

$$
c_{3}\sqrt X\gtrsim 0.31\,\lambda_{1},
$$

the difference $\tfrac{7}{12}-\tfrac14=\tfrac13$ divided by the cubic's advantage $0.577+0.5$. **That is the branch the cubic would matter in, and it is not the branch the mass matrix uses.**

## The Transition, Read From the Same Potential

**One sign, and the phase changes.**

| $\mu_{\Phi}^{2}$ | minimum | group | vectors | scalars |
| --- | --- | --- | --- | --- |
| $>0$ | $Ξ=0$ | $\mathrm{SU}(4)$, exact | $15$ massless | $16$ massive, degenerate |
| $<0$ | $\lvertΞ\rvert=v_C$, $\lambda_{1}<0$ | $\mathrm{U}(3)$, nine massless vectors | $6$ massive | $10$ massive plus $6$ eaten |

**Whether $M_C$ is a temperature is not settled here, and the article says which reading it uses.** The potential fixes a sign and a direction and carries no scale: the symmetric phase has no $M_C$ in it, and the broken phase's $v_C$ is a ratio of parameters. **A thermal reading would need the finite-temperature effective potential, with a critical temperature of order $\mu_{\Phi}$ and a barrier or none depending on the cubic; a zero-temperature reading takes $M_C$ from the matching.** The block uses the second, which is where its numbers come from, and the first is the question the transition leaves open.

**The boundary is $\mu_{\Phi}^{2}=0$, where the mass vanishes and the one-loop correction decides.** That is [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html)'s question, and it is the reason the classical statement "the symmetric phase is a region" has an edge that is not classical.

**Nothing in the potential fixes $v_C$.** It is $\sqrt{-\mu_{\Phi}^{2}/(2c)}$ with $c$ the quartic coefficient of the chosen direction, so $v_C$ is a ratio of parameters and no more. **The corpus's values of $M_C$ and $v_C$ come from the leptoquark bound and from the matching, not from here**, and this article does not pretend otherwise.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the number of quartics written | contractions of four matrix indices built from $Ξ^{2}$ and $\operatorname{tr}Ξ$ | $4$ |
| the mass at the origin | $\partial^{2}V/\partial\chi^{2}$ at $0$ | $\mu_{\Phi}^{2}$ on $15$, $\mu_{\Phi}^{2}+4\mu_{2}^{2}$ on the trace |
| the trace's quadratic coefficient | $(\operatorname{tr}\mathbb 1)^{2}/\operatorname{tr}\mathbb 1^{2}$ | $4$ |
| the degeneracy group at the origin | the quadratic form | $\mathrm{U}(4)$ for $\mu_{2}^{2}\neq0$; $\mathrm{O}(16)$ only at $\mu_{2}^{2}=0$ |
| the Goldstone count above $M_C$ | broken generators | $0$ |
| the boundedness cone, traceless | $\frac14x^{2}\le s_{2}\le x^{2}$ | $\lambda_{1}+\lambda_{2}\ge0$, $\lambda_{1}+4\lambda_{2}\ge0$ |
| the trace-channel conditions | the identity and a single entry | $\tfrac14\lambda_{1}+\lambda_{2}+4\lambda_{3}+16\lambda_{4}\ge0$, $\lambda_{1}+\lambda_{2}+\lambda_{3}+\lambda_{4}\ge0$ |
| the cone's scope | the fifth quartic set to zero | the conditions hold for $\lambda_{5}=0$; a nonzero $\lambda_{5}$ needs its own row |
| the binding direction | one end per sign of $\lambda_{1}$ | a single entry, then the identity |
| the range of $\operatorname{tr}Ξ^{4}/X^{2}$, $\operatorname{tr}Ξ=0$ | $[\tfrac14,\tfrac{7}{12}]$ | the maximum at $D$ |
| the depth ratio, declared over even split | $\tfrac14\div\tfrac{7}{12}$ | $\tfrac37$ |
| the cubic's value on the declared direction | $-24r^{3}$ with $r^{2}=X/12$ | $-\tfrac{1}{\sqrt3}X^{3/2}$ |
| the threshold for the declared vacuum | only in the $\lambda_{1}>0$ branch | $0.577\lambda_{1}$, or $0.31\lambda_{1}$ against the identity |

**The cone and the range are the two computations that could have come out otherwise**, and both follow from one inequality, $\frac14x^{2}\le\operatorname{tr}A^{2}\le x^{2}$ at fixed $\operatorname{tr}A=x$. **Its two ends are two different directions** — the identity at the lower end, a single entry at the upper — and each one decides the sign of $\lambda_{1}$ it belongs to.

## Distinctions That Are Easy to Lose

A symmetric minimum is not a fine tuning. $\mu_{\Phi}^{2}>0$ is a region, and the phase exists for every value in it; the tuning question belongs to the boundary at $\mu_{\Phi}^{2}=0$ and to the one-loop correction there.

A declared vacuum is a chosen branch. $D$'s shape follows from the lepton line, the trace condition and the Yukawa ratio; its status as the minimum needs the sign $\lambda_{1}<0$ and the sign $\mu_{2}^{2}>0$, and neither is written where the vacuum is declared. **The two statements are different and this article keeps them apart.**

A traceless vacuum is not a traceless field. $\operatorname{tr}Ξ=0$ at the minimum is a consequence of $\mu_{2}^{2}>0$ and not a condition on $Ξ$, and the sixteen components are sixteen at every scale. **Deleting the trace from the field would change the survivor count from ten to nine** and the one-loop multiplicity from sixteen to fifteen.

A bounded potential is not a stable one. Boundedness is a statement about $V_{4}$ at large field; stability is a statement about the minimum, and the one-loop correction can move it.

## Summary

**Two quadratics and four quartics, with six free coefficients and no odd term at the order the group requires.** The symmetric minimum is $\mu_{\Phi}^{2}>0$ with $\mu_{2}^{2}>0$, the fifteen traceless components sit at $\mu_{\Phi}^{2}$ and the trace at $\mu_{\Phi}^{2}+4\mu_{2}^{2}$, and the degeneracy at the origin is $\mathrm{U}(4)$ for $\mu_{2}^{2}\neq0$ and $\mathrm{O}(16)$ only at $\mu_{2}^{2}=0$.

**The boundedness cone is $\lambda_{1}+\lambda_{2}\ge0$ and $\lambda_{1}+4\lambda_{2}\ge0$ on the traceless slice**, the rank-one end binding for $\lambda_{1}<0$ and the identity end for $\lambda_{1}>0$; the factor four is $\operatorname{tr}\mathbb{1}$. **Neither half is sufficient alone**, and $\lambda_{1}\ge0$ is stronger than the cone. **The trace channel adds two rows, the identity and a single entry**, and the identity row is the one that limits a negative $\lambda_{3}$.

**The declared vacuum is the minimum in one branch of this potential.** On the hyperplane $\operatorname{tr}Ξ=0$ the ratio $\operatorname{tr}Ξ^{4}/\operatorname{tr}Ξ^{2}$ ranges over $[\tfrac14,\tfrac{7}{12}]$ with the maximum at $D$, so $\lambda_{1}<0$ selects $D$ and $\lambda_{1}>0$ selects the even split $\tfrac12\operatorname{diag}(1,1,-1,-1)$. **Two signs and no cubic are the whole of it**, and the trace sign is what makes the hyperplane the right one to compare on.

**And the phase itself needs none of this.** Above $M_C$ the statement is two signs and two masses: no vacuum, no Goldstone, fifteen massless vectors, sixteen massive scalars with the fifteen degenerate, and a group that is exact.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mu_{\Phi}^{2}$ | the quadratic coefficient of $\operatorname{tr}Ξ^{2}$; positive above $M_C$ |
| $\mu_{2}^{2}$ | the quadratic coefficient of $(\operatorname{tr}Ξ)^{2}$; positive, and that sign is what puts the vacuum on the traceless hyperplane |
| $\lambda_{1}$, $\lambda_{2}$ | the two quartic coefficients of the traceless channel |
| $\lambda_{3}$, $\lambda_{4}$ | the two quartic coefficients that carry the trace |
| $c_{3}$ | the real coefficient of $\operatorname{tr}Ξ^{3}$; absent in the minimal potential, and needed for $D$ only in the $\lambda_{1}>0$ branch |
| $A$ | $Ξ^{\dagger}Ξ$, positive semi-definite with eigenvalues $a_{i}$ |
| $x$, $s_{2}$ | $\operatorname{tr}A$ and $\operatorname{tr}A^{2}$ |
| $y$ | $\operatorname{tr}Ξ$, the trace mode: $y^{2}\le4x$ |
| $X$ | $\operatorname{tr}Ξ^{2}$ at which directions are compared |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the declared vacuum's shape |

## Further Reading

- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). What the declared vacuum does to the fifteen once it is assumed.
- [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html). The boundary of this article's region, at $\mu_{\Phi}^{2}=0$.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html). The kinetic term beside this potential, and where the metric structure that produces the quartics comes from.
- [The Scalar's Two Indices](the-scalars-two-colour-indices-and-the-count-sixteen.html). The field whose sixteen components are counted here.
