# __Kummer Theory__

## Introduction

A radical extension is obtained by adjoining $n$-th roots, and the question Kummer theory answers is which extensions arise this way and how their Galois groups look. If the base field $K$ contains a primitive $n$-th root of unity and $n$ is invertible in $K$, the answer is exact and elementary: the abelian extensions of $K$ of exponent dividing $n$ correspond bijectively to the subgroups of $K^\times$ that contain the $n$-th powers, the extension attached to a subgroup $\Delta$ being $K(\Delta^{1/n})$, and its Galois group being the group of homomorphisms $\Delta/(K^\times)^n \to \mu_n$. The correspondence is reversed by the rule that sends an element $a \in K^\times$ to the extension in which $x^n - a$ acquires a root.

The hypothesis that the roots of unity already lie in the base cannot be dropped. Over $\mathbb{Q}$ the extension $\mathbb{Q}(\sqrt[3]{2})$ is not normal and is not governed by Kummer theory, because $\mathbb{Q}$ contains no primitive cube root of unity; over $\mathbb{Q}(\zeta_3)$ the same extension is cyclic of degree $3$ and is governed by it. This is why Kummer theory is applied after adjoining the appropriate roots of unity, and why it is the tool that turns the solvability of a polynomial by radicals into a statement about abelian extensions.

This article develops the notion of a Kummer extension, proves the main theorem together with the Kummer pairing, computes the quadratic, cubic and quartic cases, and relates the theory to the solvability of equations by radicals and to the cyclotomic fields of *Cyclotomic Fields*. Throughout, $K$ is a field, $n \geq 1$ an integer with $\operatorname{char} K \nmid n$, and $\mu_n = \mu_n(K)$ is the group of $n$-th roots of unity in $K$, which is cyclic of order $n$ exactly when it is nontrivial. Field extensions, normality and separability are from *Field Extensions* and *Splitting Fields and Algebraic Closure*; the Galois correspondence and the theorem on solvability by radicals are from *Galois Theory*; the arithmetic of $\mathbb{Q}(\zeta_n)$ and the irreducibility of $\Phi_n$ are from *Cyclotomic Fields*; and finite fields, together with the cyclicity of their multiplicative groups, are from *Finite Fields*. The cohomological formulation of the main theorem is stated at the end and proved.

---

## Kummer Extensions

### The Kummer Condition

**Definition.** Let $n \geq 1$. A field extension $L/K$ is a **Kummer extension** of exponent $n$ if

**(K1)** $K$ contains a primitive $n$-th root of unity $\zeta$;

**(K2)** $L/K$ is Galois with group $\operatorname{Gal}(L/K)$ abelian of exponent dividing $n$;

**(K3)** $L = K(\Delta^{1/n})$ for some subgroup $\Delta \subseteq K^\times$ containing $(K^\times)^n$, where $\Delta^{1/n} = \{a^{1/n} : a \in \Delta\}$ in an algebraic closure of $K$.

Conditions (K1) and (K2) are the structural ones, and they are taken as the definition of a Kummer extension in the strict sense; condition (K3) is a consequence, and it is the content of the main theorem that it is equivalent to them. In practice an extension is called Kummer when it satisfies (K1) and (K2), and the theorem below produces the subgroup $\Delta$.

**Remark.** Let $\zeta \in K$ be primitive of order $n$ and let $a \in K^\times$ with $a \notin (K^\times)^n$. Let $L = K(\alpha)$ where $\alpha^n = a$. Then

$$
\alpha, \zeta\alpha, \zeta^2\alpha, \ldots, \zeta^{n-1}\alpha
$$

are the $n$ distinct roots of $x^n - a$ in $L$, so $L$ is the splitting field of the separable polynomial $x^n - a$ and $L/K$ is Galois. For each $\sigma \in \operatorname{Gal}(L/K)$ the element $\alpha$ is sent to another root of $x^n - a$, so

$$
\sigma(\alpha) = \zeta^{i(\sigma)} \alpha \quad \text{for a unique } i(\sigma) \in \mathbb{Z}/n\mathbb{Z},
$$

and $\sigma \mapsto i(\sigma)$ is a homomorphism $\operatorname{Gal}(L/K) \to \mathbb{Z}/n\mathbb{Z}$ whose kernel is trivial, because an automorphism fixing $\alpha$ fixes $L = K(\alpha)$. Hence $\operatorname{Gal}(L/K)$ is cyclic of order dividing $n$, and if $a$ is not an $n$-th power it is cyclic of order exactly $n$. This single computation is the whole of the Kummer condition, and the main theorem assembles it over a subgroup of $K^\times$.

**Lemma.** Let $K$ contain $\zeta$, primitive of order $n$, let $a_1, \ldots, a_r \in K^\times$ and let $\alpha_i$ with $\alpha_i^n = a_i$. Suppose that

$$
\prod_{i=1}^{r} a_i^{m_i} \in (K^\times)^n \quad \text{implies} \quad n \mid m_i \text{ for all } i,
$$

that is, the classes of the $a_i$ in $K^\times/(K^\times)^n$ are independent in the sense of abelian groups. Then $[K(\alpha_1, \ldots, \alpha_r) : K] = n^r$.

**Proof.** By induction on $r$. The case $r = 0$ is trivial. Let $L = K(\alpha_1, \ldots, \alpha_{r-1})$; by induction $[L:K] = n^{r-1}$. It suffices to show that $L(\alpha_r)/L$ has degree $n$, and by the remark above this fails only if $\alpha_r \in L$. Suppose $\alpha_r \in L$; then $x^n - a_r$ has a root in $L$, and the group $\operatorname{Gal}(L/K)$ acts. Since $L/K$ is Galois, $\operatorname{Gal}(L/K)$ is elementary abelian of exponent $n$ — it is a subgroup of $(\mathbb{Z}/n\mathbb{Z})^{r-1}$ — so for $\sigma$ and $\tau$ in the group one has the relation described below. Explicitly, for each $\sigma \in G = \operatorname{Gal}(L/K)$ choose $j_i(\sigma)$ with $\sigma(\alpha_i) = \zeta^{j_i(\sigma)}\alpha_i$, so that $\sigma \mapsto (j_1(\sigma), \ldots, j_{r-1}(\sigma))$ embeds $G$ into $(\mathbb{Z}/n\mathbb{Z})^{r-1}$. If $\alpha_r \in L$ then $\sigma(\alpha_r) = \zeta^{j_r(\sigma)}\alpha_r$ for some $j_r(\sigma)$, and $\sigma \mapsto j_r(\sigma)$ is a homomorphism $G \to \mathbb{Z}/n\mathbb{Z}$. By the elementary theory of elementary abelian groups, such a homomorphism is a linear combination of the coordinate homomorphisms: there are $m_1, \ldots, m_{r-1} \in \mathbb{Z}$ with $j_r(\sigma) = \sum_i m_i j_i(\sigma)$ for all $\sigma$. Define

$$
\beta = \alpha_r \prod_{i=1}^{r-1} \alpha_i^{-m_i} \in L^\times .
$$

Then for every $\sigma \in G$,

$$
\sigma(\beta) = \zeta^{j_r(\sigma) - \sum_i m_i j_i(\sigma)}\beta = \beta,
$$

so $\beta \in L^G = K$. Taking $n$-th powers, $\beta^n = a_r \prod_i a_i^{-n m_i} \cdot (\text{a product of } n\text{-th powers})$: precisely,

$$
\beta^n = a_r \prod_{i=1}^{r-1} a_i^{-m_i n} \in a_r \cdot (K^\times)^n .
$$

Since $\beta^n \in (K^\times)^n$ and $\beta^n = a_r \cdot c^n$ for some $c \in K^\times$, we get $a_r = (\beta/c)^n \in (K^\times)^n$; equivalently $a_r \prod_{i} a_i^{0} \in (K^\times)^n$ with all exponents except that of $a_r$ equal to $0$ and $m_r = 1$ not divisible by $n$, contradicting the independence hypothesis. Hence $\alpha_r \notin L$ and $[L(\alpha_r):L] = n$. $\square$

**Theorem (Kummer, first form).** Let $\zeta \in K$ be primitive of order $n$, let $\Delta \subseteq K^\times$ be a subgroup containing $(K^\times)^n$, and let

$$
L = K\bigl(\Delta^{1/n}\bigr).
$$

Then $L/K$ is abelian of exponent dividing $n$, and if $\Delta/(K^\times)^n$ is finite of order $n^r$ then $[L:K] = n^r = \lvert \Delta/(K^\times)^n\rvert$.

**Proof.** Choose representatives $a_1, \ldots, a_r$ of a basis of the finite group $\Delta/(K^\times)^n$; then $\Delta/(K^\times)^n$ is the direct sum of the classes of the $a_i$ and every element of $\Delta$ differs from a product $\prod a_i^{m_i}$ by an $n$-th power, so $L = K(\alpha_1, \ldots, \alpha_r)$ with $\alpha_i^n = a_i$. The independence hypothesis of the lemma holds by the definition of a direct sum in $K^\times/(K^\times)^n$, so $[L:K] = n^r$. The field $L$ is the splitting field of $\prod_i (x^n - a_i)$, hence normal over $K$ and separable since $\operatorname{char} K \nmid n$; each $\sigma \in \operatorname{Gal}(L/K)$ is determined by the tuple $(j_1(\sigma), \ldots, j_r(\sigma)) \in (\mathbb{Z}/n\mathbb{Z})^r$ with $\sigma(\alpha_i) = \zeta^{j_i(\sigma)}\alpha_i$, and the resulting map $\operatorname{Gal}(L/K) \hookrightarrow (\mathbb{Z}/n\mathbb{Z})^r$ is injective because the $\alpha_i$ generate $L$. Comparing orders, $[L:K] = \lvert\operatorname{Gal}(L/K)\rvert \leq n^r = [L:K]$, so the inclusion is an isomorphism and $\operatorname{Gal}(L/K) \cong (\mathbb{Z}/n\mathbb{Z})^r$; in particular the extension is abelian of exponent dividing $n$. $\square$

**Example.** $n = 2$ and any field $K$ of characteristic $\neq 2$: $\zeta = -1 \in K$ always, so the Kummer condition is automatic and the theory of exponent $2$ applies to every field of characteristic not $2$. The extensions are the multiquadratic ones $K(\sqrt{a_1}, \ldots, \sqrt{a_r})$, and $\operatorname{Gal}(L/K) \cong (\mathbb{Z}/2\mathbb{Z})^r$.

**Example.** Let $K = \mathbb{Q}(\zeta_3) = \mathbb{Q}(\sqrt{-3})$ and $n = 3$. The Kummer condition holds. The extension $K(\sqrt[3]{2})/K$ has degree $3$: if $2 = u^3$ for some $u \in K^\times$ then taking the field norm gives $4 = \operatorname{N}_{K/\mathbb{Q}}(2) = \operatorname{N}_{K/\mathbb{Q}}(u)^3$, and $4$ is not a cube in $\mathbb{Z}$. So the class of $2$ in $K^\times/(K^\times)^3$ is nontrivial and generates a subgroup of order $3$, giving the cyclic cubic extension $K(\sqrt[3]{2})/K$. Over $\mathbb{Q}$ itself the same element gives the extension $\mathbb{Q}(\sqrt[3]{2})$, of degree $3$ but not normal; the Galois closure is $\mathbb{Q}(\sqrt[3]{2},\zeta_3)$, of degree $6$ over $\mathbb{Q}$ with group $S_3$.

**Example ($\mathbb{Q}(\zeta_9)/\mathbb{Q}(\zeta_3)$).** Take $K = \mathbb{Q}(\zeta_3)$, $n = 3$ and $a = \zeta_3$. Since $\zeta_9^3 = \zeta_3$, the field $K(\sqrt[3]{\zeta_3})$ contains $\zeta_9$; it has degree $3$ over $K$ because $\varphi(9) = 6$ and $\varphi(3) = 2$ with $K = \mathbb{Q}(\zeta_3) \subseteq \mathbb{Q}(\zeta_9)$, so $[\mathbb{Q}(\zeta_9):\mathbb{Q}(\zeta_3)] = 3$. Hence $\mathbb{Q}(\zeta_9)/\mathbb{Q}(\zeta_3)$ is a cyclic Kummer extension, and iterating, $\mathbb{Q}(\zeta_{3^v})/\mathbb{Q}(\zeta_{3^{v-1}})$ is cyclic of degree $3$ for every $v \geq 2$ by the degree formula $\varphi(3^v)/\varphi(3^{v-1}) = 3$.

---

## The Main Theorem

### Statement

**Theorem (Kummer theory).** Let $K$ contain a primitive $n$-th root of unity $\zeta$ and let $\operatorname{char} K \nmid n$. The maps

$$
\Delta \longmapsto K\bigl(\Delta^{1/n}\bigr), \qquad L \longmapsto \Delta_L = (L^\times)^n \cap K^\times
$$

are mutually inverse bijections between

**(i)** the subgroups $\Delta \subseteq K^\times$ with $(K^\times)^n \subseteq \Delta$ and $\Delta/(K^\times)^n$ of finite exponent dividing $n$, equivalently the subgroups of $K^\times/(K^\times)^n$; and

**(ii)** the finite abelian extensions $L/K$ of exponent dividing $n$.

For the corresponding pair $(\Delta, L)$ there is a perfect pairing of finite abelian groups

$$
\Delta/(K^\times)^n \times \operatorname{Gal}(L/K) \longrightarrow \mu_n, \qquad (a, \sigma) \longmapsto \frac{\sigma(\alpha)}{\alpha},
$$

where $\alpha \in L^\times$ satisfies $\alpha^n = a$; the pairing is **the Kummer pairing**. It is additive in each variable, well defined, and non-degenerate on each side, and it induces an isomorphism

$$
\operatorname{Gal}(L/K) \;\cong\; \operatorname{Hom}\bigl(\Delta/(K^\times)^n,\ \mu_n\bigr),
$$

which is an isomorphism of finite abelian groups of exponent dividing $n$.

**Remark.** The definition $\Delta_L = (L^\times)^n \cap K^\times$ is forced: if $L = K(\Delta^{1/n})$ then every $a \in \Delta$ has an $n$-th root in $L$, so $\Delta \subseteq (L^\times)^n \cap K^\times$; and conversely an element $a \in K^\times$ with an $n$-th root $\alpha \in L$ must lie in the subgroup generated by the $a_i$ up to $n$-th powers, by the main theorem applied to the subgroup generated by $\Delta$ and $a$.

### Proof of the Main Theorem

**Step 1: the pairing is well defined.** Let $a \in \Delta$ and $\sigma \in \operatorname{Gal}(L/K)$, and choose $\alpha \in L^\times$ with $\alpha^n = a$. Then $\sigma(\alpha)^n = \sigma(a) = a = \alpha^n$, so $\sigma(\alpha)/\alpha$ is an $n$-th root of unity, hence lies in $\mu_n \subseteq K$. If $\alpha$ is replaced by $\zeta^j\alpha$, the quotient $\sigma(\zeta^j\alpha)/(\zeta^j\alpha) = \sigma(\alpha)/\alpha$ is unchanged since $\zeta \in K$ is fixed by $\sigma$. If $a$ is replaced by $a c^n$ with $c \in K^\times$, the root may be taken to be $\alpha c$, and the quotient is again unchanged. So the pairing is well defined on $\Delta/(K^\times)^n \times \operatorname{Gal}(L/K)$.

**Step 2: additivity in each variable.** $\sigma(\alpha)/\alpha$ depends multiplicatively on $\alpha$, hence additively on the class of $a$; and for $\sigma, \tau$ one has $(\sigma\tau)(\alpha)/\alpha = \sigma(\tau(\alpha)/\alpha) \cdot \sigma(\alpha)/\alpha = \tau(\alpha)/\alpha \cdot \sigma(\alpha)/\alpha$, since $\tau(\alpha)/\alpha \in \mu_n \subseteq K$ is fixed by $\sigma$. Thus the pairing is additive in each variable, hence a pairing of $\mathbb{Z}/n\mathbb{Z}$-modules.

**Step 3: non-degeneracy in the second variable.** Suppose $\sigma$ pairs trivially with every $a \in \Delta$. Then $\sigma(\alpha)/\alpha = 1$ for every generator $\alpha = \alpha_i$ of $L$ over $K$, so $\sigma$ fixes each $\alpha_i$ and hence fixes $L$, so $\sigma = 1$.

**Step 4: non-degeneracy in the first variable.** Let $a \in \Delta$ and suppose $\sigma(\alpha)/\alpha = 1$ for every $\sigma$, where $\alpha^n = a$. Then $\alpha$ is fixed by $\operatorname{Gal}(L/K)$, so $\alpha \in L^{\operatorname{Gal}(L/K)} = K$ by the fundamental theorem of Galois theory applied to the Galois extension $L/K$; hence $a = \alpha^n \in (K^\times)^n$, so the class of $a$ is trivial in $\Delta/(K^\times)^n$.

**Step 5: the induced map is an isomorphism.** By Steps 3 and 4 the pairing is non-degenerate, so it induces injections $\Delta/(K^\times)^n \hookrightarrow \operatorname{Hom}(\operatorname{Gal}(L/K),\mu_n)$ and $\operatorname{Gal}(L/K) \hookrightarrow \operatorname{Hom}(\Delta/(K^\times)^n, \mu_n)$, the second of which is the displayed isomorphism once the two sides have the same order. If $\Delta/(K^\times)^n$ has order $n^r$ then $\operatorname{Gal}(L/K) \cong (\mathbb{Z}/n\mathbb{Z})^r$ by the first form of the theorem, and $\operatorname{Hom}((\mathbb{Z}/n\mathbb{Z})^r, \mu_n)$ has order $n^r$, so the injection is an isomorphism. $\square$

**Step 6: the two maps are inverse.** Let $L/K$ be finite abelian of exponent dividing $n$ and put $\Delta = (L^\times)^n \cap K^\times$. Then $(K^\times)^n \subseteq \Delta$ and $M = K(\Delta^{1/n})$ is a subfield of $L$, so $M = L^H$ for some subgroup $H$ of $G = \operatorname{Gal}(L/K)$. Now let $\sigma \in H$ and $a \in \Delta$; choose $\alpha \in L^\times$ with $\alpha^n = a$. Since $a \in \Delta = (L^\times)^n \cap K^\times$ and $\Delta \subseteq (M^\times)^n$ by the definition of $M$, we may choose $\alpha \in M^\times$, so $\sigma(\alpha) = \alpha$ and the Kummer pairing pairs $(a,\sigma)$ to $1$. Thus $\sigma$ pairs trivially with every element of $\Delta$; by Step 3, $\sigma$ fixes every generator of $K(\Delta^{1/n})$, so $\sigma = 1$. Hence $H = 1$ and $M = L$. Conversely, let $L = K(\Delta^{1/n})$ for some subgroup $\Delta$ with $(K^\times)^n \subseteq \Delta \subseteq K^\times$ and $\Delta/(K^\times)^n$ finite of order $n^r$. Then $\Delta \subseteq (L^\times)^n\cap K^\times = \Delta_L$, and $K(\Delta_L^{1/n}) = L$ by the first part of this step, so

$$
n^r = [L:K] = \bigl[K(\Delta_L^{1/n}):K\bigr] = \lvert\Delta_L/(K^\times)^n\rvert \geq \lvert\Delta/(K^\times)^n\rvert = n^r,
$$

and the inclusion $\Delta \subseteq \Delta_L$ is therefore an equality. $\square$

### Consequences

**Corollary (Galois group and subgroup lattice).** With notation as in the theorem, the Galois group of $K(\Delta^{1/n})/K$ is the character group of $\Delta/(K^\times)^n$; the subgroups $\Delta'$ with $(K^\times)^n \subseteq \Delta' \subseteq \Delta$ correspond bijectively to the intermediate fields of $K(\Delta^{1/n})/K$, and

$$
\Delta' \longleftrightarrow K\bigl(\Delta'^{1/n}\bigr), \qquad \Delta' \longleftrightarrow \operatorname{Gal}\bigl(L/K(\Delta'^{1/n})\bigr)^{\perp},
$$

in the sense that the annihilator of $\Delta'/(K^\times)^n$ under the pairing is $\operatorname{Gal}(L/K(\Delta'^{1/n}))$. The correspondence reverses inclusions.

**Corollary (translation of the Galois correspondence).** Under the Kummer pairing, for subgroups $\Delta_1 \subseteq \Delta_2 \subseteq K^\times$ containing $(K^\times)^n$ of finite index,

$$
K\bigl(\Delta_1^{1/n}\bigr) \subseteq K\bigl(\Delta_2^{1/n}\bigr), \qquad
\bigl[K(\Delta_2^{1/n}) : K(\Delta_1^{1/n})\bigr] = \bigl[\Delta_2 : \Delta_1\bigr].
$$

**Corollary.** The maximal abelian extension of $K$ of exponent dividing $n$ is $K\bigl((K^\times)^{1/n}\bigr)$, the extension generated by all $n$-th roots of elements of $K^\times$. Its Galois group is the group of homomorphisms $K^\times/(K^\times)^n \to \mu_n$. The extension is finite exactly when $K^\times/(K^\times)^n$ is finite, which happens for finite fields , by the arithmetic, for fields of arithmetic type; over such a field $\operatorname{Hom}(K^\times/(K^\times)^n,\mu_n)$ is realised as a direct product of finite cyclic groups, and the group structure is the arithmetic input to the reciprocity laws. Both articles are.

**Example (finite fields).** Let $K = \mathbb{F}_q$ with $q \equiv 1 \pmod n$, so that $\mu_n \subseteq K$. The group $K^\times$ is cyclic of order $q-1$, so $K^\times/(K^\times)^n$ is cyclic of order $n$, and the unique Kummer extension of exponent $n$ is $K(\sqrt[n]{a})$ for a generator $a$ of $K^\times$, of degree $n$; it is the unique extension of $\mathbb{F}_q$ of degree $n$, namely $\mathbb{F}_{q^n}$. The Kummer pairing $\mu_n \times \operatorname{Gal}(\mathbb{F}_{q^n}/\mathbb{F}_q) \to \mu_n$ is the standard pairing of two cyclic groups of order $n$, and its non-degeneracy is the statement that the Frobenius acts on $\mu_n$ with a generator of $\operatorname{Gal}$.

---

## Examples

### The Quadratic Case

**Theorem.** Let $\operatorname{char} K \neq 2$. The $\mathbb{Z}/2$-vector space $K^\times/(K^\times)^2$, and equivalently the set of multiquadratic extensions of $K$, classifies the abelian extensions of $K$ of exponent $2$. In particular $\operatorname{Gal}(L/K) \cong (\mathbb{Z}/2\mathbb{Z})^r$ for $L = K(\sqrt{a_1}, \ldots, \sqrt{a_r})$ with the classes of the $a_i$ independent, and the pairing is the evaluation of characters of $\operatorname{Gal}(L/K)$ at the signs $\sigma(\alpha_i)/\alpha_i = \pm1$.

**Example.** Over $\mathbb{Q}$, $\mathbb{Q}^\times/(\mathbb{Q}^\times)^2$ is the $\mathbb{F}_2$-vector space with basis the classes of $-1$ and the primes; the subgroups of finite index correspond to the multiquadratic fields, and by the theorem of Kronecker that every quadratic extension is $\mathbb{Q}(\sqrt{d})$, the exponent-$2$ abelian extensions of $\mathbb{Q}$ are exactly the fields $\mathbb{Q}(\sqrt{d_1}, \ldots, \sqrt{d_r})$ with the square classes of the $d_i$ independent. The maximal such extension is $\mathbb{Q}^{\mathrm{ab},2}$, obtained by adjoining the square roots of all rational numbers.

**Example.** Over $K = \mathbb{Q}(\zeta_3)$ with $n = 2$, the exponent-$2$ Kummer extensions include $\mathbb{Q}(\zeta_3, \sqrt{-3}) = \mathbb{Q}(\zeta_3)$, which is trivial, and $K(i)$, of degree $2$; more interesting is $n = 3$, treated above.

### Cubic and Quartic Examples

**Example (cyclic cubic over $\mathbb{Q}(\zeta_3)$).** $K = \mathbb{Q}(\zeta_3)$ and $n = 3$. The classes of $2$ and $3$ in $K^\times/(K^\times)^3$ are independent. Indeed for each nontrivial pair $(i,j) \in (\mathbb{Z}/3\mathbb{Z})^2$ the norm $\operatorname{N}_{K/\mathbb{Q}}(2^i3^j) = (2^i3^j)^2$ takes one of the values $4, 9, 36, 144, 324, 1296$, none of which is a perfect cube in $\mathbb{Z}$; and if $2^i3^j$ were a cube $u^3$ in $K$ then its norm, being $\operatorname{N}(u)^3$, would be a cube. Hence the two classes are independent and $\operatorname{Gal}(K(\sqrt[3]{2},\sqrt[3]{3})/K) \cong (\mathbb{Z}/3\mathbb{Z})^2$. The same norm argument, applied to the norms $4$, $9$, $25$, shows that each of $K(\sqrt[3]{2})$, $K(\sqrt[3]{3})$, $K(\sqrt[3]{5})$ is cyclic cubic over $K$. The extension $K(\sqrt[3]{3})/K$ has ramification index $3$ at the prime $(1-\zeta_3)$ above $3$: from $1 + \zeta_3 + \zeta_3^2 = 0$ one computes $(1-\zeta_3)^2 = -3\zeta_3$, so $3$ is a unit multiple of $(1-\zeta_3)^2$ and the cube root of a uniformiser raises the ramification index by $3$.

**Example (cyclic quartic over $\mathbb{Q}(i)$).** $K = \mathbb{Q}(i)$ and $n = 4$, so $\zeta_4 = i \in K$. The extension $K(\sqrt[4]{2})/K$ has degree $4$: if $2 = u^4$ with $u \in K^\times$ then $\operatorname{N}_{K/\mathbb{Q}}(2) = 4 = \operatorname{N}(u)^4$, impossible in $\mathbb{Z}$. The group $\operatorname{Gal}(K(\sqrt[4]{2})/K)$ is cyclic of order $4$, generated by $\sigma$ with $\sigma(\sqrt[4]{2}) = i\sqrt[4]{2}$; the intermediate field is $K(\sqrt2)$, of degree $2$ over $K$, corresponding to the subgroup of squares $\langle 4\rangle \subseteq \langle 2\rangle$ in the class group $K^\times/(K^\times)^4$. Over $\mathbb{Q}$ the field $\mathbb{Q}(\sqrt[4]{2})$ is not normal, and its Galois closure $\mathbb{Q}(\sqrt[4]{2},i)$ has group the dihedral group of order $8$, so Kummer theory does not apply over the base $\mathbb{Q}$.

**Example (multiquadratic over $\mathbb{Q}$).** With $n = 2$, $K = \mathbb{Q}$ and $\Delta$ generated by $-1, 2, 3$, the extension $L = \mathbb{Q}(i, \sqrt2, \sqrt3)$ has degree $8$ over $\mathbb{Q}$ and group $(\mathbb{Z}/2\mathbb{Z})^3$. The Kummer pairing sends $(-1, \sigma)$ to $\sigma(i)/i = \pm1$ according to whether $\sigma$ fixes $i$, and similarly for the other generators; the perfectness of the pairing is the statement that the eight characters obtained this way separate the eight elements of the group.

### Cyclotomic Extensions

**Example.** Let $K = \mathbb{Q}(\zeta_n)$ with $n > 2$ and consider exponents $n$ and $2n$. The extension $\mathbb{Q}(\zeta_{n^2})/\mathbb{Q}(\zeta_n)$ has degree $n$ when $n$ is prime (indeed for $n = p$, $\varphi(p^2)/\varphi(p) = p$), and it is Kummer of exponent $n$: it is generated by an $n$-th root of $\zeta_n$, as in the example $\mathbb{Q}(\zeta_9)/\mathbb{Q}(\zeta_3)$ above.

**Remark.** Conversely, a Kummer extension of $\mathbb{Q}(\zeta_n)$ need not be cyclotomic, and Kummer theory alone does not determine which are; the decision is a matter of the ramification theory and the reciprocity law.

---

## Solvability by Radicals

### Radical Extensions

**Definition.** An extension $L/K$ is **radical** if there is a tower

$$
K = K_0 \subseteq K_1 \subseteq \cdots \subseteq K_m = L
$$

with $K_i = K_{i-1}(\alpha_i)$ and $\alpha_i^{n_i} \in K_{i-1}$ for some integers $n_i \geq 1$; equivalently, each step adjoins an $n_i$-th root of an element of the preceding field. A polynomial $f \in K[x]$ is **solvable by radicals** over $K$ if its splitting field is contained in a radical extension of $K$.

**Theorem (Galois).** Let $\operatorname{char} K = 0$ and let $f \in K[x]$. Then $f$ is solvable by radicals over $K$ if and only if its Galois group $G_f$ over $K$ is solvable.

This is the theorem of *Galois Theory*, and Kummer theory supplies its main input, as follows.

**Theorem (Kummer's contribution to solvability).** Let $\operatorname{char} K = 0$, let $L/K$ be a Galois extension with solvable group $G$, and let $n$ be the exponent of $G$. Let $K' = K(\zeta_n)$ and $L' = L K' = L(\zeta_n)$. Then $L'/K'$ is Galois with group isomorphic to a subgroup of $G$, hence solvable, and it admits a tower

$$
K' = M_0 \subseteq M_1 \subseteq \cdots \subseteq M_s = L'
$$

in which each $M_i/M_{i-1}$ is a Kummer extension of prime exponent $\ell_i$ dividing $n$.

**Proof sketch.** Since $G$ is solvable, it has a composition series with cyclic factors of prime order $\ell_i \mid n$. The corresponding tower of fixed fields consists of Galois extensions of prime degree $\ell_i$; after extending scalars from $K$ to $K'$, which contains the $\ell_i$-th roots of unity, each step of the tower is a Galois extension of prime degree $\ell_i$, and by the first form of the main theorem such an extension, being abelian of exponent $\ell_i$, is a Kummer extension $M_i = M_{i-1}(\sqrt[\ell_i]{a_i})$. $\square$

**Corollary.** Every solvable extension of a field of characteristic zero is contained in a radical extension; the converse — that a radical extension has solvable Galois group — is proved by adjoining the necessary roots of unity and applying the theorem to each Kummer step, so that the two statements together give the theorem of Galois.

### The Role of the Roots of Unity

**Example ($x^3 - 2$ over $\mathbb{Q}$).** The Galois group is $S_3$, solvable; the splitting field is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$, which is contained in the radical extension $\mathbb{Q}(\zeta_3, \sqrt[3]{2})$, the first step $\mathbb{Q}(\zeta_3)/\mathbb{Q}$ adjoining the third roots of unity — an extension of degree $2$, itself radical since $\zeta_3^2 + \zeta_3 + 1 = 0$ makes $\zeta_3 = (-1+\sqrt{-3})/2$ — and the second step adjoining $\sqrt[3]{2}$. The Kummer theorem applies to the second step over the base $\mathbb{Q}(\zeta_3)$; it does not apply to $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$, which is not even normal, which is exactly why the roots of unity must be adjoined first.

**Example ($x^5 - 2$ over $\mathbb{Q}$).** The Galois group is the Frobenius group of order $20$, solvable; the splitting field is contained in the radical extension obtained by adjoining $\zeta_5$ and $\sqrt[5]{2}$. The quintic $x^5 - x - 1$, by contrast, has group $S_5$, not solvable, and is not solvable by radicals; this is the classical theorem of Abel and Ruffini, and the computation of the group is the content of *Galois Theory*.

**Corollary.** A polynomial over a field of characteristic zero is solvable by radicals exactly when it is solvable by a tower of Kummer extensions after adjoining roots of unity, and for each prime $\ell$ the $\ell$-steps are governed by the groups $K^\times/(K^\times)^\ell$.

---

## Summary

Kummer theory applies to a field $K$ containing a primitive $n$-th root of unity with $n$ invertible in $K$. For $a \in K^\times$ and $\alpha^n = a$, the conjugates of $\alpha$ are the $\zeta^i\alpha$, so $K(\alpha)/K$ is cyclic of order $n$ when $a$ is not an $n$-th power and divides $n$ in general, and $\sigma \mapsto \sigma(\alpha)/\alpha$ is a homomorphism $\operatorname{Gal}(K(\alpha)/K) \to \mu_n$ with trivial kernel. For a subgroup $\Delta \subseteq K^\times$ containing $(K^\times)^n$, the field $K(\Delta^{1/n})$ is abelian of exponent dividing $n$ with group $(\mathbb{Z}/n\mathbb{Z})^r$ when $\Delta/(K^\times)^n$ has order $n^r$.

The main theorem is a bijection: subgroups of $K^\times/(K^\times)^n$ correspond to the finite abelian extensions of $K$ of exponent dividing $n$, by $\Delta \mapsto K(\Delta^{1/n})$ with inverse $L \mapsto (L^\times)^n \cap K^\times$. The bijection is realised by the Kummer pairing $\Delta/(K^\times)^n \times \operatorname{Gal}(L/K) \to \mu_n$, $(a,\sigma) \mapsto \sigma(\alpha)/\alpha$, which is additive in each variable and non-degenerate and gives $\operatorname{Gal}(L/K) \cong \operatorname{Hom}(\Delta/(K^\times)^n,\mu_n)$. The correspondence is compatible with the Galois correspondence: subgroups correspond to intermediate fields, inclusions reversing, and the degree of a quotient is the index of the corresponding subgroups.

Examples: the exponent-$2$ case is the theory of multiquadratic extensions and holds over any field of characteristic not $2$; over $\mathbb{Q}(\zeta_3)$ the element $2$ has no cube root, since the norm $4$ is not a cube, so $K(\sqrt[3]{2})/K$ is cyclic cubic; over $\mathbb{Q}(i)$ the extension $K(\sqrt[4]{2})/K$ is cyclic quartic; the extensions $\mathbb{Q}(\zeta_{p^v})/\mathbb{Q}(\zeta_{p^{v-1}})$ are Kummer of degree $p$. Over a finite field the Kummer theory is the theory of the unique extension of each degree.

Kummer theory is the engine of the theorem that a polynomial over a field of characteristic zero is solvable by radicals exactly when its Galois group is solvable: after adjoining the roots of unity of the exponent, a solvable group yields a tower of Kummer extensions of prime degree. The single hypothesis that the roots of unity lie in the base is essential: $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is not normal and not Kummer, while $\mathbb{Q}(\zeta_3,\sqrt[3]{2})/\mathbb{Q}(\zeta_3)$ is cyclic cubic.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Base field, containing a primitive $n$-th root of unity |
| $n$ | Exponent, with $\operatorname{char} K \nmid n$ |
| $\mu_n$, $\mu_n(K)$ | Group of $n$-th roots of unity in $K$, cyclic of order $n$ |
| $\zeta$ | A primitive $n$-th root of unity in $K$ |
| $K^\times/(K^\times)^n$ | Class group of $n$-th powers |
| $\Delta$ | Subgroup of $K^\times$ containing $(K^\times)^n$ |
| $\Delta^{1/n}$, $\alpha_i$ | Set of $n$-th roots, and chosen roots with $\alpha_i^n = a_i$ |
| $K(\Delta^{1/n})$ | The Kummer extension attached to $\Delta$ |
| $\Delta_L$ | $(L^\times)^n \cap K^\times$, the inverse map |
| $\sigma \mapsto j_i(\sigma)$ | $\sigma(\alpha_i) = \zeta^{j_i(\sigma)}\alpha_i$ |
| Kummer pairing | $(a,\sigma) \mapsto \sigma(\alpha)/\alpha \in \mu_n$ |
| $\operatorname{N}_{K/\mathbb{Q}}$ | Field norm, used in the example $2 \notin (K^\times)^3$ |
| $f \in K[x]$, $G_f$ | Polynomial and its Galois group |



## Further Reading

- Ernst Eduard Kummer, "Über die Zerlegung der aus Wurzeln der Einheit gebildeten complexen Zahlen in ihre Primfactoren", *Journal für die reine und angewandte Mathematik* 35 (1847), 327–367, for the origin of the theory in the arithmetic of cyclotomic integers.
- David Hilbert, "Die Theorie der algebraischen Zahlkörper", *Jahresbericht der Deutschen Mathematiker-Vereinigung* 4 (1897), 175–546, for the systematic Kummer theory of extensions of exponent $n$ and its use in the class field theory programme.
- Helmut Hasse, *Bericht über neuere Untersuchungen und Probleme aus der Theorie der algebraischen Zahlkörper* (Physica-Verlag, 1930), for the Kummer-theoretic construction of the abelian extensions and its place in the reciprocity laws.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for Kummer theory as the local and global reciprocity for radical extensions.
- Serge Lang, *Algebra* (Springer, revised 3rd ed. 2002), for the Kummer correspondence and the Kummer pairing in the abstract setting.
- Nicholas Bourbaki, *Algebra II* (Springer, 2003), for the Kummer theory of infinite exponent and its Galois-theoretic formulation.
- Kenneth Ireland and Michael Rosen, *A Classical Introduction to Modern Number Theory* (Springer, 2nd ed. 1990), for the cubic and quartic reciprocity laws derived from Kummer theory over $\mathbb{Q}(\zeta_3)$ and $\mathbb{Q}(i)$.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the interpretation of Kummer theory as $H^1(K,\mu_n) \cong K^\times/(K^\times)^n$.
