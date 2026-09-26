# __Absolute Values, Valuations and Completions__

## Introduction

An absolute value on a field is a real-valued size function compatible with multiplication and satisfying the triangle inequality; it turns the field into a metric space and hence into a topological field, and it makes possible the operation of completion that produces $\mathbb{R}$ from $\mathbb{Q}$ and $\mathbb{Q}_p$ from $\mathbb{Q}$. The absolute values that satisfy the stronger ultrametric inequality are the **non-Archimedean** ones, and these are equivalent to the **valuations** of commutative algebra: maps to an ordered abelian group that measure divisibility. Ostrowski's theorem states that every nontrivial absolute value on $\mathbb{Q}$ is equivalent either to the usual one or to one of the $p$-adic ones, so the completions of $\mathbb{Q}$ are exactly $\mathbb{R}$ and the fields $\mathbb{Q}_p$.

This article develops absolute values, the ultrametric geometry of the non-Archimedean case, valuations and their rings, Ostrowski's theorem, and the completion of a valued field, with $\mathbb{Q}_p$ as the central example. The general theory of topological rings and of the $I$-adic completion is from *Topological Rings and Fields*; the two have in common the inverse limit description of the completion, and they differ in that on a field the only $I$-adic topologies are the trivial ones, so the field case must proceed through a metric or a valuation.

Throughout, $F$ is a field, $\lvert \cdot \rvert$ an absolute value on it, and $v$ a valuation with value group $\Gamma$. The completion is written $\widehat{F}$, and $\mathbb{Q}_p$, $\mathbb{Z}_p$ and $\mathbb{F}_p$ retain their standard meanings.

---

## Absolute Values

### Definition and Examples

**Definition.** An **absolute value** on a field $F$ is a function $\lvert \cdot \rvert : F \to \mathbb{R}_{\geq 0}$ such that for all $x, y \in F$:

**(AV1)** $\lvert x \rvert = 0$ if and only if $x = 0$;

**(AV2)** $\lvert xy \rvert = \lvert x \rvert \lvert y \rvert$;

**(AV3)** $\lvert x + y \rvert \leq \lvert x \rvert + \lvert y \rvert$.

The absolute value is **non-Archimedean** if it satisfies the stronger **ultrametric inequality**

**(AV3')** $\lvert x + y \rvert \leq \max\{\lvert x \rvert, \lvert y \rvert\}$,

and **Archimedean** otherwise. It is **trivial** if $\lvert x \rvert = 1$ for all $x \neq 0$, and **discrete** if the subgroup $\lvert F^\times \rvert \subseteq \mathbb{R}_{>0}$ is discrete.

**Proposition.** Let $\lvert \cdot \rvert$ be an absolute value on $F$.

**(a)** $\lvert 1 \rvert = 1$ and $\lvert -x \rvert = \lvert x \rvert$; more generally $\lvert \zeta \rvert = 1$ for every root of unity $\zeta$.

**(b)** $\lvert x^{-1} \rvert = \lvert x \rvert^{-1}$ for $x \neq 0$.

**(c)** $\lvert x^n \rvert = \lvert x \rvert^n$ for $n \in \mathbb{Z}$, and $\lvert \lvert x \rvert - \lvert y \rvert \rvert \leq \lvert x - y \rvert$.

**(d)** $d(x,y) = \lvert x - y \rvert$ is a metric on $F$, and $F$ with the induced topology is a topological field.

**(e)** $\lvert \cdot \rvert$ satisfies (AV3') if and only if $\lvert n \cdot 1 \rvert \leq 1$ for every integer $n$.

**Proof.** (a) $\lvert 1 \rvert = \lvert 1 \rvert^2$ and $\lvert 1 \rvert \neq 0$; $\lvert -x \rvert^2 = \lvert x^2 \rvert = \lvert x \rvert^2$. (b) $1 = \lvert x x^{-1} \rvert$. (c) Induction gives the first, and the second is the usual reverse triangle inequality. (d) The metric axioms follow from (AV1)-(AV3); continuity of addition and multiplication follows from the estimates $\lvert (x+h) - (x+h') \rvert \leq \lvert h \rvert + \lvert h' \rvert$ and $\lvert xy - x'y' \rvert \leq \lvert x \rvert \lvert y - y' \rvert + \lvert y' \rvert \lvert x - x' \rvert$, and continuity of inversion from $\lvert x^{-1} - y^{-1} \rvert = \lvert x - y \rvert / \lvert xy \rvert$ with $\lvert x \rvert$ bounded below near $x \neq 0$. (e) If (AV3') holds then $\lvert n \cdot 1 \rvert \leq 1$ by induction. Conversely, if $\lvert n \cdot 1 \rvert \leq 1$ for all $n$, the binomial expansion gives $\lvert x + y \rvert^n \leq (n+1) \max\{\lvert x \rvert, \lvert y \rvert\}^n$, and taking $n$-th roots and letting $n \to \infty$ gives (AV3'). $\square$

### Standard Examples

**Example (the usual absolute value).** On $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ the usual absolute value (or modulus) is Archimedean, and $\lvert n \cdot 1 \rvert = n$, so it is not bounded on the integers.

**Example ($p$-adic absolute values).** Fix a prime $p$. Every $x \in \mathbb{Q}^\times$ factors uniquely as

$$
x = \pm \prod_p p^{a_p(x)}, \qquad a_p(x) \in \mathbb{Z},\ \text{finitely many nonzero},
$$

and the **$p$-adic valuation** is $v_p(x) = a_p(x)$, with $v_p(0) = \infty$. The **$p$-adic absolute value** is

$$
\lvert x \rvert_p = p^{-v_p(x)} \ (\text{for } x \neq 0), \qquad \lvert 0 \rvert_p = 0 .
$$

It is non-Archimedean and discrete: $\lvert p \rvert_p = 1/p$ and $\lvert n \rvert_p = 1$ for $n$ coprime to $p$.

**Example (function fields).** On $k(t)$ the $t$-adic valuation $v_t(f)$ is the order of vanishing of $f$ at $t = 0$, and $\lvert f \rvert = c^{-v_t(f)}$ for a fixed $c > 1$ is a non-Archimedean absolute value; more generally, each irreducible polynomial and the "point at infinity" give an absolute value.

**Example (trivial and discrete).** The trivial absolute value gives the discrete topology. Every absolute value of the form $\lvert x \rvert^\alpha$ with $0 < \alpha \leq 1$ is again an absolute value, Archimedean or not accordingly.

### Equivalence and the Product Formula

**Definition.** Two absolute values $\lvert \cdot \rvert_1$, $\lvert \cdot \rvert_2$ on $F$ are **equivalent** if they induce the same topology on $F$.

**Theorem.** Two nontrivial absolute values on a field $F$ are equivalent if and only if there is a real number $\alpha > 0$ with

$$
\lvert x \rvert_2 = \lvert x \rvert_1^{\alpha} \quad \text{for all } x \in F .
$$

**Proof sketch.** If the relation holds, the two absolute values have the same balls up to scaling of the radius, hence the same topology. Conversely, if the topologies agree, then $\lvert x \rvert_1 < 1$ implies $\lvert x \rvert_2 < 1$ (a sequence tending to $0$ in one topology tends to $0$ in the other), and one shows that the subgroups $\{x : \lvert x \rvert_1 < 1\}$ and $\{x : \lvert x \rvert_2 < 1\}$ coincide; choosing $a$ with $\lvert a \rvert_1 \neq 0, 1$ and comparing $\lvert a^n \rvert_1$ with $\lvert x \rvert_2$ for all $x$ gives the exponent $\alpha$. $\square$

**Theorem (product formula for $\mathbb{Q}$).** For every $x \in \mathbb{Q}^\times$,

$$
\lvert x \rvert_\infty \prod_{p} \lvert x \rvert_p = 1,
$$

where the product is over all primes and the product is finite because $v_p(x) = 0$ for almost all $p$.

**Proof.** Write $\lvert x \rvert_\infty = \prod_p p^{a_p(x)}$ in the factorization of $x$, which holds because $\lvert x \rvert_\infty$ collects the prime powers with sign. Then $\lvert x \rvert_p = p^{-a_p(x)}$, so the product of the $p$-adic terms is $\prod_p p^{-a_p(x)} = \lvert x \rvert_\infty^{-1}$. $\square$

---

## Non-Archimedean Absolute Values

### Ultrametric Geometry

**Theorem.** Let $\lvert \cdot \rvert$ be a non-Archimedean absolute value on $F$.

**(a)** $\lvert x + y \rvert = \max\{\lvert x \rvert, \lvert y \rvert\}$ whenever $\lvert x \rvert \neq \lvert y \rvert$.

**(b)** Every triangle is isosceles: for any $x,y,z$, the three numbers $\lvert x - y \rvert$, $\lvert y - z \rvert$, $\lvert z - x \rvert$ have the property that the two largest are equal.

**(c)** Every point of a closed ball $\{x : \lvert x - a \rvert \leq r\}$ is a centre, and the same for open balls.

**(d)** Any two balls are either disjoint or one contains the other; if they have the same radius and intersect, they are equal.

**(e)** Balls are both open and closed, and $F$ is totally disconnected.

**(f)** A sequence $(x_n)$ is Cauchy if and only if $\lvert x_{n+1} - x_n \rvert \to 0$, and a series $\sum a_n$ converges if and only if $a_n \to 0$.

**Proof.** (a) Suppose $\lvert x \rvert > \lvert y \rvert$. Then $\lvert x \rvert = \lvert (x+y) - y \rvert \leq \max\{\lvert x+y \rvert, \lvert y \rvert\}$, and since $\lvert y \rvert < \lvert x \rvert$ this forces $\lvert x + y \rvert \geq \lvert x \rvert$; combined with (AV3') gives equality. (b) Apply (a) to the identity $x - z = (x-y) + (y-z)$ and its permutations. (c) If $\lvert x - a \rvert \leq r$ and $\lvert y - a \rvert \leq r$ then $\lvert y - x \rvert \leq r$, so the ball with centre $x$ and radius $r$ is contained in the ball with centre $a$ and radius $r$, and symmetry gives equality. (d) Suppose balls $B(a,r)$ and $B(b,s)$ with $r \leq s$ intersect at $c$; then $\lvert x - b \rvert \leq \max\{\lvert x - a \rvert, \lvert a - c \rvert, \lvert c - b \rvert\} \leq s$ for $x \in B(a,r)$ after the estimates, so $B(a,r) \subseteq B(b,s)$. (e) A ball is open by definition; its complement is a union of balls of the same radius, hence open, so it is closed. Total disconnectedness follows from (d), since the only connected subsets are points. (f) If $\lvert x_{n+1} - x_n \rvert \to 0$ then for $m > n$ the telescoping estimate $\lvert x_m - x_n \rvert \leq \max_{n \leq k < m} \lvert x_{k+1} - x_k \rvert \to 0$ shows the sequence is Cauchy; the converse is immediate. For series, the same telescoping argument applies to the partial sums. $\square$

**Remark (two uses of "Archimedean").** The word Archimedean occurs in two unrelated senses in this corpus. An *ordered field* is Archimedean when the natural numbers are unbounded in it, as in *Ordered Fields*; an *absolute value* is non-Archimedean when it satisfies the ultrametric inequality, equivalently when it is bounded on the prime subring. A field with a non-Archimedean absolute value may still carry an ordering, as $\mathbb{Q}(t)$ does, and an Archimedean ordered field may carry a non-Archimedean absolute value, as $\mathbb{Q}$ does through $\lvert \cdot \rvert_p$; the two conditions govern different structures. What is true is that the metric topology of a non-Archimedean absolute value is totally disconnected, so it can never coincide with the order topology of an order-complete field.

### The Value Group

**Definition.** Let $\lvert \cdot \rvert$ be a non-Archimedean absolute value on $F$. The **value group** is the subgroup

$$
\Gamma = \lvert F^\times \rvert \subseteq \mathbb{R}_{>0},
$$

written multiplicatively, and the **residue field** is $k = \mathcal{O}/\mathfrak{m}$ where

$$
\mathcal{O} = \{x \in F : \lvert x \rvert \leq 1\}, \qquad \mathfrak{m} = \{x \in F : \lvert x \rvert < 1\}.
$$

**Proposition.** $\mathcal{O}$ is a subring of $F$ containing $1$ and

$$
\mathcal{O} = \{x : \lvert x \rvert \leq 1\}, \qquad \mathcal{O}^\times = \{x : \lvert x \rvert = 1\}, \qquad \mathfrak{m} = \{x : \lvert x \rvert < 1\}
$$

is its unique maximal ideal; $\mathcal{O}$ is a local ring with residue field $k = \mathcal{O}/\mathfrak{m}$, and $F = \operatorname{Frac}(\mathcal{O})$.

**Proof.** $\mathcal{O}$ is closed under addition by (AV3') and under multiplication by (AV2); the elements of absolute value $1$ are exactly the units, because $\lvert x \rvert = 1$ gives $\lvert x^{-1} \rvert = 1$, and every element of $\mathfrak{m}$ is noninvertible since $\lvert x \rvert < 1$ forces $\lvert x^{-1} \rvert > 1$. Every proper ideal is contained in $\mathfrak{m}$, because a unit generates the whole ring, so $\mathfrak{m}$ is the unique maximal ideal. $\square$

---

## Valuations

### Definition

**Definition.** A **valuation** on a field $F$ is a map

$$
v : F \to \Gamma \cup \{\infty\}
$$

where $\Gamma$ is a totally ordered abelian group (written additively) and $\infty$ is a symbol greater than every element of $\Gamma$, such that for all $x, y \in F$:

**(V1)** $v(x) = \infty$ if and only if $x = 0$;

**(V2)** $v(xy) = v(x) + v(y)$;

**(V3)** $v(x + y) \geq \min\{v(x), v(y)\}$.

A valuation is **discrete** if $\Gamma \cong \mathbb{Z}$, and a **rank-one** valuation if $\Gamma$ embeds in $\mathbb{R}$.

**Theorem (correspondence).** Let $F$ be a field and $c$ a real number with $c > 1$. The assignment

$$
v \mapsto \lvert x \rvert = c^{-v(x)}
$$

is a bijection between the valuations of $F$ with value group $\Gamma \subseteq \mathbb{R}$ and the non-Archimedean absolute values of $F$, and this correspondence is compatible with equivalence: two valuations give equivalent absolute values exactly when they have the same valuation ring.

**Proof.** (V2) and (V3) become (AV2) and (AV3') under $v \mapsto c^{-v}$; conversely $\log_c \lvert x \rvert$ recovers $v$ up to the sign convention. Equivalence of absolute values preserves the unit group $\{x : \lvert x \rvert = 1\}$, hence the valuation ring, and conversely equality of valuation rings determines the unit group and the set $\{x : \lvert x \rvert < 1\}$, hence the topology. $\square$

**Definition.** The **valuation ring** of $v$ is

$$
\mathcal{O}_v = \{x \in F : v(x) \geq 0\},
$$

with maximal ideal $\mathfrak{m}_v = \{x : v(x) > 0\}$ and residue field $k(v) = \mathcal{O}_v/\mathfrak{m}_v$. A **discrete valuation ring** (DVR) is the valuation ring of a discrete valuation.

**Proposition.** Valuation rings are local domains with $F = \operatorname{Frac}(\mathcal{O}_v)$, and $\mathcal{O}_v$ is a maximal proper subring of $F$: if $\mathcal{O}_v \subsetneq R \subseteq F$ with $R$ a subring, then $R = F$.

**Proof.** The local and domain properties are proved as for $\mathcal{O}$ above. For maximality, let $R$ be a subring with $\mathcal{O}_v \subseteq R \subseteq F$ and $R \neq \mathcal{O}_v$, and let $x \in R \setminus \mathcal{O}_v$; then $v(x) < 0$, so $v(x^{-1}) > 0$ and $x^{-1} \in \mathfrak{m}_v \subseteq \mathcal{O}_v \subseteq R$. Given $y \in F$, choose $m \geq 1$ with $v(y) - m\,v(x) \geq 0$, that is, $y x^{-m} \in \mathcal{O}_v \subseteq R$; then $y = (y x^{-m})\,x^{m} \in R$. Hence $R = F$, and $\mathcal{O}_v$ is a maximal proper subring of $F$. $\square$

### Examples

**Example ($p$-adic).** On $\mathbb{Q}$, $v_p$ is a discrete valuation with $\mathcal{O} = \mathbb{Z}_{(p)} = \{a/b : p \nmid b\}$, $\mathfrak{m} = p\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$; here $\mathbb{Z}_{(p)}$ is the localization of *Localization and the Fraction Field*.

**Example (DVRs).** $\mathbb{Z}_{(p)}$ and $k[t]_{(t)}$ are DVRs, as is $\mathbb{Z}_p$ after completion. A DVR is a principal ideal domain with a unique nonzero maximal ideal, and its nonzero ideals form the chain $\mathcal{O} \supsetneq \mathfrak{m} \supsetneq \mathfrak{m}^2 \supsetneq \cdots$, which is the $I$-adic filtration of *Topological Rings and Fields*.

**Example (higher rank).** The valuation on $\mathbb{C}((t))$ trivial on $\mathbb{C}$ has $\Gamma = \mathbb{Z}$, so it is discrete and of rank one. A field of generalized power series whose exponents form the lexicographically ordered group $\mathbb{Z}^2$ carries a valuation with $\Gamma = \mathbb{Z}^2$; that ordered group does not embed in $\mathbb{R}$, since $(0,1)$ is positive while $n(0,1) < (1,0)$ for every $n$, so the valuation is not of rank one and is not given by $-\log_c \lvert \cdot \rvert$ for any absolute value of that field.

---

## Ostrowski's Theorem

**Theorem (Ostrowski).** Every nontrivial absolute value on $\mathbb{Q}$ is equivalent either to the usual absolute value $\lvert \cdot \rvert_\infty$ or to a $p$-adic absolute value $\lvert \cdot \rvert_p$ for exactly one prime $p$.

**Proof sketch.** Let $\lvert \cdot \rvert$ be nontrivial on $\mathbb{Q}$. If it is Archimedean, one shows that $\lvert \cdot \rvert = \lvert \cdot \rvert_\infty^\alpha$ for some $\alpha > 0$ by comparing the growth of $\lvert m \rvert$ and $\lvert n \rvert$ for integers, using the binomial expansion as in the proof that an Archimedean absolute value is unbounded on $\mathbb{Z}$; this is the classical argument of Ostrowski. If it is non-Archimedean, then $\lvert n \rvert \leq 1$ for all $n$, and since the absolute value is nontrivial there is a prime $p$ with $\lvert p \rvert < 1$. No second prime $q \neq p$ can satisfy $\lvert q \rvert < 1$: if it did, then from a Bézout relation $1 = ap + bq$ one gets $\lvert 1 \rvert \leq \max\{\lvert a \rvert \lvert p \rvert, \lvert b \rvert \lvert q \rvert\} < 1$, a contradiction. Hence $\lvert n \rvert = 1$ for all $n$ coprime to $p$, and $\lvert \cdot \rvert$ is determined by its value $\lvert p \rvert = c \in (0,1)$, giving $\lvert x \rvert = c^{v_p(x)}$, which is equivalent to $\lvert x \rvert_p$ by the choice $\alpha = \log_p c^{-1}$. $\square$

**Corollary (the places of $\mathbb{Q}$).** The places of $\mathbb{Q}$, that is, the equivalence classes of nontrivial absolute values, are the Archimedean place $\infty$ and the non-Archimedean places $p$ for primes $p$; the product formula of the previous section holds over all of them.

**Corollary.** The nontrivial completions of $\mathbb{Q}$ are $\mathbb{R}$ and the fields $\mathbb{Q}_p$, one for each prime $p$.

---

## Completions

### The Completion of a Valued Field

**Definition.** Let $F$ be a field with absolute value $\lvert \cdot \rvert$. The **completion** $\widehat{F}$ is the set of equivalence classes of Cauchy sequences in the metric $d(x,y) = \lvert x - y \rvert$, with the operations defined termwise and the absolute value extended by continuity:

$$
\widehat{\lvert (x_n) \rvert} = \lim_n \lvert x_n \rvert .
$$

**Theorem.** Let $F$ be a field with absolute value $\lvert \cdot \rvert$.

**(a)** $\widehat{F}$ is a field, $\lvert \cdot \rvert$ extends to an absolute value on it, and $F$ embeds densely in $\widehat{F}$.

**(b)** $\widehat{F}$ is complete: every Cauchy sequence in $\widehat{F}$ converges.

**(c)** The absolute value is non-Archimedean exactly when the same is true on $F$. When it is non-Archimedean, so that the valuation ring is defined, both invariants are unchanged: $\Gamma_{\widehat{F}} = \Gamma_F$, and the natural map $\mathcal{O}_F/\mathfrak{m}_F \to \mathcal{O}_{\widehat{F}}/\mathfrak{m}_{\widehat{F}}$ is an isomorphism. The hypothesis is necessary; in the Archimedean case the value set can grow, since $\sqrt2$ is a value of the completion of $\mathbb{Q}$ at $\lvert \cdot \rvert_\infty$ but not a value on $\mathbb{Q}$.

**(d)** $\widehat{F}$ is the unique complete field containing $F$ densely, up to an isometry fixing $F$; it satisfies the universal property that every isometric embedding of $F$ into a complete field extends uniquely.

**Proof sketch.** The termwise operations are well defined on classes because sums and products of Cauchy sequences are Cauchy, and the only obstruction to field axioms is that an element with a Cauchy sequence tending to $0$ must be excluded, which is the definition of the equivalence. Completeness of $\widehat{F}$ is proved by diagonal extraction, and the extension of the absolute value is by continuity. Uniqueness follows by the same argument that identifies two completions of a metric space. For (c), the ultrametric inequality passes to the extension by continuity; if $x = \lim_n x_n \neq 0$ in $\widehat{F}$ then $\lvert x_n - x \rvert < \lvert x \rvert$ for all large $n$, and for those $n$ the ultrametric inequality gives $\lvert x_n \rvert = \lvert x \rvert$, so no new values occur and $\Gamma_{\widehat{F}} = \Gamma_F$; the residue field is unchanged because density supplies, for every $x \in \widehat{F}$ with $\lvert x \rvert \leq 1$, an element $y \in \mathcal{O}_F$ with $\lvert y - x \rvert < 1$. $\square$

**Proposition.** Suppose the topology on $F$ is induced by the $I$-adic topology of a subring $\mathcal{O} \subseteq F$, where $I$ is a proper ideal of $\mathcal{O}$ (as for $\mathbb{Z}_{(p)} \subseteq \mathbb{Q}$ with $I = (p)$, or $k[t]_{(t)} \subseteq k(t)$ with $I = (t)$). Then the metric completion of $\mathcal{O}$ is its $I$-adic completion,

$$
\widehat{\mathcal{O}} = \varprojlim_n \mathcal{O} / I^n ,
$$

and the completion of $F$ is the fraction field of that ring, $\widehat{F} = \operatorname{Frac}(\widehat{\mathcal{O}})$. In particular $\widehat{\mathbb{Z}}_{(p)} = \mathbb{Z}_p$ and $\widehat{\mathbb{Q}} = \mathbb{Q}_p$, while $\widehat{k[t]}_{(t)} = k[[t]]$ and $\widehat{k(t)} = k((t))$; the completion is taken on the subring $\mathcal{O}$, which has proper nonzero ideals, and not on the field $F$, which has none.

**Proof.** By hypothesis the two topologies on $F$ agree, so the powers $I^n$ form a fundamental system of neighbourhoods of $0$ in the metric topology on $\mathcal{O}$ as well as in the $I$-adic topology; the Cauchy sequences for the metric and for the filtration therefore coincide, and the completion of $\mathcal{O}$ is the inverse limit of the quotients $\mathcal{O}/I^n$. The absolute value of $F$ extends to the fraction field of that completion, which is therefore the completion of $F$; its valuation ring is $\widehat{\mathcal{O}}$ by the persistence of the residue field, part (c) above. $\square$

### The $p$-adic Fields

**Theorem.** The completion $\mathbb{Q}_p$ of $\mathbb{Q}$ at $\lvert \cdot \rvert_p$ is a complete non-Archimedean valued field with

$$
\mathcal{O} = \mathbb{Z}_p, \qquad \mathfrak{m} = p\mathbb{Z}_p, \qquad k = \mathbb{F}_p, \qquad \Gamma = \mathbb{Z},
$$

and the residue field is $\mathbb{F}_p$, the value group is $\mathbb{Z}$. Every $x \in \mathbb{Q}_p^\times$ has a unique Laurent expansion

$$
x = \sum_{n \geq n_0} a_n p^n, \qquad a_n \in \{0, 1, \dots, p-1\},
$$

with $n_0 = v_p(x)$; $\mathbb{Z}_p$ corresponds to $n_0 \geq 0$.

**Proof.** The assertions about the valuation ring, maximal ideal, residue field and value group follow from the corresponding facts for $\mathbb{Z}_{(p)}$ and the persistence of the residue field under completion (part (c) of the completion theorem); the expansion is the $p$-adic analogue of decimal expansion for fractions. $\square$

**Theorem (Hensel's lemma).** Let $F$ be complete with respect to a non-Archimedean absolute value, let $\mathcal{O}$ be its valuation ring, and let $f \in \mathcal{O}[x]$. If there is $a \in \mathcal{O}$ with

$$
\lvert f(a) \rvert < \lvert f'(a) \rvert^2,
$$

then there is a unique $b \in \mathcal{O}$ with $f(b) = 0$ and $\lvert b - a \rvert < \lvert f'(a) \rvert$.

**Proof sketch.** The Newton iteration $a_{n+1} = a_n - f(a_n)/f'(a_n)$ is defined by the hypothesis and is Cauchy for the non-Archimedean absolute value, with $\lvert a_{n+1} - a_n \rvert$ decreasing quadratically; completeness gives a limit $b$, and continuity of $f$ gives $f(b) = 0$. Uniqueness is by the ultrametric estimate on $f(b) - f(b')$. $\square$

**Corollary (roots of units).** Let $p$ be odd and let $u \in \mathbb{Z}_p^\times$. Then $u$ is a square in $\mathbb{Z}_p$ if and only if its image in $\mathbb{F}_p^\times$ is a square.

**Proof.** Apply Hensel's lemma to $f(x) = x^2 - u$ at a lift $a$ of a square root of the image of $u$ in $\mathbb{F}_p$: since the image is a nonzero square, $f'(a) = 2a$ has absolute value $1$, while $\lvert f(a) \rvert \leq 1/p < 1 = \lvert f'(a) \rvert^2$, so the hypothesis of Hensel's lemma holds. $\square$

**Theorem (algebraic closure of $\mathbb{Q}_p$).** The algebraic closure $\overline{\mathbb{Q}_p}$ is not complete; its completion $\mathbb{C}_p$ is algebraically closed and complete, and $\mathbb{C}_p$ is the smallest algebraically closed and complete extension of $\mathbb{Q}_p$.

**Proof sketch.** The valuation of $\mathbb{Q}_p$ extends uniquely to $\overline{\mathbb{Q}_p}$; the value group of the algebraic closure is $\mathbb{Q}$ and its residue field is $\overline{\mathbb{F}_p}$, and by part (c) above both are unchanged when the completion is taken, so $\mathbb{C}_p$ has value group $\mathbb{Q}$ and residue field $\overline{\mathbb{F}_p}$. Krasner's lemma shows that the completion of an algebraic closure of a complete non-Archimedean field is algebraically closed. $\square$

### Completions and the Number Systems

| Base field | Absolute value | Completion |
|---|---|---|
| $\mathbb{Q}$ | $\lvert \cdot \rvert_\infty$ | $\mathbb{R}$ |
| $\mathbb{Q}$ | $\lvert \cdot \rvert_p$ | $\mathbb{Q}_p$ |
| $k(t)$ | $t$-adic | $k((t))$ |
| $\overline{\mathbb{Q}_p}$ | $p$-adic (extended) | $\mathbb{C}_p$ |
| $\overline{\mathbb{Q}}$ | usual (restricted) | $\mathbb{C}$ |
| $\mathbb{C}(t)$ | $t$-adic | $\mathbb{C}((t))$ |

**Remark.** The completion of $\mathbb{Q}$ at the Archimedean place is $\mathbb{R}$, whose construction is the order-theoretic one of *Real-Closed and Complete Ordered Fields* and *The Real Numbers*; the completion at the non-Archimedean places gives the fields $\mathbb{Q}_p$, whose study is the beginning of algebraic number theory. The two constructions agree in making the field complete and, in the non-Archimedean case, in preserving the value group and the residue field, and they differ in that $\mathbb{R}$ is order-complete and real closed while $\mathbb{Q}_p$ is neither orderable nor algebraically closed.

---

## Summary

An absolute value on a field is a multiplicative size function satisfying the triangle inequality; it defines a metric and makes the field a topological field. It is non-Archimedean when the ultrametric inequality $\lvert x+y \rvert \leq \max\{\lvert x \rvert, \lvert y \rvert\}$ holds, equivalently when $\lvert n \cdot 1 \rvert \leq 1$ for all integers $n$. Two nontrivial absolute values are equivalent exactly when they are positive powers of one another, and on $\mathbb{Q}$ Ostrowski's theorem says that the nontrivial absolute values are, up to equivalence, the usual one and the $p$-adic ones; the product formula $\lvert x \rvert_\infty \prod_p \lvert x \rvert_p = 1$ holds for every nonzero rational.

In the non-Archimedean case the geometry is ultrametric: $\lvert x+y \rvert = \max$ when the terms have different sizes, every triangle is isosceles, every point of a ball is a centre, balls are nested or disjoint and are open and closed, the space is totally disconnected, and a series converges exactly when its terms tend to zero. The unit ball is the valuation ring $\mathcal{O}$, a local domain with maximal ideal $\mathfrak{m}$ and residue field $k = \mathcal{O}/\mathfrak{m}$, and the non-Archimedean absolute values correspond to valuations into ordered abelian groups, with $\mathcal{O}$ a maximal proper subring of $F$ and $F = \operatorname{Frac}(\mathcal{O})$.

Every valued field has a completion, unique up to isometry, which is complete and contains the field densely, and which agrees with the $I$-adic completion when the topology is the $I$-adic topology of a subring; it preserves the non-Archimedean character and, in that case, the value group $\Gamma_{\widehat{F}} = \Gamma_F$ and the residue field, while in the Archimedean case the value set can grow. The completions of $\mathbb{Q}$ are $\mathbb{R}$ and the $p$-adic fields $\mathbb{Q}_p$, with valuation ring $\mathbb{Z}_p$, maximal ideal $p\mathbb{Z}_p$, residue field $\mathbb{F}_p$ and value group $\mathbb{Z}$; Hensel's lemma gives a criterion for lifting simple roots modulo $\mathfrak{m}$, and the completion $\mathbb{C}_p$ of the algebraic closure of $\mathbb{Q}_p$ is algebraically closed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Field with an absolute value or valuation |
| $\lvert \cdot \rvert$ | Absolute value |
| $\lvert \cdot \rvert_p$, $\lvert \cdot \rvert_\infty$ | $p$-adic and usual absolute values |
| $v$, $v_p$ | Valuation, $p$-adic valuation |
| $\Gamma$ | Value group (multiplicative for absolute values, additive for valuations) |
| $\Gamma_{\widehat{F}}$ | Value group of the completion, equal to $\Gamma_F$ in the non-Archimedean case |
| $\operatorname{Frac}$ | Field of fractions, $\widehat{F} = \operatorname{Frac}(\widehat{\mathcal{O}})$ |
| $\mathcal{O}$, $\mathcal{O}_v$ | Valuation ring $\{x : \lvert x \rvert \leq 1\}$ |
| $\mathfrak{m}$, $\mathfrak{m}_v$ | Maximal ideal $\{x : \lvert x \rvert < 1\}$ |
| $k$, $k(v)$ | Residue field $\mathcal{O}/\mathfrak{m}$ |
| $c$ | Base of the exponential, $c > 1$, relating $v$ and $\lvert \cdot \rvert$ |
| $\widehat{F}$ | Completion of $F$ |
| $\mathbb{Z}_{(p)}$, $k[t]_{(t)}$ | Localizations, examples of DVRs |
| $\mathbb{Z}_p$, $\mathbb{Q}_p$, $\mathbb{C}_p$ | $p$-adic integers, numbers, and completed algebraic closure |
| $k((t))$ | Formal Laurent series field |
| $d(x,y) = \lvert x-y \rvert$ | Induced metric |
| $f'(x)$ | Formal derivative, in Hensel's lemma |

## Further Reading

- Alexander Ostrowski, "Über einige Lösungen der Funktionalgleichung $\varphi(x)\varphi(y) = \varphi(xy)$", *Acta Mathematica* 41 (1918), for the classification of absolute values on $\mathbb{Q}$.
- Kurt Hensel, *Theorie der algebraischen Zahlen* (Teubner, 1908), for the $p$-adic numbers and the lifting lemma.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for valuations and valuation rings.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for $\mathbb{Q}_p$, $\mathbb{C}_p$, Hensel's lemma and ramification.
- Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions* (Springer, 2nd ed. 1984), for the analytic and arithmetic theory of $\mathbb{Q}_p$.
- James Milne, *Algebraic Number Theory* (v3.08, 2020, available online), for places, the product formula and Ostrowski's theorem.
- Fernando Q. Gouvêa, *p-adic Numbers: An Introduction* (Springer, 2nd ed. 1997), for the construction of $\mathbb{Q}_p$ as a completion and for Hensel's lemma with worked examples.
