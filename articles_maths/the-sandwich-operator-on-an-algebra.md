# __The Sandwich Operator on an Algebra__

## Introduction

The product of an algebra makes two one-sided operators, the left multiplication $L(a)$ and the right multiplication $R(b)$. Composing them gives the **two-sided multiplication**, or sandwich,

$$
T_{a,b}(x) = a x b ,
$$

the operator that multiplies on the left by one element and on the right by another. It is the smallest operator that uses both sides of the product at once, and the whole of the present article is a reading of the algebra through it.

The sandwich is the place where associativity is tested. If the product is associative, the two bracketings of $axb$ agree and $T_{a,b}$ is a single operator with two factorisations, $T_{a,b} = L(a)R(b) = R(b)L(a)$; if the product is not associative, the two bracketings differ, and their difference is the **associator** $(a,x,b) = (ax)b - a(xb)$. The associator is therefore the obstruction to the commutation of the left and the right multiplication, and it is the second subject of the article.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra, not assumed commutative, of dimension $n = \dim_k A$ when $A$ is finite-dimensional. The operators live in $\operatorname{End}_k(A)$, whose ambient theory is *The Operators on an Algebra*; the left and the right multiplications $L(a)$ and $R(b)$ are those of that article, and the associator is the object of *Associative Algebras*. When the product is not assumed associative, the sandwich is still defined and the associator no longer vanishes; that case is named in one section and its identities belong to *Non-Associative Algebras and the Property Ladder*.

## The Two-Sided Operator

### Definition

**Definition.** Let $a, b \in A$. The **sandwich** determined by $a$ and $b$ is the operator

$$
T_{a,b} : A \longrightarrow A, \qquad T_{a,b}(x) = a x b .
$$

The image of the map $T : A \times A \to \operatorname{End}_k(A)$, $(a,b) \mapsto T_{a,b}$, is the **sandwich space**, written $\mathcal{S}(A)$.

The sandwich is $k$-linear in $x$, because the product is bilinear; it is $k$-linear in $a$ and in $b$ separately, so $T$ is a $k$-bilinear map of two arguments. Bilinearity is exactly the statement that

$$
T_{\alpha a + \alpha' a',\, b} = \alpha T_{a,b} + \alpha' T_{a',b},
$$

and likewise in the second argument, for $\alpha, \alpha' \in k$. The sandwich space is therefore a subspace of $\operatorname{End}_k(A)$, spanned by the operators $T_{a,b}$; equivalently it is the image of the $k$-linear map

$$
\widetilde T : A \otimes_k A \longrightarrow \operatorname{End}_k(A), \qquad \widetilde T(a \otimes b) = T_{a,b},
$$

whose existence is the universal property of the tensor product.

### Elementary Properties

**Proposition.** For all $a, b, a', b' \in A$ and $x \in A$,

**(a)** $T_{1,a} = L(a)$ and $T_{a,1} = R(a)$, where $1$ is the unit of $A$;

**(b)** $T_{a,b} = L(a) \circ R(b) = R(b) \circ L(a)$, the equality of the two factorisations being associativity;

**(c)** $T_{a,b}(1) = ab$.

*Proof.* (a) $T_{1,a}(x) = 1 \cdot x \cdot a = x a = R(a)(x)$ and $T_{a,1}(x) = a x$. (b) Both composites send $x$ to $a x b$: the left one as $a(xb)$ and the right one as $(ax)b$, equal by associativity. (c) $T_{a,b}(1) = a \cdot 1 \cdot b = ab$.

**Corollary.** The sandwich space contains the left multiplications, the right multiplications and the scalar operators, and

$$
k \cdot 1_{\operatorname{End}} \;\subseteq\; L(Z(A)) = R(Z(A)) = L(A) \cap R(A) \;\subseteq\; \mathcal{S}(A) \;\subseteq\; \operatorname{End}_k(A),
$$

where $1_{\operatorname{End}}$ is the identity operator $T_{1,1}$ and the middle equality is the statement that $L(a) = R(b)$ forces $a = b$ central.

The inner intersections are computed in *Left and Right Multiplication*; the composite space is the first and crudest invariant of the sandwich, and the exact size of $\mathcal{S}(A)$ inside $\operatorname{End}_k(A)$ is settled below.

### The Sandwich as a Bimodule Operator

The defining formula reads as an $A$-bimodule statement as soon as the regular bimodule is recognised.

**Proposition.** On the left regular module ${}_A A_A$ the operator $T_{a,b}$ is **right $A$-linear** for every $b$ and, when $a$ is central, left $A$-linear; precisely,

$$
T_{a,b}(x c) = T_{a,b}(x)\, c, \qquad T_{a,b}(c x) = T_{a, b}(c x),
$$

and the second equality rewrites as $T_{a,b}(cx) = a c x b$, so $T_{a,b}$ commutes with $L(c)$ exactly when $a c = c a$ for all $c$, that is when $a$ is central.

*Proof.* The first identity is $(a x c) b = (a x b) c$, which is associativity. For the second, $T_{a,b} L(c)(x) = a c x b$ and $L(c) T_{a,b}(x) = c a x b$, equal for all $x$ exactly when $a c = c a$; as $x = 1$ is available, no cancellation beyond the unit is needed.

The sandwich is thus the general shape of an operator that is right $A$-linear; the right multiplications $R(A)$ are the case $a = 1$, and they are the whole of the right $A$-linear operators by *The Operators on an Algebra*. For a noncentral $a$ the sandwich is right linear and not left linear, and it is therefore a point of the bimodule structure of $\operatorname{End}_k(A)$ but not of its $A$-linearly central part.

## The Multiplicative Rule

### Composition

**Theorem.** For all $a, b, c, d \in A$,

$$
T_{a,b} \circ T_{c,d} = T_{a c,\, d b}.
$$

*Proof.* Apply the right-hand operator first:

$$
T_{a,b}\bigl(T_{c,d}(x)\bigr) = a (c x d) b = (a c)\, x\, (d b) = T_{ac,\,db}(x),
$$

where the middle equality is associativity and the regrouping of the four factors.

The rule $T_{a,b}T_{c,d} = T_{ac,db}$ is the multiplication table of the sandwich space. It is not the product formula of the algebra $A \otimes_k A$, which would read $(a \otimes b)(c \otimes d) = ac \otimes bd$; the second factor is transposed, $d b$ rather than $bd$. The correct reading is over the **opposite algebra** and it is the content of the next statement.

**Corollary.** The map

$$
A \otimes_k A^{\mathrm{op}} \longrightarrow \operatorname{End}_k(A), \qquad a \otimes b \longmapsto T_{a,b}
$$

is a homomorphism of $k$-algebras onto the sandwich space.

*Proof.* In $A \otimes_k A^{\mathrm{op}}$ the product of generators is $(a \otimes b)(c \otimes d) = ac \otimes b \cdot_{\mathrm{op}} d = ac \otimes db$, which is exactly the index pair of $T_{ac,db}$, and the assignment is $k$-bilinear by construction.

The sandwich space is therefore the image of the **enveloping algebra** $A \otimes_k A^{\mathrm{op}}$ in $\operatorname{End}_k(A)$, and its dimension is that of $A \otimes_k A^{\mathrm{op}}$ modulo the kernel. The kernel consists of the tensors $\sum_i a_i \otimes b_i$ whose two-sided action vanishes, that is with $\sum_i a_i x b_i = 0$ for every $x$.

### The Invertible Sandwiches

**Theorem.** Let $A$ be finite-dimensional over $k$. The sandwich $T_{a,b}$ is invertible in $\operatorname{End}_k(A)$ if and only if $a$ and $b$ are units of $A$, and then

$$
T_{a,b}^{-1} = T_{a^{-1},\, b^{-1}} .
$$

*Proof.* If $a$ and $b$ are units, the composition rule gives $T_{a,b}T_{a^{-1},b^{-1}} = T_{1,1}$ and $T_{a^{-1},b^{-1}}T_{a,b} = T_{1,1}$. Conversely suppose $T_{a,b} = L(a)R(b)$ invertible; then $L(a)$ is surjective and $R(b)$ is injective. Since $A$ is finite-dimensional, $R(b)$ is bijective, so there is $c$ with $R(b)(c) = cb = 1$, and an element with a one-sided inverse in a finite-dimensional algebra is a unit; hence $b$ is a unit. Then $L(a) = T_{a,b}R(b)^{-1}$ is invertible, so $a$ is a unit as well.

**Corollary.** For a unit $u$ the sandwich $T_{u,u^{-1}}$ is the **inner automorphism** $\iota_u(x) = uxu^{-1}$ of *Automorphisms and Derivations of Algebras*, and the map $u \mapsto T_{u,u^{-1}}$ has kernel $Z(A)^\times$. Hence the inner automorphisms are exactly the sandwiches whose two elements are inverse to one another, and they form the quotient $A^\times/Z(A)^\times$ of the unit group.

*Proof.* The identity $T_{u,u^{-1}}(x) = uxu^{-1} = \iota_u(x)$ is the definition, and $\iota_u$ is an algebra automorphism by the cited article. The sandwich $T_{u,u^{-1}}$ is the identity operator exactly when $ux = xu$ for every $x$, that is when $u$ is central; with $u$ a unit this is $u \in Z(A)^\times$.

**Remark.** The invertible sandwiches form the group $A^\times \times A^\times$ under $(u,v) \mapsto T_{u,v}$, with composition $T_{u,v}T_{u',v'} = T_{uu',v'v}$; it acts on $A$ by $(u,v) \cdot x = u x v$, and it contains the inner automorphisms as the subgroup of pairs with $v = u^{-1}$. This is the operator reading of the group of units.

## The Associator

### Definition and the Two Readings

**Definition.** For $a, x, b \in A$ the **associator** of the triple is

$$
(a, x, b) = (a x) b - a (x b) .
$$

The algebra is **associative** exactly when every associator vanishes. The associator is $k$-trilinear in its three arguments; in the not-necessarily-associative case it is the primary measure of the failure of associativity, and the identities it satisfies are catalogued in *Non-Associative Algebras and the Property Ladder*.

The two readings of the definition are the following. Bracket the product to the right and the triple $a x b$ is the single element $a(xb)$; bracket it to the left and the product is $(ax)b$. The associator is their difference, so it lives in the algebra and not in the operator space, but it computes an operator: the difference of the two bracketings of the sandwich.

### The Associator and the Commutator of L and R

**Theorem.** For all $a, b \in A$,

$$
L(a) R(b) - R(b) L(a) = -A_{a,b}, \qquad \text{where} \qquad A_{a,b}(x) = (a, x, b) .
$$

Equivalently, $L(a)$ and $R(b)$ commute for all $a$ and $b$ if and only if the product is associative.

*Proof.* Evaluate on $x$:

$$
L(a)R(b)(x) - R(b)L(a)(x) = a(x b) - (a x) b = -\,\bigl((a x) b - a (x b)\bigr) = -A_{a,b}(x).
$$

The right-hand side vanishes for all $a$, $b$, $x$ exactly when every associator vanishes, which is associativity.

**Corollary.** An associative algebra is exactly a $k$-algebra in which the left and the right multiplications commute as operators; the sandwich is then the common value $L(a)R(b) = R(b)L(a)$ and the sandwich space satisfies $\mathcal{S}(A) = L(A)R(A) = R(A)L(A)$.

The corollary is the reason the sandwich is the natural carrier of the associativity axiom: the sandwich is defined with no hypothesis, and the hypothesis is precisely what makes its two factorisations agree. For a non-associative algebra the operator $L(a)R(b)$ is well defined but the sandwich $T_{a,b}$ is not; the two readings differ by the associator, and the correct general notion is the operator $L(a)R(b)$ together with its deviation. This is the sense in which the present article is the operator-theoretic reading of *Associative Algebras*.

### Linearity Properties

**Proposition.** Let the product be associative. Then for all $a, b, c \in A$,

**(a)** $T_{a,b}$ is right $A$-linear, $T_{a,b}(xc) = T_{a,b}(x)\,c$, and $T_{a,b}$ is left $A$-linear exactly when $a$ is central;

**(b)** the sandwich space is closed under composition, with $T_{a,b}T_{c,d} = T_{ac,db}$, and it is spanned by the products of a left and a right multiplication, $\mathcal{S}(A) = L(A)R(A)$.

*Proof.* Part (a) is the bimodule proposition above. Part (b): the composition rule is the theorem of the previous section, the space is spanned by the generators $T_{a,b} = L(a)R(b)$, and conversely each such product is a sandwich, so $\mathcal{S}(A) = L(A)R(A)$.

**Remark (the not-necessarily-associative case).** When the product need not be associative, the expression $a x b$ is ambiguous unless a bracket is fixed, and it is the operator $L(a)R(b)$ that is unambiguous; the associator then measures the deviation. The identities that survive the loss of associativity — flexibility, $(a, x, a) = 0$, and the power-associativity such an algebra retains — are those of *Non-Associative Algebras and the Property Ladder*. The present article reasons with the associative hypothesis throughout and names the failure rather than developing it.

## The Examples

### The Matrix Algebra

Let $A = M_n(k)$. The operators on $A$ form $M_{n^2}(k)$, of dimension $n^4$, and the sandwich map

$$
\widetilde T : M_n(k) \otimes_k M_n(k)^{\mathrm{op}} \longrightarrow \operatorname{End}_k(M_n(k))
$$

is an isomorphism, because $M_n(k)$ is central simple and the double centraliser theorem applies: the algebra generated by the left and the right multiplications is the whole operator algebra, and its dimension is $n^4$, matching the dimension of $M_n \otimes M_n^{\mathrm{op}}$. Hence **every $k$-linear operator on $M_n(k)$ is a sandwich**,

$$
\operatorname{End}_k(M_n(k)) = \mathcal{S}(M_n(k)), \qquad \dim_k \mathcal{S}(M_n(k)) = n^4 .
$$

This is the extreme case: the sandwich space is everything. In the basis of matrix units $E_{ij}$ the sandwich is $T_{E_{ij}, E_{kl}}(E_{pq}) = E_{ij}E_{pq}E_{kl} = \delta_{pi}\delta_{qk} E_{jl}$, an operator of rank one; the $n^4$ sandwiches with $a, b$ ranging over the matrix units are a basis of $\operatorname{End}_k(M_n(k))$.

### The Quaternion Algebra

Let $A = \mathbb{H}$, the real quaternions, of dimension $4$ over $\mathbb{R}$. The algebra is central simple over $\mathbb{R}$, so again every operator is a sandwich and

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{H}) = \mathcal{S}(\mathbb{H}) \cong \mathbb{H} \otimes_{\mathbb{R}} \mathbb{H}^{\mathrm{op}}, \qquad \dim_{\mathbb{R}} \mathcal{S}(\mathbb{H}) = 16 .
$$

The operators that are met here concretely are the left multiplications $T_{\tilde q,1} = L(\tilde q)$ and the right multiplications $T_{1,\tilde q} = R(\tilde q)$, of dimension $4$ each, and the sandwich $T_{\tilde q, \tilde q^{-1}} = \iota_{\tilde q}$ for an invertible $\tilde q$, an inner automorphism; the identity $T_{\tilde q,\tilde r}(x) = \tilde q x \tilde r$ is the quaternion product on the left and on the right at once. The identification of the anti-automorphisms realised by the sandwiches, and the reflection operators they give, belong to *Reflections as Signed Two-Sided Operators on an Algebra*, where the signed sandwich is developed; the present article stops at the unsigned case. No metric is read: the norm of a quaternion is a Part II object and is not used here.

### The Commutative Case

Let $A$ be commutative and associative. Then $L(a) = R(a)$ for every $a$, the left and the right multiplications coincide, and the sandwich collapses to a one-sided operator:

$$
T_{a,b} = L(ab) = R(ab), \qquad \mathcal{S}(A) = L(A) = R(A).
$$

The sandwich space is the multiplication algebra $L(A)$, of dimension $n$, strictly smaller than $\operatorname{End}_k(A)$ of dimension $n^2$ unless $n = 1$. For a commutative algebra the sandwich loses its two-sided character entirely; it is the operator of multiplication by the product $ab$, and every statement of the article reduces to a statement about the multiplication operator $L(a)$ of *Left and Right Multiplication*. This degeneration is the reason the sandwich is a notion of the noncommutative case.

### The Degenerate Sandwich

**Proposition.** The sandwich $T_{a,b}$ is the zero operator if and only if $aAb = 0$, that is $a x b = 0$ for every $x \in A$. In particular $T_{a,b} = 0$ forces $ab = 0$, and the converse holds when $A$ has a unit and $a$ is not a left zero divisor or $b$ is not a right zero divisor; over a domain the two conditions coincide with $a = 0$ or $b = 0$.

*Proof.* The operator $T_{a,b}$ vanishes exactly when $a x b = 0$ for every $x$, which is the stated condition, and $x = 1$ gives $ab = 0$. For the converse, if $ab = 0$ and $a$ is not a left zero divisor then $ab = 0$ gives $b = 0$, so $axb = 0$; symmetrically if $b$ is not a right zero divisor then $a = 0$. Over a domain, $aAb = 0$ says the product of the nonzero elements $a$, $x$ and $b$ vanishes, so one of the three is zero for each $x$; taking $x = 1$ gives $ab = 0$ and hence $a = 0$ or $b = 0$.

The degenerate sandwich is the operator form of the two-sided zero divisor, and it is the reason the map $A \otimes_k A^{\mathrm{op}} \to \operatorname{End}_k(A)$ need not be injective: the kernel consists of the tensors $\sum_i a_i \otimes b_i$ whose two-sided action vanishes, that is with $\sum_i a_i x b_i = 0$ for every $x$. A single generator $a \otimes b$ lies in the kernel exactly when $T_{a,b} = 0$.

## Summary

The sandwich is the operator $T_{a,b}(x) = axb$, $k$-linear in $x$ and $k$-bilinear in $a$ and $b$, with $T_{1,a} = R(a)$, $T_{a,1} = L(a)$ and $T_{a,b}(1) = ab$. In an associative algebra it has the two equal factorisations $T_{a,b} = L(a)R(b) = R(b)L(a)$, and the sandwiches compose by $T_{a,b}T_{c,d} = T_{ac,db}$, so that $a \otimes b \mapsto T_{a,b}$ is a $k$-algebra homomorphism $A \otimes_k A^{\mathrm{op}} \to \operatorname{End}_k(A)$ onto the sandwich space. A sandwich is invertible exactly when both its elements are units, with $T_{a,b}^{-1} = T_{a^{-1},b^{-1}}$, and $T_{u,u^{-1}}$ is the inner automorphism $\iota_u$; the inner automorphisms are thus the invertible sandwiches with inverse factors.

Associativity is exactly the vanishing of the associator $(a,x,b) = (ax)b - a(xb)$, and the associator is the negative of the commutator of the one-sided multiplications,

$$
L(a)R(b) - R(b)L(a) = -A_{a,b}, \qquad A_{a,b}(x) = (a,x,b),
$$

so the left and the right multiplications commute for all pairs precisely when the product is associative. For $M_n(k)$ and for $\mathbb{H}$, which are central simple, the sandwich map is an isomorphism and every operator is a sandwich, of dimension $n^4$ and $16$ respectively; for a commutative algebra the two sides collapse, $T_{a,b} = L(ab)$ and the sandwich space is the $n$-dimensional multiplication algebra; and a sandwich vanishes exactly when $aAb = 0$, which for a domain forces $a$ or $b$ to vanish. The signed analogue of the sandwich, in which the middle argument is twisted by an involutive automorphism, is the subject of *The Signed Sandwich on an Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A$ | a unital associative $k$-algebra |
| $n = \dim_k A$ | the dimension, when finite |
| $L(a)$, $L(a)(x) = ax$ | the left multiplication |
| $R(a)$, $R(a)(x) = xa$ | the right multiplication |
| $T_{a,b}(x) = axb$ | the sandwich, or two-sided multiplication |
| $\mathcal{S}(A) = L(A)R(A)$ | the sandwich space, the image of $T$ |
| $\widetilde T$ | the map $A \otimes_k A^{\mathrm{op}} \to \operatorname{End}_k(A)$, $a \otimes b \mapsto T_{a,b}$ |
| $(a,x,b) = (ax)b - a(xb)$ | the associator |
| $A_{a,b}$ | the operator $x \mapsto (a,x,b)$ |
| $\iota_u(x) = uxu^{-1}$ | the inner automorphism by a unit $u$, equal to $T_{u,u^{-1}}$ |
| $A^{\mathrm{op}}$ | the opposite algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the multiplication algebra of an associative algebra and the two-sided multiplications.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the algebra generated by the left and the right multiplications and the double centraliser theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the regular bimodule and the operators on it.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, Mathematical Association of America, 1968), for the central simple case and Skolem–Noether.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the associator in the not-necessarily-associative setting and the identities that replace associativity.
