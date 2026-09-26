
# __List of Non-Examples in Analysis__

## Introduction

This article lists the non-examples of analysis that the corpus records: the objects that are defined by the same words as a standard positive object and fail one of its properties. Each row names the non-example, records the positive object it fails to be and the failure itself, and points to the article that introduces the non-example. Every row points to an article; this article introduces nothing and proves nothing. The non-examples are grouped by the layer that introduces them: the five standard counterexamples of the real line and its measure theory, the further non-examples of measure and integration, the non-examples of the convergence of functions, the non-examples of differentiation and analyticity, and the non-examples of series and integrals. The positive object that each non-example fails to be is named beside it, so that the reader sees the example and the non-example side by side.

## The Standard Counterexamples

| Non-example | The positive object it fails to be, and the failure | Introduced in |
|---|---|---|
| the continuous nowhere differentiable function | a differentiable function: the function is continuous everywhere and has no derivative at any point. The corpus records the existence of such functions by the Baire category theorem, in the meagre-set argument, rather than by the classical Weierstrass series, which is not introduced in Parts I to III | *Metric, Uniform and Complete Spaces* |
| the path of Brownian motion | a differentiable function: the path is almost surely continuous and almost surely nowhere differentiable, with infinite variation | *Brownian Motion and Stochastic Calculus* |
| Volterra's function | a function whose derivative is Riemann integrable: it is differentiable, its derivative is bounded, and the derivative is not Riemann integrable, being discontinuous on a fat Cantor set of positive measure, so the fundamental theorem of calculus fails without the continuity of the derivative | *Measure Theory and Integration* |
| the Dirichlet function $\mathbf 1_{\mathbb Q}$ | a Riemann integrable function: it is bounded and Lebesgue integrable with integral $0$, the rationals being null, and it is not Riemann integrable, being discontinuous everywhere | *Real Integration*; *Measure Theory and Integration* |
| a non-measurable set, the Vitali set | a Lebesgue measurable set: it has no length consistent with translation invariance and countable additivity, so it lies outside the Lebesgue $\sigma$-algebra | *Measure Theory and Integration* |
| the smooth function $\exp(-1/x^2)$ extended by $0$ at the origin | an analytic function: all its derivatives at $0$ vanish, so its Taylor series is the zero series, while the function is positive away from $0$ | *Real Analysis* |

## Non-Examples of Measure and Integration

| Non-example | The positive object it fails to be, and the failure | Introduced in |
|---|---|---|
| the Cantor function | an absolutely continuous function: it is continuous, nondecreasing and constant on each complement of the Cantor set, with derivative $0$ almost everywhere, yet it rises from $0$ to $1$ | *Measure Theory and Integration*; *Measure-Theoretic Probability* |
| the Cantor distribution | an absolutely continuous law: it is singular continuous, with no density, and its distribution function is the Cantor function | *Measure-Theoretic Probability* |
| the indicator of a fat Cantor set | a Riemann integrable function: it is Lebesgue integrable and discontinuous on a set of positive measure | *Real Integration* |
| the counting measure on an uncountable set | a $\sigma$-finite measure: it is a measure, and no countable cover by finite-measure sets exists | *Measure Theory and Integration* |
| a finitely additive set function | a measure: it is additive over finite unions and not countably additive | *Measure Theory and Integration* |
| an outer measure on the whole power set | a measure: it is monotone and countably subadditive and additive only on the Carathéodory-measurable sets | *Measure Theory and Integration* |
| the set of rationals in $[0,1]$ | a set of positive measure: it is countable, hence null, and dense; a null set can be dense | *Measure Theory and Integration* |

## Non-Examples of Convergence

| Non-example | The positive object it fails to be, and the failure | Introduced in |
|---|---|---|
| $f_n = n\mathbf 1_{(0,1/n)}$ | an $L^1$-convergent sequence: it converges to $0$ almost everywhere and in measure, while $\int f_n = 1$ throughout | *Modes of Convergence* |
| the sliding dyadic intervals on $[0,1]$ | an almost-everywhere convergent sequence: it converges to $0$ in measure and in every $L^p$, and at no point of $[0,1)$ | *Modes of Convergence* |
| $f_n = x^n$ on $[0,1)$ | a uniformly convergent sequence: it converges locally uniformly and not uniformly, the rate depending on the point | *Modes of Convergence* |
| the unit vectors $e_n$ of $\ell^2$ | a norm-convergent sequence: it converges weakly to $0$ and stays at norm $1$ | *Modes of Convergence* |
| a bounded pointwise convergent sequence of Riemann integrable functions with a non-integrable limit | a sequence for which limit and Riemann integral interchange: the interchange fails without uniform convergence | *Real Integration* |
| a pointwise convergent sequence of continuous functions with a discontinuous limit | a uniformly convergent sequence: pointwise convergence does not preserve continuity, uniform convergence does | *Modes of Convergence* |

## Non-Examples of Differentiation and Analyticity

| Non-example | The positive object it fails to be, and the failure | Introduced in |
|---|---|---|
| a differentiable function with a discontinuous derivative | a $C^1$ function: differentiability does not imply the continuity of the derivative | *Differential Calculus on Normed Spaces* |
| the function $\lvert x\rvert$ | a differentiable function at $0$: continuous everywhere and not differentiable at one point | *Real Analysis* |
| a continuous function with a divergent Fourier series | a function whose Fourier series converges: continuity does not force pointwise convergence of the series | *Real Harmonic Analysis* |
| a real-analytic function at its radius of convergence | an entire function: the radius of convergence is finite, so the power-series representation, and with it the region of analyticity, is confined to the disc | *Analytic Functions and Power Series* |
| the gamma function $\Gamma$ | a function with zeros: it has no zeros, only the poles at $0, -1, -2, \dots$, since $1/\Gamma$ is entire | *Complex Special Functions* |
| a domain of holomorphy | a domain extended across its boundary: it is maximal, there is a holomorphic function on it that does not extend past the boundary, and the plurisubharmonic exhaustion measures that failure | *Several Complex Variables* |

## Non-Examples of Series and Integrals

| Non-example | The positive object it fails to be, and the failure | Introduced in |
|---|---|---|
| the harmonic series $\sum 1/n$ | a convergent series: its terms tend to $0$ and its partial sums diverge | *Real Analysis* |
| the alternating harmonic series | an absolutely convergent series: it converges conditionally, and the Archimedean rearrangement paradoxes apply to it | *Analytic Functions and Power Series* |
| the integral of $x \mapsto 1/x$ over $[1,\infty)$ | a convergent improper integral: the $p$-integral converges exactly for $p > 1$, so this one diverges | *Real Integration* |
| the integral of $x \mapsto \sin x/x$ over $(0,\infty)$ | an absolutely convergent integral: it converges conditionally and not absolutely | *Real Integration* |
| a Dirichlet series at its abscissa of convergence | a series continued holomorphically past the abscissa: by Landau's theorem a series with nonnegative coefficients has a singularity at its abscissa and no continuation across it | *Zeta Functions* |
| an infinite sum differentiated term by term without uniform convergence | a differentiable sum with the termwise derivative: the interchange fails without the uniform convergence of the derivatives | *Modes of Convergence* |

## Summary

This list gathers the non-examples of analysis that the corpus records: the continuous nowhere differentiable function, the path of Brownian motion, Volterra's function, the Dirichlet function, a non-measurable set and the smooth function that is not analytic among the standard counterexamples; the Cantor function and the singular Cantor law, the fat Cantor set indicator and the non-$\sigma$-finite counting measure among those of measure theory; the sequences that separate the modes of convergence; the differentiable and continuous functions that fail to be smooth or to have convergent Fourier series; and the series and integrals that fail to converge absolutely or at all. Each row names the positive object the non-example fails to be, so that the failure is the content of the row.

## Summary of Notation

The non-examples are named rather than denoted; the symbols in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $\mathbf 1_{\mathbb Q}$, $\mathbf 1_A$ | the indicator of the rationals, of a set $A$ |
| $\exp(-1/x^2)$ | the smooth non-analytic function |
| $V$ | the Vitali non-measurable set |
| $\ell^2$, $e_n$ | the sequence space and its unit vectors |
| $L^p$, a.e. | the Lebesgue space and the almost-everywhere mode |

## Further Reading

- Bernard R. Gelbaum and John M. H. Olmsted, *Counterexamples in Analysis* (Holden-Day, 1964; reprinted Dover, 2003), for the standard catalogue of the counterexamples of analysis.
- John C. Oxtoby, *Measure and Category* (Springer, 2nd ed. 1980), for the duality between the meagre and the null sets and the constructions behind the standard non-examples.
- Walter Rudin, *Real and Complex Analysis*, 3rd ed. (McGraw-Hill, 1987), for the Dirichlet function, the Cantor function and the failure of the fundamental theorem of calculus.
