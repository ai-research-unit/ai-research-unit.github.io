# __Splitting Fields and Algebraic Closure__

## Introduction

A polynomial over a field need not have a root in that field, and the smallest extension in which all its roots appear is its **splitting field**. Splitting fields are the normal extensions, and they are the fields on which the Galois theory operates. Taking the union of all such constructions over a field produces its **algebraic closure**, the field in which every nonconstant polynomial has a root and which is the natural ambient object for the study of extensions.

Two hypotheses control how well extensions behave. An irreducible polynomial may fail to have distinct roots, and a field in which this never happens is **perfect**; the failure is visible only in prime characteristic, and it is exactly the failure of the Frobenius map to be surjective. The second hypothesis is separability, and it is what makes a finite extension simple and what makes the counting of embeddings into an algebraic closure exact.

This article constructs splitting fields and algebraic closures, proves their uniqueness, and develops separability and perfectness. Throughout, $F$ is a field, $\overline{F}$ denotes an algebraic closure when it exists, and the notation for degrees, minimal polynomials and extensions is that of *Field Extensions*. The characteristic of $F$ is denoted $\operatorname{char} F$; the cases $\operatorname{char} F = 0$ and $\operatorname{char} F = p$ are separated throughout.

---

## Splitting Fields

### Definition

**Definition.** Let $f \in F[x]$ be a nonconstant polynomial. A **splitting field** of $f$ over $F$ is an extension $K \supseteq F$ such that

**(a)** $f$ factors into linear factors in $K[x]$,
$$
f = c\,(x - \alpha_1)(x - \alpha_2) \cdots (x - \alpha_n), \qquad c \in F^\times,
$$

**(b)** $K = F(\alpha_1, \ldots, \alpha_n)$ is generated over $F$ by the roots.

More generally, a field $K \supseteq F$ is a **splitting field** of a family $\{f_i\}$ of polynomials over $F$ if every $f_i$ splits in $K[x]$ and $K$ is generated over $F$ by all the roots.

Condition (b) is a minimality condition: it says that no proper subfield of $K$ containing $F$ already contains all the roots.

### Examples

**(a)** The splitting field of $x^2 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt2)$, of degree $2$.

**(b)** The splitting field of $x^2 + 1$ over $\mathbb{R}$ is $\mathbb{C} = \mathbb{R}(i)$, of degree $2$.

**(c)** The splitting field of $x^3 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$, of degree $6$: the polynomial is irreducible by Eisenstein, so adjoining a root gives degree $3$, and the remaining factor $x^2 + \sqrt[3]{2}\,x + \sqrt[3]{4}$ has discriminant $-3\sqrt[3]{4}$, which is negative and therefore not a square in the real field $\mathbb{Q}(\sqrt[3]{2})$; the quadratic is thus irreducible over that field and the second step contributes degree $2$. The tower law gives $[K:\mathbb{Q}] = 6$.

**(d)** The splitting field of $x^n - 1$ over $\mathbb{Q}$ is the cyclotomic field $\mathbb{Q}(\zeta_n)$.

**(e)** The splitting field of $x^q - x$ over $\mathbb{F}_p$, where $q = p^m$, is the field $\mathbb{F}_q$.

### Existence

**Theorem.** Every nonconstant $f \in F[x]$ has a splitting field over $F$.

**Proof.** Induct on $n = \deg f$. For $n = 1$ take $K = F$. For $n > 1$, let $p$ be a monic irreducible factor of $f$ and put $F_1 = F[x]/(p)$. Since $p$ is irreducible, $F_1$ is a field in which the class of $x$ is a root $\alpha_1$ of $p$ and hence of $f$. Write $f = (x - \alpha_1) g$ with $g \in F_1[x]$ of degree $n - 1$. By induction $g$ has a splitting field $K$ over $F_1$; then $K$ splits $f$ into linear factors. Replacing $K$ by the subfield generated over $F$ by the roots of $f$ (which is closed under the operations, hence a field) gives a splitting field as defined. $\square$

The same argument applies to a finite family of polynomials, adjoining roots of the irreducible factors one at a time; and a family of arbitrary cardinality is handled by taking a maximal subfamily each finite part of which has a splitting field, a Zorn argument that is used again for the algebraic closure.

**Corollary (degree bound).** If $\deg f = n$, then $[K:F] \leq n!$ for any splitting field $K$ of $f$ over $F$.

**Proof.** In the induction above, $[F_1:F] = \deg p \leq n$ and $g$ has degree $n-1$, so the bound is $[K:F] \leq n \cdot (n-1)! = n!$. $\square$

### Uniqueness

**Theorem.** Let $\varphi : F \to F'$ be an isomorphism of fields, let $f \in F[x]$ be nonconstant with image $\varphi(f) \in F'[x]$, and let $K$ and $K'$ be splitting fields of $f$ and $\varphi(f)$. Then $\varphi$ extends to an isomorphism $K \to K'$.

**Proof sketch.** Factor $f = p_1 \cdots p_r$ into irreducibles, so $\varphi(f) = \varphi(p_1) \cdots \varphi(p_r)$. Choose a root $\alpha \in K$ of $p_1$ and a root $\alpha' \in K'$ of $\varphi(p_1)$. The isomorphism $\varphi$ extends to $F(\alpha) \to F'(\alpha')$ by sending $\alpha$ to $\alpha'$, since both simple extensions are isomorphic to the quotient by the respective irreducible polynomial. Removing the factor $x - \alpha$ from $f$ over $F(\alpha)$ and repeating the argument, one extends step by step to all the roots; the resulting isomorphism between the subfields generated by the roots is the required one. $\square$

**Corollary.** Any two splitting fields of $f$ over $F$ are isomorphic by an isomorphism fixing $F$ pointwise. In particular the degree $[K:F]$ is independent of the choice of splitting field.

This is why one speaks of *the* splitting field of a polynomial, up to $F$-isomorphism.

---

## Normal Extensions

### Definition and Equivalent Conditions

**Definition.** An algebraic extension $K/F$ is **normal** if every irreducible polynomial $p \in F[x]$ that has a root in $K$ splits into linear factors in $K[x]$.

**Theorem.** An algebraic extension $K/F$ is normal if and only if $K$ is the splitting field over $F$ of a family of polynomials in $F[x]$.

**Proof.** If $K/F$ is normal, take the family of minimal polynomials over $F$ of the elements of $K$; each has a root in $K$ and therefore splits in $K$, and $K$ is generated by the roots of these polynomials, since each element of $K$ is a root of its own minimal polynomial.

Conversely, suppose $K$ is the splitting field over $F$ of a family $\{f_i\}$, let $p \in F[x]$ be irreducible with a root $\alpha \in K$, and let $\beta$ be a root of $p$ in an algebraic closure $\overline{F}$ containing $K$. The simple extensions $F(\alpha)$ and $F(\beta)$ are isomorphic over $F$, both being isomorphic to $F[x]/(p)$; fix $\tau : F(\alpha) \to F(\beta)$ with $\tau(\alpha) = \beta$. The element $\alpha$ lies in the splitting field over $F$ of finitely many members of the family, say $f_1, \ldots, f_m$: write $g = f_1 \cdots f_m$ and $N = F(\text{roots of } g) \subseteq K$. Then $N$ is the splitting field of $g$ over $F(\alpha)$, and $N(\beta)$ is the splitting field of $g$ over $F(\beta)$; by the uniqueness theorem for splitting fields applied to the isomorphism $\tau$, the map $\tau$ extends to an isomorphism
$$
\sigma : N \longrightarrow N(\beta), \qquad \sigma\vert_{F(\alpha)} = \tau .
$$
Now $\sigma$ carries the root set of $g$ into itself: if $\gamma \in N$ satisfies $g(\gamma) = 0$, then $0 = \sigma(g(\gamma)) = g(\sigma(\gamma))$, because the coefficients of $g$ lie in $F$ and are fixed by $\sigma$. Hence $\sigma(N) = F(\sigma(\text{roots of } g)) \subseteq F(\text{roots of } g) = N$, and since $\sigma$ is injective and $[N:F] = [\sigma(N):F]$ is finite, $\sigma(N) = N$. Therefore $\beta = \tau(\alpha) = \sigma(\alpha) \in \sigma(N) = N \subseteq K$. So every irreducible polynomial over $F$ with a root in $K$ splits in $K$, and $K/F$ is normal. $\square$

**Corollary.** A finite extension is normal if and only if it is the splitting field of a single polynomial over $F$: take the product of the minimal polynomials of a finite generating set.

### Normal Closure

**Definition.** Let $K/F$ be a finite extension. A **normal closure** of $K$ over $F$ is a normal extension $N/F$ containing $K$ that is minimal with this property.

**Theorem.** Every finite extension $K/F$ has a normal closure, and it is unique up to $K$-isomorphism; if $K = F(\alpha_1, \ldots, \alpha_n)$, the normal closure is the splitting field over $F$ of the product of the minimal polynomials $m_{\alpha_1} \cdots m_{\alpha_n}$.

**Proof.** Let $N$ be the splitting field over $F$ of $m = m_{\alpha_1} \cdots m_{\alpha_n}$. Then $N$ contains each $\alpha_i$, so $K \subseteq N$, and $N$ is normal by the theorem above. Any normal $M \supseteq K$ contains all conjugates of the $\alpha_i$, hence contains all roots of $m$, hence contains a splitting field of $m$ over $F$; so $N$ is minimal. Uniqueness is uniqueness of the splitting field. $\square$

**Example.** The normal closure of $\mathbb{Q}(\sqrt[3]{2})$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$, of degree $6$: it is already the splitting field of $x^3 - 2$.

---

## Separability

### Separable Polynomials

**Definition.** A nonconstant $f \in F[x]$ is **separable** if it has no repeated roots in a splitting field; equivalently, if the number of distinct roots of $f$ in a splitting field equals $\deg f$.

**Theorem (derivative criterion).** A nonconstant $f \in F[x]$ is separable if and only if $\gcd(f, f') = 1$, where $f'$ is the formal derivative of $f$. In particular an irreducible polynomial $f$ is inseparable if and only if $f' = 0$.

**Proof.** Let $K$ be a splitting field and write $f = c \prod_i (x - \alpha_i)^{e_i}$ with distinct $\alpha_i$. One computes $f'$ by the product rule. If some $e_i \geq 2$, then $x - \alpha_i$ divides both $f$ and $f'$, so $\gcd(f, f') \neq 1$ over $K[x]$ and hence over $F[x]$. Conversely if all $e_i = 1$ and $x - \alpha_i$ divided $f'$, then differentiating $f = c(x-\alpha_i) g$ gives $f'(\alpha_i) = g(\alpha_i)$; if $\alpha_i$ is not a repeated root then $g(\alpha_i) \neq 0$ (as $K$ is a field), so $f'(\alpha_i) \neq 0$ and $x - \alpha_i$ does not divide $f'$. Hence no root of $f$ is a root of $f'$ and $\gcd(f,f') = 1$. Finally an irreducible $f$ has a common factor with $f'$, which has smaller degree, only if $f' = 0$. $\square$

**Characteristic $p$.** In characteristic $p$ one has $f' = 0$ exactly when $f(x) = g(x^p)$ for some $g \in F[x]$: the derivative of $x^p$ is $p x^{p-1} = 0$, and the derivative of every power $x^{mp}$ vanishes, while powers $x^k$ with $p \nmid k$ have nonzero derivative. In characteristic $0$ an irreducible polynomial of positive degree always has $f' \neq 0$, so **every irreducible polynomial over a field of characteristic $0$ is separable**, and hence every algebraic extension of a field of characteristic $0$ is separable. Inseparability is therefore a prime-characteristic phenomenon.

### Separable Extensions

**Definition.** Let $K/F$ be an algebraic extension. An element $\alpha \in K$ is **separable over $F$** if its minimal polynomial $m_\alpha$ is separable, and $K/F$ is **separable** if every element of $K$ is separable over $F$. A finite extension that is not separable is **inseparable**; an extension is **purely inseparable** if every element outside $F$ has minimal polynomial $x^{p^e} - a$.

**Theorem.** Let $K/F$ be algebraic and let $\alpha, \beta \in K$. If $\alpha$ and $\beta$ are separable over $F$, then so are $\alpha + \beta$, $\alpha\beta$, and $\alpha/\beta$ when $\beta \neq 0$. Hence the separable elements of $K$ form an intermediate field $F_s$, the **separable closure of $F$ in $K$**.

**Proof sketch.** The extension $F(\alpha, \beta)$ is generated by two separable elements. By the counting theorem proved below, the number of $F$-embeddings of $F(\alpha)$ into $\overline{F}$ is $[F(\alpha):F]$; since $m_\beta$ remains separable over the field $F(\alpha)$, the number of extensions of each such embedding to $F(\alpha,\beta)$ is $[F(\alpha,\beta):F(\alpha)]$. Hence $F(\alpha,\beta)$ has $[F(\alpha):F][F(\alpha,\beta):F(\alpha)] = [F(\alpha,\beta):F]$ $F$-embeddings, so it is separable, and all its elements, including $\alpha \pm \beta$ and $\alpha\beta$, are separable. $\square$

**Theorem (counting embeddings).** Let $K/F$ be a finite extension and fix an algebraic closure $\overline{F} \supseteq K$. Write $\operatorname{Hom}_F(K, \overline{F})$ for the set of $F$-linear field homomorphisms $K \to \overline{F}$. Then

$$
\lvert \operatorname{Hom}_F(K, \overline{F}) \rvert \leq [K:F],
$$

with equality if and only if $K/F$ is separable.

**Proof sketch.** Write $K = F(\alpha_1, \ldots, \alpha_n)$ and put $K_i = F(\alpha_1, \ldots, \alpha_i)$, so $K_0 = F$ and $K_n = K$. An $F$-embedding of $K$ is determined by the images of the $\alpha_i$, and once $\sigma$ is fixed on $K_{i-1}$ the image $\sigma(\alpha_i)$ must be a root, in $\overline{F}$, of the minimal polynomial of $\alpha_i$ over $K_{i-1}$: a polynomial of degree $[K_i:K_{i-1}]$, with at most $[K_i:K_{i-1}]$ distinct roots, and with exactly that many when it is separable. Multiplying these bounds over $i$ and applying the tower law,

$$
\lvert \operatorname{Hom}_F(K, \overline{F}) \rvert \leq \prod_{i=1}^{n} [K_i : K_{i-1}] = [K:F],
$$

with equality exactly when each $\alpha_i$ is separable over $K_{i-1}$. If $K/F$ is separable then so is each $K_i/K_{i-1}$, so every factor is an equality and the count is $[K:F]$. Conversely, if $K/F$ is not separable, fix $\alpha \in K$ inseparable over $F$; then $\lvert \operatorname{Hom}_F(F(\alpha), \overline{F}) \rvert < [F(\alpha):F]$, while every $F$-embedding of $K$ restricts to one of $F(\alpha)$ and each such restriction has at most $[K:F(\alpha)]$ extensions, so

$$
\lvert \operatorname{Hom}_F(K, \overline{F}) \rvert \leq \lvert \operatorname{Hom}_F(F(\alpha), \overline{F}) \rvert \cdot [K:F(\alpha)] < [F(\alpha):F]\,[K:F(\alpha)] = [K:F].
$$

Hence the inequality is strict, and equality holds if and only if $K/F$ is separable. $\square$

**Corollary.** A finite extension $K/F$ is separable if and only if $\lvert \operatorname{Hom}_F(K, \overline{F}) \rvert = [K:F]$. A finite extension is Galois, in the sense, exactly when it is normal and separable.

---

## Perfect Fields

### Characterization

**Definition.** A field $F$ is **perfect** if every irreducible polynomial over $F$ is separable; equivalently, if every algebraic extension of $F$ is separable.

**Theorem.** A field $F$ is perfect if and only if $\operatorname{char} F = 0$, or $\operatorname{char} F = p$ and the Frobenius map $\varphi(x) = x^p$ is surjective.

**Proof.** If $\operatorname{char} F = 0$ then every irreducible polynomial has nonzero derivative, hence is separable. Let $\operatorname{char} F = p$ and suppose first that $\varphi$ is surjective. If $f$ is irreducible and inseparable, then $f' = 0$, so $f(x) = g(x^p)$; writing $g = \sum_i b_i x^i$ and $b_i = a_i^p$ by surjectivity, the freshman's dream (*Fields*, §3) gives $f(x) = \sum_i a_i^p x^{pi} = \left(\sum_i a_i x^i\right)^p$, contradicting irreducibility. Hence every irreducible is separable. Conversely if $\varphi$ is not surjective, choose $a \in F$ that is not a $p$-th power. The polynomial $x^p - a$ has derivative $p x^{p-1} = 0$, so it is inseparable; and it is irreducible: over a splitting field $x^p - a = (x - \alpha)^p$ with $\alpha^p = a$, so a factor of degree $k$ with $0 < k < p$ would be $(x-\alpha)^k$ up to a constant, with constant term $\pm\alpha^k \in F$; choosing integers $u, v$ with $uk + vp = 1$ gives $\alpha = (\alpha^k)^u (\alpha^p)^v \in F$ and hence $a = \alpha^p \in F^p$, a contradiction (the standard argument that $x^p - a$ is irreducible when $a \notin F^p$). Hence $F$ is not perfect. $\square$

### Examples

| Field $F$ | Characteristic | Perfect | Reason |
|---|---|---|---|
| $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | $0$ | yes | characteristic $0$ |
| any finite field $\mathbb{F}_q$ | $p$ | yes | Frobenius is injective, hence surjective, on a finite field |
| any algebraically closed field | any | yes | no irreducible polynomial of degree $> 1$ |
| $\overline{\mathbb{F}_p}$ | $p$ | yes | algebraically closed |
| $\mathbb{F}_p(t)$ | $p$ | no | $x^p - t$ is irreducible and inseparable |
| $\mathbb{F}_p(t_1, \ldots, t_n)$ | $p$ | no | same, with $x^p - t_1$ |

The non-example is worth recording concretely. In $F = \mathbb{F}_p(t)$ the polynomial $x^p - t$ has no root in $F$: if $(u/v)^p = t$ then $u^p = t v^p$, and comparing degrees in $t$ gives $p \deg u = 1 + p \deg v$, impossible. Hence $x^p - t$ is irreducible of degree $p$ over $F$, and if $\alpha$ is a root in an extension, then

$$
(x - \alpha)^p = x^p - \alpha^p = x^p - t,
$$

by the freshman's dream, so the single root $\alpha$ has multiplicity $p$ and the extension $F(\alpha)/F$ is purely inseparable of degree $p$. In particular $\alpha^p = t \in F$ while $\alpha \notin F$, so $\alpha$ is not separable over $F$, and the extension $F(\alpha)/F$ has no separating generator.

---

## The Primitive Element Theorem

### Statement and Proof

**Theorem (primitive element theorem).** Every finite separable extension $K/F$ is simple: there is $\alpha \in K$ with $K = F(\alpha)$.

**Proof sketch.** Suppose first that $F$ is finite. Then $K$ is a finite field, so $K^\times$ is cyclic; if $\alpha$ generates $K^\times$ then every nonzero element of $K$ is a power of $\alpha$, and $K = F(\alpha)$.

Assume now that $F$ is infinite. Since $K/F$ is separable, the number of $F$-embeddings $\sigma : K \to \overline{F}$ equals $[K:F]$. It suffices to find $\gamma \in K$ separated by these embeddings, that is, with $\sigma(\gamma) \neq \tau(\gamma)$ for all distinct $\sigma, \tau$: then the restrictions of the embeddings to $F(\gamma)$ are all distinct, so the separable field $F(\gamma)$ has at least $[K:F]$ $F$-embeddings, which forces $[F(\gamma):F] = [K:F]$ and hence $F(\gamma) = K$.

Consider first $K = F(\alpha, \beta)$ and, for $c \in F$, put $\gamma_c = \alpha + c\beta$. For distinct embeddings $\sigma \neq \tau$ the equality $\sigma(\gamma_c) = \tau(\gamma_c)$ is equivalent to
$$
\sigma(\alpha) - \tau(\alpha) = c\,\bigl(\tau(\beta) - \sigma(\beta)\bigr).
$$
If $\sigma(\beta) = \tau(\beta)$ then the equality would force $\sigma(\alpha) = \tau(\alpha)$, and an embedding of $K$ is determined by the images of $\alpha$ and $\beta$; so $\sigma = \tau$, contrary to hypothesis, and the equality fails for every $c$. If $\sigma(\beta) \neq \tau(\beta)$ then the equality determines at most one value of $c$, namely $\bigl(\sigma(\alpha) - \tau(\alpha)\bigr)/\bigl(\tau(\beta) - \sigma(\beta)\bigr)$. There are finitely many pairs $(\sigma, \tau)$ and hence finitely many forbidden values of $c$, while $F$ is infinite; choosing $c$ outside them gives a $\gamma_c$ that separates the embeddings, so $K = F(\gamma_c)$.

A finite extension is finitely generated, say $K = F(\alpha_1, \ldots, \alpha_m)$, and the general case follows by induction on $m$: if $F(\alpha_1, \ldots, \alpha_{m-1}) = F(\delta)$ by the inductive hypothesis, then $K = F(\delta, \alpha_m)$ is simple by the two-generator case just proved, the extension $K/F$ being separable. $\square$

**Corollary (finitely many intermediate fields).** A finite separable extension has only finitely many intermediate fields.

**Proof.** By the theorem $K = F(\alpha)$, with $n = [K:F] = \deg m_{\alpha/F}$. An intermediate field $E$ determines the minimal polynomial $m_{\alpha/E}$, a monic divisor of $m_{\alpha/F}$ in the polynomial ring over a splitting field $M \supseteq K$ of $m_{\alpha/F}$; distinct intermediate fields give distinct polynomials, because $E$ is generated over $F$ by the coefficients of $m_{\alpha/E}$. A polynomial of degree $n$, whose $n$ roots counted with multiplicity lie in $M$, has at most $2^n$ monic divisors there, so there are at most $2^n$ intermediate fields. $\square$

### Necessity of Separability

Separability cannot be dropped. Let $F = \mathbb{F}_p(x^p, y^p) \subseteq K = \mathbb{F}_p(x, y)$. Then $K = F(x, y)$, and $x, y$ have minimal polynomials $X^p - x^p = (X - x)^p$ and $Y^p - y^p = (Y - y)^p$ over $F$. Each of these is irreducible of degree $p$ over $F$ (the same argument as for $x^p - t$), so $[K:F] = p^2$. Every element of $K$ satisfies $\gamma^p \in F$: an element of $K = \mathbb{F}_p(x,y) = F(x,y)$ is a quotient $u(x,y)/v(x,y)$ of polynomials with coefficients in $\mathbb{F}_p$ and $v \neq 0$, and the freshman's dream gives
$$
\gamma^p = \frac{u(x,y)^p}{v(x,y)^p} = \frac{u(x^p, y^p)}{v(x^p, y^p)} \in \mathbb{F}_p(x^p, y^p) = F .
$$
Hence $\gamma$ is a root of $X^p - \gamma^p \in F[X]$, so $[F(\gamma):F] \leq p$ for every $\gamma$, while $[K:F] = p^2 > p$. No single element generates $K$, and $K/F$ is not simple.

---

## Algebraic Closure

### Definition and Equivalent Conditions

**Definition.** A field $K$ is **algebraically closed** if every nonconstant polynomial in $K[x]$ has a root in $K$. An **algebraic closure** of $F$ is an algebraic extension $\overline{F}/F$ with $\overline{F}$ algebraically closed.

**Theorem.** For a field $K$ the following are equivalent.

**(a)** $K$ is algebraically closed.

**(b)** Every nonconstant $f \in K[x]$ factors into linear factors in $K[x]$.

**(c)** The only irreducible polynomials in $K[x]$ are the linear ones.

**(d)** $K$ has no algebraic extension other than itself.

**Proof.** (a) $\Rightarrow$ (b): divide $f$ by $x - \alpha$ for a root $\alpha$ and iterate. (b) $\Rightarrow$ (c): an irreducible polynomial is constant or linear. (c) $\Rightarrow$ (a): a nonconstant $f$ has an irreducible factor, which is linear. (a) $\Leftrightarrow$ (d): if $K(\alpha)/K$ is algebraic and nontrivial, then $m_\alpha$ has no root in $K$; conversely, a rootless irreducible $p$ generates $K[x]/(p)$, an algebraic extension of $K$. $\square$

### Existence

**Theorem (Steinitz).** Every field $F$ has an algebraic closure.

**Proof sketch.** Write $\kappa = \max\{\aleph_0, \lvert F \rvert\}$. Every simple algebraic extension of $F$ has cardinality at most $\kappa$ and every algebraic extension of $F$ is a union of such, so it suffices to consider the algebraic extensions of $F$ of cardinality at most $\kappa$, which do form a set. Order that set by $F$-embedding; the union of a chain, taken in the direct limit along the embeddings, is again an algebraic extension of $F$ of cardinality at most $\kappa$, so Zorn's lemma gives a maximal element $E_0$. A proper algebraic extension of $E_0$ is generated by one further element and is therefore algebraic over $F$ and still of cardinality at most $\kappa$, and it would be strictly larger in the order; so $E_0$ has no proper algebraic extension and is algebraically closed by the equivalence above. Thus $E_0$ is an algebraic closure of $F$. $\square$

A more constructive route, used when $F$ is countable, is to enumerate the nonconstant polynomials $f_1, f_2, \ldots$ over $F$ and to take

$$
F = K_0 \subseteq K_1 \subseteq K_2 \subseteq \cdots, \qquad K_{i+1} = \text{splitting field of } f_i \text{ over } K_i, \qquad \overline{F} = \bigcup_i K_i.
$$

The union is a field because the $K_i$ form a chain, it is algebraic over $F$ by transitivity, and every $f_i$ splits in it; since the enumeration may be taken to include, at each stage, the polynomials over the intermediate fields, the resulting field is algebraically closed.

### Uniqueness

**Theorem.** Let $\varphi : F \to F'$ be an isomorphism of fields. If $\overline{F}$ and $\overline{F'}$ are algebraic closures, then $\varphi$ extends to an isomorphism $\overline{F} \to \overline{F'}$. In particular any two algebraic closures of $F$ are isomorphic by an isomorphism fixing $F$.

**Proof sketch.** Consider the set of pairs $(E, \sigma)$ with $F \subseteq E \subseteq \overline{F}$ and $\sigma : E \to \overline{F'}$ an $F$-homomorphism extending $\varphi$, partially ordered by extension. Zorn's lemma gives a maximal element $(E, \sigma)$; if $E \neq \overline{F}$, choose $\alpha \in \overline{F} \setminus E$ and extend $\sigma$ to $E(\alpha)$ by sending $\alpha$ to a root in $\overline{F'}$ of the image under $\sigma$ of $m_{\alpha/E}$, which exists because $\overline{F'}$ is algebraically closed. This contradicts maximality, so $E = \overline{F}$. The image $\sigma(\overline{F})$ is an algebraically closed algebraic extension of $F'$ inside $\overline{F'}$, hence equals $\overline{F'}$. $\square$

### Properties and Examples

**Proposition.** Let $\overline{F}$ be an algebraic closure of $F$.

**(a)** $\overline{F}$ contains a splitting field over $F$ of every nonconstant polynomial in $F[x]$.

**(b)** $\overline{F}$ is perfect.

**(c)** $\lvert \overline{F} \rvert = \max(\lvert F \rvert, \aleph_0)$.

**Proof.** (a) is the definition of algebraic closedness. (b) A field equal to its own algebraic closure is perfect, since its only irreducible polynomials are linear and hence separable. (c) Every element of $\overline{F}$ is a root of some nonzero polynomial over $F$, and the set $F[x]$ of such polynomials has cardinality $\max(\lvert F \rvert, \aleph_0)$, each polynomial having finitely many roots; hence $\lvert \overline{F} \rvert \leq \max(\lvert F \rvert, \aleph_0)$, while $\overline{F} \supseteq F$ gives the reverse inequality when $F$ is infinite and $F$ finite gives $\aleph_0$ from $\overline{\mathbb{F}_p} = \bigcup_n \mathbb{F}_{p^n}$. $\square$

**Examples.**

**(a)** $\mathbb{C}$ is an algebraic closure of $\mathbb{R}$: it is algebraically closed by the fundamental theorem of algebra and $\mathbb{C} = \mathbb{R}(i)$ is algebraic of degree $2$ over $\mathbb{R}$.

**(b)** $\overline{\mathbb{Q}}$, the field of algebraic numbers, is an algebraic closure of $\mathbb{Q}$: it is the union of the splitting fields of all polynomials over $\mathbb{Q}$, it is countable, and it is algebraically closed. Note that $\mathbb{C}$ is **not** an algebraic closure of $\mathbb{Q}$, because $\mathbb{C}/\mathbb{Q}$ is transcendental; it contains $\overline{\mathbb{Q}}$ as its algebraic part.

**(c)** $\overline{\mathbb{F}_p} = \bigcup_{n \geq 1} \mathbb{F}_{p^n}$ is an algebraic closure of $\mathbb{F}_p$: each $\mathbb{F}_{p^n}$ is the splitting field of $x^{p^n} - x$, the union is a field, and every polynomial over $\mathbb{F}_p$ splits in some finite field. It is countably infinite.

**(d)** If $\operatorname{char} F = p$ then $\overline{F}$ is perfect and contains $\mathbb{F}_p$; if $\operatorname{char} F = 0$ then $\overline{F}$ contains $\mathbb{Q}$.

**Remark.** Every field embeds into an algebraically closed field, namely its algebraic closure, and every algebraically closed field is infinite. The algebraic closure is the smallest algebraically closed extension in the sense that it is algebraic: any algebraically closed extension of $F$ contains a copy of $\overline{F}$. The model-theoretic properties of algebraic closures, and the classification of algebraically closed fields by characteristic and transcendence degree, belong.

---

## Summary

A splitting field of a nonconstant $f \in F[x]$ is the smallest extension in which $f$ factors into linear factors; it exists, by adjoining roots one irreducible factor at a time, has degree at most $n!$ when $\deg f = n$, and is unique up to an isomorphism fixing $F$. An algebraic extension is normal exactly when it is the splitting field of a family of polynomials, and every finite extension has a normal closure, obtained as the splitting field of the product of the minimal polynomials of a generating set.

A polynomial is separable when it has no repeated roots, equivalently when $\gcd(f, f') = 1$; an irreducible polynomial is inseparable exactly when its derivative vanishes, which happens only in characteristic $p$ and only for polynomials in $x^p$. A finite extension $K/F$ is separable exactly when the number of $F$-embeddings $K \to \overline{F}$ equals $[K:F]$, and a field is perfect exactly when it has characteristic $0$ or characteristic $p$ with surjective Frobenius. Every finite separable extension is simple, and every finite separable extension has finitely many intermediate fields.

An algebraic closure of $F$ is an algebraically closed algebraic extension; it exists by Zorn's lemma, is unique up to an isomorphism fixing $F$, contains the splitting field of every polynomial over $F$, and is perfect. The standard examples are $\overline{\mathbb{R}} = \mathbb{C}$, $\overline{\mathbb{Q}} = $ the algebraic numbers, and $\overline{\mathbb{F}_p} = \bigcup_n \mathbb{F}_{p^n}$; $\mathbb{C}$ is not an algebraic closure of $\mathbb{Q}$ because that extension is transcendental.

| Extension | Normal | Separable | Galois |
|---|---|---|---|
| $\mathbb{Q}(\sqrt2)/\mathbb{Q}$ | yes | yes | yes |
| $\mathbb{C}/\mathbb{R}$ | yes | yes | yes |
| $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ | no | yes | no |
| $\mathbb{F}_{p^n}/\mathbb{F}_p$ | yes | yes | yes |
| $\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)$ | yes | no | no |
| $\mathbb{F}_p(x,y)/\mathbb{F}_p(x^p,y^p)$ | yes | no | no |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $K$, $L$ | Fields; $F \subseteq K$ an extension |
| $\overline{F}$ | Algebraic closure of $F$ |
| $F(\alpha_1, \ldots, \alpha_n)$ | Smallest subfield containing $F$ and the $\alpha_i$ |
| $[K:F]$ | Degree, $\dim_F K$ |
| $\operatorname{char} F$ | Characteristic of the field $F$ |
| $m_\alpha$ | Minimal polynomial of $\alpha$ over $F$ |
| $f'$ | Formal derivative of $f$ |
| $\gcd(f, f')$ | Separability criterion |
| $\varphi(x) = x^p$ | Frobenius map, $F$ of characteristic $p$ |
| $\operatorname{Hom}_F(K, \overline{F})$ | $F$-embeddings of $K$ into $\overline{F}$ |
| $F_s$ | Separable closure of $F$ in $K$ |
| $\zeta_n$ | Primitive $n$-th root of unity |
| $\mathbb{F}_p$, $\mathbb{F}_{p^n}$ | Finite fields |
| $\overline{\mathbb{Q}}$ | Algebraic numbers |
| $\varphi : F \to F'$ | Isomorphism of fields, extended to splitting fields and closures |





## Further Reading

- Emil Artin, *Galois Theory* (Dover, 2nd ed. 1998), for normal extensions, the normal closure and the counting of embeddings.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the Steinitz theory of algebraic closures and perfect fields.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for splitting fields, separability and the primitive element theorem in full detail.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the uniqueness of algebraic closures and inseparable extensions.
- Rudolf Lidl and Harald Niederreiter, *Finite Fields* (Cambridge University Press, 2nd ed. 1997), for perfectness of finite fields and the structure of $\overline{\mathbb{F}_p}$.
- Bartel Leendert van der Waerden, *Algebra* (Springer, 1991), for the classical construction of the algebraic closure by adjoining roots.
