# __Algebraic Number Theory__

## Introduction

A number field is a finite extension $K$ of $\mathbb{Q}$, and its arithmetic is carried by the ring of integers $\mathcal{O}_K$, the set of elements of $K$ integral over $\mathbb{Z}$. The foundational theorem is that $\mathcal{O}_K$ is a Dedekind domain: it is Noetherian, integrally closed and of Krull dimension $1$, so its nonzero ideals factor uniquely into prime ideals even though elements need not factor uniquely. The failure of unique factorisation of elements is measured by the ideal class group $\operatorname{Cl}(\mathcal{O}_K)$, which is finite, and the units of $\mathcal{O}_K$ are described by Dirichlet's unit theorem. With these three facts — unique factorisation of ideals, finiteness of the class group, finite generation of the unit group — the arithmetic of $K$ becomes a subject: one can speak of the primes of $K$, of their splitting in an extension, of ramification, and of the reciprocity laws that govern the abelian extensions.

This article assembles the arithmetic of number fields: the ring of integers and the discriminant, the arithmetic of ideals and the class group, the decomposition of a rational prime in $\mathcal{O}_K$ with the ramification index, the residue degree and Dedekind's factorisation theorem, ramification and the different, the Minkowski bound in the form in which the present Part can state it, and Dirichlet's unit theorem. The local and analytic inputs — the volume estimate of Minkowski, the logarithm of the unit theorem, and the completion of $K$ at a prime — belong to later Parts and are named with a forward reference rather than used. Throughout, $K$ is a number field of degree $n = [K:\mathbb{Q}]$ with $r_1$ real embeddings and $r_2$ pairs of complex conjugate embeddings, so that $n = r_1 + 2r_2$; $\mathcal{O}_K$ is its ring of integers; $\mathfrak{p}$ a nonzero prime ideal; $I_K$ the group of nonzero fractional ideals. Unique factorisation of ideals, the class group, the norm of an ideal, and the theorems of Dedekind on $\mathcal{O}_K$ are from *Dedekind Domains and Ideal Class Groups*; Noetherian, Artinian and dimension theory from *Noetherian and Artinian Rings*, *Primary Decomposition* and *Integral Extensions and Krull Dimension*; valuations, discrete valuation rings and Hensel's lemma from *Valuation Theory and Henselian Rings*; the splitting of primes in Galois extensions and the Frobenius element from *Class Field Theory*; the arithmetic of cyclotomic fields from *Cyclotomic Fields*. The completions, the $p$-adic fields and the ideles are the subject and of Part II, and this article does not use them; Dirichlet's unit theorem and the finiteness of the class group are stated with the proofs deferred to the place where the required measure theory is available.

---

## Number Fields and Rings of Integers

### Embeddings and Signature

**Definition.** A **number field** is a field $K$ with $[K:\mathbb{Q}] = n < \infty$. Its **signature** is the pair $(r_1, r_2)$, where $r_1$ is the number of embeddings $K \hookrightarrow \mathbb{R}$ and $r_2$ the number of conjugate pairs of embeddings $K \hookrightarrow \mathbb{C}$ that are not real; thus $r_1 + 2r_2 = n$ and $K$ **has** $r_1 + r_2$ archimedean places, two embeddings defining the same place from a conjugate pair. The field is **totally real** if $r_1 = n$, **totally imaginary** if $r_1 = 0$.

**Definition.** Let $\sigma_1, \ldots, \sigma_n$ be the distinct embeddings $K \hookrightarrow \mathbb{C}$. The **discriminant** of an $n$-tuple $\alpha_1, \ldots, \alpha_n \in K$ is

$$
\operatorname{disc}(\alpha_1, \ldots, \alpha_n) = \Bigl(\det\bigl(\sigma_i(\alpha_j)\bigr)_{i,j=1}^{n}\Bigr)^{2} = \det\bigl(\operatorname{Tr}_{K/\mathbb{Q}}(\alpha_i\alpha_j)\bigr)_{i,j=1}^{n},
$$

and the two expressions agree. If $K = \mathbb{Q}(\alpha)$ with $f \in \mathbb{Q}[x]$ the minimal polynomial of $\alpha$, then

$$
\operatorname{disc}(1, \alpha, \ldots, \alpha^{n-1}) = (-1)^{n(n-1)/2}\operatorname{N}_{K/\mathbb{Q}}(f'(\alpha)) = \operatorname{disc}(f) .
$$

**Proof.** The second displayed identity is the standard relation between the discriminant of a basis of powers and the discriminant of the minimal polynomial, obtained by evaluating the Vandermonde determinant; the first is the definition of the discriminant as a square of a determinant. $\square$

**Example.** For $K = \mathbb{Q}(\sqrt2)$ the signature is $(2,0)$ and $\operatorname{disc}(1,\sqrt2) = \det\begin{pmatrix}1 & \sqrt2\\ 1 & -\sqrt2\end{pmatrix}^2 = 8$. For $K = \mathbb{Q}(\sqrt{-5})$ the signature is $(0,1)$ and $\operatorname{disc}(1,\sqrt{-5}) = -20$. For the power basis of $\mathbb{Q}(\sqrt[3]{2})$ one gets $\operatorname{disc}(1,\varrho,\varrho^2) = -108$ for $\varrho = \sqrt[3]{2}$, from $-4\cdot 0^3 - 27\cdot(-2)^2 = -108$.

### Integrality and the Ring of Integers

**Definition.** An element $\alpha \in K$ is **integral over $\mathbb{Z}$** if it is a root of a monic polynomial with coefficients in $\mathbb{Z}$; the **ring of integers** is

$$
\mathcal{O}_K = \{\alpha \in K : \alpha \text{ is integral over } \mathbb{Z}\} .
$$

**Theorem.** Let $K$ be a number field.

**(a)** $\mathcal{O}_K$ is a subring of $K$ with field of fractions $K$, and it is the integral closure of $\mathbb{Z}$ in $K$.

**(b)** $\mathcal{O}_K$ is a free $\mathbb{Z}$-module of rank $n = [K:\mathbb{Q}]$; every $\mathbb{Z}$-basis of $\mathcal{O}_K$ is an **integral basis** of $K$.

**(c)** $\mathcal{O}_K$ is a Dedekind domain and is the unique maximal order of $K$.

**Proof sketch.** (a) is the theorem that the integral elements form a ring, from *Integral Extensions and Krull Dimension*, together with the fact that $\mathbb{Z}$ is integrally closed; the field of fractions is $K$ because every element of $K$ is $\alpha/m$ for an integral $\alpha$ and nonzero $m \in \mathbb{Z}$. (b) Integrality implies that the $\mathbb{Z}$-module generated by $\mathcal{O}_K$ inside the finite-dimensional $\mathbb{Q}$-vector space $K$ is finitely generated of rank $n$; finite generation uses the trace form, which is nondegenerate on $K$, and the standard argument bounding denominators. (c) A Dedekind domain is a Noetherian integrally closed domain of Krull dimension $1$; $\mathcal{O}_K$ has these three properties by (a), (b) and the dimension theorem, and maximality among orders follows from integral closedness. $\square$

**Definition.** The **discriminant** $d_K$ of $K$ is $\operatorname{disc}(\alpha_1, \ldots, \alpha_n)$ for any integral basis; it is an integer independent of the basis, since a change of basis multiplies the discriminant by the square of a unit of $\mathbb{Z}$, which is $1$. Two integral bases give the same $d_K$ up to a square in $\mathbb{Z}^\times = \{\pm1\}$, and the convention that the discriminant of a basis ordered by the embeddings has the sign $(-1)^{r_2}$ fixes it.

**Example.** For $K = \mathbb{Q}(\sqrt{d})$ with $d$ squarefree:

$$
\mathcal{O}_K = \begin{cases} \mathbb{Z}\bigl[\tfrac{1+\sqrt d}{2}\bigr], & d \equiv 1 \pmod 4,\\ \mathbb{Z}[\sqrt d], & d \equiv 2, 3 \pmod 4,\end{cases}
\qquad
d_K = \begin{cases} d, & d \equiv 1 \pmod 4,\\ 4d, & d \equiv 2,3 \pmod 4 .\end{cases}
$$

The element $(1+\sqrt d)/2$ is integral in the first case because it satisfies $x^2 - x + (1-d)/4 = 0$ with $(1-d)/4 \in \mathbb{Z}$; in the second case $\mathbb{Z}[\sqrt d]$ is integrally closed. The discriminant of its basis is $d$ in the first case and $4d$ in the second, as a direct computation of the $2\times2$ determinant gives.

---

## The Arithmetic of Ideals

### Unique Factorisation and the Class Group

**Theorem (unique factorisation of ideals).** Every nonzero ideal of $\mathcal{O}_K$ is a product of prime ideals, uniquely up to order; equivalently, $\mathcal{O}_K$ is a Dedekind domain and every nonzero prime ideal is maximal and invertible. Every nonzero fractional ideal is $\prod_\mathfrak{p} \mathfrak{p}^{v_\mathfrak{p}}$ with $v_\mathfrak{p} \in \mathbb{Z}$, almost all zero.

This is the factorisation theorem of *Dedekind Domains and Ideal Class Groups*, and it is the reason the arithmetic of $K$ is the arithmetic of ideals rather than of elements.

**Definition.** The **norm** of a nonzero ideal $\mathfrak{a}$ of $\mathcal{O}_K$ is $\operatorname{N}(\mathfrak{a}) = \lvert \mathcal{O}_K/\mathfrak{a}\rvert$, finite because $\mathcal{O}_K$ is a free $\mathbb{Z}$-module of rank $n$ and $\mathfrak{a} \supseteq (m)$ for a nonzero $m \in \mathfrak{a}$. It is multiplicative, and $\operatorname{N}(\mathfrak{a}) = \lvert \operatorname{N}_{K/\mathbb{Q}}(\alpha)\rvert$ when $\mathfrak{a} = (\alpha)$ is principal.

**Definition.** The **ideal class group** is

$$
\operatorname{Cl}(\mathcal{O}_K) = \frac{\{\text{nonzero fractional ideals}\}}{\{\text{principal fractional ideals}\}},
$$

and its order $h_K = \lvert \operatorname{Cl}(\mathcal{O}_K)\rvert$ is the **class number**. It is finite by Dedekind's theorem, recorded in *Dedekind Domains and Ideal Class Groups*; $\operatorname{Cl}(\mathcal{O}_K) = 0$ if and only if $\mathcal{O}_K$ is a principal ideal domain, equivalently a unique factorisation domain.

**Example.** $\operatorname{Cl}(\mathbb{Z}) = 0$ and $h_{\mathbb{Q}} = 1$. $\operatorname{Cl}(\mathbb{Z}[i]) = 0$ and $h_{\mathbb{Q}(i)} = 1$. $\operatorname{Cl}(\mathbb{Z}[\sqrt{-5}]) \cong \mathbb{Z}/2\mathbb{Z}$ and $h_{\mathbb{Q}(\sqrt{-5})} = 2$: the prime $P = (2, 1+\sqrt{-5})$ above $2$ is not principal, and $P^2 = (2)$. The element $6 = 2\cdot3 = (1+\sqrt{-5})(1-\sqrt{-5})$ has two essentially different factorisations, and in ideal terms the four prime ideals above $2$ and $3$ rearrange: $(2) = P^2$, $(3) = Q Q'$, and $(1+\sqrt{-5}) = PQ$, $(1-\sqrt{-5}) = PQ'$ for suitable choice of labelling.

---

## Decomposition of Primes

### The Fundamental Identity

**Definition.** Let $K$ be a number field and $\mathfrak{p}$ a nonzero prime of $\mathcal{O}_K$ lying over the rational prime $p$, so that $\mathfrak{p} \cap \mathbb{Z} = (p)$ and $\operatorname{N}(\mathfrak{p}) = p^{f}$ with $f \geq 1$ the **residue degree**. In an extension $L/K$ of number fields, for a prime $\mathfrak{P}$ of $\mathcal{O}_L$ over $\mathfrak{p}$,

$$
\mathfrak{p}\mathcal{O}_L = \mathfrak{P}_1^{e_1}\cdots\mathfrak{P}_g^{e_g}, \qquad e_i \geq 1,
$$

with **ramification index** $e_i$, **residue degree** $f_i = [\mathcal{O}_L/\mathfrak{P}_i : \mathcal{O}_K/\mathfrak{p}]$, and $\mathfrak{p}$ is **unramified** in $L$ if all $e_i = 1$, **split completely** if $g = [L:K]$ and all $e_i = f_i = 1$, **inert** if $g = 1$ and $e_1 = 1$.

**Theorem (fundamental identity).** With the notation above,

$$
\sum_{i=1}^{g} e_i f_i = [L:K] .
$$

For $L/K$ Galois the numbers $e_i = e$ and $f_i = f$ are independent of $i$ and $g = [L:K]/(ef)$.

**Proof.** The identity follows by applying the norm $\operatorname{N}_{L/K}$ to both sides of $\mathfrak{p}\mathcal{O}_L = \prod \mathfrak{P}_i^{e_i}$; the norm of $\mathfrak{P}_i$ is $\mathfrak{p}^{f_i}$, so both sides have norm $\mathfrak{p}^{[L:K]}$ and $\mathfrak{p}^{e_if_i}$. This is the standard computation of *Dedekind Domains and Ideal Class Groups*; for Galois $L/K$ the group acts transitively on the primes above $\mathfrak{p}$, so the $e_i$ and the $f_i$ coincide. $\square$

**Example.** In $\mathbb{Q}(i)/\mathbb{Q}$: the prime $2$ ramifies, $(2) = (1+i)^2$ with $e = 2$, $f = g = 1$; a prime $p \equiv 1 \bmod 4$ splits, $(p) = \mathfrak{p}\bar{\mathfrak{p}}$ with $e = 1$, $f = 1$, $g = 2$; a prime $p \equiv 3 \bmod 4$ is inert, $(p)$ prime with $e = 1$, $f = 2$, $g = 1$. In each case $\sum e_if_i = 2$.

### Dedekind's Factorisation Theorem

**Theorem (Dedekind).** Let $L = K(\alpha)$ with $\alpha \in \mathcal{O}_L$ and let $f \in \mathcal{O}_K[x]$ be its minimal polynomial. Suppose $\mathfrak{p}$ is a nonzero prime of $\mathcal{O}_K$ with $\mathfrak{p} \nmid [\mathcal{O}_L : \mathcal{O}_K[\alpha]]$, and let

$$
\bar f = \bar g_1^{e_1} \cdots \bar g_g^{e_g} \in \kappa(\mathfrak{p})[x]
$$

be the factorisation of the reduction of $f$ into monic irreducibles. Then

$$
\mathfrak{p}\mathcal{O}_L = \mathfrak{P}_1^{e_1}\cdots\mathfrak{P}_g^{e_g}, \qquad
\mathfrak{P}_i = \mathfrak{p}\mathcal{O}_L + g_i(\alpha)\mathcal{O}_L, \qquad f_i = \deg \bar g_i .
$$

**Proof sketch.** The ring $\mathcal{O}_L/\mathfrak{p}\mathcal{O}_L$ is a quotient of $\mathcal{O}_K[\alpha]/\mathfrak{p}\mathcal{O}_K[\alpha] \cong \kappa(\mathfrak{p})[x]/(\bar f)$ when the index condition holds, so the prime ideals above $\mathfrak{p}$ correspond to the irreducible factors of $\bar f$; lifting the factorisation back through the isomorphism and using the factorisation of ideals in a Dedekind domain gives the displayed factorisation, and the residue degree is the degree of the corresponding factor. This is the theorem of Kummer and Dedekind; the index condition is automatic when $\mathcal{O}_L = \mathcal{O}_K[\alpha]$, which holds in all the examples below. $\square$

**Example.** For $L = \mathbb{Q}(\sqrt[3]{2})$, $\mathcal{O}_L = \mathbb{Z}[\varrho]$ with $\varrho^3 = 2$, and $f = x^3 - 2$. Modulo $5$: $x^3 - 2 \equiv x^3 + 3 \pmod 5$, and $3$ is not a cube mod $5$ (the cubes mod $5$ are $0, \pm1$), so $5$ is inert: $e = 1$, $f = 3$, $g = 1$. Modulo $7$: $2$ is a cube mod $7$ since $3^3 = 27 \equiv 6$, $2^3 = 8 \equiv 1$, $4^3 \equiv 1$, $5^3 \equiv 6$, $6^3 \equiv 6$: the cubes mod $7$ are $0, 1, 6$, so $2$ is not a cube and $7$ is inert. Modulo $31$: the cube roots of $2$ are $4$, $7$ and $20$, since $4^3 = 64 \equiv 2$, $7^3 = 343 = 31\cdot 11 + 2$ and $20^3 = 8000 = 31\cdot 258 + 2$; hence $x^3 - 2$ splits into three linear factors and $31$ splits completely with $f = 1$, $g = 3$. Modulo $2$ the polynomial reduces to $x^3$, and modulo $3$ to $x^3 + 1 = (x+1)^3$, so $2$ and $3$ are totally ramified with $e = 3$, $f = 1$, $g = 1$, consistently with the discriminant $-108 = -2^2\cdot 3^3$.

**Example.** For $L = \mathbb{Q}(\zeta_5)$ and $p \neq 5$: the order of $p$ modulo $5$ is the residue degree, and $g = 4/f$. For $p = 2$ the order of $2$ in $(\mathbb{Z}/5\mathbb{Z})^\times$ is $4$, so $f = 4$, $g = 1$: $2$ is inert. For $p = 11 \equiv 1$, $f = 1$ and $g = 4$: $11$ splits completely. For $p = 19 \equiv -1$, the order is $2$, so $f = 2$, $g = 2$. The prime $5$ is totally ramified, $(5) = (1-\zeta_5)^4$.

### Ramification and the Discriminant

**Theorem.** Let $L/K$ be an extension of number fields. A prime $\mathfrak{p}$ of $K$ ramifies in $L$ if and only if $\mathfrak{p}$ divides the **relative discriminant** $\mathfrak{d}_{L/K}$, an ideal of $\mathcal{O}_K$ defined below, if and only if $\mathfrak{p}$ divides the **different** $\mathfrak{D}_{L/K}$. In particular, for $K/\mathbb{Q}$, the rational prime $p$ ramifies in $K$ if and only if $p \mid d_K$.

**Proof sketch.** The different is the ideal generated by the images of the trace-dual of $\mathcal{O}_L$, and its valuation at $\mathfrak{P}$ is computed from the higher ramification groups; the discriminant is its norm, so the two have the same prime divisors. The classical criterion — $\mathfrak{p}$ unramified iff the trace form is nondegenerate modulo $\mathfrak{p}$, equivalently iff $\mathfrak{p} \nmid \mathfrak{D}_{L/K}$ — is proved in *Dedekind Domains and Ideal Class Groups* and in *Valuation Theory and Henselian Rings* for the local statement. $\square$

**Corollary.** A number field $K \neq \mathbb{Q}$ has at least one ramified prime, since $\lvert d_K\rvert > 1$; indeed $\lvert d_K\rvert \geq 3$ for $n \geq 2$, as follows from the Minkowski bound of the section below.

**Example.** For $K = \mathbb{Q}(\sqrt{-5})$ the discriminant is $-20$, so the ramified primes are $2$ and $5$. For $K = \mathbb{Q}(\sqrt5)$ the discriminant is $5$, so only $5$ ramifies: The prime $2$ is inert: since $\mathcal{O}_K = \mathbb{Z}[(1+\sqrt5)/2]$, the relevant minimal polynomial is $x^2-x-1$, whose reduction $x^2+x+1$ is irreducible over $\mathbb{F}_2$, so $e = 1$, $f = 2$, $g = 1$. In $\mathbb{Z}[\sqrt5]$ alone the index condition fails, which is why the integral basis must be used. For $K = \mathbb{Q}(\sqrt{-23})$, $d_K = -23$, and $23$ is the only ramified prime.

---

## Minkowski Theory and Units

### The Minkowski Bound

**Definition.** The **Minkowski bound** of a number field $K$ of degree $n$ with signature $(r_1, r_2)$ and discriminant $d_K$ is

$$
M_K = \frac{n!}{n^n}\left(\frac{4}{\pi}\right)^{r_2}\sqrt{\lvert d_K\rvert} .
$$

**Theorem (Minkowski).** Every ideal class of $\mathcal{O}_K$ contains an integral ideal $\mathfrak{a}$ with $\operatorname{N}(\mathfrak{a}) \leq M_K$; consequently the class group is finite, and $\lvert d_K\rvert > 1$ for $n \geq 2$.

**Proof sketch.** The embeddings $\sigma_1, \ldots, \sigma_n$ place $\mathcal{O}_K$ as a lattice in the real vector space $\mathbb{R}^{r_1}\times\mathbb{C}^{r_2}$, and the volume of a fundamental domain is $2^{-r_2}\sqrt{\lvert d_K\rvert}$; Minkowski's convex body theorem — a statement about volumes and convex bodies — then produces a nonzero element of small norm in any ideal, and dividing by it gives a small ideal in the class. **The proof uses the Euclidean distance and the volume on $\mathbb{R}^{r_1}\times\mathbb{C}^{r_2}$, which the present Part does not yet have**; the two ingredients are supplied in Part II, where the Euclidean structure of the space of embeddings and the convex body theorem are available, and the statement above is recorded here as the arithmetic consequence. That $\lvert d_K\rvert > 1$ follows by evaluating the bound: for $n \geq 2$ one has $\sqrt{\lvert d_K\rvert} \geq \frac{n^n}{n!}(\pi/4)^{r_2} \geq \frac{n^n}{n!}(\pi/4)^{n/2} > 1$, using $r_2 \leq n/2$ and $\pi/4 < 1$ together with $\frac{n^n}{n!} \geq 2^{n-1}$ and $(\pi/4)^{n/2} > 2^{-(n-1)}$, both valid for $n \geq 2$; numerically the lower bounds at $n = 2, 3, 4$ are $1.57$, $3.13$, $6.58$. Hence $\lvert d_K\rvert \geq 3$ for $n \geq 2$. $\square$

**Example.** For $K = \mathbb{Q}(\sqrt{-5})$: $n = 2$, $r_2 = 1$, $\lvert d_K\rvert = 20$, so $M_K = \frac{2}{4}\cdot\frac{4}{\pi}\sqrt{20} = \frac{4\sqrt5}{\pi} \approx 2.85$, and every class has a representative of norm at most $2$; the only such ideals are $\mathcal{O}_K$ and the prime $P$ above $2$, whence $h_K \leq 2$, and $P$ is not principal, whence $h_K = 2$.

**Example.** For $K = \mathbb{Q}(\sqrt{-23})$: $n = 2$, $r_2 = 1$, $\lvert d_K\rvert = 23$, so $M_K = \frac{2}{\pi}\sqrt{23} \approx 3.05$, and representatives of norm at most $3$ suffice; the ideals of norm $2$ and $3$ are the primes above $2$ and $3$, and the analysis of *Class Field Theory* gives $\operatorname{Cl}(\mathcal{O}_K) \cong \mathbb{Z}/3\mathbb{Z}$.

### Dirichlet's Unit Theorem

**Theorem (Dirichlet).** Let $K$ be a number field with signature $(r_1,r_2)$ and let $\mu_K$ be the finite cyclic group of roots of unity in $K$. Then the unit group of $\mathcal{O}_K$ is

$$
\mathcal{O}_K^\times \cong \mu_K \oplus \mathbb{Z}^{r_1+r_2-1},
$$

so that the **rank** of the unit group is $r_1 + r_2 - 1$; the free part is generated by **fundamental units**, and the **regulator** $\operatorname{Reg}_K$ is the covolume of the image of the units under the logarithmic embedding, which is the volume of a fundamental domain of the lattice of units.

**Proof sketch.** The method is to consider the homomorphism $\ell : \mathcal{O}_K^\times \to \mathbb{R}^{r_1+r_2}$ sending a unit to the logarithms of the absolute values of its conjugates; its image is a lattice of rank $r_1 + r_2 - 1$ and its kernel is $\mu_K$. Both the logarithm and the covolume are analytic and metric notions, and the proof therefore belongs to Part II and to Part III, where the logarithm and the volume are available; the statement is recorded here. $\square$

**Example.** For $K = \mathbb{Q}$: $r_1 = 1$, $r_2 = 0$, rank $0$, and $\mathcal{O}_\mathbb{Q}^\times = \{\pm1\} = \mu_\mathbb{Q}$. For $K = \mathbb{Q}(i)$: $r_1 = 0$, $r_2 = 1$, rank $0$, and $\mathcal{O}_K^\times = \{\pm1, \pm i\} = \mu_4$. For $K = \mathbb{Q}(\sqrt2)$: $r_1 = 2$, $r_2 = 0$, rank $1$, and $\mathcal{O}_K^\times = \{\pm(1+\sqrt2)^m : m \in \mathbb{Z}\}$, since $(1+\sqrt2)(\sqrt2-1) = 1$. For $K = \mathbb{Q}(\sqrt{-5})$: rank $0$ and $\mathcal{O}_K^\times = \{\pm1\}$, although $h_K = 2$. For $K = \mathbb{Q}(\zeta_5)$: $r_1 = 0$, $r_2 = 2$, rank $1$, in accordance with *Cyclotomic Fields*; and for $K = \mathbb{Q}(\zeta_7)$: $r_1 = 0$, $r_2 = 3$, rank $2$.

**Theorem (Hermite–Minkowski).** For a fixed integer $d$ there are only finitely many number fields of discriminant exactly $d$, and $\mathbb{Q}$ is the only number field with $\lvert d_K\rvert = 1$.

**Proof sketch.** Bounding the discriminant bounds the degree and the signature by the Minkowski bound, and then bounds the coefficients of the minimal polynomials of the elements of a bounded set of candidate generators; the details use the same metric arguments as above and are in Part II. $\square$

---

## The Different and the Discriminant

**Definition.** Let $L/K$ be a finite extension of number fields. The **inverse different** is

$$
\mathfrak{D}_{L/K}^{-1} = \{x \in L : \operatorname{Tr}_{L/K}(x\,\mathcal{O}_L) \subseteq \mathcal{O}_K\},
$$

a fractional ideal of $L$ containing $\mathcal{O}_L$; its inverse $\mathfrak{D}_{L/K}$ is the **different**, a nonzero ideal of $\mathcal{O}_L$, and the **relative discriminant** is $\mathfrak{d}_{L/K} = \operatorname{N}_{L/K}(\mathfrak{D}_{L/K})$, an ideal of $\mathcal{O}_K$. For $K = \mathbb{Q}$ one has $\operatorname{N}(\mathfrak{d}_{L/\mathbb{Q}}) = \lvert d_L\rvert$.

**Theorem (the different detects ramification).** Let $\mathfrak{P}$ be a nonzero prime of $\mathcal{O}_L$ over $\mathfrak{p}$.

**(a)** $\mathfrak{P} \mid \mathfrak{D}_{L/K}$ if and only if $\mathfrak{p}$ ramifies in $L$, that is, if and only if $e(\mathfrak{P}/\mathfrak{p}) > 1$.

**(b)** Consequently $\mathfrak{P}$ divides $\mathfrak{D}_{L/K}$ if and only if $\mathfrak{P}$ divides $\mathfrak{d}_{L/K}\mathcal{O}_L$.

**(c)** If $L/K$ is Galois with group $G$ and $\mathfrak{p}$ is unramified, then $\mathfrak{D}_{L/K} = (1)$ over $\mathfrak{p}$, and the Frobenius element $\operatorname{Frob}_{\mathfrak{P}}$ of *Class Field Theory* describes the splitting completely.

**Proof sketch.** (a) The trace pairing $L \times L \to K$, $(x,y) \mapsto \operatorname{Tr}_{L/K}(xy)$, is nondegenerate, and its behaviour modulo $\mathfrak{P}$ is governed by the residue extension; the pairing is nondegenerate on $\mathcal{O}_L/\mathfrak{P}$ exactly when the residue extension is separable with the same degree as the field extension, which by the fundamental identity means $e = 1$. (b) Norms of prime ideals are prime powers, so the prime divisors are the same. (c) If $e = 1$ then the different is coprime to $\mathfrak{P}$ by (a), so it is the unit ideal above $\mathfrak{p}$. $\square$

**Theorem (conductor–discriminant formula).** Let $L/K$ be a finite abelian extension and let $\widehat{G}$ be the group of irreducible characters of $G = \operatorname{Gal}(L/K)$. Then

$$
\mathfrak d_{L/K} = \prod_{\chi \in \widehat G} \mathfrak f(\chi),
$$

the product of the conductors of the characters, where the conductor of a character is defined by its vanishing on the corresponding congruence subgroup of the ray class group.

This is the arithmetic form of the factorisation of the discriminant, and it is stated and used in *Class Field Theory*, where the conductor $\mathfrak f(\chi)$ is defined; for a quadratic extension there are exactly two characters, the trivial one and the quadratic one whose conductor has norm $\lvert d_K\rvert$.

**Example.** For $L = \mathbb{Q}(\zeta_m)/\mathbb{Q}$, all the characters of $G \cong (\mathbb{Z}/m\mathbb{Z})^\times$ are one-dimensional, with conductors dividing $(m)\infty$; the conductor–discriminant formula gives $\lvert d_L\rvert = \prod_\chi f(\chi) = m^{\varphi(m)}$ up to the correction of the $2$-adic factors, and indeed the discriminant of $\mathbb{Q}(\zeta_m)$ is $(-1)^{\varphi(m)/2}m^{\varphi(m)}/\prod_{p \mid m}p^{\varphi(m)/(p-1)}$, the standard formula, as the values $5^3 = 125$ for $m = 5$ and $8^4/2^4 = 256$ for $m = 8$ illustrate. For $m = p$ prime this reads $d_{\mathbb{Q}(\zeta_p)} = (-1)^{(p-1)/2}p^{p-2}$.

**Example.** For a quadratic field $L = \mathbb{Q}(\sqrt d)$ with $d$ squarefree, the group has two characters, the trivial one of conductor $(1)$ and the quadratic character of conductor $\lvert d_L\rvert$, so the formula returns $\mathfrak d_{L/\mathbb{Q}} = \lvert d_L\rvert$, in agreement with the computation of the discriminant above.

---

## Examples

### Quadratic Fields

**Example.** For $K = \mathbb{Q}(\sqrt d)$ with $d$ squarefree, the primes that ramify are the divisors of $d$, together with $2$ when $d \equiv 2, 3 \bmod 4$. The splitting of an odd prime $p \nmid d$ is governed by the Legendre symbol: $p$ splits if $\left(\frac{d}{p}\right) = 1$, is inert if $\left(\frac{d}{p}\right) = -1$. For $d = -1$: $p \equiv 1 \bmod 4$ splits, $p \equiv 3 \bmod 4$ is inert. For $d = 5$: $p \equiv \pm1 \bmod 5$ splits, $p \equiv \pm2 \bmod 5$ is inert, and $5$ ramifies. For $d = -5$: $\left(\frac{-5}{p}\right) = 1$ for $p \equiv 1, 3, 7, 9 \bmod 20$, and $2, 5$ ramify.

### Cyclotomic Fields

**Example.** For $K = \mathbb{Q}(\zeta_m)$ with ring of integers $\mathbb{Z}[\zeta_m]$, the ramified primes are exactly the divisors of $m$, and an unramified prime $p$ has residue degree $f$ equal to the order of $p$ modulo $m$ and $g = \varphi(m)/f$ primes above it; this is *Cyclotomic Fields*. For $m = 8$: since $\zeta_8 = (1+i)/\sqrt2$ one has $\mathbb{Z}[\zeta_8] = \mathbb{Z}[\sqrt2,i]$, the ring of integers of $\mathbb{Q}(\zeta_8)$ is $\mathcal{O}_K = \mathbb{Z}[\zeta_8]$ with discriminant $d_K = 256$, the prime $2$ is totally ramified with $(2) = (1-\zeta_8)^4$, and an odd prime $p$ splits into $\varphi(8)/f = 4/f$ primes, where $f$ is the order of $p$ modulo $8$.

### Pure Cubic Fields

**Example.** Let $K = \mathbb{Q}(\sqrt[3]{m})$ with $m$ squarefree and $m \neq \pm1$. Then $\mathcal{O}_K$ need not equal $\mathbb{Z}[\sqrt[3]{m}]$; it does exactly when $m \not\equiv \pm1 \pmod 9$, and then $d_K = -27m^2$. For $m = 2$: $\mathcal{O}_K = \mathbb{Z}[\varrho]$, $d_K = -108$, the unit group has rank $r_1 + r_2 - 1 = 1 + 1 - 1 = 1$ and is generated by $\varrho - 1$ up to sign, since $(\varrho-1)(\varrho^2+\varrho+1) = \varrho^3 - 1 = 1$. The ramified primes are $2$ and $3$, both totally ramified.

**Example (unit rank).** The rank formula $r_1+r_2-1$ is checked against small fields in the table:

| $K$ | $n$ | $r_1$ | $r_2$ | rank of $\mathcal{O}_K^\times$ | $h_K$ |
|---|---|---|---|---|---|
| $\mathbb{Q}$ | $1$ | $1$ | $0$ | $0$ | $1$ |
| $\mathbb{Q}(i)$ | $2$ | $0$ | $1$ | $0$ | $1$ |
| $\mathbb{Q}(\sqrt{-5})$ | $2$ | $0$ | $1$ | $0$ | $2$ |
| $\mathbb{Q}(\sqrt2)$ | $2$ | $2$ | $0$ | $1$ | $1$ |
| $\mathbb{Q}(\sqrt[3]{2})$ | $3$ | $1$ | $1$ | $1$ | $1$ |
| $\mathbb{Q}(\zeta_5)$ | $4$ | $0$ | $2$ | $1$ | $1$ |
| $\mathbb{Q}(\zeta_7)$ | $6$ | $0$ | $3$ | $2$ | $1$ |

The class numbers are from *Dedekind Domains and Ideal Class Groups* and *Class Field Theory*; the ranks are $r_1 + r_2 - 1$.

---

## Summary

A number field is a finite extension $K$ of $\mathbb{Q}$ of degree $n$ with signature $(r_1,r_2)$ and $n = r_1+2r_2$. Its ring of integers $\mathcal{O}_K$ is the integral closure of $\mathbb{Z}$ in $K$, a free $\mathbb{Z}$-module of rank $n$, and a Dedekind domain; the discriminant $d_K$ is the discriminant of an integral basis and satisfies $d_K \equiv 0$ or $1 \bmod 4$. For quadratic fields, $\mathcal{O}_K$ and $d_K$ are computed explicitly from the residue of the squarefree $d$ modulo $4$.

Nonzero ideals of $\mathcal{O}_K$ factor uniquely into prime ideals, the class group $\operatorname{Cl}(\mathcal{O}_K)$ is finite of order $h_K$ and vanishes exactly for principal ideal domains, and the norm of an ideal is the index. A rational prime factors as $\mathfrak{p}\mathcal{O}_L = \prod \mathfrak{P}_i^{e_i}$ in an extension, with $\sum e_if_i = [L:K]$, and Dedekind's theorem computes the factorisation from the factorisation of the minimal polynomial modulo $\mathfrak{p}$; the primes that ramify are exactly the divisors of the discriminant. The Minkowski bound $M_K = \frac{n!}{n^n}(4/\pi)^{r_2}\sqrt{\lvert d_K\rvert}$ guarantees a representative of every ideal class of norm at most $M_K$, but its proof uses volume and is deferred to Part II; it implies the finiteness of the class group and $\lvert d_K\rvert > 1$ for $n \geq 2$. Dirichlet's unit theorem gives $\mathcal{O}_K^\times \cong \mu_K\oplus\mathbb{Z}^{r_1+r_2-1}$, its proof being deferred for the same reason. The different $\mathfrak{D}_{L/K}$, defined as the inverse of the trace-dual of $\mathcal{O}_L$, has $\mathfrak{P} \mid \mathfrak{D}_{L/K}$ exactly when $\mathfrak{p}$ ramifies, and its norm is the relative discriminant $\mathfrak d_{L/K}$; the conductor–discriminant formula computes the latter as the product of the conductors of the characters, as in *Class Field Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $L$ | Number fields, $n = [K:\mathbb{Q}]$ |
| $r_1$, $r_2$ | Number of real embeddings; number of conjugate pairs of complex embeddings |
| $\mathcal{O}_K$, $\mathcal{O}_L$ | Rings of integers |
| $\sigma_1, \ldots, \sigma_n$ | The distinct embeddings $K \hookrightarrow \mathbb{C}$ |
| $\operatorname{Tr}_{K/\mathbb{Q}}$, $\operatorname{N}_{K/\mathbb{Q}}$ | Field trace and norm |
| $\operatorname{disc}(\alpha_1,\ldots,\alpha_n)$ | Discriminant of an $n$-tuple |
| $d_K$ | Discriminant of $K$ |
| $\mathfrak{p}, \mathfrak{P}$ | Nonzero prime ideals of $\mathcal{O}_K$, of $\mathcal{O}_L$ over $\mathfrak{p}$ |
| $e$, $f$, $g$ | Ramification index, residue degree, number of primes above |
| $\operatorname{N}(\mathfrak{a})$ | Norm of an ideal |
| $I_K$ | Group of nonzero fractional ideals |
| $\operatorname{Cl}(\mathcal{O}_K)$, $h_K$ | Ideal class group, class number |
| $M_K$ | Minkowski bound |
| $\mathcal{O}_K^\times$, $\mu_K$ | Unit group, roots of unity in $K$ |
| $\operatorname{Reg}_K$ | Regulator |
| $\mathfrak{D}_{L/K}$, $\mathfrak{d}_{L/K}$ | Different, relative discriminant |
| $\mathfrak f(\chi)$ | Conductor of a character |
| $\varrho$ | Used for $\sqrt[3]{2}$ in the pure cubic example |



## Further Reading

- Richard Dedekind, "Über die Theorie der ganzen algebraischen Zahlen", *Supplement XI* to Dirichlet's *Vorlesungen über Zahlentheorie* (Vieweg, 1871), for the ring of integers, ideals and unique factorisation.
- Hermann Minkowski, "Zur Theorie der Einheiten in den algebraischen Zahlkörpern", *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen* (1900), 90–93, for the bound on the discriminant and the finiteness of the class group.
- Johann Peter Gustav Lejeune Dirichlet, "Einige Resultate von den unendlichen Reihen", *Journal für die reine und angewandte Mathematik* 21 (1840), 98–100, for the unit theorem and its rank.
- Erich Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen* (Akademische Verlagsgesellschaft, 1923), for the classical development of the ideal theory, the different and the discriminant.
- Serge Lang, *Algebraic Number Theory* (Springer, 2nd ed. 1994), for the systematic treatment of the different, the discriminant and the conductor–discriminant formula.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for the modern organisation of the subject by localisation and completions.
- Daniel Marcus, *Number Fields* (Springer, 1977), for concrete computations of rings of integers, discriminants and the splitting of primes.
- Henri Cohen, *A Course in Computational Algebraic Number Theory* (Springer, 1993), for algorithms for integral bases, discriminants, class groups and units.
