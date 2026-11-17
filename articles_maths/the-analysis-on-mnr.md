# __The Analysis on $M_n(\mathbb{R})$__

## Introduction

**All norms on $M_n(\mathbb{R})$ are equivalent, the algebra is complete and the product is continuous, so the algebra is a Banach algebra; the analysis on it is the analysis of $n^{2}$ real variables with a multiplicative structure, and the multiplicative structure is what makes the calculus short.**

The article fixes the Euclidean and the operator norms, proves the Banach algebra inequality, proves that the determinant, the inverse and the characteristic polynomial are analytic and computes their derivatives, computes the radius of convergence of the exponential and the logarithm, and states the analytic functional calculus with real coefficients. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$*. It defers the group structure to *The Exponential and the Lie Group Structure of $\mathrm{GL}_n(\mathbb{R})$*.

## The Two Norms

**The Euclidean norm is the Hilbert–Schmidt norm, and it makes $M_n(\mathbb{R})$ isometric to $\mathbb{R}^{n^{2}}$.**

$$
\|X\|_{2}=\Bigl(\sum_{i,j}X_{ij}^{2}\Bigr)^{1/2}=\bigl(\operatorname{tr}(X^{\mathsf T}X)\bigr)^{1/2}.
$$

**The operator norm is the supremum on the unit sphere, and it is the norm that interacts with the product.**

$$
\|X\|_{\mathrm{op}}=\sup_{\|v\|=1}\|Xv\| .
$$

**Theorem.** $\|XY\|_{\mathrm{op}}\le\|X\|_{\mathrm{op}}\|Y\|_{\mathrm{op}}$, and $\|X\|_{\mathrm{op}}\le\|X\|_{2}\le\sqrt{n}\,\|X\|_{\mathrm{op}}$.

*Proof.* The first is immediate from the definition: $\|XYv\|\le\|X\|_{\mathrm{op}}\|Yv\|\le\|X\|_{\mathrm{op}}\|Y\|_{\mathrm{op}}$ on the unit sphere. The second: $\|X\|_{\mathrm{op}}^{2}$ is the largest eigenvalue of $X^{\mathsf T}X$, while $\|X\|_{2}^{2}$ is the trace of $X^{\mathsf T}X$, the sum of the $n$ eigenvalues; the largest is at most the sum and at least the sum divided by $n$.

**Theorem.** All norms on the finite-dimensional space $M_n(\mathbb{R})$ are equivalent.

*Proof.* The unit ball of any norm is compact, since the space is finite-dimensional and the norm is continuous, and the ratio of two norms is a continuous function on the compact unit sphere of either, hence bounded above and below by positive constants.

**Consequence: completeness and continuity.** $M_n(\mathbb{R})$ with any of these norms is a complete metric space, and the product is jointly continuous because it is bilinear and bounded. So every power series in the entries converges absolutely on its domain in the same way as the scalar series, and the algebra is a **Banach algebra**.

## The Determinant and the Inverse

**The determinant is a polynomial of degree $n$ in the entries, hence analytic everywhere.** It is the sum of $n!$ monomials, each of degree $n$ with sign. Its derivative at $X$ is

$$
d(\det)_{X}(H)=\det(X)\operatorname{tr}(X^{-1}H)\quad(X\ \text{invertible}),
$$

by Jacobi's formula, and at a singular $X$ the derivative is the cofactor matrix contracted with $H$.

**Theorem.** The map $X\mapsto X^{-1}$ is analytic on the open set $\mathrm{GL}_n(\mathbb{R})$, with derivative

$$
d(X^{-1})(H)=-X^{-1}HX^{-1}.
$$

*Proof.* Differentiate the identity $X(t)X(t)^{-1}=\mathrm{I}$ for the path $X(t)=X+tH$: $HX^{-1}+X\,d(X^{-1})(H)=0$, and solve.

**The determinant's zero set is the boundary of the group, and the group is open.** $\mathrm{GL}_n(\mathbb{R})=\{\det\ne0\}$ is the complement of a closed algebraic set, hence open and dense. The function $1/\det$ is analytic on it.

**The characteristic polynomial is analytic in the entries and polynomial in $t$.** Each coefficient $e_k$ is a sum of principal minors, hence a polynomial in the entries, so the map $X\mapsto\chi_X$ into the space of monic polynomials of degree $n$ is polynomial, and in particular continuous. This is the map whose fibres are the unions of similarity classes.

## The Exponential Series

**The series $\exp X=\sum_kX^{k}/k!$ converges for every $X$, and the convergence is locally uniform.** For $\|X\|_{\mathrm{op}}\le R$ the remainder after $N$ terms is bounded by $\sum_{k>N}R^{k}/k!$, which tends to zero uniformly, so the series converges normally on every ball.

**The bound $\|\exp X\|\le e^{\|X\|}$ follows from the triangle inequality and the submultiplicativity.** Hence $\exp$ is a continuous map from $M_n(\mathbb{R})$ to $M_n(\mathbb{R})$, and it is analytic, being a normally convergent series of polynomials.

**The exponential is a local diffeomorphism at $0$, with derivative the identity.** The derivative at $0$ in the direction $H$ is the linear term of the series, that is $H$. So by the inverse function theorem there is a neighbourhood $U$ of $0$ and a neighbourhood $V$ of $\mathrm{I}$ such that $\exp:U\to V$ is an analytic diffeomorphism.

**The inverse is the logarithm, and its radius of convergence is one.** For $\|Y-\mathrm{I}\|<1$,

$$
\log Y=\sum_{k\ge1}\frac{(-1)^{k-1}}{k}(Y-\mathrm{I})^{k},
$$

which converges absolutely and satisfies $\exp\log Y=Y$. The radius one is sharp: the series diverges at $Y=-2\mathrm{I}$, where no real logarithm exists at all.

**The two series are inverse only near the identity.** $\exp$ is not injective globally: $\exp(2\pi J)=\mathrm{I}$ at $n=2$, and $\exp$ is not surjective onto $\mathrm{GL}_n(\mathbb{R})^{+}$ either. Both failures are treated in *The Two Components of $\mathrm{GL}_n(\mathbb{R})$ and the Failure of the Exponential*.

## The Derivative of the Exponential

**The derivative of $\exp$ at $X$ in the direction $H$ is a series in the two matrices.**

$$
d(\exp)_X(H)=\sum_{k\ge1}\frac{1}{k!}\sum_{j=0}^{k-1}X^{j}HX^{k-1-j}=e^{X}\sum_{k\ge0}\frac{(-1)^{k}}{(k+1)!}\operatorname{ad}_X^{k}(H),
$$

the second form being valid when the series converges, for instance when $\|\operatorname{ad}_X\|<2\pi$. The operator in the middle is the **dexp** of the Lie theory.

**When $X$ and $H$ commute the derivative is $e^{X}H$.** The sum collapses because all the terms $X^{j}HX^{k-1-j}$ are equal to $X^{k-1}H$, and the result is the derivative of the scalar exponential along a commuting direction.

**When $X$ does not commute with $H$ the derivative differs from $e^{X}H$, and the difference is the first interesting term.** At $X=0$ the derivative is $H$; at $X$ small the correction begins with $\tfrac12[X,H]$.

**Consequence: the derivative of $\det\circ\exp$ is the trace.** Composing with $\det$ and using Jacobi's formula at $\mathrm{I}$,

$$
\frac{d}{dt}\Big|_{t=0}\det e^{tX}=\operatorname{tr}X,
$$

so $\det e^{X}=e^{\operatorname{tr}X}$, which is the multiplicative form of the statement that the trace is the logarithm of the determinant.

## Analytic Functions of a Matrix

**Definition.** For a real-analytic function $f$ defined on a neighbourhood of the spectrum of $X$ and real on the real points, $f(X)$ is defined by the Cauchy integral or, equivalently, by the interpolating polynomial on the distinct eigenvalues with the derivatives matched to the multiplicities.

**Theorem.** If $f(z)=\sum_kc_kz^{k}$ has radius of convergence greater than the spectral radius of $X$, then $f(X)=\sum_kc_kX^{k}$ converges and agrees with the definition above.

*Proof.* The power series converges in the operator norm once $\|X\|$ is below the radius, and the partial sums are polynomials. For a diagonalisable $X$ the identity is checked on the eigenvectors; for a general $X$ both sides are continuous in the entries and the diagonalisable matrices are dense.

**Consequence: the analytic functional calculus is a homomorphism on the algebra generated by $X$.** $(fg)(X)=f(X)g(X)$ and $f(g(X))=(f\circ g)(X)$ when the compositions are defined, so the map $f\mapsto f(X)$ is an algebra homomorphism from the analytic functions to the commutative algebra $\mathbb{R}[X]$.

**The coefficients must be real.** The point of the real category is that $f$ has real Taylor coefficients at the real points of its domain, so $f(X)$ is real for real $X$. The function $z\mapsto\sqrt{z}$ is analytic near a positive real number and not near a negative one, which is why the positive definite matrices have a real square root and the general invertible matrix need not.

## The Inverse Function Theorem in the Algebra

**The inverse function theorem applies to every analytic map between these spaces, and the algebra supplies examples.** For instance the map $X\mapsto X^{2}$ has derivative $H\mapsto XH+HX$ at $X$, which is invertible exactly when no two eigenvalues of $X$ sum to zero. So the square root is locally analytic near every matrix whose spectrum avoids pairs summing to zero, and it is not near $\operatorname{diag}(1,-1)$.

**The map $X\mapsto X^{\mathsf T}X$ has derivative $H\mapsto H^{\mathsf T}X+X^{\mathsf T}H$, and it is a local diffeomorphism between symmetric matrices and positive definite ones.** This is the local form of the polar decomposition.

**The map $X\mapsto\operatorname{tr}(X^{2})$ is a quadratic form of inertia $(n(n+1)/2,n(n-1)/2)$, and its critical points are the isotropic cone.** The gradient at $X$ is $2X$ with respect to the Hilbert–Schmidt form, so the only critical point is $0$, which is degenerate.

**A remark on rigour.** Every statement here is a definition, a computation with a norm, or an application of the inverse function theorem; none needs a completion or a spectral measure.

## Summary

$M_n(\mathbb{R})$ is a finite-dimensional Banach algebra, with the Hilbert–Schmidt norm giving the Euclidean structure and the operator norm the submultiplicative one. The determinant is a polynomial, the inverse is analytic on the open dense group with derivative $-X^{-1}HX^{-1}$, and the characteristic polynomial is a polynomial map. The exponential converges everywhere, is a local diffeomorphism at $0$ with derivative the identity, and its inverse is the logarithm with radius of convergence one. The derivative of the exponential is given by the dexp series, and $\det e^{X}=e^{\operatorname{tr}X}$. The analytic functional calculus is a homomorphism on $\mathbb{R}[X]$, with real coefficients, and it explains when a real square root or logarithm exists locally.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\|X\|_{2}$ | the Hilbert–Schmidt norm, $(\operatorname{tr}X^{\mathsf T}X)^{1/2}$ |
| $\|X\|_{\mathrm{op}}$ | the operator norm, the supremum on the unit sphere |
| $d(\exp)_X$ | the derivative of the exponential, the dexp series |
| $\operatorname{ad}_X(H)=[X,H]$ | the commutator operator |
| $\log Y$ | the series $\sum_k(-1)^{k-1}(Y-\mathrm{I})^{k}/k$, for $\|Y-\mathrm{I}\|<1$ |
| $f(X)$ | the analytic functional calculus |

## Further Reading

- Walter Rudin, *Functional Analysis* (McGraw-Hill, 1991), for Banach algebras, the exponential and the analytic functional calculus.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the norms, the derivatives and the logarithm.
- [The Exponential of a Real Matrix and Its Image](the-exponential-of-a-real-matrix-and-its-image.html), for the global behaviour of the exponential.
- [The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m3c.html), for the norms and the singular set at $n=3$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra and its trace form.
