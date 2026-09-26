
# __Analytic Number Theory__

## Introduction

Analytic number theory is the study of the integers by the methods of complex analysis. The bridge between the two subjects is the Euler product: the identity $\zeta(s) = \prod_p(1-p^{-s})^{-1}$, valid for $\Re s>1$, converts a statement about the distribution of the primes into a statement about the singularities and the zeros of a meromorphic function, and the whole of the classical theory is the exploitation of that conversion. The mechanism is exact and it is the following: the logarithmic derivative $-\zeta'(s)/\zeta(s)$ is the Dirichlet series $\sum_n\Lambda(n)n^{-s}$ of the von Mangoldt function, the partial sums of that series are the Chebyshev function $\psi(x)$, and Cauchy's formula applied to the logarithmic derivative expresses $\psi(x)$ as a contour integral whose main term comes from the pole of $\zeta$ at $s=1$ and whose error term is a sum over the zeros of $\zeta$. Every quantitative theorem about the distribution of the primes is a statement about that sum.

This article develops the machinery. It defines the arithmetic functions of the classical theory, proves the equivalences between the several ways of stating the prime number theorem, records the Mertens estimates and the Chebyshev bounds, proves Perron's formula and the explicit formula of von Mangoldt, states the Riemann–von Mangoldt zero-counting formula and the zero-free region of de la Vallée Pouss, and treats the distribution of the primes in arithmetic progressions with the theorems of Dirichlet, Siegel–Walfisz, Bombieri–Vinogradov and Linnik. It closes with the other methods of the subject: the sieve, in the forms of Brun and Selberg with the parity phenomenon, and the circle method of Hardy–Littlewood and Vinogradov. The final assembly — the analytic proof of the prime number theorem from the zero-free region, and the consequences of the hypothesis that all the nontrivial zeros lie on the critical line — belong andwritten in parallel; the zeta and $L$-functions that are analysed here are those of *Zeta Functions* and *L-Functions*, written above it.

The analytic facts used from the theory of one complex variable — Cauchy's theorem, the residue calculus, the Phragmén–Lindelöf principle, the Hadamard factorisation of entire functions of finite order and the Stirling estimate for the Gamma function — are standard mathematics, and are cited to the standard literature rather than developed; the per-system development of that theory is the subject of the synthetic studyin which the number system is fixed, and it is deferred to it. The prerequisites are *Zeta Functions* for the Riemann and Dedekind zeta functions, their Euler products, their functional equations and Landau's theorem, *L-Functions* for the Dirichlet characters, the Dirichlet $L$-functions and their nonvanishing at $1$, *Measure Theory and Integration* for the interchange of limits, *Absolute Values, Valuations and Completions* for the local computations, and *Algebraic Number Theory* and *Rings* for the arithmetic. Throughout, $p$ denotes a prime, $\pi(x)$ the number of primes $\leq x$, $\psi(x)$ and $\theta(x)$ the Chebyshev functions, $\Lambda$ the von Mangoldt function, $\mu$ the Möbius function and $\varphi$ the Euler function; $\rho = \beta + i\gamma$ runs over the nontrivial zeros of the zeta function, and $N(T)$ counts those with $0<\gamma\leq T$. The notation of *Zeta Functions* is used without restatement.

## Arithmetic Functions and Summation

### The Classical Functions

**Definition.** The **von Mangoldt function** is $\Lambda(n) = \log p$ if $n$ is a positive power of the prime $p$ and $0$ otherwise; the **Möbius function** is $\mu(n) = (-1)^k$ if $n$ is a product of $k$ distinct primes and $0$ if $n$ is divisible by a square; the **Chebyshev functions** are
$$
\theta(x) = \sum_{p\leq x}\log p, \qquad \psi(x) = \sum_{n\leq x}\Lambda(n) = \sum_{p^k\leq x}\log p .
$$
**Proposition (the logarithmic derivative and the Euler product).** For $\Re s>1$,
$$
\sum_{n\geq1}\frac{\Lambda(n)}{n^s} = -\frac{\zeta'(s)}{\zeta(s)}, \qquad
\sum_{n\geq1}\frac{\mu(n)}{n^s} = \frac{1}{\zeta(s)}, \qquad
\sum_{n\geq1}\frac{\varphi(n)}{n^s} = \frac{\zeta(s-1)}{\zeta(s)},
$$
and the corresponding Euler products converge absolutely and locally uniformly in the half-plane.

**Proof.** The second and third identities are the multiplicative convolutions $\mu * 1 = \varepsilon$ and $\varphi * 1 = \mathrm{id}$, expanded as Dirichlet series; the first is obtained by taking the logarithmic derivative of the Euler product, term by term. $\square$

**Theorem (Abel summation).** Let $a_n$ be a sequence and $A(x) = \sum_{n\leq x}a_n$. For a continuously differentiable $f$ on $[1,x]$,
$$
\sum_{n\leq x}a_nf(n) = A(x)f(x) - \int_1^x A(t)f'(t)\,dt .
$$
**Proof.** Integration by parts on the Stieltjes integral $\int_{1^-}^x f(t)\,dA(t)$, or summation by parts. $\square$

**Theorem (Mertens).** As $x\to\infty$,
$$
\sum_{p\leq x}\frac{\log p}{p} = \log x + O(1), \qquad \prod_{p\leq x}\Bigl(1-\frac1p\Bigr) = \frac{e^{-\gamma}}{\log x}\bigl(1+o(1)\bigr), \qquad \sum_{p\leq x}\frac1p = \log\log x + M + o(1),
$$
where $\gamma$ is Euler's constant and $M$ is the Mertens constant.

**Proof sketch.** The first estimate is Abel summation applied to the Chebyshev bounds for $\psi$ of the next section; the second is the logarithm of the product, expressed as $-\sum_p\log(1-1/p) = \sum_p1/p + O(1)$, combined with the first and with the divergence of $\sum 1/p$; the third refines the same computation with one further term, and the constant is the limit of $\sum_{p\le x}1/p - \log\log x$. $\square$

### Equivalent Forms of the Prime Number Theorem

**Theorem.** The following statements are equivalent.

**(a)** $\pi(x)\sim \dfrac{x}{\log x}$;

**(b)** $\psi(x)\sim x$;

**(c)** $\theta(x)\sim x$;

**(d)** $p_n\sim n\log n$, where $p_n$ is the $n$-th prime;

**(e)** $\sum_{n\leq x}\Lambda(n) = x + o(x)$.

**Proof.** That (b) and (e) are the same statement is the definition. For (b) implies (c): $\psi(x) = \theta(x) + \theta(x^{1/2}) + \theta(x^{1/3})+\dots$ and the sum of the higher terms is $O(x^{1/2}\log x)=o(x)$, while $\psi(x)\geq\theta(x)$. For the equivalence of (a) and (c), Abel summation with the indicator of the primes as the coefficients gives the two identities
$$
\theta(x) = \pi(x)\log x - \int_2^x\frac{\pi(t)}{t}\,dt, \qquad \pi(x) = \frac{\theta(x)}{\log x} + \int_2^x\frac{\theta(t)}{t\log^2t}\,dt ;
$$
if $\pi(x)\sim x/\log x$ then the integral in the first is $(1+o(1))x/\log x$, so $\theta(x)\sim x$; if $\theta(x)\sim x$ then the integral in the second is $o(x/\log x)$, so $\pi(x)\sim x/\log x$. The equivalence with (d) is the substitution $x = p_n$, since $\pi(p_n) = n$. $\square$

**Theorem (Chebyshev's bounds; Bertrand's postulate).** There are constants $0<c_1<c_2$ with
$$
c_1x \leq \psi(x) \leq c_2 x \qquad (x \geq 2),
$$
and consequently for every $n$ there is a prime between $n$ and $2n$.

**Proof sketch.** The upper bound follows by writing $\log\lfloor x\rfloor!$ in two ways and comparing the multiplicities of $p$ in $\binom{2n}{n}$, which gives $\theta(x)\ll x$; the lower bound uses the central binomial coefficient to show that the product of the primes between $n$ and $2n$ is large, whence a prime occurs in each dyadic interval. $\square$

## Perron's Formula and the Explicit Formula

### Perron's Formula

**Theorem (Perron).** Let $F(s) = \sum_{n\geq1}a_nn^{-s}$ converge absolutely for $\Re s>\sigma_a$, and let $c>\max(0,\sigma_a)$. For $x>0$ not an integer,
$$
\sum_{n\leq x}a_n = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}F(s)\,\frac{x^s}{s}\,ds ,
$$
the integral taken over the vertical line and interpreted as the limit of the integrals over the segments $\lvert t\rvert\leq T$. If $x$ is an integer, the right side is the sum with the last term halved.

**Proof sketch.** The integral converges absolutely by the (trivial) boundedness of $F$ on the line $\Re s = c$; interchanging the integral and the sum, the inner integral $\frac{1}{2\pi i}\int x^s n^{-s}ds/s$ is the inverse Mellin transform of $s^{-1}$, equal to $1$ if $n<x$ and $0$ if $n>x$ (with the value $\tfrac12$ at $n=x$). The interchange is justified by absolute convergence, and the truncation is controlled by the tail estimate for the Dirichlet kernel. $\square$

**Corollary (the truncated Perron formula).** With the notation above, for $x\geq2$ and $T\geq1$ the difference between the sum and the truncated integral is $O\bigl(\sum_n\lvert a_n\rvert n^{-c}\min(1,\frac{n}{T\lvert x-n\rvert})\bigr) + O(\lvert a_x\rvert/T)$, so that the error depends only on the size of the coefficients near $x$.

### The Explicit Formula

**Theorem (von Mangoldt's explicit formula).** For $x>1$ not a prime power,
$$
\psi(x) = x - \sum_{\rho}\frac{x^{\rho}}{\rho} - \log 2\pi - \frac12\log\bigl(1-x^{-2}\bigr),
$$
the sum being taken over the nontrivial zeros of $\zeta$ in the sense of the symmetric limit $\lim_{T\to\infty}\sum_{\lvert\gamma\rvert\leq T}$, which converges.

**Proof sketch.** Apply Perron's formula to $-\zeta'/\zeta$ for $c>1$, and shift the contour to the line $\Re s = -\tfrac12$, picking up the residue at the pole $s=1$ (giving $x$), the residues at the nontrivial zeros $\rho$ (giving $-x^\rho/\rho$), the pole at $s=0$ from the factor $1/s$ together with the value of $\zeta'/\zeta$ there (giving $-\log2\pi$), and the trivial zeros at the negative even integers (giving the logarithmic term). The shift is justified by the standard bounds for $\zeta'/\zeta$ in the critical strip. $\square$

**Theorem (Riemann–von Mangoldt).** The number of nontrivial zeros with $0<\gamma\leq T$ satisfies
$$
N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + O(\log T),
$$
so the zeros have density $\frac{1}{2\pi}\log\frac{T}{2\pi}$ near height $T$; in particular infinitely many nontrivial zeros exist, and $\sum_\rho1/\lvert\rho\rvert^{1+\epsilon}$ converges for every $\epsilon>0$ while $\sum_\rho1/\lvert\rho\rvert$ diverges.

**Proof sketch.** The argument principle applied to $\xi$, the completed zeta function of *Zeta Functions* which is entire of order $1$ and real on the critical line, expresses $N(T)$ as the variation of the argument of $\xi$ along the boundary of the rectangle; the variation along the horizontal sides is $O(\log T)$ by the functional equation and the Stirling estimate for the Gamma factor, and the vertical sides contribute the main term. The convergence statement is the standard consequence of the density. $\square$

### The Zero-Free Region

**Theorem (de la Vallée Poussin).** There is a constant $c>0$ such that
$$
\zeta(\sigma+it) \neq 0 \qquad \text{for } \sigma > 1 - \frac{c}{\log(\lvert t\rvert + 2)} .
$$
Consequently $\zeta$ has no zero on the line $\Re s = 1$, the logarithmic derivative $-\zeta'/\zeta$ is bounded in a region to the left of that line apart from the pole at $s=1$, and the explicit formula yields
$$
\psi(x) = x + O\bigl(x\exp(-c'\sqrt{\log x})\bigr)
$$
for a positive constant $c'$; in particular $\pi(x)\sim x/\log x$.

**Proof sketch.** The nonvanishing is deduced from the inequality $3 + 4\cos\theta + \cos2\theta\geq0$ applied to the logarithm of $\zeta$ on the line $\Re s = 1+\epsilon$: with $s = \sigma+it$, $\log\lvert\zeta(\sigma)\rvert + 4\log\lvert\zeta(\sigma+it)\rvert + \log\lvert\zeta(\sigma+2it)\rvert \geq 0$ for $\sigma>1$, and the pole of $\zeta$ at $1$ bounds $\log\lvert\zeta(\sigma)\rvert$ from below by $-\log(\sigma-1)+O(1)$; a zero at $\beta+i\gamma$ with $\beta$ too close to $1$ would make the middle term too negative. The error term follows by inserting the region into the explicit formula and estimating the sum over the zeros; the final statement is the prime number theorem, and the full proof of that theorem is not covered here. $\square$

## Primes in Arithmetic Progressions

**Definition.** For $(a,q)=1$ let $\pi(x;q,a)$ be the number of primes $p\leq x$ with $p\equiv a \pmod q$, and let $\mathrm{Li}(x) = \int_2^x dt/\log t$.

**Theorem (Dirichlet).** For every $a$ with $(a,q)=1$ the progression $a \bmod q$ contains infinitely many primes; more precisely
$$
\pi(x;q,a) \sim \frac{1}{\varphi(q)}\frac{x}{\log x} \qquad (x\to\infty,\ q \text{ fixed}).
$$
**Proof sketch.** The first statement is the nonvanishing $L(1,\chi)\neq0$ of *L-Functions* together with the orthogonality relations, which write the sum over the primes in the progression as an average of the logarithmic derivatives of the $L$-functions $L(s,\chi)$; the asymptotic follows by the same argument with the residue of the pole at $s=1$ of the principal term, which is $\frac1{\varphi(q)}$ times the residue of $\zeta$. $\square$

**Theorem (Siegel–Walfisz).** For every $A>0$ there is a constant $c_A>0$, ineffective because it depends on a possible exceptional zero, such that
$$
\pi(x;q,a) = \frac{\mathrm{Li}(x)}{\varphi(q)}\Bigl(1 + O\bigl(e^{-c_A\sqrt{\log x}}\bigr)\Bigr)
$$
uniformly for $q \leq (\log x)^A$.

**Theorem (Bombieri–Vinogradov).** For every $A>0$,
$$
\sum_{q\leq x^{1/2}(\log x)^{-A}}\ \max_{(a,q)=1}\ \Bigl\lvert \pi(x;q,a) - \frac{\mathrm{Li}(x)}{\varphi(q)}\Bigr\rvert \ \ll_A\ \frac{x}{(\log x)^A},
$$
so that the Siegel–Walfisz approximation holds on average for moduli up to $x^{1/2}$.

**Theorem (Linnik).** There is an absolute constant $L$ such that for every $(a,q)=1$ there is a prime $p\equiv a\pmod q$ with $p\ll q^L$; the least such prime is therefore bounded polynomially in the modulus.

**Remark (the conjectures in this direction).** The Elliott–Halberstam conjecture asserts the Bombieri–Vinogradov estimate with the moduli running up to $x^{1-\epsilon}$; the generalised Riemann hypothesis would imply the Siegel–Walfisz approximation with an explicit error term for all moduli, and it is the statement treated. The use of these distribution results in the study of the primes is one of the two engines of the subject, the other being the sieve.

## Other Methods

### Sieve Methods

**Theorem (Brun).** The sum of the reciprocals of the twin primes converges:
$$
\sum_{\substack{p \\ p+2 \text{ prime}}} \frac1p < \infty .
$$
**Proof sketch.** The Brun sieve bounds from above the number of integers $\leq x$ all of whose prime factors exceed a parameter $z$ by an expression in the counting function of the residue classes modulo the product of the small primes; applying it twice, once to $n$ and once to $n+2$, gives a bound of the shape $O(x(\log\log x)^2/\log^2x)$ for the number of twin primes up to $x$, which is enough for the convergence since the count has density $O(1/\log^2x)$. $\square$

**Remark (the parity phenomenon).** The sieve methods, in the form of Brun and of Selberg, cannot distinguish an integer with an even number of prime factors from one with an odd number, the obstruction known as the parity problem; consequently the sieve alone cannot prove the prime number theorem, nor Goldbach's conjecture, nor the infinitude of the twin primes, without an additional input of a different kind. The modern approximations to those conjectures — Chen's theorem that every sufficiently large even number is a prime plus a number with at most two prime factors, and the theorem of Zhang and Maynard that there are bounded gaps between consecutive primes — are obtained by combining the sieve with information about the distribution of the primes in arithmetic progressions of the Bombieri–Vinogradov type.

### The Circle Method

**Definition.** The circle method writes a count of solutions of an additive equation, such as the number of representations of $n$ as a sum of $s$ $k$-th powers, as
$$
\int_0^1 f(\alpha)^s e^{-2\pi i n\alpha}\,d\alpha, \qquad f(\alpha) = \sum_{x\leq N} e^{2\pi i \alpha x^k},
$$
and analyses the integral by decomposing the circle into the arcs near rational points with small denominators, where $f$ is large and can be approximated, and the complementary arcs, where $f$ is small by Weyl's estimates for exponential sums.

**Theorem (Waring's problem; Hilbert, Hardy–Littlewood, Vinogradov).** For every $k\geq2$ there is a number $G(k)$ such that every sufficiently large integer is a sum of $G(k)$ $k$-th powers, and $G(k) \leq k(3\log k + 5.2)$ for large $k$; Vinogradov's method gives the sharper bounds and the three-primes theorem, that every sufficiently large odd integer is a sum of three primes.

**Proof sketch.** The major arcs contribute a singular series and a singular integral, whose main term is $\mathfrak{S}(n)\Gamma(1+1/k)^s/\Gamma(s/k)n^{s/k-1}$; the minor arcs contribute an error term controlled by Vinogradov's mean value estimates. The singular series is positive under the congruence conditions, and the integral is positive, so the count is positive for large $n$. $\square$

## Summary

Analytic number theory converts the distribution of the primes into the analysis of the zeta and $L$-functions. The von Mangoldt function satisfies $-\zeta'(s)/\zeta(s) = \sum\Lambda(n)n^{-s}$, its partial sums are the Chebyshev function $\psi(x)$, and Abel summation together with the Euler product gives the Mertens estimates and the Chebyshev bounds $\psi(x)\asymp x$, from which Bertrand's postulate follows. The statements $\pi(x)\sim x/\log x$, $\psi(x)\sim x$, $\theta(x)\sim x$ and $p_n\sim n\log n$ are equivalent, and the proof of any of them is the prime number theorem, whose analytic proof belongs.

The two formulas that organise the subject are Perron's formula, which recovers the partial sums of a Dirichlet series from a contour integral of the series, and the explicit formula of von Mangoldt, which evaluates $\psi(x)$ as $x$ minus a sum over the nontrivial zeros of $\zeta$ minus elementary terms; the version of the explicit formula obtained by shifting the contour is the exact sense in which the zeros of $\zeta$ govern the distribution of the primes. The zeros have density $\frac{1}{2\pi}\log\frac{T}{2\pi}$ near height $T$, by the Riemann–von Mangoldt formula, and they avoid a region to the left of the line $\Re s=1$, by the theorem of de la Vallée Poussin; that zero-free region is precisely the input of the analytic proof of the prime number theorem, with the error term $O(x\exp(-c\sqrt{\log x}))$. For the primes in an arithmetic progression the same analysis applies to the Dirichlet $L$-functions: the nonvanishing at $1$ gives Dirichlet's theorem and the prime number theorem in progressions, the Siegel–Walfisz theorem gives uniformity in the modulus at the cost of an ineffective constant, the Bombieri–Vinogradov theorem gives the same quality of approximation on average for moduli up to $\sqrt x$, and Linnik's theorem bounds the least prime in a progression polynomially in the modulus. The sieve methods, in the forms of Brun and Selberg, and the circle method of Hardy–Littlewood and Vinogradov are the other two engines of the subject: the first counts integers with restricted prime factors and yields Brun's theorem and, with distributional input, bounded gaps between primes; the second counts solutions of additive equations and yields Waring's problem and Vinogradov's three-primes theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p$, $p_n$ | A prime, the $n$-th prime |
| $\pi(x)$ | Number of primes $\leq x$ |
| $\pi(x;q,a)$ | Number of primes $\leq x$ congruent to $a$ modulo $q$ |
| $\Lambda(n)$ | Von Mangoldt function, $\log p$ at prime powers, $0$ otherwise |
| $\mu(n)$, $\varphi(n)$ | Möbius function, Euler function |
| $\theta(x)$, $\psi(x)$ | Chebyshev functions $\sum_{p\leq x}\log p$, $\sum_{n\leq x}\Lambda(n)$ |
| $A(x)$ | Partial sums $\sum_{n\leq x}a_n$ |
| $\rho = \beta+i\gamma$ | Nontrivial zero of $\zeta$ |
| $N(T)$ | Number of nontrivial zeros with $0<\gamma\leq T$ |
| $\mathrm{Li}(x)$ | Logarithmic integral $\int_2^x dt/\log t$ |
| $\gamma$, $M$ | Euler's constant, Mertens constant |
| $G(k)$ | Least $s$ with every large integer a sum of $s$ $k$-th powers |
| $\mathfrak{S}(n)$ | Singular series of the circle method |





## Further Reading

- Harold Davenport, *Multiplicative Number Theory* (3rd ed., Springer, 2000), for the explicit formula, the zero-free region and the classical proofs.
- Hugh L. Montgomery and Robert C. Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the systematic modern treatment of the analytic theory of the primes.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the $L$-functions, the sieve and the modern techniques.
- Enrico Bombieri, *Le grand crible dans la théorie analytique des nombres* (Astérisque 18, 1974), for the large sieve and the Bombieri–Vinogradov theorem.
- John Friedlander and Henryk Iwaniec, *Opera de cribro* (American Mathematical Society, 2010), for the sieve methods and the parity phenomenon.
- Robert C. Vaughan, *The Hardy–Littlewood Method* (2nd ed., Cambridge University Press, 1997), for the circle method and Waring's problem.
- Yuri V. Linnik, *On the least prime in an arithmetic progression* (Matematicheskii Sbornik 15, 1944), for Linnik's theorem.
- James Maynard, *Small gaps between primes* (Annals of Mathematics 181, 2015), for the bounded gaps theorem.
