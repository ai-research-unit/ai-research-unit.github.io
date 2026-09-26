
# __Commutative Rings__

## Introduction

The commutative law is a single equation, $ab = ba$, and this article is an account of what it buys. On its own it changes little; combined with the associative and distributive laws it makes the arithmetic of a ring algorithmic in a way that no non-commutative ring allows: powers can be expanded, the product of ideals becomes independent of the order of its factors, sums and products of ideals distribute, and the ideals themselves acquire a theory of primality reflected in a partially ordered set. Everything in the rest of this category is written over a commutative ring, and this article separates the hypotheses that make that possible from those that do not need it.

Throughout, $R$ is a **commutative ring with identity** $1 \neq 0$, and the corpus default is the commutative ring rather than the field. Ideals, left, right and two-sided, generated ideals, the correspondence theorem and quotient rings are the subject of *Rings*, §Ideals and §Quotient Rings, and are used here without restatement; units, zero divisors, nilpotents and idempotents are the vocabulary of *Rings*, §The Multiplicative Vocabulary. The radical of an ideal is defined here, and it is shown to be the intersection of the prime ideals containing it; *Reduced Rings and the Nilradical*, below this article in this category, specialises that theorem to the zero ideal.

---

## The Commutative Law

### What the Law Buys

Commutativity is the assertion that $a b = b a$ for all $a, b \in R$. Three consequences are used constantly. First, the order of the factors in a product is irrelevant: every permutation of $a_1, \ldots, a_n$ leaves $a_1 a_2 \cdots a_n$ unchanged. Second, a power is unambiguous: $a^n$ is the product of $n$ copies of $a$, with $a^m a^n = a^{m+n}$ and $(a^m)^n = a^{mn}$. Third, elements built from a fixed finite set commute with one another, so that if $b$ and $c$ are integer polynomials in $a$ then $bc = cb$. Most of the article works out the third point.

**Remark.** The product of elements and the product of ideals are both written by juxtaposition; the context names the object. The zero ring is excluded by $1 \neq 0$, as in *Rings*.

### Powers and the Binomial Theorem

The binomial coefficients are $\binom{n}{k} = n!/(k!\,(n-k)!)$ for $0 \leq k \leq n$.

**Theorem (binomial theorem).** Let $R$ be a commutative ring, let $a, b \in R$ and let $n \geq 0$. Then

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{\,n-k} .
$$

**Proof.** Expand the product of $n$ factors, each $a + b$. Distributivity expresses $(a+b)^n$ as the sum of all $2^n$ words in the letters $a, b$. By the commutative law a word with $k$ copies of $a$ and $n-k$ copies of $b$ equals $a^k b^{n-k}$, so the words group into $n+1$ classes according to $k$; the class with $k$ copies of $a$ is in bijection with the $k$-element subsets of $\{1, \ldots, n\}$, of which there are $\binom{n}{k}$. $\square$

The proof uses only that $a$ and $b$ commute: an arbitrary word in $a$ and $b$ reduces to $a^k b^{n-k}$ exactly when the two letters commute. In a general ring $(a+b)^2 = a^2 + ab + ba + b^2$ already carries the correction term $ab + ba$.

**Corollary.** If $a$ and $b$ commute then $a - b$ divides $a^n - b^n$ for every $n \geq 1$.

**Proof.** $a^n - b^n = (a-b)(a^{n-1} + a^{n-2}b + \cdots + b^{n-1})$, all factors inside the second bracket commuting with one another. $\square$

**Corollary (Frobenius after $p$ copies).** Let $R$ be a commutative ring of characteristic $p$, a prime. Then $(a+b)^p = a^p + b^p$ for all $a, b \in R$.

**Proof.** Every intermediate coefficient $\binom{p}{k}$ with $0 < k < p$ is divisible by $p$ and vanishes in $R$. $\square$

The full theory of the characteristic belongs to *Integral Domains*, below this article in this category; the corollary needs only that $p \cdot 1 = 0$.

### The Multinomial Theorem

**Theorem (multinomial theorem).** Let $R$ be commutative, let $a_1, \ldots, a_m \in R$ and let $n \geq 0$. Then

$$
(a_1 + \cdots + a_m)^n = \sum_{k_1 + \cdots + k_m = n} \frac{n!}{k_1! \cdots k_m!}\, a_1^{k_1} \cdots a_m^{k_m},
$$

the sum over all $m$-tuples of non-negative integers $(k_1, \ldots, k_m)$ with $k_1 + \cdots + k_m = n$.

**Proof.** Expanding the product of $n$ factors $a_1 + \cdots + a_m$ gives a sum over words of length $n$ in the alphabet $\{1, \ldots, m\}$. In a commutative ring the value of a word depends only on the multiplicities $k_1, \ldots, k_m$ of its letters, and the number of words with prescribed multiplicities is the multinomial coefficient, the number of ways of choosing the positions of each letter. $\square$

**Corollary.** If $a_1, \ldots, a_m$ are idempotent and $a_i a_j = 0$ for $i \neq j$, then $(a_1 + \cdots + a_m)^n = a_1 + \cdots + a_m$ for every $n \geq 1$.

**Proof.** A term of the expansion is indexed by multiplicities $k_1, \ldots, k_m$ with $k_1 + \cdots + k_m = n$. If some $k_i \geq 2$ and some other $k_j \geq 1$, the term contains the factor $a_i a_j = 0$ and vanishes; if some $k_i \geq 2$ with all other $k_j = 0$ then $k_i = n$ and the term is $a_i^{\,n} = a_i$. If instead every $k_i \leq 1$, the term is a product of $n$ distinct idempotents, which vanishes unless $n = 1$. So the sum reduces to $a_1 + \cdots + a_m$. $\square$

This is the computation that makes orthogonal idempotents behave as the identities of their summands; product decompositions are treated in *Localization and the Fraction Field*, below this article in this category.

---

## The Arithmetic of Ideals

### Sums, Products and Intersections

For ideals $I, J$ of $R$ their **sum**, **intersection** and **product** are

$$
I + J = \{a+b : a \in I,\ b \in J\}, \qquad I \cap J = \{x : x \in I \text{ and } x \in J\},
$$

$$
I J = \Bigl\{\sum_{i=1}^{n} a_i b_i : a_i \in I,\ b_i \in J,\ n \geq 0\Bigr\}.
$$

All three are ideals. Sums and intersections are ideals in any ring; the product is a two-sided ideal in any ring and satisfies $IJ \subseteq I \cap J$. What commutativity adds is that the product is generated by the products of generators and that it distributes over sums.

**Proposition.** Let $I, J, K$ be ideals of the commutative ring $R$, and let $I = (A)$, $J = (B)$ be generated by subsets $A, B \subseteq R$.

**(a)** $I + J = (A \cup B)$ and $IJ = (ab : a \in A,\ b \in B)$.

**(b)** $I(J+K) = IJ + IK$, and $(I+J)^2 \subseteq I^2 + IJ + J^2$, with equality if $I \subseteq J$ or $J \subseteq I$.

**(c)** $IJ = JI$, and $I_1 I_2 \cdots I_n$ is independent of the order of the factors.

**(d)** $IJ \subseteq I \cap J$, and $I \cap (J+K) \supseteq (I \cap J) + (I \cap K)$.

**Proof.** (a) $I+J$ consists of the finite $R$-combinations of $A \cup B$. An element of $IJ$ is a sum of products $a_i b_i$ with $a_i$ an $R$-combination of $A$ and $b_i$ of $B$, and expanding gives an $R$-combination of the products $ab$ with $a \in A$, $b \in B$.

(b) Distributivity in $R$ gives the first identity after expanding a finite sum; the second follows from $(I+J)^2 = I^2 + IJ + JI + J^2$ and (c).

(c) A generator $ab$ of $IJ$ equals $ba$, a generator of $JI$; hence the same generators. Induct on $n$.

(d) If $a \in I$, $b \in J$ then $ab \in I$ and $ab \in J$. An element of $(I \cap J) + (I \cap K)$ lies in $I$ and in $J + K$. $\square$

### The Radical of an Ideal

**Definition.** For an ideal $I$ of $R$ the **radical** of $I$ is $\sqrt{I} = \{r \in R : r^n \in I \text{ for some } n \geq 1\}$. An ideal with $I = \sqrt{I}$ is a **radical ideal**; the radical of the zero ideal is the **nilradical**, developed in *Reduced Rings and the Nilradical*, below this article in this category.

**Proposition.** Let $I, J$ be ideals of the commutative ring $R$.

**(a)** $\sqrt{I}$ is an ideal with $I \subseteq \sqrt{I} \subseteq R$.

**(b)** $\sqrt{I} = R$ if and only if $I = R$.

**(c)** $\sqrt{\sqrt{I}} = \sqrt{I}$ and $\sqrt{I^n} = \sqrt{I}$ for every $n \geq 1$.

**(d)** $\sqrt{I \cap J} = \sqrt{I} \cap \sqrt{J} = \sqrt{IJ}$.

**Proof.** (a) If $a^m \in I$ and $b^n \in I$, then every term of the binomial expansion of $(a+b)^{m+n-1}$ contains $a^i b^{m+n-1-i}$ with $i \geq m$ or $m+n-1-i \geq n$, so $(a+b)^{m+n-1} \in I$; this is where the binomial theorem and hence commutativity enter, since $a$ and $b$ must be interchangeable in the expansion. If $a^m \in I$ and $r \in R$ then $(ra)^m = r^m a^m \in I$.

(b) $I = R$ gives $1 \in \sqrt{I}$; and $1 = 1^n \in I$ if $1 \in \sqrt{I}$.

(c) $r$ has a power in $I$ exactly when a power of $r$ has a power in $I$. And $I^2 \subseteq I$ gives $\sqrt{I^2} \subseteq \sqrt{I}$, while $r^n \in I$ gives $r^{2n} \in I^2$; induct.

(d) From $IJ \subseteq I \cap J$ we get $\sqrt{IJ} \subseteq \sqrt{I \cap J}$, and $\sqrt{I \cap J} \subseteq \sqrt{I} \cap \sqrt{J}$ is immediate. Finally if $r^m \in I$ and $r^n \in J$ then $r^{m+n} \in IJ$. $\square$

**Proposition.** The radical of $I$ is the inverse image of the nilradical of the quotient under $\pi : R \to R/I$, that is $\sqrt{I} = \pi^{-1}(\operatorname{nil}(R/I))$.

**Proof.** The class $r + I$ is nilpotent exactly when $r^n \in I$ for some $n \geq 1$. $\square$

**Corollary.** An ideal is radical exactly when its quotient is reduced, in the sense of *Reduced Rings and the Nilradical*, below this article in this category.

**Lemma (prime ideals from multiplicative sets).** Let $S \subseteq R$ be multiplicatively closed with $1 \in S$ and $0 \notin S$, and let $J$ be an ideal maximal among the ideals disjoint from $S$. Then $J$ is prime.

**Proof.** Suppose $ab \in J$ with $a, b \notin J$. Then $J + (a)$ and $J + (b)$ strictly contain $J$, so by maximality each meets $S$; choose $s = j + xa$ and $t = k + yb$ with $j, k \in J$. Then $st = (j+xa)(k+yb) \in J + (ab) = J$, since $ab \in J$, while $st \in S$ because $S$ is multiplicatively closed and $s, t \in S$. This contradicts $J \cap S = \emptyset$. $\square$

The ideal $J$ exists by Zorn's lemma applied to the set of ideals disjoint from $S$, which is nonempty because $(0)$ is disjoint from $S$ when $0 \notin S$.

**Theorem (Krull).** Let $I$ be an ideal of the commutative ring $R$. Then the radical of $I$ is the intersection of the prime ideals containing $I$:

$$
\sqrt{I} = \bigcap_{\mathfrak{p} \supseteq I} \mathfrak{p} .
$$

In particular the nilradical is the intersection of all the prime ideals, $\operatorname{nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec} R} \mathfrak{p}$.

**Proof.** If $r \in \sqrt{I}$ and $\mathfrak{p} \supseteq I$, then $r^n \in I \subseteq \mathfrak{p}$ for some $n \geq 1$, so $r \in \mathfrak{p}$ since $\mathfrak{p}$ is prime; this is one inclusion. For the other, $\sqrt{I}$ is the preimage of the nilradical of $R/I$ by the proposition above, so it suffices to show that a non-nilpotent element $s$ of $R$ lies outside some prime ideal. The set $S = \{s^n : n \geq 0\}$ is multiplicatively closed, contains $1$ and not $0$; by the lemma there is an ideal $\mathfrak{p}$ maximal among those disjoint from $S$, hence prime, and $s \notin \mathfrak{p}$. $\square$

The intersection of radical ideals is radical, by (d) and its analogue for an arbitrary family; the sum of two radical ideals need not be radical.

**Example.** In $\mathbb{Z}$ the radical of $(12)$ is $(6) = (2) \cap (3)$: the radical keeps each prime divisor with multiplicity one. In a principal ideal domain $\sqrt{(a)}$ is generated by the product of the distinct primes dividing $a$.

---

## Coprime Ideals and the Chinese Remainder Theorem

**Definition.** Ideals $I, J$ of $R$ are **coprime**, or **comaximal**, if $I + J = R$.

**Proposition.** Let $I, J, K$ be ideals of the commutative ring $R$.

**(a)** $I$ and $J$ are coprime if and only if $a + b = 1$ for some $a \in I$, $b \in J$.

**(b)** If $I$ and $J$ are coprime then $IJ = I \cap J$.

**(c)** If $I$ is coprime to $J$ and to $K$ then $I$ is coprime to $JK$; hence to $J^n$ for every $n \geq 1$.

**Proof.** (a) $I+J = R$ means $1 \in I+J$. (b) If $1 = a+b$ with $a \in I$, $b \in J$ and $x \in I \cap J$, then $x = xa + xb \in IJ$ since $xa \in IJ$ (as $x \in J$, $a \in I$) and $xb \in IJ$ (as $x \in I$, $b \in J$). (c) From $a+b=1$ with $a\in I$, $b\in J$ and $a'+c=1$ with $a'\in I$, $c\in K$ we get $1 = (a+b)(a'+c) = aa' + ac + ba' + bc \in I + JK$; iterate. $\square$

**Theorem (Chinese remainder theorem).** Let $I_1, \ldots, I_n$ be pairwise coprime ideals of the commutative ring $R$. Then

$$
\varphi : R \to R/I_1 \times \cdots \times R/I_n, \qquad \varphi(r) = (r+I_1, \ldots, r+I_n),
$$

is a surjective ring homomorphism with kernel $I_1 \cap \cdots \cap I_n = I_1 I_2 \cdots I_n$, so that

$$
R/(I_1 I_2 \cdots I_n) \cong R/I_1 \times R/I_2 \times \cdots \times R/I_n .
$$

**Proof.** $\varphi$ is a homomorphism with kernel the intersection. For $n=2$, choose $a_1 \in I_1$, $a_2 \in I_2$ with $a_1 + a_2 = 1$; then $a_2 \equiv 1 \pmod{I_1}$, $a_2 \equiv 0 \pmod{I_2}$, and dually for $a_1$, so $x_1 a_2 + x_2 a_1$ maps to $(x_1 + I_1, x_2 + I_2)$. Iterate for $n \geq 3$, using that a product of ideals coprime to a given ideal is coprime to it. The intersection equals the product by the proposition, iterated. $\square$

**Corollary.** For $n = p_1^{e_1} \cdots p_r^{e_r}$ a factorisation into prime powers, $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}/p_1^{e_1}\mathbb{Z} \times \cdots \times \mathbb{Z}/p_r^{e_r}\mathbb{Z}$.

**Example.** $\mathbb{Z}/12\mathbb{Z} \cong \mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$; the idempotent corresponding to $(1,0)$ is the class of $9$, and that corresponding to $(0,1)$ is the class of $4$.

---

## Prime and Maximal Ideals

### Definitions and Quotient Characterisations

**Definition.** A proper ideal $\mathfrak{p} \subsetneq R$ is **prime** if $ab \in \mathfrak{p}$ implies $a \in \mathfrak{p}$ or $b \in \mathfrak{p}$. A proper ideal $\mathfrak{m} \subsetneq R$ is **maximal** if there is no ideal $I$ with $\mathfrak{m} \subsetneq I \subsetneq R$.

**Theorem (quotient characterisations).** Let $I$ be a proper ideal of the commutative ring $R$.

**(a)** $I$ is prime if and only if $R/I$ has no zero divisors.

**(b)** $I$ is maximal if and only if $R/I$ has no proper nonzero ideal.

**Proof.** (a) $a + I$ is a zero divisor in $R/I$ exactly when there is $b \notin I$ with $ab \in I$ and $a \notin I$; this is the negation of primeness.

(b) The ideals of $R/I$ correspond to the ideals of $R$ containing $I$, preserving inclusion, by the correspondence theorem of *Rings*, §Quotient Rings. $\square$

**Corollary.** Let $R$ be a commutative ring with $1 \neq 0$.

**(a)** $\mathfrak{p}$ is prime if and only if $R/\mathfrak{p}$ is an integral domain, in the sense of *Integral Domains*, below this article in this category.

**(b)** $\mathfrak{m}$ is maximal if and only if $R/\mathfrak{m}$ is a field, in the sense of *Fields*, later in this category.

The two notions are distinguished by what the quotient is asked to satisfy: the first asks that there be no zero divisors, the second that every nonzero class be a unit.

**Proposition.** Every maximal ideal is prime; and if $\mathfrak{m}$ is maximal then the only ideals containing $\mathfrak{m}$ are $\mathfrak{m}$ and $R$.

**Proof.** Let $\mathfrak{m}$ be maximal. By the correspondence theorem of *Rings*, §Quotient Rings the ideals of $R/\mathfrak{m}$ correspond to the ideals of $R$ containing $\mathfrak{m}$, so the only ideals of $R/\mathfrak{m}$ are $(0)$ and $R/\mathfrak{m}$. Hence for $a \notin \mathfrak{m}$ the ideal $(a + \mathfrak{m})$ of $R/\mathfrak{m}$ is nonzero, therefore all of $R/\mathfrak{m}$, and there is $x \in R$ with $xa \equiv 1 \pmod{\mathfrak{m}}$; so every nonzero class of $R/\mathfrak{m}$ is a unit. A unit is not a zero divisor, since $uv = 0$ gives $v = u^{-1}uv = 0$, so $R/\mathfrak{m}$ has no zero divisors and $\mathfrak{m}$ is prime by the theorem above. The second statement is the definition read through the correspondence theorem. $\square$

**Theorem (existence of maximal ideals).** Let $I \subsetneq R$ be a proper ideal of the commutative ring $R$. Then $I$ is contained in a maximal ideal.

**Proof.** Let $\Sigma$ be the set of proper ideals containing $I$, ordered by inclusion. It is nonempty, and the union of a chain in $\Sigma$ is a proper ideal containing $I$, since $1$ lies in no member of the chain. By Zorn's lemma, of *Cardinality and the Axiom of Choice*, $\Sigma$ has a maximal element. $\square$

This is the first use of a choice principle in the category, and it cannot be removed: over the remaining axioms of set theory, the statement that every nonzero commutative ring has a maximal ideal is equivalent to the theorem on prime ideals in Boolean algebras, a choice principle strictly weaker than the axiom of choice.

### Primality and Maximality Compared

**Proposition.** Let $\mathfrak{p}$ be a prime ideal of $R$ and $S = R \setminus \mathfrak{p}$.

**(a)** $S$ is multiplicatively closed and contains $1$.

**(b)** $\mathfrak{p}$ is maximal among the ideals disjoint from $S$.

**Proof.** (a) If $s, t \notin \mathfrak{p}$ but $st \in \mathfrak{p}$ then primeness puts $s$ or $t$ in $\mathfrak{p}$; so $st \notin \mathfrak{p}$. And $1 \notin \mathfrak{p}$.

(b) An ideal disjoint from $S$ is contained in $\mathfrak{p}$ by the definition of $S$, so $\mathfrak{p}$ is the largest such ideal. $\square$

**Remark.** The set $S = R \setminus \mathfrak{p}$ is precisely the set inverted in the localization of $R$ at $\mathfrak{p}$; localization is the subject of *Localization and the Fraction Field*, below this article in this category.

---

## The Prime Spectrum

**Definition.** The **prime spectrum** of $R$ is the set $\operatorname{Spec} R = \{\mathfrak{p} \subsetneq R : \mathfrak{p} \text{ prime}\}$ partially ordered by inclusion. Its maximal elements are the maximal ideals and its minimal elements are the **minimal primes**.

**Proposition.** Let $I$ be an ideal of the commutative ring $R$.

**(a)** $\{\mathfrak{p} \in \operatorname{Spec} R : I \subseteq \mathfrak{p}\}$ is order-isomorphic to $\operatorname{Spec}(R/I)$ by $\mathfrak{p} \mapsto \mathfrak{p}/I$.

**(b)** $(0)$ is a prime ideal exactly when $R$ is an integral domain, and then it is the least element of $\operatorname{Spec} R$; for every nonzero $R$, $\operatorname{Spec} R$ is nonempty, and it may have a least element that is not $(0)$, as $R = k[x]/(x^2)$ with the single prime $(x)$ shows.

**(c)** The maximal elements of $\operatorname{Spec} R$ are exactly the maximal ideals, and every prime lies below one.

**Proof.** (a) Ideals of $R/I$ correspond to ideals of $R$ containing $I$, and the correspondence carries primes to primes by the quotient characterisation.

(b) $(0)$ is prime exactly when $ab = 0$ forces $a = 0$ or $b = 0$, that is exactly when $R$ has no zero divisors; and if $(0)$ is prime it is contained in every prime, so it is least. A nonzero ring has a maximal ideal by the existence theorem, and that ideal is prime by the proposition above; and in $k[x]/(x^2)$ the nilpotent class $x$ lies in every prime, so $(x)$ is the only prime and is least.

(c) A maximal element of the poset lies in no other proper ideal; the rest is the existence theorem. $\square$

**Definition.** The **Krull dimension** $\dim R$ of $R$ is the supremum of the lengths $n$ of chains $\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ in $\operatorname{Spec} R$, equal to $\infty$ when the lengths are unbounded. It is developed in *Integral Extensions and Krull Dimension*, below this article in this category.

**Example.** $\operatorname{Spec} \mathbb{Z} = \{(0)\} \cup \{(p) : p \text{ prime}\}$ with $(0)$ below every $(p)$ and the $(p)$ pairwise incomparable, so $\dim \mathbb{Z} = 1$. For a field $F$, $\operatorname{Spec} F$ is the single point $(0)$, of dimension $0$.

**Proposition.** A ring homomorphism $\varphi : R \to S$ and a prime $\mathfrak{q} \subseteq S$ give a prime $\varphi^{-1}(\mathfrak{q}) \subseteq R$, and the map $\varphi^{*}(\mathfrak{q}) = \varphi^{-1}(\mathfrak{q})$ is order-preserving, so that $\operatorname{Spec}$ is a contravariant functor to posets.

**Proof.** The preimage of an ideal is an ideal, and if $ab \in \varphi^{-1}(\mathfrak{q})$ then $\varphi(a)\varphi(b) \in \mathfrak{q}$, so $a$ or $b$ lies in $\varphi^{-1}(\mathfrak{q})$. Inclusion is preserved under preimage. $\square$

The **Zariski topology** on $\operatorname{Spec} R$, its structure sheaf and the schemes they define belong to Part II and to *Schemes*; here only the order structure is used.

---

## Where Commutativity Is Used

Each statement below fails in a general ring; the non-commutative chain of this category, later in this category, rebuilds the corresponding theory without the commutative hypothesis.

**A. The binomial theorem.** For non-commuting $a, b$ the expansion acquires correction terms. In the upper triangular $2 \times 2$ matrices over a field, with $a = e_{11}$, $b = e_{12}$, one has $ab = b$ and $ba = 0$, so $(a+b)^2 = a + b$ whereas $a^2 + 2ab + b^2 = a + 2b$.

**B. Multiplication of ideals.** Ideals must be distinguished as left, right or two-sided, a one-sided ideal does not support a quotient ring, and $IJ$ and $JI$ can differ; the quotient $R/I$ exists only for two-sided $I$.

**C. Maximal ideals.** For a maximal two-sided ideal the quotient has no proper nonzero two-sided ideal, so it is a **simple** ring and not a field; $M_n(k)$ is simple for $n \geq 2$.

**D. Prime ideals.** The elementwise condition defines a **completely prime** ideal, which is not the right notion in general; the two-sided definition replaces elements by ideals, and the theory is built in *Semiprime Rings* and *Prime Rings*, later in this category.

**E. The prime spectrum.** The spectrum $\operatorname{Spec} R$ is a poset because primes are the kernels of the homomorphisms from $R$ to integral domains, and it is the elementwise condition that makes the quotient $R/\mathfrak{p}$ a domain; in the non-commutative chain below the set of prime ideals is still written $\operatorname{Spec} A$ in *Prime Rings*, but a prime quotient there is a prime ring and has zero divisors in general, and no geometric structure on the set is used.

**F. Fractions and localization.** The fraction field inverts the nonzero elements of a domain and uses the symmetry of $rs' = r's$; the non-commutative analogue needs the Ore condition and is treated in *Ore Domains and Division Rings of Fractions*, later in this category.

---

## Summary

Commutativity makes the order of factors irrelevant, powers unambiguous, and the binomial and multinomial expansions valid. For ideals it makes the product generated by the products of generators, distributive over sums and independent of the order of the factors. The radical $\sqrt{I}$ is the set of elements some power of which lies in $I$; it is an ideal, idempotent as an operation, multiplicative on intersections and products, and the preimage of the nilradical of $R/I$; by Krull's theorem it is the intersection of the prime ideals containing $I$, so that the nilradical is the intersection of all the prime ideals. Coprime ideals satisfy $IJ = I \cap J$, and the Chinese remainder theorem decomposes $R/(I_1 \cdots I_n)$ as the product of the quotients, which gives the prime power decomposition of $\mathbb{Z}/n\mathbb{Z}$.

An ideal is prime when $ab \in \mathfrak{p}$ forces a factor into it, equivalently when $R/\mathfrak{p}$ has no zero divisors, and maximal when maximal under inclusion, equivalently when $R/\mathfrak{m}$ has no proper nonzero ideal. Every maximal ideal is prime, every proper ideal lies in a maximal one by Zorn's lemma, and the primes form the poset $\operatorname{Spec} R$, order-isomorphic to the primes containing $I$ when one passes to $R/I$. Each statement has a recorded failure without commutativity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $\binom{n}{k}$ | Binomial coefficient $n!/(k!(n-k)!)$ |
| $a^n$ | Product of $n$ copies of $a$ |
| $I + J$ | Sum of ideals, $\{a+b : a \in I,\ b \in J\}$ |
| $IJ$ | Product of ideals, the finite sums of products |
| $I \cap J$ | Intersection of ideals |
| $(A)$ | Ideal generated by a subset $A \subseteq R$ |
| $\sqrt{I}$ | Radical of $I$, $\{r : r^n \in I \text{ for some } n \geq 1\}$ |
| $\operatorname{nil}(R)$ | Nilradical $\sqrt{(0)}$; *Reduced Rings and the Nilradical* |
| $I + J = R$ | Coprime (comaximal) ideals |
| $\mathfrak{p}$ | Prime ideal |
| $\mathfrak{m}$ | Maximal ideal |
| $\operatorname{Spec} R$ | Prime spectrum, the poset of primes under inclusion |
| $\dim R$ | Krull dimension; *Integral Extensions and Krull Dimension* |
| $\operatorname{char} R$ | Characteristic of $R$ |
| $\varphi^{*}(\mathfrak{q})$ | Contraction $\varphi^{-1}(\mathfrak{q})$ of a prime along a ring homomorphism |

## Further Reading

- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the arithmetic of ideals, the Chinese remainder theorem and the prime spectrum.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for the binomial identities, the radical of an ideal and the ordering of the spectrum.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for prime and maximal ideals, the existence theorem and the radical.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the binomial and multinomial theorems and the elementary ideal theory.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989), for the quotient characterisations, the spectrum and the Krull dimension.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume 1 (Van Nostrand, 1958), for the geometric reading of the prime spectrum.
