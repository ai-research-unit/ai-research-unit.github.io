
# __Modular Arithmetic and the Ring of Residues__

## Introduction

This is the second article of the Integers system in Part V, and it occupies the **applications slot** of that system. The system is the ring $\mathbb{Z}$ of *The Integers*, and the object of study is its arithmetic modulo a fixed positive integer: the congruence relation, the quotient ring $\mathbb{Z}/n\mathbb{Z}$, the group of units, and the classical theorems of Euler, Fermat and Wilson together with the solution of linear and quadratic congruences. Where the algebra slot of the system studied $\mathbb{Z}$ as an initial ring, a Euclidean domain and a unique factorisation domain, this article studies the quotients of $\mathbb{Z}$ and the arithmetic that they carry.

The system $\mathbb{Z}$ has no geometry and no analysis, and its applications are correspondingly arithmetic: the congruences are the whole of its applied content, and they are the origin of the finite rings and finite groups that occur throughout the corpus. The general theory of quotient rings, ideals and the first isomorphism theorem is from *Rings*, and the divisibility and factorisation theory of $\mathbb{Z}$ is from *The Integers* and *Unique Factorisation Domains*; the group-theoretic background, including the structure of finite abelian groups and the notion of a cyclic group, is from *Groups*. The quadratic reciprocity law is stated with a reference to the standard literature, and the analytic estimate of the distribution of the primes is not used.

Throughout, $n$ is a positive integer, $\mathbb{Z}/n\mathbb{Z}$ or $\mathbb{Z}_n$ is the ring of residues modulo $n$, and $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ is the field with $p$ elements for $p$ prime; the class of $a$ is written $\bar a$ or $a \bmod n$, and $a \equiv b \pmod n$ means that $n$ divides $a - b$. The group of units of $\mathbb{Z}/n\mathbb{Z}$ is written $(\mathbb{Z}/n\mathbb{Z})^\times$, $\varphi$ is the Euler function, $\operatorname{ord}_n(a)$ is the multiplicative order of $a$ modulo $n$, and $\left(\frac{a}{p}\right)$ is the Legendre symbol. The base is the commutative ring with identity throughout, and the specific rings here are finite and commutative.

## Congruences

### The Congruence Relation

**Definition.** For $a, b, n \in \mathbb{Z}$ with $n > 0$ one writes

$$
a \equiv b \pmod n \iff n \mid (a - b).
$$

**Theorem.** The congruence relation is an equivalence relation on $\mathbb{Z}$ whose classes are the **residue classes** modulo $n$, namely the $n$ sets

$$
\bar 0, \bar 1, \dots, \overline{n-1}, \qquad \bar k = \{k + mn : m \in \mathbb{Z}\}.
$$

It is compatible with addition and multiplication: if $a \equiv a'$ and $b \equiv b'$ modulo $n$, then $a + b \equiv a' + b'$ and $ab \equiv a'b'$ modulo $n$. Consequently the quotient $\mathbb{Z}/n\mathbb{Z}$ is a commutative ring with identity under

$$
\bar a + \bar b = \overline{a+b}, \qquad \bar a \cdot \bar b = \overline{ab}.
$$

**Proof.** The relation is the congruence modulo the ideal $(n)$, and the compatibility statements are the statements that $(n)$ is an ideal: if $n \mid (a-a')$ and $n \mid (b-b')$, then $n$ divides $(a+b)-(a'+b')$ and $ab - a'b' = a(b-b') + b'(a-a')$. The ring axioms are inherited from $\mathbb{Z}$ through the quotient. $\square$

**Theorem.** The canonical map $\pi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $\pi(a) = \bar a$, is a surjective ring homomorphism with kernel $(n)$, and $\mathbb{Z}/n\mathbb{Z}$ is characterised by the universal property of the quotient: for every ring $A$ with $n \cdot 1_A = 0$ there is a unique ring homomorphism $\mathbb{Z}/n\mathbb{Z} \to A$.

**Proof.** Surjectivity and the kernel are immediate from the division algorithm of *The Integers*, which shows that every class has a representative in $\{0, 1, \dots, n-1\}$. The universal property is the first isomorphism theorem of *Rings*. $\square$

**Example.** The ring $\mathbb{Z}/12\mathbb{Z}$ has twelve elements; the classes $\bar 0, \bar 3, \bar 4, \bar 6, \bar 8, \bar 9$ are zero divisors, and $\bar 1, \bar 5, \bar 7, \overline{11}$ are units. The sum of two classes is computed by adding representatives and reducing, the product likewise.

### Arithmetic Modulo Small Numbers

**Theorem.** In $\mathbb{Z}/n\mathbb{Z}$, an element $\bar a$ is a unit if and only if $\gcd(a, n) = 1$; it is a zero divisor if and only if $1 < \gcd(a,n) < n$, and it is nilpotent if and only if every prime dividing $n$ divides $a$.

**Proof.** If $\gcd(a,n) = 1$, Bézout gives $ua + vn = 1$, hence $\bar u \bar a = \bar 1$. Conversely if $\bar a \bar u = \bar 1$ then $n \mid (au - 1)$, so any common divisor of $a$ and $n$ divides $1$. For the zero divisor statement, if $d = \gcd(a,n)$ with $1 < d < n$, then $\bar a \cdot \overline{n/d} = \overline{0}$ with $\overline{n/d} \neq \bar 0$; conversely a zero divisor is not a unit, so $\gcd(a,n) > 1$, and it is not $n$ unless $\bar a = \bar 0$. The nilpotency statement follows by writing $n$ as a product of prime powers. $\square$

**Corollary.** For $n \geq 2$ the ring $\mathbb{Z}/n\mathbb{Z}$ is a field if and only if $n$ is prime, and it is an integral domain if and only if $n$ is prime; for $n$ composite it has zero divisors and is neither. In particular $\mathbb{F}_p$ is the field with $p$ elements, and every finite field of prime order arises this way.

**Proof.** Combine the preceding theorem with the criterion that a finite commutative ring with identity is a field exactly when its only ideals are $0$ and the whole ring, and with the primality criterion for the ideal $(n)$ of *The Integers*. $\square$

## The Structure of $\mathbb{Z}/n\mathbb{Z}$

### The Chinese Remainder Theorem

**Theorem (Chinese remainder).** If $m$ and $n$ are coprime positive integers, then the map

$$
\psi : \mathbb{Z}/mn\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}, \qquad \psi(\bar a) = (\bar a \bmod m, \bar a \bmod n),
$$

is an isomorphism of rings. More generally, for pairwise coprime $n_1, \dots, n_k$,

$$
\mathbb{Z}/n_1\cdots n_k\mathbb{Z} \cong \prod_{i=1}^{k} \mathbb{Z}/n_i\mathbb{Z}.
$$

**Proof.** The kernel of $\psi$ is the set of classes divisible by both $m$ and $n$, that is, by $mn$ since $m$ and $n$ are coprime; so $\psi$ is injective. The two rings have the same finite cardinality $mn$, so $\psi$ is bijective. The general case is induction. $\square$

**Corollary.** The group of units satisfies

$$
(\mathbb{Z}/mn\mathbb{Z})^\times \cong (\mathbb{Z}/m\mathbb{Z})^\times \times (\mathbb{Z}/n\mathbb{Z})^\times
$$

for coprime $m, n$, and the Euler function is multiplicative: $\varphi(mn) = \varphi(m)\varphi(n)$.

**Proof.** The isomorphism is the restriction of $\psi$ to units, since an element of a product of rings is a unit exactly when each component is; the multiplicativity of $\varphi$ is then the multiplicativity of the cardinality. $\square$

**Example.** $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$, and the class of $5$ corresponds to $(1, 2)$; the units of $\mathbb{Z}/6\mathbb{Z}$ are $\bar 1$ and $\bar 5$, corresponding to the pairs $(1,1)$ and $(1,2)$, which are exactly the elements of the product of the unit groups $\{1\} \subseteq \mathbb{Z}/2\mathbb{Z}$ and $\{1,2\} \subseteq \mathbb{Z}/3\mathbb{Z}$. The computation shows that the isomorphism of rings does not preserve the additive generator: the class $\bar 1$ corresponds to $(1,1)$, not to $(1,0)$.

### The Additive and Multiplicative Structure

**Theorem.** $(\mathbb{Z}/n\mathbb{Z}, +)$ is a cyclic group of order $n$, generated by $\bar 1$; it is isomorphic to the group $\mathbb{Z}/n\mathbb{Z}$ of the notation. $(\mathbb{Z}/n\mathbb{Z}, \cdot)$ is a commutative monoid with identity and zero, and its group of units has order $\varphi(n)$.

**Proof.** The classes $\bar 0, \bar 1, \dots, \overline{n-1}$ are the multiples of $\bar 1$; the order statements are then immediate. The units are counted by the preceding section. $\square$

**Theorem.** Let $n = p_1^{k_1}\cdots p_r^{k_r}$ be the prime factorisation of $n$. Then

$$
\mathbb{Z}/n\mathbb{Z} \cong \prod_{i=1}^{r} \mathbb{Z}/p_i^{k_i}\mathbb{Z}, \qquad (\mathbb{Z}/n\mathbb{Z})^\times \cong \prod_{i=1}^{r} (\mathbb{Z}/p_i^{k_i}\mathbb{Z})^\times,
$$

and $\varphi(n) = n \prod_{i=1}^{r}\left(1 - \frac{1}{p_i}\right) = \prod_i p_i^{k_i - 1}(p_i - 1)$.

**Proof.** The decomposition is the Chinese remainder theorem applied to the prime powers; the formula for $\varphi$ is the multiplicativity together with $\varphi(p^k) = p^{k-1}(p-1)$, obtained by counting the integers in $\{1, \dots, p^k\}$ not divisible by $p$. $\square$

**Theorem.** The group of units of $\mathbb{Z}/p^k\mathbb{Z}$ is cyclic for odd $p$; for $p = 2$ it is trivial for $k = 1$, of order $2$ for $k = 2$, and isomorphic to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2^{k-2}\mathbb{Z}$ for $k \geq 3$.

**Proof.** The result for odd $p$ is the existence of a primitive root modulo $p^k$: the group is cyclic of order $p^{k-1}(p-1)$, generated by a primitive root modulo $p$ lifted by Hensel's lemma. The powers of $2$ are the exceptional case, and the stated structure is the standard one; the argument is in *Groups* and in the references. $\square$

## The Group of Units

### Euler's Function

**Definition.** The **Euler function** $\varphi(n)$ is the number of integers in $\{1, \dots, n\}$ coprime to $n$; equivalently the order of $(\mathbb{Z}/n\mathbb{Z})^\times$.

**Theorem.** The Euler function satisfies

$$
\sum_{d \mid n} \varphi(d) = n,
$$

and it is the Dirichlet series coefficient determined by $\sum_{n \geq 1} \varphi(n)n^{-s} = \zeta(s-1)/\zeta(s)$ in the notation of *Combinatorial Functions and Generating Functions*.

**Proof.** Partition the integers $1, \dots, n$ by the value of $\gcd(k, n) = d$; the classes with gcd $d$ are in bijection with the integers $k/d$ coprime to $n/d$, of which there are $\varphi(n/d)$; summing over $d \mid n$ gives $\sum_{d\mid n}\varphi(n/d) = n$, which is the stated identity after reindexing. The Dirichlet series is the standard computation with Möbius inversion. $\square$

### Euler, Fermat and Wilson

**Theorem (Euler).** If $\gcd(a, n) = 1$ then

$$
a^{\varphi(n)} \equiv 1 \pmod n .
$$

**Proof.** Multiplication by $\bar a$ permutes the group $(\mathbb{Z}/n\mathbb{Z})^\times$, so $\prod_{u \in U} u = \prod_{u\in U} \bar a u = \bar a^{\varphi(n)} \prod_{u\in U} u$; cancelling the product, which is a unit, gives $\bar a^{\varphi(n)} = \bar 1$. $\square$

**Theorem (Fermat's little theorem).** If $p$ is prime then for every integer $a$,

$$
a^p \equiv a \pmod p,
$$

and if $p \nmid a$ then $a^{p-1} \equiv 1 \pmod p$.

**Proof.** The second statement is Euler's theorem with $\varphi(p) = p-1$; the first follows by multiplying by $a$ and noting that it also holds for $a \equiv 0$. $\square$

**Theorem (Wilson).** If $p$ is prime then $(p-1)! \equiv -1 \pmod p$.

**Proof.** In $\mathbb{F}_p$ the nonzero elements pair off into inverse pairs except for the self-inverse elements $\pm 1$, since the solutions of $x^2 = 1$ are $x = \pm 1$ in a field; multiplying all nonzero classes gives $\bar 1 \cdot (-\bar 1)$ times $\bar 1$ for each inverse pair, hence $-1$. $\square$

**Corollary.** The order $\operatorname{ord}_n(a)$ of a unit $a$ modulo $n$ divides $\varphi(n)$, and $a$ is a **primitive root** modulo $n$ exactly when its order is $\varphi(n)$. For $p$ prime the group $\mathbb{F}_p^\times$ is cyclic of order $p-1$.

**Proof.** Lagrange's theorem in the finite group $(\mathbb{Z}/n\mathbb{Z})^\times$ gives the divisibility; cyclicity of $\mathbb{F}_p^\times$ is the case $k = 1$ of the structure theorem above. $\square$

## Congruences and Their Solutions

### Linear Congruences

**Theorem.** The congruence $ax \equiv b \pmod n$ has a solution if and only if $d = \gcd(a,n)$ divides $b$, in which case it has exactly $d$ solutions modulo $n$, namely

$$
x \equiv x_0 + \frac{n}{d}\,t \pmod n, \qquad t = 0, 1, \dots, d-1,
$$

where $x_0 = u(b/d)$ for a Bézout coefficient $u$ with $ua + vn = d$.

**Proof.** The congruence is $n \mid (ax - b)$, so $d \mid b$ is necessary. If $d \mid b$, divide by $d$: the congruence $a'x \equiv b' \pmod{n'}$ with $a' = a/d$, $n' = n/d$ has $\gcd(a',n')=1$, so $x \equiv u b' \pmod{n'}$ by Bézout, and this class has exactly $d$ lifts modulo $n$. $\square$

**Corollary.** The congruence is solvable for every $b$ exactly when $a$ is a unit modulo $n$; in that case the solution is unique modulo $n$ and is $x \equiv a^{-1}b$.

### Quadratic Residues

**Definition.** For $p$ an odd prime and $p \nmid a$, the **Legendre symbol** is

$$
\left(\frac{a}{p}\right) = \begin{cases} 1, & a \text{ is a square modulo } p, \\ -1, & a \text{ is not a square modulo } p. \end{cases}
$$

A residue with symbol $1$ is a **quadratic residue**, one with symbol $-1$ a **quadratic non-residue**.

**Theorem (Euler's criterion).** For $p$ an odd prime and $p \nmid a$,

$$
\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod p .
$$

**Proof.** Fermat's little theorem gives $a^{p-1} = 1$, so $a^{(p-1)/2}$ is a root of $x^2 = 1$ in the field $\mathbb{F}_p$, hence is $\pm 1$. The squares are the even powers of a generator of the cyclic group $\mathbb{F}_p^\times$, and for them the exponent is a multiple of $p-1$, giving $1$; the nonsquares give $-1$. $\square$

**Corollary.** The Legendre symbol is multiplicative in $a$, and exactly half of the nonzero residues are quadratic residues.

**Theorem (quadratic reciprocity).** For distinct odd primes $p$ and $q$,

$$
\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}},
$$

and the supplementary laws are $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$ and $\left(\frac{2}{p}\right) = (-1)^{(p^2-1)/8}$.

**Proof.** The reciprocity law is Gauss's; the standard proof uses the Gaussian lemma and the counting of lattice points in a rectangle, and is given in the references. $\square$

**Corollary.** The congruence $x^2 \equiv a \pmod p$ is solvable exactly when $\left(\frac{a}{p}\right) = 1$, and the number of solutions is then $2$; the law of quadratic reciprocity makes the decidability of this question effective.

### Applications

**Theorem (divisibility tests).** In base $10$, an integer is divisible by $9$ exactly when the sum of its digits is, and by $11$ exactly when the alternating sum of its digits is.

**Proof.** Since $10 \equiv 1 \pmod 9$ and $10 \equiv -1 \pmod{11}$, the value of the decimal expansion $\sum a_i 10^i$ is congruent to $\sum a_i$ modulo $9$ and to $\sum (-1)^i a_i$ modulo $11$. $\square$

**Theorem (cancellation of periods).** If $\gcd(a, n) = 1$ then the sequence of powers $a, a^2, a^3, \dots$ modulo $n$ is periodic with period $\operatorname{ord}_n(a)$, and the period divides $\varphi(n)$; in particular the decimal expansion of $1/n$ is purely periodic of period $\operatorname{ord}_n(10)$ when $\gcd(10, n) = 1$.

**Proof.** The powers form the cyclic subgroup generated by $\bar a$ in the finite group $(\mathbb{Z}/n\mathbb{Z})^\times$, whose order is $\operatorname{ord}_n(a)$ and divides $\varphi(n)$ by Lagrange. The decimal statement is the division algorithm applied to the remainders, which repeat with the period of the powers of $10$. $\square$

## Polynomial Congruences and Hensel's Lemma

### Polynomials over $\mathbb{Z}/n\mathbb{Z}$

**Definition.** For $f \in \mathbb{Z}[x]$ and $n \geq 1$ the **polynomial congruence** $f(x) \equiv 0 \pmod n$ asks for the classes $\bar x \in \mathbb{Z}/n\mathbb{Z}$ with $f(\bar x) = \bar 0$ in the reduction of $f$ modulo $n$. The number of solutions is not a function of the degree: $x^2 \equiv 1 \pmod 8$ has the four solutions $1, 3, 5, 7$, and $x^2 \equiv 0 \pmod{p^k}$ has $p^{\lfloor k/2\rfloor}$ of them.

**Theorem (reduction to prime powers).** If $n = p_1^{k_1}\cdots p_r^{k_r}$, then the solutions of $f(x) \equiv 0 \pmod n$ are in bijection with the $r$-tuples of solutions modulo the $p_i^{k_i}$, under the Chinese remainder isomorphism. Consequently the counting of solutions reduces to the prime powers.

**Proof.** The Chinese remainder theorem identifies $\mathbb{Z}/n\mathbb{Z}$ with the product of the $\mathbb{Z}/p_i^{k_i}\mathbb{Z}$, and under a ring isomorphism the solutions of a polynomial equation correspond componentwise. $\square$

### Hensel's Lemma

**Theorem (Hensel).** Let $p$ be prime, $f \in \mathbb{Z}[x]$ and $r \in \mathbb{Z}$ with

$$
f(r) \equiv 0 \pmod p, \qquad f'(r) \not\equiv 0 \pmod p .
$$

Then for every $k \geq 1$ there is a unique $r_k \bmod p^k$ with $r_k \equiv r \pmod p$ and $f(r_k) \equiv 0 \pmod{p^k}$, and it is computed by the Newton iteration

$$
r_{k+1} = r_k - f(r_k)\, f'(r)^{-1} \pmod{p^{k+1}} .
$$

**Proof.** Suppose $r_k$ is a solution modulo $p^k$ and write $r_{k+1} = r_k + t p^k$. The Taylor expansion of the polynomial gives

$$
f(r_k + t p^k) \equiv f(r_k) + t p^k f'(r_k) \pmod{p^{2k}},
$$

and since $2k \geq k+1$, the congruence modulo $p^{k+1}$ is $f(r_k) + t p^k f'(r_k) \equiv 0$. Writing $f(r_k) = p^k s$ and using $f'(r_k) \equiv f'(r) \not\equiv 0 \pmod p$, the congruence becomes $s + t f'(r) \equiv 0 \pmod p$, which has the unique solution $t \equiv -s f'(r)^{-1} \pmod p$. The induction begins at $k = 1$ with $r_1 = r$. $\square$

**Corollary.** Let $p$ be odd and let $a$ be a quadratic residue modulo $p$ with $p \nmid a$. Then $x^2 \equiv a \pmod{p^k}$ has exactly two solutions for every $k$, obtained by lifting the two roots modulo $p$; more generally a simple root of a polynomial congruence lifts uniquely to every prime power.

**Proof.** For $f = x^2 - a$ and a root $r$ with $r^2 \equiv a \pmod p$ one has $f'(r) = 2r \not\equiv 0 \pmod p$ because $p$ is odd and $a \not\equiv 0$, so Hensel's lemma applies to each of the two roots $\pm r$; the two lifted solutions are distinct modulo $p$ and hence modulo every $p^k$. $\square$

**Example.** The lemma is sharp: for $f = x^2 - 1$ and $p = 2$ one has $f'(r) = 2r \equiv 0 \pmod 2$ for every $r$, and indeed $x^2 \equiv 1 \pmod{2^k}$ has one solution for $k=1$, two for $k=2$ and four for $k \geq 3$, namely $\pm 1$ and $\pm(1 + 2^{k-1})$. For $f = x^2$ the only root modulo $p$ is multiple, and the number of solutions modulo $p^k$ is $p^{\lfloor k/2\rfloor}$. Thus Hensel's lemma asserts exactly that the *simple* roots, and only they, lift uniquely.

### The $p$-adic Reading

**Theorem.** The $p$-adic integers $\mathbb{Z}_p$ are the inverse limit of the rings $\mathbb{Z}/p^k\mathbb{Z}$ along the reduction maps, and Hensel's lemma is the statement that every simple root in the residue field $\mathbb{F}_p$ is the reduction of a unique root in $\mathbb{Z}_p$.

**Proof.** An element of the inverse limit is a compatible sequence $(r_k)$ with $r_{k+1} \equiv r_k \pmod{p^k}$, which is exactly the output of the iteration of the lemma, and the uniqueness in the limit is the uniqueness at each finite level; the construction of $\mathbb{Z}_p$ is in *Absolute Values, Valuations and Completions*. $\square$

**Remark.** The lemma exhibits the arithmetic of the residues as a local theory: the solutions modulo $p$ control the solutions modulo every power of $p$, and the passage to the limit produces the $p$-adic integers, in which the congruence is an equality. The step from the finite rings $\mathbb{Z}/p^k\mathbb{Z}$ to their limit is the same limiting process that in the Archimedean place produces the real numbers, and the two completions are the two faces of the arithmetic of $\mathbb{Z}$.

## Summary

Congruence modulo $n$ is the equivalence relation $a \equiv b \pmod n \iff n \mid (a-b)$, compatible with addition and multiplication, and the quotient $\mathbb{Z}/n\mathbb{Z}$ is a commutative ring with identity whose elements are the classes $\bar 0, \dots, \overline{n-1}$; it is a field exactly when $n$ is prime, in which case it is $\mathbb{F}_p$. An element is a unit exactly when it is coprime to $n$, a zero divisor exactly when its gcd with $n$ is proper nontrivial, and the units form a group of order $\varphi(n)$. The Chinese remainder theorem identifies $\mathbb{Z}/mn\mathbb{Z}$ with $\mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ for coprime $m, n$, whence the multiplicativity of $\varphi$ and the decomposition of the rings and unit groups into their prime-power parts; $\varphi(n) = n\prod(1 - 1/p_i)$ and $\sum_{d\mid n}\varphi(d) = n$.

Euler's theorem states $a^{\varphi(n)} \equiv 1 \pmod n$ for units, Fermat's little theorem is its prime case $a^{p-1} \equiv 1 \pmod p$, and Wilson's theorem states $(p-1)! \equiv -1 \pmod p$. The order of a unit divides $\varphi(n)$, the group of units modulo an odd prime power is cyclic, and the multiplicative group of a finite prime field is cyclic. The linear congruence $ax \equiv b \pmod n$ is solvable exactly when $\gcd(a,n)$ divides $b$, with that many solutions, and the quadratic congruence $x^2 \equiv a \pmod p$ is governed by the Legendre symbol, Euler's criterion and the law of quadratic reciprocity. The arithmetic of the integers modulo $n$ is thus the whole applied content of the system $\mathbb{Z}$: it is the source of the finite rings and finite abelian groups of the corpus, and it is where the divisibility theory of the system becomes an effective calculus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a \equiv b \pmod n$ | $n \mid (a-b)$ |
| $\bar a$, $a \bmod n$ | Residue class of $a$ modulo $n$ |
| $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{Z}_n$ | Ring of residues modulo $n$ |
| $\mathbb{F}_p$ | Field $\mathbb{Z}/p\mathbb{Z}$, $p$ prime |
| $(\mathbb{Z}/n\mathbb{Z})^\times$ | Group of units modulo $n$ |
| $\varphi(n)$ | Euler function, order of the unit group |
| $\operatorname{ord}_n(a)$ | Multiplicative order of $a$ modulo $n$ |
| $\left(\frac{a}{p}\right)$ | Legendre symbol |
| $\pi$ | Canonical map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ |
| $\psi$ | Chinese remainder isomorphism |

## Further Reading

- Carl Friedrich Gauss, *Disquisitiones Arithmeticae* (Fleischer, 1801; English translation, Springer, 1986), for congruences, the group of units and quadratic reciprocity.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (Oxford University Press, 6th ed. 2008), for Euler's and Fermat's theorems, Wilson's theorem and the elementary theory of residues.
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (Springer, 2nd ed. 1990), for the structure of $(\mathbb{Z}/n\mathbb{Z})^\times$, primitive roots and quadratic reciprocity.
- Ivan Niven, Herbert S. Zuckerman and Hugh L. Montgomery, *An Introduction to the Theory of Numbers* (Wiley, 5th ed. 1991), for congruences, the Chinese remainder theorem and the solution of congruences.
- Neal Koblitz, *A Course in Number Theory and Cryptography* (Springer, 2nd ed. 1994), for the computational uses of modular arithmetic.
