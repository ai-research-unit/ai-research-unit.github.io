# __Ordered Fields__

## Introduction

An ordered field is a field equipped with a total order that is compatible with addition and multiplication. The compatibility has strong algebraic consequences: the field has characteristic $0$, it contains a canonical copy of $\mathbb{Q}$, every nonzero square is positive, and the positive elements form a cone closed under addition and multiplication. The extra structure that distinguishes one ordered field from another is whether the natural numbers are bounded above, and this **Archimedean** condition turns out to be equivalent to the density of $\mathbb{Q}$ and to embeddability into $\mathbb{R}$.

This article develops ordered rings and fields, the positive cone that encodes the order, the order topology in the elementary form needed here, and the Archimedean and non-Archimedean cases, with $\mathbb{Q}$ and $F(t)$ as the two standard examples. The completion theory and the theory of real-closed fields are the subjects, and the general theory of topological rings is; here the topology is used only to record the compatibility of the order with the field operations.

Throughout, an ordered field is written $F$ and its order $\leq$. The axioms of an ordered field are stated from scratch, so no prior theory of order is assumed; the theory of fields, characteristic, and prime fields is from *Fields*, and divisibility is from *Integral Domains*.

---

## Ordered Rings and Fields

### Definitions

**Definition.** An **ordered ring** is a commutative ring $R$ with $1 \neq 0$ together with a total order $\leq$ such that for all $a, b, c \in R$:

**(O1)** if $a \leq b$ then $a + c \leq b + c$;

**(O2)** if $a \geq 0$ and $b \geq 0$ then $ab \geq 0$.

An **ordered field** is an ordered ring that is a field.

The order is **translation invariant** by (O1) and **multiplication by nonnegative elements is monotone** by (O2), in the following precise sense.

**Proposition.** Let $R$ be an ordered ring and $a, b, c, d \in R$.

**(a)** If $a \leq b$ and $c \leq d$ then $a + c \leq b + d$.

**(b)** If $a \leq b$ and $c \geq 0$ then $ac \leq bc$. If $a \leq b$ and $c \leq 0$ then $ac \geq bc$.

**(c)** $a \leq b$ if and only if $b - a \geq 0$.

**(d)** $0 \leq a \leq b$ implies $a^2 \leq b^2$ and $a^2 \leq ab$.

**Proof.** (a) Apply (O1) twice. (b) If $c \geq 0$ then $bc - ac = (b-a)c \geq 0$ by (O2). If $c \leq 0$ then $-c \geq 0$ and $(b-a)(-c) \geq 0$, so $ac \geq bc$. (c) Translate by $-a$. (d) Multiply $a \leq b$ by $a \geq 0$ to get $a^2 \leq ab$, and by $b \geq 0$ to get $ab \leq b^2$. $\square$

### Basic Rules

**Theorem.** Let $F$ be an ordered field.

**(a)** $1 > 0$, and $\operatorname{char} F = 0$.

**(b)** $a^2 > 0$ for every $a \neq 0$, so every nonzero square is positive; in particular negative elements have no square root.

**(c)** $x > 0$ implies $x^{-1} > 0$, and $0 < x < y$ implies $0 < y^{-1} < x^{-1}$.

**(d)** If $a < b$ then there are elements strictly between them, for instance $a < \tfrac{a+b}{2} < b$.

**(e)** $-1$ is not a sum of squares; equivalently $F$ is **formally real**.

**Proof.** (a) $1 = 1^2 \geq 0$ by (O2), and $1 \neq 0$; if $1 \leq 0$ then $1 \geq 0$ and $1 \leq 0$ force $1 = 0$, a contradiction, so $1 > 0$. Hence $n \cdot 1 = 1 + \cdots + 1 > 0$ for every $n \geq 1$ by (a) and (a) of the proposition, so no positive integer is $0$ and the characteristic is $0$.

(b) If $a > 0$ then $a^2 = a \cdot a > 0$ by (O2) and $a \neq 0$; if $a < 0$ then $-a > 0$ and $a^2 = (-a)^2 > 0$. If $a^2 = 0$ then $a = 0$ as $F$ is a field.

(c) Since $x x^{-1} = 1 > 0$ and $x > 0$, the inverse cannot be $\leq 0$, because then $x x^{-1} \leq 0$ by (b) of the proposition. Hence $x^{-1} > 0$. If $0 < x < y$ then multiplying by $x^{-1}y^{-1} > 0$ gives $y^{-1} < x^{-1}$.

(d) $2 = 1 + 1 > 0$, so $2^{-1} > 0$ by (c), and $a = \tfrac{a+a}{2} < \tfrac{a+b}{2} < \tfrac{b+b}{2} = b$.

(e) If $-1 = \sum_i a_i^2$ then the right side is a sum of nonnegative elements, hence $\geq 0$; so $-1 \geq 0$, whence $1 \leq 0$, contradicting (a). $\square$

**Remark (the boundary of the theory).** Property (e) is what makes the orderable fields a special class among the fields of characteristic $0$: a field that is not formally real admits no ordering at all, since a sum of squares can never be negative in an ordered field. Conversely, every formally real field is orderable, so the two classes coincide.

**Theorem (Artin–Schreier).** A field $F$ admits an ordering if and only if it is formally real.

**Proof sketch.** An ordered field is formally real by (e). Conversely, suppose $-1$ is not a sum of squares, and let $\mathcal{T}$ be the collection of subsets $T \subseteq F$ that contain every square, are closed under addition and under multiplication, and satisfy $-1 \notin T$. It is nonempty, because the set of sums of squares lies in it, and it is closed under unions of chains, so Zorn's lemma gives a maximal $T$. Maximality forces $F = T \cup (-T)$: if $a \notin T \cup (-T)$, the set $T + aT = \{x + ay : x, y \in T\}$ contains $T$, contains every square because $T$ does, and is closed under addition and under multiplication because $a^2 \in T$; since it contains $a = 0 + a\cdot 1$, it contains $T$ properly, so by maximality $-1 \in T + aT$, and the same argument with $-a$ in place of $a$ gives $-1 \in T - aT$. Writing $-1 = x_1 + ay_1 = x_2 - ay_2$ with $x_i, y_i \in T$ and $y_i \neq 0$, multiply the first equation by $y_2^2$ and the second by $y_1^2$: the first becomes $a y_1 y_2^2 = -(y_2^2 + x_1 y_2^2) \in -T$, and the second becomes $a y_1^2 y_2 = y_1^2 + x_2 y_1^2 \in T$. Multiplying the first of these by $y_1^2 y_2 \in T$ and the second by $y_1 y_2^2 \in T$ gives the same element $t = a\, y_1^3 y_2^3$, which is therefore nonzero and lies in both $T$ and $-T$. Then $-1 = (-t^2)(t^{-1})^2 \in T$, because $T$ contains every square and is closed under multiplication, a contradiction. Hence $F = T \cup (-T)$, and $T \cap (-T) = \{0\}$ by the same computation applied to an element of the intersection. Therefore $P = T \setminus \{0\}$ satisfies (C1), (C2) and (C3) of the next section, and the theorem proved there produces an ordering of $F$ with positive cone $P$. $\square$

---

## Cones and Positivity

### The Positive Cone

**Definition.** The **positive cone** of an ordered field $F$ is

$$
P = \{x \in F : x > 0\}.
$$

**Theorem.** The positive cone $P$ of an ordered field satisfies

**(C1)** $P + P \subseteq P$;

**(C2)** $P \cdot P \subseteq P$;

**(C3)** $F$ is the disjoint union $F = (-P) \cup \{0\} \cup P$.

Conversely, if a subset $P \subseteq F$ of a field $F$ satisfies (C1), (C2), (C3), then the relation

$$
a \leq_P b \iff b - a \in P \cup \{0\}
$$

is a total order making $F$ an ordered field with positive cone $P$.

**Proof.** (C1): if $a > 0$ and $b > 0$ then $a + b > a > 0$ by (O1). (C2) is (O2). (C3) is trichotomy for a total order. Conversely, $\leq_P$ is total and antisymmetric by (C3), and transitive because $P \cup \{0\}$ is closed under addition by (C1). Translation invariance: $b - a = (b+c)-(a+c)$. Multiplicativity (O2): if $b - a \in P \cup \{0\}$ and $c \in P \cup \{0\}$ then $(b-a)c \in P \cup \{0\}$ by (C1) and (C2). Hence $\leq_P$ satisfies (O1) and (O2), with positive cone exactly $P$ by (C3). $\square$

**Corollary.** An ordering of a field is equivalent to the choice of a subset $P$ satisfying (C1), (C2), (C3). The notions "$F$ is orderable", "there is a total order compatible with the field structure", and "there is a positive cone in $F$" coincide.

**Proposition.** Let $F$ be an ordered field.

**(a)** Every sum of squares is $\geq 0$, and a sum of squares is $0$ only if every term is $0$.

**(b)** Every element of $F$ is a difference of two squares.

**(c)** The set of nonzero squares is contained in $P$, and it equals $P$ if and only if every positive element of $F$ has a square root in $F$; every real-closed field satisfies this, but the condition is strictly weaker than real closedness.

**Proof.** (a) Each square is $\geq 0$ by the basic-rules theorem, a sum of nonnegative elements is $\geq 0$, and a sum of nonnegative elements is $0$ only if every term is $0$, since a positive term would make the sum positive. (b) In characteristic $\neq 2$, and here $\operatorname{char} F = 0$,

$$
x = \left(\frac{x+1}{2}\right)^2 - \left(\frac{x-1}{2}\right)^2 .
$$

(c) If $x = a^2 \neq 0$ then $x > 0$, and the converse holds by hypothesis; for the rationals, $2 = 1^2 + 1^2$ is positive and is not a square, so the inclusion of nonzero squares in $P$ is strict there. $\square$

**Remark.** Positivity is a cone condition, not a square condition: in $\mathbb{Q}$ the positive element $2$ is not a square, although it is a sum of squares. The equality $P = \{$nonzero squares$\}$ is a genuine strengthening of the ordered-field axioms; a real-closed field satisfies it.

---

## The Order Topology

### Definition

**Definition.** Let $F$ be an ordered field. The **order topology** on $F$ is the topology with basis the open intervals

$$
(a, b) = \{x \in F : a < x < b\}, \qquad a, b \in F,\ a < b.
$$

The rays $(a, \infty) = \{x : x > a\}$ and $(-\infty, a) = \{x : x < a\}$ are also open, being unions of intervals — $(a, \infty) = \bigcup_{b > a} (a,b)$, since $x + 1 > x$ for every $x$ — and they occur as basis elements in the usual description of the topology of $\mathbb{R}$; the bounded intervals alone already generate the same topology.

**Theorem.** With the order topology, an ordered field $F$ is a **topological field**: the maps

$$
(x, y) \mapsto x + y, \qquad x \mapsto -x, \qquad (x,y) \mapsto xy, \qquad x \mapsto x^{-1} \ (\text{on } F^\times)
$$

are continuous, and $F$ is a Hausdorff space.

**Proof.** Continuity of addition and negation follows from translation invariance: the preimage of $(a,b)$ under $x \mapsto x+c$ is $(a-c, b-c)$, an open interval, and addition is continuous jointly by the estimate that $x' \in (x - \epsilon, x+\epsilon)$ and $y' \in (y - \epsilon, y+\epsilon)$ give $x'+y' \in (x+y-2\epsilon, x+y+2\epsilon)$. Continuity of multiplication uses $x'y' - xy = x'(y'-y) + y(x'-x)$ and the local boundedness of $x'$ and $y$; continuity of inversion on $F^\times$ follows from $x^{-1} - y^{-1} = (y - x)(xy)^{-1}$ and the continuity of multiplication, since $xy$ is bounded away from $0$ near a nonzero point. Hausdorffness: if $x < y$ then $\tfrac{x+y}{2}$ satisfies $x < \tfrac{x+y}{2} < y$, and the open rays $(-\infty, \tfrac{x+y}{2})$ and $(\tfrac{x+y}{2}, \infty)$ are disjoint neighborhoods of $x$ and $y$ respectively. $\square$

**Corollary.** The order topology on $\mathbb{Q}$ is the usual metric topology, with basis the intervals with rational endpoints, and every rational point has a countable neighborhood basis. The same holds for $\mathbb{R}$. The general theory, including uniformity, completeness and the analogue for valued fields, is developed .

---

## Archimedean Ordered Fields

### Definition and Equivalent Conditions

**Definition.** An ordered field $F$ is **Archimedean** if for every $x \in F$ there is a positive integer $n$ with

$$
n \cdot 1 > x.
$$

Equivalently, the set $\{n \cdot 1 : n \geq 1\}$ is unbounded above in $F$.

**Theorem.** For an ordered field $F$ the following are equivalent.

**(a)** $F$ is Archimedean.

**(b)** For every $\epsilon > 0$ there is $n \geq 1$ with $1/n < \epsilon$.

**(c)** $\mathbb{Q}$ is dense in $F$: for all $a < b$ in $F$ there is $q \in \mathbb{Q}$ with $a < q < b$.

**(d)** There is no element $x \in F$ with $x > n$ for all $n \geq 1$, and no element $x > 0$ with $x < 1/n$ for all $n \geq 1$.

**Proof.** (a) $\Rightarrow$ (b): apply (a) to $x = 1/\epsilon$. (b) $\Rightarrow$ (a): given $x > 0$, take $n$ with $1/n < 1/x$, i.e. $n > x$. So (a) and (b) are equivalent, and they are negated exactly by the existence of an element as in (d).

(b) $\Rightarrow$ (c): given $a < b$, first choose $n$ with $1/n < b - a$; then the multiples $k/n$ form a chain of step $1/n < b-a$, so some $k$ has $k/n \leq a < (k+1)/n \leq a + 1/n < b$, and $(k+1)/n \in \mathbb{Q}$ lies in $(a,b)$.

(c) $\Rightarrow$ (b): if $\mathbb{Q}$ is dense and $\epsilon > 0$, the interval $(0,\epsilon)$ contains a rational $q$ with $q > 0$; writing $q = m/n$ with $m \geq 1$ gives $1/n \leq m/n = q < \epsilon$. $\square$

**Corollary.** Every Archimedean ordered field contains $\mathbb{Q}$ as an ordered subfield, and in an Archimedean ordered field every element is the supremum of the rationals below it and the infimum of the rationals above it.

**Proof.** Containment of $\mathbb{Q}$ is the basic-rules theorem; density is (c); the last statement is the definition of density together with the order. $\square$

### Non-Archimedean Examples

**Example ($F(t)$ with $t$ infinite).** Let $F$ be an ordered field, let $F(t)$ be the rational function field, and define for a nonzero $r \in F(t)$

$$
r > 0 \iff \text{the leading coefficient of } r \text{ is positive},
$$

where $r$ is written as a quotient of polynomials and the leading coefficient is that of the quotient of the leading coefficients. This makes $F(t)$ an ordered field in which $t > q$ for every $q \in F$; in particular $t$ exceeds every integer, so $F(t)$ is non-Archimedean, and $1/t$ is a positive **infinitesimal**: $0 < 1/t < 1/n$ for every $n \geq 1$.

**Example (formal Laurent series).** The field of formal Laurent series

$$
F((t)) = \left\{\sum_{k \geq k_0} a_k t^k : k_0 \in \mathbb{Z},\ a_k \in F\right\}
$$

is ordered lexicographically by the lowest-degree nonzero coefficient: $\sum a_k t^k > 0$ if the least $k$ with $a_k \neq 0$ has $a_k > 0$. Then $t$ is a positive infinitesimal and $t^{-1}$ is infinite, so $F((t))$ is non-Archimedean. This ordering is the one induced by the $t$-adic valuation: it orders the subfield $F(t)$ by making $t$ infinitesimal, and $F((t))$ is the completion of $F(t)$ for that valuation in the sense. It is therefore a different ordering from the one of the previous example, in which $t$ is infinite, and the two fields are different as well — for $F = \mathbb{Q}$ the series field is uncountable while the rational function field is countable. The field $F((t))$ is complete as a valued field, but it is not order-complete: an order-complete ordered field is Archimedean, and $t$ is an infinitesimal here.

**Example (non-Archimedean vs not-formally-real).** The ordering of $F(t)$ above is one of many orderings; the field $\mathbb{C}$ has none, and $\mathbb{Q}(\sqrt2)$ has exactly two, one with $\sqrt2 > 0$ and one with $\sqrt2 < 0$. The number of orderings of a field is the subject of the theory of formally real fields and is not needed here.

---

## The Rational Numbers as an Ordered Field

### The Prime Field

**Theorem.** Every ordered field $F$ contains a unique subfield isomorphic to $\mathbb{Q}$, and the order induced on it is the usual order of $\mathbb{Q}$. Consequently $\mathbb{Q}$ is, up to isomorphism of ordered fields, the smallest ordered field.

**Proof.** By the basic-rules theorem, $\operatorname{char} F = 0$, so the map $\mathbb{Z} \to F$, $n \mapsto n \cdot 1$, is injective and extends to an embedding $\mathbb{Q} \to F$ by the universal property of the fraction field. Since $n \cdot 1 > 0$ for $n \geq 1$ and inverses of positive elements are positive, the embedding carries positive rationals to positive elements and negatives to negatives; hence it is order-preserving and its image is the prime field. Uniqueness: any subfield isomorphic to $\mathbb{Q}$ contains the prime field, which is exactly the image of this embedding. $\square$

**Theorem.** $\mathbb{Q}$ has exactly one ordering, and relative to it $\mathbb{Q}$ is Archimedean.

**Proof.** In any ordering of $\mathbb{Q}$, the element $1 > 0$ by the basic-rules theorem, so $n > 0$ for all positive integers $n$, and the order on $\mathbb{Q}$ is determined by the positive cone, which is then forced: a rational $m/n$ is positive exactly when $mn > 0$ in the usual sense. Hence the ordering is unique. It is Archimedean: for a rational $x$, choose an integer $k > \lvert x \rvert$, which exists by the well-ordering of $\mathbb{N}$, and then $k \cdot 1 = k > x$. $\square$

**Remark.** The uniqueness of the ordering of $\mathbb{Q}$ contrasts with the general case: $\mathbb{Q}(\sqrt2)$ has two orderings and $\mathbb{Q}(t)$ has many, one for each way of specifying the sign of $t$ together with a location for $t$ relative to the rationals. The orderings of a field are the points of a compact space, the real spectrum, whose theory belongs to real algebraic geometry.

---

## Embeddings and Order

### Order-Preserving Maps

**Definition.** An **order-preserving** map of ordered fields (or of ordered sets) $\varphi : F \to K$ satisfies $x \leq y \implies \varphi(x) \leq \varphi(y)$. An **ordered-field embedding** is an injective field homomorphism that is order-preserving, and its image is then an ordered subfield.

**Proposition.** Let $F$ and $K$ be ordered fields and let $\sigma : F \to K$ be a field homomorphism such that $x > 0$ in $F$ implies $\sigma(x) > 0$ in $K$. Then $\sigma$ is strictly order-preserving and injective. In particular, the embedding of the prime field $\mathbb{Q}$ into any ordered field is order-preserving.

**Proof.** If $x < y$ then $y - x > 0$, so $\sigma(y) - \sigma(x) = \sigma(y-x) > 0$ and $\sigma(x) < \sigma(y)$; hence $\sigma$ is strictly order-preserving. If $\sigma(x) = \sigma(y)$ with $x \neq y$, then either $x < y$, giving $\sigma(x) < \sigma(y)$, or $x > y$, giving $\sigma(x) > \sigma(y)$, a contradiction; so $\sigma$ is injective. On the prime field, $\sigma(n \cdot 1) = n \cdot 1 > 0$ for $n \geq 1$ and $\sigma(1/n) = \sigma(n)^{-1} > 0$, so positive rationals go to positive elements. $\square$

**Remark.** A field homomorphism between ordered fields need not be order-preserving. The nontrivial automorphism of $\mathbb{Q}(\sqrt2)$, namely $\sqrt2 \mapsto -\sqrt2$, with the ordering $\sqrt2 > 0$, sends the positive element $\sqrt2$ to the negative element $-\sqrt2$; it is an automorphism of the field but not of the ordered structure. The automorphisms of an ordered field, meaning order-preserving automorphisms, form a subgroup of $\operatorname{Aut}(F)$; for $\mathbb{Q}$ and for $\mathbb{R}$ this subgroup is trivial.

### Archimedean Fields Embed in $\mathbb{R}$

**Theorem.** Let $F$ be an Archimedean ordered field. Then the map

$$
\Phi : F \to \mathbb{R}, \qquad \Phi(x) = \sup\{q \in \mathbb{Q} : q < x\},
$$

is an injective order-preserving field homomorphism; hence $F$ is isomorphic, as an ordered field, to a subfield of $\mathbb{R}$.

**Proof sketch.** The set on the right is a nonempty bounded-above subset of $\mathbb{Q}$ because $F$ is Archimedean, and it defines a real number; the map is order-preserving by construction, additive and multiplicative by the arithmetic of suprema of bounded sets of rationals, and its kernel is $0$ because $\Phi(x) = 0$ forces $\{q : q < x\}$ to be the nonpositive rationals, so $x = 0$. $\square$

**Corollary.** Up to ordering-preserving isomorphism, the Archimedean ordered fields are exactly the subfields of $\mathbb{R}$, and $\mathbb{Q}$ is the smallest and $\mathbb{R}$ the largest: every Archimedean ordered field embeds as an ordered subfield of $\mathbb{R}$, and every ordered subfield of $\mathbb{R}$ is Archimedean.

**Proof.** The second statement is that $\mathbb{R}$ is Archimedean, which follows from its construction and is proved in *The Real Numbers*; the first is the theorem. $\square$

**Remark.** The theorem separates the two questions of this article and the next. Whether a field embeds in $\mathbb{R}$ is the Archimedean condition; whether it *is* $\mathbb{R}$ is a completeness condition, and completeness is treated. The rationals are Archimedean but not complete; the real numbers are Archimedean and complete; and $F(t)$ is neither.

---

## Summary

An ordered ring is a commutative ring with a total order compatible with addition and multiplication, and an ordered field is an ordered ring that is a field. In an ordered field $1 > 0$, the characteristic is $0$, every nonzero square is positive, inverses of positive elements are positive, the order is dense, and $-1$ is not a sum of squares; the last condition is formal reality, and a field is orderable exactly when it is formally real (Artin–Schreier). An ordering is equivalent to a choice of positive cone $P$, a subset closed under addition and multiplication and making $F = (-P) \cup \{0\} \cup P$ a disjoint union; equivalently the order is determined by the positive cone, and every element of a field of characteristic different from $2$ is a difference of squares.

The order topology has the open intervals as a basis, makes the field a Hausdorff topological field, and agrees with the usual topology on $\mathbb{Q}$ and $\mathbb{R}$; the general theory of topological fields is. An ordered field is Archimedean when the natural numbers are unbounded, equivalently when $\mathbb{Q}$ is dense, equivalently when every positive element exceeds some $1/n$, equivalently when there is no infinite element and no infinitesimal; $F(t)$ ordered by leading coefficients and $F((t))$ ordered lexicographically are the standard non-Archimedean examples, with $t$ infinite in the former and infinitesimal in the latter. Every ordered field contains a unique copy of $\mathbb{Q}$ as its prime field, with the unique ordering of $\mathbb{Q}$, and every Archimedean ordered field embeds as an ordered subfield of $\mathbb{R}$, so the Archimedean ordered fields are exactly the subfields of $\mathbb{R}$.

| Ordered field | Archimedean | $\mathbb{Q}$ dense | Contains infinitesimals |
|---|---|---|---|
| $\mathbb{Q}$ | yes | yes | no |
| $\mathbb{R}$ | yes | yes | no |
| $\mathbb{Q}(\sqrt2)$ | yes | yes | no |
| $F(t)$, $t$ infinite | no | no | yes |
| $F((t))$, $t$ infinitesimal | no | no | yes |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $K$ | Ordered fields |
| $R$ | Ordered ring |
| $\leq$ | Total order compatible with the field operations |
| $P = \{x : x > 0\}$ | Positive cone |
| $(a,b)$ | Open interval, basis element of the order topology |
| $n \cdot 1$ | Integer multiple of the identity, $n \in \mathbb{Z}$ |
| $\mathbb{Q}$ | Prime field of every ordered field; uniquely ordered |
| $\mathbb{R}$ | Largest Archimedean ordered field (complete) |
| $F(t)$ | Rational function field, ordered by leading coefficients |
| $F((t))$ | Formal Laurent series field, ordered lexicographically |
| $\operatorname{char} F$ | Characteristic of $F$; equals $0$ if $F$ is ordered |
| $\operatorname{Frac}(R)$ | Fraction field |
| $\sup$, $\inf$ | Supremum, infimum in an ordered set |



## Further Reading

- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for ordered fields, formally real fields and the Artin–Schreier theorem.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for ordered rings, positive cones and the order topology.
- Alexander Prestel and Charles N. Delzell, *Positive Polynomials* (Springer, 2001), for the real spectrum and the orderings of a field.
- Norman L. Alling, *Foundations of Analysis over Surreal Number Fields* (North-Holland, 1987), for non-Archimedean ordered fields and formal power series.
- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for the order topology, its basis of open intervals, and the topological properties of $\mathbb{Q}$ and $\mathbb{R}$.
