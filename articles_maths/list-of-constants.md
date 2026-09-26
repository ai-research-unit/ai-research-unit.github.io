
# __List of Constants__

## Introduction

This article lists the mathematical constants the corpus names and computes. A constant is a definite real or complex number that recurs across the corpus and carries a proved arithmetic property, and a row below names one, records its definition and the arithmetic fact proved for it — rationality, irrationality, transcendence, or non-computability — and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The constants are grouped by the layer that introduces them: the elementary constants of the real line and the special functions, the constants of analysis and number theory, and the constants of dynamics and information. The rows that record what is not proved — $\gamma$, the Catalan constant and the Feigenbaum constants, for which no irrationality is known — and the rows that record a constant which is irrational and not transcendental stand beside the proved ones as non-examples, so that the article records examples and non-examples side by side.

## The Elementary Constants

| Object | Its definition, and the arithmetic fact proved for it | Introduced in |
|---|---|---|
| $\sqrt2$ | the positive root of $x^2 = 2$; irrational, by the classical parity argument | *The Rational Numbers* |
| the golden ratio $\varphi = (1+\sqrt5)/2$ | the positive root of $x^2 = x+1$; irrational, and the worst approximable irrational, with continued fraction $[1;1,1,\dots]$ | *Diophantine Approximation and Continued Fractions* |
| $e = \exp(1)$ | the sum $\sum_{n\geq0} 1/n!$; transcendental over $\mathbb Q$, by Hermite's theorem | *Real Special Functions*; *Fields*; *Field Extensions* |
| $\pi$ | twice the smallest positive zero of $\cos$; transcendental over $\mathbb Q$, by Lindemann's theorem, hence so is $\sqrt\pi$ | *Real Special Functions*; *Fields*; *Field Extensions* |
| $\log 2$ | the logarithm of $2$, the normalising constant of the Gauss measure $d\mu = dx/((1+x)\log2)$ and the entropy of the doubling map | *Diophantine Approximation and Continued Fractions*; *Ergodic Theory* |
| the Liouville number $\sum_{k\geq1}10^{-k!}$ | an explicit real number; transcendental, because its rational truncations beat every polynomial approximation bound | *Diophantine Approximation and Continued Fractions* |

## The Constants of Analysis and Number Theory

| Object | Its definition, and the arithmetic fact proved for it | Introduced in |
|---|---|---|
| $\gamma$, Euler's constant | the limit $\lim_{n\to\infty}(\sum_{k\leq n}1/k - \log n)$; the corpus proves no irrationality and no transcendence, and it is the constant of the Weierstrass product $1/\Gamma(z) = ze^{\gamma z}\prod(1+z/n)e^{-z/n}$ | *Zeta Functions*; *Complex Special Functions* |
| $\zeta(2) = \pi^2/6$ | the value of the zeta function at $2$; a rational multiple of $\pi^2$, hence irrational and transcendental | *Zeta Functions* |
| $\zeta(3)$ | the value of the zeta function at $3$; irrational, by Apéry's theorem, with no rational multiple of a power of $\pi$ known | *Zeta Functions* |
| $\zeta(4) = \pi^4/90$ and $\zeta(6) = \pi^6/945$ | the even zeta values; rational multiples of powers of $\pi$, hence transcendental, in contrast to the odd ones | *Zeta Functions* |
| the de Bruijn–Newman constant $\Lambda$ | the threshold of the family $H_\lambda$ at which the zeros of the zeta function become real; de Bruijn proved $\Lambda \leq \tfrac12$, Rodgers and Tao proved $\Lambda \geq 0$, and the Riemann hypothesis is the statement $\Lambda \leq 0$, so the hypothesis is $\Lambda = 0$ | *The Riemann Hypothesis* |
| the Catalan constant $G = \beta(2)$ | the value $\sum_{n\geq0}(-1)^n(2n+1)^{-2}$ of the Dirichlet beta function at $2$; a period, and no irrationality is proved in the corpus | *Zeta Functions* |
| $K_0$, Khinchin's constant | the almost-sure geometric mean of the partial quotients, $2.6854520010\dots$; defined by the ergodic theorem for the Gauss map, with no arithmetic proved | *Diophantine Approximation and Continued Fractions* |
| $M$, the Mertens constant | the constant in the estimate of the sum of the reciprocals of the primes; defined, with no arithmetic proved | *Analytic Number Theory* |
| the Lagrange constant of an irrational $\alpha$, $\liminf_q q\lVert q\alpha\rVert$ | the measure of how badly $\alpha$ is approximable; its largest value $1/\sqrt5$ is attained by the golden ratio, by Hurwitz's theorem | *Diophantine Approximation and Continued Fractions* |
| the Grothendieck constant $K_G$ | the universal constant of Grothendieck's inequality, with $1 < K_G < 2$, comparing the projective and the injective tensor norm; its exact value is not determined by the corpus | *Topological Tensor Products* |

## The Constants of Dynamics and Information

| Object | Its definition, and the arithmetic fact proved for it | Introduced in |
|---|---|---|
| the Feigenbaum constant $\delta = 4.669201609\dots$ | the limit of the ratios of successive period-doubling parameter intervals of a unimodal family; computed, and no irrationality or transcendence is proved | *Bifurcation Theory* |
| the Feigenbaum scaling factor $\alpha = -2.502907875\dots$ | the scaling factor of the renormalisation fixed point of the doubling operator; computed, with no arithmetic proved | *Bifurcation Theory* |
| the Lévy constant $\pi^2/(12\log2) = 3.2758229187\dots$ | the almost-sure exponential growth rate of the continued-fraction denominators; it is half the entropy of the Gauss map | *Dynamics and Number Theory* |
| the entropy $h(T) = \pi^2/(6\log2) = 2.373138\dots$ of the Gauss map | the Kolmogorov–Sinai entropy of the continued-fraction map, twice the Lévy constant | *Dynamics and Number Theory* |
| the Gauss–Kuzmin–Wirsing constant $\lambda_2 = -0.303663\dots$ | the second eigenvalue of the Gauss–Kuzmin–Wirsing operator, the rate of the exponential error in the Gauss–Kuzmin theorem; no arithmetic is proved | *Dynamics and Number Theory* |
| Chaitin's $\Omega$ | the halting probability $\sum_{U(p)\downarrow}2^{-\lvert p\rvert}$ of a universal machine; not computable, and its binary expansion is algorithmically random, so it is not an algebraic number that a machine can decide | *Computability Theory*; *Algorithmic Randomness and Chaitin's $\Omega$* (planned) |

## Irrational and Not Transcendental

| Object | The property it records | Introduced in |
|---|---|---|
| $\sqrt2$ | is irrational and not transcendental: it is algebraic of degree $2$ | *The Rational Numbers*; *Field Extensions* |
| the golden ratio $\varphi$ | is a quadratic irrational, hence algebraic, and is the extremal case of Hurwitz's theorem | *Diophantine Approximation and Continued Fractions* |
| $\zeta(3)$ | is irrational and not known to be transcendental; it is not a rational multiple of a power of $\pi$ as far as is known | *Zeta Functions* |
| $\gamma$ | is expected to be transcendental and is not even known to be irrational | *Zeta Functions* |
| the computable reals | are dense in $\mathbb R$ but have measure zero; a constant with no arithmetic proof is still a definite real number | *Computability Theory* |

## Summary

This list gathers the constants of the corpus: the elementary constants $\sqrt2$, $\varphi$, $e$, $\pi$ and $\log2$ with the Liouville number; the constants of analysis and number theory, $\gamma$, the zeta values $\zeta(2)$, $\zeta(3)$, $\zeta(4)$ and $\zeta(6)$, the de Bruijn–Newman constant $\Lambda$, the Catalan, Khinchin, Mertens, Lagrange and Grothendieck constants; and the constants of dynamics and information, the Feigenbaum constants, the Lévy constant, the entropy of the Gauss map, the Gauss–Kuzmin–Wirsing constant and Chaitin's $\Omega$. Each row records the definition and the arithmetic fact proved for the constant, and the closing table records which constants are irrational but not transcendental and which carry no arithmetic proof at all.

## Summary of Notation

The constants are named by their standard letters; the symbols in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $e$, $\pi$, $\gamma$, $\varphi$ | the base of the natural logarithm, the circle constant, Euler's constant, the golden ratio |
| $G$ | the Catalan constant |
| $K_0$, $M$ | Khinchin's constant, the Mertens constant |
| $\Lambda$ | the de Bruijn–Newman constant |
| $K_G$ | the Grothendieck constant |
| $L$, $h(T)$ | the Lévy constant and the entropy of the Gauss map |
| $\lambda_2$ | the Gauss–Kuzmin–Wirsing constant |
| $\delta$, $\alpha$ | the Feigenbaum constants |
| $\Omega$ | Chaitin's halting probability |
| $\zeta(s)$, $\beta(s)$ | the Riemann zeta and Dirichlet beta functions |

## Further Reading

- Steven R. Finch, *Mathematical Constants* (Cambridge University Press, 2003), for the catalogue of the classical constants with their numerical values and known arithmetic properties.
- Godfrey H. Hardy and Edward M. Wright, *An Introduction to the Theory of Numbers*, 6th ed. (Oxford University Press, 2008), for the irrationality and transcendence of $e$, $\pi$ and the quadratic irrationals.
- Cristian S. Calude, *Information and Randomness: An Algorithmic Perspective*, 2nd ed. (Springer, 2002), for Chaitin's $\Omega$ and the arithmetic of algorithmic randomness.
