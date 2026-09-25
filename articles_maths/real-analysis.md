# __Real Analysis__

## Introduction

This article introduces real analysis as the study of limits, continuity, differentiation, and integration on the real line. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The order and completeness of $\mathbb{R}$ are used throughout, and every topological notion is defined in terms of them. No abstract topology is assumed.

## The Real Line as a Metric Space

### Definition

The **distance** between two real numbers $a$ and $b$ is

$$
d(a, b) = |a - b|.
$$

It satisfies:

$$
d(a, b) \geq 0, \qquad d(a, b) = 0 \iff a = b,
$$

$$
d(a, b) = d(b, a),
$$

$$
d(a, c) \leq d(a, b) + d(b, c).
$$

The pair $(\mathbb{R}, d)$ is a **metric space**. Every notion in real analysis is defined in terms of this metric.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $a$ is

$$
B(a, r) = \{x \in \mathbb{R} : |x - a| < r\} = (a - r, a + r).
$$

The **closed ball** is

$$
\overline{B}(a, r) = \{x \in \mathbb{R} : |x - a| \leq r\} = [a - r, a + r].
$$

A **neighborhood** of $a$ is any set containing some $B(a, r)$.

### Open and Closed Sets

A set $U \subseteq \mathbb{R}$ is **open** if for every $a \in U$ there exists $r > 0$ with $B(a, r) \subseteq U$.

A set $F \subseteq \mathbb{R}$ is **closed** if its complement $\mathbb{R} \setminus F$ is open.

**Theorem.** The open sets of $\mathbb{R}$ are exactly the unions of open intervals.

**Theorem.** Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually, arbitrary intersections of closed sets are closed. Finite unions of closed sets are closed.

**Theorem.** A set $F$ is closed iff every convergent sequence in $F$ has its limit in $F$.

### Compactness

A set $K \subseteq \mathbb{R}$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{R}$ is compact iff it is closed and bounded.

**Theorem (Bolzano–Weierstrass).** Every bounded sequence in $\mathbb{R}$ has a convergent subsequence.

**Theorem.** A continuous real-valued function on a compact set is bounded and attains its maximum and minimum.

## Sequences and Series

### Convergence

A sequence $(a_n)$ of real numbers **converges** to $L \in \mathbb{R}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies |a_n - L| < \epsilon.
$$

We write $a_n \to L$ or $\lim_{n \to \infty} a_n = L$.

**Uniqueness.** If $a_n \to L$ and $a_n \to L'$, then $L = L'$.

**Boundedness.** Every convergent sequence is bounded. The converse fails: $(-1)^n$ is bounded but not convergent.

### Cauchy Sequences

A sequence $(a_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies |a_m - a_n| < \epsilon.
$$

**Theorem.** In $\mathbb{R}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{R}$ expressed in sequence form.

**Theorem.** Every subsequence of a convergent sequence converges to the same limit.

### Monotone Convergence

A sequence $(a_n)$ is **monotone increasing** if $a_{n+1} \geq a_n$ for all $n$.

**Theorem (Monotone Convergence).** Every bounded monotone sequence converges.

**Proof.** Suppose $(a_n)$ is monotone increasing and bounded above. Let $L = \sup \{a_n\}$. For $\epsilon > 0$, $L - \epsilon$ is not an upper bound, so there exists $N$ with $a_N > L - \epsilon$. By monotonicity, $n \geq N$ implies $L - \epsilon < a_n \leq L$. Hence $a_n \to L$. $\square$

### Subsequences and Limit Points

A real number $L$ is a **limit point** of a sequence $(a_n)$ if some subsequence converges to $L$.

**Theorem.** $L$ is a limit point of $(a_n)$ iff for every $\epsilon > 0$ and every $N \in \mathbb{N}$ there exists $n \geq N$ with $|a_n - L| < \epsilon$.

**Theorem (Bolzano–Weierstrass, sequence form).** Every bounded sequence has a limit point.

### Limsup and Liminf

The **limit superior** of a sequence $(a_n)$ is

$$
\limsup_{n \to \infty} a_n = \lim_{n \to \infty} \left( \sup_{k \geq n} a_k \right),
$$

and the **limit inferior** is

$$
\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left( \inf_{k \geq n} a_k \right).
$$

Both exist in $\mathbb{R} \cup \{-\infty, +\infty\}$ for any sequence, because the sequences $(\sup_{k \geq n} a_k)$ and $(\inf_{k \geq n} a_k)$ are monotone.

**Theorem.** $\liminf a_n \leq \limsup a_n$. Equality holds iff $(a_n)$ converges in $\mathbb{R} \cup \{-\infty, +\infty\}$ — that is, iff it converges in $\mathbb{R}$, or diverges to $+\infty$, or diverges to $-\infty$. For instance $a_n = n$ has $\liminf a_n = \limsup a_n = +\infty$ without converging in $\mathbb{R}$.

### Series

A **series** is a formal sum $\sum_{n=1}^\infty a_n$. Its **partial sums** are

$$
S_N = \sum_{n=1}^N a_n.
$$

The series **converges** if the sequence $(S_N)$ converges. The limit is the **sum** of the series.

**Theorem (Cauchy criterion).** $\sum a_n$ converges iff for every $\epsilon > 0$ there exists $N$ such that

$$
m > n \geq N \implies \left| \sum_{k=n+1}^m a_k \right| < \epsilon.
$$

**Theorem.** If $\sum a_n$ converges, then $a_n \to 0$. The converse fails: the harmonic series $\sum 1/n$ diverges even though $1/n \to 0$.

**Theorem (Comparison).** If $0 \leq a_n \leq b_n$ and $\sum b_n$ converges, then $\sum a_n$ converges.

**Theorem (Absolute convergence).** If $\sum |a_n|$ converges, then $\sum a_n$ converges.

**Theorem (Ratio test).** If $\lim |a_{n+1}/a_n| = L$, the series converges absolutely if $L < 1$ and diverges if $L > 1$. The test is inconclusive if $L = 1$.

**Theorem (Root test).** If $\lim |a_n|^{1/n} = L$, the series converges absolutely if $L < 1$ and diverges if $L > 1$. The test is inconclusive if $L = 1$.

## Limits and Continuity

### Limits of Functions

Let $f : D \to \mathbb{R}$ with $D \subseteq \mathbb{R}$, and let $a$ be a limit point of $D$. We say

$$
\lim_{x \to a} f(x) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
x \in D, \; 0 < |x - a| < \delta \implies |f(x) - L| < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{x \to a} f(x) = L$ iff for every sequence $(x_n)$ in $D \setminus \{a\}$ with $x_n \to a$, we have $f(x_n) \to L$.

### Continuity

A function $f : D \to \mathbb{R}$ is **continuous at** $a \in D$ if $\lim_{x \to a} f(x) = f(a)$ when $a$ is a limit point of $D$; a point of $D$ that is isolated in $D$ is a point of continuity by convention. Equivalently, and in a form that covers isolated points as well, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
x \in D, \; |x - a| < \delta \implies |f(x) - f(a)| < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** $f$ is continuous at $a$ iff for every sequence $(x_n)$ in $D$ with $x_n \to a$, we have $f(x_n) \to f(a)$.

**Theorem.** Sums, products, and quotients (where defined) of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

### The Intermediate Value Theorem

**Theorem (IVT).** If $f : [a, b] \to \mathbb{R}$ is continuous and $y$ lies between $f(a)$ and $f(b)$, then there exists $c \in [a, b]$ with $f(c) = y$.

**Proof.** Suppose $f(a) < y < f(b)$. Let

$$
S = \{x \in [a, b] : f(x) \leq y\}.
$$

$S$ is non-empty ($a \in S$) and bounded above (by $b$), so $c = \sup S$ exists. By continuity, $f(c) \leq y$. If $f(c) < y$, then for $x$ slightly greater than $c$, $f(x) < y$, contradicting the definition of $c$. Hence $f(c) = y$. $\square$

**Corollary.** If $f$ is continuous on $[a, b]$ and $f(a) f(b) < 0$, then $f$ has a root in $(a, b)$.

### The Extreme Value Theorem

**Theorem (EVT).** If $f : [a, b] \to \mathbb{R}$ is continuous, then $f$ is bounded and attains its maximum and minimum.

**Proof.** $[a, b]$ is compact. Continuous images of compact sets are compact. A compact subset of $\mathbb{R}$ is closed and bounded, hence contains its supremum and infimum. $\square$

### Uniform Continuity

A function $f : D \to \mathbb{R}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
x, y \in D, \; |x - y| < \delta \implies |f(x) - f(y)| < \epsilon.
$$

The difference from ordinary continuity is that $\delta$ depends only on $\epsilon$, not on the point.

**Theorem.** A continuous function on a compact set is uniformly continuous.

**Theorem.** A uniformly continuous function on a bounded interval is bounded. A continuous function on a bounded interval need not be bounded: $1/x$ on $(0, 1)$ is continuous but unbounded.

## Differentiation

### The Derivative

Let $f : (a, b) \to \mathbb{R}$ and $x_0 \in (a, b)$. The **derivative** of $f$ at $x_0$ is

$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h},
$$

provided the limit exists. If it does, $f$ is **differentiable** at $x_0$.

**Theorem.** Differentiable implies continuous. The converse fails: $|x|$ is continuous at $0$ but not differentiable there.

### Rules of Differentiation

**Linearity.** $(af + bg)' = a f' + b g'$.

**Product rule.** $(fg)' = f' g + f g'$.

**Quotient rule.** $(f/g)' = (f' g - f g')/g^2$ where $g \neq 0$.

**Chain rule.** $(f \circ g)'(x) = f'(g(x)) g'(x)$.

**Inverse function rule.** If $f$ is differentiable at $x_0$ with $f'(x_0) \neq 0$ and $f^{-1}$ is defined near $f(x_0)$, then

$$
(f^{-1})'(f(x_0)) = \frac{1}{f'(x_0)}.
$$

### The Mean Value Theorem

**Theorem (Rolle).** If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then there exists $c \in (a, b)$ with $f'(c) = 0$.

**Proof.** If $f$ is constant, any $c$ works. Otherwise, $f$ attains a maximum or minimum in $(a, b)$ by the EVT, and at an interior extremum the derivative vanishes. $\square$

**Theorem (Mean Value Theorem).** If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $c \in (a, b)$ with

$$
f'(c) = \frac{f(b) - f(a)}{b - a}.
$$

**Proof.** Apply Rolle to $g(x) = f(x) - \frac{f(b) - f(a)}{b - a}(x - a)$. $\square$

**Corollary.** If $f' = 0$ on an interval, $f$ is constant there.

**Corollary.** If $f' > 0$ on an interval, $f$ is strictly increasing there.

### Taylor's Theorem

**Theorem (Taylor).** If $f$ is $n$ times differentiable on an interval containing $a$ and $x$, with $f^{(n)}$ continuous on the interval between them, then

$$
f(x) = \sum_{k=0}^{n-1} \frac{f^{(k)}(a)}{k!} (x - a)^k + R_n(x),
$$

where the remainder is

$$
R_n(x) = \frac{f^{(n)}(\xi)}{n!} (x - a)^n
$$

for some $\xi$ between $a$ and $x$.

**Corollary.** If $f^{(n+1)} = 0$ on an interval, $f$ is a polynomial of degree at most $n$ there.

## Integration

### The Riemann Integral

Let $f : [a, b] \to \mathbb{R}$ be bounded. A **partition** of $[a, b]$ is a finite set

$$
P = \{a = x_0 < x_1 < \dots < x_n = b\}.
$$

The **upper sum** and **lower sum** are

$$
U(f, P) = \sum_{i=1}^n M_i (x_i - x_{i-1}), \qquad L(f, P) = \sum_{i=1}^n m_i (x_i - x_{i-1}),
$$

where $M_i = \sup_{[x_{i-1}, x_i]} f$ and $m_i = \inf_{[x_{i-1}, x_i]} f$.

The **upper integral** and **lower integral** are

$$
\overline{\int_a^b} f = \inf_P U(f, P), \qquad \underline{\int_a^b} f = \sup_P L(f, P).
$$

$f$ is **Riemann integrable** if the two agree. The common value is

$$
\int_a^b f.
$$

**Theorem (Cauchy criterion).** $f$ is Riemann integrable iff for every $\epsilon > 0$ there exists a partition $P$ with $U(f, P) - L(f, P) < \epsilon$.

**Theorem.** Continuous functions on $[a, b]$ are Riemann integrable. Monotone functions on $[a, b]$ are Riemann integrable. Functions with finitely many discontinuities on $[a, b]$ are Riemann integrable.

**Theorem (Fundamental Theorem of Calculus, I).** If $f$ is continuous on $[a, b]$ and

$$
F(x) = \int_a^x f(t) \, dt,
$$

then $F$ is differentiable on $(a, b)$ and $F' = f$.

**Theorem (Fundamental Theorem of Calculus, II).** If $f$ is Riemann integrable on $[a, b]$ and $F$ is an antiderivative of $f$ on $[a, b]$, then

$$
\int_a^b f = F(b) - F(a).
$$

### Properties of the Integral

**Linearity.** $\int_a^b (cf + g) = c \int_a^b f + \int_a^b g$.

**Additivity.** $\int_a^b f = \int_a^c f + \int_c^b f$.

**Monotonicity.** If $f \leq g$ on $[a, b]$, then $\int_a^b f \leq \int_a^b g$.

**Absolute value.** $\left| \int_a^b f \right| \leq \int_a^b |f|$.

**Integration by parts.** If $f, g$ are differentiable with continuous derivatives, then

$$
\int_a^b f g' = [f g]_a^b - \int_a^b f' g.
$$

**Substitution.** If $\phi$ is continuously differentiable and $f$ is continuous, then

$$
\int_{\phi(a)}^{\phi(b)} f(u) \, du = \int_a^b f(\phi(x)) \phi'(x) \, dx.
$$

### Improper Integrals

If $f$ is defined on $[a, \infty)$ and Riemann integrable on every $[a, R]$, the **improper integral** is

$$
\int_a^\infty f = \lim_{R \to \infty} \int_a^R f,
$$

provided the limit exists. The integral **converges** if the limit exists and is finite.

**Comparison test.** If $0 \leq f \leq g$ on $[a, \infty)$ and $\int_a^\infty g$ converges, then $\int_a^\infty f$ converges.

**Example.** $\int_1^\infty x^{-p} \, dx$ converges iff $p > 1$.

## Sequences of Functions

### Pointwise Convergence

A sequence of functions $f_n : D \to \mathbb{R}$ **converges pointwise** to $f : D \to \mathbb{R}$ if for every $x \in D$,

$$
f_n(x) \to f(x).
$$

Pointwise convergence is weak: limits of continuous functions need not be continuous.

**Example.** $f_n(x) = x^n$ on $[0, 1]$ converges pointwise to $0$ on $[0, 1)$ and to $1$ at $x = 1$. The limit is discontinuous.

### Uniform Convergence

A sequence $(f_n)$ **converges uniformly** to $f$ on $D$ if

$$
\sup_{x \in D} |f_n(x) - f(x)| \to 0.
$$

**Theorem.** Uniform convergence implies pointwise convergence. The converse fails.

**Theorem.** If $(f_n)$ is a sequence of continuous functions converging uniformly to $f$ on $D$, then $f$ is continuous.

**Theorem.** If $(f_n)$ converges uniformly to $f$ on $[a, b]$ and each $f_n$ is Riemann integrable, then $f$ is Riemann integrable and

$$
\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.
$$

**Theorem.** If $(f_n)$ is a sequence of differentiable functions with $f_n \to f$ pointwise and $f_n' \to g$ uniformly, then $f$ is differentiable and $f' = g$.

### Series of Functions

A series of functions $\sum f_n$ **converges uniformly** if the sequence of partial sums does.

**Weierstrass M-test.** If $|f_n(x)| \leq M_n$ for all $x \in D$ and $\sum M_n$ converges, then $\sum f_n$ converges uniformly and absolutely on $D$.

**Theorem.** A uniformly convergent series of continuous functions has a continuous sum.

**Theorem.** A uniformly convergent series of integrable functions can be integrated term by term.

**Theorem.** A series of differentiable functions that converges at one point, and whose derivatives converge uniformly, can be differentiated term by term.

## Power Series

### Definition

A **power series** centered at $a$ is

$$
\sum_{n=0}^\infty c_n (x - a)^n, \qquad c_n \in \mathbb{R}.
$$

### Radius of Convergence

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} |c_n|^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $|x - a| < R$ and diverges for $|x - a| > R$. On $|x - a| < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is differentiable on $|x - a| < R$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dx} \sum_{n=0}^\infty c_n (x - a)^n = \sum_{n=1}^\infty n c_n (x - a)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

If $f$ is infinitely differentiable at $a$, its **Taylor series** at $a$ is

$$
\sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x - a)^n.
$$

**Theorem.** If $f$ equals its Taylor series on an interval around $a$, then $f$ is **analytic** there.

**Theorem.** A function is analytic at $a$ iff it has a power series expansion around $a$ with positive radius of convergence.

**Caution.** A smooth function need not be analytic. The standard example is

$$
f(x) = \begin{cases} e^{-1/x^2} & x \neq 0, \\ 0 & x = 0. \end{cases}
$$

All derivatives at $0$ vanish, so the Taylor series is $0$, but $f(x) > 0$ for $x \neq 0$.

## The Riemann–Stieltjes Integral

### Definition

Let $f, g : [a, b] \to \mathbb{R}$ with $f$ bounded. For a partition $P = \{x_0, \dots, x_n\}$ and tags $\xi_i \in [x_{i-1}, x_i]$, the **Riemann–Stieltjes sum** is

$$
S(f, g, P, \xi) = \sum_{i=1}^n f(\xi_i) (g(x_i) - g(x_{i-1})).
$$

If the limit exists as the mesh of $P$ tends to $0$, it is the **Riemann–Stieltjes integral**

$$
\int_a^b f \, dg.
$$

**Theorem.** If $f$ is continuous and $g$ is of bounded variation, the integral exists.

**Theorem.** If $g$ is continuously differentiable, then

$$
\int_a^b f \, dg = \int_a^b f g' \, dx.
$$

**Theorem (Integration by parts).** If $f$ is integrable with respect to $g$, then $g$ is integrable with respect to $f$ and

$$
\int_a^b f \, dg = f(b) g(b) - f(a) g(a) - \int_a^b g \, df.
$$

## Summary

Real analysis is the study of limits, continuity, differentiation and integration on the real line, and it is the base case on which the analysis of every other system of the corpus is modelled. The line carries the distance $d(a, b) = \lvert a - b\rvert$, and with it the convergent sequences, the convergent series, the limits of functions, the continuous functions and the open sets on which the subject is built.

Differentiation and integration are the two central constructions. The derivative $f'(x_0) = \lim_{h \to 0}(f(x_0 + h) - f(x_0))/h$ is the limit of the difference quotient, and the Riemann integral is defined through the upper and lower sums over the partitions of an interval, with the Riemann–Stieltjes integral generalising the construction by admitting a second function as integrator. The basic properties of both, and the theorems that relate them, are recorded.

The article also passes from sequences of numbers to sequences of functions, where pointwise and uniform convergence are distinguished, and it develops power series with their radius of convergence. The Riemann–Stieltjes integral closes the treatment.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $d(a, b) = \|a - b\|$ | Distance on $\mathbb{R}$ |
| $B(a, r)$ | Open ball of radius $r$ |
| $U, F$ | Open, closed sets |
| $K$ | Compact set |
| $a_n \to L$ | Convergence of a sequence |
| $\limsup a_n, \liminf a_n$ | Limit superior, limit inferior |
| $\sum a_n$ | Series |
| $\lim_{x \to a} f(x)$ | Limit of a function |
| $f'(x)$ | Derivative |
| $\int_a^b f$ | Riemann integral |
| $\int_a^b f \, dg$ | Riemann–Stieltjes integral |
| $f_n \to f$ uniformly | Uniform convergence |
| $\sum c_n (x - a)^n$ | Power series |
| $R$ | Radius of convergence |

## Further Reading

- Richard Dedekind, *Stetigkeit und irrationale Zahlen* (1872), for the construction of $\mathbb{R}$.
- Karl Weierstrass, *Vorlesungen über die Theorie der analytischen Functionen* (1895), for uniform convergence.
- Walter Rudin, *Principles of Mathematical Analysis* (McGraw-Hill, 1976), for the standard modern treatment.
- Tom M. Apostol, *Mathematical Analysis* (Addison-Wesley, 1974), for the Riemann–Stieltjes integral.
- Stephen Abbott, *Understanding Analysis* (Springer, 2015), for a gentle but rigorous introduction.

