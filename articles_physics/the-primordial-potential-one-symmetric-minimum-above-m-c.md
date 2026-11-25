# __The Primordial Potential: One Symmetric Minimum Above $M_C$__

## Introduction

**The question.** What must the potential of the unbroken phase look like for the group to be exact, and what does the same potential do when the sign of its quadratic term flips?

**The answer.** With $\mu_{\Phi}^{2}>0$ and a bounded quartic, the minimum is at $Ξ=0$; every one of the sixteen real components is massive with the common mass $\sqrt2\,\mu_{\Phi}$; no direction is eaten; and the group is exact. **The symmetric phase is not a fine-tuned point but a region of parameter space**, and the article states its boundaries.

**One result of this article is a condition and it is stated first.** The corpus's declared vacuum, $D=\operatorname{diag}(-3,1,1,1)$ up to scale, **is the minimum of the two-quartic potential in the branch $\lambda_{1}<0$, once $\operatorname{tr}Ξ=0$ is imposed, and it is not the minimum in the branch $\lambda_{1}>0$.** No cubic is needed; a sign and a trace declaration are, and §*The Declared Vacuum, and the Branch Where It Is the Minimum* states bothat closes it.

**What this article does.** It writes the potential, derives the condition for the symmetric minimum, computes the mass spectrum there, derives the boundedness cone, and then confronts the potential with the vacuum the transition assumes.

**What it does not do.** It does not run the potential, does not compute the one-loop correction — [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html) does — and does not fix any coefficient. **Three coefficients and the group fixes none of them.**

## The Potential

**Two quartics, one quadratic, and no odd term at the level the group requires.**

$$
V(Ξ)=\mu_{\Phi}^{2}\operatorname{tr}Ξ^{\dagger}Ξ
+\lambda_{1}\operatorname{tr}\bigl(Ξ^{\dagger}Ξ\bigr)^{2}
+\lambda_{2}\bigl(\operatorname{tr}Ξ^{\dagger}Ξ\bigr)^{2},
$$

with $Ξ$ the Hermitian $4\times4$ matrix of [The Scalar's Two Indices](the-scalars-two-colour-indices-and-the-count-sixteen.html), the trace taken over colour, and no copy index on $Ξ$: one Hermitian matrix, sixteen real parameters.

**Why two quartics and not one.** $\operatorname{tr}(Ξ^{\dagger}Ξ)^{2}$ and $(\operatorname{tr}Ξ^{\dagger}Ξ)^{2}$ are different contractions of four matrix indices. **Neither is a function of the other**, and a vector-valued scalar would admit only one of them. [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-two-quartics.html) tabulates the count.

**Why no cubic, yet.** $\operatorname{tr}Ξ^{3}$ is invariant when $Ξ\to UΞ U^{\dagger}$ and real for Hermitian $Ξ$, so the group allows it and the term is legitimate. **It is omitted because neither phase needs it**: the symmetric minimum is at $Ξ=0$ without it, and the declared vacuum is selected by $\lambda_{1}<0$ without it. §*The Declared Vacuum, and the Branch Where It Is the Minimum* shows what its absence costs.

**Why no term of degree six.** It is irrelevant for the questions this article asks, and its omission is a truncation of the potential stated as one.

## The Symmetric Minimum

**The condition is one sign, and it is not a tuning.**

$$
\frac{\partial V}{\partialΞ^{\dagger}}\bigg\rvert_{Ξ=0}=\mu_{\Phi}^{2}Ξ=0
\quad\Longleftrightarrow\quad
Ξ=0 ,
$$

which is a minimum and not a saddle when $\mu_{\Phi}^{2}>0$. **Every direction is equivalent at the origin**, so the statement is one-dimensional: the quadratic form is $\mu_{\Phi}^{2}\operatorname{tr}Ξ^{\dagger}Ξ=\mu_{\Phi}^{2}\sum_{i,j}\lvertΞ_{ij}\rvert^{2}$.

**The mass spectrum at the origin, and its degeneracy.**

$$
m^{2}_{ij}=2\mu_{\Phi}^{2}\quad\text{for all }16\text{ real components},
\qquad
m_{\Phi}=\sqrt2\,\mu_{\Phi} .
$$

**The degeneracy is not an accident of the group; it is larger than the group.** At $Ξ=0$ the quadratic part is invariant under all of $\mathrm{O}(16)$, because every component enters through the same sum of squares, $\operatorname{tr}Ξ^{2}$. **The unbroken phase therefore has an accidental symmetry that the quartic terms break**, and the breaking of that accidental symmetry by $\lambda_{1}$ and $\lambda_{2}$ is what will make the transition's direction a dynamical choice rather than a symmetric one.

**Consequences, stated as counts.**

| statement | reason | value |
| --- | --- | --- |
| the number of Goldstone bosons | no generator is broken | $0$ |
| the number of eaten directions | no vector is massive | $0$ |
| the number of massive scalars | all components | $16$ |
| the number of massless vectors | no vacuum | $15$ |

**The last row is the phase's defining property.** Fifteen massless vectors, sixteen massive scalars, and no scale in the gauge sector at all: **the unbroken phase has no $M_C$ in it**, and $M_C$ is the scale at which the vacuum forms.

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

## The Declared Vacuum, and the Branch Where It Is the Minimum

**Flip the sign and compare the directions at fixed $\operatorname{tr}Ξ^{2}=X$.** The comparison is drawn on the hyperplane $\operatorname{tr}Ξ=0$, because that is the corpus's declaration: the $\mathbf1$ part of $Ξ$ does not take a vacuum.

| direction | $Ξ$ | $R=\operatorname{tr}Ξ^{4}/X^{2}$ | quartic coefficient $c$ |
| --- | --- | --- | --- |
| the declared vacuum | $r\operatorname{diag}(-3,1,1,1)$, $r^{2}=X/12$ | $\tfrac{7}{12}$ | $\tfrac{7}{12}\lambda_{1}+\lambda_{2}$ |
| the even split | $\tfrac{\sqrt X}{2}\operatorname{diag}(1,1,-1,-1)$ | $\tfrac14$ | $\tfrac14\lambda_{1}+\lambda_{2}$ |

**The ratio is bounded by $\tfrac14$ and $\tfrac{7}{12}$ on the hyperplane $\operatorname{tr}Ξ=0$, and both ends are attained.** The lower end is $\operatorname{diag}(1,1,-1,-1)$ by Cauchy–Schwarz, the upper is $\operatorname{diag}(-3,1,1,1)$ and its permutations. **The declared shape is the maximum of $\operatorname{tr}Ξ^{4}$ at fixed $\operatorname{tr}Ξ^{2}$**, which is exactly the direction a negative $\lambda_{1}$ selects.

**So the sign of $\lambda_{1}$ decides between two vacua, and the corpus's is the one the negative sign gives.** With $V=-\mu^{2}X+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}X^{2}$ and $\mu^{2}>0$:

- *If $\lambda_{1}<0$*, the minimum at fixed $X$ is $D$, its depth is $-\mu^{4}/(4c)$ with $c=\tfrac{7}{12}\lambda_{1}+\lambda_{2}>0$ on the cone, and **no cubic is needed**.
- *If $\lambda_{1}>0$*, the minimum is the even split, of depth $-\mu^{4}/(4c)$ with $c=\tfrac14\lambda_{1}+\lambda_{2}$.

**The even split breaks $\mathrm{SU}(4)$ to $\mathrm{SU}(2)\times\mathrm{SU}(2)\times\mathrm{U}(1)$.** Its stabiliser is $S(\mathrm{U}(2)\times\mathrm{U}(2))$, eight generators broken and rank three: not $\mathrm{U}(3)$, and not nothing.

**The trace is a declaration, and the potential does not enforce it.** Nothing in $V$ singles out $\operatorname{tr}Ξ=0$; the identity direction is a competing minimum of its own, with $R=\tfrac14$ and no breaking at all. **Read without the declaration, the two branches give four different vacua.**

| $\lambda_{1}$ | with $\operatorname{tr}Ξ=0$ imposed | without it |
| --- | --- | --- |
| $<0$ | $D$, stabiliser $\mathrm{U}(3)$, six eaten | a single entry, $\mathrm{SU}(3)\times\mathrm{U}(1)$ |
| $>0$ | the even split, $\mathrm{SU}(2)^{2}\times\mathrm{U}(1)$ | the identity, $\mathrm{SU}(4)$ exact |

**The corpus's vacuum is the top-left entry, and it needs the sign $\lambda_{1}<0$ and the declaration $\operatorname{tr}Ξ=0$.** Neither is written where the vacuum is declared, and both are consistent with the shape the lepton line, the trace condition and the Yukawa ratio fix.

**The cubic is neither needed nor forbidden.** $\operatorname{tr}Ξ^{3}$ is real for Hermitian $Ξ$, so $c_{3}(\operatorname{tr}Ξ^{3}+\text{h.c.})=2c_{3}\operatorname{tr}Ξ^{3}$; the group allows it, and it lowers $D$ against the even split because $\operatorname{tr}D^{3}<0$. **In the $\lambda_{1}<0$ branch $D$ already wins, so the cubic adds nothing.** In the $\lambda_{1}>0$ branch the quartic gap is $\tfrac13\lambda_{1}X^{2}$; the even split's cubic vanishes, so the cubic must supply the whole of it and $c_{3}\sqrt X\gtrsim0.577\,\lambda_{1}$, while against the identity the threshold is

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
| the number of quartics | contractions of four matrix indices | $2$ |
| the mass at the origin | $\partial^{2}V/\partialΞ^{2}$ at $0$ | $2\mu_{\Phi}^{2}$ on all $16$ |
| the degeneracy group at the origin | the quadratic form in $\operatorname{tr}Ξ^{2}$ | $\mathrm{O}(16)$, larger than $\mathrm{SU}(4)$ |
| the Goldstone count above $M_C$ | broken generators | $0$ |
| the boundedness cone | $\frac14x^{2}\le s_{2}\le x^{2}$ | $\lambda_{1}+\lambda_{2}\ge0$, $\lambda_{1}+4\lambda_{2}\ge0$ |
| the binding direction | one end per sign of $\lambda_{1}$ | a single entry, then the identity |
| the range of $\operatorname{tr}Ξ^{4}/X^{2}$, $\operatorname{tr}Ξ=0$ | $[\tfrac14,\tfrac{7}{12}]$ | the maximum at $D$ |
| the depth ratio, declared over even split | $\tfrac14\div\tfrac{7}{12}$ | $\tfrac37$ |
| the cubic's value on the declared direction | $-24r^{3}$ with $r^{2}=X/12$ | $-\tfrac{1}{\sqrt3}X^{3/2}$ |
| the threshold for the declared vacuum | only in the $\lambda_{1}>0$ branch | $0.577\lambda_{1}$, or $0.31\lambda_{1}$ against the identity |

**The cone and the range are the two computations that could have come out otherwise**, and both follow from one inequality, $\frac14x^{2}\le\operatorname{tr}A^{2}\le x^{2}$ at fixed $\operatorname{tr}A=x$. **Its two ends are two different directions** — the identity at the lower end, a single entry at the upper — and each one decides the sign of $\lambda_{1}$ it belongs to.

## Distinctions That Are Easy to Lose

A symmetric minimum is not a fine tuning. $\mu_{\Phi}^{2}>0$ is a region, and the phase exists for every value in it; the tuning question belongs to the boundary at $\mu_{\Phi}^{2}=0$ and to the one-loop correction there.

A declared vacuum is a chosen branch. $D$'s shape follows from the lepton line, the trace condition and the Yukawa ratio; its status as the minimum needs the sign $\lambda_{1}<0$ and the declaration $\operatorname{tr}Ξ=0$, and neither is written where the vacuum is declared. **The two statements are different and this article keeps them apart.**

A bounded potential is not a stable one. Boundedness is a statement about $V_{4}$ at large field; stability is a statement about the minimum, and the one-loop correction can move it.

## Summary

**Two quartics and one quadratic, with three free coefficients and no odd term at the order the group requires.** The symmetric minimum is $\mu_{\Phi}^{2}>0$, the mass is $\sqrt2\,\mu_{\Phi}$ on all sixteen real components, and the degeneracy at the origin is $\mathrm{O}(16)$ rather than $\mathrm{SU}(4)$.

**The boundedness cone is $\lambda_{1}+\lambda_{2}\ge0$ and $\lambda_{1}+4\lambda_{2}\ge0$**, the rank-one end binding for $\lambda_{1}<0$ and the identity end for $\lambda_{1}>0$; the factor four is $\operatorname{tr}\mathbb{1}$. **Neither half is sufficient alone**, and $\lambda_{1}\ge0$ is stronger than the cone.

**The declared vacuum is the minimum in one branch of this potential.** On the hyperplane $\operatorname{tr}Ξ=0$ the ratio $\operatorname{tr}Ξ^{4}/\operatorname{tr}Ξ^{2}$ ranges over $[\tfrac14,\tfrac{7}{12}]$ with the maximum at $D$, so $\lambda_{1}<0$ selects $D$ and $\lambda_{1}>0$ selects the even split $\tfrac12\operatorname{diag}(1,1,-1,-1)$. **The sign and the trace declaration are the two conditions**, and no cubic is needed.

**And the phase itself needs none of this.** Above $M_C$ the statement is one sign and one degeneracy: no vacuum, no Goldstone, fifteen massless vectors, sixteen degenerate scalars, and a group that is exact.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mu_{\Phi}^{2}$ | the quadratic coefficient; positive above $M_C$ |
| $\lambda_{1}$, $\lambda_{2}$ | the two quartic coefficients |
| $c_{3}$ | the cubic coefficient; absent in the minimal potential, and needed for $D$ only in the $\lambda_{1}>0$ branch |
| $A$ | $Ξ^{\dagger}Ξ$, positive semi-definite with eigenvalues $a_{i}$ |
| $x$, $s_{2}$ | $\operatorname{tr}A$ and $\operatorname{tr}A^{2}$ |
| $X$ | $\operatorname{tr}Ξ^{2}$ at which directions are compared |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the declared vacuum's shape |

## Further Reading

- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). What the declared vacuum does to the fifteen once it is assumed.
- [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html). The boundary of this article's region, at $\mu_{\Phi}^{2}=0$.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-two-quartics.html). The kinetic term beside this potential, and the two quartics' origin.
- [The Scalar's Two Indices](the-scalars-two-colour-indices-and-the-count-sixteen.html). The field whose sixteen components are counted here.
