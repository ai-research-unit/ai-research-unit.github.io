# __The Evolution Operator__

## Introduction

The **evolution operator** of a dynamical system is the two-parameter family $\Phi(t,s)$ of linear maps that carries an initial state forward from time $s$ to time $t$; for the non-autonomous linear equation $\dot u=A(t)u$ it is the family with $u(t)=\Phi(t,s)u(s)$, and it obeys the **cocycle law** $\Phi(t,s)=\Phi(t,r)\Phi(r,s)$ for $s\le r\le t$. The law is the whole structural content of the notion: it says that the family is a representation of the ordered time axis by operators, and it holds for every system whose state is propagated linearly — the solution operator of a linear differential equation, the derivative of a flow, the linearisation of a map along an orbit, and the cocycles of a random dynamical system. When the law of motion does not depend on time the operator depends on the difference of its arguments alone, $\Phi(t,s)=T(t-s)$, and $T(t)$ is a one-parameter semigroup whose **generator** is the operator of the autonomous equation; the family and its generator determine each other, and the passage between them is the generation theory.

This article develops the evolution operator as an operator and nothing else, and it fixes the operator conventions that the rest of its group uses. It defines the two-parameter family, the cocycle law, strong continuity and the two-parameter group; it identifies the three places in which the operator arises — the non-autonomous linear equation, the variational equation along an orbit, and the derivative of a flow or of a map — and proves the law in each; it specialises to the autonomous case, states the generator, and quotes the generation theorems of *Semigroups and Evolution Equations* rather than reproving them; it treats the periodic case, where the operator over one period is the **monodromy operator** and the Floquet–Lyapunov factorisation reads the stability of a periodic orbit from its spectrum; and it closes with the operator as a cocycle over the time translation, the form in which it appears in *Random Dynamical Systems*.

The one-parameter semigroups, the generator, the resolvent, the Hille–Yosida and Lumer–Phillips theorems, the analytic semigroups and the spectral mapping theorem are those of *Semigroups and Evolution Equations*, which is the abstract theory of this article; the first-order linear systems, the fundamental matrix and the variation of constants are those of *Ordinary Differential Equations*; the vector fields, the flows, the variational equation $D\varphi_t$ and the derivative of a map are those of *Smooth Dynamical Systems*. The one-parameter flow acting on observables is *The Flow Operator*, its discrete counterpart is *The Koopman Operator*, the reduction of a flow to a return map is *The Poincaré Map*, and the pre-adjoint of these operators is *The Transfer Operator*, all later in this category. The operator-theoretic adjoint and the reversing involution are not used here: they are *The Adjoint of the Koopman Operator* and *Reversible Operators and the Involution*, in the `- * Operator Theory` group of this category.

No physics is invoked.

## The Two-Parameter Family

### Definition and the Cocycle Law

**Definition.** Let $X$ be a Banach space and let $J$ be an interval of $\mathbb{R}$ with the order. An **evolution operator** on $J$ is a family $\{\Phi(t,s)\}_{s,t\in J,\ s\le t}\subset B(X)$ with

$$
\Phi(s,s)=I \qquad (s\in J), \qquad \Phi(t,s)=\Phi(t,r)\Phi(r,s) \qquad (s\le r\le t \text{ in } J),
$$

the second identity being the **cocycle law**. The family is **strongly continuous** if $(t,s)\mapsto\Phi(t,s)x$ is continuous for every $x\in X$, and it is a **two-parameter group** if it is defined for all $s,t\in J$ and every $\Phi(t,s)$ is invertible, in which case the cocycle law holds without the order restriction and $\Phi(t,s)^{-1}=\Phi(s,t)$.

**Proposition (elementary consequences).** Let $\Phi$ be an evolution operator. Then (i) $\Phi(t,s)$ is determined by the one-parameter family $Y(t)=\Phi(t,t_0)$ for any fixed base time $t_0$, through $\Phi(t,s)=Y(t)Y(s)^{-1}$ whenever $Y(s)$ is invertible; (ii) if $\Phi$ is a two-parameter group then $\Phi(t,s)$ is invertible for all $s,t$; and (iii) the family is a cocycle for the additive action of $J$ on itself, $\Phi(t,s)=\Phi(t,r)\Phi(r,s)$, which is the defining relation of a **skew product** system.

*Proof.* Composing the cocycle law with the identity $\Phi(s,s)=I$ gives $\Phi(t,s)\Phi(s,t)=I$ and $\Phi(s,t)\Phi(t,s)=I$ whenever both orders are defined, which is (ii); the law $\Phi(t,s)=Y(t)Y(s)^{-1}$ follows from $\Phi(t,s)\Phi(s,t_0)=\Phi(t,t_0)$ and the definition of $Y$, which is (i). The reading (iii) is the cocycle law itself, with the second factor acting first.

### The Evolution Operator of a Linear Equation

**Definition.** Let $A(t)$, $t\in J$, be a family of closed densely defined operators on $X$, and consider the **non-autonomous linear equation**

$$
u'(t)=A(t)u(t) \qquad (t\in J).
$$

The **fundamental solution** or **evolution operator** of the equation is the family $\Phi(t,s)$ whose value on an initial datum $u(s)=x$ gives the solution $u(t)=\Phi(t,s)x$ of the equation. Under the hypotheses under which the equation is well posed — $A(t)$ the generator of an evolution family, or $A(t)$ continuous and bounded on compact subintervals — the family exists, is strongly continuous, and satisfies the cocycle law.

**Theorem (the cocycle law).** Let $\Phi$ be the fundamental solution of $u'=A(t)u$. Then $\Phi(t,s)=\Phi(t,r)\Phi(r,s)$ for $s\le r\le t$.

*Proof.* Fix $x\in X$ and let $u(t)=\Phi(t,s)x$ be the solution with $u(s)=x$. The function $v(t)=\Phi(t,r)u(r)$ solves the same equation with $v(r)=\Phi(r,r)u(r)=u(r)$, so by the uniqueness of the solution of the initial value problem $v(t)=u(t)$ for all $t\ge r$; at $t$ this reads $\Phi(t,s)x=\Phi(t,r)\Phi(r,s)x$, and $x$ was arbitrary.

**Theorem (the Peano series).** Let $A:J\to B(X)$ be continuous and let the interval be $[s,t]$. Then the fundamental solution is given by the norm-convergent **Peano series**

$$
\Phi(t,s)=\sum_{n\ge0}\ \int_{s\le t_1\le\cdots\le t_n\le t}A(t_1)\cdots A(t_n)\,dt_1\cdots dt_n,
$$

with the $n=0$ term the identity, and $\|\Phi(t,s)\|\le e^{\int_s^t\|A(u)\|\,du}$.

*Proof.* The integral equation $u(t)=x+\int_s^tA(u)u(u)\,du$ is solved by the Volterra iteration $u_0=x$, $u_{n+1}(t)=x+\int_s^tA(u)u_n(u)\,du$, whose $n$-th increment is the displayed $n$-fold integral; the estimate $\|u_{n+1}-u_n\|\le\frac{1}{(n+1)!}\bigl(\int_s^t\|A\|\bigr)^{n+1}\|x\|$ makes the series converge uniformly to the unique solution, and the norm bound follows by summing.

**Example (the commuting case).** If the operators $A(t)$ commute for distinct times, the Peano series sums to the exponential of the integral,

$$
\Phi(t,s)=\exp\Bigl(\int_s^tA(u)\,du\Bigr),
$$

because the ordered and the unordered integrals agree; a constant coefficient family, a family in a commutative algebra, and the scalar equation are the instances. When the operators do not commute the ordered integrals are all distinct and the exponential formula fails, the correction beginning with the commutator of two successive integrals.

### The Variational Equation along an Orbit

**Definition.** Let $X\in\mathrm{X}(M)$ be a smooth vector field on a manifold $M$ with flow $\varphi_t$. The **variational equation** along the orbit of $x$ is the linear equation

$$
Y'(t)=DX(\varphi_t(x))Y(t)
$$

on the tangent space $T_xM$, and its fundamental solution is the derivative $D\varphi_t(x)$ of the flow, since differentiating $\varphi_t$ in the initial condition gives this equation with $Y(0)=I$.

**Theorem (the evolution operator along an orbit).** The derivative of the flow is the evolution operator of the variational equation, and

$$
D\varphi_{t-s}(\varphi_s(x))=D\varphi_t(x)\,D\varphi_s(x)^{-1}, \qquad \Phi(t,s)=D\varphi_{t-s}(\varphi_s(x)) ;
$$

the cocycle law is the chain rule for the flow. For a diffeomorphism $T$ with orbit $\{T^nx\}$ the corresponding family is $\Phi(n,m)=DT^{n-m}(T^mx)$ on the tangent space.

*Proof.* The chain rule for $\varphi_t=\varphi_{t-s}\circ\varphi_s$ gives $D\varphi_t(x)=D\varphi_{t-s}(\varphi_s(x))\,D\varphi_s(x)$; composing with $D\varphi_s(x)^{-1}$, which exists because each $\varphi_s$ is a diffeomorphism, gives the identity. The discrete statement follows from $DT^{n}=DT^{n-m}(T^mx)\,DT^m(x)$.

The variational evolution operator is the linearisation of the system along a single orbit, and it is the object whose growth rates are the Lyapunov exponents; its spectrum at a periodic orbit is the set of Floquet multipliers of the smooth theory, treated below for the periodic coefficient case.

## The Semigroup Property and the Autonomous Case

### One-Parameter Semigroups

**Definition.** The evolution operator is **autonomous** if $A(t)=A$ does not depend on $t$. Then $\Phi(t,s)$ depends only on the difference, and writing

$$
T(t)=\Phi(t,0) \qquad (t\ge0), \qquad \Phi(t,s)=T(t-s),
$$

the cocycle law becomes the **semigroup law** $T(0)=I$ and $T(t+s)=T(t)T(s)$ for $s,t\ge0$; the family $\{T(t)\}_{t\ge0}$ is a **one-parameter semigroup** on $X$.

**Theorem (generation, quoted).** A strongly continuous semigroup $\{T(t)\}$ has a closed densely defined **generator** $A=\lim_{t\to0^+}\frac{1}{t}(T(t)-I)$, the map $t\mapsto T(t)x$ is differentiable with derivative $T(t)Ax$ for $x\in D(A)$, and the semigroup is recovered from the resolvent by the Laplace transform $R(\lambda,A)=\int_0^\infty e^{-\lambda t}T(t)\,dt$ for $\operatorname{Re}\lambda>\omega_0$. The semigroup is a contraction semigroup exactly when $A$ is closed, densely defined and $\|R(\lambda,A)\|\le1/\lambda$ for $\lambda>0$, by the **Hille–Yosida theorem**; the dissipative form of the same criterion is the **Lumer–Phillips theorem**.

*Proof.* Quoted as standard from *Semigroups and Evolution Equations*, where the generation theorems, the resolvent identity and the spectral mapping theorem are proved; the statement is repeated here only to fix the correspondence between the generator of the semigroup and the coefficient operator of the autonomous equation.

### The Generator of a Non-Autonomous Family

**Definition.** Let $\Phi$ be an evolution operator generated by the family $A(t)$. The **generator at time $t$** is the operator $A(t)$ of the equation, and the evolution operator is related to it by the two differential identities

$$
\frac{\partial}{\partial t}\Phi(t,s)=A(t)\Phi(t,s), \qquad \frac{\partial}{\partial s}\Phi(t,s)=-\Phi(t,s)A(s),
$$

the derivatives being taken in the strong sense on the domains of the operators.

*Proof.* The first identity is the equation $u'=A(t)u$ applied to $u(t)=\Phi(t,s)x$; the second follows from the first by differentiating the identity $\Phi(t,s)\Phi(s,t)=I$ with respect to $s$ and using the first with the roles of the arguments exchanged, which gives $A(s)\Phi(s,t)+\Phi(t,s)\frac{\partial}{\partial s}\Phi(s,t)=0$ and hence $\frac{\partial}{\partial s}\Phi(t,s)=-\Phi(t,s)A(s)$ after composing with $\Phi(t,s)$.

**Theorem (the abstract Cauchy problem, quoted).** Let $A(t)$ generate the evolution family $\Phi(t,s)$. Then the Cauchy problem $u'=A(t)u$, $u(s)=x$ has the unique mild solution $u(t)=\Phi(t,s)x$ for every $x\in X$, and it is a classical solution exactly when $x\in D(A(s))$. In the autonomous case this is the unique mild solution $u(t)=T(t)x$ of $u'=Au$.

*Proof.* Quoted from *Semigroups and Evolution Equations* for the autonomous case, and from *Ordinary Differential Equations* for the non-autonomous case with bounded generators; the uniqueness argument is the one given above for the cocycle law.

**Remark (what is not proved here).** The existence of an evolution family for a general family of unbounded operators $A(t)$ requires the **Kato theory** of the stable family of generators and the hyperbolic condition on the domains; the theorem is quoted as standard and no proof is attempted. The autonomous generation theorems are the content of *Semigroups and Evolution Equations*, and the present article uses them as a black box.

## Periodic Coefficients and the Monodromy Operator

### The Monodromy Operator

**Definition.** Let $A(t)$ be $T$-periodic, $A(t+T)=A(t)$, and let $\Phi(t,s)$ be its evolution operator. The **monodromy operator** over one period is

$$
M=\Phi(T,0)\in B(X);
$$

the values of the evolution operator at later periods are the powers of the monodromy, $\Phi(nT,0)=M^n$, and $\Phi(t+nT,s+nT)=\Phi(t,s)$.

**Theorem (Floquet–Lyapunov).** Let $A(t)$ be $T$-periodic and let $M$ be its monodromy. Then there is a $T$-periodic family $P(t)\in B(X)$ with $P(0)=I$ and a bounded operator $B$ with $e^{TB}=M$ such that

$$
\Phi(t,0)=P(t)e^{tB}, \qquad \Phi(t,s)=P(t)e^{(t-s)B}P(s)^{-1}.
$$

The eigenvalues of $M$ are the **Floquet multipliers** and the numbers $\lambda$ with $e^{T\lambda}\in\sigma(M)$ the **Floquet exponents**; the zero solution of the equation is exponentially stable exactly when every Floquet multiplier lies inside the unit circle, and unstable when one lies outside.

*Proof.* One defines $P(t)=\Phi(t,0)e^{-tB}$, where $B$ is a logarithm of $M$; then $P(t+T)=\Phi(t+T,0)e^{-tB}e^{-TB}=\Phi(t,0)Me^{-TB}e^{-tB}=P(t)$ by the periodicity of the equation and the choice $e^{TB}=M$, so $P$ is $T$-periodic and $P(0)=I$. The stability statement is the spectral radius formula for the powers of the monodromy, $M^n=\Phi(nT,0)$.

**Remark (the link with the return map).** For a periodic orbit of a flow the monodromy of the variational equation over one period and the derivative of the **Poincaré return map** on a transverse section carry the same stability information: the multipliers of the return map are the Floquet multipliers other than the trivial multiplier $1$ of the flow direction. The return map and its operator theory are *The Poincaré Map*, later in this category; the derivative of the return map at a periodic orbit belongs to *Smooth Dynamical Systems*, and no new proof is offered here.

**Example (a check of the monodromy series).** For the constant coefficient family $A(t)=J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and the period $T=\pi$, the Peano series

$$
\Phi(\pi,0)=\sum_{n\ge0}\frac{\pi^n}{n!}J^n=\begin{pmatrix}\cos\pi&-\sin\pi\\ \sin\pi&\cos\pi\end{pmatrix}=-I
$$

converges to the monodromy; truncating at $n=1,2,3,5,8,12,17$ gives the maximal entry errors $3.14$, $3.14$, $2.94$, $1.12$, $7.52\times10^{-2}$, $4.45\times10^{-4}$, $1.35\times10^{-7}$ against $-I$, the factorial decay of the series. The Floquet exponent is $i$, and the two multipliers are both $-1=e^{i\pi}$, so the monodromy is at the boundary of the unit disc and the stability is neutral.

## The Evolution Operator as a Cocycle

**Definition.** The cocycle law $\Phi(t,s)=\Phi(t,r)\Phi(r,s)$ is the defining relation of a **cocycle over the translation action** of the time axis on itself. If in addition the operators depend on a parameter $\omega$ in a probability space and the law reads

$$
\Phi(t+s,\omega)=\Phi(t,\theta_s\omega)\,\Phi(s,\omega)
$$

for a measure-preserving flow $\theta_t$ on the parameter space, the family is a **linear cocycle** over $\theta$, that is, a random dynamical system on $X$.

**Theorem (the multiplicative ergodic theorem, quoted).** Let $\Phi$ be a linear cocycle over a measure-preserving system $(\Omega,\theta)$ with $\log^+\|\Phi(1,\cdot)^{\pm1}\|\in L^1$. Then there are finitely many **Lyapunov exponents** $\lambda_1>\cdots>\lambda_r$ and a measurable equivariant filtration of $X$ such that $\frac1n\log\|\Phi(n,\omega)v\|\to\lambda_i$ for every nonzero $v$ in the corresponding subquotient, for almost every $\omega$.

*Proof.* Quoted as standard from *Random Dynamical Systems*, where the Oseledets theorem, the Kingman subadditive ergodic theorem and the Furstenberg–Kesten formula are proved; the deterministic variational evolution operator of the section above is the case of a single orbit, and its exponents are the limits $\frac1t\log\|D\varphi_t(x)v\|$ of *Hyperbolic Dynamics and Anosov Systems*.

The evolution operator is therefore the common form of three theories at once: the linear equation determines it, the derivative of the flow is an instance of it, and the random cocycle is its stochastic generalisation. The operator-theoretic statements about it — the adjoint, the involution that reverses time, and the duality with the transfer operator — belong to the `- * Operator Theory` group of this category and are not used here.

## Summary

The **evolution operator** of a dynamical system is a two-parameter family $\Phi(t,s)\subset B(X)$ with $\Phi(s,s)=I$ and the **cocycle law** $\Phi(t,s)=\Phi(t,r)\Phi(r,s)$ for $s\le r\le t$; it is the solution operator of a non-autonomous linear equation $\dot u=A(t)u$, in which case the law is the uniqueness of the initial value problem, and it is given by the norm-convergent **Peano series** $\Phi(t,s)=\sum_n\int_{s\le t_1\le\cdots\le t_n\le t}A(t_1)\cdots A(t_n)$ when $A(\cdot)$ is continuous and bounded, with $\|\Phi(t,s)\|\le e^{\int_s^t\|A\|}$ and the exponential formula in the commuting case. The **variational equation** along an orbit of a flow has the derivative $D\varphi_t(x)$ as its evolution operator, and the chain rule is the cocycle law: $\Phi(t,s)=D\varphi_{t-s}(\varphi_s(x))$; for a diffeomorphism the family is $\Phi(n,m)=DT^{n-m}(T^mx)$, and its growth rates are the Lyapunov exponents. In the **autonomous** case $\Phi(t,s)=T(t-s)$ for a one-parameter semigroup $T(t)$ with generator $A$, recovered from the resolvent as the Laplace transform; the generation theorems — Hille–Yosida, Feller–Miyadera–Phillips, Lumer–Phillips — are quoted from *Semigroups and Evolution Equations*, and the Cauchy problem has the unique mild solution $u(t)=\Phi(t,s)x$. For **$T$-periodic** coefficients the **monodromy operator** is $M=\Phi(T,0)$ and the **Floquet–Lyapunov** factorisation is $\Phi(t,0)=P(t)e^{tB}$ with $P$ $T$-periodic and $e^{TB}=M$; the eigenvalues of $M$ are the Floquet multipliers and decide the exponential stability, with the trivial multiplier $1$ of the flow direction corresponding to the derivative of the return map of *The Poincaré Map*. The family is a **cocycle over the time translation**, and over a measure-preserving parameter flow it is a linear cocycle whose exponents are given by the multiplicative ergodic theorem of *Random Dynamical Systems*; the adjoint and the time-reversing involution are not used here and belong to the `- * Operator Theory` group of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(t,s)$ | Evolution operator; $s\le t$, $\Phi(s,s)=I$, cocycle law |
| $A(t)$, $A$ | Coefficient operator of the non-autonomous equation; generator in the autonomous case |
| $X$ | Banach space on which the operators act |
| $J$ | Interval of times |
| $u'=A(t)u$ | Non-autonomous linear equation |
| $T(t)=\Phi(t,0)$ | One-parameter semigroup in the autonomous case |
| $D(A)$, $R(\lambda,A)$, $\omega_0$ | Domain, resolvent and growth bound of the semigroup |
| $M$, $P(t)$, $B$ | Monodromy, periodic factor and Floquet exponent operator |
| $\varphi_t$, $X$, $D\varphi_t(x)$ | Flow, vector field and derivative of the flow |
| $\theta_t$, $\omega$ | Parameter flow and parameter of a linear cocycle |
| $\lambda_1>\cdots>\lambda_r$ | Lyapunov exponents of a cocycle |

## Further Reading

- Einar Hille and Ralph S. Phillips, *Functional Analysis and Semi-Groups* (American Mathematical Society, 1957), for the generation theory and the resolvent representation.
- Kôsaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the semigroup and the Yosida approximation.
- Jerome A. Goldstein, *Semigroups of Linear Operators and Applications* (Oxford University Press, 1985), for the abstract Cauchy problem.
- Amnon Pazy, *Semigroups of Linear Operators and Applications to Partial Differential Equations* (Springer, 1983), for the analytic semigroups.
- Klaus-Jochen Engel and Rainer Nagel, *One-Parameter Semigroups for Linear Evolution Equations* (Springer, 2000), for the spectral mapping theorem and the evolution families.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the evolution families of a stable family of generators.
- Jack K. Hale, *Ordinary Differential Equations* (Krieger, 2nd ed. 1980), for the fundamental matrix, the variation of constants and the Floquet theory.
- W. A. Coppel, *Dichotomies in Stability Theory* (Springer, 1978), for the exponential dichotomies of the evolution operator.
- Ludwig Arnold, *Random Dynamical Systems* (Springer, 1998), for the linear cocycle and the multiplicative ergodic theorem.
