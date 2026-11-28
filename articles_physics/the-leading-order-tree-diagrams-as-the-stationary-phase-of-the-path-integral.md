# __The Leading Order: Tree Diagrams as the Stationary Phase of the Path Integral__

## Introduction

**The claim.** The diagram series has a leading term, and the leading term is the field equation. Evaluating the path integral by stationary phase gives $\delta S=0$ at leading order; the Gaussian about the stationary point gives the determinant; and the expansion about that point reproduces the tree diagrams order by order in the coupling. The tree diagrams are the perturbative solution of the classical equation, and each loop is one power of the action quantum on top of it. The two routes — solve the equation, or draw the diagrams — are one computation organised two ways.

**Why the identification is not decorative.** It tells a reader where to put a computation that solves an equation and where a computation that draws a diagram. A tree amplitude can be checked against a solution of the field equation, which is a different calculation with different error modes. And it tells a reader what the loop expansion is: the semiclassical expansion of one integral, not a second perturbation theory.

**The strongest objection.** *Tree diagrams and the classical solution are different objects, because the classical solution is not a diagram.* The objection is right at finite coupling and wrong order by order. The classical solution is a series in the coupling; its $n$-th term is the sum of the tree diagrams with $n$ vertices; the two are equal term by term. What is not equal is the sum, because the sum need not converge. The article states the identification order by order and states the gap.

**Position.** After [stage $4$](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html) in the section [The Lagrangian Method](the-lagrangian-method-from-the-truncated-action-to-the-feynman-diagram.html), and the article that ties the section back to the variation that produces the field equation.

## The Stationary Phase

**The path integral is an oscillating integral with a large parameter, so its leading behaviour is its saddle.** With the corpus's weight,

$$
Z[J]=\int\mathcal D\phi\;\exp\Bigl(\frac{2\pi i}{h}S[\phi]+\frac{2\pi i}{h}\int J\phi\Bigr)
=\int\mathcal D\phi\;\exp\Bigl(\frac{2\pi i}{h}\bigl(S[\phi]+\!\int J\phi\bigr)\Bigr),
$$

the stationary points solve

$$
\frac{\delta S}{\delta\phi}+J=0 ,
$$

which is the Euler–Lagrange equation with the source. At $J=0$ the condition is $\delta S=0$, the classical equation of the corpus's [Klein–Gordon derivation](the-lagrangian-and-the-klein-gordon-equation.html).

**The next order is the Gaussian about the saddle, and the next is the determinant of its second variation.** Writing $\phi=\phi_{\mathrm c}+\eta$ and expanding,

$$
S[\phi]=S[\phi_{\mathrm c}]+\tfrac12\bigl\langle\eta,\,S^{(2)}[\phi_{\mathrm c}]\,\eta\bigr\rangle+O(\eta^{3}),
$$

so the leading term is the classical action and the first correction is the determinant of $S^{(2)}$. That determinant is [stage $2$'s leftover](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html), and it is the one-loop term.

**The expansion parameter is $\frac{h}{2\pi}$, and this is where a factor is easily lost.** The corpus's exponent is $\frac{2\pi}{h}S$, so a term of order $\bigl(\frac{h}{2\pi}\bigr)^{L}$ carries $L$ closed loops. Writing the parameter as $h$ alone is right up to the $2\pi$ and wrong by it in a comparison of numerical coefficients; the article therefore counts in $\frac{h}{2\pi}$ and calls it the action quantum.

## The Tree Series and the Classical Solution

**Expand the classical field in the coupling and the equation solves itself order by order.** With $S=S_{2}+gS_{\mathrm{int}}$ and $\phi_{\mathrm c}=\phi_{0}+g\phi_{1}+g^{2}\phi_{2}+\cdots$,

$$
S^{(2)}\phi_{1}=-S_{\mathrm{int}}^{(1)}[\phi_{0}],\qquad
S^{(2)}\phi_{2}=-S_{\mathrm{int}}^{(2)}[\phi_{0},\phi_{1}],\qquad\dots
$$

**Each equation is the free operator acting on the next term, with a source built from the previous terms.** That sentence is the whole correspondence: the free operator's inverse is the propagator, and the source built from previous terms is a vertex with earlier fields on its legs. So $\phi_{1}=\Delta\ast(\text{one vertex with }\phi_{0}\text{'s})$, and the tree diagram at order $g$ is $\phi_{1}$ amputated.

**The running example makes the correspondence one line.** For the quartic, the first-order equation is

$$
\bigl(\Box_{\Phi}-4\pi^{2}\nu_{m}^{2}\bigr)\Xi_{1}=\varpi_{\mathrm{cpl}}\,N_{0}\,\Xi_{0},
$$

so $\Xi_{1}$ is the propagator applied to the source $\varpi_{\mathrm{cpl}}N_{0}\Xi_{0}$. Amputating the external leg and putting it on the shell returns the tree vertex of [stage $3$](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html), and nothing else. The equation's solution *is* the tree diagram, written in position space.

**The correspondence was checked on a model where both sides are computable to machine precision.** In the zero-dimensional truncation of the same structure, with $m^{2}x+\lambda x^{3}=J$ as the classical equation and $x=J/m^{2}-\lambda(J/m^{2})^{3}/m^{2}-\cdots$ as the tree series, take $m=1$, $\lambda=1$, $J=0.225$. The classical root is $x_{\mathrm c}=0.21505$, and iterating $x\mapsto\bigl(J-\lambda x^{3}\bigr)/m^{2}$ gave errors $9.95\times10^{-3}$, $1.45\times10^{-3}$, $1.99\times10^{-4}$, $2.77\times10^{-5}$, $3.84\times10^{-6}$, $5.32\times10^{-7}$ at orders zero to five. The ratio of successive errors settled at $0.1387$, which is $\lambda\cdot3x_{\mathrm c}^{2}/m^{2}=0.1387$ to four figures: each iteration multiplies the error by the derivative of the classical map at its fixed point, and the tree series is the classical solution's Taylor series.

## The Loops Are the Powers of the Action Quantum

**One closed loop is one order in $\frac{h}{2\pi}$, and the determinant is the first such term.** The loop count is the graph's cycle rank,

$$
L=I-V+1 ,
$$

and the semiclassical expansion's $L$-th term is the $L$-th power of the action quantum. The tree diagrams are order zero; the determinant is order one; each additional closed line is one more.

| order in $\frac{h}{2\pi}$ | the object | what it is |
|---|---|---|
| $0$ | the tree diagrams | the perturbative classical solution |
| $1$ | the determinant of $S^{(2)}$ | the one-loop effective action, $\frac12\mathrm{Tr}\log S^{(2)}$ |
| $L$ | the $L$-loop diagrams | the $L$-th semiclassical correction |

**The two expansions are different groupings of one series, and the difference was checked numerically.** In a zero-dimensional model with $S=\tfrac12m^{2}x^{2}+\lambda x^{4}-Jx$ and $m=1$, $\lambda=0.5$, $J=0.05$, the expectation $\langle x\rangle$ was computed by quadrature at four values of the action quantum, and the deviation from the classical value $x_{\mathrm c}=0.049754$ was $-4.56\times10^{-3}$, $-2.54\times10^{-3}$, $-1.35\times10^{-3}$, $-6.99\times10^{-4}$ at $\frac{h}{2\pi}=0.02,0.01,0.005,0.0025$. Successive deviations have ratio $0.557$, $0.532$, $0.517$: the deviation halves when the parameter halves, so it is linear in the parameter — one power, one loop. The ratio of the deviation to the parameter drifted from $-0.228$ to $-0.280$ over the four values, converging on the analytic first-order coefficient $-\tfrac12 S'''/S''^{2}=-0.290$; that drift is the $O\bigl((h/2\pi)^{2}\bigr)$ contamination and the reason four values are quoted rather than one.

**The equivalence is precise and it is bounded.** The two expansions are the same diagrams, grouped by loop number instead of by coupling power. Truncating at fixed loop order is not the same as truncating at fixed coupling order: a fixed-order truncation contains finitely many loops, and a fixed-loop truncation contains infinitely many orders. A reader who treats the two truncations as interchangeable will compare two different approximations and call the difference a discrepancy.

## The Two Routes Are One

**Stated as a table, the identification is exact line by line.**

| the equation route | the diagram route |
|---|---|
| $\delta S=0$ | the stationary point, order $\bigl(\frac{h}{2\pi}\bigr)^{0}$ |
| $\phi_{\mathrm c}=\phi_{0}+g\phi_{1}+\cdots$ | the tree diagrams at $O(g^{n})$ |
| $S^{(2)}$ inverted once | the propagator, one line |
| the source built from earlier terms | the vertex, one point |
| the determinant of $S^{(2)}$ | the one-loop diagrams |
| the second variation about the one-loop field | the two-loop diagrams |

**The classical route is the tree projection of the quantum one, and the quantum route is the classical one with its own corrections.** A reader who computes a tree amplitude by solving the equation and a reader who computes it by drawing one vertex are doing the same multiplication, and the corpus states both so that either can check the other.

**What the identification does not say.** It does not say that the classical solution equals the sum of the trees. The sum of the trees is a series in the coupling and the series need not converge; where it converges the two agree, and where it does not the classical solution exists and the series does not describe it. It does not say that the loops are small: each loop is one power of $\frac{h}{2\pi}$ and the coefficient may be large. And it does not say that the classical solution exists globally: a nonlinear equation can have solutions that no perturbative series reaches, and those are the non-perturbative objects [the last article](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) lists.

**The claim is therefore one-directional and order by order.** Every tree diagram is a term in the classical solution's expansion, and every term of that expansion is a tree diagram. That is enough to identify the two computations, and it is all that is claimed.

## Summary

**The leading term of the diagram series is the stationary phase of the path integral.** $\delta S=0$ gives the Euler–Lagrange equation; the Gaussian about the saddle gives the determinant; and the expansion about the saddle reproduces the tree diagrams order by order in the coupling. The tree diagrams are the perturbative classical solution, and each closed loop is one power of $\frac{h}{2\pi}$.

**The identification was checked on a model where both sides are exact.** The tree series matched the Newton solution with errors falling by $0.1387$ per order, and the deviation of the expectation from the classical value halved when the action quantum halved, as one power of it does.

**The equivalence of the coupling and loop expansions is a regrouping of the same diagrams and nothing more.** Truncating at fixed loop order is not truncating at fixed coupling order, and the identification of trees with the classical solution holds order by order and not as a statement about sums or convergence.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\phi_{\mathrm c}$, $\phi_{n}$ | the classical field and its $n$-th term in the coupling |
| $S^{(2)}$ | the second variation, the quadratic operator of the fluctuation |
| $L=I-V+1$ | the loop number of a connected graph |
| $\frac{h}{2\pi}$ | the expansion parameter of the stationary-phase expansion |
| $\eta$ | the fluctuation about the stationary point |

## Further Reading

- [The Lagrangian and the Klein–Gordon Equation](the-lagrangian-and-the-klein-gordon-equation.html), the variation that stationary phase returns, worked on the scalar.
- [The Feynman Rules and the Diagram Expansion: Propagators, Vertices, Loops and Symmetry Factors](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html), the diagrams whose trees this article identifies with the solution.
- [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), the one-loop term as a determinant.
- [The Limits of the Expansion: Gauge Fixing, Asymptotic Series and Strong Coupling](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html), the objects no finite order reaches.
- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), the classical route in the corpus's own fluid form.
