# __Valuation Theory and Henselian Rings__

## Introduction

A valuation on a field is a homomorphism from its multiplicative group to an ordered abelian group, extended by the convention that the zero element has value infinity; it measures divisibility, and its subring of elements of nonnegative value is the **valuation ring**. When the value group embeds in the real numbers the valuation is equivalent to a non-Archimedean absolute value, and that case — the metric case, with completions and the $p$-adic fields — is the subject in Part II. The present article takes the general algebraic theory: value groups of arbitrary rank, the valuation rings and their ideals, the extension of a valuation to an algebraic extension, the approximation theorem for independent valuations, and the identification of the integral closure as an intersection of valuation rings.

The second half of the article concerns **Henselian rings**, the local rings in which a factorisation of a polynomial modulo the maximal ideal lifts to a factorisation over the ring. Hensel's lemma, in the form stated for complete non-Archimedean fields, is the model; the general definition does not require completeness, and every local ring has a best Henselian approximation, its **henselization**. Henselian rings are the local rings in which the extension theory of valuations is unambiguous, and the property is what makes the ramification theory of an algebraic number field or of an algebraic curve work.

This article develops general valuations and their rings, the correspondence between prime ideals and convex subgroups, the existence of extensions of a valuation and the fundamental inequality, the approximation theorem, and the theory of Henselian local rings with their henselizations. Throughout, $K$ is a field, $v : K \to \Gamma \cup \{\infty\}$ is a valuation with value group $\Gamma$, ordered additively, and $\mathcal{O}_v$, $\mathfrak{m}_v$, $k(v)$ are its valuation ring, maximal ideal and residue field. Integrality and integral closure are from *Integral Extensions and Krull Dimension*, Dedekind domains and localisation from *Dedekind Domains and Ideal Class Groups* and *Localization and the Fraction Field*, and the rank-one case, with completions and the fields $\mathbb{Q}_p$, is not developed here. Nothing in the article depends on a metric or a completion.

---

## General Valuations

### Definition

**Definition.** Let $K$ be a field and let $\Gamma$ be an abelian group written additively and equipped with a total order compatible with addition:

$$
\gamma \leq \delta \implies \gamma + \varepsilon \leq \delta + \varepsilon .
$$

A **valuation** on $K$ with values in $\Gamma$ is a surjective map

$$
v : K \longrightarrow \Gamma \cup \{\infty\}
$$

such that for all $x, y \in K$:

**(V1)** $v(x) = \infty$ if and only if $x = 0$;

**(V2)** $v(xy) = v(x) + v(y)$;

**(V3)** $v(x + y) \geq \min\{v(x), v(y)\}$,

with the conventions $\gamma + \infty = \infty$ and $\gamma < \infty$ for all $\gamma \in \Gamma$. The group $\Gamma$ is the **value group**, and $v$ is **trivial** if $\Gamma = 0$. The **rank** of $v$ is the order rank of $\Gamma$, the supremum of the lengths of chains of proper convex subgroups.

**Proposition.** Let $v$ be a valuation on $K$.

**(a)** $v(1) = 0$, $v(-x) = v(x)$, $v(x^{-1}) = -v(x)$ for $x \neq 0$.

**(b)** If $v(x) \neq v(y)$ then $v(x + y) = \min\{v(x), v(y)\}$; the values are "all triangles isosceles".

**(c)** The set $\mathcal{O}_v = \{x \in K : v(x) \geq 0\}$ is a subring of $K$, the **valuation ring**, and $\mathfrak{m}_v = \{x : v(x) > 0\}$ is its unique maximal ideal. Its fraction field is $K$.

**(d)** $k(v) = \mathcal{O}_v/\mathfrak{m}_v$ is a field, the **residue field**, and $k(v) = \mathcal{O}_v/\mathfrak{m}_v$ is the image of the elements of value $0$.

**Proof.** (a) From $v(1) = v(1) + v(1)$; from $v(-1) + v(-1) = v(1) = 0$ and the only solutions of $2\gamma = 0$ in an ordered group are $\gamma = 0$; and from $v(x) + v(x^{-1}) = v(1) = 0$. (b) If $v(x) < v(y)$ then $v(x) = v((x+y) - y) \geq \min\{v(x+y), v(y)\}$ forces $v(x+y) \leq v(x)$, while (V3) gives $v(x+y) \geq v(x)$. (c) Closure under addition and multiplication is (V3) and (V2); an element of value $0$ has inverse of value $0$, so it is a unit, and every element of positive value is a non-unit, so $\mathfrak{m}_v$ is exactly the set of non-units, which is then the unique maximal ideal. (d) The kernel of the restriction of the residue map to the value-zero subgroup is $\{0\}$, since $v(x) = 0$ means $x$ is a unit, and the residue field is the quotient by $\mathfrak{m}_v$. $\square$

**Definition.** Two valuations $v, w$ on $K$ are **equivalent** if their valuation rings agree. For rank one this is the usual notion of equivalence of absolute values, and the correspondence between non-Archimedean absolute values and rank-one valuations is the reason the two languages agree in that case.

### Examples

**Example ($p$-adic).** On $\mathbb{Q}$ the $p$-adic valuation $v_p$ has value group $\mathbb{Z}$, so it is discrete of rank one, with $\mathcal{O} = \mathbb{Z}_{(p)}$, $\mathfrak{m} = p\mathbb{Z}_{(p)}$ and residue field $\mathbb{F}_p$.

**Example (order of vanishing).** On the rational function field $k(x)$ and on its subring $k[x]$, the order of vanishing at the irreducible polynomial $p(x)$ gives a discrete rank-one valuation with residue field $k[x]/(p(x))$. The point at infinity gives a further valuation, of the same form after the change of variable $x \mapsto 1/x$.

**Example (a rank-two valuation).** Let $K = k(x,y)$ and define $v$ as follows. For $0 \neq f \in K$, regard $f$ as an element of $k(x)(y)$ and let $m = \operatorname{ord}_y(f) \in \mathbb{Z}$ be its order of vanishing in $y$; write $f = y^m c\,(1 + u)$ with $c \in k(x)^\times$ and $u$ of positive $y$-order. Put

$$
v(f) = (m,\, \operatorname{ord}_x(c)) \in \mathbb{Z} \oplus \mathbb{Z},
$$

where the group $\mathbb{Z} \oplus \mathbb{Z}$ carries the **lexicographic** order, $(m_1, n_1) < (m_2, n_2)$ when $m_1 < m_2$, or $m_1 = m_2$ and $n_1 < n_2$. This is a valuation: additivity is multiplicativity of the order in $y$ and of the leading coefficient in $x$, and (V3) holds because the lexicographic order compares the $y$-orders first. Its value group is $\mathbb{Z} \oplus \mathbb{Z}$, of rank $2$, since the convex subgroups are $0$, $\{0\} \oplus \mathbb{Z}$ and $\mathbb{Z} \oplus \mathbb{Z}$. The valuation ring $\mathcal{O}_v$ contains $k[x,y]$ and its maximal ideal meets $k[x,y]$ in $(x,y)$; so $\mathcal{O}_v$ is a rank-two valuation ring dominating the two-dimensional local ring $k[x,y]_{(x,y)}$.

**Example (a rank-one, non-discrete valuation).** On $k(x)$ fix a real number $\alpha$ transcendental over $k$ and define $v(f) = \operatorname{ord}_{x=\alpha}(f)$ by evaluation in the real closure; more algebraically, order the group $\mathbb{Z} \oplus \mathbb{Z}\alpha \subseteq \mathbb{R}$ lexicographically and use the embedding $k(x) \subseteq k(\alpha)$, with $v$ the composite of the $(x - \alpha)$-adic order and the order of the coefficient. The value group is a dense subgroup of $\mathbb{R}$, so the valuation is rank one and non-discrete, and its valuation ring is not Noetherian; this is the reason a rank-one valuation ring need not be a discrete valuation ring.

### Ideals of a Valuation Ring

**Theorem.** Let $V$ be an integral domain with fraction field $K$. Then $V$ is a valuation ring of $K$ — that is, $V = \mathcal{O}_v$ for some valuation $v$ of $K$ — if and only if for every $0 \neq x \in K$ at least one of $x, x^{-1}$ lies in $V$. When this holds, the ideals of $V$ are totally ordered by inclusion, and $V$ is a local ring whose maximal ideal is the set of non-units.

**Proof.** If $V = \mathcal{O}_v$, then $v(x) \geq 0$ or $v(x) \leq 0$, that is, $x \in V$ or $x^{-1} \in V$. Conversely, suppose $V$ has the property, and define $\Gamma = K^\times/V^\times$ with the order $x V^\times \leq y V^\times \iff x y^{-1} \in V$. The order is total by the hypothesis, and compatible with multiplication; the quotient map $v : K^\times \to \Gamma$ extends by $v(0) = \infty$ and satisfies (V2). For (V3), if $v(x) \geq v(y)$ then $x/y \in V$, and $x + y = y(x/y + 1)$ with $x/y + 1 \in V$, so $v(x+y) \geq v(y) = \min$. Hence $V$ is the valuation ring of $v$. If $I, J$ are ideals and $I \not\subseteq J$, choose $x \in I \setminus J$; for $y \in J$, $y/x \notin V$ (else $y \in I$), so $x/y \in V$, giving $x \in (y) \subseteq J$, a contradiction; hence $J \subseteq I$. The maximal ideal is the union of the proper ideals, which is the set of non-units, and it is the unique maximal ideal. $\square$

**Theorem.** A valuation ring is integrally closed in its fraction field. Conversely, every integrally closed domain is an intersection of valuation rings of its fraction field. A valuation ring is Noetherian if and only if it is a discrete valuation ring; equivalently, if and only if its value group is $\mathbb{Z}$ up to equivalence.

**Proof sketch.** If $x$ is integral over $V$ with $x \notin V$, then $x^{-1} \in V$ and $x^{-1}$ is a non-unit; a monic equation $x^n + a_{n-1}x^{n-1} + \cdots = 0$ multiplied by $x^{-n}$ exhibits $1$ as an element of the maximal ideal, a contradiction. For the converse, the intersection of all valuation rings containing a given integrally closed domain is proved in the next section. The final statement is the theorem of Krull: a Noetherian valuation ring has a principal maximal ideal, hence value group $\mathbb{Z}$. $\square$

**Theorem (primes and convex subgroups).** Let $v$ be a valuation on $K$ with value group $\Gamma$. The prime ideals of $\mathcal{O}_v$ correspond bijectively to the convex subgroups $\Delta \subseteq \Gamma$, by

$$
\mathfrak{p}_\Delta = \{x \in K : v(x) > \Delta\},
$$

with the convention that $\mathfrak{p}_0 = \mathfrak{m}_v$ and $\mathfrak{p}_\Gamma = (0)$. The correspondence reverses inclusions, and

$$
\dim \mathcal{O}_v = \operatorname{rank} \Gamma .
$$

**Proof sketch.** A subset $\Delta \subseteq \Gamma$ is convex if $\gamma \leq \delta \leq \varepsilon$ with $\gamma, \varepsilon \in \Delta$ forces $\delta \in \Delta$. The set $\mathfrak{p}_\Delta$ defined above is an ideal, and it is prime exactly when $\Delta$ is convex; conversely every prime arises this way from its set of values. The chain of primes is then in bijection with the chain of convex subgroups. $\square$

**Corollary.** A valuation ring has dimension $1$ exactly when its value group is rank one. A valuation ring has dimension $0$ exactly when it is a field, that is, when the valuation is trivial.

---

## Extensions and the Approximation Theorem

### Existence of Extensions

**Theorem (Chevalley).** Let $R$ be a subring of a field $K$ and let $\mathfrak{p}$ be a prime ideal of $R$. Then there is a valuation ring $V$ of $K$ with $R \subseteq V$ and $\mathfrak{m}_V \cap R = \mathfrak{p}$.

**Proof sketch.** Consider the set of pairs $(A, \mathfrak{q})$ where $A$ is a subring of $K$ containing $R$ and $\mathfrak{q}$ is a prime of $A$ with $\mathfrak{q} \cap R = \mathfrak{p}$. The set is nonempty, contains $(\mathfrak{p}$-localisation of $R, \mathfrak{p})$, and is partially ordered by extension; every chain has an upper bound given by the union, which is a subring and whose union of primes is prime. By Zorn's lemma there is a maximal such pair $(V, \mathfrak{m})$. Maximality forces $\mathfrak{m}$ to be the set of non-units of $V$: any element outside $\mathfrak{m}$ can be inverted without disturbing the prime. Hence $V$ is a local ring whose non-units form an ideal, and the criterion of the preceding section — its proof shows that a local ring with this property is a valuation ring — gives that $V$ is a valuation ring of $K$ with the required prime. $\square$

**Theorem (integral closure as an intersection).** Let $R$ be an integral domain with fraction field $K$. The integral closure of $R$ in $K$ is the intersection of all valuation rings $V$ of $K$ with $R \subseteq V$:

$$
\overline{R} = \bigcap_{V \supseteq R} V .
$$

**Proof.** An element of $\overline{R}$ lies in every valuation ring containing $R$, since valuation rings are integrally closed; this gives one inclusion. Conversely, suppose $x \in K$ is not integral over $R$. Then the ideal $x^{-1} R[x^{-1}]$ of the ring $R[x^{-1}]$ is proper: if it were the whole ring, then $1 = x^{-1} a$ for some $a \in R[x^{-1}]$, whence $x = a$ is a polynomial $\sum r_i x^{-i}$ in $x^{-1}$, and multiplying by a power $x^n$ gives a monic equation for $x$ over $R$. So $x^{-1}R[x^{-1}]$ lies in a maximal ideal $\mathfrak{m}$ of $R[x^{-1}]$, and by Chevalley there is a valuation ring $V$ of $K$ with $R[x^{-1}] \subseteq V$ and $\mathfrak{m}_V \cap R[x^{-1}] = \mathfrak{m}$. Then $x^{-1} \in \mathfrak{m}_V$, so $v(x^{-1}) > 0$ and $v(x) < 0$, hence $x \notin V$. Thus a non-integral element is missed by some valuation ring containing $R$, and the intersection is exactly $\overline{R}$. $\square$

**Corollary.** An integral domain $R$ with fraction field $K$ is integrally closed if and only if it is the intersection of the valuation rings of $K$ that contain it. In particular every Dedekind domain is an intersection of discrete valuation rings, and

$$
R = \bigcap_{\mathfrak{m}} R_\mathfrak{m}, \qquad \mathfrak{m} \text{ ranging over the maximal ideals.}
$$

This recovers the local characterisation of Dedekind domains of *Dedekind Domains and Ideal Class Groups*: the localisations there are exactly the valuation rings occurring in the intersection.

### Extension of a Valuation

**Theorem.** Let $v$ be a valuation of $K$ and let $L/K$ be an algebraic extension. Then $v$ extends to a valuation of $L$; that is, there is a valuation $w$ of $L$ with $w\vert_K = v$.

**Proof sketch.** One first extends to a simple extension $K(\alpha)$ by taking a maximal element, under Zorn's lemma, among the pairs consisting of a subring $A \supseteq \mathcal{O}_v$ of $K(\alpha)$ and a prime $\mathfrak{q}$ of $A$ contracting to $\mathfrak{m}_v$; Chevalley's maximality argument produces a valuation ring $W$ with $W \cap K = \mathcal{O}_v$, and a valuation ring with that intersection restriction gives a valuation extending $v$. The general case follows by another Zorn argument on the set of partial extensions, ordered by extension of the domain. $\square$

**Definition.** Let $L/K$ be finite and let $w$ be an extension of $v$ to $L$. The **ramification index** and **residue degree** are

$$
e(w/v) = [\Gamma_w : \Gamma_v], \qquad f(w/v) = [k(w) : k(v)] .
$$

**Theorem (fundamental inequality).** Let $L/K$ be a finite extension of degree $n$ and let $w_1, \ldots, w_g$ be the distinct extensions of $v$ to $L$. Then

$$
\sum_{i=1}^{g} e(w_i/v)\, f(w_i/v) \leq n .
$$

If $v$ is Henselian, in the sense defined below, then there is exactly one extension and equality holds, $e f = n$. If moreover $L/K$ is separable, equality holds for arbitrary $v$; this is the separable case of the fundamental equality, proved by passing to the completion and quoted here as a standard theorem of valuation theory from the literature.

**Proof sketch.** Reduce to the case of a normal extension by passing to a normal closure; the extensions of $v$ are permuted transitively by the Galois group, so all the products $e f$ are equal, and it suffices to bound $[L:K]$ below by $g \cdot e f$. Choose for each $i$ a uniformiser and a residue field basis; the standard norm argument, using a residue field basis and the fact that the $\Gamma_w$-components are comparable only through $\Gamma_v$, shows that the resulting set of $e f$ elements is linearly independent over $K$, giving the inequality. $\square$

### Independence and Approximation

**Definition.** Nontrivial valuations $v_1, \ldots, v_n$ of $K$ are **independent** if for every choice of $\gamma_i \in \Gamma_{v_i}$ there is $x \in K^\times$ with $v_i(x) = \gamma_i$ for all $i$. For rank-one valuations this is equivalent to their being pairwise inequivalent.

**Theorem (approximation theorem).** Let $v_1, \ldots, v_n$ be independent nontrivial valuations of $K$, let $a_1, \ldots, a_n \in K$ and let $\gamma_i \in \Gamma_{v_i}$. Then there is $x \in K$ with

$$
v_i(x - a_i) > \gamma_i \qquad \text{for } i = 1, \ldots, n.
$$

**Proof sketch.** It suffices to treat the case $a_1 = 1$ and $a_2 = \cdots = a_n = 0$, since the general case is obtained by adding the $a_i$ afterwards and enlarging the $\gamma_i$. Independence supplies, for each $i$, an element $u_i$ with $v_i(u_i)$ large and $v_j(u_i)$ small for $j \neq i$, and the required element is $x = u_1 (u_1 + \cdots + u_n)^{-1}$, whose value at each $v_i$ is close to $1$ at $i = 1$ and close to $0$ at $i \neq 1$, in the precise sense of the inequalities. $\square$

**Corollary (weak approximation).** If $v_1, \ldots, v_n$ are independent nontrivial valuations with valuation rings $\mathcal{O}_i$ and maximal ideals $\mathfrak{m}_i$, then for prescribed $a_i \in K$ and exponents $N_i$ there is $x \in K$ with $x \equiv a_i \bmod \mathfrak{m}_i^{N_i}$ for all $i$. When the $v_i$ are the $p$-adic valuations of $\mathbb{Q}$ this is the Chinese remainder theorem for the ideals $p_i^{N_i}\mathbb{Z}$.

**Corollary.** Let $R$ be a Dedekind domain with fraction field $K$. The set of nontrivial valuations $v$ of $K$ with $\mathcal{O}_v \supseteq R$ is in bijection with the set of maximal ideals of $R$, by $v \leftrightarrow \mathfrak{m}$, where $v$ is the discrete valuation of the localisation $R_\mathfrak{m}$. These valuations are pairwise independent, and the approximation theorem for them is the ideal-theoretic approximation statement of *Dedekind Domains and Ideal Class Groups*.

---

## Henselian Rings

### The Henselian Property

**Definition.** A local ring $(R, \mathfrak{m}, k)$ is **Henselian** if for every monic polynomial $f \in R[x]$ whose image $\bar f \in k[x]$ factors as $\bar f = \bar g \, \bar h$ with $\bar g, \bar h$ monic and coprime, there exist monic $g, h \in R[x]$ with $f = gh$ and $\bar g, \bar h$ the respective images. This is the **Henselian property**.

The definition is the general form of the lifting statement for complete non-Archimedean fields; there the hypothesis of completeness supplies a metric iteration, whereas here the property is required of the ring directly.

**Theorem (equivalent conditions).** For a local ring $(R, \mathfrak{m}, k)$ the following are equivalent.

**(a)** $R$ is Henselian.

**(b)** For every $f \in R[x]$ and every $a \in R$ with $\bar f(\bar a) = 0$ and $\bar f'(\bar a) \neq 0$ in $k$, there is $b \in R$ with $f(b) = 0$ and $\bar b = \bar a$; a simple root modulo $\mathfrak{m}$ lifts to a root in $R$.

**(c)** Every finite $R$-algebra that is a product of copies of the residue field after reduction modulo $\mathfrak{m}$ is itself a product of copies of $R$.

**(d)** Every idempotent of $R/\mathfrak{m}$ [respectively of a finite $R$-algebra modulo $\mathfrak{m}$] lifts to $R$.

**Proof sketch.** (a) $\Rightarrow$ (b): the polynomial $f$ modulo $\mathfrak{m}$ is divisible by $x - \bar a$ with complementary factor coprime to $x - \bar a$, since $\bar f'(\bar a) \neq 0$; lifting the factorisation gives a linear factor $x - b$. (b) $\Rightarrow$ (a): given $\bar f = \bar g \bar h$ coprime, the resultant-type construction produces a root modulo $\mathfrak{m}$ of a polynomial whose derivative is a unit, and (b) lifts it; induction on the degree gives the full factorisation. The equivalence of (c) and (d) with (a) is the same lifting read through idempotents: an idempotent of the reduction corresponds to a splitting of a finite ring extension into two factors. $\square$

**Theorem (valuations and Hensel).** Let $v$ be a valuation of a field $K$. Then $v$ is Henselian — meaning that its valuation ring is a Henselian local ring — if and only if $v$ extends uniquely to every algebraic extension of $K$.

**Proof sketch.** If $v$ extends uniquely to an algebraic extension $L$, then the valuation ring of $L$ is the unique one over $\mathcal{O}_v$, which forces the factorisation of a polynomial to be rigid; conversely if $v$ is Henselian and $w_1, w_2$ are two extensions, the fundamental inequality applied to a finite normal subextension shows $g = 1$, and a Henselian valuation ring is integrally closed so that the uniqueness propagates. This equivalence is the valuation-theoretic content of the definition. $\square$

### Examples and the Henselization

**Example (complete fields).** A field complete with respect to a non-Archimedean absolute value is Henselian: this is exactly Hensel's lemma, quoted from the literature, and it is the reason the fields $\mathbb{Q}_p$ are the standard Henselian fields. Completeness is sufficient but not necessary.

**Example (separably closed fields).** A separably closed field is Henselian with respect to any valuation, since the unique extension property holds trivially. Thus the class of Henselian fields is much larger than the class of complete ones.

**Example (algebraically closed residue field).** If $k(v)$ is algebraically closed and $\Gamma_v$ is divisible, the valuation is Henselian; the standard examples are the fields $\mathbb{C}_p$.

**Example (the $p$-adics and their algebraic extensions).** The valuation of $\mathbb{Q}_p$ is Henselian and extends uniquely to $\mathbb{Q}_{p^n}$ and to the maximal unramified extension; the ramification theory of these extensions is the arithmetic content of Hensel's lemma, with $e$ and $f$ of the fundamental inequality satisfying $ef = n$.

**Theorem (henselization).** Every local ring $(R, \mathfrak{m})$ has a **henselization** $R^h$: a Henselian local ring with a local homomorphism $R \to R^h$ that is initial among local homomorphisms from $R$ to Henselian local rings. It satisfies

**(a)** the induced map on residue fields $R/\mathfrak{m} \to R^h/\mathfrak{m}R^h$ is an isomorphism, and $\mathfrak{m}R^h$ is the maximal ideal of $R^h$;

**(b)** $R^h$ is the filtered colimit of the local rings $S_{\mathfrak{n}}$, over the finite $R$-algebras $S$ such that every idempotent of $S/\mathfrak{m}S$ lifts to $S$, with $\mathfrak{n}$ a maximal ideal lying over $\mathfrak{m}$;

**(c)** if $R$ is a field, $R^h$ is the subfield of an algebraic closure fixed by the inertia group of a chosen extension of the valuation, so that the henselization of $K$ consists of the elements whose minimal polynomial has a simple root reduction.

**Proof sketch.** The filtered colimit in (b) exists, is local with residue field $k$, and is Henselian because every coprime factorisation modulo $\mathfrak{m}$ lifts through one of the finite algebras $S$ by construction; the universal property follows from the lifting property of those algebras, which is exactly what a map to a Henselian local ring can absorb. Part (c) is the description for a valued field: the inertia group fixes precisely the elements whose minimal polynomial reduces to a polynomial with a simple root, and the fixed field is Henselian by the unique extension property. The henselization sits inside the completion, $R^h \subseteq \widehat{R}$ for a valuation ring $R$, with equality exactly when $R$ is already Henselian; the completion is the metric object, and it is used here only for this comparison. $\square$

**Corollary.** Every local ring has a Henselian closure that is the smallest Henselian local ring through which every map to a Henselian local ring factors; for a discrete valuation ring the henselization is the ring of elements of the completion whose minimal polynomial over the fraction field has a simple root reduction modulo the maximal ideal. In particular, a discrete valuation ring with separably closed residue field is Henselian.

**Remark.** Completeness is a metric condition and belongs to the metric theory of valued fields; Henselianity is an algebraic condition satisfied by many fields that are not complete. The passage from a local ring to its henselization replaces the analytic operation of passage to the completion by an algebraic one, and this substitution is what makes the ramification theory of valuations purely algebraic.

---

## Summary

A valuation on a field with values in an ordered abelian group $\Gamma$ defines a valuation ring $\mathcal{O}_v$, a local ring whose maximal ideal is the set of positive-value elements and whose residue field is $k(v)$. Valuation rings are exactly the domains in which each element of the fraction field or its inverse lies in the ring, equivalently the domains whose ideals are totally ordered; they are integrally closed. The prime ideals of a valuation ring correspond to the convex subgroups of the value group, so the ring has dimension one exactly when the value group has rank one, and it is Noetherian exactly when it is a discrete valuation ring.

Chevalley's theorem produces a valuation ring containing a given subring and contracting a given prime to its maximal ideal, and Krull's theorem, proved with it, identifies the integral closure as the intersection of all valuation rings containing the base. Every valuation of $K$ extends to every algebraic extension, and the extensions obey the fundamental inequality $\sum e_i f_i \leq [L:K]$, with equality when the valuation is Henselian; independent valuations satisfy the approximation theorem, which specialises to the Chinese remainder theorem for the primes of a Dedekind domain.

A local ring is Henselian when a coprime factorisation modulo the maximal ideal lifts to a factorisation over the ring, equivalently when every simple root modulo the maximal ideal lifts. Complete non-Archimedean fields are Henselian, as is any separably closed field, and a valuation is Henselian exactly when it extends uniquely to every algebraic extension. Every local ring has a henselization, the initial Henselian local ring mapping to it, obtained as a filtered colimit of étale algebras and contained in the completion; for a valued field the henselization consists of the elements whose minimal polynomial has a simple root reduction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Field |
| $v : K \to \Gamma \cup \{\infty\}$ | Valuation |
| $\Gamma$, $\Gamma_v$ | Value group, additively written ordered abelian group |
| $\operatorname{rank} v$ | Order rank of $\Gamma_v$ |
| $\mathcal{O}$, $\mathcal{O}_v$ | Valuation ring $\{x : v(x) \geq 0\}$ |
| $\mathfrak{m}$, $\mathfrak{m}_v$ | Maximal ideal $\{x : v(x) > 0\}$ |
| $k(v)$ | Residue field $\mathcal{O}_v/\mathfrak{m}_v$ |
| $\mathfrak{p}_\Delta$ | Prime ideal of $\mathcal{O}_v$ attached to a convex subgroup $\Delta$ |
| $(m, n)$ in $\mathbb{Z} \oplus \mathbb{Z}$ | Lexicographic coordinates of a rank-two valuation |
| $e(w/v)$, $f(w/v)$ | Ramification index, residue degree |
| $v_1, \ldots, v_n$ independent | Approximation with prescribed values possible |
| $(R, \mathfrak{m}, k)$ | Local ring with maximal ideal and residue field |
| $R^h$ | Henselization of $R$ |
| Henselian property | Coprime factorisation modulo $\mathfrak{m}$ lifts |
| $\widehat{R}$ | Completion of a valued field |
| $\mathbb{Q}_p$, $\mathbb{Z}_p$, $\mathbb{C}_p$ | Non-Archimedean fields, cited from the companion article |
| $\overline{R}$ | Integral closure of $R$ in its fraction field |



## Further Reading

- Wolfgang Krull, "Allgemeine Bewertungstheorie", *Journal für die reine und angewandte Mathematik* 167 (1932), 160–196, for general valuations with arbitrary value groups, valuation rings and the correspondence with primes.
- Claude Chevalley, "La notion d'anneau de valuation", *Comptes Rendus de l'Académie des Sciences* 186 (1928), 1333–1335, for the existence theorem producing a valuation ring with prescribed contraction.
- Otto Endler, *Valuation Theory* (Springer, 1972), for the extension theorem, the independence of valuations and the approximation theorem.
- Paulo Ribenboim, *Théorie des valuations* (Presses de l'Université de Montréal, 1964), for the fundamental inequality and the ramification theory of extensions of a valuation.
- Michel Raynaud, *Anneaux locaux henséliens* (Springer Lecture Notes in Mathematics 169, 1970), for Henselian rings, the lifting theorem and the henselization.
- Masayoshi Nagata, *Local Rings* (Interscience, 1962), for Henselian local rings and their place in dimension theory.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for valuations, valuation rings and the Henselian property in the standard systematic form.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra, Volume II* (Van Nostrand, 1960), for valuation theory, the extension theorem and the approximation theorem with applications to algebraic surfaces.
