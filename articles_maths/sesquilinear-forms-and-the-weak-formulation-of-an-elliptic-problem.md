# __Sesquilinear Forms and the Weak Formulation of an Elliptic Problem__

## Introduction

An elliptic equation is solved in the weak sense by transposing it onto a sesquilinear form. For the operator

$$
Lu = -\sum_{i,j}\partial_i\bigl(a_{ij}\,\partial_ju\bigr) + \sum_j b_j\,\partial_ju + c\,u
$$

the form

$$
a(u,v) = \int_\Omega\Bigl(\sum_{i,j}a_{ij}\,\partial_ju\,\overline{\partial_iv} + \sum_j b_j\,\partial_ju\,\bar v + c\,u\,\bar v\Bigr)dx
$$

is obtained from the equation by one integration by parts, and it is defined on the first-order Sobolev space rather than on the second-order space of the classical problem. The equation $Lu=f$ then asks for a $u$ with $a(u,v)=\langle f,v\rangle$ for every admissible test function $v$; the boundary condition that the derivatives alone do not see is imposed by restricting the test space, and the derivative that falls on $u$ in the equation falls on $v$ in the form, so the equation makes sense for a $u$ with only one weak derivative. This is the **weak formulation**, and its existence theory is the Lax–Milgram theorem: boundedness and coercivity of the form produce a unique solution.

This article reads the elliptic problem with the conjugation of the unknown function, which is the reading of the star group. It fixes the sesquilinear form of a second-order elliptic operator, proves the boundedness and the coercivity that the theorem needs and identifies the Hermitian case with the formally self-adjoint operator; it states the weak formulation, derives the existence and uniqueness of the weak solution and its estimate; and it proves the equivalence with the classical problem when the solution is smooth, together with the regularity that carries the weak solution back to the strong one. It closes by identifying the solution operator with the inverse of the realisation.

The Sobolev spaces $H^1(\Omega)$, $H^1_0(\Omega)$, the weak derivative, the trace and the Rellich–Kondrachov theorem are those of *Sobolev Spaces and Weak Solutions*; the bounded sesquilinear forms, the represented operator and the Lax–Milgram theorem are those of *Sesquilinear Forms and the Lax–Milgram Theorem*, cited here and not reproved; the Dirichlet form, its generator and the energy functional are those of *Dirichlet Forms and the Hermitian Dirichlet Principle*; the realisation of a differential operator under a boundary condition and its Green operator are those of *Differential Operators* and *The Green Operator*; the classical elliptic problem and the boundary-value theory are those of *Partial Differential Equations*; and the formal adjoint and the Green formula are those of *Differential Operators* and *The Lagrange Identity and the Self-Adjoint System*. The minimisation of the energy and the variational characterisation of the eigenvalues are *The Dirichlet Principle and the Hermitian Functional* and *Variational Methods and the Hermitian Form*, below.

## The Sesquilinear Form of an Elliptic Operator

**Definition.** Let $\Omega\subseteq\mathbb{R}^n$ be a bounded open set with Lipschitz boundary, let the coefficients $a_{ij},b_j,c$ be bounded measurable functions on $\Omega$, and let $A=(a_{ij})$ be a real matrix-valued function. The **sesquilinear form of the operator** is

$$
a(u,v) = \int_\Omega\Bigl(\sum_{i,j}a_{ij}\,\partial_ju\,\overline{\partial_iv} + \sum_j b_j\,\partial_ju\,\bar v + c\,u\,\bar v\Bigr)dx ,
$$

defined for $u,v\in H^1(\Omega)$; the **elliptic form** is the case $b=0$ with $A$ symmetric,

$$
a(u,v) = \int_\Omega\Bigl(A\nabla u\cdot\overline{\nabla v} + c\,u\,\bar v\Bigr)dx .
$$

The form is linear in $u$ and conjugate-linear in $v$; it is the conjugation of $v$ that makes the principal part positive rather than merely real. The operator is recovered from the form by the Green formula of *Differential Operators*: for $u\in H^2(\Omega)$ and $v\in H^1_0(\Omega)$,

$$
a(u,v) = \int_\Omega (Lu)\,\bar v\,dx .
$$

**Theorem (boundedness).** Let the coefficients be bounded, with $\Lambda = \sup_{x}\|A(x)\|_{\mathrm{op}}$ the operator norm of the matrix and $M$ bounding the absolute values of the remaining coefficients. Then

$$
|a(u,v)| \le C\,\|u\|_{H^1}\|v\|_{H^1} \qquad (u,v\in H^1(\Omega)) ,
$$

with $C$ depending on $\Lambda$, $M$ and $n$; the form is a bounded sesquilinear form on $H^1(\Omega)$.

*Proof.* The estimate is the Cauchy–Schwarz inequality applied to each term of the sum: $|A\nabla u\cdot\overline{\nabla v}|\le\Lambda|\nabla u||\nabla v|$, $|b_j\partial_ju\bar v|\le\|b_j\|_\infty|\nabla u||v|$ and $|cu\bar v|\le\|c\|_\infty|u||v|$, followed by $|\nabla u||v|\le\frac12(|\nabla u|^2+|v|^2)$ and integration; the constants combine into $C$.

**Theorem (coercivity of the elliptic form).** Let $A$ be symmetric and **uniformly elliptic**, $\lambda|\xi|^2\le A(x)\xi\cdot\xi\le\Lambda|\xi|^2$ with $\lambda>0$, and let $c\ge0$ be bounded. Then the elliptic form is coercive on $H^1_0(\Omega)$:

$$
a(u,u)\ge\lambda\int_\Omega|\nabla u|^2 \ge \frac{\lambda}{1+C_P}\,\|u\|_{H^1}^2 ,
$$

where $C_P$ is the Poincaré constant; that is, $\operatorname{Re}a(u,u)\ge c_*\|u\|_{H^1}^2$ with $c_*=\lambda/(1+C_P)>0$, and the form is coercive.

*Proof.* For real symmetric $A$ the principal part is $\int A\nabla u\cdot\overline{\nabla u}\ge\lambda\|\nabla u\|^2$, by the ellipticity, and the lower-order term $\int c|u|^2$ is nonnegative. On $H^1_0(\Omega)$ the Poincaré inequality gives $\|u\|_{L^2}^2\le C_P\|\nabla u\|_{L^2}^2$, so $\|u\|_{H^1}^2=\|u\|^2+\|\nabla u\|^2\le(1+C_P)\|\nabla u\|^2$; substituting the bound on $\|\nabla u\|^2$ gives the display.

**Theorem (the Hermitian case).** The form $a$ is Hermitian, $a(u,v)=\overline{a(v,u)}$, if and only if $A=A^{\mathsf T}$ and $b=0$ with $c$ real; in that case the operator is formally self-adjoint, the form is the Hermitian form of the self-adjoint problem, and $a(u,u)$ is real.

*Proof.* Exchanging $u$ and $v$ and conjugating gives $\overline{a(v,u)}=\int(\sum a_{ji}\partial_iu\overline{\partial_jv}+\sum\bar b_j\partial_j\bar u\,v+\bar cu\bar v)$; comparing the terms with $a(u,v)$ gives $a_{ij}=\bar a_{ji}$, $b_j=0$ and $c=\bar c$. Since the coefficients are real, $a_{ij}=a_{ji}$ for all $i,j$ is $A=A^{\mathsf T}$, and then $a(u,u)$ is real.

## The Weak Formulation

**Definition.** Let $f\in L^2(\Omega)$ and let $H^1_0(\Omega)$ be the closed subspace of $H^1(\Omega)$ obtained by closing the test functions $C_c^\infty(\Omega)$. A **weak solution** of the Dirichlet problem for $L$ is a function $u\in H^1_0(\Omega)$ with

$$
a(u,v) = \langle f,v\rangle \qquad \text{for every } v\in H^1_0(\Omega) ,
$$

where $\langle f,v\rangle=\int_\Omega f\bar v\,dx$. The equation is the **weak formulation** of $Lu=f$ with the **Dirichlet condition** $u=0$ on $\partial\Omega$; the condition is imposed by the choice of the test space and not stated separately. A **Neumann problem** is the same equation with the full space $H^1(\Omega)$ as test space, and the boundary condition appears there as an extra term.

**Theorem (existence and uniqueness of the weak solution).** Let the elliptic form be bounded and coercive on $H^1_0(\Omega)$ and let $f\in L^2(\Omega)$. Then there is a unique $u\in H^1_0(\Omega)$ with $a(u,v)=\langle f,v\rangle$ for every $v$, and

$$
\|u\|_{H^1} \le \frac1c\,\|f\|_{L^2} .
$$

*Proof.* The map $v\mapsto\langle f,v\rangle$ is a bounded conjugate-linear functional on the Hilbert space $H^1_0(\Omega)$, because $|\langle f,v\rangle|\le\|f\|_{L^2}\|v\|_{L^2}\le\|f\|_{L^2}\|v\|_{H^1}$. The form $a$ is bounded and coercive, so the Lax–Milgram theorem of *Sesquilinear Forms and the Lax–Milgram Theorem* represents it by a boundedly invertible operator and gives the unique $u$ solving the equation, with the stated bound on $u$ in the form norm and hence in $H^1$.

**Theorem (equivalence with the classical problem).** If the weak solution $u$ lies in $H^2(\Omega)$, then $Lu=f$ almost everywhere on $\Omega$ and $u=0$ on $\partial\Omega$ in the trace sense; conversely, a classical solution of $Lu=f$ with $u=0$ on the boundary is a weak solution.

*Proof.* For $u\in H^2(\Omega)$ and $v\in C_c^\infty(\Omega)$ the Green formula gives $a(u,v)=\int(Lu)\bar v$; comparing with $\langle f,v\rangle$ for all test functions gives $Lu=f$ by the fundamental lemma. The boundary condition is the definition of $H^1_0(\Omega)$ as the closure of the test functions, and its trace vanishes. The converse is the Green formula in the other direction.

## Weak Boundary Conditions

**Definition.** The **essential** boundary condition of a weak formulation is one imposed by restricting the test space; the **natural** boundary condition is one that emerges from the equation as a boundary term and needs no restriction. For the second-order elliptic form the Dirichlet condition $u=0$ is essential on $H^1_0(\Omega)$, and the Neumann condition is natural.

**Theorem (the Neumann problem).** Let the elliptic form be bounded and coercive on the whole space $H^1(\Omega)$ and let $f\in L^2(\Omega)$ and $g\in L^2(\partial\Omega)$. Then there is a unique $u\in H^1(\Omega)$ with

$$
a(u,v) = \langle f,v\rangle + \langle g,\gamma v\rangle_{\partial\Omega} \qquad \text{for every } v\in H^1(\Omega) ,
$$

and if $u\in H^2(\Omega)$ then $Lu=f$ on $\Omega$ and $\partial_\nu u = g$ on $\partial\Omega$ in the trace sense, where $\partial_\nu$ is the co-normal derivative of the form.

*Proof.* The functional is bounded on $H^1(\Omega)$ because the trace maps $H^1(\Omega)$ boundedly into $L^2(\partial\Omega)$ by *Sobolev Spaces and Weak Solutions*; Lax–Milgram gives the unique $u$. For a smooth $u$, the Green formula applied to a test function $v\in C_c^\infty(\Omega)$ gives $Lu=f$, and applied to a general $v$ after subtracting the interior equation gives $\langle\partial_\nu u,v\rangle_{\partial\Omega}=\langle g,v\rangle_{\partial\Omega}$, whence the co-normal condition.

**Theorem (the interior weak condition).** For the Dirichlet problem the condition $u=0$ on $\partial\Omega$ is imposed in the trace sense, that is $\gamma u=0$, and every $u\in H^1_0(\Omega)$ has this property; conversely the weak solution with $f\in L^2(\Omega)$ and a coercive form is the unique $H^1_0$ function solving the equation.

*Proof.* The trace of a function of $H^1_0(\Omega)$ vanishes because the trace is continuous and the test functions have trace zero; the vanishing of the trace characterises $H^1_0(\Omega)$ when the boundary is Lipschitz. The uniqueness is the existence theorem.

**Remark (Robin and mixed conditions).** A **Robin condition** $\partial_\nu u+\sigma u=h$ is natural for the form with the boundary term $\langle\sigma u,v\rangle_{\partial\Omega}$; it is coercive on $H^1(\Omega)$ when $\sigma\ge0$ and the form is elliptic. A **mixed condition**, Dirichlet on part of the boundary and Neumann on the rest, is handled by the space of $H^1$ functions vanishing on the Dirichlet part, which is closed and on which the Poincaré inequality holds; the boundary form of *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory* is what selects which conditions are admissible.

## The Solution Operator and Regularity

**Definition.** The **solution operator** of the weak problem is the map $S : L^2(\Omega)\to H^1_0(\Omega)$ carrying $f$ to the unique weak solution. It is the inverse of the realisation of $L$ with domain $H^2(\Omega)\cap H^1_0(\Omega)$, and for a self-adjoint elliptic form with $c>0$ it is the Green operator of *The Green Operator* for the Dirichlet condition.

**Theorem (the solution operator is bounded and injective).** The solution operator $S$ is a bounded linear map $L^2(\Omega)\to H^1_0(\Omega)$, with $\|Sf\|_{H^1}\le\|f\|_{L^2}/c$; it is injective, and its range is the set of the weak solutions.

*Proof.* The bound is the estimate of the existence theorem, and the linearity is that of the equation. If $Sf=0$ then $a(0,v)=0=\langle f,v\rangle$ for every $v$ in the dense subspace $H^1_0$, so $f=0$; the range is by definition the set of weak solutions.

**Theorem (elliptic regularity).** Let the coefficients be smooth and the form uniformly elliptic, and let $f\in L^2(\Omega)$. Then the weak solution lies in $H^2_{\mathrm{loc}}(\Omega)$, and

$$
\|u\|_{H^2(\Omega)} \le C\bigl(\|f\|_{L^2(\Omega)}+\|u\|_{L^2(\Omega)}\bigr)
$$

when the boundary is smooth and the Dirichlet condition is imposed; in particular the solution operator factors through $H^2\cap H^1_0$ and is compact on $L^2(\Omega)$.

*Proof.* The interior regularity is the elliptic regularity theorem of *Distributions and Fundamental Solutions*, obtained by differentiating the weak equation and testing against the difference quotient, and the boundary regularity is the standard estimate for the Dirichlet problem with smooth data; the compactness is the Rellich–Kondrachov theorem of *Sobolev Spaces and Weak Solutions* applied to the inclusion $H^2\cap H^1_0\hookrightarrow L^2$. The detailed proof, with the boundary estimates, is that of *Partial Differential Equations*.

**Remark (Gårding's inequality).** The coercivity of the elliptic form holds when $c$ is large, and for a general bounded form with a possibly small $c$ the form satisfies **Gårding's inequality**, $a(u,u)\ge c\|u\|_{H^1}^2 - C\|u\|_{L^2}^2$; the equation $Lu=f$ is then shifted, $L+\mu$ for large $\mu$ is coercive, and the solvability of the original equation follows from the Fredholm alternative because the shift changes the operator by a bounded perturbation of the identity. The shift and the alternative are the standard route from the Lax–Milgram theorem to the general second-order elliptic problem, and they are carried out in *Partial Differential Equations*; the abstract form of the alternative is *Fredholm Theory*, later in this Part.

## Summary

The elliptic operator $L=-\sum\partial_i(a_{ij}\partial_j\cdot)+\sum b_j\partial_j\cdot+c$ is read through its sesquilinear form $a(u,v)=\int(\sum a_{ij}\partial_ju\overline{\partial_iv}+\sum b_j\partial_ju\bar v+cu\bar v)$, defined on $H^1(\Omega)$, linear in $u$ and conjugate-linear in $v$, and recovered from the operator by the Green formula. For bounded coefficients the form is bounded, $|a(u,v)|\le C\|u\|_{H^1}\|v\|_{H^1}$; for a symmetric uniformly elliptic matrix $A$ with $c$ bounded below it is coercive on $H^1_0(\Omega)$, $a(u,u)\ge c\|u\|^2_{H^1}$, by the ellipticity and the Poincaré inequality; and it is Hermitian exactly when $A$ is symmetric, $b=0$ and $c$ is real, which is the formal self-adjointness of the operator.

A weak solution of the Dirichlet problem is a $u\in H^1_0(\Omega)$ with $a(u,v)=\langle f,v\rangle$ for every test function, the boundary condition being imposed by the test space; for a bounded coercive form and $f\in L^2$ the Lax–Milgram theorem of *Sesquilinear Forms and the Lax–Milgram Theorem* gives a unique weak solution with $\|u\|_{H^1}\le\|f\|_{L^2}/c$, and for a smooth solution the weak and classical problems agree. The solution operator $S$ is bounded and injective, and elliptic regularity places its range in $H^2_{\mathrm{loc}}$; on a smooth bounded domain it factors through $H^2\cap H^1_0$ and is compact. When the form is not coercive but only satisfies Gårding's inequality, a shift and the Fredholm alternative give the solvability of the general problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega$ | Bounded open set with Lipschitz boundary |
| $a_{ij},b_j,c$ | Coefficients of the second-order elliptic operator |
| $L$ | Elliptic operator $-\sum\partial_i(a_{ij}\partial_j\cdot)+\sum b_j\partial_j\cdot+c$ |
| $a(u,v)$ | Sesquilinear form of the operator |
| $\Lambda$, $\lambda$ | Bounds of the coefficient matrix $A$ |
| $H^1(\Omega)$, $H^1_0(\Omega)$ | Sobolev space, and the closure of the test functions |
| weak solution | $u\in H^1_0$ with $a(u,v)=\langle f,v\rangle$ for all $v$ |
| $S$ | Solution operator $f\mapsto u$, the inverse of the realisation |
| $c_P$ | Poincaré constant |
| Gårding inequality | $a(u,u)\ge c\|u\|_{H^1}^2-C\|u\|_{L^2}^2$ |

## Further Reading

- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the weak formulation, Gårding's inequality and the elliptic regularity.
- Haïm Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (Springer, 2011), for Lax–Milgram in the elliptic setting and the weak Dirichlet problem.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the form of an elliptic operator and the solution operator.
- Lawrence C. Evans, *Partial Differential Equations* (American Mathematical Society, 2nd ed. 2010), for the energy method and the weak solutions of elliptic equations.
- Jean-Louis Lions and Enrico Magenes, *Non-Homogeneous Boundary Value Problems and Applications I* (Springer, 1972), for the variational formulation and the boundary conditions in the weak setting.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the Dirichlet principle and the weak existence theory.
