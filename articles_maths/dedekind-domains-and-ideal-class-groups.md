# __Dedekind Domains and Ideal Class Groups__

## Introduction

In the ring of integers of a number field, unique factorisation of elements can fail, but unique factorisation of *ideals* never does: every nonzero ideal is a product of prime ideals in one and only one way. Rings with this property are the **Dedekind domains**, and they are exactly the Noetherian integrally closed domains of Krull dimension one. The theorem is the compensation for the loss of unique factorisation of elements, and it is the foundation of algebraic number theory.

The failure of unique factorisation is measured by the **ideal class group**: the quotient of the group of fractional ideals by the subgroup of principal fractional ideals. Its order is the **class number**, and the ring is a principal ideal domain exactly when the class group is trivial. For the ring of integers of a number field the class group is finite, and its order is one of the most delicate invariants of the field.

This article defines Dedekind domains, proves the unique factorisation of ideals, develops fractional ideals and their invertibility, constructs the ideal class group, and computes it in the basic examples, including the Gaussian integers and $\mathbb{Z}[\sqrt{-5}]$, the classical example of class number $2$. Throughout, $R$ is an integral domain with fraction field $K = \operatorname{Frac}(R)$ and $R \neq$ a field; the theory of integrally closed domains, integral extensions and Krull dimension is from *Integral Extensions and Krull Dimension*, chain conditions and primary decomposition from *Noetherian and Artinian Rings* and *Primary Decomposition*, localisation from *Localization and the Fraction Field*, and divisibility and unique factorisation from *Unique Factorisation Domains*. The valuation-theoretic description of the local rings of a Dedekind domain is; here the local rings are described by their ideals instead.

---

## Dedekind Domains

### Definition and First Consequences

**Definition.** An integral domain $R$ that is not a field is a **Dedekind domain** if

**(D1)** $R$ is Noetherian;

**(D2)** $R$ is integrally closed in its fraction field $K$;

**(D3)** $R$ has Krull dimension one: every nonzero prime ideal is maximal.

**Example.** $\mathbb{Z}$ is a Dedekind domain. It is Noetherian, integrally closed in $\mathbb{Q}$, and its nonzero primes $(p)$ are maximal.

**Example.** The polynomial ring $k[x]$ over a field is a Dedekind domain, indeed a Euclidean domain, hence Noetherian, integrally closed, and of dimension one.

**Example.** The Gaussian integers $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ are a Dedekind domain. They are Euclidean for the norm $N(a+bi) = a^2 + b^2$, so Noetherian and integrally closed; the dimension is one because $\mathbb{Z}[i]$ is integral over $\mathbb{Z}$ and has the same dimension, by *Integral Extensions and Krull Dimension*.

**Example.** The ring $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a,b\in\mathbb{Z}\}$ is a Dedekind domain. It is the ring of integers of $\mathbb{Q}(\sqrt{-5})$, so it is integral over $\mathbb{Z}$ and integrally closed, but it is **not** a unique factorisation domain, since

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}),
$$

and $2, 3, 1+\sqrt{-5}, 1-\sqrt{-5}$ are all irreducible and pairwise non-associate. The ideal theory of this ring is worked out below.

**Example.** Not every Noetherian domain of dimension one is Dedekind: the ring $R = k[t^2, t^3]$ has dimension one, since it is integral over the polynomial ring $k[t^2]$ and dimension is preserved by integral extensions, but it is not integrally closed. The element $t$ lies in $\operatorname{Frac}(R) = k(t)$ and is integral over $R$, being a root of $x^2 - t^2$ with $t^2 \in R$, yet $t \notin R$. The failure is precisely the failure of (D2), and it is what makes the ideal theory of $k[t^2,t^3]$ more complicated than that of $k[t]$.

**Proposition.** In a Dedekind domain the prime ideals are the zero ideal and the nonzero maximal ideals; there are no other primes, and no nonzero prime is contained in another.

**Proof.** Dimension one says exactly that a nonzero prime is maximal, and a maximal ideal has height one in a domain of dimension one. $\square$

### Local Structure

The local study of a Dedekind domain is completely explicit, and it avoids the theory of valuations, which is developed separately.

**Definition.** A **discrete valuation ring** is a local principal ideal domain that is not a field. Its unique maximal ideal is principal, say $(\pi)$, and every nonzero ideal is a power $(\pi^n)$ of it; the element $\pi$ is a **uniformiser**.

The name is justified, where it is shown that a discrete valuation ring is exactly the valuation ring of a discrete valuation of its fraction field; that article is the natural place for the valuation-theoretic description, and here only the ideal structure is used.

**Theorem (local structure).** Let $R$ be a Dedekind domain and let $\mathfrak{m}$ be a nonzero prime ideal. Then the localisation $R_\mathfrak{m}$ is a discrete valuation ring, with maximal ideal $\mathfrak{m} R_\mathfrak{m}$. Conversely, a Noetherian domain of dimension one whose localisations at maximal ideals are all discrete valuation rings is a Dedekind domain.

**Proof sketch.** The localisation $R_\mathfrak{m}$ is a Noetherian local domain of dimension one, integrally closed (integral closedness is preserved by localisation), with maximal ideal $\mathfrak{m}R_\mathfrak{m}$. It remains to see that this maximal ideal is principal. Choose $0 \neq a \in \mathfrak{m}$; since $\mathfrak{m}$ is the only nonzero prime, the radical of $(a)$ is $\mathfrak{m}$, so $(a)$ is $\mathfrak{m}$-primary and $\mathfrak{m}^n \subseteq (a)$ for some $n$. Take $n$ minimal and $b \in \mathfrak{m}^{n-1} \setminus (a)$. Then $b/a \notin R$, while $(b/a)\mathfrak{m} \subseteq (1/a)\mathfrak{m}^n \subseteq R$, so $(b/a) \in (R : \mathfrak{m})$ and $(R:\mathfrak{m}) \supsetneq R$. The product $\mathfrak{m}(R:\mathfrak{m})$ is an ideal with $\mathfrak{m} \subseteq \mathfrak{m}(R:\mathfrak{m}) \subseteq R$, and since $\mathfrak{m}$ is maximal, either $\mathfrak{m}(R:\mathfrak{m}) = \mathfrak{m}$ or it equals $R$. The first alternative would put $(R:\mathfrak{m})$ inside $\{x \in K : x\mathfrak{m} \subseteq \mathfrak{m}\}$, whose elements are integral over $R$ by the determinant argument applied to the finitely generated $R$-submodule $\mathfrak{m}$, hence lie in $R$ by integral closedness; then $(R:\mathfrak{m}) = R$, a contradiction. So $\mathfrak{m}(R:\mathfrak{m}) = R$, the ideal $\mathfrak{m}$ is invertible, and an invertible ideal of a local ring is principal. Thus $\mathfrak{m}R_\mathfrak{m} = (\pi)$ and every ideal, being an $\mathfrak{m}$-primary power, is a power of $(\pi)$. The converse assembles the local conditions into (D1)–(D3). $\square$

**Corollary.** In a Dedekind domain, for each nonzero prime $\mathfrak{m}$ and each nonzero element $x \in K$ there is a unique integer $v_\mathfrak{m}(x) \in \mathbb{Z}$ with $x R_\mathfrak{m} = (\pi_\mathfrak{m})^{v_\mathfrak{m}(x)}$, where $\pi_\mathfrak{m}$ is a uniformiser, and $v_\mathfrak{m}$ is additive. The integer $v_\mathfrak{m}(x)$ is the **order of vanishing** of $x$ at $\mathfrak{m}$.

The functions $v_\mathfrak{m}$ are valuations, and their systematic theory — independent valuations, extensions, the approximation theorem in valuation language — is not covered here. The present article uses only that each $v_\mathfrak{m}$ is an additive integer-valued function with $v_\mathfrak{m}(x) \geq 0$ exactly when $x \in R_\mathfrak{m}$.

---

## Unique Factorisation of Ideals

### Fractional Ideals

**Definition.** A **fractional ideal** of $R$ is a nonzero subset $J \subseteq K$ such that

**(a)** $J$ is an $R$-submodule of $K$: it is closed under addition and under multiplication by elements of $R$;

**(b)** there is $0 \neq x \in K$ with $xJ \subseteq R$.

The **product** of two fractional ideals is

$$
I J = \Bigl\{\sum_{i=1}^{n} a_i b_i : a_i \in I,\ b_i \in J,\ n \geq 0\Bigr\},
$$

which is again a fractional ideal. An **integral ideal** is a fractional ideal contained in $R$, that is, an ordinary nonzero ideal of $R$. A fractional ideal $I$ is **invertible** if there is a fractional ideal $J$ with $I J = R$, and then $J$ is written $I^{-1}$.

The inverse, when it exists, is determined and is

$$
I^{-1} = (R : I) = \{x \in K : x I \subseteq R\}.
$$

**Proposition.** In an integral domain $R$, the invertible fractional ideals form an abelian group under multiplication, with identity $R$; an invertible integral ideal is principal, and the principal fractional ideals are invertible. A fractional ideal $I$ is invertible if and only if $I R_\mathfrak{m} = x_\mathfrak{m} R_\mathfrak{m}$ for some $x_\mathfrak{m} \in K^\times$ at every maximal ideal $\mathfrak{m}$.

**Proof.** The group law is inherited from multiplication of $K$-subsets, with inverse $(R:I)$; associativity and commutativity are immediate, and $IR = I$. An integral ideal $I$ that is invertible satisfies $I (R:I) = R$, so there are $a_i \in I$ and $x_i \in (R:I)$ with $\sum a_i x_i = 1$. For $b \in I$, one has $x_i b \in R$, so $b = \sum a_i (x_i b)$ lies in the ideal $(a_1, \ldots, a_n)$, and since each $a_i \in I$ this ideal is $I$; hence $I = (a_1, \ldots, a_n)$ is principal. Conversely a principal fractional ideal $xR$ has inverse $x^{-1}R$. The local criterion is the standard statement that an invertible ideal is locally principal; conversely, a locally principal ideal is invertible, $\sum_i y_i b_i = 1$ with $y_i$ local inverses providing the global inverse after a partition of unity of finitely many localisations. $\square$

### The Factorisation Theorem

**Theorem (unique factorisation of ideals).** Let $R$ be a Dedekind domain and let $0 \neq I \subsetneq R$ be a proper nonzero ideal. Then

$$
I = \mathfrak{p}_1^{e_1} \mathfrak{p}_2^{e_2} \cdots \mathfrak{p}_r^{e_r}
$$

with $\mathfrak{p}_i$ distinct nonzero prime ideals and $e_i \geq 1$, and the representation is unique up to the order of the factors. Equivalently, every nonzero fractional ideal is a product $\prod_{\mathfrak{m}} \mathfrak{m}^{v_\mathfrak{m}}$ with $v_\mathfrak{m} \in \mathbb{Z}$ and $v_\mathfrak{m} = 0$ for all but finitely many $\mathfrak{m}$.

**Proof.** Existence: since $R$ is Noetherian of dimension one, the primary decomposition of $I$ is an intersection of $\mathfrak{m}$-primary ideals for the finitely many maximal ideals $\mathfrak{m}$ containing $I$. In a Dedekind domain an $\mathfrak{m}$-primary ideal is a power of $\mathfrak{m}$: by the local structure theorem the ideal becomes $(\pi^{n})$ in $R_\mathfrak{m}$, and contracting gives $\mathfrak{m}^n$. Taking the product of the primary components, which are pairwise comaximal, gives $I$ as a product of prime powers, since the primary components lie in distinct maximal ideals.

Uniqueness: if $I = \prod \mathfrak{p}_i^{e_i} = \prod \mathfrak{p}_i^{f_i}$, localise at $\mathfrak{p}_j$. Localisation commutes with products of ideals, so $(I)_{\mathfrak{p}_j} = \mathfrak{p}_j^{e_j} R_{\mathfrak{p}_j} = \mathfrak{p}_j^{f_j} R_{\mathfrak{p}_j}$; since $\mathfrak{p}_j R_{\mathfrak{p}_j} = (\pi_j)$ with $\pi_j$ a non-unit and non-zero-divisor, comparing powers in the discrete valuation ring gives $e_j = f_j$. $\square$

**Corollary.** The nonzero fractional ideals of a Dedekind domain form a free abelian group on the set of nonzero prime ideals: every fractional ideal is uniquely

$$
I = \prod_{\mathfrak{m}} \mathfrak{m}^{v_\mathfrak{m}(I)}, \qquad v_\mathfrak{m}(I) \in \mathbb{Z},
$$

the product being finite. In particular every nonzero fractional ideal is invertible, and

$$
I \subseteq J \iff v_\mathfrak{m}(I) \geq v_\mathfrak{m}(J) \ \text{ for every nonzero prime } \mathfrak{m}.
$$

**Proof.** Write a fractional ideal as $x^{-1} I_0$ with $x \in R$ and $I_0 = I \cap R$ an integral ideal, and apply the theorem to $I_0$ and to $(x)$. Invertibility follows from the description, the inverse of $\mathfrak{m}$ being the fractional ideal with $v_{\mathfrak{m}'} = -\delta_{\mathfrak{m},\mathfrak{m}'}$. The containment criterion follows by localising. $\square$

**Corollary (arithmetic of ideals).** For nonzero ideals $I, J$ of a Dedekind domain,

$$
I J = \prod_{\mathfrak{m}} \mathfrak{m}^{v_\mathfrak{m}(I)+v_\mathfrak{m}(J)}, \qquad
I \cap J = \prod_{\mathfrak{m}} \mathfrak{m}^{\max(v_\mathfrak{m}(I), v_\mathfrak{m}(J))}, \qquad
I + J = \prod_{\mathfrak{m}} \mathfrak{m}^{\min(v_\mathfrak{m}(I), v_\mathfrak{m}(J))}.
$$

Thus the ideal lattice of a Dedekind domain is the lattice of divisors of an integer, with intersection, sum and product playing the roles of least common multiple, greatest common divisor and product; and $I \subseteq J$ if and only if $J$ divides $I$.

**Proof.** For the sum and intersection, localise at each maximal ideal, where the identity is the corresponding identity for powers of a principal generator in a discrete valuation ring. $\square$

### The Chinese Remainder Theorem

**Theorem (Chinese remainder).** Let $R$ be a Dedekind domain and let $\mathfrak{a}_1, \ldots, \mathfrak{a}_r$ be nonzero ideals that are pairwise comaximal, meaning $\mathfrak{a}_i + \mathfrak{a}_j = R$ for $i \neq j$. Then the natural map

$$
R \longrightarrow R/\mathfrak{a}_1 \times \cdots \times R/\mathfrak{a}_r
$$

is surjective with kernel $\mathfrak{a}_1 \cap \cdots \cap \mathfrak{a}_r = \mathfrak{a}_1 \cdots \mathfrak{a}_r$, hence induces an isomorphism

$$
R/(\mathfrak{a}_1 \cdots \mathfrak{a}_r) \;\cong\; R/\mathfrak{a}_1 \times \cdots \times R/\mathfrak{a}_r .
$$

**Proof.** The kernel is the intersection, which equals the product for pairwise comaximal ideals. Surjectivity is the standard Chinese remainder argument: for $r = 2$, comaximality gives $a_1 + a_2 = 1$ with $a_i \in \mathfrak{a}_i$, and the element $x = b_1 a_2 + b_2 a_1$ maps to $(b_1, b_2)$ modulo $(\mathfrak{a}_1,\mathfrak{a}_2)$ since $a_2 \equiv 1$ mod $\mathfrak{a}_1$ and $a_1 \equiv 1$ mod $\mathfrak{a}_2$; induction gives the general case. $\square$

The Chinese remainder theorem is what allows a congruence modulo an ideal to be solved prime by prime, and it is the arithmetic engine of class field theory.

---

## The Ideal Class Group

### Definition

**Definition.** Let $R$ be a Dedekind domain. A nonzero fractional ideal is **principal** if it has the form $xR$ for some $x \in K^\times$. Principal fractional ideals form a subgroup of the group of all nonzero fractional ideals, and the **ideal class group** (or **Picard group**) is the quotient

$$
\operatorname{Cl}(R) = \frac{\{\text{nonzero fractional ideals}\}}{\{\text{principal fractional ideals}\}} .
$$

The class of a fractional ideal $I$ is written $[I]$, and the order $\lvert \operatorname{Cl}(R) \rvert$ is the **class number** of $R$ when finite.

**Theorem.** The ideal class group is an abelian group. Its identity is the class of $R$, and $[I] = [J]$ if and only if $I = xJ$ for some $x \in K^\times$. Moreover

$$
\operatorname{Cl}(R) = 0 \iff R \text{ is a principal ideal domain} \iff R \text{ is a unique factorisation domain}.
$$

**Proof.** The group law is induced by multiplication of fractional ideals, which is associative and commutative with identity $R$ and inverses from the corollary above; the quotient by principal ideals is therefore a group, and $[I]=[J]$ exactly when $IJ^{-1}$ is principal, i.e. $I = xJ$.

For the equivalences: $\operatorname{Cl}(R)=0$ says every fractional ideal, in particular every integral ideal, is principal, which is the definition of a principal ideal domain. Over an integral domain, a principal ideal domain is a unique factorisation domain; conversely a Dedekind domain that is a unique factorisation domain is a principal ideal domain, because every nonzero ideal factors into primes and every prime ideal contains an irreducible element, which generates a prime ideal by unique factorisation, so each prime is principal and hence so is every ideal. $\square$

Thus the class group is exactly the obstruction to unique factorisation. When it is trivial one recovers unique factorisation of elements; when it is nontrivial, the ideal factorisation of the elements gives the correction.

**Theorem (Dedekind's theorem on the class group of a number field).** Let $K$ be a number field of degree $n = [K:\mathbb{Q}]$ and let $\mathcal{O}_K$ be its ring of integers, which is a Dedekind domain. Then $\operatorname{Cl}(\mathcal{O}_K)$ is finite.

**Proof sketch.** The ring $\mathcal{O}_K$ embeds into $\mathbb{R}^{r_1} \times \mathbb{C}^{r_2}$ through its real and complex embeddings, and the image is a lattice; Minkowski's convex body theorem then produces, in every ideal class, an integral ideal of norm at most

$$
M_K = \left(\frac{4}{\pi}\right)^{r_2} \frac{n!}{n^n} \sqrt{\lvert d_K \rvert},
$$

the **Minkowski bound**, where $d_K$ is the discriminant. There are only finitely many ideals of norm at most $M_K$, since an ideal of norm $m$ contains $m$ and there are finitely many ideals containing a fixed nonzero element; representatives of the finitely many classes are therefore drawn from a finite set, and the class group is finite. The two ingredients used here are the lattice embedding and the volume estimate of Minkowski; both are statements about distance and measure, which the present Part does not yet have. The proof is therefore completed in Part II, where the Euclidean structure of $\mathbb{R}^{r_1} \times \mathbb{C}^{r_2}$ is available, and the algebraic construction of $\mathcal{O}_K$ itself is carried out; the statement above is recorded here as the arithmetic consequence of the factorisation theorem. $\square$

**Remark (function fields).** The same ideal theory governs the affine rings of algebraic curves: for a smooth affine algebraic curve over a field $k$, the ring of regular functions is a Dedekind doma, and its class group measures the obstruction to unique factorisation of functions. The projective completion of the curve, its divisor group and the degree-zero part of that group are developed andboth, where the class group acquires a geometric meaning; nothing in the present article depends on that development.

---

## Computations

### Principal Ideal Domains

**Example.** $\operatorname{Cl}(\mathbb{Z}) = 0$: every nonzero ideal is $(n)$.

**Example.** $\operatorname{Cl}(k[x]) = 0$: the polynomial ring over a field is a principal ideal domain.

**Example.** $\operatorname{Cl}(\mathbb{Z}[i]) = 0$. The Gaussian integers are Euclidean, hence a principal ideal domain. As a by-product, every prime $p \equiv 1 \pmod 4$ is a sum of two squares, and this is visible in the factorisation of the ideal $(p)$: since $-1$ is a square modulo $p$ in that case, the polynomial $x^2+1$ splits modulo $p$, the ideal $(p)$ splits as a product of two distinct primes, and each of these is principal, generated by an element $a+bi$ with $a^2+b^2 = p$.

### The Class Group of $\mathbb{Z}[\sqrt{-5}]$

Let $R = \mathbb{Z}[\sqrt{-5}]$, $K = \mathbb{Q}(\sqrt{-5})$, and let

$$
P = (2, 1 + \sqrt{-5})
$$

be the ideal generated by $2$ and $1+\sqrt{-5}$. This is a proper ideal, and the quotient $R/P$ is isomorphic to $\mathbb{F}_2$, so $P$ is a prime ideal of norm $2$; it is the unique prime over $(2)$, and $2$ **ramifies**.

**Proposition.** $P$ is not principal, and $P^2 = (2)$.

**Proof.** If $P = (a)$ were principal, then $a$ would divide both $2$ and $1+\sqrt{-5}$ in $R$, so the norm $N(x+y\sqrt{-5}) = x^2+5y^2$ of $a$ would divide both $N(2) = 4$ and $N(1+\sqrt{-5}) = 6$, hence would divide $2$. A element of norm $2$ would satisfy $x^2+5y^2 = 2$, which has no integer solution: $y = 0$ gives $x^2 = 2$, and $|y| \geq 1$ gives $x^2 + 5y^2 \geq 5$. So the norm is $1$ and $a$ is a unit, contradicting that $P$ is proper. Hence $P$ is not principal.

For the square,

$$
P^2 = (4,\ 2(1+\sqrt{-5}),\ (1+\sqrt{-5})^2) = (4,\ 2+2\sqrt{-5},\ -4+2\sqrt{-5}),
$$

using $(1+\sqrt{-5})^2 = 1 + 2\sqrt{-5} - 5 = -4 + 2\sqrt{-5}$. Every generator is divisible by $2$, so $P^2 \subseteq (2)$. Conversely $2 \in P^2$: the ideal contains $4$ and $-4+2\sqrt{-5} = 2(-2+\sqrt{-5})$, and also $2(1+\sqrt{-5})$; since $(1+\sqrt{-5}) - (-2+\sqrt{-5}) = 3$ and $2 \in P^2$, the ideal $P^2$ contains $2$ and $3$ up to the factor $2$: explicitly $(1+\sqrt{-5}) + 2 = 3+\sqrt{-5}$ and $(-4+2\sqrt{-5}) + 2(1+\sqrt{-5}) = 2 - 2\sqrt{-5} + \ldots$, the computation reduces to $2 = 2(1+\sqrt{-5}) - (-4+2\sqrt{-5}) - 4 + 2\cdot 2$, all terms in $P^2$. Hence $P^2 = (2)$. $\square$

**Theorem.** $\operatorname{Cl}(\mathbb{Z}[\sqrt{-5}]) \cong \mathbb{Z}/2\mathbb{Z}$, so the class number is $2$.

**Proof.** The ideal $(3)$ splits: with $R = (3, 1+\sqrt{-5})$ and its conjugate $R' = (3, 1-\sqrt{-5})$, one computes $R R' = (3)$ and $R \neq R'$, so $(3)$ is not prime. Similarly $(1+\sqrt{-5}) = P R$ and $(1-\sqrt{-5}) = P R'$, so the two factorisations of $6$ become the single ideal factorisation

$$
(6) = (2)(3) = P^2 R R' = (P R)(P R') = (1+\sqrt{-5})(1-\sqrt{-5}).
$$

The class $[P]$ has order $2$ since $P^2 = (2)$ is principal and $P$ is not principal. To see that there are no other classes, one uses the Minkowski bound: here $n = 2$, $r_1 = 0$, $r_2 = 1$, $d_K = -20$, so $M_K = (4/\pi)\cdot (2!/4)\sqrt{20} = (4/\pi)\cdot \tfrac12 \cdot 2\sqrt5 = 4\sqrt5/\pi \approx 2.85$. Every ideal class contains an integral ideal of norm at most $2.85$, hence of norm $1$ or $2$; the only ideals of norm $2$ are $P$ and $R$ itself, and the ideals of norm $1$ are $R$ and principal. Hence every class is $[R]$ or $[P]$, and $\operatorname{Cl} \cong \mathbb{Z}/2\mathbb{Z}$. $\square$

The same computation classifies the behaviour of the primes: $2$ ramifies, $3$ splits, and an odd prime $p$ splits exactly when $-5$ is a quadratic residue modulo $p$; this is the first instance of the reciprocity laws developed.

### Class Numbers of Small Quadratic Fields

For the imaginary quadratic field $\mathbb{Q}(\sqrt{-d})$ with $d > 0$ squarefree, the class number is computed from the arithmetic of the ideals of the ring of integers, and the classical tables record the outcome. The first values are as follows.

| $d$ | Field | Ring of integers | Class number |
|---|---|---|---|
| $1$ | $\mathbb{Q}(\sqrt{-1})$ | $\mathbb{Z}[i]$ | $1$ |
| $2$ | $\mathbb{Q}(\sqrt{-2})$ | $\mathbb{Z}[\sqrt{-2}]$ | $1$ |
| $3$ | $\mathbb{Q}(\sqrt{-3})$ | $\mathbb{Z}[\tfrac{1+\sqrt{-3}}{2}]$ | $1$ |
| $5$ | $\mathbb{Q}(\sqrt{-5})$ | $\mathbb{Z}[\sqrt{-5}]$ | $2$ |
| $6$ | $\mathbb{Q}(\sqrt{-6})$ | $\mathbb{Z}[\sqrt{-6}]$ | $2$ |
| $10$ | $\mathbb{Q}(\sqrt{-10})$ | $\mathbb{Z}[\sqrt{-10}]$ | $2$ |
| $14$ | $\mathbb{Q}(\sqrt{-14})$ | $\mathbb{Z}[\sqrt{-14}]$ | $4$ |

The entry for $d = 5$ is the computation above, and the entry for $d = 14$ is included because its class group is not of exponent $2$. For $\mathbb{Q}(\sqrt{-14})$, of discriminant $-56$, the prime $2$ ramifies and the prime $3$ splits: $2\mathcal{O}_K = P_2^2$ and $3\mathcal{O}_K = P_3P_3'$. The class $[P_2]$ has order $2$: it is not principal, since an element of norm $2$ would give $x^2 + 14y^2 = 2$, which has no integral solution, while $P_2^2 = (2)$ is principal. The class $[P_3]$ is not principal for the same reason, and $[P_3]^2 = [P_2]$; hence $[P_3]$ has order $4$ and the class group is cyclic of order $4$, generated by $[P_3]$.

**Remark.** The class group of a Dedekind domain is the obstruction to its being a principal ideal doma, and the class number is therefore the extent of the failure of unique factorisation of elements. The deeper invariants built from it — the class field, the $L$-function, the analytic class number formula — belong, and to the analytic theory of later Parts. The finiteness theorem above makes the class group a finite abelian group, and its structure is one of the central objects of algebraic number theory.

---

## Summary

A Dedekind domain is a Noetherian integrally closed integral domain of Krull dimension one; equivalently, a Noetherian domain of dimension one all of whose localisations at maximal ideals are discrete valuation rings. Standard examples are $\mathbb{Z}$, the polynomial ring $k[x]$, the Gaussian integers $\mathbb{Z}[i]$, and rings of integers of number fields, including $\mathbb{Z}[\sqrt{-5}]$, which is Dedekind though not a unique factorisation domain.

In a Dedekind domain every nonzero ideal factors uniquely as a product of prime powers, and every nonzero fractional ideal is uniquely a finite product of integer powers of prime ideals. The ideal lattice is therefore the divisor lattice of a number: inclusion is divisibility, intersection is least common multiple, and sum is greatest common divisor. The Chinese remainder theorem holds for pairwise comaximal ideals and is the arithmetic engine of the theory.

The class group is the quotient of the group of nonzero fractional ideals by the principal ones. It is trivial exactly for principal ideal domains, hence for those Dedekind domains in which unique factorisation of elements holds; its order is the class number. For the ring of integers of a number field the class group is finite, by the Minkowski bound, whose geometric proof belongs to Part II. The class number of $\mathbb{Z}[\sqrt{-5}]$ is $2$, the class of the prime ideal $P = (2, 1+\sqrt{-5})$ having order $2$ and satisfying $P^2 = (2)$; the two factorisations $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ become one and the same ideal factorisation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Dedekind domain; $K = \operatorname{Frac}(R)$ its fraction field |
| $\mathfrak{p}, \mathfrak{m}$ | Nonzero prime (maximal) ideals |
| $R_\mathfrak{m}$ | Localisation at $\mathfrak{m}$, a discrete valuation ring |
| $\pi_\mathfrak{m}$ | Uniformiser of $R_\mathfrak{m}$ |
| $v_\mathfrak{m}(x)$ | Order of $x \in K^\times$ at $\mathfrak{m}$ |
| $\mathfrak{p}^{e}$ | Prime power; a primary ideal of a Dedekind domain |
| $IJ$ | Product of fractional ideals |
| $(R:I)$, $I^{-1}$ | Inverse fractional ideal, $\{x : xI \subseteq R\}$ |
| $\operatorname{Cl}(R)$ | Ideal class group, fractional ideals modulo principal ideals |
| $[I]$ | Class of the fractional ideal $I$ |
| $\lvert \operatorname{Cl}(R) \rvert$ | Class number |
| $\mathcal{O}_K$ | Ring of integers of a number field $K$ |
| $N(x + y\sqrt{-5})$ | $= x^2 + 5y^2$, the norm on $\mathbb{Z}[\sqrt{-5}]$ |
| $d_K$, $M_K$ | Discriminant of $K$, Minkowski bound |





## Further Reading

- Richard Dedekind, "Über die Theorie der ganzen algebraischen Zahlen", *Supplement XI to Vorlesungen über Zahlentheorie* (Vieweg, 1871), for the original theory of ideals and their unique factorisation in rings of integers.
- Emmy Noether, "Abstrakter Aufbau der Idealtheorie in algebraischen Zahl- und Funktionenkörpern", *Mathematische Annalen* 96 (1927), 26–61, for the abstract characterisation of Dedekind domains and the role of the ascending chain condition.
- Hermann Minkowski, *Geometrie der Zahlen* (Teubner, 1910), for the lattice point argument and the bound that gives the finiteness of the class number.
- Pierre Samuel, *Algebraic Theory of Numbers* (Hermann, 1970), for a compact treatment of Dedekind domains, fractional ideals and the class group.
- Serge Lang, *Algebraic Number Theory* (Springer, 2nd ed. 1994), for the arithmetic of rings of integers, the Minkowski bound and class group computations.
- J. S. Milne, *Algebraic Number Theory* (available online, 2020), for the ideal-theoretic development and the classification of primes in quadratic fields.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for the classical computation of class numbers and the tables of small quadratic fields.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for Dedekind domains as integrally closed one-dimensional Noetherian domains.
