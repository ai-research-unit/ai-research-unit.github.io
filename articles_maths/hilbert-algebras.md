# __Hilbert Algebras__

## Introduction

A **Hilbert algebra** is an associative algebra carrying an involution $\bar{\cdot}$ and a positive definite sesquilinear form $\langle \cdot, \cdot \rangle$ that the involution turns into the adjoint of multiplication:

$$
\langle xy, z \rangle = \langle y, x^{\dagger} z \rangle .
$$

Three data enter: a product, an involution, and a positive definite form; one axiom ties them together. The form is what makes the algebra *Hilbert*: it is an inner product, so Cauchy–Schwarz, orthogonality and the completion are available. The involution is what makes it *involutive*. The axiom says that the left regular representation is a $\ast$-representation, that is, that the involution computes the adjoint of every multiplication operator.

This article settles the three data for one category. The involution is built here: the algebra carries intrinsic anti-involutions with no hypothesis on the base, and an involution of the base induces the **dagger**. The form is built here as well: it is the **trace form** $\langle x, y \rangle = \tau(x^{\dagger}y)$, whose Gram matrix is Hermitian, and it is positive definite exactly when the involution is positive. Positivity is the third datum, and it is the cone of the elements $x^{\dagger}x$.

The algebras of `- Theory` and `- Operator Theory` of *Algebras with a degree-2 form*, once equipped with a dagger, are the instances this article serves.

The algebraic base of the structure — the involution, the Hermitian form and the adjoint axiom, with no positivity of the form and no completion of the algebra — is *Hermitian Algebras* in `Sesqualgebras with a degree-2 form`. This article is the **positive definite and completed case** of that structure: it adds the positivity, the cone and the completion, and it keeps the dagger, the trace form and the Gram matrix that the case makes available. The operators built from the dagger — the Hermitian forms carried by the algebra and the Hermitian sandwich — are the groups `- * Theory, Two-Sided Operator with Hermitian Adjoint`, `- * Theory, One-Sided Operator with Hermitian Adjoint` and their signed variants in the same category, and the completion, the modular operator and the Von Neumann completeness belong to the later articles of the group.

## The Axioms

### Definition

Let $A$ be a unital associative algebra over a field $F$ carrying an **involution** $\bar{\cdot}$, that is an additive map with

$$
(xy)^{\dagger} = y^{\dagger}x^{\dagger}, \qquad (x^{\dagger})^{\dagger} = x, \qquad 1^{\dagger} = 1 .
$$

A **Hilbert algebra** is the pair $(A, \bar{\cdot})$ together with a form $\langle \cdot, \cdot \rangle : A \times A \to F$ that is

- **sesquilinear**: additive in each argument, with $\langle ax, y \rangle = a\langle x, y\rangle$ and $\langle x, ay \rangle = \sigma(a)\langle x, y \rangle$ for a central $a$;
- **Hermitian**: $\langle x, y \rangle = \sigma(\langle y, x \rangle)$, so that the diagonal $q(x) = \langle x, x \rangle$ lies in the fixed field $F^\sigma$;
- **positive definite**: $q(x) = \langle x, x \rangle > 0$ for every $x \neq 0$;
- **adjoint**: $\langle xy, z \rangle = \langle y, x^{\dagger}z \rangle$ for all $x, y, z \in A$.

The last axiom is the one that binds the form to the involution. When the base involution $\sigma$ is the identity the form is bilinear, and the examples of the category are of this kind; a non-trivial $\sigma$ is what makes the form sesquilinear rather than bilinear.

### The Adjoint Axiom and Its Forms

**Proposition.** The adjoint axiom is equivalent to each of

$$
\langle xy, z \rangle = \langle x, z\,y^{\dagger} \rangle, \qquad \langle x^{\dagger}y, z \rangle = \langle y, xz \rangle .
$$

**Proof.** For the first, apply the axiom to the pair $(y^{\dagger}, x^{\dagger})$ and use $y^{\dagger}x^{\dagger} = (xy)^{\dagger}$: $\langle y^{\dagger}x^{\dagger}, z\rangle = \langle x^{\dagger}, yz \rangle$, and substituting $z \mapsto z y^{\dagger}$ in the axiom gives $\langle xy, zy^{\dagger}\rangle = \langle y, x^{\dagger}zy^{\dagger}\rangle$. The two readings coincide because $\langle \cdot, \cdot\rangle$ is positive definite and hence non-degenerate. The second follows from the first by transposing the roles of the two arguments.

**Proposition.** Let $\lambda : A \to \operatorname{End}_F(A)$ be the left regular representation, $\lambda(x) = m_x$, where $m_x(y) = xy$. Then $\lambda(x^{\dagger}) = \lambda(x)^{\ast}$, the adjoint being taken with respect to $\langle \cdot, \cdot \rangle$.

**Proof.** $\langle m_xy, z \rangle = \langle xy, z \rangle = \langle y, x^{\dagger}z \rangle = \langle y, m_{x^{\dagger}}z\rangle$ for all $y, z$, which is the defining relation of the adjoint. Positivity makes the form non-degenerate, so the adjoint is unique.

### Positivity and the Cone

**Proposition.** For every $x \in A$ the element $x^{\dagger}x$ is self-adjoint, $(x^{\dagger}x)^{\dagger} = x^{\dagger}x$, and the scalar $\tau(x^{\dagger}x)$ with $\tau(y) = \langle y, 1\rangle$ is non-negative:

$$
\tau(x^{\dagger}x) = \langle x^{\dagger}x, 1 \rangle = \langle x, x \rangle \geq 0 .
$$

**Proof.** $(x^{\dagger}x)^{\dagger} = x^{\dagger}(x^{\dagger})^{\dagger} = x^{\dagger}x$. For the scalar, apply the adjoint axiom with $x$ replaced by $x^{\dagger}$, $y$ by $x$ and $z$ by $1$, using $(x^{\dagger})^{\dagger} = x$; the value is $\langle x, x \rangle$, which is positive for $x \neq 0$ by the positive definiteness of the form.

The set $P = \{\sum_i x_i^{\dagger}x_i\}$ of finite sums of such elements is the **positive cone** of the algebra. It is closed under addition by construction, it contains $0$, and it meets its negative only in $0$: if $\sum_i x_i^{\dagger}x_i = 0$ then $\tau$ of it is $\sum_i \langle x_i, x_i\rangle = 0$, so every $x_i = 0$ by positive definiteness. An **order** on $A$ is read off $P$ by $x \leq y$ if and only if $y - x \in P$, and a linear map is **positive** when it carries $P$ into $P$. The dagger is a **positive involution** when every $x^{\dagger}x$ lies in the closure of $P$ in the order it defines; over a field and in finite dimension the three notions — the positivity of the form, the order of the cone, and the positivity of the involution — agree, and a finite-dimensional algebra over $\mathbb{R}$ with a positive involution is a $C^*$-algebra.

Since the form is an inner product, the Cauchy–Schwarz inequality $\lvert \langle x, y\rangle\rvert^2 \leq \langle x, x\rangle \langle y, y\rangle$ holds, and the algebra embeds in its **completion**, which is a Hilbert space on which the left regular representation acts by bounded operators. The completion and the operator theory built on it are the subject of the later articles of the group.

## The Involution and the Dagger

### The Intrinsic Anti-Involutions

The algebras of the category carry a $\mathbb{Z}/2$-grading, $A = A^0 \oplus A^1$, and with it the **grade involution** $\alpha$, the automorphism acting by $\alpha(x) = (-1)^k x$ on the degree-$k$ part. Two anti-involutions are then defined with no hypothesis on the base ring:

- **reversion** $x^{r}$, the anti-automorphism fixing each vector;
- the **conjugate** $x^{\natural} = \alpha(x^{r})$.

Both satisfy $(xy)^{\ast} = y^{\ast}x^{\ast}$ and $(x^{\ast})^{\ast} = x$. They agree on the even part, because $\alpha$ is the identity there, and they differ on the odd part, where reversion fixes the vectors and the conjugate negates them. Their signs on a decomposition element $e_I$ of degree $k$ depend on $k$ alone:

| anti-involution | sign on a $k$-blade | vectors |
|---|---|---|
| reversion $x^{r}$ | $(-1)^{k(k-1)/2}$ | fixed |
| conjugate $x^{\natural} = \alpha(x^{r})$ | $(-1)^{k(k+1)/2}$ | negated |

So $(A, r)$ and $(A, \bar\cdot)$ are each a ring with involution over every base, and this is the sense in which the algebra is always involutive: the involution is not imported from the coefficients, it is part of the algebra.

### The Involution of the Base and the Dagger

Let the base ring $A_0$ carry an involution $\sigma$. Its action on the coefficients extends to a map of the algebra, written again $\sigma$,

$$
\sigma\Bigl(\sum_I a_I e_I\Bigr) = \sum_I \sigma(a_I)\,e_I ,
$$

in an orthogonal basis. This map is an automorphism of $A_0$-rings, it fixes each vector, and it is $\sigma$-**semilinear**: $\sigma(ax) = \sigma(a)\sigma(x)$ for $a \in A_0$ and $x \in A$. It commutes with reversion, with the grade involution and with the conjugate, since those act on the basis and $\sigma$ acts on the coefficients.

**Definition.** The **dagger** is the composite

$$
x^{\dagger} = \sigma(\alpha(x^{r})) = \sigma(x^{\natural}).
$$

It is the composite of the anti-involution $\bar\cdot$ with the automorphism $\sigma$, so it is an anti-automorphism, and since $\sigma$ and $\bar\cdot$ commute and both have order two, it has order two:

$$
(xz)^{\dagger} = \bar{z}x^{\dagger}, \qquad (x^{\dagger})^{\dagger} = x, \qquad (ax)^{\dagger} = \sigma(a)\,x^{\dagger}.
$$

The dagger is $\sigma$-semilinear over $A_0$. When $\sigma = \mathrm{id}$ it reduces to the conjugate, $x^{\dagger} = x^{\natural}$, and the theory collapses to the ordinary orthogonal one.

**Definition.** The **conjugate reversion** is $x^{r,\sigma} = \sigma(x^{r})$. It is the other anti-involution of order two carried by the algebra, and the two are related by

$$
x^{\dagger} = \alpha\bigl(x^{r,\sigma}\bigr).
$$

The choice between them is the choice of a sign per grade, hence the choice of a signature.

**Example (the biquaternions).** On $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the three commuting conjugations ${}^{\natural}$, $\sigma$ and $\bar{\cdot}$ are involutions; $\sigma$ conjugates the complex coefficients and $\bar{\cdot} = \sigma\circ{}^{\natural}$ is the dagger. Their composition rules make $\{\mathrm{id}, {}^{\natural}, \sigma, \bar{\cdot}\}$ a Klein four-group, which is the smallest case in which the involution of the base and the intrinsic anti-involutions are both visible.

### Semilinearity

A map $f$ between $A_0$-modules is $\sigma$-**semilinear** if $f(x + y) = f(x) + f(y)$ and $f(ax) = \sigma(a)f(x)$. The dagger is $\sigma$-semilinear, and so is every map of the form $x \mapsto xc$, composed with the dagger. A form $s$ on a right $A_0$-module is $\sigma$-**sesquilinear** if $s(xa, yb) = \sigma(a)s(x,y)b$, the convention of *Hermitian Forms over an Involution Ring and the Unitary Witt Group*. The passage from the linear to the semilinear theory is exactly the passage from $\sigma = \mathrm{id}$ to a general $\sigma$.

## The Form and the Trace Form

### The Canonical Form of an Involutive Algebra

An anti-involution supplies forms with no further structure. For an anti-involution $c$ of a ring $R$ the two-variable map

$$
h_c(x, y) = c(x)\,y
$$

is Hermitian with respect to $c$, in the sense $h_c(x,y) = c(h_c(y,x))$, and its diagonal $q_c(x) = c(x)x$ is fixed by $c$. The verification is the definition of an anti-involution together with $c^2 = \mathrm{id}$, and it needs nothing else: no commutativity, no order, no hypothesis on the ring.

So each of the anti-involutions of the algebra carries a form: reversion gives $h_r$, the conjugate gives $h_{\bar\cdot}$, and the dagger gives $h_{\dagger}$. The three are the canonical Hermitian forms of the algebra. They are **algebra-valued**; the scalar form is the trace form, and the operators built from them belong to the group `- * Operator Theory`.

### The Trace Form

Let $A$ be a finite-dimensional unital associative algebra over a field $F$, and for $x \in A$ let $m_x : A \to A$ be left multiplication by $x$, an $F$-linear endomorphism.

**Definition.** The **regular norm** and the **regular trace** of $x$ are

$$
N(x) = \det(m_x), \qquad \operatorname{Tr}(x) = \operatorname{Tr}(m_x),
$$

and the **trace form** of $A$ is the symmetric bilinear form

$$
T(x, y) = \operatorname{Tr}(m_{xy}) = \operatorname{Tr}(m_x m_y).
$$

**Proposition.** The regular norm is multiplicative, $N(xy) = N(x)N(y)$, and homogeneous of degree $n = \dim_F A$; the trace form is symmetric, $T(x, y) = T(y, x)$.

**Proof.** $m_{xy} = m_x \circ m_y$, so $\det(m_{xy}) = \det(m_x)\det(m_y)$; homogeneity of degree $n$ follows from $\det(\lambda I) = \lambda^n$ applied to $m_{\lambda x} = \lambda m_x$. The trace form is symmetric because $\operatorname{Tr}(m_{xy}) = \operatorname{Tr}(m_xm_y) = \operatorname{Tr}(m_ym_x) = \operatorname{Tr}(m_{yx})$.

When $A$ is central simple over $F$ of degree $d$, so that $A\otimes_F \bar F \cong M_d(\bar F)$, the **reduced trace** and **reduced norm** are the trace and determinant of the image in $M_d(\bar F)$; both lie in $F$ and are independent of the isomorphism, and for $d$ invertible,

$$
\operatorname{Trd}(x) = \operatorname{Tr}(m_x)/d, \qquad \operatorname{Nrd}(x)^{\,d} = N(x).
$$

The **reduced trace form** is $T_{\operatorname{red}}(x,y) = \operatorname{Trd}(xy)$.

**Definition.** The **trace form of the Hilbert algebra** is the scalar form obtained by inserting the dagger into the trace:

$$
\langle x, y \rangle = \tau(x^{\dagger}y),
$$

with $\tau$ the reduced trace when $A$ is central simple and the regular trace otherwise. It is Hermitian with respect to $\bar{\cdot}$, because

$$
\sigma\bigl(\tau(y^{\dagger}x)\bigr) = \tau\bigl(\sigma(y^{\dagger}x)\bigr) = \tau\bigl(x^{\dagger}y\bigr),
$$

using the $\sigma$-semilinearity of the dagger and the invariance of $\tau$ under $\sigma$, and it is the form that the adjoint axiom is stated for.

### The Gram Matrix

Assume $A$ is free of finite rank over the base with basis $(e_1, \ldots, e_n)$ and that the base is a division ring. The **Gram matrix** of $\langle \cdot, \cdot\rangle$ is $H_{ij} = \langle e_i, e_j\rangle$, and $H$ is Hermitian in the sense $H^{\dagger} = H$, where $H^{\dagger} = \sigma(H)^T$. For $x = \sum_i e_ix_i$ and $y = \sum_j e_jy_j$,

$$
\langle x, y \rangle = \sum_{i,j}\sigma(x_i)\,H_{ij}\,y_j = x^{\dagger}H\,y ,
$$

so the form is represented by a Hermitian matrix, and it is non-degenerate exactly when $H$ is invertible. The **radical** $\operatorname{rad}\langle\cdot,\cdot\rangle = \{x : \langle x, y\rangle = 0$ for all $y\}$ is the kernel of $H$, so the form of a Hilbert algebra is non-degenerate, its radical being zero by positive definiteness.

The transpose that appears in the Gram matrix is $\bar{\cdot}$, not ${}^{\natural}$: the shared block reserves $\bar{\cdot}$ for Hermitian conjugation and $\sigma$ for the conjugation of coefficients, which is what makes the article agree with its own use of $\bar{\cdot}$ for the biquaternion Hermitian conjugation.

### Positivity of the Trace Form

**Example (the biquaternions).** For $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \cong M_2(\mathbb{C})$ the reduced norm is the determinant and the regular norm is its square; the norm $N(\tilde Q) = \tilde Q\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ is the reduced norm. It is $\mathbb{C}$-valued and isotropic, and it vanishes on the zero divisors, its nonzero zeros being exactly the matrices of rank one.

The dagger changes the picture completely. The form $\operatorname{Trd}(\tilde P\bar{\tilde{Q}})$ is complex-Hermitian with diagonal

$$
\operatorname{Trd}(\tilde Q\bar{\tilde{Q}}) = 2\sum_\mu \lvert Q_\mu\rvert^2 ,
$$

which is a sum of non-negative reals: it is positive definite on the underlying real space, and it vanishes only at $\tilde Q = 0$. It is therefore the trace form of a Hilbert algebra, while $\operatorname{Trd}(\tilde P\tilde Q)$ is the symmetric form of the ordinary trace and is not positive definite. The two forms are related by the conjugation $\bar{\cdot}$, and the whole difference between the two lies in the dagger.

### The Polar Form of the Reduced Norm

For a quaternion algebra $D$ over a field $F$ of characteristic not $2$, with reduced norm $N(x) = x x^{\natural} = \operatorname{Nrd}(x)$, the polar form of $N$ is

$$
B_N(x, y) = \tfrac{1}{2}\bigl(N(x + y) - N(x) - N(y)\bigr) = \tfrac{1}{2}\bigl(x y^{\natural} + y x^{\natural}\bigr) = \tfrac{1}{2}\operatorname{Trd}(x y^{\natural}).
$$

**Proposition.** The polar form $B_N$ of the reduced norm is not a scalar multiple of the reduced trace form $T_{\operatorname{red}}(x,y) = \operatorname{Trd}(xy)$.

**Proof.** For $y = 1$ the two forms give $B_N(x,1) = \tfrac{1}{2}(x + x^{\natural}) = \tfrac{1}{2}\operatorname{Trd}(x)$ and $T_{\operatorname{red}}(x,1) = \operatorname{Trd}(x)$, so any constant of proportionality would have to be $\tfrac{1}{2}$. Equality would then require $\operatorname{Trd}(x y^{\natural}) = \operatorname{Trd}(xy)$ for all $x, y$, that is $\operatorname{Trd}\bigl(x(y^{\natural} - y)\bigr) = 0$. With $x = y = e_1$ this reads $\operatorname{Trd}(-2e_1^2) = \operatorname{Trd}(2) = 4 \neq 0$, a contradiction.

The two forms are the two halves of the same structure: $T_{\operatorname{red}}$ is the symmetric form of the trace, and $B_N$ is the Hermitian form $\operatorname{Trd}(x^{\dagger}y)$ written with the conjugate in place of the dagger. Only the second is positive definite.

## What Belongs Elsewhere

- The **involutions of a ring** for their own sake — the first and the second kind, the orthogonal and symplectic types over a central simple algebra, the symmetric and skew decomposition, the adjoint involution of a form — belong to *Involutive Rings*. Nothing of that layer is repeated here.
- The **general theory of $\sigma$-sesquilinear and Hermitian forms** over an involution ring — the Gram matrix, the radical, the isometry group, the Dieudonné extension and cancellation theorems, the unitary Witt group — belongs to *Hermitian Forms over an Involution Ring and the Unitary Witt Group*, and the bilinear case $\sigma = \mathrm{id}$ over a commutative base to *Bilinear Forms*.
- The **norms of an algebra** — the regular norm, the reduced norm and trace of a central simple algebra, the norms of the complex, quaternion and biquaternion algebras and Hurwitz's theorem — belong to *Quadratic Forms over Algebras and Norms*.
- The **algebraic base without positivity** — the involution, the Hermitian form, the adjoint axiom, the radical, the isometry group and the unitary slice — is *Hermitian Algebras*, the Part I entry of `Sesqualgebras with a degree-2 form`. This article is its positive definite and completed case.
- The **operators built from the dagger** — the algebra-valued Hermitian forms, the blade form, the Hermitian sandwich $\Theta_x(y) = xyx^{\dagger}$, the unitary slice — belong to the groups `- * Theory, Two-Sided Operator with Hermitian Adjoint`, `- * Theory, One-Sided Operator with Hermitian Adjoint` and their signed variants of `Sesqualgebras with a degree-2 form`, where the involution defines the adjoint and the positive cone supplies the order.
- The **completion of the algebra**, the **GNS construction**, the **modular operator and Tomita–Takesaki theory**, the **modular group and the KMS condition** and the **Von Neumann algebra completeness** are the later articles of the star group, and they presuppose this one.

## Summary

A **Hilbert algebra** is an associative algebra with an involution $\bar{\cdot}$ carrying a positive definite sesquilinear form $\langle \cdot, \cdot\rangle$ subject to the **adjoint axiom** $\langle xy, z\rangle = \langle y, x^{\dagger}z\rangle$. Equivalently $\langle xy, z\rangle = \langle x, zy^{\dagger}\rangle$ and $\langle x^{\dagger}y, z\rangle = \langle y, xz\rangle$, and the left regular representation $\lambda(x) = m_x$ is a $\ast$-representation, $\lambda(x^{\dagger}) = \lambda(x)^{\ast}$. The diagonal of the form is Hermitian and takes values in the fixed field.

For each $x$ the element $x^{\dagger}x$ is self-adjoint and $\langle x^{\dagger}x, 1\rangle = \langle x, x\rangle \geq 0$, and the finite sums $\sum_i x_i^{\dagger}x_i$ form the **positive cone**, which meets its negative only in $0$ and defines an order on the algebra. An involution whose $x^{\dagger}x$ lie in the cone is **positive**, and in finite dimension over $\mathbb{R}$ a positive involution makes the algebra a $C^*$-algebra. Positive definiteness gives Cauchy–Schwarz and hence the completion, on which the left regular representation acts by bounded operators.

The involution is built in two steps. The algebra carries a $\mathbb{Z}/2$-grading and the grade involution $\alpha$, and with them two intrinsic anti-involutions, **reversion** $x^{r}$ and the **conjugate** $x^{\natural} = \alpha(x^{r})$, which agree on the even part and differ on the odd part by a sign per degree. An involution $\sigma$ of the base extends to a $\sigma$-semilinear automorphism fixing the vectors, and the composite $x^{\dagger} = \sigma(\alpha(x^{r})) = \sigma(x^{\natural})$ is the **dagger**, an anti-automorphism of order two with $(xz)^{\dagger} = \bar{z}x^{\dagger}$ and $(ax)^{\dagger} = \sigma(a)x^{\dagger}$. Its companion is the **conjugate reversion** $x^{r,\sigma} = \sigma(x^{r})$, related by $x^{\dagger} = \alpha(x^{r,\sigma})$; the choice between them is a choice of sign per grade, hence of signature.

The form is the **trace form** $\langle x, y\rangle = \tau(x^{\dagger}y)$, with $\tau$ the reduced trace $\operatorname{Trd} = \operatorname{Tr}/d$ for a central simple algebra of degree $d$ and the regular trace otherwise. It is Hermitian with respect to the dagger, its Gram matrix satisfies $H^{\dagger} = \sigma(H)^T = H$, the form is represented by $x^{\dagger}Hy$, and its radical is the kernel of $H$, so it is non-degenerate. In the biquaternion algebra the trace form $\operatorname{Trd}(\tilde P\bar{\tilde{Q}})$ has diagonal $2\sum_\mu\lvert Q_\mu\rvert^2$, a sum of non-negative reals, so it is positive definite, while the symmetric form $\operatorname{Trd}(\tilde P\tilde Q)$ is not; the two differ by the insertion of the dagger. The polar form of the reduced norm, $B_N(x,y) = \tfrac{1}{2}\operatorname{Trd}(x y^{\natural})$, is never proportional to the reduced trace form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Associative algebra, usually finite-dimensional over $F$ |
| $F$, $A_0$ | Field of scalars; base ring |
| $\bar{\cdot}$ | The involution of the Hilbert algebra; $x^{\dagger} = \sigma(\alpha(x^{r}))$ |
| $\sigma$ | Involution of the base; the identity for a bilinear form |
| $\langle x, y\rangle = \tau(x^{\dagger}y)$ | The trace form, positive definite |
| $q(x) = \langle x, x\rangle$ | Diagonal of the form, valued in the fixed field |
| $H$, $H^{\dagger} = \sigma(H)^T$ | Gram matrix of the form; Hermitian transpose |
| $\operatorname{rad}\langle\cdot,\cdot\rangle$ | Radical, the kernel of $H$ |
| $P = \{\sum_i x_i^{\dagger}x_i\}$ | Positive cone |
| $x^{r}$ | Reversion, the anti-involution fixing the vectors |
| $x^{\natural} = \alpha(x^{r})$ | The conjugate anti-involution, negating the vectors |
| $\alpha$ | Grade involution, $\alpha(x) = (-1)^k x$ on the degree-$k$ part |
| $x^{r,\sigma} = \sigma(x^{r})$ | Conjugate reversion, $x^{\dagger} = \alpha(x^{r,\sigma})$ |
| ${}^{\natural}$ | The conjugate, negating the vectors; the coefficient conjugation is $\sigma$, so on $\mathbb{B}$, $\bar{\cdot} = \sigma\circ{}^{\natural}$ |
| $m_x$, $\lambda(x)$ | Left multiplication by $x$; the left regular representation |
| $\operatorname{Tr}$, $N(x) = \det(m_x)$ | Regular trace and regular norm |
| $\operatorname{Trd}$, $\operatorname{Nrd}$ | Reduced trace and reduced norm, $A$ central simple of degree $d$ |
| $T(x,y) = \operatorname{Tr}(m_{xy})$ | Trace form of the algebra |
| $T_{\operatorname{red}}(x,y) = \operatorname{Trd}(xy)$ | Reduced trace form |
| $B_N(x,y) = \tfrac{1}{2}\operatorname{Trd}(x y^{\natural})$ | Polar form of the reduced norm |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras*, North-Holland Mathematical Library 27 (North-Holland, 1981), for Hilbert algebras, their axioms and the modular theory built on them.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II (Academic Press, 1986), for the completion of an involutive algebra and the regular representations.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular operator of a Hilbert algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for algebras with involution and the classification of their involutions.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the trace form, the reduced trace and the reduced norm.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular norm, the reduced norm and central simple algebras.
