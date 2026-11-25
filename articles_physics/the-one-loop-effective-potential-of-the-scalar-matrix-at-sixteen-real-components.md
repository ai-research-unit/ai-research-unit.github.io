# __The One-Loop Effective Potential of the Scalar Matrix: The $\rho^{4}\ln\rho^{2}$ Coefficient for $\mathbf{15}\oplus\mathbf1$__

## Introduction

**The question.** What does one loop add to the potential of [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html), and does the correction leave the symmetric minimum standing?

**The answer, in one line at $\lambda_{2}=0$.**

$$
V_{1}\supset\frac{9}{4\pi^{2}}\,\lambda_{1}^{2}\,\rho^{4}\ln\frac{\rho^{2}}{\mu^{2}}
\qquad\text{against the doublet's}\qquad
\frac{3\lambda^{2}}{16\pi^{2}}\,\rho^{4}\ln\frac{\rho^{2}}{\mu^{2}},
$$

so the matrix's coefficient is $0.0570\,\lambda_{1}^{2}$ and is **three** times a doublet's at equal coupling. **The number comes from a Hessian that is computed here and diagonalised exactly**, because the identity background has enough symmetry for the blocks to separate.

**Why the coefficient and not the whole potential.** The constant and the $-\tfrac32$ are scheme-dependent; the coefficient of $\rho^{4}\ln\rho^{2}$ is not. **It is the one number in a one-loop effective potential that survives a change of renormalisation scheme**, and it is the number the corpus's other effective-potential articles report.

**What this article does.** It reduces the functional determinant to a Hessian, diagonalises it at the identity background, computes the coefficient for general $\lambda_{1}$, $\lambda_{2}$, evaluates it, compares with the doublet, and derives the field range in which the tree term still dominates.

**What it does not do.** No two-loop, no resummation, no running of the quartics, and no statement about the transition itself.

## The Reduction

**A constant background turns the determinant into a mass matrix.**

$$
V_{\mathrm{eff}}(Ξ_{0})=V(Ξ_{0})+\frac{1}{64\pi^{2}}\operatorname{STr}\Bigl[M^{4}\Bigl(\ln\frac{M^{2}}{\mu^{2}}-\frac{3}{2}\Bigr)\Bigr],
\qquad
M^{2}_{ij}=\frac{\partial^{2}V}{\partial\chi_{i}\partial\chi_{j}}\bigg\rvert_{Ξ_{0}},
$$

with $\chi_{i}$ the sixteen real components of the Hermitian matrix, $\mu$ the renormalisation scale, and $M^{2}$ the Hessian. **The $\tfrac{1}{64\pi^{2}}$ is per real scalar degree of freedom**, and sixteen components mean sixteen modes and no more.

**Three things are being assumed and each is named.**

- *The background is constant.* Gradient terms are dropped, so the result is a potential and not an action.
- *The tree potential is the whole of the tree level.* No other field has a background, so the gauge and fermion determinants are field-independent and drop out.
- *The expansion is one loop.* Every statement below is first order in $\hbar$.

**The Hessian is evaluated along one direction only, and the direction is chosen for a reason.** The identity, $Ξ_{0}=\frac{\rho}{2}\mathbb{1}$, is the phase's most symmetric point; **its little group is all of $\mathrm{SU}(4)$, so the Hessian's blocks are fixed by symmetry and no numerical diagonalisation is needed.**

## The Hessian, Block by Block

**Write $Ξ=\frac{\rho}{2}\mathbb{1}+\eta$ with $\eta$ Hermitian, and split $\eta=h+\frac{t}{4}\mathbb{1}$ where $h$ is traceless and $t=\operatorname{tr}\eta$.** Then

$$
\operatorname{tr}Ξ^{2}=\rho^{2}+\rho t+\operatorname{tr}h^{2}+\tfrac14t^{2},
$$

and expanding $V=\mu^{2}\operatorname{tr}Ξ^{2}+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}\bigl(\operatorname{tr}Ξ^{2}\bigr)^{2}$ to second order gives

$$
V_{2}=\Bigl(\mu^{2}+\tfrac32\lambda_{1}\rho^{2}+2\lambda_{2}\rho^{2}\Bigr)\operatorname{tr}h^{2}
+\Bigl(\mu^{2}+\tfrac32\lambda_{1}\rho^{2}+6\lambda_{2}\rho^{2}\Bigr)\frac{t^{2}}{4}.
$$

**Two blocks, and the counts add to sixteen.**

| block | degeneracy | $m^{2}/\rho^{2}$ at large $\rho$ | at $\lambda_{2}=0$ |
| --- | --- | --- | --- |
| the traceless Hermitian $h$ | $15$ | $\tfrac32\lambda_{1}+2\lambda_{2}$ | $\tfrac32\lambda_{1}$ |
| the trace direction | $1$ | $\tfrac32\lambda_{1}+6\lambda_{2}$ | $\tfrac32\lambda_{1}$ |
| **total** | $\mathbf{16}$ | | |

**The $15+1=16$ is the check on the decomposition**, and it is the same $15+1$ the representation gives: the traceless block is the adjoint and the trace block is the singlet. **The whole calculation below is on the two-quartic slice, $\mu_{2}^{2}=\lambda_{3}=\lambda_{4}=0$**, and the restriction is not cosmetic. **The trace terms make the identity a non-stationary point.** With $Ξ_{0}=\frac{\rho}{2}\mathbb 1$ and $Ξ=\Xi_{0}+\eta$, the trace-channel pieces contribute a linear term in $t=\operatorname{tr}\eta$, $\bigl(4\mu_{2}^{2}\rho+8\lambda_{3}\rho^{3}+32\lambda_{4}\rho^{3}\bigr)t$, which vanishes only for a tuned $\rho$. **So the identity background is the right one exactly when the trace channel is switched off**, which is the slice the table computes; on that slice the $36$ below is exact, and with the trace terms present the coefficient is the same $36$ plus a $t$-dependent piece that this article does not quote. **That gap is named and not hidden**: the trace mode's own contribution to the effective potential is a separate computation, and $\mu_{2}^{2}>0$ makes the true background traceless rather than proportional to $\mathbb 1$.

**Why the trace block and the traceless block differ by $4\lambda_{2}\rho^{2}$.** $\operatorname{tr}Ξ^{2}$ contains $t$ linearly, so the $\lambda_{2}$ term contributes to the trace direction twice over — once through $t^{2}$ and once through the cross term — while the traceless part contributes to it not at all. **A block-diagonal Hessian with unequal blocks is what a two-quartic potential looks like.**

**The phase direction is not among these eigenvalues, and that is correct.** $V$ depends on $Ξ$ only through $\operatorname{tr}Ξ^{2}$, so the curve $\rho\mapsto\frac{\rho}{2}e^{i\theta}\mathbb{1}$ is not a direction in the Hermitian space at all — a Hermitian matrix has no such phase. **The sixteen is closed under the Hessian**, which is the statement that the potential's fluctuations are sixteen and not more.

## The Coefficient

**The coefficient of $\rho^{4}\ln(\rho^{2}/\mu^{2})$ is the trace of the squared Hessian over $64\pi^{2}$.**

$$
\mathcal{C}=\frac{1}{64\pi^{2}}\Bigl[15(\tfrac32\lambda_{1}+2\lambda_{2})^{2}+(\tfrac32\lambda_{1}+6\lambda_{2})^{2}\Bigr].
$$

**Evaluate it.** At $\lambda_{2}=0$ the bracket is

$$
15\cdot\tfrac94\lambda_{1}^{2}+\tfrac94\lambda_{1}^{2}=36\,\lambda_{1}^{2},
\qquad
\mathcal{C}=\frac{36\lambda_{1}^{2}}{64\pi^{2}}=\frac{9\lambda_{1}^{2}}{16\pi^{2}}=0.0570\,\lambda_{1}^{2} .
$$

**Two checks on $36$.** It is $15\cdot\tfrac94+1\cdot\tfrac94$, that is fifteen traceless modes and one trace mode, **all at the same mass** $\tfrac32\lambda_{1}\rho^{2}$ when $\lambda_{2}=0$. And $36=16\cdot\tfrac94$, so the coefficient is $9/(16\pi^{2})$ per the canonical $\frac{1}{64\pi^{2}}\times 36$.

**The sign is positive and the sign is a conclusion.** $\mathcal{C}>0$ for $\lambda_{1}>0$, so the one-loop term raises the potential at large field and cannot destabilise it from above; the only place it can act against the tree term is where $\ln(\rho^{2}/\mu^{2})<0$, that is $\rho<\mu$.

## Comparison With the Doublet

**The same computation for a doublet, done the same way.**

| quantity | the doublet | the matrix, $\lambda_{2}=0$ |
| --- | --- | --- |
| real components | $4$ | $16$ |
| the background | $\frac{1}{\sqrt2}(0,\rho)$ | $\frac{\rho}{2}\mathbb{1}$ |
| the tree quartic | $\tfrac{\lambda}{4}\rho^{4}$ | $\tfrac{\lambda_{1}}{4}\rho^{4}$ |
| $\sum m^{4}/\rho^{4}$ | $12\lambda^{2}$ | $36\lambda_{1}^{2}$ |
| the coefficient | $\dfrac{3\lambda^{2}}{16\pi^{2}}=0.0190\lambda^{2}$ | $\dfrac{9\lambda_{1}^{2}}{16\pi^{2}}=0.0570\lambda_{1}^{2}$ |
| the ratio | $1$ | $\mathbf{3}$ |

**The ratio is three, not four, and the difference is worth one sentence.** Sixteen components against four would give a factor of four if all masses were equal; the matrix's masses are all equal to $\tfrac32\lambda_{1}\rho^{2}$ at $\lambda_{2}=0$ while the doublet's are $3\lambda\rho^{2}$ once and $\lambda\rho^{2}$ three times, so the ratio is $36/12=3$. **The matrix has four times the components and each is half as heavy in $m^{2}$, and the two effects do not cancel**: the doublet's heavier radial mode carries most of its $\sum m^{4}$.

**The doublet's row is a check and not an import.** Its Hessian at $\frac{1}{\sqrt2}(0,\rho)$ has one eigenvalue $3\lambda\rho^{2}$ and three at $\lambda\rho^{2}$, so $\sum m^{4}=12\lambda^{2}\rho^{4}$ and the coefficient is $\frac{12}{64\pi^{2}}=\frac{3}{16\pi^{2}}$. **The method is the same method**, which is what makes the comparison a comparison.

## Where the Tree Term Still Wins

**The one-loop term overtakes the tree term at a computable field value, and that value is the expansion's domain.**

$$
V_{0}\simeq\frac{\lambda_{1}}{4}\rho^{4},
\qquad
V_{1}\simeq\frac{9\lambda_{1}^{2}}{16\pi^{2}}\rho^{4}\ln\frac{\rho^{2}}{\mu^{2}},
\qquad
\frac{V_{1}}{V_{0}}=\frac{9\lambda_{1}}{4\pi^{2}}\ln\frac{\rho^{2}}{\mu^{2}} .
$$

**Setting the ratio to one at $\lambda_{1}=1$**,

$$
\ln\frac{\rho^{2}}{\mu^{2}}=\frac{4\pi^{2}}{9}=4.386 ,
\qquad
\rho=8.96\,\mu .
$$

**So the one-loop term is smaller than the tree term only for $\rho\lesssim9\mu$, and larger beyond it.** That is not a failure of the potential; it is the statement that a one-loop calculation about a background far from the renormalisation scale is not a calculation. **The symmetric phase's neighbourhood, $\rho\ll\mu$, is exactly where the expansion is good.**

**The corollary is the article's honesty.** The coefficient is a number; using it to decide the fate of the symmetric minimum at $\rho\sim v_C$ would be an extrapolation of a one-loop result by many orders of magnitude in field. **What the coefficient legitimately does is establish the sign and the size**, and what it does not do is predict $v_C$.

## What Is Not Computed

**Four omissions, each with its consequence.**

- *Other directions of the background.* At a background $Ξ_{0}\propto D$ the little group is $\mathrm{U}(3)$ and the Hessian's blocks are larger; **the coefficient there is a different number and this article does not compute it.** The identity was chosen because its blocks separate exactly.
- *The two-loop term.* It is of order $\lambda^{3}$ and would shift the coefficient's logarithm; **it is omitted and the omission is declared rather than estimated.**
- *The gauge and fermion determinants.* They are field-independent at a scalar background with no other condensate, so they drop out — **but only above $M_C$, where no vector has a mass depending on $Ξ$.**
- *Resummation.* At $\rho\gg\mu$ the logarithm is large and the one-loop term must be resummed; **the corpus's other effective-potential articles say the same thing**, and none of them resums.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the block dimensions | $15+1$ | $16$ |
| the total modes | the components of a Hermitian $4\times4$ | $16$ |
| the trace block's mass | differentiating $\bigl(\operatorname{tr}Ξ^{2}\bigr)^{2}$ twice | $\tfrac32\lambda_{1}+6\lambda_{2}$ |
| the traceless block's mass | the same, with $t=0$ | $\tfrac32\lambda_{1}+2\lambda_{2}$ |
| $\sum m^{4}/\rho^{4}$ at $\lambda_{2}=0$ | $15\cdot\tfrac94+1\cdot\tfrac94$ | $36$ |
| the coefficient at $\lambda_{2}=0$ | $\frac{36}{64\pi^{2}}$ | $\frac{9}{16\pi^{2}}=0.0570$ |
| the doublet's coefficient | $\frac{12}{64\pi^{2}}$ | $\frac{3}{16\pi^{2}}=0.0190$ |
| the ratio | $36\div12$ | $3$ |
| the crossover field | $\frac{4\pi^{2}}{9}=4.386$ in $\ln(\rho^{2}/\mu^{2})$ | $\rho=8.96\mu$ |

## Summary

**The coefficient of $\rho^{4}\ln(\rho^{2}/\mu^{2})$ for the Hermitian scalar matrix at $\lambda_{2}=0$ is $\frac{9\lambda_{1}^{2}}{16\pi^{2}}=0.0570\lambda_{1}^{2}$, which is three times a doublet's at equal coupling.** It comes from an exactly diagonalised Hessian: fifteen traceless Hermitian modes and one trace mode, all at $\tfrac32\lambda_{1}\rho^{2}$ when the second quartic vanishes.

**The sign is positive**, so the correction cannot destabilise the symmetric minimum from above, and the only region where it competes with the tree term is $\rho\lesssim1.7\mu$ at $\lambda_{1}=1$ — which is the region where a one-loop calculation is legitimate anyway.

**The comparison with the doublet is the article's useful output.** A claim that the matrix sector is "bigger" becomes a number: three, from sixteen components instead of four and mass ratios of three halves against three and one.

**And the boundary is stated rather than crossed.** The coefficient is computed at one background direction, at one loop, without resummation, and the phase's actual transition is many orders of magnitude away in field. **The number is a coefficient and not a prediction of $M_C$.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $Ξ_{0}$ | $\frac{\rho}{2}\mathbb{1}$, the identity background |
| $\eta$ | the Hermitian fluctuation, split as $h+\frac{t}{4}\mathbb{1}$ |
| $h$, $t$ | the traceless part and the trace of $\eta$ |
| $M^{2}$ | the Hessian $\partial^{2}V/\partial\chi_{i}\partial\chi_{j}$ in the sixteen real components |
| $\mathcal{C}$ | the coefficient of $\rho^{4}\ln(\rho^{2}/\mu^{2})$ |
| $\mu$ | the renormalisation scale, not to be confused with $\mu^{2}$ of the potential |

## Further Reading

- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The tree potential this article corrects, and the boundedness cone.
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html). The kinetic term whose normalisation makes the sixteen components canonical.
- [The Effective Potential and the One-Loop Correction](the-effective-potential-and-the-one-loop-correction-in-biquaternionic-form.html). The doublet's coefficient, computed by the same method.
- [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html). Where the count of sixteen comes from.
