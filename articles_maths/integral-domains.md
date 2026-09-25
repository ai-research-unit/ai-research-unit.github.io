
# __Integral Domains__

## Introduction

An **integral domain** is a commutative ring with $1 \neq 0$ in which a product of two nonzero elements is nonzero. The hypothesis is one line long, and almost the whole multiplicative theory of the category rests on it: it gives cancellation, it makes divisibility a partial order on associate classes, it forces the characteristic to be $0$ or a prime, and it makes a nonzero polynomial of degree $n$ have at most $n$ roots. The rung that it occupies is the fourth of the commutative chain, above *Reduced Rings and the Nilradical*, of which a domain is the special case whose nilradical vanishes and whose zero ideal is prime.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, the corpus default, and $K$ is a field wherever a field is needed; each place where a field rather than a general ring is required is marked. Divisibility is the heart of the article, and the three rungs above it — *GCD Domains*, *Bézout Domains* and *Unique Factorisation Domains*, below this article in this category — are each a statement about how well divisibility in a domain behaves. The two constructions that a domain carries but does not develop here are the fraction field, deferred to *Localization and the Fraction Field*, below this article in this category, and the greatest common divisor, deferred to *GCD Domains*.

---

## Definition and Elementary Properties

### Cancellation

**Definition.** An **integral domain** is a commutative ring $R$ with $1 \neq 0$ such that

$$
a b = 0 \quad \Longrightarrow \quad a = 0 \ \text{or}\ b = 0 .
$$

Equivalently, $R$ has no zero divisors in the sense of *Rings*, §Zero Divisors, the element $0$ being the only element that annihilates a nonzero element. A field is the special case in which every nonzero element is a unit; the field axioms belong to *Fields*, later in this category.

**Proposition (cancellation).** Let $R$ be an integral domain, $a, b, c \in R$ and $a \neq 0$. If $ab = ac$ then $b = c$.

**Proof.** From $a(b-c) = 0$ and $a \neq 0$ the definition gives $b - c = 0$. $\square$

**Proposition.** Every integral domain is a reduced ring in the sense of *Reduced Rings and the Nilradical*, above this article in this category, and every domain other than the zero ring is connected, its only idempotents being $0$ and $1$.

**Proof.** A nonzero nilpotent $a$ with $a^n = 0$ and $n$ minimal satisfies $a \cdot a^{n-1} = 0$ with $a^{n-1} \neq 0$, so $a$ is a zero divisor, which a domain does not have. If $e$ is idempotent and $e \neq 0$ then $e(1-e) = 0$, so $1 - e = 0$ and $e = 1$. $\square$

**Remark.** The condition "$1 \neq 0$" is not redundant: the zero ring satisfies $ab = 0 \Rightarrow a = 0$ or $b = 0$ vacuously, and is excluded in order that the prime subring of a domain be well defined.

### Subrings, Products and Polynomial Rings

**Proposition.** Let $R$ be an integral domain.

**(a)** Every subring of $R$ containing $1$ is an integral domain.

**(b)** If $S$ is a nonzero commutative ring with $1 \neq 0$, then $R \times S$ is not an integral domain.

**(c)** The polynomial ring $R[x]$ is an integral domain, and $\deg(fg) = \deg f + \deg g$ for nonzero $f, g \in R[x]$.

**(d)** $(R[x])^{\times} = R^{\times}$.

**Proof.** (a) A subring with the same $1$ inherits the absence of zero divisors. (b) $(1, 0)(0, 1) = (0,0)$ with both factors nonzero. (c) If $f$ and $g$ are nonzero with leading coefficients $a$ and $b$, then the term of degree $\deg f + \deg g$ in $fg$ is $ab x^{\deg f + \deg g}$, and $ab \neq 0$ in the domain $R$; no higher-degree term occurs, so the coefficient is nonzero and $fg \neq 0$. (d) If $fg = 1$ then $\deg f + \deg g = \deg 1 = 0$, so $f$ and $g$ are nonzero constants, and a constant is a unit of $R[x]$ exactly when it is a unit of $R$. $\square$

The general theory of polynomial rings — degree, the division algorithm, roots in the applications sense and the arithmetic of $R[x]$ as a ring — is *Polynomial Rings and Rational Functions*, below this article in this category, and only the two facts above and the root theorem of this article are used before it is reached.

**Example.** $\mathbb{Z}$ is an integral domain, since a product of two nonzero integers has nonzero absolute value. For a field $K$ the polynomial ring $K[x]$ is an integral domain by (c), and its units are the nonzero constants. The rings $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$ and $\mathbb{Z}[\sqrt{-5}]$ are integral domains, each being a subring of $\mathbb{C}$; the last is a domain that is not a unique factorisation domain, as the rung below records.

**Remark.** $\mathbb{Z}/n\mathbb{Z}$ is an integral domain only when $n$ is prime, in which case it is the field $\mathbb{F}_p$; for composite $n$ it has zero divisors. So being a domain is a genuine restriction on a quotient, and a prime ideal in the sense of *Commutative Rings*, above this article, is exactly one whose quotient is a domain.

---

## Divisibility

### The Divisibility Preorder

**Definition.** For $a, b \in R$, write $a \mid b$, and say that $a$ **divides** $b$, if $b = ac$ for some $c \in R$. An element $a$ is a **divisor** of $b$ in that case, and $b$ is a **multiple** of $a$.

**Proposition.** Let $R$ be an integral domain and $a, b, c \in R$, with $u \in R^{\times}$ a unit.

**(a)** $a \mid a$, and $1 \mid a$, and $a \mid 0$.

**(b)** If $a \mid b$ and $b \mid c$ then $a \mid c$.

**(c)** $a \mid b$ if and only if the principal ideal satisfies $(b) \subseteq (a)$.

**(d)** $u \mid a$ and $a \mid u a$; if $a \neq 0$ then $a \mid u a$ has $u$ as its only cofactor in the sense that $ua = av$ forces $v = u$.

**(e)** If $a \mid b$ and $a \mid c$ then $a \mid (bx + cy)$ for all $x, y \in R$.

**Proof.** (a) $a = a \cdot 1$, $a = 1 \cdot a$ and $0 = a \cdot 0$. (b) If $b = ax$ and $c = by$ then $c = a(xy)$. (c) $b = ac$ says exactly that $b \in (a)$, that is, $(b) \subseteq (a)$. (d) Clear from the definition; cancellation gives $ua = av \Rightarrow u = v$ when $a \neq 0$. (e) $bx + cy = a(x'x + y'y)$ if $b = ax'$ and $c = ay'$. $\square$

Thus divisibility is a reflexive and transitive relation, a preorder; by (c) it is the inclusion order of principal ideals read backwards.

### Associates

**Definition.** Two elements $a, b \in R$ are **associates**, written $a \sim b$, if $a = ub$ for some unit $u \in R^{\times}$.

**Proposition (associates).** Let $R$ be an integral domain and $a, b \in R$. Then $a \sim b$ if and only if $a \mid b$ and $b \mid a$.

**Proof.** If $a = ub$ with $u$ a unit then $b = u^{-1}a$, so each divides the other. Conversely suppose $b = ax$ and $a = by$. If $a = 0$ then $b = a x = 0$, and $a = 1 \cdot b$. If $a \neq 0$, then $a = axy$ and cancellation gives $1 = xy$, so $x$ is a unit and $a \sim b$. $\square$

This is the point at which the domain hypothesis is used: in a general commutative ring the conclusion fails, and what breaks it is that the two cofactors need not be units. In $R = k[s,t]/(s^2, st^2)$ the element $s$ divides $s + st$, because $s + st = s(1+t)$, and $s + st$ divides $s$, because $s = (s+st)(1-t)$; but the units of $R$ are the classes $c + s(b + et)$ with $c \neq 0$, and these multiply $s$ to $cs$, so $s+st$ is not an associate of $s$.

**Corollary.** Association is an equivalence relation, and divisibility induces a partial order on the associate classes of an integral domain: $[a] \leq [b]$ exactly when $a \mid b$. The class of $0$ is the largest element, and the class of the units is the smallest.

**Proof.** Reflexivity, symmetry and transitivity follow from $1 \in R^{\times}$ and the closure of $R^{\times}$ under inverses and products; antisymmetry on classes is the proposition above. $\square$

### Irreducible and Prime Elements

Immediately above a domain in the chain one asks which elements cannot be factored further and which control divisibility of products.

**Definition.** Let $R$ be an integral domain. A nonzero non-unit $a \in R$ is

**(a)** **irreducible** if every factorisation $a = bc$ has $b$ or $c$ a unit;

**(b)** **prime** if $a \mid bc$ always implies $a \mid b$ or $a \mid c$.

**Proposition.** Let $R$ be an integral domain.

**(a)** A prime element is irreducible.

**(b)** The ideal $(p)$ generated by a prime element $p$ is a prime ideal, and conversely if $(p)$ is prime and $p \neq 0$ then $p$ is prime.

**Proof.** (a) Let $p$ be prime and $p = bc$. Since $p \mid bc = p$, primality gives $p \mid b$ or $p \mid c$. If $p \mid b$, say $b = pd$, then $p = pdc$ and cancellation of $p \neq 0$ gives $dc = 1$, so $c$ is a unit; the other case is symmetric. (b) $ab \in (p)$ means $p \mid ab$, which for prime $p$ means $p \mid a$ or $p \mid b$, that is $a \in (p)$ or $b \in (p)$; conversely $(p)$ prime says $p \mid ab$ implies $p \mid a$ or $p \mid b$. $\square$

**Remark.** The converse of (a) fails, and its failure is the arithmetic obstruction that the rung *Unique Factorisation Domains*, below this article in this category, is defined to exclude: in $\mathbb{Z}[\sqrt{-5}]$ the element $2$ is irreducible but not prime. What is missing in a general domain is not the factorisation theory but the existence of greatest common divisors, which *GCD Domains*, below this article in this category, adds.

---

## Characteristic

### The Characteristic of a Domain

**Definition.** The **characteristic** $\operatorname{char} R$ of a unital ring $R$ is the least positive integer $n$ with $n \cdot 1 = 0$, if such an $n$ exists, and $0$ otherwise. Equivalently, $\operatorname{char} R$ is the order of $1$ in the additive group $(R,+)$ when that order is finite, the two conventions agreeing under the first one, and it generates the kernel of the unique unital homomorphism

$$
\chi : \mathbb{Z} \to R, \qquad \chi(n) = n \cdot 1 .
$$

**Theorem.** Let $R$ be an integral domain. Then $\operatorname{char} R$ is either $0$ or a prime number. In particular $\operatorname{char} R \neq 1$, and no domain has composite characteristic.

**Proof.** Suppose $n = \operatorname{char} R$ is finite and $n = ab$ with $a, b > 1$. Then $(a \cdot 1)(b \cdot 1) = (ab) \cdot 1 = n \cdot 1 = 0$, and since $R$ is a domain one factor vanishes, so $a \cdot 1 = 0$ or $b \cdot 1 = 0$, contradicting the minimality of $n$. Hence $n$ has no proper factorisation. $\square$

**Corollary.** $\mathbb{Z}/6\mathbb{Z}$ is not an integral domain, since it has characteristic $6$; a domain of characteristic $0$ contains a copy of $\mathbb{Z}$ and no finite subring, and a domain of characteristic $p$ contains a copy of $\mathbb{F}_p$. The quotient $\mathbb{Z}/p\mathbb{Z}$ is the field $\mathbb{F}_p$, the field axioms being those of *Fields*, later in this category.

**Proposition (freshman's dream).** Let $R$ be a commutative ring of prime characteristic $p$. Then for all $x, y \in R$ and all $n \geq 1$,

$$
(x + y)^{p^n} = x^{p^n} + y^{p^n}, \qquad (xy)^{p^n} = x^{p^n} y^{p^n} .
$$

**Proof.** For $n = 1$, expand $(x+y)^p$ by the binomial theorem of *Commutative Rings*. Each binomial coefficient $\binom{p}{k}$ with $0 < k < p$ is divisible by $p$ and so vanishes in $R$, leaving $x^p + y^p$; the second identity is the commutativity of $R$. The general case follows by iterating the case $n = 1$. $\square$

### The Prime Subring and the Prime Field

The image of $\chi$ is the smallest subring of $R$ containing $1$.

**Definition.** The **prime subring** of a unital ring $R$ is the image of $\chi : \mathbb{Z} \to R$, the subring generated by $1$.

**Proposition.** Let $R$ be an integral domain, with prime subring $P$.

**(a)** If $\operatorname{char} R = 0$ then $\chi$ is injective, so $P \cong \mathbb{Z}$.

**(b)** If $\operatorname{char} R = p$ then $P \cong \mathbb{F}_p$, a field, and $P$ is the **prime field** of $R$.

**(c)** The characteristic of a subring of $R$ that contains $1$ equals $\operatorname{char} R$, and its prime subring is $P$.

**Proof.** (a) If $\chi(m) = \chi(n)$ with $m > n$ then $(m-n) \cdot 1 = 0$ with $m - n > 0$, contradicting $\operatorname{char} R = 0$. (b) The kernel of $\chi$ is $p\mathbb{Z}$ and $\mathbb{Z}/p\mathbb{Z}$ is a field. (c) The element $1$ and the subring it generates are the same in $R$ and in a subring containing $1$. $\square$

**Proposition (embedding of the prime field).** Let $R$ be an integral domain. Then $R$ contains a smallest subfield, namely $\mathbb{Q}$ if $\operatorname{char} R = 0$ and $\mathbb{F}_p$ if $\operatorname{char} R = p$.

**Proof.** In prime characteristic the prime subring is the field $\mathbb{F}_p$ by the proposition above. In characteristic $0$ the prime subring is $\mathbb{Z}$, which is not a field; it is contained in every subfield of $R$, and the smallest subfield containing it is its fraction field. $\square$

The fraction field of a domain is constructed in *Localization and the Fraction Field*, below this article in this category: every integral domain $R$ embeds in a field $\operatorname{Frac}(R)$, its **fraction field**, characterised by the property that every injective homomorphism from $R$ into a field extends uniquely to $\operatorname{Frac}(R)$. In characteristic $0$ the fraction field of $\mathbb{Z}$ is $\mathbb{Q}$; in prime characteristic the fraction field of $\mathbb{F}_p$ is $\mathbb{F}_p$ itself.

---

## Roots of Polynomials

### The Root Theorem

The domain hypothesis converts a statement about divisibility of polynomials into the finite bound on roots that the applications below this article rely on.

**Definition.** Let $f \in R[x]$ and $a \in R$. Then $a$ is a **root** of $f$ if $f(a) = 0$, where $f(a) = \sum_k c_k a^k$ for $f = \sum_k c_k x^k$.

**Lemma.** Let $R$ be a commutative ring, $f \in R[x]$ and $a \in R$ with $f(a) = 0$. Then $f = (x - a)g$ for some $g \in R[x]$, and $\deg g = \deg f - 1$ when $f \neq 0$.

**Proof.** For every $k \geq 1$, $x^k - a^k = (x - a)(x^{k-1} + x^{k-2}a + \cdots + a^{k-1})$; the identity is verified by expanding the right-hand side, and it uses only distributivity. Hence, with $f = \sum_{k=0}^{n} c_k x^k$,

$$
f(x) = f(x) - f(a) = \sum_{k=1}^{n} c_k (x^k - a^k) = (x-a) \sum_{k=1}^{n} c_k (x^{k-1} + x^{k-2}a + \cdots + a^{k-1}),
$$

which exhibits $g$ of the stated degree when $c_n \neq 0$. $\square$

**Theorem (root theorem).** Let $R$ be an integral domain and let $f \in R[x]$ have degree $< m$. If $f$ has $m$ distinct roots $a_1, \ldots, a_m$ in $R$, then $f = 0$.

**Proof.** Induction on $m$. For $m = 0$ the hypothesis on the degree says $f = 0$. For $m \geq 1$, the lemma applied to the root $a_1$ gives $f = (x - a_1)g$ with $\deg g < m - 1$. For $i \geq 2$,

$$
0 = f(a_i) = (a_i - a_1) g(a_i),
$$

and $a_i - a_1 \neq 0$ since the roots are distinct, so $g(a_i) = 0$ because $R$ is a domain. Thus $g$ has the $m - 1$ distinct roots $a_2, \ldots, a_m$ and degree $< m - 1$, and the induction hypothesis gives $g = 0$, hence $f = 0$. $\square$

### Consequences

**Corollary.** Let $R$ be an integral domain and $f \in R[x]$ nonzero of degree $n$. Then $f$ has at most $n$ roots in $R$.

**Proof.** If $f$ had $n+1$ distinct roots, the root theorem with $m = n+1$ would give $f = 0$, since $\deg f = n < n+1$. $\square$

**Corollary.** Let $R$ be an integral domain and let $f, g \in R[x]$ have degree $\leq n$. If $f(a) = g(a)$ for $n+1$ distinct elements $a \in R$, then $f = g$.

**Proof.** Apply the previous corollary to $f - g$, of degree $\leq n$. $\square$

**Example.** Over $\mathbb{Z}/4\mathbb{Z}$, which is not a domain, the polynomial $2x$ of degree $1$ has the two roots $0$ and $2$; over $\mathbb{Z}/8\mathbb{Z}$, the polynomial $x^2 - 1$ has the four roots $1, 3, 5, 7$, since each of these is its own inverse modulo $8$. So the number of roots can exceed the degree when the ring has zero divisors, and the domain hypothesis in the root theorem and in both corollaries cannot be dropped. Over a domain the bound is sharp: $x^2 - 1$ has exactly the two roots $\pm 1$ in $\mathbb{Z}$, and $x^2 + 1$ has none.

**Corollary.** A finite integral domain is a field.

**Proof.** Let $R$ be a finite domain and $a \in R$ nonzero. The powers $a, a^2, a^3, \ldots$ cannot all be distinct in the finite set $R$, so $a^i = a^j$ for some $i > j \geq 1$. Then $a^j (a^{i-j} - 1) = 0$ with $a^j \neq 0$, so $a^{i-j} = 1$ and $a \cdot a^{i-j-1} = 1$ exhibits $a$ as a unit. $\square$

---

## The Shape of the Rung

### Examples

**Example ($\mathbb{Z}$).** The integers form an integral domain of characteristic $0$, whose units are $\pm 1$ and whose irreducible elements are the primes. Divisibility in $\mathbb{Z}$ is governed by the absolute value of the divisor, and the prime factorisation of an integer is the model case of the rungs above this article in this category.

**Example ($K[x]$, $K$ a field).** The polynomial ring over a field is an integral domain of characteristic $\operatorname{char} K$, with units the nonzero constants, by the proposition above. Its irreducibles are the irreducible polynomials, and the root theorem gives the standard test: a polynomial of degree $2$ or $3$ over a field is irreducible exactly when it has no root in the field.

**Example (quadratic rings).** For a squarefree integer $d$, $\mathbb{Z}[\sqrt{d}]$ is an integral domain, being a subring of $\mathbb{C}$. Its multiplicative structure is governed by the norm

$$
N(a + b\sqrt{d}) = a^2 - d b^2 = (a + b\sqrt{d})(a - b\sqrt{d}),
$$

which is multiplicative, so that $N(xy) = N(x)N(y)$, and an element is a unit exactly when its norm is a unit of $\mathbb{Z}$, that is, when $N(x) = \pm 1$; when $d < 0$ the norm is non-negative and the condition is $N(x) = 1$. For $d = -1$ and $d = -5$ the norm reads $N(a+bi) = a^2 + b^2$ and $N(a + b\sqrt{-5}) = a^2 + 5b^2$. This $N$ is the norm form on a quadratic ring; it is not the Euclidean degree function of *Euclidean Domains*, below this article in this category, although the letter is the same.

### Where the Rung Sits

The integral domain is the point at which cancellation and a well-behaved divisibility theory are available, and it is the weakest rung of the commutative chain at which that is so: a reduced ring such as $\mathbb{Z} \times \mathbb{Z}$ has cancellation only for elements that are not zero divisors, and its divisibility is not a partial order on associate classes.

**Remark (the rungs above).** Every field is an integral domain, and the converse fails, witness $\mathbb{Z}$; the division rings that generalise fields by dropping commutativity are *Division Rings*, later in this category, and a non-commutative division ring is not an integral domain, since the terminology reserves the word for the commutative case.

**Remark (what the rung does not yet supply).** Two elements of a domain need not have a greatest common divisor, and an irreducible element need not be prime. The first failure is repaired by *GCD Domains*, below this article in this category; the second, and with it unique factorisation, by the chain *Unique Factorisation Domains*, *Principal Ideal Domains*, *Euclidean Domains*, each below this article in this category. The standard witness in both cases is $\mathbb{Z}[\sqrt{-5}]$, which is an integral domain, which is not a unique factorisation domain because

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

are two factorisations into irreducibles differing neither by order nor by units; the verification is carried out in *Unique Factorisation Domains*, below this article in this category.

---

## Summary

An integral domain is a commutative ring with $1 \neq 0$ and no zero divisors, equivalently a commutative ring in which $ab = 0$ forces $a = 0$ or $b = 0$. Cancellation holds for nonzero factors, subrings and polynomial rings over a domain remain domains, and a product of two nonzero rings is never a domain. Divisibility is a preorder, equivalent to reverse inclusion of principal ideals, and it becomes a partial order on associate classes because in a domain $a \mid b$ and $b \mid a$ force $a \sim b$; this is the point at which domains are separated from general commutative rings.

A nonzero non-unit is irreducible when it admits no nontrivial factorisation and prime when it divides a product only through its factors; every prime is irreducible, and the converse can fail. The characteristic of a domain is $0$ or a prime, and the prime subring is $\mathbb{Z}$ in characteristic $0$ and the field $\mathbb{F}_p$ in characteristic $p$; every domain contains exactly one smallest field, $\mathbb{Q}$ or $\mathbb{F}_p$. Over a domain a polynomial of degree $< m$ with $m$ distinct roots vanishes identically, so a nonzero polynomial of degree $n$ has at most $n$ roots, and a finite domain is a field. The greatest common divisor, the fraction field and the factorisation rungs are the content of articles below this one in the category, each of which is a statement about how well divisibility in a domain behaves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Integral domain (commutative ring with $1 \neq 0$ and no zero divisors) |
| $K$, $F$ | Fields, where the field axioms are needed |
| $R^{\times}$ | Group of units |
| $a \mid b$ | $a$ divides $b$, that is, $b = ac$ for some $c \in R$ |
| $a \sim b$ | Associates, $a = ub$ with $u \in R^{\times}$ |
| $(a)$, $(a, b)$ | Principal ideal generated by $a$; ideal generated by $a$ and $b$ |
| irreducible, prime | Nonzero non-unit admitting no nontrivial factorisation; dividing products only through factors |
| $R[x]$ | Polynomial ring in one indeterminate |
| $f(a)$ | Evaluation of $f$ at $a$; $a$ a root when $f(a) = 0$ |
| $\operatorname{char} R$ | Characteristic of $R$ |
| $n \cdot 1$ | Sum of $n$ copies of $1$ |
| $\chi : \mathbb{Z} \to R$ | The unique unital homomorphism, $n \mapsto n \cdot 1$ |
| $\mathbb{F}_p$ | The field $\mathbb{Z}/p\mathbb{Z}$ of $p$ elements |
| $\operatorname{Frac}(R)$ | Fraction field of $R$ |
| $N(a + b\sqrt{d}) = a^2 - d b^2$ | Norm form on a quadratic ring $\mathbb{Z}[\sqrt{d}]$ |

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for integral domains, cancellation and divisibility, with examples.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the characteristic of a domain, the prime subfield and the root theorem.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the prime subring, characteristic and polynomial roots over a domain.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for domains, divisibility and the passage to the fraction field.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for characteristic, the prime field, and the arithmetic of quadratic rings.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for $\mathbb{Z}[\sqrt{-5}]$ and the failure of unique factorisation in quadratic rings.
