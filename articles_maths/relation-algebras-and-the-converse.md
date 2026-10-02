
# __Relation Algebras and the Converse__

## Introduction

The binary relations on a set carry three operations: the Boolean operations of union, intersection and
complement, the **composition** $R ; S$ of two relations, and the **converse** $R^{-1}$ that reverses
each ordered pair. Composition is associative, has the **diagonal** $\Delta = 1'$ as identity, and
distributes over unions; the converse is an **involution on the elements**, reversing the order of the
factors of a composite and commuting with the Boolean operations. A **relation algebra** is the
abstract structure with those operations and the axioms they satisfy, of which the relations on a set
form the standard example. This article states the axioms, proves that the relations on a set satisfy
them, isolates the converse as the involution and examines its fixed part, the **symmetric** relations,
and it treats the **residuals** of composition and the **Peircean law** that links the converse to
composition through the complement.

The article presupposes *Sets, Functions and Relations* — relations, their composition and their
converse — *The Converse Relation as an Operator*, in this category, where the passage $R \mapsto
R^{-1}$ is studied as an operator, and *Order Theory and Lattices* and *Boolean Algebras with an
Involution*, in this group, for the Boolean operations and the complement. The article uses the
notation of *The Converse Relation as an Operator* for the converse and writes it $R^{-1}$; the
literature mark $\breve{R}$ is not used.

Three boundaries are observed. No **topology** is used. The algebra of **matrices over a field** and
the **transpose**, which is the other standard instance of a converse, are *Linear Spaces* and *Linear
Algebras*, later in this Part, and are named only; the article works with relations on a set. The
**adjoint** in the involutive sense, and the reading of the converse as an adjoint, belong to the
`* Operator Theory` group of this category and are named only. Nothing linear and no **form** is used.

## The Algebra of Binary Relations

### Composition, Converse and the Diagonal

Let $X$ be a set and let $\mathcal{P}(X \times X)$ be the set of binary relations on $X$. For $R, S
\subseteq X \times X$ put

$$
R ; S = \{(x,z) : \text{there is } y \in X \text{ with } (x,y) \in R \text{ and } (y,z) \in S\},
\qquad R^{-1} = \{(y,x) : (x,y) \in R\},
$$

and let $\Delta = \{(x,x) : x \in X\}$ be the **diagonal**, written $1'$.

**Proposition.** Composition is associative, $\Delta$ is a two-sided identity for it, and composition
distributes over unions on both sides:

$$
(R ; S) ; T = R ; (S ; T), \qquad R ; \Delta = R = \Delta ; R, \qquad
R ; (S \cup T) = (R ; S) \cup (R ; T), \qquad (S \cup T) ; R = (S ; R) \cup (T ; R) .
$$

**Proof.** For the associativity, $(x,w) \in (R;S);T$ if and only if there are $y,z$ with $(x,y) \in
R$, $(y,z) \in S$, $(z,w) \in T$, which is symmetric in the two groupings. The identity and the
distributivity are immediate from the definition, the latter because a witness $y$ for the union is a
witness for one of the two relations.

**Proposition.** The converse reverses composition and commutes with the Boolean operations:

$$
(R^{-1})^{-1} = R, \qquad (R ; S)^{-1} = S^{-1} ; R^{-1}, \qquad
(R \cup S)^{-1} = R^{-1} \cup S^{-1}, \qquad (\overline{R})^{-1} = \overline{R^{-1}},
$$

where $\overline{R} = (X \times X) \setminus R$. Hence $R \mapsto R^{-1}$ is an order isomorphism of
$\mathcal{P}(X \times X)$ with its opposite, of order two, and it is the involution of the relation
algebra.

**Proof.** The first identity is the definition read twice. For the second, $(z,x) \in (R;S)^{-1}$
means $(x,z) \in R;S$, so there is $y$ with $(x,y) \in R$, $(y,z) \in S$; then $(z,y) \in S^{-1}$ and
$(y,x) \in R^{-1}$, so $(z,x) \in S^{-1};R^{-1}$. The congruence for the union is the same reading, and
the one for the complement follows because the converse is a bijection of $X \times X$.

### The Relation Algebra Axioms

**Definition.** A **relation algebra** is a set $A$ with two binary operations $\vee$ and $;$ and a
unary operation ${}^{-1}$ and two constants $0$ and $1'$, such that

1. $(A, \vee)$ is a join-semilattice with least element $0$, and the associated order has meets and a
   greatest element $1$, making $A$ a Boolean algebra;
2. $;$ is associative, has identity $1'$, and distributes over $\vee$ on both sides;
3. ${}^{-1}$ is an involution with $(x \vee y)^{-1} = x^{-1} \vee y^{-1}$ and $(x ; y)^{-1} = y^{-1} ;
   x^{-1}$;
4. the **Peircean law** holds: $(x ; y) \wedge \overline{z} = 0$ implies $(x^{-1} ; z) \wedge
   \overline{y} = 0$ and $(z ; y^{-1}) \wedge \overline{x} = 0$.

**Theorem.** The relations on a set $X$ form a relation algebra under union, composition, the converse
and the constants $\emptyset$ and $\Delta$; the greatest element is $X \times X$, and the complement is
the set complement.

**Proof.** The Boolean part is *Sets, Functions and Relations* and the power-set lattice is treated in
*Order Theory and Lattices*; the first three axioms are the two propositions above, with the converse
of a union and of a composite already computed. The Peircean law is proved in the next section.

The axioms are those of Tarski. The relation algebra $\mathcal{P}(X \times X)$ is the standard
**proper** relation algebra; an abstract relation algebra need not be of this form, and the
representation theorem saying which are is a deeper result and is not used here.

### The Converse as the Involution and the Symmetric Part

The map $R \mapsto R^{-1}$ is the **involution on the elements** of the relation algebra; its fixed
elements are the **symmetric** relations. The symmetry of a relation is a property of the relation,
not of the algebra, and the fixed elements do not form a subalgebra of the relation algebra: they are
closed under union, intersection and complement, but not under composition.

**Proposition.** The fixed elements of the involution are closed under the Boolean operations and
contain $\emptyset$, $X \times X$ and $\Delta$, but they are not closed under composition whenever $X$
has at least three elements.

**Proof.** If $R = R^{-1}$ and $S = S^{-1}$ then $(R \cup S)^{-1} = R^{-1} \cup S^{-1} = R \cup S$ and
likewise for the intersection and the complement, so the fixed set is a Boolean subalgebra. For the
composition, let $X = \{0,1,2\}$, let $R$ be the relation $\{(0,1),(1,0)\}$ and $S$ the relation
$\{(1,2),(2,1)\}$, both symmetric; then $R ; S$ contains $(0,2)$ but not $(2,0)$, so it is not
symmetric.

**Proposition.** Every relation $R$ decomposes as $R = R_{\mathrm{s}} \cup R_{\mathrm{a}}$ with
$R_{\mathrm{s}} = R \cap R^{-1}$ symmetric and $R_{\mathrm{a}} = R \setminus R^{-1}$ satisfying $R_{
\mathrm{a}} \cap R_{\mathrm{a}}^{-1} = \emptyset$.

**Proof.** The two parts are disjoint and their union is $R$; the first is fixed by the involution
because the involution is order-reversing and of order two, and the second is disjoint from its
converse by construction.

## The Residuals and the Peircean Law

### The Residuals of Composition

Composition of relations is a residuated map in each variable, in the sense of *Operators on a Poset*,
and the residuals are computed by a universal condition.

**Definition.** For relations $R, T \subseteq X \times X$ put

$$
R \backslash T = \{(y,z) : (x,y) \in R \Rightarrow (x,z) \in T \text{ for all } x \in X\}, \qquad
T / R = \{(x,y) : (y,z) \in R \Rightarrow (x,z) \in T \text{ for all } z \in X\} .
$$

**Theorem.** For all relations $R, S, T$,

$$
R ; S \subseteq T \quad\Longleftrightarrow\quad S \subseteq R \backslash T \quad\Longleftrightarrow\quad
R \subseteq T / S .
$$

**Proof.** $R;S \subseteq T$ says that every $(x,z)$ with a witness $y$, $(x,y) \in R$, $(y,z) \in S$,
lies in $T$. This holds if and only if for every $(y,z) \in S$ and every $x$ with $(x,y) \in R$ one has
$(x,z) \in T$, which is $S \subseteq R \backslash T$. The second equivalence is the same statement with
the roles of $R$ and $S$ exchanged.

**Corollary.** The maps $S \mapsto R;S$ and $R \mapsto R;S$ are residuated; the residual $R \backslash
T$ is the greatest $S$ with $R;S \subseteq T$, and $T/R$ the greatest $R$ with $R;S \subseteq T$. The
two residuals are related to the converse by $(R \backslash T)^{-1} = T^{-1} / R^{-1}$.

**Proof.** The residuals are the greatest solutions by the theorem and the definition of the order; the
last identity is the definition read through the converse.

### The Peircean Law

**Theorem (Peircean law).** For relations $R, S, T$ on $X$ the following are equivalent:

$$
(R ; S) \cap T = \emptyset, \qquad (R^{-1} ; T) \cap S = \emptyset, \qquad
(T ; S^{-1}) \cap R = \emptyset .
$$

**Proof.** (1) $\Rightarrow$ (2): suppose $(R;S) \cap T = \emptyset$ and suppose some $(a,b)$ lies in
both $R^{-1};T$ and $S$. From $(a,b) \in R^{-1};T$ there is $y$ with $(a,y) \in R^{-1}$ and $(y,b) \in
T$, that is, $(y,a) \in R$ and $(y,b) \in T$; with $(a,b) \in S$ this gives $(y,b) \in R;S$ and $(y,b)
\in T$, contradicting $(R;S) \cap T = \emptyset$. (1) $\Rightarrow$ (3): suppose $(a,b) \in T;S^{-1}$
and $(a,b) \in R$; from $(a,b) \in T;S^{-1}$ there is $y$ with $(a,y) \in T$ and $(y,b) \in S^{-1}$,
that is, $(b,y) \in S$, so $(a,y) \in R;S$ and $(a,y) \in T$, again a contradiction. The implications
(2) $\Rightarrow$ (1) and (3) $\Rightarrow$ (1) are the same arguments read backwards, so the three
statements are equivalent.

**Corollary.** The residual identity $R;S \subseteq T \Leftrightarrow S \subseteq R \backslash T$ and
the Peircean law are equivalent in a relation algebra, in the presence of the other axioms; the
Peircean law is the form in which the converse enters the residual calculus.

**Proof.** The law is the instance $T = \overline{U}$ of the residual identity, and conversely the
residual identity follows from the law by complementing and using the Boolean axioms; the two are two
readings of the same triangle condition.

## Summary

The relations on a set form a relation algebra: a Boolean algebra with an associative composition that
distributes over the joins and has the diagonal as identity, and with the converse $R \mapsto R^{-1}$
as an **involution on the elements** that reverses composites and commutes with the Boolean operations.
The fixed elements of the involution are the symmetric relations, a Boolean subalgebra that is not
closed under composition; every relation is the disjoint union of its symmetric part $R \cap R^{-1}$
and its asymmetric part $R \setminus R^{-1}$.

Composition is residuated in each variable: $R;S \subseteq T$ if and only if $S \subseteq R \backslash
T$ if and only if $R \subseteq T/S$, with the residuals computed by a universal condition and the
residuals exchanged by the converse. The **Peircean law** is the form of that residual calculus that
uses the complement, $(R;S) \cap T = \emptyset$ implying $(R^{-1};T) \cap S = \emptyset$; it is one of
the axioms of the abstract relation algebra, and the relations on a set satisfy it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R ; S$ | Composition of relations: $(x,z)$ with a witness $y$ |
| $R^{-1}$ | Converse of $R$; the involution on the elements |
| $\Delta = 1'$ | The diagonal, the identity of composition |
| $\overline{R}$ | Complement of $R$ in $X \times X$ |
| $R \backslash T$, $T / R$ | Right and left residuals of composition |
| symmetric | $R^{-1} = R$; the fixed elements of the involution |
| $R_{\mathrm{s}}, R_{\mathrm{a}}$ | Symmetric and asymmetric parts $R \cap R^{-1}$ and $R \setminus R^{-1}$ |

## Further Reading

- Alfred Tarski, "On the calculus of relations", *Journal of Symbolic Logic* **6** (1941), 73–89, for the axioms of a relation algebra and the calculus of relations.
- Roger D. Maddux, *Relation Algebras*, Studies in Logic 150 (Elsevier, 2006), for the Peircean law, the residuals and the representation theory.
- Bjarni Jónsson, "Varieties of relation algebras", *Algebra Universalis* **15** (1982), 273–298, for the equational theory and the relation-algebra identities.
- Chris Brink, Wolfram Kahl and Gunther Schmidt, *Relational Methods in Computer Science* (Springer, 1997), for composition, the residuals and the residuated structure of relations.
- Gunther Schmidt and Thomas Ströhlein, *Relations and Graphs* (Springer, 1993), for the calculus of relations, the Peircean law and the residual operations.
