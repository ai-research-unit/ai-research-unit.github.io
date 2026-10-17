# __Variational Methods and the Hermitian Form__

## Introduction

A Hermitian form is a quadratic functional, and its critical points on a constraint are eigenvectors. For a Hermitian form $\mathfrak{a}$ and a positive Hermitian form $\mathfrak{b}$ — the pairing of the space — the **Rayleigh quotient**

$$
R(w) = \frac{\mathfrak{a}(w,w)}{\mathfrak{b}(w,w)}
$$

has for its critical values the eigenvalues of the pair $(a,b)$, and the eigenvalues are recovered from $R$ by the **min–max principle**: the $k$-th eigenvalue is the maximum of $R$ over the $k$-dimensional subspaces, minimised over the choice of subspace. The eigenvalue equation is the **Euler–Lagrange equation** of the quotient, the first variation $\mathfrak{a}(w,v)=\lambda \mathfrak{b}(w,v)$ being the vanishing of the derivative of $R$ in every admissible direction, and the form $\mathfrak{a}$ is the second variation of the functional.

This article reads the Hermitian form variationally. It fixes the quadratic functional of the form and the polarisation identity that recovers the form from it; derives the Euler–Lagrange equation of a constrained critical point and identifies it with the eigenvalue problem; proves the min–max principle for the eigenvalues of a Hermitian form relative to a positive one, with the reality and the ordering of the critical values; and connects the general first variation of a Lagrangian functional to the Euler–Lagrange equation, showing that for a quadratic Lagrangian the second variation is the Hermitian form itself. It closes with the comparison of the two variational principles of the elliptic problem, the minimisation of the energy with a source and the minimisation of the quotient without one.

The sesquilinear form, its Hermitian property and the Hermitian form $\mathfrak{a}(w,v)=\langle Lw,v\rangle$ of a boundary-value problem are those of *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem* and *Self-Adjoint Boundary Value Problems and the Sturm–Liouville Theory*; the Dirichlet principle and the energy functional are *The Dirichlet Principle and the Hermitian Functional*; the general calculus of variations, the first variation and the Euler–Lagrange equation are *The Calculus of Variations* and *The Euler–Lagrange Equation*; the compact self-adjoint spectral theorem is *Banach and Hilbert Spaces*; and the eigenvalues of the Sturm–Liouville problem and the eigenvalue asymptotics are *The Sturm–Liouville Operator* and *Ordinary Differential Equations*. The spectral theorem for the elliptic operator and the Weyl law are *Self-Adjoint Elliptic Operators and the Spectral Theorem*, below.

## The Quadratic Functional of a Hermitian Form

**Definition.** Let $\mathfrak{a}$ be a Hermitian sesquilinear form on a complex vector space $\mathcal{D}$, linear in the first argument and conjugate-linear in the second. Its **quadratic functional** is

$$
\mathfrak{Q}(w) = \mathfrak{a}(w,w) ,
$$

real-valued on $\mathcal{D}$; a second positive Hermitian form $\mathfrak{b}$ plays the role of the constraint pairing. The **polarisation identity**

$$
\mathfrak{a}(w,v) = \frac14\Bigl(\mathfrak{Q}(w+v)-\mathfrak{Q}(w-v)+i\,\mathfrak{Q}(w+iv)-i\,\mathfrak{Q}(w-iv)\Bigr)
$$

recovers the form from its quadratic functional, so the form and the functional carry the same information.

**Proof of the polarisation identity.** Expanding, $\mathfrak{Q}(w\pm v)=\mathfrak{a}(w,w)\pm2\operatorname{Re}\mathfrak{a}(w,v)+\mathfrak{a}(v,v)$ and $\mathfrak{Q}(w\pm iv)=\mathfrak{a}(w,w)\pm2\operatorname{Im}\mathfrak{a}(w,v)+\mathfrak{a}(v,v)$, so the four terms $\mathfrak{Q}(w+v)-\mathfrak{Q}(w-v)+iQ(w+iv)-iQ(w-iv)$ combine to $4\operatorname{Re}\mathfrak{a}(w,v)+4i\operatorname{Im}\mathfrak{a}(w,v)=4\mathfrak{a}(w,v)$; the display is the combination divided by four.

**Definition.** A **critical point** of $Q$ on the set $\{w : \mathfrak{b}(w,w)=1\}$ is a $w$ with $\mathfrak{b}(w,w)=1$ at which the derivative of $Q$ vanishes in every direction tangent to the set; equivalently, a $w$ with

$$
\mathfrak{a}(w,v) = \lambda\,\mathfrak{b}(w,v) \qquad \text{for every } v ,
$$

for some $\lambda$, the **Lagrange multiplier**; this equation is the **Euler–Lagrange equation** of the constrained problem, and $\lambda=R(w)$.

**Theorem (critical points are eigenvectors).** Let $a,b$ be Hermitian, with $\mathfrak{b}$ positive, and let $w$ be a critical point of $Q$ on $\{\mathfrak{b}(w,w)=1\}$. Then $\lambda=R(w)$ is real and $w$ solves the eigenvalue problem $\mathfrak{a}(w,v)=\lambda \mathfrak{b}(w,v)$ for every $v$; conversely a solution of the eigenvalue problem with $\mathfrak{b}(w,w)=1$ is a critical point of $Q$.

*Proof.* The constraint is $\mathfrak{b}(w,w)=1$, and a tangent direction is a $v$ with $\operatorname{Re}\mathfrak{b}(w,v)=0$; the derivative of $Q$ in the direction $v$ is $2\operatorname{Re}\mathfrak{a}(w,v)$. The Lagrange multiplier rule gives $\mathfrak{a}(w,v)=\lambda \mathfrak{b}(w,v)$ for all $v$, with $\mu$ the multiplier; testing with $v=w$ gives $\lambda=\mathfrak{a}(w,w)/\mathfrak{b}(w,w)=R(w)$, which is real because both forms are Hermitian. The converse is the computation in reverse.

## The Rayleigh Quotient and the Min–Max Principle

**Theorem (the min–max principle).** Let $\mathfrak{a}$ be a Hermitian form and $\mathfrak{b}$ a positive Hermitian form on a space $\mathcal{D}$, with $\mathfrak{a}$ coercive relative to $\mathfrak{b}$, $\mathfrak{a}(w,w)\ge c\,\mathfrak{b}(w,w)$, and suppose that the operator representing $\mathfrak{a}$ relative to $\mathfrak{b}$ has a compact inverse. Then the eigenvalues $\lambda_1\le\lambda_2\le\cdots$ of the pair are positive, of finite multiplicity and tending to $+\infty$, and for every $k$,

$$
\lambda_k = \min_{\substack{V\subseteq\mathcal{D}\\ \dim V=k}}\ \max_{\substack{w\in V\\ w\neq0}} R(w) = \max_{\substack{V\subseteq\mathcal{D}\\ \operatorname{codim}V=k-1}}\ \min_{\substack{w\in V\\ w\neq0}} R(w) ,
$$

the minimum and the maximum being attained at the $k$-dimensional span of the first $k$ eigenfunctions and its orthogonal complement, respectively.

*Proof.* The coercivity and the compactness make the operator $A$ representing $\mathfrak{a}$ relative to $\mathfrak{b}$, $\mathfrak{a}(w,v)=\mathfrak{b}(Aw,v)$, boundedly invertible with a compact self-adjoint inverse; the spectral theorem of *Banach and Hilbert Spaces* gives an orthonormal basis $(\varphi_n)$ for $\mathfrak{b}$ of eigenvectors, $A\varphi_n=\lambda_n\varphi_n$, with the eigenvalues real, of finite multiplicity and tending to zero for $A^{-1}$, hence $\lambda_n\to\infty$ with no accumulation. Ordering them gives the sequence. For the first formula: if $V$ has dimension $k$ then the intersection of $V$ with the $\mathfrak{b}$-orthogonal complement of $\varphi_1,\dots,\varphi_{k-1}$ is nonzero, and on it every $w$ has the expansion on $\varphi_k,\varphi_{k+1},\dots$, so $R(w)\ge\lambda_k$; hence $\max_V R\ge\lambda_k$ for every $V$, and the minimum over $V$ is at least $\lambda_k$. Choosing $V=\operatorname{span}(\varphi_1,\dots,\varphi_k)$ gives $\max R=\lambda_k$, since there $R$ is the Rayleigh quotient of the diagonal matrix $\operatorname{diag}(\lambda_1,\dots,\lambda_k)$, whose maximum is $\lambda_k$; so the minimum over $V$ equals $\lambda_k$. For the second formula: if $\operatorname{codim}V=k-1$ then $V\cap\operatorname{span}(\varphi_1,\dots,\varphi_k)\neq0$, and on that intersection $R\le\lambda_k$, so $\min_VR\le\lambda_k$; the choice of $V$ as the $\mathfrak{b}$-orthogonal complement of $\varphi_1,\dots,\varphi_{k-1}$ gives $\min_VR=\lambda_k$. Hence the max–min also equals $\lambda_k$.

**Corollary (the smallest eigenvalue).** The smallest eigenvalue of the pair is the minimum of the Rayleigh quotient,

$$
\lambda_1 = \min_{w\neq0} R(w) ,
$$

attained at the eigenfunction belonging to $\lambda_1$; when $\mathfrak{a}$ is coercive with respect to $\mathfrak{b}$ this minimum is positive and $R$ is bounded below.

**Example (the Sturm–Liouville eigenvalues).** For the Sturm–Liouville form $\mathfrak{a}(w,v)=\int_a^\mathfrak{b}(p\,w'\bar v'+q\,w\bar v)\,dx$ and the weighted pairing $\mathfrak{b}(w,v)=\int_a^b w\bar v\,w\,dx$ on the space of admissible functions, the Rayleigh quotient is

$$
R(w) = \frac{\int_a^b\bigl(p|w'|^2+q|w|^2\bigr)dx}{\int_a^b|w|^2 w\,dx} ,
$$

and the min–max principle gives the $k$-th eigenvalue as the minimum over the $k$-dimensional subspaces of the maximal quotient; for $p>0$ and $q\ge0$ the eigenvalues are positive and $\lambda_k\to\infty$. The classical comparison with the eigenvalue asymptotics and the Sturm oscillation theorem is that of *Ordinary Differential Equations* and *The Sturm–Liouville Operator*, and the min–max formula there is the same statement read with the eigenfunction expansion.

## The Euler–Lagrange Equation

**Definition.** Let $L(x,w,\nabla w)$ be a Lagrangian on a domain, real-valued and smooth, and let

$$
\mathcal{J}(w) = \int_\Omega L(x,w,\nabla w)\,dx
$$

be the **action**. A **critical point** of $\mathcal{J}$ is a $w$ at which the first variation vanishes in every direction $v\in C_c^\infty(\Omega)$:

$$
\frac{d}{dt}\Bigr|_{t=0}\mathcal{J}(w+tv) = 0 \qquad \text{for every } v .
$$

**Theorem (the Euler–Lagrange equation).** For a smooth Lagrangian $L$, a critical point $w$ of $\mathcal{J}$ satisfies

$$
\frac{\partial L}{\partial w} - \sum_j \partial/\partial x_j\,\Bigl(\frac{\partial L}{\partial w_j}\Bigr) = 0 ,
$$

the **Euler–Lagrange equation**, in the weak sense; conversely a solution of the equation is a critical point.

*Proof.* The derivative of $\mathcal{J}$ at $w$ in the direction $v$ is $\int_\Omega\bigl(\partial L/\partial w v+\partial L/\partial w_j\,\partial/\partial x_j\,v\bigr)dx$ with $\partial L/\partial w,\partial L/\partial w_j$ evaluated at $(x,w,\nabla w)$; integrating the second term by parts and using $v\in C_c^\infty$ gives $\int_\Omega\bigl(\partial L/\partial w-\sum_j\partial/\partial x_j\,\partial L/\partial w_j\bigr)\bar v\,dx$, which vanishes for all $v$ exactly at the equation. The converse is the same computation.

**Theorem (the quadratic Lagrangian).** Let the Lagrangian be quadratic in $w$ and $\nabla w$ with the Hermitian form $\mathfrak{a}$ as its integral,

$$
L(x,w,\nabla w) = \sum_{i,j}a_{ij}\,\partial/\partial x_j\,w\,\overline{\partial/\partial x_i\,w} + c\,|w|^2 ,
$$

so that $\mathcal{J}(w)=\mathfrak{a}(w,w)$. Then the Euler–Lagrange equation of the Lagrangian is $\mathfrak{a}(w,v)=0$ for every $v$ — the homogeneous equation, whose only solution is $w=0$ when $\mathfrak{a}$ is coercive — and the **second variation** of $\mathcal{J}$ at any $w$ is

$$
\frac{d^2}{dt^2}\Bigr|_{t=0}\mathcal{J}(w+tv) = 2\,\mathfrak{a}(v,v) ,
$$

so a critical point is a local minimum exactly when $\mathfrak{a}(v,v)\ge0$ for every $v$, that is, exactly when the form is positive semidefinite.

*Proof.* The first variation of $\mathfrak{a}(w,w)$ is $2\operatorname{Re}\mathfrak{a}(w,v)$ and its vanishing for all $v$ is the equation $\mathfrak{a}(w,v)=0$ for all $v$; the second derivative is $2\mathfrak{a}(v,v)$ by the expansion $\mathfrak{a}(w+tv,w+tv)=\mathfrak{a}(w,w)+2t\operatorname{Re}\mathfrak{a}(w,v)+t^2\mathfrak{a}(v,v)$. The sign of the second variation is the definiteness of $\mathfrak{a}$.

**Remark (the two variational principles).** The Dirichlet principle of *The Dirichlet Principle and the Hermitian Functional* minimises the energy $E_f(w)=\mathfrak{a}(w,w)-2\operatorname{Re}\langle f,w\rangle$ with a fixed source, and its stationarity is the equation $\mathfrak{a}(w,v)=\langle f,v\rangle$. The Rayleigh quotient minimises the ratio $R(w)$ on the whole space, and its stationarity is the eigenvalue equation $\mathfrak{a}(w,v)=\lambda \mathfrak{b}(w,v)$; the first principle produces the weak solution of the inhomogeneous problem, the second the eigenvalues of the homogeneous one, and both are the vanishing of the first variation of a Hermitian functional with the same form $\mathfrak{a}$ as the second variation.

## Summary

A Hermitian form $\mathfrak{a}$ is the quadratic functional $\mathfrak{Q}(w)=\mathfrak{a}(w,w)$, from which the polarisation identity recovers the form; relative to a positive Hermitian form $\mathfrak{b}$ its critical points on the constraint $\mathfrak{b}(w,w)=1$ are the eigenvectors, the Lagrange multiplier being the eigenvalue and the derivative condition being $\mathfrak{a}(w,v)=\lambda \mathfrak{b}(w,v)$. The Rayleigh quotient $R(w)=\mathfrak{a}(w,w)/\mathfrak{b}(w,w)$ has for its critical values the eigenvalues of the pair, and the min–max principle gives them as alternating extrema: $\lambda_k$ is the smallest over the $k$-dimensional subspaces of the largest value of $R$, equivalently the largest over the codimension-$k-1$ subspaces of the smallest value. The smallest eigenvalue is the minimum of $R$ over the whole space, and for a coercive form the minimum is positive; the Sturm–Liouville eigenvalues are the instance, with the classical quotient $\int(p|w'|^2+q|w|^2)/\int|w|^2w$. For a Lagrangian functional the first variation vanishes exactly at the Euler–Lagrange equation, and for a quadratic Lagrangian the equation is the Euler–Lagrange equation of the Hermitian form, a critical point being a minimum exactly when the form is positive semidefinite; the Dirichlet principle and the Rayleigh quotient are the two variational principles of the same form, with and without a source.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{a}(w,v)$ | Hermitian form |
| $\mathfrak{b}(w,v)$ | Positive Hermitian form, the constraint pairing |
| $\mathfrak{Q}(w)=\mathfrak{a}(w,w)$ | Quadratic functional |
| $R(w)=\mathfrak{a}(w,w)/\mathfrak{b}(w,w)$ | Rayleigh quotient |
| $\lambda$, $\lambda_k$ | Eigenvalues, the critical values of $R$ |
| $\varphi_k$ | Eigenfunctions, the critical points |
| $V_k$ | $k$-dimensional subspace in the min–max |
| $\mathcal{J}(w)=\int L$ | Action functional of a Lagrangian |
| $\partial L/\partial w$, $\partial L/\partial w_j$ | Partial derivatives of the Lagrangian |

## Further Reading

- Richard Courant and David Hilbert, *Methods of Mathematical Physics I* (Interscience, 1953), for the Rayleigh quotient, the min–max principle and the eigenvalue variational problem.
- Richard Courant, *Variational methods for the solution of problems of equilibrium and vibration* (Bulletin of the American Mathematical Society 49, 1943), for the variational approach to eigenvalues.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* (Academic Press, 1978), for the min–max principle and the Courant–Fischer theorem.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the variational characterisation of the eigenvalues of a self-adjoint operator.
- Jean Dieudonné, *Foundations of Modern Analysis* (Academic Press, 1969), for the first variation and the Euler–Lagrange equation.
- Israel M. Gelfand and Sergei V. Fomin, *Calculus of Variations* (Prentice–Hall, 1963), for the Euler–Lagrange equation and the second variation.
