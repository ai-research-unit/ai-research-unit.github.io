
# __Zeta Functions__

## Introduction

A zeta function is a Dirichlet series with an Euler product, an analytic continuation to a meromorphic function of the whole plane, and a functional equation relating its values at $s$ and at $1-s$. The prototype is the Riemann zeta function
$$
\zeta(s) = \sum_{n \geq 1} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}},
$$
introduced by Euler for real $s > 1$, continued by Riemann to the complex plane, and shown by him to satisfy the functional equation that relates $\zeta(s)$ to $\zeta(1-s)$ through the Gamma function. The same three properties hold for the Dedekind zeta function of a number field, whose Euler product runs over the prime ideals, whose pole at $s=1$ carries the class number and the regulator, and whose functional equation involves the discriminant, and they hold conjecturally, and in the cases of a curve and of a variety, for the zeta functions of algebraic geometry. This article develops the theory of the analytic continuation, the Euler product, the functional equation and the special values, first for the Riemann zeta function and then for the Dedekind zeta function, and sets the general theory of Dirichlet series in which both live.

The analytic input is Tate's thesis, the adelic integration and Fourier analysis of *Adelic Analysis*, written immediately: the completed zeta function is the integral of a Schwartz–Bruhat function against the norm character on the idele class group, the Euler product is the product of the local integrals, and the functional equation is the Poisson summation formula together with the self-duality of the adeles. That is the conceptual reason for the shape of the formulas; the elementary proofs by the theta function and by the Mellin transform are given as well, since they are the classical route and are needed for the estimates. The Dirichlet $L$-functions, their characters and their functional equations are not covered here; the distribution of the primes, the methods of complex analysis applied to arithmetic and the analytic proof of the prime number theorem belong ; the statements and consequences of the hypothesis that all the zeros lie on the critical line belong. All four are in this Part. The per-system treatment of the zeta function as a special function of a particular number system is Part V's and is deferred.

The prerequisites are *Adelic Analysis* for the adelic integrals and the local factors,andfor the Gamma function, the Mellin transform, the theta function and the theory of analytic continuation, *Measure Theory and Integration* for the interchange of limits, *Algebraic Number Theory* for the ideals, the class number, the regulator and the discriminant, *Absolute Values, Valuations and Completions* and *Local Fields* for the local computations, and *Modules* and *Rings* for the arithmetic. The Gamma function is used as standard mathematics: $\Gamma(s) = \int_0^\infty e^{-t}t^{s-1}dt$ for $\Re s > 0$, extended meromorphically to $\mathbb{C}$ with simple poles at the nonpositive integers, satisfying $\Gamma(s+1) = s\Gamma(s)$, $\Gamma(1/2) = \sqrt{\pi}$ and the reflection formula $\Gamma(s)\Gamma(1-s) = \pi/\sin(\pi s)$; the Bernoulli numbers are those of the generating function $t/(e^t-1)$, so that $B_0=1$, $B_1=-\tfrac12$, $B_2=\tfrac16$, $B_4=-\tfrac{1}{30}$, and $B_{2m+1}=0$ for $m \geq 1$. Throughout, $s = \sigma + it$ is a complex variable.

## Dirichlet Series

### Convergence and Analyticity

**Definition.** A **Dirichlet series** is a series $F(s) = \sum_{n\geq1} a_n n^{-s}$ with complex coefficients. Its **abscissa of absolute convergence** is $\sigma_a = \inf\{\sigma : \sum \lvert a_n\rvert n^{-\sigma} < \infty\}$, its **abscissa of convergence** is $\sigma_c = \inf\{\sigma : \sum a_n n^{-s}$ converges for some (equivalently every) $s$ with $\Re s = \sigma\}$, and its **abscissa of boundedness** $\sigma_b$ is the infimum of the $\sigma$ for which the partial sums are bounded on $\{\Re s \geq \sigma\}$.

**Theorem.** With these definitions $\sigma_c \leq \sigma_a \leq \sigma_c + 1$; the series converges absolutely and locally uniformly, hence to a holomorphic function, on $\Re s > \sigma_a$, and converges to a holomorphic function on $\Re s > \sigma_c$; the function so defined is holomorphic on the whole half-plane of convergence, and its derivative is the series $\sum_n (-a_n\log n)n^{-s}$, valid in the same half-plane.

**Theorem (Landau).** Let $F(s) = \sum_n a_n n^{-s}$ have nonnegative real coefficients and finite abscissa of convergence $\sigma_c$. Then $F$ has a singularity at the point $s = \sigma_c$ of the real axis, and it cannot be continued analytically to any neighbourhood of that point.

**Proof sketch.** If $F$ extended holomorphically past $\sigma_c$, then the Taylor expansion of $F$ about a real point $\sigma > \sigma_c$ would converge in a disc reaching beyond the line $\Re s = \sigma_c$; the coefficients of that expansion are nonnegative multiples of the values $F^{(k)}(\sigma) \geq 0$, and evaluating at a real point to the left of $\sigma_c$ gives a convergent series, contradicting the definition of $\sigma_c$. $\square$

### Euler Products

**Theorem (Euler product).** Let $a_1 = 1$, let $a_{mn} = a_ma_n$ whenever $(m,n) = 1$ and let $\lvert a_{p^k}\rvert \leq C^k$ for some constant $C$ and all primes $p$ and $k \geq 0$. Then for $\sigma$ large the Dirichlet series factors as
$$
\sum_{n\geq1} a_n n^{-s} = \prod_p \Bigl(\sum_{k \geq 0} a_{p^k}p^{-ks}\Bigr),
$$
and the product converges absolutely and locally uniformly in the half-plane of absolute convergence.

**Proof.** The multiplicativity makes the partial sums factor over the primes $p \leq N$ up to the terms with $n$ composed of primes $\leq N$; the difference between the sum over all $n$ and the finite product is controlled by the tail, and the local factors are bounded by $\sum_k C^k p^{-k\sigma} = (1-Cp^{-\sigma})^{-1}$, so their product converges for $\sigma$ large. $\square$

The theorem is the mechanism by which the analytic properties of the counting function of the primes are read off from a Dirichlet series: the Euler product is what makes $\sum_{n\ge1}n^{-s}$ a function of the primes, and the logarithm of the Euler product is the Dirichlet series $\sum_p p^{-s} + \dots$ whose analytic behaviour governs the distribution of the primes.

## The Riemann Zeta Function

### Definition and the Integral Representation

**Definition.** The **Riemann zeta function** is $\zeta(s) = \sum_{n\geq1} n^{-s}$ for $\Re s > 1$, with the Euler product $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ of the previous section applied to $a_n = 1$.

**Theorem (the integral representation).** For $\sigma > 1$,
$$
\Gamma(s)\zeta(s) = \int_0^\infty \frac{x^{s-1}}{e^x - 1} \, dx ,
$$
the integral converging at $0$ because $x^{s-1}/(e^x-1) \sim x^{s-2}$ and $s > 1$, and at $\infty$ by the exponential decay. The formula exhibits the pole of $\zeta$ at $s=1$: the function $\Gamma(s)\zeta(s)$, continued meromorphically by the integral, has a simple pole at $s=1$ of residue $1$, and since $\Gamma$ is holomorphic and nonzero at $1$, that pole belongs to $\zeta$ and has the same residue.

**Proof.** Expand $(e^x-1)^{-1} = \sum_{n\geq1}e^{-nx}$ for $x>0$, integrate term by term with $\int_0^\infty e^{-nx}x^{s-1}dx = \Gamma(s)n^{-s}$ and sum. $\square$

**Theorem (analytic continuation).** The function $\zeta$ extends to a meromorphic function on $\mathbb{C}$, holomorphic outside $s=1$, with a simple pole at $s=1$ of residue $1$, and with the Laurent expansion
$$
\zeta(s) = \frac{1}{s-1} + \gamma + O(s-1), \qquad \gamma = \lim_{N\to\infty}\Bigl(\sum_{n\leq N}\frac1n - \log N\Bigr),
$$
where $\gamma$ is Euler's constant. The continuation is unique.

**Proof sketch.** The integral representation, split at $x=1$, gives $\Gamma(s)\zeta(s) = \int_1^\infty\frac{x^{s-1}}{e^x-1}dx + \int_0^1 x^{s-2}\cdot\frac{x}{e^x-1}dx$; the second integrand extends to a holomorphic function of $s$ on a neighbourhood of $\Re s>1$ minus $s=1$ with a simple pole of residue $1$ and is continued by expanding $x/(e^x-1)$ in powers of $x$ and integrating term by term, the resulting series converging for $s$ off the nonpositive integers. Dividing by $\Gamma(s)$ and continuing meromorphically gives the statement. $\square$

### The Functional Equation

**Definition.** The **theta function** is $\theta(t) = \sum_{n\in\mathbb{Z}} e^{-\pi n^2 t}$ for $t>0$, and the **completed zeta function** is $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$.

**Theorem (Jacobi's functional equation for theta).** For $t > 0$, $\theta(1/t) = \sqrt{t}\,\theta(t)$.

**Proof sketch.** Both sides are the value at $0$ of the periodisation of the Gaussian $e^{-\pi t x^2}$, and the Poisson summation formula on the real line identifies the periodisation with the sum of the Fourier transforms of the Gaussian at the integers; the Gaussian $e^{-\pi t x^2}$ has Fourier transform $t^{-1/2}e^{-\pi \xi^2/t}$. $\square$

**Theorem (functional equation of the zeta function).** For all $s \in \mathbb{C}$,
$$
\Lambda(s) = \Lambda(1-s), \qquad\text{equivalently}\qquad \zeta(s) = 2^s\pi^{s-1}\sin\Bigl(\frac{\pi s}{2}\Bigr)\Gamma(1-s)\,\zeta(1-s).
$$
Moreover $\zeta(1-s)$ on the right is the analytic continuation, so the formula continues $\zeta$ to the whole plane and exhibits the trivial zeros.

**Proof sketch.** The Mellin transform of $(\theta(t)-1)/2$ is $\Lambda(s)$ for $\sigma>1$:
$$
\Lambda(s) = \int_0^\infty \frac{\theta(t)-1}{2}\, t^{s/2}\,\frac{dt}{t} .
$$
Splitting the integral at $t=1$ and substituting $t\mapsto1/t$ in the part over $(0,1)$, the theta functional equation turns that part into the same expression with $s$ replaced by $1-s$, giving the invariance. The asymmetric form follows by substituting the reflection and duplication formulas for the Gamma function. $\square$

**Corollary (the trivial zeros and the pole).** $\zeta$ has no zeros in $\Re s > 1$; it has simple zeros at the negative even integers $s = -2,-4,-6,\dots$; its only pole is the simple pole at $s=1$; and all its remaining zeros lie in the **critical strip** $0 \leq \Re s \leq 1$.

**Proof.** The Euler product, convergent and nonzero for $\sigma>1$, shows $\zeta\neq0$ there. The functional equation writes $\zeta(s)$ for $\sigma<0$ as $\sin(\pi s/2)$ times a Gamma factor times $\zeta(1-s)$, and $\zeta(1-s)$ has no pole and no zero for $\sigma<0$ except possibly the zeros from $\sin(\pi s/2)$, which are simple and occur at the negative even integers; the Gamma factor has no zeros. The remaining zeros must therefore satisfy $0\le\sigma\le1$. $\square$

**Remark (the Riemann hypothesis).** The zeros in the critical strip, and there are infinitely many of them, are conjectured to satisfy $\Re s = \tfrac12$; this is the Riemann hypothesis, whose statement, history, consequences and generalisations are not covered here. What is proved unconditionally is that $\zeta$ has no zeros on the line $\Re s = 1$, which is equivalent to the prime number theorem, and that the zeros in the strip satisfy the zero-free region $\sigma > 1 - \frac{c}{\log\lvert t \rvert}$ for an absolute constant $c$ and all sufficiently large $\lvert t\rvert$; both are the analytic content.

### Special Values

**Theorem (the positive even values).** For every $n \geq 1$,
$$
\zeta(2n) = \frac{(-1)^{n+1}B_{2n}(2\pi)^{2n}}{2(2n)!},
$$
so that in particular $\zeta(2) = \pi^2/6$, $\zeta(4) = \pi^4/90$, $\zeta(6) = \pi^6/945$; the values at the positive odd integers are not known to be rational multiples of powers of $\pi$, and $\zeta(3)$ is irrational (Apéry).

**Theorem (the values at the nonpositive integers).** $\zeta(0) = -\tfrac12$, and for $n \geq 1$
$$
\zeta(-n) = -\frac{B_{n+1}}{n+1},
$$
so that $\zeta(-1) = -\tfrac{1}{12}$, $\zeta(-3) = \tfrac{1}{120}$, $\zeta(-5) = -\tfrac{1}{252}$, and $\zeta(-2m) = 0$ for $m \geq 1$. The apparent exception at $n=0$ is the change of Bernoulli convention: the formula $\zeta(1-n) = -B_n/n$ holds for all $n \geq 1$ in the convention in which $B_1 = +\tfrac12$, whereas the generating function $t/(e^t-1)$ used here gives $B_1 = -\tfrac12$ and requires $\zeta(0) = -\tfrac12$ to be stated separately.

**Proof sketch.** Both families follow from the functional equation and from the values of the Bernoulli numbers, which compute the coefficients of the Mittag-Leffler expansion of $\pi\cot(\pi s)$; the even values are also the values of $\zeta$ obtained by the Fourier expansion of the Bernoulli polynomials, and the nonpositive values by the integral representation together with the expansion of the integrand. The vanishing at the negative even integers is the statement above about the trivial zeros. $\square$

**Corollary (the growth and convexity bounds).** In the critical strip $\zeta$ satisfies $\lvert\zeta(\sigma+it)\rvert \ll \lvert t\rvert^{(1-\sigma)/2+\epsilon}$ for every $\epsilon>0$, by the Phragmén–Lindelöf principle applied between the lines $\sigma=0$, where the functional equation gives the bound $O(\lvert t\rvert^{1/2})$, and $\sigma=1$, where the Euler product gives the bound $O(\log\lvert t\rvert)$. The Lindelöf hypothesis asserts the same bound with $\lvert t\rvert^{\epsilon}$; it is weaker than the Riemann hypothesis and stronger than the prime number theorem.

**Remark.** The same circle of ideas gives the values of the Dirichlet beta function $\beta(s)=\sum_{n\geq0}(-1)^n(2n+1)^{-s}$, namely $\beta(1)=\pi/4$, $\beta(2)=G$ — **Catalan's constant**, $G=\sum_{n\geq0}(-1)^n(2n+1)^{-2}$ — and $\beta(3)=\pi^3/32$; thus $G$ is a period in the same sense as the even values of $\zeta$, and $\beta$ is the Dirichlet $L$-function of the nontrivial character modulo $4$.

## The Dedekind Zeta Function

### Definition and Euler Product

**Definition.** Let $K$ be a number field with ring of integers $\mathcal{O}_K$ and class number $h$, regulator $R$, discriminant $d_K$, $r_1$ real places, $r_2$ complex places and $w$ roots of unity. The **Dedekind zeta function** is
$$
\zeta_K(s) = \sum_{\mathfrak{a} \subset \mathcal{O}_K} \frac{1}{N(\mathfrak{a})^s} = \prod_{\mathfrak{p}} \frac{1}{1 - N(\mathfrak{p})^{-s}},
$$
the sum over the nonzero ideals and the product over the nonzero prime ideals, with $N(\mathfrak{a}) = \lvert \mathcal{O}_K/\mathfrak{a}\rvert$; for $K = \mathbb{Q}$ it is the Riemann zeta function.

**Theorem.** The series and the product converge absolutely and locally uniformly for $\Re s > 1$, the product is the Euler product of the sum, and both define the same holomorphic function there, nonzero throughout the half-plane.

**Proof.** The number of ideals of norm $\leq X$ is $O(X)$ and the number of prime ideals of norm $\leq X$ is $O(X/\log X)$, so the sum and the product converge for $\sigma>1$; multiplicativity and unique factorisation of ideals give the Euler product as in the general Euler-product theorem; the product is nonzero because no factor vanishes. $\square$

### Analytic Continuation, Functional Equation and the Pole

**Definition.** The completed Dedekind zeta function is
$$
\Lambda_K(s) = \lvert d_K \rvert^{s/2}\,\Gamma_{\mathbb{R}}(s)^{r_1}\,\Gamma_{\mathbb{C}}(s)^{r_2}\,\zeta_K(s),
$$
with $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$ and $\Gamma_{\mathbb{C}}(s) = 2(2\pi)^{-s}\Gamma(s)$.

**Theorem (Hecke).** $\zeta_K$ extends to a meromorphic function on $\mathbb{C}$ with a simple pole at $s=1$ and no other pole, and the completed function satisfies the functional equation
$$
\Lambda_K(s) = \Lambda_K(1-s).
$$
The residue at the pole is the class number formula
$$
\operatorname*{Res}_{s=1}\zeta_K(s) = \frac{2^{r_1}(2\pi)^{r_2}\,h\,R}{w\sqrt{\lvert d_K \rvert}} .
$$
**Proof sketch.** The adelic proof is the one of *Adelic Analysis*: $\zeta_K(s) = Z(s,1,\Phi)$ for the trivial Hecke character and a factorisable $\Phi$ whose finite components are $\mathbf{1}_{\mathcal{O}_v}$ and whose infinite components are Gaussians normalised with respect to the trace form, the $|d_K|^{s/2}$ of the completed function being the normalisation of those Gaussians; the Euler product is the product of the local integrals, each local integral is the local $L$-factor of the local zeta integral theorem, and the global functional equation is Poisson summation. The residue is the volume of the idele class group computed there, divided by the local factors. The classical proof uses the theta series associated with the lattice $\mathcal{O}_K$ in the Minkowski space and the same Mellin transform as in the case of $\mathbb{Q}$. $\square$

**Corollary (the class number formula).** The residue formula contains Dirichlet's class number formula: for an imaginary quadratic field the left side is $2\pi h/(w\sqrt{\lvert d\rvert})$, which recovers the classical formula in terms of a character sum; more generally, the formula relates the analytic datum $\operatorname{Res}_{s=1}\zeta_K(s)$ to the arithmetic data $h$ and $R$, which is why the residue is a computable invariant of the field.

**Corollary (nonvanishing at $1$ and the prime ideal theorem).** $\zeta_K$ has no zero on the line $\Re s = 1$; consequently the Euler product does not vanish there and the analytic machinery applies to the prime ideals, yielding the prime ideal theorem for $K$ when it is applied to $\log\zeta_K$. The analogous statement for the primes in an arithmetic progression in $\mathbb{Q}$ requires the Dirichlet $L$-functions, whose nonvanishing at $1$ is proved in the same way and which are not covered here; the use of the two nonvanishing statements for counting primes is not covered here.

## Other Zeta Functions

**Definition.** For a variety $X$ over $\mathbb{Z}$ of finite type the **Hasse–Weil zeta function** is
$$
\zeta_X(s) = \prod_p \zeta_{X_p}(p^{-s}),
$$
where $X_p$ is the reduction of $X$ modulo $p$ and $\zeta_{X_p}$ is the zeta function of the variety over the finite field $\mathbb{F}_p$, itself defined by $\zeta_{X_p}(t) = \exp\bigl(\sum_{n\geq1}\lvert X_p(\mathbb{F}_{p^n})\rvert t^n/n\bigr)$ with $t = p^{-s}$, equivalently by the requirement that the logarithmic derivative $\sum_{n\geq1}\lvert X_p(\mathbb{F}_{p^n})\rvert p^{-ns}$ be the Dirichlet series of the point counts; for $X = \mathrm{Spec}\,\mathcal{O}_K$ this recovers the Dedekind zeta function, and for $X = \mathrm{Spec}\,\mathbb{Z}$ the Riemann zeta function.

**Theorem (Dwork).** For a variety $X$ over a finite field the zeta function $\zeta_X$ is a rational function of $q^{-s}$.

**Proof sketch.** Dwork's lemma of *p-adic Differential Equations* states that a power series whose coefficients satisfy the integrality conditions imposed by the action of the Frobenius converges on the open unit disc; applied to the coefficient series of the zeta function over $\mathbb{F}_p$ it gives a nonvanishing analytic function on a disc containing the origin together with an estimate for its logarithmic derivative, and the two together force the point counts $\lvert X_p(\mathbb{F}_{p^n})\rvert$ to satisfy a linear recurrence, so that $\zeta_{X_p}$ is a quotient of polynomials in $t$ and hence a rational function of $q^{-s}$. The modern proof passes instead through the Lefschetz trace formula and the eigenvalues of the Frobenius, which belong to the arithmetic geometry of Part I. $\square$

The rationality of the local factor is the first of the Weil conjectures; the functional equation, the Riemann hypothesis for the local factor and the global theory of the Hasse–Weil zeta function belong to the arithmetic geometry of Part I, and are cited rather than developed here. What this article supplies is the analytic theory of the two zeta functions of number theory, the Riemann and the Dedekind, together with the general Dirichlet series framework in which their properties are stated.

## Summary

A Dirichlet series $\sum a_nn^{-s}$ has an abscissa of convergence $\sigma_c$ and an abscissa of absolute convergence $\sigma_a$ with $\sigma_c\le\sigma_a\le\sigma_c+1$, it is holomorphic on the half-plane $\Re s>\sigma_c$, and a series with nonnegative coefficients has a singularity at its abscissa of convergence, by Landau's theorem. A series with multiplicative coefficients has an Euler product, which is the mechanism that puts the primes into the analytic function.

The Riemann zeta function $\zeta(s) = \sum n^{-s}$ converges for $\Re s>1$, has the Euler product over the primes, and extends to a meromorphic function whose only pole is simple at $s=1$ with residue $1$; the completed function $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ satisfies $\Lambda(s) = \Lambda(1-s)$ and equivalently $\zeta(s) = 2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s)$, the proof being the Mellin transform of the theta function together with its functional equation $\theta(1/t) = \sqrt t\,\theta(t)$. The completions give the special values: $\zeta(2n)$ is a rational multiple of $\pi^{2n}$ with the Bernoulli numbers as coefficients, and $\zeta(-n) = -B_{n+1}/(n+1)$ for $n\ge1$ with $\zeta(0) = -\tfrac12$, so that the negative even integers are simple zeros and all other nontrivial zeros lie in the critical strip. The Dedekind zeta function of a number field has an Euler product over the prime ideals, a meromorphic continuation whose only pole is simple at $s=1$, a functional equation for the completed function with the discriminant and the Gamma factors, and a residue at the pole that is the class number formula; the adelic proof of all of this is Tate's thesis, the local and global zeta integrals of *Adelic Analysis*. The zeta function of a variety over a finite field is rational, by Dwork's lemma, and the Hasse–Weil zeta function of a variety over $\mathbb{Z}$ is the product of the local factors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $s = \sigma + it$ | Complex variable and its real and imaginary parts |
| $\zeta(s)$ | Riemann zeta function, $\sum_{n\ge1}n^{-s}$ |
| $\prod_p$ | Product over the primes |
| $\Lambda(s)$ | Completed zeta, $\pi^{-s/2}\Gamma(s/2)\zeta(s)$ |
| $\theta(t)$ | Theta function, $\sum_{n\in\mathbb{Z}}e^{-\pi n^2t}$ |
| $\Gamma$ | Gamma function, $\Gamma(s+1)=s\Gamma(s)$ |
| $\gamma$ | Euler's constant |
| $B_n$ | Bernoulli numbers, generating function $t/(e^t-1)$ |
| $\sigma_c$, $\sigma_a$ | Abscissas of convergence and of absolute convergence |
| $\zeta_K(s)$ | Dedekind zeta function of a number field $K$ |
| $\mathcal{O}_K$, $\mathfrak{a}$, $\mathfrak{p}$, $N(\mathfrak{a})$ | Ring of integers, ideals, prime ideals, absolute norm |
| $d_K$, $r_1$, $r_2$, $h$, $R$, $w$ | Discriminant, real and complex places, class number, regulator, roots of unity |
| $\Gamma_{\mathbb{R}}(s)$, $\Gamma_{\mathbb{C}}(s)$ | $\pi^{-s/2}\Gamma(s/2)$, $2(2\pi)^{-s}\Gamma(s)$ |
| $\Lambda_K(s)$ | Completed Dedekind zeta function, $\Lambda_K(s)=\Lambda_K(1-s)$ |
| $\zeta_X(s)$ | Hasse–Weil zeta function of a variety $X$ |
| $\lvert X(\mathbb{F}_{p^n})\rvert$ | Number of points of the reduction over the finite field |









## Further Reading

- Bernhard Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Größe* (Monatsberichte der Berliner Akademie, 1859), for the original statement of the functional equation and the hypothesis.
- Edmund Landau, *Handbuch der Lehre von der Verteilung der Primzahlen* (Teubner, 1909), for the classical theory of Dirichlet series, Landau's theorem and the Euler products.
- Erich Hecke, *Über die Zetafunktion beliebiger algebraischer Zahlkörper* (Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, 1917), for the Dedekind zeta function, its functional equation and the class number formula.
- Harold Davenport, *Multiplicative Number Theory* (3rd ed., Springer, 2000), for the analytic continuation, the zero-free region and the estimates used in the prime number theorem.
- Hugh L. Montgomery and Robert C. Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for a modern systematic treatment of the Dirichlet series of number theory.
- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (doctoral thesis, Princeton, 1950), for the adelic proof of the functional equation and the class number formula.
- Bernard Dwork, *On the rationality of the zeta function of an algebraic variety* (American Journal of Mathematics 82, 1960), for the rationality of the local zeta function.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for the Dedekind zeta function and its arithmetic content.
