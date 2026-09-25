
# __Rings__

## Introduction

A **ring** is a set carrying an addition under which it is an abelian group and an associative multiplication distributing over that addition. This article is the first rung of the chain of *Rings and Fields*, and it fixes the vocabulary that every later article of the corpus uses: subrings, ring homomorphisms, kernels and quotients, ideals and the ideals they generate, and the multiplicative vocabulary of units, zero divisors, nilpotents and idempotents. Commutativity is **not** assumed here. The general ring is written $A$ throughout, and the corpus's default base, the commutative ring with $1 \neq 0$, is written $R$ and is the subject of *Commutative Rings*, directly below this article in this category.

The article is deliberately narrow, because each further hypothesis on a ring belongs to its own rung of the category. The commutative law and the ideal theory that uses it are *Commutative Rings*; the absence of zero divisors, and the divisibility theory that the absence supports, are *Integral Domains*, later in this category; the nilpotent structure of a ring is *Reduced Rings and the Nilradical*; fields are *Fields*; division rings are *Division Rings*; the factorisation rungs are *Unique Factorisation Domains*, *Principal Ideal Domains* and *Euclidean Domains*; and modules and algebras over rings are *Modules* and *Algebras*, in the later categories of this Part. What is owned here is the ring itself, its elements, its ideals and its quotients.

---

## Rings

### The Definition

**Definition.** A **ring** is a set $A$ with two binary operations, written $+$ and juxtaposition, such that

**(A1)** $(A, +)$ is an abelian group: addition is associative and commutative, there is an element $0 \in A$ with $a + 0 = a$ for all $a$, and for every $a$ there is $-a$ with $a + (-a) = 0$;

**(A2)** multiplication is associative: $(ab)c = a(bc)$ for all $a, b, c \in A$;

**(A3)** multiplication distributes over addition on both sides:

$$
a(b + c) = ab + ac, \qquad (a + b)c = ac + bc
$$

for all $a, b, c \in A$;

**(A4)** there is an element $1 \in A$ with $1a = a1 = a$ for all $a \in A$, and $1 \neq 0$.

A ring in this sense is **unital**, or a ring with identity, and **associative**. The corpus assumes both properties of every ring. A ring is **commutative** if $ab = ba$ for all $a, b \in A$, and **non-commutative** otherwise; *Commutative Rings*, below this article in this category, takes up the commutative case.

**Remark.** Associativity is an axiom of (A2) and is not automatic: the algebras of *Algebras* and the non-associative systems of *Non-Associative Algebras and the Property Ladder*, both in a later category of this Part, satisfy (A1), (A3) and (A4) with a multiplication that need not be associative. The rings here are associative, so the non-associative law never needs checking again.

**Remark (the zero ring).** A ring in which $1 = 0$ has $a = a \cdot 1 = a \cdot 0 = 0$ for every $a$, so it is the **zero ring** $\{0\}$, and it is the only such ring. The condition $1 \neq 0$ in (A4) excludes it, and no article of this category admits it as a ring.

### Elementary Properties

Let $A$ be a ring.

**(a) Uniqueness of the identities.** The elements $0$ and $1$ are unique, and the additive inverse $-a$ of $a$ is unique.

**(b) Multiplication by zero.** For all $a \in A$,

$$
a \cdot 0 = 0 \cdot a = 0 .
$$

**(c) Sign rules.** For all $a, b \in A$,

$$
(-a)b = a(-b) = -(ab), \qquad (-a)(-b) = ab .
$$

**(d) Integer multiples.** For $n \in \mathbb{Z}$ and $a \in A$, the multiple $n \cdot a$ is the repeated sum when $n > 0$, zero when $n = 0$ and $-(|n| \cdot a)$ when $n < 0$; the multiples of $1$ form a subring of $A$, its **prime subring**.

**Proof.** (a) If $0$ and $0'$ are both additive identities then $0 = 0 + 0' = 0'$; if $1$ and $1'$ are both multiplicative identities then $1 = 1 \cdot 1' = 1'$; and if $b, b'$ are both inverses of $a$ then $b = b + 0 = b + a + b' = b'$. (b) $a \cdot 0 = a(0 + 0) = a \cdot 0 + a \cdot 0$, and cancelling in the additive group gives $a \cdot 0 = 0$; the other side is symmetric. (c) $0 = a \cdot 0 = a(b + (-b)) = ab + a(-b)$ gives $a(-b) = -(ab)$, and $(-a)b = -(ab)$ is symmetric; then $(-a)(-b) = -(a(-b)) = -(-(ab)) = ab$. (d) The set of multiples of $1$ is closed under subtraction and under multiplication, and contains $1$. $\square$

The **characteristic** of a ring — the least positive $n$ with $n \cdot 1 = 0$, or $0$ if there is none — is developed with the domains that use it, in *Integral Domains*, later in this category.

### Subrings

**Definition.** A subset $S \subseteq A$ is a **subring** of $A$ if $S$ is a subgroup of $(A, +)$, is closed under multiplication, and contains $1$.

A subring is itself a ring under the inherited operations, with the same $1$ and $0$.

**Proposition.** The intersection of any family of subrings of $A$ is a subring of $A$.

**Proof.** The intersection contains $1$ and is closed under subtraction and under multiplication, being so in each member of the family. $\square$

**Example.** The multiples of $1$ in $A$ form the smallest subring of $A$, the prime subring; it is the image of the unique ring homomorphism $\mathbb{Z} \to A$.

---

## Ring Homomorphisms

### Definition

**Definition.** Let $A$ and $B$ be rings. A **ring homomorphism** is a function $\varphi : A \to B$ with

$$
\varphi(a + b) = \varphi(a) + \varphi(b), \qquad \varphi(ab) = \varphi(a)\varphi(b), \qquad \varphi(1_A) = 1_B
$$

for all $a, b \in A$. A bijective homomorphism is an **isomorphism**, written $A \cong B$ when one exists. A homomorphism $A \to A$ from a ring to itself is an **endomorphism**, and a bijective one is an **automorphism** of $A$.

**Proposition.** Let $\varphi : A \to B$ be a ring homomorphism. Then $\varphi(0) = 0$, $\varphi(-a) = -\varphi(a)$ and $\varphi(n \cdot a) = n \cdot \varphi(a)$ for every $n \in \mathbb{Z}$.

**Proof.** $\varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0)$ gives $\varphi(0) = 0$; then $0 = \varphi(a + (-a)) = \varphi(a) + \varphi(-a)$ gives the sign rule; the integer multiples follow by induction on $n$. $\square$

**Example.** Complex conjugation $z \mapsto \bar z$ is an automorphism of $\mathbb{C}$, and it is the standard example of a non-trivial automorphism of a ring. The transformation group of a ring, and what an automorphism preserves, is *Ring and Field Automorphisms*, later in this category.

### Kernels and Images

**Definition.** The **kernel** of $\varphi : A \to B$ is $\ker \varphi = \{a \in A : \varphi(a) = 0\}$, and its **image** is $\operatorname{im}\varphi = \{\varphi(a) : a \in A\}$.

**Proposition.** $\operatorname{im}\varphi$ is a subring of $B$; $\ker\varphi$ is a two-sided ideal of $A$ in the sense of the next section; and $\varphi$ is injective if and only if $\ker\varphi = (0)$.

**Proof.** The image contains $1_B$ and is closed under subtraction and under multiplication, since $\varphi$ is a homomorphism. The kernel is an additive subgroup, and if $a \in \ker\varphi$ then $\varphi(xa) = \varphi(x)\varphi(a) = 0$ and $\varphi(ax) = \varphi(a)\varphi(x) = 0$ for every $x \in A$, so it is closed under multiplication on both sides. Finally, $\varphi(a) = \varphi(b)$ if and only if $\varphi(a - b) = 0$. $\square$

---

## Ideals

### One-Sided and Two-Sided Ideals

**Definition.** Let $A$ be a ring. A subset $I \subseteq A$ is

**(a)** a **left ideal** if $I$ is an additive subgroup of $A$ and $aI \subseteq I$ for every $a \in A$;

**(b)** a **right ideal** if $I$ is an additive subgroup of $A$ and $IA \subseteq I$ for every $a \in A$;

**(c)** a **two-sided ideal**, written $I \trianglelefteq A$, if it is both a left and a right ideal.

The three notions coincide in a commutative ring, where one speaks simply of an ideal, and the ideal theory of that case is *Commutative Rings*, below this article in this category. A **proper** ideal is one with $I \neq A$; a proper ideal contains no unit, by the proposition on units below.

**Example.** In the matrix ring $M_n(F)$ over a field, the set of matrices whose only possibly nonzero column is the first is a left ideal, the set of matrices whose only possibly nonzero row is the first is a right ideal, and neither is two-sided. The two-sided ideal generated by the matrix unit $E_{11}$ is the whole ring, so a set of generators that generates $A$ as a two-sided ideal need not contain a unit.

**Proposition.** Let $A$ be a ring with $1 \neq 0$. Then every nonzero element of $A$ is a unit if and only if $A$ has no left ideal other than $(0)$ and $A$, equivalently no right ideal other than $(0)$ and $A$; and a ring with this property has no two-sided ideal other than $(0)$ and $A$. The converse of the last implication fails.

**Proof.** If every nonzero element is a unit and $L \neq (0)$ is a left ideal, then $L$ contains a nonzero $a$, hence contains $a^{-1}a = 1$, so $L = A$; the right-handed statement is symmetric. Conversely suppose the only left ideals are $(0)$ and $A$, and let $a \neq 0$. Then $Aa = A$, so $ba = 1$ for some $b$. If $ab \neq 1$ then $1 - ab \neq 0$ and $ab$ is idempotent, so $A(1-ab) = A$ and there is $c$ with $c(1-ab) = 1$; multiplying this on the right by $ab$ gives $ab = c(ab - (ab)^2) = 0$, contradicting $ab \neq 0$, which follows from $a = a\cdot 1 = a(ba) = (ab)a$. Hence $ab = 1$ as well, and $a$ is a unit. Finally, a two-sided ideal is a left ideal, so the one-sided condition implies the two-sided one; the converse fails because $M_n(F)$ for $n \geq 2$ has no nonzero proper two-sided ideal, by the example below, while $E_{11}$ is not a unit. $\square$

### Ideals Generated by a Set

**Definition.** Let $S \subseteq A$. The **two-sided ideal generated by $S$** is the intersection of the two-sided ideals containing $S$, written $(S)$; the **left ideal generated by $S$**, written $AS$, and the **right ideal generated by $S$**, written $SA$, are defined analogously with left and with right ideals. For a single element $a$, the **principal ideal** generated by $a$ is $(a) = AaA$.

**Proposition.** Let $S \subseteq A$. Then

$$
(S) = \Big\{ \sum_{i=1}^{n} x_i s_i y_i : n \geq 1, \ x_i, y_i \in A, \ s_i \in S \Big\}, \qquad AS = \Big\{ \sum_{i=1}^{n} x_i s_i : x_i \in A, \ s_i \in S \Big\},
$$

and $SA$ is described symmetrically.

**Proof.** The displayed set is an additive subgroup, by the grouping of finite sums; it is closed under multiplication by elements of $A$ on both sides, since $x(a s y)$ and $(x a s)y$ are again of the displayed form; and it contains $S$, taking $x = y = 1$. Every two-sided ideal containing $S$ contains every $x_i s_i y_i$ and hence their sums, so the displayed set is the smallest one. The left-hand case is identical with the $y_i$ omitted. $\square$

**Example.** In $M_n(F)$ the ideal generated by $E_{11}$ is the whole ring: $E_{ij} = E_{i1} E_{11} E_{1j}$, so all matrix units lie in $(E_{11})$, whereas $A E_{11}$ is only the left ideal of the previous example. In $\mathbb{Z}$ the ideals are the $(n)$ with $n \geq 0$.

**Example.** The ring $M_n(F)$ has no two-sided ideals other than $(0)$ and $M_n(F)$: if $M \neq 0$ has an entry $c = M_{kl} \neq 0$, then $E_{ik} M E_{lj} = c E_{ij}$, so every matrix unit, and with them every matrix, lies in the ideal generated by $M$.

### Sums, Products and Intersections

**Definition.** For ideals $I, J$ of $A$ define $I + J = \{x + y : x \in I, y \in J\}$ and $IJ = \{\sum_{k} x_k y_k : x_k \in I, y_k \in J\}$, the sums being finite.

**Proposition.** Let $I, J, K$ be two-sided ideals of $A$. Then $I + J$, $I \cap J$ and $IJ$ are two-sided ideals, $IJ \subseteq I \cap J$, and $(I + J)K = IK + JK$ and $I(J + K) = IJ + IK$. If $I$ and $J$ are only left ideals, then $I + J$ and $I \cap J$ are left ideals and $IJ$ is a left ideal.

**Proof.** Each of the three sets is an additive subgroup; closure under multiplication by $a \in A$ follows from the corresponding closure of $I$ and of $J$, and for $IJ$ by pushing $a$ into the first factor of each summand. Every $xy$ with $x \in I$, $y \in J$ lies in $I$ and in $J$, giving $IJ \subseteq I \cap J$. Distributivity follows from distributivity in $A$ and from the closure of the ideals. $\square$

**Remark.** The union of two ideals is an ideal only when one contains the other, and the smallest ideal containing both is the sum. The product of ideals is not commutative in the non-commutative case, $IJ \neq JI$ in general; the commutativity of the product of ideals is taken up in *Commutative Rings*, below this article in this category.

### Prime and Maximal Ideals

**Definition.** Let $P \subsetneq A$ be a proper two-sided ideal. Then $P$ is **prime** if for all two-sided ideals $I, J$,

$$
IJ \subseteq P \implies I \subseteq P \text{ or } J \subseteq P ,
$$

and $P$ is **maximal** if there is no two-sided ideal strictly between $P$ and $A$.

**Theorem.** A maximal two-sided ideal is prime.

**Proof.** Let $M$ be maximal and let $IJ \subseteq M$ with $I \not\subseteq M$ and $J \not\subseteq M$. Then $M + I$ and $M + J$ are two-sided ideals strictly containing $M$, hence both equal $A$ by maximality. Therefore

$$
A = A \cdot A = (M + I)(M + J) = M^2 + MJ + IM + IJ \subseteq M ,
$$

since each of the four terms on the right lies in $M$, and $A = M$ contradicts the properness of $M$. $\square$

**Remark.** In a commutative ring, $P$ is prime exactly when $ab \in P$ implies $a \in P$ or $b \in P$, the two formulations being equivalent there; and the quotient by a maximal ideal is a field while the quotient by a prime ideal is an integral domain, in the terminology of *Fields* and *Integral Domains*, later in this category. In a general ring the correct quotient characterisation of a prime ideal is not the absence of zero divisors, and it is stated in *Prime Rings*, below this article in this category.

---

## Quotient Rings

### The Construction

**Definition.** Let $I \trianglelefteq A$ be a two-sided ideal and let $A/I$ be the set of additive cosets $a + I$. Define

$$
(a + I) + (b + I) = (a + b) + I, \qquad (a + I)(b + I) = ab + I .
$$

**Proposition.** The operations are well defined, and $A/I$ is a ring with zero $0 + I$ and identity $1 + I$. The map $\pi : A \to A/I$, $a \mapsto a + I$, is a surjective ring homomorphism with kernel $I$.

**Proof.** If $a' = a + x$ and $b' = b + y$ with $x, y \in I$, then $a'b' = ab + ay + xb + xy \in ab + I$, using the two-sidedness of $I$ for $ay$ and for $xb$; the verification for addition is immediate. The axioms are inherited from $A$, and $\pi$ is a homomorphism by the definition of the operations, with $a \in \ker\pi$ exactly when $a \in I$. $\square$

The ideal $I$ has to be two-sided for $A/I$ to be a ring. The quotients by one-sided ideals are quotients of modules rather than of rings, and are treated in *Modules*, in a later category of this Part.

### The Correspondence Theorem

**Theorem (correspondence theorem).** Let $I \trianglelefteq A$ and let $\pi : A \to A/I$ be the quotient map. Then $J \mapsto \pi(J)$ is a bijection from the set of two-sided ideals of $A$ containing $I$ onto the set of two-sided ideals of $A/I$, its inverse being $K \mapsto \pi^{-1}(K)$. It preserves inclusions, sums and products, and carries primes to primes and maximal ideals to maximal ideals.

**Proof.** A two-sided ideal $K$ of $A/I$ has inverse image $\pi^{-1}(K)$ containing $I$ that is an additive subgroup closed under multiplication by $A$ on both sides; conversely $\pi(J)$ has the same properties in $A/I$. The two constructions are inverse to one another, since $\pi$ is surjective. Inclusions, sums, products and one-sided conditions are preserved in both directions, since $\pi$ is a surjective homomorphism, and the prime and the maximal conditions are subsethood conditions, hence preserved. $\square$

**Corollary.** The two-sided ideals of $A/I$ correspond to the two-sided ideals of $A$ containing $I$; in particular $A/I$ has no nonzero proper two-sided ideals exactly when $I$ is a maximal two-sided ideal of $A$.

**Proof.** Immediate from the theorem. $\square$

### The Isomorphism Theorems

**Theorem (first isomorphism theorem).** Let $\varphi : A \to B$ be a ring homomorphism. Then the induced map $\varphi' : A/\ker\varphi \to \operatorname{im}\varphi$, $a + \ker\varphi \mapsto \varphi(a)$, is an isomorphism.

**Proof.** The map is well defined, since $\varphi$ is constant on the cosets of its kernel; it is additive, multiplicative and unital because $\varphi$ is; it is injective because $\varphi(a) = 0$ implies $a \in \ker\varphi$; and its image is $\operatorname{im}\varphi$ by construction. $\square$

**Theorem (second isomorphism theorem).** Let $I \trianglelefteq A$ and let $S$ be a subring of $A$. Then $I + S$ is a subring, $I \cap S$ is a two-sided ideal of $S$, and

$$
(I + S)/I \cong S/(I \cap S) .
$$

**Proof.** $I + S$ is a subring since both are additive subgroups and $IS \subseteq I$; the kernel of the restriction to $S$ of the quotient map $A \to A/I$ is $I \cap S$, and its image is $(I + S)/I$, so the first isomorphism theorem applies. $\square$

**Theorem (third isomorphism theorem).** Let $I \subseteq J$ be two-sided ideals of $A$. Then $J/I$ is a two-sided ideal of $A/I$ and $(A/I)/(J/I) \cong A/J$.

**Proof.** The composite of the quotient maps $A \to A/I$ and $A/I \to (A/I)/(J/I)$ is a surjective homomorphism with kernel $J$. $\square$

---

## The Multiplicative Vocabulary

### Units

**Definition.** An element $a \in A$ is a **unit** if there is $b \in A$ with $ab = ba = 1$. The units form a group under multiplication, written $A^{\times}$, with identity $1$, and $a^{-1}$ is written for the inverse of the unit $a$.

**Proposition.** For $a \in A$ the following are equivalent: $a$ is a unit; $Aa = A$ and $aA = A$; the principal left ideal generated by $a$ and the principal right ideal generated by $a$ are both $A$. When $A$ is commutative each of these is equivalent to $(a) = A$.

**Proof.** If $a$ is a unit then $Aa = A = aA$, since $x = (xa^{-1})a$ and $x = a(a^{-1}x)$. If $Aa = A$ then $1 = ba$ for some $b$, so $a$ has a left inverse; if also $aA = A$ then $1 = ac$ for some $c$, so $a$ has a right inverse; from $ba = 1 = ac$ we get $b = b(ac) = (ba)c = c$, so $b = c = a^{-1}$. The commutative case is the special case in which the left and the right conditions coincide. $\square$

**Corollary.** A proper two-sided ideal contains no unit; in particular $A$ is the only ideal containing a unit.

### Zero Divisors

**Definition.** A nonzero $a \in A$ is a **left zero divisor** if $ab = 0$ for some nonzero $b \in A$, and a **right zero divisor** if $ba = 0$ for some nonzero $b \in A$; a **zero divisor** is an element that is a left or a right zero divisor. The condition $a \neq 0$ is part of the definition, since otherwise $0$ would be a zero divisor in every nonzero ring.

**Proposition.** If $a$ is not a left zero divisor then $ab = ac$ implies $b = c$; if $a$ is not a right zero divisor then $ba = ca$ implies $b = c$. In a commutative ring the two-sided cancellation is available exactly for the elements that are not zero divisors.

**Proof.** $ab = ac$ gives $a(b - c) = 0$ in the additive group, and $a$ not being a zero divisor forces $b - c = 0$; the right-hand case is symmetric. $\square$

**Remark.** A ring in which a product of nonzero elements is nonzero, so that there are no zero divisors, is the subject of *Integral Domains* in the commutative case and of *Non-Commutative Domains* in the general case, later in this category; the cancellation calculus just stated is the heart of both articles.

### Nilpotents

**Definition.** An element $a \in A$ is **nilpotent** if $a^n = 0$ for some integer $n \geq 1$. The element $0$ is nilpotent, and it is the only nilpotent in $A$ exactly when $A$ is **reduced**.

**Proposition.** Let $a, b \in A$ be nilpotent with $a^m = 0$ and $b^n = 0$, and let $x \in A$.

**(a)** If $x$ commutes with $a$, then $ax$ and $xa$ are nilpotent.

**(b)** If $a$ and $b$ commute, then $a + b$ is nilpotent.

**(c)** $1 - a$ is a unit, with two-sided inverse $\sum_{k=0}^{m-1} a^k$.

**Proof.** (a) If $ax = xa$ then $(ax)^m = a^m x^m = 0$, and similarly on the left. (b) If $ab = ba$, every term of the binomial expansion of $(a + b)^{m+n-1}$ contains a factor $a^m$ or a factor $b^n$. (c) $(1 - a)\sum_{k=0}^{m-1} a^k = 1 - a^m = 1$, and the product in the other order is the same, so the displayed sum is the two-sided inverse. $\square$

**Remark.** Commutativity is needed in (a): in $M_2(k)$ the element $a = E_{12}$ satisfies $a^2 = 0$, while $ax = E_{11}$ for $x = E_{21}$, and $E_{11}$ is idempotent and not nilpotent. So the product of a nilpotent with an arbitrary element need not be nilpotent, and the set of nilpotents is closed under multiplication only in the commutative case. What does hold generally is that $1 - ax$ is a unit exactly when $1 - xa$ is, with the two inverses conjugate; the argument is the same telescoping sum as in (c) and is cited from the literature.

**Remark.** The set of nilpotent elements is closed under addition only when the ring is commutative, by (b); in the commutative case it is the **nilradical**, an ideal, and the whole nilpotent structure — the nilradical as the intersection of the prime ideals, and reduced rings as subrings of products of domains — belongs to *Reduced Rings and the Nilradical*, below this article in this category. The corresponding non-commutative theory is *Semiprime Rings*, further below in this category.

### Idempotents

**Definition.** An element $e \in A$ is **idempotent** if $e^2 = e$. The elements $0$ and $1$ are idempotents, and $e$ is idempotent exactly when $1 - e$ is.

**Proposition.** **(a)** If $e$ is idempotent and $e \neq 0$, then $e$ is not nilpotent and $e$ is a unit only if $e = 1$. **(b)** If $e$ and $f$ are commuting idempotents then $ef$ is idempotent. **(c)** If $e$ is an idempotent unit then $e = 1$.

**Proof.** (a) $e^n = e$ for every $n \geq 1$, so $e$ is nilpotent only if $e = 0$; and if $e$ is a unit then $e = e^2$ gives $1 = e$ after multiplying by $e^{-1}$. (b) $(ef)^2 = efef = eeff = ef$, using the commutativity of $e$ and $f$ in the middle. (c) This is the second half of (a). $\square$

**Remark.** Idempotents detect decompositions of a ring: a central idempotent $e$, one with $ea = ae$ for every $a \in A$, splits $A$ as the product of the rings $eA$ and $(1-e)A$, since $x = ex + (1-e)x$ for every $x$. The proof that this product is a ring isomorphism, that the same idempotent gives the four-corner Peirce decomposition $A = eAe \oplus eAf \oplus fAe \oplus fAf$ for $f = 1-e$, and that centrality is exactly what collapses that decomposition to a product, is carried out for algebras in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the ring-theoretic statement is the special case of it. The rings in which the principal left ideals are generated by idempotents are *Von Neumann Regular Rings*, below this article in this category.

---

## Summary

A ring is a set with an abelian group structure $+$, an associative multiplication distributing over it, and an identity $1 \neq 0$; commutativity is not assumed, the general ring is written $A$, and the corpus's default commutative ring is written $R$. The elementary properties of the operations, the notion of a subring, and the behaviour of ring homomorphisms with their kernels and images follow from the axioms. A ring homomorphism has a two-sided ideal as kernel, and conversely every two-sided ideal is the kernel of the quotient map.

The ideals of a ring are its additive subgroups closed under left multiplication (left ideals), under right multiplication (right ideals), or under both (two-sided ideals); the three notions coincide in the commutative case, whose ideal theory is *Commutative Rings*. The ideal generated by a set is the set of finite sums $\sum x_i s_i y_i$, the principal ideal $(a)$ being $AaA$. Sums, intersections and products of two-sided ideals are two-sided ideals, with $IJ \subseteq I \cap J$. A proper two-sided ideal is prime when it contains a product of ideals only through its factors, and maximal when no ideal lies properly between it and the ring; every maximal ideal is prime. Quotients by two-sided ideals are rings, their ideals correspond to the ideals of $A$ containing the kernel, and the three isomorphism theorems hold.

The multiplicative vocabulary consists of the units, the group $A^{\times}$ of invertible elements, characterised by the two conditions $Aa = A$ and $aA = A$; the zero divisors, which obstruct cancellation; the nilpotents, whose structure is *Reduced Rings and the Nilradical*; and the idempotents, which split the ring and whose ideal-theoretic role belongs to *Von Neumann Regular Rings*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A ring, not assumed commutative: the general ring of this article |
| $R$ | The corpus default, a commutative ring with $1 \neq 0$, of *Commutative Rings* |
| $1$, $0$ | Multiplicative and additive identity, with $1 \neq 0$ |
| $a^{-1}$ | Inverse of the unit $a$ |
| $A^{\times}$ | Group of units of $A$ |
| $+$, juxtaposition | Addition and multiplication of the ring |
| $n \cdot a$ | The integer multiple of $a$ |
| $\mathbb{Z}$ | The integers, the initial ring; its image is the prime subring of $A$ |
| $S \subseteq A$ | A subset; a subring when it is a subgroup closed under multiplication and containing $1$ |
| $\varphi : A \to B$ | A ring homomorphism, unital by definition |
| $\ker\varphi$, $\operatorname{im}\varphi$ | Kernel and image of $\varphi$ |
| $A \cong B$ | Isomorphic rings |
| $I \trianglelefteq A$ | A two-sided ideal |
| $AS$, $SA$ | The left ideal and the right ideal generated by $S$ |
| $(S)$, $(a)$ | The two-sided ideal generated by $S$, by $a$; $(a) = AaA$ |
| $I + J$, $IJ$, $I \cap J$ | Sum, product and intersection of ideals |
| $A/I$ | The quotient ring by a two-sided ideal |
| $\pi$ | The quotient homomorphism $A \to A/I$ |
| $\mathfrak{p}$, $\mathfrak{m}$ | A prime ideal, a maximal ideal |
| $E_{11}$, $M_n(F)$ | A matrix unit, and the matrix ring, the standard non-commutative example |
| reduced | Having no nonzero nilpotent element, of *Reduced Rings and the Nilradical* |

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for the axioms, ideals and quotient rings, with matrices as the standard non-commutative example.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the correspondence and isomorphism theorems for rings.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for subrings, homomorphisms, one-sided and two-sided ideals and the quotient constructions.
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the non-commutative examples and the elementary properties of rings.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the axioms, the prime subring and the multiplicative vocabulary.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for one-sided and two-sided ideals, units, nilpotents and idempotents in the non-commutative setting.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for ideals, quotients and the isomorphism theorems.
