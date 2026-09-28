
# __Split-Complex Algebra__

## Introduction

This article introduces the split complex algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real subspaces that arise from the natural conjugations: the real and split imaginary lines, and the two idempotent lines.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The idempotent decomposition is defined algebraically.

The split complex algebra is the two-dimensional real algebra $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, written in a generator $j$ with $j^2 = +1$. It is the indefinite member of the two-dimensional pair whose definite member is the field $\mathbb{C}$ of complex numbers; the two share their basis, their conjugation and their dimension and differ in the sign of the square of the imaginary unit. The complex numbers are assumed from *Complex Algebra*, together with their basis, their multiplication and their conjugation, and no facts about them are restated here except where the comparison is the point.

## The Split Complex Algebra

### Definition

The **split complex algebra** is the two-dimensional real algebra with basis

$$
1, \qquad j,
$$

and multiplication rules

$$
j^2 = +1.
$$

A general split complex number is written in developed form as

$$
Z = a + j b, \qquad a, b \in \mathbb{R},
$$

in the basis $\{1, j\}$. The real number $a$ is the **real part** and the real number $b$ is the **imaginary part**:

$$
a = \operatorname{Re} Z, \qquad b = \operatorname{Im} Z.
$$

The notation $j$ is chosen deliberately. In the complex algebra the imaginary unit satisfies $i^2 = -1$. In the split complex algebra the unit satisfies $j^2 = +1$. Writing $j$ rather than $i$ makes the sign explicit and avoids confusion with the complex case; this is the notation used throughout the category.

### The Real Algebra View

Unlike the biquaternion algebra, which is a complex algebra and a real algebra at once, the split complex algebra has a single ground field. It is a **two-dimensional algebra over $\mathbb{R}$**: its basis is $\{1, j\}$, every element is a real linear combination of the two basis elements, and the multiplication is $\mathbb{R}$-bilinear. The center is all of $\mathbb{D}$, because the algebra is commutative.

There is no second ground field to pass to, and no scalar imaginary inside the algebra. This is the first of the systematic differences from the four-dimensional members of the family, and it is the reason the subspace lattice below collapses.

### Developed Form

Equivalently, $\mathbb{D}$ is the quotient ring

$$
\mathbb{D} = \mathbb{R}[x]/(x^2-1),
$$

the image of the generator $x$ being $j$. Since $x^2 - 1 = (x-1)(x+1)$ is not prime, the quotient is not a field but a product of two copies of $\mathbb{R}$; that product is exhibited explicitly in *The Isomorphism with $\mathbb{R}\oplus\mathbb{R}$* below.

### The Algebra Structure

The algebra $\mathbb{D}$ is a two-dimensional commutative, associative and unital algebra over $\mathbb{R}$, with unit $1$. As a ring it is a commutative ring with zero divisors. It is **not** a division algebra: the elements $1+j$ and $1-j$ are non-zero, but

$$
(1+j)(1-j) = 1 - j^2 = 0.
$$

So $\mathbb{D}$ is not a field, and not a division algebra. This is the fundamental difference from $\mathbb{C}$, and it is the source of everything that distinguishes the two theories.

**Frobenius theorem.** The finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$. The split complex algebra is a commutative associative real algebra of dimension two that is not a division algebra, so it lies outside that list; it is not one of the three.

### Multiplication

The product of two split complex numbers is defined by extending the real multiplication bilinearly:

$$
Z W = (a + j b)(c + j d) = (a c + b d) + (a d + b c) j, \qquad Z = a + j b, \quad W = c + j d.
$$

In developed form,

$$
Z W = \sum_{\mu=0}^{1} \sum_{\nu=0}^{1} Z_\mu W_\nu \, e_\mu e_\nu,
$$

where the products $e_\mu e_\nu$ are those of the split complex algebra. The multiplication is commutative and associative, and $1$ is the two-sided unit.

### Conjugations

There are **two** natural conjugations on $\mathbb{D}$, and they turn out to coincide.

**Split complex conjugation** $\bar{Z}$:

$$
\bar{Z} = a - j b.
$$

It is the extension of the identity on $\mathbb{R}$ that sends $j$ to $-j$, it is $\mathbb{R}$-linear, and it is an algebra involution: $\overline{Z W} = \bar{Z}\,\bar{W}$ and $\overline{\bar{Z}} = Z$.

**Idempotent conjugation** (the swap):

$$
\tilde{Z} = (a - b) \Pi_1 + (a + b) \Pi_2.
$$

In the basis $\{1, j\}$ the idempotent conjugation is

$$
\tilde{Z} = a - j b = \bar{Z}.
$$

So in the split complex algebra the split complex conjugation and the idempotent conjugation coincide. The coincidence is a special feature of the two-dimensional case: the conjugation induced on $\mathbb{D}$ by the idempotent basis is the same map as the conjugation of the algebra, because the single non-trivial involution has only one non-trivial choice to make.

Each conjugation is an involution: applying it twice returns the original split complex number. Each therefore splits $\mathbb{D}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{D}$; those subspaces are described in the following sections.

### The Group of Conjugations

The split complex conjugation $\bar{\cdot}$ is an involution distinct from the identity, so the conjugation group is

$$
\{\mathrm{id}, \bar{\cdot}\} \cong \mathbb{Z}/2.
$$

There is no second independent involution, hence no Klein four-group and no Hermitian or anti-Hermitian conjugation. This is the systematic degeneration of the two-dimensional case: the biquaternion algebra carries the Klein four-group $\{\mathrm{id}, \bar{\cdot}, {}^{*}, {}^{\dagger}\}$ of three commuting involutions, and each of those involutions contributes two subspaces; here there is one non-trivial involution, and it contributes the pair of lines below. The idempotent conjugation does not enlarge the group, since it is the same map.

## The Distinguished Subspaces

The single non-trivial involution $\bar{\cdot}$ splits $\mathbb{D}$ into its fixed space and its anti-fixed space, two real vector subspaces of dimension $1$. The idempotent basis, developed below, cuts the algebra into its two primitive lines; it is the finest decomposition of $\mathbb{D}$, and it names the two null directions in place of the two coordinate axes.

### The Real Subspace

The fixed points of split complex conjugation are the split complex numbers satisfying $\bar{Z} = Z$. In developed form,

$$
a - j b = a + j b.
$$

Comparing the coefficients of $1$ and $j$:

- coefficient of $1$: $a = a$, always satisfied;
- coefficient of $j$: $-b = b$, so $b = 0$.

The fixed points are split complex numbers with vanishing imaginary part:

$$
Z = a, \qquad a \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{D}}$, a copy of the real line embedded in $\mathbb{D}$ as the real axis. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{D}$ isomorphic to $\mathbb{R}$, and as a ring it is a field. The form it carries is treated in *Split-Complex Norm and Invertibility*.

### The Split Imaginary Subspace

The anti-fixed points of split complex conjugation are the split complex numbers satisfying $\bar{Z} = -Z$, which forces $a = 0$:

$$
Z = j b, \qquad b \in \mathbb{R}.
$$

This is the **split imaginary subspace** $j\mathbb{R}_{\mathbb{D}}$, a real vector space of dimension $1$. It is not a subalgebra: $(j b)^2 = b^2 \in \mathbb{R}_{\mathbb{D}}$, which is not in $j\mathbb{R}_{\mathbb{D}}$ unless $b = 0$. The form it carries is treated in *Split-Complex Norm and Invertibility*.

There is only one non-trivial fixed-point set and one non-trivial anti-fixed-point set, because there is only one non-trivial involution. The six-subspace lattice of the biquaternion algebra therefore has no analogue here: the involution lattice of $\mathbb{D}$ is the single edge $\{0\}\subset\mathbb{Z}/2$ drawn on the two lines.

### The Idempotent Basis

Define the **idempotents**

$$
\Pi_1 = \frac{1 + j}{2}, \qquad \Pi_2 = \frac{1 - j}{2}.
$$

They satisfy

$$
\Pi_1^2 = \Pi_1, \qquad \Pi_2^2 = \Pi_2, \qquad \Pi_1 \Pi_2 = \Pi_2 \Pi_1 = 0, \qquad \Pi_1 + \Pi_2 = 1.
$$

A general split complex number is written uniquely in the idempotent basis as

$$
Z = a + j b = (a + b) \Pi_1 + (a - b) \Pi_2.
$$

This is the **idempotent decomposition** of $Z$. It is the single most important structural fact about the split complex algebra, and the two lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ are the finest direct summands of the algebra.

### The Isomorphism with $\mathbb{R} \oplus \mathbb{R}$

The map

$$
\varphi : \mathbb{D} \to \mathbb{R} \oplus \mathbb{R}, \qquad \varphi(a + j b) = (a + b, a - b),
$$

is an algebra isomorphism. It is bijective, and it satisfies

$$
\varphi(Z + W) = \varphi(Z) + \varphi(W), \qquad \varphi(Z W) = \varphi(Z) \varphi(W),
$$

where the multiplication on $\mathbb{R} \oplus \mathbb{R}$ is componentwise:

$$
(u_1, u_2)(v_1, v_2) = (u_1 v_1, u_2 v_2).
$$

So $\mathbb{D}$ is not a new algebra. It is $\mathbb{R} \oplus \mathbb{R}$ in disguise. Everything that can be said about $\mathbb{D}$ is a statement about pairs of real numbers, and everything that is surprising about $\mathbb{D}$ is a consequence of the fact that the disguise hides the zero divisors: the pairs with one coordinate zero are exactly the zero divisors.

## The Split Complex Decomposition

The real subspace $\mathbb{R}_{\mathbb{D}}$ and the split imaginary subspace $j\mathbb{R}_{\mathbb{D}}$ are the two eigenspaces of split complex conjugation. Every split complex number decomposes uniquely as the sum of a real part and an imaginary part:

$$
Z = Z_r + j Z_i, \qquad Z_r = a, \quad Z_i = b.
$$

The two components are obtained from the split complex conjugation:

$$
Z_r = \frac{1}{2}(Z + \bar{Z}), \qquad Z_i = \frac{1}{2j}(Z - \bar{Z}) = b.
$$

Indeed, $Z_r$ is fixed by split complex conjugation, so it lies in $\mathbb{R}_{\mathbb{D}}$, and $Z_i = b$ is real, so $j Z_i$ lies in $j \mathbb{R}_{\mathbb{D}}$. The sum is $Z_r + j Z_i = Z$.

This gives the direct sum decomposition

$$
\mathbb{D} = \mathbb{R}_{\mathbb{D}} \oplus j \mathbb{R}_{\mathbb{D}},
$$

where $j \mathbb{R}_{\mathbb{D}}$ is the set of split complex numbers of the form $j b$ with $b \in \mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{D}$ of real dimension $2$.

This is the **split complex decomposition** of a split complex number. It expresses $Z$ as a real number plus $j$ times another real number. In the biquaternion algebra the analogous decomposition is the quaternion decomposition $\mathbb{B} = \mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$; here the two summands are the two eigenspaces of the unique non-trivial involution.

## The Idempotent Decomposition

The idempotent decomposition is the second natural decomposition of $\mathbb{D}$, and it is not the eigenspace decomposition of an involution:

$$
Z = Z_+ \Pi_1 + Z_- \Pi_2, \qquad Z_+ = a + b, \quad Z_- = a - b.
$$

The two components are obtained from the idempotents:

$$
Z_+ = Z \Pi_1, \qquad Z_- = Z \Pi_2,
$$

which, since $\mathbb{D}$ is commutative, is unambiguous.

This gives the direct sum decomposition

$$
\mathbb{D} = \mathbb{D} \Pi_1 \oplus \mathbb{D} \Pi_2,
$$

where $\mathbb{D} \Pi_1$ and $\mathbb{D} \Pi_2$ are the two ideals of $\mathbb{D}$, each isomorphic to $\mathbb{R}$. Both are real vector spaces of dimension $1$, and their direct sum is the full algebra $\mathbb{D}$ of real dimension $2$.

The idempotent decomposition and the split complex decomposition are related by

$$
Z_+ = Z_r + Z_i, \qquad Z_- = Z_r - Z_i.
$$

So the idempotent components are the sum and difference of the real and imaginary parts.

## Zero Divisors

**Definition.** An element $Z \in \mathbb{D}$ is a **zero divisor** if $Z \neq 0$ and there exists $W \in \mathbb{D}$ with $W \neq 0$ and $ZW = 0$; the **annihilator** of $Z$ is the ideal

$$
\operatorname{ann}(Z) = \{W \in \mathbb{D} : ZW = 0\}.
$$

The algebra has zero divisors already among its primitive elements:

$$
(1+j)(1-j) = 1 - j^2 = 0,
$$

so $1+j$ and $1-j$ are non-zero elements with zero product, and $\mathbb{D}$ is not a domain.

**Proposition.** Write $Z = Z_+\Pi_1 + Z_-\Pi_2$ in the idempotent basis, with $Z$ not both coordinates zero. Then $Z$ is a zero divisor if and only if one of $Z_+, Z_-$ vanishes; if both are nonzero then $Z$ is a unit, with inverse

$$
Z^{-1} = Z_+^{-1}\Pi_1 + Z_-^{-1}\Pi_2.
$$

**Proof.** In the idempotent basis multiplication is componentwise, $ZW = Z_+W_+\Pi_1 + Z_-W_-\Pi_2$. If $Z_+ = 0$ then $Z\Pi_1 = Z_-\Pi_2\Pi_1 = 0$ with $\Pi_1 \neq 0$, so $Z$ is a zero divisor, and symmetrically for $Z_- = 0$. If both coordinates are nonzero, the displayed formula gives $Z Z^{-1} = \Pi_1 + \Pi_2 = 1$, so $Z$ is a unit, and a unit is never a zero divisor.

So the zero divisors are exactly the non-zero elements of the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, and the non-units of $\mathbb{D}$ are $0$ together with the zero divisors. The classification of the zero-divisor set, its two families and its relation to the isotropic cone are the subject of *Split-Complex Zero Divisors*; the criterion by the norm belongs to *Split-Complex Norm and Invertibility*, where the norm, the Hermitian form and the inner product — a form and a distance — are treated.

## Summary

The split complex algebra $\mathbb{D}$ is the two-dimensional real algebra with basis $1$, $j$ and the relation $j^2 = +1$. It is commutative, associative and unital, and it is not a field: it has zero divisors. A general element is written $Z = a + j b$, and the algebra is $\mathbb{R}[x]/(x^2-1)$.

Split complex conjugation sends $a + j b$ to $a - j b$; it is the unique non-trivial involution, and the idempotent conjugation coincides with it, so the conjugation group is $\mathbb{Z}/2$. Its fixed points form the real subspace $\mathbb{R}_{\mathbb{D}}$ and its anti-fixed points the split imaginary subspace $j\mathbb{R}_{\mathbb{D}}$; these are the eigenspaces for the eigenvalues $+1$ and $-1$, and every split complex number decomposes uniquely as a real part plus an imaginary part. The algebra carries a second natural decomposition, which the complex case does not have: the idempotent decomposition $Z = Z_+\Pi_1 + Z_-\Pi_2$, where $\Pi_\pm = (1 \pm j)/2$ are the two nontrivial idempotents and $Z_\pm = a \pm b$. The two components are independent ring homomorphisms, so $\mathbb{D}$ is the direct sum $\mathbb{R} \oplus \mathbb{R}$.

The algebra has zero divisors: $(1+j)(1-j) = 0$, and in the idempotent basis a non-zero element $Z = Z_+\Pi_1 + Z_-\Pi_2$ is a zero divisor exactly when one of its two coordinates vanishes, while it is a unit with $Z^{-1} = Z_+^{-1}\Pi_1 + Z_-^{-1}\Pi_2$ exactly when both are nonzero. The zero divisors are therefore the non-zero elements of the two idempotent lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, classified in *Split-Complex Zero Divisors*. The norm, the Hermitian form and the inner product are a form and a distance and belong to *Split-Complex Norm and Invertibility*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra, $\mathbb{R}[x]/(x^2-1)$ |
| $1$ | Identity |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $Z = a + j b$ | General split complex number |
| $a = \operatorname{Re} Z$ | Real part |
| $b = \operatorname{Im} Z$ | Imaginary part |
| $\bar{Z} = Z^{*} = a - j b$ | Split complex conjugate (the unique non-trivial involution) |
| $\tilde{Z} = \bar{Z}$ | Idempotent conjugate; equal to $\bar{Z}$ |
| $\Pi_1 = (1 + j)/2$ | Positive idempotent |
| $\Pi_2 = (1 - j)/2$ | Negative idempotent |
| $Z = Z_+ \Pi_1 + Z_- \Pi_2$ | Idempotent decomposition, $Z_\pm = a \pm b$ |
| $\operatorname{ann}(Z)$ | Annihilator, the ideal $\{W : ZW = 0\}$ |
| $\mathbb{R}_{\mathbb{D}}$ | Real subspace, fixed-point set of $\bar{\cdot}$ |
| $j \mathbb{R}_{\mathbb{D}}$ | Split imaginary subspace, $-1$ eigenspace of $\bar{\cdot}$ |
| $\mathbb{D} \Pi_1, \mathbb{D} \Pi_2$ | The two ideals, isomorphic to $\mathbb{R}$ |

## Further Reading

- William Kingdon Clifford, *Preliminary Sketch of Biquaternions* (1873), for the origin of the split complex algebra in the biquaternion program.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
