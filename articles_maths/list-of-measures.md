
# __List of Measures__

## Introduction

This article lists the measures the corpus constructs and uses. A measure is a countably additive function on a $\sigma$-algebra of sets, and a row below names one measure, records the family of sets it measures and the property that distinguishes it — invariance, dimension, finiteness, atomicity — and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The measures are grouped by the layer that introduces them: the abstract measures and their constructions, the measures of Euclidean space and of its subsets, the invariant measures on groups, and the measures that arise in potential theory, probability and spectral theory. The non-examples — the set that carries no measure, the outer measure that is not a measure, the finitely additive function that is not countably additive — are recorded beside the measures as rows whose property cell names the failure.

## Abstract Measures and Their Constructions

| Object | The sets it measures, and the property it has | Introduced in |
|---|---|---|
| a measure $\mu$ | the sets of a $\sigma$-algebra $\mathcal A$ on $X$; countably additive, $\mu(\emptyset) = 0$ | *Measure Theory and Integration* |
| a probability measure | every measurable set, with $\mu(X) = 1$ | *Measure Theory and Integration*; *Measure-Theoretic Probability* |
| a finite measure, a $\sigma$-finite measure | the measurable sets; $\mu(X) < \infty$, or $X$ a countable union of finite-measure sets | *Measure Theory and Integration* |
| a complete measure | the measurable sets and the subsets of null sets; every subset of a null set is measurable and null | *Measure Theory and Integration* |
| an outer measure $\mu^*$ | every subset of $X$; monotone and countably subadditive, but not additive in general | *Measure Theory and Integration* |
| a premeasure on an algebra | the sets of an algebra $\mathcal A_0$; extends to a measure on $\sigma(\mathcal A_0)$ by Carathéodory | *Measure Theory and Integration* |
| the counting measure | every subset of a discrete set $X$, by cardinality; its atoms are the singletons | *Measure Theory and Integration* |
| the Dirac measure $\delta_x$ | every measurable set, by $\delta_x(A) = 1$ if $x \in A$; the only atom is $\{x\}$ | *Measure Theory and Integration* |
| a sum $\mu + \nu$ and a normalisation $\mu/\mu(X)$ | the measurable sets; the normalisation is a probability measure | *Measure Theory and Integration* |
| an atom, and a diffuse measure | the measurable subsets of a set of positive measure; a diffuse measure has no atoms | *Measure Theory and Integration* |

## Measures on Euclidean Space

| Object | The sets it measures, and the property it has | Introduced in |
|---|---|---|
| Lebesgue measure $\lambda^n$ | the Borel and Lebesgue measurable sets of $\mathbb R^n$; translation-invariant, $\lambda^n([0,1]^n) = 1$ | *Measure Theory and Integration* |
| the product measure $\mu \otimes \nu$ | the sets of $\mathcal A \otimes \mathcal B$ on $X \times Y$; $(\mu \otimes \nu)(A \times B) = \mu(A)\nu(B)$ | *Measure Theory and Integration* |
| the Hausdorff measure $\mathcal H^s$ | every subset of a metric space, by covers of diameter at most $\delta$; it sees dimension | *Geometric Measure Theory* |
| Hausdorff dimension $\dim_{\mathcal H}$ | every bounded set; the exponent at which $\mathcal H^s$ jumps from $+\infty$ to $0$ | *Geometric Measure Theory*; *Fractal Geometry* |
| the Radon measure on a locally compact space | the Borel sets, finite on compact sets; produced by the Riesz representation theorem | *Locally Compact Groups and Haar Measure*; *Distributions and Fundamental Solutions* |

## Invariant Measures on Groups

| Object | The sets it measures, and the property it has | Introduced in |
|---|---|---|
| the Haar measure $\mu_L$ | the Borel sets of a locally compact group, finite on compacta; left-invariant, unique up to scale | *Locally Compact Groups and Haar Measure* |
| the right Haar measure $\mu_R$ | the Borel sets; $d\mu_R = \Delta^{-1}d\mu_L$ | *Locally Compact Groups and Haar Measure* |
| the modular function $\Delta$ | the group, measuring the failure of bi-invariance; a continuous homomorphism to $\mathbb R_{>0}$ | *Locally Compact Groups and Haar Measure* |
| a unimodular group | the Borel sets; abelian, compact, discrete, nilpotent and semisimple groups have a bi-invariant measure | *Locally Compact Groups and Haar Measure* |
| the normalised counting measure $\lvert G\rvert^{-1}\sum_g\delta_g$ | every subset of a finite group; a bi-invariant probability measure | *Measure Theory and Integration* |
| the additive Haar measure on $\mathbb Q_p$ | the balls $a + p^n\mathbb Z_p$, with $\mu(a+p^n\mathbb Z_p) = p^{-n}$ after $\mu(\mathbb Z_p) = 1$ | *p-adic Integration* |
| the multiplicative Haar measure $d^\times x$ | the Borel sets of $\mathbb Q_p^\times$; $\mu^\times(\mathbb Z_p^\times) = 1$ | *p-adic Integration* |
| a quasi-invariant measure on $G/H$ | the Borel sets of a homogeneous space, with Radon–Nikodym cocycle $\rho$ | *Locally Compact Groups and Haar Measure* |
| the Tamagawa measure | the adelic quotient, assembled as the product of the local Haar measures | *Adeles and Ideles*; *Adelic Analysis* |
| an invariant measure of a dynamical system | the measurable sets of the phase space; preserved by the transformation | *Ergodic Theory*; *Topological Dynamics* |

## Measures in Potential Theory, Probability and Spectral Theory

| Object | The sets it measures, and the property it has | Introduced in |
|---|---|---|
| the equilibrium measure | the compact subsets of $\mathbb R^n$; the measure of minimal energy, with capacity as its total mass | *Potential Theory* |
| the harmonic measure | the boundary of a domain; the distribution of the exit point of a Brownian path | *Potential Theory*; *Brownian Motion and Stochastic Calculus* |
| the Wiener measure | the Borel sets of the space of continuous paths; the law of Brownian motion | *Brownian Motion and Stochastic Calculus* |
| a Gaussian measure | the Borel sets of a Banach or Hilbert space; a centred Gaussian cylinder measure | *Stochastic Partial Differential Equations* |
| the law $\mu_X = \mathbb P \circ X^{-1}$ of a random variable | the Borel sets of the range; a probability measure | *Measure-Theoretic Probability* |
| a spectral measure $E(\lambda)$, $E$ projection-valued | the Borel sets of the spectrum; values are orthogonal projections | *Banach and Hilbert Spaces*; *Operator Algebras* |
| a signed measure $\nu$ | the measurable sets, with values in $\mathbb R$; $\sigma$-additive and taking at most one infinite value | *Measure Theory and Integration* |
| a complex measure | the measurable sets, with values in $\mathbb C$ | *Measure Theory and Integration* |
| the total variation $\lvert\nu\rvert$ | the measurable sets; the least measure dominating $\nu$ | *Measure Theory and Integration* |
| the Radon–Nikodym derivative $d\nu/d\mu$ | the measurable sets; a density realising the absolutely continuous part of $\nu$ | *Measure Theory and Integration* |

## Sets and Functions That Are Not Measures

| Object | The failure | Introduced in |
|---|---|---|
| the Vitali set $V \subseteq [0,1)$ | not Lebesgue measurable: no length can be assigned consistently with translation invariance and countable additivity | *Measure Theory and Integration* |
| an outer measure on all subsets | restricts to a measure only on the Carathéodory-measurable sets, and is not a measure on the whole power set | *Measure Theory and Integration* |
| the counting measure on an uncountable set | measures every set, but is not $\sigma$-finite | *Measure Theory and Integration* |
| a finitely additive set function | satisfies additivity over finite unions only, and need not be a measure | *Measure Theory and Integration* |
| a decreasing sequence without the finiteness hypothesis | continuity from above fails, as on $\mathbb N$ with counting measure and the sets $\{n, n+1,\dots\}$ | *Measure Theory and Integration* |

## Summary

This list gathers the measures of the corpus: the abstract measures and their construction by Carathéodory, the counting and Dirac measures, Lebesgue and the Hausdorff measures of Euclidean space, the Haar measures of locally compact groups with the modular function and the adelic Tamagawa measure, and the measures of potential theory, probability and spectral theory. Each row records the family of sets the measure acts on and the property that separates it, and the final table records the constructions that carry the name of a measure and are not one.

## Summary of Notation

The objects are named rather than denoted; the symbols occurring in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $\mu$, $\nu$, $\lambda$ | measures; $\lambda^n$ Lebesgue measure on $\mathbb R^n$ |
| $\mathcal A$, $\mathcal B$, $\mathcal B(X)$ | a $\sigma$-algebra, the Borel $\sigma$-algebra |
| $\delta_x$ | the Dirac measure at $x$ |
| $\mathcal H^s$ | Hausdorff $s$-measure |
| $\mu_L$, $\mu_R$, $\Delta$ | left and right Haar measure, modular function |
| $d^\times x$ | multiplicative Haar measure on $\mathbb Q_p^\times$ |
| $\mu_X$, $\mu \otimes \nu$ | law of $X$, product measure |
| $E(\lambda)$ | spectral measure |
| $d\nu/d\mu$ | Radon–Nikodym derivative |

## Further Reading

- Paul R. Halmos, *Measure Theory* (Van Nostrand, 1950; reprinted Springer, 1974), for the construction of measures by outer measures and the classical examples.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for Haar measure and invariant integration on groups.
- Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces* (Cambridge University Press, 1995), for the Hausdorff measures and the measures of geometric measure theory.
