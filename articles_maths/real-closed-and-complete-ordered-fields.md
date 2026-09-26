# __Real-Closed and Complete Ordered Fields__

## Introduction

Two independent conditions single out the field of real numbers among ordered fields. The first is **real closedness**, an algebraic condition: the field is ordered, every positive element is a square, and every polynomial of odd degree has a root. The second is **order completeness**, a condition on the ordering: every nonempty subset that is bounded above has a least upper bound. Real closedness describes the *algebraic* shape of $\mathbb{R}$ and is inherited by the field of real algebraic numbers, which is countable; order completeness describes its *analytic* shape and is not inherited by any proper subfield. Each condition characterises $\mathbb{R}$ together with an additional hypothesis: an order-complete ordered field is $\mathbb{R}$ up to isomorphism, and a real-closed field whose ordering is order-complete and whose rationals are dense in it is also $\mathbb{R}$.

This article develops both notions, proves that a real-closed field has a unique ordering determined by its field structure, constructs the **real closure** of an ordered field and proves its uniqueness, and proves the uniqueness of $\mathbb{R}$ as the order-complete ordered field. The relation between real closedness and algebraic closedness is settled by showing that $F(i)$ is algebraically closed whenever $F$ is real closed.

Throughout, $F$ is an ordered field with positive cone $P$ as in *Ordered Fields*, and $F^{rc}$ denotes a real closure. The reader should not confuse the real closure $F^{rc}$, which is an algebraic extension, with the topological completion of $F$, which is not; the two constructions are compared in the final section.

---

## Real-Closed Fields

### Definition

**Definition.** An ordered field $F$ is **real closed** if

**(RC1)** every positive element of $F$ is a square in $F$, and

**(RC2)** every polynomial in $F[x]$ of odd degree has a root in $F$.

**Theorem.** A field $F$ is real closed if and only if it is formally real and admits no proper algebraic extension that is formally real. Equivalently, $F$ is real closed if and only if $F$ has an ordering and no proper algebraic extension of $F$ can be ordered.

**Proof sketch.** If $F$ is real closed and $K/F$ is a proper algebraic extension, then $K$ contains an element $\alpha$ of degree $> 1$ over $F$; its minimal polynomial has even degree (otherwise (RC2) gives a root in $F$, contradicting the choice of $\alpha$), and an argument with (RC1) shows that $-1$ is a sum of squares in $K$, so $K$ is not formally real. Conversely, if $F$ is formally real and has no proper formally real algebraic extension, then every positive element of $F$ has a square root (else adjoining a square root is a proper formally real extension by the standard analysis of $x^2 - a$ with $a > 0$), and every odd-degree polynomial has a root (else an odd-degree extension of $F$ can be ordered, by the standard ordering-extension lemma for an irreducible polynomial of odd degree). $\square$

### Equivalent Conditions

**Theorem.** For an ordered field $F$ the following are equivalent.

**(a)** $F$ is real closed.

**(b)** $F(i)$ is algebraically closed, where $i^2 = -1$.

**(c)** $F$ has no proper algebraic extension that is formally real, and $F$ is formally real.

**(d)** $F$ is elementarily equivalent to $\mathbb{R}$: every first-order statement in the language of ordered fields is true in $F$ if and only if it is true in $\mathbb{R}$.

**Proof sketch.** (a) $\Leftrightarrow$ (c) is the theorem above. (a) $\Rightarrow$ (b) is the algebraic-closedness theorem proved below. (b) $\Rightarrow$ (a): if $F(i)$ is algebraically closed, then $F$ is not algebraically closed itself (as $x^2+1$ has no root in $F$) and $F$ is real closed by the standard result that a field whose extension by a square root of $-1$ is algebraically closed is real closed. (d) is Tarski's theorem on the completeness of the theory of real-closed fields: the axioms of an ordered field together with (RC1) and (RC2) are first-order and true in every real-closed field, and any two real-closed fields are elementarily equivalent, so a first-order sentence holds in one if and only if it holds in all. $\square$

**Proposition.** If $F$ is real closed, then its positive cone is the set of nonzero squares, $P = \{a^2 : a \in F^\times\}$; consequently a real-closed field carries a unique ordering, and that ordering is determined by the field structure. Every field isomorphism between real-closed fields is order-preserving.

**Proof.** (RC1) says that every positive element is a square, so $P \subseteq \{a^2 : a \in F^\times\}$, and every nonzero square is positive by the ordered-field axioms, so equality holds. The cone is therefore intrinsic to the field, and there is only one ordering of $F$; an isomorphism of fields carries squares to squares, hence carries the cone of one field onto the cone of the other, and so preserves the order. $\square$

**Remark (the square condition is not equivalent to real closedness).** An ordered field in which every positive element is a square is called **Euclidean**, and every real-closed field is Euclidean by the proposition above, but the converse fails. The field of real numbers constructible from $\mathbb{Q}$ by straightedge and compass is Euclidean, since a square root of a positive constructible number is constructible; it is not real closed, because every constructible number has degree a power of $2$ over $\mathbb{Q}$, while $\sqrt[3]{2}$ has degree $3$, so $\sqrt[3]{2}$ is not constructible and $x^3 - 2$ has no root in the field. What the equivalence (a) $\Leftrightarrow$ (b) above adds to the square condition is exactly the algebraic closedness of $F(i)$, which fails here.

### Examples

| Ordered field | Real closed | Reason |
|---|---|---|
| $\mathbb{R}$ | yes | every positive real is a square; odd-degree real polynomials have real roots |
| $\overline{\mathbb{Q}} \cap \mathbb{R}$ (real algebraic numbers) | yes | real closure of $\mathbb{Q}$ |
| real closure of $\mathbb{R}(t)$, $t$ infinite | yes | real closure of an ordered field is real closed |
| $\mathbb{Q}$ | no | $2$ is not a square |
| $\mathbb{Q}(\sqrt2)$ | no | $3$ is not a square in $\mathbb{Q}(\sqrt2)$ |
| $F(t)$ with $t$ infinite | no | $t$ is not a square |
| $\mathbb{C}$ | no | not formally real |

The table separates the two phenomena: $\mathbb{R}$ and the real algebraic numbers are both real closed, one uncountable and one countable, so real closedness does not determine the cardinality.

---

## The Real Closure

### Definition

**Definition.** Let $F$ be an ordered field. A **real closure** of $F$ is an ordered field $F^{rc}$ together with an order-preserving embedding $F \hookrightarrow F^{rc}$ such that $F^{rc}$ is algebraic over $F$ and real closed.

**Theorem (Artin–Schreier).** Every ordered field has a real closure, and any two real closures of $F$ are isomorphic by a unique isomorphism fixing $F$ pointwise and preserving the order.

**Proof sketch.** By Zorn's lemma take an algebraic extension of $F$ that is maximal with respect to being orderable, which exists because the union of a chain of orderable algebraic extensions is orderable; a maximal such extension has no proper orderable algebraic extension, hence is real closed by the characterization above. Uniqueness: given two real closures, the isomorphism between the algebraic extensions is constructed by the usual step-by-step extension of the identity on $F$ to the roots of irreducible polynomials, and it is order-preserving because the order in a real-closed field is determined by the field structure, by the corollary above. $\square$

**Example.** The real closure of $\mathbb{Q}$ is the field of real algebraic numbers $\overline{\mathbb{Q}} \cap \mathbb{R}$, the field of real roots of polynomials with rational coefficients. It is countable, Archimedean, and real closed, but it is not order-complete: the set

$$
A = \{x \in \overline{\mathbb{Q}} \cap \mathbb{R} : x < \pi\}
$$

is nonempty and bounded above by $4$, and its supremum in $\mathbb{R}$ is $\pi$, since $\mathbb{Q} \subseteq A$ is dense in $\mathbb{R}$; if $A$ had a supremum $s$ in $\overline{\mathbb{Q}} \cap \mathbb{R}$, then $s$ would equal the real supremum $\pi$, contradicting the transcendence of $\pi$. So $A$ has no least upper bound in the real algebraic numbers.

**Example.** The real closure of $\mathbb{R}(t)$ with $t$ infinite is a real-closed field of generalized Puiseux series; it is not a subfield of $\mathbb{R}$, in contrast to the real closure of any ordered subfield of $\mathbb{R}$.

### Real Closure versus Algebraic Closure

**Theorem.** Let $F$ be an ordered field with real closure $F^{rc}$ and algebraic closure $\overline{F}$. Then

$$
\overline{F} = F^{rc}(i), \qquad i^2 = -1, \qquad [\overline{F} : F^{rc}] = 2 .
$$

Thus the algebraic closure of a real-closed field is obtained by adjoining a single square root of $-1$. In particular, for $F = \mathbb{R}$ one has $\overline{F} = \mathbb{C} = \mathbb{R}(i)$.

**Proof.** The field $F^{rc}$ is real closed, so $F^{rc}(i)$ is algebraically closed by the theorem on algebraic closedness of $F(i)$ below, and it is algebraic over $F$ because $F^{rc}$ is. Since it contains $F$, the embedding $F^{rc}(i) \to \overline{F}$ fixing $F$ is an isomorphism, and $i \notin F^{rc}$ because a formally real field contains no square root of $-1$. Hence the degree is $2$. $\square$

---

## Order Completeness

### Dedekind Completeness

**Definition.** An ordered field $F$ is **order-complete** (or **Dedekind-complete**) if every nonempty subset $A \subseteq F$ that is bounded above has a least upper bound $\sup A$ in $F$. Equivalently (applying the condition to $-A$), every nonempty subset bounded below has a greatest lower bound.

**Proposition.** Every order-complete ordered field is Archimedean.

**Proof.** Suppose $F$ is not Archimedean. Then the set $A = \{n \cdot 1 : n \geq 1\}$ is nonempty and bounded above, so it has a supremum $s = \sup A$. Since $n \cdot 1 \leq s$ for all $n$, also $(n+1) \cdot 1 \leq s$ for all $n$, hence $n \cdot 1 \leq s - 1$ for all $n$, so $s - 1$ is an upper bound of $A$ strictly smaller than $s$, contradicting the definition of $s$. Hence $F$ is Archimedean. $\square$

**Theorem (equivalent formulations).** For an ordered field $F$ the following are equivalent.

**(a)** $F$ is order-complete: every nonempty subset bounded above has a supremum.

**(b)** Every nonempty subset bounded below has an infimum.

**(c)** Every **Dedekind cut** of $F$ is realized in $F$: for every partition $F = A \cup B$ with both parts nonempty and $a < b$ for all $a \in A$, $b \in B$, either $A$ has a greatest element or $B$ has a least element.

**Proof.** (a) $\Leftrightarrow$ (b): negating all elements turns upper bounds into lower bounds and suprema into infima. (a) $\Rightarrow$ (c): given a cut $(A,B)$, the set $A$ is nonempty and bounded above by any element of $B$, so $s = \sup A$ exists; then either $s \in A$ and $s$ is the greatest element of $A$, or $s \in B$, and $s$ is a lower bound of $B$ while no element of $B$ is smaller, so $s$ is the least element of $B$. (c) $\Rightarrow$ (a): given a nonempty $A$ bounded above, if $A$ has a greatest element then that element is $\sup A$. Otherwise let $B$ be the set of upper bounds of $A$; no element of $A$ is an upper bound, so $A \cap B = \emptyset$, both parts of the partition $(F \setminus B, B)$ are nonempty, and every element of $F \setminus B$ lies below every element of $B$. So (c) applies. No element of $F \setminus B$ is greatest: if $x$ is not an upper bound of $A$ then some $a \in A$ satisfies $x < a$, and that $a$ is again not an upper bound. Hence $B$ has a least element, which is the smallest upper bound of $A$, that is, $\sup A$. $\square$

### Density and the Least Upper Bound Property

**Theorem.** Let $F$ be an order-complete ordered field. Then $\mathbb{Q}$ is dense in $F$, and every element of $F$ is both the supremum of the rationals below it and the infimum of the rationals above it.

**Proof.** $F$ is Archimedean by the proposition, so $\mathbb{Q}$ is dense by the characterization of Archimedean fields in *Ordered Fields*. For $x \in F$, the set $A_x = \{q \in \mathbb{Q} : q < x\}$ is nonempty (as $F$ is Archimedean, $-n < x$ for $n$ large) and bounded above by $x$, so it has a supremum $s \leq x$. If $s < x$, density gives a rational $q$ with $s < q < x$, hence $q \in A_x$ and $q > s$, contradicting $s = \sup A_x$; so $s = x$. The statement for the infimum follows by applying the result to $-x$. $\square$

**Corollary.** In an order-complete ordered field, the rationals separate points and the order is the order generated by the embedding of $\mathbb{Q}$; consequently, if $F$ and $F'$ are order-complete ordered fields, any order-preserving isomorphism between their prime fields extends to at most one isomorphism $F \to F'$.

**Proof.** An order-preserving field isomorphism is determined by its values on $\mathbb{Q}$ together with the description of each element as a supremum of rationals, which is preserved. $\square$

---

## The Uniqueness of $\mathbb{R}$

### The Isomorphism Theorem

**Theorem (Cantor).** Any two order-complete ordered fields are isomorphic by a unique order-preserving field isomorphism.

**Proof sketch.** Let $F$ and $F'$ be order-complete ordered fields. Their prime fields are the images of $\mathbb{Q}$, and the unique ordering of $\mathbb{Q}$ is preserved, giving an isomorphism $\varphi_0$ of the prime subfields that is order-preserving. Extend $\varphi_0$ to a map $\varphi : F \to F'$ by

$$
\varphi(x) = \sup\{ \varphi_0(q) : q \in \mathbb{Q},\ q < x \},
$$

which is defined because $\varphi_0(A_x)$ is nonempty and bounded above in $F'$. The map is order-preserving and additive and multiplicative by the arithmetic of suprema, and its kernel is trivial; it is surjective because, given $y \in F'$, the element $x = \sup\{q \in \mathbb{Q} : \varphi_0(q) < y\}$ satisfies $\varphi(x) = y$ by the density of $\mathbb{Q}$ in both fields. Uniqueness holds because an order-preserving field map is determined by its restriction to $\mathbb{Q}$, hence to the dense subfield $\mathbb{Q}$, hence to $F$. $\square$

**Corollary (the real numbers are unique).** Up to a unique order-preserving field isomorphism there is exactly one order-complete ordered field, namely $\mathbb{R}$. In particular every complete ordered field is $\mathbb{R}$, and every order-complete ordered field contains $\mathbb{Q}$ densely and is isomorphic to $\mathbb{R}$.

**Corollary (characterisation by order).** $\mathbb{R}$ is Archimedean and order-complete; conversely an Archimedean order-complete ordered field is $\mathbb{R}$. Hence among ordered fields the field of real numbers is characterised by the least upper bound property.

**Remark (completeness does not follow from Archimedean).** The field $\mathbb{Q}$ is Archimedean but not order-complete: the set $\{q \in \mathbb{Q} : q > 0,\ q^2 < 2\}$ is nonempty and bounded above and has no supremum in $\mathbb{Q}$. The real closure $\overline{\mathbb{Q}} \cap \mathbb{R}$ is Archimedean and real closed but still not order-complete, for the same reason. Order completeness is a strictly stronger condition than Archimedean real closedness, and it is the condition that makes $\mathbb{R}$ unique.

### Real Closedness of $\mathbb{R}$

**Theorem.** $\mathbb{R}$ is real closed; equivalently, every positive real number is a square and every real polynomial of odd degree has a real root.

**Pro.** That every positive real has a square root is the completeness of $\mathbb{R}$ applied to the set $\{y \geq 0: y^2 \leq x\}$, which is nonempty and bounded above and whose supremum $\sqrt x$ satisfies $(\sqrt x)^2 = x$; the verification that the supremum has this property uses the order and the Archimedean property. For odd degree, a real polynomial $p$ of odd degree takes both signs, say $p(a) < 0 < p(b)$ with $a < b$ chosen far enough out, and the set $S = \{x \in (a,b): p < 0 \text{ on } (a,x]\}$ is nonempty and bounded above; its supremum $s \in (a,b]$ satisfies $p(s) = 0$, because polynomial functions are continuous for the order topology and both $p(s) < 0$ and $p(s) > 0$ contradict the definition of $s$. The case of negative leading coefficient is analogous. $\square$

**Theorem (fundamental theorem of algebra, real-closed form).** Let $F$ be a real-closed field and let $i^2 = -1$ in an algebraic closure. Then $F(i)$ is algebraically closed.

**Proof sketch.** One shows that every nonconstant polynomial over $F(i)$ has a root, reducing by conjugation to a real polynomial $p \in F[x]$ and then to $p\bar p$. By the odd-degree condition (RC2) applied to an auxiliary polynomial, one exhibits a root. The argument is the classical proof of the fundamental theorem of algebra in the real-closed setting and is given in the references. $\square$

**Corollary.** $\mathbb{C} = \mathbb{R}(i)$ is algebraically closed, and it is an algebraic closure of $\mathbb{R}$; the algebraic closure of the real algebraic numbers $\overline{\mathbb{Q}} \cap \mathbb{R}$ is the field $\overline{\mathbb{Q}}$ of algebraic numbers, which is a proper subfield of $\mathbb{C}$ because $\mathbb{C}$ is transcendental over $\mathbb{Q}$.

---

## Real Closure, Completion and $\mathbb{R}$

The two constructions of this article differ in a way worth recording.

| Construction | Input | Output | Extension type |
|---|---|---|---|
| Real closure $F^{rc}$ | ordered field $F$ | real-closed, algebraic over $F$ | algebraic |
| Order completion $\widehat{F}$ | ordered field $F$ | order-complete, containing $F$ densely | not algebraic in general |

**Proposition.** For an Archimedean ordered field $F$ the order completion $\widehat{F}$ is an order-complete ordered field containing $F$ as a dense subfield; it is unique up to a unique order-preserving $F$-isomorphism, and $\widehat{\mathbb{Q}} = \mathbb{R}$.

**Proof sketch.** The completion is constructed from the Dedekind cuts of $F$, ordered by inclusion, with the field operations defined by the arithmetic of cuts; the same construction applied to $\mathbb{Q}$ produces $\mathbb{R}$. Uniqueness is Cantor's theorem. $\square$

**Remark.** The Archimedean hypothesis is not removable. A non-Archimedean ordered field has a positive infinitesimal $\epsilon$, so $\{n\epsilon : n \geq 1\}$ is bounded above by $1$ and has a supremum $u$ in the Dedekind completion $\widehat{F}$. If $\widehat{F}$ were an ordered field, multiplication by $2$ would preserve suprema, and since $\{2n\epsilon : n \geq 1\}$ and $\{n\epsilon : n \geq 1\}$ are cofinal in one another,

$$
2u = \sup_{n \geq 1} 2n\epsilon = \sup_{n \geq 1} n\epsilon = u,
$$

forcing $u = 0$, although $u \geq \epsilon > 0$. Hence $\widehat{F}$ is a complete linear order containing $F$ densely but carries no field structure making it an ordered field extension of $F$: the completion row of the table above is an ordered field only in the Archimedean case.

**Corollary.** $\mathbb{R}$ is simultaneously the order completion of $\mathbb{Q}$ and the order completion of the real algebraic numbers. The real closure of $\mathbb{Q}$ is the smaller field $\overline{\mathbb{Q}} \cap \mathbb{R}$, and $\mathbb{R}$ is the order completion of that real closure.

**Remark.** The distinction is exactly the distinction between the algebraic and the order-theoretic content of the real numbers. The real closure of $\mathbb{Q}$ contains every real root of every rational polynomial and is countable; the completion adds the transcendental limits, and its construction requires the supremum principle. The companion articles *The Rational Numbers* and *The Real Numbers* carry out both constructions in full.

---

## The Cardinality of $\mathbb{R}$

**Theorem.** $|\mathbb{R}| = |\mathcal{P}(\mathbb{N})| = 2^{\aleph_0}$; in particular $\mathbb{R}$ is uncountable, and the cardinal $\mathfrak{c}$ of *Cardinality and the Axiom of Choice* is its cardinality.

**Proof sketch.** The identification $|\mathbb{R}| = |\mathcal{P}(\mathbb{N})|$ is the binary expansion: a real number has a binary expansion, which is a function $\mathbb{N} \to \{0,1\}$ modulo the ambiguity of the expansions ending in $1$s, and the standard reduction to the non-ambiguous expansions gives a bijection between $\mathbb{R}$ and a subset of $\mathcal{P}(\mathbb{N})$; order-completeness supplies the expansion, since each digit is decided by a bounded-above set, and Schröder–Bernstein, applied to the inclusion and to a suitable injection the other way, gives the equality. Uncountability is then immediate from Cantor's theorem. $\square$

**Remark.** The powers $\mathbb{R}^n$ are equipotent to $\mathbb{R}$, by interleaving binary expansions of the coordinates; the interval $(0,1)$ is equipotent to $\mathbb{R}$ by the rational function $x \mapsto (2x-1)/(x(1-x))$, which is strictly increasing on $(0,1)$ and carries it onto $\mathbb{R}$. The limiting language that the description of that map invites is only a way of saying that the values become arbitrarily large in absolute value near the endpoints; the rigorous statement of that fact belongs to Part II, where the order is enriched by a distance, and the cardinality result itself uses only the explicit formula. The arithmetic of the cardinal $\mathfrak{c} = 2^{\aleph_0}$ is treated in *Cardinality and the Axiom of Choice*.

## Summary

An ordered field is real closed when every positive element is a square and every polynomial of odd degree has a root. This is equivalent to $F$ being formally real with no proper formally real algebraic extension, to $F(i)$ being algebraically closed, and, by Tarski's theorem, to $F$ being elementarily equivalent to $\mathbb{R}$; a real-closed field carries a unique ordering, determined by the field structure through the identity $P = \{a^2 : a \neq 0\}$, so all isomorphisms of real-closed fields preserve the order. Every ordered field has a real closure, unique up to order-preserving isomorphism fixing the base field: the real closure of $\mathbb{Q}$ is the countable field of real algebraic numbers, while the real closure of $\mathbb{R}(t)$ with $t$ infinite is a field of generalized Puiseux series that does not sit inside $\mathbb{R}$.

An ordered field is order-complete when every nonempty bounded-above subset has a supremum; order-complete fields are Archimedean, they contain $\mathbb{Q}$ densely, and they are all isomorphic to $\mathbb{R}$ by Cantor's uniqueness theorem. Among Archimedean ordered fields, real closedness is strictly weaker than order completeness: the real algebraic numbers are real closed but not order-complete, and no proper subfield of $\mathbb{R}$ is order-complete, while completeness does imply real closedness, because every order-complete ordered field is isomorphic to $\mathbb{R}$. The field $\mathbb{R}$ is real closed, and for a real-closed field $F$ the extension $F(i)$ is algebraically closed, so $\mathbb{C} = \mathbb{R}(i)$ is algebraically closed and is the algebraic closure of $\mathbb{R}$.

| Ordered field | Real closed | Archimedean | Order-complete |
|---|---|---|---|
| $\mathbb{Q}$ | no | yes | no |
| $\overline{\mathbb{Q}} \cap \mathbb{R}$ | yes | yes | no |
| $\mathbb{R}$ | yes | yes | yes |
| $\mathbb{C}$ (not ordered) | no | — | — |
| $F(t)$, $t$ infinite | no | no | no |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Ordered field |
| $P$ | Positive cone, $P = \{x : x > 0\}$ |
| $F^{rc}$ | Real closure of $F$: real-closed, algebraic over $F$ |
| $\widehat{F}$ | Order completion of $F$; an ordered field when $F$ is Archimedean |
| $\overline{F}$ | Algebraic closure of $F$ |
| $\overline{\mathbb{Q}} \cap \mathbb{R}$ | Real algebraic numbers, real closure of $\mathbb{Q}$ |
| $\overline{\mathbb{Q}}$ | Algebraic numbers |
| $i$ | A square root of $-1$ |
| (RC1), (RC2) | Real-closedness axioms |
| $\sup A$, $\inf A$ | Least upper bound, greatest lower bound |
| $\mathbb{R}$ | The unique order-complete ordered field |
| $F(i)$ | Quadratic extension by a square root of $-1$ |
| $F(t)$ | Rational function field, ordered by leading coefficients |



## Further Reading

- Emil Artin and Otto Schreier, *Algebraische Konstruktion reeller Körper* (Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 5, 1927), for the existence and uniqueness of the real closure.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for real-closed fields, real closures and the Artin–Schreier theory.
- Alfred Tarski, *A Decision Method for Elementary Algebra and Geometry* (University of California Press, 1951), for the completeness and decidability of the theory of real-closed fields.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for Dedekind completeness and Cantor's uniqueness theorem for ordered fields.
- Walter Rudin, *Principles of Mathematical Analysis* (McGraw-Hill, 3rd ed. 1976), for the construction of $\mathbb{R}$ by cuts, the least upper bound property and the intermediate value theorem.
- Alexander Prestel and Charles N. Delzell, *Positive Polynomials* (Springer, 2001), for real-closed fields and their orderings in the general theory.
