# __Galois Cohomology__

## Introduction

The Galois group of a field extension acts on everything built from the field: on its additive group, on its multiplicative group, on its roots of unity, and on the algebraic objects defined over it. Galois cohomology is the cohomology of that action, and it converts questions of arithmetic into questions about the cohomology groups $H^n(K, A)$ attached to the absolute Galois group of $K$ and an abelian group $A$ carrying a compatible action. The gain is a systematic machine: short exact sequences of coefficient groups become long exact sequences of cohomology groups, and the resulting connecting maps are exactly the classical constructions of algebraic number theory.

Two computations govern everything. Hilbert's theorem 90, in its multiplicative form $H^1(K,\overline K^\times) = 0$, is the statement that every element of norm $1$ in a cyclic extension is a ratio of a conjugate; in cohomological form it kills the first cohomology of the multiplicative group and makes the Kummer isomorphism $H^1(K,\mu_n) \cong K^\times/(K^\times)^n$ immediate from the exact sequence $1 \to \mu_n \to \overline K^\times \xrightarrow{n} \overline K^\times \to 1$. The second computation, $H^2(K,\overline K^\times)$, identifies the second cohomology of the multiplicative group with the Brauer group, whose local and global structure is the content of class field theory.

This article develops the cohomology of a Galois group, the low-degree interpretations, the exact sequences of restriction, inflation and corestriction, Shapiro's lemma, Hilbert's theorem 90 in both forms, the cohomological reformulation of Kummer theory, and the cohomological dimension with the values it takes for algebraically closed fields, finite fields, local fields and number fields. Throughout, $K$ is a field, $\overline K$ a separable algebraic closure, and $G_K = \operatorname{Gal}(\overline K/K)$ the absolute Galois group; for a finite Galois extension $L/K$ we write $G = \operatorname{Gal}(L/K)$. Coefficients are abelian groups $A$ with an action of the relevant Galois group, and the general theory of the cohomology groups $H^n(G,A)$, of the standard resolution, of the long exact sequence and of the restriction and corestriction maps is that of *Group Cohomology*; this article cites it and applies it. Root-of-unity groups and cyclotomic fields are from *Cyclotomic Fields*, Kummer extensions and the Kummer pairing from *Kummer Theory*, and the ideal theory of number fields from *Dedekind Domains and Ideal Class Groups*. The local and global reciprocity laws are the subject andboth.

---

## The Cohomology of a Galois Group

### Coefficients and the Base Field

**Definition.** Let $G$ be a group. A **$G$-group** is a group $A$ together with an action $G \times A \to A$, $(g,a) \mapsto ga$, by group automorphisms; the group is **abelian** as a $G$-group if $A$ is abelian. When $A$ is abelian, the **invariants** and **coinvariants** are

$$
A^G = \{a \in A : ga = a \text{ for all } g \in G\}, \qquad A_G = A / \langle ga - a : g \in G,\ a \in A\rangle .
$$

**Definition.** For a Galois extension $L/K$, a **Galois coefficient group** is an abelian $G$-group $A$ with $G = \operatorname{Gal}(L/K)$. For the absolute Galois group, a coefficient group is an abelian group together with an action of $G_K$.

The examples that matter are the additive group $L$ with trivial twisting, the multiplicative group $L^\times$, the group $\mu_n = \mu_n(L)$ of $n$-th roots of unity with the natural action $\sigma \cdot \zeta = \sigma(\zeta)$, the integers $\mathbb{Z}$ with trivial action, and $\mathbb{Z}/n\mathbb{Z}$ with trivial action or with the action through roots of unity.

**Definition.** Let $L/K$ be a Galois extension and $A$ a Galois coefficient group. The **Galois cohomology groups** are

$$
H^n(L/K, A) = H^n(\operatorname{Gal}(L/K), A), \qquad H^n(K, A) = H^n(G_K, A),
$$

the second with the convention that $H^n(G_K,A)$ is the direct limit $\varinjlim_M H^n(\operatorname{Gal}(M/K), A^{\operatorname{Gal}(\overline K/M)})$ over the finite Galois extensions $M/K$ contained in $\overline K$; this is the algebraic description of $H^n$ of an inverse limit of finite groups, and it agrees with the cochain definition of *Group Cohomology* because every cochain of the inverse limit factors through a finite quotient.

**Remark.** For $L/K$ a *finite* Galois extension the group $H^n(L/K,A)$ is the ordinary cohomology of the finite group $G$ with coefficients in $A$, as in *Group Cohomology*; the direct limit convention is needed only because $G_K$ is an inverse limit of finite groups and is not itself finite. Concretely, an element of $H^n(G_K,A)$ is represented by a cochain on some finite quotient and two representatives are equal when they agree on a smaller quotient.

### Low Degrees

**Proposition.** Let $A$ be an abelian group with an action of $G$.

**(a)** $H^0(G,A) = A^G$, the group of invariants of $A$ under $G$.

**(b)** $H^1(G,A)$ is the quotient of the group of **crossed homomorphisms** — maps $f : G \to A$ with $f(gh) = f(g) + g f(h)$ — by the subgroup of **principal** ones, those of the form $f(g) = ga - a$ for some $a \in A$.

**(c)** If $A$ carries the trivial action then $H^1(G,A) = \operatorname{Hom}(G,A)$, the group of homomorphisms of groups.

**(d)** $H^2(G,A)$ classifies the group extensions of $G$ by $A$ that realise the given action of $G$ on $A$, that is, the exact sequences $1 \to A \to E \to G \to 1$ with the conjugation action of $E$ on $A$ inducing the given $G$-action, up to equivalence. When $A$ is central in $E$, the classification is by the second cohomology with the trivial action.

**Proof.** (a) is the definition of the zeroth cohomology. (b) is the standard identification: a $1$-cochain is a map $G \to A$, the cocycle condition $\partial f = 0$ is exactly $f(gh) = f(g) + g f(h)$, and the $1$-coboundaries are the principal crossed homomorphisms. (c) is immediate from (b) with trivial action. (d) is the classical classification of extensions: given an extension one chooses a section $s : G \to E$ and the failure of $s$ to be a homomorphism is a $2$-cocycle; changing the section by an element of $A$ changes it by a coboundary. $\square$

**Example (the absolute Galois group of a finite field).** Let $K = \mathbb{F}_q$. Then $\overline K = \overline{\mathbb{F}_q}$ and $G_K$ is the inverse limit of the groups $\operatorname{Gal}(\mathbb{F}_{q^n}/\mathbb{F}_q) \cong \mathbb{Z}/n\mathbb{Z}$ under the natural compatible maps, which we may write $\widehat{\mathbb{Z}}$; it is generated in the natural sense by the Frobenius. It is abelian, and $H^1(G_K, A) = \operatorname{Hom}(G_K, A)$ for trivial coefficients.

**Example (the absolute Galois group of a real closed field).** For $K = \mathbb{R}$, $\overline K = \mathbb{C}$ and $G_K = \mathbb{Z}/2\mathbb{Z}$ with the nontrivial element acting by complex conjugation. Hence $H^n(\mathbb{R}, A) = H^n(\mathbb{Z}/2\mathbb{Z}, A)$, which by the periodicity of the cohomology of a cyclic group is $2$-periodic: $H^{2i}(\mathbb{R},A) = A^{\mathbb{Z}/2}/\{\text{norms}\}$ and $H^{2i+1}(\mathbb{R}, A) = \{a \in A : \operatorname{Tr}(a) = 0\}/(\sigma-1)A$, for the action of complex conjugation.

**Proposition (the zeroth cohomology of the multiplicative group).** For $L/K$ finite Galois with group $G$, $H^0(L/K, L^\times) = K^\times$ and $H^0(L/K, L) = K$. For the absolute Galois group, $H^0(K, \overline K^\times) = K^\times$ and $H^0(K, \overline K) = K$.

**Proof.** The invariants of $L^\times$ under $G$ are the elements of $L^\times$ fixed by every $K$-automorphism of $L$, and these are exactly $K^\times$ by the fundamental theorem of Galois theory; the same argument for the additive group. $\square$

---

## Exact Sequences and the Standard Maps

### Functoriality

**Proposition.** Galois cohomology is a functor in both variables. A homomorphism of coefficient groups $\varphi : A \to A'$ compatible with the actions induces $H^n(G,A) \to H^n(G,A')$; an inclusion of Galois groups $H \subseteq G = \operatorname{Gal}(L/K)$ with $H = \operatorname{Gal}(L/M)$, $M/K$ Galois, gives the **restriction** map

$$
\operatorname{res} : H^n(G,A) \to H^n(H,A),
$$

induced by the inclusion of $H$ in $G$; and there is a **corestriction** map

$$
\operatorname{cor} : H^n(H,A) \to H^n(G,A)
$$

with $\operatorname{cor} \circ \operatorname{res} = [G:H]$, the multiplication by the index.

**Proof.** These are the standard constructions of *Group Cohomology*: restriction is the functoriality of $H^n$ in the group variable, and corestriction is the transfer in the group algebra. $\square$

**Theorem (long exact sequence).** Let $0 \to A \to B \to C \to 0$ be an exact sequence of abelian $G$-groups. Then there is a long exact sequence

$$
0 \to A^G \to B^G \to C^G \xrightarrow{\delta} H^1(G,A) \to H^1(G,B) \to H^1(G,C) \xrightarrow{\delta} H^2(G,A) \to \cdots
$$

which is natural in the coefficient sequence.

**Proof.** The short exact sequence of coefficient groups becomes a short exact sequence of cochain complexes after applying $\operatorname{Hom}(\mathbb{Z}[G\text{-free resolution}], -)$; the zig-zag lemma produces the connecting homomorphism $\delta$ and the long exact sequence. This is the fundamental theorem of *Group Cohomology*. $\square$

**Theorem (inflation–restriction).** Let $L/K$ be Galois, $M/K$ a Galois subextension with $K \subseteq M \subseteq L$, $H = \operatorname{Gal}(L/M) \trianglelefteq G = \operatorname{Gal}(L/K)$ and $Q = G/H = \operatorname{Gal}(M/K)$. For an abelian $G$-group $A$ there is an exact sequence

$$
0 \to H^1(Q, A^H) \xrightarrow{\inf} H^1(G,A) \xrightarrow{\operatorname{res}} H^1(H,A)^{Q} \xrightarrow{\operatorname{tg}} H^2(Q,A^H) \xrightarrow{\inf} H^2(G,A),
$$

where $\inf$ is the **inflation** $H^n(Q,A^H) \to H^n(G,A)$ induced by the quotient map $G \to Q$, and $\operatorname{tg}$ is the **transgression**.

**Proof.** The $5$-term sequence is obtained from the Hochschild–Serre spectral sequence for the group extension $1 \to H \to G \to Q \to 1$, and it may also be obtained by a diagram chase with the standard resolution; the identification of the terms is the content of *Group Cohomology*. $\square$

**Theorem (Shapiro's lemma).** Let $H \leq G$ and let $B$ be an abelian $H$-group. Let $A = \operatorname{Ind}_H^G B$ be the group of functions $f : G \to B$ with the $G$-action $(gf)(g') = f(g'g)$, so that $A$ is an abelian $G$-group whose $H$-action agrees with that on $B$ under the identification of $B$ with the functions supported on $H$. Then

$$
H^n(G, \operatorname{Ind}_H^G B) \cong H^n(H, B)
$$

for every $n \geq 0$. In particular, if $A$ is induced from the trivial subgroup, $H^n(G,A) = 0$ for $n \geq 1$.

**Proof.** The standard proof of *Group Cohomology* identifies the standard resolution of $G$ with the induced resolution of $H$, so that the two cohomology groups are the cohomology of the same complex. $\square$

**Corollary.** If $G$ is finite then $\lvert G\rvert$ annihilates $H^n(G,A)$ for every $n \geq 1$ and every abelian $G$-group $A$. Indeed, taking $H = 1$ and $B = A$ in the proposition, $\operatorname{cor} \circ \operatorname{res}$ on $H^n(G,A)$ is multiplication by $[G:1] = \lvert G\rvert$, while $H^n(1,A) = 0$ for $n \geq 1$, so $\lvert G\rvert$ acts as the zero map. The same argument applied to the finite quotient through which the action on $A$ factors shows that the order of that quotient also annihilates $H^n(G,A)$.

---

## Hilbert's Theorem 90

### The Statement

**Theorem (Hilbert's theorem 90, multiplicative form).** Let $L/K$ be a finite Galois extension with group $G$. Then

$$
H^1(L/K, L^\times) = 0 .
$$

Equivalently, if $x \in L^\times$ satisfies $\prod_{g \in G} g(x) = \operatorname{N}_{L/K}(x) = 1$, then there is $y \in L^\times$ with $x = y / g_0(y)$ for a generator $g_0$ when $G$ is cyclic; more generally an element of $H^1$ vanishes if and only if it is a principal crossed homomorphism.

**Proof.** Let $f : G \to L^\times$ be a crossed homomorphism: $f(gh) = f(g)\, g(f(h))$. The elements $\{f(h) : h \in G\}$ are not all zero, so by Dedekind's theorem on the linear independence of the distinct characters $h : L \to L$ — as in *Galois Theory* — the sum

$$
c = \sum_{h \in G} f(h)\, h(z)
$$

is nonzero for some $z \in L$. For $g \in G$ we compute, using linearity of $g$ and the crossed homomorphism property,

$$
g(c) = \sum_{h} g(f(h))\, gh(z) = \sum_{h} f(gh) f(g)^{-1} \, gh(z) = f(g)^{-1} \sum_{h} f(gh)\, (gh)(z) = f(g)^{-1} c ,
$$

the last step because $h \mapsto gh$ is a bijection of $G$. Hence $f(g) = c / g(c) = g^{-1}(c)/c$ for all $g$, so $f$ is a principal crossed homomorphism and represents the zero class. $\square$

**Theorem (Hilbert's theorem 90, additive form).** With $L/K$ finite Galois with group $G$, the additive group $L$ carries a $G$-action and

$$
H^1(L/K, L) = 0 .
$$

**Proof.** The normal basis theorem, proved in *Galois Theory*, supplies $z \in L$ whose conjugates $g(z)$, $g \in G$, form a $K$-basis of $L$. Given a crossed homomorphism $f : G \to L$, define $c = \sum_h f(h) h(z)$ exactly as above and repeat the computation, which is purely additive. $\square$

**Corollary.** For the absolute Galois group,

$$
H^1(K, \overline K^\times) = 0, \qquad H^1(K, \overline K) = 0 .
$$

**Proof.** Every element of $H^1(G_K, \overline K^\times)$ is represented on a finite Galois extension $L/K$ and is killed by the vanishing of $H^1(L/K,L^\times)$; the direct limit of zero groups is zero. $\square$

**Example (cyclic extensions and the norm).** Let $L/K$ be cyclic of degree $n$ with group generated by $\sigma$. Then $H^1$ is $\ker(\operatorname{N})/(\sigma-1)L^\times$ and $H^{-1}$ is likewise, so Hilbert 90 says

$$
\operatorname{N}_{L/K}(x) = 1 \implies x = y/\sigma(y) \quad \text{for some } y \in L^\times .
$$

For $L = \mathbb{Q}(i)/\mathbb{Q}$ with $\sigma(i) = -i$, the element $i$ has norm $1$ and indeed $i = y/\sigma(y)$ with $y = 1+i$: $\sigma(y) = 1-i$ and $(1+i)/(1-i) = (1+i)^2/2 = i$. For $L = \mathbb{Q}(\sqrt d)/\mathbb{Q}$ and $x = (a+b\sqrt d)/(a-b\sqrt d)$ of norm $1$, the theorem asserts that such elements are exactly the ratios $y/\sigma(y)$, which is the classical parametrisation of the rational points of the norm-one group.

---

## Kummer Theory Revisited

### The Kummer Isomorphism

**Theorem.** Let $\operatorname{char} K \nmid n$ and let $\mu_n = \mu_n(\overline K)$ be the group of $n$-th roots of unity in $\overline K$, with the natural action of $G_K$. Then

$$
H^1(K, \mu_n) \cong K^\times / (K^\times)^n,
$$

the isomorphism being the connecting homomorphism of the exact sequence of coefficient groups.

**Proof.** The $n$-th power map on $\overline K^\times$ is surjective with kernel $\mu_n$, so there is a short exact sequence of abelian $G_K$-groups

$$
1 \longrightarrow \mu_n \longrightarrow \overline K^\times \xrightarrow{\ x \mapsto x^n\ } \overline K^\times \longrightarrow 1 .
$$

Taking cohomology and using $H^0(K,\overline K^\times) = K^\times$, $H^1(K,\overline K^\times) = 0$ from Hilbert's theorem 90, the long exact sequence begins

$$
1 \to \mu_n(K) \to K^\times \xrightarrow{\ n\ } K^\times \xrightarrow{\delta} H^1(K,\mu_n) \to H^1(K,\overline K^\times) = 0 .
$$

Exactness at $H^1(K,\mu_n)$ gives that $\delta$ is surjective, and exactness at the middle $K^\times$ gives $\ker \delta = (K^\times)^n$; hence $\delta$ induces $K^\times/(K^\times)^n \cong H^1(K,\mu_n)$. $\square$

**Corollary (the cohomological form of Kummer theory).** Let $\zeta_n \in K$. Then $G_K$ acts trivially on $\mu_n$ and hence $H^1(K,\mu_n) = \operatorname{Hom}(G_K, \mu_n)$, so

$$
\operatorname{Hom}(G_K,\mu_n) \cong K^\times/(K^\times)^n .
$$

Taking the quotient of $G_K$ by the closure of the commutator subgroup and restricting to quotients of exponent dividing $n$, the dual statement is exactly the Kummer correspondence of *Kummer Theory*: the abelian extensions of $K$ of exponent dividing $n$ correspond to the subgroups of $K^\times/(K^\times)^n$, and the Kummer pairing is the evaluation of the two dual finite abelian groups. The finite quotients of $G_K$ of exponent dividing $n$ are $\operatorname{Gal}(K(\Delta^{1/n})/K)$ for the subgroups $\Delta \supseteq (K^\times)^n$, and the identification of the Galois group with the character group $\operatorname{Hom}(\Delta/(K^\times)^n, \mu_n)$ is the pairing $\sigma(\alpha)/\alpha$ of that article.

**Example ($\mathbb{Q}$).** For $K = \mathbb{Q}$ and $n = 2$, $\mu_2(\mathbb{Q}) = \{\pm1\}$ and $H^1(\mathbb{Q},\mu_2) \cong \mathbb{Q}^\times/(\mathbb{Q}^\times)^2$, which is the group of square classes; the corresponding exponent-$2$ abelian extensions are the multiquadratic fields, as in *Kummer Theory*.

**Example (finite fields).** For $K = \mathbb{F}_q$ and $n$ dividing $q - 1$, $K^\times/(K^\times)^n$ is cyclic of order $n$, so $H^1(\mathbb{F}_q, \mu_n)$ is cyclic of order $n$; the extension attached to the nontrivial class is $\mathbb{F}_{q^n}$, of degree $n$.

### The Second Cohomology and Roots of Unity

**Theorem.** Let $\operatorname{char} K \nmid n$. Then

$$
H^2(K, \mu_n) \cong {}_n \operatorname{Br}(K),
$$

the subgroup of elements of order dividing $n$ in the Brauer group of $K$, defined as $H^2(K,\overline K^\times)$. Under this identification the connecting map of the Kummer sequence is the **period** map of the Brauer group. The class of a cyclic algebra is determined by the pair consisting of the class $\alpha \in K^\times/(K^\times)^n$ and the cyclic extension, in accordance with the crossed product construction. The group $H^2(K,\overline K^\times)$ is by definition the Brauer group, whose description in terms of central simple algebras over $K$ is given in the companion articles of the Part treating algebras.

**Proof.** Applying the long exact sequence to $1 \to \mu_n \to \overline K^\times \to \overline K^\times \to 1$ and using Hilbert 90 gives

$$
H^1(K,\mu_n) \xrightarrow{\delta} H^2(K,\mu_n) \to H^2(K,\overline K^\times) \xrightarrow{n} H^2(K,\overline K^\times),
$$

so the image of $\delta$ is the kernel of multiplication by $n$ on $H^2(K,\overline K^\times)$, which is the definition of ${}_n\operatorname{Br}(K)$; the kernel of $\delta$ is the image of $K^\times$ under the $n$-th power map, so $\delta$ identifies $K^\times/(K^\times)^n$ with a subgroup of ${}_n\operatorname{Br}(K)$, and the two have the same order by the exactness of the remaining terms. $\square$

**Example.** For $K = \mathbb{R}$, the cohomology of the group of order $2$ gives $H^2(\mathbb{R},\mathbb{C}^\times) = \frac12\mathbb{Z}/\mathbb{Z} = \mathbb{Z}/2\mathbb{Z}$, generated by the class of the unique nontrivial central division algebra over $\mathbb{R}$ (the quaternion algebra, treated in the algebra layer, in *Division Algebras* and *Central Simple Algebras and the Brauer Group*), and $H^1(\mathbb{R},\mathbb{C}^\times) = 0$; thus the cohomological dimension of $\mathbb{R}$ is $2$.

**Example.** For an algebraically closed field $K$, the group $G_K$ is trivial and $H^n(K,A) = 0$ for all $n \geq 1$; in particular $\operatorname{Br}(\mathbb{C}) = 0$.

---

## Cohomological Dimension

**Definition.** Let $G$ be a group. The **cohomological dimension** $\operatorname{cd}(G)$ is the least $n \geq 0$ with $H^i(G,A) = 0$ for all $i > n$ and all abelian $G$-groups $A$, if such an $n$ exists. For a field $K$ one writes $\operatorname{cd}(K) = \operatorname{cd}(G_K)$, and for a finite extension $L/K$ the cohomology is that of $\operatorname{Gal}(\overline K/L)$, so that $\operatorname{cd}$ is a property of the absolute Galois group.

**Theorem.** Let $K$ be a field.

**(a)** $\operatorname{cd}(K) = 0$ if and only if $G_K = 1$, that is, if and only if $K$ is separably closed; in particular $\operatorname{cd}(\mathbb{C}) = 0$.

**(b)** $\operatorname{cd}(K) \leq 1$ if and only if the Brauer group of every finite extension of $K$ vanishes. This holds for finite fields and, more generally, for fields of transcendence degree $1$ over an algebraically closed field, by the theorem of Tsen; the classical instance is that $\operatorname{cd}(\mathbb{F}_q) = 1$ with $G_{\mathbb{F}_q}$ the inverse limit of the finite cyclic groups.

**(c)** For $\mathbb{R}$, $\operatorname{cd}(\mathbb{R}) = 2$, as computed from the cohomology of the group of order $2$; the same value holds for a number field, and the proof of that case passes through the completions of $K$ at its places, so it belongs to Part II , and only the statement is recorded here.

**Proof sketch.** (a) A trivial Galois group has trivial cohomology in positive degrees. (b) If some finite extension $L/K$ has $\operatorname{Br}(L) \neq 0$ then $H^2(L,\overline L{}^\times) \neq 0$ and $\operatorname{cd}(L) \geq 2$, so the vanishing for all finite extensions is necessary; it is sufficient by the cohomological interpretation of the Brauer group together with the periodicity of finite group cohomology. For finite fields, $\widehat{\mathbb{Z}} = G_{\mathbb{F}_q}$ acts trivially on $\overline{\mathbb{F}_q}^\times = \mu$, a divisible-by-finite group with no $p$-torsion for the relevant primes, so $H^2(\mathbb{F}_q,\overline{\mathbb{F}_q}^\times) = 0$ and $\operatorname{cd} = 1$; Tsen's theorem gives $\operatorname{cd} \leq 1$ for $C_1$ fields. (c) For $\mathbb{R}$ the periodicity of the cohomology of the group of order $2$ gives the nonvanishing second cohomology $\mathbb{Z}/2\mathbb{Z}$ computed above, so $\operatorname{cd}(\mathbb{R}) = 2$. For a number field the invariant maps at the places combine to a nonzero $H^2$, and the vanishing above degree $2$ follows from the theory of the Brauer group; the details pass through the completions and belong to Part II and . $\square$

**Theorem (local invariant).** Let $K$ be a field complete with respect to a discrete valuation, with residue field $\mathbb{F}_q$. Then there is an isomorphism, the **invariant map**,

$$
\operatorname{inv}_K : H^2(K,\overline K^\times) \xrightarrow{\ \sim\ } \mathbb{Q}/\mathbb{Z},
$$

and for a finite extension $L/K$ of degree $n$ the diagram commutes with multiplication by $n$: $\operatorname{inv}_K \circ \operatorname{cor} = n \cdot \operatorname{inv}_L$. The restriction of $\operatorname{inv}_K$ to $H^2(K,\mu_m)$ is injective with image $\frac1m\mathbb{Z}/\mathbb{Z}$ when $\operatorname{char} K \nmid m$.

**Remark.** A complete discretely valued field is a **local field**, and its valuation, valuation ring and completion are the subject and of Part II; the theorem above is therefore stated here and proved, and it is not developed in this article.

**Theorem (global duality, statement).** Let $K$ be a number field and let $A$ be a finite abelian $G_K$-group. Then for each $n$ the cup product

$$
H^n(K, A) \times H^{2-n}(K, \operatorname{Hom}(A, \overline K^\times)) \longrightarrow H^2(K,\overline K^\times)
$$

is a perfect pairing of finite groups, the **Tate duality** of the global field, and the local analogues hold with $\mathbb{Q}/\mathbb{Z}$ replaced by the invariant map of the completion at each place. The proofs are. The cup product is the standard product of *Group Cohomology*, and no metric or topological structure enters.

---

## Summary

Galois cohomology is the cohomology of the action of a Galois group on an abelian group, with $H^0(G,A) = A^G$, with $H^1$ the crossed homomorphisms modulo the principal ones, and with $H^2$ classifying group extensions. For an infinite Galois group it is the direct limit over the finite Galois subextensions, which is the algebraic description of the inverse limit of finite groups. Functoriality gives restriction and corestriction, with corestriction followed by restriction equal to multiplication by the index, and a short exact sequence of coefficients gives a long exact sequence with connecting maps; inflation and restriction fit into the five-term sequence of Hochschild and Serre, and Shapiro's lemma identifies the cohomology of an induced coefficient group with the cohomology of the subgroup.

Hilbert's theorem 90, in the multiplicative form $H^1(L/K,L^\times) = 0$ and the additive form $H^1(L/K,L) = 0$, is proved by summing a crossed homomorphism against a separating element, using the linear independence of the distinct field characters and the normal basis theorem respectively; it gives $H^1(K,\overline K^\times) = H^1(K,\overline K) = 0$. The Kummer sequence $1 \to \mu_n \to \overline K^\times \to \overline K^\times \to 1$ then yields $H^1(K,\mu_n) \cong K^\times/(K^\times)^n$, which is Kummer theory in cohomological form, and $H^2(K,\mu_n) \cong {}_n\operatorname{Br}(K)$ with $H^2(K,\overline K^\times)$ the Brauer group. The cohomological dimension is $0$ for separably closed fields, $1$ for finite fields and for fields of transcendence degree one over an algebraically closed field, and $2$ for $\mathbb{R}$ and for a number field; the invariant map $H^2(K,\overline K^\times) \cong \mathbb{Q}/\mathbb{Z}$ of class field theory and the Tate duality of a global field are the arithmetic computations of the second cohomology, deferred to Part II , where the completions are available.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $L$ | Field, and a Galois extension field |
| $\overline K$ | Separable algebraic closure of $K$ |
| $G_K$ | Absolute Galois group $\operatorname{Gal}(\overline K/K)$ |
| $G = \operatorname{Gal}(L/K)$ | Galois group of a finite Galois extension |
| $A$, $B$, $C$ | Abelian groups with a $G$-action (coefficient groups) |
| $A^G$, $A_G$ | Invariants, coinvariants |
| $H^n(G,A)$, $H^n(L/K,A)$, $H^n(K,A)$ | Cohomology groups; the last a direct limit over finite subextensions |
| $f : G \to A$ crossed | $f(gh) = f(g) + g f(h)$ |
| $\delta$ | Connecting homomorphism of a coefficient sequence |
| $\operatorname{res}$, $\operatorname{cor}$, $\inf$, $\operatorname{tg}$ | Restriction, corestriction, inflation, transgression |
| $\operatorname{N}_{L/K}$ | Field norm, the multiplicative $H^0$ |
| $\operatorname{Tr}$ | Field trace, the additive $H^0$ |
| $\mu_n$ | Group of $n$-th roots of unity, with the natural action |
| ${}_n \operatorname{Br}(K)$ | $n$-torsion of the Brauer group $H^2(K,\overline K^\times)$ |
| $\operatorname{cd}(G)$, $\operatorname{cd}(K)$ | Cohomological dimension |
| $\operatorname{inv}_K$ | Local invariant, $H^2(K,\overline K^\times) \cong \mathbb{Q}/\mathbb{Z}$ |
| $\widehat{\mathbb{Z}}$ | Inverse limit of the groups $\mathbb{Z}/n\mathbb{Z}$, the Galois group of a finite field |





## Further Reading

- David Hilbert, "Die Theorie der algebraischen Zahlkörper", *Jahresbericht der Deutschen Mathematiker-Vereinigung* 4 (1897), 175–546, for the theorem now numbered 90 and its use in the arithmetic of cyclic extensions.
- Claude Chevalley, "Généralisation de la théorie du corps de classes pour les extensions infinies", *Journal de Mathématiques Pures et Appliquées* 15 (1936), 359–371, for the cohomological formulation of class field theory.
- Gerhard Hochschild and Jean-Pierre Serre, "Cohomology of group extensions", *Transactions of the American Mathematical Society* 74 (1953), 110–134, for the five-term inflation–restriction sequence.
- John Tate, "The higher dimensional cohomology groups of class field theory", *Annals of Mathematics* 56 (1952), 294–297, for the cohomological dimension of local and global fields and for Tate duality.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the standard development of the cohomology of Galois groups, Hilbert 90, the Brauer group and the dimension theorems.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the invariant map, the local reciprocity and the second cohomology of a local field.
- Jürgen Neukirch, Alexander Schmidt and Kay Wingberg, *Cohomology of Number Fields* (Springer, 2nd ed. 2008), for the global duality theorems, the Brauer group and the local–global sequences.
- Kenneth S. Brown, *Cohomology of Groups* (Springer, 1982), for the general theory of group cohomology, restriction, corestriction and Shapiro's lemma used here.
