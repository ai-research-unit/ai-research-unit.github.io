
# __Worked Examples in the Dual-Number Algebra__

## Introduction

This article collects explicit computations in the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, in the spirit of the worked computation that accompanies the algebra of a number system. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the criterion for invertibility, *Dual-Numbers Ideals and the Maximal Ideal* for the ideal structure, *Dual-Numbers Zero Divisors* for the zero-divisor classification. Every computation was recomputed in exact rational arithmetic; where a floating-point value appears it is flagged.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Unless a statement is labelled otherwise, the base is $R = \mathbb{R}$ and the algebra is $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$. A general dual number is

$$
A = a + \varepsilon a', \qquad a, a' \in \mathbb{R},
$$

with $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$, dual conjugation $\bar A = a - \varepsilon a'$, unit criterion $a \neq 0$, and maximal ideal $\mathrm{M} = (\varepsilon)$. The two distinguished submodules are $R_{\mathbb{D}'} = \mathbb{R}\cdot 1$ and $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$.

Each computation below is a worked instance of a general result proved in a companion article; the instance is stated with its reference, so that the article remains a table of examples rather than a second proof of the theory.

## The Algebra in Coordinates

### The Basis and the Product

The algebra has the basis $\{1, \varepsilon\}$ with the multiplication table

| $\cdot$ | $1$ | $\varepsilon$ |
|---|---|---|
| $1$ | $1$ | $\varepsilon$ |
| $\varepsilon$ | $\varepsilon$ | $0$ |

**Example (product, worked).** For $A = 2 + 3\varepsilon$ and $B = 4 + 5\varepsilon$,

$$
AB = (2\cdot 4) + (2\cdot 5 + 3\cdot 4)\varepsilon = 8 + 22\varepsilon.
$$

The real parts multiply, and the infinitesimal part is $a\,b' + a'\,b$; the cross terms do not interact, because $\varepsilon^2 = 0$.

**Example (squaring, worked).** For $A = a + \varepsilon a'$, the square is

$$
A^2 = a^2 + 2aa'\,\varepsilon.
$$

In particular $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon$ and $(\varepsilon)^2 = 0$.

### The Conjugate

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$, and

$$
(2 + 3\varepsilon)(2 - 3\varepsilon) = 4 + (-6 + 6)\varepsilon = 4.
$$

## The Two Involutions

### The Identity Involution

The identity map $\operatorname{id}(A) = A$ is an involutive algebra automorphism. Its fixed-point submodule is the whole algebra $\mathbb{D}'$, and the associated $\pm1$-eigenspace decomposition is the trivial one, with eigenvalue $+1$ everywhere.

### The Dual Conjugation

Dual conjugation is

$$
\bar{\cdot} : a + \varepsilon a' \longmapsto a - \varepsilon a'.
$$

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$; applying it twice returns $2 + 3\varepsilon$, so $\bar{\bar A} = A$. It is an algebra automorphism: $\overline{AB} = \bar A\bar B$, checked on the worked product by $\overline{8 + 22\varepsilon} = 8 - 22\varepsilon$ and $(2 - 3\varepsilon)(4 - 5\varepsilon) = 8 - 22\varepsilon$.

### The Fixed-Point Submodules

**Proposition.** The $+1$-eigenspace of dual conjugation is the real submodule

$$
R_{\mathbb{D}'} = \{A : \bar A = A\} = \{a : a \in \mathbb{R}\},
$$

and the $-1$-eigenspace is the infinitesimal submodule

$$
\varepsilon R_{\mathbb{D}'} = \{A : \bar A = -A\} = \{\varepsilon a' : a' \in \mathbb{R}\}.
$$

**Proof.** $\bar{a + \varepsilon a'} = a - \varepsilon a'$ equals $a + \varepsilon a'$ exactly when $a' = 0$, and equals $-(a + \varepsilon a')$ exactly when $a = 0$; the two sets are as displayed.

**Example (worked projections).** For $A = 2 + 3\varepsilon$,

$$
\tfrac{1}{2}(A + \bar A) = 2, \qquad \tfrac{1}{2}(A - \bar A) = 3\varepsilon,
$$

and indeed $2 + 3\varepsilon = A$.

### The Intersection

**Proposition.** $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$, and $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$.

**Proof.** An element of the intersection satisfies $a' = 0$ and $a = 0$, so it is zero. The sum decomposition is the worked projection identity above.

So the algebra has exactly **one** nontrivial involution, and the two submodules are the eigenspaces. The biquaternion algebra, by contrast, carries four conjugations and six eigenspace-type subspaces; here the lattice degenerates to two submodules and the single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = 0$.

## The Nilpotents and the Maximal Ideal

### Squaring the Maximal Ideal

**Example (worked).** Every element of $\mathrm{M} = \varepsilon\mathbb{R}$ is nilpotent of index two:

$$
(3\varepsilon)^2 = 9\varepsilon^2 = 0, \qquad (-5\varepsilon)^2 = 25\varepsilon^2 = 0, \qquad (7\varepsilon)^2 = 0.
$$

So $\mathrm{M}^2 = 0$ and $\mathrm{M} \neq 0$: the maximal ideal is nilpotent of index exactly two.

**Example (worked).** A mixed element is never nilpotent: $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon \neq 0$, and more generally $(a + \varepsilon a')^n = a^n + na^{n-1}\varepsilon a'$, which vanishes only when $a = 0$.

### The Powers of an Element

**Proposition.** For every integer $n \geq 1$, $(a + \varepsilon a')^n = a^n + n\,a^{n-1}\varepsilon a'$, interpreted for $n = 1$ as the element itself.

**Proof.** Induction on $n$ using $(a + \varepsilon a')^n(a + \varepsilon a') = a^{n+1} + (n a^{n-1}a'\,a + a^n a')\varepsilon = a^{n+1} + (n+1)a^n \varepsilon a'$.

**Example (worked).** $(1 + \varepsilon)^{5} = 1 + 5\varepsilon$, and $(2 + \varepsilon)^3 = 8 + 12\varepsilon$.

## Explicit Zero-Divisor Pairs

### The General Pair

By *Dual-Numbers Zero Divisors* the zero divisors are exactly the nonzero elements of $\mathrm{M}$, that is, the elements $\varepsilon a'$ with $a' \neq 0$, and any two of them multiply to zero:

$$
(\varepsilon a')(\varepsilon b') = a' b'\,\varepsilon^2 = 0 \qquad \text{for all } a', b'.
$$

### A Table

Each row is a pair of nonzero zero divisors whose product is zero; the product is computed in the last column.

| $A$ | $B$ | $AB$ |
|---|---|---|
| $\varepsilon$ | $\varepsilon$ | $0$ |
| $2\varepsilon$ | $5\varepsilon$ | $0$ |
| $-3\varepsilon$ | $\varepsilon$ | $0$ |
| $7\varepsilon$ | $-4\varepsilon$ | $0$ |

The point is that the annihilation is not special to any pair: it holds for every pair of nonzero elements of the line $\mathrm{M}$. Equivalently, $\operatorname{Ann}(\varepsilon a') = \mathrm{M}$ for every $a' \neq 0$, so every nonzero zero divisor annihilates the entire punctured line.

**Example (worked, mixed pair).** The element $2 + 3\varepsilon$ is not a zero divisor and annihilates nothing nonzero:

$$
(2 + 3\varepsilon)(b + \varepsilon b') = 2 b + (2 b' + 3 b)\varepsilon,
$$

which vanishes only when $b = 0$ and $2b' + 3b = 0$, that is $b = b' = 0$.

## Units and Inverses, Worked

### Units

**Example (worked).** $A = 2 + 3\varepsilon$ has real part $2 \neq 0$, so it is a unit. Its inverse is

$$
A^{-1} = \frac{1}{2} - \frac{3}{4}\,\varepsilon,
$$

and the check is

$$
(2 + 3\varepsilon)\Bigl(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon\Bigr) = 1 + \Bigl(-\tfrac{3}{2} + \tfrac{3}{2}\Bigr)\varepsilon = 1.
$$

### Non-Units

**Example (worked).** $A = 0 + 3\varepsilon$ has real part $0$, so it is not a unit. Any attempted inverse fails: if $(3\varepsilon)(b + \varepsilon b') = 3b\,\varepsilon = 1$, then $3b = 1$ and $0 = 1$, a contradiction.

**Example (worked).** $A = -4 + \varepsilon$ has real part $-4 \neq 0$, so it is a unit, since the criterion is $a \neq 0$ and not $a > 0$:

$$
(-4 + \varepsilon)^{-1} = -\frac{1}{4} - \frac{1}{16}\varepsilon.
$$

### The Inverse Worked, in General

**Example (worked).** For $A = a + \varepsilon a'$ with $a \neq 0$, the inverse formula gives

$$
A^{-1} = \frac{1}{a} - \frac{a'}{a^2}\,\varepsilon,
$$

and the general check is

$$
(a + \varepsilon a')\Bigl(\frac{1}{a} - \frac{a'}{a^2}\varepsilon\Bigr) = 1 + \Bigl(-\frac{a'}{a} + \frac{a'}{a}\Bigr)\varepsilon = 1.
$$

## The Matrix Model and the Shear

### The Matrix of a Worked Product

By *Dual-Numbers Matrix Element Representation* the algebra embeds faithfully in $M_2(\mathbb{R})$ through

$$
\Phi(a + \varepsilon a') = \begin{pmatrix} a & a' \\ 0 & a \end{pmatrix}.
$$

Worked, $\Phi(2 + 3\varepsilon) = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}$ and $\Phi(4 + 5\varepsilon) = \begin{pmatrix} 4 & 5 \\ 0 & 4 \end{pmatrix}$, and

$$
\Phi(2 + 3\varepsilon)\,\Phi(4 + 5\varepsilon) = \begin{pmatrix} 8 & 2\cdot 5 + 3\cdot 4 \\ 0 & 8 \end{pmatrix} = \begin{pmatrix} 8 & 22 \\ 0 & 8 \end{pmatrix} = \Phi(8 + 22\varepsilon),
$$

matching the coordinate product worked above. The matrix is upper triangular with equal diagonal entries, and $\Phi(1 + \varepsilon) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

### Multiplication by a Unit Is a Shear

Let $A = a + \varepsilon a'$ be a unit, so $a \neq 0$, and write $s = a'/a$, giving $A = a(1 + s\varepsilon)$. Acting on $B = b + \varepsilon b'$,

$$
A B = a(1 + s\varepsilon)(b + \varepsilon b') = a b + (a b' + a s b)\varepsilon = a\bigl(b + (b' + s b)\varepsilon\bigr).
$$

In the coordinates $(b, b')$ of $B$ this is the linear map

$$
(b, b') \longmapsto \bigl(a b,\ a(b' + s b)\bigr),
$$

a dilation by $a$ followed by the shear $(b, b') \mapsto (b, b' + s b)$; the shear alone is multiplication by $1 + s\varepsilon$, which fixes the real axis pointwise.

**Example (worked).** For $A = 1 + \varepsilon$ and $B = 2 + 5\varepsilon$,

$$
(1 + \varepsilon)(2 + 5\varepsilon) = 2 + (5 + 2)\varepsilon = 2 + 7\varepsilon,
$$

so the point $(2, 5)$ goes to $(2, 7)$, raised by the shear amount $s b = 1 \cdot 2 = 2$.

**Example (worked).** For $A = 2 + 3\varepsilon$ one has $a = 2$, $s = 3/2$, and for $B = 2 + 5\varepsilon$,

$$
(2 + 3\varepsilon)(2 + 5\varepsilon) = 4 + (10 + 6)\varepsilon = 4 + 16\varepsilon = 2\Bigl(2 + \bigl(5 + \tfrac{3}{2}\cdot 2\bigr)\varepsilon\Bigr),
$$

a dilation by $2$ of the sheared point $(2, 8)$.

## Worked Hyperbolic Elements

### The Two Factors of a Unit

Every unit factors as $A = a(1 + s\varepsilon)$ with $a \neq 0$ and $s = a'/a$: the real factor $a$ is the scale and $1 + s\varepsilon$ the parabolic factor.

**Example (worked).** $2 + 3\varepsilon = 2\bigl(1 + \tfrac{3}{2}\varepsilon\bigr)$ and $-4 + \varepsilon = -4\bigl(1 - \tfrac{1}{4}\varepsilon\bigr)$.

### Powers of a Worked Element

**Example (worked).** For $A = 2 + 3\varepsilon$,

$$
(2 + 3\varepsilon)^3 = 2^3 + 3\cdot 2^2 \cdot 3\,\varepsilon = 8 + 36\varepsilon,
$$

and in the factorised form $2^3\bigl(1 + \tfrac{3}{2}\varepsilon\bigr)^3 = 8\bigl(1 + 3\cdot\tfrac{3}{2}\varepsilon\bigr) = 8 + 36\varepsilon$, the two computations agreeing.

### The Hyperbolic Case Degenerates

In the split-complex algebra the units $a + jb$ satisfy $a^2 - b^2 = 1$ and form a hyperbola, a one-parameter multiplicative family with a genuine hyperbolic parameter; in the complex algebra the units form a circle. In $\mathbb{D}'$ the corresponding family of units is the pair of parallel lines $a = \pm 1$, and each line is carried by the parabolic family $1 + s\varepsilon$ with the additive parameter $s$. The hyperbola and the circle have both degenerated to lines, the hyperbolic parameter being replaced by the shear parameter; this is the arithmetic content of $\varepsilon^2 = 0$.

## Relation Between the Decompositions

The two decompositions of the dual-number algebra coincide, and the worked examples make the coincidence explicit.

- The **conjugate decomposition** is $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$, from the eigenspaces of $\bar{\cdot}$; worked for $A = 2 + 3\varepsilon$ as $A = 2 + 3\varepsilon$.
- The **real–infinitesimal decomposition** is the same identity written as $A = \operatorname{Re}(A) + \operatorname{Inf}(A)\varepsilon$.

There is no third decomposition, and no nontrivial Peirce decomposition: the only idempotents are $0$ and $1$, so the corners of *Dual-Numbers Ideals and the Maximal Ideal* are trivial. The single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$ is the only intersection of the two submodules, and the worked example $2 + 3\varepsilon = A$ is its arithmetic content.

## Summary

The worked computations in the dual-number algebra are these. The two involutions are the identity and dual conjugation; the identity has fixed set all of $\mathbb{D}'$, while dual conjugation has $+1$-eigenspace $R_{\mathbb{D}'} = \mathbb{R}$ and $-1$-eigenspace $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$, meeting only in $0$. Every element of the maximal ideal is nilpotent of index two, $(\varepsilon a')^2 = 0$, while a mixed element has $(a + \varepsilon a')^n = a^n + n a^{n-1}\varepsilon a'$ and is never nilpotent unless $a = 0$. The zero divisors are the nonzero elements $\varepsilon a'$ of $\mathrm{M}$, and any two of them multiply to zero; for instance $(2\varepsilon)(5\varepsilon) = 0$. The criterion for a unit is $a \neq 0$, and the inverse is $a^{-1} - a^{-2}\varepsilon a'$; the check $(2 + 3\varepsilon)(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon) = 1$ is the worked instance. Under the matrix model $\Phi(a + \varepsilon a') = \begin{pmatrix} a & a' \\ 0 & a \end{pmatrix}$ the worked product $\Phi(2 + 3\varepsilon)\Phi(4 + 5\varepsilon) = \Phi(8 + 22\varepsilon)$ reproduces the coordinate product, and multiplication by the unit $a(1 + s\varepsilon)$ acts as the dilation by $a$ followed by the shear $(b, b') \mapsto (b, b' + s b)$. The two decompositions of the algebra coincide, and no nontrivial Peirce decomposition exists.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $A = a + \varepsilon a'$ | General dual number |
| $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$ | Real and infinitesimal parts |
| $\bar{A} = a - \varepsilon a'$ | Dual conjugation, the nontrivial involution |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, $\mathrm{M}^2 = 0$ |
| $\Phi(a + \varepsilon a') = \begin{pmatrix} a & a' \\ 0 & a \end{pmatrix}$ | The faithful matrix model |
| $a(1 + s\varepsilon)$ | Factorisation of a unit, $s = a'/a$ |
| $(b, b') \mapsto (b, b' + s b)$ | The shear of multiplication by $1 + s\varepsilon$ |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the classical coordinate computations in the dual numbers and their geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for worked computations in the dual, complex and split-complex algebras side by side.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for worked examples in the two-dimensional real algebras.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the computed algebra of nilpotent extensions.
