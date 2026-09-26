
# __Central Simple Algebras and the Brauer Group__

## Introduction

A **central simple algebra** over a field $F$ is a finite-dimensional $F$-algebra with centre exactly $F$ and no two-sided ideal other than $0$ and the algebra itself. These are the algebras that behave, over an arbitrary field, as the matrix algebras behave over an algebraically closed one: every one of them becomes a full matrix algebra after a suitable extension of scalars, and every one of them is a matrix algebra over a division algebra, by Wedderburn's structure theorem. They are the natural home of the Skolem–Noether theorem, of the notion of similarity, and of the tensor product; and the classes of central simple algebras under similarity form a group, the **Brauer group** $\operatorname{Br}(F)$, which is the subject of this article.

The article develops the theory from the definition of a central simple algebra. The facts used are stated as standard: that a finite-dimensional algebra over a field without zero divisors is a division algebra; that the tensor product of central simple algebras is central simple; Frobenius' theorem; Wedderburn's little theorem; and the Skolem–Noether theorem. What this article adds is the systematic theory: the structure and dimension of a central simple algebra, the index and the exponent, splitting fields, the crossed-product description of the classes, and the computation of the Brauer group for the standard fields. The generalisation from a field to a commutative ring is not developed here.

Everything is algebraic. The norm form of a quaternion algebra, the composition of quadratic forms, and the cohomological interpretation of the relative Brauer group over a local or global field are named where they belong and deferred to the articles that own them; in particular, the class-field-theoretic identifications belong to the Part I article *Class Field Theory*, in the category *Rings and Fields*.

## Central Simple Algebras

### Definition and first properties

**Definition.** Let $F$ be a field. A finite-dimensional $F$-algebra $A$ with $1 \neq 0$ is **central** if its centre is $F \cdot 1_A$, and **central simple** if in addition the only two-sided ideals of $A$ are $0$ and $A$.

Throughout this article $F$ is a field and $A$, $B$ are finite-dimensional unital associative $F$-algebras, and all tensor products are over $F$ unless a subscript says otherwise.

**Proposition.** Let $A$ be central simple over $F$.

1. $A$ is a division algebra if and only if $A$ has no zero divisors, by the standard finite-dimensional criterion (a finite-dimensional algebra over a field with no zero divisors is a division algebra).
2. Every nonzero two-sided ideal of $A \otimes_F L$ meets $A$ trivially, for every field extension $L/F$; equivalently $A \otimes_F L$ is simple.
3. The centre of $A \otimes_F L$ is $L \cdot 1$, so $A \otimes_F L$ is central simple over $L$.

*Proof.* Statement 1 is the standard finite-dimensional criterion. For 2 and 3, the centre statement is standard: it is proved by extending scalars to an algebraic closure, where the algebra becomes a matrix algebra; the simplicity is the standard argument that a nonzero ideal of $A \otimes_F \bar F$ intersects $M_n(\bar F)$ in a nonzero ideal, hence contains a matrix unit, and the matrix units generate. $\square$

Thus centrality and simplicity are preserved by **base change**, which is the technical heart of the theory: an $F$-algebra is central simple exactly when it becomes a matrix algebra over a suitable extension, in a sense made precise by the notion of a splitting field below.

### Examples

**(a) Matrix algebras.** For every $n \geq 1$, the algebra $M_n(F)$ is central simple: its centre is $F I_n$, by the computation, and it is simple because the matrix units generate it from any nonzero element.

**(b) Division algebras.** A finite-dimensional division algebra $D$ over $F$ is simple, and it is central simple exactly when its centre is $F$.

**(c) Quaternion algebras.** Let $F$ be a field of characteristic not $2$ and let $a, b \in F^\times$. The **quaternion algebra** $(a,b)_F$ has $F$-basis $1, u, v, w$ with

$$
u^2 = a, \qquad v^2 = b, \qquad uv = w = -vu .
$$

It is central: $u, v, w$ each anticommute with one another and the only central elements are the scalars. It is simple of dimension $4$, hence, by Wedderburn's structure theorem below, either a division algebra or $M_2(F)$. For $F = \mathbb{R}$ and $a = b = -1$ it is $\mathbb{H}$; for $a = b = 1$ the element $1 + u$ is a zero divisor and the algebra is $M_2(\mathbb{R})$. The quaternion algebras are the four-dimensional central simple algebras, and their classification is the first case of the general theory.

**(d) The biquaternions are not central over $\mathbb{R}$.** The algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ has centre $\mathbb{C}$, so it is simple but not central over $\mathbb{R}$; over $\mathbb{C}$ it is $M_2(\mathbb{C})$ and is central simple. This is the distinction that the phrase "central *over* $F$" records, and it is why the ground field is named at each step.

**(e) A non-example.** The split-complex algebra $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$ is commutative and the dual numbers $\mathbb{D}' = \mathbb{R}[x]/(x^2)$ are not simple. Neither is central simple. The group algebra $\mathbb{C}[G]$ of a finite group is central simple only in the trivial case $G = 1$: otherwise it is a product of two or more ideals.

### The dimension is a square

**Theorem.** Let $A$ be central simple over $F$ of finite dimension $n = \dim_F A$. Then $A \otimes_F \bar F \cong M_d(\bar F)$ where $\bar F$ is an algebraic closure of $F$, and $n = d^2$.

*Proof.* By the proposition above, $A \otimes_F \bar F$ is central simple over the algebraically closed field $\bar F$. Over an algebraically closed field the only finite-dimensional division algebra is the field itself; and Wedderburn's structure theorem writes a central simple algebra over $\bar F$ as $M_d(\bar F)$. Comparing dimensions, $n = d^2$. $\square$

The integer $d$ is the **degree** of $A$, written $\deg(A)$. It is a numerical invariant of $A$ and not of a presentation: the dimension of a central simple algebra is always a perfect square. The theorem also shows that simplicity is a property detectable after base change, since the matrix algebra $M_d(\bar F)$ is visibly central simple.

## The Structure of Central Simple Algebras

### Wedderburn's structure theorem

**Theorem (Wedderburn, standard).** Every finite-dimensional central simple $F$-algebra $A$ is isomorphic to a matrix algebra $M_n(D)$ over a central $F$-division algebra $D$, with $n \geq 1$ and $D$ determined up to isomorphism. Equivalently, writing $A = \operatorname{End}_D(V)$ for the unique simple $A$-module $V = D^n$, the division algebra is $D = \operatorname{End}_A(V)^{\mathrm{op}}$.

*Pro.* The algebra $A$ is simple and finite-dimensional, so by the Wedderburn–Artin theorem it is $M_n(D)$ for a division algebra $D$; the centre of $M_n(D)$ is the centre of $D$, computed, so centrality of $A$ makes $D$ central over $F$. Uniqueness follows because $D$ is recovered as $\operatorname{End}_A(V)^{\mathrm{op}}$ for the unique simple module $V$, and the simple module is unique because $A$ is simple. $\square$

The theorem reduces the classification of central simple algebras to the classification of central division algebras together with the integer $n$. The division algebra $D$ is called the **division algebra part** of $A$, and

$$
\deg(A) = n \sqrt{\dim_F D}, \qquad \operatorname{ind}(A) := \sqrt{\dim_F D}
$$

defines the **index** of $A$. The index is a positive integer, $\deg(A) = n \cdot \operatorname{ind}(A)$, and $\operatorname{ind}(A) = 1$ exactly when $A$ is a matrix algebra over $F$, in which case $A$ is called **split**.

### Skolem–Noether and inner automorphisms

**Theorem (Skolem–Noether, standard).** Let $A$ be central simple over $F$, let $B$ be a simple $F$-subalgebra of $A$, and let $f, g : B \to A$ be two unital $F$-algebra homomorphisms. Then there is a unit $a \in A^\times$ with

$$
g(b) = a\, f(b)\, a^{-1} \qquad \text{for all } b \in B .
$$

The theorem is stated as standard, and two corollaries are used repeatedly.

**Corollary.** For a central simple algebra $A$ the map $A^\times \to \operatorname{Aut}_F(A)$, $a \mapsto (x \mapsto axa^{-1})$, is surjective with kernel $F^\times$, so

$$
\operatorname{Aut}_F(A) \cong A^\times / F^\times .
$$

In particular two matrix algebras $M_n(D)$ and $M_m(D')$ over division algebras are isomorphic if and only if $n = m$ and $D \cong D'$, and the embeddings of a separable subfield of $A$ into $A$ are conjugate.

**Example (the real quaternions, and the commutative boundary).** For $A = \mathbb{H}$ over $\mathbb{R}$ the corollary gives $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times$: every $\mathbb{R}$-automorphism of $\mathbb{H}$ is conjugation by a unit, the kernel of $\mathbb{H}^\times \to \operatorname{Inn}(\mathbb{H})$ being the centre $\mathbb{R}^\times$, and each such automorphism preserves the norm form $N(Q) = Q\bar Q$. The same computation is carried out in *Division Algebras*. In the commutative case the statement is empty, because $\operatorname{Inn}(A)$ is trivial there; for example $\mathbb{C}$ is simple over $\mathbb{R}$ but not central, and complex conjugation is an $\mathbb{R}$-automorphism of $\mathbb{C}$ that is not inner. Centrality is exactly what the theorem needs and cannot be dropped.

**Corollary (the double centralizer theorem).** Let $B$ be a simple $F$-subalgebra of $A$ with centre $L$. Then the centralizer $C_A(B)$ is simple, $B \otimes_L C_A(B) \cong A$ as $L$-algebras, and

$$
\dim_F A = \dim_F B \cdot \dim_F C_A(B) .
$$

*Proof.* The centralizer is an $L$-algebra containing $L$, and the map $B \otimes_L C_A(B) \to A$, $b \otimes c \mapsto bc$, is an injective homomorphism of $L$-algebras; since $A$ is simple and $B \otimes_L C_A(B)$ is a tensor product of central simple $L$-algebras by the tensor product theorem below, the map is an isomorphism. Taking dimensions gives the formula. $\square$

### The reduced trace and the opposite algebra

For a central simple algebra $A$ of degree $d$, choose a splitting field $L$ with $A \otimes_F L \cong M_d(L)$ and define the **reduced trace** and **reduced norm**

$$
\operatorname{Trd} : A \to F, \qquad \operatorname{Nrd} : A \to F
$$

so that after base change they become the matrix trace and determinant. Both take values in $F$ and are independent of the splitting field chosen; the reduced trace is $F$-linear, $\operatorname{Trd}(ab) = \operatorname{Trd}(ba)$, and the reduced norm is multiplicative, $\operatorname{Nrd}(ab) = \operatorname{Nrd}(a)\operatorname{Nrd}(b)$. The **opposite algebra** $A^{\mathrm{op}}$ has the same underlying $F$-vector space and product $a \cdot_{\mathrm{op}} b = ba$. It is central simple, of the same degree as $A$, and it is anti-isomorphic to $A$; the transpose map on a matrix algebra identifies $M_n(F)^{\mathrm{op}} \cong M_n(F)$, and quaternion conjugation identifies $\mathbb{H}^{\mathrm{op}} \cong \mathbb{H}$.

The opposite algebra is the reason the Brauer group has inverses. For every central simple $A$ of degree $d$ there is an isomorphism

$$
A \otimes_F A^{\mathrm{op}} \;\cong\; \operatorname{End}_F(A) \;\cong\; M_{d^2}(F),
$$

the first map being $a \otimes b \mapsto (x \mapsto axb)$, which is an injective algebra homomorphism because the tensor product is simple, and hence an isomorphism by the dimension count $d^2 \cdot d^2 = (d^2)^2$. So the tensor product of a central simple algebra with its opposite is split.

## The Brauer Group

### The tensor product of central simple algebras

**Theorem.** If $A$ and $B$ are central simple over $F$, then $A \otimes_F B$ is central simple over $F$, of degree $\deg(A)\deg(B)$ and dimension $(\dim_F A)(\dim_F B)$.

The theorem is standard, and the article uses it as such: the centre is computed from the centre of each factor, and simplicity follows by extending scalars to a splitting field, where the tensor product of two matrix algebras is a matrix algebra. The theorem is what allows the tensor product to be used as a group operation; without it the classes below would not be closed under multiplication.

### Similarity

**Definition.** Two central simple $F$-algebras $A$ and $B$ are **similar**, written $A \sim B$, if

$$
A \otimes_F M_m(F) \cong B \otimes_F M_n(F) \qquad \text{for some } m, n \geq 1 .
$$

By Wedderburn's structure theorem this is equivalent to the assertion that the division algebras $D_A$ and $D_B$ underlying $A$ and $B$ are isomorphic, so similarity is an equivalence relation, and each class has a unique representative up to isomorphism that is a division algebra. We write $[A]$ for the class of $A$ and speak of the **division algebra representative** of $[A]$.

**Lemma.** Similarity is compatible with the tensor product: if $A \sim A'$ and $B \sim B'$ then $A \otimes_F B \sim A' \otimes_F B'$.

*Proof.* It suffices to check that $A \otimes M_m(F) \sim A$ for all $m$, since then

$$
(A \otimes M_m(F)) \otimes (B \otimes M_n(F)) \;\cong\; (A \otimes B) \otimes (M_m(F) \otimes M_n(F)) \;\cong\; (A\otimes B)\otimes M_{mn}(F)
$$

and the tensor products in the statement may be replaced one factor at a time. But $A \otimes_F M_m(F) \cong M_m(A)$, which is a matrix algebra over $A$, hence similar to $A$ by definition. $\square$

### The group law

**Theorem (the Brauer group).** The set of similarity classes of central simple $F$-algebras, with product

$$
[A] \cdot [B] := [A \otimes_F B]
$$

and identity the class of $F$, is an abelian group, the **Brauer group** $\operatorname{Br}(F)$. The inverse of $[A]$ is $[A^{\mathrm{op}}]$, and every element has finite order.

*Proof.* The product is well defined by the lemma, associative and commutative because the tensor product of algebras is associative and commutative up to canonical isomorphism, and unital because $A \otimes_F F \cong A$. The class of $A^{\mathrm{op}}$ is inverse to that of $A$ by the isomorphism $A \otimes_F A^{\mathrm{op}} \cong M_{d^2}(F)$ above. Finiteness of the order is the theorem of the next subsection: the order of $[A]$ is the exponent, and it divides the index, which is finite. $\square$

The group is abelian but generally not finite: over $\mathbb{Q}$ and over every number field it is infinite, by the theorem of Hasse, Brauer and Noether recalled below.

### Splitting fields, index and exponent

**Definition.** A **splitting field** of a central simple $F$-algebra $A$ is a field extension $L/F$ with

$$
A \otimes_F L \;\cong\; M_d(L), \qquad d = \deg(A) .
$$

Every central simple algebra has a splitting field: an algebraic closure of $F$ splits it, by the dimension theorem of the second section. The interest of the notion is that a splitting field of finite degree exists, and the degree of the smallest one is the index.

**Theorem (standard).** Let $A$ be central simple over $F$, of degree $d$ and index $e$. Then:

1. A field extension $L/F$ splits $A$ if and only if $L$ contains a subfield isomorphic to a maximal subfield of the division algebra representative $D$ of $A$.
2. The index $e$ is the degree of every maximal subfield of $D$, and every such subfield has degree $e$ over $F$.
3. There is a splitting field of degree $e$ over $F$, namely any maximal subfield of $D$; consequently the index divides the degree of every splitting field, and in particular $e \mid d = \deg(A)$.
4. The **exponent** $\exp(A)$, the order of $[A]$ in $\operatorname{Br}(F)$, divides the index $e$.

*Proof.* Statements 1 and 2 are the standard theory of maximal subfields of a division algebra; the dimension count $\dim_F D = e^2$ and the double centralizer theorem give that a maximal subfield has degree $e$. For 3, a maximal subfield $L$ of $D$ has $D \otimes_F L \cong M_e(L)$ because $D$ becomes split over its own maximal subfield, the centralizer of $L$ in $D$ being $L$ itself; and every splitting field has degree divisible by $e$ by the same argument applied to $D \otimes_F L$. For 4, the exponent divides the index: if $K$ is a maximal subfield of $D$, then $[D]$ lies in $\operatorname{Br}(K/F)$, and the restriction–corestriction identity of the cohomological theory gives $[D]^{[K:F]} = [D]^{e} = 0$ in $\operatorname{Br}(F)$, since restriction to $K$ kills the class; alternatively the same conclusion follows from the reduced norm and the theory of the reduced characteristic polynomial. Either argument is the standard one, and both are recorded in the references. $\square$

The two invariants are related by the theorem: every central simple algebra is a crossed product with respect to a splitting field, and the resulting cohomological description of the Brauer group makes the exponent the order of a cohomology class.

### The relative Brauer group

For a field extension $L/F$, base change $A \mapsto A \otimes_F L$ is a homomorphism of groups,

$$
\operatorname{Br}(F) \longrightarrow \operatorname{Br}(L), \qquad [A] \longmapsto [A \otimes_F L],
$$

well defined by the compatibility of the tensor product with base change and the preservation of centrality and simplicity. Its kernel,

$$
\operatorname{Br}(L/F) := \ker\bigl(\operatorname{Br}(F) \to \operatorname{Br}(L)\bigr),
$$

is the **relative Brauer group** of $L/F$: the classes split by $L$. For a finite Galois extension $L/F$ with group $G$, the crossed-product description identifies

$$
\operatorname{Br}(L/F) \;\cong\; H^2(G, L^\times),
$$

the second cohomology group of $G$ with coefficients in the multiplicative group of $L$; the group cohomology is that of *Group Cohomology*. This is the cohomological face of the theory and the reason the exponent of a class is the order of a cohomology class.

## Crossed Products and Cyclic Algebras

### Cyclic algebras

The most explicit central simple algebras are the **cyclic algebras**. Let $L/F$ be a cyclic extension of degree $n$ with Galois group generated by $\sigma$, and let $a \in F^\times$. The cyclic algebra $(\chi, a)$ is the $F$-algebra

$$
(\chi, a) = L \oplus Lz \oplus \cdots \oplus Lz^{n-1}, \qquad z^n = a, \qquad z\ell = \sigma(\ell) z \quad (\ell \in L).
$$

It is central simple of degree $n$, and its class lies in $\operatorname{Br}(L/F)$. The construction is a special case of the crossed product, with factor set determined by the class of $a$ modulo norms from $L^\times$; the isomorphism classes of such algebras are parametrised by $F^\times/\operatorname{N}_{L/F}(L^\times)$, and the cyclic algebra is split exactly when $a$ is a norm from $L$. In the smallest case $n = 2$, with $L = F(\sqrt a)$ and $\sigma$ the nontrivial automorphism, the cyclic algebra $(\chi, b)$ is the quaternion algebra

$$
(a, b)_F = F(\sqrt a) \oplus F(\sqrt a) z, \qquad z^2 = b, \qquad z \sqrt a = -\sqrt a\, z ,
$$

which is the doubled description of the four-dimensional algebra of the first section. The algebra is a division algebra when $b$ is not a norm from $F(\sqrt a)$ and $M_2(F)$ otherwise.

### The crossed-product description

**Theorem (Noether–Deuring, standard).** Let $L/F$ be a finite Galois extension with group $G$, and let $A$ be a central simple $F$-algebra split by $L$. Then there is a $G$-graded $L$-algebra structure $A \otimes_F L = \bigoplus_{\sigma \in G} A_\sigma$ and a factor set $c : G \times G \to L^\times$ with

$$
A \otimes_F L \;\cong\; \bigoplus_{\sigma \in G} L u_\sigma, \qquad u_\sigma \ell = \sigma(\ell) u_\sigma, \qquad u_\sigma u_\tau = c(\sigma, \tau) u_{\sigma\tau},
$$

and the class of $A$ in $\operatorname{Br}(L/F) \cong H^2(G, L^\times)$ is the cohomology class of the factor set $c$. The factor set is a coboundary exactly when $A$ is split by $F$.

The theorem is the content, where the crossed product $L \rtimes_c G$ is defined and the isomorphism with $H^2(G, L^\times)$ is established; it is cited here because it explains both the name "Brauer group" and the structure of the cyclic algebras above. A central simple algebra need not be a crossed product with respect to every splitting field, and need not be cyclic; the question of which algebras are cyclic is a genuine restriction, settled for local fields by the theorem below and open in general.

## Computations of the Brauer Group

### Algebraically closed fields and finite fields

**Theorem.** If $F$ is algebraically closed, then $\operatorname{Br}(F) = 0$.

*Proof.* Over an algebraically closed field the only finite-dimensional division algebra is $F$ itself, so every central simple algebra is $M_n(F)$ and is similar to $F$. $\square$

**Theorem (Wedderburn).** If $F$ is a finite field, then $\operatorname{Br}(F) = 0$.

*Proof.* By Wedderburn's little theorem every finite division ring is a field, so the only finite-dimensional central division algebra over $\mathbb{F}_q$ is $\mathbb{F}_q$ itself. Wedderburn's structure theorem then makes every central simple $\mathbb{F}_q$-algebra a matrix algebra over $\mathbb{F}_q$, hence split. $\square$

The two results say that the Brauer group measures how far a field is from being algebraically closed or finite, and that the interesting cases are the number fields, the local fields and the function fields.

### The real and complex numbers

Over $\mathbb{R}$ the division algebras are $\mathbb{R}, \mathbb{C}, \mathbb{H}$ by Frobenius' theorem, and $\mathbb{C}$ is not central, so the only central division algebra besides $\mathbb{R}$ is $\mathbb{H}$. Therefore

$$
\operatorname{Br}(\mathbb{R}) \;\cong\; \mathbb{Z}/2\mathbb{Z},
$$

generated by $[\mathbb{H}]$, with $[\mathbb{H}]^2 = [\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H}] = [M_4(\mathbb{R})] = 0$; consistently, $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H} \cong M_4(\mathbb{R})$. Over $\mathbb{C}$, which is algebraically closed, the group is trivial. The **relative Brauer group** of $\mathbb{C}/\mathbb{R}$ is all of $\operatorname{Br}(\mathbb{R})$, since complexification sends $\mathbb{H}$ to $M_2(\mathbb{C})$; and $\operatorname{Br}(\mathbb{C}/\mathbb{R}) \cong H^2(\mathbb{Z}/2, \mathbb{C}^\times) \cong \mathbb{Z}/2$, the generator being the class of the nontrivial cocycle $\sigma \mapsto -1$ in the sense of the crossed-product theorem.

### Number fields and local fields

**Theorem (Hasse–Brauer–Noether, standard).** Let $F$ be a number field with places $v$, and for a finite-dimensional central division algebra $D$ over $F$ let $\operatorname{inv}_v(D) \in \mathbb{Q}/\mathbb{Z}$ be its Hasse invariant at $v$, which is zero for all but finitely many $v$. Then the map

$$
\operatorname{Br}(F) \longrightarrow \bigoplus_v \mathbb{Q}/\mathbb{Z}, \qquad [D] \longmapsto (\operatorname{inv}_v(D))_v
$$

is an isomorphism onto the subgroup of the direct sum consisting of the families whose sum is $0$ in $\mathbb{Q}/\mathbb{Z}$, and the index of $[D]$ is the order of the corresponding element of $\mathbb{Q}/\mathbb{Z}$ at any place with nonzero invariant.

This is the reciprocity law of class field theory, and it belongs to the article *Class Field Theory*; it is recorded here because it computes the Brauer group of a number field completely and shows that it is infinite, with $\operatorname{Br}(\mathbb{Q}) \cong \bigoplus_p \mathbb{Q}/\mathbb{Z} / \text{(the global relation)}$. For a non-Archimedean local field $F$ the same construction gives $\operatorname{Br}(F) \cong \mathbb{Q}/\mathbb{Z}$, the invariant of a cyclic algebra being $1/n$ for a degree-$n$ unramified cyclic algebra, and for $\mathbb{R}$ it gives $\operatorname{Br}(\mathbb{R}) \cong \frac{1}{2}\mathbb{Z}/\mathbb{Z} \subseteq \mathbb{Q}/\mathbb{Z}$. The local invariant map is additive, so tensor products correspond to sums of invariants, and the global isomorphism is the statement that a central simple algebra over a number field is determined by its local invariants subject to the single reciprocity relation.

### A table

| Field $F$ | $\operatorname{Br}(F)$ | Generators and remarks |
|---|---|---|
| algebraically closed | $0$ | every central simple algebra is $M_n(F)$ |
| finite $\mathbb{F}_q$ | $0$ | Wedderburn's little theorem |
| $\mathbb{R}$ | $\mathbb{Z}/2\mathbb{Z}$ | generated by $[\mathbb{H}]$, of index $2$ |
| $\mathbb{C}$ | $0$ | algebraically closed |
| local (non-Archimedean) | $\mathbb{Q}/\mathbb{Z}$ | invariant $1/n$ for a degree-$n$ unramified cyclic algebra |
| number field | $\bigoplus_v \mathbb{Q}/\mathbb{Z}$ with reciprocity | Hasse–Brauer–Noether |

## Summary

A **central simple algebra** over a field $F$ is a finite-dimensional $F$-algebra with centre $F$ and no nontrivial two-sided ideal. Its dimension is a perfect square $d^2$, it is a matrix algebra $M_n(D)$ over a central $F$-division algebra $D$ by Wedderburn's structure theorem, and its **index** $\operatorname{ind}(A) = \sqrt{\dim_F D}$ divides its degree $d$ and equals the degree of every maximal subfield of $D$. The **Skolem–Noether theorem** makes every $F$-algebra automorphism of a central simple algebra inner, so $\operatorname{Aut}_F(A) \cong A^\times/F^\times$, and the double centralizer theorem computes the centralizer of a simple subalgebra. The tensor product of two central simple algebras is central simple, so the similarity classes of central simple algebras form an abelian group under the tensor product, the **Brauer group** $\operatorname{Br}(F)$, with identity the class of $F$ and inverse the class of the opposite algebra, since $A \otimes_F A^{\mathrm{op}} \cong M_{d^2}(F)$.

A splitting field of $A$ is a field extension $L/F$ with $A \otimes_F L \cong M_d(L)$; a splitting field of degree $\operatorname{ind}(A)$ always exists, and the **exponent** of $A$, its order in $\operatorname{Br}(F)$, divides its index. For a finite Galois extension $L/F$ with group $G$, every central simple algebra split by $L$ is a crossed product, and the relative Brauer group is $\operatorname{Br}(L/F) \cong H^2(G, L^\times)$, so the Brauer group is the cohomological home of the factor-set classification; the cyclic algebras $(L/F, \sigma, a)$ are the explicit case. The computations are $\operatorname{Br}(F) = 0$ for algebraically closed and for finite $F$, $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2$ generated by $[\mathbb{H}]$ with $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H} \cong M_4(\mathbb{R})$, $\operatorname{Br}(F) \cong \mathbb{Q}/\mathbb{Z}$ for a non-Archimedean local field, and for a number field the Hasse–Brauer–Noether isomorphism onto the families of local invariants with zero sum, which belongs to *Class Field Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $L$ | fields; $L/F$ a field extension |
| $A$, $B$ | central simple $F$-algebras |
| $A^{\mathrm{op}}$ | opposite algebra, $a \cdot_{\mathrm{op}} b = ba$ |
| $M_n(F)$ | matrix algebra, central simple of dimension $n^2$ |
| $D$ | central $F$-division algebra, the division algebra part of $A$ |
| $(a,b)_F$ | quaternion algebra, $u^2 = a$, $v^2 = b$, $uv = -vu$ |
| $\mathbb{H}, \mathbb{B}$ | real quaternions; biquaternions, central over $\mathbb{C}$ but not over $\mathbb{R}$ |
| $\deg(A) = \sqrt{\dim_F A}$ | degree of a central simple algebra |
| $\operatorname{ind}(A) = \sqrt{\dim_F D}$ | index, the degree of a maximal subfield of $D$ |
| $\exp(A)$ | exponent, the order of $[A]$ in $\operatorname{Br}(F)$ |
| $A \sim B$ | similarity: $A \otimes M_m(F) \cong B \otimes M_n(F)$ for some $m,n$ |
| $\operatorname{Br}(F)$ | Brauer group: similarity classes under $\otimes_F$ |
| $\operatorname{Br}(L/F)$ | relative Brauer group, classes split by $L$ |
| $\operatorname{Trd}, \operatorname{Nrd}$ | reduced trace and reduced norm |
| $C_A(B)$ | centralizer of $B$ in $A$ |
| $\operatorname{Aut}_F(A) \cong A^\times/F^\times$ | automorphisms, all inner (Skolem–Noether) |
| $(\chi, a)$ or $(L/F, \sigma, a)$ | cyclic algebra, $z^n = a$, $z\ell = \sigma(\ell)z$ |
| $H^2(G, L^\times)$ | second cohomology, $\cong \operatorname{Br}(L/F)$ for $G = \operatorname{Gal}(L/F)$ |
| $\operatorname{inv}_v(D)$ | Hasse invariant at a place $v$ |





## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of central simple algebras, the Brauer group and the Skolem–Noether theorem.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the double centralizer theorem and the theory of simple algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for central simple algebras, splitting fields and the exponent–index relation.
- Philippe Gille and Tamás Szamuely, *Central Simple Algebras and Galois Cohomology* (Cambridge, 2006), for the crossed-product description, the relative Brauer group and the cohomological theory.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the local invariant map and the Brauer group of a local field.
- Jürgen Neukirch, Alexander Schmidt and Kay Wingberg, *Cohomology of Number Fields* (Springer, 2nd ed. 2008), for the Hasse–Brauer–Noether theorem and the Brauer group of a number field.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for algebras with involution and the deeper structure of central simple algebras.
