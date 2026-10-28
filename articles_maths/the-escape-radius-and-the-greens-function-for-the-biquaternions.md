# __The Escape Radius and the Green's Function for the Biquaternions__

## Introduction

In the complex plane the escape radius and the Green's function are the two faces of one computation. A point $\zeta$ with $|\zeta|>1+|C|$ has $|\zeta_n|\to\infty$ monotonically, so the finite bound $1+|C|$ certifies escape; and on the escaping set the limit

$$
G_C(\zeta)=\lim_{n\to\infty}2^{-n}\log|\zeta_n|
$$

exists, vanishes exactly on the filled Julia set, satisfies $G_C(\zeta^2+C)=2G_C(\zeta)$, and behaves like $\log|\zeta|$ at infinity. In the biquaternion algebra $\mathbb{B}$ the first object fails: there is no single escape radius, because the square of a non-zero element can be zero. This article shows that the second object survives, in a conditional form off the zero divisors, states the exact form it takes for a central parameter, and assembles the pluripotential framework it supports: the Monge–Ampère current, the conditional equilibrium measure, its product form on the idempotent plane, and the mass loss at the cone.

The quadratic family and its critical set are *The Biquaternion Quadratic Map and Its Julia Sets*; the failure of the single radius and the conditional radius $R_\delta$ are *The Biquaternion Mandelbrot Set and the Connectedness Locus*; the classical theory is *The Escape Radius and the Green's Function*, *The Filled Julia Set and the Green's Function* and *Plurisubharmonic Functions*; the pluripotential theory of several variables is *Plurisubharmonic Functions*, *Several Complex Variables* and *Fractal Analysis*.

The article owns the escaping set, the Green's function of a biquaternion parameter, its norm-independence, its functional equation and its vanishing locus on the regular part, the exact eigenvalue formula for a central parameter, the Monge–Ampère current and the conditional equilibrium measure, the product form of the measure on the idempotent plane, and the statement of the obstruction at the zero divisors.

**Standing convention.** $F_{\tilde Q_2}(\tilde Q)=\tilde Q^2+\tilde Q_2$ in the general plain bilinear product, $\mathcal K_{\tilde Q_2}$ the filled Julia set, $J_{\tilde Q_2}$ its boundary, $\|\cdot\|_E$ the Euclidean norm, $\|\cdot\|_F$ the Frobenius norm on $M_2(\mathbb{C})$.

## The Escaping Set

**Definition.** The **escaping set** of the parameter $\tilde Q_2$ is

$$
\Omega_{\tilde Q_2}=\{\tilde Q\in\mathbb{B} : \|F_{\tilde Q_2}^n(\tilde Q)\|_E\to\infty\}, \qquad \text{equivalently } F_{\tilde Q_2}^n(\tilde Q)\to\infty ,
$$

and its complement is the **non-escaping set** $\mathcal K^+_{\tilde Q_2}=\mathbb{B}\setminus\Omega_{\tilde Q_2}$, which contains the filled Julia set $\mathcal K_{\tilde Q_2}$.

**Remark (the escaping set is norm-independent).** On the finite-dimensional space $\mathbb{B}$ all norms are equivalent, so $\|F^n(\tilde Q)\|_E\to\infty$ for one norm exactly when it does for every norm. **The escaping set, like the filled Julia set, is a set-theoretic object of the algebra, and only the radius that certifies membership in it is a metric object.**

The escaping set is strictly larger than the complement of the filled Julia set in general: an unbounded orbit is not the same as an orbit tending to infinity, and a biquaternion orbit can visit the zero-divisor cone and drop in norm without being bounded. The gap between $\Omega_{\tilde Q_2}$ and the complement of $\mathcal K_{\tilde Q_2}$ is where the Green's function may fail to exist.

## The Green's Function and Its Norm-Independence

**Definition.** For a point whose orbit tends to infinity put

$$
G_{\tilde Q_2}(\tilde Q)=\lim_{n\to\infty}2^{-n}\log^+\|F_{\tilde Q_2}^n(\tilde Q)\|_E ,
$$

when the limit exists, where $\log^+t=\max(\log t,0)$, and write $G_{\tilde Q_2}(\tilde Q)=+\infty$ if the extended limit is $+\infty$. On an escaping orbit $\|F^n\|_E$ eventually exceeds $1$, so the plus is inactive there and the limit is the one written without it; the plus is what makes the value $0$ and not $-\infty$ on an orbit that meets the origin.

**Proposition (norm-independence).** If the limit defining $G_{\tilde Q_2}(\tilde Q)$ exists for the Euclidean norm, then it exists and is equal for every norm on $\mathbb{B}$; the limit is thus a function of the algebra and the parameter and not of the metric.

**Proof.** Let $\|\cdot\|$ be another norm. Equivalence gives constants $m,M>0$ with $m\|\tilde Q_1\|_E\le\|\tilde Q_1\|\le M\|\tilde Q_1\|_E$ for all $\tilde Q_1$. Then

$$
2^{-n}\log^+ m+2^{-n}\log^+\|F^n(\tilde Q)\|_E \le 2^{-n}\log^+\|F^n(\tilde Q)\| \le 2^{-n}\log^+ M+2^{-n}\log^+\|F^n(\tilde Q)\|_E ,
$$

where the two comparisons use $|\log^+(mt)-\log^+t|\le|\log m|$ for $m,t>0$, and the two outer terms tend to the Euclidean limit because $2^{-n}\log^+m$ and $2^{-n}\log^+M$ do. A squeezed sequence has the limit of its bounds.

**Proposition (the functional equation and the vanishing locus).** Wherever $G_{\tilde Q_2}$ is defined,

$$
\boxed{\;G_{\tilde Q_2}(F_{\tilde Q_2}(\tilde Q))=2\,G_{\tilde Q_2}(\tilde Q)\;},
$$

and $G_{\tilde Q_2}=0$ on $\mathcal K_{\tilde Q_2}$: on every bounded orbit the sequence $2^{-n}\log^+\|F^n(\tilde Q)\|_E$ is $O(2^{-n})$ and tends to $0$.

**Proof.** The first identity is the shift $2^{-n}\log^+\|F^{n+1}(\tilde Q)\|=2\cdot 2^{-(n+1)}\log^+\|F^{n+1}(\tilde Q)\|$; the second is that a bounded orbit has $\log^+\|F^n\|_E\le\log^+(1+\sup\|\cdot\|_E)$ uniformly.

**Remark (the missing normalization at infinity).** In the complex plane the Green's function of a polynomial satisfies $G_C(\zeta)=\log|\zeta|+O(1)$ as $\zeta\to\infty$, and this normalization is what makes the function usable: it identifies the escape rate and turns $G_C$ into a potential. In $\mathbb{B}$ the normalization fails on the zero-divisor cone, because $\|\tilde Q^2\|_E$ has no lower bound in terms of $\|\tilde Q\|_E$ and a point of large norm can be sent to the origin in one step. **On the regular part of the escaping set the normalization holds; on the cone it cannot.** The precise statement is the next proposition.

## The Conditional Green's Function

**Proposition (conditional existence and normalization).** Let $\delta>0$ and let $\Omega_{\tilde Q_2,\delta}$ be the set of the points $\tilde Q\in\Omega_{\tilde Q_2}$ whose orbit satisfies $\sigma_2(M_n)\ge\delta\,\sigma_1(M_n)$ for every $n$, where $M_n=\mathsf{M}_2(F_{\tilde Q_2}^n(\tilde Q))$. Then $G_{\tilde Q_2}$ is defined on $\Omega_{\tilde Q_2,\delta}$, and on it

$$
\boxed{\;G_{\tilde Q_2}(\tilde Q)=\log\|\tilde Q\|_E+O(1), \qquad \tilde Q\to\infty\;}.
$$

**Proof.** By the conditional escape proposition of *The Biquaternion Mandelbrot Set and the Connectedness Locus*, $\|F_{\tilde Q_2}(\tilde Q)\|_E\ge\delta^2\|\tilde Q\|_E^2$ on the condition, so with $\tilde Q_n=F_{\tilde Q_2}^n(\tilde Q)$ and $t=\|\tilde Q\|_E$ one gets $\log\|\tilde Q_n\|_E\ge 2^n(\log t+2\log\delta)+O(1)$, and submultiplicativity up to the fixed factor gives the matching upper bound $\log\|\tilde Q_n\|_E\le 2^n(\log t+\tfrac12\log2)+O(1)$. Dividing by $2^n$ and letting $n\to\infty$ the limit exists and lies between $\log t+2\log\delta$ and $\log t+\tfrac12\log2$, whence $G_{\tilde Q_2}(\tilde Q)=\log\|\tilde Q\|_E+O(1)$ with a constant depending on $\delta$. When $\delta^2\|\tilde Q\|_E\ge1$ the sizes increase from the first iterate, so the limit is an increasing limit, well defined whether finite or $+\infty$.

**Remark (why $\delta$ is unavoidable).** The condition is a lower bound on the reciprocal condition number of the iterate and is exactly what the collapse of the square forbids on the zero divisors. **The Green's function of a biquaternion parameter is a function on the $\delta$-regular part of the escaping set for every $\delta>0$, and it is on the union over $\delta$ of these sets; it fails to have a meaning on the orbits that meet the cone infinitely often, and there it is open.** The conditional radius $R_\delta$ of the previous article is the level set of $G_{\tilde Q_2}$ implied by the same estimate.

## The Central Parameter

For a central parameter the whole pluripotential picture collapses to the complex one, because the orbit is the polynomial in one element and the spectrum separates.

**Theorem (the Green's function of a central parameter).** Let $\tilde Q_2=Ce_t$, let $G_C$ be the Green's function of $\zeta\mapsto\zeta^2+C$, and let $\tilde Q$ have a diagonalisable matrix $\mathsf{M}_2(\tilde Q)$ with spectrum $\{\lambda_1,\lambda_2\}$. Then

$$
\boxed{\;G_{\tilde Q_2}(\tilde Q)=\max\bigl(G_C(\lambda_1),\,G_C(\lambda_2)\bigr)\;},
$$

and in particular $\tilde Q\in\Omega_{\tilde Q_2}$ if and only if at least one eigenvalue escapes, while $\tilde Q\in\mathcal K_{\tilde Q_2}$ if and only if both eigenvalues lie in the filled Julia set $K_C$.

**Proof.** By the eigenvalue reduction the spectrum of $\mathsf{M}_2(F_{\tilde Q_2}^n(\tilde Q))$ is $\{q_n(\lambda_1),q_n(\lambda_2)\}$. A matrix norm is comparable to the maximum modulus of the eigenvalues up to a constant depending only on the matrix and its diagonaliser, so $\log\|\mathsf{M}_2(F^n(\tilde Q))\|_F=\max_j\log|q_n(\lambda_j)|+O(1)$; dividing by $2^n$ and letting $n\to\infty$ the $O(2^{-n})$ term vanishes and the limit is the maximum of the two complex Green's functions. The escape and boundedness statements follow from $\Omega=\{G>0\}$ and $\mathcal K=\{G=0\}$ in the complex theory.

**Corollary (the escape radius of the central slice).** For $\tilde Q_2=Ce_t$ every point whose matrix has an eigenvalue of modulus exceeding $1+|C|$ escapes, and the level sets of $G_{\tilde Q_2}$ on a slice are the level sets of the two complex Green's functions.

## The Equilibrium Measure and the Monge–Ampère Current

The Green's function of a polynomial map of $\mathbb{C}^k$ carries a measure, and the measure is the bridge between the dynamics and the geometry: it is the harmonic measure of the fractal, the maximal-entropy measure, and the limit of the distribution of the preimages. For a proper map the construction is a theorem. For the biquaternion map the construction is conditional, and the failure is again the cone.

**Theorem (the equilibrium measure of a proper polynomial map).** Let $P:\mathbb{C}^k\to\mathbb{C}^k$ be a polynomial map of algebraic degree $d$ whose leading homogeneous part is proper, and let $G_P=\lim_{n\to\infty}d^{-n}\log^+\|P^n\|$ be its Green's function. Then $G_P$ is plurisubharmonic on $\mathbb{C}^k$ or identically $-\infty$, $P^*G_P=d\,G_P$, and

$$
\boxed{\;\mu_P=(dd^cG_P)^k\;}
$$

is a probability measure with $P^*\mu_P=d^k\mu_P$, supported on the Julia set of $P$, of maximal entropy $k\log d$, and satisfying the equidistribution of preimages.

**Proof.** This is the theorem of Fornæss–Sibony and Bedford–Jonsson, presented in *Several Complex Variables* and *Plurisubharmonic Functions*; the invariance is the chain rule $P^*dd^cG=dd^c(P^*G)=d\,dd^cG$ raised to the power $k$, and the normalisation is the definition of $\mu_P$.

**Remark (what properness buys).** The properness of the leading homogeneous part is what makes the pullback of $dd^cG$ a current of the right mass, equivalently what makes the pullback of the class of the hyperplane have the expected degree. **The biquaternion map fails exactly this hypothesis: the leading part $\tilde Q_1\mapsto\tilde Q_1^2$ has the square-zero cone as its fibre over $0$, and the mass is lost there.**

**Proposition (the current and its formal invariance).** Let $\tilde Q_2=Ce_t$ be central and let $G_{\tilde Q_2}$ be the Green's function, defined on the $\delta$-regular part of the escaping set. On the open set where $G_{\tilde Q_2}$ is plurisubharmonic and smooth, the current

$$
\boxed{\;\gamma_{\tilde Q_2}=(dd^cG_{\tilde Q_2})^4\;}
$$

is positive and satisfies $F_{\tilde Q_2}^*\gamma_{\tilde Q_2}=16\,\gamma_{\tilde Q_2}$.

**Proof.** $F_{\tilde Q_2}^*G_{\tilde Q_2}=2G_{\tilde Q_2}$ (*The Conditional Green's Function*, above), the pullback commutes with $dd^c$, and $dd^c(2G)=2\,dd^cG$; raising to the fourth power multiplies the current by $2^4=16$.

**Remark (sixteen is not the branch count).** The multiplier $16$ is the algebraic degree raised to the complex dimension, and it is the multiplier of the current, not the mass of a probability measure. The square map has four inverse branches generically, not sixteen (*Square Roots of an Element*), so the entropy suggested by the branches is $2\log2$, not $4\log2$. **The discrepancy between $16$ and $4$ is the measure-theoretic form of the mass loss at the cone, and it is the precise sense in which the several-variable theorem does not globalise.** The normalised equilibrium measure of the biquaternion map is therefore conditional: it exists on the regular part, it is not known to extend across the cone, and its entropy, where it exists, is expected to be $2\log2$.

**Theorem (the product form on the idempotent plane).** Let $\tilde\Pi$ be a primitive idempotent, $\tilde\Pi'$ the complementary primitive idempotent, $W_{\tilde\Pi}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'$ the idempotent plane, and $\tilde Q_2=C_1\tilde\Pi+C_2\tilde\Pi'$ a parameter in that plane. Then the equilibrium measure of the restriction is the product

$$
\boxed{\;\mu_{\tilde Q_2}\big|_{W_{\tilde\Pi}}=\mu_{C_1}\otimes\mu_{C_2}\;}
$$

of the two one-variable equilibrium measures of $\zeta\mapsto\zeta^2+C_j$, and its entropy is $2\log2$.

**Proof.** On the plane the map is the pair of complex quadratic maps (*The Slices of the Biquaternion Julia Sets*), the ambient complex dimension is two, and the equilibrium measure of a product map is the product of the equilibrium measures of the factors, the standard product theorem for polynomial maps (*Several Complex Variables*). The entropy adds, $\log2+\log2=2\log2$.

## The General Parameter

For a non-central parameter the orbit is no longer a polynomial in one element, the spectrum does not separate, and there is no formula. What remains is the general pluripotential theory of polynomial maps of a complex space, and it must be quoted carefully, because the map here is degenerate.

**Remark (what the general theory gives, and what it does not).** For a polynomial map $F:\mathbb{C}^k\to\mathbb{C}^k$ of algebraic degree $d$ whose leading homogeneous part is proper, the limit $d^{-n}\log^+\|F^n\|$ exists, is plurisubharmonic or identically $-\infty$, vanishes exactly on the filled Julia set and satisfies $G(F)=d\,G$ (*Several Complex Variables*, *Plurisubharmonic Functions*, and the pluripotential theory of Part III). **The leading part of the biquaternion quadratic map is $\tilde Q^2$, and it is not proper: its fibre over $0$ is the square-zero cone** (a subset of the zero-divisor cone, of complex dimension two; *Square Roots of an Element*). The general theory therefore does not apply off the cone without modification, the plurisubharmonic candidate $\log^+\|\tilde Q\|_E$ has the right growth but the pullback estimate fails on the cone, and the existence and regularity of the Green's function for a general biquaternion parameter are open. **The article's position is: the object is defined on the regular part, is exact for a central parameter, and is a research question in general.**

## Summary

There is no single escape radius for a biquaternion parameter, because a non-zero element can square to zero; the escaping set is nevertheless well defined and independent of the norm, and the finite certification of escape is the conditional radius $R_\delta$ indexed by the reciprocal condition number of the iterate. The Green's function $G_{\tilde Q_2}=\lim 2^{-n}\log^+\|F_{\tilde Q_2}^n\|$ is independent of the norm whenever it exists, satisfies $G_{\tilde Q_2}\circ F_{\tilde Q_2}=2G_{\tilde Q_2}$, vanishes on the filled Julia set, and is defined on the $\delta$-regular part of the escaping set for every $\delta>0$, with the normalization $G=\log\|\tilde Q\|_E+O(1)$ there. For a central parameter it is exactly the maximum of the two complex Green's functions of the eigenvalues, so the central slice reproduces the classical escape radius and the classical level sets.

The Monge–Ampère current $\gamma=(dd^cG)^4$ is positive and formally invariant with multiplier $16$ on the open set where $G$ is plurisubharmonic and smooth, but $16$ is the algebraic degree raised to the complex dimension and not the branch count: the square has four inverse branches, so the entropy suggested by them is $2\log2$, not $4\log2$. The discrepancy is the mass lost at the cone, and it is why the equilibrium measure is conditional on the regular part and why the several-variable theorem does not globalise. On the idempotent plane the measure is the product of the two one-variable equilibrium measures and its entropy is $2\log2$.

For a non-central parameter the general pluripotential theory does not apply unchanged, because the leading part of the map is not proper and its exceptional set contains the zero-divisor cone; the existence and regularity of the Green's function there are open.

## Summary of Notation

| symbol | meaning |
|---|---|
| $F_{\tilde Q_2}(\tilde Q)=\tilde Q^2+\tilde Q_2$ | the biquaternion quadratic family |
| $\Omega_{\tilde Q_2}$ | the escaping set, $\|F_{\tilde Q_2}^n\|\to\infty$ |
| $\mathcal K_{\tilde Q_2}$, $J_{\tilde Q_2}$ | the filled Julia set and the Julia set |
| $G_{\tilde Q_2}$ | the Green's function $\lim 2^{-n}\log\|F_{\tilde Q_2}^n\|_E$ |
| $G_C$, $K_C$ | the classical Green's function and filled Julia set of $\zeta\mapsto\zeta^2+C$ |
| $\delta=\sigma_2/\sigma_1$ | the reciprocal condition number of $\mathsf{M}_2(\tilde Q)$ |
| $\Omega_{\tilde Q_2,\delta}$ | the $\delta$-regular part of the escaping set |
| $R_\delta$ | the conditional escape radius |
| $q_n$ | the iterates of the complex quadratic map |
| $\gamma_{\tilde Q_2}=(dd^cG_{\tilde Q_2})^4$ | the Monge–Ampère current |
| $\mu_{\tilde Q_2}$ | the equilibrium measure, where it exists |
| $\mu_C$ | the one-variable equilibrium measure of $\zeta\mapsto\zeta^2+C$ |
| $k=4$, $d=2$ | the complex dimension and the algebraic degree |
| $W_{\tilde\Pi}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'$ | the idempotent plane |

## Further Reading

- [The Biquaternion Quadratic Map and Its Julia Sets](the-biquaternion-quadratic-map-and-its-julia-sets.html), for the family and the central-parameter reduction.
- [The Biquaternion Mandelbrot Set and the Connectedness Locus](the-biquaternion-mandelbrot-set-and-the-connectedness-locus.html), for the collapse of the square and the conditional radius.
- [The Escape Radius and the Green's Function](the-escape-radius-and-the-greens-function.html), for the classical object and its normalization.
- [The Biquaternion Holomorphic Dynamics and the Jacobian](the-biquaternion-holomorphic-dynamics-and-the-jacobian.html), for the Fatou set, the dynamical Julia set and the several definitions of the Julia set.
- [Square Roots of an Element](square-roots-of-a-general-element-in-the-biquaternion-algebra.html), for the four inverse branches of the square and the cone of roots of zero.
- [Several Complex Variables](several-complex-variables.html), for the plurisubharmonic tools and the several-variable theory the general case would need.
- [The Self-Similar Measure and the Invariant Measure](the-self-similar-measure-and-the-invariant-measure.html) and [Multifractal Analysis and the Legendre Transform](multifractal-analysis-and-the-legendre-transform.html), for the measure-theoretic statements of the category.
