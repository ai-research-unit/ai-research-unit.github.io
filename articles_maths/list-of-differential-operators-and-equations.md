
# __List of Differential Operators and Equations__

## Introduction

This article lists the differential operators and the differential equations the corpus introduces. A differential operator is a map on functions assembled from the partial derivatives, and a differential equation is the equation obtained by setting such an operator, possibly with nonlinear terms, equal to a datum; a row below names one, records its order, its symbol and the solution theory that accompanies it, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The objects are grouped by the layer that introduces them: the operators of the vector and complex calculus, the linear equations of first and second order, the classification by symbol into the elliptic, parabolic and hyperbolic types, the nonlinear and nonlocal equations, and the solution theories that the corpus attaches to them. The rows that record a failure — an equation with no solution, an ill-posed problem, a breakdown of uniqueness — stand beside the equations as non-examples, so that the article records examples and non-examples side by side.

## The Operators of the Vector, Complex and Harmonic Calculus

| Object | Its order, symbol and setting | Introduced in |
|---|---|---|
| the derivative and the Fréchet derivative | order $1$; symbol $\sigma(D)(\xi) = i\xi$; the differential of a map between normed spaces | *Differential Calculus on Normed Spaces* |
| the gradient, divergence and curl | order $1$; the symbols $\xi$, $\langle\xi,\cdot\rangle$ and $\xi\times\cdot$; the operators of the vector calculus, and the Laplacian as $\operatorname{div}\nabla$ | *Differential Forms and Stokes' Theorem* |
| the exterior derivative $d$ | order $1$; symbol the exterior multiplication by $i\xi$; the operator of the de Rham complex, with $d^2=0$ | *Differential Forms and Stokes' Theorem* |
| the Laplacian $\Delta$ | order $2$; symbol $-\lvert\xi\rvert^2$; the elliptic operator of the corpus, with $\Delta = \operatorname{div}\nabla$ | *Partial Differential Equations*; *Harmonic Maps* |
| the d'Alembertian $\Box = \partial_t^2 - \Delta$ | order $2$; symbol $-\xi_0^2 + \lvert\xi\rvert^2$; the hyperbolic operator of the wave equation | *Partial Differential Equations*; *Biquaternion Analysis* |
| the Cauchy–Riemann operator $\bar\partial$ and its conjugate | order $1$; symbol $i(\xi_1 + i\xi_2)/2$; the operator of the complex and hypercomplex analysis | *Regularity and the Cauchy–Riemann Operator*; *Complex Analysis* |
| the Dirac operator $D$ and the twisted Cauchy–Riemann operator | order $1$; symbol the Clifford multiplication by $\xi$; the square is the Laplacian with a curvature term | *Dirac Operators*; *Clifford Modules and the Twisted Cauchy–Riemann Operator* |
| a Fourier multiplier | order and symbol free; defined by $\widehat{m(D)f} = m(\xi)\hat f$, and the general constant-coefficient operator | *Fourier Analysis on Euclidean Spaces*; *Pseudodifferential Operators* |
| a pseudodifferential operator | order $m$; a symbol $a(x,\xi)$ with an asymptotic expansion; the calculus that closes under composition and adjoints | *Pseudodifferential Operators*; *Microlocal Analysis* |

## The Linear Equations of First and Second Order

| Object | Its order, symbol and solution theory | Introduced in |
|---|---|---|
| a linear ordinary differential equation $y' = A(t)y$ | order $1$; symbol $-i\lambda$; solved by the matrix exponential, with the fundamental matrix | *Ordinary Differential Equations* |
| the Sturm–Liouville problem | order $2$; symbol $-(p\xi^2) + q$; the eigenvalue problem with the Riccati and oscillation theory | *Ordinary Differential Equations*; *The Calculus of Variations* |
| the Laplace equation $\Delta u = 0$ | order $2$; symbol $-\lvert\xi\rvert^2$; harmonic functions, the mean value property and the maximum principle | *Partial Differential Equations*; *Harmonic Maps* |
| the Poisson equation $\Delta u = f$ | order $2$; symbol $-\lvert\xi\rvert^2$; solved by the Newtonian potential, the fundamental solution of $\Delta$ | *Distributions and Fundamental Solutions*; *Partial Differential Equations* |
| the heat equation $u_t = \Delta u$ | order $2$; symbol $i\tau + \lvert\xi\rvert^2$; solved by the Gaussian kernel and the heat semigroup | *Semigroups and Evolution Equations*; *Partial Differential Equations* |
| the wave equation $u_{tt} = \Delta u$ | order $2$; symbol $-\tau^2 + \lvert\xi\rvert^2$; solved by the Kirchhoff and d'Alembert formulas, finite propagation speed | *Partial Differential Equations* |
| the Schrödinger equation $iu_t = -\Delta u + Vu$ | order $2$; symbol $\tau - \lvert\xi\rvert^2 + V$; solved by the unitary group $e^{-itH}$ of a self-adjoint operator, by Stone's theorem | *Semigroups and Evolution Equations*; *Integrable Systems* |
| the transport equation $u_t + b\,u_x = 0$ | order $1$, hyperbolic; symbol $i\tau + ib\xi$; solved along the characteristics by translation of the datum, with no smoothing | *Partial Differential Equations* |
| a delay differential equation | order $1$ with memory; the symbol is entire, $i\tau - A - Be^{-\tau h}$; solutions by the method of steps | *Delay and Functional Differential Equations* |
| a fractional differential equation | order $\alpha \in (0,1)$; symbol $\lvert\xi\rvert^\alpha$; solved by the Mittag-Leffler functions and the fractional semigroup | *Fractional Differential Equations* |

## The Classification by Symbol

| Object | The classification it carries | Introduced in |
|---|---|---|
| an elliptic operator | principal symbol positive definite: the Laplace type, with the elliptic regularity theory | *Partial Differential Equations*; *Regularity and the Cauchy–Riemann Operator* |
| a parabolic operator | symbol of the form $i\tau + a(\xi)$ with $a \geq 0$: the heat type, with smoothing for positive time | *Partial Differential Equations*; *Semigroups and Evolution Equations* |
| a hyperbolic operator | nondegenerate symbol of signature $(1,n)$: the wave type, with finite propagation speed and the Cauchy problem | *Partial Differential Equations* |
| the characteristic variety and the wave front set | the zeros of the principal symbol, and the directions in which a distribution fails to be smooth | *Microlocal Analysis*; *Pseudodifferential Operators* |
| the fundamental solution of an operator | the distribution $E$ with $PE = \delta$; the Green function and the parametrix | *Distributions and Fundamental Solutions* |
| the semigroup generated by an operator | a closed densely defined $A$ with the Hille–Yosida condition; $u' = Au$ solved by $T(t)$ | *Semigroups and Evolution Equations* |

## The Nonlinear, Variational and Geometric Equations

| Object | Its order, symbol and solution theory | Introduced in |
|---|---|---|
| the Euler–Lagrange equation | order $2$; the variational equation of a functional, symbol from the second variation | *The Calculus of Variations*; *Lagrangian and Hamiltonian Systems* |
| the minimal-surface equation | order $2$, quasilinear elliptic; the mean curvature equation, solved by the plateau problem | *Minimal Surfaces* |
| the harmonic-map equation | order $2$, semilinear elliptic; the harmonic map equation $\Delta u = A(u)(du,du)$ | *Harmonic Maps* |
| the Hamilton–Jacobi equation | order $1$, nonlinear; the eikonal and the characteristics | *Lagrangian and Hamiltonian Systems*; *The Calculus of Variations* |
| the Korteweg–de Vries equation | order $3$, dispersive; solved by the inverse scattering transform, with solitons | *Integrable Systems*; *Soliton Theory* |
| the nonlinear Schrödinger equation | order $2$, dispersive; the integrable and the focusing cases | *Integrable Systems* |
| the Navier–Stokes equations | order $2$, parabolic nonlinear; the existence and regularity problem | *Partial Differential Equations*; *Stochastic Partial Differential Equations* |
| a stochastic partial differential equation | order $2$ with a noise term; solved in the Itô and the Stratonovich sense | *Stochastic Partial Differential Equations* |
| an integral equation | order $0$; the Volterra and Fredholm forms, solved by the resolvent kernel | *Distributions and Fundamental Solutions* |

## Failures of the Solution Theory

| Object | The failure | Introduced in |
|---|---|---|
| the backward heat equation | ill-posed: the solution does not depend continuously on the data | *Partial Differential Equations* |
| a nonlinear equation with blow-up | no global solution, the norm reaching infinity in finite time | *Partial Differential Equations*; *Harmonic Maps* |
| the wave equation with a non-smooth characteristic datum | no classical solution; the solution must be taken in the sense of distributions or of energy | *Distributions and Fundamental Solutions*; *Partial Differential Equations* |
| a hyperbolic equation with a double characteristic | loses the finite propagation speed of the strictly hyperbolic case | *Microlocal Analysis* |
| the Euler–Lagrange equation of a non-convex functional | a critical point need not be a minimiser, and a minimiser need not exist | *The Calculus of Variations*; *Nonlinear Functional Analysis* |
| the Navier–Stokes equations in three dimensions | global regularity is unresolved; only the local and the weak theories are known | *Partial Differential Equations* |

## Summary

This list gathers the differential operators and equations of the corpus: the derivative, the vector-calculus operators, the Laplacian, the d'Alembertian, the Cauchy–Riemann and Dirac operators, the Fourier multipliers and the pseudodifferential operators; the linear equations of first and second order, from the ordinary equation to the heat, wave, Schrödinger and Sturm–Liouville problems; the elliptic, parabolic and hyperbolic classification by symbol; the variational, geometric and dispersive nonlinear equations; and the solution theories — fundamental solutions, semigroups, energy methods and microlocal parametrices. The closing table records the equations whose solution theory breaks down.

## Summary of Notation

The objects are named by their standard symbols; the tables use the following.

| Symbol | Meaning |
|---|---|
| $\Delta$, $\Box$ | Laplacian, d'Alembertian |
| $\bar\partial$, $D$ | Cauchy–Riemann operator, Dirac operator |
| $\sigma(P)$, $a(x,\xi)$ | principal symbol, full symbol of an operator |
| $E$, $G$ | fundamental solution, Green function |
| $T(t)$, $A$ | semigroup, its generator |
| $\operatorname{char}(P)$ | characteristic variety |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, vols. I–III (Springer, 1983–1985), for the classification by symbol, the fundamental solutions and the microlocal theory.
- Lawrence C. Evans, *Partial Differential Equations*, 2nd ed. (American Mathematical Society, 2010), for the classical solution theories of the Laplace, heat and wave equations and the nonlinear equations.
- Michael E. Taylor, *Partial Differential Equations*, vols. I–III (Springer, 1996), for the pseudodifferential calculus and the modern solution theories.
