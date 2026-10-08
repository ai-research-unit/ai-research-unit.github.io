# __The Escape Radius and the Green's Function for the Biquaternions__

## Introduction

In the complex plane the escape radius and the Green's function are the two faces of one computation. A point $\zeta$ with $|\zeta|>1+|C|$ has $|\zeta_n|\to\infty$ monotonically, so the finite bound $1+|C|$ certifies escape; and on the escaping set the limit

$$
G_C(\zeta)=\lim_{n\to\infty}2^{-n}\log|\zeta_n|
$$

exists, vanishes exactly on the filled Julia set, satisfies $G_C(\zeta^2+C)=2G_C(\zeta)$, and behaves like $\log|\zeta|$ at infinity. In the biquaternion algebra $\mathbb{B}$ the first object fails: there is no single escape radius, because the square of a non-zero element can be zero. This article shows that the second object survives, in a conditional form off the zero divisors, states the exact form it takes for a central parameter, and places the general existence question in the pluripotential theory of Part III.

The quadratic family and its critical set are *The Biquaternion Quadratic Map and Its Julia Sets*; the failure of the single radius and the conditional radius $R_\delta$ are *The Biquaternion Mandelbrot Set and the Connectedness Locus*; the classical theory is *The Escape Radius and the Green's Function*, *The Filled Julia Set and the Green's Function* and *Plurisubharmonic Functions*; the pluripotential theory of several variables is *Plurisubharmonic Functions* and *Several Complex Variables*.

The article owns the escaping set, the Green's function of a biquaternion parameter, its norm-independence, its functional equation and its vanishing locus on the regular part, the exact eigenvalue formula for a central parameter, and the statement of the obstruction at the zero divisors.

**Standing convention.** $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ in the general plain bilinear product, $\mathcal K_{\tilde C}$ the filled Julia set, $J_{\tilde C}$ its boundary, $\|\cdot\|_E$ the Euclidean norm, $\|\cdot\|_F$ the Frobenius norm on $M_2(\mathbb{C})$.

## The Escaping Set

**Definition.** The **escaping set** of the parameter $\tilde C$ is

$$
\Omega_{\tilde C}=\{\tilde Q\in\mathbb{B} : \|F_{\tilde C}^n(\tilde Q)\|_E\to\infty\}, \qquad \text{equivalently } F_{\tilde C}^n(\tilde Q)\to\infty ,
$$

and its complement is the **non-escaping set** $\mathcal K^+_{\tilde C}=\mathbb{B}\setminus\Omega_{\tilde C}$, which contains the filled Julia set $\mathcal K_{\tilde C}$.

**Remark (the escaping set is norm-independent).** On the finite-dimensional space $\mathbb{B}$ all norms are equivalent, so $\|F^n(\tilde Q)\|_E\to\infty$ for one norm exactly when it does for every norm. **The escaping set, like the filled Julia set, is a set-theoretic object of the algebra, and only the radius that certifies membership in it is a metric object.**

The escaping set is strictly larger than the complement of the filled Julia set in general: an unbounded orbit is not the same as an orbit tending to infinity, and a biquaternion orbit can visit the zero-divisor cone and drop in norm without being bounded. The gap between $\Omega_{\tilde C}$ and the complement of $\mathcal K_{\tilde C}$ is where the Green's function may fail to exist.

## The Green's Function and Its Norm-Independence

**Definition.** For a point whose orbit tends to infinity put

$$
G_{\tilde C}(\tilde Q)=\lim_{n\to\infty}2^{-n}\log^+\|F_{\tilde C}^n(\tilde Q)\|_E ,
$$

when the limit exists, where $\log^+t=\max(\log t,0)$, and write $G_{\tilde C}(\tilde Q)=+\infty$ if the extended limit is $+\infty$. On an escaping orbit $\|F^n\|_E$ eventually exceeds $1$, so the plus is inactive there and the limit is the one written without it; the plus is what makes the value $0$ and not $-\infty$ on an orbit that meets the origin.

**Proposition (norm-independence).** If the limit defining $G_{\tilde C}(\tilde Q)$ exists for the Euclidean norm, then it exists and is equal for every norm on $\mathbb{B}$; the limit is thus a function of the algebra and the parameter and not of the metric.

**Proof.** Let $\|\cdot\|$ be another norm. Equivalence gives constants $m,M>0$ with $m\|\tilde V\|_E\le\|\tilde V\|\le M\|\tilde V\|_E$ for all $\tilde V$. Then

$$
2^{-n}\log^+ m+2^{-n}\log^+\|F^n(\tilde Q)\|_E \le 2^{-n}\log^+\|F^n(\tilde Q)\| \le 2^{-n}\log^+ M+2^{-n}\log^+\|F^n(\tilde Q)\|_E ,
$$

where the two comparisons use $|\log^+(mt)-\log^+t|\le|\log m|$ for $m,t>0$, and the two outer terms tend to the Euclidean limit because $2^{-n}\log^+m$ and $2^{-n}\log^+M$ do. A squeezed sequence has the limit of its bounds.

**Proposition (the functional equation and the vanishing locus).** Wherever $G_{\tilde C}$ is defined,

$$
G_{\tilde C}(F_{\tilde C}(\tilde Q))=2\,G_{\tilde C}(\tilde Q),
$$

and $G_{\tilde C}=0$ on $\mathcal K_{\tilde C}$: on every bounded orbit the sequence $2^{-n}\log^+\|F^n(\tilde Q)\|_E$ is $O(2^{-n})$ and tends to $0$.

**Proof.** The first identity is the shift $2^{-n}\log^+\|F^{n+1}(\tilde Q)\|=2\cdot 2^{-(n+1)}\log^+\|F^{n+1}(\tilde Q)\|$; the second is that a bounded orbit has $\log^+\|F^n\|_E\le\log^+(1+\sup\|\cdot\|_E)$ uniformly.

**Remark (the missing normalization at infinity).** In the complex plane the Green's function of a polynomial satisfies $G_C(\zeta)=\log|\zeta|+O(1)$ as $\zeta\to\infty$, and this normalization is what makes the function usable: it identifies the escape rate and turns $G_C$ into a potential. In $\mathbb{B}$ the normalization fails on the zero-divisor cone, because $\|\tilde Q^2\|_E$ has no lower bound in terms of $\|\tilde Q\|_E$ and a point of large norm can be sent to the origin in one step. **On the regular part of the escaping set the normalization holds; on the cone it cannot.** The precise statement is the next proposition.

## The Conditional Green's Function

**Proposition (conditional existence and normalization).** Let $\delta>0$ and let $\Omega_{\tilde C,\delta}$ be the set of the points $\tilde Q\in\Omega_{\tilde C}$ whose orbit satisfies $\sigma_2(M_n)\ge\delta\,\sigma_1(M_n)$ for every $n$, where $M_n=\Phi(F_{\tilde C}^n(\tilde Q))$. Then $G_{\tilde C}$ is defined on $\Omega_{\tilde C,\delta}$, and on it

$$
G_{\tilde C}(\tilde Q)=\log\|\tilde Q\|_E+O(1), \qquad \tilde Q\to\infty .
$$

**Proof.** By the conditional escape proposition of *The Biquaternion Mandelbrot Set and the Connectedness Locus*, $\|F_{\tilde C}(\tilde Q)\|_E\ge\delta^2\|\tilde Q\|_E^2$ on the condition, so with $\tilde Q_n=F_{\tilde C}^n(\tilde Q)$ and $t=\|\tilde Q\|_E$ one gets $\log\|\tilde Q_n\|_E\ge 2^n(\log t+2\log\delta)+O(1)$, and submultiplicativity up to the fixed factor gives the matching upper bound $\log\|\tilde Q_n\|_E\le 2^n(\log t+\tfrac12\log2)+O(1)$. Dividing by $2^n$ and letting $n\to\infty$ the limit exists and lies between $\log t+2\log\delta$ and $\log t+\tfrac12\log2$, whence $G_{\tilde C}(\tilde Q)=\log\|\tilde Q\|_E+O(1)$ with a constant depending on $\delta$. When $\delta^2\|\tilde Q\|_E\ge1$ the sizes increase from the first iterate, so the limit is an increasing limit, well defined whether finite or $+\infty$.

**Remark (why $\delta$ is unavoidable).** The condition is a lower bound on the reciprocal condition number of the iterate and is exactly what the collapse of the square forbids on the zero divisors. **The Green's function of a biquaternion parameter is a function on the $\delta$-regular part of the escaping set for every $\delta>0$, and it is on the union over $\delta$ of these sets; it fails to have a meaning on the orbits that meet the cone infinitely often, and there it is open.** The conditional radius $R_\delta$ of the previous article is the level set of $G_{\tilde C}$ implied by the same estimate.

## The Central Parameter

For a central parameter the whole pluripotential picture collapses to the complex one, because the orbit is the polynomial in one element and the spectrum separates.

**Theorem (the Green's function of a central parameter).** Let $\tilde C=Ce_0$, let $G_C$ be the Green's function of $\zeta\mapsto\zeta^2+C$, and let $\tilde Q$ have a diagonalisable matrix $\Phi(\tilde Q)$ with spectrum $\{\lambda_1,\lambda_2\}$. Then

$$
G_{\tilde C}(\tilde Q)=\max\bigl(G_C(\lambda_1),\,G_C(\lambda_2)\bigr),
$$

and in particular $\tilde Q\in\Omega_{\tilde C}$ if and only if at least one eigenvalue escapes, while $\tilde Q\in\mathcal K_{\tilde C}$ if and only if both eigenvalues lie in the filled Julia set $K_C$.

**Proof.** By the eigenvalue reduction the spectrum of $\Phi(F_{\tilde C}^n(\tilde Q))$ is $\{q_n(\lambda_1),q_n(\lambda_2)\}$. A matrix norm is comparable to the maximum modulus of the eigenvalues up to a constant depending only on the matrix and its diagonaliser, so $\log\|\Phi(F^n(\tilde Q))\|_F=\max_j\log|q_n(\lambda_j)|+O(1)$; dividing by $2^n$ and letting $n\to\infty$ the $O(2^{-n})$ term vanishes and the limit is the maximum of the two complex Green's functions. The escape and boundedness statements follow from $\Omega=\{G>0\}$ and $\mathcal K=\{G=0\}$ in the complex theory.

**Corollary (the escape radius of the central slice).** For $\tilde C=Ce_0$ every point whose matrix has an eigenvalue of modulus exceeding $1+|C|$ escapes, and the level sets of $G_{\tilde C}$ on a slice are the level sets of the two complex Green's functions.

## The General Parameter

For a non-central parameter the orbit is no longer a polynomial in one element, the spectrum does not separate, and there is no formula. What remains is the general pluripotential theory of polynomial maps of a complex space, and it must be quoted carefully, because the map here is degenerate.

**Remark (what the general theory gives, and what it does not).** For a polynomial map $F:\mathbb{C}^k\to\mathbb{C}^k$ of algebraic degree $d$ whose leading homogeneous part is proper, the limit $d^{-n}\log^+\|F^n\|$ exists, is plurisubharmonic or identically $-\infty$, vanishes exactly on the filled Julia set and satisfies $G(F)=d\,G$ (*Several Complex Variables*, *Plurisubharmonic Functions*, and the pluripotential theory of Part III). **The leading part of the biquaternion quadratic map is $\tilde Q^2$, and it is not proper: its fibre over $0$ is the square-zero cone** (a subset of the zero-divisor cone, of complex dimension two; *Biquaternion Square Roots of a General Element*). The general theory therefore does not apply off the cone without modification, the plurisubharmonic candidate $\log^+\|\tilde Q\|_E$ has the right growth but the pullback estimate fails on the cone, and the existence and regularity of the Green's function for a general biquaternion parameter are open. **The article's position is: the object is defined on the regular part, is exact for a central parameter, and is a research question in general.**

## Summary

There is no single escape radius for a biquaternion parameter, because a non-zero element can square to zero; the escaping set is nevertheless well defined and independent of the norm, and the finite certification of escape is the conditional radius $R_\delta$ indexed by the reciprocal condition number of the iterate. The Green's function $G_{\tilde C}=\lim 2^{-n}\log^+\|F_{\tilde C}^n\|$ is independent of the norm whenever it exists, satisfies $G\circ F=2G$, vanishes on the filled Julia set, and is defined on the $\delta$-regular part of the escaping set for every $\delta>0$, with the normalization $G=\log\|\tilde Q\|_E+O(1)$ there. For a central parameter it is exactly the maximum of the two complex Green's functions of the eigenvalues, so the central slice reproduces the classical escape radius and the classical level sets. For a non-central parameter the general pluripotential theory does not apply unchanged, because the leading part of the map is not proper and its exceptional set contains the zero-divisor cone; the existence and regularity of the Green's function there are open.

## Summary of Notation

| symbol | meaning |
|---|---|
| $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ | the biquaternion quadratic family |
| $\Omega_{\tilde C}$ | the escaping set, $\|F_{\tilde C}^n\|\to\infty$ |
| $\mathcal K_{\tilde C}$, $J_{\tilde C}$ | the filled Julia set and the Julia set |
| $G_{\tilde C}$ | the Green's function $\lim 2^{-n}\log\|F_{\tilde C}^n\|_E$ |
| $G_C$, $K_C$ | the classical Green's function and filled Julia set of $\zeta\mapsto\zeta^2+C$ |
| $\delta=\sigma_2/\sigma_1$ | the reciprocal condition number of $\Phi(\tilde Q)$ |
| $\Omega_{\tilde C,\delta}$ | the $\delta$-regular part of the escaping set |
| $R_\delta$ | the conditional escape radius |
| $q_n$ | the iterates of the complex quadratic map |

## Further Reading

- *The Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.md`), for the family and the central-parameter reduction.
- *The Biquaternion Mandelbrot Set and the Connectedness Locus* (`articles_maths/the-biquaternion-mandelbrot-set-and-the-connectedness-locus.md`), for the collapse of the square and the conditional radius.
- *The Escape Radius and the Green's Function* (`articles_maths/the-escape-radius-and-the-greens-function.md`), for the classical object and its normalization.
- *The Pluripotential Theory of the Biquaternion Dynamics* (`articles_maths/the-pluripotential-theory-of-the-biquaternion-dynamics.md`), for the several-variable theory and the equilibrium measure.
- *Several Complex Variables* (`articles_maths/several-complex-variables.md`), for the plurisubharmonic tools and the several-variable theory the general case would need.
