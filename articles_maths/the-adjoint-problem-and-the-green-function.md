# __The Adjoint Problem and the Green Function__

## Introduction

Every boundary-value problem has an adjoint, and the two Green functions are transposes of one another. For the problem

$$
Lu=f,\quad Bu=0
$$

the **adjoint problem** is

$$
L^{\dagger}v=g,\quad B^{*}v=0 ,
$$

where $L^{\dagger}$ is the formal adjoint and $B^{*}$ is the boundary condition selected by the requirement that the boundary form of the pair vanish; the Green function $G$ of the problem and the Green function $G^{*}$ of the adjoint problem satisfy the **reciprocity relation**

$$
G(x,y) = \overline{G^{*}(y,x)} ,
$$

and in the self-adjoint case, $L^{\dagger}=L$ and $B^{*}=B$, the Green function is Hermitian, $G(x,y)=\overline{G(y,x)}$. The reciprocity is the integral form of the identity $\langle Lu,v\rangle=\langle u,L^{\dagger}v\rangle$ on the admissible pairs, and it is the reason the solution operators of the two problems are adjoints.

This article reads the boundary-value problem with the conjugation that produces the adjoint. It fixes the adjoint problem and the adjoint boundary condition, proves the reciprocity relation for the Green functions and the symmetry of the Green function of a self-adjoint problem, derives the reciprocity of the solutions and the adjointness of the solution operators, and works the one-dimensional case and the first-order example in which the adjoint problem is genuinely different. It closes with the relation to the boundary form of *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*, of which the reciprocity is the operator form.

The formal adjoint $L^{\dagger}$, the boundary operator and the Green operator are those of *Differential Operators* and *The Green Operator*; the boundary form and the self-adjoint condition are *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the weak formulation and the solution operator are *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem*; the adjoint of a bounded operator and the Fredholm alternative are *Banach and Hilbert Spaces* and *Fredholm Theory*; the spectral theorem for the self-adjoint realisation is *Self-Adjoint Elliptic Operators and the Spectral Theorem*; and the classical Green function of the interval and its symmetry are *Ordinary Differential Equations* and *The Green Operator*. The pairing of the boundary data that defines the adjoint condition is *The Adjoint Boundary Condition*, below, and the general identity behind the computation is *The Lagrange Identity and the Self-Adjoint System*, below.

## The Adjoint Problem

**Definition.** Let $L$ be a differential operator with smooth coefficients on a domain $\Omega$ and let $B$ be a boundary condition, so that the realisation is defined on the admissible subspace $\mathcal{A}=\{u : Bu=0\}$. The **adjoint problem** is the boundary-value problem for $L^{\dagger}$ with the boundary condition $B^{*}$ whose admissible subspace is

$$
\mathcal{A}^{*} = \{v : B^{*}v=0\} ,
$$

chosen so that the boundary form vanishes on the pair:

$$
\langle u,v\rangle_\partial = 0 \qquad \text{for every } u\in\mathcal{A},\ v\in\mathcal{A}^{*} .
$$

A condition $B^{*}$ with this property is the **adjoint boundary condition**; when $B^{*}=B$ the problem is self-adjoint.

**Theorem (existence and the adjoint condition).** For every boundary condition $B$ of a differential operator there is an adjoint condition $B^{*}$, unique when the realisation of $L$ has dense domain; the realisation of $L^{\dagger}$ under $B^{*}$ is the adjoint of the realisation of $L$ under $B$. The problem is self-adjoint exactly when $L^{\dagger}=L$ and $B^{*}=B$.

*Proof.* The adjoint operator has the domain characterised by the vanishing of the boundary form against the admissible subspace: $\mathrm{dom}\,L^{*}=\{v : \langle Lu,v\rangle=\langle u,L^{\dagger}v\rangle \text{ for all } u\in\mathcal{A}\}$, and by the Green formula this is the set of $v$ with $\langle u,v\rangle_\partial=0$ for all $u\in\mathcal{A}$, which is a boundary condition of the same order as $B$; that condition is $B^{*}$. The uniqueness and the self-adjoint case follow from the definition.

**Definition.** The **Green function of the adjoint problem** is the kernel $G^{*}$ of the inverse of the realisation of $L^{\dagger}$ under $B^{*}$: for $g$ in the range,

$$
(L^{\dagger}v=g,\ B^{*}v=0) \iff v(x) = \int_\Omega G^{*}(x,y)\,g(y)\,dy .
$$

## Reciprocity

**Theorem (the reciprocity relation).** Let $G$ be the Green function of the problem $(L,B)$ and $G^{*}$ that of the adjoint problem $(L^{\dagger},B^{*})$. Then

$$
G(x,y) = \overline{G^{*}(y,x)} ,
$$

for almost every $(x,y)$; equivalently $G^{*}(x,y)=\overline{G(y,x)}$.

*Proof.* Let $u$ solve $Lu=f$ with $Bu=0$ and let $v$ solve $L^{\dagger}v=g$ with $B^{*}v=0$. The Green formula gives

$$
\int_\Omega(Lu)\bar v - \int_\Omega u\,\overline{L^{\dagger}v} = \langle u,v\rangle_\partial = 0 ,
$$

the vanishing being the defining property of the adjoint condition; hence

$$
\int_\Omega f\bar v = \int_\Omega u\,\bar g .
$$

Substituting the two Green representations, the left side becomes $\iint f(x)\overline{G^{*}(x,z)}\,\bar g(z)\,dz\,dx$ and the right side becomes $\iint G(y,w)f(w)\bar g(y)\,dw\,dy$; equating for all $f,g$ and relabelling gives the kernel identity

$$
G(y,w) = \overline{G^{*}(w,y)}
$$

for almost every pair $(y,w)$, which is the display after renaming the variables.

**Theorem (symmetry in the self-adjoint case).** If the problem is self-adjoint, then $G^{*}=G$ and the Green function is Hermitian,

$$
G(x,y) = \overline{G(y,x)} .
$$

*Proof.* Self-adjointness is $L^{\dagger}=L$ and $B^{*}=B$, so the adjoint problem is the original one and $G^{*}=G$; the reciprocity relation then reads $G(x,y)=\overline{G(y,x)}$.

**Corollary (reciprocity of the solutions).** Under the hypotheses of the reciprocity theorem, the solutions $u$ of $Lu=f$ and $v$ of $L^{\dagger}v=g$ satisfy

$$
\langle u,g\rangle = \langle f,v\rangle ,
$$

the **reciprocity of the solutions**; in the self-adjoint case this is the symmetry of the Green operator, $\langle Gf,g\rangle=\langle f,Gg\rangle$.

*Proof.* The identity $\int f\bar v=\int u\bar g$ is the display; the self-adjoint case is the same statement with $G^{*}=G$, which is the symmetry of the Green operator.

## The One-Dimensional Case and an Example

**Theorem (the adjoint of a Sturm–Liouville problem).** Let $\ell u=-(pu')'+qu$ on $(a,b)$ with real $p>0$, $q$, and let $B$ be a separated boundary condition. Then $L^{\dagger}=L$, and the adjoint condition $B^{*}$ is obtained by transposing the boundary matrices; for the Dirichlet, the Neumann and the Robin conditions the problem is self-adjoint, while for a general separated condition $B^{*}$ differs from $B$ and the two Green functions are related by the reciprocity relation.

*Proof.* The formal self-adjointness $L^{\dagger}=L$ is the integration by parts of *The Sturm–Liouville Operator*; the boundary form is the bracket $[p(u\bar v'-u'\bar v)]_a^b$, and the adjoint condition is the set of $v$ making the bracket zero against all admissible $u$, which is the transposed boundary matrix. For the listed conditions the matrix is symmetric up to the bracket and the condition is its own adjoint.

**Example (the first-order operator).** Let $L=d/dx$ on $(0,1)$ with the boundary condition $u(0)=0$. The formal adjoint is $L^{\dagger}=-d/dx$, and the boundary form is $\int_0^1(u'v+u v')dx=[u\bar v]_0^1 = u(1)\bar v(1)-u(0)\bar v(0)$; with $u(0)=0$ the vanishing for all admissible $u$ forces $v(1)=0$, so the adjoint condition is $v(1)=0$, the condition at the opposite endpoint. The Green function of $L=d/dx$ with $u(0)=0$ is $G(x,y)=\mathbf{1}_{y<x}$, the indicator of $y<x$; the Green function of the adjoint problem $-v'=g$ with $v(1)=0$ is $G^{*}(x,y)=\mathbf{1}_{x<y}$, the indicator of $x<y$; and the reciprocity relation reads $\mathbf{1}_{y<x}=\overline{\mathbf{1}_{x<y}}$, which is the identity of the two complementary indicators. The example shows the adjoint problem as a genuinely different problem, with the boundary condition moved to the other endpoint and the Green function transposed.

**Example (the self-adjoint Dirichlet problem).** For $-\Delta$ on $\Omega$ with the Dirichlet condition the problem is self-adjoint and the Green function is symmetric in the real case, $G(x,y)=G(y,x)$; the symmetry is the reciprocity of *The Green Operator* and the integral form of the symmetry of the realisation, and it is what makes the Dirichlet principle of *The Dirichlet Principle and the Hermitian Functional* available.

## Summary

Every boundary-value problem $(L,B)$ has an adjoint problem $(L^{\dagger},B^{*})$, where $L^{\dagger}$ is the formal adjoint and $B^{*}$ is the boundary condition making the boundary form vanish on the admissible pairs; $B^{*}$ is the condition characterising the domain of the adjoint operator, and the problem is self-adjoint when $L^{\dagger}=L$ and $B^{*}=B$. The Green function of the adjoint problem is related to the original one by the reciprocity relation $G(x,y)=\overline{G^{*}(y,x)}$, proved from the vanishing of the boundary form and the two Green representations; in the self-adjoint case $G^{*}=G$ and the Green function is Hermitian, $G(x,y)=\overline{G(y,x)}$, so in the real case it is symmetric. The same computation gives the reciprocity of the solutions $\langle u,g\rangle=\langle f,v\rangle$, that is, the adjointness of the two solution operators. In one dimension the adjoint of a Sturm–Liouville problem is computed by transposing the boundary matrices; the Dirichlet, Neumann and Robin conditions are self-adjoint, while the first-order example $L=d/dx$ with $u(0)=0$ has the adjoint $L^{\dagger}=-d/dx$ with $v(1)=0$ and the transposed Green functions $\mathbf{1}_{y<x}$ and $\mathbf{1}_{x<y}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$, $L^{\dagger}$ | Differential operator and its formal adjoint |
| $B$, $B^{*}$ | Boundary condition and its adjoint condition |
| $\mathcal{A}$, $\mathcal{A}^{*}$ | Admissible subspaces of $B$ and $B^{*}$ |
| $\langle u,v\rangle_\partial$ | Boundary form of the pair |
| $G(x,y)$, $G^{*}(x,y)$ | Green functions of the problem and of the adjoint problem |
| $G(x,y)=\overline{G^{*}(y,x)}$ | Reciprocity relation |
| $\langle u,g\rangle=\langle f,v\rangle$ | Reciprocity of the solutions |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the adjoint boundary-value problem and the symmetry of the Green function.
- Philip Hartman, *Ordinary Differential Equations* (Wiley, 2nd ed. 1982), for the adjoint conditions of a Sturm–Liouville problem.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the adjoint operator and its domain.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the adjoint of an unbounded operator and the boundary conditions.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the adjoint elliptic problem and the Green function.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the adjoint boundary conditions and the reciprocity.
