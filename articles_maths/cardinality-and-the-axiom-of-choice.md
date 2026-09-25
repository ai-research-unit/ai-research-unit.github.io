
# __Cardinality and the Axiom of Choice__

## Introduction

Cardinality is the measure of the size of a set, taken not by counting but by matching: two sets have the same size when a bijection between them exists. This definition is one of the most economical in mathematics and one of the most consequential, because it applies to infinite sets, where it produces results that are not available to any finite counting: the set of integers has the same size as the set of natural numbers, the power set of a set is always strictly larger than the set, and there is no largest size at all. The article develops this theory: equipotence and the Schröder–Bernstein theorem, the distinction between countable and uncountable sets, Cantor's theorem and the arithmetic of infinite cardinals.

The second subject of the article is the axiom of choice and its two great equivalents, Zorn's lemma and the well-ordering theorem. The axiom of choice asserts that every family of nonempty sets admits a function selecting one element from each; it is independent of the other axioms of set theory, it is used constantly and often invisibly, and three of the most important existence theorems of algebra — a maximal ideal in every nontrivial ring, a basis in every vector space, an algebraic closure for every field — are applications of it. The article states the axiom, proves its equivalence with Zorn's lemma and the well-ordering theorem, and catalogues the uses made of it in the corpus.

The article sits fourth in the corpus, above *Sets, Functions and Relations*, *Logic and Proof* and *Order Theory and Lattices*, and uses them freely: the Schröder–Bernstein theorem is proved as an application of the Knaster–Tarski fixed-point theorem of *Order Theory and Lattices*, and the applications of Zorn's lemma are applications to the partial orders of that article. The formal axiomatisation of set theory, the ordinals and the cumulative hierarchy, transfinite induction and recursion, and the independence of the continuum hypothesis are the subject , which follows this one; the present article uses the well-ordering of $\mathbb{N}$ and only so much of the theory of well-orderings as the statements of its theorems require, and defers the ordinal machinery explicitly where a proof needs it.

## Cardinality and Equipotence

### Equipotent Sets

**Definition.** Two sets $X$ and $Y$ are **equipotent**, written $X \cong Y$ or $|X| = |Y|$, if there is a bijection $X \to Y$. The **cardinality** of $X$ is the object $|X|$ that records the equipotence class of $X$.

For finite sets this is the ordinary number of elements; for infinite sets it is a new kind of quantity. The notation $|X| = |Y|$ is read as an abbreviation for the existence of a bijection, and the notation $|X| \leq |Y|$ as an abbreviation for the existence of an injection $X \to Y$; the relation $\leq$ between cardinals is then defined by the existence of an injective function, and the relation $|X| < |Y|$ means $|X| \leq |Y|$ and not $|X| = |Y|$.

**Proposition.** Equipotence is an equivalence relation on sets.

**Proof.** The identity map is a bijection, so $X \cong X$. If $f : X \to Y$ is a bijection then $f^{-1} : Y \to X$ is a bijection by the results of *Sets, Functions and Relations*, so the relation is symmetric. If $f : X \to Y$ and $g : Y \to Z$ are bijections then $g \circ f : X \to Z$ is a bijection, so the relation is transitive. $\square$

The **cardinals** themselves — canonical sets of each cardinality — are the initial ordinals, and they are constructed. The present article uses the notations $|X|$, $|X| = |Y|$ and $|X| \leq |Y|$ as abbreviations, which is sufficient for every statement made here and avoids presupposing the ordinal machinery.

**Remark.** The relation $\leq$ between cardinals is reflexive and transitive. That it is antisymmetric is the Schröder–Bernstein theorem below, and that it is total — that any two sets are comparable — is a consequence of the well-ordering theorem, hence of the axiom of choice.

### Finite and Infinite Sets

**Definition.** A set $X$ is **finite** if it is equipotent to $\{1, \ldots, n\}$ for some $n \in \mathbb{N}$, with $\{1,\ldots,0\} = \emptyset$; it is **infinite** otherwise. A set is **countably infinite** if it is equipotent to $\mathbb{N}$, and **countable** if it is finite or countably infinite.

**Theorem (pigeonhole principle).** If $n \neq m$ then there is no bijection $\{1,\ldots,n\} \to \{1,\ldots,m\}$.

**Proof.** It suffices to show that there is no injection $\{1,\ldots,m\} \to \{1,\ldots,n\}$ when $m > n$. Induct on $n$. For $n = 0$ the target is empty and no injection exists from a nonempty set. Suppose the statement true for $n$ and let $f : \{1,\ldots,m\} \to \{1,\ldots,n+1\}$ with $m > n+1$. If $n+1$ is not in the image, then $f$ is an injection into $\{1,\ldots,n\}$ with $m > n+1 > n$, contradicting the induction hypothesis. If $n+1 = f(k)$, define $g$ on $\{1,\ldots,m\} \setminus \{k\}$, relabelled as $\{1,\ldots,m-1\}$, by $g(i) = f(i)$ for $i \neq k$ and $g(k) = f(m)$ when $k \neq m$ and $g(i)=f(i)$ otherwise; then $g$ is an injection into $\{1,\ldots,n\}$ with $m - 1 > n$, again contradicting the induction hypothesis. $\square$

The pigeonhole principle shows that the number of elements of a finite set is well defined: the $n$ in the definition is unique. It also makes the finite cardinals the ordinary natural numbers, and it is the reason that a proper subset of a finite set is strictly smaller.

**Definition.** A set $X$ is **Dedekind-infinite** if it is equipotent to a proper subset of itself: there is an injection $X \to X$ that is not surjective.

**Proposition.** Every Dedekind-infinite set is infinite.

**Proof.** Contrapositively, a finite set is not Dedekind-infinite: if $X$ is equipotent to $\{1,\ldots,n\}$ and $A \subsetneq X$, then $A$ is equipotent to $\{1,\ldots,m\}$ with $m < n$ by the pigeonhole principle, so $A$ cannot be equipotent to $X$. $\square$

The converse — that every infinite set is Dedekind-infinite — is not a theorem of the other axioms: it is equivalent to the axiom of countable choice, a weak form of the axiom of choice, and it is proved in the companion article. The distinction is the classical illustration that the theory of infinite sets is not a matter of definitions alone.

### The Schröder–Bernstein Theorem

**Theorem (Schröder–Bernstein).** Let $f : X \to Y$ and $g : Y \to X$ be injective. Then there is a bijection $X \to Y$, and hence $|X| = |Y|$.

**Proof.** Define $\Phi : \mathcal{P}(X) \to \mathcal{P}(X)$ by

$$
\Phi(A) = X \setminus g\big(Y \setminus f(A)\big).
$$

If $A \subseteq A'$ then $f(A) \subseteq f(A')$, so $Y \setminus f(A) \supseteq Y \setminus f(A')$, so $g(Y \setminus f(A)) \supseteq g(Y \setminus f(A'))$, and taking complements reverses again: $\Phi(A) \subseteq \Phi(A')$. Thus $\Phi$ is monotone, and by the Knaster–Tarski theorem of *Order Theory and Lattices* it has a greatest fixed point $C = \Phi(C)$, that is,

$$
C = X \setminus g\big(Y \setminus f(C)\big), \quad \text{equivalently} \quad X \setminus C = g\big(Y \setminus f(C)\big).
$$

Define $h : X \to Y$ by

$$
h(x) = \begin{cases} f(x), & x \in C, \\ g^{-1}(x), & x \in X \setminus C. \end{cases}
$$

The second case is well defined because $X \setminus C = g(Y \setminus f(C))$ is contained in the image of $g$, which is injective. The image of the first case is $f(C)$, and the image of the second is $g^{-1}(X \setminus C) = Y \setminus f(C)$, the equality following from $X \setminus C = g(Y \setminus f(C))$ and the injectivity of $g$; since these two sets are complementary and $f, g^{-1}$ are injective, $h$ is injective. For surjectivity, let $y \in Y$: if $y \in f(C)$ then $y = f(x)$ for some $x \in C$; otherwise $y \notin f(C)$, so $g(y) \in g(Y \setminus f(C)) = X \setminus C$, and $h(g(y)) = g^{-1}(g(y)) = y$. Hence $h$ is bijective. $\square$

The theorem is often stated with the roles of the two injections exchanged, as **Cantor–Bernstein–Schröder**; the form above is the one used in the corpus. Its content is that the relation $|X| \leq |Y|$ between cardinals is antisymmetric, so that cardinals are partially ordered by $\leq$.

**Corollary.** $|X| \leq |Y|$ and $|Y| \leq |X|$ imply $|X| = |Y|$.

## Countable and Uncountable Sets

### Countable Sets

**Definition.** A set is **countably infinite** if it is equipotent to $\mathbb{N}$, and **countable** if it is finite or countably infinite. A set that is not countable is **uncountable**.

**Theorem.** $\mathbb{N} \times \mathbb{N}$ is countably infinite.

**Proof.** Define $\pi : \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ by $\pi(m,n) = 2^m (2n+1) - 1$. Uniqueness of the factorisation of a positive integer into a power of $2$ and an odd number shows that $\pi$ is injective; $2^m(2n+1)$ ranges over all positive integers, so $\pi$ is surjective onto $\mathbb{N}$. Alternatively, the enumeration along diagonals,

$$
(0,0),\ (1,0), (0,1),\ (2,0), (1,1), (0,2),\ \ldots,
$$

lists every pair exactly once. Either argument exhibits a bijection. $\square$

**Corollary.** If $A$ and $B$ are countable then $A \times B$ is countable.

**Proof.** If one of the sets is finite then the product is finite, by induction on the number of elements. If both are countably infinite, transport the bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ of the theorem along bijections $A \to \mathbb{N}$ and $B \to \mathbb{N}$. $\square$

**Theorem.** $\mathbb{Z}$ is countably infinite, and so is $\mathbb{N}^k$ for every $k \geq 1$.

**Proof.** The map $\mathbb{Z} \to \mathbb{N}$ sending $n \geq 0$ to $2n$ and $n < 0$ to $-2n - 1$ is a bijection, so $\mathbb{Z}$ is countably infinite. For $\mathbb{N}^k$ we argue by induction on $k$: the case $k = 1$ is the definition, and $\mathbb{N}^{k+1} = \mathbb{N}^k \times \mathbb{N}$ is countable by the corollary on products. $\square$

**Remark.** The same argument applies to a quotient of $\mathbb{Z} \times \mathbb{Z}$, so the field of rationals of the later categories is countably infinite; that statement is a statement about the fraction field of $\mathbb{Z}$ and is proved in *Localization and the Fraction Field*.

**Theorem.** A countable union of countable sets is countable, and more generally, if $I$ is countable and each $A_i$ is countable then $\bigcup_{i \in I} A_i$ is countable.

**Proof.** If some $A_i$ are empty they may be omitted. Otherwise, for each $i$ fix an enumeration $A_i = \{a_{i,0}, a_{i,1}, \ldots\}$, which exists by the definition of countability, and enumerate the union along the diagonals of $I \times \mathbb{N}$ using the preceding theorem. $\square$

**Remark.** The proof chooses an enumeration for each $i$ simultaneously, which is an appeal to the **axiom of countable choice**, the restriction of the axiom of choice to countable families; without it the theorem is not provable from the other axioms. The choice is invisible in the finite case, and the comment marks the first point at which the axiom is required in the corpus.

### Uncountable Sets and the Continuum

**Theorem (Cantor).** For every set $X$ there is no surjection $X \to \mathcal{P}(X)$; consequently $|X| < |\mathcal{P}(X)|$.

**Proof.** Let $h : X \to \mathcal{P}(X)$ be any function, and consider the set

$$
D = \{x \in X : x \notin h(x)\} \subseteq X.
$$

If $D = h(d)$ for some $d \in X$, then $d \in D$ if and only if $d \notin h(d) = D$, a contradiction. Hence $D$ is not in the image of $h$, so $h$ is not surjective. The injection $X \to \mathcal{P}(X)$, $x \mapsto \{x\}$, gives $|X| \leq |\mathcal{P}(X)|$, and the two facts together give $|X| < |\mathcal{P}(X)|$. $\square$

Cantor's theorem is the diagonal argument in its purest form; the set $D$ is constructed so as to differ from $h(x)$ at the point $x$, for every $x$, which is exactly the diagonal of the array.

**Corollary.** $\mathcal{P}(\mathbb{N})$ is uncountable, and there is no largest cardinal.

**Proof.** $\mathcal{P}(\mathbb{N})$ is not finite, and by the theorem it is not equipotent to $\mathbb{N}$. For the second statement, if $\kappa$ is a cardinal then $\kappa < 2^{\kappa}$ by the theorem, so no cardinal is largest. $\square$

**Corollary.** $|\mathcal{P}(\mathbb{N})| = 2^{\aleph_0}$, and $|\mathcal{P}(\mathbb{N})^n| = 2^{\aleph_0}$ for every $n \geq 1$.

**Proof.** The first statement is the definition $|\mathcal{P}(X)| = 2^{|X|}$ at $X = \mathbb{N}$. For the second, $|\mathcal{P}(\mathbb{N})^n| = |\mathcal{P}(\mathbb{N})|^n = \kappa^n = \kappa$ for the infinite cardinal $\kappa = 2^{\aleph_0}$, by the cardinal arithmetic proved below. $\square$

**Remark.** The set of reals of the later categories is equipotent to $\mathcal{P}(\mathbb{N})$, and so are its interval and its finite powers; these are statements about the order-complete field $\mathbb{R}$ and are proved in *Real-Closed and Complete Ordered Fields*. Nothing here needs them: the power set of $\mathbb{N}$ already realises the cardinality.

**Definition.** The cardinality of $\mathcal{P}(\mathbb{N})$ is written $\mathfrak{c}$ and is called the **cardinality of the continuum**; the cardinality of $\mathbb{N}$ is written $\aleph_0$. Thus

$$
\mathfrak{c} = 2^{\aleph_0}.
$$

## Cardinal Arithmetic

### Sums, Products and Exponentiation

**Definition.** Let $\kappa = |X|$ and $\lambda = |Y|$ be cardinals, with $X$ and $Y$ chosen disjoint (replace $Y$ by $Y \times \{0\}$ if necessary). Define the **sum**, **product** and **exponentiation** by

$$
\kappa + \lambda = |X \sqcup Y|, \qquad \kappa \cdot \lambda = |X \times Y|, \qquad \kappa^{\lambda} = |X^{Y}|,
$$

where $X^{Y}$ is the set of functions $Y \to X$.

Each operation is well defined: a bijection $X \to X'$ and a bijection $Y \to Y'$ induce, by composition, bijections $X \sqcup Y \to X' \sqcup Y'$, $X \times Y \to X' \times Y'$ and $X^{Y} \to (X')^{Y'}$, so the operations depend only on the cardinals and not on the representatives. The operations extend the finite ones: for finite cardinals they are the usual sum, product and power.

**Proposition (arithmetic laws).** For all cardinals $\kappa, \lambda, \mu$,

1. $\kappa + \lambda = \lambda + \kappa$ and $\kappa \cdot \lambda = \lambda \cdot \kappa$;
2. $(\kappa + \lambda) + \mu = \kappa + (\lambda + \mu)$ and $(\kappa \cdot \lambda) \cdot \mu = \kappa \cdot (\lambda \cdot \mu)$;
3. $\kappa \cdot (\lambda + \mu) = \kappa \cdot \lambda + \kappa \cdot \mu$;
4. $(\kappa \cdot \lambda)^{\mu} = \kappa^{\mu} \cdot \lambda^{\mu}$ and $\kappa^{\lambda + \mu} = \kappa^{\lambda} \cdot \kappa^{\mu}$ and $(\kappa^{\lambda})^{\mu} = \kappa^{\lambda \cdot \mu}$;
5. $2^{\kappa} = |\mathcal{P}(X)|$ and $2^{\aleph_0} = \mathfrak{c}$.

**Proof.** Each identity is a bijection between the two sets, obtained by the evident rearrangements of coordinates: for instance, a function $Y \sqcup Z \to X$ is the same as a pair of functions $Y \to X$ and $Z \to X$, which gives the first law of (4); a function $Y \times Z \to X$ is the same as a function $Y \to X^{Z}$, which gives the third. For (5), a subset of $X$ is determined by its characteristic function, which is a map $X \to \{0,1\}$. $\square$

### Cantor's Theorem in Cardinal Form

Cantor's theorem reads $2^{\kappa} > \kappa$ for every cardinal $\kappa$, and it is the engine behind the absence of a largest cardinal. Its diagonal proof above needs no cardinal arithmetic, and it is the reason the power set is not merely larger but strictly larger, for every set.

**Corollary.** The sequence $\kappa, 2^{\kappa}, 2^{2^{\kappa}}, \ldots$ is strictly increasing, and no cardinal bounds all of $\mathbb{N}, \mathcal{P}(\mathbb{N}), \mathcal{P}(\mathcal{P}(\mathbb{N})), \ldots$.

### Infinite Cardinal Arithmetic

For infinite cardinals the arithmetic simplifies drastically; the simplification rests on the well-ordering theorem and hence on the axiom of choice.

**Theorem.** Let $\kappa$ and $\lambda$ be infinite cardinals. Then

$$
\kappa + \lambda = \kappa \cdot \lambda = \max(\kappa, \lambda), \qquad \kappa^n = \kappa \ \text{for every finite } n \geq 1.
$$

In particular $\aleph_0 + \aleph_0 = \aleph_0 \cdot \aleph_0 = \aleph_0$, and $\aleph_0 + \mathfrak{c} = \aleph_0 \cdot \mathfrak{c} = \mathfrak{c}$.

**Proof sketch.** The argument is the countability of $\mathbb{N} \times \mathbb{N}$ transposed to an arbitrary infinite $\kappa$. Well-order a set $X$ of cardinality $\kappa$ by the well-ordering theorem and define a bijection $X \times X \to X$ by recursion on that well-order: at the stage of the pair $(x,y)$, the pairs already assigned lie in the initial segments determined by $x$ and by $y$, whose union has cardinality $< \kappa$ by the induction hypothesis, so the values already used form a subset of $X$ of cardinality $< \kappa$; assign to $(x,y)$ the least element of $X$ not already used. Then $|X \times X| = |X|$, and the assertions for $\kappa \cdot \lambda$ follow by padding the smaller cardinal with a set of the larger one's cardinality. The equality $\kappa + \lambda = \max(\kappa,\lambda)$ follows by padding a disjoint union in the same way, and $\kappa^n = \kappa$ by induction on $n$. $\square$

The theorem uses the axiom of choice twice — through the well-ordering and through the identification of cardinals with well-ordered sets — and it fails for cardinals that are not well-orderable. It is the reason that infinite cardinal arithmetic is so much simpler than finite arithmetic, and it is a standard result in the literature. The arithmetic of the cardinals that are not well-orderable, and the finite case, are entirely different; the theorem above concerns only infinite cardinals and is stated under the axiom of choice, which is fixed in the next section.

### The Continuum Hypothesis

**Definition.** The **continuum hypothesis** (CH) is the assertion

$$
2^{\aleph_0} = \aleph_1,
$$

where $\aleph_1$ is the least uncountable cardinal; equivalently, that every subset of a set of cardinality $\mathfrak{c}$ is either countable or of cardinality $\mathfrak{c}$.

The formulation uses $\aleph_1$, whose construction as the least uncountable cardinal requires the ordinals and is given. The **generalised continuum hypothesis** (GCH) asserts $2^{\aleph_\alpha} = \aleph_{\alpha+1}$ for every ordinal $\alpha$.

**Theorem (Gödel; Cohen).** If the Zermelo–Fraenkel axioms with the axiom of choice are consistent, then neither CH nor its negation is provable from them.

The independence of the continuum hypothesis is one of the great results of set theory. The two halves are Gödel's construction of the constructible universe, in which CH holds, and Cohen's method of forcing, which produces models in which it fails; both belong to the theory, where the cumulative hierarchy and the axioms are set out, and the present article records only the statement and its consequence: cardinal arithmetic is not determined by the axioms alone.

## The Axiom of Choice

### The Axiom

**Definition.** The **axiom of choice** (AC) is the assertion that for every family $(A_i)_{i \in I}$ of nonempty sets there is a function $f$ with domain $I$ and $f(i) \in A_i$ for every $i \in I$. Equivalently, $\prod_{i \in I} A_i \neq \emptyset$ for every family of nonempty sets.

The axiom is a statement about the existence of a single function, not of a rule defining it. For finite index sets it follows from the other axioms by induction. The **axiom of countable choice** (AC$_\omega$) is its restriction to countable families, and the **axiom of dependent choice** (DC) asserts that if every element of a set has a relation to some element then there is a sequence following the relation; the implications

$$
\mathrm{AC} \Longrightarrow \mathrm{DC} \Longrightarrow \mathrm{AC}_\omega
$$

are strict, and the weaker principles suffice for most of analysis. The corpus uses the full axiom, and it names the weaker principles only where a result needs no more than they provide.

**Proposition.** The axiom of choice is equivalent to the assertion that every surjective function has a right inverse.

**Proof.** If every surjection has a right inverse, let $(A_i)_{i \in I}$ be a family of nonempty sets, put $U = \{(i,a) : a \in A_i\}$, and let $p : U \to I$ be $p(i,a) = i$; then $p$ is surjective, and a right inverse $s$ selects an element $s(i) = (i, a_i)$ with $a_i \in A_i$, so that $i \mapsto a_i$ is a choice function. Conversely, if $p : X \to I$ is surjective, the fibres $A_i = p^{-1}(i)$ are nonempty and a choice function on the family provides a right inverse. $\square$

### Zorn's Lemma

**Definition.** A **maximal element** of a poset $(P, \leq)$ is an $m \in P$ such that $m \leq x$ implies $x = m$.

**Zorn's lemma.** Let $(P, \leq)$ be a nonempty poset in which every chain has an upper bound. Then $P$ has a maximal element.

The hypothesis that every chain has an upper bound is the essential one; the conclusion is the existence of a maximal element, not of a greatest one, and Zorn's lemma gives no information about which element it is. The lemma is used in the following pattern: one forms the poset of partial solutions to a problem, ordered by extension; the upper bound of a chain of partial solutions is their union, which is again a partial solution; Zorn's lemma gives a maximal partial solution, and maximality is then shown to force the solution to be total.

### The Well-Ordering Theorem

**Theorem (Zermelo).** Every set can be well-ordered: for every set $X$ there is a total order on $X$ in which every nonempty subset has a least element.

The well-ordering is not produced by an explicit rule; it is a choice of a least element from every nonempty subset, which is the content of the axiom.

### The Equivalence

**Theorem.** The axiom of choice, Zorn's lemma and the well-ordering theorem are equivalent.

**Proof.** **(Zorn $\Rightarrow$ well-ordering).** Let $X$ be a set, and let $P$ be the set of **well-orderings of subsets of $X$**, that is, of pairs $(A, \preceq)$ with $A \subseteq X$ and $\preceq$ a well-ordering of $A$. Order $P$ by extension: $(A,\preceq) \leq (B,\preceq')$ if $A \subseteq B$, the order $\preceq'$ restricts to $\preceq$ on $A$, and every element of $A$ precedes every element of $B \setminus A$ in $\preceq'$. Every chain in $P$ has an upper bound: the union of the members of the chain, with the order that restricts to the given one on each member and that puts all elements of an earlier member before all elements of a later one; the union of a chain of well-orderings of this shape is again a well-ordering of the union, since any nonempty subset meets the first member of the chain it intersects and there takes its least element. By Zorn's lemma $P$ has a maximal element $(A,\preceq)$. If $A \neq X$, choose $x \in X \setminus A$ and put $B = A \cup \{x\}$ with the order extending $\preceq$ and with $x$ greatest; this is a well-ordering strictly extending $(A,\preceq)$, a contradiction. Hence $A = X$ and $X$ is well-ordered.

**(Well-ordering $\Rightarrow$ axiom of choice).** Let $(A_i)_{i \in I}$ be a family of nonempty sets with union $U$. Well-order $U$ and define $f(i)$ to be the least element of $A_i$ in that well-ordering. Then $f$ is a choice function.

**(Axiom of choice $\Rightarrow$ Zorn's lemma).** Assume AC and let $(P,\leq)$ be a nonempty poset in which every chain has an upper bound. Suppose that $P$ has no maximal element, so that for every $x \in P$ the set $U(x) = \{y \in P: x < y\}$ is nonempty. By AC there is a function $s$ with $s(x) \in U(x)$ for every $x$. Define by transfinite recursion a function $F$ on the ordinals into $P$ by $F(0) = $ any element of $P$, $F(\alpha+1) = s(F(\alpha))$, , for a limit ordinal $\lambda$, $F(\lambda) = s(u_\lambda)$ where $u_\lambda$ is an upper bound of the chain $\{F(\beta): \beta < \lambda\}$, which exists by hypothesis and is selected by a fixed choice function on the nonempty subsets of $P$. The construction makes $F$ strictly increasing, so $F$ is an injection from the proper class of ordinals into the set $P$, which is impossible. Hence $P$ has a maximal element. The transfinite recursion and the fact that the ordinals form a proper class are results; the two implications proved above need only the language of well-orders.

This completes the cycle $AC \Rightarrow \text{Zorn} \Rightarrow \text{well-ordering} \Rightarrow AC$, so the three statements are equivalent. $\square$

### Uses in the Corpus

The axiom of choice enters algebra through Zorn's lemma, and the corpus records the following applications, each in the article where the objects are introduced.

- **Maximal ideals.** Every nonzero commutative ring has a maximal ideal; the poset is the set of proper ideals ordered by inclusion, and the union of a chain of proper ideals is a proper ideal. Treated.
- **Bases of a vector space.** Every vector space has a basis, and any linearly independent set is contained in a basis; the poset is the set of linearly independent subsets ordered by inclusion. Treated, over a general ring.
- **Algebraic closure.** Every field has an algebraic closure; the poset is the set of algebraic extensions ordered by inclusion. Treated.
- **Maximal filters.** Every filter on a set extends to an ultrafilter; the poset is the set of filters containing a given one, ordered by inclusion, and the union of a chain of filters is a filter. The argument is given below, since it uses only the power-set lattice of *Sets, Functions and Relations* and the order theory of *Order Theory and Lattices*.

**Proposition.** Every filter on a set $X$ is contained in an ultrafilter on $X$.

**Proof.** A **filter** on $X$ is a family $\mathcal{F} \subseteq \mathcal{P}(X)$ that is upward closed ($A \in \mathcal{F}$ and $A \subseteq B$ imply $B \in \mathcal{F}$), closed under finite intersections, and does not contain $\emptyset$; it is an **ultrafilter** if in addition, for every $A \subseteq X$, exactly one of $A$ and $X \setminus A$ lies in $\mathcal{F}$. Let $\mathcal{F}$ be a filter and let $P$ be the set of filters on $X$ containing $\mathcal{F}$, ordered by inclusion. $P$ is nonempty, and the union of a chain of filters is a filter: upward closure and finite intersections are inherited from the members of the chain, and $\emptyset$ is in no member. By Zorn's lemma, choose a maximal element $\mathcal{U} \in P$. If $A \subseteq X$ with neither $A$ nor $X \setminus A$ in $\mathcal{U}$, then $\mathcal{U} \cup \{A \cap B : B \in \mathcal{U}\}$ generates a strictly larger filter, since $A \cap B \neq \emptyset$ for every $B \in \mathcal{U}$ (else $X \setminus A \in \mathcal{U}$ by upward closure of $\mathcal{U}$), contradicting maximality; the case with $X \setminus A$ is symmetric. Hence $\mathcal{U}$ is an ultrafilter. $\square$

The proposition is the set-theoretic form of the **ultrafilter principle**, itself equivalent to a weak form of the axiom of choice; the corpus uses it in the construction of ultraproducts and in the Stone representation of Boolean algebras in Part V.

## Summary

Two sets are equipotent when a bijection between them exists; equipotence is an equivalence relation, and $|X| \leq |Y|$ means that an injection $X \to Y$ exists. A set is finite when it is equipotent to $\{1,\ldots,n\}$ for some $n$, and infinite otherwise; the number of elements of a finite set is well defined by the pigeonhole principle. A Dedekind-infinite set — one equipotent to a proper subset — is infinite, and the converse needs countable choice. The Schröder–Bernstein theorem, proved from the Knaster–Tarski fixed-point theorem, states that injections in both directions yield a bijection, so $\leq$ is antisymmetric.

$\mathbb{N} \times \mathbb{N}$, $\mathbb{Z}$ and $\mathbb{N}^k$ are countably infinite; a countable union of countable sets is countable, by countable choice. Cantor's theorem, $|X| < |\mathcal{P}(X)|$, makes $\mathcal{P}(\mathbb{N})$ uncountable and shows that there is no largest cardinal. Cardinal sum, product and exponentiation are defined by disjoint union, product and function set, satisfy the usual arithmetic laws, and satisfy $2^{\kappa} = |\mathcal{P}(X)|$ for $|X| = \kappa$; for infinite cardinals under the axiom of choice, $\kappa + \lambda = \kappa \cdot \lambda = \max(\kappa,\lambda)$ and $\kappa^n = \kappa$. The continuum hypothesis asserts $2^{\aleph_0} = \aleph_1$ and is independent of the Zermelo–Fraenkel axioms with choice.

The axiom of choice asserts the existence of choice functions on arbitrary families and is equivalent to the assertion that every surjection has a right inverse; Zorn's lemma asserts that a nonempty poset in which every chain has an upper bound has a maximal element; the well-ordering theorem asserts that every set can be well-ordered. The three are equivalent: Zorn gives the well-ordering by a maximal well-orderable subset, the well-ordering gives choice by selecting least elements, and choice gives Zorn by an unbounded transfinite recursion. The corpus uses Zorn's lemma for maximal ideals, bases of vector spaces, algebraic closures and ultrafilters, and the ultrafilter case is carried out here from the power-set lattice alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X \cong Y$, $|X| = |Y|$ | Equipotence: a bijection $X \to Y$ exists |
| $|X| \leq |Y|$, $|X| < |Y|$ | Injection $X \to Y$ exists; injection but no bijection |
| $\{1,\ldots,n\}$ | Canonical finite set of $n$ elements |
| $\mathbb{N}$, $\mathbb{Z}$ | Natural numbers and integers; the further number systems belong to *Rings and Fields* |
| $\aleph_0 = |\mathbb{N}|$ | First infinite cardinal, the countable one |
| $\aleph_1$ | Least uncountable cardinal |
| $\mathfrak{c} = 2^{\aleph_0}$ | Cardinality of the continuum, $|\mathcal{P}(\mathbb{N})|$ |
| $\mathcal{P}(X)$ | Power set; $|\mathcal{P}(X)| = 2^{|X|}$ |
| $\sqcup$, $\kappa + \lambda$ | Disjoint union; sum of cardinals |
| $X \times Y$, $\kappa \cdot \lambda$ | Product; product of cardinals |
| $X^{Y}$, $\kappa^{\lambda}$ | Set of functions $Y \to X$; cardinal exponentiation |
| CH, GCH | Continuum hypothesis $2^{\aleph_0}=\aleph_1$; generalised form |
| AC, AC$_\omega$, DC | Axiom of choice; countable choice; dependent choice |
| Zorn's lemma | Chain-bounded nonempty poset has a maximal element |
| $\mathcal{U}$, $\mathcal{F}$ | Ultrafilter; filter on a set |





## Further Reading

- Thomas Jech, *Set Theory*, 3rd millennium ed. (Springer, 2003), for cardinal arithmetic, the axiom of choice and its equivalents, and the independence of the continuum hypothesis.
- Kenneth Kunen, *Set Theory: An Introduction to Independence Proofs* (North-Holland, 1980), for the Zermelo–Fraenkel axioms, the constructible universe and forcing.
- Paul J. Cohen, *Set Theory and the Continuum Hypothesis* (Benjamin, 1966), for the forcing method and the independence of CH.
- Kurt Gödel, *The Consistency of the Continuum Hypothesis* (Princeton University Press, 1940), for the constructible universe and the consistency of CH.
- Horst Herrlich, *Axiom of Choice* (Springer, 2006), for the catalogue of equivalent principles and of the results that fail without choice.
- Wacław Sierpiński, *Cardinal and Ordinal Numbers*, 2nd ed. (PWN, 1965), for the classical development of cardinal arithmetic and the Schröder–Bernstein theorem.
- Thomas J. Jech, *The Axiom of Choice* (North-Holland, 1973), for the weak choice principles AC$_\omega$ and DC and their interdependence.
