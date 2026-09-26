
# __List of Inequalities__

## Introduction

This article lists the inequalities the corpus states and uses. An inequality is a relation of order or of size between quantities, and a row below names one inequality, records what it bounds — an inner product by a product of norms, an integral by a product of integrals, a function by its derivative, a solution by its data — and points to the article that proves it. Every row points to an article; this article introduces nothing and proves nothing. The inequalities are grouped by the layer that introduces them: the pointwise inequalities of convexity and order, the integral inequalities of the $L^p$ theory, the inequalities of the Sobolev scale, and the inequalities of geometry and of differential equations. The rows that record a failure — the converse that is false, the exponent that is sharp, the equality case that is the boundary of the inequality — stand beside the inequalities as non-examples.

## The Pointwise Inequalities of Convexity and Order

| Object | What it bounds, and its relation to the others | Introduced in |
|---|---|---|
| Cauchy–Schwarz | $\lvert\langle x,y\rangle\rvert \leq \lVert x\rVert\lVert y\rVert$; the basic inequality of an inner product space, with equality exactly on proportional vectors | *Banach and Hilbert Spaces* |
| Jensen's inequality | $\varphi(\int f\,d\mu) \leq \int \varphi\circ f\,d\mu$ for convex $\varphi$; the definition of convexity in its integral form | *Convex Analysis*; *Measure-Theoretic Probability* |
| the Fenchel–Young inequality | $\langle x,y\rangle \leq f(x) + f^*(y)$; the general form of Young's inequality, with equality exactly when $y \in \partial f(x)$ | *Convex Analysis* |
| the arithmetic–geometric mean inequality | $\sqrt{ab} \leq (a+b)/2$; the case $p = q = 2$ of Young | *Sobolev Spaces and Weak Solutions* |
| the convexity of the sublevel sets, and the supporting hyperplane inequality | $f(x) \geq f(x_0) + \langle v, x - x_0\rangle$ for $v$ in the subdifferential | *Convex Analysis* |
| Kantorovich's inequality | the ratio $\langle Ax,x\rangle\langle A^{-1}x,x\rangle \leq (M+m)^2/(4Mm)$ for positive spectra in $[m,M]$ | *Nonlinear Functional Analysis* |

## The Integral Inequalities of the $L^p$ Theory

| Object | What it bounds | Introduced in |
|---|---|---|
| Hölder's inequality | $\int \lvert fg\rvert \leq \lVert f\rVert_p\lVert g\rVert_q$ for $1/p+1/q=1$; the fundamental inequality of the $L^p$ spaces | *Measure Theory and Integration* |
| Minkowski's inequality | $\lVert f+g\rVert_p \leq \lVert f\rVert_p + \lVert g\rVert_p$; the triangle inequality that makes $L^p$ a normed space | *Measure Theory and Integration* |
| Young's convolution inequality | $\lVert f*g\rVert_r \leq \lVert f\rVert_p\lVert g\rVert_q$ for $1/p+1/q = 1/r + 1$ | *Real Harmonic Analysis* |
| Hausdorff–Young | $\lVert\hat f\rVert_q \leq \lVert f\rVert_p$ for $1 \leq p \leq 2$, $1/p + 1/q = 1$ | *Fourier Analysis on Euclidean Spaces* |
| the Riesz–Thorin interpolation inequality | $\lVert T\rVert_{L^p\to L^q} \leq \lVert T\rVert_{L^{p_0}\to L^{q_0}}^{1-\theta}\lVert T\rVert_{L^{p_1}\to L^{q_1}}^{\theta}$ | *Interpolation Theory*; *Fourier Analysis on Euclidean Spaces* |
| Chebyshev's inequality | $\mu(\lvert f\rvert \geq \lambda) \leq \lambda^{-p}\lVert f\rVert_p^p$; the bridge from $L^p$ convergence to convergence in measure | *Measure Theory and Integration* |
| the Hardy–Littlewood maximal inequality | $\lVert Mf\rVert_p \leq C_p\lVert f\rVert_p$ for $1<p\leq\infty$, with the weak-type bound at $p=1$ | *Real Harmonic Analysis* |
| the Hardy–Littlewood–Sobolev inequality | the fractional integral $I_\alpha f$ is bounded from $L^p$ to $L^q$ with $1/q = 1/p - \alpha/n$ | *Real Harmonic Analysis* |
| the maximal inequality for martingales | the maximal-function bound $\lambda\mathbb P(\sup_n \lvert M_n\rvert \geq \lambda) \leq \mathbb E\lvert M_N\rvert$ | *Martingales* |
| the Cauchy–Schwarz inequality for integrals | $\left(\int fg\right)^2 \leq \int f^2\int g^2$; the special case $p = q = 2$ of Hölder | *Fourier Analysis on Euclidean Spaces* |

A warning belongs here. The classical **Hardy inequality**, which bounds the mean of a function by the mean of its primitive, is not introduced anywhere in Parts I to III, and it is therefore absent from this list. The Hardy inequalities the corpus does carry are the maximal inequality and the fractional-integral inequality of the table above, both of them harmonic-analytic rather than the elementary averaging inequality, and they are the entries a reader who looks for "Hardy" should find.

## The Inequalities of the Sobolev Scale

| Object | What it bounds | Introduced in |
|---|---|---|
| the Sobolev embedding inequality | $\lVert f\rVert_{L^{p^*}} \leq C\lVert\nabla f\rVert_{L^p}$ for $p^* = np/(n-p)$, $p < n$ | *Sobolev Spaces and Weak Solutions* |
| the Sobolev inequality of geometric measure theory | the same bound as an isoperimetric inequality for the gradient measure | *Geometric Measure Theory* |
| the Gagliardo–Nirenberg inequality | $\lVert D^j f\rVert \leq C\lVert D^k f\rVert^\theta\lVert f\rVert^{1-\theta}$; the interpolation between derivatives | *Sobolev Spaces and Weak Solutions* |
| the Poincaré inequality | $\int_\Omega \lvert f - f_\Omega\rvert^p \leq C\int_\Omega \lvert\nabla f\rvert^p$; the control of a function by its gradient | *Sobolev Spaces and Weak Solutions*; *Markov Chains and Processes* |
| the Ladyzhenskaya inequality | $\lVert f\rVert_{L^4}^2 \leq C\lVert f\rVert_{L^2}\lVert\nabla f\rVert_{L^2}$ in two and three dimensions | *Sobolev Spaces and Weak Solutions* |
| the Morrey inequality | the Hölder continuity of a Sobolev function with $p>n$ | *Sobolev Spaces and Weak Solutions* |
| the Nash inequality | $\lVert f\rVert_2^{2+4/n} \leq C\lVert\nabla f\rVert_2^2\lVert f\rVert_1^{4/n}$; the embedding that underlies the heat-kernel bounds | *Random Walks on Groups* |
| the Besov embedding | $B^s_{p,q} \hookrightarrow B^{s'}_{p',q'}$ when $s - n/p = s' - n/p'$ and $q \leq q'$ | *Besov and Triebel–Lizorkin Spaces* |
| the Gagliardo–Nirenberg–Sobolev comparison | the Sobolev, Hölder, Morrey and Besov embeddings as the cases of one family | *Interpolation Theory* |

## The Inequalities of Geometry and of Differential Equations

| Object | What it bounds | Introduced in |
|---|---|---|
| the isoperimetric inequality | $\lvert\partial E\rvert \geq n\omega_n^{1/n}\lvert E\rvert^{(n-1)/n}$; the perimeter of a set by its volume | *Geometric Measure Theory* |
| the Brunn–Minkowski inequality | $\lvert E + F\rvert^{1/n} \geq \lvert E\rvert^{1/n} + \lvert F\rvert^{1/n}$ | *Geometric Measure Theory* |
| the Bellman–Grönwall inequality | a function bounded by an integral of itself is bounded by the exponential of the integral | *Ordinary Differential Equations* |
| the continuous-dependence estimate | the distance between two solutions bounded by the Grönwall factor times the perturbation | *Ordinary Differential Equations* |
| the Bellman–Grönwall inequality for delay equations | the same bound in the presence of a memory term | *Delay and Functional Differential Equations* |
| the comparison inequality for the delay equation | a solution bounded above by the solution of the associated comparison equation | *Delay and Functional Differential Equations* |
| the energy-decay inequality for the heat semigroup | $\lVert T(t)x\rVert \leq e^{\omega t}\lVert x\rVert$, the semigroup growth bound | *Semigroups and Evolution Equations* |
| the Ekeland variational inequality | the perturbed minimisation inequality $f(v) \leq \inf f + \epsilon$ at a near-minimiser | *Nonlinear Functional Analysis* |

## Failures, Sharpness and Equality Cases

| Object | The failure or the sharpness it records | Introduced in |
|---|---|---|
| Hölder's inequality outside the conjugate exponents | fails if $1/p + 1/q \neq 1$; equality holds exactly when $\lvert f\rvert^p$ and $\lvert g\rvert^q$ are proportional | *Measure Theory and Integration* |
| Young's convolution inequality at the endpoint $p = q = 1$ | is an equality, $\lVert f*g\rVert_1 = \lVert f\rVert_1\lVert g\rVert_1$, the boundary of the interpolated family | *Real Harmonic Analysis* |
| the sharp constant of the Sobolev inequality | attained exactly by the translates and dilates of a fixed extremal, so the inequality is strict off that orbit | *Sobolev Spaces and Weak Solutions* |
| the maximal inequality at $p = 1$ | the strong-type bound fails; only the weak-type $(1,1)$ bound holds | *Real Harmonic Analysis* |
| the isoperimetric inequality | equality holds exactly for balls; no other set attains it | *Geometric Measure Theory* |
| the Poincaré inequality without a normalisation | fails on functions with a constant part; the mean must be removed for the inequality to hold | *Sobolev Spaces and Weak Solutions* |
| Jensen's inequality for a non-convex $\varphi$ | fails; convexity is sharp for the inequality | *Convex Analysis* |

## Summary

This list gathers the inequalities of the corpus: the pointwise inequalities of convexity — Cauchy–Schwarz, Jensen, Young and the arithmetic–geometric mean — the integral inequalities of the $L^p$ theory, among them Hölder, Minkowski, Hausdorff–Young and the maximal and fractional-integral bounds, the inequalities of the Sobolev scale with the Poincaré, Gagliardo–Nirenberg, Ladyzhenskaya and Nash bounds, and the isoperimetric, Brunn–Minkowski and Bellman–Grönwall inequalities of geometry and of differential equations. The closing table records the sharpness of each and the cases where it fails.

## Summary of Notation

The objects are named rather than denoted; the symbols in the tables are collected here.

| Symbol | Meaning |
|---|---|
| $p$, $q$ | conjugate exponents, $1/p + 1/q = 1$ |
| $\lVert f\rVert_p$ | the $L^p$ norm |
| $\nabla f$, $D^j f$ | gradient and $j$-th derivative |
| $Mf$ | the Hardy–Littlewood maximal function |
| $I_\alpha f$ | the Riesz fractional integral of order $\alpha$ |
| $p^*$ | the Sobolev conjugate $np/(n-p)$ |
| $E$, $F$ | measurable sets; $\lvert E\rvert$ their volume |

## Further Reading

- Godfrey H. Hardy, John E. Littlewood and George Pólya, *Inequalities* (Cambridge University Press, 2nd ed. 1952), for the classical inequalities and their equality cases.
- Elliott H. Lieb and Michael Loss, *Analysis*, 2nd ed. (American Mathematical Society, 2001), for the sharp constants of the Sobolev, Hardy–Littlewood–Sobolev and Young inequalities.
- Robert A. Adams and John J. F. Fournier, *Sobolev Spaces*, 2nd ed. (Academic Press, 2003), for the embedding inequalities of the Sobolev and Besov scales.
