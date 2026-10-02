# __The Lagrange Identity and the Self-Adjoint System__

## Introduction

The Green formula is the integrated form of an identity between the operator and its adjoint, and that identity is the **Lagrange identity**: the difference $\bar v\,Lu-u\,\overline{L^{\dagger}v}$ is a divergence,

$$
\bar v\,Lu-u\,\overline{L^{\dagger}v} = \operatorname{div}\mathbf P(u,v) ,
$$

where $\mathbf P(u,v)$ is the **bilinear concomitant**, a vector of boundary expressions of order one less than the operator in each variable. Integrating the identity over the domain and applying the divergence theorem produces the Green formula, the boundary integral being the flux of the concomitant through the boundary; the boundary form of *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory* is exactly that flux. When the operator is written as a first-order system, the same identity becomes the invariance of a **symplectic form**: the system is self-adjoint for a form $\omega$ when $\omega(Ay,z)+\omega(y,Az)=0$ for all $y,z$, and then $\omega$ is constant on pairs of solutions, its boundary values $[\omega(y,z)]_a^b$ being the boundary term.

This article reads the differential equation with the conjugation that defines the adjoint. It fixes the Lagrange identity in one and several variables, with the concomitant of a second-order operator written out and the general order stated; derives the Green formula from it; and passes to the system form, where the symplectic form appears, states the self-adjointness of the system, and identifies the boundary term as the boundary value of the symplectic form. It closes with the Sturm–Liouville equation as the instance, whose system is self-adjoint and whose concomitant is the classical bracket.

The formal adjoint and the boundary operator are those of *Differential Operators*; the boundary form, the Green formula and the self-adjoint condition are *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the Green function and the kernel symmetry are *The Green Operator* and *The Adjoint Problem and the Green Function*; the divergence theorem is *Vector Calculus and the Divergence Theorem*; the Sturm–Liouville expression and the classical bracket are *The Sturm–Liouville Operator* and *Ordinary Differential Equations*; and the systems of first-order equations, the fundamental matrix and the adjoint system are *Ordinary Differential Equations* and *Linear Systems of Differential Equations*. The pairing of the boundary data and the self-adjoint conditions are *The Adjoint Boundary Condition* and *Self-Adjoint Sturm–Liouville Operators*, below.

## The Lagrange Identity

**Theorem (the Lagrange identity).** Let $L=\sum_{k=0}^m p_k(x)\,\frac{d^k}{dx^k}$ be a differential operator on an interval with smooth coefficients and let $L^{\dagger}=\sum_{k=0}^m(-1)^k\frac{d^k}{dx^k}\bigl(\bar p_k\,\cdot\bigr)$ be its formal adjoint. Then there is a sesquilinear expression $P(u,v)$, the **bilinear concomitant**, of order at most $m-1$ in each of $u,v$, with

$$
\bar v\,Lu - u\,\overline{L^{\dagger}v} = \frac{d}{dx}P(u,v) ,
$$

the **Lagrange identity**; for the second-order operator $Lu=-(pu')'+qu$ with real $p>0$ and real $q$,

$$
P(u,v) = p\,(u\bar v'-u'\bar v) .
$$

*Proof.* Both sides are sesquilinear in $u,v$ and of order at most $m$ in each, and it suffices to verify the identity for the monomials $p_k u^{(k)}$ and $p_k\bar v^{(k)}$ by the product rule: each $k$-th derivative term contributes a total derivative after the $k$-fold integration by parts that defines the adjoint, and the accumulating boundary expressions assemble into $P$. For the second order, $\bar v\,(-(pu')'+qu)-u\,(-\overline{(pv')'}+qv) = p(u\bar v''-u''\bar v)+p'(u\bar v'-u'\bar v) = \frac{d}{dx}\bigl[p(u\bar v'-u'\bar v)\bigr]$, since $u\bar v''-u''\bar v=\frac{d}{dx}(u\bar v'-u'\bar v)$.

**Theorem (the divergence form).** Let $L=\sum_{|\alpha|\le m}a_\alpha(x)\partial^\alpha$ be a differential operator on a domain $\Omega\subseteq\mathbb{R}^n$ with smooth coefficients and let $L^{\dagger}$ be its formal adjoint. Then there is a vector field $x\mapsto\mathbf P(u,v)(x)$, the **concomitant vector**, with

$$
\bar v\,Lu - u\,\overline{L^{\dagger}v} = \operatorname{div}\mathbf P(u,v) ,
$$

a sesquilinear in $u,v$, of order at most $m-1$ in each variable in each component; in one variable $\mathbf P$ is the scalar $P$ above.

*Proof.* Each monomial $a_\alpha\partial^\alpha$ pairs with the adjoint monomial through the integration by parts, and the boundary terms of the $n$-dimensional product rule assemble into the divergence of a vector field built from the derivatives of $u$ and $v$ of order at most $m-1$; the scalar case is the display above. The argument is that of the divergence theorem applied monomial by monomial, and the resulting vector field is unique up to a divergence-free field, which does not change the identity.

## The Green Formula

**Theorem (the Green formula).** With the notation above and $\Omega$ a bounded domain with smooth boundary,

$$
\int_\Omega(Lu)\,\bar v\,dx - \int_\Omega u\,\overline{L^{\dagger}v}\,dx = \int_{\partial\Omega}\mathbf P(u,v)\cdot\nu\,dS ,
$$

where $\nu$ is the outward unit normal; the right side is the **boundary form**

$$
\langle u,v\rangle_\partial = \int_{\partial\Omega}\mathbf P(u,v)\cdot\nu\,dS ,
$$

an expression in the boundary data of $u$ and $v$, skew-Hermitian when $L=L^{\dagger}$.

*Proof.* Integrate the Lagrange identity over $\Omega$ and apply the divergence theorem of *Vector Calculus and the Divergence Theorem*; the left side is the difference of the two pairings and the right side is the flux of the concomitant. The skew-Hermitian property is that of *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*, computed by exchanging $u$ and $v$ and conjugating.

**Example (the second-order operator and the classical bracket).** For $Lu=-(pu')'+qu$ the concomitant vector is $\mathbf P(u,v)=p\,(u\nabla\bar v-\bar v\nabla u)$ and the boundary form is the classical bracket

$$
\langle u,v\rangle_\partial = \Bigl[p\,(u\bar v'-u'\bar v)\Bigr]_a^b
$$

in one dimension, and $\langle u,v\rangle_\partial=\int_{\partial\Omega}p\,\bigl(u\,\partial_\nu\bar v-\bar v\,\partial_\nu u\bigr)dS$ in several; the separated and periodic conditions of the classical theory are exactly the conditions that make it vanish, by *The Sturm–Liouville Operator*.

## The Self-Adjoint System

**Definition.** Let $y'=A(x)\,y$ be a first-order system of $n$ equations on an interval, with $A$ a smooth matrix-valued function, and let $z'=-A^{*}z$ be the **adjoint system**, $A^{*}=\bar A^{\mathsf T}$. A **symplectic form** for the system is a sesquilinear form $\omega(y,z)$ on the fibres such that $\omega(Ay,z)+\omega(y,Az)=0$ for all $y,z$; the system is then **self-adjoint for $\omega$**, and $\omega$ is **infinitesimally preserved**.

**Theorem (invariance of the symplectic form).** Let $\omega$ be a symplectic form for the system $y'=Ay$. Then for two solutions $y,z$ the function $x\mapsto\omega(y,z)$ is constant,

$$
\frac{d}{dx}\omega(y,z) = \omega(y',z)+\omega(y,z') = \omega(Ay,z)+\omega(y,Az) = 0 ,
$$

and the boundary term of the Lagrange identity is the difference of the boundary values $[\omega(y,z)]_a^b$.

*Proof.* The derivative of the sesquilinear form along the two solutions is $\omega(y',z)+\omega(y,z')$, the derivatives being $A y$ and $Az$; substituting the definition of the symplectic form gives zero. The boundary term of the Lagrange identity is by construction the cotangent expression in the boundary values, which for the first-order system is $\omega(y,z)$ evaluated at the endpoints.

**Theorem (the adjoint system and the pairing).** For the system $y'=Ay$ and its adjoint $z'=-A^*z$ the fibre pairing $\langle y,z\rangle$ is constant on pairs of solutions, $\frac{d}{dx}\langle y,z\rangle=0$, and the boundary form of the pair of problems is $[\langle y,z\rangle]_a^b$; the system is self-adjoint, that is, coincides with its adjoint system, exactly when $A^{*}=-A$, in which case $\omega=\langle\cdot,\cdot\rangle$ is a symplectic form in the sense above.

*Proof.* $\frac{d}{dx}\langle y,z\rangle=\langle y',z\rangle+\langle y,z'\rangle=\langle Ay,z\rangle+\langle y,-A^*z\rangle=\langle Ay,z\rangle-\langle Ay,z\rangle=0$. The self-adjoint case is $-A^{*}=A$; then the two derivatives of the pairing vanish and $\langle Ay,z\rangle+\langle y,Az\rangle=0$ by the skew-Hermitian property of $A$, so the pairing is a symplectic form.

**Theorem (the Sturm–Liouville system).** Let $\ell u=-(pu')'+qu$ on $(a,b)$ with real $p>0$ and real $q$, and write $y=(u,pu')$. Then $\ell u=\lambda w u$ reads as the system $y'=Ay$ with

$$
A = \begin{pmatrix}0 & 1/p\\ q-\lambda w & 0\end{pmatrix} ,
$$

and the form $\omega(y,z)=y_1\bar z_2-y_2\bar z_1=p(u\bar v'-u'\bar v)$ is symplectic for $A$ when $\lambda$ is real; the system is self-adjoint, $\omega$ is invariant on pairs of solutions, and the boundary term is the classical bracket $[\,p(u\bar v'-u'\bar v)\,]_a^b$. The two boundary conditions at $a$ and $b$ make the problem self-adjoint exactly when this form vanishes against the admissible pairs.

*Proof.* The first equation is $u'=y_2/p$ and the second is $(pu')'=(q-\lambda w)u$, which is the arrangement displayed. For real $\lambda$ and real coefficients, $\omega(Ay,z)+\omega(y,Az)=0$ by direct computation: $\omega(Ay,z)=\frac1p y_2\bar z_2-(q-\lambda w)y_1\bar z_1$ and $\omega(y,Az)=(q-\lambda w)y_1\bar z_1-\frac1p y_2\bar z_2$, which sum to zero. Invariance and the boundary form then follow from the two preceding theorems, and the self-adjointness of the scalar problem is the vanishing of the boundary term, which is *Self-Adjoint Sturm–Liouville Operators*, below.

## Summary

The Lagrange identity states that the difference $\bar v\,Lu-u\,\overline{L^{\dagger}v}$ is a divergence, $\operatorname{div}\mathbf P(u,v)$, the bilinear concomitant $\mathbf P$ being sesquilinear and of order one less than $L$ in each variable; for $Lu=-(pu')'+qu$ it is the scalar $p(u\bar v'-u'\bar v)$, and the identity is verified by the product rule. Integrating the identity over a domain and applying the divergence theorem gives the Green formula, whose boundary integral is the boundary form $\langle u,v\rangle_\partial$, an expression in the boundary data and skew-Hermitian when the operator is formally self-adjoint; in one dimension it is the classical bracket $[\,p(u\bar v'-u'\bar v)\,]_a^b$. Written as a first-order system $y'=Ay$, the identity becomes the invariance of a symplectic form: the system is self-adjoint for $\omega$ when $\omega(Ay,z)+\omega(y,Az)=0$, and then $\omega$ is constant on pairs of solutions and its boundary values are the boundary term. The adjoint system $z'=-A^*z$ has the pairing $\langle y,z\rangle$ constant on pairs of solutions and is self-adjoint exactly when $A^{*}=-A$. The Sturm–Liouville equation as the system $y=(u,pu')$ is the instance: its matrix $A$ is symplectic-skew for the classical form $p(u\bar v'-u'\bar v)$, the form is invariant, and the boundary term is the classical bracket whose vanishing is the self-adjointness of the problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$, $L^{\dagger}$ | Differential operator and its formal adjoint |
| $P(u,v)$ | Bilinear concomitant (scalar case) |
| $\mathbf P(u,v)$ | Concomitant vector (several variables) |
| $\operatorname{div}\mathbf P=\bar vLu-u\overline{L^{\dagger}v}$ | Lagrange identity |
| $\langle u,v\rangle_\partial=\int_{\partial\Omega}\mathbf P\cdot\nu\,dS$ | Boundary form (Green formula) |
| $y'=Ay$ | First-order system |
| $z'=-A^{*}z$ | Adjoint system, $A^{*}=\bar A^{\mathsf T}$ |
| $\omega(y,z)$ | Symplectic form; $\omega(Ay,z)+\omega(y,Az)=0$ |
| $p(u\bar v'-u'\bar v)$ | Classical concomitant and boundary bracket |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the Lagrange identity, the bilinear concomitant and the adjoint system.
- Einar Hille, *Lectures on Ordinary Differential Equations* (Addison–Wesley, 1969), for the self-adjoint boundary-value problems and the system form.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 2nd ed. 1982), for the Lagrange identity and the self-adjoint conditions of a linear system.
- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 2nd ed. 1989), for the symplectic form and the Hamiltonian systems, where the invariance is the conservation of the form.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the Lagrange identity, the concomitant and the Green formula in several variables.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the Green formula and the boundary terms of an elliptic operator.
