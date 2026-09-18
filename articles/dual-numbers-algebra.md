
# Dual Numbers Algebra

## Introduction

This article introduces the dual number algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugation.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given, and no applications are discussed. The algebra is defined over an arbitrary commutative ring in which the defining nilpotent is available, and the specializations to specific rings are left for the reader.

Throughout this article, the algebra of dual numbers is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The notation is chosen so that the two do not collide. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## The Dual Numbers

### Definition

Let $R$ be a commutative ring. The **dual number algebra** $\mathbb{D}'_R$ is the two-dimensional free $R$-module with basis

$$
e_0 = 1, \qquad e_1 = \varepsilon,
$$

and multiplication rules

$$
e_0 e_0 = e_0, \qquad e_0 e_1 = e_1 e_0 = e_1, \qquad e_1 e_1 = 0.
$$

A general dual number is written in developed form as

$$
z = a e_0 + b e_1, \qquad a, b \in R,
$$

or, more compactly, as

$$
z = a + b \varepsilon, \qquad a, b \in R.
$$

The element $a$ is the **real part**, and $b$ is the **infinitesimal part**. We write

$$
a = \operatorname{Re} z, \qquad b = \operatorname{Inf} z.
$$

When $R = \mathbb{R}$, we write $\mathbb{D}'$ for $\mathbb{D}'_{\mathbb{R}}$. The notation $\varepsilon$ is chosen deliberately. In some of the older literature, the nilpotent unit is written $i$ or $j$, which collides with the imaginary unit of the complex numbers or with the hyperbolic unit of the split complex numbers. This collision is a persistent source of confusion. Using $\varepsilon$ for the nilpotent unit and reserving $i$ and $j$ for the other two cases avoids the collision entirely.

### Basic Properties

**Commutative.** Dual multiplication is commutative: $z w = w z$.

**Associative.** Dual multiplication is associative: $(z w) u = z (w u)$.

**Not a division algebra.** The dual algebra has zero divisors. The element $\varepsilon$ is non-zero, but

$$
\varepsilon^2 = 0.
$$

So $\mathbb{D}'$ is not a field, and not a division algebra. This is the fundamental difference from $\mathbb{C}$, and it is the source of everything that distinguishes the two theories.

**Not semisimple.** The algebra $\mathbb{D}'$ is local, with unique maximal ideal $(\varepsilon)$. The maximal ideal is nilpotent of index two, so the algebra is not semisimple.

**Frobenius theorem.** The dual algebra is not one of the three finite-dimensional associative real division algebras. Those are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. The dual algebra is a commutative associative real algebra of dimension two, but it is not a division algebra.

### The Isomorphism with $R[\varepsilon]/(\varepsilon^2)$

The dual algebra $\mathbb{D}'_R$ is isomorphic to the quotient ring

$$
\mathbb{D}'_R \cong R[\varepsilon]/(\varepsilon^2),
$$

the ring of polynomials in $\varepsilon$ modulo $\varepsilon^2$. This is the simplest example of a **local ring** that is not a field: it has a unique maximal ideal, namely $(\varepsilon)$, and the quotient by that ideal is $R$.

### The Relation to the Truncated Polynomial Algebra

For $n \geq 1$, the **truncated polynomial algebra** is

$$
\mathbb{D}'_{R, n} = R[\varepsilon]/(\varepsilon^{n+1}),
$$

the ring of polynomials in $\varepsilon$ modulo $\varepsilon^{n+1}$. The case $n = 1$ recovers the dual numbers. The case $n = 0$ gives $R$ itself. The truncated polynomial algebras are the algebraic model for higher-order infinitesimals.

## Dual Numbers Algebra

### Definition

The **dual numbers algebra** is the algebra $\mathbb{D}'_R$ considered as a two-dimensional free $R$-module equipped with its multiplication. As an $R$-module, $\mathbb{D}'_R$ has rank $2$. As a ring, it is a commutative local ring with nilpotent maximal ideal. A general element is written in developed form as

$$
z = a e_0 + b e_1, \qquad a, b \in R,
$$

or, more compactly, as

$$
z = a + b \varepsilon, \qquad a, b \in R.
$$

We write

$$
z = a + b \varepsilon,
$$

where $a$ is the **real part** and $b$ is the **infinitesimal part**.

### Multiplication

The product of two dual numbers is defined by extending the ring multiplication bilinearly:

$$
z w = (a + b\varepsilon)(c + d\varepsilon) = ac + (ad + bc) \varepsilon.
$$

In developed form,

$$
z w = \sum_{\mu=0}^{1} \sum_{\nu=0}^{1} z_\mu w_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the dual algebra.

### Conjugations

There are **two** natural conjugations on $\mathbb{D}'_R$:

**Dual conjugation** $\bar{z}$:

$$
\bar{z} = a - b \varepsilon.
$$

**Identity conjugation** $\operatorname{id}$:

$$
\operatorname{id}(z) = z.
$$

Each conjugation is an involution: applying it twice returns the original dual number. Each has a fixed-point set, which is an $R$-submodule of $\mathbb{D}'_R$. The two submodules are described in the following sections.

## The Two Fixed-Point Submodules

Each of the two conjugations has a fixed-point set. The two submodules are described below.

### The Real Submodule

The fixed points of **dual conjugation** are the dual numbers satisfying $\bar{z} = z$. In developed form,

$$
a - b \varepsilon = a + b \varepsilon.
$$

Comparing the coefficients of $1$ and $\varepsilon$:

- Coefficient of $1$: $a = a$, always satisfied.
- Coefficient of $\varepsilon$: $-b = b$, so $2b = 0$.

If $2$ is invertible in $R$, then $b = 0$. In that case, the fixed points are dual numbers with vanishing infinitesimal part:

$$
z = a, \qquad a \in R.
$$

This is the **real submodule** $R_{\mathbb{D}'}$, a copy of $R$ embedded in $\mathbb{D}'_R$ as the real axis. It is an $R$-module of rank $1$. It is a subalgebra of $\mathbb{D}'_R$ (isomorphic to $R$).

If $2$ is not invertible in $R$, the fixed-point set is larger, and the theory requires more care. We assume from this point on that $2$ is invertible in $R$.

### The Infinitesimal Submodule

The fixed points of the **identity conjugation** are all dual numbers. In developed form,

$$
z = z.
$$

The fixed points are

$$
z = a + b \varepsilon, \qquad a, b \in R.
$$

This is the **dual submodule** $\mathbb{D}'_{\mathbb{D}'}$, a copy of the dual algebra embedded in itself as the whole thing. It is an $R$-module of rank $2$. It is a subalgebra of $\mathbb{D}'_R$.

The **infinitesimal submodule** $\varepsilon R_{\mathbb{D}'}$ is not a fixed-point set of either conjugation; it is the set of dual numbers of the form $b \varepsilon$ with $b \in R$. It is the maximal ideal of $\mathbb{D}'_R$, and it is nilpotent of index two.

## Dual Decomposition

The real submodule $R_{\mathbb{D}'}$ and the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ are the two eigenspaces of dual conjugation. Every dual number decomposes uniquely as the sum of a real part and an infinitesimal part:

$$
z = z_r + \varepsilon z_i, \qquad z_r \in R, \quad z_i \in R.
$$

The two components are obtained from the dual conjugation:

$$
z_r = \frac{1}{2}(z + \bar{z}), \qquad z_i = \frac{1}{2\varepsilon}(z - \bar{z}).
$$

The first formula is well-defined because $2$ is invertible in $R$. The second formula is formal: it says that $z - \bar{z} = 2b\varepsilon$, so dividing by $2\varepsilon$ recovers $b$. The division by $\varepsilon$ is not an algebra operation, because $\varepsilon$ is not invertible. So the second formula is a convenient notation, not a computation in the algebra.

This gives the direct sum decomposition

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'},
$$

where $\varepsilon R_{\mathbb{D}'}$ is the maximal ideal. Both are $R$-modules of rank $1$, and their direct sum is the full algebra $\mathbb{D}'_R$ of rank $2$.

This is the **dual decomposition** of a dual number. It expresses $z$ as a real number plus $\varepsilon$ times another real number.

## Conjugate Decomposition

The dual conjugation $\bar{\cdot}$ is an involution, so it has eigenvalues $+1$ and $-1$. Its eigenspaces are the real submodule $R_{\mathbb{D}'}$ (eigenvalue $+1$) and the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ (eigenvalue $-1$). Every dual number decomposes uniquely as

$$
z = z_+ + z_-, \qquad z_+ = z_r, \quad z_- = \varepsilon z_i.
$$

This is the same decomposition as above, written in terms of the eigenspaces of the conjugation.

## Quadratic Forms and Inner Product

### The Norm Form

The **norm form** of a dual number $z$ is

$$
N(z) = z \bar{z} = (a + b\varepsilon)(a - b\varepsilon) = a^2.
$$

It is an element of $R$, and it vanishes if and only if $a = 0$, i.e. if and only if $z$ lies in the maximal ideal. It is a **degenerate** quadratic form: it does not detect the infinitesimal part at all, and it is not positive-definite in general.

The norm form is **multiplicative**:

$$
N(z w) = N(z) N(w).
$$

This is the statement that $(ac)^2 = a^2 c^2$, which is true in any commutative ring.

### The Degeneracy of the Norm Form

The norm form is degenerate in the following sense: there exist non-zero elements $z$ with $N(z) = 0$. These are precisely the elements of the maximal ideal, i.e. the elements of the form $b \varepsilon$ with $b \neq 0$. So the norm form does not distinguish between the zero element and the non-zero infinitesimals.

This is the algebraic content of the nilpotence of $\varepsilon$: the infinitesimal part is invisible to the norm form, because the product $\varepsilon \cdot \varepsilon = 0$ annihilates it.

### The Hermitian Form

There is no **positive-definite Hermitian form** on $\mathbb{D}'_R$ analogous to the one on $\mathbb{C}$, because the norm form is degenerate. The closest analogue is the **real form**

$$
z \mapsto a^2 + b^2,
$$

which is the Euclidean norm squared on the underlying $R$-module $\mathbb{D}'_R \cong R^2$. It is positive-definite when $R$ is an ordered ring, and it is not multiplicative. It is the natural "length squared" of $z$ as a point in the plane.

The corresponding **Euclidean norm** is

$$
\|z\|_E = \sqrt{a^2 + b^2}.
$$

It is a genuine norm on the real vector space $\mathbb{D}' \cong \mathbb{R}^2$ when $R = \mathbb{R}$: positive-definite, subadditive, and homogeneous of degree one. It is **not** multiplicative with respect to the dual product, because the dual product does not preserve the Euclidean norm.

### The Inner Product

The **inner product** of two dual numbers $z = a + b\varepsilon$ and $w = c + d\varepsilon$ is

$$
\langle z, w \rangle = a c + b d.
$$

It is the ordinary Euclidean inner product on $R^2$, written in dual notation. It is real-valued, symmetric, and bilinear.

The inner product of a dual number with itself is

$$
\langle z, z \rangle = a^2 + b^2,
$$

which is the Euclidean norm squared. So the Euclidean norm is the restriction of the inner product to the diagonal.

Note that this inner product is **not** the same as the real part of $z \bar{w}$. Indeed,

$$
z \bar{w} = (a + b\varepsilon)(c - d\varepsilon) = ac + (bc - ad) \varepsilon,
$$

so

$$
\operatorname{Re}(z \bar{w}) = ac,
$$

which is the degenerate form, not the Euclidean one. The distinction between the two forms is the distinction between the degenerate and the Euclidean structures on $R^2$.

## The Maximal Ideal

The **maximal ideal** of $\mathbb{D}'_R$ is

$$
\mathfrak{m} = (\varepsilon) = \{b \varepsilon : b \in R\}.
$$

It is the set of elements with vanishing real part. It is nilpotent of index two:

$$
\mathfrak{m}^2 = 0.
$$

**Basic properties.**

- $\mathfrak{m}$ is the unique maximal ideal of $\mathbb{D}'_R$.
- The quotient $\mathbb{D}'_R / \mathfrak{m}$ is isomorphic to $R$.
- The algebra $\mathbb{D}'_R$ is local, with residue field $R$.
- Every element not in $\mathfrak{m}$ is invertible.

The maximal ideal is the obstruction to the algebra being a field, and it is the source of the nilpotence in the algebra.

## The Group of Units

The **group of units** of $\mathbb{D}'_R$ is

$$
(\mathbb{D}'_R)^\times = \{a + b\varepsilon : a \in R^\times\}.
$$

An element is invertible if and only if its real part is invertible in $R$. The inverse is

$$
(a + b\varepsilon)^{-1} = a^{-1} - a^{-1} b a^{-1} \varepsilon.
$$

When $R$ is commutative, this simplifies to

$$
(a + b\varepsilon)^{-1} = \frac{1}{a} - \frac{b}{a^2} \varepsilon.
$$

The group of units is an extension of $R^\times$ by the additive group $R$:

$$
1 \to R \to (\mathbb{D}'_R)^\times \to R^\times \to 1,
$$

where the kernel is the maximal ideal $\mathfrak{m} \cong R$ and the quotient is $R^\times$.

## The Lie Algebra Structure

The dual algebra carries a Lie bracket, defined by the commutator

$$
[x, y] = xy - yx.
$$

Since $\mathbb{D}'_R$ is commutative, the commutator is identically zero. So the Lie algebra structure of $\mathbb{D}'_R$ is trivial. This is the fundamental difference from the split complex and quaternion cases, where the commutator is non-trivial.

The **Lie algebra of derivations** of $\mathbb{D}'_R$ is more interesting. A **derivation** is an $R$-linear map $D : \mathbb{D}'_R \to \mathbb{D}'_R$ satisfying the Leibniz rule

$$
D(xy) = D(x) y + x D(y).
$$

**Theorem.** Every derivation of $\mathbb{D}'_R$ is of the form

$$
D(a + b\varepsilon) = c b,
$$

for some $c \in R$. In other words, the derivation is determined by its value on $\varepsilon$, and it maps the real part to zero.

**Proof.** Let $D$ be a derivation. Since $D(1) = D(1 \cdot 1) = 2D(1)$, we have $D(1) = 0$ when $2$ is invertible. Then $D(a) = a D(1) = 0$ for all $a \in R$. So $D$ is determined by $D(\varepsilon)$. Write $D(\varepsilon) = c$ for some $c \in R$. Then

$$
D(a + b\varepsilon) = D(a) + D(b) \varepsilon + b D(\varepsilon) = b c.
$$

So every derivation is of the stated form. $\square$

The module of derivations is isomorphic to $R$, and it is generated by the derivation $\partial / \partial \varepsilon$ that sends $a + b\varepsilon$ to $b$. This derivation is the algebraic content of the derivative: it extracts the infinitesimal part.

## The Tensor Product Decomposition

The dual algebra of a direct sum of two free modules with nilpotent structures is the tensor product of the dual algebras of the summands. More precisely, if $R$ is a commutative ring and $\mathbb{D}'_R$ is the dual algebra, then

$$
\mathbb{D}'_R \otimes_R \mathbb{D}'_R \cong R[\varepsilon_1, \varepsilon_2]/(\varepsilon_1^2, \varepsilon_2^2),
$$

the algebra of polynomials in two commuting nilpotent variables. This is four-dimensional over $R$, with basis $1, \varepsilon_1, \varepsilon_2, \varepsilon_1 \varepsilon_2$, and the generators satisfy $\varepsilon_1^2 = \varepsilon_2^2 = 0$ and $\varepsilon_1 \varepsilon_2 = \varepsilon_2 \varepsilon_1$.

The tensor product is **not** the truncated polynomial algebra $R[\varepsilon]/(\varepsilon^3)$, because the two nilpotents are independent. The truncated polynomial algebra has a single nilpotent of index three, while the tensor product has two commuting nilpotents of index two. The two are not isomorphic.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\mathbb{D}'_R$ | Dual number algebra over $R$ |
| $\mathbb{D}'_{R, n}$ | Truncated polynomial algebra |
| $e_0 = 1$ | Identity |
| $e_1 = \varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $z = a + b \varepsilon$ | General dual number |
| $a = \operatorname{Re} z$ | Real part |
| $b = \operatorname{Inf} z$ | Infinitesimal part |
| $\bar{z} = a - b \varepsilon$ | Dual conjugation |
| $\operatorname{id}(z) = z$ | Identity conjugation |
| $N(z) = a^2$ | Norm form (degenerate) |
| $a^2 + b^2$ | Euclidean norm squared |
| $\langle z, w \rangle = ac + bd$ | Euclidean inner product |
| $\|z\|_E = \sqrt{a^2 + b^2}$ | Euclidean norm |
| $R_{\mathbb{D}'}$ | Real submodule, fixed-point set of $\bar{\cdot}$ |
| $\varepsilon R_{\mathbb{D}'}$ | Infinitesimal submodule, maximal ideal |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal |
| $(\mathbb{D}'_R)^\times$ | Group of units |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.

