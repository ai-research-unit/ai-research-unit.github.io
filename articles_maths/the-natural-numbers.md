
# __The Natural Numbers ($\mathbb{N}$)__

## Introduction

This is the first article of the Natural Numbers system in Part V, and it occupies the **algebra slot** of that system. The system is the semiring $(\mathbb{N}, +, \cdot, 0, 1)$ together with its order, and this article constructs it, establishes its universal property, records its arithmetic and its divisibility, and describes its place among the other systems. Everything about $\mathbb{N}$ that is algebraic follows from one construction: it is the free commutative semiring on no generators, the least inductive set, and the initial object in the category of commutative semirings with identity. It is the system in which addition and multiplication are defined by recursion and in which the induction principle is an algebraic law rather than a theorem about a larger structure.

This article carries out the construction from the Peano axioms and from the von Neumann ordinal $\omega$, establishes the recursion and induction theorems, develops the arithmetic and the order, and describes the divisibility structure, the cardinality and the embeddings into the later systems. The system supports an algebra slot and a special-functions slot and nothing else: there is no geometry of a line to develop, because $\mathbb{N}$ carries no compatible order-complete or metric structure of its own, and the arithmetic functions are not covered here. The model theory of the first-order theory of $\mathbb{N}$ is treated, and its computability theory; neither is used here.

Throughout, $\mathbb{N} = \{0,1,2,\dots\}$ is the set of natural numbers including $0$, the successor map is $S : \mathbb{N} \to \mathbb{N}$, and $\omega$ is the first infinite von Neumann ordinal. The standard reference structures for set theory, order and cardinality are *Set-Theoretic Foundations*, *Order Theory and Lattices* and *Cardinality and the Axiom of Choice*; divisibility and factorization are from *Unique Factorisation Domains*. The corpus's default base is the commutative ring; this article's base is the commutative **semiring** $\mathbb{N}$, which is not a ring, and every result below is stated for that base. No concept of analysis enters: $\mathbb{N}$ carries no compatible metric or order-completeness, and the systems $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ are reached by adjoining structure, not by a construction inside $\mathbb{N}$.

## The Construction of $\mathbb{N}$

### The Peano Axioms

**Definition.** A **Peano system** is a set $N$ with a distinguished element $0 \in N$ and a map $S : N \to N$, the **successor**, such that

**(P1)** $S$ is injective;

**(P2)** $0 \notin S(N)$;

**(P3)** if $A \subseteq N$ contains $0$ and is closed under $S$, then $A = N$.

Axiom (P3) is the **induction principle**. A **model of arithmetic** is the structure $(N, 0, S)$ with addition and multiplication defined as below.

**Theorem (Dedekind).** Any two Peano systems are isomorphic: if $(N,0,S)$ and $(N',0',S')$ satisfy (P1)–(P3), there is a unique bijection $f : N \to N'$ with $f(0) = 0'$ and $f(S(n)) = S'(f(n))$ for all $n$.

**Proof.** Define $f$ as the unique function with those two properties, whose existence is the recursion theorem below. For injectivity let $A = \{n : f(m) = f(n) \Rightarrow m = n \text{ for all } m\}$. Then $0 \in A$: if $f(m) = f(0) = 0'$ and $m = S(k)$ then $f(m) = S'(f(k)) \in S'(N')$, contradicting (P2), so $m = 0$. And $A$ is closed under $S$: if $n \in A$ and $f(m) = f(S(n)) = S'(f(n))$, then $m \neq 0$ by (P2), so $m = S(k)$ and $S'(f(k)) = S'(f(n))$, whence $f(k) = f(n)$ by (P1) and $k = n$ by the hypothesis on $n$, giving $m = S(n)$. Hence $A = N$ by (P3). The image of $f$ contains $0'$ and is closed under $S'$, so it is all of $N'$. $\square$

**Theorem.** The set $\omega$ of finite von Neumann ordinals, with $\varnothing$ in the role of $0$ and $n \mapsto n \cup \{n\}$ in the role of $S$, is a Peano system.

**Proof.** The ordinals are transitive sets well ordered by $\in$, and $n \cup \{n\}$ is the least ordinal greater than $n$; hence the map $n \mapsto n\cup\{n\}$ is injective, no ordinal has $\varnothing$ as a successor, and the induction principle is the standard transfinite induction restricted to the finite ordinals, using that every nonzero element of $\omega$ is a successor. $\square$

### Recursion

**Theorem (recursion theorem).** Let $X$ be a set, $x_0 \in X$ and $g : X \to X$. Then there is a unique function $f : \mathbb{N} \to X$ with $f(0) = x_0$ and $f(S(n)) = g(f(n))$ for all $n$.

**Proof.** Consider the set of functions $f_k : \{0,1,\dots,k\} \to X$ satisfying the two conditions on their domains; it is nonempty because the function on $\{0\}$ with value $x_0$ works, and the functions agree on overlaps by induction, so their union is a function $\mathbb{N} \to X$ with the required properties. Uniqueness is (P3) applied to the set of $n$ on which two such functions agree. $\square$

**Definition (addition and multiplication).** Define

$$
m + 0 = m, \qquad m + S(n) = S(m + n), \qquad m \cdot 0 = 0, \qquad m \cdot S(n) = m\cdot n + m .
$$

Both are defined by recursion on the second variable, with $X = \mathbb{N}$ and the appropriate $g$.

**Example.** From the definitions, $1 + 1 = S(1) = 2$, $2 \cdot 3 = 2 + 2 + 2 = 6$, and the successor is the addition of $1$: $S(n) = n + 1$. The two operations are not symmetric in their definitions, and the commutativity of addition and of multiplication is a theorem with an induction proof.

### The Order

**Definition.** For $m, n \in \mathbb{N}$ put $m \leq n$ if there is $k$ with $m + k = n$.

**Theorem.** The relation $\leq$ is a total order with least element $0$, and

$$
m \leq n \iff m = n \ \text{or}\ m < n, \qquad m < n \iff S(m) \leq n .
$$

**Proof.** Reflexivity is $m + 0 = m$; antisymmetry follows from cancellation of addition and the successor axioms; transitivity is associativity of addition, proved by induction. For totality, fix $m$ and apply induction to the statement that every $n$ is comparable with $m$: for $n = 0$ use $0 \leq m$; if $n$ is comparable, then $m + k = n$ gives $m + S(k) = S(n)$ and $n + 1 = S(n)$ gives comparability of $S(n)$ in the other case, and the remaining case $m = n$ gives $m \leq S(n)$. $\square$

**Theorem.** $\mathbb{N}$ is **well ordered**: every nonempty subset $A \subseteq \mathbb{N}$ has a least element. Consequently there is no infinite descending sequence $n_0 > n_1 > n_2 > \cdots$ in $\mathbb{N}$, and the three principles — induction, strong induction, and well ordering — are equivalent.

**Proof.** Let $A$ be nonempty and suppose it has no least element; let $B$ be the set of $n$ below every element of $A$, that is, $n < a$ for all $a \in A$. Then $0 \in B$ because otherwise $0 \in A$ would be a least element, and $B$ is closed under $S$ because if $S(n) \in A$ then $n \in B$ and $S(n)$ would be least; hence $B = \mathbb{N}$ by induction, so $A$ is empty, a contradiction. The equivalence of the three principles is standard: well ordering gives strong induction by considering the set of counterexamples, and strong induction gives ordinary induction trivially. $\square$

## Arithmetic in $\mathbb{N}$

### The Semiring Laws

**Theorem.** For all $m, n, k \in \mathbb{N}$:

$$
m + n = n + m, \qquad (m+n)+k = m+(n+k), \qquad m\cdot n = n\cdot m, \qquad (m\cdot n)\cdot k = m\cdot(n\cdot k),
$$

$$
m\cdot(n+k) = m\cdot n + m\cdot k, \qquad m + 0 = m, \qquad m\cdot 1 = m, \qquad m\cdot 0 = 0 .
$$

Thus $(\mathbb{N}, +, \cdot, 0, 1)$ is a commutative semiring with identity.

**Proof.** Each law is an induction on one of the variables, using the recursive definitions. For commutativity of addition one proves first $S(m+n) = m + S(n)$ (an induction on $n$) and then $m+n=n+m$ (an induction on $n$ with the first identity as the successor step); associativity is an induction on $k$. For multiplication one proves distributivity $m\cdot(n+k) = m\cdot n+m\cdot k$ by induction on $k$, then $m\cdot 1 = m$, then commutativity by induction using distributivity, and associativity by induction on $k$ using associativity of addition. The laws involving $0$ and $1$ are the definitions. $\square$

**Theorem (cancellation).** If $m + k = n + k$ then $m = n$, and if $k \neq 0$ and $m\cdot k = n\cdot k$ then $m = n$.

**Proof.** The additive statement is an induction on $k$ using injectivity of $S$. The multiplicative statement follows from the additive one by well ordering: let $k > 0$ be least with $m \cdot k = n\cdot k$ and $m \neq n$, write $k = k' + 1$, and use $m\cdot k = m\cdot k' + m$ to obtain a contradiction with the minimality of $k$. $\square$

**Corollary.** $\mathbb{N}$ is an additive and multiplicative **cancellative** commutative monoid and an integral domain in the semiring sense: $m\cdot n = 0$ implies $m = 0$ or $n = 0$.

**Proof.** The last statement is by induction on $n$: if $n = 0$ there is nothing to prove, and if $n = S(n')$ then $m\cdot n = m\cdot n' + m = 0$ forces $m = 0$ because a sum of naturals is zero only if both summands are zero. $\square$

### The Universal Property

**Theorem.** Let $(A, +, \cdot, 0_A, 1_A)$ be a commutative semiring with identity and let $a \in A$. Then there is a unique semiring homomorphism $\varphi : \mathbb{N} \to A$ with $\varphi(1) = 1_A$; it is given by $\varphi(n) = n \cdot 1_A$ and is the unique homomorphism of unital semirings. In particular $\mathbb{N}$ is the **initial object** in the category of commutative semirings with identity, and it is the free such semiring on the empty set of generators.

**Proof.** The map $n \mapsto n\cdot 1_A$ is defined by recursion and is additive and multiplicative by the distributive and associative laws in $A$; uniqueness is forced because a unital semiring homomorphism must send $1$ to $1_A$ and preserve sums. $\square$

**Corollary.** For a commutative ring $A$ with identity, the universal map $\mathbb{N} \to A$ is injective if and only if $A$ has characteristic $0$. In particular $\mathbb{N}$ embeds in $\mathbb{Z}$, in $\mathbb{Q}$, in $\mathbb{R}$ and in $\mathbb{C}$ as a subsemiring, and it is the smallest subsemiring containing $1$ in each of them.

**Definition.** The **embedding** $\mathbb{N} \hookrightarrow \mathbb{Z}$ is the map $n \mapsto [(n,0)]$ in the construction of $\mathbb{Z}$ as the Grothendieck group of the additive monoid $\mathbb{N}$; it is injective and preserves $+, \cdot, 0, 1$.

## Divisibility

### The Multiplicative Structure

**Definition.** For $a, b \in \mathbb{N}$ one writes $a \mid b$ if there is $c$ with $b = ac$. The **units** of $\mathbb{N}$ are the divisors of $1$, namely $1$. A natural number $p > 1$ is **prime** if its only divisors are $1$ and $p$, and **composite** otherwise.

**Theorem (division algorithm).** For all $a, b \in \mathbb{N}$ with $b \neq 0$ there are unique $q, r \in \mathbb{N}$ with

$$
a = qb + r, \qquad 0 \leq r < b .
$$

**Proof.** Existence by induction on $a$: if $a < b$ take $q = 0$, $r = a$; otherwise $a \geq b$, so $a = a' + 1 = a' + b\cdot 0 + 1$; if $a' = q'b + r'$ with $r' < b$ then $a = q'b + (r'+1)$ and either $r'+1 < b$ or $r' + 1 = b$, in which case $a = (q'+1)b + 0$. Uniqueness: if $qb + r = q'b + r'$ with $r, r' < b$, then $b \mid r - r'$ and $\lvert r - r'\rvert < b$, so $r = r'$ and then $q = q'$ by cancellation. $\square$

**Theorem (Euclid).** Every pair $a, b \in \mathbb{N}$ not both zero has a greatest common divisor $d$, and there are integers $u, v$ with $ua + vb = d$; the Euclidean algorithm computes $d$ and terminates. In particular $a$ and $b$ are **coprime** exactly when $ua + vb = 1$ for some integers $u, v$.

**Proof.** The Euclidean algorithm is the iterated division algorithm applied to $(a,b)$, and termination is by the well-ordering of $\mathbb{N}$, since the remainders strictly decrease. The Bézout identity is the standard back-substitution, and the gcd properties follow from it; the details are in *GCD Domains*. $\square$

**Theorem (fundamental theorem of arithmetic).** Every natural number $n > 1$ has a factorization $n = p_1 p_2 \cdots p_k$ into primes, unique up to the order of the factors.

**Proof.** Existence by strong induction: if $n$ is not prime it has a factorization $n = ab$ with $a, b < n$, and the induction hypothesis factors $a$ and $b$. Uniqueness by the standard argument using Euclid's lemma: if $p$ is prime and $p \mid ab$ then $p \mid a$ or $p \mid b$, which follows from the Bézout identity $up + va = 1$ for $p \nmid a$ by multiplying by $b$. The full argument is in *Unique Factorisation Domains*. $\square$

**Corollary.** $(\mathbb{N}\setminus\{0\}, \cdot, 1)$ is the free commutative monoid on the set of primes: every positive natural number has a unique expression $\prod_p p^{v_p(n)}$ with $v_p(n) \in \mathbb{N}$ and only finitely many exponents nonzero. Its group of fractions is the multiplicative group $\mathbb{Q}^\times$ of *The Rational Numbers*.

**Theorem (Euclid).** There are infinitely many primes.

**Proof.** Given finitely many primes $p_1, \dots, p_k$, the number $p_1\cdots p_k + 1$ is greater than $1$ and is divisible by none of them, so some prime divides it and is not among them. $\square$

## Cardinality and Embedding

### Countability

**Definition.** A set is **countable** if it is in bijection with a subset of $\mathbb{N}$, and **countably infinite** if it is in bijection with $\mathbb{N}$.

**Theorem.** $\mathbb{N}$ is well ordered and every infinite subset of $\mathbb{N}$ is countably infinite; the cardinality of $\mathbb{N}$ is written $\aleph_0$, and it is the least infinite cardinal.

**Proof.** An infinite subset $A \subseteq \mathbb{N}$ is enumerated by $a_0 = $ least element of $A$, $a_{n+1} = $ least element of $A \setminus \{a_0,\dots,a_n\}$, which exists by well ordering; the enumeration is a bijection by induction. The cardinal statement is the definition of $\aleph_0$ as the least infinite cardinal. $\square$

**Theorem (Cantor).** There is no surjection from $\mathbb{N}$ onto its power set $\mathcal{P}(\mathbb{N})$; hence $\lvert \mathcal{P}(\mathbb{N})\rvert > \aleph_0$.

**Proof.** Given any map $f : \mathbb{N} \to \mathcal{P}(\mathbb{N})$, the diagonal set $D = \{n : n \notin f(n)\}$ is not in the image of $f$, since $D = f(m)$ would give $m \in D \iff m \notin D$. $\square$

**Corollary.** $\mathbb{Z}$, $\mathbb{Q}$ and $\overline{\mathbb{Q}}$ are countable, and $\mathbb{R}$ and $\mathbb{C}$ are not; the details are in *Cardinality and the Axiom of Choice*. The system $\mathbb{N}$ is the smallest infinite system of the ladder, and every later system of Part V is either countable, as $\mathbb{Z}$, $\mathbb{Q}$ and $\overline{\mathbb{Q}}$ are, or uncountable, as $\mathbb{R}$ and $\mathbb{C}$ are.

### The Place of $\mathbb{N}$ among the Systems

$\mathbb{N}$ is the base of the ladder of Part V, and each later system is obtained by adjoining a structure that $\mathbb{N}$ lacks:

| System | Adjoined structure | What fails in $\mathbb{N}$ |
|---|---|---|
| $\mathbb{Z}$ | additive inverses | no solution to $x + 1 = 0$ |
| $\mathbb{Q}$ | multiplicative inverses | no solution to $2x = 1$ |
| $\mathbb{R}$ | order-completeness | no supremum for $\{x : x^2 < 2\}$ |
| $\mathbb{C}$ | algebraic closure | no root of $x^2 + 1$ |

The table is the ladder of Part V read from its base, and the additions are cumulative: $\mathbb{Z}$ is the ring of fractions of the additive monoid $\mathbb{N}$ in the sense of Grothendieck, $\mathbb{Q}$ is the fraction field of $\mathbb{Z}$, and $\mathbb{R}$ and $\mathbb{C}$ are the completions and algebraic closure. No arrow in the table reverses, so $\mathbb{N}$ cannot be recovered from a later system by an algebraic operation alone; it is recovered by taking the nonnegative elements, which requires the order of the later system.

**Remark.** The system $\mathbb{N}$ carries no geometry and no analysis, and correspondingly this Part develops for it only the algebra and the arithmetic functions. There is no real line geometry of $\mathbb{N}$, no integration, no harmonic analysis and no representation theory: those slots are occupied by the systems that carry a field and a completion. What $\mathbb{N}$ does carry beyond its semiring structure is a well ordering and a recursion principle, and those are the source of its two further articles, the model theory of its first-order theory and the theory of the functions defined on it.

## Summary

The natural numbers are the Peano system $(\mathbb{N}, 0, S)$: a set with a distinguished element and an injective successor map omitting $0$, satisfying the induction principle. This structure is unique up to a unique isomorphism, and it is realised by the finite von Neumann ordinals. The recursion theorem turns the successor into the two operations $+$ and $\cdot$, defined by $m+0 = m$, $m+S(n) = S(m+n)$, $m\cdot 0 = 0$ and $m\cdot S(n) = m\cdot n + m$, and the arithmetic laws — commutativity, associativity, distributivity, cancellation and the absence of zero divisors — follow by induction. The order $m \leq n \iff \exists k\, m + k = n$ is total with least element $0$, and $\mathbb{N}$ is well ordered; induction, strong induction and well ordering are equivalent.

$(\mathbb{N}, +, \cdot, 0, 1)$ is a commutative semiring with identity, and it is the initial such semiring and the free one on no generators: every commutative semiring with identity receives a unique unital homomorphism from $\mathbb{N}$. It is not a ring, and it embeds in $\mathbb{Z}$, hence in $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$. Divisibility in $\mathbb{N}$ is governed by the division algorithm and the Euclidean algorithm, the units are just $1$, and the fundamental theorem of arithmetic expresses every positive natural number uniquely as a product of primes; the positive naturals form the free commutative monoid on the primes, and there are infinitely many primes. The cardinality of $\mathbb{N}$ is $\aleph_0$, the least infinite cardinal, and Cantor's theorem shows that its power set is strictly larger. $\mathbb{N}$ is the base of the ladder of Part V, and the passage to $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$ adjoins, successively, additive inverses, multiplicative inverses, order-completeness and algebraic closure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{N}$ | The natural numbers, $\{0,1,2,\dots\}$ |
| $S$ | Successor map, $S(n) = n+1$ |
| $(P1)$–$(P3)$ | The Peano axioms, injectivity, omission of $0$, induction |
| $\omega$ | First infinite von Neumann ordinal, a model of $\mathbb{N}$ |
| $+$, $\cdot$ | Addition and multiplication, defined by recursion |
| $\leq$, $<$ | The total order and its strict part |
| $m \mid n$ | Divisibility in $\mathbb{N}$ |
| $\gcd(a,b)$ | Greatest common divisor |
| $p$ | A prime |
| $v_p(n)$ | Exponent of $p$ in $n$ |
| $\aleph_0$ | Cardinality of $\mathbb{N}$ |
| $\binom{n}{k}$, $n!$ | Binomial coefficient and factorial |
| $\mathcal{P}(\mathbb{N})$ | Power set, of strictly larger cardinality |





## Further Reading

- Richard Dedekind, *Was sind und was sollen die Zahlen?* (Vieweg, 1888), for the Peano system, the recursion theorem and the categoricity of the second-order axioms.
- Giuseppe Peano, *Arithmetices principia, nova methodo exposita* (Bocca, 1889), for the original axiomatisation of arithmetic.
- Edmund Landau, *Foundations of Analysis* (Chelsea, 1951), for the construction of the number systems beginning with the natural numbers.
- Paul R. Halmos, *Naive Set Theory* (Van Nostrand, 1960), for the von Neumann ordinals and the construction of $\mathbb{N}$ in set theory.
- G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (Oxford University Press, 6th ed. 2008), for the division algorithm, the Euclidean algorithm and the fundamental theorem of arithmetic.
- Thomas Jech, *Set Theory* (Springer, 3rd millennium ed. 2003), for the ordinals, recursion, well ordering and the cardinal $\aleph_0$.
