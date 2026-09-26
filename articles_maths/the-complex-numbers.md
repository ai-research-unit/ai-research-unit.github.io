# __The Complex Numbers ($\mathbb{C}$)__

## Introduction

The complex numbers are the field obtained by adjoining to $\mathbb{R}$ a root of $x^2 + 1$: they are the quotient ring $\mathbb{R}[x]/(x^2+1)$, equivalently the quadratic extension $\mathbb{R}(i)$ with $i^2 = -1$. They are algebraically closed, so they contain a root of every nonconstant polynomial over themselves, and they are the algebraic closure of $\mathbb{R}$; at the same time they are not orderable, and they admit exactly one nontrivial automorphism fixing $\mathbb{R}$, namely conjugation. The tension between these two facts — algebraic completeness and the loss of order — is the formal content of the passage from $\mathbb{R}$ to $\mathbb{C}$.

This article constructs $\mathbb{C}$, records its field, order-theoretic and automorphism structure, develops conjugation and the norm, describes its roots of unity, and classifies it among algebraically closed fields by the Steinitz theorem. The fundamental theorem of algebra and the algebraic closedness of $\mathbb{C}$ are proved in *Real-Closed and Complete Ordered Fields* and *Algebraically Closed Fields* and are used here; the analytic theory of holomorphic functions on $\mathbb{C}$ belongs to the companion articles of categories 25–26, and only the algebraic and topological structure is developed here.

Throughout, $\mathbb{R}$ is the complete ordered field and $i$ is a fixed square root of $-1$. The quadratic form $N(z) = z\bar z$ is the norm of the quadratic extension $\mathbb{C}/\mathbb{R}$, in the sense of *Field Extensions*.

---

## Construction of $\mathbb{C}$

### As a Quotient Ring

**Theorem.** The polynomial $x^2 + 1$ is irreducible over $\mathbb{R}$, and the quotient

$$
\mathbb{C} = \mathbb{R}[x]/(x^2+1)
$$

is a field of characteristic $0$ and degree $2$ over $\mathbb{R}$. Writing $i$ for the class of $x$, every element has a unique expression

$$
z = a + bi, \qquad a, b \in \mathbb{R}, \qquad i^2 = -1,
$$

and the field operations are

$$
(a + bi) + (c + di) = (a+c) + (b+d)i, \qquad (a+bi)(c+di) = (ac - bd) + (ad + bc)i .
$$

**Proof.** $x^2 + 1$ has no real root and has degree $2$, so it is irreducible; the quotient of a ring by an irreducible polynomial is a field, by *Fields*. The normal form $a + bi$ is the division algorithm in $\mathbb{R}[x]$ modulo $x^2+1$, and the multiplication formula is the reduction of the product using $i^2 = -1$. The characteristic is that of $\mathbb{R}$, namely $0$. $\square$

**Corollary.** $\mathbb{C}$ is a splitting field of $x^2 + 1$ over $\mathbb{R}$, and $\{1, i\}$ is a basis of $\mathbb{C}$ as an $\mathbb{R}$-vector space; the theory of that vector-space structure belongs to *Vector Spaces*, and only the basis and the degree $[\mathbb{C}:\mathbb{R}] = 2$ are used here.

### Embeddings and the Prime Field

**Theorem.** The map $\mathbb{R} \to \mathbb{C}$, $a \mapsto a + 0i$, is an injective field homomorphism whose image is a real-closed subfield of $\mathbb{C}$, and

$$
\mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C}
$$

is a chain of fields above the prime field: $\mathbb{Q}$ is the prime field of both $\mathbb{R}$ and $\mathbb{C}$.

**Proof.** The map is a unital ring homomorphism, and its kernel is an ideal of the field $\mathbb{R}$, hence either $0$ or $\mathbb{R}$; it is not $\mathbb{R}$ because $1$ maps to $1 \neq 0$ in $\mathbb{C}$, so the kernel is $0$ and the map is injective. The image is isomorphic to $\mathbb{R}$, hence real closed. The prime field of $\mathbb{C}$ is the image of the unique ring homomorphism from $\mathbb{Z}$, which is $\mathbb{Q}$ because the characteristic is $0$, by *The Rational Numbers*. $\square$

**Corollary.** $\mathbb{C}$ is not isomorphic to $\mathbb{R}$ as a field: $\mathbb{C}$ contains a square root of $-1$ and $\mathbb{R}$ does not, and $\mathbb{C}$ is algebraically closed whereas $\mathbb{R}$ is not.

**Remark.** The quotient displayed above is written $\mathbb{R}[x]/(x^2+1)$, with $x$ an indeterminate and its class renamed $i$; and $\mathbb{C}$ is also the Clifford algebra $\mathrm{Cl}_{0,1}$ of the one-dimensional negative definite quadratic form, viewed as an algebra over $\mathbb{R}$. The Clifford-algebraic description of the number systems is developed in *The Number Systems as Clifford Algebras*; this article uses only the field structure of $\mathbb{C}$ and the quadratic extension $\mathbb{C}/\mathbb{R}$.

---

## The Field Structure

### Algebraic Closedness

**Theorem (fundamental theorem of algebra).** $\mathbb{C}$ is algebraically closed: every nonconstant polynomial in $\mathbb{C}[x]$ has a root in $\mathbb{C}$.

**Proof.** $\mathbb{R}$ is real closed by *Real-Closed and Complete Ordered Fields*, and for a real-closed field $F$ the field $F(i)$ is algebraically closed, as proved in that article and in *Algebraically Closed Fields*. Taking $F = \mathbb{R}$ gives $\mathbb{C} = \mathbb{R}(i)$ algebraically closed. $\square$

**Corollary.** $\mathbb{C}$ is the algebraic closure of $\mathbb{R}$, and $[\mathbb{C}:\mathbb{R}] = 2$; every algebraic extension of $\mathbb{R}$ is $\mathbb{R}$ or $\mathbb{C}$.

**Corollary.** Every polynomial of degree $n \geq 1$ over $\mathbb{C}$ factors into $n$ linear factors, counted with multiplicity, and in particular $\mathbb{C}$ is its own algebraic closure.

### Order-Theoretic Properties

**Theorem.** $\mathbb{C}$ admits no ordering, and it is not real closed.

**Proof.** If $\mathbb{C}$ were ordered, then $i^2 = -1$ would be a square, hence $\geq 0$, while $1 > 0$ in any ordered field and therefore $-1 < 0$; a contradiction. Hence $\mathbb{C}$ is not formally real, and a real-closed field is by definition formally real and orderable, so $\mathbb{C}$ is not real closed. $\square$

**Corollary.** The two properties of $\mathbb{R}$ that fail for $\mathbb{C}$ are orderability and real closedness, and the two properties of $\mathbb{C}$ that fail for $\mathbb{R}$ are algebraic closedness and the existence of a square root of $-1$. The passage from $\mathbb{R}$ to $\mathbb{C}$ trades order for algebraic closure, irreversibly.

---

## Conjugation and the Norm

### Conjugation

**Definition.** The **complex conjugate** of $z = a + bi$ is

$$
\bar z = a - bi .
$$

**Proposition.** Conjugation is an automorphism of $\mathbb{C}$ with $\overline{\bar z} = z$, it is the identity exactly on $\mathbb{R}$, and it satisfies

$$
\overline{z + w} = \bar z + \bar w, \qquad \overline{zw} = \bar z\, \bar w, \qquad \overline{z^{-1}} = \bar z^{-1}
$$

for $z \neq 0$. It is the unique nontrivial $\mathbb{R}$-automorphism of $\mathbb{C}$:

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = \operatorname{Gal}(\mathbb{C}/\mathbb{R}) \cong \mathbb{Z}/2\mathbb{Z}.
$$

**Proof.** The identities are immediate from the multiplication formula. An $\mathbb{R}$-automorphism $\sigma$ satisfies $\sigma(i)^2 = \sigma(-1) = -1$, so $\sigma(i) = \pm i$, and $\sigma$ is determined by $\sigma(i)$ because $\{1,i\}$ is an $\mathbb{R}$-basis; hence there are at most two, and conjugation is a nontrivial one. $\square$

**Definition.** An element $z \in \mathbb{C}$ is **real** if $\bar z = z$ and **imaginary** if $\bar z = -z$; write

$$
\operatorname{Re}(z) = \tfrac12(z + \bar z), \qquad \operatorname{Im}(z) = \tfrac{1}{2i}(z - \bar z),
$$

so that $\mathbb{R}$ is the fixed field of conjugation, $\operatorname{Im}(z) \in \mathbb{R}$ for every $z$, and the map $z \mapsto \operatorname{Im}(z)\, i = \tfrac12(z - \bar z)$ has image the subspace $i\mathbb{R}$ of purely imaginary elements.

### The Norm and Polar Decomposition

**Definition.** The **norm** of $z = a + bi$ is

$$
N(z) = z\bar z = a^2 + b^2 \in \mathbb{R}_{\geq 0},
$$

and the **absolute value** is $\lvert z \rvert = \sqrt{N(z)}$.

**Theorem.** The norm is multiplicative and positive definite:

$$
N(zw) = N(z)N(w), \qquad N(z) > 0 \text{ for } z \neq 0, \qquad N(z) = 0 \iff z = 0 .
$$

Moreover $\mathbb{C}$ is a field with an absolute value $\lvert \cdot \rvert$, complete for the induced metric, and it is locally compact in the topology.

**Proof.** Multiplicativity follows from $N(zw) = zw \overline{zw} = zw\bar z \bar w = (z\bar z)(w\bar w)$, using that $\mathbb{R}$ is central. Positivity and nondegeneracy are the corresponding facts for sums of two squares in $\mathbb{R}$. The absolute value satisfies the axioms of *Absolute Values, Valuations and Completions*, and completeness is the completeness of $\mathbb{R}^2$ for the Euclidean metric, established in *The Real Numbers*. $\square$

**Corollary (polar decomposition).** Every $z \neq 0$ is uniquely $z = r\zeta$ with $r = \lvert z \rvert > 0$ and $\lvert \zeta \rvert = 1$, giving an isomorphism of topological groups

$$
\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1), \qquad z \mapsto (\lvert z \rvert,\ z/\lvert z \rvert),
$$

where $U(1) = \{z : \lvert z \rvert = 1\}$ is the **unit circle**.

**Proof.** Existence and uniqueness of the decomposition are immediate from $\lvert z/\lvert z \rvert \rvert = 1$ and the positivity of $r$; multiplicativity of the norm shows the map is a group homomorphism with inverse $(r, \zeta) \mapsto r\zeta$, and both maps are continuous. $\square$

### Norm and Trace of the Quadratic Extension

**Theorem.** For $z \in \mathbb{C}$ the **trace** $T(z) = z + \bar z = 2\operatorname{Re}(z)$ and the norm $N(z) = z\bar z$ are elements of $\mathbb{R}$, and if $z \notin \mathbb{R}$ then the minimal polynomial of $z$ over $\mathbb{R}$ is

$$
x^2 - T(z)x + N(z) = (x - z)(x - \bar z) .
$$

In particular every element of $\mathbb{C} \setminus \mathbb{R}$ is the root of a unique monic quadratic over $\mathbb{R}$, and $\mathbb{C}/\mathbb{R}$ is a separable quadratic extension with exactly one nontrivial automorphism, as befits a Galois extension of degree $2$.

**Proof.** The displayed polynomial has the two roots $z$ and $\bar z$, distinct because $z \notin \mathbb{R}$, and coefficients $T(z), N(z) \in \mathbb{R}$; it is irreducible over $\mathbb{R}$ by the absence of real roots and degree $2$, hence it is the minimal polynomial. Normality and separability are from *Galois Theory*, and the group is computed above. $\square$

---

## Automorphisms of $\mathbb{C}$

### The Relative Automorphisms

**Theorem.** $\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = \{\mathrm{id}, \text{conjugation}\} \cong \mathbb{Z}/2\mathbb{Z}$, and the fixed field of conjugation is $\mathbb{R}$; hence $\mathbb{C}/\mathbb{R}$ is a Galois extension of degree $2$ with Galois group $\mathbb{Z}/2\mathbb{Z}$.

**Proof.** Computed above; the fixed field of an order-$2$ subgroup has index $2$ by the fundamental theorem of *Galois Theory*, and it contains $\mathbb{R}$ and is not all of $\mathbb{C}$, so it equals $\mathbb{R}$. $\square$

### The Absolute Automorphisms

**Theorem.** As a field, $\mathbb{C}$ has uncountably many automorphisms: the group $\operatorname{Aut}(\mathbb{C})$ has cardinality

$$
\lvert \operatorname{Aut}(\mathbb{C}) \rvert = 2^{2^{\aleph_0}} .
$$

Every automorphism of $\mathbb{C}$ fixes $\mathbb{Q}$ and preserves the set of algebraic numbers, but not every automorphism preserves $\mathbb{R}$; the only continuous automorphisms are the identity and conjugation, and hence the only $\mathbb{R}$-algebra automorphisms are those two.

**Proof sketch.** Any $\sigma \in \operatorname{Aut}(\mathbb{C})$ fixes $\mathbb{Q}$ and permutes the algebraic numbers $\overline{\mathbb{Q}}$, since it carries roots of a polynomial over $\mathbb{Q}$ to roots of the same polynomial. The group is large: a transcendence basis of $\mathbb{C}$ over $\overline{\mathbb{Q}}$ has cardinality $2^{\aleph_0}$, and the associated field is the function field in $2^{\aleph_0}$ indeterminates over $\overline{\mathbb{Q}}$, whose automorphism group is already large; the extension of these automorphisms to $\mathbb{C}$ gives the stated cardinality. A continuous automorphism is the identity on $\mathbb{Q}$ and hence, by continuity, on the closure $\mathbb{R}$, so it is an $\mathbb{R}$-automorphism and equals the identity or conjugation. $\square$

**Remark.** The existence of discontinuous automorphisms of $\mathbb{C}$ uses the axiom of choice, through the choice of a transcendence basis and the extension of its permutations; without the axiom of choice it is consistent that every automorphism of $\mathbb{C}$ is continuous, and hence that the identity and conjugation are the only automorphisms. This is why the arithmetic of $\mathbb{C}$ is studied through the topological field structure and through the Galois theory of $\overline{\mathbb{Q}}$, rather than through $\operatorname{Aut}(\mathbb{C})$; the absolute Galois group $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ is the object of *Ring and Field Automorphisms* and of algebraic number theory.

---

## Roots of Unity and Cyclotomic Structure

**Definition.** For $n \geq 1$ let

$$
\mu_n = \{z \in \mathbb{C} : z^n = 1\}, \qquad \mu = \bigcup_{n \geq 1} \mu_n .
$$

**Theorem.** For each $n$, $\mu_n$ is a cyclic subgroup of $\mathbb{C}^\times$ of order $n$, generated by any element of order $n$, that is, by any **primitive $n$-th root of unity**. The groups form a directed system under divisibility, and

$$
\mu \cong \mathbb{Q}/\mathbb{Z}
$$

as abstract groups. The elements of $\mu$ are exactly the roots of unity, and for each $n$ the field $\mathbb{Q}(\mu_n) = \mathbb{Q}(\zeta_n)$ is the cyclotomic field, with Galois group $(\mathbb{Z}/n\mathbb{Z})^\times$, as in *Galois Theory*.

**Proof.** The polynomial $x^n - 1$ has at most $n$ roots in a field, and it has exactly $n$ distinct roots in $\mathbb{C}$ because its derivative $nx^{n-1}$ vanishes only at $0$, so the roots are simple; the set of roots is closed under multiplication and inversion, so it is a finite subgroup of $\mathbb{C}^\times$, and a finite subgroup of the multiplicative group of a field is cyclic. For the isomorphism, fix a compatible system of primitive roots, that is, elements $\zeta_n$ of order $n$ with $\zeta_m^{m/n} = \zeta_n$ whenever $n \mid m$; such a system exists because the transition maps $\mu_m \to \mu_n$ are surjective and the groups are finite, so the inverse limit of the system is nonempty. Then $a/n \mapsto \zeta_n^a$ is well defined and is an isomorphism $\mathbb{Q}/\mathbb{Z} \to \mu$: if $a/n = b/n'$ then reducing to a common multiple $m$ of $n$ and $n'$ shows $\zeta_n^a = \zeta_m^{a m/n} = \zeta_m^{b m/n'} = \zeta_{n'}^b$, and injectivity follows because the orders range over all divisors of the denominators. $\square$

**Corollary.** $\mathbb{C}$ contains a primitive $n$-th root of unity for every $n$, and it contains a subfield isomorphic to every cyclotomic field; since $\mathbb{C}$ is algebraically closed, it contains a subfield isomorphic to every algebraic extension of $\mathbb{Q}$.

---

## The Gaussian Integers

### The Ring $\mathbb{Z}[i]$ and Its Norm

**Definition.** The **Gaussian integers** are the subring

$$
\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\} \subseteq \mathbb{C},
$$

with the **norm** $N(a+bi) = a^2 + b^2 = (a+bi)(a-bi)$.

**Proposition.** $\mathbb{Z}[i]$ is a subring of $\mathbb{C}$ and an integral domain; its field of fractions is $\mathbb{Q}(i)$; its group of units is $\{\pm 1, \pm i\}$; and the norm is multiplicative and positive definite.

**Proof.** Closure under the ring operations is immediate from the addition and multiplication formulas for $\mathbb{C}$, and the norm is the restriction of $z \mapsto z\bar z$, which is multiplicative and vanishes only at $0$; hence there are no zero divisors. Every quotient lies in $\mathbb{Q}(i)$, since

$$
\frac{a+bi}{c+di} = \frac{(a+bi)(c-di)}{c^2+d^2} \in \mathbb{Q}(i) \quad (c+di \neq 0),
$$

so $\operatorname{Frac}(\mathbb{Z}[i]) \subseteq \mathbb{Q}(i)$; conversely $\mathbb{Q} \subseteq \operatorname{Frac}(\mathbb{Z}[i])$ and $i \in \operatorname{Frac}(\mathbb{Z}[i])$, so $\mathbb{Q}(i) \subseteq \operatorname{Frac}(\mathbb{Z}[i])$. Finally $x$ is a unit if and only if $N(x) = 1$, since $xu = 1$ gives $N(x)N(u) = 1$ with both norms nonnegative integers; $a^2 + b^2 = 1$ has the solutions $(\pm1,0), (0,\pm1)$. $\square$

### Euclidean Structure

**Theorem.** $\mathbb{Z}[i]$ is a Euclidean domain for the norm $N$, hence a principal ideal domain and a unique factorization domain.

**Proof.** Let $z, w \in \mathbb{Z}[i]$ with $w \neq 0$. Then $z/w = z\bar w/N(w)$ has rational coordinates, since $\bar w \in \mathbb{Z}[i]$ and $N(w) \in \mathbb{Z}\setminus\{0\}$; choose integers $m, n$ with

$$
\lvert \operatorname{Re}(z/w) - m \rvert \leq \tfrac12, \qquad \lvert \operatorname{Im}(z/w) - n \rvert \leq \tfrac12,
$$

and set $q = m + ni \in \mathbb{Z}[i]$. Then

$$
N(z/w - q) = \left(\operatorname{Re}(z/w) - m\right)^2 + \left(\operatorname{Im}(z/w) - n\right)^2 \leq \tfrac14 + \tfrac14 = \tfrac12 < 1,
$$

so for $r = z - qw$ we get $N(r) = N(w)N(z/w - q) < N(w)$. This is the Euclidean division property, and the consequences are those of *Euclidean Domains*. $\square$

**Corollary (the primes of $\mathbb{Z}[i]$).** Let $p$ be a rational prime. If $p \equiv 3 \pmod 4$ then $p$ remains prime in $\mathbb{Z}[i]$; if $p \equiv 1 \pmod 4$ then $p$ splits as $p = \pi\bar\pi$ with $\pi$ and $\bar\pi$ nonassociate primes; and $2 = -i(1+i)^2$ ramifies.

**Proof.** If $p$ were not prime in $\mathbb{Z}[i]$ then $p = xy$ with $N(x), N(y) > 1$, so $p^2 = N(x)N(y)$ forces $N(x) = N(y) = p$, giving $p = a^2 + b^2$; this is impossible for $p \equiv 3 \pmod 4$, since squares are $0$ or $1$ modulo $4$ and $a^2 + b^2 \equiv 3 \pmod 4$ has no solution. For $p \equiv 1 \pmod 4$ the congruence $m^2 \equiv -1 \pmod p$ is soluble, so $p \mid (m+i)(m-i)$ while $p$ divides neither factor in $\mathbb{Z}[i]$ (as $p \nmid m$ and $p \nmid 1$), and since $\mathbb{Z}[i]$ is a unique factorization domain, $p$ admits a nontrivial factorization $p = \pi\bar\pi$ with $N(\pi) = p$. Finally $(1+i)^2 = 2i$ gives $2 = -i(1+i)^2$. $\square$

**Theorem (Fermat).** A positive integer $n$ is a sum of two squares of integers if and only if every prime $p \equiv 3 \pmod 4$ occurs in the prime factorization of $n$ with an even exponent.

**Proof.** By the description of the primes of $\mathbb{Z}[i]$, an element $n \in \mathbb{Z}$ is a norm $N(z)$ for some $z \in \mathbb{Z}[i]$ exactly when the primes $p \equiv 3 \pmod 4$ dividing $n$ divide it to an even power: such primes stay prime and their exponents in $N(z)$ are twice their exponents in $z$, while the primes $p \equiv 1 \pmod 4$ and the prime $2$ are norms of elements and can be distributed arbitrarily. The norm of $z = a + bi$ is $a^2 + b^2$. $\square$

**Remark.** $\mathbb{Z}[i]$ is the ring of integers of the quadratic field $\mathbb{Q}(i)$, and the example shows the general mechanism by which arithmetic in a number field controls representations of integers by quadratic forms; quadratic form theory in this corpus is developed in category 14, and the use made here is only to exhibit $\mathbb{Z}[i]$ as a Euclidean domain inside $\mathbb{C}$.

---

## The Automorphism Group of $\mathbb{C}(t)$

**Definition.** $\mathbb{C}(t) = \operatorname{Frac}(\mathbb{C}[t])$ is the rational function field in one variable over $\mathbb{C}$; it is a purely transcendental extension of $\mathbb{C}$ of transcendence degree $1$.

**Theorem.** Every $\mathbb{C}$-automorphism of $\mathbb{C}(t)$ is induced by a fractional linear substitution,

$$
t \mapsto \frac{at + b}{ct + d}, \qquad ad - bc \neq 0,
$$

and the assignment of an automorphism to its matrix is an isomorphism

$$
\operatorname{Aut}(\mathbb{C}(t)/\mathbb{C}) \cong \operatorname{PGL}_2(\mathbb{C}) = \operatorname{GL}_2(\mathbb{C})/\mathbb{C}^\times .
$$

**Proof sketch.** A $\mathbb{C}$-automorphism $\sigma$ is determined by $u = \sigma(t)$, since it fixes $\mathbb{C}$; the element $u$ must generate $\mathbb{C}(t)$ over $\mathbb{C}$ (otherwise $\sigma$ is not surjective), and conversely any generator defines an automorphism. The generators of $\mathbb{C}(t)$ over $\mathbb{C}$ are exactly the elements $(at+b)/(ct+d)$ with nonzero determinant, which is a classical theorem of Lüroth type; every such substitution is an automorphism because it has an inverse of the same shape, given by the inverse matrix. Composition of substitutions corresponds to multiplication of matrices, and two matrices with the same image differ by a scalar, giving the quotient $\operatorname{PGL}_2(\mathbb{C})$. $\square$

**Corollary.** $\operatorname{PGL}_2(\mathbb{C})$ acts on the projective line $\mathbb{C} \cup \{\infty\}$ by the displayed substitutions, and its finite subgroups are the cyclic, dihedral, tetrahedral, octahedral and icosahedral groups; for the finite group generated by $t \mapsto \zeta_n t$ with $\zeta_n$ a primitive $n$-th root of unity, the fixed field is $\mathbb{C}(t^n)$, since $\mathbb{C}(t)/\mathbb{C}(t^n)$ is a Galois extension of degree $n$ with that group.

**Remark.** The rational function field is not algebraically closed and not real closed, and it carries the $t$-adic valuation whose completion is the field $\mathbb{C}((t))$ of *Absolute Values, Valuations and Completions*. Its algebraic closure $\overline{\mathbb{C}(t)}$ has cardinality $2^{\aleph_0}$, hence transcendence degree $2^{\aleph_0}$ over $\mathbb{Q}$, so by the Steinitz classification it is isomorphic as an abstract field to $\mathbb{C}$; the isomorphism does not preserve the subfield $\mathbb{C}(t)$, the derivation $\tfrac{d}{dt}$ or the topology, and the Galois theory of $\overline{\mathbb{C}(t)}/\mathbb{C}(t)$ is the theory of the absolute Galois group of a rational function field.

---

## Classification and Cardinality

**Theorem.** The complex field has the following properties.

**(a)** $\lvert \mathbb{C} \rvert = 2^{\aleph_0}$ and $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{C} = 2^{\aleph_0}$.

**(b)** $\mathbb{C}$ is the completion of the algebraic numbers $\overline{\mathbb{Q}}$ for the usual absolute value, and $\mathbb{C}$ is the unique algebraically closed field of characteristic $0$ and cardinality $2^{\aleph_0}$ up to isomorphism.

**(c)** $\mathbb{C}$ is isomorphic, as an abstract field, to the completed algebraic closure $\mathbb{C}_p$ of $\mathbb{Q}_p$ for every prime $p$; the isomorphism is not continuous and does not respect the valuations.

**(d)** $\mathbb{C}$ is connected and locally compact as a topological field, and it is not isomorphic, as a topological field, to any $\mathbb{Q}_p$ or to $\mathbb{R}$.

**Proof.** (a) $\mathbb{C} = \mathbb{R}^2$ in the basis $\{1,i\}$, so it has the cardinality of $\mathbb{R}$; the transcendence degree is computed by cardinality as in *Algebraically Closed Fields*. (b) $\overline{\mathbb{Q}}$ is countable and contained in $\mathbb{C}$, and the completion of a countable dense subfield of $\mathbb{C}$ is $\mathbb{C}$; the uniqueness is the Steinitz classification, which for uncountable cardinals classifies algebraically closed fields of fixed characteristic by cardinality. (c) $\mathbb{C}_p$ is algebraically closed of characteristic $0$ and cardinality $2^{\aleph_0}$, so it falls in the same Steinitz class. (d) Connectedness and local compactness are the corresponding properties of $\mathbb{R}^2$; the non-isomorphism with $\mathbb{Q}_p$ follows from $\mathbb{C}$ being algebraically closed while $\mathbb{Q}_p$ is not, and the non-isomorphism with $\mathbb{R}$ from $\mathbb{C}$ being non-orderable while $\mathbb{R}$ is ordered, orderability being a property of the field structure that a field isomorphism would carry from $\mathbb{R}$ to $\mathbb{C}$. $\square$

**Remark (what the classification does and does not see).** The Steinitz theorem is a statement about the field structure alone, and it says that all algebraically closed fields of characteristic $0$ and cardinality $2^{\aleph_0}$ look alike. The distinctions that matter in arithmetic and analysis — completeness, the absolute value, the topology, the order for $\mathbb{R}$ — are not visible to the field structure of an algebraically closed field, which is why $\mathbb{C}$ and $\mathbb{C}_p$ are isomorphic as fields and belong to different subjects as valued fields. The complex numbers are in this sense the canonical algebraically closed field of characteristic $0$ of continuum cardinality, and their use in the corpus is as that canonical object together with its conjugation, its norm and its topology.

---

## Summary

$\mathbb{C} = \mathbb{R}[x]/(x^2+1) = \mathbb{R}(i)$ is the quadratic extension of $\mathbb{R}$ obtained by adjoining a square root of $-1$, with $\{1,i\}$ as an $\mathbb{R}$-basis, characteristic $0$ and prime field $\mathbb{Q}$. It is algebraically closed, by the fundamental theorem of algebra, and is the algebraic closure of $\mathbb{R}$, with no proper algebraic extension and with every polynomial of degree $n$ factorising into $n$ linear factors. It admits no ordering, being non-formally-real because $-1 = i^2$ is a square, and it is therefore not real closed; the passage from $\mathbb{R}$ to $\mathbb{C}$ trades orderability for algebraic closedness.

Conjugation $z \mapsto \bar z$ is the unique nontrivial $\mathbb{R}$-automorphism, with $\operatorname{Gal}(\mathbb{C}/\mathbb{R}) \cong \mathbb{Z}/2\mathbb{Z}$ and fixed field $\mathbb{R}$; the norm $N(z) = z\bar z$ is multiplicative and positive definite, and $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$. Every element outside $\mathbb{R}$ has minimal polynomial $x^2 - T(z)x + N(z)$ over $\mathbb{R}$. The roots of unity form the group $\mu \cong \mathbb{Q}/\mathbb{Z}$, and $\mathbb{C}$ contains every cyclotomic field and every algebraic extension of $\mathbb{Q}$. As a field, $\mathbb{C}$ has $2^{2^{\aleph_0}}$ automorphisms, of which only the identity and conjugation are continuous; it is the unique algebraically closed field of characteristic $0$ and cardinality $2^{\aleph_0}$ up to isomorphism, and it is isomorphic as an abstract field, but not as a topological or valued field, to the completed algebraic closure of $\mathbb{Q}_p$.

Inside $\mathbb{C}$ the Gaussian integers $\mathbb{Z}[i]$ form a Euclidean domain for the norm $a^2+b^2$, hence a unique factorization domain; this yields the description of the primes of $\mathbb{Z}[i]$, with $p \equiv 3 \pmod 4$ inert, $p \equiv 1 \pmod 4$ split and $2$ ramified, and gives Fermat's criterion for an integer to be a sum of two squares. The rational function field $\mathbb{C}(t)$ has automorphism group $\operatorname{Aut}(\mathbb{C}(t)/\mathbb{C}) \cong \operatorname{PGL}_2(\mathbb{C})$ acting by fractional linear substitutions, with finite subgroups the cyclic, dihedral and polyhedral groups, and $\mathbb{C}(t)$ is an example of a field that is neither algebraically closed nor real closed but whose algebraic closure is, as an abstract field, isomorphic to $\mathbb{C}$.

| Property | Value for $\mathbb{C}$ |
|---|---|
| Construction | $\mathbb{R}[x]/(x^2+1) = \mathbb{R}(i)$ |
| Degree over $\mathbb{R}$ | $2$ |
| Characteristic, prime field | $0$, $\mathbb{Q}$ |
| Algebraically closed | yes; algebraic closure of $\mathbb{R}$ |
| Orderable | no |
| Real closed | no |
| Cardinality | $2^{\aleph_0}$ |
| $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{C}$ | $2^{\aleph_0}$ |
| $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$ | $\mathbb{Z}/2\mathbb{Z}$ |
| $\operatorname{Aut}(\mathbb{C})$ | $2^{2^{\aleph_0}}$; only id and conjugation continuous |
| Roots of unity | $\mu \cong \mathbb{Q}/\mathbb{Z}$ |
| Norm | $N(z) = z\bar z$, multiplicative |
| Subring $\mathbb{Z}[i]$ | Gaussian integers, Euclidean, UFD |
| Function field $\mathbb{C}(t)$ | $\operatorname{Aut}(\mathbb{C}(t)/\mathbb{C}) \cong \operatorname{PGL}_2(\mathbb{C})$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex numbers |
| $i$ | Fixed square root of $-1$ |
| $a + bi$ | Normal form |
| $\bar z$ | Complex conjugate |
| $\operatorname{Re}(z)$, $\operatorname{Im}(z)$ | Real and imaginary parts |
| $N(z) = z\bar z$ | Norm (squared modulus) |
| $\lvert z \rvert = \sqrt{N(z)}$ | Absolute value |
| $T(z) = z + \bar z$ | Trace of the quadratic extension |
| $U(1)$ | Unit circle $\{z : \lvert z \rvert = 1\}$ |
| $\mu_n$, $\mu$ | $n$-th roots of unity, all roots of unity |
| $\operatorname{Gal}(\mathbb{C}/\mathbb{R})$ | $\mathbb{Z}/2\mathbb{Z}$ |
| $\operatorname{Aut}(\mathbb{C})$ | Full automorphism group, of cardinality $2^{2^{\aleph_0}}$ |
| $\overline{\mathbb{Q}}$, $\mathbb{C}_p$ | Algebraic numbers; completed algebraic closure of $\mathbb{Q}_p$ |
| $\operatorname{Frac}$ | Field of fractions, $\operatorname{Frac}(\mathbb{Z}[i]) = \mathbb{Q}(i)$ |
| $\operatorname{tr.deg}$ | Transcendence degree |
| $\mathbb{Z}[i]$ | Gaussian integers, norm $N(a+bi) = a^2+b^2$ |
| $\mathrm{Cl}_{0,1}$ | Clifford algebra isomorphic to $\mathbb{C}$ |
| $\mathbb{C}(t)$ | Rational function field; $\operatorname{Aut}(\mathbb{C}(t)/\mathbb{C}) \cong \operatorname{PGL}_2(\mathbb{C})$ |
| $\operatorname{PGL}_2(\mathbb{C})$ | $\operatorname{GL}_2(\mathbb{C})/\mathbb{C}^\times$, fractional linear substitutions |

## Further Reading

- Carl Friedrich Gauss, *Demonstratio nova theorematis omnem functionem algebraicam rationalem integram unius variabilis in factores reales primi vel secundi gradus resolvi posse* (Helmstedt, 1799), for the first substantial proof of the fundamental theorem of algebra.
- Reinhold Remmert, *Theory of Complex Functions* (Springer, 1991), for the analytic theory of $\mathbb{C}$ and the analytic proof of the fundamental theorem.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for $\mathbb{C}$ as the algebraic closure of $\mathbb{R}$ and for the classification of algebraically closed fields.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for Galois theory over $\mathbb{R}$ and the structure of $\mathbb{C}/\mathbb{R}$.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the field structure, conjugation and the norm.
- Robert M. Solovay, "A model of set-theory in which every set of reals is Lebesgue measurable", *Annals of Mathematics* 92 (1970), for the consistency of the statement that every automorphism of $\mathbb{C}$ is continuous.
