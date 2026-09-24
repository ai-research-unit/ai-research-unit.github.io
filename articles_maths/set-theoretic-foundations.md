
# __Set-Theoretic Foundations__

## Introduction

The preceding four articles used sets naively: they formed unions, intersections, power sets and quotients, and they took for granted that these operations are legitimate. This article supplies the axiomatic basis that justifies them. It states the Zermelo–Fraenkel axioms with the axiom of choice, derives the elementary consequences that the corpus uses — the existence of the natural numbers, the definition of ordered pairs, the formation of images and quotients — and then develops the theory of the **ordinals**, on which the notions of cardinal and of transfinite recursion rest. It concludes with the cumulative hierarchy, the independence of the continuum hypothesis, and a survey of the large-cardinal axioms.

The article is the fifth of the corpus, above *Sets, Functions and Relations*, *Logic and Proof*, *Order Theory and Lattices* and *Cardinality and the Axiom of Choice*, and it depends on all four. The language in which the axioms are written is the first-order language of *Logic and Proof*; the relations and functions of which the axioms speak are those of *Sets, Functions and Relations*; the well-orderings and fixed points that transfinite recursion uses are those of *Order Theory and Lattices*; and the cardinal arithmetic and the theorem that no set is equipotent to its power set are those of *Cardinality and the Axiom of Choice*. The article's purpose is foundational: it does not create new algebra but it explains why the set-theoretic operations that other articles perform are available.

The treatment is honest about what is proved and what is quoted. The axioms, the construction of the ordinals, the definition of the cumulative hierarchy and the elementary theory of cardinal and ordinal arithmetic are proved in full or in outline. The independence of the continuum hypothesis and the existence of large cardinals are quoted as the major theorems of the subject, with the standard references, and the forcing machinery is described only to the extent that its conclusion can be stated. Where a result is a theorem of the metatheory — the reflection principle, for instance — the article says so and citesandwhere the metatheoretic tools are developed. No topology, no distance and no form appears; the article is the last of the foundational layer and closes it.

## The Axioms

### The Language of Set Theory

The language of set theory is a first-order language, in the sense of *Logic and Proof*, with a single non-logical symbol, the binary relation $\in$, and no function or constant symbols. Its formulas are built from the atomic formulas $x \in y$ and $x = y$ by the connectives and quantifiers. A **set** is a value of the variables; the quantifiers range over all sets. The formula $x \subseteq y$ abbreviates $\forall z\,(z \in x \to z \in y)$, and $x = y$ is taken as a primitive, though the axiom of extensionality makes it equivalent to $\forall z\,(z \in x \leftrightarrow z \in y)$.

A **class** is a collection defined by a formula $\varphi(x)$, written $\{x : \varphi(x)\}$, and is not in general a set: the class of all sets that are not members of themselves is a class, and the paradoxes show that it is not a set. Every set is a class, via the formula $x \in a$; a class that is not a set is a **proper class**. The distinction is not part of the formal language — classes are a convenient abbreviation for formulas — and the corpus uses it only as a shorthand. The standard convention is that a class $\{x : \varphi(x)\}$ may be substituted for a variable in any statement, by translating the statement into the formula $\varphi$.

### The Zermelo–Fraenkel Axioms

The following sentences are the **Zermelo–Fraenkel axioms**; together with the axiom of choice they form **ZFC**. The names are standards of the literature.

1. **Extensionality.** $\forall x \forall y\,(\forall z\,(z \in x \leftrightarrow z \in y) \to x = y)$.
2. **Pairing.** For all $a, b$ there is a set $c$ whose elements are exactly $a$ and $b$: $\forall a \forall b \exists c \forall z\,(z \in c \leftrightarrow z = a \vee z = b)$. The unordered pair is written $\{a,b\}$, and the singleton $\{a\} = \{a,a\}$.
3. **Union.** For every $a$ there is a set $\bigcup a$ with $z \in \bigcup a \leftrightarrow \exists y\,(y \in a \wedge z \in y)$.
4. **Power set.** For every $a$ there is a set $\mathcal{P}(a)$ with $z \in \mathcal{P}(a) \leftrightarrow z \subseteq a$.
5. **Separation.** For every $a$ and every formula $\varphi(z, \vec{p})$, there is a set $b$ with $z \in b \leftrightarrow z \in a \wedge \varphi(z,\vec{p})$. The set is $\{z \in a : \varphi(z, \vec{p})\}$.
6. **Replacement.** For every formula $\varphi(x,y,\vec{p})$ that is functional in $x$, and every $a$, there is a set $b$ whose elements are the values $y$ for $x \in a$: the image of a set under a definable function is a set.
7. **Infinity.** There is a set containing $\emptyset$ and closed under $z \mapsto z \cup \{z\}$.
8. **Foundation (regularity).** Every nonempty set $a$ has an element disjoint from it: no set is a member of itself, and there are no infinite descending membership chains.
9. **Choice.** For every set $a$ whose elements are nonempty and pairwise disjoint, there is a set $c$ meeting each element of $a$ in exactly one point.

Axioms 1–8 are the Zermelo–Fraenkel axioms; the ninth is the axiom of choice. The axiom of choice in the form stated here is equivalent to the choice-function form of *Cardinality and the Axiom of Choice*, by a standard argument: given a family of nonempty sets, apply the ninth axiom to the family of copies $\{i\} \times A_i$.

The axioms are not independent in their formulation — separation follows from replacement and the empty set, and pairing follows from replacement and power set in the presence of the empty set — and they are usually presented in a minimal list. The list above is the one that matches the constructions the corpus performs, and each axiom is used at least once in the following sections. The corpus does not work in a weak fragment: it uses the full ZFC, and it flags the few places where a weaker principle would suffice, as in the countable-union theorem of *Cardinality and the Axiom of Choice*.

### Consequences Used in the Corpus

The operations of the earlier articles are derived from the axioms, and it is worth recording the derivations, because they are the licence for everything that follows.

**Proposition.** The following hold in ZF.

1. **Empty set.** There is a set with no elements, and it is unique; it is written $\emptyset$.
2. **Intersection.** For every nonempty $a$ there is a set $\bigcap a$ with $z \in \bigcap a \leftrightarrow \forall y\,(y \in a \to z \in y)$.
3. **Ordered pairs.** For all $a,b$ the set $(a,b) = \{\{a\},\{a,b\}\}$ exists.
4. **Cartesian products.** For all $a, b$ the set $a \times b$ exists.
5. **Quotients.** If $\sim$ is an equivalence relation on a set $a$, the quotient $a/{\sim}$ exists.
6. **Functions.** The graph of a function is a set, and the set $b^a$ of functions $a \to b$ exists.
7. **Finite and countable sets.** The set $\omega$ of natural numbers exists, and so does $\omega \times \omega$.

**Proof.** (1) Take any set $a$ (one exists by infinity) and form $\{z \in a : z \neq z\}$ by separation; uniqueness is extensionality. (2) Take $c \in a$ and form $\{z \in c : \forall y\,(y \in a \to z \in y)\}$, which is independent of $c$. (3) By pairing. (4) Since $(a,b) \in \mathcal{P}(\mathcal{P}(a \cup b))$, the product is a subset of a set and exists by separation. (5) The classes $[x]$ are subsets of $a$; the quotient is the image of $a$ under the definable function $x \mapsto [x]$, so replacement applies. (6) A function is a subset of $a \times b$, so separation applies within $\mathcal{P}(a \times b)$. (7) The set $\omega$ is the least set containing $\emptyset$ and closed under $z \mapsto z \cup \{z\}$, obtained from the set given by infinity by separation; the product is (4). $\square$

## Ordinals

### Well-Orderings and Order Types

**Definition.** A **well-ordering** on a set $a$ is a total order $\leq$ on $a$ such that every nonempty subset of $a$ has a least element. Two well-orderings $(a, \leq)$ and $(b, \preceq)$ are **isomorphic** if there is an order isomorphism between them, in the sense of *Order Theory and Lattices*.

**Lemma.** Let $(a, <)$ be a well-ordering and let $f : a \to a$ be order-preserving, so that $x < y$ implies $f(x) < f(y)$. Then $f(x) \geq x$ for every $x \in a$. Consequently the only order isomorphism of a well-ordering with itself is the identity.

**Proof.** Suppose not and let $m$ be the least element of $\{x \in a : f(x) < x\}$. Then $f(m) < m$, so by minimality of $m$ the inequality $f(f(m)) \geq f(m)$ holds; but order-preservation applied to $f(m) < m$ gives $f(f(m)) < f(m)$, a contradiction. For the consequence, an order isomorphism $f$ satisfies $f(x) \geq x$ and, applying the same to $f^{-1}$, also $x \geq f(x)$; hence $f(x) = x$. $\square$

**Theorem (comparability of well-orderings).** Any two well-orderings are isomorphic, or one is isomorphic to a proper initial segment of the other, and not both.

**Proof sketch.** Let $(a,\leq)$ and $(b,\preceq)$ be well-orderings. By transfinite recursion, define a partial isomorphism $f$ from $a$ to $b$: put $f(x)$ equal to the least element of $b$ not yet in the range if such exists, and stop otherwise. The recursion is well defined because the range so far is a set; the condition that $b$ be exhausted or an element be left over is decided at the first $x$ where no unused element remains, and the initial segment so obtained is an initial segment of $a$. The three possible outcomes — $f$ defined on all of $a$, on a proper initial segment of $a$, or the process stopping with an element of $b$ unused — are the three alternatives of the statement. $\square$

### Von Neumann Ordinals

**Definition.** A set $x$ is **transitive** if every element of an element of $x$ is an element of $x$: $\forall y \in x\,(y \subseteq x)$. An **ordinal** is a transitive set well-ordered by the relation $\in$. Ordinals are written $\alpha, \beta, \gamma, \lambda$; the class of all ordinals is written $\mathrm{On}$.

**Example.** The empty set $\emptyset$ is an ordinal, written $0$. Its successor $\{\emptyset\}$ is an ordinal, written $1$; then $2 = \{0,1\}$, $3 = \{0,1,2\}$, and in general $n+1 = n \cup \{n\}$. The set $\omega = \{0,1,2,\ldots\}$ is an ordinal, and so are $\omega+1 = \omega \cup \{\omega\}$, $\omega + 2$, and so on.

**Theorem.** The following hold.

1. Every element of an ordinal is an ordinal, and every ordinal is the set of all smaller ordinals: $\alpha = \{\beta : \beta < \alpha\}$.
2. The ordinals are totally ordered by $\in$: for ordinals $\alpha, \beta$, exactly one of $\alpha \in \beta$, $\alpha = \beta$, $\beta \in \alpha$ holds.
3. For every set $a$ of ordinals, $\bigcup a$ is an ordinal, and it is the least ordinal greater than or equal to every element of $a$; it is written $\sup a$.
4. For every ordinal $\alpha$ there is a least ordinal greater than $\alpha$, namely $\alpha \cup \{\alpha\}$, written $\alpha+1$; an ordinal of the form $\alpha+1$ is a **successor ordinal**, and an ordinal not of this form and not $0$ is a **limit ordinal**.
5. Let $W$ be a well-ordered set. There is a unique ordinal $\alpha$ and a unique order isomorphism $W \to \alpha$; the ordinal is the **order type** of $W$.

**Proof sketch.** (1) If $\alpha$ is an ordinal and $\beta \in \alpha$, then $\beta$ is a subset of $\alpha$, hence transitive and well-ordered by $\in$; so $\beta$ is an ordinal. The identity $\alpha = \{\beta : \beta < \alpha\}$ follows from transitivity. (2) Let $\alpha,\beta$ be ordinals and suppose they are incomparable; then by the comparability theorem for well-orderings one is isomorphic to a proper initial segment of the other, say $\alpha \cong \beta$ with $\beta < \alpha$; the isomorphism is then the identity on the ordinals and $\alpha \in \alpha$, contradicting foundation. (3) and (4) follow from (1) and (2). (5) The identity map on a well-ordered set is the order isomorphism with its order type; uniqueness uses the comparability theorem, and existence uses that the isomorphism to a proper initial segment composed with the identity forces the segment to be all of the ordinal, which contradicts foundation unless the segment is everything. $\square$

**Theorem (Burali–Forti).** There is no set of all ordinals; the class $\mathrm{On}$ is a proper class.

**Proof.** If $\mathrm{On}$ were a set, it would be a transitive set well-ordered by $\in$, hence an ordinal, and so $\mathrm{On} \in \mathrm{On}$, contradicting foundation. $\square$

The Burali–Forti paradox is the ordinal form of the Russell paradox, and it is the reason a cardinals-as-ordinals approach must take the cardinals to be the **initial ordinals** rather than the class of all ordinals of a given size.

### Transfinite Induction and Recursion

**Theorem (transfinite induction).** Let $C$ be a class of ordinals such that, for every ordinal $\alpha$, if every $\beta < \alpha$ lies in $C$ then $\alpha \in C$. Then $C = \mathrm{On}$.

**Proof.** Otherwise let $\alpha$ be the least ordinal not in $C$ (it exists because the ordinals are well-ordered by $\in$). Every $\beta < \alpha$ is then in $C$, so $\alpha \in C$ by the hypothesis, a contradiction. $\square$

The induction has three cases in practice: the base case $\alpha = 0$, the successor case $\alpha = \beta + 1$ assuming the statement at $\beta$, and the limit case $\alpha$ a limit ordinal assuming the statement at all $\beta < \alpha$. This trichotomy is the ordinal analogue of the weak/strong induction of *Logic and Proof*.

**Theorem (transfinite recursion).** Let $G$ be a class function defined on all sets. There is a unique class function $F$ on $\mathrm{On}$ such that

$$
F(\alpha) = G(F \restriction \alpha)
$$

for every ordinal $\alpha$, where $F \restriction \alpha$ is the restriction of $F$ to the ordinals below $\alpha$.

**Proof sketch.** Define $F(\alpha) = x$ to mean that there is a function $f$ with domain $\alpha$ such that $f(\beta) = G(f \restriction \beta)$ for all $\beta < \alpha$ and $x = G(f)$ (or $x = G(f\restriction\alpha)$ with $f$ of domain $\alpha$). The existence and uniqueness of $f$ for each $\alpha$ are proved by transfinite induction: $f$ for the successor $\alpha+1$ is obtained by adjoining to $f$ for $\alpha$ the value $G(f)$, and $f$ for a limit $\lambda$ is the union of the $f$ for $\beta<\lambda$. Uniqueness of $F$ follows because two candidate functions agree at $0$ and, if they agree below $\alpha$, at $\alpha$. The argument is the ordinal form of the recursion theorem of *Logic and Proof*, and it uses replacement to collect the values. $\square$

**Corollary (definition by transfinite recursion).** If $G$ is given by a formula, then so is $F$; in particular one may define $F(0) = a$, $F(\alpha+1) = G(F(\alpha))$ and $F(\lambda) = \bigcup_{\beta<\lambda} F(\beta)$ for limit $\lambda$, and the result is a definable class function.

### Ordinal Arithmetic

Ordinal addition, multiplication and exponentiation are defined by transfinite recursion.

**Definition.** For ordinals $\alpha, \beta$, define $\alpha + \beta$ by recursion on $\beta$:

$$
\alpha + 0 = \alpha, \qquad \alpha + (\beta+1) = (\alpha+\beta)+1, \qquad \alpha + \lambda = \sup_{\beta < \lambda} (\alpha + \beta) \ \text{for limit } \lambda.
$$

Define $\alpha \cdot \beta$ by

$$
\alpha \cdot 0 = 0, \qquad \alpha \cdot (\beta+1) = \alpha \cdot \beta + \alpha, \qquad \alpha \cdot \lambda = \sup_{\beta<\lambda} \alpha \cdot \beta,
$$

and $\alpha^{\beta}$ by

$$
\alpha^{0} = 1, \qquad \alpha^{\beta+1} = \alpha^{\beta} \cdot \alpha, \qquad \alpha^{\lambda} = \sup_{\beta<\lambda} \alpha^{\beta}.
$$

**Proposition.** Ordinal addition is associative but not commutative, and $\alpha + \beta$ is the order type of a copy of $\alpha$ followed by a copy of $\beta$. Ordinal multiplication is associative, distributive on the left over addition, but not commutative; $\alpha \cdot \beta$ is the order type of $\beta$ copies of $\alpha$ laid end to end.

**Example.** $1 + \omega = \omega$, since $\sup_{n<\omega}(1+n) = \omega$, whereas $\omega + 1 > \omega$: appending one element after the natural numbers gives a well-ordering with a greatest element. Hence $1+\omega \neq \omega+1$, and addition is not commutative. Similarly $2 \cdot \omega = \sup_{n<\omega} 2n = \omega$, while $\omega \cdot 2 = \omega + \omega > \omega$; multiplication is not commutative either.

The arithmetic of the ordinals is thus genuinely non-commutative, and it is the arithmetic of order types, not of cardinalities. Cardinal arithmetic, which *is* commutative for infinite cardinals, is recovered by passing to initial ordinals.

## Cardinals

### Initial Ordinals and the Alephs

**Definition.** A **cardinal** is an ordinal $\alpha$ such that no $\beta < \alpha$ is equipotent to $\alpha$; such an ordinal is an **initial ordinal**. Every ordinal is equipotent to exactly one cardinal, its **cardinality**, and the cardinality of a set $X$ is written $|X|$. The finite cardinals are the natural numbers, and the infinite ones are the **alephs** $\aleph_0 < \aleph_1 < \aleph_2 < \cdots$, indexed by the ordinals, where $\aleph_\alpha$ is the $\alpha$-th infinite cardinal in increasing order.

**Theorem.** Every set can be put in bijection with a unique cardinal if and only if the axiom of choice holds.

**Proof sketch.** If the axiom of choice holds then every set can be well-ordered by *Cardinality and the Axiom of Choice*, hence has an order type, and the least ordinal equipotent to it is a cardinal. Conversely, if every set has a cardinality, well-order $X$ by transporting the well-ordering of $|X|$ along the bijection. $\square$

The alephs are then defined by transfinite recursion: $\aleph_0 = \omega$, and $\aleph_{\alpha+1}$ is the least cardinal strictly greater than $\aleph_\alpha$, with $\aleph_\lambda = \sup_{\beta<\lambda}\aleph_\beta$ for limit $\lambda$. The existence of $\aleph_{\alpha+1}$ uses Hartogs' theorem, which is stated below.

**Theorem (Hartogs).** For every set $X$ there is an ordinal that does not inject into $X$; the least such ordinal is written $\mathrm{H}(X)$.

**Proof sketch.** Consider the set $W$ of well-orderings of subsets of $X$ (which is a set, being a subset of $\mathcal{P}(X \times X)$), and let $\mathrm{H}(X)$ be the set of their order types. This set of ordinals is transitive and well-ordered by $\in$, hence an ordinal; if $\mathrm{H}(X)$ injected into $X$, it would be the order type of a well-ordering of a subset of $X$, hence a member of itself, contradicting foundation. $\square$

Hartogs' theorem makes the aleph sequence definable and is the engine of Zermelo's proof that the well-ordering theorem follows from the axiom of choice; the proof of that implication in *Cardinality and the Axiom of Choice* used exactly this device in the guise of a maximal well-orderable subset.

### Cardinal Arithmetic Revisited

With cardinals identified as initial ordinals, the arithmetic of *Cardinality and the Axiom of Choice* is available, and three further results are standard.

**Theorem.** For infinite cardinals $\kappa$ and $\lambda$, $\kappa + \lambda = \kappa \cdot \lambda = \max(\kappa,\lambda)$, and $\kappa^{\lambda} > \kappa$ when $\lambda \geq 2$.

**Theorem (König).** For any family $(\kappa_i)$ of cardinals, $\sum_i \kappa_i < \prod_i \lambda_i$ whenever $\kappa_i < \lambda_i$ for all $i$. In particular $\kappa^{\mathrm{cf}(\kappa)} > \kappa$ for every infinite $\kappa$, and $2^{\aleph_0}$ is not the sum of countably many smaller cardinals.

**Definition.** The **cofinality** $\mathrm{cf}(\kappa)$ of a cardinal $\kappa$ is the least cardinality of a subset of $\kappa$ that is unbounded in $\kappa$. A cardinal is **regular** if $\mathrm{cf}(\kappa) = \kappa$ and **singular** otherwise. A cardinal $\kappa$ is a **strong limit** if $2^{\lambda} < \kappa$ for every $\lambda < \kappa$.

**Example.** $\aleph_0$ is regular, since a finite union of finite sets is finite. $\aleph_1$ is regular. The cardinal $\aleph_\omega = \sup_n \aleph_n$ is singular, of cofinality $\aleph_0$. Every successor cardinal is regular; a regular limit cardinal is called weakly inaccessible, and whether any such cardinal exists is not decidable in ZFC and is the first question of the large-cardinal theory below.

## The Cumulative Hierarchy

### The Rank Function

**Definition.** The **cumulative hierarchy** is defined by transfinite recursion on the ordinals:

$$
V_0 = \emptyset, \qquad V_{\alpha+1} = \mathcal{P}(V_\alpha), \qquad V_\lambda = \bigcup_{\beta < \lambda} V_\beta \ \text{for limit } \lambda,
$$

and $V = \bigcup_{\alpha \in \mathrm{On}} V_\alpha$.

**Theorem.** The following hold.

1. Each $V_\alpha$ is transitive, and $V_\alpha \subseteq V_\beta$ for $\alpha \leq \beta$.
2. Every $V_\alpha$ is a set.
3. **(Foundation of the hierarchy)** Every set belongs to some $V_\alpha$: for every $x$ there is an ordinal $\alpha$ with $x \in V_{\alpha+1}$, and the least such $\alpha$ is the **rank** $\operatorname{rk}(x)$ of $x$.
4. $V_\alpha \cap \mathrm{On} = \alpha$, so the ordinals are recovered from the hierarchy.
5. $V_\omega$ consists of the hereditarily finite sets, and every $V_\alpha$ is an element of $V_\beta$ for $\beta > \alpha$.

**Proof sketch.** (1) and (2) are by transfinite induction, using that the power set of a set is a set. (3) is proved by $\in$-induction: assuming every element of $x$ lies in some $V_\alpha$, replacement collects the ranks of the elements into a set of ordinals with supremum $\beta$, and then $x \subseteq V_\beta$, so $x \in V_{\beta+1}$. The use of foundation is what forces the induction on the membership relation to be well founded. (4) is a transfinite induction: an ordinal $\alpha$ is a set of ordinals, each below it, so $\alpha \subseteq V_\alpha$ by (3), and no ordinal $\geq \alpha$ lies in $V_\alpha$ by induction. (5) is immediate from the definition and (4). $\square$

The hierarchy is the picture of the set-theoretic universe that the corpus presupposes: every set is built from the empty set by iterated power sets and unions, with the ordinals as the stages of the construction. Nothing in the algebra of the corpus needs the picture, but it is the reason the recursion and induction principles of the previous sections are available for every set, not only for sets of a special form.

### The Reflection Principle

**Theorem (reflection, schema).** For every formula $\varphi(x_1,\ldots,x_n)$ and every ordinal $\alpha$ there is an ordinal $\beta > \alpha$ such that, for all $a_1,\ldots,a_n \in V_\beta$,

$$
\varphi(a_1,\ldots,a_n) \iff \varphi^{V_\beta}(a_1,\ldots,a_n),
$$

where $\varphi^{V_\beta}$ is $\varphi$ with every quantifier relativised to $V_\beta$.

**Proof sketch.** The proof is a syntactic induction on $\varphi$, using the absoluteness of $\Delta_0$ formulas and the existence of a closure ordinal for each existential quantifier: for a formula $\exists y\,\psi(y,x_1,\ldots,x_n)$, one collects, for each tuple in a given $V_\beta$, a witness $y$ of smallest rank and takes the supremum of the ranks, iterating $\omega$ times to close under all subformulas. The argument is a theorem of ZFC and belongs to the metatheory of set theory; the arithmetisation of syntax and the metatheoretic techniques used to state it are developed and revisited. $\square$

The reflection principle is the reason a set is a faithful miniature of the universe for any finite list of formulas, and it is the technical heart of the constructions of model theory. It is stated here because it is the bridge between this article and the logical layer that follows.

## Independence

### Gödel's Constructible Universe

**Definition.** A formula is $\Delta_0$ if all its quantifiers are bounded, $\exists x \in y$ or $\forall x \in y$; a class is $\Delta_0$-definable if it is defined by such a formula with parameters. The **constructible hierarchy** is defined by

$$
L_0 = \emptyset, \qquad L_{\alpha+1} = \text{the set of } \Delta_0\text{-definable subsets of } L_\alpha \text{ with parameters in } L_\alpha, \qquad L_\lambda = \bigcup_{\beta<\lambda} L_\beta,
$$

and $L = \bigcup_\alpha L_\alpha$. A set is **constructible** if it lies in $L$.

**Theorem (Gödel).** The class $L$ satisfies all the axioms of ZFC, and in $L$ the generalised continuum hypothesis holds. Consequently, if ZFC is consistent, then so are ZFC + GCH and ZFC + CH.

The construction builds the smallest inner model of ZFC, one in which every set is definable from ordinals and finitely many parameters; the axiom of choice and the generalised continuum hypothesis are provable inside it. The theorem shows that CH cannot be *refuted* from ZFC, provided ZFC is consistent.

### Forcing and Cohen's Theorem

**Theorem (Cohen).** If ZFC is consistent, then so is ZFC + $\neg$CH; that is, there is a model of ZFC in which $2^{\aleph_0} \neq \aleph_1$.

The method is **forcing**. One begins with a countable transitive model $M$ of a finite fragment of ZFC, adjoining to it a **generic filter** $G$ for a partially ordered set $\mathbb{P} \in M$ of **forcing conditions**, and forms the **generic extension** $M[G]$, which contains $M$ and satisfies ZFC. By choosing $\mathbb{P}$ to add $\aleph_2$ distinct reals and arranging that cardinals are preserved, one obtains a model in which $2^{\aleph_0} \geq \aleph_2$, contradicting CH. The verification that $M[G]$ satisfies ZFC is a transfinite induction on the forcing relation, and the existence of a generic filter is the one place where a method of the metatheory (or a countable model) is needed. The details belong to the standard literature, cited below.

**Theorem (independence of CH).** If ZFC is consistent, then neither CH nor its negation is provable in ZFC.

**Pro.** Gödel's theorem gives the consistency of CH, Cohen's the consistency of its negation; by the soundness and completeness of first-order logic, discussed, neither statement is a theorem of a consistent ZFC. $\square$

## Large Cardinals in Outline

### Inaccessible Cardinals

**Definition.** An uncountable cardinal $\kappa$ is **weakly inaccessible** if it is regular and a limit cardinal (that is, not a successor cardinal), and **strongly inaccessible** if it is regular and a strong limit, so that $2^{\lambda} < \kappa$ for every $\lambda < \kappa$.

**Theorem.** The existence of a strongly inaccessible cardinal is not provable in ZFC, provided ZFC is consistent.

**Proof sketch.** If $\kappa$ is strongly inaccessible then $V_\kappa$ is a set model of ZFC: the axioms of pairing, union, power set and separation hold because $\kappa$ is a limit cardinal closed under power sets; infinity holds because $\omega < \kappa$; replacement holds because $\kappa$ is regular; foundation holds in every transitive set. A model of ZFC cannot be proved to exist from ZFC by Gödel's second incompleteness theorem, quoted and developed. Hence the existence of $\kappa$ is unprovable. $\square$

### Measurable Cardinals and Beyond

**Definition.** An uncountable cardinal $\kappa$ is **measurable** if there is a $\kappa$-complete nonprincipal ultrafilter on $\kappa$; that is, an ultrafilter closed under intersections of fewer than $\kappa$ of its members and containing no singleton.

Every measurable cardinal is strongly inaccessible. Measurable cardinals are the first of the **large cardinal axioms**, a hierarchy of existence principles of increasing consistency strength: measurable cardinals, Ramsey and Erdős cardinals, strongly compact and supercompact cardinals, and the ranks beyond. Large cardinals are not assumed in the corpus; the algebra of the corpus takes place in ZFC, and the large-cardinal statements are recorded here only to mark the boundary of what the axioms prove, and to indicate where the subject continues.

**Remark.** The pattern of the independence results is that a statement is undecidable in ZFC because both it and its negation have models constructed by transfinite techniques; large cardinal axioms are statements of the opposite kind, which settle undecidable statements by making the universe richer. Whether a given large cardinal axiom is consistent with ZFC is itself a question of consistency strength, ordered by the technique of **inner models**, and no part of this hierarchy is used by the corpus.

## Summary

The Zermelo–Fraenkel axioms with choice are the nine sentences above, written in the language with a single binary relation $\in$; they license the empty set, pairing, union, the power set, separation, replacement, the natural numbers, the well-foundedness of $\in$, and the existence of choice sets. Separation and replacement are schemas, one instance for every formula, and the corpus uses all the axioms; the axiom of choice is stated in the disjoint-family form, equivalent to the choice-function form of *Cardinality and the Axiom of Choice*.

An ordinal is a transitive set well-ordered by $\in$; the ordinals are totally ordered by membership, every well-ordered set has a unique order type, and the class of ordinals is a proper class (Burali–Forti). Transfinite induction and recursion hold on the ordinals and generalise the induction and recursion of *Logic and Proof*. Ordinal addition, multiplication and exponentiation are defined by recursion on the second argument and are non-commutative; $1 + \omega = \omega \neq \omega + 1$.

A cardinal is an initial ordinal, and every set has a cardinality exactly when the axiom of choice holds. The alephs are the infinite cardinals in increasing order, indexed by the ordinals; Hartogs' theorem produces the ordinal that does not inject into a given set and makes the aleph sequence definable. Cardinal arithmetic over infinite cardinals is commutative and absorbing, and König's theorem and the cofinality of a cardinal are refined by the notions of regular and singular cardinals.

The cumulative hierarchy $V_\alpha$ is built by iterated power sets and unions; every set has a rank, the ordinals appear as $V_\alpha \cap \mathrm{On} = \alpha$, and the reflection principle says that a set can mirror the universe for any finite list of formulas. Gödel's constructible universe $L$ is an inner model satisfying ZFC and the generalised continuum hypothesis; Cohen's forcing produces models in which CH fails; together they show the independence of CH from ZFC. Large cardinals — inaccessible, measurable and beyond — are existence principles of increasing consistency strength, unprovable in ZFC if ZFC is consistent, and not assumed in the corpus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\in$ | Membership; the single non-logical symbol of the language |
| $x \subseteq y$, $\mathcal{P}(a)$ | Subset; power set |
| $\bigcup a$, $\bigcap a$ | Union and intersection of the elements of $a$ |
| $\emptyset$ | Empty set |
| $\omega$ | The least infinite ordinal, the set of natural numbers |
| $\{x : \varphi(x)\}$ | Class defined by a formula; proper class if not a set |
| $\alpha, \beta, \gamma, \lambda$ | Ordinals |
| $\mathrm{On}$ | Proper class of all ordinals |
| $\alpha + 1 = \alpha \cup \{\alpha\}$ | Successor ordinal |
| $\alpha + \beta$, $\alpha \cdot \beta$, $\alpha^{\beta}$ | Ordinal addition, multiplication, exponentiation |
| $\aleph_0, \aleph_1, \ldots, \aleph_\alpha$ | Infinite cardinals (alephs), in increasing order |
| $\mathrm{cf}(\kappa)$ | Cofinality of $\kappa$ |
| $\mathrm{H}(X)$ | Hartogs ordinal of $X$: least ordinal not injecting into $X$ |
| $V_\alpha$, $V$ | Cumulative hierarchy and its union |
| $\operatorname{rk}(x)$ | Rank of $x$: least $\alpha$ with $x \in V_{\alpha+1}$ |
| $L_\alpha$, $L$ | Constructible hierarchy and the constructible universe |
| $\varphi^{V_\beta}$ | Relativisation of $\varphi$ to $V_\beta$ |
| $\mathbb{P}$, $G$, $M[G]$ | Forcing conditions, generic filter, generic extension |
| ZF, ZFC | Zermelo–Fraenkel axioms; with the axiom of choice |





## Further Reading

- Kenneth Kunen, *Set Theory: An Introduction to Independence Proofs* (North-Holland, 1980), for the axioms, the ordinals, the cumulative hierarchy and forcing.
- Thomas Jech, *Set Theory*, 3rd millennium ed. (Springer, 2003), for the comprehensive account of ordinals, cardinals, forcing and large cardinals.
- Kurt Gödel, *The Consistency of the Continuum Hypothesis* (Princeton University Press, 1940), for the constructible universe and the consistency of GCH.
- Paul J. Cohen, *Set Theory and the Continuum Hypothesis* (Benjamin, 1966), for forcing and the independence of CH.
- Azriel Lévy, *Basic Set Theory* (Springer, 1979; reprinted Dover, 2002), for a careful development of the ZF axioms, ordinals and transfinite recursion.
- Jean R. Shoenfield, *Mathematical Logic* (Addison-Wesley, 1967), for the reflection principle and its use in model-theoretic constructions.
- Akihiro Kanamori, *The Higher Infinite*, 2nd ed. (Springer, 2003), for measurable cardinals and the large-cardinal hierarchy.
