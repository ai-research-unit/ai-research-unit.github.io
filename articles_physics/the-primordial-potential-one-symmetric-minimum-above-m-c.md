# __The Primordial Potential: One Symmetric Minimum Above $M_C$__

## Introduction

**The question.** What must the potential of the unbroken phase look like for the group to be exact, and what does the same potential do when the sign of its quadratic term flips?

**The answer.** With $\mu_{\Phi}^{2}>0$ and a bounded quartic, the minimum is at $\Phi=0$; every one of the sixteen real components is massive with the same mass $\mu_{\Phi}$; no direction is eaten; and the group is exact. **The symmetric phase is not a fine-tuned point but a region of parameter space**, and the article states its boundaries.

**One result of this article is negative and it is stated first.** The corpus's declared vacuum, $D=\operatorname{diag}(-3,1,1,1)$ up to scale, **is not the minimum of the two-quartic potential the model otherwise writes.** The identity direction is always deeper. Reaching the declared vacuum needs a cubic term, and §*The Declared Vacuum Is Not the Minimum* computes the gap and the coefficient that closes it.

**What this article does.** It writes the potential, derives the condition for the symmetric minimum, computes the mass spectrum there, derives the boundedness cone, and then confronts the potential with the vacuum the transition assumes.

**What it does not do.** It does not run the potential, does not compute the one-loop correction — [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html) does — and does not fix any coefficient. **Three coefficients and the group fixes none of them.**

## The Potential

**Two quartics, one quadratic, and no odd term at the level the group requires.**

$$
V(\Phi)=\mu_{\Phi}^{2}\operatorname{tr}\Phi^{\dagger}\Phi
+\lambda_{1}\operatorname{tr}\bigl(\Phi^{\dagger}\Phi\bigr)^{2}
+\lambda_{2}\bigl(\operatorname{tr}\Phi^{\dagger}\Phi\bigr)^{2},
$$

with $\Phi$ the Hermitian $4\times4$ matrix of [The Scalar's Two Indices](the-scalars-two-colour-indices-and-the-count-sixteen.html), the trace taken over colour, and the copy index summed.

**Why two quartics and not one.** $\operatorname{tr}(\Phi^{\dagger}\Phi)^{2}$ and $(\operatorname{tr}\Phi^{\dagger}\Phi)^{2}$ are different contractions of four matrix indices. **Neither is a function of the other**, and a vector-valued scalar would admit only one of them. [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-two-quartics.html) tabulates the count.

**Why no cubic, yet.** $\operatorname{tr}\Phi^{3}$ is invariant when $\Phi\to U\Phi U^{\dagger}$, so the group does not forbid it. **It is omitted here because the symmetric phase does not need it** and because it is not real for a complex $\Phi$ unless written with its conjugate. §*The Declared Vacuum Is Not the Minimum* shows what its absence costs.

**Why no term of degree six.** It is irrelevant for the questions this article asks, and its omission is a truncation of the potential stated as one.

## The Symmetric Minimum

**The condition is one sign, and it is not a tuning.**

$$
\frac{\partial V}{\partial\Phi^{\dagger}}\bigg\rvert_{\Phi=0}=\mu_{\Phi}^{2}\Phi=0
\quad\Longleftrightarrow\quad
\Phi=0 ,
$$

which is a minimum and not a saddle when $\mu_{\Phi}^{2}>0$. **Every direction is equivalent at the origin**, so the statement is one-dimensional: the quadratic form is $\mu_{\Phi}^{2}\operatorname{tr}\Phi^{\dagger}\Phi=\mu_{\Phi}^{2}\sum_{i,j}\lvert\Phi_{ij}\rvert^{2}$.

**The mass spectrum at the origin, and its degeneracy.**

$$
m^{2}_{ij}=\mu_{\Phi}^{2}\quad\text{for all }16\text{ real components},
\qquad
m_{\Phi}=\mu_{\Phi} .
$$

**The degeneracy is not an accident of the group; it is larger than the group.** At $\Phi=0$ the quadratic part is invariant under all of $\mathrm{O}(16)$, because every component enters through the same sum of squares, $\operatorname{tr}\Phi^{2}$. **The unbroken phase therefore has an accidental symmetry that the quartic terms break**, and the breaking of that accidental symmetry by $\lambda_{1}$ and $\lambda_{2}$ is what will make the transition's direction a dynamical choice rather than a symmetric one.

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

Write $A=\Phi^{\dagger}\Phi$, a positive semi-definite Hermitian matrix with eigenvalues $a_{1},\dots,a_{4}\ge0$, and let $x=\operatorname{tr}A$ and $s_{2}=\operatorname{tr}A^{2}$. The quartic is

$$
V_{4}=\lambda_{1}s_{2}+\lambda_{2}x^{2} .
$$

**At fixed $x$ the smallest $s_{2}$ is $x^{2}/4$**, attained when all four eigenvalues are equal, because $\sum a_{i}^{2}\ge\frac{1}{4}\bigl(\sum a_{i}\bigr)^{2}$ with equality at $a_{1}=\dots=a_{4}$.

- *If $\lambda_{1}\ge0$*, then $V_{4}\ge x^{2}\bigl(\lambda_{1}/4+\lambda_{2}\bigr)$, so boundedness needs $\lambda_{1}+4\lambda_{2}\ge0$.
- *If $\lambda_{1}<0$*, then $s_{2}$ can grow at fixed $x$, and $V_{4}\to-\infty$; so $\lambda_{1}<0$ is excluded.

$$
\boxed{\;\lambda_{1}\ge0\quad\text{and}\quad\lambda_{1}+4\lambda_{2}\ge0 .\;}
$$

**The condition is weaker than the naive one and the factor is the group's.** The frequently quoted bound $\lambda_{1}+\lambda_{2}>0$ comes from the rank-one direction $A=rE_{11}$, where $s_{2}=x^{2}$. **The binding direction is the identity**, where $s_{2}=x^{2}/4$, and the ratio $4$ is $\operatorname{tr}\mathbb{1}$ for $\mathrm{SU}(4)$. **A potential bounded on the rank-one directions alone can still be unbounded**, and the gap between the two conditions is a factor of four.

## The Declared Vacuum Is Not the Minimum

**Flip the sign and compare three directions at fixed $\operatorname{tr}\Phi^{2}=X$.**

| direction | $\Phi$ | $\operatorname{tr}\Phi^{4}/X^{2}$ | $V_{\min}$ at $\lambda_{2}=0$ |
| --- | --- | --- | --- |
| the identity | $\frac{\sqrt X}{2}\mathbb{1}$ | $\tfrac14$ | $-\mu^{4}/\lambda_{1}$ |
| the declared vacuum | $r\operatorname{diag}(-3,1,1,1)$, $r^{2}=X/12$ | $\tfrac{7}{12}$ | $-\tfrac{3}{7}\,\mu^{4}/\lambda_{1}$ |
| a single entry | $rE_{11}$, $r^{2}=X$ | $1$ | $-\tfrac14\,\mu^{4}/\lambda_{1}$ |

**The identity is the deepest, by a factor $\tfrac73$ over the declared vacuum and by $4$ over a single entry.** The column is computed from $V_{\min}=-\mu^{4}/(4c)$ where $c$ is the quartic coefficient at fixed $X$: $\tfrac14\lambda_{1}$, $\tfrac{7}{12}\lambda_{1}$ and $\lambda_{1}$.

**So the two-quartic potential breaks $\mathrm{SU}(4)$ to nothing at all.** The identity direction preserves the group entirely — it is the statement that $\Phi\propto\mathbb{1}$ commutes with every generator — and the other two are not distinguished in the right order. **A potential whose deepest direction is the identity has no transition in it.**

**What the declared vacuum needs.** The cubic, taken with its conjugate,

$$
V\supset c_{3}\bigl(\operatorname{tr}\Phi^{3}+\text{h.c.}\bigr),
$$

whose value on the three directions at fixed $X$ is $+\tfrac12 c_{3}X^{3/2}$ for the identity, $-\tfrac{1}{\sqrt3}c_{3}X^{3/2}$ for the declared vacuum, and $+c_{3}X^{3/2}$ for a single entry. **The cubic lowers the declared direction and raises the other two**, and with $\lambda_{2}=0$ the declared direction wins once

$$
c_{3}\sqrt X\gtrsim 0.31\,\lambda_{1} ,
$$

which is the difference $\tfrac{7}{12}-\tfrac14=\tfrac13$ of $\lambda_{1}$ divided by the cubic's advantage $0.577+0.5$.

**That is the honest status of the corpus's vacuum.** $D=\operatorname{diag}(-3,1,1,1)$ is declared, and the lepton-line argument and the trace condition fix its *shape*. **What the corpus has not done is write the term that makes the shape the minimum**, and this article states the gap rather than closing it by silence: the two-quartic potential prefers the identity, and the cubic is the term that prefers $D$.

**Why the corpus's $D$ is still the right shape to declare.** Three facts about the declared direction survive the correction and are independent of the potential: its trace is zero, so the $\mathbf1$ part of $\Phi$ does not take a vacuum; its eigenvalues are integers in the ratio $(-3,1,1,1)$, so the stabiliser is $\mathrm{U}(3)$ and the eaten count is six; and its entries give the $3:1$ ratio the Yukawa sector needs. **The shape is fixed by those three requirements; only its status as a minimum is unfinished business**, and it is named here.

## The Transition, Read From the Same Potential

**One sign, and the phase changes.**

| $\mu_{\Phi}^{2}$ | minimum | group | vectors | scalars |
| --- | --- | --- | --- | --- |
| $>0$ | $\Phi=0$ | $\mathrm{SU}(4)$, exact | $15$ massless | $16$ massive, degenerate |
| $<0$ | $\lvert\Phi\rvert=v_C$ | $\mathrm{U}(3)$, nine massless vectors | $6$ massive | $10$ massive plus $6$ eaten |

**The boundary is $\mu_{\Phi}^{2}=0$, where the mass vanishes and the one-loop correction decides.** That is [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html)'s question, and it is the reason the classical statement "the symmetric phase is a region" has an edge that is not classical.

**Nothing in the potential fixes $v_C$.** It is $\sqrt{-\mu_{\Phi}^{2}/(2c)}$ with $c$ the quartic coefficient of the chosen direction, so $v_C$ is a ratio of parameters and no more. **The corpus's values of $M_C$ and $v_C$ come from the leptoquark bound and from the matching, not from here**, and this article does not pretend otherwise.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the number of quartics | contractions of four matrix indices | $2$ |
| the mass at the origin | $\partial^{2}V/\partial\Phi^{2}$ at $0$ | $\mu_{\Phi}^{2}$ on all $16$ |
| the degeneracy group at the origin | the quadratic form in $\operatorname{tr}\Phi^{2}$ | $\mathrm{O}(16)$, larger than $\mathrm{SU}(4)$ |
| the Goldstone count above $M_C$ | broken generators | $0$ |
| the boundedness cone | $\lambda_{1}\ge0$, $\lambda_{1}+4\lambda_{2}\ge0$ | from $s_{2}\ge x^{2}/4$ |
| the binding direction | all four eigenvalues equal | the identity |
| the depth ratio, identity over declared | $\tfrac{7}{12}\div\tfrac14$ | $\tfrac73$ |
| the depth ratio, identity over single entry | $1\div\tfrac14$ | $4$ |
| the cubic's value on the declared direction | $-24r^{3}$ with $r^{2}=X/12$ | $-\tfrac{1}{\sqrt3}X^{3/2}$ |
| the threshold for the declared vacuum | $\tfrac13\lambda_{1}/(0.577+0.5)$ | $c_{3}\sqrt X\gtrsim0.31\lambda_{1}$ |

**The boundedness row and the depth rows are the two computations that could have come out otherwise**, and both are decided by the same fact: the identity direction minimises $\operatorname{tr}A^{2}$ at fixed $\operatorname{tr}A$. **One inequality, two consequences**, and the factor $4$ appears in both.

## Distinctions That Are Easy to Lose

A symmetric minimum is not a fine tuning. $\mu_{\Phi}^{2}>0$ is a region, and the phase exists for every value in it; the tuning question belongs to the boundary at $\mu_{\Phi}^{2}=0$ and to the one-loop correction there.

A declared vacuum is not a derived one. $D$'s shape follows from the lepton line, the trace condition and the Yukawa ratio; its status as the minimum needs a term the corpus has not written. **The two statements are different and this article keeps them apart.**

A bounded potential is not a stable one. Boundedness is a statement about $V_{4}$ at large field; stability is a statement about the minimum, and the one-loop correction can move it.

## Summary

**Two quartics and one quadratic, with three free coefficients and no odd term at the order the group requires.** The symmetric minimum is $\mu_{\Phi}^{2}>0$, the mass is $\mu_{\Phi}$ on all sixteen real components, and the degeneracy at the origin is $\mathrm{O}(16)$ rather than $\mathrm{SU}(4)$.

**The boundedness cone is $\lambda_{1}\ge0$ and $\lambda_{1}+4\lambda_{2}\ge0$**, and the binding direction is the identity because $\operatorname{tr}A^{2}\ge\frac14(\operatorname{tr}A)^{2}$. The naive rank-one bound is weaker by a factor of four and is not sufficient.

**The declared vacuum is not the minimum of this potential.** At fixed $\operatorname{tr}\Phi^{2}$ the identity direction is deeper than $D$ by $\tfrac73$ and deeper than a single entry by $4$. Reaching $D$ needs $c_{3}(\operatorname{tr}\Phi^{3}+\text{h.c.})$ with $c_{3}\sqrt X\gtrsim0.31\lambda_{1}$, and writing that term is left as the model's open item rather than assumed away.

**And the phase itself needs none of this.** Above $M_C$ the statement is one sign and one degeneracy: no vacuum, no Goldstone, fifteen massless vectors, sixteen degenerate scalars, and a group that is exact.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mu_{\Phi}^{2}$ | the quadratic coefficient; positive above $M_C$ |
| $\lambda_{1}$, $\lambda_{2}$ | the two quartic coefficients |
| $c_{3}$ | the cubic coefficient, absent in the minimal potential and needed for $D$ |
| $A$ | $\Phi^{\dagger}\Phi$, positive semi-definite with eigenvalues $a_{i}$ |
| $x$, $s_{2}$ | $\operatorname{tr}A$ and $\operatorname{tr}A^{2}$ |
| $X$ | $\operatorname{tr}\Phi^{2}$ at which directions are compared |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the declared vacuum's shape |

## Further Reading

- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). What the declared vacuum does to the fifteen once it is assumed.
- [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html). The boundary of this article's region, at $\mu_{\Phi}^{2}=0$.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-two-quartics.html). The kinetic term beside this potential, and the two quartics' origin.
- [The Scalar's Two Indices](the-scalars-two-colour-indices-and-the-count-sixteen.html). The field whose sixteen components are counted here.
