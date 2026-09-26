# __The Rational Numbers ($\mathbb{Q}$)__

## Introduction

The rational numbers are the field of fractions of the integers: the smallest field containing $\mathbb{Z}$, equivalently the smallest field of characteristic $0$, equivalently the prime field of every field of characteristic $0$. Everything about $\mathbb{Q}$ that is algebraic follows from this one construction: the field axioms, the absence of proper subfields, the uniqueness of the ordering, the triviality of the automorphism group, and the fact that every element is a ratio of two integers in essentially one way. What $\mathbb{Q}$ lacks is completeness, and the two ways of repairing that defect, by order and by absolute value, produce $\mathbb{R}$ and the fields $\mathbb{Q}_p$.

This article carries out the construction of $\mathbb{Q}$ from $\mathbb{Z}$, establishes its universal property, records its order and divisibility structure, and describes its subrings, its unit group, its orderings and its completions. The analysis of $\mathbb{Q}$ as a metric space belongs to the companion treatments of the real numbers and of valuations; the completions are named here and constructed in *Absolute Values, Valuations and Completions* and *The Real Numbers*.

Throughout, $\mathbb{Z}$ is the ring of integers and $\mathbb{Q} = \operatorname{Frac}(\mathbb{Z})$. Divisibility, prime factorization and localization are from *Integral Domains*, *Unique Factorisation Domains* and *Localization and the Fraction Field*.

---

## The Field of Fractions of $\mathbb{Z}$

### Construction

**Theorem.** $\mathbb{Z}$ is an integral domain, and its field of fractions

$$
\mathbb{Q} = \operatorname{Frac}(\mathbb{Z}) = (\mathbb{Z} \times (\mathbb{Z} \setminus \{0\}))/\sim, \qquad (a,b) \sim (c,d) \iff ad = bc,
$$

with addition and multiplication defined by

$$
\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd},
$$

is a field of characteristic $0$.

**Proof.** $\mathbb{Z}$ is an integral domain, so the relation $\sim$ is an equivalence relation and the displayed operations are well defined; the general construction of the fraction field is given in *Localization and the Fraction Field*. In $\mathbb{Q}$ the class of $\tfrac{a}{1}$ is nonzero whenever $a \neq 0$, and $n \cdot 1 = \tfrac{n}{1} \neq 0$ for every $n \geq 1$, so the characteristic is $0$. $\square$

**Theorem (universal property).** Let $K$ be a field and let $\varphi : \mathbb{Z} \to K$ be an injective ring homomorphism. Then there is a unique ring homomorphism $\Phi : \mathbb{Q} \to K$ with $\Phi(\tfrac{n}{1}) = \varphi(n)$; it is injective, and its image is the prime field of $K$.

**Proof.** The map $\Phi(\tfrac{a}{b}) = \varphi(a)\varphi(b)^{-1}$ is well defined because $\varphi(b) \neq 0$ for $b \neq 0$, and it is a ring homomorphism; uniqueness is forced because every rational is a quotient of images of integers. Injectivity: a field homomorphism is injective. $\square$

**Corollary.** $\mathbb{Q}$ is the prime field of characteristic $0$: it is the smallest subfield of any field of characteristic $0$, and every field of characteristic $0$ contains a copy of $\mathbb{Q}$ as its prime field. Up to isomorphism, $\mathbb{Q}$ is the only field of characteristic $0$ whose only subfield is itself, and it is the initial object in the category of fields of characteristic $0$.

### Basic Arithmetic

**Theorem (fundamental theorem of arithmetic).** Every nonzero integer has a factorization into primes, unique up to order and signs, and consequently every $x \in \mathbb{Q}^\times$ has a unique expression

$$
x = \operatorname{sgn}(x) \prod_p p^{v_p(x)}, \qquad v_p(x) \in \mathbb{Z},\ \text{finitely many nonzero},
$$

where $\operatorname{sgn}(x) = \pm 1$ and $v_p$ is the $p$-adic valuation of *Absolute Values, Valuations and Completions*.

**Proof.** The factorization of integers is the unique factorization property of $\mathbb{Z}$ as a Euclidean domain, from *Euclidean Domains*; the rational statement follows by writing $x = a/b$ and subtracting the exponent vectors of $b$ from those of $a$, the uniqueness following from uniqueness for $a$ and $b$. $\square$

**Corollary (the unit group).** There is a group isomorphism

$$
\mathbb{Q}^\times \cong \mathbb{Z}/2\mathbb{Z} \oplus \bigoplus_p \mathbb{Z},
$$

the sign giving the $\mathbb{Z}/2$ and the exponent of each prime giving a copy of $\mathbb{Z}$.

**Corollary.** $\mathbb{Q}$ is a field; hence its only ideals are $0$ and $\mathbb{Q}$, it is a principal ideal domain and a unique factorization domain in the trivial sense, and so is $\mathbb{Q}[x]$, which is moreover a Euclidean domain for the degree function.

---

## The Order of $\mathbb{Q}$

### The Ordering

**Definition.** A rational $x = \tfrac{a}{b}$ is **positive** if $ab > 0$ in $\mathbb{Z}$; the order is $x < y$ iff $y - x$ is positive.

**Theorem.** The relation so defined is a total order on $\mathbb{Q}$ making it an ordered field, and it is the only ordering of $\mathbb{Q}$.

**Proof.** Well-definedness: if $\tfrac{a}{b} = \tfrac{c}{d}$ then $ad = bc$ and $ab$ has the same sign as $cd$, since $abd^2 = b^2cd$ and $d^2, b^2 > 0$. The order axioms reduce to the corresponding facts in $\mathbb{Z}$, and multiplication by a positive rational preserves positivity by the sign rules. Uniqueness: in any ordering of a field, $1 > 0$ by the basic rules of *Ordered Fields*, hence $n \cdot 1 > 0$ for $n \geq 1$ and $n \cdot 1 < 0$ for $n \leq -1$; so the sign of every integer is forced, and then the sign of every ratio is forced, giving the positive cone displayed. $\square$

**Corollary.** $\mathbb{Q}$ is an Archimedean ordered field and the smallest one: it embeds as an ordered subfield in every ordered field. Its automorphism group is trivial, $\operatorname{Aut}(\mathbb{Q}) = 1$, and the only order-preserving automorphism of $\mathbb{Q}$ is the identity.

**Theorem (the embedding of $\mathbb{Z}$ and density).** The map $\mathbb{Z} \to \mathbb{Q}$, $n \mapsto \tfrac{n}{1}$ is an injective order-preserving ring homomorphism, and $\mathbb{Z}$ is unbounded above in $\mathbb{Q}$. The order on $\mathbb{Q}$ is dense: for $x < y$ there is $z$ with $x < z < y$, for instance $z = \tfrac{x+y}{2}$.

**Proof.** Injectivity and order-preservation are immediate from the construction. Unboundedness: for any $\tfrac{a}{b}$ with $b > 0$ the integer $\lvert a \rvert + 1$ exceeds it, since $\tfrac{a}{b} \leq a < a+1$ for $a \geq 0$ and $\tfrac{a}{b} < 0 < \lvert a \rvert + 1$ for $a < 0$. Density: $2 = 1 + 1 > 0$, so $2^{-1} > 0$ and $x = \tfrac{x+x}{2} < \tfrac{x+y}{2} < \tfrac{y+y}{2} = y$. $\square$

**Remark.** Density is a property of the order alone and does not make $\mathbb{Q}$ complete: the set $\{x \in \mathbb{Q} : x > 0,\ x^2 < 2\}$ is nonempty and bounded above and has no least upper bound in $\mathbb{Q}$, by the classical irrationality of $\sqrt2$. Completeness is treated in *Real-Closed and Complete Ordered Fields* and *The Real Numbers*.

---

## Subrings, Ideals and Localizations

### The Subrings of $\mathbb{Q}$

**Theorem.** Every subring $R \subseteq \mathbb{Q}$ is a localization of $\mathbb{Z}$: there is a set of primes $S$ such that

$$
R = \mathbb{Z}_S = \left\{\frac{a}{b} \in \mathbb{Q} : a \in \mathbb{Z},\ b \in \mathbb{Z}\setminus\{0\},\ \text{every prime dividing } b \text{ lies in } S\right\}.
$$

Conversely each such $\mathbb{Z}_S$ is a subring of $\mathbb{Q}$ containing $\mathbb{Z}$, and the correspondence $S \mapsto \mathbb{Z}_S$ is bijective between sets of primes and subrings of $\mathbb{Q}$ containing $\mathbb{Z}$.

**Proof sketch.** Given $R$, let $S = \{p \text{ prime} : \tfrac1p \in R\}$. If $x = \tfrac{a}{b} \in R$ in lowest terms, then $\gcd(a,b) = 1$, so there are integers $u, v$ with $ua + vb = 1$, whence $\tfrac{1}{b} = u\tfrac{a}{b} + v \in R$ by the Bézout relation; multiplying $\tfrac1b$ by $b/p$ for a prime $p \mid b$ gives $\tfrac1p \in R$, so every prime divisor of $b$ lies in $S$ and $R \subseteq \mathbb{Z}_S$. Conversely, if $x = \tfrac{a}{b}$ with every prime divisor of $b$ in $S$, then $\tfrac1b$ is a product of the elements $\tfrac1p \in R$ and their powers, so $\tfrac1b \in R$ and $x = a \cdot \tfrac1b \in R$; hence $\mathbb{Z}_S \subseteq R$. Bijectivity: $S$ is recovered from $\mathbb{Z}_S$ as the primes with $\tfrac1p \in \mathbb{Z}_S$. $\square$

**Corollary.** $\mathbb{Z}$ and $\mathbb{Q}$ are the extreme cases $S = \emptyset$ and $S = $ all primes; the intermediate rings $\mathbb{Z}_S$ are precisely the rings between $\mathbb{Z}$ and $\mathbb{Q}$, and each is a principal ideal domain obtained from $\mathbb{Z}$ by inverting the primes in $S$. The rings $\mathbb{Z}_{(p)}$ for a single prime $p$, the localizations of *Localization and the Fraction Field*, are the valuation rings of the $p$-adic valuations.

### Ideals and Modules over $\mathbb{Q}$

**Proposition.** The only ideals of $\mathbb{Q}$ are $0$ and $\mathbb{Q}$; consequently $\mathbb{Q}$ is a field, every nonzero element is a unit, and $\mathbb{Q}$ has no proper nonzero quotients.

**Proof.** If $I \neq 0$ contains $x \neq 0$ then $1 = x \cdot x^{-1} \in I$, so $I = \mathbb{Q}$. $\square$

**Proposition.** $\mathbb{Z}$-submodules of $\mathbb{Q}$ need not be ideals, and are not classified by a single invariant: the additive subgroups of $\mathbb{Q}$ include $\mathbb{Z}$, $\mathbb{Z}[\tfrac12]$, $\mathbb{Z}_{(p)}$ and the $p$-primary subgroups, and the classification of the subgroups of $\mathbb{Q}$ belongs to the theory of abelian groups. The finitely generated $\mathbb{Z}$-submodules of $\mathbb{Q}$ are exactly the cyclic ones, $\mathbb{Z}\tfrac{a}{b}$, and the structure theory of modules over $\mathbb{Z}$ belongs to *Modules*.

---

## $\mathbb{Q}$ as a Field: Algebraic Properties

**Theorem.** The following hold for $\mathbb{Q}$.

**(a)** $\mathbb{Q}$ has characteristic $0$, and every field of characteristic $0$ contains a copy of $\mathbb{Q}$.

**(b)** $\mathbb{Q}$ is countable.

**(c)** $\mathbb{Q}$ is not algebraically closed: the polynomial $x^2 - 2$ has no rational root.

**(d)** The algebraic closure of $\mathbb{Q}$ is the field $\overline{\mathbb{Q}}$ of algebraic numbers, which is countable; $\mathbb{Q}$ has extensions of every finite degree, and its absolute Galois group $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ is a large profinite group.

**(e)** $\mathbb{Q}$ is a perfect field, and every finite extension of $\mathbb{Q}$ is separable.

**(f)** $\mathbb{Q}$ has a unique ordering, and it is Archimedean; it is not order-complete and it is not real closed.

**(g)** $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{Q} = 0$, and every extension of $\mathbb{Q}$ that is algebraic over $\mathbb{Q}$ has transcendence degree $0$ over $\mathbb{Q}$.

**Proof.** (a) is the universal property. (b) $\mathbb{Q}$ is the image of the countable set $\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})$. (c) $\sqrt2 \notin \mathbb{Q}$ by the classical parity argument. (d) The algebraic closure is constructed in *Algebraically Closed Fields*; $x^n - 2$ is irreducible over $\mathbb{Q}$ for every $n$ by Eisenstein, giving extensions of every degree. (e) A field of characteristic $0$ is perfect. (f) The ordering is unique by the theorem above; $\mathbb{Q}$ is Archimedean by *Ordered Fields*; incompleteness is the remark above. (g) An algebraic extension has transcendence degree $0$ over its base field, and $\mathbb{Q}$ is algebraic over itself. $\square$

**Remark (the place of $\mathbb{Q}$ among fields).** $\mathbb{Q}$ is the prime field of characteristic $0$ and the initial object among such fields; it is not algebraically closed, not real closed, and not order-complete. Its completions are $\mathbb{R}$ and the fields $\mathbb{Q}_p$, which are locally compact, while $\mathbb{Q}$ itself is not locally compact in the usual topology. The rationals are the field in which the arithmetic of $\mathbb{Z}$ becomes invertibility of the primes, and the two families of completions, together with the product formula, are the starting point of algebraic number theory.

---

## Extensions of $\mathbb{Q}$

### Finite Extensions

**Theorem.** Every finite extension of $\mathbb{Q}$ is separable and simple: it is of the form $\mathbb{Q}(\alpha)$ for some algebraic $\alpha$, and its degree is the degree of the minimal polynomial of $\alpha$.

**Proof.** Every field of characteristic $0$ is perfect, so every algebraic extension is separable, by *Splitting Fields and Algebraic Closure*; in characteristic $0$ every finite extension is simple by the theorem of the primitive element, since a finite separable extension is simple (*Field Extensions*). The degree statement is the definition of the minimal polynomial, from *Field Extensions*. $\square$

**Theorem.** The algebraic closure $\overline{\mathbb{Q}}$ is countable, and $[\overline{\mathbb{Q}}:\mathbb{Q}]$ is infinite: there are extensions of $\mathbb{Q}$ of every finite degree.

**Proof.** The polynomial $x^n - 2$ is irreducible over $\mathbb{Q}$ by Eisenstein's criterion at $2$, so $\mathbb{Q}(\sqrt[n]{2})$ has degree $n$; hence the degree of $\overline{\mathbb{Q}}$ exceeds every integer. For countability, $\overline{\mathbb{Q}}$ is the union of the splitting fields of countably many polynomials over $\mathbb{Q}$, each finite and hence countable, so the union is countable. $\square$

### Quadratic Fields

**Theorem.** The quadratic extensions of $\mathbb{Q}$, up to isomorphism, are the fields $\mathbb{Q}(\sqrt{d})$ for squarefree integers $d \neq 0, 1$, and

$$
\mathbb{Q}(\sqrt{d}) \cong \mathbb{Q}(\sqrt{d'}) \iff d/d' \in (\mathbb{Q}^\times)^2 .
$$

The square classes $\mathbb{Q}^\times/(\mathbb{Q}^\times)^2$ form a vector space over $\mathbb{F}_2$ with basis the class of $-1$ and the classes of the primes, so there are countably many quadratic extensions of $\mathbb{Q}$.

**Proof.** A quadratic extension is generated by an element $\alpha$ with $\alpha^2 = q \in \mathbb{Q}$, and writing $q$ with squarefree numerator and denominator gives $\mathbb{Q}(\alpha) = \mathbb{Q}(\sqrt d)$ for a squarefree integer $d$. The displayed equivalence follows because an isomorphism of quadratic fields must send $\sqrt d$ to an element whose square is $d$. The description of the square classes is the unit group computation $\mathbb{Q}^\times \cong \mathbb{Z}/2\mathbb{Z} \oplus \bigoplus_p \mathbb{Z}$ read modulo squares: the sign class gives $-1$ and each free generator gives the class of a prime. $\square$

### Cyclotomic Fields

**Theorem.** Let $\zeta_n$ be a primitive $n$-th root of unity. Then $\mathbb{Q}(\zeta_n)$ is the splitting field of $x^n - 1$ over $\mathbb{Q}$, it has degree $\varphi(n)$ over $\mathbb{Q}$, and

$$
\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times ,
$$

so $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is an abelian Galois extension. The cyclotomic fields, as $n$ varies, generate the maximal abelian extension of $\mathbb{Q}$: every finite abelian extension of $\mathbb{Q}$ is contained in some $\mathbb{Q}(\zeta_n)$, by the Kronecker–Weber theorem.

**Proof.** The roots of $x^n - 1$ are the powers of $\zeta_n$, so the field generated by $\zeta_n$ is the splitting field; an automorphism over $\mathbb{Q}$ is determined by $\zeta_n \mapsto \zeta_n^a$ with $\gcd(a,n) = 1$, giving the isomorphism onto $(\mathbb{Z}/n\mathbb{Z})^\times$, of order $\varphi(n)$; that the degree is exactly $\varphi(n)$ is the irreducibility of the cyclotomic polynomial, proved for prime $n$ by Eisenstein's criterion in *Unique Factorisation Domains*, and standard in general. Kronecker–Weber is a standard theorem of algebraic number theory, stated here for the structure of $\overline{\mathbb{Q}}$. $\square$

**Example (the splitting field of $x^3 - 2$).** The polynomial $x^3 - 2$ is irreducible over $\mathbb{Q}$, so $\mathbb{Q}(\sqrt[3]{2})$ has degree $3$; it is not a normal extension, because the other two roots are $\omega \sqrt[3]{2}$ and $\omega^2 \sqrt[3]{2}$ with $\omega = \zeta_3$ a primitive cube root of unity. The normal closure is $\mathbb{Q}(\sqrt[3]{2}, \omega)$, of degree $6$ over $\mathbb{Q}$, with Galois group $S_3$ acting on the three roots, as computed in *Galois Theory*.

---

## Endomorphisms and Derivations of $\mathbb{Q}$

**Theorem.** $\operatorname{End}(\mathbb{Q}) = \{\mathrm{id}\}$ and $\operatorname{Der}(\mathbb{Q}) = 0$: every unital ring endomorphism of $\mathbb{Q}$ is the identity, every derivation of $\mathbb{Q}$ into itself is zero, and the only non-unital ring homomorphisms $\mathbb{Q} \to \mathbb{Q}$ are the identity and the zero map.

**Proof.** A unital ring homomorphism $\varphi : \mathbb{Q} \to \mathbb{Q}$ has kernel an ideal, so either $0$ or $\mathbb{Q}$; the kernel is not $\mathbb{Q}$ because $\varphi(1) = 1 \neq 0$, so $\varphi$ is injective, whence $\varphi(n) = n$ for integers and $\varphi(a/b) = \varphi(a)\varphi(b)^{-1} = a/b$. Dropping the unital condition adds the zero map and nothing else, since every other homomorphism carries $1$ to an idempotent of $\mathbb{Q}$ and the only nonzero idempotent is $1$. For derivations, $D(1) = D(1 \cdot 1) = D(1) + D(1)$ gives $D(1) = 0$, so $D(n) = 0$ for all integers and $0 = D(1) = D(b \cdot \tfrac1b) = b D(\tfrac1b)$, whence $D(\tfrac1b) = 0$ and $D(\tfrac{a}{b}) = 0$. $\square$

**Corollary.** $\operatorname{Aut}(\mathbb{Q}) = 1$, in agreement with the rigidity of the prime field observed in *Ring and Field Automorphisms*; and $\mathbb{Q}$ carries no nonzero derivation, so the tangent-space intuitions of differential algebra are vacuous over the rationals.

---

## Completions and the Places of $\mathbb{Q}$

### Ostrowski and the Places

**Theorem (Ostrowski, restated from *Absolute Values, Valuations and Completions*).** Every nontrivial absolute value on $\mathbb{Q}$ is equivalent to the usual absolute value $\lvert \cdot \rvert_\infty$ or to one of the $p$-adic absolute values $\lvert \cdot \rvert_p$. Hence the places of $\mathbb{Q}$ are $\infty$ and the primes $p$.

**Corollary (the completions of $\mathbb{Q}$).** The nontrivial completions of $\mathbb{Q}$ are

$$
\widehat{\mathbb{Q}}_\infty = \mathbb{R}, \qquad \widehat{\mathbb{Q}}_p = \mathbb{Q}_p \ (p \text{ prime}),
$$

and no two of these are isomorphic: $\mathbb{R}$ is Archimedean and orderable, while each $\mathbb{Q}_p$ is not orderable, and $\mathbb{Q}_p \not\cong \mathbb{Q}_q$ for $p \neq q$ because the torsion subgroup of $\mathbb{Q}_p^\times$ is $\mu_{p-1}$, so two of these fields isomorphic as fields would force $p - 1 = q - 1$.

**Theorem (product formula).** For every $x \in \mathbb{Q}^\times$,

$$
\lvert x \rvert_\infty \prod_p \lvert x \rvert_p = 1 .
$$

**Proof.** Immediate from the prime factorization $x = \operatorname{sgn}(x)\prod_p p^{v_p(x)}$, as in *Absolute Values, Valuations and Completions*. $\square$

### The Local Structure

**Proposition.** For each prime $p$, the valuation ring of $\lvert \cdot \rvert_p$ on $\mathbb{Q}$ is the localization

$$
\mathbb{Z}_{(p)} = \left\{\frac{a}{b} : p \nmid b\right\} = \mathbb{Z}_S \ \text{with} \ S = \{\text{primes} \neq p\},
$$

with maximal ideal $p\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$; its completion is $\mathbb{Z}_p$. The field $\mathbb{Q}$ is recovered from each localization by inverting the remaining primes, and $\mathbb{Q}$ is the localization of $\mathbb{Z}$ at the multiplicative set of all nonzero integers.

**Proof.** The identification of the valuation ring is the previous section; the residue field and maximal ideal are computed from the valuation, and the completion statement is from *Absolute Values, Valuations and Completions*. $\square$

---

## Summary

$\mathbb{Q}$ is the field of fractions of $\mathbb{Z}$ and the prime field of characteristic $0$: it embeds as the smallest subfield in every field of characteristic $0$, its construction is the localization of $\mathbb{Z}$ at the nonzero integers, and it is characterised up to isomorphism as the unique field of characteristic $0$ with no proper subfield. It is countable, perfect, of characteristic $0$, and its only ideals are $0$ and $\mathbb{Q}$; its unit group is $\mathbb{Q}^\times \cong \mathbb{Z}/2\mathbb{Z} \oplus \bigoplus_p \mathbb{Z}$, the free abelian group on the primes modulo sign, by the fundamental theorem of arithmetic.

The ordering of $\mathbb{Q}$ is unique, Archimedean and dense, and makes $\mathbb{Q}$ the smallest ordered field; the order is not complete, and $\mathbb{Q}$ is neither real closed nor algebraically closed, with algebraic closure $\overline{\mathbb{Q}}$. Every subring of $\mathbb{Q}$ is a localization $\mathbb{Z}_S$ for a set of primes $S$, and the rings between $\mathbb{Z}$ and $\mathbb{Q}$ are exactly these localizations, with the $p$-localizations $\mathbb{Z}_{(p)}$ as valuation rings. Ostrowski's theorem gives the places of $\mathbb{Q}$ as the Archimedean place and the primes, the completions are $\mathbb{R}$ and the fields $\mathbb{Q}_p$, and the product formula holds over all places at once.

Every finite extension of $\mathbb{Q}$ is separable and simple, so it is $\mathbb{Q}(\alpha)$ for an algebraic $\alpha$; the algebraic closure $\overline{\mathbb{Q}}$ is countable and of infinite degree over $\mathbb{Q}$. The quadratic extensions are the fields $\mathbb{Q}(\sqrt d)$ for squarefree $d$, classified by the square classes $\mathbb{Q}^\times/(\mathbb{Q}^\times)^2$, and there are countably many of them; the cyclotomic fields $\mathbb{Q}(\zeta_n)$ are the abelian extensions generated by the roots of unity, with Galois group $(\mathbb{Z}/n\mathbb{Z})^\times$ and degree $\varphi(n)$, and by the Kronecker–Weber theorem they generate the maximal abelian extension of $\mathbb{Q}$. The field $\mathbb{Q}$ is rigid in the strongest sense: its only unital endomorphism is the identity, the only homomorphism of $\mathbb{Q}$ into itself that is not unital is the zero map, and its only derivation is zero.

| Property | Value for $\mathbb{Q}$ |
|---|---|
| Characteristic | $0$ |
| Prime field | itself |
| Cardinality | $\aleph_0$ |
| Orderings | exactly one, Archimedean, non-complete |
| Real closed | no |
| Algebraically closed | no; closure $\overline{\mathbb{Q}}$, countable |
| Unit group | $\mathbb{Z}/2 \oplus \bigoplus_p \mathbb{Z}$ |
| Subrings | localizations $\mathbb{Z}_S$ |
| Completions | $\mathbb{R}$, $\mathbb{Q}_p$ $(p$ prime$)$ |
| Automorphisms | $\operatorname{Aut}(\mathbb{Q}) = 1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$ | Integers |
| $\mathbb{Q} = \operatorname{Frac}(\mathbb{Z})$ | Rational numbers |
| $\mathbb{Q}^\times$ | Nonzero rationals |
| $v_p$ | $p$-adic valuation |
| $\lvert \cdot \rvert_p$, $\lvert \cdot \rvert_\infty$ | $p$-adic and usual absolute values |
| $\operatorname{sgn}(x)$ | Sign of a nonzero rational |
| $\mathbb{Z}_S$, $\mathbb{Z}_{(p)}$ | Localizations of $\mathbb{Z}$ |
| $\overline{\mathbb{Q}}$ | Algebraic numbers, the algebraic closure; $[\overline{\mathbb{Q}}:\mathbb{Q}]$ is infinite |
| $\mathbb{R}$, $\mathbb{Q}_p$ | The completions of $\mathbb{Q}$ |
| $\operatorname{tr.deg}$ | Transcendence degree |
| $\operatorname{Aut}(\mathbb{Q})$ | Automorphism group, trivial |
| $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ | Absolute Galois group of $\mathbb{Q}$ |
| $\operatorname{End}(\mathbb{Q})$, $\operatorname{Der}(\mathbb{Q})$ | Unital endomorphisms $\{\mathrm{id}\}$, all homomorphisms $\{0,\mathrm{id}\}$, derivations $0$ |
| $(a,b) \sim (c,d)$ | Equivalence relation defining $\mathbb{Q}$ |
| $(\mathbb{Q}^\times)^2$ | Squares, defining the square classes $\mathbb{Q}^\times/(\mathbb{Q}^\times)^2$ |
| $\mathbb{Q}(\sqrt d)$ | Quadratic field, $d$ squarefree |
| $\zeta_n$, $\varphi(n)$ | Primitive $n$-th root of unity, Euler function |
| $\mathbb{Q}(\zeta_n)$ | Cyclotomic field, Galois group $(\mathbb{Z}/n\mathbb{Z})^\times$ |

## Further Reading

- Edmund Landau, *Foundations of Analysis* (Chelsea, 1951), for the construction of the number systems beginning from the integers.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the prime field, the field of fractions and Ostrowski's theorem.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (Oxford University Press, 6th ed. 2008), for unique factorization and the arithmetic of $\mathbb{Q}$.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the places of $\mathbb{Q}$, the product formula and the beginnings of local arithmetic.
- Fernando Q. Gouvêa, *p-adic Numbers: An Introduction* (Springer, 2nd ed. 1997), for the completions of $\mathbb{Q}$ and their comparison with $\mathbb{R}$.
