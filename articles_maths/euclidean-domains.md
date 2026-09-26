
# __Euclidean Domains__

## Introduction

A **Euclidean domain** is an integral domain equipped with a size function on its nonzero elements that allows division with remainder. The definition is the constructive one: it supplies an algorithm for the gcd of a pair, and through that algorithm every divisibility question in the ring is decided by finite computation. The rung is the strongest of the chain of *Rings and Fields*, and the chain of implications that it completes,

$$
\text{Euclidean} \Longrightarrow \text{principal} \Longrightarrow \text{unique factorisation} \Longrightarrow \text{integral domain},
$$

is the reason the classical rings $\mathbb{Z}$ and $K[x]$ carry an arithmetic at all.

The size function is written $N$ throughout and called the Euclidean degree function; it is not required to be multiplicative, but the classical examples carry a multiplicative norm, and the two uses of the letter $N$ are kept apart by their arguments. The middle of the article works the Gaussian integers $\mathbb{Z}[i]$ in full: division with remainder, the Euclidean algorithm, and the complete classification of the Gaussian primes, which is the form in which the rung is used in number theory. The article ends with the strictness of the chain: $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a principal ideal domain that admits no Euclidean degree function at all, a standard theorem stated here with its citation. Throughout, integral domains, divisibility and irreducibles are *Integral Domains* and *Unique Factorisation Domains*, above, and principal ideal domains are *Principal Ideal Domains*, directly above this article.

---

## Euclidean Degree Functions

### The Definition

**Definition.** A **Euclidean degree function** on an integral domain $R$ is a function

$$
N : R \setminus \{0\} \longrightarrow \mathbb{Z}_{\geq 0}
$$

such that for all $a \in R$ and all $b \in R \setminus \{0\}$ there exist $q, r \in R$ with

$$
a = q b + r, \qquad r = 0 \ \text{or} \ N(r) < N(b).
$$

The element $q$ is the **quotient** and $r$ the **remainder** of the division of $a$ by $b$. An integral domain is a **Euclidean domain** if it admits a Euclidean degree function.

**Remark.** Only the division property is required: $N$ need not be multiplicative, and $N(ab) \geq N(a)$ is not assumed. Both conditions hold in the classical examples and are useful when they do; the results of this article never use them.

**Example.** $\mathbb{Z}$ is a Euclidean domain with $N(a) = |a|$, since division by a nonzero integer with remainder in the usual sense gives $|r| < |b|$.

**Example.** For a field $F$ the polynomial ring $F[x]$ is a Euclidean domain with $N(f) = \deg f$: the division algorithm with remainder, of *Polynomial Rings and Rational Functions*, below this article in this category, gives $f = qg + r$ with $r = 0$ or $\deg r < \deg g$.

**Example.** $\mathbb{Z}[i]$ is a Euclidean domain with $N(a + bi) = a^2 + b^2$, proved in the section on the Gaussian integers below.

**Remark.** The degree function of $F[x]$ is not multiplicative, since $\deg(fg) = \deg f + \deg g$ is additive. It can be replaced by the equivalent multiplicative degree function $N(f) = 2^{\deg f}$, because a nonzero remainder has smaller degree than the divisor exactly when it has smaller value of $2^{\deg}$, and $N(fg) = 2^{\deg f + \deg g} = N(f)N(g)$. A degree function equivalent to a multiplicative one is what a "norm" means in the section on norm-Euclidean domains below.

### The Euclidean Algorithm

**Theorem (Euclidean algorithm).** Let $R$ be a Euclidean domain with degree function $N$, let $a, b \in R$ with $b \neq 0$, and define recursively

$$
r_{-1} = a, \quad r_0 = b, \quad r_{k-1} = q_k r_k + r_{k+1} \ \ (k \geq 0),
$$

where $r_{k+1}$ is the remainder of the division of $r_{k-1}$ by $r_k$, and the recursion stops at the first $k$ with $r_{k+1} = 0$. Then the recursion terminates, and the last nonzero remainder $r_k$ is a greatest common divisor of $a$ and $b$.

**Proof.** As long as $r_k \neq 0$ the next remainder satisfies $N(r_{k+1}) < N(r_k)$, since $r_{k+1} \neq 0$ by hypothesis; a strictly decreasing sequence in $\mathbb{Z}_{\geq 0}$ is finite, so the recursion stops. For the gcd statement, the identity $r_{k-1} = q_k r_k + r_{k+1}$ shows that the pair $(r_{k-1}, r_k)$ has the same common divisors as the pair $(r_k, r_{k+1})$: a common divisor of the first pair divides $r_{k+1}$, and a common divisor of the second divides $r_{k-1}$. Hence all consecutive pairs have the same common divisors, and the last pair $(r_k, 0)$ has common divisors exactly the divisors of $r_k$; so $\gcd(a,b) \sim r_k$. $\square$

**Theorem (extended Euclidean algorithm).** With the notation of the algorithm, there are $x, y \in R$ with

$$
r_k = a x + b y .
$$

The coefficients are computed by running the divisions forwards as in the proof, or equivalently by substituting each division into the one above it, starting from the last nonzero remainder and working upwards.

**Proof.** By induction on $j$ we have $r_j = a x_j + b y_j$ for all $j \geq -1$, starting with $(x_{-1}, y_{-1}) = (1,0)$ and $(x_0, y_0) = (0,1)$; the recursion $r_{j+1} = r_{j-1} - q_j r_j$ gives $(x_{j+1}, y_{j+1}) = (x_{j-1} - q_j x_j, y_{j-1} - q_j y_j)$. $\square$

**Corollary.** Every Euclidean domain is a Bézout domain, and every gcd in a Euclidean domain is a Bézout combination.

**Proof.** The extended algorithm produces $r_k = ax + by$ with $r_k \sim \gcd(a,b)$, so the gcd is a combination of $a$ and $b$; the condition of *Bézout Domains*, above this article in this category, is therefore satisfied for every pair. $\square$

**Example.** In $\mathbb{Z}$ with $a = 240$ and $b = 46$, the algorithm gives $240 = 5\cdot 46 + 10$, $46 = 4 \cdot 10 + 6$, $10 = 1 \cdot 6 + 4$, $6 = 1 \cdot 4 + 2$, $4 = 2\cdot 2$, so $\gcd(240,46) = 2$; back-substituting, $2 = 6 - 4 = 6 - (10 - 6) = 2\cdot 6 - 10 = 2(46 - 4\cdot 10) - 10 = 2 \cdot 46 - 9 \cdot 10 = 2\cdot 46 - 9(240 - 5\cdot 46) = 47 \cdot 46 - 9 \cdot 240$. The combination is the same one that *GCD Domains*, above, produces by hand.

---

## Euclidean Domains Are Principal Ideal Domains

**Theorem.** Every Euclidean domain is a principal ideal domain.

**Proof.** Let $I$ be a nonzero ideal of the Euclidean domain $R$ with degree function $N$, and choose $b \in I \setminus \{0\}$ with $N(b)$ minimal among the nonzero elements of $I$, possible because $\mathbb{Z}_{\geq 0}$ is well ordered. For $a \in I$ divide $a$ by $b$: $a = qb + r$ with $r = 0$ or $N(r) < N(b)$. Since $r = a - qb \in I$ and no nonzero element of $I$ has degree less than $N(b)$, either $r = 0$, or $r \neq 0$ with $N(r) < N(b)$; the second alternative is impossible, so $r = 0$ and $a = qb \in (b)$. Hence $I = (b)$. $\square$

**Theorem (the Euclidean chain).** Every Euclidean domain is a principal ideal domain, every principal ideal domain is a unique factorisation domain, and every unique factorisation domain is an integral domain. Each implication is strict.

**Proof.** The first implication is the theorem above, the second is *Principal Ideal Domains*, above this article in this category, and the third is the definition of a unique factorisation domain. For the strictness: $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a principal ideal domain that is not Euclidean, with its citation in the last section of this article; $\mathbb{Z}[x]$ is a unique factorisation domain that is not principal, by *Principal Ideal Domains*, above; and $\mathbb{Z}[\sqrt{-5}]$ is an integral domain that is not a unique factorisation domain, by *Unique Factorisation Domains*, above. $\square$

**Corollary.** In a Euclidean domain every nonzero non-unit factors into irreducibles, every irreducible is prime, every pair has a gcd, and the gcd is computed by the Euclidean algorithm. In particular $\mathbb{Z}$ and, for a field $F$, the ring $F[x]$ are unique factorisation domains.

**Proof.** A Euclidean domain is principal, hence Bézout and Noetherian, hence satisfies the criteria of *Principal Ideal Domains*, above, and of *Unique Factorisation Domains*, above. $\square$

**Remark.** The Euclidean rung is the only rung of the chain whose definition is algorithmic: it supplies an effective procedure, not merely a divisibility theorem. That is the reason the classical rings, and the rings of the form $\mathbb{Z}[\sqrt{d}]$ whose norm permits rounding, are the ones in which arithmetic is computable by hand.

---

## The Gaussian Integers

### The Norm and Division with Remainder

**Definition.** The **Gaussian integers** are the subring

$$
\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\} \subseteq \mathbb{C},
$$

with the norm $N(a + bi) = a^2 + b^2$, which is multiplicative: $N(zw) = N(z)N(w)$ for all $z, w$.

**Lemma (division with remainder in $\mathbb{Z}[i]$).** Let $z, w \in \mathbb{Z}[i]$ with $w \neq 0$. Then there exist $q, r \in \mathbb{Z}[i]$ with

$$
z = q w + r, \qquad N(r) \leq \tfrac{1}{2} N(w) < N(w).
$$

**Proof.** Write $z/w = \alpha + \beta i$ with $\alpha, \beta \in \mathbb{Q}$, possible because $w \neq 0$ and $z/w = z\bar w / N(w)$. Choose integers $m, n$ with $|\alpha - m| \leq \tfrac12$ and $|\beta - n| \leq \tfrac12$, and set $q = m + ni \in \mathbb{Z}[i]$, $r = z - qw$. Then

$$
N(r) = N(w) \, N\!\left(\frac{z}{w} - q\right) = N(w)\big((\alpha - m)^2 + (\beta - n)^2\big) \leq N(w)\left(\tfrac14 + \tfrac14\right) = \tfrac12 N(w),
$$

and $\tfrac12 N(w) < N(w)$ because $N(w) > 0$. $\square$

**Corollary.** $\mathbb{Z}[i]$ is a Euclidean domain with degree function $N$, hence a unique factorisation domain; its units are $\pm 1, \pm i$, and the elements of norm $1$.

**Proof.** The lemma is the division property. The units are the elements of norm $1$, namely $a + bi$ with $a^2 + b^2 = 1$, which are exactly $\pm 1$ and $\pm i$; unique factorisation follows from the Euclidean chain above. $\square$

### The Euclidean Algorithm in $\mathbb{Z}[i]$

**Example.** The gcd of $5$ and $3 + 4i$. Dividing, $5/(3+4i) = 5(3-4i)/25 = \tfrac35 - \tfrac45 i$, whose nearest Gaussian integer is $1 - i$; then

$$
5 = (1 - i)(3 + 4i) + (-2 - i), \qquad (-2-i)^2 = 3 + 4i,
$$

so $3 + 4i = (-2-i)(-2-i) + 0$ and $\gcd(5, 3+4i) \sim -2-i$, of norm $5$. This is the arithmetic identity behind the splitting $5 = (2+i)(2-i)$, since $-2-i$ is an associate of $2+i$.

**Example.** The gcd of $3 + 4i$ and $11 + 7i$. Dividing, $11 + 7i = (2 - i)(3 + 4i) + (1 + 2i)$ and $3 + 4i = 2(1+2i) + 1$, so $\gcd(3+4i, 11+7i) = 1$: the two elements are coprime, and the algorithm exhibits $1$ as a Bézout combination of them by back-substitution.

### The Gaussian Primes

**Theorem (classification of the Gaussian primes).** An element $\pi \in \mathbb{Z}[i]$ is irreducible if and only if one of the following holds.

**(a)** $N(\pi) = 2$, equivalently $\pi \sim 1 + i$.

**(b)** $\pi$ is an associate of a rational prime $p$ with $p \equiv 3 \pmod 4$.

**(c)** $N(\pi) = p$ for a rational prime $p$ with $p = 2$ or $p \equiv 1 \pmod 4$, equivalently $\pi \sim a \pm bi$ with $a^2 + b^2 = p$.

**Proof.** If $N(\pi)$ is a rational prime then $\pi$ is irreducible, since a factorisation $\pi = zw$ with both factors non-units gives $N(\pi) = N(z)N(w)$ with both norms greater than $1$.

Let $p$ be a rational prime. If $p \equiv 3 \pmod 4$ then $p$ is irreducible in $\mathbb{Z}[i]$: a nontrivial factorisation $p = zw$ would give $N(z), N(w) > 1$ with $N(z)N(w) = p^2$, hence $N(z) = p$, that is, $p = a^2 + b^2$; but squares are $0$ or $1$ modulo $4$, so a sum of two squares is never $3$ modulo $4$. If $p \equiv 1 \pmod 4$ then by the two-squares theorem, cited as standard, $p = a^2 + b^2 = (a+bi)(a-bi)$ with both factors of norm $p$, so $p$ is reducible and $a \pm bi$ has prime norm. If $p = 2$ then $2 = (1+i)(1-i) = -i(1+i)^2$ and $N(1+i) = 2$.

Conversely, let $\pi$ be irreducible and let $p$ be a rational prime dividing $N(\pi) = \pi\bar\pi$. If $p \equiv 3 \pmod 4$ then $p$ is irreducible, hence prime because $\mathbb{Z}[i]$ is a unique factorisation domain, so $p \mid \pi$ or $p \mid \bar\pi$, and the second gives $p \mid \pi$ as well; writing $\pi = pc$ and taking norms gives $N(\pi) = p^2 N(c)$, and since $\pi$ is irreducible and $p$ is a non-unit, $c$ is a unit, so $\pi \sim p$. If $p = 2$ or $p \equiv 1 \pmod 4$, the two previous paragraphs produce an irreducible $\pi_0$ with $N(\pi_0) = p$; then $\pi_0 \mid \pi \bar\pi$, so $\pi_0 \mid \pi$ or $\pi_0 \mid \bar\pi$, and in either case writing $\pi = \pi_0 c$ and comparing norms gives $N(\pi) = p N(c)$ with $c$ a unit, so $N(\pi) = p$. $\square$

**Corollary (the rational primes in $\mathbb{Z}[i]$).** Let $p$ be a rational prime. Then exactly one of the following holds, and in each case the factorisation is unique up to units.

**(a)** $p = -i(1+i)^2$: the prime $2$ ramifies, and $1 + i$ is the unique Gaussian prime above it.

**(b)** $p = \pi \bar\pi$ with $N(\pi) = p$: the primes $p \equiv 1 \pmod 4$ split.

**(c)** $p$ remains irreducible in $\mathbb{Z}[i]$: the primes $p \equiv 3 \pmod 4$ are inert.

**Example.** The splitting primes and their Gaussian factors begin

$$
5 = (2+i)(2-i), \quad 13 = (3+2i)(3-2i), \quad 17 = (4+i)(4-i), \quad 29 = (5+2i)(5-2i), \quad 41 = (5+4i)(5-4i),
$$

the representations $p = a^2 + b^2$ being those of the two-squares theorem; the inert primes begin $3, 7, 11, 19, 23, 31$, none of which is a sum of two squares. As a factorisation in $\mathbb{Z}[i]$, $6 = -i \cdot (1+i)^2 \cdot 3$.

**Corollary.** Let $\pi$ be a Gaussian prime. Then $\mathbb{Z}[i]/(\pi)$ is a finite field with $N(\pi)$ elements.

**Proof.** The quotient is a domain because $(\pi)$ is prime, in fact maximal because $\mathbb{Z}[i]$ is a principal ideal domain and $\pi$ is irreducible, and it is finite because the residues of $\mathbb{Z}[i]$ modulo $\pi$ are represented by the lattice points of a fundamental square of area $N(\pi)$. $\square$

---

## Norm-Euclidean Domains

### The Definition and the Classical Cases

**Definition.** Two Euclidean degree functions on a domain $R$ are **equivalent** if they order the nonzero elements the same way, $N(a) \leq N(b) \iff N'(a) \leq N'(b)$, so that either both satisfy the division property or neither does. A degree function is **multiplicative**, or a **norm**, if $N(ab) = N(a)N(b)$ for all nonzero $a, b$, and $R$ is **norm-Euclidean** if it admits a multiplicative degree function. For the rings $\mathbb{Z}[\sqrt{d}]$ the function is the absolute value of the field norm of $\mathbb{Q}(\sqrt{d})$, which is the origin of the term and the reason the classical rings are norm-Euclidean.

**Example.** $\mathbb{Z}$ is norm-Euclidean with $N(a) = |a|$, and $\mathbb{Z}[i]$ is norm-Euclidean with $N(a+bi) = a^2+b^2$, by the lemma above. The ring $F[x]$ is Euclidean for the degree as it stands, but it is not norm-Euclidean for that degree function, since degree is additive rather than multiplicative; it becomes norm-Euclidean for the equivalent degree function $2^{\deg}$.

**Theorem.** A norm-Euclidean domain is Euclidean, hence a principal ideal domain and a unique factorisation domain.

**Proof.** A norm is a Euclidean degree function by definition, so the chain of the previous section applies. $\square$

### The Principal Ideal Domain That Is Not Euclidean

**Theorem (Gauss; Motzkin).** The ring $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a principal ideal domain, and it is not a Euclidean domain with respect to any Euclidean degree function whatsoever.

**Proof.** The ring is the ring of integers of the imaginary quadratic field $\mathbb{Q}(\sqrt{-19})$, and that every ideal of it is principal is the classical statement that its class number is one, cited here from the literature. That no Euclidean degree function exists, multiplicative or not, is Motzkin's theorem; its proof uses the theory of the minima of ideals and lies beyond this rung, and it is cited here rather than reproduced. $\square$

**Remark.** That a ring can be principal without being Euclidean is the reason the chain of this article is written with a strict first implication. The imaginary quadratic fields of class number one are those for $d = -1, -2, -3, -7, -11, -19, -43, -67, -163$, a theorem of Heegner, Baker and Stark; among the corresponding rings of integers only those for $d = -1, -2, -3, -7, -11$ are norm-Euclidean, so $\mathbb{Z}[(1+\sqrt{-19})/2]$ is the smallest principal ideal domain that fails to be Euclidean.

**Example.** $\mathbb{Z}[\sqrt{-5}]$ is not even a GCD domain, by *GCD Domains*, above, so it is not principal and not Euclidean, and it witnesses the strictness of the implication from unique factorisation to integral domain; its failure is coarser than that of $\mathbb{Z}[x]$, since it is the gcd itself that is missing.

---

## Summary

A Euclidean domain is an integral domain with a degree function $N : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$ permitting division with remainder, $a = qb + r$ with $r = 0$ or $N(r) < N(b)$. Division with remainder yields the Euclidean algorithm, whose last nonzero remainder is a gcd, and the extended algorithm, which exhibits every gcd as a Bézout combination; hence every Euclidean domain is a Bézout domain. Choosing an element of minimal degree in a nonzero ideal shows that every Euclidean domain is a principal ideal domain, so the chain Euclidean $\Rightarrow$ principal $\Rightarrow$ unique factorisation $\Rightarrow$ domain holds, with $\mathbb{Z}$ and $F[x]$ as the classical examples.

The Gaussian integers $\mathbb{Z}[i]$ are Euclidean for the norm $N(a+bi) = a^2+b^2$, the remainder satisfying $N(r) \leq \tfrac12 N(w)$. Their irreducibles are classified: the associates of $1+i$, the associates of the rational primes $p \equiv 3 \pmod 4$, and the elements of prime norm, which produce the splitting $p = \pi\bar\pi$ for $p \equiv 1 \pmod 4$. The rung is strict: $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a principal ideal domain admitting no Euclidean degree function, by Motzkin's theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Integral domain, and a Euclidean domain where stated |
| $R^{\times}$ | Group of units |
| $N$ | Euclidean degree function on $R \setminus \{0\}$, values in $\mathbb{Z}_{\geq 0}$ |
| $N(a + bi) = a^2 + b^2$ | The multiplicative norm on $\mathbb{Z}[i]$ |
| $N(a + b\sqrt{-5}) = a^2 + 5b^2$ | The multiplicative norm on $\mathbb{Z}[\sqrt{-5}]$, of *Integral Domains*, above |
| $a = qb + r$ | Division with remainder, $r = 0$ or $N(r) < N(b)$ |
| $r_k = ax + by$ | Extended Euclidean algorithm: the gcd as a Bézout combination |
| $\gcd(a,b)$, $\operatorname{lcm}(a,b)$ | Greatest common divisor, least common multiple |
| $\mathbb{Z}[i]$ | Gaussian integers |
| Gaussian prime | Irreducible of $\mathbb{Z}[i]$, classified by the norm |
| $\pi$, $\bar\pi$ | A Gaussian prime and its conjugate |
| Norm-Euclidean | Euclidean for a multiplicative norm |
| PID, UFD | Principal ideal domain, unique factorisation domain |
| $\mathbb{Z}[(1+\sqrt{-19})/2]$ | Ring of integers of $\mathbb{Q}(\sqrt{-19})$: principal, not Euclidean |

## Further Reading

- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for Euclidean domains, the Euclidean algorithm and the Gaussian integers.
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (Springer, 2nd ed. 1990), for the classification of the Gaussian primes and the two-squares theorem.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for Euclidean domains, Bézout domains and the chain of divisibility rungs.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for norm-Euclidean domains and the arithmetic of quadratic rings.
- Theodor Motzkin, "The Euclidean algorithm", *Bulletin of the American Mathematical Society* 55 (1949), for the principal ideal domain $\mathbb{Z}[(1+\sqrt{-19})/2]$ that is not Euclidean.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for imaginary quadratic fields, their class numbers and the norm-Euclidean cases.
