
# Split Complex Algebra

## Introduction

This article introduces the split complex algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugations.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The idempotent decomposition is defined algebraically, and its identification with the light cone is left for a later article.

## The Split Complex Numbers

### Definition

The **split complex algebra** $\mathbb{D}$ is the two-dimensional real algebra with basis

$$
e_0 = 1, \qquad e_1 = j,
$$

and multiplication rules

$$
e_0 e_0 = e_0, \qquad e_0 e_1 = e_1 e_0 = e_1, \qquad e_1 e_1 = +e_0.
$$

A general split complex number is written in developed form as

$$
z = a e_0 + b e_1, \qquad a, b \in \mathbb{R},
$$

or, more compactly, as

$$
z = a + b j, \qquad a, b \in \mathbb{R}.
$$

The real number $a$ is the **real part**, and the real number $b$ is the **imaginary part**. We also write

$$
z = a + b j, \qquad a = \operatorname{Re} z, \quad b = \operatorname{Im} z.
$$

The notation $j$ is chosen deliberately. In the complex algebra, the imaginary unit satisfies $i^2 = -1$. In the split complex algebra, the unit satisfies $j^2 = +1$. Writing $j$ rather than $i$ makes the sign explicit and avoids confusion with the complex case. This is the notation we use throughout the blog.

### Basic Properties

**Commutative.** Split complex multiplication is commutative: $z w = w z$.

**Associative.** Split complex multiplication is associative: $(z w) u = z (w u)$.

**Not a division algebra.** The split complex algebra has zero divisors. The elements $1 + j$ and $1 - j$ are non-zero, but

$$
(1 + j)(1 - j) = 1 - j^2 = 0.
$$

So $\mathbb{D}$ is not a field, and not a division algebra. This is the fundamental difference from $\mathbb{C}$, and it is the source of everything that distinguishes the two theories.

**Frobenius theorem.** The split complex algebra is not one of the three finite-dimensional associative real division algebras. Those are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. The split complex algebra is a commutative associative real algebra of dimension two, but it is not a division algebra.

### The Idempotent Basis

Define the **idempotents**

$$
e_+ = \frac{1 + j}{2}, \qquad e_- = \frac{1 - j}{2}.
$$

They satisfy

$$
e_+^2 = e_+, \qquad e_-^2 = e_-, \qquad e_+ e_- = e_- e_+ = 0, \qquad e_+ + e_- = 1.
$$

A general split complex number is written uniquely in the idempotent basis as

$$
z = a + b j = (a + b) e_+ + (a - b) e_-.
$$

This is the **idempotent decomposition** of $z$. It is the single most important structural fact about the split complex algebra.

### The Isomorphism with $\mathbb{R} \oplus \mathbb{R}$

The map

$$
\varphi : \mathbb{D} \to \mathbb{R} \oplus \mathbb{R}, \qquad \varphi(a + b j) = (a + b, a - b),
$$

is an algebra isomorphism. It is bijective, and it satisfies

$$
\varphi(z + w) = \varphi(z) + \varphi(w), \qquad \varphi(z w) = \varphi(z) \varphi(w),
$$

where the multiplication on $\mathbb{R} \oplus \mathbb{R}$ is componentwise:

$$
(u_1, u_2)(v_1, v_2) = (u_1 v_1, u_2 v_2).
$$

So $\mathbb{D}$ is not a new algebra. It is $\mathbb{R} \oplus \mathbb{R}$ in disguise. Everything that can be said about $\mathbb{D}$ is a statement about pairs of real numbers, and everything that is surprising about $\mathbb{D}$ is a consequence of the fact that the disguise hides the zero divisors.

## Split Complex Algebra

### Definition

The **split complex algebra** is the algebra $\mathbb{D}$ considered as a two-dimensional real vector space equipped with its multiplication. As a real vector space, $\mathbb{D}$ has dimension $2$. As a ring, it is a commutative ring with zero divisors. A general element is written in developed form as

$$
z = a e_0 + b e_1, \qquad a, b \in \mathbb{R},
$$

or, more compactly, as

$$
z = a + b j, \qquad a, b \in \mathbb{R}.
$$

We write

$$
z = a + b j,
$$

where $a$ is the **real part** and $b$ is the **imaginary part**.

### Multiplication

The product of two split complex numbers is defined by extending the real multiplication bilinearly:

$$
z w = (a + bj)(c + dj) = (ac + bd) + (ad + bc) j.
$$

In developed form,

$$
z w = \sum_{\mu=0}^{1} \sum_{\nu=0}^{1} z_\mu w_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the split complex algebra.

### Conjugations

There are **two** natural conjugations on $\mathbb{D}$:

**Split complex conjugation** $\bar{z}$:

$$
\bar{z} = a - b j.
$$

**Idempotent conjugation** (swap) $\tilde{z}$:

$$
\tilde{z} = (a - b) e_+ + (a + b) e_-.
$$

In the basis $1, j$, the idempotent conjugation is

$$
\tilde{z} = a - b j = \bar{z}.
$$

So in the split complex algebra, the split complex conjugation and the idempotent conjugation coincide. This is a special feature of the two-dimensional case, and it is the reason the split complex algebra has fewer distinct involutions than the quaternion algebra.

Each conjugation is an involution: applying it twice returns the original split complex number. Each has a fixed-point set, which is a real vector subspace of $\mathbb{D}$. The two subspaces are described in the following sections.

## The Two Fixed-Point Subspaces

Each of the two conjugations has a fixed-point set. The two subspaces are described below.

### The Real Subspace

The fixed points of **split complex conjugation** are the split complex numbers satisfying $\bar{z} = z$. In developed form,

$$
a - b j = a + b j.
$$

Comparing the coefficients of $1$ and $j$:

- Coefficient of $1$: $a = a$, always satisfied.
- Coefficient of $j$: $-b = b$, so $b = 0$.

The fixed points are split complex numbers with vanishing imaginary part:

$$
z = a, \qquad a \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{D}}$, a copy of the real number line embedded in $\mathbb{D}$ as the real axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{D}$ (isomorphic to $\mathbb{R}$), and it is a field.

### The Split Imaginary Subspace

The fixed points of the **idempotent conjugation** are the split complex numbers satisfying $\tilde{z} = z$. Since $\tilde{z} = \bar{z}$ in this algebra, the fixed points are the same as above:

$$
z = a, \qquad a \in \mathbb{R}.
$$

So there is only one non-trivial fixed-point set. The **split imaginary subspace** $j \mathbb{R}_{\mathbb{D}}$ is not a fixed-point set of either conjugation; it is the $-1$ eigenspace of the split complex conjugation, consisting of elements $b j$ with $b \in \mathbb{R}$.

## Split Complex Decomposition

The real subspace $\mathbb{R}_{\mathbb{D}}$ and its imaginary translate $j \mathbb{R}_{\mathbb{D}}$ are the two eigenspaces of split complex conjugation. Every split complex number decomposes uniquely as the sum of a real part and an imaginary part:

$$
z = z_r + j z_i, \qquad z_r \in \mathbb{R}, \quad z_i \in \mathbb{R}.
$$

The two components are obtained from the split complex conjugation:

$$
z_r = \frac{1}{2}(z + \bar{z}), \qquad z_i = \frac{1}{2j}(z - \bar{z}).
$$

Indeed, $z_r$ is fixed by split complex conjugation, so it lies in $\mathbb{R}_{\mathbb{D}}$, and $z_i$ is real, so $j z_i$ lies in $j \mathbb{R}_{\mathbb{D}}$.

This gives the direct sum decomposition

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j \mathbb{R}_{\mathbb{D}},
$$

where $j \mathbb{R}_{\mathbb{D}}$ is the set of split complex numbers of the form $j b$ with $b \in \mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{D}$ of real dimension $2$.

This is the **split complex decomposition** of a split complex number. It expresses $z$ as a real number plus $j$ times another real number.

## Idempotent Decomposition

The idempotent decomposition is the second natural decomposition of $\mathbb{D}$:

$$
z = z_+ e_+ + z_- e_-, \qquad z_+ = a + b, \quad z_- = a - b.
$$

The two components are obtained from the idempotents:

$$
z_+ = z e_+, \qquad z_- = z e_-,
$$

which, since $\mathbb{D}$ is commutative, is unambiguous.

This gives the direct sum decomposition

$$
\mathbb{D} = \mathbb{D} e_+ \oplus \mathbb{D} e_-,
$$

where $\mathbb{D} e_+$ and $\mathbb{D} e_-$ are the two ideals of $\mathbb{D}$, each isomorphic to $\mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{D}$ of real dimension $2$.

The idempotent decomposition and the split complex decomposition are related by

$$
z_+ = z_r + z_i, \qquad z_- = z_r - z_i.
$$

So the idempotent components are the sum and difference of the real and imaginary parts.

## The Norm Form

### Definition

The **norm form** of a split complex number $z$ is

$$
N(z) = z \bar{z} = a^2 - b^2.
$$

It is a real number, but it is **indefinite**: it takes positive values on the region $|a| > |b|$, negative values on the region $|a| < |b|$, and vanishes on the light cone $a = \pm b$.

The norm form is **multiplicative**:

$$
N(z w) = N(z) N(w).
$$

This is the statement that $(a^2 - b^2)(c^2 - d^2) = (ac + bd)^2 - (ad + bc)^2$, which is the Brahmagupta–Fibonacci identity in dimension two.

### Zero Divisors

The norm form vanishes on the light cone, so the non-zero elements of the light cone are **zero divisors**. The two primitive zero divisors are

$$
e_+ = \frac{1 + j}{2}, \qquad e_- = \frac{1 - j}{2}.
$$

Both satisfy $N(e_+) = N(e_-) = 0$, and $e_+ e_- = 0$. Every zero divisor of $\mathbb{D}$ is a real multiple of $e_+$ or $e_-$, or a sum of such multiples.

## The Hermitian Form

There is no **positive-definite Hermitian form** on $\mathbb{D}$ analogous to the one on $\mathbb{C}$, because the norm form is indefinite. The closest analogue is the **idempotent form**

$$
z \mapsto z_+^2 + z_-^2 = (a + b)^2 + (a - b)^2 = 2(a^2 + b^2),
$$

which is positive-definite but is not multiplicative. It is the Euclidean norm squared on the underlying real vector space $\mathbb{D} \cong \mathbb{R}^2$, and it is the natural "length squared" of $z$ as a point in the plane.

The corresponding **Euclidean norm** is

$$
\|z\|_E = \sqrt{a^2 + b^2}.
$$

It is a genuine norm on the real vector space $\mathbb{D} \cong \mathbb{R}^2$: positive-definite, subadditive, and homogeneous of degree one. It is **not** multiplicative with respect to the split complex product, because the split complex product does not preserve the Euclidean norm.

## The Inner Product

The **inner product** of two split complex numbers $z = a + bj$ and $w = c + dj$ is

$$
\langle z, w \rangle = a c + b d.
$$

It is the ordinary Euclidean inner product on $\mathbb{R}^2$, written in split complex notation. It is real-valued, symmetric, and bilinear.

The inner product of a split complex number with itself is

$$
\langle z, z \rangle = a^2 + b^2,
$$

which is the Euclidean norm squared. So the Euclidean norm is the restriction of the inner product to the diagonal.

Note that this inner product is **not** the same as the real part of $z \bar{w}$. Indeed,

$$
z \bar{w} = (a + bj)(c - dj) = (ac - bd) + (bc - ad) j,
$$

so

$$
\operatorname{Re}(z \bar{w}) = ac - bd,
$$

which is the indefinite form, not the Euclidean one. The Euclidean inner product is $\operatorname{Re}(z \tilde{w})$ where $\tilde{w}$ is the idempotent conjugate, which coincides with $\bar{w}$ in this algebra. So the distinction between the two forms is the distinction between the indefinite and the Euclidean structures on $\mathbb{R}^2$, and it is the source of the difference between split complex analysis and ordinary real analysis in the plane.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $e_0 = 1$ | Identity |
| $e_1 = j$ | Split imaginary unit, $j^2 = +1$ |
| $z = a + b j$ | General split complex number |
| $a = \operatorname{Re} z$ | Real part |
| $b = \operatorname{Im} z$ | Imaginary part |
| $e_+ = (1 + j)/2$ | Positive idempotent |
| $e_- = (1 - j)/2$ | Negative idempotent |
| $\bar{z} = a - b j$ | Split complex conjugate |
| $\tilde{z} = \bar{z}$ | Idempotent conjugate |
| $N(z) = z \bar{z} = a^2 - b^2$ | Norm form (indefinite) |
| $a^2 + b^2$ | Euclidean norm squared |
| $\langle z, w \rangle = ac + bd$ | Euclidean inner product |
| $\|z\|_E = \sqrt{a^2 + b^2}$ | Euclidean norm |
| $\mathbb{R}_{\mathbb{D}}$ | Real subspace, fixed-point set of $\bar{\cdot}$ |
| $j \mathbb{R}_{\mathbb{D}}$ | Imaginary subspace, $-1$ eigenspace of $\bar{\cdot}$ |
| $\mathbb{D} e_+, \mathbb{D} e_-$ | Idempotent ideals |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the split complex algebra in the biquaternion program.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of SL(2, ℝ)* (Imperial College Press, 2012), for the analytic applications.

