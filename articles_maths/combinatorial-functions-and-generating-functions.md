
# __Combinatorial Functions and Generating Functions__

## Introduction

This is the fourth article of the Natural Numbers system in Part V, and it occupies the **special-functions slot** of that system. The natural numbers carry one slot of functions, and it is this one: the arithmetic and combinatorial functions $\mathbb{N} \to R$ — the factorials, binomial coefficients, Stirling and Bell numbers, Catalan numbers, partition numbers, the divisor and Möbius functions — together with the generating functions that encode them. The system $\mathbb{N}$ has no geometry, no analysis and no harmonic analysis, and its functions are correspondingly discrete: they are sequences, and the theory of their generating functions is the algebraic theory of formal power series and of Dirichlet series.

The corpus's default base is the commutative ring $R$ with identity $1 \neq 0$, and this article uses that base throughout: generating functions are elements of the formal power series ring $R[[x]]$, and the arithmetic functions take values in $R$. Two places require more than a commutative ring, and they are flagged where they occur: the reciprocal $(1 - x)^{-1}$ and the composition of formal power series require conditions on the constant terms, and the formal logarithm and exponential require that $R$ be a $\mathbb{Q}$-algebra, that is, that every positive integer be invertible. Coefficient extraction, the Cauchy product and Lagrange inversion need no such hypothesis.

The general theory of rings and ideals is from *Rings*, and the theory of the formal power series ring is from *Formal Power Series and Completion*; the recursive definitions of the functions are from *The Natural Numbers*, and the arithmetic functions and their Dirichlet series are from *Analytic Number Theory*. The asymptotic estimates at the end of the article are real-valued statements about functions on $\mathbb{N}$, and they belong to the analytic side of the corpus; they are quoted from the standard literature and are marked as such. Throughout, a sequence $(a_n)_{n \geq 0}$ in $R$ has **ordinary generating function** $A(x) = \sum_{n \geq 0} a_n x^n$ and **exponential generating function** $\hat A(x) = \sum_{n \geq 0} a_n x^n / n!$, the latter requiring that $R$ be a $\mathbb{Q}$-algebra; $\mu$ is the Möbius function, $\varphi$ the Euler function, $\zeta$ the Riemann zeta function and $[x^n] A(x)$ the coefficient of $x^n$.

## Generating Functions

### Formal Power Series

**Definition.** Let $R$ be a commutative ring with identity. The **ring of formal power series** $R[[x]]$ is the set of all sequences $(a_n)_{n \geq 0}$ in $R$, written $\sum_{n\geq 0} a_n x^n$, with

$$
\sum a_n x^n + \sum b_n x^n = \sum (a_n + b_n) x^n, \qquad \left(\sum a_n x^n\right)\left(\sum b_n x^n\right) = \sum_{n \geq 0} \left(\sum_{k=0}^{n} a_k b_{n-k}\right) x^n .
$$

**Theorem.** With these operations $R[[x]]$ is a commutative ring with identity $1$, the polynomial ring $R[x]$ is a subring, and a series $\sum a_n x^n$ is a unit in $R[[x]]$ if and only if $a_0$ is a unit of $R$. The map $R \to R[[x]]$, $a \mapsto a$, is an injective ring homomorphism.

**Proof.** The ring axioms are those of $R$ applied componentwise; associativity of the product is the associativity of the convolution $\sum_{k} a_k b_{n-k}$, which is finite for each $n$. If $a_0$ is a unit then the coefficients of the inverse are determined recursively by $b_0 = a_0^{-1}$ and $b_n = -a_0^{-1}\sum_{k=1}^n a_k b_{n-k}$, and conversely a unit must have invertible constant term because the constant term of a product is the product of the constant terms. The last statement is clear. $\square$

**Definition.** For a formal power series $A = \sum a_n x^n$ one writes

$$
[x^n] A = a_n, \qquad A' = \sum_{n \geq 1} n a_n x^{n-1}, \qquad A(0) = a_0 .
$$

The **order** of a nonzero series is the least $n$ with $a_n \neq 0$.

**Theorem.** For every $R$, the derivation $A \mapsto A'$ satisfies the formal counterparts of the sum, product and chain rules, the constant term of $A'$ is zero, and if $R$ is a $\mathbb{Q}$-algebra then the formal logarithm and exponential

$$
\log(1 - x) = -\sum_{n \geq 1} \frac{x^n}{n}, \qquad \exp(x) = \sum_{n \geq 0} \frac{x^n}{n!}
$$

satisfy $\exp(\log(1-x)) = 1-x$ and the usual identity $\exp(A + B) = \exp(A)\exp(B)$ whenever $A$ and $B$ have zero constant term.

**Proof.** The derivation is linear and satisfies $A' B + A B' = (AB)'$ by differentiating the convolution. For the logarithm and exponential, all the displayed coefficients require the division by $n$ and by $n!$, which is where the hypothesis that $R$ be a $\mathbb{Q}$-algebra enters; the identities then follow by the formal computation of the coefficients. $\square$

**Remark.** The hypothesis that $R$ be a $\mathbb{Q}$-algebra is genuinely needed for the exponential: in characteristic $p$ the coefficient $1/p!$ does not exist. Over a field of characteristic $p$ the exponential series has no meaning as a formal power series, although the truncated versions $\exp(x) \bmod x^{p}$ do. The generating functions of the next sections that use $n!$ or $1/n$ carry this hypothesis; those that only use integers do not.

### Operations on Generating Functions

**Theorem (dictionary).** Let $(a_n)$, $(b_n)$ be sequences in $R$ with generating functions $A(x)$, $B(x)$. Then

$$
[x^n] A(x) B(x) = \sum_{k=0}^{n} a_k b_{n-k}, \qquad [x^n] \frac{A(x)}{1-x} = \sum_{k=0}^{n} a_k, \qquad [x^n] \frac{1}{1-x} = 1,
$$

and if $B$ has zero constant term, the composition $A(B(x))$ is a well-defined formal power series whose $x^n$-coefficient depends on finitely many coefficients of $A$; the substitution $x \mapsto x^k$ multiplies the coefficient sequence by the indicator of the multiples of $k$.

**Proof.** The first identity is the Cauchy product. The second follows from the first with $b_n = 1$, and the third is the geometric series computed from $(1-x)(1+x+x^2+\cdots) = 1$. Composition is well defined because in degree $n$ only the terms $a_0, \dots, a_n$ and powers of $B$ of order at least $1$ contribute. $\square$

**Corollary.** Generating functions convert the sum of sequences, the convolution and the partial-sum operator into the ring operations on $R[[x]]$ and the multiplication by $(1-x)^{-1}$; the map $(a_n) \mapsto A(x)$ is a ring isomorphism from the ring of sequences with convolution onto $R[[x]]$, by the dictionary of *Formal Power Series and Completion*.

## Combinatorial Coefficients

### The Binomial Coefficients

**Definition.** For $n, k \in \mathbb{N}$ the **binomial coefficient** is $\binom{n}{k} = n!/(k!(n-k)!)$ for $k \leq n$, and $0$ for $k > n$. The **Pascal identity** is $\binom{n+1}{k+1} = \binom{n}{k+1} + \binom{n}{k}$.

**Theorem (binomial theorem).** In every commutative ring $R$, and for all $n \in \mathbb{N}$,

$$
(1 + x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k ,
$$

and consequently

$$
\sum_{n \geq k} \binom{n}{k} x^n = \frac{x^k}{(1-x)^{k+1}} .
$$

**Proof.** The binomial theorem is an induction on $n$ using Pascal's identity, which is the identity $\binom{n+1}{k+1} = \binom{n}{k} + \binom{n}{k+1}$. The generating function follows from $(1-x)^{-k-1} = \sum_{m \geq 0}\binom{m+k}{k} x^m$, itself the binomial theorem with negative exponent or an induction on $k$. $\square$

**Corollary (Vandermonde).** $\binom{m+n}{k} = \sum_{j} \binom{m}{j}\binom{n}{k-j}$.

**Proof.** Compare coefficients in $(1+x)^{m+n} = (1+x)^m (1+x)^n$. $\square$

### Stirling, Bell and Catalan Numbers

**Definition.** The **Stirling numbers of the second kind** $S(n,k)$ count the partitions of an $n$-element set into $k$ nonempty blocks; the **Stirling numbers of the first kind** $s(n,k)$ are defined by the falling factorial $x^{\underline n} = \sum_k s(n,k) x^k$. The **Bell number** is $B_n = \sum_k S(n,k)$, and the **Catalan number** is $C_n = \frac{1}{n+1}\binom{2n}{n}$.

**Theorem.** The Stirling numbers of the second kind satisfy the recurrence

$$
S(n+1,k) = k\, S(n,k) + S(n,k-1), \qquad S(0,0) = 1,
$$

and their exponential and ordinary generating functions are

$$
\sum_{n \geq k} S(n,k) \frac{x^n}{n!} = \frac{(e^x - 1)^k}{k!}, \qquad \sum_{n \geq k} S(n,k) x^n = \frac{x^k}{(1-x)(1-2x)\cdots(1-kx)} .
$$

The Bell numbers have exponential generating function $\sum_{n \geq 0} B_n x^n / n! = \exp(e^x - 1)$.

**Proof.** The recurrence is by the position of the block containing a fixed element: either it is a singleton, giving $S(n,k-1)$, or it joins one of the $k$ blocks of a partition of the remaining $n$ elements, giving $k S(n,k)$. The exponential generating function is obtained by observing that a partition into $k$ blocks is an unordered set of $k$ nonempty sets, and the exponential generating function of nonempty sets is $e^x - 1$; the ordinary generating function follows from the partial fraction expansion of the product. For the Bell numbers, sum over $k$ and use $\exp$. $\square$

**Theorem (Catalan).** The Catalan numbers satisfy $C_0 = 1$ and

$$
C_{n+1} = \sum_{i=0}^{n} C_i C_{n-i} ,
$$

so that the generating function $C(x) = \sum_{n \geq 0} C_n x^n$ satisfies the functional equation $C(x) = 1 + x C(x)^2$ and hence

$$
C(x) = \frac{1 - \sqrt{1 - 4x}}{2x}, \qquad C_n = \frac{1}{n+1}\binom{2n}{n}.
$$

**Proof.** The recurrence is the standard decomposition of a Catalan object into two smaller ones, and it translates into $C = 1 + xC^2$ by the convolution dictionary; solving the quadratic over $\mathbb{Q}[[x]]$ and choosing the branch with constant term $1$ gives the closed form. The coefficient formula follows by the binomial expansion of $\sqrt{1-4x}$; the computation is standard. $\square$

### Partitions and the Pentagonal Theorem

**Definition.** The **partition function** $p(n)$ counts the partitions of $n$ into positive parts, and **Euler's product** is $\phi(x) = \prod_{k \geq 1}(1 - x^k)$.

**Theorem (Euler).** The generating function of $p(n)$ is

$$
\sum_{n \geq 0} p(n) x^n = \prod_{k \geq 1} \frac{1}{1 - x^k} = \frac{1}{\phi(x)},
$$

and Euler's pentagonal number theorem states

$$
\phi(x) = \prod_{k \geq 1}(1 - x^k) = \sum_{j \in \mathbb{Z}} (-1)^j x^{j(3j-1)/2} .
$$

**Proof.** The first identity is the expansion of each factor as a geometric series $1 + x^k + x^{2k} + \cdots$ and the collection of the contributions to $x^n$, each partition of $n$ contributing once. The pentagonal theorem is Euler's; the standard proof multiplies out the product and observes that the surviving terms are those in which the parts form a strictly decreasing then strictly decreasing-by-one pattern, giving the pentagonal exponents $j(3j\pm1)/2$ with signs $(-1)^j$. $\square$

**Corollary (Euler's recurrence).** The pentagonal theorem gives $p(n)$ by the recurrence $p(n) = \sum_{j \neq 0} (-1)^{j+1} p(n - j(3j-1)/2)$ with $p(0) = 1$ and $p(n) = 0$ for $n < 0$.

## Exponential and Dirichlet Generating Functions

### Labelled Structures

**Definition.** The **exponential generating function** of a sequence $(a_n)$ is $\hat A(x) = \sum_{n\geq 0} a_n x^n/n!$; it is defined when $R$ is a $\mathbb{Q}$-algebra. The **product** of two labelled structures corresponds to the binomial convolution

$$
c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k}, \qquad \text{i.e.} \qquad \hat C(x) = \hat A(x)\hat B(x) .
$$

**Theorem.** The exponential generating function converts the labelled product into multiplication, the disjoint union into addition, and the formation of nonempty sets into the exponential: if a structure is an unordered set of its connected components and the components have exponential generating function $\hat A$, then the whole structure has exponential generating function $\exp(\hat A(x))$. The class of permutations has $\sum n!\,x^n/n! = (1-x)^{-1}$, and the class of cyclic permutations has $-\log(1-x)$.

**Proof.** The binomial convolution is the coefficientwise form of the product; the composition with $\exp$ is the standard exponential formula for sets of components, whose coefficients are the Bell-type sums. The two examples follow from the geometric series and the formal logarithm. $\square$

### Dirichlet Series and Arithmetic Functions

**Definition.** An **arithmetic function** is a function $f : \mathbb{N}_{\geq 1} \to R$. The **Dirichlet convolution** is

$$
(f * g)(n) = \sum_{d \mid n} f(d) g(n/d),
$$

and the **Dirichlet series** of $f$ is $\sum_{n \geq 1} f(n) n^{-s}$, formally a sum over the positive integers. The unit is the function $\varepsilon$ with $\varepsilon(1) = 1$ and $\varepsilon(n) = 0$ for $n > 1$, the constant function $1$ is written $\zeta$, and the **Möbius function** is defined by $\mu(1) = 1$, $\mu(n) = (-1)^k$ if $n$ is a product of $k$ distinct primes, and $\mu(n) = 0$ if $n$ is divisible by a square.

**Theorem.** The arithmetic functions form a commutative ring with identity $\varepsilon$ under pointwise addition and Dirichlet convolution, and $\mu * \zeta = \varepsilon$; equivalently $\sum_{n \geq 1} \mu(n) n^{-s} = 1/\zeta(s)$. **Möbius inversion** holds:

$$
g(n) = \sum_{d \mid n} f(d) \iff f(n) = \sum_{d \mid n} \mu(n/d) g(d).
$$

**Proof.** Associativity and commutativity of the convolution follow from the reindexing of the divisors of a product; the identity is $\varepsilon$. The identity $\mu * \zeta = \varepsilon$ is verified at $n$ by grouping the divisors of $n$ according to their squarefree part, the alternating sum over the subsets of the primes dividing $n$ being $(1-1)^k = 0$ for $n > 1$. Möbius inversion is the statement that $\mu$ is the inverse of $\zeta$ in the convolution ring. $\square$

**Theorem.** **Euler's totient function** $\varphi(n)$ satisfies $\sum_{d\mid n}\varphi(d) = n$ and $\sum_{n\geq 1} \varphi(n) n^{-s} = \zeta(s-1)/\zeta(s)$; the divisor function $\tau$, the sum-of-divisors function $\sigma$ and the Liouville function have the Dirichlet series $\zeta(s)^2$, $\zeta(s)\zeta(s-1)$ and $\zeta(2s)/\zeta(s)$ respectively.

**Proof.** The divisor identity for $\varphi$ counts the elements of a cyclic group by their order; the Dirichlet series follow from the multiplicativity of the functions and the Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$. The computations are in *Analytic Number Theory*. $\square$

## Lagrange Inversion and Applications

### The Lagrange–Bürmann Formula

**Definition.** Let $R$ be a commutative $\mathbb{Q}$-algebra and let $w(x) = \sum_{n \geq 1} w_n x^n$ have $w_1$ a unit. Then $w$ has a compositional inverse $\bar w$ with $w(\bar w(x)) = x = \bar w(w(x))$.

**Theorem (Lagrange inversion).** With $w$ as above and $n \geq 1$,

$$
[x^n]\, \bar w(x) = \frac{1}{n} [x^{n-1}] \left( \frac{x}{w(x)} \right)^{n} .
$$

More generally, for any formal power series $H$,

$$
[x^n]\, H(\bar w(x)) = \frac{1}{n} [x^{n-1}]\, H'(x) \left( \frac{x}{w(x)} \right)^{n} .
$$

**Proof.** The formula is the Lagrange–Bürmann inversion theorem, proved by the residue calculus of formal power series: the substitution $x = w(t)$ turns the coefficient extraction into the evaluation of a residue, and the change-of-variables formula for residues gives the displayed expression. The argument is standard and is in *Formal Power Series and Completion*. $\square$

### Cayley's Tree Formula

**Theorem (Cayley).** The number of labelled trees on $n$ vertices is $n^{n-2}$ for $n \geq 1$; equivalently, the number of rooted labelled trees on $n$ vertices is $n^{n-1}$.

**Proof.** Let $T(x) = \sum_{n \geq 1} n^{n-1} x^n/n!$ be the exponential generating function of rooted labelled trees. A rooted tree is a root together with a set of rooted subtrees, so $T = x\exp(T)$, that is, $T = w^{-1}$ for $w(x) = x e^{-x}$. Lagrange inversion gives

$$
[x^n] T(x) = \frac{1}{n}[x^{n-1}] e^{nx} = \frac{n^{n-1}}{n!},
$$

so the coefficient of $x^n/n!$ is $n^{n-1}$, as claimed; dividing by $n$ to forget the root gives $n^{n-2}$. $\square$

## Asymptotics

### Stirling's Formula

**Theorem (Stirling).** As $n \to \infty$,

$$
n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n ,
$$

so that $\log(n!) = n\log n - n + \tfrac12 \log(2\pi n) + O(1/n)$.

**Proof.** The estimate is obtained by comparing $\log(n!) = \sum_{k=1}^n \log k$ with the integral $\int_1^n \log t\, dt$ and refining the Euler–Maclaurin expansion; the argument belongs to real analysis and is quoted from the standard literature. $\square$

**Corollary.** The two conventions have different analytic behaviour. The ordinary generating function $\sum_{n \geq 0} n!\,x^n$ has zero radius of convergence, since the coefficients grow like $n!$ and outrun every geometric series; the exponential generating function $\sum_{n\geq 0} x^n/n!$ of the elementary functions converges everywhere, and this is the reason the exponential convention is the natural one for the labelled structures above. The ordinary generating function of the Catalan numbers has radius $1/4$, because $C_n \sim 4^n/(n^{3/2}\sqrt{\pi})$.

### The Growth of the Partition Function

**Theorem (Hardy–Ramanujan).** As $n \to \infty$,

$$
p(n) \sim \frac{1}{4n\sqrt{3}} \exp\left( \pi \sqrt{\frac{2n}{3}} \right).
$$

**Proof.** The estimate is obtained by the circle method, applied to the generating function $\prod_k (1-x^k)^{-1}$ near the unit circle; the theorem of Hardy and Ramanujan, later refined by Rademacher to an exact series, is quoted. $\square$

**Remark.** The two theorems show the two uses of generating functions: the algebraic use, in which the coefficients are computed exactly from the functional equation or the recurrence, and the analytic use, in which the growth of the coefficients is read off from the singularities of the generating function. The first is the content of the present article for the system $\mathbb{N}$; the second is the analytic theory of the special functions of the later systems of the ladder.

## Pólya Enumeration and the Cycle Index

### The Cycle Index

**Definition.** Let a finite group $G$ act on a finite set $X$. For $g \in G$ let $c_k(g)$ be the number of cycles of length $k$ in the permutation of $X$ induced by $g$. The **cycle index** of the action is the polynomial in the indeterminates $s_1, \dots, s_{\lvert X\rvert}$

$$
Z_G(s_1, \dots, s_{\lvert X\rvert}) = \frac{1}{\lvert G\rvert}\sum_{g \in G} \prod_{k=1}^{\lvert X\rvert} s_k^{\,c_k(g)} .
$$

**Theorem (Burnside).** The number of orbits of $G$ on $X$ is the number of fixed points averaged over the group:

$$
\lvert X/G\rvert = \frac{1}{\lvert G\rvert}\sum_{g\in G}\lvert X^g\rvert = Z_G(1,1,\dots,1) .
$$

**Proof.** Counting the pairs $(g,x)$ with $gx = x$ in the two possible orders gives $\sum_g \lvert X^g\rvert = \sum_{x}\lvert G_x\rvert$, and the orbit–stabiliser theorem turns the right-hand side into $\lvert G\rvert$ times the number of orbits. $\square$

### Pólya's Theorem

**Theorem (Pólya).** Let $G$ act on $X$ and let $Y$ be a set of colours with weights. Then the generating function for the orbits of $G$ on the colourings $Y^X$, counted by total weight, is obtained from the cycle index by the substitution that replaces $s_k$ by the power sum $p_k = \sum_{y \in Y} y^k$:

$$
\sum_{\text{orbits } O} \prod_{x \in O} \text{weight}(x) = Z_G(p_1, p_2, \dots) .
$$

**Proof.** The number of colourings fixed by $g$ is $\prod_k p_k^{c_k(g)}$, because a colouring is fixed exactly when it is constant on the cycles of $g$, and the orbit counting of Burnside applied weight by weight gives the substitution. $\square$

**Corollary (necklaces).** The number of necklaces with $n$ beads and $k$ colours is

$$
N(n,k) = \frac{1}{n}\sum_{d \mid n} \varphi(d)\, k^{\,n/d},
$$

and the number of bracelets is obtained by adding the reversal to the group and applying the same formula to the dihedral group.

**Proof.** The cyclic group $C_n$ acts on the $n$ positions; the rotations with $n/d$ cycles of length $d$ are counted by $\varphi(d)$, and Pólya's theorem with $k$ colours of weight $1$ gives the formula. $\square$

**Example.** With $n = 4$ and $k = 2$ the formula gives $\tfrac14(2^4 + 2^2 + 0 + 2^2) = 6$ necklaces, namely $0000$, $0001$, $0011$, $0101$, $0111$, $1111$; with the reversal included the bracelets still number $6$, because the reversal maps each of the six necklaces to a rotation of itself.

## Summary

A commutative ring $R$ gives the formal power series ring $R[[x]]$, in which addition is componentwise and multiplication is the Cauchy convolution; a series is a unit exactly when its constant term is a unit, the derivation is formal and satisfies the usual rules, and the logarithm and exponential exist when $R$ is a $\mathbb{Q}$-algebra. The ordinary generating function converts the convolution of sequences into multiplication and the partial-sum operator into multiplication by $(1-x)^{-1}$, while the exponential generating function converts the labelled product into multiplication and the formation of sets of components into the exponential.

The binomial coefficients satisfy the Pascal identity, the binomial theorem and Vandermonde's identity, with generating function $\sum_n \binom{n}{k} x^n = x^k/(1-x)^{k+1}$. The Stirling numbers of the second kind satisfy $S(n+1,k) = kS(n,k) + S(n,k-1)$ with exponential generating function $(e^x-1)^k/k!$, the Bell numbers have exponential generating function $\exp(e^x-1)$, and the Catalan numbers satisfy $C = 1 + xC^2$ with $C_n = \binom{2n}{n}/(n+1)$. The partition function has generating function $\prod_k(1-x^k)^{-1}$, Euler's pentagonal theorem gives its recurrence, and the arithmetic functions form a commutative ring under Dirichlet convolution in which $\mu * \zeta = \varepsilon$ and Möbius inversion holds; the Euler totient, divisor and Liouville functions have the classical Dirichlet series. Lagrange inversion inverts a compositional relation and yields Cayley's formula $n^{n-2}$ for the labelled trees, and the asymptotic estimates of Stirling and Hardy–Ramanujan give the growth of the factorial and the partition function. The special functions of $\mathbb{N}$ are thus the combinatorial and arithmetic functions, and their generating functions are the algebraic and analytic encoding of the system's arithmetic.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R[[x]]$ | Ring of formal power series over $R$ |
| $[x^n] A$ | Coefficient extraction |
| $A'$ | Formal derivative |
| $a_n$, $A(x)$ | Sequence and its ordinary generating function |
| $\hat A(x)$ | Exponential generating function, $\sum a_n x^n/n!$ |
| $\binom{n}{k}$ | Binomial coefficient |
| $S(n,k)$, $s(n,k)$ | Stirling numbers of the second, first kind |
| $B_n$ | Bell number |
| $C_n$, $C(x)$ | Catalan number and its generating function |
| $p(n)$, $\phi(x)$ | Partition function, Euler's product $\prod(1-x^k)$ |
| $\varphi(n)$ | Euler's totient function, the count of $k \leq n$ coprime to $n$ |
| $\mu, \tau, \sigma$ | Möbius, divisor and sum-of-divisors functions |
| $f * g$ | Dirichlet convolution |
| $\varepsilon, \zeta$ | Unit and constant-one arithmetic functions, with Dirichlet series $\zeta(s)$ |
| $\bar w$ | Compositional inverse of $w$ |
| $n!$ | Factorial, with $n! \sim \sqrt{2\pi n}(n/e)^n$ |

## Further Reading

- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (Oxford University Press, 6th ed. 2008), for the arithmetic functions, Möbius inversion and the partition function.
- G. Pólya and G. Szegő, *Problems and Theorems in Analysis I* (Springer, 1972), for generating functions, Lagrange inversion and coefficient estimates.
- Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics* (Cambridge University Press, 2009), for the algebraic and analytic theory of generating functions and their asymptotics.
- Herbert S. Wilf, *generatingfunctionology* (A K Peters, 3rd ed. 2006), for a systematic introduction to ordinary, exponential and Dirichlet generating functions.
- Richard P. Stanley, *Enumerative Combinatorics*, Volumes 1 and 2 (Cambridge University Press, 2nd ed. 2012, 1999), for the combinatorial interpretation of the coefficients and the exponential formula.
- Godfrey H. Hardy and Srinivasa Ramanujan, "Asymptotic formulae in combinatory analysis", *Proceedings of the London Mathematical Society* 17 (1918), for the asymptotic formula for the partition function.
- Tom M. Apostol, *Introduction to Analytic Number Theory* (Springer, 1976), for Dirichlet series, multiplicative functions and the zeta function.
