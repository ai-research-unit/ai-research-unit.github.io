# __Topological Rings and Fields__

## Introduction

A topological ring is a ring equipped with a topology in which addition, negation and multiplication are continuous; a topological field additionally has inversion continuous on the nonzero elements. The theory is the meeting point of algebra and topology: it makes sense of limits of algebraic operations, of completeness of a ring, and of the passage from a ring to a larger one in which certain limits exist, the **completion**. The two families of examples that matter most are the $I$-adic topologies of commutative algebra, where a descending chain of ideals $I^n$ supplies neighbourhoods of $0$, and the topologies induced by absolute values and valuations, whose completions are not covered here.

This article develops topological rings and fields in the generality needed for the corpus, defines the $I$-adic topology, states the Krull intersection theorem that decides when that topology is Hausdorff, and constructs the $I$-adic completion as an inverse limit of quotients. The metric and valued completions, together with the $p$-adic fields, are not covered here; here they appear only as examples.

Throughout, $R$ is a commutative ring with $1 \neq 0$, the topology on a topological ring is assumed to make the additive group a topological group, and Cauchy sequences are used rather than filters unless a statement is cleaner in the filter language. Ideals and quotients are from *Rings*, and the $I$-adic ideals $I^n$ are from the same source.

---

## Topological Rings

### Definition

**Definition.** A **topological ring** is a ring $R$ together with a topology such that the maps

$$
R \times R \to R, \quad (x,y) \mapsto x + y, \qquad R \to R, \quad x \mapsto -x, \qquad R \times R \to R, \quad (x,y) \mapsto xy
$$

are continuous, where $R \times R$ carries the product topology.

**Proposition.** Let $R$ be a topological ring.

**(a)** For each $x \in R$ the translations $y \mapsto y + x$ and $y \mapsto -y + x$ are homeomorphisms; hence the topology is determined by the filter of neighbourhoods of $0$.

**(b)** If $U$ is a neighbourhood of $0$ then there is a neighbourhood $V$ of $0$ with $V + V \subseteq U$ and $V \subseteq -U$.

**(c)** For every neighbourhood $U$ of $0$ there is a neighbourhood $V$ of $0$ with $V \cdot V \subseteq U$.

**(d)** The closure $\overline{\{0\}}$ is the intersection of all neighbourhoods of $0$ and is a closed ideal of $R$; the quotient $R/\overline{\{0\}}$ is Hausdorff. In particular

$$
R \text{ is Hausdorff} \iff \overline{\{0\}} = \{0\} \iff \bigcap_{U \ni 0} U = \{0\}.
$$

**(e)** $R$ is Hausdorff if and only if it is $T_1$, and if and only if it is $T_0$.

**Proof.** (a) is the continuity of addition in one variable and the existence of inverses. (b) is the continuity of addition at $(0,0)$ and of negation. (c) is the continuity of multiplication at $(0,0)$. (d) The complement of a neighbourhood of $0$ is closed, so $\overline{\{0\}} \subseteq U$ for every neighbourhood $U$; conversely any point in all neighborhoods of $0$ cannot be separated from $0$. Adding and multiplying elements of $\overline{\{0\}}$ by elements of $R$ keeps them in every neighbourhood of $0$ by continuity, so $\overline{\{0\}}$ is an ideal; the quotient is Hausdorff because its zero element has closure $\{0\}$. (e) In the additive topological group $R$, the $T_0$, $T_1$ and $T_2$ conditions are equivalent, since translating a pair of distinct points to $(x-y, 0)$ and applying the group operations separates them. $\square$

**Corollary.** Every topological ring has a Hausdorff quotient, namely $R/\overline{\{0\}}$, and the ideal $\overline{\{0\}}$ is contained in every neighbourhood of $0$; it is the obstruction to Hausdorffness.

### Examples

**Example (discrete).** Every ring with the discrete topology is a topological ring; the only neighbourhood of $0$ is $\{0\}$.

**Example ($\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$).** The fields $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$ with the order or metric topology are topological fields: addition, multiplication and inversion are continuous, and $\mathbb{Q}$ is a subfield of $\mathbb{R}$ with the subspace topology.

**Example (rings of functions).** The ring of continuous real-valued functions on a topological space with the compact-open topology is a topological ring, with pointwise operations; this illustrates that topological rings are not confined to the algebraic main line of this corpus.

### Subrings, Quotients and Products

**Proposition.** Let $R$ be a topological ring.

**(a)** If $S \subseteq R$ is a subring, then $S$ with the subspace topology is a topological ring, and $\overline{S}$ is a subring of $R$.

**(b)** If $I \subseteq R$ is an ideal, then $R/I$ with the quotient topology is a topological ring, and $R/I$ is Hausdorff if and only if $I$ is closed in $R$.

**(c)** If $\{R_\alpha\}$ is a family of topological rings, then $\prod_\alpha R_\alpha$ with the product topology is a topological ring, and it is Hausdorff if and only if every $R_\alpha$ is.

**Proof.** (a) The subspace topology makes the restricted operations continuous; the closure of a subring is a subring by continuity of the operations. (b) The quotient map is open and continuous, so the operations factor to continuous maps; the quotient is Hausdorff exactly when the point $\{0\}$ is closed, exactly when $I$ is closed. (c) Continuity of the operations is a coordinatewise matter, and a product of Hausdorff spaces is Hausdorff. $\square$

---

## Topological Fields

### Definition

**Definition.** A **topological field** is a field $F$ with a topology making it a topological ring in which the inversion map

$$
F^\times \to F^\times, \qquad x \mapsto x^{-1}
$$

is continuous, where $F^\times$ carries the subspace topology. A **topological field** is required to be Hausdorff in what follows.

**Proposition.** Let $F$ be a topological field.

**(a)** $F^\times$ is open in $F$, and $F \setminus \{0\}$ is open.

**(b)** For $a \neq 0$, the maps $x \mapsto ax$ and $x \mapsto ax^{-1}$ are homeomorphisms of $F$ and of $F^\times$.

**(c)** Inversion is a homeomorphism of $F^\times$ onto itself.

**(d)** A field admits no proper nonzero ideal, so the only $I$-adic topologies on a field are the discrete one, from $I = 0$, and the indiscrete one, from $I = F$. Consequently the interesting topologies on fields arise from absolute values and valuations, not from ideals.

**Proof.** (a) $\{0\}$ is closed because $F$ is Hausdorff, so its complement is open and equals $F^\times$ as $F$ is a field. (b) Multiplication by $a \neq 0$ is a continuous map with continuous inverse given by multiplication by $a^{-1}$; the same for $F^\times$ and composition with inversion. (c) Inversion is continuous on $F^\times$ and is an involution, hence a homeomorphism. (d) immediate. $\square$

**Remark.** The inclusion $F^\times \to F$ is continuous and open, its image $F^\times$ being the open set of (a); it is not closed when $F$ is not discrete, since then $0$ lies in the closure of $F^\times$. The zero element is the only point at which inversion fails to be defined. This is why completion statements for fields are stated for the multiplicative group $F^\times$ and for the additive group $F$ separately, and why a topological field structure contains strictly more than the additive and multiplicative group structures.

### Examples

| Field | Topology | Hausdorff | Complete |
|---|---|---|---|
| $\mathbb{Q}$ | usual, from the metric $\lvert \cdot \rvert$ | yes | no |
| $\mathbb{R}$ | usual, from the metric $\lvert \cdot \rvert$ | yes | yes |
| $\mathbb{C}$ | usual, from the metric $\lvert \cdot \rvert$ | yes | yes |
| $\mathbb{Q}(t)$ | order topology, $t$ infinite | yes | no |
| $k((t))$ | $t$-adic topology | yes | yes |
| $\mathbb{Q}_p$ | $p$-adic topology | yes | yes |
| any field | discrete | yes | yes |
| any field | indiscrete | no if $F \neq 0$ | yes |

**Remark.** The $p$-adic field $\mathbb{Q}_p$ and the field of formal Laurent series $k((t))$ are topological fields whose topologies are neither order topologies nor metric topologies in the naive sense; both are completions, the second of $k(t)$ and the first of $\mathbb{Q}$, and both are treated.

---

## The $I$-adic Topology

### Definition

**Definition.** Let $R$ be a ring and let $I \subseteq R$ be an ideal. The **$I$-adic topology** on $R$ is the topology in which a fundamental system of neighbourhoods of $0$ is given by the powers

$$
I^0 = R \supseteq I^1 = I \supseteq I^2 \supseteq I^3 \supseteq \cdots,
$$

that is, the basic open neighbourhoods of a point $x$ are the cosets $x + I^n$, $n \geq 0$. A topology obtained this way from an ideal is called a **linear topology**, and more generally a topology is linear when $0$ has a fundamental system of neighbourhoods consisting of additive subgroups.

**Proposition.** The $I$-adic topology makes $R$ a topological ring.

**Proof.** Addition: $(x + I^n) + (y + I^n) \subseteq x+y+I^n$. Negation: $-(x+I^n) = -x+I^n$. Multiplication: $(x+I^n)(y+I^n) \subseteq xy + I^n$, since $xI^n \subseteq I^n$ and $yI^n \subseteq I^n$ and $I^n I^n \subseteq I^n$, all ideals. Hence the operations are continuous with the cosets as basic neighbourhoods. $\square$

**Proposition (change of ideal).** The $I$-adic topology depends only on the cofinality class of the filtration $I^n$: if $J$ is an ideal and there are $m, n \geq 1$ with $I^n \subseteq J$ and $J^m \subseteq I$, then the $J$-adic topology and the $I$-adic topology on $R$ coincide.

**Proposition (Hausdorff criterion).** The $I$-adic topology on $R$ is Hausdorff if and only if

$$
\bigcap_{n \geq 0} I^n = 0.
$$

**Proof.** By the general criterion, the topology is Hausdorff exactly when the intersection of all neighbourhoods of $0$ is $\{0\}$; the neighbourhoods of $0$ contain the sets $I^n$ and are contained in cosets of them, so the intersection of all neighbourhoods of $0$ equals $\bigcap_n I^n$. $\square$

**Theorem (Krull intersection theorem).** Let $R$ be a Noetherian local ring with maximal ideal $\mathfrak{m}$. Then

$$
\bigcap_{n \geq 0} \mathfrak{m}^n = 0 .
$$

Consequently the $\mathfrak{m}$-adic topology on a Noetherian local ring is Hausdorff. More generally, for a Noetherian ring $R$ and an ideal $I$, the intersection $\bigcap_n I^n$ is the set of elements of $R$ annihilated by $1 + x$ for some $x \in I$; the intersection is $0$ when $R$ is a domain and $I \neq R$.

**Proof.** The theorem is standard and is proved by the Artin–Rees lemma; it is cited here for the Hausdorff statement and is not reproved. $\square$

**Corollary.** For a Noetherian domain $R$ and a proper ideal $I \neq 0$, the $I$-adic topology is Hausdorff. In particular the $p$-adic topology on $\mathbb{Z}$ and the $(t)$-adic topology on $k[t]$ are Hausdorff, and the topology on $R$ is the same as the topology defined by the decreasing chain $I^n$.

### Examples

**Example ($p$-adic topology on $\mathbb{Z}$).** Take $R = \mathbb{Z}$ and $I = (p)$ for a prime $p$. The topology has basic neighbourhoods of $0$ the ideals $p^n\mathbb{Z}$, so two integers are close when they are congruent modulo a high power of $p$. This topology is Hausdorff by Krull. It is not the same as the usual topology: the sequence $p^n$ converges to $0$ in the $p$-adic topology, while in the usual topology it diverges.

**Example ($(t)$-adic topology on $k[t]$).** Take $R = k[t]$ for a field $k$ and $I = (t)$. Two polynomials are close when they agree to high order at $0$; the basic neighbourhood of $0$ at level $n$ is $t^n k[t]$. The topology is Hausdorff.

**Example (nilpotent ideal: the topology is discrete).** Let $R = k[t]/(t^2)$ and $I = (t)$. Then $I^2 = 0$, so the powers are $R \supseteq I \supseteq 0 \supseteq 0 \supseteq \cdots$ and $\{0\} = I^2$ is a neighbourhood of $0$: the $I$-adic topology is discrete. Hence it is Hausdorff and complete, and $\bigcap_n I^n = 0$ holds trivially. More generally the $I$-adic topology on $R/I^m$ is discrete, because the powers of $I(R/I^m) = I/I^m$ vanish from the $m$-th on.

**Example (non-Hausdorff).** Let $k$ be a field, let $R = \prod_{n \geq 1} k$ be the product of countably many copies of $k$, and let $I = \bigoplus_{n \geq 1} k$ be the direct sum, an ideal of $R$. Writing $e_n$ for the idempotent supported at $n$, one has $e_n = e_n^2 \in I^2$, so $I^n = I$ for every $n \geq 1$, and hence

$$
\bigcap_{n \geq 0} I^n = I \neq 0 .
$$

The $I$-adic topology is therefore not Hausdorff: the neighbourhood filter of $0$ is generated by the single ideal $I$, so the closure of $\{0\}$ is $I \neq 0$, and no element of $I$ can be separated from $0$. The ideal $I$ is both open and closed, since a coset $x + I$ with $x \notin I$ is disjoint from $I$, so the quotient $R/I$ is discrete. The ring $R$ is not Noetherian, so the Krull intersection theorem does not apply, and it need not: the hypothesis of Noetherianity is exactly what fails here.

---

## Completions

### Cauchy Sequences and Completeness

**Definition.** Let $R$ be a ring with a linear topology defined by a descending filtration $R = R_0 \supseteq R_1 \supseteq R_2 \supseteq \cdots$ of ideals, so that the basic neighbourhoods of $0$ are the ideals $R_n$.

**(a)** A sequence $(x_n)$ in $R$ is **Cauchy** if for every $N$ there is $n_0$ with $x_n - x_m \in R_N$ for all $n, m \geq n_0$.

**(b)** The sequence **converges** to $x$ if for every $N$ there is $n_0$ with $x_n - x \in R_N$ for all $n \geq n_0$.

**(c)** $R$ is **complete** if every Cauchy sequence converges.

The definitions are the usual ones for the metric-like uniformity generated by the filtration, and they agree with the metric definitions when the filtration comes from an absolute value or from the powers of a valuation ideal.

### The $I$-adic Completion

**Definition.** Let $R$ be a ring and $I \subseteq R$ an ideal. The **$I$-adic completion** of $R$ is the inverse limit

$$
\widehat{R} = \varprojlim_{n} R/I^n,
$$

the ring of compatible sequences $(x_n)$ with $x_n \in R/I^n$ and $x_{n+1} \mapsto x_n$ under the natural projections. The natural maps $R \to R/I^n$ give a ring homomorphism $\iota : R \to \widehat{R}$.

**Theorem.** Let $R$ be a ring and $I \subseteq R$ an ideal.

**(a)** $\widehat{R}$ is a ring, and it is a topological ring for the topology whose basic neighbourhoods of $0$ are the ideals $\widehat{I}^{\,n}$ where $\widehat{I} = \ker(\widehat{R} \to R/I)$; the natural map $\iota : R \to \widehat{R}$ is continuous.

**(b)** $\widehat{R}$ is complete and Hausdorff, and $\widehat{R}/\widehat{I}^{\,n} \cong R/I^n$ for all $n$.

**(c)** $\ker \iota = \bigcap_{n \geq 0} I^n$, so $\iota$ is injective exactly when the $I$-adic topology is Hausdorff; the image of $\iota$ is dense in $\widehat{R}$.

**(d) (Universal property)** If $S$ is a complete Hausdorff topological ring and $f : R \to S$ is a continuous ring homomorphism, then there is a unique continuous ring homomorphism $\widehat{f} : \widehat{R} \to S$ with $\widehat{f} \circ \iota = f$.

**Proof sketch.** (a) The inverse limit of rings is a ring, and the canonical maps are ring homomorphisms; the topology on $\widehat{R}$ is the inverse limit topology, which is linear. (b) A Cauchy sequence in $\widehat{R}$ has coordinates converging in the discrete rings $R/I^n$, and the limit exists and is compatible, so $\widehat{R}$ is complete; Hausdorffness follows from the definition of the inverse limit, since an element with all coordinates $0$ is $0$. The isomorphism $\widehat{R}/\widehat{I}^{\,n} \cong R/I^n$ is the standard exactness of inverse limits for constant quotients. (c) The kernel consists of the elements whose images in every $R/I^n$ vanish, which is exactly the intersection; density holds because the image of $R$ surjects onto each $R/I^n$. (d) A continuous homomorphism of topological groups is uniformly continuous for the additive uniformities, so it extends uniquely and continuously from the dense subring $R \subseteq \widehat{R}$ to $\widehat{R}$; the extension is a ring homomorphism because multiplication is continuous and $R$ is dense. $\square$

**Corollary.** If $R$ is Hausdorff for the $I$-adic topology, then $R$ embeds densely in $\widehat{R}$, and $\widehat{R}$ is the smallest complete Hausdorff ring containing $R$ as a dense subring.

### Examples

**Example (the $p$-adic integers).** The $(p)$-adic completion of $\mathbb{Z}$ is

$$
\mathbb{Z}_p = \varprojlim_n \mathbb{Z}/p^n\mathbb{Z},
$$

the ring of $p$-adic integers. It is a complete Hausdorff topological ring, a discrete valuation ring whose maximal ideal is $p\mathbb{Z}_p$, and its fraction field is the field $\mathbb{Q}_p$ of $p$-adic numbers. The natural map $\mathbb{Z} \to \mathbb{Z}_p$ is injective, and $\mathbb{Z}_p/p^n\mathbb{Z}_p \cong \mathbb{Z}/p^n\mathbb{Z}$.

**Example (formal power series).** The $(t)$-adic completion of $k[t]$ is

$$
k[[t]] = \varprojlim_n k[t]/(t^n),
$$

the ring of formal power series. Its fraction field is the field $k((t))$ of formal Laurent series, obtained by adjoining $t^{-1}$, and $k((t))$ is the completion of $k(t)$ for the $t$-adic valuation.

**Example (the reals).** The completion of $\mathbb{Q}$ for the usual absolute value is $\mathbb{R}$; this completion is not $I$-adic, because $\mathbb{Q}$ is a field and has no proper nonzero ideal, and it is constructed from the metric instead. That construction, and the corresponding construction of $\mathbb{Q}_p$, belongs and to *The Real Numbers*.

**Remark.** The three completions of $\mathbb{Q}$ by the absolute values are $\mathbb{R}$ (the usual absolute value) and $\mathbb{Q}_p$ for each prime $p$ (the $p$-adic absolute values); the fields $\mathbb{Q}_p$ are exactly the completions of $\mathbb{Q}$ that arise from the $(p)$-adic topology on the subring $\mathbb{Z}_{(p)}$ of *Localization and the Fraction Field*.

---

## Summary

A topological ring is a ring in which addition, negation and multiplication are continuous, and the topology is determined by the neighbourhood filter of $0$; the closure of $\{0\}$ is a closed ideal, the quotient by it is Hausdorff, and a topological ring is Hausdorff exactly when it is $T_1$, exactly when it is $T_0$. Subrings, quotients by closed ideals and products of topological rings are topological rings. A topological field has inversion continuous on the open set $F^\times$; because a field has no proper nonzero ideal, the only $I$-adic topologies on a field are the discrete and the indiscrete ones, and the useful topologies on fields come instead from absolute values and valuations.

For an ideal $I$ of a ring $R$ the $I$-adic topology has the powers $I^n$ as a fundamental system of neighbourhoods of $0$ and makes $R$ a topological ring; it is Hausdorff exactly when $\bigcap_n I^n = 0$, which holds for $\mathfrak{m}$-adic topologies on Noetherian local rings by the Krull intersection theorem and, more generally, for proper ideals in Noetherian domains. The $I$-adic completion $\widehat{R} = \varprojlim_n R/I^n$ is a complete Hausdorff topological ring containing $R$ with dense image, with kernel of the natural map $\bigcap_n I^n$, and it is universal among complete Hausdorff topological rings receiving a continuous homomorphism from $R$. The standard examples are $\mathbb{Z}_p$ as the $(p)$-adic completion of $\mathbb{Z}$, the formal power series ring $k[[t]]$ as the $(t)$-adic completion of $k[t]$, and $\mathbb{R}$ as the metric completion of $\mathbb{Q}$ with respect to the usual absolute value; the valued completion of $\mathbb{Q}$ at each prime gives the field $\mathbb{Q}_p$.

| Ring or field | Topology | Complete | Hausdorff |
|---|---|---|---|
| $\mathbb{Z}$ | $p$-adic, $I = (p)$ | no | yes |
| $\mathbb{Z}_p$ | $p$-adic | yes | yes |
| $k[t]$ | $t$-adic | no | yes |
| $k[[t]]$ | $t$-adic | yes | yes |
| $k(t)$ | $t$-adic | no | yes |
| $k((t))$ | $t$-adic | yes | yes |
| $\mathbb{Q}$ | usual metric | no | yes |
| $\mathbb{R}$ | usual metric | yes | yes |
| $\mathbb{Q}$ | $p$-adic metric | no | yes |
| $\mathbb{Q}_p$ | $p$-adic | yes | yes |
| $\prod_n k$, $I = \bigoplus_n k$ | $I$-adic | yes | no |
| $k[t]/(t^2)$ | $t$-adic, discrete | yes | yes |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Topological ring; often commutative with $1 \neq 0$ |
| $F$ | Topological field |
| $R^\times$, $F^\times$ | Unit groups, open when $R$, $F$ are Hausdorff |
| $\overline{\{0\}}$ | Closure of zero, a closed ideal |
| $I^n$ | Powers of an ideal, a filtration |
| $x + I^n$ | Basic neighbourhood in the $I$-adic topology |
| $\mathfrak{m}$ | Maximal ideal of a local ring |
| $\widehat{R} = \varprojlim_n R/I^n$ | $I$-adic completion |
| $\widehat{I}$ | Ideal of $\widehat{R}$ generated by $\iota(I)$, defining its topology |
| $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$ | $p$-adic integers |
| $k[[t]] = \varprojlim k[t]/(t^n)$ | Formal power series ring |
| $k((t))$ | Formal Laurent series field |
| $\mathbb{Q}_p$ | $p$-adic numbers, fraction field of $\mathbb{Z}_p$ |
| $\mathbb{R}$ | Metric completion of $\mathbb{Q}$ |





## Further Reading

- Nicolas Bourbaki, *General Topology, Chapters 1–4* and *Commutative Algebra, Chapters 1–7* (Springer, 1995, 1998), for topological groups, topological rings and linear topologies.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989), for the Krull intersection theorem, the Artin–Rees lemma and completions.
- Atiyah and Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the $I$-adic topology, the Krull intersection theorem and the structure of complete local rings.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the theory of topological fields and their completions.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for $\mathbb{Z}_p$, $\mathbb{Q}_p$ and the interplay with valuations.
