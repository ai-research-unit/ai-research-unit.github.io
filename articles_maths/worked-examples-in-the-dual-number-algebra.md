
# __Worked Examples in the Dual-Number Algebra__

## Introduction

This article collects explicit computations in the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, in the spirit of the worked computation that accompanies the algebra of a number system. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the norm form and the criterion for invertibility, *Dual-Numbers Ideals and the Maximal Ideal* for the ideal structure, *Dual-Numbers Zero Divisors* for the zero-divisor classification. Every computation was recomputed in exact rational arithmetic; where a floating-point value appears it is flagged.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Unless a statement is labelled otherwise, the base is $R = \mathbb{R}$ and the algebra is $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in \mathbb{R},
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, dual conjugation $\bar{Z} = a - \varepsilon b$, norm form $N(Z) = Z\bar{Z} = a^2$, and maximal ideal $\mathfrak{m} = (\varepsilon)$. The two distinguished submodules are $R_{\mathbb{D}'} = \mathbb{R}\cdot 1$ and $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$.

Each computation below is a worked instance of a general result proved in a companion article; the instance is stated with its reference, so that the article remains a table of examples rather than a second proof of the theory.

## The Algebra in Coordinates

### The Basis and the Product

The algebra has the basis $\{1, \varepsilon\}$ with the multiplication table

| $\cdot$ | $1$ | $\varepsilon$ |
|---|---|---|
| $1$ | $1$ | $\varepsilon$ |
| $\varepsilon$ | $\varepsilon$ | $0$ |

**Example (product, worked).** For $Z = 2 + 3\varepsilon$ and $W = 4 + 5\varepsilon$,

$$
ZW = (2\cdot 4) + (2\cdot 5 + 3\cdot 4)\varepsilon = 8 + 22\varepsilon.
$$

The real parts multiply, and the infinitesimal part is $a\,d + b\,c$; the cross terms do not interact, because $\varepsilon^2 = 0$.

**Example (squaring, worked).** For $Z = a + \varepsilon b$, the square is

$$
Z^2 = a^2 + 2ab\,\varepsilon.
$$

In particular $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon$ and $(\varepsilon)^2 = 0$.

### The Conjugate and the Norm

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$ and

$$
N(2 + 3\varepsilon) = (2 + 3\varepsilon)(2 - 3\varepsilon) = 4.
$$

The norm form ignores the infinitesimal part: $N(2 + 3\varepsilon) = N(2) = 4 = 2^2$.

## The Two Involutions

### The Identity Involution

The identity map $\operatorname{id}(Z) = Z$ is an involutive algebra automorphism. Its fixed-point submodule is the whole algebra $\mathbb{D}'$, and the associated $\pm1$-eigenspace decomposition is the trivial one, with eigenvalue $+1$ everywhere.

### The Dual Conjugation

Dual conjugation is

$$
\bar{\cdot} : a + \varepsilon b \longmapsto a - \varepsilon b.
$$

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$; applying it twice returns $2 + 3\varepsilon$, so $\bar{\bar{Z}} = Z$. It is an algebra automorphism: $\overline{ZW} = \bar{Z}\bar{W}$, checked on the worked product by $\overline{8 + 22\varepsilon} = 8 - 22\varepsilon$ and $(2 - 3\varepsilon)(4 - 5\varepsilon) = 8 - 22\varepsilon$.

### The Fixed-Point Submodules

**Proposition.** The $+1$-eigenspace of dual conjugation is the real submodule

$$
R_{\mathbb{D}'} = \{Z : \bar{Z} = Z\} = \{a : a \in \mathbb{R}\},
$$

and the $-1$-eigenspace is the infinitesimal submodule

$$
\varepsilon R_{\mathbb{D}'} = \{Z : \bar{Z} = -Z\} = \{b\varepsilon : b \in \mathbb{R}\}.
$$

**Proof.** $\bar{a + \varepsilon b} = a - \varepsilon b$ equals $a + \varepsilon b$ exactly when $b = 0$, and equals $-(a + \varepsilon b)$ exactly when $a = 0$; the two sets are as displayed. $\square$

**Example (worked projections).** For $Z = 2 + 3\varepsilon$,

$$
\tfrac{1}{2}(Z + \bar{Z}) = 2, \qquad \tfrac{1}{2}(Z - \bar{Z}) = 3\varepsilon,
$$

and indeed $2 + 3\varepsilon = 2 + 3\varepsilon$.

### The Intersection

**Proposition.** $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$, and $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$.

**Proof.** An element of the intersection satisfies $b = 0$ and $a = 0$, so it is zero. The sum decomposition is the worked projection identity above. $\square$

So the algebra has exactly **one** nontrivial involution, and the two submodules are the eigenspaces. The biquaternion algebra, by contrast, carries four conjugations and six eigenspace-type subspaces; here the lattice degenerates to two submodules and the single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = 0$.

## The Nilpotents and the Maximal Ideal

### Squaring the Maximal Ideal

**Example (worked).** Every element of $\mathfrak{m} = \varepsilon\mathbb{R}$ is nilpotent of index two:

$$
(3\varepsilon)^2 = 9\varepsilon^2 = 0, \qquad (-5\varepsilon)^2 = 25\varepsilon^2 = 0, \qquad (7\varepsilon)^2 = 0.
$$

So $\mathfrak{m}^2 = 0$ and $\mathfrak{m} \neq 0$: the maximal ideal is nilpotent of index exactly two.

**Example (worked).** A mixed element is never nilpotent: $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon \neq 0$, and more generally $(a + \varepsilon b)^n = a^n + na^{n-1}\varepsilon b$, which vanishes only when $a = 0$.

### The Powers of an Element

**Proposition.** For every integer $n \geq 1$, $(a + \varepsilon b)^n = a^n + n\,a^{n-1}\varepsilon b$, interpreted for $n = 1$ as the element itself.

**Proof.** Induction on $n$ using $(a + \varepsilon b)^n(a + \varepsilon b) = a^{n+1} + (n a^{n-1}b\,a + a^n b)\varepsilon = a^{n+1} + (n+1)a^n \varepsilon b$. $\square$

**Example (worked).** $(1 + \varepsilon)^{5} = 1 + 5\varepsilon$, and $(2 + \varepsilon)^3 = 8 + 12\varepsilon$.

## Explicit Zero-Divisor Pairs

### The General Pair

By *Dual-Numbers Zero Divisors* the zero divisors are exactly the nonzero elements of $\mathfrak{m}$, that is, the elements $\varepsilon b$ with $b \neq 0$, and any two of them multiply to zero:

$$
(\varepsilon b)(\varepsilon d) = bd\,\varepsilon^2 = 0 \qquad \text{for all } b, d.
$$

### A Table

Each row is a pair of nonzero zero divisors whose product is zero; the product is computed in the last column.

| $Z$ | $W$ | $ZW$ |
|---|---|---|
| $\varepsilon$ | $\varepsilon$ | $0$ |
| $2\varepsilon$ | $5\varepsilon$ | $0$ |
| $-3\varepsilon$ | $\varepsilon$ | $0$ |
| $7\varepsilon$ | $-4\varepsilon$ | $0$ |

The point is that the annihilation is not special to any pair: it holds for every pair of nonzero elements of the line $\mathfrak{m}$. Equivalently, $\operatorname{Ann}(\varepsilon b) = \mathfrak{m}$ for every $b \neq 0$, so every nonzero zero divisor annihilates the entire punctured line.

**Example (worked, mixed pair).** The element $2 + 3\varepsilon$ is not a zero divisor and annihilates nothing nonzero:

$$
(2 + 3\varepsilon)(c + \varepsilon d) = 2c + (2d + 3c)\varepsilon,
$$

which vanishes only when $c = 0$ and $2d + 3c = 0$, that is $c = d = 0$.

## The Norm Criterion Worked

### Units

**Example (worked).** $Z = 2 + 3\varepsilon$ has real part $2 \neq 0$, so it is a unit, and $N(Z) = 4 \neq 0$. Its inverse is

$$
Z^{-1} = \frac{1}{2} - \frac{3}{4}\,\varepsilon,
$$

and the check is

$$
(2 + 3\varepsilon)\Bigl(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon\Bigr) = 1 + \Bigl(-\tfrac{3}{2} + \tfrac{3}{2}\Bigr)\varepsilon = 1.
$$

### Non-Units

**Example (worked).** $Z = 0 + 3\varepsilon$ has real part $0$, so it is not a unit, and $N(Z) = 0$. Any attempted inverse fails: if $(3\varepsilon)(c + \varepsilon d) = 3c\,\varepsilon = 1$, then $3c = 1$ and $0 = 1$, a contradiction.

**Example (worked).** $Z = -4 + \varepsilon$ has real part $-4 \neq 0$, so it is a unit, since the criterion is $a \neq 0$ and not $a > 0$:

$$
(-4 + \varepsilon)^{-1} = -\frac{1}{4} - \frac{1}{16}\varepsilon.
$$

### The Inverse Worked, in General

**Example (worked).** For $Z = a + \varepsilon b$ with $a \neq 0$, the inverse formula gives

$$
Z^{-1} = \frac{1}{a} - \frac{b}{a^2}\,\varepsilon,
$$

and the general check is

$$
(a + \varepsilon b)\Bigl(\frac{1}{a} - \frac{b}{a^2}\varepsilon\Bigr) = 1 + \Bigl(-\frac{b}{a} + \frac{b}{a}\Bigr)\varepsilon = 1.
$$

## Worked Exponential and Logarithmic Forms

### The Exponential

By *Dual-Numbers Exponential and Lie Group Structure*, the exponential of a dual number is

$$
\exp(a + \varepsilon b) = e^{a}\bigl(1 + \varepsilon b\bigr) = e^{a} + e^{a}\varepsilon b.
$$

**Example (worked).** $\exp(2 + 3\varepsilon) = e^{2}(1 + 3\varepsilon)$. Numerically, $e^2 = 7.389056\ldots$, so the real part is $7.389056\ldots$ and the infinitesimal part is $3e^2 = 22.167168\ldots$.

**Example (worked).** $\exp(\varepsilon) = 1 + \varepsilon$, $\exp(s\varepsilon) = 1 + s\varepsilon$ for every $s \in \mathbb{R}$; the exponential of a purely infinitesimal element is a shear.

### The Logarithm

The dual logarithm inverts the exponential on the shear group $1 + \mathfrak{m}$:

$$
\log(1 + s\varepsilon) = s\varepsilon, \qquad \exp(\log(1 + s\varepsilon)) = 1 + s\varepsilon.
$$

**Example (worked).** $\log(1 + 5\varepsilon) = 5\varepsilon$ and $\log(1 - \varepsilon) = -\varepsilon$.

## Relation Between the Decompositions

The two decompositions of the dual-number algebra coincide, and the worked examples make the coincidence explicit.

- The **conjugate decomposition** is $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$, from the eigenspaces of $\bar{\cdot}$; worked for $Z = 2 + 3\varepsilon$ as $Z = 2 + 3\varepsilon$.
- The **real–infinitesimal decomposition** is the same identity written as $Z = \operatorname{Re}(Z) + \operatorname{Inf}(Z)\varepsilon$.
- The **norm form** reads $N(Z) = (\operatorname{Re} Z)^2$ on the first summand and $N(Z) = 0$ on the second.

There is no third decomposition, and no nontrivial Peirce decomposition: the only idempotents are $0$ and $1$, so the corners of *Dual-Numbers Ideals and the Maximal Ideal* are trivial. The single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$ is the only intersection of the two submodules, and the worked example $2 + 3\varepsilon = 2 + 3\varepsilon$ is its arithmetic content.

## Summary

The worked computations in the dual-number algebra are these. The two involutions are the identity and dual conjugation; the identity has fixed set all of $\mathbb{D}'$, dual conjugation has $+1$-eigenspace $R_{\mathbb{D}'} = \mathbb{R}$ and $-1$-eigenspace $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$, meeting only in $0$. Every element of the maximal ideal is nilpotent of index two, $(\varepsilon b)^2 = 0$, while a mixed element has $(a + \varepsilon b)^n = a^n + na^{n-1}\varepsilon b$ and is never nilpotent unless $a = 0$. The zero divisors are the nonzero elements $\varepsilon b$ of $\mathfrak{m}$, and any two of them multiply to zero; for instance $(2\varepsilon)(5\varepsilon) = 0$. The criterion for a unit is $a \neq 0$, and the inverse is $a^{-1} - a^{-2}\varepsilon b$; the check $(2 + 3\varepsilon)(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon) = 1$ is the worked instance. The exponential is $\exp(a + \varepsilon b) = e^a(1 + \varepsilon b)$ and the dual logarithm is $\log(1 + s\varepsilon) = s\varepsilon$. The two decompositions of the algebra coincide, and no nontrivial Peirce decomposition exists.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation, the nontrivial involution |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $N(Z) = Z\bar{Z} = a^2$ | Norm form |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal, $\mathfrak{m}^2 = 0$ |
| $\exp(a + \varepsilon b) = e^a(1 + \varepsilon b)$ | Exponential |
| $\log(1 + s\varepsilon) = s\varepsilon$ | Dual logarithm |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the classical coordinate computations in the dual numbers and their geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for worked computations in the dual, complex and split-complex algebras side by side.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for worked examples in the two-dimensional real algebras.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the computed algebra of nilpotent extensions.
