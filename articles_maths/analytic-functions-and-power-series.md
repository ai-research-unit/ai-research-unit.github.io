
# __Analytic Functions and Power Series__

## Introduction

A power series is the first object of analysis that is written in the language of algebra: a formal sum $\sum_n a_n x^n$, which is an element of the ring $k[[x]]$ of Part I, acquires a numerical value at a point $x$ only once a limit is available. The theory of the article is the passage from the formal object to the function. Over a valued field there is a distinguished set — the disc of convergence — on which the sum exists, and on that disc the sum can be added, multiplied, composed, differentiated and antidifferentiated term by term. The radius of the disc is computed from the coefficients alone, and the two cases of the theory, the Archimedean and the non-Archimedean, share the formula and differ in almost everything that follows from it: in the Archimedean case the boundary of the disc is delicate and the sum is only locally controlled, while in the non-Archimedean case convergence at one interior point already gives uniform convergence on the whole closed sub-disc, a rigidity with no Archimedean analogue.

This article develops the general theory over a complete valued field: the convergence of series, the radius of convergence and the description of the domain, analytic functions as functions locally represented by power series, the identity theorem, term-by-term differentiation and antidifferentiation, and the three principal series of elementary analysis — the exponential, the logarithm and the binomial series — with the explicit radii and functional equations. It then records, in the last two sections, where the classical theory that a reader brings from real analysis fails: over an incomplete field, over a field without an order, and in characteristic $p$.

The prerequisites are *Absolute Values, Valuations and Completions* for absolute values, valuations, completions and the ultrametric geometry of balls, and *Formal Power Series and Completion* for the formal-algebraic side of the matter; uniform convergence and the Weierstrass test are the vocabulary of *Modes of Convergence*. The article is the analysis of a general valued field and not of a particular one: the analytic theory of $\mathbb{Q}_p$ and of $\mathbb{C}_p$ is the subject, the affinoid theory and the maximum modulus principle for the Tate algebra belong, and the complex theory — Cauchy's theorem, the residue calculus, conformal maps — belongs in the synthetic part of the corpus, where the system is fixed and the whole ladder is traversed for it. The order-theoretic theory of the real line isin that same part. The differential equations that power series solve belong when the field is non-Archimedean. No physics is invoked.

Throughout, $F$ is a field with a nontrivial absolute value $\lvert \cdot \rvert$, complete unless stated, with valuation ring $\mathcal{O}$, maximal ideal $\mathfrak{m}$ and residue field $k$; the completion is written $\widehat{F}$. The characteristic is zero except in the section that removes that hypothesis, and a uniformiser of a discretely valued $F$ is written $\pi$. Power series are written $\sum_{n \geq 0} a_n (x-a)^n$ with $a_n \in F$, and a disc of centre $a$ and radius $r > 0$ is

$$
B(a, r) = \{x \in F : \lvert x - a \rvert < r\}, \qquad \overline{B}(a, r) = \{x \in F : \lvert x - a \rvert \leq r\}.
$$

## Valued Fields and Convergence of Series

### Series in a Complete Valued Field

A series $\sum_{n \geq 0} a_n$ in a valued field converges if its partial sums $s_N = \sum_{n \leq N} a_n$ converge, and the sum is the limit. The elementary facts are collected in *Absolute Values, Valuations and Completions*; the ones used below are these.

**Proposition.** Let $F$ be complete and let $\sum_n a_n$ be a series in $F$.

**(a)** If $\sum_n \lvert a_n \rvert < \infty$ the series converges, and $\lvert \sum_n a_n \rvert \leq \sum_n \lvert a_n \rvert$; such a series is **absolutely convergent**.

**(b)** If $\lvert \cdot \rvert$ is non-Archimedean, the series converges if and only if $a_n \to 0$, and then $\lvert \sum_n a_n \rvert \leq \max_n \lvert a_n \rvert$ whenever the maximum exists. For a non-Archimedean field, convergence and absolute convergence coincide, and a convergent series may be rearranged at will.

**(c)** If $\sum_n \lvert a_n \rvert < \infty$ then every rearrangement converges to the same sum, and the series may be grouped and bracketed freely.

**Proof.** (a) is the completeness of $F$ applied to the Cauchy sequence of partial sums and the triangle inequality for the sum. In (b) the telescoping estimate $\lvert s_M - s_N \rvert = \lvert \sum_{N < n \leq M} a_n \rvert \leq \max_{N < n \leq M} \lvert a_n \rvert$ shows that $s_N$ is Cauchy exactly when $a_n \to 0$. (c) is the standard rearrangement argument, valid for absolutely convergent series over a complete Archimedean field and for all convergent series over a non-Archimedean one. $\square$

The contrast recorded in (b) is the first place where the two cases part company. Over $\mathbb{R}$ the harmonic series $\sum 1/n$ diverges although its terms tend to $0$; over a non-Archimedean field no such series exists. Conditionally convergent series and the rearrangement paradoxes they generate belong to the Archimedean case alone.

### Uniform Convergence of Series

When the terms depend on a parameter the relevant notion is uniform convergence, in the sense fixed by *Modes of Convergence*.

**Definition.** Let $X$ be a set and let $f_n : X \to F$ be functions. The series $\sum_n f_n$ **converges uniformly** on $X$ if the partial sums converge uniformly, and **normally** if $\sum_n \lVert f_n \rVert_\infty < \infty$.

**Theorem (Weierstrass test).** Let $F$ be complete and let $\sum_n \lVert f_n \rVert_\infty < \infty$. Then $\sum_n f_n$ converges uniformly and absolutely on $X$, its sum is continuous whenever the $f_n$ are continuous, and term-by-term differentiation and integration are licensed by the theorems of *Modes of Convergence*.

**Proof.** The partial sums are Cauchy for the supremum norm, since $\lVert \sum_{n=p}^{q} f_n \rVert_\infty \leq \sum_{n=p}^q \lVert f_n \rVert_\infty$, and the space of bounded functions is complete for that norm. Continuity follows from the uniform convergence of continuous functions. $\square$

In the non-Archimedean case the supremum norm satisfies the stronger inequality $\lVert \sum_n f_n \rVert_\infty \leq \max_n \lVert f_n \rVert_\infty$, so a series of functions is uniformly convergent as soon as $f_n \to 0$ uniformly, and the hypothesis of the test can be weakened to that. This is the form of the test that the $p$-adic theory uses.

## Power Series and the Radius of Convergence

### The Radius of Convergence

**Definition.** A **power series** about $a \in F$ is a series of functions

$$
f(x) = \sum_{n \geq 0} a_n (x - a)^n, \qquad a_n \in F .
$$

The **radius of convergence** of the series is

$$
R = \frac{1}{\limsup_{n \to \infty} \lvert a_n \rvert^{1/n}} \in [0, +\infty],
$$

where $R = 0$ when the limsup is $+\infty$ and $R = +\infty$ when the limsup is $0$. The **disc of convergence** is the set of $x$ with $\lvert x - a \rvert < R$.

The radius is a real number or an infinity, computed from the coefficients, and the two extremal cases occur: $\sum_n n!\,x^n$ has $R = 0$ and converges only at $x = 0$, and $\sum_n x^n/n!$ has $R = +\infty$.

**Theorem (Cauchy–Hadamard).** Let $f(x) = \sum_n a_n (x-a)^n$ have radius of convergence $R$.

**(a)** If $\lvert x - a \rvert < R$ then the series converges absolutely, and it converges uniformly on $\overline{B}(a, r)$ for every $r < R$.

**(b)** If $\lvert x - a \rvert > R$ then the terms $a_n (x-a)^n$ do not tend to $0$ and the series diverges.

**(c)** In the non-Archimedean case the convergence in (a) is uniform on the closed disc of radius $\lvert x - a \rvert$ itself, whenever the series converges at a point $x$ with $\lvert x - a \rvert < R$: the series converges at $x$ if and only if $\lvert a_n \rvert \lvert x - a \rvert^n \to 0$.

**Proof.** Let $\rho = \limsup_n \lvert a_n \rvert^{1/n}$ and let $\lvert x - a \rvert = r$. If $r < R$, that is $r\rho < 1$, choose $r'$ with $r < r' < R$; then $\lvert a_n \rvert^{1/n} \leq 1/r'$ for all large $n$, so $\lvert a_n \rvert r^n \leq (r/r')^n$, and the geometric bound gives absolute convergence. Uniformity on $\overline{B}(a,r)$ follows because the bound $(r/r')^n$ is independent of the point. If $r > R$, then $\lvert a_n \rvert^{1/n} \geq 1/r'$ for infinitely many $n$ and some $r'$ with $R < r' < r$, so $\lvert a_n \rvert r^n \geq (r/r')^n \to \infty$ along that subsequence and the terms do not tend to $0$. In the non-Archimedean case the bound $\lvert a_n \rvert s^n \leq \lvert a_n \rvert r^n$ for every $s \leq r$ is uniform in $s$, and the criterion of the previous section makes the convergence equivalent to $\lvert a_n \rvert r^n \to 0$. $\square$

Part (c) is the **rigidity** of the non-Archimedean disc: a single convergent point drags the whole closed disc of that radius with it. There is no such statement over $\mathbb{R}$: the geometric series $\sum_nx^n$ converges at $x = 1/2$, and indeed at every point of $[1/2,1)$, yet not uniformly on that interval.

### The Domain of Convergence

**Theorem.** Let $R$ be the radius of a power series $f$. On the disc $B(a, R)$ the sum $f$ is continuous and the series may be differentiated and antidifferentiated term by term; on the complement of the closed disc $\overline{B}(a,R)$ the series diverges. On the sphere $\lvert x - a \rvert = R$ every behaviour is possible.

**(a)** In the Archimedean case: $\sum_n x^n$ has $R = 1$ and diverges at every point of $\lvert x \rvert = 1$; $\sum_n x^n/n^2$ has $R = 1$ and converges at every point of $\lvert x \rvert = 1$; $\sum_n x^n/n$ has $R = 1$ and converges at $x = -1$ and diverges at $x = 1$.

**(b)** In the non-Archimedean case, whether the series converges at a point of the sphere $\lvert x - a \rvert = R$ depends only on the radius $R$ and not on the point: it converges at every point of the sphere, or at none, according to whether $\lvert a_n \rvert R^n \to 0$. Both behaviours occur. The geometric series $\sum_n x^n$ and the logarithmic series $\sum_n x^n/n$ both have radius $1$ and diverge at every point of $\lvert x \rvert = 1$: the first because its terms have absolute value $1$ there, the second because $\lvert 1/n \rvert$ equals $\lvert p \rvert^{-v_p(n)}$, which is unbounded along $n = p^k$. On the other hand, for $0 < \lvert t \rvert < 1$ the series $\sum_n t^{\lfloor\sqrt n\rfloor}x^n$ has radius $1$, since $\lvert t \rvert^{\lfloor\sqrt n\rfloor/n} \to \lvert t \rvert^{0} = 1$, and converges at every point of the sphere, since $\lvert t \rvert^{\lfloor\sqrt n\rfloor} \to 0$. The Archimedean example of (a) does not transfer: the coefficients $1/n^2$ are units of $\mathcal{O}$ whenever $p \nmid n$, so $\sum_n x^n/n^2$ diverges at every point of the sphere in the non-Archimedean case as well.

**Proof.** Continuity and term-by-term operations on $B(a,R)$ are consequences of the uniformity of the convergence on each $\overline{B}(a,r)$ with $r < R$, by the theorems of *Modes of Convergence*. Divergence off the closed disc is Cauchy–Hadamard (b). In (b) the quantity $\lvert a_n (x-a)^n \rvert = \lvert a_n \rvert R^n$ is independent of the point of the sphere, and the non-Archimedean convergence criterion depends only on these numbers. $\square$

The non-Archimedean case has no analogue of the delicate boundary behaviour of the Archimedean case, and this is the same rigidity as before: the absolute value of the $n$-th term at a boundary point is a function of the radius alone. Over an algebraically closed non-Archimedean field with dense value group the convergence disc is not merely open but is a union of closed balls of radii $< R$, and the "generic" values of $\lvert x - a \rvert$ make the convergence set neither the open disc nor the closed disc of any fixed radius; the honest statement is the one above.

## Analytic Functions

### Definition and Elementary Properties

**Definition.** Let $F$ be a complete valued field and $U \subseteq F$ open. A function $f : U \to F$ is **analytic on $U$** if for every $a \in U$ there is a power series $\sum_n c_n (x-a)^n$ with positive radius of convergence whose sum agrees with $f$ on $B(a,\rho)$ for some $\rho > 0$. The set of analytic functions on $U$ is written $\mathcal{O}(U)$.

The definition is local: analyticity is a property of the germ of $f$ at each point, and it is inherited by restrictions to smaller open sets. A polynomial is analytic on $F$, and a power series with radius $R$ is analytic on its disc of convergence, with the expansion about any interior point $a$ obtained by expanding $(x - b)^n = ((x-a) + (a-b))^n$ and regrouping; the regrouping is legitimate because the resulting double series converges absolutely in the Archimedean case, and because its terms tend to $0$ in each variable in the non-Archimedean case.

**Theorem.** Let $f$ be analytic on $U$. Then:

**(a)** $f$ is continuous on $U$;

**(b)** $f$ is differentiable on $U$, in the sense that

$$
f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}
$$

exists for every $a \in U$, and $f'$ is analytic on $U$, with $f'(x) = \sum_n n\,c_n (x-a)^{n-1}$ on a neighbourhood of $a$;

**(c)** if $f$ is analytic and $f(a) \neq 0$ then $1/f$ is analytic on a neighbourhood of $a$;

**(d)** the sum and the product of analytic functions are analytic, and the composition $f \circ g$ of analytic functions is analytic wherever it is defined.

**Proof sketch.** (a) A power series is continuous on its disc by Cauchy–Hadamard and the Weierstrass test. (b) The usual algebraic division of the difference quotient gives $\bigl(\sum_{n \leq N} c_n ((a+h)^n - a^n)\bigr)/h = \sum_{n \leq N} c_n \sum_{k<n} a^{n-1-k}(a+h)^k$, and the limit as $N \to \infty$ and then $h \to 0$ is $\sum_n n c_n a^{n-1}$; the interchange of the two limits is licensed by the uniform convergence on a small disc. Denominators are avoided because $h \neq 0$ is a field element. (c) and (d) are the standard manipulations of absolutely convergent series, and in the non-Archimedean case the manipulations are simpler because every rearrangement is legitimate. $\square$

The derivative makes sense over any topological field, because the difference quotient is formed by division in the field and its limit requires only the topology; no order is needed, and this is why the theory is available in the non-Archimedean case while the mean value theorem is not.

### The Identity Theorem

**Theorem (identity theorem).** Let $F$ be complete of characteristic $0$, let $B(a,R)$ be a disc of positive radius and let $f = \sum_n c_n (x-a)^n$ converge on it. If $f$ vanishes on a nonempty open subset of $B(a,R)$, then $c_n = 0$ for every $n$ and $f$ is the zero function.

**Proof.** Suppose $f = 0$ on $B(b,s) \subseteq B(a,R)$. Expand $f$ about $b$:

$$
f(x) = \sum_{m \geq 0} d_m (x-b)^m, \qquad d_m = \sum_{n \geq m} \binom{n}{m} c_n (b-a)^{n-m} .
$$

The expansion is valid on $B(b, \lvert b - a \rvert + s')$ for some $s' > 0$ by the regrouping of the absolutely convergent (Archimedean) or termwise-vanishing (non-Archimedean) double series. Since $f$ vanishes on $B(b,s)$, its derivatives at $b$ vanish, so $d_m = f^{(m)}(b)/m! = 0$ for every $m$. The triangular system $d_m = \sum_{n \geq m} \binom{n}{m} c_n (b-a)^{n-m}$ with the coefficients $d_m$ all zero is solved recursively for the $c_n$: the diagonal coefficient is $\binom{m}{m}=1$ and the division by the binomial coefficients is legitimate in characteristic $0$, so $c_0 = d_0 = 0$, then $c_1 = d_1 = 0$, and so on. Hence $f$ is the zero series. $\square$

**Corollary (uniqueness of analytic continuation).** If $f$ and $g$ are analytic on a disc and agree on a nonempty open subset, then $f = g$ on the disc, and in particular a nonzero analytic function on a disc has isolated zeros: if $f(a) = 0$ and $f$ is not identically zero, then $f(x) = (x-a)^m h(x)$ with $h(a) \neq 0$ and $f$ is nonzero on a punctured neighbourhood of $a$.

**Proof.** Apply the theorem to $f - g$, and for the second statement divide the expansion at $a$ by the lowest power of $(x-a)$ that occurs: the quotient is analytic and nonzero at $a$, hence nonzero near $a$ by continuity. $\square$

Over the real line the classical statement adds the hypothesis that the agreement set has an accumulation point; over a complete valued field the result as stated is stronger in the non-Archimedean case, because an open ball there is also closed and the "open subset" of the hypothesis may be a single ball. What is essential in the proof is characteristic $0$ and completeness: the coefficients $d_m$ are obtained as limits, and the recursion for the $c_n$ divides by binomial coefficients.

## Differentiation and Antidifferentiation

**Definition.** Let $\sum_n a_n (x-a)^n$ be a power series. Its **formal derivative** is the series $\sum_{n \geq 1} n\,a_n (x-a)^{n-1}$, and its **formal primitive** is $\sum_{n\geq0} \frac{a_n}{n+1}(x-a)^{n+1}$.

**Proposition.** Differentiation and antidifferentiation preserve the radius of convergence.

**Proof.** The $n$-th coefficient of the derivative is $(n+1)a_{n+1}$, and $\lvert (n+1) a_{n+1} \rvert^{1/n} = \bigl(\lvert a_{n+1} \rvert^{1/(n+1)}\bigr)^{(n+1)/n} (n+1)^{1/n} \to \limsup \lvert a_n \rvert^{1/n}$, since $(n+1)^{1/n} \to 1$ and the two exponents agree in the limit. The primitive is the same computation. $\square$

**Theorem.** Let $f = \sum_n a_n (x-a)^n$ have radius $R > 0$.

**(a)** $f$ is differentiable on $B(a,R)$ and $f' = \sum_n n a_n (x-a)^{n-1}$ there, the derivative having the same radius.

**(b)** If $F$ is archimedean and $f$ is differentiable with $f' = 0$ on the disc, then $f$ is constant. If $F$ is non-Archimedean and of characteristic $0$, the same holds.

**(c)** Conversely, every analytic function $g$ on $B(a,R)$ has a primitive $G$ on the disc with $G' = g$, unique up to an additive constant, given by the termwise primitive of the expansion.

**Proof.** (a) is the differentiation theorem for a uniformly convergent series applied on smaller discs. For (b) in the Archimedean case the mean value theorem gives $f(x) - f(y) = f'(\xi)(x-y) = 0$; in the non-Archimedean case the hypothesis of characteristic $0$ makes the same conclusion available from the coefficient expansion, since the expansion about $a$ has all higher coefficients $f^{(n)}(a)/n!$ vanishing and the formula for the primitive is the unique solution of $G' = g$ with the prescribed constant. (c) is the termwise construction and the radius computation above. $\square$

Part (b) is a place where the two cases diverge in hypothesis rather than in conclusion: the non-Archimedean statement requires characteristic $0$, and the reason is the failure recorded at the end of this article, where in characteristic $p$ a nonconstant analytic function can have identically vanishing derivative.

## The Exponential, the Logarithm and the Binomial Series

### The Exponential

**Definition.** The exponential is the power series

$$
\exp x = \sum_{n \geq 0} \frac{x^n}{n!}.
$$

**Theorem.** Let $F$ be complete and non-Archimedean, with residue field $k$ of characteristic $p > 0$ unless stated, and let $\lvert p \rvert$ be the absolute value of the prime $p$ of the prime subfield.

**(a)** If $k$ has characteristic $p > 0$ the radius of convergence of $\exp$ is $\rho_{\exp} = \lvert p \rvert^{1/(p-1)} < 1$. If $k$ has characteristic $0$ then $\lvert n \rvert = 1$ for every positive integer $n$, so the radius is $1$. Over an Archimedean complete field, $\mathbb{R}$ or $\mathbb{C}$, the radius is $+\infty$.

**(b)** $\exp(x+y) = \exp x \cdot \exp y$ whenever $\lvert x \rvert, \lvert y \rvert < \rho_{\exp}$ and the two series and that of $x+y$ converge.

**(c)** In the discretely valued case $\rho_{\exp} = p^{-1/(p-1)}$ when $\lvert p \rvert = p^{-1}$; the disc $\lvert x \rvert < \rho_{\exp}$ therefore contains the ball $p\mathcal{O}$ when $p > 2$ and the ball $4\mathcal{O}$ when $p = 2$.

**Proof.** (a) By Legendre's formula $v(n!) = (n - s_p(n))/(p-1)$ for the valuation normalised by $v(p) = 1$, where $s_p(n)$ is the sum of the base-$p$ digits of $n$. Writing $\lvert \cdot \rvert = q^{-v(\cdot)}$ with $q = \lvert p \rvert^{-1} > 1$, one has

$$
v(n!) = \frac{n - s_p(n)}{p-1}, \qquad \bigl\lvert 1/n! \bigr\rvert^{1/n} = q^{-(n - s_p(n))/((p-1)n)} \longrightarrow q^{-1/(p-1)} = \lvert p \rvert^{1/(p-1)},
$$

since $s_p(n) \leq (p-1)(1 + \log_p n)$ is negligible against $n$. When $k$ has characteristic $0$ there is no such prime and $v(n!) = 0$ for every $n$, so the radius is $1$. (b) is the binomial theorem $\exp x \exp y = \sum_{m,n} x^m y^n/(m! n!) = \sum_N (x+y)^N/N!$; the double series converges absolutely in the Archimedean case and termwise to $0$ in the non-Archimedean case, because $\lvert x \rvert, \lvert y \rvert < \rho_{\exp}$ forces $x^n/n! \to 0$ and $y^n/n! \to 0$, and the sum $x+y$ satisfies $\lvert x + y \rvert \leq \max\{\lvert x \rvert, \lvert y \rvert\} < \rho_{\exp}$ in the non-Archimedean case. In (c) the normalisation $\lvert p \rvert = p^{-1}$ gives $\rho_{\exp} = p^{-1/(p-1)}$, which is $> p^{-1}$ for $p>2$, so the ball of radius $p^{-1}$ is contained in the disc of convergence, while for $p=2$ one has $\rho_{\exp} = 2^{-1}$ and the open disc $\lvert x \rvert < 2^{-1}$ is the ball $4\mathcal{O}$. $\square$

**Example.** In $\mathbb{Q}_5$, $\exp$ converges on $5\mathbb{Z}_5$ and not on $\mathbb{Z}_5$; the value $\exp 5$ is a $5$-adic number whose reduction is $1$. In $\mathbb{R}$, $\exp$ converges everywhere and is unbounded; the non-Archimedean exponential is bounded on every disc of radius $< \rho_{\exp}$ by the maximum of $\lvert x^n/n! \rvert$, a consequence of the rigidity of the next section.

### The Logarithm

**Definition.** The logarithm is the power series

$$
\log(1+x) = \sum_{n \geq 1} \frac{(-1)^{n+1}}{n} x^n, \qquad \log' (1+x) = \frac{1}{1+x}.
$$

**Theorem.** Let $F$ be complete.

**(a)** The radius of convergence of $\log(1+x)$ is $1$. In the Archimedean case the series converges at $x = 1$ and diverges at $x = -1$, so its interval of convergence is $(-1,1]$. In the non-Archimedean case the series converges exactly on the open unit disc and diverges at every point of the sphere $\lvert x \rvert = 1$: the $n$-th term at such a point has absolute value $\lvert 1/n \rvert$, which is unbounded because it equals $\lvert p \rvert^{-v_p(n)}$ for the integers $n = p^k$.

**(b)** $\log\bigl((1+x)(1+y)\bigr) = \log(1+x) + \log(1+y)$ as an identity of formal power series in $x$ and $y$, hence wherever the three series converge; in the non-Archimedean case this holds for $\lvert x \rvert, \lvert y \rvert < 1$, and consequently $\log\bigl((1+x)^n\bigr) = n \log(1+x)$ for every $n \in \mathbb{Z}$.

**(c)** $\exp \log(1+x) = 1 + x$ for $\lvert x \rvert < \min(1, \rho_{\exp})$, and $\log \exp x = x$ whenever $\lvert \exp x - 1 \rvert < 1$, which in the non-Archimedean case holds for every $\lvert x \rvert < \rho_{\exp}$.

**Proof.** (a) Since $\lvert 1/n \rvert \leq 1$, the radius is $\lim \lvert 1/n \rvert^{-1/n} = 1$; the boundary statement is the non-Archimedean convergence criterion. (b) Both sides are formal power series in $x$ and $y$ with rational coefficients, and both have the same derivative with respect to $x$, namely $\sum_{n \geq 0} (-1)^n x^n = 1/(1+x)$, the two denominators differing by the factor $1+y$ that cancels; both vanish at $x = 0$. Their difference, regarded as a formal power series in $x$ over the field of formal Laurent series in $y$, therefore has zero derivative and vanishes at $x = 0$, so it is zero; this is the case $f' = 0$ of the differentiation theorem above, valid in characteristic $0$. Convergence of the rearranged series at a point follows from the convergence of the three series at that point. (c) Substituting the logarithm series into the exponential and collecting by degree gives the identity of formal power series $\exp\log(1+x) = 1+x$, because the derivative of the left side is $\exp\log(1+x) \cdot (1/(1+x)) = 1$ whenever it is defined and the value at $x=0$ is $1$, and the right side has the same derivative and value; the second identity is the symmetry obtained by interchanging the roles of $\exp$ and $\log$. $\square$

**Remark (the logarithm and the principal units).** When $F$ is a non-Archimedean local field with uniformiser $\pi$ and residue characteristic $p$, the logarithmic series converges on the open unit ball $B(0,1) = \mathfrak{m}$ and the exponential on the ball $\lvert x \rvert < \rho_{\exp}$. On the disc where both converge the two are mutually inverse, and the resulting isomorphism between a principal-unit group and an additive subgroup of $F$, with the exceptional behaviour for $p = 2$, is made precise. What is used here is only the convergence radius and the functional equations.

### The Binomial Series

**Definition.** For $\alpha \in F$ put $\binom{\alpha}{n} = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$ and define

$$
(1+x)^{\alpha} = \sum_{n \geq 0} \binom{\alpha}{n} x^n .
$$

**Theorem.** Let $F$ be non-Archimedean, complete, with residue characteristic $p$, and let $\alpha \in \mathcal{O}$.

**(a)** The radius of convergence is $\geq 1$ and is exactly $1$ when $\alpha \notin \mathbb{Z}_{\geq 0}$ and the residue field has characteristic $0$.

**(b)** If $\alpha \in \mathbb{Z}$, the series terminates when $\alpha \geq 0$ and has radius $1$ when $\alpha < 0$.

**(c)** The coefficients satisfy $\lvert \binom{\alpha}{n} \rvert \leq 1$, so the series converges on the open unit disc; but $\binom{\alpha}{n}$ does not tend to $0$ unless $\alpha \in \mathbb{Z}_{\geq 0}$, and the series converges on the closed unit disc $\lvert x \rvert \leq 1$ only in that terminating case. Indeed for $\alpha \in \mathcal{O}$ and $n = p^k$ one has $\lvert \binom{\alpha}{p^k} \rvert \geq 1$: the coefficients are bounded but do not decay.

**(d)** $(1+x)^{\alpha}(1+x)^{\beta} = (1+x)^{\alpha+\beta}$ for $\lvert x \rvert < 1$ and $\alpha, \beta \in \mathcal{O}$, and $\frac{d}{dx}(1+x)^\alpha = \alpha (1+x)^{\alpha-1}$.

**Proof sketch.** For (c), $\binom{x}{n}$ is an integer-valued polynomial, so its values on $\mathbb{Z}_{\geq 0}$ lie in $\mathcal{O}$; those values are continuous in the variable $\alpha$ and $\mathbb{Z}_{\geq 0}$ is dense in $\mathcal{O}$, so $\binom{\alpha}{n} \in \mathcal{O}$ and $\lvert \binom{\alpha}{n} \rvert \leq 1$ for $\alpha \in \mathcal{O}$, whence the radius is at least $1$. For the non-decay, write $\binom{\alpha}{p^k} = \prod_{j=0}^{p^k-1}(\alpha - j)/p^k!$; the numerator has $v(p^k)! = (p^k-1)/(p-1)$ accounted for by the residue classes modulo the powers of $p$ below $p^k$, and the remaining contributions only increase its valuation, so $v\bigl(\binom{\alpha}{p^k}\bigr) \geq 0$, that is $\lvert \binom{\alpha}{p^k} \rvert \geq 1$, for every $k$; a coefficient sequence with this property cannot tend to $0$. The identity (d) is the binomial theorem, valid by the absolute convergence of the Cauchy product on the open unit disc; the derivative is termwise. $\square$

The binomial series is the standard tool for the logarithm and for the structure of the principal units: for $\alpha$ in the valuation ring the coefficients $\binom{\alpha}{n}$ are bounded by $1$, the interpolated power $x \mapsto (1+x)^{\alpha}$ is defined on the open unit disc, and the continuity of the map $\alpha \mapsto \binom{\alpha}{n}$ on the valuation ring is what makes the interpolated power continuous in its parameter.

## Where the Classical Theory Fails

### Incomplete Fields

The constructions above use completeness twice: to know that a convergent series has a sum in the field, and to know that the coefficients of a power series are recovered as limits of derivatives. Over an incomplete field both uses fail, and the remedy is to replace $F$ by its completion.

**Remark (the natural domain is a disc in the completion).** Let $\lvert \cdot \rvert$ be an absolute value on $F$ and let $\widehat{F}$ be the completion. A power series with coefficients in $F$ has a radius $R$ computed in $\mathbb{R}$, and its sum is defined on a disc in $\widehat{F}$; the points of that disc that lie in $F$ give values in $F$ only when the sum happens to lie in $F$, which is not automatic. For example, with $F = \mathbb{Q}$ and the usual absolute value, $\sum_n x^n/n!$ evaluated at $x = 1$ gives $e \notin \mathbb{Q}$. The honest theory over an incomplete field is therefore the theory over $\widehat{F}$ restricted to $F$; questions of rationality of the values belong to arithmetic, not to analysis.

**Remark (where completeness is used in the identity theorem).** The proof of the identity theorem obtained the Taylor coefficients as limits of derivatives, so completeness is used in the identification of the coefficients of the expansion about $b$. Over an incomplete field the series may converge on a disc in the completion without its expansion about an interior point converging back in $F$; the identity theorem as stated is a theorem about complete fields. Over $\mathbb{R}$ and $\mathbb{C}$, and over $\mathbb{Q}_p$ and its finite extensions, it holds.

### Fields Without an Order

The real theory of analytic functions rests on the order of $\mathbb{R}$ through three theorems: the intermediate value theorem, Rolle's theorem, and the mean value theorem. None of them survives in the general valued field.

**Remark (the replacements, and where each lives).** Over $\mathbb{C}$, and over any non-Archimedean field, there is no order compatible with the field operations. The mean value theorem for the derivative is unavailable, and the interchange of a limit and a derivative in the form used for real functions must be replaced. Two substitutes exist in the corpus. Over $\mathbb{C}$ the substitute is the Cauchy integral and the maximum modulus principle, developed andin the synthetic part of the corpus. Over a non-Archimedean field the substitute is the ultrametric rigidity of series, developed in the next section , for the higher-dimensional theory. The differentiation theorem of this article is stated for power series, where no order is needed, and the general differentiation theory of Part III — which does use the mean value theorem — is restricted to the real and complex cases and belongs.

### Characteristic $p$

Let $F$ be complete of characteristic $p > 0$, such as $\mathbb{F}_p((t))$ with the $t$-adic absolute value. The formulas for the derivative and for the coefficients change qualitatively, because the integer $n$ may vanish in $F$.

**Remark (three failures).**

**(a)** The derivative of a nonconstant analytic function may vanish identically: if $f(x) = x^p$ then $f'(x) = p x^{p-1} = 0$. Hence the implication "$f' = 0 \Rightarrow f$ constant" fails, and with it the real-analysis proof of that fact.

**(b)** The exponential and the logarithm degenerate: $n! = 0$ for $n \geq p$ in the prime field, so $\exp x = \sum_{n < p} x^n/n!$ is a polynomial of degree $p-1$, and the logarithm is defined only on the range on which $1+x$ is a $p$-th power of a convergent series; the functional equations hold only on the small disc where the relevant series have meaning.

**(c)** The identity theorem's recursion fails because the binomial coefficients $\binom{n}{m}$ can vanish in characteristic $p$; the statement one keeps is the one in which the zero set contains an open ball *and* the field has characteristic $0$. In characteristic $p$ a nonzero polynomial such as $x^p - x$ vanishes at every element of $\mathbb{F}_p$ without vanishing identically, so the "vanishing on a set" form of the identity theorem is false.

None of these failures is an accident of the hypotheses: each is the loss of a property of the characteristic-zero coefficient field. The theory of power series in characteristic $p$ is used in arithmetic — through the Artin–Hasse exponential $\prod_{p \nmid n} (1 - x^n)^{\mu(n)/n}$, which has integral coefficients and converges on the open unit disc, and through the Cartier operators — and the relevant statements are collected.

## The Non-Archimedean Rigidity

The properties collected here are the ones that distinguish the non-Archimedean theory from the Archimedean one and are used repeatedly.

**Theorem (uniform convergence from one point).** Let $F$ be non-Archimedean and complete and let $f = \sum_n a_n (x-a)^n$ converge at $x = b$. Then the series converges uniformly on $\overline{B}(a, \lvert b - a \rvert)$, and its sum is continuous there.

**Proof.** For $\lvert x - a \rvert \leq \lvert b - a \rvert$ one has $\lvert a_n (x-a)^n \rvert \leq \lvert a_n (b-a)^n \rvert$, so the tail supremum is at most $\max_{n > N} \lvert a_n (b-a)^n \rvert$, which tends to $0$ because the series converges at $b$. $\square$

**Theorem (maximum modulus principle for a power series).** Let $F$ be non-Archimedean and complete with infinite residue field, let $f = \sum_n a_n x^n$ converge on $\overline{B}(0,r)$, and put $\lVert f \rVert_r = \sup_{\lvert x \rvert \leq r} \lvert f(x) \rvert$ and

$$
\lVert f \rVert_G = \max_{n \geq 0} \lvert a_n \rvert r^n ,
$$

the **Gauss norm** of $f$ at the radius $r$. Then $\lVert f \rVert_r = \lVert f \rVert_G$, and the supremum is attained: there is $x_0$ with $\lvert x_0 \rvert = r$ and $\lvert f(x_0) \rvert = \lVert f \rVert_G$.

**Proof sketch.** The inequality $\lVert f \rVert_r \leq \lVert f \rVert_G$ is the ultrametric inequality applied term by term at each point of the disc. For the reverse, let $F_0$ be the finite set of indices at which $\lvert a_n \rvert r^n$ is maximal and let

$$
P(\xi) = \sum_{n \in F_0} \tilde{a}_n \xi^n \in k[\xi] ,
$$

with $\tilde{a}_n$ the reduction of $a_n$; the polynomial $P$ is nonzero, its coefficient at $N = \max F_0$ being the unit $\tilde{a}_N$, so it has at most $\deg P$ roots and an infinite residue field contains a $\xi$ with $P(\xi) \neq 0$. Choose $x_0$ with $\lvert x_0 \rvert = r$ and reduction $\xi$, which exists whenever $r$ lies in the value group. At $x_0$ the terms of index in $F_0$ all have absolute value $\lVert f \rVert_G$ and their sum is $a_N x_0^N P(\xi)/\tilde{a}_N$, of absolute value $\lVert f \rVert_G$ because $P(\xi) \neq 0$; every term of index outside $F_0$ is strictly smaller; hence $\lvert f(x_0) \rvert = \lVert f \rVert_G$ by the equality case of the ultrametric inequality. $\square$

**Remark (necessity of the hypothesis).** The identity fails over a finite residue field. Over $\mathbb{Q}_2$ and at $r = 1$ the series $f(x) = x + x^2$ has $\lVert f \rVert_G = 1$, while $\lvert x + x^2 \rvert = \lvert x \rvert\lvert 1 + x \rvert \leq \tfrac12$ for every $\lvert x \rvert \leq 1$: the two maximal coefficients cancel modulo the maximal ideal, since $1 + x$ is divisible by $2$ whenever $x$ is odd. The identity is restored over an extension with infinite residue field, the Gauss norm being unchanged by the extension.

The theorem is proved here for a single variable and a single disc; the general affinoid statement, in which the role of the maximum is taken by the spectral seminorm, is the subject of the several-variable theory, and the Weierstrass preparation theorem that factorises a power series on the unit disc by a polynomial is treated. What this article fixes is the rigidity: over a field with infinite residue field the size of an analytic function on a disc is read from its coefficients, and the maximal coefficients cannot cancel; over a finite residue field they can, which is why the hypothesis is not removable and why the several-variable theory replaces the supremum by the spectral seminorm.

## Summary

A power series over a complete valued field has a radius of convergence $R = 1/\limsup \lvert a_n \rvert^{1/n}$, converges absolutely and uniformly on every closed sub-disc of radius $< R$, and diverges outside the closed disc of radius $R$; on the boundary sphere the Archimedean behaviour is delicate and every possibility occurs, while in the non-Archimedean case convergence at one point of the sphere implies it at the whole sphere. In the non-Archimedean case convergence at an interior point gives uniform convergence on the whole closed disc of that radius, and for a non-Archimedean field convergence and absolute convergence coincide, so that a convergent series may be rearranged at will.

A function is analytic on an open set when it is locally the sum of a convergent power series. Analytic functions are continuous, closed under addition, multiplication, division by nonvanishing functions and composition, and differentiable with an analytic derivative given term by term; differentiation and antidifferentiation preserve the radius. The identity theorem — a power series over a complete field of characteristic zero that vanishes on a nonempty open set vanishes identically — makes the Taylor expansion unique and the zeros of a nonzero analytic function isolated.

The exponential has radius $\lvert p \rvert^{1/(p-1)}$ over a field of residue characteristic $p$, radius $1$ over a non-Archimedean field of residue characteristic $0$, where $\lvert n \rvert = 1$ for every $n$, and infinite radius over $\mathbb{R}$ and $\mathbb{C}$; the logarithm has radius $1$ and converges exactly on the open unit disc in the non-Archimedean case and on $(-1,1]$ in the real case; and the binomial series with parameter in the valuation ring has radius $1$ and coefficients bounded by $1$, so it converges on the open unit disc, while on the closed unit disc it converges only when it terminates. The classical theorems that fail are those that use completeness, an order, or the characteristic-zero coefficient field: over an incomplete field the sum lives in the completion, over a field without an order the mean value theorem is unavailable, and in characteristic $p$ the derivative may vanish identically and the exponential degenerates. The non-Archimedean replacement for the missing maximum principle of the real theory is the rigidity of the ultrametric estimate together with the maximum modulus principle for a power series, whose value on a disc is the largest coefficient term.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $\widehat{F}$ | Valued field, its completion |
| $\lvert \cdot \rvert$ | Absolute value |
| $\mathcal{O}$, $\mathfrak{m}$, $k$ | Valuation ring, maximal ideal, residue field |
| $p$ | Residue characteristic of a non-Archimedean $F$ |
| $\pi$ | Uniformiser of a discretely valued $F$ |
| $v$ | Valuation, $\lvert \cdot \rvert = q^{-v(\cdot)}$ |
| $B(a,r)$, $\overline{B}(a,r)$ | Open and closed discs of centre $a$, radius $r$ |
| $\sum_n a_n (x-a)^n$ | Power series about $a$ |
| $R$ | Radius of convergence $1/\limsup \lvert a_n \rvert^{1/n}$ |
| $\mathcal{O}(U)$ | Ring of analytic functions on $U$ |
| $f'$, $f^{(n)}$ | Derivative, $n$-th derivative |
| $\exp$, $\log$ | Exponential and logarithmic series |
| $\rho_{\exp} = \lvert p \rvert^{1/(p-1)}$ | Radius of convergence of the exponential |
| $(1+x)^\alpha$, $\binom{\alpha}{n}$ | Binomial series and binomial coefficients |
| $\lVert f \rVert_r$ | Supremum of $\lvert f \rvert$ on $\overline{B}(0,r)$ |
| $\lVert f \rVert_G$ | Gauss norm $\max_n \lvert a_n \rvert r^n$ |
| $s_p(n)$ | Sum of the base-$p$ digits of $n$ |





## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the exponential, the logarithm and the principal units over a local field.
- Neal Koblitz, *$p$-adic Numbers, $p$-adic Analysis, and Zeta-Functions*, 2nd ed. (Springer, 1984), for power series, the exponential and the logarithm over $\mathbb{Q}_p$ with worked examples.
- Alain M. Robert, *A Course in $p$-adic Analysis* (Springer, 2000), for the general theory of power series over a non-Archimedean field.
- Wim H. Schikhof, *Ultrametric Calculus* (Cambridge University Press, 1984), for analytic functions, the identity theorem and the maximum modulus principle in the ultrametric case.
- John B. Conway, *Functions of One Complex Variable*, 2nd ed. (Springer, 1978), for the Archimedean theory of power series and analytic functions.
- Walter Rudin, *Real and Complex Analysis*, 3rd ed. (McGraw-Hill, 1987), for power series on the real and complex line and the boundary behaviour of the disc.
- Paulo Ribenboim, *The Theory of Classical Valuations* (Springer, 1999), for absolute values, completions and the arithmetic of valued fields.
- Siegfried Bosch, *Lectures on Formal and Rigid Analytic Geometry* (Springer, 2014), for the passage from power series to affinoid algebras.
