
# __Degenerate Clifford Algebras and the Radical__

## Introduction

A quadratic form can fail to be non-degenerate, and when it does the Clifford algebra acquires a nilpotent factor that is invisible in the non-degenerate theory. The failure is concentrated in the **radical** of the form, the submodule of vectors orthogonal to everything; the radical is totally isotropic, its Clifford generators square to zero and anticommute, and the algebra they generate is the exterior algebra on the radical. The Clifford algebra of a degenerate form is therefore the graded tensor product of the Clifford algebra of the reduced non-degenerate form and an exterior algebra, and the radical generates a nilpotent ideal that is the ring-theoretic radical of the algebra.

This article proves the reduction, identifies the nilpotent factor, computes the rank, and gives the criterion for semisimplicity. The base is a commutative ring $R$ in which $2$ is invertible, the module is free of finite rank, and the form may be degenerate. The construction of the Clifford algebra, the fundamental relation and the graded tensor product are from *The Clifford Algebra*; the radical and non-degeneracy of a form are from *Bilinear Forms*; the exterior algebra is from *The Exterior Algebra*. The non-degenerate case is developed, whose basis, filtration and centre are cited rather than repeated.

## The Radical of a Quadratic Form

### Definition and First Properties

**Definition.** The **radical** of a quadratic form $q$ on $V$ with polar form $B$ is the submodule

$$
\operatorname{rad}(q) = \{v \in V : B(v, w) = 0 \text{ for all } w \in V\}.
$$

Equivalently, $\operatorname{rad}(q)$ is the kernel of the linear map $V \to V^*$, $v \mapsto B(v, \cdot)$. The form is **non-degenerate** exactly when this map is an isomorphism; over a field that is the same as $\operatorname{rad}(q) = 0$, while over a general commutative ring the map must also be surjective.

**Proposition.** The radical is a totally isotropic subspace, and $q$ vanishes on it:

$$
v \in \operatorname{rad}(q) \implies q(v) = B(v, v) = 0.
$$

**Proof.** Take $w = v$ in the defining condition. $\square$

**Proposition.** The radical is orthogonal to all of $V$ and contains every vector orthogonal to all of $V$; hence it is the largest totally isotropic subspace orthogonal to the whole space. For a subspace $W$ complementary to the radical, the restriction $q|_W$ is non-degenerate.

**Proof.** Orthogonality to all of $V$ is the definition. If $W$ is a complement, $V = W \oplus \operatorname{rad}(q)$, then a vector $w \in W$ orthogonal to all of $W$ is orthogonal to all of $V$, hence lies in $W \cap \operatorname{rad}(q) = 0$. $\square$

### The Reduced Form

**Proposition.** The form $q$ induces a quadratic form $\bar{q}$ on the quotient $V/\operatorname{rad}(q)$ by $\bar{q}(v + \operatorname{rad}(q)) = q(v)$, and the polar form of $\bar{q}$ is the induced bilinear form on the quotient; when $\operatorname{rad}(q)$ is a direct summand with complement $W$, the quotient is identified with $W$ and $\bar{q}$ with $q|_W$.

**Proof.** The form $q$ is constant on the cosets of the radical because for $r \in \operatorname{rad}(q)$ one has $q(v + r) = q(v) + 2B(v, r) + q(r) = q(v)$, using $B(v, r) = 0$ and $q(r) = 0$. The polar form descends by the same computation applied to $B$. $\square$

**Remark.** Over a field every subspace is a direct summand, so a complement $W$ always exists and $\bar{q}$ is a form on $W$. Over a general commutative ring the existence of a complement is an additional hypothesis, and it is assumed throughout the decomposition below.

## The Reduction to the Non-Degenerate Case

### The Splitting

Let $W$ be a complement of the radical, so that

$$
V = W \oplus \operatorname{rad}(q), \qquad q|_W = \bar{q} \text{ non-degenerate.}
$$

Because every element of $\operatorname{rad}(q)$ is orthogonal to every element of $V$, and in particular to every element of $W$, the decomposition is an **orthogonal** decomposition of quadratic spaces:

$$
(V, q) = (W, \bar{q}) \perp (\operatorname{rad}(q), 0),
$$

where $0$ denotes the zero form on the radical. The second summand is the zero form on a space that is its own radical.

### The Tensor Product Decomposition

**Theorem.** With $W$ a complement of $\operatorname{rad}(q)$, there is an isomorphism of $\mathbb{Z}/2$-graded algebras

$$
\mathrm{Cl}(V, q) \cong \mathrm{Cl}(W, \bar{q}) \,\hat{\otimes}\, \Lambda(\operatorname{rad}(q)),
$$

where $\Lambda(\operatorname{rad}(q))$ is the exterior algebra on the radical and $\hat\otimes$ is the graded tensor product of *The Clifford Algebra*.

**Proof.** The orthogonal decomposition above and the splitting theorem of *The Clifford Algebra* give

$$
\mathrm{Cl}(V, q) \cong \mathrm{Cl}(W, \bar{q}) \,\hat{\otimes}\, \mathrm{Cl}(\operatorname{rad}(q), 0),
$$

and $\mathrm{Cl}(\operatorname{rad}(q), 0) \cong \Lambda(\operatorname{rad}(q))$ because the defining relation $v^2 = 0$ on the second factor is exactly the defining relation of the exterior algebra. $\square$

**Proof by relations.** The same statement can be read off from the fundamental relation. Write $V = W \oplus \operatorname{rad}(q)$ and let $v, w \in W$ and $r, s \in \operatorname{rad}(q)$. The fundamental relation gives three families:

- $vw + wv = 2B(v, w)\cdot 1$ for $v, w \in W$, the relations of $\mathrm{Cl}(W, \bar{q})$;
- $vr + rv = 2B(v, r)\cdot 1 = 0$ for $v \in W$, $r \in \operatorname{rad}(q)$, so the generators of $W$ and of the radical anticommute;
- $rs + sr = 2B(r, s)\cdot 1 = 0$ for $r, s \in \operatorname{rad}(q)$, so the radical generators anticommute and each squares to zero, the relations of $\Lambda(\operatorname{rad}(q))$.

The first family generates the first factor, the third generates the second, and the second family is precisely the sign rule of the graded tensor product. $\square$

### Dependence on the Complement

**Proposition.** The isomorphism depends on the choice of complement $W$. Two complements $W, W'$ of the radical give algebras $\mathrm{Cl}(W, \bar{q})$ and $\mathrm{Cl}(W', \bar{q})$ that are isomorphic — the two projections of $W'$ onto $W$ along the radical define an isometry and hence an isomorphism of Clifford algebras — but the isomorphism between the two tensor product decompositions of $\mathrm{Cl}(V, q)$ depends on that choice.

**Proof.** The projection $W' \to W$ along $\operatorname{rad}(q)$ is an isometry for $\bar{q}$ because $\bar{q}$ is constant on cosets of the radical; it is bijective by symmetry of the decomposition. The induced isomorphism of Clifford algebras is the one from functoriality. $\square$

## The Nilpotent Factor and the Rank

### The Exterior Algebra on the Radical

Let $r_0 = \operatorname{rank}\operatorname{rad}(q)$ and let $r_1, \ldots, r_{r_0}$ be a basis of the radical. Then

$$
\Lambda(\operatorname{rad}(q)) = \bigoplus_{k \geq 0} \Lambda^k(\operatorname{rad}(q)),
$$

with basis the products $r_{i_1}\cdots r_{i_k}$ for $i_1 < \cdots < i_k$, and the generators satisfy

$$
r_i^2 = 0, \qquad r_ir_j = -r_jr_i \quad (i \neq j).
$$

Every element of $\bigoplus_{k \geq 1}\Lambda^k(\operatorname{rad}(q))$ is nilpotent, with nilpotency index at most $r_0 + 1$: a product of more than $r_0$ of the generators vanishes because some index repeats.

### The Rank

**Theorem.** Let $V$ be free of rank $n$ and $r_0 = \operatorname{rank}\operatorname{rad}(q)$. Then $\mathrm{Cl}(V, q)$ is free of rank

$$
\operatorname{rank}\mathrm{Cl}(V, q) = 2^{n - r_0} \cdot 2^{r_0} = 2^n.
$$

**Pro.** The graded tensor product of two free modules of ranks $2^{n - r_0}$ and $2^{r_0}$ is free of rank $2^{n - r_0} \cdot 2^{r_0} = 2^n$. The rank of the non-degenerate factor is the dimension count. $\square$

So the presence of a radical changes the structure but not the rank: it replaces part of the algebra by an exterior algebra on the same number of generators.

### The Nilpotent Ideal

**Theorem.** The image of $\operatorname{rad}(q)$ generates a two-sided ideal

$$
\mathfrak{n} = \operatorname{rad}(q)\cdot \mathrm{Cl}(V, q) = \mathrm{Cl}(V, q)\cdot \operatorname{rad}(q),
$$

which under the decomposition is $\mathrm{Cl}(W, \bar{q}) \otimes \bigoplus_{k\geq 1}\Lambda^k(\operatorname{rad}(q))$. The ideal $\mathfrak{n}$ is nilpotent, and the quotient $\mathrm{Cl}(V, q)/\mathfrak{n}$ is $\mathrm{Cl}(W, \bar{q})$. For a field $F$ of characteristic not $2$, $\mathfrak{n}$ is the Jacobson radical of $\mathrm{Cl}(V, q)$.

**Proof.** For $r \in \operatorname{rad}(q)$ and $x \in \mathrm{Cl}(V, q)$ the products $rx$ and $xr$ lie in $\mathfrak{n}$, so $\mathfrak{n}$ is a two-sided ideal; the decomposition identifies it with the positive part of the exterior factor tensored with the non-degenerate factor. Its $(r_0+1)$-st power vanishes because a product of $r_0 + 1$ radical generators vanishes, so $\mathfrak{n}^{r_0+1} = 0$. The quotient is obtained by setting the radical generators to zero, which is the defining presentation of $\mathrm{Cl}(W, \bar{q})$. A nilpotent ideal is contained in the Jacobson radical, and when $\mathrm{Cl}(W, \bar{q})$ is semisimple the quotient has zero Jacobson radical, so the two coincide. $\square$

**Corollary.** For a field $F$ of characteristic not $2$, $\mathrm{Cl}(V, q)$ is semisimple if and only if $q$ is non-degenerate.

**Proof.** If $q$ is non-degenerate then $\mathfrak{n} = 0$ and the algebra is $\mathrm{Cl}(W, \bar{q})$, which is semisimple as a finite-dimensional algebra over a field that is either simple or a product of two simple algebras. If $q$ is degenerate then $\mathfrak{n} \neq 0$ is nilpotent, so the algebra is not semisimple. $\square$

### The Nilpotency Index

**Theorem.** With the notation of the decomposition,

$$
\mathfrak{n}^k = \mathrm{Cl}(W, \bar{q}) \otimes \bigoplus_{j \geq k} \Lambda^j(\operatorname{rad}(q)),
$$

and if the radical is free of rank $r_0$ the nilpotency index of $\mathfrak{n}$ is exactly $r_0 + 1$.

**Proof.** A product of $k$ elements of $\mathfrak{n}$ involves at least $k$ radical generators in each of its terms after expansion in a basis of $\operatorname{rad}(q)$, so $\mathfrak{n}^k$ is contained in the displayed submodule. Conversely that submodule is spanned by the products $x\,r_{i_1}\cdots r_{i_j}$ with $x \in \mathrm{Cl}(W, \bar q)$ and $j \geq k$, each of which is a product of $k$ elements of $\mathfrak{n}$ when $j \geq k$: write it as $\bigl(x r_{i_1}\cdots r_{i_{j-k}}\bigr)\bigl(r_{i_{j-k+1}}\bigr)\cdots\bigl(r_{i_j}\bigr)$. Hence the two submodules coincide. For the index, $\Lambda^{r_0}(\operatorname{rad}(q)) \cong R$ with generator the product of a basis, which is nonzero in the free case; therefore $\mathfrak{n}^{r_0} = \mathrm{Cl}(W,\bar q)\otimes\Lambda^{r_0}(\operatorname{rad}(q))$ is nonzero as a free $R$-module, while $\mathfrak{n}^{r_0+1} = 0$ since there is no exterior degree above $r_0$. $\square$

Thus the nilpotency index grows linearly with the rank of the radical; in the non-degenerate case $\mathfrak{n} = 0$ and the algebra has no nilpotent factor at all.

### The Filtration by the Radical Ideal

The ideal $\mathfrak{n}$ is generated by the image of $\operatorname{rad}(q)$ in $\mathrm{Cl}(V,q)$, so it is independent of any choice of complement, and so is the decreasing filtration

$$
\mathrm{Cl}(V, q) = \mathfrak{n}^0 \supseteq \mathfrak{n}^1 \supseteq \mathfrak{n}^2 \supseteq \cdots \supseteq \mathfrak{n}^{r_0+1} = 0.
$$

**Proposition.** The successive quotients have rank

$$
\operatorname{rank}\bigl(\mathfrak{n}^k/\mathfrak{n}^{k+1}\bigr) = 2^{\,n - r_0}\binom{r_0}{k},
$$

so the associated graded has total rank $\sum_k 2^{n-r_0}\binom{r_0}{k} = 2^{n-r_0}\cdot 2^{r_0} = 2^n$, which is the rank of the algebra.

**Proof.** Choosing a complement identifies $\mathfrak{n}^k$ with $\mathrm{Cl}(W,\bar q)\otimes\bigoplus_{j\geq k}\Lambda^j(\operatorname{rad}(q))$ by the theorem above, and $\Lambda^k(\operatorname{rad}(q))$ is free of rank $\binom{r_0}{k}$; hence the quotient $\mathfrak{n}^k/\mathfrak{n}^{k+1}$ is free of the stated rank, and the identification of the associated graded is independent of the complement because the filtration is. $\square$

So the filtration detects the rank of the radical through the length of the filtration and the ranks of its quotients: the rank of $\mathfrak{n}/\mathfrak{n}^2$ is $2^{n-r_0}r_0$, which together with the length $r_0 + 1$ of the filtration determines $r_0$, and then $2^n$ determines $n - r_0$. This is the precise sense in which the Clifford algebra of a degenerate form retains the rank of the radical, even though it does not retain the form on it.

### The Split Extension

The decomposition also describes the algebra as an extension of a semisimple algebra by a nilpotent ideal.

**Theorem.** Let $\mathfrak{g} = \mathrm{Cl}(W, \bar q) \otimes 1$ be the image of the reduced Clifford algebra in $\mathrm{Cl}(V, q)$. Then $\mathfrak{g}$ is a subalgebra, $\mathfrak{n}$ is a two-sided ideal, $\mathfrak{g} \cap \mathfrak{n} = 0$ and $\mathfrak{g} + \mathfrak{n} = \mathrm{Cl}(V,q)$; hence

$$
\mathrm{Cl}(V, q) = \mathfrak{g} \oplus \mathfrak{n}
$$

as a direct sum of $R$-modules, the quotient map restricts to an isomorphism $\mathfrak{g} \to \mathrm{Cl}(V, q)/\mathfrak{n}$, and $\mathfrak{n}$ is the largest nilpotent two-sided ideal of the algebra.

**Proof.** The image of $\mathrm{Cl}(W,\bar q)$ under $x \mapsto x \otimes 1$ is a subalgebra because the map is an algebra homomorphism; the image of the positive part of the exterior algebra is $\mathfrak{n}$ by the theorem above, and the intersection is zero because the two factors meet only in degree zero on the second side: an element $x \otimes b$ with $b$ of positive degree is not of the form $y \otimes 1$. The ranks add, $2^{n - r_0} + 2^{n-r_0}(2^{r_0} - 1) = 2^n$, so the sum is everything, and the restriction of the quotient map is injective with image of full rank, hence an isomorphism. Finally $\mathfrak{n}$ is nilpotent and the Jacobson radical of the algebra, so it contains every nilpotent ideal. $\square$

**Remark.** This is the split extension of the semisimple algebra $\mathfrak{g} \cong \mathrm{Cl}(V,q)/\mathfrak{n}$ by the nilpotent bimodule $\mathfrak{n}$: the products of an element of $\mathfrak{g}$ with an element of $\mathfrak{n}$ lie in $\mathfrak{n}$, and the multiplication of the whole algebra is determined by the multiplication in $\mathfrak{g}$, the bimodule structure of $\mathfrak{n}$ and the multiplication inside $\mathfrak{n}$. When $r_0 = 1$ the interior product vanishes, so $\mathfrak{n}^2 = 0$ and the extension is a split null extension. The complement $\mathfrak{g}$ is not canonical, since it comes from the choice of $W$, while $\mathfrak{n}$ and the isomorphism class of the quotient are.

## The Degenerate and Non-Degenerate Cases Compared

The table records how each feature of the algebra behaves as the radical grows.

| Feature | Non-degenerate $q$ | Degenerate $q$ |
|---|---|---|
| $\operatorname{rad}(q)$ | $0$ | nonzero, totally isotropic |
| Decomposition | $\mathrm{Cl}(V, q)$ | $\mathrm{Cl}(W, \bar{q}) \,\hat\otimes\, \Lambda(\operatorname{rad}(q))$ |
| Rank | $2^n$ | $2^n$ |
| Centre | $R$ or $R \oplus R\omega$ | $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q))$, and $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q)) \oplus R\omega$ when $n$ is odd |
| Nilpotent ideal | none | nonzero, generating $\mathfrak{n}$ |
| Semisimple | yes | no |
| Quadratic form detected | up to isometry | only the reduced form |

The last line is the content of the reduction: the Clifford algebra of a degenerate form sees the form only through its non-degenerate part, and loses all information about the radical except its rank.

In the centre row $\omega = e_1 \cdots e_n$ denotes the volume element of an orthogonal basis of $V$, and $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q))$ is the even part of the exterior algebra on the radical, spanned by the products of an even number of radical generators. Moving $e_i$ past the $n - i$ generators to its right in $\omega e_i$ and past the $i - 1$ generators to its left in $e_i\omega$ gives $\omega e_i = (-1)^{n-i}a_i\,e_1\cdots\hat e_i\cdots e_n$ and $e_i\omega = (-1)^{i-1}a_i\,e_1\cdots\hat e_i\cdots e_n$, so $\omega e_i = (-1)^{n-2i+1}e_i\omega = (-1)^{n-1}e_i\omega$: for odd $n$ the volume element commutes with every generator and is therefore central. For the non-degenerate column this is the classical statement: the centre is $R$ for even $n$ and $R \oplus R\omega$ for odd $n$, which is the case $\operatorname{rad}(q) = 0$ of the degenerate entry, where $\Lambda^{\mathrm{ev}}(0) = R$. In the degenerate column the graded tensor product with $\Lambda(\operatorname{rad}(q))$ enlarges the even part of the centre, and two verifications give the count. First, an element $1 \otimes b$ with $b$ even commutes with every element of $\mathrm{Cl}(V, q)$: even elements of a supercommutative algebra commute with all elements of it, so $b$ passes the generators of $\mathrm{Cl}(W, \bar q)$ without a sign; this produces the subspace $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q))$, of rank $2^{r_0 - 1}$ when $r_0 \geq 1$ and of rank $1$ when $r_0 = 0$. Second, no central elements other than these and the multiples of $\omega$ occur. A homogeneous central term $a \otimes b$ must be graded-central in each of the two factors with parity twists dual to one another; the elements of the reduced non-degenerate factor that can occur are the scalars and the multiples of its volume element $\omega_W$, and the only even elements of $\Lambda(\operatorname{rad}(q))$ that can occur as the second factor are the even elements themselves, while an odd second factor must be a multiple of the radical volume element; so a term not of the form $1 \otimes b$ with $b$ even has $a$ a multiple of $\omega_W$ and $b$ a multiple of $\omega_{\operatorname{rad}}$, that is, it is a multiple of $\omega$, and such a term occurs exactly when $\dim W$ and $r_0$ have opposite parity, that is, when $n$ is odd. Hence the centre is $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q))$ for even $n$ and $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q)) \oplus R\omega$ for odd $n$. When $q = 0$ the reduced factor is $R$, and the formula reads $\Lambda^{\mathrm{ev}}(V)$ for even $n$ and $\Lambda^{\mathrm{ev}}(V) \oplus R\omega$ for odd $n$, which is the centre of the exterior algebra.

## Examples

### The Zero Form

If $q = 0$ then every vector is in the radical and $\operatorname{rad}(q) = V$; the complement is $0$ and $\bar{q}$ is the empty form. The theorem gives

$$
\mathrm{Cl}(V, 0) \cong \Lambda(V),
$$

so the Clifford algebra of the zero form is the exterior algebra, as it must be, since the defining relation $v^2 = 0$ is the defining relation of $\Lambda(V)$. This is the extreme degenerate case, and it is the one in which the nilpotent ideal is the whole positive part.

### The Dual Numbers

Let $R = \mathbb{R}$ and $V = \mathbb{R}$ with the zero form, $q(x) = 0$. Then $\operatorname{rad}(q) = V$ and

$$
\mathrm{Cl}(\mathbb{R}, 0) \cong \mathbb{R}[\varepsilon]/(\varepsilon^2), \qquad \varepsilon^2 = 0,
$$

which is the algebra of **dual numbers** $\mathbb{D}'$. This is the one-dimensional degenerate Clifford algebra, and its unit $\varepsilon$ is the radical generator; the algebra is local with maximal ideal $(\varepsilon)$, and it is the smallest example of a Clifford algebra with a nonzero radical. It is recorded in the number-system dictionary of the companion entry with this article.

### A Degenerate Form in Two Variables

Let $V = \mathbb{R}^2$ with $q(x, y) = x^2$. The polar form is $B((x, y), (x', y')) = xx'$, whose kernel is the line $\{(0, y)\} = \operatorname{rad}(q)$; a complement is the line spanned by $e_1$ with $\bar{q}(e_1) = 1$, so $\mathrm{Cl}(W, \bar{q}) \cong \mathbb{R}[t]/(t^2 - 1) \cong \mathbb{R}\times\mathbb{R}$, the split complex algebra $\mathbb{D}$. Write $e$ for the generator of the complement, $e^2 = 1$, and $\varepsilon$ for the generator of the radical, $\varepsilon^2 = 0$. The decomposition is

$$
\mathrm{Cl}(\mathbb{R}^2, x^2) \cong \mathbb{D}\,\hat{\otimes}\,\Lambda(\mathbb{R}), \qquad e^2 = 1, \quad \varepsilon^2 = 0, \quad e\varepsilon = -\varepsilon e,
$$

a four-dimensional algebra. The grading of $\mathbb{D}$ is nontrivial — its generator $e$ is odd — so the graded tensor product is not the ordinary tensor product, and the algebra is not the product of two copies of $\mathbb{R}[\varepsilon]/(\varepsilon^2)$: the idempotents $(1 \pm e)/2$ are not central, since $e\varepsilon = -\varepsilon e$, and the centre is only $\mathbb{R}$. The radical generator spans the nonzero nilpotent ideal $\mathfrak{n} = \operatorname{span}\{\varepsilon, e\varepsilon\}$ with $\mathfrak{n}^2 = 0$, and the reduced form is the one-dimensional form of square $+1$, in agreement with the rank count $2^2 = 4$.

### A Radical of Rank Two

Let $V = \mathbb{R}^3$ with $q(x, y, z) = x^2$, so that $\operatorname{rad}(q)$ is spanned by $e_2, e_3$ and the complement $W = \langle e_1\rangle$ carries the form of square $1$, whose Clifford algebra is the split complex algebra $\mathbb{D}$. The decomposition reads

$$
\mathrm{Cl}(\mathbb{R}^3, x^2) \cong \mathbb{D} \,\hat{\otimes}\, \Lambda(\mathbb{R}^2), \qquad \text{rank } 2 \cdot 4 = 8 = 2^3,
$$

with generators $e$ of square $1$ and $\varepsilon, \eta$ of square $0$, all three odd and mutually anticommuting. The nilpotent ideal has rank $6$, spanned by the elements containing a radical generator; its square is spanned by the two elements $\varepsilon\eta$ and $e\varepsilon\eta$ and is nonzero, while its cube vanishes. So the nilpotency index is $3 = r_0 + 1$, the value predicted by the theorem, and the nilpotent factor has index greater than $2$. The centre is $\Lambda^{\mathrm{ev}}(\operatorname{rad}(q)) \oplus \mathbb{R}\omega = \operatorname{span}\{1, \varepsilon\eta, e\varepsilon\eta\}$, of rank $3$, in agreement with the formula for odd $n$.

### A Non-Degenerate Reduced Factor

Let $V = \mathbb{R}^3$ with $q(x, y, z) = x^2 - y^2$, the hyperbolic plane on the first two coordinates and the zero form on the last. The radical is spanned by $e_3$, the reduced form is the hyperbolic plane, and $\mathrm{Cl}(W, \bar q) \cong M_2(\mathbb{R})$, the Clifford algebra of a hyperbolic plane being a matrix algebra. Hence

$$
\mathrm{Cl}(\mathbb{R}^3, x^2 - y^2) \cong M_2(\mathbb{R}) \,\hat{\otimes}\, \Lambda(\mathbb{R}), \qquad \text{rank } 4 \cdot 2 = 8,
$$

and the ideal $\mathfrak{n} = M_2(\mathbb{R}) \otimes \mathbb{R}\varepsilon$ has rank $4$ with $\mathfrak{n}^2 = 0$, so the nilpotency index is $2 = r_0 + 1$ with $r_0 = 1$. The example shows that the nilpotency index is governed by the rank of the radical alone and is independent of the size of the reduced algebra.

## Summary

The **radical** $\operatorname{rad}(q) = \{v : B(v, w) = 0 \ \forall w\}$ of a quadratic form is a totally isotropic subspace on which $q$ vanishes, and it is the kernel of the map $V \to V^*$ induced by the polar form; the form is non-degenerate exactly when the radical is zero. The form descends to the quotient by the radical, and when the radical is a direct summand with complement $W$, the reduced form $q|_W$ is non-degenerate and $(V, q) = (W, q|_W) \perp (\operatorname{rad}(q), 0)$.

The **decomposition theorem** states that for such a complement

$$
\mathrm{Cl}(V, q) \cong \mathrm{Cl}(W, q|_W) \,\hat{\otimes}\, \Lambda(\operatorname{rad}(q)),
$$

the graded tensor product of the Clifford algebra of the reduced non-degenerate form and the exterior algebra on the radical. It follows both from the splitting theorem for orthogonal sums and from the three families of fundamental relations among vectors of $W$ and of the radical. The isomorphism depends on the choice of complement, although different complements give isomorphic factors.

The generator $r$ of the radical satisfies $r^2 = 0$, so the exterior algebra is nilpotent in positive degree. In fact $\mathfrak{n}^k = \mathrm{Cl}(W, \bar{q}) \otimes \bigoplus_{j\geq k}\Lambda^j(\operatorname{rad}(q))$ and the nilpotency index is exactly $\operatorname{rank}\operatorname{rad}(q) + 1$ when the radical is free. The radical generates a nilpotent two-sided ideal $\mathfrak{n}$, the quotient by which is the non-degenerate factor; over a field of characteristic not $2$, $\mathfrak{n}$ is the Jacobson radical and $\mathrm{Cl}(V, q)$ is semisimple if and only if $q$ is non-degenerate. The **centre** is the even part of the exterior algebra on the radical, of rank $2^{r_0 - 1}$ for $r_0 \geq 1$, together with the span of the volume element when $n$ is odd, which reduces to the classical $R$ or $R \oplus R\omega$ when the radical vanishes. The **rank** of the algebra is $2^n$ whether or not the form is degenerate, since the dimension lost by the reduced form is recovered by the exterior factor. The extreme case is the zero form, for which $\mathrm{Cl}(V, 0) = \Lambda(V)$; the one-dimensional case is the algebra of dual numbers $\mathbb{D}'$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with $2$ invertible |
| $V$ | Free $R$-module of finite rank $n$ |
| $q$, $B$ | Quadratic form and polar form, $q(v) = B(v, v)$ |
| $\operatorname{rad}(q)$ | Radical $\{v : B(v, w) = 0\ \forall w\}$ |
| $r_0$ | Rank of the radical |
| $W$ | Complement of the radical, with $V = W \oplus \operatorname{rad}(q)$ |
| $\bar{q}$ | Reduced non-degenerate form $q|_W$ on the complement |
| $\mathrm{Cl}(V, q)$ | Clifford algebra |
| $\Lambda(V)$, $\Lambda^k$ | Exterior algebra and its degree-$k$ part |
| $\Lambda^{\mathrm{ev}}(U)$ | Even part of $\Lambda(U)$, spanned by the products of even degree |
| $\hat\otimes$ | Graded tensor product |
| $r_i$ | Basis elements of the radical, $r_i^2 = 0$ |
| $\mathfrak{n}$ | Nilpotent ideal generated by the radical; Jacobson radical over a field |
| $\mathfrak{n}^k$ | Its powers, $\mathrm{Cl}(W,\bar q)\otimes\bigoplus_{j\geq k}\Lambda^j(\operatorname{rad}(q))$ |
| Nilpotency index | $r_0 + 1$, the least $k$ with $\mathfrak{n}^k = 0$ |
| $M_2(\mathbb{R})$ | $2 \times 2$ real matrices, $\mathrm{Cl}$ of the hyperbolic plane |
| $\omega$ | Volume element $e_1 \cdots e_n$ of an orthogonal basis of $V$, central when $n$ is odd |
| $\omega_W$, $\omega_{\operatorname{rad}}$ | Volume elements of the reduced factor and of the radical |
| $\mathbb{D}'$ | Dual numbers, $\mathbb{R}[\varepsilon]/(\varepsilon^2)$ |
| $\mathbb{D}$ | Split complex numbers, $\mathbb{R}[t]/(t^2-1)$ |
| $\mathbb{R}$ | Real numbers |



## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the radical of a form and the Clifford algebra over a ring.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the algebraic preliminaries on Clifford algebras of possibly degenerate forms.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the exterior-algebra factor and worked degenerate examples.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the radical, non-degeneracy and the reduction of a form.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the filtration and the exterior-algebra comparison without a non-degeneracy hypothesis.
