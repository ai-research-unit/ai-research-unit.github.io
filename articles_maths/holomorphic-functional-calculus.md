
# __Holomorphic Functional Calculus__

## Introduction

The holomorphic functional calculus assigns to an element $a$ of a Banach algebra and a function $f$ holomorphic on a neighbourhood of the spectrum of $a$ an element $f(a)$ of the algebra, in such a way that the assignment is an algebra homomorphism, is continuous, and carries the constant function $1$ to the identity and the function $\lambda$ to $a$. The construction is the Cauchy integral

$$
f(a) = \frac{1}{2\pi i}\oint_\Gamma f(\lambda)\,(\lambda 1-a)^{-1}\,d\lambda ,
$$

taken along a contour that surrounds the spectrum and avoids it; the integral converges because the resolvent is bounded on the contour and $f$ is continuous there, and the value is independent of the contour because the resolvent is analytic away from the spectrum and the integrand is exact there. The calculus is the analytic form of the statement that a Banach algebra knows its elements through their spectra: everything that a holomorphic function of the complex variable can do to a number, it can do to an element of the algebra.

The article develops the calculus for the general unital complex Banach algebra and then for the algebra of bounded operators on a Banach space, where it becomes the **Dunford calculus**, with the **Riesz projections** on the parts of the spectrum and the invariant decomposition of the space that they produce. The spectral theory itself — the spectrum, the resolvent, the spectral radius, the Gelfand transform and the theory of commutative Banach algebras — is *Topological Algebras and Banach Algebras* and *Operator Algebras*, quoted here; the theory of an unbounded self-adjoint operator, its spectral measure and the Borel calculus is *Unbounded Operators and Spectral Measures*, and is cited where the holomorphic calculus meets it. What the article adds to those is the calculus: the construction, its algebraic and continuity properties, the spectral mapping theorem, the composition rule, the Riesz projection and the applications that make the calculus a working tool — the logarithm and the square root of an element, the matrix case and its interpolation description, Wiener's theorem for the algebra of absolutely convergent Fourier series, and the agreement of the holomorphic calculus with the continuous one for normal operators.

The base field is $\mathbb{C}$ throughout, and the algebras have an identity $1\neq0$; the non-unital case is a limiting case that is stated in a Remark. The characteristic of the field is zero, so that the binomial and exponential manipulations below are legitimate, and the algebras are complete, so that the contour integrals converge. These hypotheses are those of *Topological Algebras and Banach Algebras*.

## The Calculus on a Banach Algebra

### The Resolvent

Let $A$ be a unital complex Banach algebra, with norm submultiplicative, $\|xy\|\le\|x\|\|y\|$, and complete. For $a\in A$ the **spectrum** is

$$
\sigma(a) = \{\lambda\in\mathbb{C} : a-\lambda1\ \text{is not invertible in } A\} ,
$$

a compact nonempty subset of the disc $\{|\lambda|\le\|a\|\}$, and the **resolvent set** $\rho(a)=\mathbb{C}\setminus\sigma(a)$ is open. The **resolvent** is the $A$-valued function

$$
R(\lambda) = (\lambda 1-a)^{-1} , \qquad \lambda\in\rho(a) .
$$

**Proposition (properties of the resolvent).** The resolvent is analytic on $\rho(a)$ and satisfies

$$
R(\lambda)-R(\mu) = (\lambda-\mu)R(\lambda)R(\mu) , \qquad \|R(\lambda)\|\le\frac{1}{|\lambda|-\|a\|}\ \ (|\lambda|>\|a\|) .
$$

In particular $\|R(\lambda)\|\to0$ as $|\lambda|\to\infty$, so $R$ is bounded on every contour lying outside a disc containing the spectrum.

*Proof.* The resolvent identity follows by multiplying the identity $(\lambda-a)-(\mu-a)=(\lambda-\mu)$ on both sides by $R(\lambda)$ and $R(\mu)$; it exhibits the resolvent as continuous, and dividing by $\lambda-\mu$ gives its analyticity. The estimate follows from the Neumann series $R(\lambda)=-\lambda^{-1}\sum_{n\ge0}(a/\lambda)^n$. $\square$

### The Definition

Let $f$ be holomorphic on an open set $U\supseteq\sigma(a)$, and let $\Gamma$ be a finite union of positively oriented simple closed curves in $U\cap\rho(a)$, disjoint and with $\sigma(a)$ in the interior of $\Gamma$; such a contour exists because $\sigma(a)$ is compact and $U\cap\rho(a)$ is an open neighbourhood of it.

**Definition.** The **holomorphic functional calculus** of $a$ is

$$
f(a) = \frac{1}{2\pi i}\oint_\Gamma f(\lambda)\,R(\lambda)\,d\lambda ,
$$

the integral of a continuous $A$-valued function on a compact contour.

**Proposition (well-definedness).** The integral does not depend on the contour $\Gamma$: for two admissible contours the difference of the integrals is the integral of the analytic $A$-valued function $f(\lambda)R(\lambda)$ over the boundary of a region on which it is analytic, and it vanishes by Cauchy's theorem.

*Proof.* On the region between the two contours the integrand is analytic, since $f$ is holomorphic on $U$ and $R$ on $\rho(a)$; Cauchy's theorem for vector-valued analytic functions (the scalar theorem applied to each continuous linear functional) gives the vanishing. $\square$

**Theorem (the calculus is a continuous homomorphism).** The map $f\mapsto f(a)$ from the algebra of germs of functions holomorphic on neighbourhoods of $\sigma(a)$ to $A$ is a unital algebra homomorphism: $(f+g)(a)=f(a)+g(a)$, $(fg)(a)=f(a)g(a)$, $1(a)=1$, $\lambda(a)=a$; it is continuous with respect to uniform convergence on neighbourhoods of $\sigma(a)$.

*Proof.* Linearity is immediate from the linearity of the integral. For the product, use the resolvent identity and the identity $R(\lambda)R(\mu)=(\lambda-\mu)^{-1}(R(\mu)-R(\lambda))$ for $\lambda\neq\mu$ to reduce the double contour integral of $f(\lambda)g(\mu)R(\lambda)R(\mu)$ to the sum of the two integrals representing $f(a)g(a)$ and $g(a)f(a)$; the function $(\lambda-\mu)^{-1}$ has poles only on the diagonals $\lambda=\mu$, which the contours avoid. The constants are immediate: $1(a)=\frac{1}{2\pi i}\oint\Gamma R(\lambda)d\lambda=1$, and $\lambda(a)=\frac{1}{2\pi i}\oint\Gamma\lambda R(\lambda)d\lambda=a$. Continuity follows from the estimate $\|f(a)\|\le\frac{1}{2\pi}\ell(\Gamma)\max_\Gamma|f|\|R\|$. $\square$

**Theorem (spectral mapping).** For every $f$ holomorphic on a neighbourhood of $\sigma(a)$,

$$
\sigma\bigl(f(a)\bigr) = f\bigl(\sigma(a)\bigr) .
$$

*Proof.* Quoted as standard. One direction is elementary: if $\mu=f(\lambda_0)$ for some $\lambda_0\in\sigma(a)$, write $f(\lambda)-f(\lambda_0)=(\lambda-\lambda_0)g(\lambda)$ with $g$ holomorphic, so $f(a)-f(\lambda_0)1=(a-\lambda_01)g(a)$, and since $a-\lambda_01$ is not invertible neither is $f(a)-\mu1$. The other direction uses the calculus applied to the function $1/(f(\lambda)-\mu)$ when $\mu\notin f(\sigma(a))$. $\square$

**Corollary (invertibility criterion).** If $f$ has no zero on $\sigma(a)$ then $f(a)$ is invertible, with $f(a)^{-1}=(1/f)(a)$; conversely an invertible $f(a)$ forces $f$ to be zero-free on $\sigma(a)$.

**Corollary (spectral radius).** The spectral radius is

$$
r(a) = \max_{\lambda\in\sigma(a)}|\lambda| = \lim_{n\to\infty}\|a^n\|^{1/n} ,
$$

the Gelfand formula; the limit exists and equals the maximum by the spectral mapping theorem applied to the function $\lambda\mapsto\lambda^n$ and the standard estimate $r(a)\le\|a\|$.

**Theorem (composition and locality).** If $g$ is holomorphic on a neighbourhood of $\sigma(a)$ and $f$ holomorphic on a neighbourhood of $g(\sigma(a))$, then $(f\circ g)(a)=f(g(a))$. If $f=g$ on a neighbourhood of $\sigma(a)$, then $f(a)=g(a)$. The calculus is **natural**: for every continuous unital algebra homomorphism $\pi:A\to B$ one has $\pi(f(a))=f(\pi(a))$, the spectrum of $\pi(a)$ being contained in that of $a$.

*Proof.* Locality is immediate from the definition, since the integral sees $f$ only on $\Gamma$. Naturality follows because $\pi$ intertwines the resolvents, $\pi(R_a(\lambda))=R_{\pi(a)}(\lambda)$, and commutes with the Bochner integral. The composition rule is the Runge approximation argument: $(f\circ g)(a)$ and $f(g(a))$ are both continuous in the data and agree when $f$ is a polynomial, and polynomials are dense in the holomorphic functions on a neighbourhood of $g(\sigma(a))$ by Runge's theorem. $\square$

**Remark (the non-unital case).** In a non-unital Banach algebra, or for a function that does not vanish at infinity, one adjoins an identity and applies the calculus to the unitisation; the resulting calculus assigns to $f$ an element of the unitisation, and the holomorphic functions that vanish at infinity act on the original algebra. The distinction is the one between the algebra and its unitisation, and it is the only modification the non-unital case requires.

## The Riesz Projection and Spectral Decomposition

**Definition.** Let $\sigma(a)$ be the disjoint union of a compact set $\sigma_1$ and its complement in $\sigma(a)$, and suppose $\sigma_1$ is separated from the rest by a contour $\Gamma_1$ in $\rho(a)$. The **Riesz projection** of $a$ onto $\sigma_1$ is

$$
P_1 = \frac{1}{2\pi i}\oint_{\Gamma_1}R(\lambda)\,d\lambda .
$$

**Theorem (properties of the Riesz projection).** With the notation above, $P_1$ is an idempotent of $A$; it commutes with $a$; it is the value at $a$ of any function holomorphic near $\sigma(a)$ that equals $1$ on a neighbourhood of $\sigma_1$ and $0$ on a neighbourhood of the rest of the spectrum. Its image $P_1A$ and its kernel $(1-P_1)A$ are closed subspaces invariant under $a$, and

$$
\sigma(a|_{P_1A})=\sigma_1 , \qquad \sigma(a|_{(1-P_1)A})=\sigma(a)\setminus\sigma_1 .
$$

*Proof.* Idempotency follows from the calculus applied to the indicator-type function: $P_1=f(a)$ for $f$ the function described, and $f^2=f$ on a neighbourhood of the spectrum, so $P_1^2=f(a)^2=(f^2)(a)=f(a)=P_1$ by the homomorphism property and locality. Commutation with $a$ follows from the resolvent identity. The image and kernel are closed because $P_1$ is a bounded projection, invariant because $a$ commutes with $P_1$, and the spectra are computed by the spectral mapping theorem applied to the restriction. $\square$

**Corollary (the operator case).** Let $T$ be a bounded operator on a complex Banach space $X$ and let $\sigma(T)=\sigma_1\sqcup\sigma_2$ with $\sigma_1$ compact and separated. Then

$$
X = \ker P_1\oplus\operatorname{im}P_1 = X_2\oplus X_1 ,
$$

each summand is $T$-invariant, $T$ restricted to $X_i$ has spectrum $\sigma_i$, and $T$ is block diagonal with respect to this decomposition. Iterating the construction over the connected components of the spectrum gives the **Dunford decomposition** of $T$ into the parts of the spectrum, and if the spectrum is finite the decomposition is into finitely many invariant pieces.

*Proof.* Apply the theorem to the algebra $B(X)$ of bounded operators; the image and kernel of an idempotent operator are closed complementary subspaces, and the spectrum statements are those of the theorem. $\square$

**Remark (the calculus and the spectral theorem).** For $T$ normal on a Hilbert space, the holomorphic calculus is a homomorphism from the analytic functions on a neighbourhood of $\sigma(T)$ into the algebra generated by $T$, and the continuous functional calculus of *Operator Algebras* extends it to all continuous functions on the spectrum through the spectral measure; the two agree on the holomorphic functions, since both are continuous homomorphisms sending $\lambda$ to $T$ and determined by that property on polynomials, and polynomials are dense. The Borel calculus of *Unbounded Operators and Spectral Measures* is the further extension to bounded Borel functions, and the holomorphic calculus is then the smallest of the three: analytic, continuous, Borel.

## Applications

### The Exponential, the Logarithm and the Square Root

**Proposition (entire functions).** If $f(\lambda)=\sum_{n\ge0}c_n\lambda^n$ is entire, then the series $\sum_nc_na^n$ converges in $A$ and its sum is $f(a)$; hence the calculus for entire functions is the substitution of $a$ into the power series.

*Proof.* The series converges absolutely because $f$ has infinite radius of convergence and $\|a^n\|\le\|a\|^n$; the integral defining $f(a)$ can be expanded as the uniformly convergent sum of the integrals of $c_n\lambda^nR(\lambda)$, and each of those is $c_na^n$ by the resolvent expansion. $\square$

**Proposition (the logarithm).** Let $a\in A$ and suppose $\sigma(a)$ is contained in a simply connected open set $U\subseteq\mathbb{C}\setminus\{0\}$. Then there exists $b\in A$ with $e^b=a$; if $\sigma(a)\subset\{|\lambda-1|<1\}$ then $b=\log a$ is given by the series $\sum_{n\ge1}(-1)^{n+1}(a-1)^n/n$.

*Proof.* Let $g$ be a holomorphic branch of the logarithm on $U$; set $b=g(a)$. Then $\exp(g(\lambda))=\lambda$ on a neighbourhood of $\sigma(a)$, so by the composition rule $e^b=(e^{\,\cdot}\circ g)(a)=\lambda(a)=a$. The series statement is the principal branch and the power-series case of the preceding proposition. $\square$

**Proposition (the square root).** If $0\notin\sigma(a)$ and the spectrum lies in a simply connected set avoiding $0$, then $a$ has a square root in the closed subalgebra generated by $1$ and $a$, namely $f(a)$ for a holomorphic branch $f(\lambda)=\lambda^{1/2}$. If in addition $\sigma(a)\subset(0,\infty)$ then the square root is the limit of the Newton iteration and is a function of $a$ in the strong sense.

*Proof.* The branch $f$ is holomorphic on the domain and $f^2=\lambda$, so $f(a)^2=(f^2)(a)=\lambda(a)=a$ by the homomorphism property. $\square$

### The Matrix Case

**Example ($A=M_n(\mathbb{C})$).** For a matrix $a$, the calculus computes $f(a)$ through the Jordan form: if $a=S(J\oplus J'\oplus\cdots)S^{-1}$ with Jordan blocks $J$, then $f(a)=S(f(J)\oplus f(J')\oplus\cdots)S^{-1}$, where $f(J)$ is the Toeplitz (upper triangular) matrix with $f(\lambda_0),f'(\lambda_0),\frac{1}{2!}f''(\lambda_0),\dots$ along its diagonals at the eigenvalue $\lambda_0$ of the block. Equivalently, $f(a)$ is the value at $a$ of the Hermite interpolating polynomial of $f$ at the spectrum, with the derivatives up to the algebraic multiplicities as data; the calculus is therefore determined by finitely many values of $f$ and its derivatives, and it is the unique continuous calculus with this property.

**Example (nilpotents).** For a nilpotent $n$ with $n^k=0$, the entire-function rule gives $f(n)=\sum_{j=0}^{k-1}\frac{f^{(j)}(0)}{j!}n^j$, a polynomial in $n$ of degree $<k$; in particular $e^n$ is this finite sum, and $(1+n)^{1/2}$ is its binomial expansion, which terminates. This is the finite-dimensional shadow of the general rule that an entire function of a quasinilpotent element is not necessarily the naive series unless the series is finite.

### The Group Algebra and Wiener's Theorem

**Example ($A=\ell^1(\mathbb{Z})$).** Let $A$ be the Banach algebra of absolutely convergent Fourier series on the circle, with convolution product; its Gelfand transform is the map $\hat{\ }:\ell^1(\mathbb{Z})\to C(\mathbb{T})$ sending a coefficient sequence to its sum, with the sup norm on the circle, and $\widehat{a*b}=\hat a\hat b$. The Gelfand transform is a continuous unital algebra homomorphism, so by naturality

$$
\widehat{f(a)} = f(\hat a)
$$

for every $f$ holomorphic on a neighbourhood of $\sigma(a)=\hat a(\mathbb{T})$. Two classical consequences follow in one line. **Wiener's theorem**: if $a\in\ell^1(\mathbb{Z})$ has $\hat a$ nowhere zero, then $a$ is invertible in $\ell^1(\mathbb{Z})$, with $\widehat{a^{-1}}=1/\hat a$; for $0\notin\sigma(a)=\hat a(\mathbb{T})$ and $1/\lambda$ is holomorphic on a neighbourhood of the spectrum, so $(1/\lambda)(a)$ is the inverse. **The Wiener–Lévy theorem**: if $f$ is holomorphic on a neighbourhood of the range $\hat a(\mathbb{T})$, then $f\circ\hat a$ is again the Gelfand transform of an element of $\ell^1(\mathbb{Z})$, namely of $f(a)$. The two statements are the standard illustration that the calculus converts a problem about a concrete class of series into the spectral mapping theorem for a Banach algebra.

**Remark (commutative algebras).** In a commutative unital complex Banach algebra the calculus is compatible with the Gelfand transform, as the example shows, and its image lies in the closed subalgebra generated by $a$; the spectral mapping theorem then reproves the invertibility criterion of the Gelfand theory and the openness of the set of invertible elements. The Gelfand theory and the maximal ideal space are *Topological Algebras and Banach Algebras*.

### Operators and the Dunford Calculus

**Example (bounded operators).** For $A=B(X)$ the calculus is the **Dunford calculus**: for $T\in B(X)$ and $f$ holomorphic on a neighbourhood of $\sigma(T)$, the operator $f(T)=\frac{1}{2\pi i}\oint_\Gamma f(\lambda)(\lambda I-T)^{-1}d\lambda$ acts on $X$, commutes with $T$, and satisfies the spectral mapping theorem $\sigma(f(T))=f(\sigma(T))$; the Riesz projections of the preceding section are the functions of $T$ attached to the parts of the spectrum. Two consequences are used constantly: the invariant-subspace decomposition of $T$ into its spectral parts, and the existence of a logarithm or a square root of $T$ when the spectrum avoids $0$ and is simply connected.

**Remark (several variables).** The calculus extends to several commuting elements $a_1,\dots,a_n$ of a Banach algebra: the spectrum is then a compact subset of $\mathbb{C}^n$, and the integral is taken over a cycle in the complement of the joint spectrum, the result being the **Taylor–Shilov calculus**. The one-variable calculus is the case $n=1$, and the several-variable case requires the holomorphic functional calculus of several variables and the theory of the joint spectrum, which is standard; it is mentioned here only to record that the construction is not essentially one-dimensional.

## Summary

The holomorphic functional calculus of an element $a$ of a unital complex Banach algebra assigns to a function $f$ holomorphic on a neighbourhood of the spectrum $\sigma(a)$ the element $f(a)=\frac{1}{2\pi i}\oint_\Gamma f(\lambda)(\lambda1-a)^{-1}d\lambda$, the value being independent of the contour because the resolvent is analytic off the spectrum. The assignment is a unital, continuous algebra homomorphism, natural with respect to continuous algebra homomorphisms and local in $f$; the spectral mapping theorem $\sigma(f(a))=f(\sigma(a))$ holds, the composition rule $(f\circ g)(a)=f(g(a))$ holds, and the spectral radius is $\max|\sigma(a)|=\lim\|a^n\|^{1/n}$. The **Riesz projection** $P_1=\frac{1}{2\pi i}\oint_{\Gamma_1}R(\lambda)d\lambda$ attached to an isolated part of the spectrum is an idempotent commuting with $a$, the space decomposes as $\ker P_1\oplus\operatorname{im}P_1$ into invariant pieces carrying the two parts of the spectrum, and iterating gives the Dunford decomposition of a bounded operator. The calculus yields the exponential of any element, the logarithm and the square root under the stated spectral hypotheses, and for entire functions it coincides with the substitution into the power series. For matrices it is the Hermite interpolation of $f$ at the spectrum with the Jordan structure; for the algebra of absolutely convergent Fourier series, naturality of the calculus together with the Gelfand transform gives Wiener's theorem and the Wiener–Lévy theorem. For a normal operator the holomorphic calculus is the restriction of the continuous functional calculus, which is in turn the restriction of the Borel calculus; the spectral theory, the Gelfand theory and the Borel calculus belong to *Topological Algebras and Banach Algebras*, *Operator Algebras* and *Unbounded Operators and Spectral Measures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Unital complex Banach algebra |
| $a$, $1$ | Element of $A$ and the identity |
| $\sigma(a)$, $\rho(a)$ | Spectrum and resolvent set of $a$ |
| $R(\lambda)=(\lambda1-a)^{-1}$ | Resolvent |
| $\Gamma$ | Admissible contour around $\sigma(a)$ |
| $f(a)=\frac{1}{2\pi i}\oint_\Gamma fR\,d\lambda$ | Holomorphic functional calculus |
| $r(a)=\max|\sigma(a)|$ | Spectral radius |
| $P_1$ | Riesz projection onto an isolated spectral part |
| $X_1\oplus X_2$ | Invariant spectral decomposition of a Banach space |
| $\hat a$ | Gelfand transform |
| $\ell^1(\mathbb{Z})$ | Algebra of absolutely convergent Fourier series |
| $f(T)$ | Dunford calculus for a bounded operator |

## Further Reading

- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I: General Theory* (Interscience, 1958), for the Dunford calculus, the Riesz projection and spectral decomposition.
- Walter Rudin, *Functional Analysis*, 2nd ed. (McGraw–Hill, 1991), for the holomorphic functional calculus in a Banach algebra and its applications.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the calculus in the general Banach-algebra setting and the Gelfand theory.
- John B. Conway, *A Course in Functional Analysis*, 2nd ed. (Springer, 1990), for the spectral theory of bounded operators and the functional calculus.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the analytic calculus, the spectral projections and their stability under perturbation.
- Frigyes Riesz and Béla Sz.-Nagy, *Functional Analysis* (Dover reprint, 1990), for the Riesz projection and the classical spectral decomposition.
- Norbert Wiener, "Tauberian Theorems", *Annals of Mathematics* 33 (1932), 1–100, for the theorem on absolutely convergent Fourier series that the calculus proves.
- Joseph L. Taylor, "A Joint Spectrum for Several Commuting Operators", *Journal of Functional Analysis* 6 (1970), 172–191, for the several-variable extension of the calculus.
