
# __Dual-Numbers Algebra__

## Introduction

This article introduces the dual number algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished real vector subspaces that arise from the natural conjugation.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given, and no applications are discussed. The algebra is defined over an arbitrary commutative ring in which the defining nilpotent is available, and the specializations to specific rings are left for the reader.

Throughout this article, the algebra of dual numbers is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The notation is chosen so that the two do not collide. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## The Dual Numbers

### Definition

Let $R$ be a commutative ring with identity in which $2$ is invertible. The **dual number algebra** $\mathbb{D}'_R$ is the quotient ring

$$
\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2),
$$

equivalently the two-dimensional free $R$-module with basis $1, \varepsilon$ and the single multiplication rule $\varepsilon^2 = 0$. A general dual number is written as

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

and the product of two dual numbers is

$$
Z W = (a + \varepsilon b)(c + \varepsilon d) = a c + (a d + b c)\,\varepsilon.
$$

The element $a$ is the **real part** and $b$ the **infinitesimal part**, written

$$
a = \operatorname{Re} Z, \qquad b = \operatorname{Inf} Z.
$$

The notation $\varepsilon$ is chosen deliberately. In some of the older literature the nilpotent unit is written $i$ or $j$, which collides with the imaginary unit of the complex numbers or with the hyperbolic unit of the split complex numbers; using $\varepsilon$ for the nilpotent unit and reserving $i$ and $j$ for those two cases avoids the collision. The split complex algebra is written $\mathbb{D}$ throughout, so that it does not collide with $\mathbb{D}'$. When $R = \mathbb{R}$ we write $\mathbb{D}'$ for $\mathbb{D}'_{\mathbb{R}}$.

### Basic Properties

**Commutative.** Dual multiplication is commutative, $ZW = WZ$.

**Associative.** Dual multiplication is associative, $(ZW)u = Z(Wu)$.

**Unit and rank.** The identity is $1$, and $\mathbb{D}'_R$ is a free $R$-module of rank $2$.

**Not a division algebra.** The element $\varepsilon$ is non-zero and satisfies $\varepsilon^2 = 0$, so $\varepsilon$ is a zero divisor. A division algebra is precisely an algebra in which every non-zero element is invertible, so the non-zero nilpotent $\varepsilon$ shows that $\mathbb{D}'_R$ is neither a field nor a division algebra. This is the source of everything that distinguishes it from $\mathbb{C}$.

**Not semisimple.** The ideal $(\varepsilon)$ is nilpotent of index two, $\varepsilon^2 = 0$ with $\varepsilon \neq 0$. Over a field the algebra is local with unique maximal ideal $(\varepsilon)$, and the presence of this non-zero nilpotent ideal makes the algebra not semisimple; the ideal theory is developed in *Dual-Numbers Ideals and the Maximal Ideal*.

**Frobenius theorem.** The dual algebra is not one of the three finite-dimensional associative real division algebras $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$: it is a commutative associative two-dimensional real algebra, and it is not a division algebra.

### Conjugations

There are **two** natural conjugations on $\mathbb{D}'_R$:

**Dual conjugation** $\bar{Z} = a - \varepsilon b$ and **identity conjugation** $\operatorname{id}(Z) = Z$. Each is an involution, and each has a fixed-point set, an $R$-submodule of $\mathbb{D}'_R$, described in the next section.

### The Isomorphism with $R[\varepsilon]/(\varepsilon^2)$

The definition presents the algebra as the quotient ring $\mathbb{D}'_R \cong R[\varepsilon]/(\varepsilon^2)$, the ring of polynomials in $\varepsilon$ modulo $\varepsilon^2$. The ideal $(\varepsilon)$ is nilpotent of index two and the quotient by it is $R$. Over a field $k$ this is the simplest example of a local ring that is not a field: $\mathbb{D}'_k$ has the unique maximal ideal $(\varepsilon)$. Over a general commutative ring the maximal ideals of $\mathbb{D}'_R$ correspond to those of $R$, as recorded in *Dual-Numbers Ideals and the Maximal Ideal*.

**Remark.** For $n \geq 1$ the ring $R[\varepsilon]/(\varepsilon^{n+1})$ is the **truncated polynomial algebra** of order $n$, the ring of polynomials in $\varepsilon$ modulo $\varepsilon^{n+1}$; the case $n = 1$ recovers the dual numbers and the case $n = 0$ gives $R$ itself. The higher cases are used in *Dual-Numbers Integration*.

## The Two Fixed-Point Submodules

Each of the two conjugations has a fixed-point set. The two submodules are described below.

### The Real Submodule

The fixed points of **dual conjugation** are the dual numbers satisfying $\bar{Z} = Z$. In developed form,

$$
a - \varepsilon b = a + \varepsilon b.
$$

Comparing the coefficients of $1$ and $\varepsilon$:

- Coefficient of $1$: $a = a$, always satisfied.
- Coefficient of $\varepsilon$: $-b = b$, so $2b = 0$.

If $2$ is invertible in $R$, then $b = 0$. In that case, the fixed points are dual numbers with vanishing infinitesimal part:

$$
Z = a, \qquad a \in R.
$$

This is the **real submodule** $R_{\mathbb{D}'}$, a copy of $R$ embedded in $\mathbb{D}'_R$ as the real axis. It is an $R$-module of rank $1$. It is a subalgebra of $\mathbb{D}'_R$ (isomorphic to $R$).

If $2$ is not invertible in $R$, the fixed-point set is larger, and the theory requires more care. We assume from this point on that $2$ is invertible in $R$.

### The Infinitesimal Submodule

The fixed points of the **identity conjugation** are all dual numbers. In developed form,

$$
Z = Z.
$$

The fixed points are

$$
Z = a + \varepsilon b, \qquad a, b \in R.
$$

This is the **dual submodule** $\mathbb{D}'_{\mathbb{D}'}$, a copy of the dual algebra embedded in itself as the whole thing. It is an $R$-module of rank $2$. It is a subalgebra of $\mathbb{D}'_R$.

The **infinitesimal submodule** $\varepsilon R_{\mathbb{D}'}$ is not a fixed-point set of either conjugation; it is the set of dual numbers of the form $\varepsilon b$ with $b \in R$. It is the maximal ideal of $\mathbb{D}'_R$, and it is nilpotent of index two.

## Dual Decomposition

The real submodule $R_{\mathbb{D}'}$ and the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ are the two eigenspaces of dual conjugation. Every dual number decomposes uniquely as the sum of a real part and an infinitesimal part:

$$
Z = Z_r + \varepsilon Z_i, \qquad Z_r \in R, \quad Z_i \in R.
$$

The two components are obtained from the dual conjugation:

$$
Z_r = \frac{1}{2}(Z + \bar{Z}), \qquad Z_i = \frac{1}{2\varepsilon}(Z - \bar{Z}).
$$

The first formula is well-defined because $2$ is invertible in $R$. The second formula is formal: it says that $Z - \bar{Z} = 2\varepsilon b$, so dividing by $2\varepsilon$ recovers $b$. The division by $\varepsilon$ is not an algebra operation, because $\varepsilon$ is not invertible. So the second formula is a convenient notation, not a computation in the algebra.

This gives the direct sum decomposition

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'},
$$

where $\varepsilon R_{\mathbb{D}'}$ is the maximal ideal. Both are $R$-modules of rank $1$, and their direct sum is the full algebra $\mathbb{D}'_R$ of rank $2$.

This is the **dual decomposition** of a dual number. It expresses $Z$ as a real number plus $\varepsilon$ times another real number.

## Conjugate Decomposition

The dual conjugation $\bar{\cdot}$ is an involution, so it has eigenvalues $+1$ and $-1$. Its eigenspaces are the real submodule $R_{\mathbb{D}'}$ (eigenvalue $+1$) and the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ (eigenvalue $-1$). Every dual number decomposes uniquely as

$$
Z = Z_+ + Z_-, \qquad Z_+ = Z_r, \quad Z_- = \varepsilon Z_i.
$$

This is the same decomposition as above, written in terms of the eigenspaces of the conjugation.

## The Maximal Ideal

The ideal $(\varepsilon)$ of $\mathbb{D}'_R$ is

$$
\mathrm{M} = (\varepsilon) = \{\varepsilon b : b \in R\}.
$$

It is the set of elements with vanishing real part. It is nilpotent of index two:

$$
\mathrm{M}^2 = 0.
$$

**Theorem (basic properties of the maximal ideal).**

- $\mathrm{M} = (\varepsilon)$ is a nilpotent ideal of index two, and $\mathrm{M}^2 = 0$.
- The quotient $\mathbb{D}'_R / \mathrm{M}$ is isomorphic to $R$.
- Over a field $k$, $\mathrm{M}$ is the **unique** maximal ideal of $\mathbb{D}'_k$, so $\mathbb{D}'_k$ is local with residue field $k$. Over a general commutative ring $R$ the maximal ideals of $\mathbb{D}'_R$ are the ideals $\mathrm{P} + \mathrm{M} = \mathrm{P} \oplus R\varepsilon$ for $\mathrm{P}$ maximal in $R$; hence $\mathbb{D}'_R$ is local if and only if $R$ is local.
- The element $a + \varepsilon b$ is invertible if and only if $a \in R^\times$ (see the group of units below); over a field this says: every element not in $\mathrm{M}$ is invertible.

The maximal ideal is the obstruction to the algebra being a field, and it is the source of the nilpotence in the algebra.

## The Group of Units

**Theorem (group of units).** The **group of units** of $\mathbb{D}'_R$ is

$$
(\mathbb{D}'_R)^\times = \{a + \varepsilon b : a \in R^\times\}.
$$

An element is invertible if and only if its real part is invertible in $R$. The inverse is

$$
(a + \varepsilon b)^{-1} = a^{-1} - a^{-1} b a^{-1} \varepsilon.
$$

When $R$ is commutative, this simplifies to

$$
(a + \varepsilon b)^{-1} = \frac{1}{a} - \frac{b}{a^2} \varepsilon.
$$

The group of units is an extension of $R^\times$ by the additive group $R$:

$$
1 \to R \to (\mathbb{D}'_R)^\times \to R^\times \to 1,
$$

where the kernel is the maximal ideal $\mathrm{M} \cong R$ and the quotient is $R^\times$.

## The Lie Algebra Structure

The dual algebra carries a Lie bracket, defined by the commutator

$$
[Z, W] = ZW - WZ.
$$

Since $\mathbb{D}'_R$ is commutative, the commutator is identically zero. So the Lie algebra structure of $\mathbb{D}'_R$ is trivial. This is the fundamental difference from the quaternion case, where the commutator is non-trivial (the split complex algebra, like the dual algebra, is commutative).

The **Lie algebra of derivations** of $\mathbb{D}'_R$ is more interesting. A **derivation** is an $R$-linear map $D : \mathbb{D}'_R \to \mathbb{D}'_R$ satisfying the Leibniz rule

$$
D(xy) = D(x) y + x D(y).
$$

**Theorem.** Every derivation of $\mathbb{D}'_R$ is of the form

$$
D(a + \varepsilon b) = c \varepsilon b,
$$

for some $c \in R$. In other words, the derivation is determined by its value on $\varepsilon$, and it maps the real part to zero.

**Proof.** Let $D$ be a derivation. Since $D(1) = D(1 \cdot 1) = 2D(1)$, we have $D(1) = 0$ when $2$ is invertible. Then $D(a) = a D(1) = 0$ for all $a \in R$. So $D$ is determined by $D(\varepsilon)$. Since $D(\varepsilon^2) = D(0) = 0$ while $D(\varepsilon^2) = 2 \varepsilon D(\varepsilon)$, we have $\varepsilon D(\varepsilon) = 0$, so $D(\varepsilon)$ lies in the ideal $(\varepsilon)$. Write $D(\varepsilon) = \varepsilon c$ for some $c \in R$. Then

$$
D(a + \varepsilon b) = D(a) + D(b) \varepsilon + b D(\varepsilon) = b \varepsilon c.
$$

So every derivation is of the stated form.

The module of derivations is isomorphic to $R$, and it is generated by the derivation $\partial_\varepsilon$ that sends $a + \varepsilon b$ to $\varepsilon b$. This derivation is the algebraic content of the derivative: it sends each element to $\varepsilon$ times its infinitesimal part.

## Summary

The dual number algebra $\mathbb{D}'_R$ is the two-dimensional free $R$-module with basis $1$, $\varepsilon$ and the single relation $\varepsilon^2 = 0$. It is commutative and associative with unit, and it is not a field: the element $\varepsilon$ is a nonzero nilpotent. A general element is written $Z = a + \varepsilon b$, with $a$ its real part and $b$ its infinitesimal part.

Dual conjugation is the involution sending $a + \varepsilon b$ to $a - \varepsilon b$. Its fixed points form the real submodule $R_{\mathbb{D}'}$ and its anti-fixed points the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$; these are the eigenspaces for the eigenvalues $+1$ and $-1$, and every dual number decomposes uniquely both as a real part plus an infinitesimal part and as the sum of the two eigencomponents.

The algebra is characterised by its ideal $(\varepsilon)$. The ideal $\mathrm{M} = (\varepsilon)$ is the set of elements of vanishing real part; it is nilpotent of index two, $\mathrm{M}^2 = 0$, and the quotient $\mathbb{D}'_R/\mathrm{M}$ is $R$. Over a field it is the unique maximal ideal, so $\mathbb{D}'_k$ is local; over a general commutative ring the maximal ideals of $\mathbb{D}'_R$ correspond to those of $R$, and the algebra is local exactly when the base ring is. The element $a + \varepsilon b$ is a unit exactly when its real part $a$ is a unit of $R$, so the group of units is $\{a + \varepsilon b : a \in R^\times\}$; the scale and the norm that measure this are a distance and are developed in *Dual-Numbers Norm and Invertibility*. Because the algebra is commutative the commutator vanishes identically and the Lie algebra structure is abelian, while the derivations form a free $R$-module of rank one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra over $\mathbb{R}$ |
| $\mathbb{D}'_R$ | Dual number algebra over $R$ |
| $1$ | Identity |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $1$, $\varepsilon$ | The $R$-basis of $\mathbb{D}'_R$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$ | Real part |
| $b = \operatorname{Inf} Z$ | Infinitesimal part |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation |
| $\operatorname{id}(Z) = Z$ | Identity conjugation |
| $R_{\mathbb{D}'}$ | Real submodule, fixed-point set of $\bar{\cdot}$ |
| $\varepsilon R_{\mathbb{D}'}$ | Infinitesimal submodule, maximal ideal |
| $\mathrm{M} = (\varepsilon)$ | The nilpotent ideal $(\varepsilon)$, $\mathrm{M}^2 = 0$; the unique maximal ideal over a field |
| $\partial_\varepsilon(a + \varepsilon b) = \varepsilon b$ | The derivation, $\operatorname{Der}_R(\mathbb{D}'_R) \cong R$ |
| $[Z, W] = ZW - WZ$ | Lie bracket, identically zero |
| $(\mathbb{D}'_R)^\times = \{a + \varepsilon b : a \in R^\times\}$ | Group of units |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, Reading, 1969), for local rings, nilpotent ideals and the maximal ideal.
- Serge Lang, *Algebra*, 3rd ed. (Springer, New York, 2002), for the structure of algebras over a commutative ring and their ideals.

