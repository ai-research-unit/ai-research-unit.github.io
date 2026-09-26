
# __Reduced Rings and the Nilradical__

## Introduction

A nilpotent is an element some power of which is zero, and a ring is **reduced** when the only nilpotent it contains is $0$. Reducedness is the third rung of the ring hierarchy of this category: it is weaker than being a domain, since a product of fields has no nonzero nilpotent but has zero divisors, and it is stronger than being an arbitrary commutative ring, since $\mathbb{Z}/4\mathbb{Z}$ has the nonzero nilpotent $2$. The single invariant that governs the rung is the **nilradical** $\operatorname{nil}(R)$, the set of nilpotent elements, which is an ideal and which vanishes precisely when $R$ is reduced.

Nilpotents and the nilradical are introduced as vocabulary in *Rings*, §The Multiplicative Vocabulary, and prime ideals in *Rings*, §Prime and Maximal Ideals; the present article takes those notions and develops the structure they carry. The theorem that the nilradical is the intersection of the prime ideals, and more generally that the radical of an ideal is the intersection of the prime ideals containing it, is Krull's theorem, proved in *Commutative Rings*, directly above this article. Throughout, $R$ is a commutative ring with identity $1 \neq 0$, the corpus default; nilpotents behave badly without commutativity, and the non-commutative analogue of this rung, the semiprime ring, is *Semiprime Rings*, later in this category.

---

## Nilpotents as a Class

### The Ideal of Nilpotents

An element $x \in R$ is **nilpotent** if $x^n = 0$ for some $n \geq 1$, and the set of nilpotent elements is the **nilradical** $\operatorname{nil}(R)$; both notions are those of *Rings*, §The Multiplicative Vocabulary, where $0$ is counted as nilpotent. The first point of the theory is that the class is closed under addition, and this is exactly where commutativity is used.

**Proposition.** Let $x, y \in R$ be nilpotent, with $x^m = 0$ and $y^n = 0$. Then $x + y$ and $xy$ are nilpotent, so $\operatorname{nil}(R)$ is an ideal.

**Proof.** Every term of the binomial expansion of $(x+y)^{m+n-1}$ is a multiple of $x^i y^{m+n-1-i}$; if $i \geq m$ the term vanishes, and otherwise $m+n-1-i \geq n$, so the term vanishes too. Hence $(x+y)^{m+n-1} = 0$. The binomial theorem of *Commutative Rings* is used here, so the argument needs $x$ and $y$ to commute; in a non-commutative ring the sum of two nilpotents need not be nilpotent, which is why the non-commutative rung below is defined by ideals rather than by elements. For the product, $(xy)^m = x^m y^m = 0$, and if $r \in R$ then $(rx)^m = r^m x^m = 0$; so $\operatorname{nil}(R)$ is closed under addition and under multiplication by $R$. $\square$

**Remark.** $\operatorname{nil}(R)$ is the radical of the zero ideal, $\operatorname{nil}(R) = \sqrt{(0)}$, by the definition of the radical in *Commutative Rings*: an element has a power equal to $0$ exactly when it lies in $\sqrt{(0)}$.

**Example.** $\operatorname{nil}(\mathbb{Z}/12\mathbb{Z}) = (6) = \{0, 6\}$, since $6^2 = 36 \equiv 0$ and no other class of $\mathbb{Z}/12\mathbb{Z}$ is nilpotent other than $0$. $\operatorname{nil}(\mathbb{Z}/4\mathbb{Z}) = (2) = \{0,2\}$. For the ring of dual numbers, $\operatorname{nil}(k[\varepsilon]/(\varepsilon^2)) = (\varepsilon)$, and the square of this ideal is zero.

**Example.** A nonzero nilpotent is a zero divisor: if $x^n = 0$ with $n$ the least such exponent, then $x \cdot x^{n-1} = 0$ with $x^{n-1} \neq 0$ and $x \neq 0$. The converse fails: in $\mathbb{Z}/6\mathbb{Z}$ the class of $2$ is a zero divisor, since $2 \cdot 3 = 0$, but it is not nilpotent, since $2^k$ is $2$ or $4$ for every $k \geq 1$.

### Nilpotents and Units

Nilpotent elements do not change the unit group, and this is the technical reason the nilradical is invisible to much of the arithmetic.

**Proposition.** Let $u \in R$ be a unit and let $x \in R$ be nilpotent. Then $u + x$ is a unit. In particular, if $x^n = 0$ then $1 - x$ is a unit with

$$
(1-x)^{-1} = 1 + x + x^2 + \cdots + x^{n-1} .
$$

**Proof.** The displayed identity follows from $(1-x)(1 + x + \cdots + x^{n-1}) = 1 - x^n = 1$; the sum is finite and so needs no convergence. In general $u + x = u\,(1 + u^{-1}x)$, and $u^{-1}x$ is nilpotent since $(u^{-1}x)^n = u^{-n}x^n$. $\square$

**Corollary.** Let $\pi : R \to R/\operatorname{nil}(R)$ be the quotient map. Then an element $u \in R$ is a unit if and only if $\pi(u)$ is a unit. In particular $\pi$ induces a surjection $R^{\times} \to (R/\operatorname{nil}(R))^{\times}$.

**Proof.** A homomorphism carries units to units. Conversely if $\pi(u) = u + \operatorname{nil}(R)$ is a unit, choose $v + \operatorname{nil}(R)$ with $uv + \operatorname{nil}(R) = 1 + \operatorname{nil}(R)$; then $uv = 1 - x$ for some nilpotent $x$, so $uv$ is a unit by the proposition, and therefore so is $u$. $\square$

**Example.** In $\mathbb{Z}/4\mathbb{Z}$, with nilradical $(2)$, the class of $1 + 2 = 3$ is a unit because the class of $1$ is; indeed $3 \cdot 3 = 9 \equiv 1$. The four elements of $k[x]/(x^2)$ of the form $a + bx$ with $a \neq 0$ are units, by the proposition applied to $a(1 + a^{-1}bx)$.

### Nilpotents and Idempotents

Nilpotents and idempotents are at opposite ends of the spectrum of a ring: a nilpotent is absorbed by every power of itself, while an idempotent is fixed by every power.

**Proposition.** Let $e \in R$ be idempotent, $e^2 = e$.

**(a)** $1 - e$ is idempotent, and $e(1-e) = 0$.

**(b)** $e$ is a unit if and only if $e = 1$.

**(c)** The only nilpotent idempotent is $0$.

**Proof.** (a) $(1-e)^2 = 1 - 2e + e^2 = 1 - 2e + e = 1 - e$, and $e(1-e) = e - e^2 = 0$. (b) If $e$ is a unit then $e = e^2$ gives $1 = e^{-1}e = e^{-1}e^2 = e$ after multiplying by $e^{-1}$; the converse is clear. (c) If $e^2 = e$ and $e^n = 0$ with $n \geq 1$, then $e = e^n = 0$. $\square$

Idempotents are the vocabulary of *Rings*, §The Multiplicative Vocabulary, and their use in product decompositions belongs to *Localization and the Fraction Field*, below this article in this category.

---

## Reduced Rings

### Definition and First Properties

**Definition.** A commutative ring $R$ is **reduced** if $\operatorname{nil}(R) = (0)$, that is, if the only nilpotent element of $R$ is $0$.

**Proposition.** For a commutative ring $R$ the following are equivalent.

**(a)** $R$ is reduced.

**(b)** $R$ has no nonzero nilpotent element.

**(c)** $\operatorname{nil}(R) = (0)$.

**(d)** $\bigcap_{\mathfrak{p} \in \operatorname{Spec} R} \mathfrak{p} = (0)$.

**Proof.** (a), (b) and (c) restate one another, since $\operatorname{nil}(R)$ is by definition the set of nilpotent elements. The equivalence with (d) is Krull's theorem of *Commutative Rings*, which identifies $\operatorname{nil}(R)$ with the intersection of the prime ideals. $\square$

**Proposition.** Let $I$ be an ideal of $R$. Then $R/I$ is reduced if and only if $I = \sqrt{I}$, that is, if and only if $I$ is a radical ideal.

**Proof.** By *Commutative Rings*, the radical of $I$ is the preimage of $\operatorname{nil}(R/I)$ under the quotient map; hence $\operatorname{nil}(R/I) = (0)$ exactly when $\sqrt{I} = I$. $\square$

So the reduced quotients of $R$ are precisely its quotients by radical ideals, and every ring has a largest reduced quotient.

**Definition.** The **reduced quotient** of $R$ is $R_{\mathrm{red}} = R/\operatorname{nil}(R)$.

**Proposition.** $R_{\mathrm{red}}$ is reduced, and if $I$ is any ideal with $R/I$ reduced then $\operatorname{nil}(R) \subseteq I$, so $R_{\mathrm{red}}$ is the largest reduced quotient of $R$.

**Proof.** That $R_{\mathrm{red}}$ is reduced follows from the criterion above applied to the radical ideal $\operatorname{nil}(R) = \sqrt{(0)}$. If $R/I$ is reduced and $x \in R$ is nilpotent with $x^n = 0$, then the class of $x$ in $R/I$ is nilpotent and hence zero, so $x \in I$; thus $\operatorname{nil}(R) \subseteq I$. $\square$

**Proposition.** A subring of a reduced ring is reduced, and a product $\prod_{i \in \Lambda} R_i$ of nonzero commutative rings is reduced if and only if every $R_i$ is reduced.

**Proof.** A nilpotent in a subring is a nilpotent in the ring; and an element of the product is nilpotent exactly when each of its components is nilpotent, since the components of a power are the powers of the components. $\square$

**Example (reduced rings).** $\mathbb{Z}$ is reduced, since $a^n = 0$ forces $a = 0$ in $\mathbb{Z}$. Every field is reduced, since a field has no zero divisors and a nonzero element cannot have a zero power; fields are introduced in *Fields*, later in this category. The polynomial ring $k[x]$ over a field is reduced, since $k[x]$ is an integral domain. The product $\mathbb{Z} \times \mathbb{Z}$ is reduced, by the proposition above, and so is $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$.

**Example (non-reduced rings).** $\mathbb{Z}/4\mathbb{Z}$ is not reduced, since the class of $2$ is nonzero and squares to zero. The ring $k[\varepsilon]/(\varepsilon^2)$ of dual numbers is not reduced, its nilradical being the ideal $(\varepsilon)$. For $n = p_1^{e_1} \cdots p_r^{e_r}$ the ring $\mathbb{Z}/n\mathbb{Z}$ is reduced exactly when every $e_i = 1$, that is, when $n$ is squarefree; indeed $\operatorname{nil}(\mathbb{Z}/n\mathbb{Z})$ is generated by the product of the distinct primes dividing $n$.

### The Counterexamples That Fix the Rung

Two rings show that reducedness is a rung strictly between the general commutative ring and the domain.

**Example ($\mathbb{Z}/4\mathbb{Z}$: not reduced).** In $\mathbb{Z}/4\mathbb{Z}$ the element $2$ is nonzero and $2^2 = 0$; the nilradical is $(2)$, the unique prime ideal, and the reduced quotient is $\mathbb{Z}/2\mathbb{Z}$. So "commutative ring with $1 \neq 0$" does not imply "reduced".

**Example ($\mathbb{Z} \times \mathbb{Z}$: reduced but not a domain).** The nilradical of $\mathbb{Z} \times \mathbb{Z}$ is $(0) \times (0)$, so the ring is reduced, but $(1,0)(0,1) = (0,0)$ with both factors nonzero, so it has zero divisors. The same is true of $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$. Hence "reduced" does not imply "domain".

The rings $\mathbb{Z} \times \mathbb{Z}$ and $\mathbb{Z}/6\mathbb{Z}$ are products of reduced rings and are reduced; they are the standard witnesses that reducedness is the product-closed property one obtains when the no-zero-divisors condition is weakened to the vanishing of the nilradical. The domain is the case in which the intersection of the prime ideals is zero and the primes form a single minimal element; an integral domain is a reduced ring with $(0)$ prime, the definition belonging to *Integral Domains*, below this article in this category.

---

## The Nilradical

### Krull's Theorem

The nilradical is characterised by the prime ideals, and this is the structural statement that makes reducedness checkable.

**Theorem (Krull).** Let $R$ be a commutative ring with $1 \neq 0$. Then

$$
\operatorname{nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec} R} \mathfrak{p} = \sqrt{(0)} .
$$

**Proof.** This is the case $I = (0)$ of Krull's theorem in *Commutative Rings*, where the radical of an ideal is identified with the intersection of the prime ideals containing it; the second identity is the definition of the nilradical as the radical of the zero ideal. $\square$

**Corollary.** $R$ is reduced if and only if the intersection of its prime ideals is zero. Every ring has a reduced ring as a quotient, namely $R/\operatorname{nil}(R)$, and $R/\operatorname{nil}(R)$ embeds injectively into a product of integral domains.

The last statement is made precise in the next section.

**Corollary.** If $R$ is reduced then the intersection of all its minimal primes is $(0)$; in particular a reduced ring has no nonzero element lying in every minimal prime. A reduced ring may have infinitely many minimal primes, as an infinite product of fields shows.

**Proof.** Every prime contains a minimal prime, so the intersection over all primes equals the intersection over the minimal ones; the statement is then Krull's theorem. $\square$

### The Nilradical as the Radical of the Zero Ideal

The identity $\operatorname{nil}(R) = \sqrt{(0)}$ places the nilradical in the lattice of radical ideals.

**Proposition.** Let $I$ be an ideal of $R$.

**(a)** $I \subseteq \operatorname{nil}(R)$ if and only if every element of $I$ is nilpotent.

**(b)** $\operatorname{nil}(R/I) = \sqrt{I}/I$.

**(c)** $\operatorname{nil}(R) = R$ if and only if $R$ is the zero ring, which is excluded.

**Proof.** (a) is the definition. (b) is the identification of $\sqrt{I}$ with the preimage of $\operatorname{nil}(R/I)$. (c) If $1$ is nilpotent then $1 = 1^n = 0$. $\square$

**Proposition (nilpotent ideals).** An ideal $I$ with $I^n = (0)$ for some $n \geq 1$ satisfies $I \subseteq \operatorname{nil}(R)$. The converse fails: the nilradical of a ring need not be nilpotent as an ideal.

**Proof.** If $x \in I$ then $x^n \in I^n = (0)$, so $x$ is nilpotent. For the failure, let $R = k[x_1, x_2, x_3, \ldots]/(x_1^2, x_2^3, x_3^4, \ldots)$, a quotient of the polynomial ring in countably many indeterminates, and let $I = (x_1, x_2, x_3, \ldots)$. An element of $I$ is a finite sum of monomials of positive degree, and a monomial $\prod_i x_i^{a_i}$ has vanishing $N$-th power as soon as $N a_i \geq i+1$ for some $i$ with $a_i \geq 1$, so each monomial is nilpotent and the finite sum of them is too, by the proposition above; hence $I \subseteq \operatorname{nil}(R)$. But $I^n \neq (0)$ for every $n$, since the class of $x_{n+1}$ is nonzero and $x_{n+1}^n \neq 0$ while $x_{n+1}^{n+2} = 0$. Hence $\operatorname{nil}(R) = I$ is not nilpotent. $\square$

Whether the nilradical is nilpotent is governed by a finiteness condition: in a Noetherian ring the nilradical is nilpotent, and the general criterion belongs to *Noetherian and Artinian Rings*, below this article in this category.

**Remark.** The nilradical is a proper ideal of every ring with $1 \neq 0$, by (c) above, and it is contained in every prime ideal, so in particular in every maximal ideal.

---

## Reduced Rings as Subrings of Products of Domains

### The Canonical Embedding

The prime ideals of $R$ can be used to separate the elements of $R$ from one another, and reducedness says exactly that the separation is complete.

**Theorem.** Let $R$ be a commutative ring with $1 \neq 0$. The map

$$
R \longrightarrow \prod_{\mathfrak{p} \in \operatorname{Spec} R} R/\mathfrak{p}, \qquad r \mapsto (r + \mathfrak{p})_{\mathfrak{p}},
$$

is a ring homomorphism whose kernel is $\operatorname{nil}(R)$. Consequently $R$ is reduced if and only if this map is injective.

**Proof.** The map is the product of the quotient maps $R \to R/\mathfrak{p}$, so it is a homomorphism, and an element lies in its kernel exactly when it lies in every prime, that is, when it lies in $\bigcap_{\mathfrak{p}} \mathfrak{p} = \operatorname{nil}(R)$ by Krull's theorem. $\square$

**Corollary.** $R$ is reduced if and only if $R$ is isomorphic to a subring of a product of integral domains.

**Proof.** If $R$ is reduced, the theorem embeds it into the product of the quotients $R/\mathfrak{p}$, and each $R/\mathfrak{p}$ is an integral domain, in the sense of *Integral Domains*, below this article in this category. Conversely a subring of a product of domains is reduced, because a product of reduced rings is reduced and a subring of a reduced ring is reduced. $\square$

**Example.** For $R = \mathbb{Z}$ the primes are $(0)$ and the $(p)$, and the embedding is the familiar one into $\mathbb{Q} \times \prod_p \mathbb{F}_p$, whose kernel is zero. For $R = \mathbb{Z}/6\mathbb{Z}$ the primes are $(2)$ and $(3)$, and the embedding is the Chinese remainder isomorphism $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$. For $R = \mathbb{Z}/4\mathbb{Z}$ the only prime is $(2)$, and the map to $\mathbb{Z}/2\mathbb{Z}$ has kernel $(2) = \operatorname{nil}(R) \neq (0)$, so it is not injective.

### Subdirect Products

**Definition.** A ring $R$ is a **subdirect product** of a family of rings $(R_i)_{i \in \Lambda}$ if $R$ is a subring of $\prod_i R_i$ whose image under each coordinate projection $\prod_i R_i \to R_i$ is all of $R_i$.

**Theorem.** A commutative ring $R$ with $1 \neq 0$ is reduced if and only if it is a subdirect product of integral domains. If $R$ is reduced, $R$ is a subdirect product of the domains $R/\mathfrak{p}$ with $\mathfrak{p} \in \operatorname{Spec} R$.

**Proof.** For the forward direction, the embedding of the previous theorem has image meeting each coordinate surjectively, by construction; so the image realises $R$ as a subdirect product of the domains $R/\mathfrak{p}$. Conversely a subring of a product of domains is reduced, since each domain is reduced and the product and subring operations preserve reducedness. $\square$

**Corollary.** A finite reduced commutative ring is a product of finitely many finite fields.

**Proof.** Such a ring has finitely many maximal ideals, by the finiteness of its underlying set, and every prime ideal is maximal, since in a finite ring every integral domain is a field; the Chinese remainder theorem applied to the pairwise coprime maximal ideals exhibits the ring as a product of the quotients, each a field. The structure theory of rings with finitely many maximal ideals is *Noetherian and Artinian Rings*, below this article in this category. $\square$

**Example.** $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{F}_2 \times \mathbb{F}_3$ and $\mathbb{F}_2 \times \mathbb{F}_2$ is a reduced ring of characteristic two with four elements and two maximal ideals; both are subdirect products of their residue fields.

---

## Summary

The nilpotent elements of a commutative ring form an ideal, the nilradical $\operatorname{nil}(R) = \sqrt{(0)}$, because the binomial theorem makes the sum of two nilpotents nilpotent; without commutativity this closure fails and the non-commutative rung is defined by ideals instead. Nilpotents do not affect the unit group: $u + x$ is a unit whenever $u$ is a unit and $x$ is nilpotent, and an element is a unit if and only if its class modulo the nilradical is. A ring is reduced when its nilradical vanishes, equivalently when the intersection of its prime ideals is zero, by Krull's theorem of *Commutative Rings*, and its reduced quotients are exactly its quotients by radical ideals, the largest of them being $R/\operatorname{nil}(R)$. Reducedness sits strictly between the general commutative ring and the domain: $\mathbb{Z}/4\mathbb{Z}$ is not reduced, while $\mathbb{Z} \times \mathbb{Z}$ and $\mathbb{Z}/6\mathbb{Z}$ are reduced and not domains.

The prime ideals separate the elements of a reduced ring: the product of the quotient maps $R \to R/\mathfrak{p}$ has kernel $\operatorname{nil}(R)$, so a reduced ring embeds into a product of domains and is a subdirect product of the domains $R/\mathfrak{p}$, one for each prime $\mathfrak{p}$. A finite reduced ring is a product of finitely many fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $x$ nilpotent | $x^n = 0$ for some $n \geq 1$ (*Rings*, §The Multiplicative Vocabulary) |
| $\operatorname{nil}(R)$ | Nilradical, the ideal of nilpotent elements |
| $\sqrt{I}$ | Radical of $I$; $\operatorname{nil}(R) = \sqrt{(0)}$ |
| $R_{\mathrm{red}}$ | Reduced quotient $R/\operatorname{nil}(R)$ |
| $R^{\times}$ | Group of units |
| $R$ reduced | $\operatorname{nil}(R) = (0)$ |
| $\mathfrak{p}$ | Prime ideal |
| $\operatorname{Spec} R$ | Prime spectrum, the poset of prime ideals |
| $\varepsilon$ | The nilpotent generator in the dual numbers $k[\varepsilon]/(\varepsilon^2)$ |
| $I^n$ | Product of $n$ copies of the ideal $I$ |

## Further Reading

- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the nilradical, the reduced quotient and the characterisation by prime ideals.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for nilpotents, the radical of an ideal and subdirect products.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for reduced rings, the nilradical and the passage to domains.
- Wolfgang Krull, *Idealtheorie* (Springer, 1935), for the original form of the theorem identifying the nilradical with the intersection of the prime ideals.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for nilpotent elements, idempotents and the reduced quotient.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989), for reduced rings and their relation to the prime spectrum.
