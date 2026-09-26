# __Algebraically Closed Fields__

## Introduction

An algebraically closed field is one in which every nonconstant polynomial has a root, so that the irreducible polynomials are exactly the linear ones and the field admits no proper algebraic extension. The complex numbers are the prototype, and the fundamental theorem of algebra is the statement that $\mathbb{C}$ is algebraically closed. Every field embeds in an algebraically closed field, and the smallest such algebraic extension, the **algebraic closure**, is unique up to isomorphism; it is the algebraically closed analogue of the real closure of *Real-Closed and Complete Ordered Fields*.

The classification of algebraically closed fields is remarkably rigid: by the Steinitz theorem a field of this kind is determined up to isomorphism by its characteristic and its transcendence degree over the prime field. This rigidity has a logical counterpart, the Lefschetz principle, which transfers any first-order statement from one algebraically closed field of characteristic zero to all of them.

This article defines algebraically closed fields, records their elementary properties, constructs the algebraic closure and proves its uniqueness, states the fundamental theorem of algebra and locates its algebraic proof in the real-closed theory, and formulates the Steinitz and Lefschetz theorems. Throughout, $F$ is a field, $K$ an extension field, and $\overline{F}$ denotes an algebraic closure of $F$. Splitting fields and normality are from *Splitting Fields and Algebraic Closure*, real-closedness from *Real-Closed and Complete Ordered Fields*, and the theory of polynomial factorization from *Unique Factorisation Domains*.

---

## Algebraically Closed Fields

### Definition and Equivalent Conditions

**Definition.** A field $K$ is **algebraically closed** if every nonconstant polynomial $p \in K[x]$ has a root in $K$.

**Theorem.** For a field $K$ the following are equivalent.

**(a)** $K$ is algebraically closed.

**(b)** Every polynomial $p \in K[x]$ of positive degree splits into linear factors over $K$, so $K$ contains all roots of every polynomial with coefficients in $K$.

**(c)** The only irreducible polynomials in $K[x]$ are the linear ones.

**(d)** $K$ has no proper algebraic extension: if $L/K$ is algebraic then $L = K$.

**(e)** $K$ has no finite extension of degree $> 1$.

**(f)** $K[x]$ is a unique factorization domain in which every irreducible element is of degree $1$, and every element of $K$ has an $n$-th root in $K$ for every $n \geq 1$.

**Proof.** (a) $\Rightarrow$ (b): divide $p$ by $x - a$ for a root $a$ and iterate, using that the degree drops at each step. (b) $\Rightarrow$ (c): an irreducible polynomial of positive degree is nonconstant, hence has a linear factor, hence is linear. (c) $\Rightarrow$ (d): if $L/K$ is algebraic and $\alpha \in L$ with minimal polynomial $m$ over $K$, then $m$ is irreducible, hence linear, so $\alpha \in K$. (d) $\Rightarrow$ (e) is immediate since a finite extension is algebraic. (e) $\Rightarrow$ (a): given $p$ of degree $> 0$ and an irreducible factor $m$, the field $K[x]/(m)$ is a finite extension of $K$ of degree $\deg m$, so $\deg m = 1$ and $m$ has a root in $K$. For (f): $K[x]$ is a UFD for every field, so the first clause of (f) says exactly that the irreducible elements of $K[x]$ are the linear polynomials, which is (c); conversely (c) gives both clauses, the second because $x^n - a$ then splits into linear factors. $\square$

### Elementary Properties

**Proposition.** Let $K$ be an algebraically closed field.

**(a)** $K$ is infinite.

**(b)** $K$ is perfect, and if $\operatorname{char} K = p > 0$ the Frobenius endomorphism $x \mapsto x^p$ is an automorphism of $K$.

**(c)** $K$ is the unique algebraic extension of itself, and every finite extension of $K$ is trivial.

**(d)** $K$ has no nontrivial Galois extension, so $\operatorname{Gal}(\overline{K}/K) = 1$ for an algebraic closure $\overline{K}$ of $K$.

**(e)** Every field homomorphism of $K$ into an algebraically closed field $L$ extends to an embedding of any algebraic extension of $K$ into $L$.

**Proof.** (a) If $K$ were finite it would have $q$ elements and the polynomial $x^q - x + 1$ would have no root in $K$, since $a^q = a$ for all $a \in K^\times$ and for $0$; contradiction. (b) In characteristic $p$ the polynomial $x^p - a$ has a root for every $a$, so Frobenius is surjective; hence $K$ is perfect. (c) is (d) of the previous theorem. (d) A Galois extension is algebraic, hence trivial. (e) is the isomorphism extension theorem of *Splitting Fields and Algebraic Closure* applied inside the algebraic closure of $L$. $\square$

### Examples

| Field | Algebraically closed | Reason |
|---|---|---|
| $\mathbb{C}$ | yes | fundamental theorem of algebra |
| $\overline{\mathbb{Q}}$ | yes | algebraic closure of $\mathbb{Q}$, countable |
| $\overline{\mathbb{F}_p}$ | yes | algebraic closure of a finite field, countable |
| the field of Puiseux series over $\mathbb{C}$ | yes | algebraic closure of $\mathbb{C}((t))$ |
| $\mathbb{Q}$ | no | $x^2 - 2$ has no rational root |
| $\mathbb{R}$ | no | $x^2 + 1$ has no real root, but $\mathbb{R}$ is real closed |
| $\mathbb{F}_q$ | no | finite, hence not algebraically closed by (a) |
| $\mathbb{C}(t)$ | no | $x^2 - t$ has no root in $\mathbb{C}(t)$ |
| $\mathbb{Q}(t)$ | no | $x^2 - t$ has no root |

**Remark.** Real closedness and algebraic closedness are different: $\mathbb{R}$ is real closed and not algebraically closed, while $\mathbb{C} = \mathbb{R}(i)$ is algebraically closed and not orderable. The relation between the two is exactly the theorem of *Real-Closed and Complete Ordered Fields* that $F(i)$ is algebraically closed for every real-closed $F$, and that this $F(i)$ is an algebraic closure of $F$.

**Remark.** Algebraic closedness is not inherited by function fields: if $K$ is algebraically closed and $t$ is transcendental over $K$, then $K(t)$ is not algebraically closed, and its algebraic closure is described by the Puiseux series in the case $K = \mathbb{C}$.

---

## The Algebraic Closure

### Definition

**Definition.** An **algebraic closure** of a field $F$ is an extension field $\overline{F}$ that is algebraic over $F$ and algebraically closed.

**Example.** $\mathbb{C}$ is an algebraic closure of $\mathbb{R}$; the algebraic numbers $\overline{\mathbb{Q}}$ form an algebraic closure of $\mathbb{Q}$; for each prime $p$ the union $\overline{\mathbb{F}_p} = \bigcup_{n \geq 1} \mathbb{F}_{p^n}$ is an algebraic closure of $\mathbb{F}_p$.

**Proposition.** If $\overline{F}$ is an algebraic closure of $F$, then $\overline{F}$ is a **splitting field over $F$ of the family of all polynomials in $F[x]$**: every algebraic extension of $F$ embeds in $\overline{F}$, and $\overline{F}$ is generated over $F$ by the roots of polynomials in $F[x]$.

**Proof.** Given an algebraic extension $L/F$ and $\alpha \in L$, the element $\alpha$ has a minimal polynomial over $F$, which splits in $\overline{F}$; the set of roots of all such minimal polynomials in $\overline{F}$ is a subfield of $\overline{F}$ algebraic over $F$, hence equal to $\overline{F}$ by (d) of the equivalent-conditions theorem applied with $K = \overline{F}$ and $L$ that subfield. Algebraicity of $\overline{F}/F$ gives that every element is a root of some polynomial in $F[x]$. $\square$

### Existence

**Theorem (Steinitz).** Every field $F$ has an algebraic closure.

**Proof.** Suppose first that $F$ is countable, so that $F_n[x]$ is countable at every stage below. Put $F_0 = F$, and given $F_n$, enumerate the nonconstant polynomials of $F_n[x]$ as $p_{n,1}, p_{n,2}, \ldots$ and build an ascending chain of fields

$$
F_n = K_{n,0} \subseteq K_{n,1} \subseteq K_{n,2} \subseteq \cdots, \qquad K_{n,j+1} = \text{splitting field of } p_{n,j+1} \text{ over } K_{n,j},
$$

which exists by *Splitting Fields and Algebraic Closure*, and put $F_{n+1} = \bigcup_j K_{n,j}$. Then every $F_n$ is countable and every polynomial of $F_n[x]$ splits in $F_{n+1}$, while $K = \bigcup_n F_n$ is a field, being a union of an increasing chain of fields, and it is algebraic over $F$ by transitivity. Given $q \in K[x]$, its finitely many coefficients lie in $F_n$ for some $n$, so $q$ splits in $F_{n+1} \subseteq K$; hence $K$ is algebraically closed, and it is an algebraic closure of $F$.

For a general field $F$ the same construction is carried out by transfinite recursion: at each stage one takes a splitting field over the field constructed so far of every nonconstant polynomial over it, and at limit ordinals one takes the union of the chain. Equivalently, one orders by inclusion the algebraic extensions of $F$ of cardinality at most $\max\{\aleph_0, \lvert F \rvert\}$, applies Zorn's lemma as in *Splitting Fields and Algebraic Closure*, and obtains an algebraic extension of $F$ with no proper algebraic extension, which is algebraically closed. $\square$

**Remark.** The construction uses the axiom of choice only in the splitting-field steps. The transfinite version of the same argument, closing under splitting fields of all polynomials by transfinite recursion on the ordinals, gives the algebraic closure directly and shows that its cardinality is at most $\max \{\aleph_0, \lvert F \rvert\}$.

### Uniqueness

**Theorem.** Let $F$ be a field and let $\overline{F}$, $\overline{F}'$ be two algebraic closures of $F$. Then there is an $F$-isomorphism $\overline{F} \to \overline{F}'$.

**Proof.** Consider the set of pairs $(E, \sigma)$ with $E$ an intermediate field $F \subseteq E \subseteq \overline{F}$ and $\sigma : E \to \overline{F}'$ an $F$-embedding. The set is nonempty ($E = F$) and is partially ordered by extension, and Zorn's lemma provides a maximal element $(E, \sigma)$, because the union of a chain of compatible embeddings is an embedding. If $E \neq \overline{F}$, take $\alpha \in \overline{F} \setminus E$ and let $m$ be its minimal polynomial over $E$; the polynomial $m^\sigma$ over $\sigma(E)$ has a root $\beta$ in the algebraically closed field $\overline{F}'$, since $\overline{F}'$ is algebraically closed and $\sigma(E) \subseteq \overline{F}'$. Then $\sigma$ extends to $E(\alpha) \to \overline{F}'$ with $\alpha \mapsto \beta$, contradicting maximality. Hence $E = \overline{F}$, and $\sigma(\overline{F}) \subseteq \overline{F}'$ is an algebraic extension of $\sigma(F) = F$ inside the algebraic closure $\overline{F}'$, hence equals $\overline{F}'$ by (d). $\square$

**Corollary.** The algebraic closure of $F$ is unique up to $F$-isomorphism, and one writes $\overline{F}$ for any chosen representative.

**Corollary.** If $K/F$ is algebraic then every $F$-embedding $K \to \overline{F}$ extends to an automorphism of $\overline{F}$.

**Proof.** Apply the uniqueness construction with $K$ in place of $F$: the embedding extends to an isomorphism of algebraic closures, and $\overline{F}$ is an algebraic closure of $K$ as well. $\square$

---

## The Fundamental Theorem of Algebra

**Theorem (fundamental theorem of algebra).** The field $\mathbb{C}$ of complex numbers is algebraically closed: every nonconstant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Algebraic proof, in outline.** By *Real-Closed and Complete Ordered Fields*, $\mathbb{R}$ is real closed: every positive real is a square, and every real polynomial of odd degree has a real root. The theorem proved there states that if $F$ is real closed then $F(i)$ is algebraically closed; taking $F = \mathbb{R}$ gives $\mathbb{C} = \mathbb{R}(i)$ algebraically closed. The two ingredients of the proof are the odd-degree root condition, which handles the real part of the problem by reducing degrees through the auxiliary polynomial argument, and the square-root condition, which handles the quadratic factor. $\square$

**Remark (the analytic proof).** The classical alternative proof shows that a polynomial $p$ of degree $n \geq 1$ without a root would make $1/p$ a bounded entire function, hence constant by Liouville's theorem, a contradiction. This proof belongs to the analytic theory of $\mathbb{C}$, which lies in categories 25–26 and is not developed in this corpus's ring-theoretic articles; the algebraic proof above is the one that generalises to arbitrary real-closed fields.

**Corollary.** $\mathbb{C}$ is an algebraic closure of $\mathbb{R}$, and $\mathbb{C} = \overline{\mathbb{R}}$.

**Corollary.** Every real polynomial of degree $n \geq 1$ factors over $\mathbb{R}$ into linear and irreducible quadratic factors, and over $\mathbb{C}$ into $n$ linear factors counted with multiplicity.

**Corollary.** Every polynomial of degree $n$ over an algebraically closed field has exactly $n$ roots counted with multiplicity, and its discriminant vanishes exactly when it has a repeated root.

**Proof.** Factor into linear terms over the algebraically closed field, and count. The discriminant statement is the standard criterion from *Galois Theory*. $\square$

---

## The Steinitz Classification

### Transcendence Degree

**Definition.** Let $K/F$ be a field extension. A subset $S \subseteq K$ is **algebraically independent** over $F$ if no nonzero polynomial in finitely many distinct elements of $S$ with coefficients in $F$ vanishes at them. A **transcendence basis** of $K/F$ is a maximal algebraically independent subset. The **transcendence degree** $\operatorname{tr.deg}_F K$ is the cardinality of a transcendence basis; it is well defined by the exchange property, and every two transcendence bases have the same cardinality.

**Example.** $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{Q}(t) = 1$, and $\operatorname{tr.deg}_{\mathbb{Q}} \overline{\mathbb{Q}} = 0$; more generally an extension is algebraic exactly when its transcendence degree is $0$.

**Example.** $\operatorname{tr.deg}_{\mathbb{Q}} \mathbb{C} = 2^{\aleph_0}$, the cardinality of the continuum, and $\operatorname{tr.deg}_{\overline{\mathbb{Q}}} \mathbb{C} = 2^{\aleph_0}$; both are the cardinality of a transcendence basis of $\mathbb{C}$, and the computation is by cardinality: $\mathbb{C}$ has cardinality $2^{\aleph_0}$ and $\overline{\mathbb{Q}}$ is countable, so a transcendence basis of $\mathbb{C}$ over $\mathbb{Q}$ has cardinality $2^{\aleph_0}$.

**Theorem (Steinitz).** Two algebraically closed fields are isomorphic if and only if they have the same characteristic and the same transcendence degree over their common prime field. More explicitly, if $k$ is a prime field (so $k = \mathbb{Q}$ or $k = \mathbb{F}_p$) and $K$ is an algebraically closed field of characteristic $\operatorname{char} k$ with $\operatorname{tr.deg}_k K = \kappa$, then $K$ is isomorphic to an algebraic closure of the purely transcendental extension $k(t_\alpha : \alpha < \kappa)$ in $\kappa$ indeterminates.

**Proof sketch.** Given algebraically closed fields $K, K'$ with the same characteristic and transcendence degrees $\kappa = \kappa'$, choose transcendence bases $\{t_\alpha\}$, $\{t'_\alpha\}$ indexed by $\kappa$ and extend the isomorphism of prime fields by $t_\alpha \mapsto t'_\alpha$; this is an isomorphism of $k(\{t_\alpha\})$ onto $k(\{t'_\alpha\})$, both purely transcendental extensions of $k$ with the same transcendence basis. This embedding lies in algebraic extensions $K$ and $K'$, and the isomorphism-extension argument of the uniqueness theorem extends it to $K \to K'$. The converse is immediate because characteristic and transcendence degree are isomorphism invariants. $\square$

**Corollary (classification by cardinality and degree).** Fix a characteristic. Since $\lvert K \rvert = \max\{\aleph_0, \operatorname{tr.deg}_k K\}$ for an algebraically closed field $K$ with prime field $k$, the isomorphism classes of algebraically closed fields of the given characteristic correspond exactly to the possible values of the transcendence degree $\kappa$: for $\kappa$ infinite, $\lvert K \rvert = \kappa$, so all algebraically closed fields of the given characteristic and of an uncountable cardinal $\lambda$ are isomorphic, and they all have $\operatorname{tr.deg} = \lambda$. For countable fields the transcendence degree can be any element of $\{0, 1, 2, \dots\} \cup \{\aleph_0\}$, so there are countably many isomorphism classes of countable algebraically closed fields of a fixed characteristic, one for each degree; the class of degree $0$ is $\overline{\mathbb{Q}}$ in characteristic $0$ and $\overline{\mathbb{F}_p}$ in characteristic $p$.

**Remark (structure of the algebraic closure).** The algebraic closure $\overline{F}$ of a field $F$ has the same cardinality as $F$ when $F$ is infinite, and is countable when $F$ is finite; its transcendence degree over $F$ is $0$, and $\overline{F}$ is unique. The absolute Galois group $\operatorname{Gal}(\overline{F}/F)$, studied in *Ring and Field Automorphisms*, carries the arithmetic content that the isomorphism class of $\overline{F}$ alone does not see.

---

## The Lefschetz Principle

### Statement

**Theorem (Lefschetz principle).** Let $\varphi$ be a statement of first-order logic in the language of rings. Then $\varphi$ holds in every algebraically closed field of characteristic $0$ if and only if it holds in $\mathbb{C}$. More generally, if $\varphi$ holds in one algebraically closed field of characteristic $0$ then it holds in all of them.

**Proof sketch.** The theory of algebraically closed fields of characteristic $0$, denoted $\mathrm{ACF}_0$, has as axioms the field axioms, an axiom scheme stating that every nonconstant polynomial in one variable has a root, one axiom for each degree, and the axioms $n \cdot 1 \neq 0$ for each $n \geq 1$. This theory admits quantifier elimination, proved by a back-and-forth argument that extends an isomorphism between finitely generated subfields step by step; in characteristic $0$ the prime field is $\mathbb{Q}$ in every model, so a quantifier-free sentence has the same truth value in all models of $\mathrm{ACF}_0$. Hence any two models of $\mathrm{ACF}_0$ are elementarily equivalent, and a complete theory has exactly one elementary equivalence class, so a first-order sentence is true in one model if and only if it is true in all. $\square$

**Corollary (transfer).** A first-order statement in the language of fields that involves only finitely many polynomial identities with integer coefficients and is true in $\mathbb{C}$ is true in every algebraically closed field of characteristic $0$.

**Corollary (the principle in its classical form).** Let $f_1, \dots, f_m, g \in \mathbb{Z}[x_1, \dots, x_n]$ be polynomials. If the implication

$$
f_1 = \dots = f_m = 0 \implies g = 0
$$

holds over $\mathbb{C}$, then it holds over every algebraically closed field of characteristic $0$; and it holds over every algebraically closed field of sufficiently large characteristic.

**Proof sketch.** The first assertion is the previous corollary applied to the sentence expressing the implication, which is first-order and has no free variables once universally quantified. For the second, the same sentence, written out, involves finitely many integer coefficients, and the set of characteristics in which it can fail is described by a first-order statement in each prime characteristic; by the appropriate completeness results for $\mathrm{ACF}_p$, a sentence is true in $\overline{\mathbb{F}_p}$ for all sufficiently large $p$ if it is true in $\mathbb{C}$, since the sentences true in $\mathbb{C}$ are exactly the sentences provable in $\mathrm{ACF}_0$, and a proof uses finitely many primes. $\square$

**Example (Hilbert's Nullstellensatz).** For an algebraically closed field $K$ and an ideal $I \subseteq K[x_1, \dots, x_n]$, the radical of $I$ consists exactly of the polynomials vanishing on the common zero set of $I$. This is the standard Nullstellensatz of commutative algebra, cited here rather than proved: its weak form states that a proper ideal of $K[x_1, \dots, x_n]$ has a common zero in $K^n$ when $K$ is algebraically closed, and the strong form quoted here is deduced from the weak form by the Rabinowitsch trick.

**Remark (limits of the principle).** The Lefschetz principle applies to first-order statements only, that is, to statements about elements of the field, polynomial identities and the field operations. Statements that quantify over subsets, over ideals, or over finitely generated modules are not first-order in this language, and statements involving the order do not transfer, since an algebraically closed field is not orderable. In particular $\mathbb{R}$ and $\mathbb{C}$ are not elementarily equivalent: the sentence $\exists x\,(x^2 + 1 = 0)$ holds in $\mathbb{C}$ and fails in $\mathbb{R}$. The model companion of the theory of fields is the theory of algebraically closed fields, while the model companion of the theory of ordered fields is the theory of real-closed fields treated in *Real-Closed and Complete Ordered Fields*.

---

## Summary

A field $K$ is algebraically closed when every nonconstant polynomial over $K$ has a root, equivalently when every polynomial splits into linear factors, equivalently when the only irreducible polynomials are linear, equivalently when $K$ has no proper algebraic or finite extension. Such a field is infinite, perfect, and admits no nontrivial Galois extension. Every field $F$ has an algebraic closure $\overline{F}$, an algebraic extension that is algebraically closed, constructed as the union of an increasing chain of splitting fields; it is unique up to $F$-isomorphism by a maximality argument, and it is a splitting field over $F$ of the family of all polynomials in $F[x]$ into which every algebraic extension of $F$ embeds.

$\mathbb{C}$ is algebraically closed, by the fundamental theorem of algebra; the algebraic proof proceeds through the real closedness of $\mathbb{R}$ and the theorem that $F(i)$ is algebraically closed for real-closed $F$. Algebraically closed fields are classified by the Steinitz theorem: two of them are isomorphic exactly when they have the same characteristic and the same transcendence degree over the prime field; since the cardinality of an infinite such field is the maximum of $\aleph_0$ and the transcendence degree, fields of a fixed characteristic and uncountable cardinal $\lambda$ form a single isomorphism class, while the countable ones are classified by the countably many possible degrees, the degree-$0$ class being $\overline{\mathbb{Q}}$ or $\overline{\mathbb{F}_p}$ according to the characteristic. The Lefschetz principle is the logical counterpart: a first-order sentence in the language of rings holds in every algebraically closed field of characteristic $0$ if and only if it holds in $\mathbb{C}$, and it holds in all algebraically closed fields of sufficiently large characteristic; this transfers polynomial identities, and their ideal-theoretic consequences such as the Nullstellensatz, between algebraically closed fields.

| Field | Algebraically closed | Characteristic | $\operatorname{tr.deg}$ over prime field |
|---|---|---|---|
| $\overline{\mathbb{Q}}$ | yes | $0$ | $0$ |
| $\mathbb{C}$ | yes | $0$ | $2^{\aleph_0}$ |
| $\overline{\mathbb{F}_p}$ | yes | $p$ | $0$ |
| $\overline{\mathbb{F}_p(t)}$ | yes | $p$ | $1$ |
| $\mathbb{Q}$ | no | $0$ | $0$ |
| $\mathbb{R}$ | no | $0$ | $2^{\aleph_0}$ |
| $\mathbb{F}_q$ | no | $p$ | $0$ |
| $\mathbb{C}(t)$ | no | $0$ | $2^{\aleph_0}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $K$ | Fields |
| $\operatorname{char} K$ | Characteristic of the field $K$ |
| $\overline{F}$ | Algebraic closure of $F$ |
| $F^{rc}$ | Real closure of $F$ (from *Real-Closed and Complete Ordered Fields*) |
| $\overline{\mathbb{Q}}$ | Algebraic numbers |
| $\overline{\mathbb{F}_p}$ | Algebraic closure of $\mathbb{F}_p$ |
| $\mathbb{C}(t)$, $\mathbb{F}_p(t)$ | Rational function fields |
| $\operatorname{tr.deg}_F K$ | Transcendence degree of $K$ over $F$ |
| $\operatorname{Gal}(L/K)$ | Galois group |
| $F(i)$ | Quadratic extension by a square root of $-1$ |
| $\mathrm{ACF}_0$, $\mathrm{ACF}_p$ | First-order theory of algebraically closed fields of the given characteristic |
| $K[x]$ | Polynomial ring in one variable |
| $K[x_1,\dots,x_n]$ | Polynomial ring in $n$ variables |

## Further Reading

- Ernst Steinitz, "Algebraische Theorie der Körper", *Journal für die reine und angewandte Mathematik* 137 (1910), for the existence and uniqueness of the algebraic closure and the classification of algebraically closed fields.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for algebraic closures, transcendence degree and the Steinitz theorem.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the fundamental theorem of algebra and the extension theorems for embeddings.
- Bartel Leendert van der Waerden, *Algebra I and II* (Springer, 2003), for the Lefschetz principle and the classical transfer of algebraic statements.
- Solomon Lefschetz, *Algebraic Geometry* (Princeton University Press, 1953), for the principle in its original algebraic-geometric form.
- David Marker, *Model Theory: An Introduction* (Springer, 2002), for $\mathrm{ACF}_0$, $\mathrm{ACF}_p$, quantifier elimination and the precise form of the Lefschetz principle.
- David Mumford, *The Red Book of Varieties and Schemes* (Springer, 1999), for the Nullstellensatz over algebraically closed fields.
