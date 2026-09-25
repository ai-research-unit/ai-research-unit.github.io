
# __GCD Domains__

## Introduction

Divisibility in an integral domain is a partial order on associate classes, and the question that organises this rung of the chain is whether two elements have a greatest common divisor in that order. When they always do, the domain is a **GCD domain**. The hypothesis is weaker than any of the factorisation hypotheses above it and stronger than being a domain, and it is the most general rung at which divisibility is governed by a gcd: in a GCD domain the gcd of two elements exists, generates $(a) + (b)$ when it is a linear combination, and the gcd and lcm of a pair are linked by $\gcd(a,b)\operatorname{lcm}(a,b) \sim ab$.

Above the GCD domain the chain splits and then rejoins. Two incomparable classes strengthen it: the unique factorisation domains, in which the gcd is computed from prime factorisations, and the Bézout domains, in which the gcd is always a linear combination of its arguments. Neither contains the other; the article's central structural point is that a single rung can be strengthened in two directions that meet only further up. The **only** material this article assumes from above is the divisibility theory of *Integral Domains*, directly above this article, and the two strengthenings are forward-referenced with flags.

Throughout, $R$ is an integral domain, as fixed in *Integral Domains*; divisibility, associates, irreducibles and primes are used in the sense of that article.

---

## The Greatest Common Divisor

### Definition and Uniqueness

**Definition.** Let $a, b \in R$, not both zero. An element $d \in R$ is a **greatest common divisor** of $a$ and $b$, written $d = \gcd(a,b)$, if

$$
d \mid a, \qquad d \mid b, \qquad \text{and} \qquad c \mid a,\ c \mid b \ \Longrightarrow \ c \mid d .
$$

An element $c$ with the first two properties is a **common divisor** of $a$ and $b$; so a greatest common divisor is a common divisor that every common divisor divides. The definition extends to any finite set of elements not all zero.

**Proposition.** Let $R$ be an integral domain.

**(a)** If $\gcd(a,b)$ exists for a pair not both zero, it is unique up to associates.

**(b)** $\gcd(a, 0) = a$ for $a \neq 0$, and $\gcd(a, b) = \gcd(b, a)$.

**(c)** If $u \in R^{\times}$ then $\gcd(ua, b) \sim \gcd(a,b)$, and $a \mid b$ if and only if $\gcd(a,b) \sim a$.

**Proof.** (a) If $d$ and $d'$ are both greatest common divisors then $d \mid d'$ and $d' \mid d$, so $d \sim d'$ by the proposition on associates in *Integral Domains*. (b) Every element divides $0$, and $a \mid a$. (c) Multiplication by a unit permutes the common divisors; and if $a \mid b$ then $a$ is a common divisor of $a$ and $b$ divisible by every common divisor, while $\gcd(a,b) \mid a$ with both being common divisors forces the two to be associates. $\square$

**Definition.** An integral domain $R$ is a **GCD domain** if every pair of elements of $R$, not both zero, has a greatest common divisor in $R$.

**Definition.** Two elements $a, b \in R$, not both zero, are **coprime** if their only common divisors are units; when $\gcd(a,b)$ exists this says $\gcd(a,b) \sim 1$.

### Divisibility Properties of the gcd

**Proposition.** Let $a, b, c \in R$, with $\gcd(a,b)$ and $\gcd(ca, cb)$ existing and $c \neq 0$. Then

$$
\gcd(ca, cb) \sim c \cdot \gcd(a,b) .
$$

**Proof.** Put $d = \gcd(a,b)$ and $e = \gcd(ca,cb)$. Since $cd \mid ca$ and $cd \mid cb$, the defining property of $e$ gives $cd \mid e$, say $e = c d f$. Now $e \mid ca$ and $e \mid cb$, that is, $cdf \mid ca$ and $cdf \mid cb$; cancelling $c$ by the domain hypothesis, $df \mid a$ and $df \mid b$. Hence $df \mid d$ by the defining property of $d$, so $f$ is a unit and $e \sim cd$. $\square$

**Corollary.** Let $d = \gcd(a,b)$ with $a, b$ not both zero, and write $a = da'$, $b = db'$. Then $a'$ and $b'$ have no common divisor outside $R^{\times}$; that is, $\gcd(a',b') \sim 1$. Moreover, if $\gcd(a', b) \sim 1$ and $\gcd(a', c) \sim 1$, then $\gcd(a', bc) \sim 1$.

**Proof.** Since $d = \gcd(da', db') \sim d \cdot \gcd(a',b')$ by the proposition, cancelling $d$ gives $1 \sim \gcd(a',b')$. For the second statement, coprimality is multiplicative in a GCD domain: if $\gcd(x, y) \sim 1$ and $\gcd(x, z) \sim 1$ then $\gcd(x, yz) \sim 1$, because a common divisor of $x$ and $yz$ is coprime to $z$ and therefore divides $y$ by the standard Euclid property of a GCD domain, that a divisor of a product coprime to one factor divides the other; the property is cited from the literature. The coprimality of $a'$ must be with $b$ and not merely with $b'$: for $a = 12$, $b = 18$, $d = 6$ one has $a' = 2$, $b' = 3$ and $\gcd(2,3) = 1$, while $\gcd(2, 18) = 2$. $\square$

**Remark.** The proposition is the reason a GCD domain behaves as if its elements had prime decompositions, even when they do not: every pair can be reduced to a coprime pair by dividing out the gcd. What a GCD domain does **not** supply is a factorisation of an element into irreducibles, and this is exactly what the strengthening to a unique factorisation domain adds. The class in which the reduction is accompanied by unique factorisation into irreducibles is *Unique Factorisation Domains*, below this article in this category.

---

## The Least Common Multiple

### Definition and the gcd–lcm Identity

**Definition.** Let $a, b \in R$, not both zero. An element $m \in R$ is a **least common multiple** of $a$ and $b$, written $m = \operatorname{lcm}(a,b)$, if

$$
a \mid m, \qquad b \mid m, \qquad \text{and} \qquad a \mid c,\ b \mid c \ \Longrightarrow \ m \mid c .
$$

A least common multiple, when it exists, is unique up to associates, by the same argument as for the gcd.

**Theorem.** Let $a, b \in R$ be nonzero. Then $\gcd(a,b)$ exists if and only if $\operatorname{lcm}(a,b)$ exists, and in that case

$$
\gcd(a,b) \cdot \operatorname{lcm}(a,b) \sim a b .
$$

**Proof.** Suppose $d = \gcd(a,b)$ exists and put $m = ab/d$, which lies in $R$ because $d \mid a$ and $d \mid b$. Then $m = a(b/d) = b(a/d)$, so $a \mid m$ and $b \mid m$. If $a \mid c$ and $b \mid c$, then $ab \mid cb$ and $ab \mid ca$, hence $ab$ divides the gcd of $cb$ and $ca$, which is $c \cdot \gcd(a,b) = cd$ by the proposition above; so $ab \mid cd$ and therefore $m = ab/d \mid c$. Hence $m = \operatorname{lcm}(a,b)$ and the identity holds. The converse is symmetric, reading $d = ab/m$; the details are the same. $\square$

**Corollary.** In any integral domain, $(a) \cap (b) = (\operatorname{lcm}(a,b))$ whenever the least common multiple exists, and $(a) + (b) \subseteq (\gcd(a,b))$ whenever the greatest common divisor exists.

**Proof.** $c \in (a) \cap (b)$ means $a \mid c$ and $b \mid c$, which by the definition of the lcm means $m \mid c$, that is, $c \in (m)$; conversely $a \mid m$ and $b \mid m$ say $m \in (a) \cap (b)$. For the second statement, $d \mid a$ and $d \mid b$ say $a, b \in (d)$, so $(a) + (b) \subseteq (d)$. $\square$

### The Ideal-Theoretic Characterisation

**Proposition.** Let $a, b \in R$ be nonzero and $d \in R$. Then $d$ is a greatest common divisor of $a$ and $b$ if and only if $(d)$ is the least principal ideal containing $(a) + (b)$: that is, $(a) + (b) \subseteq (d)$, and $(a) + (b) \subseteq (e)$ implies $(d) \subseteq (e)$.

**Proof.** The condition $(a) + (b) \subseteq (d)$ says exactly that $d \mid a$ and $d \mid b$. Given that, a further ideal $(e) \supseteq (a) + (b)$ satisfies $e \mid a$ and $e \mid b$, and the requirement $(d) \subseteq (e)$ is the requirement $e \mid d$. So the two formulations say the same thing. $\square$

**Theorem.** For an integral domain $R$ the following are equivalent.

**(a)** $R$ is a GCD domain.

**(b)** For all $a, b \in R$ the intersection $(a) \cap (b)$ is a principal ideal.

**(c)** Every pair of elements of $R$ has a least common multiple.

**Proof.** By the identity $\gcd \cdot \operatorname{lcm} \sim ab$, the existence of the gcd of a pair is equivalent to the existence of the lcm, so (a) and (c) are equivalent, and the ideal $(a) \cap (b)$ is generated by the lcm when it exists, by the corollary above; this gives (a) $\Leftrightarrow$ (b). $\square$

**Remark.** The characterisation (b) is the one that passes to the ideal theory of a general commutative ring: it says that the lattice of principal ideals of a GCD domain is closed under finite intersections. The class of Bézout domains below captures the dual closure property.

---

## The Two Incomparable Strengthenings

### Unique Factorisation Domains, Forward

**Proposition.** Every unique factorisation domain is a GCD domain.

**Proof.** In a unique factorisation domain every nonzero non-unit is a product of primes, and the gcd of two nonzero elements is the product of the primes occurring in both factorisations, each taken to the smaller exponent; this element divides both and is divisible by every common divisor, since a common divisor has a factorisation whose prime factors occur in both factorisations with exponents no larger. The details, together with the definition of unique factorisation, are *Unique Factorisation Domains*, below this article in this category. $\square$

That article also supplies the standard example that is a unique factorisation domain without being either a Bézout domain or a principal ideal domain, namely $\mathbb{Z}[x]$.

### Bézout Domains, Forward

**Proposition.** Let $R$ be an integral domain and $a, b \in R$ not both zero. Then $\gcd(a,b)$ exists and satisfies $(a,b) = (\gcd(a,b))$ if and only if the ideal $(a) + (b)$ is principal.

**Proof.** If $(a) + (b) = (d)$ then $d \mid a$ and $d \mid b$; if $c \mid a$ and $c \mid b$ then $d \in (a) + (b) \subseteq (c)$, so $c \mid d$; hence $d = \gcd(a,b)$. Conversely if $d = \gcd(a,b)$ and $d = ax + by$ then $d \in (a)+(b)$ and $(d) \subseteq (a)+(b) \subseteq (d)$, so equality holds. $\square$

**Definition.** An integral domain $R$ is a **Bézout domain** if every finitely generated ideal of $R$ is principal.

Thus in a Bézout domain every gcd exists, so a Bézout domain is a GCD domain; the converse fails, and the standard witness is $\mathbb{Z}[x]$, a GCD domain in which $(2, x)$ is not principal. The Bézout domains, their identity $d = ax + by$, and the ring of all algebraic integers as the standard non-Noetherian example, are *Bézout Domains*, below this article in this category.

### Incomparability

**Theorem.** The classes of unique factorisation domains and of Bézout domains are incomparable, and both are contained in the class of GCD domains.

**Proof.** Each of the two classes consists of GCD domains, by the two propositions above. For the incomparability, a unique factorisation domain that is not a Bézout domain is $\mathbb{Z}[x]$, in which $(2,x)$ is not principal, so $\gcd(2,x)$ is not a linear combination; and a Bézout domain that is not a unique factorisation domain is the ring $\overline{\mathbb{Z}}$ of all algebraic integers, which is Bézout but in which elements fail to factor into irreducibles. The first example is *Unique Factorisation Domains* and the second *Bézout Domains*, both below this article in this category. $\square$

The two strengthenings are therefore the two directions in which one can demand that divisibility be computable: by prime factorisation, or by a linear-combination identity. They meet in the principal ideal domains, which are precisely the Noetherian Bézout domains and also a subclass of the unique factorisation domains; the chain returns to a single line there, and continues to the Euclidean domains. Both statements belong to *Principal Ideal Domains*, below this article in this category.

---

## Linear Combinations and Back-Substitution

### The Identity

A greatest common divisor is not always a linear combination: it is when the ideal generated by the pair is principal, by the proposition above.

**Definition.** A greatest common divisor $d = \gcd(a,b)$ is a **Bézout combination** of $a$ and $b$ if there exist $x, y \in R$ with

$$
d = a x + b y .
$$

**Proposition.** Let $a, b \in R$ be nonzero and let $d = \gcd(a,b)$.

**(a)** $d$ is a Bézout combination of $a$ and $b$ if and only if $(d) = (a) + (b)$.

**(b)** If $d = ax + by$ and $e \mid a$, $e \mid b$, then $e \mid d$.

**Proof.** (a) is the proposition of the previous section. For (b), $e$ divides each of $a$ and $b$, hence each term of $ax + by$. $\square$

**Remark (back-substitution).** When the gcd is computed by a finite chain of divisions,

$$
r_{0} = a, \quad r_{1} = b, \quad r_{k+1} = \text{remainder of } r_{k-1} \text{ on division by } r_{k},
$$

the last nonzero remainder is a gcd, and each $r_{k+1}$ is an integer combination of the preceding two, so substituting the equations one after another **from the bottom upwards** exhibits the gcd as a combination $ax + by$. The construction requires a division algorithm and is carried out in *Euclidean Domains*, below this article in this category; the identity it produces is the Bézout combination of this section.

### Worked Example

In $\mathbb{Z}$ take $a = 240$ and $b = 46$. The division chain is

$$
240 = 5 \cdot 46 + 10, \qquad 46 = 4 \cdot 10 + 6, \qquad 10 = 1 \cdot 6 + 4, \qquad 6 = 1 \cdot 4 + 2, \qquad 4 = 2 \cdot 2 + 0 .
$$

The last nonzero remainder is $2 = \gcd(240,46)$. Back-substituting from the bottom,

$$
2 = 6 - 4 = 6 - (10 - 6) = 2 \cdot 6 - 10 = 2(46 - 4 \cdot 10) - 10 = 2 \cdot 46 - 9 \cdot 10 = 47 \cdot 46 - 9 \cdot 240 .
$$

So the Bézout combination is $2 = 240 \cdot (-9) + 46 \cdot 47$, and the identity is verified by expanding $47 \cdot 46 - 9 \cdot 240 = 2162 - 2160 = 2$.

**Corollary.** Let $a, b \in R$ be nonzero. If there exist $x, y$ with $ax + by = 1$, then every common divisor of $a$ and $b$ is a unit, so $1$ is a greatest common divisor of $a$ and $b$. Conversely, if $\gcd(a,b) = d$ is a Bézout combination $d = ax + by$ and $d$ is a unit, then $a(xd^{-1}) + b(yd^{-1}) = 1$.

**Proof.** A common divisor of $a$ and $b$ divides $ax + by = 1$, hence is a unit. Conversely, multiply the identity by $d^{-1}$. $\square$

---

## A Domain That Is Not a GCD Domain

The rung is strict: a domain need not have greatest common divisors.

**Example ($\mathbb{Z}[\sqrt{-5}]$).** Let $R = \mathbb{Z}[\sqrt{-5}]$ and recall the norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$ of *Integral Domains*, above this article, which is multiplicative. The pair $6$ and $2(1+\sqrt{-5})$ has no greatest common divisor.

- The elements $2$ and $1 + \sqrt{-5}$ both divide $6$, since $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$, and both divide $2(1+\sqrt{-5})$.
- Neither divides the other: $2 \nmid 1+\sqrt{-5}$, and $1+\sqrt{-5} \nmid 2$ since $N(1+\sqrt{-5}) = 6$ does not divide $N(2) = 4$.
- The elements of $R$ of norm dividing $36 = N(6)$ are the associates of $1, 2, 3, 6$, of $1 \pm \sqrt{-5}$, of $2 \pm \sqrt{-5}$ and of $4 \pm 2\sqrt{-5}$: a norm $a^2 + 5b^2$ dividing $36$ leaves $b = 0$ with $a \in \{\pm 1, \pm 2, \pm 3, \pm 6\}$, $b = \pm 1$ with $a \in \{\pm 1, \pm 2\}$, and $b = \pm 2$ with $a = \pm 4$. Among these, the divisors of $6$ up to units are $1, 2, 3, 6, 1+\sqrt{-5}, 1-\sqrt{-5}$: the elements $4 \pm 2\sqrt{-5}$ and $2 \pm \sqrt{-5}$ do not divide $6$, since $6/(4+2\sqrt{-5}) = (2-\sqrt{-5})/3 \notin R$ and $6/(2+\sqrt{-5}) = (4-2\sqrt{-5})/3 \notin R$.
- A greatest common divisor $d$ of $6$ and $2(1+\sqrt{-5})$ would divide $6$ and be divisible by both $2$ and $1+\sqrt{-5}$. From the list, the divisors of $6$ divisible by $2$ are the associates of $2$ and of $6$; of these only $6$ is divisible by $1+\sqrt{-5}$, since $2/(1+\sqrt{-5}) = (1-\sqrt{-5})/3 \notin R$. Hence $d$ would be an associate of $6$.
- But $6$ does not divide $2(1+\sqrt{-5})$, since $N(6) = 36$ does not divide $N(2(1+\sqrt{-5})) = 24$.

Hence no greatest common divisor exists, and $\mathbb{Z}[\sqrt{-5}]$ is a domain that is not a GCD domain. The same pair shows that $\mathbb{Z}[\sqrt{-5}]$ is not a unique factorisation domain, and the failure is not a defect of the ring of integers: $-5 \equiv 3 \pmod 4$, so $\mathbb{Z}[\sqrt{-5}]$ is already the whole ring of integers of $\mathbb{Q}(\sqrt{-5})$, and the failure of unique factorisation is a property of that ring of integers itself.

**Remark.** The repair of this failure is not elementwise but ideal-theoretic: one passes to the ideals of a Dedekind domain, where factorisation into prime ideals always holds. That theory is *Dedekind Domains and Ideal Class Groups*, below this article in this category.

---

## Summary

A greatest common divisor of a pair in an integral domain is a common divisor that every common divisor divides; it is unique up to associates, and it exists exactly when the pair has a least common multiple, in which case $\gcd(a,b)\operatorname{lcm}(a,b) \sim ab$. A GCD domain is a domain in which every pair has a greatest common divisor, equivalently one in which the intersection of two principal ideals is always principal. The gcd multiplies: $\gcd(ca,cb) \sim c\gcd(a,b)$, so dividing an element by the gcd of a pair leaves a coprime pair. The gcd is a linear combination of its arguments exactly when the ideal they generate is principal, and the combination is computed by back-substitution whenever a division algorithm is available.

The rung is strengthened in two incomparable directions. Every unique factorisation domain is a GCD domain, because the gcd is read off from prime factorisations; every Bézout domain is a GCD domain, because the gcd is the generator of the ideal generated by the pair. Neither class contains the other: $\mathbb{Z}[x]$ is a unique factorisation domain that is not Bézout, and the ring of all algebraic integers is Bézout and not a unique factorisation domain. The strictly weaker status of the GCD rung is witnessed by $\mathbb{Z}[\sqrt{-5}]$, in which $6$ and $2(1+\sqrt{-5})$ have no gcd.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Integral domain |
| $R^{\times}$ | Group of units |
| $a \mid b$ | $a$ divides $b$ |
| $a \sim b$ | Associates, $a = ub$ with $u \in R^{\times}$ |
| $(a)$, $(a, b)$ | Principal ideal generated by $a$; ideal generated by $a$ and $b$ |
| $\gcd(a,b)$ | Greatest common divisor, defined by divisibility and maximality |
| $\operatorname{lcm}(a,b)$ | Least common multiple, defined dually |
| GCD domain | Domain in which every pair not both zero has a gcd |
| Coprime | Having no common divisor outside $R^{\times}$ |
| Bézout combination | An expression $d = ax + by$ for $d = \gcd(a,b)$ |
| $(a) + (b)$ | Sum of ideals, the ideal generated by $a$ and $b$ |
| $(a) \cap (b)$ | Intersection, principal exactly when the lcm exists |
| $N(a + b\sqrt{-5}) = a^2 + 5b^2$ | Multiplicative norm on $\mathbb{Z}[\sqrt{-5}]$ |

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for gcds, lcms and Bézout's identity in the classical rings.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for divisibility, content and the gcd in a unique factorisation domain.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for greatest common divisors and the divisibility lattice of a domain.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for GCD domains, Bézout domains and the ideal-theoretic reading of divisibility.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for gcds, lcms and the arithmetic of quadratic rings.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for $\mathbb{Z}[\sqrt{-5}]$ and the failure of greatest common divisors in quadratic rings.
