# __Power Counting on a Frame__

## Introduction

**The question.** Which operators can sit in an action built from the frame, and how many of them are there? The answer is a list, and the list is short. This article writes it, verifies the one identity that trims it, and states what the trimming costs in unknown coefficients.

**Why the question is worth a separate article.** The action article argues that the exact functional is missing and that its missing pieces are the frame-letter variation and the boundary term. That argument would be worth little if the functional's *ingredients* were also missing, because then the gap would be open-ended. They are not. Power counting is a finite procedure, and it terminates at a list that can be read off. So the gap has a shape and a size, and this article is where the size is computed.

**The premise, and it is the whole of the input.** The Gram matrix is the metric, and the metric is dimensionless in the units where it multiplies $dx^{\imath}dx^{\jmath}$ with the coordinate differentials carrying length. So the frame is dimensionless, $\partial_{\imath}$ carries one unit of dimension, and every operator's dimension is the number of derivatives it contains plus the dimensions of its fields. Nothing about the algebra enters that counting. This is the reason the counting is worth doing: it is the one part of the problem that does not depend on which letters the theory is written in.

## The Menu at Dimension Four

An action is a sum of terms of dimension four, each multiplied by a coupling with the dimension that makes up the difference. With the frame dimensionless and the field content of the corpus — the frame, its connection, one complex scalar doublet, one Dirac field, the gauge fields — the terms of dimension four are these.

| operator | derivatives | content | in frame letters |
| --- | --- | --- | --- |
| $\Lambda$ | 0 | a number | the scalar part |
| $\phi^{\dagger}\phi$ (mass) | 0 | scalar bilinear | the scalar sector |
| $\phi^{4}$ | 0 | scalar quartic | the scalar sector |
| $(\bar\psi\psi)^{2}$ | 0 | fermion quartic | contact terms |
| $\bar\psi\,\gamma^{\imath}D_{\imath}\psi$ | 1 | fermion kinetic | the Dirac sector |
| $\bar\psi\psi\,\phi$ | 0 | Yukawa | the mass terms |
| $D_{\imath}\phi\,D^{\imath}\phi^{\dagger}$ | 2 | scalar kinetic | the scalar sector |
| $F_{\imath\jmath}F^{\imath\jmath}$ | 2 | gauge kinetic | the Maxwell sector |
| $\xi\,R\,\phi^{\dagger}\phi$ | 2 | conformal coupling | needs $R$ |
| $R$ | 2 | gravitational kinetic | the trace of the squared Dirac operator |
| $R^{2}$ | 4 | curvature squared | two curvatures multiplied |
| $R_{\imath\jmath}R^{\imath\jmath}$ | 4 | Ricci squared | two curvatures multiplied |
| $R_{\imath\jmath k l}R^{\imath\jmath k l}$ | 4 | Riemann squared | two curvatures multiplied |

Thirteen entries, and the table is complete for this field content: the symmetries of the curvature tensor, the antisymmetry of the field strength, and the requirement that the term be a scalar exhaust the possibilities at each derivative order. Nothing in the algebra's multiplication table appears as a restriction, and nothing in it appears as a permission either — the list is the same list any framework would write.

**The one entry that is not what it seems.** $R_{\imath\jmath k l}R^{\imath\jmath k l}$ looks independent of the other two curvature squares, and in five or more dimensions it is. In four it is not, and the reason is the next section.

## The Identity That Trims the List

Decompose the curvature into the part with no trace and the parts with trace:

$$
R_{\imath\jmath k l}=C_{\imath\jmath k l}+\tfrac12\left(g_{\imath k}R_{\jmath l}-g_{\imath l}R_{\jmath k}-g_{\jmath k}R_{\imath l}+g_{\jmath l}R_{\imath k}\right)-\tfrac{R}{6}\left(g_{\imath k}g_{\jmath l}-g_{\imath l}g_{\jmath k}\right),
$$

with $C$ the trace-free part. Squaring gives the algebraic identity

$$
C^{2}=R_{\imath\jmath k l}R^{\imath\jmath k l}-2R_{\imath\jmath}R^{\imath\jmath}+\tfrac{1}{3}R^{2},
$$

and hence the Gauss–Bonnet combination

$$
\mathrm{GB}=R_{\imath\jmath k l}R^{\imath\jmath k l}-4R_{\imath\jmath}R^{\imath\jmath}+R^{2}=C^{2}-2R_{\imath\jmath}R^{\imath\jmath}+\tfrac{2}{3}R^{2}.
$$

**Both identities were verified exactly, not to a tolerance.** The metric chosen is the one family that carries all four invariants at once, Schwarzschild–de Sitter,

$$
ds^{2}=-f\,dt^{2}+\frac{dr^{2}}{f}+r^{2}d\theta^{2}+r^{2}\sin^{2}\theta\,d\phi^{2},\qquad f=1-\frac{2M}{r}+\frac{r^{2}}{L^{2}},
$$

and the computation was done symbolically in $M$, $L$, $r$ and $\theta$, so the result holds for every value of the parameters and not at a point. The four invariants come out in closed form:

$$
R^{2}=\frac{144}{L^{4}},\qquad R_{\imath\jmath}R^{\imath\jmath}=\frac{36}{L^{4}},\qquad R_{\imath\jmath k l}R^{\imath\jmath k l}=\frac{48M^{2}}{r^{6}}+\frac{24}{L^{4}},\qquad C^{2}=\frac{48M^{2}}{r^{6}},
$$

and substituting them makes both identities vanish identically: the first because $\frac{48M^{2}}{r^{6}}+\frac{24}{L^{4}}-\frac{72}{L^{4}}+\frac{48}{L^{4}}=\frac{48M^{2}}{r^{6}}$, the second because $-\frac{144}{L^{4}}+\frac{144}{L^{4}}=0$.

**The two limiting cases are the two checks that were made before this one, and they are weaker.** With $M\to0$ the metric is de Sitter space, $C^{2}=0$ and the trace-free part vanishes because de Sitter is conformally flat; with $L\to\infty$ it is Schwarzschild, $R=0$ and $R_{\imath\jmath}R^{\imath\jmath}=0$, and the whole of the Gauss–Bonnet density is the trace-free square $48M^{2}/r^{6}$. A check in either limit tests one identity against one vanishing invariant; the Schwarzschild–de Sitter computation tests both against four non-vanishing ones at once.

**What that trims.** The Gauss–Bonnet density is a total derivative in four dimensions — the Gauss–Bonnet theorem, quoted, not re-derived here — so of the three curvature squares only two combinations carry dynamics. The four-derivative gravitational menu is therefore

$$
\{R^{2},\;R_{\imath\jmath}R^{\imath\jmath}\},
$$

with $R_{\imath\jmath k l}R^{\imath\jmath k l}$ fixed by the total derivative and the Euler density. In five dimensions the count changes and the third entry returns; in four, two is the number.

**Why the trim matters for the corpus.** A framework that can write two curvature squares and one topological density has written the whole four-derivative gravitational sector, with no gap. The gap is in the coefficients, and the coefficients are the next section.

## Why the Algebra Is Not Asked to Count

The action article states the point and this one repeats it because the list above invites the opposite reading.

**Derivative order is not an algebraic property.** No algebra counts derivatives: not the gauge group, not the Clifford algebra, not the tangent space. The order of a field equation is fixed by power counting, by the demand that the equation be second order, and by experiment. So the biquaternions are not being asked to do what groups cannot do, and the fact that they count nothing is a property of the method.

**What they are asked to do, they can.** Every entry in the table is a product of frame bilinears and curvature two-forms, and the corpus writes both. The scalar kinetic term is the scalar sector's second-order variation; the gauge kinetic term is the field strength's square; the fermion kinetic term is the Dirac sector's own functional; the curvature squares are two curvatures multiplied, which the algebra's product does without comment. The one entry that needed work was $R$, and the trace of the squared Dirac operator supplies it.

**So the correct reading of the table is not a list of what is missing.** It is a list of what has to be matched by coefficients once the framework's own action is written, and the coefficients are a measurement problem rather than an algebraic one.

## What the Coefficients Cost

Lovelock's theorem leaves two constants at second order and the two curvature squares at fourth order. Written out, the gravitational action of this framework is

$$
S=\int d^{4}x\sqrt{|\det G|}\left[\frac{1}{16\pi G}\left(R-2\Lambda\right)+\alpha R^{2}+\beta R_{\imath\jmath}R^{\imath\jmath}\right],
$$

with three numbers that the corpus does not fix: $\Lambda$, $\alpha$, $\beta$.

**One of them is calibrated.** The Newtonian limit fixes $16\pi G/c^{4}$ uniquely, and the article that does it records the coefficient as calibrated rather than chosen. That is the strongest kind of statement the corpus can make about a coupling, and it makes it exactly once.

**Two are not, and the corpus's position should be stated plainly.** $\Lambda$ is measured and enters as an additive number; $\alpha$ and $\beta$ are either zero by fiat or measured, and no observation in the corpus's own articles constrains them. A framework in that position is in general relativity's position, which is a respectable position and not a derivation.

**The consequence for the claim that the action is "Einstein's".** If $\alpha=\beta=0$ the action is the Hilbert one, and the corpus's choice is a choice. Nothing in the framework selects it. The honest ledger entry is: the corpus writes the Hilbert action and does not derive the vanishing of the curvature squares.

## Observability, and Why the Corpus Can Postpone It

The curvature squares are suppressed relative to $R$ by two powers of the ratio of the field's curvature scale to the scale at which the terms are generated, and the corpus has such a scale in $M_{C}$, the scale above which the cell labels are dropped.

**What that buys.** Any prediction that depends on $\alpha$ or $\beta$ is suppressed by $(E/M_{C})^{2}$ at energies $E$, so a corpus whose stated domain is below $M_{C}$ can set them to zero without contradicting itself, provided it says that setting them to zero is what it is doing. That is the difference between an approximation and a claim, and the articles that use the Hilbert action should be read as making the first.

**What it costs.** One observable is lost. A theory with curvature squares predicts a different gravitational-wave dispersion and a different scalar sector's conformal coupling; the corpus predicts neither, and it cannot be tested against the measurements that constrain them. That is a real cost and it is worth stating once rather than in every article.

## What Is Open

**Three items, and they are small ones.** First, the count above is for the field content the corpus has; adding a right-handed neutrino, an axion, or a second doublet lengthens the table, and the lengthening is mechanical. Second, the suppression argument needs the matching calculation that connects $\alpha$ and $\beta$ at $M_{C}$ to their low-energy values, and the corpus has no matching. Third, the cosmological constant's value is measured and unexplained, which is the same position every framework occupies.

**One item that is not small.** The frame-letter form of $R^{2}$ and $R_{\imath\jmath}R^{\imath\jmath}$ has the same defect as the frame-letter form of $R$: the two-derivative term's variation is owed, and the four-derivative terms' variations are owed twice over, because each curvature already carries two derivatives of the frame. If the exact functional is out of reach, the curvature squares are further out.

## Summary

The frame is dimensionless, so the operator menu at dimension four is finite and enumerable: thirteen entries for the corpus's field content, from the cosmological constant to the three curvature squares.

The three curvature squares are not independent in four dimensions. The decomposition of the curvature into trace-free and trace parts gives $C^{2}=R_{\imath\jmath k l}R^{\imath\jmath k l}-2R_{\imath\jmath}R^{\imath\jmath}+\tfrac13R^{2}$ and $\mathrm{GB}=C^{2}-2R_{\imath\jmath}R^{\imath\jmath}+\tfrac23R^{2}$, both verified exactly on Schwarzschild–de Sitter, where the four invariants are $R^{2}=144/L^{4}$, $R_{\imath\jmath}R^{\imath\jmath}=36/L^{4}$, $R_{\imath\jmath k l}R^{\imath\jmath k l}=48M^{2}/r^{6}+24/L^{4}$ and $C^{2}=48M^{2}/r^{6}$, so that both identities cancel term by term. Since the Gauss–Bonnet density is a total derivative in four dimensions, two combinations carry dynamics and the four-derivative gravitational menu is $\{R^{2},R_{\imath\jmath}R^{\imath\jmath}\}$.

Nothing in the menu is unwritable in the algebra's operations, and nothing in the algebra selects it. That is the correct reading: the algebra is not asked to count derivatives, because no algebra is, and the list it must write is finite. What the list costs is three coefficients — $\Lambda$, $\alpha$, $\beta$ — of which the corpus calibrates none and constrains one through the Newtonian limit.

## Further Reading

- [The Exact Gravitational Action](the-exact-gravitational-action-the-functional-the-boundary-term-and-the-variation.html), for Lovelock's theorem, the argument that no algebra counts derivatives, and the ledger of which sectors have an action.
- [The Variation in Frame Letters](the-variation-in-frame-letters.html), for why the frame variation of $R^{2}$ is further out of reach than the frame variation of $R$.
- [The Lagrangian and Linearised Gravity](the-lagrangian-and-linearised-gravity.html), for the quadratic action, its surface term, and the coefficient $16\pi G/c^{4}$ calibrated by the Newtonian limit.
- [The Scalar Sector on a Frame](the-scalar-sector-on-a-frame.html), for the conformal coupling $\xi R\phi^{\dagger}\phi$ and the frame in which $\rho$ and $p$ are read.
- [The Sector Hub](the-sector-hub-what-the-lagrangian-family-reaches-in-each-sector.html), for the matter sector's entries in the same table.
