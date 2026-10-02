# __Variational Methods and the Hermitian Form__

## Introduction

A Hermitian form is a quadratic functional, and its critical points on a constraint are eigenvectors. For a Hermitian form $a$ and a positive Hermitian form $b$ — the pairing of the space — the **Rayleigh quotient**

$$
R(u) = \frac{a(u,u)}{b(u,u)}
$$

has for its critical values the eigenvalues of the pair $(a,b)$, and the eigenvalues are recovered from $R$ by the **min–max principle**: the $k$-th eigenvalue is the maximum of $R$ over the $k$-dimensional subspaces, minimised over the choice of subspace. The eigenvalue equation is the **Euler–Lagrange equation** of the quotient, the first variation $a(u,v)=\lambda b(u,v)$ being the vanishing of the derivative of $R$ in every admissible direction, and the form $a$ is the second variation of the functional.

This article reads the Hermitian form variationally. It fixes the quadratic functional of the form and the polarisation identity that recovers the form from it; derives the Euler–Lagrange equation of a constrained critical point and identifies it with the eigenvalue problem; proves the min–max principle for the eigenvalues of a Hermitian form relative to a positive one, with the reality and the ordering of the critical values; and connects the general first variation of a Lagrangian functional to the Euler–Lagrange equation, showing that for a quadratic Lagrangian the second variation is the Hermitian form itself. It closes with the comparison of the two variational principles of the elliptic problem, the minimisation of the energy with a source and the minimisation of the quotient without one.

The sesquilinear form, its Hermitian property and the Hermitian form $a(u,v)=\langle Lu,v\rangle$ of a boundary-value problem are those of *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem* and *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the Dirichlet principle and the energy functional are *The Dirichlet Principle and the Hermitian Functional*; the general calculus of variations, the first variation and the Euler–Lagrange equation are *The Calculus of Variations* and *The Euler–Lagrange Equation*; the compact self-adjoint spectral theorem is *Banach and Hilbert Spaces*; and the eigenvalues of the Sturm–Liouville problem and the eigenvalue asymptotics are *The Sturm–Liouville Operator* and *Ordinary Differential Equations*. The spectral theorem for the elliptic operator and the Weyl law are *Self-Adjoint Elliptic Operators and the Spectral Theorem*, below.

## The Quadratic Functional of a Hermitian Form

**Definition.** Let $a$ be a Hermitian sesquilinear form on a complex vector space $\mathcal{D}$, linear in the first argument and conjugate-linear in the second. Its **quadratic functional** is

$$
Q(u) = a(u,u) ,
$$

real-valued on $\mathcal{D}$; a second positive Hermitian form $b$ plays the role of the constraint pairing. The **polarisation identity**

$$
a(u,v) = \frac14\Bigl(Q(u+v)-Q(u-v)+i\,Q(u+iv)-i\,Q(u-iv)\Bigr)
$$

recovers the form from its quadratic functional, so the form and the functional carry the same information.

**Proof of the polarisation identity.** Expanding, $Q(u\pm v)=a(u,u)\pm2\operatorname{Re}a(u,v)+a(v,v)$ and $Q(u\pm iv)=a(u,u)\pm2\operatorname{Im}a(u,v)+a(v,v)$, so the four terms $Q(u+v)-Q(u-v)+iQ(u+iv)-iQ(u-iv)$ combine to $4\operatorname{Re}a(u,v)+4i\operatorname{Im}a(u,v)=4a(u,v)$; the display is the combination divided by four.

**Definition.** A **critical point** of $Q$ on the set $\{u : b(u,u)=1\}$ is a $u$ with $b(u,u)=1$ at which the derivative of $Q$ vanishes in every direction tangent to the set; equivalently, a $u$ with

$$
a(u,v) = \lambda\,b(u,v) \qquad \text{for every } v ,
$$

for some $\lambda$, the **Lagrange multiplier**; this equation is the **Euler–Lagrange equation** of the constrained problem, and $\lambda=R(u)$.

**Theorem (critical points are eigenvectors).** Let $a,b$ be Hermitian, with $b$ positive, and let $u$ be a critical point of $Q$ on $\{b(u,u)=1\}$. Then $\lambda=R(u)$ is real and $u$ solves the eigenvalue problem $a(u,v)=\lambda b(u,v)$ for every $v$; conversely a solution of the eigenvalue problem with $b(u,u)=1$ is a critical point of $Q$.

*Proof.* The constraint is $b(u,u)=1$, and a tangent direction is a $v$ with $\operatorname{Re}b(u,v)=0$; the derivative of $Q$ in the direction $v$ is $2\operatorname{Re}a(u,v)$. The Lagrange multiplier rule gives $a(u,v)=\lambda b(u,v)$ for all $v$, with $\mu$ the multiplier; testing with $v=u$ gives $\lambda=a(u,u)/b(u,u)=R(u)$, which is real because both forms are Hermitian. The converse is the computation in reverse.

## The Rayleigh Quotient and the Min–Max Principle

**Theorem (the min–max principle).** Let $a$ be a Hermitian form and $b$ a positive Hermitian form on a space $\mathcal{D}$, with $a$ coercive relative to $b$, $a(u,u)\ge c\,b(u,u)$, and suppose that the operator representing $a$ relative to $b$ has a compact inverse. Then the eigenvalues $\lambda_1\le\lambda_2\le\cdots$ of the pair are positive, of finite multiplicity and tending to $+\infty$, and for every $k$,

$$
\lambda_k = \min_{\substack{V\subseteq\mathcal{D}\\ \dim V=k}}\ \max_{\substack{u\in V\\ u\neq0}} R(u) = \max_{\substack{V\subseteq\mathcal{D}\\ \operatorname{codim}V=k-1}}\ \min_{\substack{u\in V\\ u\neq0}} R(u) ,
$$

the minimum and the maximum being attained at the $k$-dimensional span of the first $k$ eigenfunctions and its orthogonal complement, respectively.

*Proof.* The coercivity and the compactness make the operator $A$ representing $a$ relative to $b$, $a(u,v)=b(Au,v)$, boundedly invertible with a compact self-adjoint inverse; the spectral theorem of *Banach and Hilbert Spaces* gives an orthonormal basis $(\varphi_n)$ for $b$ of eigenvectors, $A\varphi_n=\lambda_n\varphi_n$, with the eigenvalues real, of finite multiplicity and tending to zero for $A^{-1}$, hence $\lambda_n\to\infty$ with no accumulation. Ordering them gives the sequence. For the first formula: if $V$ has dimension $k$ then the intersection of $V$ with the $b$-orthogonal complement of $\varphi_1,\dots,\varphi_{k-1}$ is nonzero, and on it every $u$ has the expansion on $\varphi_k,\varphi_{k+1},\dots$, so $R(u)\ge\lambda_k$; hence $\max_V R\ge\lambda_k$ for every $V$, and the minimum over $V$ is at least $\lambda_k$. Choosing $V=\operatorname{span}(\varphi_1,\dots,\varphi_k)$ gives $\max R=\lambda_k$, since there $R$ is the Rayleigh quotient of the diagonal matrix $\operatorname{diag}(\lambda_1,\dots,\lambda_k)$, whose maximum is $\lambda_k$; so the minimum over $V$ equals $\lambda_k$. For the second formula: if $\operatorname{codim}V=k-1$ then $V\cap\operatorname{span}(\varphi_1,\dots,\varphi_k)\neq0$, and on that intersection $R\le\lambda_k$, so $\min_VR\le\lambda_k$; the choice of $V$ as the $b$-orthogonal complement of $\varphi_1,\dots,\varphi_{k-1}$ gives $\min_VR=\lambda_k$. Hence the max–min also equals $\lambda_k$.

**Corollary (the smallest eigenvalue).** The smallest eigenvalue of the pair is the minimum of the Rayleigh quotient,

$$
\lambda_1 = \min_{u\neq0} R(u) ,
$$

attained at the eigenfunction belonging to $\lambda_1$; when $a$ is coercive with respect to $b$ this minimum is positive and $R$ is bounded below.

**Example (the Sturm–Liouville eigenvalues).** For the Sturm–Liouville form $a(u,v)=\int_a^b(p\,u'\bar v'+q\,u\bar v)\,dx$ and the weighted pairing $b(u,v)=\int_a^b u\bar v\,w\,dx$ on the space of admissible functions, the Rayleigh quotient is

$$
R(u) = \frac{\int_a^b\bigl(p|u'|^2+q|u|^2\bigr)dx}{\int_a^b|u|^2 w\,dx} ,
$$

and the min–max principle gives the $k$-th eigenvalue as the minimum over the $k$-dimensional subspaces of the maximal quotient; for $p>0$ and $q\ge0$ the eigenvalues are positive and $\lambda_k\to\infty$. The classical comparison with the eigenvalue asymptotics and the Sturm oscillation theorem is that of *Ordinary Differential Equations* and *The Sturm–Liouville Operator*, and the min–max formula there is the same statement read with the eigenfunction expansion.

## The Euler–Lagrange Equation

**Definition.** Let $L(x,u,\nabla u)$ be a Lagrangian on a domain, real-valued and smooth, and let

$$
\mathcal{J}(u) = \int_\Omega L(x,u,\nabla u)\,dx
$$

be the **action**. A **critical point** of $\mathcal{J}$ is a $u$ at which the first variation vanishes in every direction $v\in C_c^\infty(\Omega)$:

$$
\frac{d}{dt}\Bigr|_{t=0}\mathcal{J}(u+tv) = 0 \qquad \text{for every } v .
$$

**Theorem (the Euler–Lagrange equation).** For a smooth Lagrangian $L$, a critical point $u$ of $\mathcal{J}$ satisfies

$$
\frac{\partial L}{\partial u} - \sum_j \partial_j\Bigl(\frac{\partial L}{\partial u_j}\Bigr) = 0 ,
$$

the **Euler–Lagrange equation**, in the weak sense; conversely a solution of the equation is a critical point.

*Proof.* The derivative of $\mathcal{J}$ at $u$ in the direction $v$ is $\int_\Omega\bigl(L_u v+L_{u_j}\partial_jv\bigr)dx$ with $L_u,L_{u_j}$ evaluated at $(x,u,\nabla u)$; integrating the second term by parts and using $v\in C_c^\infty$ gives $\int_\Omega\bigl(L_u-\sum_j\partial_jL_{u_j}\bigr)\bar v\,dx$, which vanishes for all $v$ exactly at the equation. The converse is the same computation.

**Theorem (the quadratic Lagrangian).** Let the Lagrangian be quadratic in $u$ and $\nabla u$ with the Hermitian form $a$ as its integral,

$$
L(x,u,\nabla u) = \sum_{i,j}a_{ij}\,\partial_ju\,\overline{\partial_iu} + c\,|u|^2 ,
$$

so that $\mathcal{J}(u)=a(u,u)$. Then the Euler–Lagrange equation of the Lagrangian is $a(u,v)=0$ for every $v$ — the homogeneous equation, whose only solution is $u=0$ when $a$ is coercive — and the **second variation** of $\mathcal{J}$ at any $u$ is

$$
\frac{d^2}{dt^2}\Bigr|_{t=0}\mathcal{J}(u+tv) = 2\,a(v,v) ,
$$

so a critical point is a local minimum exactly when $a(v,v)\ge0$ for every $v$, that is, exactly when the form is positive semidefinite.

*Proof.* The first variation of $a(u,u)$ is $2\operatorname{Re}a(u,v)$ and its vanishing for all $v$ is the equation $a(u,v)=0$ for all $v$; the second derivative is $2a(v,v)$ by the expansion $a(u+tv,u+tv)=a(u,u)+2t\operatorname{Re}a(u,v)+t^2a(v,v)$. The sign of the second variation is the definiteness of $a$.

**Remark (the two variational principles).** The Dirichlet principle of *The Dirichlet Principle and the Hermitian Functional* minimises the energy $E_f(u)=a(u,u)-2\operatorname{Re}\langle f,u\rangle$ with a fixed source, and its stationarity is the equation $a(u,v)=\langle f,v\rangle$. The Rayleigh quotient minimises the ratio $R(u)$ on the whole space, and its stationarity is the eigenvalue equation $a(u,v)=\lambda b(u,v)$; the first principle produces the weak solution of the inhomogeneous problem, the second the eigenvalues of the homogeneous one, and both are the vanishing of the first variation of a Hermitian functional with the same form $a$ as the second variation.

## Summary

A Hermitian form $a$ is the quadratic functional $Q(u)=a(u,u)$, from which the polarisation identity recovers the form; relative to a positive Hermitian form $b$ its critical points on the constraint $b(u,u)=1$ are the eigenvectors, the Lagrange multiplier being the eigenvalue and the derivative condition being $a(u,v)=\lambda b(u,v)$. The Rayleigh quotient $R(u)=a(u,u)/b(u,u)$ has for its critical values the eigenvalues of the pair, and the min–max principle gives them as alternating extrema: $\lambda_k$ is the smallest over the $k$-dimensional subspaces of the largest value of $R$, equivalently the largest over the codimension-$k-1$ subspaces of the smallest value. The smallest eigenvalue is the minimum of $R$ over the whole space, and for a coercive form the minimum is positive; the Sturm–Liouville eigenvalues are the instance, with the classical quotient $\int(p|u'|^2+q|u|^2)/\int|u|^2w$. For a Lagrangian functional the first variation vanishes exactly at the Euler–Lagrange equation, and for a quadratic Lagrangian the equation is the Euler–Lagrange equation of the Hermitian form, a critical point being a minimum exactly when the form is positive semidefinite; the Dirichlet principle and the Rayleigh quotient are the two variational principles of the same form, with and without a source.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a(u,v)$ | Hermitian form |
| $b(u,v)$ | Positive Hermitian form, the constraint pairing |
| $Q(u)=a(u,u)$ | Quadratic functional |
| $R(u)=a(u,u)/b(u,u)$ | Rayleigh quotient |
| $\lambda$, $\lambda_k$ | Eigenvalues, the critical values of $R$ |
| $\varphi_k$ | Eigenfunctions, the critical points |
| $V_k$ | $k$-dimensional subspace in the min–max |
| $\mathcal{J}(u)=\int L$ | Action functional of a Lagrangian |
| $L_u$, $L_{u_j}$ | Partial derivatives of the Lagrangian |

## Further Reading

- Richard Courant and David Hilbert, *Methods of Mathematical Physics I* (Interscience, 1953), for the Rayleigh quotient, the min–max principle and the eigenvalue variational problem.
- Richard Courant, *Variational methods for the solution of problems of equilibrium and vibration* (Bulletin of the American Mathematical Society 49, 1943), for the variational approach to eigenvalues.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* (Academic Press, 1978), for the min–max principle and the Courant–Fischer theorem.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the variational characterisation of the eigenvalues of a self-adjoint operator.
- Jean Dieudonné, *Foundations of Modern Analysis* (Academic Press, 1969), for the first variation and the Euler–Lagrange equation.
- Israel M. Gelfand and Sergei V. Fomin, *Calculus of Variations* (Prentice–Hall, 1963), for the Euler–Lagrange equation and the second variation.
