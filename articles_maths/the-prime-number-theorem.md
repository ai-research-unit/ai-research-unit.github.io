
# __The Prime Number Theorem__

## Introduction

The prime number theorem asserts that the primes thin out like the reciprocal of the logarithm:
$$
\pi(x) \sim \frac{x}{\log x}, \qquad\text{equivalently}\qquad \psi(x) = \sum_{n\leq x}\Lambda(n) \sim x,
$$
so that the $n$-th prime satisfies $p_n\sim n\log n$, and the average density of the primes near $x$ is $1/\log x$. It was conjectured by Gauss and by Legendre from numerical evidence, it was reduced by Riemann to the behaviour of the zeta function, and it was proved in 1896 independently by Hadamard and by de la Vallée Poussin by showing that $\zeta$ has no zeros on the line $\Re s = 1$. The proof is the model instance of the general principle established in *Analytic Number Theory*: the distribution of an arithmetic sequence is read off from the analytic behaviour of the Dirichlet series it generates, and a statement about zeros becomes a statement about the average order of the primes.

This article gives the proof. It is organised around two theorems, one analytic and one tauberian. The analytic theorem is the nonvanishing of $\zeta$ on the line $\Re s=1$, proved from the elementary inequality $3+4\cos\theta+\cos2\theta\geq0$ applied to the logarithmic derivative; the tauberian theorem is the Wiener–Ikehara theorem, in the short form due to Newman, which converts the analytic continuation of a Mellin transform past the line $\Re s=1$, with a simple pole of residue $c$ at $1$, into the asymptotic $A(x)\sim cx$ of the nondecreasing function transformed. Applied to $-\zeta'/\zeta$, whose Mellin transform is the Chebyshev function $\psi$, the two give $\psi(x)\sim x$. The article then quantifies the result: the zero-free region of de la Vallée Poussin and of Vinogradov–Korobov gives error terms, the hypothesis that all the zeros lie on the critical line gives the conjecturally optimal error term of order $\sqrt x$, and it is shown that the prime number theorem is equivalent to each of several other statements, including the vanishing of the summatory Möbius function and the nonvanishing of $\zeta$ on the whole line $\Re s = 1$. The elementary proof of Erdős and Selberg, which avoids complex analysis, is stated with its identity and its defect. The article closes with the extensions: the theorem in arithmetic progressions and the prime ideal theorem for a number field, the theorem in short intervals with the Baker–Harman–Pintz exponent, and the sense in which the theorem is a one-place statement that says nothing about the error with which the primes approach their density.

The prerequisites are *Analytic Number Theory*, written immediately above, for the arithmetic functions, Perron's formula, the explicit formula of von Mangoldt, the Riemann–von Mangoldt zero count and the Chebyshev bounds; *Zeta Functions* for the Euler product, the functional equation, the location of the trivial zeros and Landau's theorem; *L-Functions* for the Dirichlet $L$-functions and their nonvanishing at $1$; *Measure Theory and Integration* and *Modes of Convergence* for the interchange of limits; andin the synthetic part of the corpus where the number system is fixed, for the Cauchy theory that the contour arguments use, cited and deferred rather than developed. The statements about the zeros beyond the line $\Re s=1$ — the distribution of the zeros, the consequences of the hypothesis that they all lie on the critical line, the generalised hypothesis and its applications — belong, written in parallel, which takes the equivalence established here as one of its starting points; the arithmetic functions of a general number field belong to *Algebraic Number Theory*, and the modular and automorphic methods of attacking the zeros belong and *Automorphic Forms*.

## The Statement and its Equivalent Forms

**Definition.** The **Chebyshev functions** are
$$
\psi(x) = \sum_{n\leq x}\Lambda(n) = \sum_{p^k\leq x}\log p, \qquad \theta(x) = \sum_{p\leq x}\log p,
$$
and $\mathrm{Li}(x) = \int_2^x\frac{dt}{\log t}$ is the logarithmic integral.

**Theorem (the prime number theorem; Hadamard and de la Vallée Poussin).** As $x\to\infty$,
$$
\pi(x) \sim \frac{x}{\log x}, \qquad \psi(x)\sim x, \qquad \theta(x)\sim x, \qquad p_n \sim n\log n .
$$
All four statements are equivalent.

**Proof of the equivalence.** This is the theorem on the equivalent forms in *Analytic Number Theory*: $\psi-\theta = \sum_{k\geq2}\theta(x^{1/k})=O(x^{1/2}\log x)=o(x)$, so $\psi\sim x$ and $\theta\sim x$ are the same statement; Abel summation converts $\theta(x)\sim x$ into $\pi(x)\sim x/\log x$ and back, by the two identities displayed there; and $p_n\sim n\log n$ is the same statement evaluated at $x = p_n$. $\square$

**Remark (what the theorem does not say).** The statement is a one-term asymptotic. It does not say that $\pi(x)-\mathrm{Li}(x)$ is small, that the primes are equidistributed in short intervals without a lower bound on the length, or that the gaps between consecutive primes are small; each of these is a separate problem, and the last is discussed below . The sharper asymptotic $\pi(x) = \mathrm{Li}(x) + O(xe^{-c\sqrt{\log x}})$ proved below is stronger than the theorem and is the form in which the result is used.

## Nonvanishing on the Line $\Re s = 1$

### The Elementary Inequality

**Lemma.** For every real $\theta$, $3 + 4\cos\theta + \cos2\theta = 2(1+\cos\theta)^2 \geq 0$.

**Proof.** $\cos2\theta = 2\cos^2\theta-1$, so the left side is $2\cos^2\theta + 4\cos\theta + 2 = 2(\cos\theta+1)^2$. $\square$

**Theorem.** $\zeta(\sigma+it)\neq0$ for every $\sigma\geq1$ and every real $t$.

**Proof.** For $\sigma>1$ the Euler product converges absolutely, so $\zeta(\sigma+it)\neq0$; it remains to treat $\sigma=1$. Write the logarithm of the Euler product,
$$
\log\zeta(s) = \sum_p\sum_{k\geq1}\frac{e^{-ik t\log p}}{k p^{k\sigma}} = \sum_{n\geq2}\frac{c_n}{n^{\sigma}}e^{-it\log n},
$$
with $c_n = \Lambda(n)/\log n\geq0$; this is a Dirichlet series with nonnegative coefficients, so its real part is at least the contribution of the constants, and taking the real part of the combination with the weights $3,4,1$ of the inequality gives
$$
3\log\lvert\zeta(\sigma)\rvert + 4\log\lvert\zeta(\sigma+it)\rvert + \log\lvert\zeta(\sigma+2it)\rvert
= \sum_n\frac{c_n}{n^\sigma}\bigl(3+4\cos(t\log n)+\cos(2t\log n)\bigr) \geq 0
$$
by the lemma, for every $\sigma>1$. Suppose $\zeta(1+it_0)=0$ for some $t_0\neq0$. Since $\zeta$ has a simple pole at $s=1$, $\log\lvert\zeta(\sigma)\rvert = -\log(\sigma-1)+O(1)$ as $\sigma\downarrow1$, so the first term is $-3\log(\sigma-1)+O(1)$; the zero at $1+it_0$ makes the second term $4\log(\sigma-1)+O(1)$; and the third is bounded above, since $\zeta$ is holomorphic near $1+2it_0$. The sum is therefore $+\log(\sigma-1)+O(1)$, which tends to $-\infty$, contradicting its nonnegativity. Hence no such $t_0$ exists, and the same argument excludes a zero at $s=1$ itself, where the pole already excludes it. $\square$

**Corollary.** $1/\zeta(s)$ extends analytically to the half-plane $\Re s\geq1$ away from the pole at $s=1$, and $-\zeta'/\zeta(s) - \frac{1}{s-1}$ extends continuously to $\Re s \geq 1$.

**Proof.** The zeros of $\zeta$ are isolated and lie off the closed half-plane $\Re s\geq1$ by the theorem; the pole at $s=1$ is simple, so $\zeta(s)(s-1)$ is holomorphic and nonvanishing on a neighbourhood of that closed half-plane, and its reciprocal is holomorphic there. The logarithmic derivative is $-\frac{1}{s-1}$ plus the logarithmic derivative of the holomorphic nonvanishing factor. $\square$

**Remark (the strength of the method).** The proof uses only the inequality of the lemma and the pole at $s=1$; it shows in particular that $\zeta$ has no zero on the line, and identifies the pole as the obstruction. It is the only place in the proof of the prime number theorem where the arithmetic of $\zeta$ — the Euler product — is used in an essential way; the rest is analysis. The same argument, with the same inequality, proves that a Dirichlet $L$-function has no zero at $s=1$ when it has no pole there, and hence Dirichlet's theorem; the case of a real character, where the harmonic series $\sum\chi(p)/p$ must be shown to diverge, needs in addition the nonnegativity argument of *L-Functions*.

## The Tauberian Theorem and the Proof

### The Mellin Transform of the Chebyshev Function

**Definition.** Let $A:[1,\infty)\to\mathbb{C}$ be locally of bounded variation and suppose the integral $\int_1^\infty A(x)x^{-s-1}dx$ converges for $\Re s>1$. Its value is the **Mellin transform** $g(s)$ of $A$.

**Lemma.** With $\psi$ the Chebyshev function,
$$
g(s) = \int_1^\infty \psi(x)\,x^{-s-1}\,dx = -\frac{\zeta'(s)}{s\,\zeta(s)} = \frac{1}{s-1} + h(s) \qquad (\Re s>1),
$$
where $h$ extends continuously to the closed half-plane $\Re s \geq 1$.

**Proof.** Partial summation in the form $\sum_{n\leq x}a_n = x^{-s}\int\dots$, or the Stieltjes integral: $g(s) = \int_{1^-}^\infty x^{-s-1}d\psi(x) = \frac{1}{s}\sum_{n\ge1}\Lambda(n)n^{-s} = -\frac{\zeta'(s)}{s\zeta(s)}$, the integration by parts producing the factor $1/s$ and the last identity being the logarithmic-derivative formula of *Analytic Number Theory*. The principal part at $s=1$ is $1/(s-1)$, from the simple pole of $\zeta$ with residue $1$; the remainder $h$ is continuous on $\Re s\geq1$ by the corollary above. $\square$

### The Wiener–Ikehara and Newman Theorems

**Theorem (Wiener–Ikehara).** Let $A:[1,\infty)\to[0,\infty)$ be nondecreasing, with $A(x)=0$ for $x<1$, and let
$$
g(s) = \int_1^\infty A(x)\,x^{-s-1}dx = H(s) + \frac{c}{s-1}
$$
for $\Re s>1$, where $c\geq0$ is constant and $H$ extends continuously to the closed half-plane $\Re s\geq1$. Then $A(x) \sim c\,x$ as $x\to\infty$.

**Theorem (Newman's form).** Let $f:[0,\infty)\to\mathbb{C}$ be bounded and locally integrable, and suppose that the Laplace transform $g(s) = \int_0^\infty f(t)e^{-st}dt$, which converges for $\Re s>0$, extends to a continuous function on the closed half-plane $\Re s\geq0$. Then the improper integral $\int_0^\infty f(t)\,dt$ converges, and its value is $g(0)$.

**Proof sketch (Newman).** For $T>0$ put $g_T(s) = \int_0^T f(t)e^{-st}dt$, an entire function. The difference $g(s)-g_T(s)$ is the tail integral, bounded by $\lVert f\rVert_\infty e^{-T\sigma}/\sigma$ for $\sigma>0$. Cauchy's formula applied to $g-g_T$ on the circle with diameter $[-R,R]$ in the plane, evaluated at $s=0$, gives
$$
g(0)-g_T(0) = \frac{1}{2\pi i}\oint\bigl(g(s)-g_T(s)\bigr)e^{sT}\Bigl(1+\frac{s^2}{R^2}\Bigr)\frac{ds}{s} ,
$$
a form chosen so that the factor $e^{sT}(1+s^2/R^2)$ is bounded by $e^{T\sigma}$ on the circle and the integrand is entire; splitting the contour at $\Re s = -1/T$, on the left of which the tail is exponentially small while $g$ is bounded by the hypothesis, and estimating on the right where the difference is controlled, gives $\lvert g(0)-g_T(0)\rvert \to 0$ as $T\to\infty$ after taking $R\to\infty$. Hence $\int_0^Tf\to g(0)$. $\square$

**Proof sketch (the two forms are the same).** Substituting $x = e^t$ and $A(e^t) = e^t f(t)$ converts the Mellin transform of $A$ into the Laplace transform of $f$ up to the shift $s\mapsto s-1$; the monotonicity of $A$ supplies the boundedness of $f$ needed in Newman's theorem, and the pole $c/(s-1)$ of $g$ becomes a finite limit of $g$ at $s=0$ after subtracting the principal part, which is the continuity hypothesis. $\square$

### The Proof of the Theorem

**Theorem (prime number theorem, analytic proof).** $\psi(x)\sim x$.

**Proof.** By the corollary of the nonvanishing theorem, $-\zeta'(s)/(s\zeta(s)) = \frac{1}{s-1}+h(s)$ with $h$ continuous on $\Re s\geq1$; by the lemma this is the Mellin transform of the nondecreasing function $\psi$. The Wiener–Ikehara theorem with $c=1$ gives $\psi(x)\sim x$, and the theorem follows by the equivalence of its forms. $\square$

**Corollary (the logarithmic integral form).** There is a constant $c>0$ with
$$
\pi(x) = \mathrm{Li}(x) + O\bigl(x\,e^{-c\sqrt{\log x}}\bigr) \qquad (x\to\infty),
$$
and the error $O(xe^{-c\sqrt{\log x}})$ is smaller than $x/\log^A x$ for every $A$; consequently $\pi(x) = \mathrm{Li}(x)(1+o(1))$ and in particular $\pi(x)\sim x/\log x$.

**Proof sketch.** Inserting the zero-free region of the next section into the explicit formula of von Mangoldt and estimating the sum over the zeros, and then converting $\psi$ to $\pi$ by the Abel-summation identities. $\square$

## The Error Term

### The Zero-Free Region

**Theorem (de la Vallée Poussin).** There is a constant $c>0$ such that $\zeta(\sigma+it)\neq0$ whenever
$$
\sigma > 1 - \frac{c}{\log(\lvert t\rvert+2)} .
$$
**Proof sketch.** The lemma of the first section is applied at the three points $\sigma$, $\sigma+it$, $\sigma+2it$ with the further information that $\sum_p p^{-2\sigma}$ and similar sums are bounded below; subtracting the pole behaviour of $\log\zeta$ at $s=1$ and using $\lvert\zeta(1+i t)\rvert$ bounded below by a negative power of $\log\lvert t\rvert$ — the standard estimate from the functional equation and the convexity bounds of *Zeta Functions* — gives the region. The constant depends only on the constants in those estimates. $\square$

**Corollary (error terms).** With the region above,
$$
\psi(x) = x + O\bigl(x\,e^{-c'\sqrt{\log x}}\bigr), \qquad \pi(x) = \mathrm{Li}(x) + O\bigl(x\,e^{-c'\sqrt{\log x}}\bigr)
$$
for a constant $c'>0$; the zero-free region and the error term are equivalent in the sense that a wider zero-free region gives a smaller error and conversely.

**Theorem (Vinogradov–Korobov).** $\zeta(\sigma+it)\neq0$ for
$$
\sigma > 1 - \frac{c}{(\log\lvert t\rvert)^{2/3}(\log\log\lvert t\rvert)^{1/3}} ,
$$
and consequently
$$
\psi(x) = x + O\Bigl(x\exp\Bigl(-\frac{c'(\log x)^{3/5}}{(\log\log x)^{1/5}}\Bigr)\Bigr).
$$
**Proof sketch.** Vinogradov's method estimates the exponential sums $\sum_{n\leq N}n^{it}$ in mean square with a saving over the trivial estimate; the saving is fed into the classical zero-free-region argument, replacing the estimate $\lvert\zeta(1+it)\rvert^{-1}\ll\log^{A}\lvert t\rvert$ by the sharper one obtained from the sum estimates. $\square$

**Remark (the conditional error term).** If all the nontrivial zeros of $\zeta$ lie on the line $\Re s = \tfrac12$, then the explicit formula gives $\psi(x) = x + O(\sqrt x\log^2x)$ and $\pi(x) = \mathrm{Li}(x)+O(\sqrt x\log x)$, and this is optimal for the method: the oscillation of $\psi(x)-x$ is of order at least $\sqrt x$, so no smaller power of $x$ can occur. This is the content of the Riemann hypothesis as it concerns the primes; the hypothesis itself, its consequences and the generalised form belong. What is unconditional is that the error is $o(x)$ and that it is bounded by $x\exp(-c'\sqrt{\log x})$; the gap between that and $\sqrt x$ is the gap between the known zero-free region and the line.

## Equivalences and the Elementary Proof

### Equivalences

**Theorem.** The following are equivalent.

**(a)** $\psi(x)\sim x$ (the prime number theorem);

**(b)** $\sum_{n\leq x}\mu(n) = o(x)$;

**(c)** $\zeta(1+it)\neq0$ for every real $t$;

**(d)** $\sum_{n\leq x}\frac{\mu(n)}{n} = o(1)$.

**Proof sketch.** The implication (a)$\Rightarrow$(c) is the argument of the first section run in reverse: the nonnegativity relation $3\log\lvert\zeta(\sigma)\rvert+4\log\lvert\zeta(\sigma+it)\rvert+\log\lvert\zeta(\sigma+2it)\rvert\geq0$, evaluated with the asymptotic $\sum\Lambda(n)n^{-\sigma}\sim1/(\sigma-1)$, forces $\zeta(1+it)\neq0$. The implication (c)$\Rightarrow$(a) is the analytic proof above, with the tauberian theorem applied to the Dirichlet series $1/\zeta$ and to $-\zeta'/\zeta$. The equivalence of (b) and (c) is the same argument applied to the series $\sum\mu(n)n^{-s}=1/\zeta(s)$, whose Mellin transform has abscissa $1$ exactly when $1/\zeta$ is holomorphic on $\Re s\geq1$, that is exactly when $\zeta$ has no zero there; and (d) is the Abel-summed form of (b), since $M(x) = x\sum_{n\le x}\mu(n)/n-\int_1^x\sum_{n\le t}\mu(n)/n\,dt$. The implication (b)$\Rightarrow$(a) can also be run directly, by partial summation and Möbius inversion, and it is in that form that the equivalence is used in the elementary proof. $\square$

### The Elementary Proof

**Theorem (Erdős–Selberg).** The prime number theorem holds, and its proof requires no complex analysis. The central identity is
$$
\sum_{p\leq x}(\log p)^2 + \sum_{pq\leq x}\log p\,\log q = 2x\log x + O(x),
$$
equivalently $\sum_{n\leq x}\Lambda(n)\log n + \sum_{mn\leq x}\Lambda(m)\Lambda(n) = 2x\log x + O(x)$, equivalently, with $R(x) = \psi(x)-x$,
$$
R(x)\log x + \sum_{n\leq x}\Lambda(n)\,R\!\left(\frac xn\right) = O(x),
$$
and it implies $\psi(x)\sim x$ by the elementary argument of Selberg and Erdős, which uses only the Chebyshev bounds $\psi(x)\asymp x$ and Mertens' first estimate $\sum_{n\leq x}\Lambda(n)/n = \log x+O(1)$ in addition to the identity.

**Proof sketch.** The identity is Selberg's, and its standard derivation compares the two evaluations of $\sum_{n\leq x}\Lambda(n)\log n$: one as $\psi(x)\log x-\int_1^x\psi(t)t^{-1}dt$, the other as the double sum $\sum_{mn\leq x}\Lambda(m)\Lambda(n)$ corrected by the divisor estimate $\sum_{n\le x}d(n) = x\log x+O(x)$. To pass from the identity to the theorem, write $\psi = x+R$ and $K(x) = \int_1^x\psi(t)t^{-1}dt$; the identity becomes
$$
R(x)\log x + \sum_{n\leq x}\Lambda(n)R\!\left(\frac xn\right) = x\log x - x\sum_{n\leq x}\frac{\Lambda(n)}{n} + K(x)+O(x),
$$
and the right side is $O(x)$, because Mertens' first estimate $\sum_{n\le x}\Lambda(n)/n = \log x+O(1)$ is elementary and $K(x) = O(x)$ by the Chebyshev bounds. The elementary lemma of Selberg and Erdős then deduces $R(x) = o(x)$ from this relation, using only $R(x)\ll x$: the relation expresses $R(x)$ in terms of its own averages over the scaled arguments $x/n$, and averaging over the range forces the oscillation to vanish. $\square$

**Remark (the elementary proof gives no error term).** The elementary method produces $\psi(x) = x+o(x)$ but no rate; the proof of the rate requires the analytic information on the zeros, and the strongest known unconditional error term is the Vinogradov–Korobov one above. The elementary proof is therefore not a substitute for the analytic theory but a different route to the main term, and the analytic route is the one that organises the information about the zeros. The relation between the error term and the zeros is the explicit formula of *Analytic Number Theory*, in which each zero $\rho$ contributes a term $-x^\rho/\rho$ to $\psi(x)-x$.

## Extensions

**Theorem (prime number theorem in arithmetic progressions).** For fixed $q$ and $(a,q)=1$,
$$
\pi(x;q,a) \sim \frac{1}{\varphi(q)}\frac{x}{\log x},
$$
and more precisely $\pi(x;q,a) = \mathrm{Li}(x)/\varphi(q) + O(xe^{-c\sqrt{\log x}})$ for a constant $c>0$ depending on $q$.

**Proof sketch.** The proof is the proof of the prime number theorem with $-\zeta'/\zeta$ replaced by the average $\frac1{\varphi(q)}\sum_\chi\bar\chi(a)\bigl(-\frac{L'}{L}(s,\chi)\bigr)$ over the characters modulo $q$; the nonvanishing on the line holds for every $L(s,\chi)$ by the same inequality, and the only genuine difference is that no $L(s,\chi)$ has a pole at $s=1$ except the principal one, which supplies the factor $1/\varphi(q)$. The uniformity in $q$ is the subject of the Siegel–Walfisz and Bombieri–Vinogradov theorems of *Analytic Number Theory*. $\square$

**Theorem (prime ideal theorem).** Let $K$ be a number field and $\psi_K(x) = \sum_{N(\mathfrak{p})^k\leq x}\log N(\mathfrak{p})$. Then $\psi_K(x)\sim x$, and $\pi_K(x)\sim x/\log x$.

**Proof sketch.** The same proof with $\zeta_K$ in place of $\zeta$: the Dedekind zeta function has a simple pole at $s=1$ with residue the class number formula, it has no zeros on the line $\Re s=1$, by the same inequality applied to its Euler product over the prime ideals, and the Tauberian theorem applied to $-\zeta_K'/\zeta_K$ gives $\psi_K(x)\sim x$. $\square$

**Theorem (primes in short intervals; Baker–Harman–Pintz).** For every $\theta>0.525$ and all sufficiently large $x$,
$$
\pi(x+x^{\theta}) - \pi(x) \sim \frac{x^{\theta}}{\log x},
$$
so the interval $[x,x+x^{\theta}]$ contains about its expected number of primes; under the Riemann hypothesis the same holds for every $\theta>\tfrac12$.

**Theorem (the number of primes and the nth prime).** The theorem gives $\pi(x)\sim x/\log x$ and $p_n\sim n\log n$; the sharper forms are $\pi(x) = \mathrm{Li}(x)+O(xe^{-c\sqrt{\log x}})$ and, with the sharp zero-free region, $p_n = n(\log n + \log\log n - 1 + o(1))$.

**Proof sketch.** The second display is the inversion of the asymptotic for $\pi$ by the standard expansion of the logarithmic integral and one iteration of the relation $p_n\log p_n\sim n\log n$. $\square$

**Remark (the place of the theorem).** The prime number theorem is the first quantitative statement about the primes and the simplest consequence of the nonvanishing of $\zeta$ on the line $\Re s = 1$; the whole of the further information about the primes is carried by the zeros in the strip, and it is read off from them through the explicit formula. The hypothesis that all of them lie on the critical line, and the consequences of that hypothesis for the error term, for the distribution of the gaps between consecutive primes and for the generalised statement over number fields, are the subject, which begins from the equivalences established here.

## Summary

The prime number theorem is the statement $\pi(x)\sim x/\log x$, equivalently $\psi(x)\sim x$ for the Chebyshev function $\psi(x) = \sum_{n\leq x}\Lambda(n)$, equivalently $\theta(x)\sim x$ for the sum of $\log p$ over the primes, equivalently $p_n\sim n\log n$ for the $n$-th prime. The proof rests on two theorems, one analytic and one tauberian. The analytic theorem is the nonvanishing $\zeta(\sigma+it)\neq0$ for $\sigma\geq1$, proved by applying the nonnegative trigonometric combination $3+4\cos\theta+\cos2\theta = 2(1+\cos\theta)^2$ to the Dirichlet series $\log\zeta$ with nonnegative coefficients and comparing the pole at $s=1$ with a hypothetical zero; it implies that $-\zeta'(s)/(s\zeta(s)) = \frac{1}{s-1}+h(s)$ with $h$ continuous on the closed half-plane. The tauberian theorem, in the Wiener–Ikehara form and in Newman's short form, converts the Mellin transform of a nondecreasing function, with a simple pole of residue $c$ at $s=1$ and continuous remainder on the closed half-plane, into the asymptotic $A(x)\sim cx$; applied to the Mellin transform of $\psi$, which is exactly $-\zeta'/(s\zeta)$, it gives $\psi(x)\sim x$.

The rate is governed by the zeros. The zero-free region of de la Vallée Poussin, $\sigma > 1-c/\log(\lvert t\rvert+2)$, gives $\psi(x) = x + O(xe^{-c'\sqrt{\log x}})$; the Vinogradov–Korobov region gives $x\exp(-c'(\log x)^{3/5}/(\log\log x)^{1/5})$; and the Riemann hypothesis would give the optimal $O(\sqrt x\log^2x)$. The prime number theorem is equivalent to the vanishing of the summatory Möbius function, $\sum_{n\leq x}\mu(n)=o(x)$, and to the nonvanishing of $\zeta$ on the line $\Re s=1$; it was proved by Hadamard and de la Vallée Poussin in 1896 and, without complex analysis, by Erdős and Selberg in 1949, the elementary method supplying the main term but no error term, from the identity $\sum_{p\leq x}(\log p)^2+\sum_{pq\leq x}\log p\log q = 2x\log x+O(x)$. The same proof applies to the arithmetic progressions, giving $\pi(x;q,a)\sim \mathrm{Li}(x)/\varphi(q)$ for fixed $q$, and to a number field, giving the prime ideal theorem $\psi_K(x)\sim x$ from the Dedekind zeta function; in short intervals the theorem is known for intervals of length $x^{0.525}$ and, conditionally, for $x^{1/2+\epsilon}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi(x)$ | Number of primes $\leq x$ |
| $\pi(x;q,a)$ | Number of primes $\leq x$ in the progression $a \bmod q$ |
| $\Lambda(n)$ | Von Mangoldt function |
| $\psi(x)$, $\theta(x)$ | Chebyshev functions $\sum_{n\leq x}\Lambda(n)$, $\sum_{p\leq x}\log p$ |
| $\mathrm{Li}(x)$ | Logarithmic integral $\int_2^x dt/\log t$ |
| $p_n$ | The $n$-th prime |
| $\rho = \beta+i\gamma$ | Nontrivial zero of $\zeta$ |
| $-\zeta'(s)/\zeta(s) = \sum\Lambda(n)n^{-s}$ | Logarithmic derivative, the Dirichlet series of $\Lambda$ |
| $g(s) = \int_1^\infty A(x)x^{-s-1}dx$ | Mellin transform of $A$ |
| $H(s) + c/(s-1)$ | Principal part of the Mellin transform at $s=1$ |
| $\zeta_K$, $\psi_K$, $\pi_K$ | Dedekind zeta function and the Chebyshev and prime counts of a number field |
| $N(\mathfrak{p})$ | Absolute norm of a prime ideal |
| $\varphi(q)$ | Euler function; order of $(\mathbb{Z}/q\mathbb{Z})^\times$ |
| $c$, $c'$ | Positive constants, not necessarily the same at each occurrence |



## Further Reading

- Jacques Hadamard, *Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques* (Bulletin de la Société Mathématique de France 24, 1896), for the first proof of the prime number theorem.
- Charles-Jean de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers* (Annales de la Société Scientifique de Bruxelles 20, 1896), for the independent proof and the zero-free region.
- Bernhard Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Größe* (Monatsberichte der Berliner Akademie, 1859), for the reduction of the problem to the zeros.
- Atle Selberg, *An elementary proof of the prime-number theorem* (Annals of Mathematics 50, 1949), and Paul Erdős, *On a new method in elementary number theory which leads to an elementary proof of the prime number theorem* (Proceedings of the National Academy of Sciences 35, 1949), for the elementary proof.
- Donald J. Newman, *Simple analytic proof of the prime number theorem* (American Mathematical Monthly 87, 1980), for the short tauberian proof reproduced here.
- Norbert Wiener, *The Fourier integral and certain of its applications* (Cambridge University Press, 1933), for the Wiener–Ikehara theorem and the tauberian theory behind it.
- Hugh L. Montgomery and Robert C. Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the proof with the zero-free region, the equivalences and the error terms.
- Roger Baker, Glyn Harman and Janos Pintz, *The difference between consecutive primes II* (Proceedings of the London Mathematical Society 83, 2001), for the prime number theorem in short intervals with the exponent $0.525$.
- Ivan M. Vinogradov, *A new proof of Waring's theorem* (Izvestiya Akademii Nauk SSSR 4, 1934), and Nikolai M. Korobov, *Estimates of trigonometric sums and their applications* (Uspekhi Matematicheskikh Nauk 13, 1958), for the sharpest known unconditional zero-free region and error term.
