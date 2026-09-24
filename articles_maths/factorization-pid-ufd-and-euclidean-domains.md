# __Factorization: PID, UFD and Euclidean Domains__

## Introduction

Divisibility in a ring is not a single notion but a chain of increasingly strong hypotheses. The integers admit a Euclidean algorithm, hence their ideals are principal, hence every element factors into primes in exactly one way. Each of these properties can be isolated, and the classes of **Euclidean domains**, **principal ideal domains** and **unique factorization domains** are the result. This article studies them in that order of strength, proves the resulting strict chain

$$
\text{Euclidean domains} \subsetneq \text{principal ideal domains} \subsetneq \text{unique factorization domains} \subsetneq \text{integral domains},
$$

and develops the two tools, the Euclidean algorithm and Gauss's lemma, that make the theory effective.

Throughout, $R$ is an integral domain, as fixed in *Units, Zero Divisors and Integral Domains*: a commutative ring with $1 \neq 0$ and no zero divisors, so that cancellation holds and the equivalence of divisibility with association is available. Units, associates and the unit group $R^\times$ are used without restatement.

**Remark on the letter $N$.** Following *Rings*, §19, the **Euclidean degree function** of a Euclidean domain is written $N$. This $N$ is unrelated to the norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ of the quaternion and biquaternion articles; where both could occur, the context names the object.

---

## Divisibility

### Associates and the Divisibility Preorder

For $a, b \in R$, write $a \mid b$ if $b = ac$ for some $c \in R$. The relation is reflexive and transitive, so it is a preorder; it is not antisymmetric because $a \mid b$ and $b \mid a$ hold exactly for associates $a \sim b$, by the proposition on associates in *Units, Zero Divisors and Integral Domains*. Divisibility is therefore a partial order on the set of associate classes.

**Proposition.** Let $a, b, c \in R$ and let $u \in R^\times$.

**(a)** $u \mid a$ for every $a$, and $a \mid 0$ for every $a$.

**(b)** $a \mid b$ if and only if $(b) \subseteq (a)$.

**(c)** $a \sim b$ if and only if $(a) = (b)$, if and only if $a \mid b$ and $b \mid a$.

**(d)** If $a \mid b$ and $a \mid c$ then $a \mid (b x + c y)$ for all $x, y \in R$.

**Proof.** (a) $a = u(u^{-1}a)$ and $0 = a \cdot 0$. (b) $b = ac$ means $b \in (a)$, and $(b) \subseteq (a)$. (c) The first equivalence is the previous proposition together with (b); the second is its statement there. (d) Immediate from the definition. $\square$

Thus the divisibility theory of $R$ is the inclusion theory of its principal ideals. This is the observation that turns divisibility into commutative algebra.

### Irreducibles and Primes

Recall from *Rings*, §18 the two notions:

**Definition.** A nonzero non-unit $a \in R$ is

**(a)** **irreducible** if $a = bc$ always has $b$ or $c$ a unit;

**(b)** **prime** if $a \mid bc$ always implies $a \mid b$ or $a \mid c$.

**Proposition.** In an integral domain every prime element is irreducible.

**Proof.** Let $p$ be prime and $p = bc$. Since $p \mid bc = p$, primality gives $p \mid b$ or $p \mid c$; say $b = pd$. Then $p = pdc$, and cancellation of $p \neq 0$ gives $dc = 1$, so $c$ is a unit. Hence $p$ is irreducible. $\square$

The converse is the first genuinely arithmetic obstruction.

**Example (irreducible but not prime).** Let $R = \mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$ and let $N(a + b\sqrt{-5}) = a^2 + 5b^2$, which is multiplicative: $N(xy) = N(x)N(y)$.

- The units are the elements of norm $1$, so $R^\times = \{\pm 1\}$.
- $2$ is irreducible: if $2 = xy$ with both non-units, then $4 = N(x)N(y)$ with $N(x), N(y) > 1$, so $N(x) = N(y) = 2$; but $a^2 + 5b^2 = 2$ has no solution in integers.
- $2$ is not prime: it divides $(1+\sqrt{-5})(1-\sqrt{-5}) = 6$, while $1 \pm \sqrt{-5}$ is not divisible by $2$, since $2$ does not divide either coefficient.

The same argument shows that $3$ is irreducible and not prime, and that $1 \pm \sqrt{-5}$ are irreducible of norm $6$. Hence in $R$,

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

are two factorizations into irreducibles that differ neither by order nor by units. So $\mathbb{Z}[\sqrt{-5}]$ has no unique factorization, and it is the standard witness that an integral domain need not be a UFD. The ring $\mathbb{Z}[\sqrt{-5}]$ is the full ring of integers of $\mathbb{Q}(\sqrt{-5})$, since $-5 \equiv 3 \pmod 4$.

### Greatest Common Divisors

**Definition.** Let $a, b \in R$, not both zero. An element $d \in R$ is a **greatest common divisor** of $a$ and $b$ if $d \mid a$, $d \mid b$, and every common divisor of $a$ and $b$ divides $d$. A **least common multiple** $m$ is defined dually: $a \mid m$, $b \mid m$, and $m$ divides every common multiple.

**Proposition.** In an integral domain, a greatest common divisor, when it exists, is unique up to associates; the same holds for a least common multiple.

**Proof.** If $d$ and $d'$ are both greatest common divisors, then $d \mid d'$ and $d' \mid d$, so $d \sim d'$. $\square$

**Remark.** A greatest common divisor need not exist. In $\mathbb{Z}[\sqrt{-5}]$ the elements $6$ and $2(1+\sqrt{-5})$ have $2$ and $1+\sqrt{-5}$ as common divisors, of norm $4$ and $6$; neither of these divides the other. No common divisor is divisible by both: the divisors of $6$ are $\pm 1, \pm 2, \pm 3, \pm 6, \pm(1 \pm \sqrt{-5})$ up to units, and the only ones divisible by both $2$ and $1+\sqrt{-5}$ are the associates of $6$, while $6 \nmid 2(1+\sqrt{-5})$, since $N(6) = 36$ does not divide $N(2(1+\sqrt{-5})) = 24$. Existence of greatest common divisors for all pairs is one of the properties that a UFD supplies.

---

## Principal Ideal Domains

### Definition and Ideal Structure

**Definition.** An integral domain $R$ is a **principal ideal domain** (PID) if every ideal of $R$ is principal, that is, $I = (a)$ for some $a \in R$.

**Examples.** $\mathbb{Z}$ is a PID, since every subgroup of $(\mathbb{Z},+)$ is generated by its least positive element. For a field $F$, the polynomial ring $F[x]$ is a PID, since it carries a division algorithm with degree. $\mathbb{Z}[i]$ is a PID, as shown in the section on Euclidean domains. The polynomial rings $\mathbb{Z}[x]$ and $F[x,y]$ are **not** PIDs: in $\mathbb{Z}[x]$ the ideal $(2, x)$ is not principal, because a generator would divide both $2$ and $x$, hence be a unit, and $(2,x) \neq \mathbb{Z}[x]$.

**Proposition.** In a PID, a nonzero element $a$ is irreducible if and only if the ideal $(a)$ is maximal; consequently in a PID every irreducible element is prime.

**Proof.** Let $a$ be irreducible and suppose $(a) \subseteq I \subseteq R$ with $I = (b)$ principal. Then $a = bc$ for some $c$. Since $a$ is irreducible, either $b$ is a unit, in which case $I = R$, or $c$ is a unit, in which case $a \sim b$ and $I = (a)$. Hence $(a)$ is maximal. Conversely if $(a)$ is maximal and $a = bc$, then $(a) \subseteq (b)$; maximality forces $(b) = (a)$ or $(b) = R$, so $b \sim a$ or $b$ is a unit, and $a$ is irreducible. A maximal ideal is prime by *Rings*, §6, and $(a)$ prime means $a$ is prime. $\square$

**Corollary.** A PID is a UFD, in the sense that every nonzero non-unit factors into irreducibles and the factorization is unique.

**Proof.** Existence holds by the ascending chain argument given below; uniqueness holds because irreducibles are prime, and the uniqueness argument for products of primes is given in the section on unique factorization domains. $\square$

### Bézout's Identity and Coprimality

**Definition.** Elements $a, b \in R$ are **coprime** (or **relatively prime**) if $1$ is a greatest common divisor of $a$ and $b$; equivalently, if the only common divisors are units.

**Theorem (Bézout).** Let $R$ be a PID and $a, b \in R$. Then $a$ and $b$ have a greatest common divisor $d$, and $d = ax + by$ for some $x, y \in R$. In particular $a$ and $b$ are coprime if and only if the ideal $(a, b)$ is all of $R$.

**Proof.** The ideal $(a) + (b) = \{ax + by\}$ is principal, say $(d)$. Then $a, b \in (d)$, so $d \mid a$ and $d \mid b$. If $c \mid a$ and $c \mid b$, then $c$ divides every element of $(d)$ and in particular $d$. So $d$ is a greatest common divisor, and it is a linear combination of $a$ and $b$ by construction. Finally $(a,b) = (d) = R$ if and only if $d$ is a unit. $\square$

**Corollary.** Let $p$ be irreducible in a PID and $a, b \in R$. If $p \mid ab$ then $p \mid a$ or $p \mid b$. If $p \nmid a$ then there exist $x, y$ with $ax + py = 1$.

### Ascending Chains

**Definition.** $R$ satisfies the **ascending chain condition on principal ideals** (ACCP) if there is no infinite strictly increasing chain

$$
(a_1) \subsetneq (a_2) \subsetneq (a_3) \subsetneq \cdots
$$

of principal ideals.

**Proposition.** A PID satisfies ACCP.

**Proof.** Given a chain $(a_1) \subseteq (a_2) \subseteq \cdots$, the union $U = \bigcup_n (a_n)$ is an ideal: it is closed under addition since two elements lie in a common $(a_n)$ by the chain condition, and it is closed under multiplication by $R$. Since $R$ is a PID, $U = (c)$ for some $c$, and $c \in (a_n)$ for some $n$; then $(c) \subseteq (a_n) \subseteq U = (c)$, so the chain is constant from $n$ on. $\square$

---

## Unique Factorization Domains

### Definition

**Definition.** An integral domain $R$ is a **unique factorization domain** (UFD) if

**(a)** every nonzero non-unit of $R$ is a product of irreducible elements, and

**(b)** this factorization is unique up to order and multiplication by units: if

$$
a = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s
$$

with all $p_i, q_j$ irreducible, then $r = s$ and, after reordering, $p_i \sim q_i$ for all $i$.

**Examples.** $\mathbb{Z}$ is a UFD by the fundamental theorem of arithmetic. Every PID is a UFD (below). For a field $F$, the ring $F[x]$ is a UFD, since it is Euclidean. $\mathbb{Z}[x]$ is a UFD by Gauss's lemma, although it is not a PID. The domain $\mathbb{Z}[\sqrt{-5}]$ is not a UFD, by the example above.

### Prime versus Irreducible

**Proposition.** A UFD has no irreducible element that is not prime; conversely, a domain in which every irreducible is prime and in which factorizations exist has unique factorization.

**Proof.** Suppose $p$ is irreducible in a UFD and $p \mid ab$, so $ab = pc$. Factor $a$, $b$, $c$ into irreducibles. The two factorizations of $ab$ and of $pc$ agree up to order and units, so $p$ is an associate of one of the irreducible factors of $a$ or of $b$; hence $p \mid a$ or $p \mid b$. For the converse, suppose $p_1 \cdots p_r = q_1 \cdots q_s$ with all factors irreducible and all prime. Since $p_1$ is prime and divides the right-hand product, $p_1 \mid q_j$ for some $j$; as $q_j$ is irreducible and $p_1$ is not a unit, $p_1 \sim q_j$. Cancel $p_1$ using cancellation in the domain and repeat. $\square$

### The Criterion

**Theorem.** An integral domain $R$ is a UFD if and only if $R$ satisfies ACCP and every irreducible element of $R$ is prime.

**Proof.** If $R$ is a UFD then ACCP holds, since a strictly increasing chain $(a_1) \subsetneq (a_2) \subsetneq \cdots$ would give $a_{n} = a_{n+1} b_n$ with $b_n$ a non-unit, and factorizations of $a_1$ would refine forever, contradicting finiteness of $r$ in the definition; and irreducibles are prime by the proposition.

Conversely, suppose $R$ has ACCP and every irreducible is prime. First, every nonzero non-unit $a$ has a factorization: if not, then $a$ is not irreducible, an irreducible element being its own factorization, so $a = a_1 b_1$ with both factors non-units. A factorization of both factors would multiply to one of $a$, so at least one of them has none, and after relabelling it is $a_1$; this $a_1$ is again a nonzero non-unit with no factorization, and $(a) \subsetneq (a_1)$, because $b_1$ is a non-unit and $a \neq 0$. Repeating the argument with $a_1$ in place of $a$ produces a strictly increasing chain $(a) \subsetneq (a_1) \subsetneq (a_2) \subsetneq \cdots$, contradicting ACCP. Hence factorizations exist, and uniqueness follows by the previous proposition. $\square$

**Corollary.** Every PID is a UFD.

**Proof.** A PID satisfies ACCP, and by the proposition on maximal ideals its irreducibles are prime. $\square$

**Corollary.** In a UFD, any two elements not both zero have a greatest common divisor, namely the product of the primes occurring in both factorizations, each to the smaller exponent.

**Proof.** The product described divides both elements; and any common divisor has a factorization whose prime factors occur in both, with exponents no larger than the smaller exponent. $\square$

The second corollary shows that in a PID the abstract Bézout identity and the concrete prime-exponent formula compute the same $d$. Bézout's identity is stronger, since it also exhibits $d$ as a linear combination; that stronger conclusion is exactly what fails in a general UFD.

---

## Euclidean Domains

### Definition

**Definition.** An integral domain $R$ is a **Euclidean domain** if there is a function

$$
N : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}
$$

such that for all $a, b \in R$ with $b \neq 0$ there exist $q, r \in R$ with

$$
a = q b + r, \qquad r = 0 \text{ or } N(r) < N(b).
$$

The element $q$ is the **quotient** and $r$ the **remainder**. The function $N$ is a **Euclidean degree function**; it need not be multiplicative.

**Examples.** $R = \mathbb{Z}$ with $N(a) = \lvert a \rvert$; $R = F[x]$ with $N(f) = \deg f$; $R = \mathbb{Z}[i]$ with $N(a+bi) = a^2 + b^2$; $R = \mathbb{Z}[\sqrt{2}]$ with $N(a + b\sqrt2) = \lvert a^2 - 2b^2 \rvert$; the Eisenstein integers $\mathbb{Z}[\omega]$ with $\omega = e^{2\pi i/3}$ and $N(a + b\omega) = a^2 - ab + b^2$. Each is Euclidean with the stated function; the case of $\mathbb{Z}[i]$ is proved below.

### Euclidean Implies PID

**Theorem.** Every Euclidean domain is a principal ideal domain.

**Proof.** Let $I$ be a nonzero ideal of the Euclidean domain $R$ and choose $b \in I \setminus \{0\}$ with $N(b)$ minimal. For any $a \in I$, divide: $a = qb + r$ with $r = 0$ or $N(r) < N(b)$. Since $r = a - qb \in I$, the second alternative contradicts the minimality of $N(b)$; hence $r = 0$ and $a \in (b)$. Therefore $I = (b)$. $\square$

The same division also yields the **Euclidean algorithm**: for $a, b \neq 0$, the sequence $r_0 = a$, $r_1 = b$, $r_{k+1}$ the remainder of $r_{k-1}$ on division by $r_k$ has strictly decreasing values $N(r_k)$, so it must terminate at $r_m = 0$. Then $r_{m-1}$ is a greatest common divisor of $a$ and $b$, since the common divisors are preserved at each step. Running the algorithm backwards expresses $r_{m-1}$ as a linear combination of $a$ and $b$, giving Bézout's identity constructively.

**Corollary.** Every Euclidean domain is a UFD.

**Proof.** A Euclidean domain is a PID, and a PID is a UFD. $\square$

### The Euclidean Algorithm in the Gaussian Integers

**Theorem.** The Gaussian integers $\mathbb{Z}[i]$ form a Euclidean domain with $N(a + bi) = a^2 + b^2$.

**Proof.** Let $z, w \in \mathbb{Z}[i]$ with $w \neq 0$. In the field $\mathbb{Q}(i)$ write $z/w = s + ti$ with $s, t \in \mathbb{Q}$. Choose integers $q_1, q_2$ with $\lvert s - q_1 \rvert \leq \tfrac{1}{2}$ and $\lvert t - q_2 \rvert \leq \tfrac{1}{2}$, and set $q = q_1 + q_2 i \in \mathbb{Z}[i]$. Then

$$
N(z/w - q) = (s - q_1)^2 + (t - q_2)^2 \leq \tfrac{1}{4} + \tfrac{1}{4} = \tfrac{1}{2} < 1.
$$

Multiplying by the multiplicative function $N$, with $r = z - qw$,

$$
N(r) = N(w)\, N(z/w - q) < N(w),
$$

so $z = qw + r$ is a division with $N(r) < N(w)$. $\square$

**Example.** In $\mathbb{Z}[i]$ one has

$$
2 = -i\,(1+i)^2, \qquad 5 = (2+i)(2-i),
$$

and the two factors $2 + i$ and $2 - i$ are not associates, since a unit multiple of $2+i$ is one of $\pm(2+i)$ or $\pm i(2+i) = \pm(-1 + 2i)$, and none equals $2 - i$. Thus $2$ is a unit times the square of the irreducible $1+i$ (this is **ramification**), while the rational prime $5$ splits into two distinct conjugate irreducibles. The general rule is that a rational prime $p$ is a sum of two squares, hence reducible in $\mathbb{Z}[i]$, exactly when $p = 2$ or $p \equiv 1 \pmod 4$; for $p \equiv 3 \pmod 4$ the element $p$ remains irreducible, because no integer solution of $a^2 + b^2 = p$ exists.

### A PID That Is Not Euclidean

**Theorem (Motzkin).** The ring of integers of $\mathbb{Q}(\sqrt{-19})$, namely $\mathbb{Z}\bigl[\tfrac{1+\sqrt{-19}}{2}\bigr]$, is a principal ideal domain but admits no Euclidean degree function.

This is the standard example showing that the first inclusion above is strict; its verification uses the ideal class group and a norm argument and is cited here as a theorem of the literature.

---

## Polynomial Rings and Gauss's Lemma

### Content and Primitive Polynomials

Let $R$ be a UFD and let $F = \operatorname{Frac}(R)$ be its fraction field, as constructed in *Localization and the Fraction Field*. For a nonzero $f = a_n x^n + \cdots + a_0 \in R[x]$, the **content** $c(f)$ is a greatest common divisor of the nonzero coefficients $a_0, \ldots, a_n$; it is defined up to associates, and we fix a representative. The polynomial $f$ is **primitive** if $c(f) \sim 1$.

**Lemma.** Every nonzero $f \in R[x]$ can be written $f = c(f) f_0$ with $f_0 \in R[x]$ primitive.

**Proof.** Divide the coefficients by their greatest common divisor. $\square$

### Gauss's Lemma

**Theorem (Gauss's lemma).** Let $R$ be a UFD and $F = \operatorname{Frac}(R)$. Then:

**(a)** For nonzero $f, g \in R[x]$, $\ c(fg) \sim c(f) c(g)$. In particular the product of two primitive polynomials is primitive.

**(b)** If $f \in R[x]$ is primitive, then $f$ is irreducible in $R[x]$ if and only if $f$ is irreducible in $F[x]$.

**Proof sketch.** (a) Reduce coefficients modulo a prime element $p$ of $R$: if $f$ is primitive then some coefficient is not divisible by $p$, so $\bar f \neq 0$ in $(R/pR)[x]$, and similarly for $g$; since $R/pR$ is an integral domain, $\bar f \bar g \neq 0$, so $fg$ has a coefficient not divisible by $p$. Hence no prime divides $c(fg)$ to a higher power than it divides $c(f)c(g)$, and the two contents are associates. (b) If $f = gh$ in $F[x]$, clear denominators to write $f = c \cdot g_0 h_0$ with $g_0, h_0 \in R[x]$ primitive and $c \in F$; by (a) $g_0 h_0$ is primitive, and comparing contents in $R[x]$ forces $c$ to be a unit of $R$, so $f$ factors in $R[x]$. The converse is immediate. $\square$

**Theorem.** If $R$ is a UFD then $R[x]$ is a UFD, with the units of $R$ as its units.

**Proof sketch.** Let $f \in R[x]$ be a nonzero non-unit and write $f = c(f) f_0$ with $f_0$ primitive. The content $c(f) \in R$ factors into irreducibles of $R$, which are irreducible in $R[x]$; and $f_0$ factors in $F[x]$ into irreducibles, which by Gauss's lemma lie in $R[x]$ up to units of $F$ and can be taken primitive in $R[x]$. Uniqueness is inherited from $F[x]$, which is Euclidean, together with the uniqueness of the content in $R$. $\square$

**Corollary.** $\mathbb{Z}[x]$ is a UFD, and it is not a PID, since $(2, x)$ is not principal.

**Corollary.** For a field $F$, the ring $F[x_1, \ldots, x_n]$ is a UFD, by induction on $n$, while it is a PID only for $n \leq 1$.

### Eisenstein's Criterion

**Theorem (Eisenstein's criterion).** Let $R$ be a UFD and let

$$
f = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_0 \in R[x]
$$

be primitive of positive degree. If there is a prime element $p \in R$ with

$$
p \nmid a_n, \qquad p \mid a_i \text{ for } 0 \leq i < n, \qquad p^2 \nmid a_0,
$$

then $f$ is irreducible in $R[x]$.

**Proof.** Suppose $f = gh$ with $g$ and $h$ non-units of $R[x]$. Since $f$ is primitive of positive degree, both factors have positive degree, so $\deg g + \deg h = n$. Reducing modulo $p$ gives $\bar f = \bar a_n x^n$ with $\bar a_n \neq 0$ in the domain $(R/pR)[x]$, so each of $\bar g$ and $\bar h$ is a monomial; since $\deg \bar g \leq \deg g$ and $\deg \bar h \leq \deg h$ while $\deg \bar g + \deg \bar h = n = \deg g + \deg h$, both degrees are positive. Hence the constant term of each of $g$ and $h$ is divisible by $p$, and $p^2 \mid g(0)h(0) = a_0$, contradicting the hypothesis. $\square$

**Examples.** The polynomial $x^3 - 2$ is irreducible in $\mathbb{Z}[x]$ by Eisenstein at $p = 2$, so $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$. The polynomial $x^4 + 1$ is irreducible in $\mathbb{Z}[x]$: apply Eisenstein at $p = 2$ to

$$
(x+1)^4 + 1 = x^4 + 4x^3 + 6x^2 + 4x + 2,
$$

which is Eisenstein, and irreducibility is preserved by the substitution $x \mapsto x+1$, since it is a ring automorphism of $\mathbb{Z}[x]$. Likewise, for a prime $p$ the cyclotomic polynomial

$$
\Phi_p(x) = \frac{x^p - 1}{x-1} = x^{p-1} + x^{p-2} + \cdots + x + 1
$$

is irreducible: applying Eisenstein at $p$ to $\Phi_p(x+1)$ gives coefficients $\binom{p}{k}$ divisible by $p$ for $1 \leq k \leq p-1$, leading coefficient $1$, and constant term $p$ with $p^2 \nmid p$. This irreducibility is used in *Galois Theory* to compute $[\mathbb{Q}(\zeta_p) : \mathbb{Q}] = p - 1$.

---

## The Hierarchy and Examples

| Implication | Strictness | Witness |
|---|---|---|
| Euclidean $\Rightarrow$ PID | strict | $\mathbb{Z}\bigl[\tfrac{1+\sqrt{-19}}{2}\bigr]$ is a PID, not Euclidean (Motzkin) |
| PID $\Rightarrow$ UFD | strict | $\mathbb{Z}[x]$ is a UFD, not a PID: $(2,x)$ is not principal |
| UFD $\Rightarrow$ integral domain | strict | $\mathbb{Z}[\sqrt{-5}]$ is a domain, not a UFD: $2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ |

The ring $\mathbb{Z}[\sqrt{-5}]$ fails both to be a UFD and to be a PID. Concretely, the ideal $(2, 1+\sqrt{-5})$ is not principal: if it were $(d)$ then $d$ would divide both generators, and $N(2) = 4$, $N(1+\sqrt{-5}) = 6$ force $N(d) \mid \gcd(4,6) = 2$; but no element of norm $2$ exists, and $d$ is not a unit, because the ideal is proper: an equation $2(a + b\sqrt{-5}) + (1+\sqrt{-5})(c + d\sqrt{-5}) = 1$ would force $2(a - b - 3d) = 1$ on comparing coordinates. So the ring is not a PID, and the presence of irreducible non-prime elements reflects that.

| Ring | Euclidean | PID | UFD | Domain |
|---|---|---|---|---|
| $\mathbb{Z}$ | yes | yes | yes | yes |
| $F[x]$, $F$ a field | yes | yes | yes | yes |
| $\mathbb{Z}[i]$ | yes | yes | yes | yes |
| $\mathbb{Z}[\sqrt2]$ | yes | yes | yes | yes |
| $\mathbb{F}_p[[x]]$ | yes | yes | yes | yes |
| $\mathbb{Z}[x]$ | no | no | yes | yes |
| $\mathbb{Z}[[x]]$ | no | no | yes | yes |
| $F[x,y]$ | no | no | yes | yes |
| $\mathbb{Z}\bigl[\tfrac{1+\sqrt{-19}}{2}\bigr]$ | no | yes | yes | yes |
| $\mathbb{Z}[\sqrt{-5}]$ | no | no | no | yes |
| $\mathbb{Z}[\sqrt{-3}]$ | no | no | no | yes |

The last row is instructive: $\mathbb{Z}[\sqrt{-3}]$ is not integrally closed (the element $\tfrac{1+\sqrt{-3}}{2}$ is integral over it but not in it), and it is not a UFD, whereas the full ring of integers $\mathbb{Z}[\omega]$ of $\mathbb{Q}(\sqrt{-3})$ is Euclidean. So passing to the integral closure can repair unique factorization; this is the beginning of the ideal-theoretic remedy, in which ideals rather than elements are factored, and it lies beyond the scope of this article.

---

## Summary

Divisibility in an integral domain is the inclusion of principal ideals, and the elements that cannot be factored further are the irreducibles; a prime element is one whose generated ideal is prime, and every prime is irreducible, while the converse can fail. A principal ideal domain is a domain in which every ideal is principal; there greatest common divisors exist and Bézout's identity holds, irreducible elements generate maximal ideals, and the ascending chain condition holds. A unique factorization domain is a domain in which every nonzero non-unit factors into irreducibles uniquely up to order and units; this is equivalent to the conjunction of ACCP and the primeness of every irreducible, and every PID is therefore a UFD.

A Euclidean domain is a domain with a division algorithm, and the division algorithm makes every ideal principal, so Euclidean domains form the smallest of the three classes. The chain of implications and its strictness are as tabulated above, the witnesses being $\mathbb{Z}[x]$ (UFD not PID), $\mathbb{Z}\bigl[\tfrac{1+\sqrt{-19}}{2}\bigr]$ (PID not Euclidean) and $\mathbb{Z}[\sqrt{-5}]$ (domain not UFD). Over a UFD, Gauss's lemma controls factorization in the polynomial ring: content is multiplicative, primitive polynomials are irreducible over the ring exactly when they are irreducible over the fraction field, and consequently $R[x]$ is a UFD whenever $R$ is. Eisenstein's criterion turns these observations into a practical irreducibility test.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Integral domain, unless stated otherwise |
| $R^\times$ | Group of units |
| $a \mid b$ | $a$ divides $b$ |
| $a \sim b$ | $a$ and $b$ are associates, $a = ub$ with $u \in R^\times$ |
| $(a)$ | Principal ideal generated by $a$ |
| $(a, b)$ | Ideal generated by $a$ and $b$ |
| $\gcd(a,b)$, $\operatorname{lcm}(a,b)$ | Greatest common divisor, least common multiple |
| $N$ | Euclidean degree function $R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$ |
| $c(f)$ | Content of a polynomial, a gcd of its coefficients |
| $F = \operatorname{Frac}(R)$ | Fraction field of $R$ |
| $\Phi_p(x)$ | Cyclotomic polynomial $x^{p-1} + \cdots + x + 1$ |
| ACCP | Ascending chain condition on principal ideals |
| PID, UFD | Principal ideal domain, unique factorization domain |
| $N(z) = a^2 + b^2$ for $z = a + bi$ | Multiplicative norm on $\mathbb{Z}[i]$ |
| $N(a + b\sqrt{-5}) = a^2 + 5b^2$ | Multiplicative norm on $\mathbb{Z}[\sqrt{-5}]$ |

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for divisibility, irreducibles and the Euclidean algorithm in examples.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the equivalence UFD $\Leftrightarrow$ ACCP plus prime irreducibles, and Gauss's lemma.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for Euclidean domains, norm-Euclidean fields and Eisenstein's criterion.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, rev. ed. 1974), for PIDs, Dedekind domains and the ideal-theoretic remedy for failure of unique factorization.
- T. Motzkin, "The Euclidean algorithm", *Bulletin of the American Mathematical Society* 55 (1949), for the PID that is not Euclidean.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for the arithmetic of quadratic rings such as $\mathbb{Z}[\sqrt{-5}]$ and $\mathbb{Z}[i]$.
