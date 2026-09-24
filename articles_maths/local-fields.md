
# __Local Fields__

## Introduction

A local field is a field carrying a nontrivial absolute value with respect to which it is complete and locally compact. The two Archimedean examples are $\mathbb{R}$ and $\mathbb{C}$; the non-Archimedean ones are the finite extensions of the $p$-adic fields $\mathbb{Q}_p$ and the finite extensions of the formal Laurent series fields $\mathbb{F}_p((t))$. The definition is topological: it asks that the distance on the field produce enough compactness for the field to behave like a field with a finite residue field and a discrete valuation. That combination of hypotheses is what makes the additive and multiplicative groups tractable — the additive group is locally compact, and the multiplicative group is abelian, locally compact, and built from a discrete copy of $\mathbb{Z}$ and a compact unit group — and it is why the local fields are the local objects of algebraic number theory.

This article develops the definition, the classification theorem, the topology of a non-Archimedean local field, its residue field and ramification invariants, and the structure of its multiplicative group. It assumes *Absolute Values, Valuations and Completions*, from which the absolute values, valuation rings, residue fields and completions are taken, and *Topological Rings and Fields*, from which the $I$-adic topologies and completions are taken. The arithmetic of local fields — class field theory, the local reciprocity law, and the use of local data to describe global fields — belongs to Part I and is cited rather than developed. The analysis over a local field — power series, integration, differential equations, and analytic functions in the non-Archimedean sense — belongs to Part III, where the limit and the measure are available. The application articledevelops the standard example concretely, and the geometry of a valued field — rigid analytic, Berkovich, adic and perfectoid spaces — occupies the other articles of this Part.

Throughout, $F$ is a local field, $\lvert \cdot \rvert$ its absolute value, $\mathcal{O}$ its valuation ring, $\mathfrak{m}$ its maximal ideal, $k = \mathcal{O}/\mathfrak{m}$ its residue field and $\Gamma = \lvert F^\times \rvert$ its value group, in the notation of *Absolute Values, Valuations and Completions*. A uniformiser is written $\pi$, and $q = \lvert k \rvert$ denotes the cardinality of the residue field.

---

## The Definition and the Classification

### Definition

**Definition.** A **local field** is a field $F$ together with a nontrivial absolute value $\lvert \cdot \rvert$ such that

**(LF1)** $F$ is complete for the metric $d(x,y) = \lvert x - y \rvert$, and

**(LF2)** the metric topology on $F$ is locally compact: every point has a compact neighbourhood.

The definition depends only on the equivalence class of the absolute value, because equivalent absolute values induce the same topology, so completeness and local compactness are properties of the topological field rather than of the particular size function. The trivial absolute value is excluded because it gives the discrete topology; a discrete field is occasionally admitted as a degenerate local field, and the convention of this article is to exclude it.

The usual absolute value on $\mathbb{R}$ is complete and $\mathbb{R}$ is locally compact, and the same holds for $\mathbb{C}$; thus $\mathbb{R}$ and $\mathbb{C}$ are local fields. The $p$-adic absolute value on $\mathbb{Q}_p$ is complete and $\mathbb{Q}_p$ is locally compact, since its unit ball $\mathbb{Z}_p$ is compact by *Topological Rings and Fields* and *Absolute Values, Valuations and Completions*; thus $\mathbb{Q}_p$ is a local field. For a prime $p$, the $t$-adic absolute value on the Laurent series field $\mathbb{F}_p((t))$ is complete and $\mathbb{F}_p[[t]]$ is compact, so $\mathbb{F}_p((t))$ is a local field. These are the **prime examples**, and the classification theorem says that there are no others.

**Remark (two senses of local).** The adjective *local* in *local field* refers to the locality of a place of a global field. It does not refer to the property of a ring being local, although the valuation ring $\mathcal{O}$ of a non-Archimedean local field is indeed a local ring with maximal ideal $\mathfrak{m}$. Both senses occur below, and the context distinguishes them.

### The Classification Theorem

**Theorem (classification of local fields).** Let $F$ be a local field. Then exactly one of the following holds.

**(a)** $F$ is isomorphic, as a topological field, to $\mathbb{R}$ or to $\mathbb{C}$, with the usual absolute value; these are the **Archimedean local fields**.

**(b)** $F$ is a finite extension of $\mathbb{Q}_p$ for a unique prime $p$, carrying the unique absolute value extending the $p$-adic one.

**(c)** $F$ is a finite extension of $\mathbb{F}_p((t))$ for a unique prime $p$, carrying the unique absolute value extending the $t$-adic one.

**Proof sketch.** Suppose first that $\lvert \cdot \rvert$ is Archimedean. Then $F$ is a complete Archimedean field, and the classical theorem of Ostrowski for fields — of which the theorem of *Absolute Values, Valuations and Completions* for $\mathbb{Q}$ is the special case — identifies a complete Archimedean field with $\mathbb{R}$ or $\mathbb{C}$ up to topological isomorphism, according to whether the prime subfield is fixed or not. Suppose next that $\lvert \cdot \rvert$ is non-Archimedean. Let $\mathcal{O}$ be the unit ball and $\mathfrak{m}$ its maximal ideal. The residue field $k = \mathcal{O}/\mathfrak{m}$ is a quotient of the compact set $\mathcal{O}$ and is discrete, hence finite; the value group $\Gamma = \lvert F^\times \rvert$ is a discrete subgroup of $\mathbb{R}_{>0}$, hence cyclic, and one writes $\mathfrak{m} = (\pi)$ for a uniformiser. If $\operatorname{char} F = p$ then the prime field $\mathbb{F}_p$ is contained in $\mathcal{O}$; the field $\mathbb{F}_p((t))$ sits inside $F$ as the subfield generated by $\mathbb{F}_p$ and a uniformiser, and the extension degree $[F : \mathbb{F}_p((t))]$ is finite because the residue field extension and the value group extension are both finite. If $\operatorname{char} F = 0$ then the prime field is $\mathbb{Q}$, and since the absolute value is non-Archimedean it defines the $p$-adic topology on $\mathbb{Q}$ for some prime $p$ by Ostrowski's theorem; then $\mathbb{Q}_p \subseteq F$, and the degree $[F : \mathbb{Q}_p]$ is finite by the same comparison of residue field and value group. $\square$

**Remark.** The theorem is originally due to Pontryagin, Jacobson and Weil, in the form that every non-discrete locally compact topological field is one of the listed fields. It is quoted here as a standard classification. Its content is the statement that the algebraic and the topological hypotheses are equivalent: a field can be locally compact for a nontrivial absolute value exactly when it is one of these configurations.

### The Non-Archimedean Prime Examples

**Example ($\mathbb{Q}_p$ and $\mathbb{Z}_p$).** Here $\mathcal{O} = \mathbb{Z}_p$, $\mathfrak{m} = p\mathbb{Z}_p$, $k = \mathbb{F}_p$, $\Gamma = \mathbb{Z}$ and $q = p$. The absolute value is normalised as $\lvert p \rvert = 1/p$. The field $\mathbb{Q}_p$ is the fraction field of the compact ring $\mathbb{Z}_p$.

**Example ($\mathbb{F}_p((t))$ and $\mathbb{F}_p[[t]]$).** Here $\mathcal{O} = \mathbb{F}_p[[t]]$, $\mathfrak{m} = t\mathbb{F}_p[[t]]$, $k = \mathbb{F}_p$, $\Gamma = \mathbb{Z}$ and $q = p$. The absolute value is normalised as $\lvert t \rvert = 1/p$. The ring $\mathcal{O}$ is compact because it is the inverse limit $\varprojlim_n \mathbb{F}_p[t]/(t^n)$ of finite rings.

**Example (an unramified extension).** Let $F = \mathbb{Q}_p(\sqrt{2})$ for an odd prime $p$ with $2$ a nonsquare modulo $p$. Then $F$ is a local field with residue field $\mathbb{F}_{p^2}$, residue degree $f = 2$ and value group $\mathbb{Z}$; it is an unramified quadratic extension, since $X^2 - 2$ is irreducible over $\mathbb{Q}_p$ and remains irreducible modulo $p$. Its valuation ring is $\mathbb{Z}_p[\sqrt{2}]$, and the uniformiser may be taken to be $p$.

**Example (a ramified extension).** Let $F = \mathbb{Q}_p(\sqrt{p})$ for an odd prime $p$. The valuation ring is $\mathbb{Z}_p[\sqrt{p}]$, the residue field is $\mathbb{F}_p$, and the uniformiser is $\sqrt{p}$. Hence the extension has ramification index $e = 2$ and residue degree $f = 1$: the residue field does not grow and the value group stays $\mathbb{Z}$, while the uniformiser changes.

**Example (a field that is not local).** The completion $\mathbb{C}_p$ of the algebraic closure of $\mathbb{Q}_p$ is complete and algebraically closed, but it is not locally compact: its value group is $\mathbb{Q}$, which is dense in $\mathbb{R}$, and its residue field is the infinite field $\overline{\mathbb{F}_p}$. A compact neighbourhood would force the residue field to be finite, as in the proof of the classification theorem, so no such neighbourhood exists. This is the standard example separating *complete* from *locally compact*.

---

## The Non-Archimedean Topology

### The Valuation Ring and its Ideals

Throughout this section $F$ is non-Archimedean, with the notation of *Absolute Values, Valuations and Completions*: the valuation ring is

$$
\mathcal{O} = \{x \in F : \lvert x \rvert \leq 1\},
$$

a local domain with maximal ideal $\mathfrak{m} = \{x : \lvert x \rvert < 1\}$ and residue field $k = \mathcal{O}/\mathfrak{m}$, and $F = \operatorname{Frac}(\mathcal{O})$.

**Proposition.** Let $F$ be a non-Archimedean local field.

**(a)** $\Gamma = \lvert F^\times \rvert$ is a discrete subgroup of $\mathbb{R}_{>0}$, hence is generated by a single element; the element $\pi$ with $\lvert \pi \rvert$ generating $\Gamma$ is a uniformiser and $\mathfrak{m} = (\pi)$.

**(b)** The nonzero ideals of $\mathcal{O}$ are exactly the powers $\mathfrak{m}^n = (\pi^n)$, $n \geq 0$, and they form a strictly decreasing chain

$$
\mathcal{O} = \mathfrak{m}^0 \supsetneq \mathfrak{m} \supsetneq \mathfrak{m}^2 \supsetneq \cdots, \qquad \bigcap_{n \geq 0} \mathfrak{m}^n = 0 .
$$

**(c)** $\mathcal{O}$ is a discrete valuation ring and a principal ideal domain, and every element $x \in F^\times$ factors uniquely as $x = \pi^{v(x)} u$ with $v(x) \in \mathbb{Z}$ and $u \in \mathcal{O}^\times$.

**(d)** The topology on $\mathcal{O}$ is the $\mathfrak{m}$-adic topology of *Topological Rings and Fields*, and on $F$ it is the topology of the descending chain of the $\mathfrak{m}^n$.

**Proof.** (a) Local compactness makes $\Gamma$ discrete: the residue field is finite as above, and if the value group had an accumulation point in $\mathbb{R}_{>0}$ then the balls of the topology would accumulate, contradicting the existence of a compact neighbourhood; a discrete subgroup of $\mathbb{R}_{>0}$ is cyclic. (b) Every nonzero ideal $I$ of $\mathcal{O}$ is determined by $\inf\{v(x) : x \in I\}$, which is attained because $\Gamma$ is cyclic and discrete; the ideal is then $\mathfrak{m}^n$ with $n$ that minimum. The intersection is $0$ because an element of all the $\mathfrak{m}^n$ has $v(x) = \infty$. (c) This is the definition of a discrete valuation ring applied to the maximal ideal $(\pi)$, together with $F = \operatorname{Frac}(\mathcal{O})$; the factorisation is the statement that $x\pi^{-v(x)}$ has absolute value $1$, hence is a unit, and uniqueness follows from $\mathfrak{m}^n \neq \mathfrak{m}^{n+1}$. (d) The sets $a + \mathfrak{m}^n$ are the balls of radius $\lvert \pi \rvert^n$, and they are exactly the cosets of the $\mathfrak{m}$-adic filtration. $\square$

**Remark.** Part (a) shows where local compactness is used: in a general complete non-Archimedean field the value group may be dense and the residue field infinite, as $\mathbb{C}_p$ shows, and then the field is not locally compact and the argument above fails.

### Balls, Compactness and Total Disconnectedness

**Theorem.** Let $F$ be a non-Archimedean local field with the notation above, and let $q = \lvert k \rvert$.

**(a)** $\mathcal{O}$ is compact and open, and $\mathfrak{m}^n$ is compact and open for every $n \geq 0$.

**(b)** $\mathcal{O}$ is the disjoint union of the $q$ residue classes $a + \mathfrak{m}$, each of which is open and closed and of diameter $\lvert \pi \rvert$; more generally, $\mathfrak{m}^n$ is the disjoint union of $q$ cosets of $\mathfrak{m}^{n+1}$.

**(c)** $F$ is $\sigma$-compact and is the union of the increasing chain of compact open sets

$$
\mathcal{O} \subseteq \pi^{-1}\mathcal{O} \subseteq \pi^{-2}\mathcal{O} \subseteq \cdots, \qquad F = \bigcup_{n \geq 0} \pi^{-n}\mathcal{O} ,
$$

and no term of the chain is all of $F$; hence $F$ is not compact.

**(d)** $F$ is totally disconnected, Hausdorff, metrisable and complete, and its topology has a countable base.

**Proof.** (a) The quotient map $\mathcal{O} \to k$ is continuous with finite discrete target, so its fibres are open; the fibre over $0$ is $\mathfrak{m}$. Total boundedness of $\mathcal{O}$ follows by iterating: $\mathcal{O}$ is covered by finitely many cosets of $\mathfrak{m}$, each of those by finitely many cosets of $\mathfrak{m}^2$, and so on, so for every $n$ the ring $\mathcal{O}$ is covered by finitely many sets of diameter at most $\lvert \pi \rvert^n$, which is total boundedness; completeness is the hypothesis, so $\mathcal{O}$ is compact. Each $\mathfrak{m}^n$ is a closed subgroup of $\mathcal{O}$, hence compact, and it is open as a neighbourhood of $0$. (b) The cosets of $\mathfrak{m}$ are the fibres of reduction; they partition $\mathcal{O}$, and each has diameter $\lvert \pi \rvert$ because the difference of two elements of one coset lies in $\mathfrak{m}$. The same argument at level $n$ gives the second statement, and $\mathfrak{m}^n/\mathfrak{m}^{n+1} \cong k$ additively has $q$ elements. (c) The sets $\pi^{-n}\mathcal{O} = \{x : \lvert x \rvert \leq \lvert \pi \rvert^{-n}\}$ are dilates of a compact set by the homeomorphism $x \mapsto \pi^{-n}x$, hence compact; they increase with $n$ and their union is $F$, because $\lvert x \rvert \leq \lvert \pi \rvert^{-n}$ for all large $n$. If $F$ were compact it would be the union of finitely many of them, hence equal to one of them, contradicting the existence of $\pi^{-n-1}$, whose absolute value exceeds $\lvert \pi \rvert^{-n}$. (d) Total disconnectedness is from *Absolute Values, Valuations and Completions*; metrisability and completeness are part of the definition; the countable base is the family of cosets $a + \mathfrak{m}^n$ with $n \geq 0$. $\square$

**Corollary (local compactness is inherited).** Every finite extension of a non-Archimedean local field is again a local field for the unique absolute value extending that of the base field, with residue field and value group extending those of the base field and with $[F : K] = e f$, where $e = [\Gamma_F : \Gamma_K]$ is the **ramification index** and $f = [k_F : k_K]$ the **residue degree**.

**Proof.** The absolute value of $K$ extends uniquely to the finite extension $F$ by *Absolute Values, Valuations and Completions*; the completion of $F$ for that absolute value is a finite-dimensional $K$-vector space in which $F$ is closed, hence equals $F$, so $F$ is complete. Local compactness follows from finite-dimensionality over the locally compact field $K$: the valuation ring of $F$ is contained in a finitely generated $\mathcal{O}_K$-module, and a closed bounded subset of a finite-dimensional $K$-vector space over a locally compact field is compact. The degree formula is the standard multiplicative formula for a finite separable extension of valued fields. $\square$

**Example (unramified extensions).** For each $n \geq 1$ the non-Archimedean local field $F$ has a unique unramified extension of degree $n$, obtained by adjoining to $F$ a primitive $(q^n - 1)$-th root of unity $\zeta$. Its residue field is $\mathbb{F}_{q^n}$, its ramification index is $e = 1$, its residue degree is $f = n$, and its uniformiser may be taken to be a uniformiser of $F$. The extension is Galois with cyclic group generated by the lift of the Frobenius sending $\zeta \mapsto \zeta^q$.

**Example (totally ramified extensions).** The other extreme is $e = n$, $f = 1$. Such an extension is generated by a root of an Eisenstein polynomial, and its uniformiser is a root of that polynomial; the residue field does not change and the value group does not change. A general finite extension is composed of an unramified part and a totally ramified part, the two being independent in the sense that the degree is the product of the two degrees.

---

## The Multiplicative Group

### The Decomposition $F^\times = \langle \pi \rangle \times \mathcal{O}^\times$

**Theorem.** Let $F$ be a non-Archimedean local field. Then the map

$$
\mathbb{Z} \times \mathcal{O}^\times \longrightarrow F^\times, \qquad (n, u) \longmapsto \pi^n u
$$

is an isomorphism of topological groups, where $\mathbb{Z}$ carries the discrete topology and $\mathcal{O}^\times$ the subspace topology. Consequently $F^\times$ is abelian, locally compact, totally disconnected and $\sigma$-compact, and $\mathcal{O}^\times = \mathcal{O} \setminus \mathfrak{m}$ is compact and open.

**Proof.** The factorisation of part (c) of the previous proposition gives the bijection, and multiplicativity is immediate. For continuity and openness, the sets $\pi^n \mathcal{O}^\times$ are open in $F^\times$ and homeomorphic to $\mathcal{O}^\times$, and they partition $F^\times$; the map is a homeomorphism on each factor, the topology on $F^\times$ being the subspace topology of a disjoint union. Compactness of $\mathcal{O}^\times$ is that of the closed subset $\mathcal{O} \setminus \mathfrak{m}$ of the compact space $\mathcal{O}$. $\square$

**Theorem (the residues of the units).** Let $F$ be non-Archimedean with residue field $k$ of cardinality $q$ and residue characteristic $p$. Then there is an isomorphism of topological groups

$$
\mathcal{O}^\times \cong \mu_{q-1}(F) \times U^1, \qquad U^1 = 1 + \mathfrak{m},
$$

where $\mu_{q-1}(F)$ is the group of $(q-1)$-th roots of unity in $F$. The **principal units** $U^n = 1 + \mathfrak{m}^n$ form a decreasing chain

$$
\mathcal{O}^\times = U^0 \supseteq U^1 \supseteq U^2 \supseteq \cdots, \qquad \bigcap_{n \geq 0} U^n = \{1\},
$$

of compact open subgroups, and for every $n \geq 1$ there is an isomorphism of topological groups

$$
U^n / U^{n+1} \cong k^+ = (k, +),
$$

the additive group of the residue field, induced by $1 + \pi^n a \mapsto a \bmod \mathfrak{m}$.

**Proof.** The reduction map $\mathcal{O}^\times \to k^\times$ is a surjective continuous homomorphism of compact groups. The group $k^\times$ is cyclic of order $q-1$; since $q-1$ is coprime to $p$, Hensel's lemma applied to $X^{q-1} - 1$ lifts each root of unity of $k^\times$ uniquely to $\mathcal{O}^\times$, and the lifts form a subgroup $\mu_{q-1}(F)$ mapped isomorphically onto $k^\times$. Its complement is the kernel $U^1$, so the map to $k^\times$ splits and the decomposition follows. The chain and its intersection are immediate from $\bigcap_n \mathfrak{m}^n = 0$. For the last isomorphism, $1 + \pi^n a$ and $1 + \pi^n b$ are congruent modulo $U^{n+1}$ exactly when $a \equiv b \bmod \mathfrak{m}$, and the map is a homomorphism because

$$
(1 + \pi^n a)(1 + \pi^n b) = 1 + \pi^n(a + b) + \pi^{2n} ab \equiv 1 + \pi^n(a+b) \pmod{\mathfrak{m}^{n+1}}
$$

for $n \geq 1$. $\square$

**Corollary.** $\mathcal{O}^\times$ is profinite, and $U^1$ is a pro-$p$ group when $\operatorname{char} F = p$; when $\operatorname{char} F = 0$ the group $U^1$ contains the group $\mu_{p^\infty}(F)$ of roots of unity of $p$-power order, which is finite or isomorphic to $\mathbb{Q}_p/\mathbb{Z}_p$ according to the field, and the quotient $U^1 / \mu_{p^\infty}(F)$ is pro-$p$.

**Proof.** $\mathcal{O}^\times$ is compact, Hausdorff and totally disconnected, and the $U^n$ form a basis of open subgroups around $1$; hence it is an inverse limit of the finite groups $\mathcal{O}^\times/U^n$, that is, profinite. The finite $p$-quotients of $U^1/U^n$ show that the pro-$p$ part is the closure of the $p$-power torsion, and the structure of that torsion in characteristic zero is the standard statement about the torsion of the group of principal units. $\square$

### The Additive Group

**Proposition.** The additive group of a non-Archimedean local field $F$ is a locally compact, totally disconnected topological group, and it is isomorphic as a topological group to the countable direct limit of the compact groups $\pi^{-n}\mathcal{O}$; it is torsion-free when $\operatorname{char} F = 0$ and of exponent $p$ when $\operatorname{char} F = p$.

**Proof.** The locally compact and totally disconnected properties are those of $F$. The description as a union of the increasing chain $\pi^{-n}\mathcal{O}$ is part (c) of the theorem on balls, and the topology of $F$ is the final topology of that union because each $\pi^{-n}\mathcal{O}$ is open. In characteristic $0$ an integer $n \neq 0$ acts invertibly on $F$, so $nx = 0$ forces $x = 0$; in characteristic $p$ one has $px = 0$ for every $x$, and $F$ is an elementary abelian $p$-group as an additive group. $\square$

**Remark.** The additive group of $F$ is neither compact nor discrete; it is $\sigma$-compact. The natural measure-theoretic statements about these groups — the existence and uniqueness of a translation-invariant measure on $F$ and on $F^\times$, and the module function relating the left and right variants — belong to *Locally Compact Groups and Haar Measure*, where the measure and its invariance are constructed, and their integration theory is Part III's; only the topological statements are made here.

---

## Ramification and the Galois Theory

### The Invariants

**Definition.** Let $F$ be a non-Archimedean local field with residue field $k$ of order $q$ and value group $\Gamma \cong \mathbb{Z}$, and let $L/F$ be a finite extension with residue field $k_L$, value group $\Gamma_L$, ramification index $e = [\Gamma_L : \Gamma]$ and residue degree $f = [k_L : k]$.

**(a)** $L/F$ is **unramified** if $e = 1$, **totally ramified** if $f = 1$, and **tamely ramified** if $e$ is prime to the residue characteristic $p$.

**(b)** The **different** $\mathfrak{D}_{L/F}$ is the inverse of the codifferent, the dual of $\mathcal{O}_L$ with respect to the trace form; the **discriminant** is the ideal $\mathfrak{d}_{L/F} = N_{L/F}(\mathfrak{D}_{L/F})$ of $\mathcal{O}_F$.

**Theorem (the fundamental equality).** For a finite separable extension $L/F$ of non-Archimedean local fields, $[L : F] = e f$. The extension is unramified exactly when $[L:F] = f$, and then $\mathcal{O}_L = \mathcal{O}_F[\alpha]$ for a generator $\alpha$ whose reduction generates $k_L$ over $k$ and whose minimal polynomial has a simple root in the residue field.

**Proof.** The degree is additive over a compositum of an unramified and a totally ramified part; the unramified part has $e = 1$ and contributes the residue degree, the totally ramified part has $f = 1$ and contributes the ramification index, and the multiplicativity of $e$ and $f$ over towers gives the formula. The characterisation of the unramified case is the standard statement that an unramified extension is generated by a lift of a generator of the residue field extension, and Hensel's lemma applied to the minimal polynomial of such a lift supplies the factorisation. $\square$

**Proposition (Hensel's lemma on the extension).** Let $F$ be complete for a non-Archimedean absolute value and let $g \in \mathcal{O}_F[X]$. If $a \in \mathcal{O}_F$ satisfies $\lvert g(a) \rvert < \lvert g'(a) \rvert^2$, then there is a unique $b \in \mathcal{O}_F$ with $g(b) = 0$ and $\lvert b - a \rvert < \lvert g'(a) \rvert$. In particular, if the reduction of $g$ modulo $\mathfrak{m}$ has a simple root in $k$, then $g$ has a root in $\mathcal{O}_F$ lifting it.

**Proof.** This is Hensel's lemma of *Absolute Values, Valuations and Completions*, applied to the valuation ring; the second statement is the case $g(a) \equiv 0$ and $g'(a) \not\equiv 0$ modulo $\mathfrak{m}$, which gives $\lvert g(a) \rvert < 1 = \lvert g'(a) \rvert^2$. $\square$

**Corollary (the unramified extension is unique).** For each $n \geq 1$ there is exactly one unramified extension of $F$ of degree $n$ inside a fixed algebraic closure, and its residue field is the unique extension $\mathbb{F}_{q^n}$ of $k$ of degree $n$.

**Proof.** An unramified extension of degree $n$ has residue field of degree $n$ over $k$, and the extension of degree $n$ of a finite field is unique up to isomorphism; the compositum of two unramified extensions of degree $n$ is unramified with residue degree $n$, hence equals each of them, so the extension of degree $n$ is unique. It is obtained by adjoining a primitive $(q^n - 1)$-th root of unity, whose minimal polynomial over $F$ reduces to a polynomial with simple roots over $k$ and splits by Hensel after extending the residue field. $\square$

### Frobenius and Solvability

**Definition.** Let $L/F$ be a finite unramified Galois extension of non-Archimedean local fields. The **Frobenius automorphism** $\varphi \in \operatorname{Gal}(L/F)$ is the unique element inducing the Frobenius $x \mapsto x^q$ on the residue field $k_L$, where $q = \lvert k \rvert$.

**Proposition.** For an unramified Galois extension $L/F$, reduction induces an isomorphism $\operatorname{Gal}(L/F) \to \operatorname{Gal}(k_L/k)$, which is cyclic and generated by the Frobenius; hence $\operatorname{Gal}(L/F)$ is cyclic of order $f = [L:F]$, generated by $\varphi$.

**Proof.** Reduction is a homomorphism of groups, and it is injective because an automorphism fixing the residue field pointwise acts trivially on the maximal ideal and hence, the totally ramified part being absent, acts trivially on $\mathcal{O}_L$ and therefore on $L$. It is surjective because the Frobenius of the residue field lifts by Hensel to an automorphism of $\mathcal{O}_L$ acting on a lift of a generator, and by the uniqueness of the unramified extension this automorphism extends to $L$. $\square$

**Theorem (the Galois group is solvable).** Let $L/F$ be a finite Galois extension of non-Archimedean local fields. Then $\operatorname{Gal}(L/F)$ is solvable, and its **ramification filtration** is a finite chain of normal subgroups with abelian successive quotients.

**Proof.** The group is an extension of the cyclic Galois group of the maximal unramified subextension by the Galois group of the totally ramified part. The latter has a filtration by the higher ramification groups $G_i = \{\sigma : v_L(\sigma(x) - x) \geq i + 1 \text{ for all } x \in \mathcal{O}_L\}$, whose successive quotients $G_i/G_{i+1}$ are abelian, and killed by $p$ for $i \geq 1$. $\square$

**Remark.** The explicit reciprocity law, identifying the abelian extensions of a local field with the open subgroups of $F^\times$ of finite index, is class field theory and belongs to Part I. It is cited here only to record that the local field topology supplies the open subgroup $F^\times$ and the norm subgroup to which the law refers.

---

## Relation to the Global Theory

**Definition.** A **global field** is a finite extension of $\mathbb{Q}$ (a **number field**) or a finite extension of $\mathbb{F}_p(t)$ for a prime $p$ (a **function field**); the two are unified by the product formula over their places.

**Proposition.** Let $K$ be a global field and let $w$ be a place of $K$, that is, an equivalence class of nontrivial absolute values on $K$. Then the completion $K_w$ is a local field, Archimedean when $w$ is Archimedean and non-Archimedean when $w$ is finite, and every non-Archimedean local field is a completion of a global field, namely a finite extension of $\mathbb{Q}_p$ for a number field or a finite extension of $\mathbb{F}_p((t))$ for a function field.

**Proof.** Completion of a global field at a place gives a complete field with a nontrivial absolute value. Local compactness in the non-Archimedean case is the statement that the valuation ring is compact, which holds because the residue field of a place of a global field is finite and the value group is $\mathbb{Z}$; the Archimedean completions of a number field are $\mathbb{R}$ or $\mathbb{C}$. The converse is the classification theorem. $\square$

**Example (the places of $\mathbb{Q}$).** The places of $\mathbb{Q}$ are the Archimedean place $\infty$ with completion $\mathbb{R}$ and the non-Archimedean places $p$ with completions $\mathbb{Q}_p$; the product formula $\lvert x \rvert_\infty \prod_p \lvert x \rvert_p = 1$ of *Absolute Values, Valuations and Completions* holds over all of them. The assembly of all the completions of a global field into a single ring is the adelic construction, another article of this category.

---

## Summary

A **local field** is a field complete with respect to a nontrivial absolute value and locally compact for the induced topology. The classification theorem says that the local fields are $\mathbb{R}$ and $\mathbb{C}$, the finite extensions of $\mathbb{Q}_p$ and the finite extensions of $\mathbb{F}_p((t))$; the first two are the Archimedean local fields and the remaining ones the non-Archimedean. A non-Archimedean local field is a complete discretely valued field with finite residue field and value group $\Gamma \cong \mathbb{Z}$; its valuation ring $\mathcal{O}$ is a discrete valuation ring and a principal ideal domain whose nonzero ideals are the powers $\mathfrak{m}^n = (\pi^n)$ of the maximal ideal, with $\bigcap_n \mathfrak{m}^n = 0$, and the topology is the $\mathfrak{m}$-adic topology of that descending chain.

Topologically, $\mathcal{O}$ and each $\mathfrak{m}^n$ are compact and open, $\mathcal{O}$ splits into $q = \lvert k \rvert$ residue classes each of diameter $\lvert \pi \rvert$, the field $F$ is $\sigma$-compact but not compact, and it is totally disconnected, metrisable, Hausdorff, complete and second countable. Every finite extension of a non-Archimedean local field is a local field for the unique extension of the absolute value, with $[F : K] = ef$ for the ramification index $e$ and the residue degree $f$; the extension is unramified when $e = 1$, totally ramified when $f = 1$, and for each $n$ there is a unique unramified extension of degree $n$, obtained by adjoining a primitive $(q^n - 1)$-th root of unity, with cyclic Galois group generated by the Frobenius.

The multiplicative group decomposes topologically as $F^\times \cong \mathbb{Z} \times \mathcal{O}^\times$ with $\mathcal{O}^\times$ compact and open; the filtration $U^n = 1 + \mathfrak{m}^n$ of the principal units has $U^n/U^{n+1} \cong k^+$ and exhibits $\mathcal{O}^\times$ as a profinite group, with the Teichmüller splitting $\mathcal{O}^\times \cong \mu_{q-1}(F) \times U^1$. Hensel's lemma lifts simple roots modulo $\mathfrak{m}$ and is the tool that makes the unramified theory explicit. The Galois group of a finite Galois extension of a non-Archimedean local field is solvable, with the ramification filtration as its abelian layers. Every global field has local fields as its completions at places, and this passage is the beginning of the adelic theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | A local field |
| $\lvert \cdot \rvert$ | The absolute value, normalised so that $\lvert \pi \rvert = q^{-1}$ |
| $\mathcal{O}$ | Valuation ring $\{x : \lvert x \rvert \leq 1\}$ |
| $\mathfrak{m}$ | Maximal ideal $\{x : \lvert x \rvert < 1\}$ |
| $k = \mathcal{O}/\mathfrak{m}$ | Residue field |
| $q = \lvert k \rvert$ | Cardinality of the residue field |
| $\Gamma = \lvert F^\times \rvert$ | Value group, isomorphic to $\mathbb{Z}$ |
| $\pi$ | Uniformiser, $\mathfrak{m} = (\pi)$ |
| $v(x)$ | Valuation, $x = \pi^{v(x)}u$ |
| $\mathcal{O}^\times$, $F^\times$ | Unit group (compact) and multiplicative group |
| $U^n = 1 + \mathfrak{m}^n$ | Principal units, $U^0 = \mathcal{O}^\times$ |
| $\mu_{q-1}(F)$ | Teichmüller roots of unity in $F$ |
| $e$, $f$ | Ramification index and residue degree, $[F:K] = ef$ |
| $k^+$ | Additive group of the residue field |
| $L/F$, $k_L$, $\Gamma_L$ | A finite extension and its residue field and value group |
| $\mathfrak{D}_{L/F}$, $\mathfrak{d}_{L/F}$ | Different and discriminant |
| $\varphi$ | Frobenius automorphism of an unramified extension |
| $K$, $K_w$ | A global field and its completion at a place $w$ |
| $\mathbb{Q}_p$, $\mathbb{Z}_p$, $\mathbb{F}_p((t))$, $\mathbb{F}_p[[t]]$ | The prime examples |
| $\mathbb{C}_p$ | Completion of $\overline{\mathbb{Q}_p}$, complete but not locally compact |







## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the classification, ramification, the different and the Galois theory of local fields.
- André Weil, *Basic Number Theory* (Springer, 3rd ed. 1974), for the topological characterisation of local fields and the structure of the multiplicative group.
- J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory* (Academic Press, 1967), for the local-global theory, the different and the discriminant.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for local fields as completions of global fields and the ramification filtration.
- Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions* (Springer, 2nd ed. 1984), for the elementary structure of $\mathbb{Q}_p$ and its extensions.
- Fernando Q. Gouvêa, *p-adic Numbers: An Introduction* (Springer, 2nd ed. 1997), for accessible proofs of Hensel's lemma and of the structure of $\mathbb{Z}_p^\times$.
- John W. Milnor, *Introduction to Algebraic K-Theory* (Princeton, 1971), for the local-field computations that recur in K-theory and class field theory.
