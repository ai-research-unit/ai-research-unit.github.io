
# __Worked Examples in the Dual-Number Algebra__

## Introduction

This article collects explicit computations in the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, in the spirit of the worked computation that accompanies the algebra of a number system. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the criterion for invertibility, *Dual-Numbers Ideals and the Maximal Ideal* for the ideal structure, *Dual-Numbers Zero Divisors* for the zero-divisor classification. Every computation was recomputed in exact rational arithmetic; where a floating-point value appears it is flagged.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Unless a statement is labelled otherwise, the base is $R = \mathbb{R}$ and the algebra is $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in \mathbb{R},
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, dual conjugation $\bar{Z} = a - \varepsilon b$, unit criterion $a \neq 0$, and maximal ideal $\mathrm{M} = (\varepsilon)$. The two distinguished submodules are $R_{\mathbb{D}'} = \mathbb{R}\cdot 1$ and $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$.

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

### The Conjugate

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$, and

$$
(2 + 3\varepsilon)(2 - 3\varepsilon) = 4 + (-6 + 6)\varepsilon = 4.
$$

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

**Proof.** $\bar{a + \varepsilon b} = a - \varepsilon b$ equals $a + \varepsilon b$ exactly when $b = 0$, and equals $-(a + \varepsilon b)$ exactly when $a = 0$; the two sets are as displayed.

**Example (worked projections).** For $Z = 2 + 3\varepsilon$,

$$
\tfrac{1}{2}(Z + \bar{Z}) = 2, \qquad \tfrac{1}{2}(Z - \bar{Z}) = 3\varepsilon,
$$

and indeed $2 + 3\varepsilon = 2 + 3\varepsilon$.

### The Intersection

**Proposition.** $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$, and $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$.

**Proof.** An element of the intersection satisfies $b = 0$ and $a = 0$, so it is zero. The sum decomposition is the worked projection identity above.

So the algebra has exactly **one** nontrivial involution, and the two submodules are the eigenspaces. The biquaternion algebra, by contrast, carries four conjugations and six eigenspace-type subspaces; here the lattice degenerates to two submodules and the single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = 0$.

## The Nilpotents and the Maximal Ideal

### Squaring the Maximal Ideal

**Example (worked).** Every element of $\mathrm{M} = \varepsilon\mathbb{R}$ is nilpotent of index two:

$$
(3\varepsilon)^2 = 9\varepsilon^2 = 0, \qquad (-5\varepsilon)^2 = 25\varepsilon^2 = 0, \qquad (7\varepsilon)^2 = 0.
$$

So $\mathrm{M}^2 = 0$ and $\mathrm{M} \neq 0$: the maximal ideal is nilpotent of index exactly two.

**Example (worked).** A mixed element is never nilpotent: $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon \neq 0$, and more generally $(a + \varepsilon b)^n = a^n + na^{n-1}\varepsilon b$, which vanishes only when $a = 0$.

### The Powers of an Element

**Proposition.** For every integer $n \geq 1$, $(a + \varepsilon b)^n = a^n + n\,a^{n-1}\varepsilon b$, interpreted for $n = 1$ as the element itself.

**Proof.** Induction on $n$ using $(a + \varepsilon b)^n(a + \varepsilon b) = a^{n+1} + (n a^{n-1}b\,a + a^n b)\varepsilon = a^{n+1} + (n+1)a^n \varepsilon b$.

**Example (worked).** $(1 + \varepsilon)^{5} = 1 + 5\varepsilon$, and $(2 + \varepsilon)^3 = 8 + 12\varepsilon$.

## Explicit Zero-Divisor Pairs

### The General Pair

By *Dual-Numbers Zero Divisors* the zero divisors are exactly the nonzero elements of $\mathrm{M}$, that is, the elements $\varepsilon b$ with $b \neq 0$, and any two of them multiply to zero:

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

The point is that the annihilation is not special to any pair: it holds for every pair of nonzero elements of the line $\mathrm{M}$. Equivalently, $\operatorname{Ann}(\varepsilon b) = \mathrm{M}$ for every $b \neq 0$, so every nonzero zero divisor annihilates the entire punctured line.

**Example (worked, mixed pair).** The element $2 + 3\varepsilon$ is not a zero divisor and annihilates nothing nonzero:

$$
(2 + 3\varepsilon)(c + \varepsilon d) = 2c + (2d + 3c)\varepsilon,
$$

which vanishes only when $c = 0$ and $2d + 3c = 0$, that is $c = d = 0$.

## Units and Inverses, Worked

### Units

**Example (worked).** $Z = 2 + 3\varepsilon$ has real part $2 \neq 0$, so it is a unit. Its inverse is

$$
Z^{-1} = \frac{1}{2} - \frac{3}{4}\,\varepsilon,
$$

and the check is

$$
(2 + 3\varepsilon)\Bigl(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon\Bigr) = 1 + \Bigl(-\tfrac{3}{2} + \tfrac{3}{2}\Bigr)\varepsilon = 1.
$$

### Non-Units

**Example (worked).** $Z = 0 + 3\varepsilon$ has real part $0$, so it is not a unit. Any attempted inverse fails: if $(3\varepsilon)(c + \varepsilon d) = 3c\,\varepsilon = 1$, then $3c = 1$ and $0 = 1$, a contradiction.

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

## The Matrix Model and the Shear

### The Matrix of a Worked Product

By *Dual-Numbers Matrix Representation* the algebra embeds faithfully in $M_2(\mathbb{R})$ through

$$
\Phi(a + \varepsilon b) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}.
$$

Worked, $\Phi(2 + 3\varepsilon) = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}$ and $\Phi(4 + 5\varepsilon) = \begin{pmatrix} 4 & 5 \\ 0 & 4 \end{pmatrix}$, and

$$
\Phi(2 + 3\varepsilon)\,\Phi(4 + 5\varepsilon) = \begin{pmatrix} 8 & 2\cdot 5 + 3\cdot 4 \\ 0 & 8 \end{pmatrix} = \begin{pmatrix} 8 & 22 \\ 0 & 8 \end{pmatrix} = \Phi(8 + 22\varepsilon),
$$

matching the coordinate product worked above. The matrix is upper triangular with equal diagonal entries, and $\Phi(1 + \varepsilon) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

### Multiplication by a Unit Is a Shear

Let $Z = a + \varepsilon b$ be a unit, so $a \neq 0$, and write $s = b/a$, giving $Z = a(1 + s\varepsilon)$. Acting on $W = c + \varepsilon d$,

$$
Z W = a(1 + s\varepsilon)(c + \varepsilon d) = a c + (a d + a s c)\varepsilon = a\bigl(c + (d + s c)\varepsilon\bigr).
$$

In the coordinates $(x, y)$ of $W = x + \varepsilon y$ this is the linear map

$$
(x, y) \longmapsto \bigl(a x,\ a(y + s x)\bigr),
$$

a dilation by $a$ followed by the shear $(x, y) \mapsto (x, y + s x)$; the shear alone is multiplication by $1 + s\varepsilon$, which fixes the real axis pointwise.

**Example (worked).** For $Z = 1 + \varepsilon$ and $W = 2 + 5\varepsilon$,

$$
(1 + \varepsilon)(2 + 5\varepsilon) = 2 + (5 + 2)\varepsilon = 2 + 7\varepsilon,
$$

so the point $(2, 5)$ goes to $(2, 7)$, raised by the shear amount $s x = 1 \cdot 2 = 2$.

**Example (worked).** For $Z = 2 + 3\varepsilon$ one has $a = 2$, $s = 3/2$, and for $W = 2 + 5\varepsilon$,

$$
(2 + 3\varepsilon)(2 + 5\varepsilon) = 4 + (10 + 6)\varepsilon = 4 + 16\varepsilon = 2\Bigl(2 + \bigl(5 + \tfrac{3}{2}\cdot 2\bigr)\varepsilon\Bigr),
$$

a dilation by $2$ of the sheared point $(2, 8)$.

## Worked Hyperbolic Elements

### The Two Factors of a Unit

Every unit factors as $Z = a(1 + s\varepsilon)$ with $a \neq 0$ and $s = b/a$: the real factor $a$ is the scale and $1 + s\varepsilon$ the parabolic factor.

**Example (worked).** $2 + 3\varepsilon = 2\bigl(1 + \tfrac{3}{2}\varepsilon\bigr)$ and $-4 + \varepsilon = -4\bigl(1 - \tfrac{1}{4}\varepsilon\bigr)$.

### Powers of a Worked Element

**Example (worked).** For $Z = 2 + 3\varepsilon$,

$$
(2 + 3\varepsilon)^3 = 2^3 + 3\cdot 2^2 \cdot 3\,\varepsilon = 8 + 36\varepsilon,
$$

and in the factorised form $2^3\bigl(1 + \tfrac{3}{2}\varepsilon\bigr)^3 = 8\bigl(1 + 3\cdot\tfrac{3}{2}\varepsilon\bigr) = 8 + 36\varepsilon$, the two computations agreeing.

### The Hyperbolic Case Degenerates

In the split-complex algebra the units $a + jb$ satisfy $a^2 - b^2 = 1$ and form a hyperbola, a one-parameter multiplicative family with a genuine hyperbolic parameter; in the complex algebra the units form a circle. In $\mathbb{D}'$ the corresponding family of units is the pair of parallel lines $a = \pm 1$, and each line is carried by the parabolic family $1 + s\varepsilon$ with the additive parameter $s$. The hyperbola and the circle have both degenerated to lines, the hyperbolic parameter being replaced by the shear parameter; this is the arithmetic content of $\varepsilon^2 = 0$.

## Relation Between the Decompositions

The two decompositions of the dual-number algebra coincide, and the worked examples make the coincidence explicit.

- The **conjugate decomposition** is $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$, from the eigenspaces of $\bar{\cdot}$; worked for $Z = 2 + 3\varepsilon$ as $Z = 2 + 3\varepsilon$.
- The **real–infinitesimal decomposition** is the same identity written as $Z = \operatorname{Re}(Z) + \operatorname{Inf}(Z)\varepsilon$.

There is no third decomposition, and no nontrivial Peirce decomposition: the only idempotents are $0$ and $1$, so the corners of *Dual-Numbers Ideals and the Maximal Ideal* are trivial. The single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$ is the only intersection of the two submodules, and the worked example $2 + 3\varepsilon = 2 + 3\varepsilon$ is its arithmetic content.

## Summary

The worked computations in the dual-number algebra are these. The two involutions are the identity and dual conjugation; the identity has fixed set all of $\mathbb{D}'$, while dual conjugation has $+1$-eigenspace $R_{\mathbb{D}'} = \mathbb{R}$ and $-1$-eigenspace $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$, meeting only in $0$. Every element of the maximal ideal is nilpotent of index two, $(\varepsilon b)^2 = 0$, while a mixed element has $(a + \varepsilon b)^n = a^n + n a^{n-1}\varepsilon b$ and is never nilpotent unless $a = 0$. The zero divisors are the nonzero elements $\varepsilon b$ of $\mathrm{M}$, and any two of them multiply to zero; for instance $(2\varepsilon)(5\varepsilon) = 0$. The criterion for a unit is $a \neq 0$, and the inverse is $a^{-1} - a^{-2}\varepsilon b$; the check $(2 + 3\varepsilon)(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon) = 1$ is the worked instance. Under the matrix model $\Phi(a + \varepsilon b) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$ the worked product $\Phi(2 + 3\varepsilon)\Phi(4 + 5\varepsilon) = \Phi(8 + 22\varepsilon)$ reproduces the coordinate product, and multiplication by the unit $a(1 + s\varepsilon)$ acts as the dilation by $a$ followed by the shear $(x, y) \mapsto (x, y + sx)$. The two decompositions of the algebra coincide, and no nontrivial Peirce decomposition exists.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation, the nontrivial involution |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, $\mathrm{M}^2 = 0$ |
| $\Phi(a + \varepsilon b) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$ | The faithful matrix model |
| $a(1 + s\varepsilon)$ | Factorisation of a unit, $s = b/a$ |
| $(x, y) \mapsto (x, y + sx)$ | The shear of multiplication by $1 + s\varepsilon$ |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the classical coordinate computations in the dual numbers and their geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for worked computations in the dual, complex and split-complex algebras side by side.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for worked examples in the two-dimensional real algebras.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the computed algebra of nilpotent extensions.
