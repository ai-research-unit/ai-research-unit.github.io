# __The Real Numbers ($\mathbb{R}$)__

## Introduction

The real numbers are the order completion of the rationals: the unique ordered field with the least upper bound property, obtained by filling the Dedekind cuts of $\mathbb{Q}$. Equivalently they are the metric completion of $\mathbb{Q}$ for the usual absolute value. The two constructions agree, and the result is the unique complete ordered field up to a unique order-preserving isomorphism, so $\mathbb{R}$ is determined by its order and its field structure together, not by either alone.

This article carries out the two constructions, records the order, field and topological properties of $\mathbb{R}$, proves that the only field automorphism of $\mathbb{R}$ is the identity, and locates $\mathbb{R}$ among the ordered fields and among the completions of $\mathbb{Q}$. Real closedness, the proof that $\mathbb{R}$ is real closed, and the uniqueness of the complete ordered field are proved in *Real-Closed and Complete Ordered Fields* and are used here; the constructions by cuts and by Cauchy sequences also underlie *The Complex Numbers* and the valued completion of *Absolute Values, Valuations and Completions*.

Throughout, $\mathbb{Q}$ is the field of rationals with its unique order and $\mathbb{R}$ is the order-complete ordered field. Convergence and continuity are used only as the completion and order theories make them necessary; the analytic theory of functions on $\mathbb{R}$ belongs to the companion real-analysis articles of categories 25–26.

---

## The Two Constructions

### Dedekind Cuts

**Definition.** A **Dedekind cut** of $\mathbb{Q}$ is a subset $A \subseteq \mathbb{Q}$ such that

**(C1)** $A \neq \emptyset$ and $A \neq \mathbb{Q}$;

**(C2)** if $a \in A$ and $q \in \mathbb{Q}$ with $q < a$, then $q \in A$;

**(C3)** $A$ has no greatest element.

The set of all cuts is denoted $\mathcal{R}$.

**Theorem.** With the order $A \leq B \iff A \subseteq B$ and the operations

$$
A + B = \{a + b : a \in A,\ b \in B\}, \qquad
A \cdot B = \{ab : a \in A,\ b \in B,\ a, b \geq 0\} \cup \{q \in \mathbb{Q} : q < 0\} \ (\text{for } A, B \geq 0),
$$

and with negative elements handled by sign, $\mathcal{R}$ is an order-complete ordered field. The map $q \mapsto \{x \in \mathbb{Q} : x < q\}$ embeds $\mathbb{Q}$ as an ordered subfield, and $\mathcal{R}$ is the order completion of $\mathbb{Q}$.

**Proof sketch.** $\mathcal{R}$ is totally ordered by inclusion, since cuts are downward closed subsets of $\mathbb{Q}$. A nonempty family of cuts that is bounded above has a supremum: every upper bound is a cut and hence is not all of $\mathbb{Q}$, the family is contained in such a bound, so the union of the family is a downward closed subset of $\mathbb{Q}$ that is neither empty nor all of $\mathbb{Q}$, and it has no greatest element because no member of the family has one; hence the union is a cut, and it is the least upper bound. A nonempty family that is bounded below has an infimum, namely the intersection of the family with the greatest element removed if the intersection has one: the intersection is downward closed and nonempty because it contains a lower bound, and a cut contained in every member of the family has no greatest element, so it lies in the intersection with the greatest element removed, which is therefore the largest such cut. Addition of cuts is well defined and makes $\mathcal{R}$ an ordered abelian group whose zero is the cut of negative rationals, and multiplication is defined on nonnegative cuts by the display and extended by the sign rule; the field axioms are verified case by case, distributivity being the only substantive one. The embedding $q \mapsto \{x < q\}$ preserves the order and the operations, and the least upper bound property is the sup-of-unions statement. $\square$

**Remark.** The cut construction is the one explained in *Real-Closed and Complete Ordered Fields* as the order completion $\widehat{F}$ of an Archimedean ordered field $F$, applied to $F = \mathbb{Q}$.

### Cauchy Sequences

**Definition.** A sequence $(x_n)$ in $\mathbb{Q}$ is **Cauchy** if for every rational $\epsilon > 0$ there is $n_0$ with $\lvert x_n - x_m \rvert < \epsilon$ for all $n, m \geq n_0$. Two Cauchy sequences are **equivalent** if $\lvert x_n - y_n \rvert \to 0$, and the completion is

$$
\mathcal{C} = \{\text{Cauchy sequences in } \mathbb{Q}\}/\sim .
$$

**Theorem.** With termwise addition and multiplication, $\mathcal{C}$ is an order-complete ordered field, and the map $q \mapsto (q, q, q, \dots)$ embeds $\mathbb{Q}$ as an ordered subfield; $\mathcal{C}$ is the metric completion of $\mathbb{Q}$ for the usual absolute value, and it is complete as a metric space.

**Proof.** Termwise sums and products of Cauchy sequences are Cauchy, and the operations respect the equivalence relation, so $\mathcal{C}$ is a commutative ring with $1$; it is a field because a Cauchy sequence that does not converge to $0$ is eventually bounded away from $0$ in absolute value, so a sufficiently far tail can be inverted termwise, producing an inverse class. Completeness of $\mathcal{C}$ is proved by the diagonal argument on Cauchy sequences of Cauchy sequences, and order-completeness by identifying each class with the cut of rationals below it. $\square$

### Agreement

**Theorem.** The two constructions produce isomorphic ordered fields, canonically: the map

$$
\Phi : \mathcal{C} \to \mathcal{R}, \qquad \Phi[(x_n)] = \left\{q \in \mathbb{Q} : q + \epsilon < x_n \text{ for all sufficiently large } n \text{ and some rational } \epsilon > 0\right\},
$$

is an order-preserving field isomorphism.

**Proof sketch.** The set displayed is a cut: it is nonempty and not all of $\mathbb{Q}$ because $(x_n)$ is Cauchy and hence bounded; it is downward closed, and it has no greatest element, because $q$ lies in it with gap $\epsilon$ precisely when $q + \epsilon/2$ lies in it with gap $\epsilon/2$; and it depends only on the class of $(x_n)$, since two equivalent Cauchy sequences are eventually within any prescribed rational distance of one another. The element $q$ lies in $\Phi[(x_n)]$ exactly when $q < x$, where $x$ is the limit of $(x_n)$ in the complete field $\mathcal{C}$: if $q < x$ then eventually $x_n \geq q + \epsilon$ for a rational $\epsilon$ with $q + \epsilon < x$, and conversely $q + \epsilon < x_n$ eventually gives $q < x$. Conversely every cut arises from a Cauchy sequence, for instance from an increasing sequence of rationals converging to the cut, which exists by density. The map is additive and multiplicative by the arithmetic of cuts, and it preserves the order by construction. $\square$

**Corollary.** Any two order-complete ordered fields are isomorphic by a unique order-preserving isomorphism, by *Real-Closed and Complete Ordered Fields*; hence $\mathcal{R} \cong \mathcal{C} \cong \mathbb{R}$ and $\mathbb{R}$ is unique up to a unique ordered-field isomorphism.

---

## The Order Structure

**Theorem.** $\mathbb{R}$ has the following properties.

**(a)** $\mathbb{R}$ is a complete ordered field: every nonempty subset that is bounded above has a least upper bound, and every nonempty subset bounded below has a greatest lower bound.

**(b)** $\mathbb{R}$ is Archimedean, and $\mathbb{Q}$ is dense in $\mathbb{R}$; every real is the supremum of the rationals below it.

**(c)** $\mathbb{R}$ is order-complete and therefore, by *Real-Closed and Complete Ordered Fields*, no proper subfield of $\mathbb{R}$ is order-complete.

**(d)** The order topology on $\mathbb{R}$ is the metric topology of $\lvert \cdot \rvert_\infty$; $\mathbb{R}$ is connected and locally compact in it.

**Proof.** (a) is the least upper bound property, proved in the cut model. (b) is the theorem on order-complete fields from *Real-Closed and Complete Ordered Fields*. (c) Let $F \subsetneq \mathbb{R}$ be a subfield and let $x \in \mathbb{R} \setminus F$. The set $S = \{q \in \mathbb{Q} : q < x\}$ is a nonempty subset of $F$, since $\mathbb{Q} \subseteq F$, and it is bounded above in $F$ because $\mathbb{R}$ is Archimedean; its least upper bound in $\mathbb{R}$ is $x$. If $y \in F$ is an upper bound of $S$ then $y \geq x$, and if $y > x$ then, $\mathbb{Q}$ being dense in $\mathbb{R}$, there is a rational $q$ with $x < q < y$, and $q \in F$ is an upper bound of $S$ smaller than $y$. Hence a least upper bound of $S$ in $F$, if it existed, would have to equal $x$ and lie in $F$, a contradiction. Hence no proper subfield is order-complete. (d) The intervals with rational endpoints and those with real endpoints define the same topology on $\mathbb{R}$, so the order topology and the metric topology agree. For connectedness, a separation $\mathbb{R} = U \cup V$ into disjoint nonempty open sets, with $a \in U$, $b \in V$ and $a < b$, would give an element $s = \sup([a,b] \cap U)$ lying in $U$ or in $V$: if $s \in U$ then openness at $s$ produces points of the interval above $s$ in $U$, contradicting $s$ being an upper bound, and if $s \in V$ then openness at $s$ puts an interval below $s$ inside $V$, while the definition of supremum puts elements of $U$ arbitrarily close below $s$, so the two sets meet, a contradiction. Local compactness holds because each closed bounded interval is compact and contains a neighbourhood of each of its points. $\square$

**Remark.** Property (b) is what makes the order of $\mathbb{R}$ usable: every real is determined by the rationals below it, which is the content of the cut construction, and by Cantor's theorem this determination is what makes $\mathbb{R}$ unique.

---

## The Field and Algebraic Structure

**Theorem.** $\mathbb{R}$ has the following properties.

**(a)** $\mathbb{R}$ has characteristic $0$ and contains $\mathbb{Q}$ as its prime field.

**(b)** $\mathbb{R}$ is real closed: every positive real is a square, and every real polynomial of odd degree has a real root.

**(c)** $\mathbb{R}$ is not algebraically closed, and $\mathbb{C} = \mathbb{R}(i)$ with $i^2 = -1$ is an algebraic closure of $\mathbb{R}$; the extension has degree $2$.

**(d)** The algebraic elements of $\mathbb{R}$ over $\mathbb{Q}$ form the subfield $\overline{\mathbb{Q}} \cap \mathbb{R}$ of real algebraic numbers, which is countably infinite, real closed, and not order-complete; it is the real closure of $\mathbb{Q}$.

**(e)** The transcendence degree of $\mathbb{R}$ over $\mathbb{Q}$ is

$$
\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{R} = 2^{\aleph_0},
$$

and $\mathbb{C}$ is the algebraic closure of a purely transcendental extension $\mathbb{Q}(T)$ where $T$ is a transcendence basis of $\mathbb{C}$ over $\mathbb{Q}$, of cardinality $2^{\aleph_0}$, by the Steinitz classification.

**(f)** $\mathbb{R}$ is perfect, and every algebraic extension of $\mathbb{R}$ is either $\mathbb{R}$ itself or $\mathbb{C}$.

**Proof.** (a) and (b) are from *Real-Closed and Complete Ordered Fields*, where real closedness is proved from completeness. (c) $x^2 + 1$ has no real root, and $\mathbb{C}$ is algebraically closed and algebraic over $\mathbb{R}$ of degree $2$. (d) The algebraic elements form a subfield; the field is countable because there are countably many polynomials over $\mathbb{Q}$ with finitely many roots each, and real closed because it is the real closure of $\mathbb{Q}$ in the sense of *Real-Closed and Complete Ordered Fields*. (e) $\mathbb{R}$ has cardinality $2^{\aleph_0}$ and $\overline{\mathbb{Q}}$ is countable, so a transcendence basis has cardinality $2^{\aleph_0}$; the statement about $\mathbb{C}$ is the Steinitz classification of *Algebraically Closed Fields*. (f) A field of characteristic $0$ is perfect, and the algebraic closure has degree $2$ over $\mathbb{R}$. $\square$

**Corollary (dimension as a $\mathbb{Q}$-vector space).** Every set of $\mathbb{Q}$-linearly independent reals has cardinality at most $2^{\aleph_0}$ and a maximal such set, a **Hamel basis**, has cardinality exactly $2^{\aleph_0}$; the linear-algebraic theory of these bases belongs to *Vector Spaces*, and its use here is only to record the cardinality.

---

## The Topological and Automorphism Structure

### Cardinality and Connectedness

**Theorem.** $\mathbb{R}$ is uncountable, of cardinality

$$
\lvert \mathbb{R} \rvert = 2^{\aleph_0},
$$

and the set of irrationals is uncountable, of the same cardinality. The order topology is connected and locally compact, and $\mathbb{R}$ is not countable and not discrete.

**Proof.** $\mathbb{R}$ has a Hamel basis of cardinality continuum, or directly: $\mathbb{R}$ is uncountable by Cantor's diagonal argument applied to the interval $(0,1)$, it has cardinality at most $2^{\aleph_0}$ as the set of Dedekind cuts of $\mathbb{Q}$, which is a subset of the power set of $\mathbb{Q}$, and at least $2^{\aleph_0}$ because the subsets of $\mathbb{N}$ inject into $\mathbb{R}$ by mapping a subset to the real whose ternary expansion has digit $2$ exactly at the positions in that subset. The irrationals are $\mathbb{R} \setminus \mathbb{Q}$, the complement of a countable set in an uncountable one. Connectedness and local compactness are as in the previous section. $\square$

### Automorphisms

**Theorem.** Every field automorphism of $\mathbb{R}$ is the identity: $\operatorname{Aut}(\mathbb{R}) = 1$. Consequently every order-preserving automorphism of $\mathbb{R}$ is the identity as well, and $\mathbb{R}$ has no nontrivial field automorphism.

**Proof.** Let $\sigma \in \operatorname{Aut}(\mathbb{R})$. Since $\mathbb{R}$ is real closed, a real number $x$ is positive if and only if $x$ is a nonzero square, because every positive real has a square root and every nonzero square is positive. Hence $\sigma(x) = \sigma(y^2) = \sigma(y)^2 > 0$ for $x = y^2 > 0$; so $\sigma$ carries positive elements to positive elements and is therefore order-preserving. Since $\sigma$ fixes $1$ it fixes $\mathbb{Q}$, and an order-preserving map fixing a dense subset of an ordered field is the identity: for any $x$, the rationals below $x$ map to the rationals below $\sigma(x)$, and both are determined by the same set. Hence $\sigma = \mathrm{id}$. $\square$

**Corollary.** The subgroup of order-preserving automorphisms of $\mathbb{R}$ is trivial, in agreement with the general statement of *Ordered Fields* that an order-preserving automorphism of an ordered field fixes its prime field pointwise and is determined by it when the field is Archimedean.

### $\mathbb{R}$ among the Completions of $\mathbb{Q}$

**Theorem.** $\mathbb{R}$ is the completion of $\mathbb{Q}$ at the Archimedean place: it is the metric completion of $\mathbb{Q}$ for $\lvert \cdot \rvert_\infty$ and the order completion of $\mathbb{Q}$ for its unique order. The other completions of $\mathbb{Q}$ are the fields $\mathbb{Q}_p$, and no $\mathbb{Q}_p$ is isomorphic to $\mathbb{R}$ as a field.

**Proof.** The two completions of $\mathbb{Q}$ that give $\mathbb{R}$ are the theorems of the first section and of *Real-Closed and Complete Ordered Fields*; the classification of completions is Ostrowski's theorem from *Absolute Values, Valuations and Completions*. Finally $\mathbb{R}$ is real closed and hence formally real, while $\mathbb{Q}_p$ is not formally real, so no field isomorphism can exist. $\square$

**Remark (a warning about "the" completion).** A field can have several inequivalent completions, and a field isomorphism between two completions need not respect the topology or the valuation. As abstract fields, $\mathbb{C}$ and the completed algebraic closure $\mathbb{C}_p$ of $\mathbb{Q}_p$ are isomorphic, because both are algebraically closed fields of characteristic $0$ with transcendence degree $2^{\aleph_0}$ and hence fall in the same Steinitz class of *Algebraically Closed Fields*; they are not isomorphic as topological or as valued fields. The real numbers, by contrast, are rigid in both senses: they have no nontrivial field automorphism, so no such phenomenon occurs for $\mathbb{R}$.

---

## Order Types and Embeddings

### The Order Type of $\mathbb{R}$

**Definition.** A linear order is **dense** if between any two distinct points there is a third, **without endpoints** if it has neither least nor greatest element, and **complete** if every nonempty subset that is bounded above has a least upper bound.

**Theorem (Cantor).** Any two countable dense linear orders without endpoints are order-isomorphic. In particular every such order is isomorphic to $\mathbb{Q}$.

**Proof.** The back-and-forth argument enumerates both orders as $(a_n)$ and $(b_n)$ and builds an increasing bijection by alternating the extension of the partial isomorphism on the side with the smaller index, using density and the absence of endpoints to place each new point. $\square$

**Theorem.** Any two complete dense linear orders without endpoints that contain a countable dense subset are order-isomorphic; in particular any such order is isomorphic to $\mathbb{R}$.

**Proof.** The same back-and-forth construction on the countable dense subsets, with completeness and density extending the partial isomorphism to a map of the whole order: given $x$ in the first order, send it to the supremum in the second order of the images of the dense elements below $x$, which exists by completeness and is strictly increasing by density. $\square$

**Corollary.** The order type of $\mathbb{R}$ is the unique complete dense order type without endpoints that has a countable dense subset; $\mathbb{Q}$ is the unique countable dense order type without endpoints, and it is the dense subset of $\mathbb{R}$ in the above.

### The Archimedean Criterion for Embedding into $\mathbb{R}$

**Theorem.** An ordered field $F$ admits an order-preserving field embedding into $\mathbb{R}$ if and only if $F$ is Archimedean, and the embedding is then unique.

**Proof sketch.** If $F$ embeds in $\mathbb{R}$ it is Archimedean, because $\mathbb{R}$ is. Conversely, if $F$ is Archimedean then the map

$$
\varphi : F \to \mathbb{R}, \qquad \varphi(x) = \sup\{q \in \mathbb{Q} : q < x\},
$$

is well defined because $\{q \in \mathbb{Q} : q < x\}$ is nonempty and bounded above in $F$, hence bounded by a real after the identification of the rationals; it is order-preserving by construction, additive because the rationals below $x + y$ are exactly the sums of rationals below $x$ and below $y$ up to arbitrarily small error, and multiplicative by the analogous squeezing argument using the Archimedean property; it fixes $\mathbb{Q}$ and is therefore the unique such embedding. $\square$

**Corollary.** $\mathbb{R}$ contains an isomorphic copy of every Archimedean ordered field, and it is the order-complete field generated by $\mathbb{Q}$; a non-Archimedean ordered field, such as $\mathbb{Q}(t)$ with $t$ infinite, admits no order-preserving embedding into $\mathbb{R}$, though its underlying field may still embed by a non-order-preserving map.

### Subfields of $\mathbb{R}$

**Theorem.** Every subfield $F \subseteq \mathbb{R}$ is ordered by the restriction of the order of $\mathbb{R}$, and this order is Archimedean. Let

$$
M = \{x \in \mathbb{R} : x \text{ is algebraic over } F\}.
$$

Then $M$ is a subfield of $\mathbb{R}$, it is real closed, and it is the smallest real-closed subfield of $\mathbb{R}$ containing $F$; it is the **real closure** of $F$ inside $\mathbb{R}$.

**Proof.** The restriction of the order satisfies the ordered-field axioms on any subfield and is Archimedean because $\mathbb{R}$ is. The set of elements algebraic over $F$ is a subfield, being closed under the field operations by the algebraic dependence of sums, products and inverses. It is real closed: a positive $x \in M$ has a square root in the real-closed field $\mathbb{R}$, and $\sqrt x$ satisfies the quadratic $X^2 - x$ over $M$, hence is algebraic over $F$ and lies in $M$; and a polynomial of odd degree over $M$ has a root in the real-closed field $\mathbb{R}$, and that root is algebraic over $M$ and hence over $F$, so it lies in $M$. Minimality is because any real-closed subfield of $\mathbb{R}$ containing $F$ must contain every real root of a polynomial over $F$, hence every element algebraic over $F$. $\square$

**Corollary.** The real closure of an ordered field is unique up to an order-preserving isomorphism, by *Real-Closed and Complete Ordered Fields*, and inside $\mathbb{R}$ it is the literal set $M$ above; in particular $\overline{\mathbb{Q}} \cap \mathbb{R}$ is the real closure of $\mathbb{Q}$.

**Examples.** The subfields $\mathbb{Q} \subset \mathbb{Q}(\sqrt2) \subset \overline{\mathbb{Q}} \cap \mathbb{R} \subset \mathbb{R}$ show the tower from the prime field to the real algebraic numbers, which are real closed and countable and not order-complete; adjoining a transcendental $t$ gives $\mathbb{Q}(t) \subset \mathbb{R}$ with the induced Archimedean order, in which $t$ is a finite real number rather than an infinite element; and the real closure of $\mathbb{Q}(t)$ inside $\mathbb{R}$ consists of the real numbers algebraic over $\mathbb{Q}(t)$.

---

## Summary

$\mathbb{R}$ is the order completion of $\mathbb{Q}$ and the metric completion of $\mathbb{Q}$ for the usual absolute value; the two constructions, by Dedekind cuts and by Cauchy sequences, give canonically isomorphic ordered fields, and any two order-complete ordered fields are isomorphic by a unique order-preserving isomorphism, so $\mathbb{R}$ is the unique complete ordered field. It is Archimedean, the rationals are dense in it, every real is the supremum of the rationals below it, and no proper subfield of $\mathbb{R}$ is order-complete. The order topology agrees with the metric topology, is connected and locally compact, and $\mathbb{R}$ has cardinality $2^{\aleph_0}$ with an uncountable set of irrationals.

The field $\mathbb{R}$ has characteristic $0$ and prime field $\mathbb{Q}$; it is real closed, so every positive real is a square and every odd-degree real polynomial has a real root, and it is not algebraically closed, its algebraic closure being $\mathbb{C} = \mathbb{R}(i)$ of degree $2$ over it. The real algebraic numbers $\overline{\mathbb{Q}} \cap \mathbb{R}$ form the real closure of $\mathbb{Q}$ and are countable and not complete, while $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{R} = 2^{\aleph_0}$. Every field automorphism of $\mathbb{R}$ is the identity, so $\mathbb{R}$ is rigid; and $\mathbb{R}$ is not isomorphic to any $\mathbb{Q}_p$, since it is formally real and they are not.

In the order-theoretic terms of Cantor's theorems, $\mathbb{Q}$ is the unique countable dense linear order without endpoints and $\mathbb{R}$ is the unique complete dense linear order without endpoints with a countable dense subset. An ordered field embeds order-preservingly into $\mathbb{R}$ exactly when it is Archimedean, the embedding being $x \mapsto \sup\{q \in \mathbb{Q} : q < x\}$, and it is then unique; so $\mathbb{R}$ is the order-complete field universal for Archimedean ordered fields. Every subfield of $\mathbb{R}$ inherits an Archimedean order and has a real closure inside $\mathbb{R}$, namely its relative algebraic closure.

| Property | Value for $\mathbb{R}$ |
|---|---|
| Order | complete, Archimedean, $\mathbb{Q}$ dense |
| Uniqueness | unique order-complete ordered field |
| Cardinality | $2^{\aleph_0}$ |
| Characteristic | $0$, prime field $\mathbb{Q}$ |
| Real closed | yes |
| Algebraically closed | no; closure $\mathbb{C} = \mathbb{R}(i)$ |
| $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{R}$ | $2^{\aleph_0}$ |
| Real algebraic subfield | $\overline{\mathbb{Q}} \cap \mathbb{R}$, countable, real closed, not complete |
| Automorphisms | $\operatorname{Aut}(\mathbb{R}) = 1$ |
| Completions of $\mathbb{Q}$ giving $\mathbb{R}$ | $\lvert \cdot \rvert_\infty$, order |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}$ | The real numbers, the complete ordered field |
| $\mathbb{Q}$ | Rational numbers, prime field |
| $\mathcal{R}$, $\mathcal{C}$ | Cut model and Cauchy-sequence model of $\mathbb{R}$ |
| $\lvert \cdot \rvert_\infty$ | Usual absolute value |
| $\widehat{F}$ | Order or metric completion of $F$ |
| $A \leq B \iff A \subseteq B$ | Order on cuts |
| $i$ | Square root of $-1$ |
| $\mathbb{C} = \mathbb{R}(i)$ | Algebraic closure of $\mathbb{R}$ |
| $\overline{\mathbb{Q}} \cap \mathbb{R}$ | Real algebraic numbers, real closure of $\mathbb{Q}$ |
| $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{R}$ | Transcendence degree, $2^{\aleph_0}$ |
| $\operatorname{Aut}(\mathbb{R})$ | Automorphism group, trivial |
| $\mathbb{Q}_p$, $\mathbb{C}_p$ | Non-Archimedean completions of $\mathbb{Q}$ |
| $\varphi : F \to \mathbb{R}$ | Archimedean embedding $x \mapsto \sup\{q \in \mathbb{Q} : q < x\}$ |
| $M$ | Relative algebraic closure of a subfield $F \subseteq \mathbb{R}$ |

## Further Reading

- Richard Dedekind, *Stetigkeit und irrationale Zahlen* (Vieweg, 1872), for the construction of $\mathbb{R}$ by cuts.
- Georg Cantor, "Über die Ausdehnung eines Satzes aus der Theorie der trigonometrischen Reihen", *Mathematische Annalen* 5 (1872), for the Cauchy-sequence construction and the uniqueness of the complete ordered field.
- Edmund Landau, *Foundations of Analysis* (Chelsea, 1951), for a careful construction of $\mathbb{R}$ from $\mathbb{Q}$.
- Walter Rudin, *Principles of Mathematical Analysis* (McGraw-Hill, 3rd ed. 1976), for the least upper bound property and its consequences.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for real-closed fields, the real algebraic numbers and transcendence degree.
- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for the order topology of $\mathbb{Q}$ and $\mathbb{R}$ and for the completion of a metric space.
