
# __Unique Factorisation Domains__

## Introduction

An integral domain is a **unique factorisation domain** when every nonzero non-unit is a product of irreducible elements in exactly one way up to order and multiplication by units. The definition is the arithmetic one, and the article's work is to make it checkable: a domain is a unique factorisation domain exactly when factorisations exist and every irreducible is prime, and in that case the divisibility theory of the domain is the arithmetic of its prime elements, with the gcd of a pair read off from the two factorisations. The rung is the highest in the category at which this reading of divisibility is available by elements alone.

Two tools make the theory effective and are the part of this article that other articles cite: **Gauss's lemma**, which controls the passage of factorisation between a unique factorisation domain and its polynomial ring, and **Eisenstein's criterion**, which certifies irreducibility of a polynomial from the divisibility of its coefficients. The failure that the rung is defined against is $\mathbb{Z}[\sqrt{-5}]$, where $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ are two factorisations into irreducibles, and it is worked in full here.

Throughout, $R$ is an integral domain; divisibility, associates, irreducibles, primes and the gcd are used in the sense of *Integral Domains* and *GCD Domains*, both above this article in this category. Fields are used where a field is needed and are introduced in *Fields*, later in this category. The fraction field $\operatorname{Frac}(R)$, used for Gauss's lemma, is constructed in *Localization and the Fraction Field*, below this article in this category.

---

## Irreducibles, Primes and Factorisation

### The Vocabulary

Recall from *Integral Domains*, above, that a nonzero non-unit $a$ of the domain $R$ is **irreducible** if every factorisation $a = bc$ has $b$ or $c$ a unit, and **prime** if $a \mid bc$ always implies $a \mid b$ or $a \mid c$. Every prime element is irreducible, and the converse may fail; the failure is exactly what a unique factorisation domain excludes.

**Definition.** An integral domain $R$ is a **unique factorisation domain** (UFD) if

**(a)** every nonzero non-unit of $R$ is a product of irreducible elements, and

**(b)** the factorisation is unique up to order and units: if

$$
a = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s
$$

with all $p_i$ and $q_j$ irreducible, then $r = s$ and, after reordering, $p_i \sim q_i$ for every $i$.

Condition (a) speaks of nonzero non-units, since $0$ and the units are not products of irreducibles; condition (b) is the uniqueness, where the order of the factors is irrelevant by commutativity, so the content of the condition is the pairing of the factors up to units.

**Definition.** $R$ satisfies the **ascending chain condition on principal ideals** (ACCP) if there is no infinite strictly increasing chain

$$
(a_1) \subsetneq (a_2) \subsetneq (a_3) \subsetneq \cdots
$$

of principal ideals of $R$.

### Existence and Uniqueness

**Theorem.** An integral domain $R$ is a unique factorisation domain if and only if every irreducible element of $R$ is prime and every nonzero non-unit of $R$ is a product of irreducibles. Equivalently, $R$ is a unique factorisation domain if and only if $R$ satisfies ACCP and every irreducible element of $R$ is prime.

**Proof.** Suppose first that $R$ is a unique factorisation domain. If $p$ is irreducible and $p \mid ab$, say $ab = pc$, factor $a$, $b$ and $c$ into irreducibles. The two factorisations of $ab$ and of $pc$ have the same irreducible factors up to order and units, so $p$ is an associate of a factor of $a$ or of $b$; hence $p \mid a$ or $p \mid b$. For ACCP, a strictly increasing chain $(a_1) \subsetneq (a_2) \subsetneq \cdots$ gives $a_n = a_{n+1} b_n$ with $b_n$ a non-unit, so a factorisation of $a_1$ would refine at every step, contradicting the finiteness of $r$ in the definition.

Conversely, suppose every irreducible is prime and every nonzero non-unit is a product of irreducibles. Let $p_1 \cdots p_r = q_1 \cdots q_s$ with all factors irreducible, hence all prime. Since $p_1$ is prime and divides the right-hand product, $p_1 \mid q_j$ for some $j$; as $q_j$ is irreducible and $p_1$ is not a unit, $p_1 \sim q_j$. Reordering so that $j = 1$ and cancelling $p_1$ by *Integral Domains*, above, gives $p_2 \cdots p_r = q_2 \cdots q_s$, and induction gives $r = s$ and the pairing. For the second form of the criterion, ACCP supplies the existence of factorisations: if a nonzero non-unit $a$ had none, then $a = a_1 b_1$ with both factors non-units, at least one of $a_1, b_1$ would again have no factorisation, and iterating would produce a strictly increasing chain $(a) \subsetneq (a_1) \subsetneq (a_2) \subsetneq \cdots$, contradicting ACCP. $\square$

**Corollary.** Let $R$ be a unique factorisation domain and let $a = u p_1^{e_1} \cdots p_r^{e_r}$ be the factorisation of a nonzero non-unit, with the $p_i$ pairwise non-associate irreducibles and $u$ a unit. Then the divisors of $a$ are, up to units, exactly the products $p_1^{f_1} \cdots p_r^{f_r}$ with $0 \leq f_i \leq e_i$, and the gcd of two nonzero elements is the product of the common prime factors, each to the smaller exponent.

**Proof.** Every divisor is a product of irreducibles drawn from the factors of $a$ with exponents bounded by $e_i$, by uniqueness applied to the factorisation of a multiple; conversely each such product divides $a$. The statement about the gcd is *GCD Domains*, above. $\square$

**Remark.** The corollary is the sense in which a unique factorisation domain has an arithmetic: divisibility is decided by comparing exponents of prime elements. The article *Bézout Domains*, above this article in this category, shows that the class of domains in which this reading is available by identity instead of by factorisation is incomparable with the class of unique factorisation domains; $\mathbb{Z}[x]$ is a unique factorisation domain that is not a Bézout domain.

### Euclid's Lemma

**Theorem (Euclid's lemma).** Let $R$ be a Bézout domain, or more generally a domain in which every gcd is a Bézout combination, and let $p \in R$ be irreducible. If $p \mid ab$ then $p \mid a$ or $p \mid b$.

**Proof.** Suppose $p \nmid a$. Since $p$ is irreducible, its divisors are the units and the associates of $p$; as $p \nmid a$, the element $p$ is not a common divisor of $p$ and $a$, so $\gcd(p,a) \sim 1$. Write $up + va = 1$ with $u, v \in R$, possible by *Bézout Domains*, above. Multiplying by $b$ gives

$$
b = upb + vab .
$$

The first term is divisible by $p$, and the second is divisible by $p$ because $p \mid ab$; hence $p \mid b$. $\square$

**Corollary.** In a Bézout domain every irreducible element is prime.

**Proof.** This is the lemma with the definition of a prime element. $\square$

Thus in $\mathbb{Z}$ the lemma reads: if a prime divides a product then it divides a factor, which is the step that makes the fundamental theorem of arithmetic independent of the uniqueness of factorisation. In a unique factorisation domain the lemma is true for prime elements by definition, and the criterion of the previous section makes it true for irreducibles.

---

## The Failure in $\mathbb{Z}[\sqrt{-5}]$

### The Two Factorisations of $6$

Let $R = \mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$ with the multiplicative norm

$$
N(a + b\sqrt{-5}) = a^2 + 5b^2, \qquad N(xy) = N(x)N(y),
$$

as in *Integral Domains*, above. The units are the elements of norm $1$, namely $\pm 1$, so two elements are associates exactly when they are equal up to sign.

| Element | Norm | Irreducible? | Reason |
|---|---|---|---|
| $2$ | $4$ | yes | a factor would have norm $2$, and $a^2 + 5b^2 = 2$ has no integer solution |
| $3$ | $9$ | yes | a factor would have norm $3$, and $a^2 + 5b^2 = 3$ has no integer solution |
| $1 + \sqrt{-5}$ | $6$ | yes | a factor would have norm $2$ or $3$, both impossible |
| $1 - \sqrt{-5}$ | $6$ | yes | as for $1 + \sqrt{-5}$ |

**Proposition.** The two factorisations

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

are factorisations of $6$ into irreducibles, and they differ neither by the order of the factors nor by units.

**Proof.** Both identities are verified by expanding: $2 \cdot 3 = 6$ and $(1+\sqrt{-5})(1-\sqrt{-5}) = 1 - (-5) = 6$. The four factors are irreducible by the table, whose entries use the multiplicativity of $N$: a proper factor of an element of norm $n$ would have norm a proper divisor of $n$ greater than $1$. Finally the two sides are not the same list up to units: $N(2) = 4$ while $N(1 \pm \sqrt{-5}) = 6$, so no factor of the left side is an associate of a factor of the right side, and the units are $\pm 1$. $\square$

**Corollary.** $\mathbb{Z}[\sqrt{-5}]$ is not a unique factorisation domain.

**Proof.** The proposition exhibits a nonzero non-unit with two factorisations into irreducibles that do not agree up to order and units. $\square$

**Corollary.** In $\mathbb{Z}[\sqrt{-5}]$ the element $2$ is irreducible but not prime.

**Proof.** $2$ is irreducible by the table. It divides $(1+\sqrt{-5})(1-\sqrt{-5}) = 6$, but it divides neither factor: $2 \nmid 1 + \sqrt{-5}$ and $2 \nmid 1 - \sqrt{-5}$, since $2$ does not divide either coefficient. $\square$

So the criterion of the previous section fails at exactly the point it names: irreducibles need not be prime. The same ring is the standard witness that a domain need not be a GCD domain (*GCD Domains*, above), and the two failures have the same content, since a unique factorisation domain is a GCD domain in which the gcd is computed by exponents.

---

## Content and Gauss's Lemma

### Content and Primitive Polynomials

Let $R$ be a unique factorisation domain and let $f = a_n x^n + \cdots + a_0 \in R[x]$ be nonzero. The **content** of $f$ is the greatest common divisor of its coefficients,

$$
c(f) = \gcd(a_0, a_1, \ldots, a_n),
$$

which exists by *GCD Domains*, above, and is defined up to associates; a representative is fixed once for all. The polynomial $f$ is **primitive** if $c(f) \sim 1$.

**Lemma.** Every nonzero $f \in R[x]$ can be written $f = c(f) f_0$ with $f_0 \in R[x]$ primitive.

**Proof.** Divide each coefficient by the gcd of them all; the quotient polynomial has content a unit. $\square$

### Gauss's Lemma

**Theorem (Gauss's lemma).** Let $R$ be a unique factorisation domain and $F = \operatorname{Frac}(R)$ its fraction field, constructed in *Localization and the Fraction Field*, below this article in this category.

**(a)** For nonzero $f, g \in R[x]$, $\ c(fg) \sim c(f) c(g)$. In particular the product of two primitive polynomials is primitive.

**(b)** A primitive $f \in R[x]$ is irreducible in $R[x]$ if and only if it is irreducible in $F[x]$.

**Proof sketch.** (a) It suffices to show that the product of primitive polynomials is primitive. Let $p \in R$ be a prime element; a primitive polynomial has at least one coefficient not divisible by $p$, so its image in $(R/pR)[x]$ is nonzero, and the same holds for the other factor. Since $p$ is prime the ring $R/pR$ is an integral domain by *Integral Domains*, above, so the image of the product is nonzero: $fg$ has a coefficient not divisible by $p$. Hence no prime element divides $c(fg)$, and $c(fg)$ is a unit; the general statement follows by writing $f = c(f)f_0$ and $g = c(g)g_0$ with $f_0, g_0$ primitive. (b) Let $f$ be primitive. If $f$ is reducible in $F[x]$, say $f = gh$ with $g, h \in F[x]$ of positive degree, clear denominators and divide out contents to write $f = c\,g_0h_0$ with $c \in F$ and $g_0, h_0 \in R[x]$ primitive of positive degree; by (a) the product $g_0h_0$ is primitive, so taking contents gives $c \sim c(f) \sim 1$, that is, $c$ is a unit of $R$, and $f = (c\,g_0)h_0$ is a factorisation of $f$ in $R[x]$ into two elements of positive degree, neither a unit. Hence $f$ is reducible in $R[x]$. Conversely, if $f$ is reducible in $R[x]$, say $f = gh$ with $g, h$ non-units, then $c(g)c(h) \sim c(f) \sim 1$ by (a), so neither $g$ nor $h$ is a constant and both have positive degree, hence both are non-units of $F[x]$; so $f$ is reducible in $F[x]$. $\square$

**Remark.** Part (b) needs the fraction field, which is why the statement is placed here and not in the Euclidean theory of polynomials. The content is not multiplicative on sums: $c(f+g)$ need not divide $c(f)c(g)$.

---

## Eisenstein's Criterion

### The Criterion

**Theorem (Eisenstein's criterion).** Let $R$ be a unique factorisation domain and let

$$
f = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_0 \in R[x]
$$

be primitive of positive degree. If there is a prime element $p \in R$ with

$$
p \nmid a_n, \qquad p \mid a_i \ \text{for} \ 0 \leq i < n, \qquad p^2 \nmid a_0,
$$

then $f$ is irreducible in $R[x]$.

**Proof.** Suppose $f = gh$ with $g, h$ non-units of $R[x]$. Since $f$ is primitive of positive degree, neither factor is a non-unit constant, so both have positive degree and $\deg g + \deg h = n$. Reducing coefficients modulo $p$ gives, in $(R/pR)[x]$,

$$
\bar f = \bar a_n x^n, \qquad \bar a_n \neq 0,
$$

because all lower coefficients vanish modulo $p$. The ring $(R/pR)[x]$ is a polynomial ring over the domain $R/pR$, so $\bar g$ and $\bar h$ are monomials; since $\deg \bar g \leq \deg g$ and $\deg \bar h \leq \deg h$ with $\deg \bar g + \deg \bar h = n = \deg g + \deg h$, both degrees are positive. Hence the constant terms of $g$ and of $h$ are divisible by $p$, and $p^2$ divides $g(0)h(0) = a_0$, contradicting the hypothesis. $\square$

**Corollary.** Let $R$ be a unique factorisation domain and let $f \in R[x]$ have positive degree. If $f$ is not primitive then $f$ is reducible in $R[x]$, since $f = c(f) f_0$ with $c(f)$ a non-unit of $R$ and $f_0$ of the same positive degree, hence a non-unit of $R[x]$. Eisenstein's criterion is therefore applied only to primitive polynomials, after dividing out the content.

### Examples

**Example ($x^3 - 2$).** The polynomial $x^3 - 2$ is primitive in $\mathbb{Z}[x]$ and Eisenstein at $p = 2$: the leading coefficient $1$ is not divisible by $2$, the coefficients of $x^2$, $x$ and $x^0$ are $0, 0, -2$, all divisible by $2$, and $4 \nmid 2$. Hence $x^3 - 2$ is irreducible over $\mathbb{Q}$.

**Example ($x^4 + 1$).** The polynomial $x^4 + 1$ is not itself Eisenstein, but its translate is. Expanding,

$$
(x+1)^4 + 1 = x^4 + 4x^3 + 6x^2 + 4x + 2,
$$

the coefficients $4, 6, 4, 2$ are divisible by $2$, the leading coefficient $1$ is not, and the constant term $2$ is not divisible by $4$: so the translate is Eisenstein at $2$. Since $x \mapsto x+1$ is a ring automorphism of $\mathbb{Z}[x]$, irreducibility of the translate is equivalent to irreducibility of $x^4 + 1$.

**Theorem (irreducibility of $\Phi_p$).** Let $p$ be a prime number and let

$$
\Phi_p(x) = \frac{x^p - 1}{x - 1} = x^{p-1} + x^{p-2} + \cdots + x + 1 \in \mathbb{Z}[x].
$$

Then $\Phi_p$ is irreducible in $\mathbb{Z}[x]$.

**Proof.** Substitute $x + 1$ for $x$:

$$
\Phi_p(x+1) = \frac{(x+1)^p - 1}{x} = \sum_{k=1}^{p} \binom{p}{k} x^{k-1} = x^{p-1} + p x^{p-2} + \cdots + p .
$$

The coefficients $\binom{p}{k}$ with $1 \leq k \leq p-1$ are divisible by $p$, the leading coefficient $\binom{p}{p} = 1$ is not, and the constant term $\binom{p}{1} = p$ is not divisible by $p^2$. So $\Phi_p(x+1)$ is Eisenstein at $p$, hence irreducible in $\mathbb{Z}[x]$, and the substitution $x \mapsto x+1$ preserves irreducibility. $\square$

**Corollary.** $[\mathbb{Q}(\zeta_p) : \mathbb{Q}] = p - 1$ for a primitive $p$-th root of unity $\zeta_p$, since $\Phi_p$ is the minimal polynomial of $\zeta_p$ over $\mathbb{Q}$; the theory of the cyclotomic fields is *Cyclotomic Fields*, later in this category.

---

## Polynomial Rings and Unique Factorisation

### Transfer to the Polynomial Ring

**Theorem.** If $R$ is a unique factorisation domain then so is $R[x]$, and the units of $R[x]$ are the units of $R$.

**Proof sketch.** Let $f$ be a nonzero non-unit and write $f = c(f) f_0$ with $f_0$ primitive. The content $c(f) \in R$ is a product of irreducibles of $R$, which remain irreducible in $R[x]$; and $f_0$ factors in $F[x]$, which is a Euclidean domain and hence a unique factorisation domain, by *Euclidean Domains*, below this article in this category, into irreducible factors of $F[x]$, which by Gauss's lemma lie in $R[x]$ up to units of $F$ and can be taken primitive. Uniqueness is inherited from the unique factorisation in $F[x]$ together with the uniqueness of the content, which is an element of the unique factorisation domain $R$. $\square$

**Corollary.** $\mathbb{Z}[x]$ and, for a field $F$, the ring $F[x_1, \ldots, x_n]$ are unique factorisation domains, by induction on the number of indeterminates.

**Corollary.** For a field $F$ the polynomial ring $F[x]$ is a unique factorisation domain; more precisely $F[x]$ is a Euclidean domain, hence a principal ideal domain, hence a unique factorisation domain, and therefore Noetherian. The Euclidean and principal ideal rungs are *Euclidean Domains* and *Principal Ideal Domains*, below this article in this category, and the Noetherian statement is *Noetherian and Artinian Rings*, below this article in this category.

**Corollary.** The chain of implications

$$
\text{Euclidean} \Longrightarrow \text{principal} \Longrightarrow \text{unique factorisation} \Longrightarrow \text{integral domain}
$$

holds, and each implication is strict: $\mathbb{Z}[(1+\sqrt{-19})/2]$ is a principal ideal domain that is not Euclidean, $\mathbb{Z}[x]$ is a unique factorisation domain that is not principal, and $\mathbb{Z}[\sqrt{-5}]$ is a domain that is not a unique factorisation domain. The strictness of the first two implications is established in *Euclidean Domains* and *Principal Ideal Domains*, below this article in this category, and the third by the section on $\mathbb{Z}[\sqrt{-5}]$ of this article.

### Factorisation of Polynomials over a Field

**Theorem.** Let $F$ be a field. Every nonzero $f \in F[x]$ has a factorisation

$$
f = c \, p_1(x) \, p_2(x) \cdots p_r(x)
$$

with $c \in F^{\times}$ and the $p_i$ monic irreducible polynomials, and this factorisation is unique up to the order of the factors.

**Proof.** $F[x]$ is a unique factorisation domain by the corollary above; the units of $F[x]$ are the nonzero constants, and multiplying an irreducible by the inverse of its leading coefficient makes it monic, which fixes the representative of each associate class. $\square$

**Corollary.** Let $F$ be a field and $f \in F[x]$ nonzero. Then $f$ is irreducible in $F[x]$ if and only if it is not the product of two polynomials of positive degree, and a polynomial of degree $2$ or $3$ is irreducible if and only if it has no root in $F$.

**Proof.** The first statement is the definition of irreducibility in a domain. For the second, a reducible polynomial of degree $2$ or $3$ has a factor of degree $1$, hence a root, by the root theorem of *Integral Domains*, above; and a root gives a linear factor by the same theorem. $\square$

**Corollary.** The quotient $F[x]/(f)$ of the polynomial ring by a nonzero polynomial $f$ decomposes according to the factorisation of $f$ into irreducibles, by the Chinese remainder theorem of *Commutative Rings*, above; the ideal structure of the quotient under a given factorisation is *Principal Ideal Domains*, below this article in this category.

**Remark.** The divisibility theory of $F[x]$ is the arithmetic of its irreducible polynomials: a nonzero $g$ divides $f$ exactly when every irreducible factor of $g$ occurs in the factorisation of $f$ with an exponent at least as large, by the corollary on divisors above. This is the form in which divisibility is used whenever a quotient $F[x]/(f)$ is studied one irreducible factor of $f$ at a time.

---

## Summary

A unique factorisation domain is an integral domain in which every nonzero non-unit is a product of irreducibles and this factorisation is unique up to order and units. It is equivalently a domain satisfying the ascending chain condition on principal ideals in which every irreducible is prime, or a domain in which every irreducible is prime and factorisations exist. In such a ring the divisors of an element are read off from the exponents in its factorisation, and the gcd of two elements is the product of the common prime factors to the smaller exponent. Euclid's lemma, that a prime element dividing a product divides a factor, holds in every Bézout domain, where it follows from the Bézout combination $up + va = 1$; in a unique factorisation domain it is the definition of primality applied to irreducibles.

The rung is strictly stronger than being a domain: $\mathbb{Z}[\sqrt{-5}]$ is a domain in which $6 = 2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ are two inequivalent factorisations into irreducibles, so $2$ is irreducible and not prime. Over a unique factorisation domain the polynomial ring is again a unique factorisation domain, by Gauss's lemma: the content is multiplicative, a primitive polynomial is irreducible over the ring exactly when it is irreducible over the fraction field, and Eisenstein's criterion certifies irreducibility from the divisibility of the coefficients, as in the proof that $\Phi_p$ is irreducible. Over a field every polynomial factors uniquely into monic irreducibles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Integral domain, and a unique factorisation domain where stated |
| $R^{\times}$ | Group of units |
| $a \mid b$, $a \sim b$ | Divisibility; associates |
| irreducible, prime | Nonzero non-unit with no nontrivial factorisation; dividing products only through factors |
| UFD | Unique factorisation domain |
| ACCP | Ascending chain condition on principal ideals |
| $R[x]$ | Polynomial ring in one indeterminate |
| $c(f)$ | Content of $f$, a gcd of its coefficients |
| primitive | $c(f) \sim 1$ |
| $F = \operatorname{Frac}(R)$ | Fraction field of $R$ |
| $N(a + b\sqrt{-5}) = a^2 + 5b^2$ | Multiplicative norm on $\mathbb{Z}[\sqrt{-5}]$ |
| $\Phi_p(x)$ | Cyclotomic polynomial $x^{p-1} + \cdots + x + 1$ |
| $\zeta_p$ | Primitive $p$-th root of unity |
| PID | Principal ideal domain |

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for irreducibles, primes and the failure of unique factorisation in quadratic rings.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the criterion UFD $\Leftrightarrow$ ACCP plus prime irreducibles, content, Gauss's lemma and Eisenstein's criterion.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for unique factorisation domains, Gauss's lemma and the ideal-theoretic reading of divisibility.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for Eisenstein's criterion, the irreducibility of the cyclotomic polynomials and factorisation over a field.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for $\mathbb{Z}[\sqrt{-5}]$ and the arithmetic of quadratic rings.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra, Volume I* (Van Nostrand, 1958), for content, primitive polynomials and the transfer of unique factorisation to polynomial rings.
