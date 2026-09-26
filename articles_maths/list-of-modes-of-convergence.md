
# __List of Modes of Convergence__

## Introduction

This article lists the modes of convergence the corpus uses. A mode of convergence is a prescription of what it means for a sequence to approach a limit — at every point, uniformly, off a null set, in a mean, in duality — and a row below names one mode, records the setting in which it is defined and its relation of implication to the modes above and below it, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The modes are grouped by the layer that introduces them: convergence in a topological and a uniform space, the pointwise and uniform modes of function theory, the measure-theoretic modes of almost everywhere and in measure, convergence in the $L^p$ norms, and the weak and weak-$\ast$ modes of functional analysis. Beside them stand the non-examples that separate them — a pointwise convergence that is not uniform, an in-measure convergence with no pointwise limit, a weakly convergent sequence that does not converge in norm — recorded as rows whose property cells name the failure, so that the article records examples and non-examples side by side.

## Convergence in a Topological and a Uniform Space

| Object | The setting, and the property it has | Introduced in |
|---|---|---|
| convergence of a sequence | a topological space; every neighbourhood of the limit contains all but finitely many terms | *Modes of Convergence* |
| convergence of a net and of a filter | an arbitrary directed set, and a filter; the general form of the limit | *Modes of Convergence* |
| Cauchy sequence, Cauchy filter | a uniform space; the terms are eventually close to one another | *Modes of Convergence*; *Metric, Uniform and Complete Spaces* |
| completeness | a uniform space; every Cauchy sequence or filter converges | *Metric, Uniform and Complete Spaces* |
| convergence in a metric space | the metric; $d(x_n, x) \to 0$ | *Metric, Uniform and Complete Spaces* |
| uniform convergence in a uniform space | $f_n$ eventually within every entourage of $f$, uniformly in the point | *Metric, Uniform and Complete Spaces* |

## Pointwise and Uniform Convergence

| Object | Its definition, and its relation to the other modes | Introduced in |
|---|---|---|
| pointwise convergence | $f_n(x) \to f(x)$ for each $x$; the weakest of the function modes | *Modes of Convergence* |
| uniform convergence | $\sup_x \lVert f_n(x) - f(x)\rVert \to 0$; convergence in the supremum metric, hence implies pointwise | *Modes of Convergence* |
| locally uniform convergence, uniform on compacta | uniform on every compact subset; lies between uniform and pointwise, and neither implication reverses | *Modes of Convergence* |
| Dini's monotone convergence | a compact space and a monotone sequence of continuous functions with a continuous pointwise limit; the convergence is then uniform | *Modes of Convergence* |
| convergence in the space $B(X,Y)$ | the sup metric; complete when $Y$ is complete, and the home of uniform convergence | *Metric, Uniform and Complete Spaces* |

## Almost Everywhere and in Measure

| Object | Its definition, and its relation to the other modes | Introduced in |
|---|---|---|
| convergence almost everywhere | $f_n(x) \to f(x)$ outside a null set; a mode on the quotient by a.e. equality | *Modes of Convergence* |
| almost uniform convergence | uniform convergence off sets of arbitrarily small measure; implies both a.e. and in measure | *Modes of Convergence* |
| convergence in measure | $\mu(\{\lvert f_n - f\rvert > \epsilon\}) \to 0$ for every $\epsilon>0$ | *Modes of Convergence* |
| convergence in probability | convergence in measure on a probability space; the same condition under the probabilistic name | *Measure-Theoretic Probability* |
| Egorov's theorem | a finite measure space; a.e. convergence implies almost uniform convergence | *Modes of Convergence* |
| Riesz's theorem | in-measure convergence implies a.e. convergence along a subsequence | *Modes of Convergence* |

## Convergence in $L^p$

| Object | Its definition, and its relation to the other modes | Introduced in |
|---|---|---|
| convergence in $L^p$, $1 \leq p < \infty$ | $\lVert f_n - f\rVert_p \to 0$; implies convergence in measure, by Chebyshev | *Modes of Convergence*; *Measure Theory and Integration* |
| convergence in $L^\infty$ | essential supremum convergence; equivalent to uniform convergence off a null set | *Measure Theory and Integration* |
| uniform integrability | the condition that makes in-measure convergence into $L^1$ convergence | *Modes of Convergence* |
| the Vitali convergence theorem | a finite measure space and uniform integrability; in-measure convergence becomes $L^1$ convergence | *Modes of Convergence* |
| monotone, Fatou and dominated convergence | $L^1$ convergence from a.e. convergence, under monotonicity, nonnegativity or a dominating function | *Measure Theory and Integration* |
| inclusion of $L^q$ in $L^p$, $q \geq p$ | a finite measure space; then $L^q \subseteq L^p$ and $L^q$ convergence implies $L^p$ convergence | *Measure Theory and Integration* |

## Weak and Weak-$\ast$ Convergence

| Object | Its definition, and its relation to the other modes | Introduced in |
|---|---|---|
| weak convergence $x_n \rightharpoonup x$ | $\varphi(x_n) \to \varphi(x)$ for every bounded functional; implied by norm convergence | *Modes of Convergence*; *Banach and Hilbert Spaces* |
| weak-$\ast$ convergence $f_n \overset{\ast}{\rightharpoonup} f$ | pointwise convergence on the predual; on $X^\ast$ | *Modes of Convergence*; *Banach and Hilbert Spaces* |
| Banach–Alaoglu theorem | the weak-$\ast$ compactness of the unit ball of a dual space | *Banach and Hilbert Spaces* |
| weak lower semicontinuity of the norm | $\lVert x\rVert \leq \liminf \lVert x_n\rVert$ along a weakly convergent sequence | *Modes of Convergence* |
| weak convergence of measures | $\int f\,d\mu_n \to \int f\,d\mu$ for every bounded continuous $f$; the weak-$\ast$ convergence on $C_0(X)$ | *Modes of Convergence*; *Measure-Theoretic Probability* |
| convergence in distribution | weak convergence of laws on a metric space; also written $\mu_n \Rightarrow \mu$ | *Measure-Theoretic Probability* |
| vague convergence of measures | weak-$\ast$ convergence tested against $C_c(X)$ | *Measure Theory and Integration* |
| the portmanteau theorem | the equivalence of the definitions of weak convergence of measures | *Modes of Convergence*; *Measure-Theoretic Probability* |

## The Counterexamples That Separate the Modes

| Object | The implication it refutes | Introduced in |
|---|---|---|
| $f_n = x^n$ on $[0,1)$ | locally uniform convergence does not imply uniform convergence | *Modes of Convergence* |
| $f_n = \min(1, \lvert x\rvert/n)$ on $\mathbb R$ | locally uniform convergence does not imply uniform convergence | *Modes of Convergence* |
| the dyadic sliding intervals on $[0,1]$ | convergence in measure (and in every $L^p$, $p<\infty$) does not imply convergence at any point | *Modes of Convergence* |
| $f_n = n\mathbf 1_{(0,1/n)}$ | a.e. convergence does not imply convergence in $L^1$; in-measure convergence does not imply $L^1$ convergence | *Modes of Convergence* |
| $f_n = \mathbf 1_{[n,n+1]}$ | on an infinite measure space, a.e. convergence does not control the integrals | *Modes of Convergence* |
| $e_n$, the unit vectors of $\ell^2$ | weak convergence does not imply norm convergence in infinite dimensions | *Modes of Convergence* |
| a pointwise convergence without a continuous limit | pointwise convergence does not preserve continuity, while uniform convergence does | *Modes of Convergence* |
| a uniformly convergent sequence of Riemann integrable functions with bounded pointwise convergence and a limit that is not Riemann integrable | bounded pointwise convergence does not permit the interchange of limit and Riemann integral | *Real Integration* |

## Summary

This list gathers the modes of convergence of the corpus: convergence in a topological and a uniform space, pointwise, uniform and locally uniform convergence, convergence almost everywhere, almost uniformly, in measure and in probability, convergence in the $L^p$ norms with uniform integrability, and weak and weak-$\ast$ convergence together with the weak convergence of measures. The implication structure is that uniform convergence implies locally uniform, which implies pointwise; that a.e. convergence and convergence in measure are linked by Egorov and Riesz; that $L^p$ convergence implies convergence in measure but not a.e.; and that norm convergence implies weak, which implies weak-$\ast$ on a dual. The inseparable cases are recorded in the closing table.

## Summary of Notation

The objects are named rather than denoted; the symbols used in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $f_n \to f$ | pointwise convergence |
| $f_n \rightrightarrows f$ | uniform convergence |
| $f_n \to f$ a.e. | convergence almost everywhere |
| $f_n \xrightarrow{\mu} f$ | convergence in measure |
| $f_n \xrightarrow{L^p} f$ | convergence in the $L^p$ norm |
| $x_n \rightharpoonup x$, $f_n \overset{\ast}{\rightharpoonup} f$ | weak convergence, weak-$\ast$ convergence |
| $\mu_n \to \mu$ weakly, $\Rightarrow$ | weak convergence of measures, convergence in distribution |

## Further Reading

- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed. (Wiley, 1999), for the modes of convergence collected with their counterexamples and for the weak topologies.
- Halsey L. Royden and Patrick M. Fitzpatrick, *Real Analysis*, 4th ed. (Pearson, 2010), for the implications between the modes and the interchange theorems.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for weak and weak-$\ast$ convergence and the Banach–Alaoglu theorem.
