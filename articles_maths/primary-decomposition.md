# __Primary Decomposition__

## Introduction

An integer factors uniquely into prime powers, and the ideal-theoretic counterpart of this statement is the **primary decomposition** of an ideal: the expression of an arbitrary ideal of a Noetherian ring as a finite intersection of primary ideals. The primary ideals play the role of the prime powers, the primes that occur are the **associated primes** of the ideal, and the theorem of Lasker and Noether asserts that every ideal has such a decomposition and that the associated primes are determined by the ideal.

The decomposition is not unique — one can always drop redundant components and refine others — but the ambiguity is controlled by two uniqueness theorems. The minimal associated primes and the corresponding primary components are unique, and the set of associated primes is unique; only the components attached to embedded primes are free to vary. This is the sense in which a primary decomposition is "unique up to the ambiguity that does not matter".

The theory is the algebraic form of the decomposition of an algebraic set into irreducible components, and it is the tool behind the Hilbert Nullstellensatz. Throughout, $R$ is a commutative Noetherian ring with $1 \neq 0$; the chain conditions and the nilradical are from *Noetherian and Artinian Rings*, localization and the ideal correspondence from *Localization and the Fraction Field*, and prime and maximal ideals from *Rings*, §§6–7. Where a result requires that the ring be Noetherian this is stated, since primary decomposition fails without it.

---

## Primary Ideals

### Definition and First Properties

**Definition.** A proper ideal $\mathfrak{q} \subsetneq R$ is **primary** if for all $x, y \in R$,

$$
xy \in \mathfrak{q} \quad \implies \quad x \in \mathfrak{q} \ \text{ or } \ y \in \operatorname{rad}(\mathfrak{q}),
$$

where $\operatorname{rad}(\mathfrak{q}) = \{r : r^n \in \mathfrak{q} \text{ for some } n \geq 1\}$ is the **radical** of $\mathfrak{q}$, also written $\sqrt{\mathfrak{q}}$.

The definition is asymmetric on purpose: the second alternative allows a power of $y$ to lie in $\mathfrak{q}$, which is what distinguishes a primary ideal from a prime ideal. Every prime ideal is primary, since then $\operatorname{rad}(\mathfrak{p}) = \mathfrak{p}$.

**Proposition (equivalent formulations).** Let $\mathfrak{q} \subsetneq R$ be a proper ideal. The following are equivalent.

**(a)** $\mathfrak{q}$ is primary.

**(b)** Every zero divisor of the quotient ring $R/\mathfrak{q}$ is nilpotent.

**(c)** The radical $\mathfrak{p} = \operatorname{rad}(\mathfrak{q})$ is prime, and for every $x \notin \mathfrak{q}$ the colon ideal $(\mathfrak{q} : x)$ is $\mathfrak{p}$-primary.

**Proof.** (a) $\Leftrightarrow$ (b): a class $\bar x \in R/\mathfrak{q}$ is a zero divisor exactly when there is $y \notin \mathfrak{q}$ with $xy \in \mathfrak{q}$; if $\mathfrak{q}$ is primary this forces $x \in \operatorname{rad}(\mathfrak{q})$, that is, $\bar x$ nilpotent. Conversely if every zero divisor of $R/\mathfrak{q}$ is nilpotent and $xy \in \mathfrak{q}$ with $y \notin \mathfrak{q}$, then $\bar x$ is a zero divisor, hence nilpotent, hence $x \in \operatorname{rad}(\mathfrak{q})$.

(a) $\Rightarrow$ (c): by the proposition below, $\mathfrak{p} = \operatorname{rad}(\mathfrak{q})$ is prime. Let $x \notin \mathfrak{q}$ and put $\mathfrak{c} = (\mathfrak{q} : x)$. If $ab \in \mathfrak{c}$ and $a \notin \mathfrak{c}$, then $abx \in \mathfrak{q}$ and $ax \notin \mathfrak{q}$, so primaryness gives $b \in \operatorname{rad}(\mathfrak{q}) = \mathfrak{p}$. Also $\operatorname{rad}(\mathfrak{c}) = \mathfrak{p}$: indeed $r \in \operatorname{rad}(\mathfrak{c})$ means $r^n x \in \mathfrak{q}$ for some $n$, which since $x \notin \mathfrak{q}$ forces $r^n \in \mathfrak{p}$, that is, $r \in \mathfrak{p}$. Hence $\mathfrak{c}$ is $\mathfrak{p}$-primary.

(c) $\Rightarrow$ (a): let $xy \in \mathfrak{q}$ with $x \notin \mathfrak{q}$, and put $\mathfrak{c} = (\mathfrak{q} : x)$. Then $y \in \mathfrak{c} \subseteq \operatorname{rad}(\mathfrak{c}) = \operatorname{rad}(\mathfrak{q})$, so the second alternative of primaryness holds. $\square$

**Definition.** If $\mathfrak{q}$ is primary, the radical $\mathfrak{p} = \operatorname{rad}(\mathfrak{q})$ is prime, and one says that $\mathfrak{q}$ is **$\mathfrak{p}$-primary**. The prime $\mathfrak{p}$ is uniquely determined by $\mathfrak{q}$.

**Proposition.** Let $\mathfrak{q}$ be a primary ideal. Then $\operatorname{rad}(\mathfrak{q})$ is a prime ideal, and it is the smallest prime ideal containing $\mathfrak{q}$. Conversely, if $\operatorname{rad}(\mathfrak{q})$ is a maximal ideal, then $\mathfrak{q}$ is primary.

**Proof.** Let $\mathfrak{p} = \operatorname{rad}(\mathfrak{q})$ and suppose $xy \in \mathfrak{p}$, so $(xy)^n \in \mathfrak{q}$ for some $n$. If $x \notin \mathfrak{p}$ then $x^n \notin \mathfrak{q}$, and $x^n y^n \in \mathfrak{q}$ with $x^n \notin \mathfrak{q}$ forces $y^n \in \mathfrak{p}$, hence $y \in \mathfrak{p}$. So $\mathfrak{p}$ is prime. It contains $\mathfrak{q}$ and is contained in every prime containing $\mathfrak{q}$, since a prime containing $\mathfrak{q}$ contains its radical. For the converse, if $\mathfrak{p} = \operatorname{rad}(\mathfrak{q})$ is maximal and $xy \in \mathfrak{q}$ with $x \notin \mathfrak{q}$, the image of $x$ in $R/\mathfrak{q}$ is a non-unit but the image of $\mathfrak{p}$ is the unique maximal ideal, so $x \in \mathfrak{p}$; write $x^n \in \mathfrak{q}$. Then $x^n y^n = (xy)^n \in \mathfrak{q}$; if $y \notin \mathfrak{p}$ then $y^n \notin \mathfrak{p}$ hence $y^n \notin \mathfrak{q}$, and from $x^n y^n \in \mathfrak{q}$ with $y^n \notin \mathfrak{q}$ we get $x \in \operatorname{rad}(\mathfrak{q}) = \mathfrak{p}$, a contradiction. So $y \in \mathfrak{p}$ and $\mathfrak{q}$ is primary. $\square$

### Examples

**Example.** In $\mathbb{Z}$ the primary ideals are $(0)$ together with the ideals $(p^n)$ for $p$ prime and $n \geq 1$. Indeed $(p^n)$ has radical $(p)$, which is maximal, hence $(p^n)$ is primary; and an ideal $(m)$ with $m$ divisible by two distinct primes is not primary, because if $m = p^a q^b \cdots$ with $p \neq q$ then $p \cdot (m/p) \in (m)$ with $p \notin (m)$ and $m/p \notin \operatorname{rad}((m)) = (p q \cdots)$. This is the ideal-theoretic reading of the factorisation of integers into prime powers.

**Example.** In a field $k$, the ideal $(x^n) \subseteq k[x]$ is $(x)$-primary for every $n \geq 1$, since its radical is the maximal ideal $(x)$. More generally $(f^n)$ is $(f)$-primary when $f$ is irreducible, by the same reason.

**Example.** The ideal $(x^2, y)$ in $k[x,y]$ is $(x,y)$-primary: its radical is the maximal ideal $(x,y)$, and the quotient $k[x,y]/(x^2,y) \cong k[x]/(x^2)$ has only nilpotent zero divisors.

**Example.** The ideal $\mathfrak{q} = (x^2, xy)$ in $k[x,y]$ is **not** primary. Indeed $x \cdot y \in \mathfrak{q}$, while $x \notin \mathfrak{q}$ and $y \notin \operatorname{rad}(\mathfrak{q}) = (x)$; equivalently, the class of $x$ in $k[x,y]/\mathfrak{q}$ is a zero divisor — killed by the class of $y$ — but is not nilpotent. Its primary decomposition appears below.

**Example.** A prime ideal $\mathfrak{p}$ that is not maximal gives many $\mathfrak{p}$-primary ideals, and not all of them are powers of $\mathfrak{p}$; for instance in $k[x,y]$ the ideal $(x, y^2)$ is $(x,y)$-primary while $((x,y)^2) = (x^2, xy, y^2)$ is also $(x,y)$-primary, and $(x, y^2) \supsetneq (x,y)^2$.

**Remark.** The radical of a primary ideal is prime, but the radical of an arbitrary ideal need not be: $\operatorname{rad}((xy)) = (xy)$ in $k[x,y]$, and $(xy)$ is not prime. What is true is that the radical of any ideal is the intersection of the minimal primes over it, a fact that follows from the existence of primary decomposition.

---

## The Lasker–Noether Theorem

### Irreducible Ideals

**Definition.** A proper ideal $I \subsetneq R$ is **irreducible** if it cannot be written as an intersection $I = J \cap K$ of two ideals $J, K$ both strictly larger than $I$.

**Lemma.** In a Noetherian ring, every ideal is a finite intersection of irreducible ideals.

**Proof.** Suppose not. The set of ideals that are not finite intersections of irreducible ideals is nonempty and therefore has a maximal element $I$ by the ascending chain condition. Then $I$ is reducible, say $I = J \cap K$ with $J, K \supsetneq I$. By maximality of $I$, both $J$ and $K$ are finite intersections of irreducible ideals, and hence so is their intersection $I$, a contradiction. $\square$

**Lemma.** In a Noetherian ring, every irreducible ideal is primary.

**Proof.** Let $I$ be irreducible and suppose it is not primary. Then there are $x, y \in R$ with $xy \in I$, $x \notin I$ and $y \notin \operatorname{rad}(I)$. Consider the ascending chain of ideals

$$
(I : y) \subseteq (I : y^2) \subseteq (I : y^3) \subseteq \cdots, \qquad (I : y^n) = \{r \in R : r y^n \in I\}.
$$

It stabilises, so there is $N$ with $(I : y^N) = (I : y^{N+1})$. We claim

$$
I = (I + (x)) \cap (I + (y^N)).
$$

One inclusion is clear. For the other, let $z = a + r x = b + s y^N$ with $a, b \in I$ and $r, s \in R$ lie in the intersection. Then

$$
z y = a y + r x y \in I,
$$

because $a \in I$ and $xy \in I$; hence $z \in (I : y)$. On the other hand $z y = b y + s y^{N+1} \in I$, so $s y^{N+1} \in I$, that is, $s \in (I : y^{N+1}) = (I : y^N)$; therefore $s y^N \in I$ and $z = b + s y^N \in I$. So the intersection is contained in $I$, and equality holds. Now $(I + (x)) \supsetneq I$ because $x \notin I$, and $(I + (y^N)) \supsetneq I$ because $y^N \notin I$, since $y \notin \operatorname{rad}(I)$. This contradicts the irreducibility of $I$. Hence $I$ is primary. $\square$

### Existence

**Theorem (Lasker–Noether).** Let $R$ be a commutative Noetherian ring. Every proper ideal $I \subsetneq R$ is a finite intersection of primary ideals,

$$
I = \mathfrak{q}_1 \cap \mathfrak{q}_2 \cap \cdots \cap \mathfrak{q}_r .
$$

**Proof.** By the two lemmas, $I$ is a finite intersection of irreducible ideals, and each irreducible ideal is primary. $\square$

**Definition.** A primary decomposition $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_r$ is **irredundant** (or minimal) if no $\mathfrak{q}_i$ contains the intersection of the others, and the $\mathfrak{q}_i$ have pairwise distinct radicals. Every decomposition can be made irredundant by deleting redundant components and combining components with the same radical.

The following structural fact is useful and is not entirely obvious from the definition.

**Proposition.** Let $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_r$ be an irredundant primary decomposition. Then the primes $\mathfrak{p}_i = \operatorname{rad}(\mathfrak{q}_i)$ are precisely the prime ideals of the form $(I : x)$ for some $x \in R$, where $(I : x) = \{r : rx \in I\}$.

**Proof sketch.** For $x \in R$ the annihilator-type ideal $(I : x)$ is contained in some $\mathfrak{p}_i$ whenever it is prime, because $(I : x) \subseteq (I : x) + \mathfrak{q}_i$ and the standard computation on the finitely many components shows any prime of this form is one of the $\mathfrak{p}_i$. Conversely, for each $i$, irredundance supplies $x \notin \mathfrak{q}_i$ lying in every other $\mathfrak{q}_j$; then $(I : x)$ has radical exactly $\mathfrak{p}_i$, and after replacing $x$ by a suitable power one finds an element for which $(I : x) = \mathfrak{p}_i$. $\square$

---

## Associated Primes

### Definition and Finiteness

**Definition.** Let $I$ be a proper ideal of $R$. A prime ideal $\mathfrak{p}$ is an **associated prime** of $I$ if

$$
\mathfrak{p} = (I : x)
$$

for some $x \in R$, where $(I : x) = \{r \in R : rx \in I\}$. The set of associated primes is written $\operatorname{Ass}(I)$. The **minimal primes** of $I$ are the prime ideals minimal among those containing $I$; they are also called the **isolated primes**, and the associated primes that are not minimal are **embedded**.

**Theorem.** For a proper ideal $I$ of a Noetherian ring $R$, the set $\operatorname{Ass}(I)$ is finite, and it contains every minimal prime of $I$. The minimal primes of $I$ are exactly the minimal elements of $\operatorname{Ass}(I)$.

**Proof sketch.** Finiteness follows from the finiteness of the primary decomposition together with the proposition above. For the second claim, if $\mathfrak{p}$ is a prime containing $I$, localizing at $\mathfrak{p}$ gives $I_\mathfrak{p} \subseteq \mathfrak{p}_\mathfrak{p}$; the associated primes of $I$ in the localization are the extensions of associated primes contained in $\mathfrak{p}$, and one of them is $\mathfrak{p}$ itself when $\mathfrak{p}$ is minimal over $I$, because then the localized quotient has a unique minimal prime. This identifies the minimal primes with the minimal associated primes. $\square$

**Theorem (zero divisors).** The zero divisors of $R/I$ form the union of the associated primes,

$$
\bigcup_{x \notin I} \operatorname{ann}(\bar x) \;=\; \bigcup_{\mathfrak{p} \in \operatorname{Ass}(I)} \mathfrak{p},
$$

where $\operatorname{ann}(\bar x) = (I : x) \subseteq R$. In particular, an element $x \in R$ is a zero divisor modulo $I$ exactly when it lies in some associated prime of $I$.

**Proof sketch.** If $x \in \mathfrak{p} \in \operatorname{Ass}(I)$ with $\mathfrak{p} = (I : y)$, then $xy \in I$ with $y \notin I$, so $x$ kills the nonzero class of $y$. Conversely, if $xy \in I$ with $y \notin I$, then $(I : y)$ is a nonzero ideal, and any maximal element among the ideals $\operatorname{ann}(\bar z)$ with $z \notin I$ is prime and hence associated; it contains $(I : y)$, so $x$ lies in an associated prime. $\square$

### The Uniqueness Theorems

The first uniqueness theorem is the statement that the associated primes carry no ambiguity.

**Theorem (first uniqueness theorem).** The set $\operatorname{Ass}(I)$ depends only on $I$, and not on the choice of irredundant primary decomposition: the primes $\operatorname{rad}(\mathfrak{q}_i)$ of any irredundant decomposition are exactly the associated primes of $I$ and are distinct.

**Proof.** Immediate from the description of the $\mathfrak{p}_i$ as the primes of the form $(I : x)$ and the finiteness of the decomposition. $\square$

**Theorem (second uniqueness theorem).** Let $I = \bigcap_i \mathfrak{q}_i$ be an irredundant primary decomposition and let $\mathfrak{p}_i = \operatorname{rad}(\mathfrak{q}_i)$. If $\mathfrak{p}_i$ is a minimal prime of $I$, then the component $\mathfrak{q}_i$ is uniquely determined by $I$ and $\mathfrak{p}_i$: with $\iota : R \to R_{\mathfrak{p}_i}$ the localization map and $I_{\mathfrak{p}_i}$ the localization of the ideal $I$,

$$
\mathfrak{q}_i = \iota^{-1}(I_{\mathfrak{p}_i}).
$$

Equivalently, $\mathfrak{q}_i$ consists of those $r \in R$ with $sr \in I$ for some $s \notin \mathfrak{p}_i$.

**Proof.** Localizing at $\mathfrak{p}_i$ kills every component $\mathfrak{q}_j$ with $j \neq i$ for which $\mathfrak{p}_j \not\subseteq \mathfrak{p}_i$, and the minimality of $\mathfrak{p}_i$ guarantees this for every $j \neq i$. So $I_{\mathfrak{p}_i} = (\mathfrak{q}_i)_{\mathfrak{p}_i}$, and the contraction of $(\mathfrak{q}_i)_{\mathfrak{p}_i}$ is the set of $r$ with $sr \in \mathfrak{q}_i$ for some $s \notin \mathfrak{p}_i$. Since $\mathfrak{q}_i$ is $\mathfrak{p}_i$-primary, this contraction equals $\mathfrak{q}_i$; and it is determined by $I$ and $\mathfrak{p}_i$ alone. $\square$

Thus the decomposition is unique on the minimal primes; the ambiguity resides entirely in the components at embedded primes. The following corollary is a frequent substitute for a full decomposition.

**Corollary.** Let $I = \bigcap_i \mathfrak{q}_i$ be an irredundant primary decomposition with minimal primes $\mathfrak{p}_1, \ldots, \mathfrak{p}_s$. Then

$$
\operatorname{rad}(I) = \mathfrak{p}_1 \cap \cdots \cap \mathfrak{p}_s,
$$

the intersection of the minimal primes. In particular $\operatorname{rad}(I)$ is radical, and $R/\operatorname{rad}(I)$ is a reduced ring.

**Proof.** Taking radicals of an intersection gives the intersection of the radicals, and the radical of a primary ideal is its prime. The embedded primes contain minimal primes and are therefore absorbed in the intersection. $\square$

### Worked Decompositions

**Example.** In $k[x,y]$,

$$
(x^2, xy) = (x) \cap (x^2, y).
$$

Indeed every element of the left side is divisible by $x$ and lies in $(x^2, y)$; conversely, if $f \in (x) \cap (x^2,y)$ then $f = x g = x^2 a + y b$, and modulo $x$ we get $x \mid y b$, hence $x \mid b$, say $b = x c$, giving $f = x(xa + yc) \in (x^2, xy)$. The associated primes are

$$
\operatorname{Ass}((x^2,xy)) = \{(x), (x,y)\},
$$

with $(x)$ minimal and $(x,y)$ embedded. The component at the minimal prime $(x)$ is $(x)$ itself, and it is unique by the second uniqueness theorem.

**Example.** In $k[x,y,z]$,

$$
(xy, xz) = (x) \cap (y, z).
$$

The right side consists of the polynomials divisible by $x$ and vanishing on the line $y = z = 0$, which is exactly the set of $f$ vanishing on the union of a plane and a line; the left side is generated by $xy$ and $xz$. Both components are prime, so the decomposition has no embedded primes.

**Example.** In $\mathbb{Z}$, the decomposition of $(360)$ with $360 = 2^3 \cdot 3^2 \cdot 5$ is

$$
(360) = (8) \cap (9) \cap (5).
$$

All three primes $(2), (3), (5)$ are minimal, so the decomposition is unique; this is the unique factorisation of $360$ written as an ideal decomposition.

---

## Primary Decomposition and the Nullstellensatz

### The Nullstellensatz

Let $k$ be a field and let $\overline{k}$ be an algebraic closure. For an ideal $I \subseteq k[x_1, \ldots, x_n]$, the **zero set** of $I$ in $\overline{k}^n$ is

$$
V(I) = \{a \in \overline{k}^n : f(a) = 0 \text{ for all } f \in I\},
$$

and for a subset $S \subseteq \overline{k}^n$ the **ideal** of $S$ is

$$
I(S) = \{f \in k[x_1, \ldots, x_n] : f(a) = 0 \text{ for all } a \in S\}.
$$

The set $V(I)$ depends only on $\operatorname{rad}(I)$, so the correspondence is between radical ideals and zero sets. Each $V(I)$ is the intersection of the finitely many sets $V(\mathfrak{p})$ with $\mathfrak{p}$ a minimal prime of $I$, and these are the **irreducible components** of $V(I)$; the geometric content of primary decomposition is that the decomposition into irreducible pieces is finite.

**Theorem (weak Nullstellensatz).** Let $k$ be algebraically closed and let $I \subseteq k[x_1, \ldots, x_n]$ be a proper ideal. Then $V(I) \neq \emptyset$: every proper ideal has a common zero.

**Proof sketch.** A proper ideal is contained in a maximal ideal $\mathfrak{m}$, and it suffices to show that a maximal ideal $\mathfrak{m} \subseteq k[x_1, \ldots, x_n]$ with $k$ algebraically closed has the form $(x_1 - a_1, \ldots, x_n - a_n)$. This is the algebraic form of the statement that $k[x_1, \ldots, x_n]/\mathfrak{m}$ is a finite extension field of $k$, hence equal to $k$ by algebraic closedness. The finiteness of the extension is Zariski's lemma, an instance of the Nullstellensatz that uses the integral extension theory. $\square$

**Theorem (strong Nullstellensatz).** Let $k$ be algebraically closed and let $I \subseteq k[x_1, \ldots, x_n]$ be an ideal. Then

$$
I(V(I)) = \operatorname{rad}(I).
$$

Equivalently, the maps $I \mapsto V(I)$ and $S \mapsto I(S)$ are inverse bijections between radical ideals and algebraic subsets of $k^n$.

**Proof sketch.** The inclusion $\operatorname{rad}(I) \subseteq I(V(I))$ is clear. For the reverse inclusion, let $f$ vanish wherever $I$ does. Introduce a new variable $t$ and consider the ideal $J = I + (t f - 1) \subseteq k[x_1, \ldots, x_n, t]$; it has no common zero, so by the weak Nullstellensatz it is the whole ring, say $1 = \sum g_i h_i + g(tf - 1)$. Substituting $t = 1/f$ and clearing denominators, which is the classical Rabinowitsch trick, produces an identity $f^m = \sum a_i h_i$ with $h_i \in I$, whence $f \in \operatorname{rad}(I)$. $\square$

**Corollary (bijection).** Over an algebraically closed field the radical ideals of $k[x_1, \ldots, x_n]$ correspond bijectively to the algebraic subsets of $k^n$, and the maximal ideals correspond to the points $(a_1, \ldots, a_n)$. An algebraic set is irreducible exactly when its ideal is prime.

**Proof.** The first two statements are the strong Nullstellensatz and the description of maximal ideals. For the last, if $V = V(\mathfrak{p})$ with $\mathfrak{p}$ prime and $V = V_1 \cup V_2$ with $V_i$ algebraic, then $\mathfrak{p} = I(V) = I(V_1) \cap I(V_2)$; a prime containing an intersection contains one factor, so $V \subseteq V_i$ for some $i$ and $V = V_i$. Conversely if $V$ is irreducible and $fg \in I(V)$, then $V \subseteq V(f) \cup V(g)$ with both closed, so $V \subseteq V(f)$ or $V \subseteq V(g)$ by irreducibility, giving $f \in I(V)$ or $g \in I(V)$. $\square$

**Remark.** Primary decomposition and the Nullstellensatz are dual descriptions of the same finiteness: the decomposition $I = \bigcap \mathfrak{q}_i$ with minimal primes $\mathfrak{p}_i$ gives $V(I) = \bigcup V(\mathfrak{p}_i)$ as the decomposition into irreducible components, and the embedded primes correspond to components contained in others and invisible in the zero set. The scheme-theoretic strengthening of this correspondence, in which the primary components retain the infinitesimal information that $V(I)$ discards, requires the sheaves of Part II.

### Krull's Principal Ideal Theorem Revisited

The dimension theory takes from primary decomposition one input.

**Theorem (Krull's principal ideal theorem).** Let $R$ be Noetherian and let $a \in R$. Then every minimal prime over the principal ideal $(a)$ has height at most $1$.

**Proof sketch.** A minimal prime $\mathfrak{p}$ over $(a)$ is an associated prime in the localization at $\mathfrak{p}$, so it is isolated and its primary component is unique; after localizing one may suppose $R$ is a Noetherian local ring with maximal ideal $\mathfrak{p}$ and $\operatorname{rad}((a)) = \mathfrak{p}$. The argument then shows that the maximal ideal has height at most $1$, by an induction on the number of generators of $\mathfrak{p}$ that uses primary decomposition to identify the minimal primes of the successive quotients. $\square$

The height of a prime ideal is the supremum of the lengths of chains of primes below it, and the theorem is the reason a Noetherian ring has finite-dimensional local behaviour in codimension one; the full development lies outside this article.

---

## Summary

A proper ideal $\mathfrak{q}$ is primary when a product $xy \in \mathfrak{q}$ can only be explained by $x \in \mathfrak{q}$ or by a power of $y$ lying in $\mathfrak{q}$; equivalently, every zero divisor of $R/\mathfrak{q}$ is nilpotent. The radical of a primary ideal is prime, and a primary ideal is called $\mathfrak{p}$-primary for its unique radical $\mathfrak{p}$; if this radical is maximal then the ideal is primary.

Every ideal of a Noetherian ring is a finite intersection of primary ideals, by the theorem of Lasker and Noether: an ideal is a finite intersection of irreducible ideals, and every irreducible ideal of a Noetherian ring is primary. The primes occurring in an irredundant decomposition are exactly the associated primes, that is, the primes of the form $(I : x)$; they are finite in number, and they are the union of the zero divisors of $R/I$. The minimal primes are the minimal associated primes, and the corresponding primary components are uniquely determined by $I$. The components at embedded primes are not unique, and this is the only ambiguity.

Over an algebraically closed field primary decomposition is dual to the decomposition of an algebraic set into irreducible components, and the Nullstellensatz states that $I(V(I)) = \operatorname{rad}(I)$: radical ideals correspond to algebraic sets, maximal ideals to points, and prime ideals to irreducible sets.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative Noetherian ring with $1 \neq 0$ |
| $I, J$ | Ideals of $R$ |
| $\mathfrak{p}, \mathfrak{q}, \mathfrak{m}$ | Prime, primary, maximal ideal |
| $\operatorname{rad}(I) = \sqrt{I}$ | Radical of $I$, $\{x : x^n \in I \text{ for some } n\}$ |
| $\mathfrak{p}$-primary | Primary ideal with radical $\mathfrak{p}$ |
| $(I : x)$ | $= \{r \in R : rx \in I\}$, a colon ideal |
| $\operatorname{Ass}(I)$ | Set of associated primes of $I$ |
| $\operatorname{Min}(I)$ | Set of minimal primes over $I$ |
| $\operatorname{Spec}(R)$ | Set of prime ideals of $R$ |
| $R_{\mathfrak{p}}$ | Localization of $R$ at the prime $\mathfrak{p}$ |
| $I_\mathfrak{p}$ | Localization of the ideal $I$ |
| $k[x_1, \ldots, x_n]$ | Polynomial ring over a field $k$ |
| $V(I)$ | Zero set of $I$ in $\overline{k}^n$ |
| $I(S)$ | Ideal of polynomials vanishing on $S$ |
| $\overline{k}$ | Algebraic closure of $k$ |





## Further Reading

- Emanuel Lasker, "Zur Theorie der Moduln und Ideale", *Mathematische Annalen* 60 (1905), 20–116, for the original decomposition theorem for polynomial rings.
- Emmy Noether, "Idealtheorie in Ringbereichen", *Mathematische Annalen* 83 (1921), 24–66, for primary decomposition in an arbitrary Noetherian ring and the associated primes.
- Wolfgang Krull, "Primidealketten in allgemeinen Ringbereichen", *Sitzungsberichte der Heidelberger Akademie der Wissenschaften* (1928), for the principal ideal theorem and the height of primes.
- David Hilbert, "Über die Theorie der algebraischen Formen", *Mathematische Annalen* 36 (1890), 473–534, for the Nullstellensatz and the algebraic theory of zero sets.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for primary decomposition, the associated primes and the uniqueness theorems.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989), for the two uniqueness theorems and Krull's principal ideal theorem in the standard modern presentation.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra, Volume I* (Van Nostrand, 1958), for the geometric reading of primary decomposition and irreducible components.
- Miles Reid, *Undergraduate Commutative Algebra* (Cambridge University Press, 1995), for the worked decomposition of monomial ideals and the Nullstellensatz with examples.
