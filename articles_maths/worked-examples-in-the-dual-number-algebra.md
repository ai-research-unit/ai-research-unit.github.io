
# __Worked Examples in the Dual-Number Algebra__

## Introduction

This article collects explicit computations in the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, in the spirit of the worked computation that accompanies the algebra of a number system. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the criterion for invertibility, *Dual-Numbers Ideals and the Maximal Ideal* for the ideal structure, *Dual-Numbers Zero Divisors* for the zero-divisor classification. Every computation was recomputed in exact rational arithmetic; where a floating-point value appears it is flagged.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Unless a statement is labelled otherwise, the base is $R = \mathbb{R}$ and the algebra is $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$. A general dual number is

$$
Q = q + \varepsilon q', \qquad q, q' \in \mathbb{R},
$$

with $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$, dual conjugation $\bar Q = q - \varepsilon q'$, unit criterion $q \neq 0$, and maximal ideal $\mathrm{M} = (\varepsilon)$. The two distinguished submodules are $R_{\mathbb{D}'} = \mathbb{R}\cdot 1$ and $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$.

Each computation below is a worked instance of a general result proved in a companion article; the instance is stated with its reference, so that the article remains a table of examples rather than a second proof of the theory.

## The Algebra in Coordinates

### The Basis and the Product

The algebra has the basis $\{1, \varepsilon\}$ with the multiplication table

| $\cdot$ | $1$ | $\varepsilon$ |
|---|---|---|
| $1$ | $1$ | $\varepsilon$ |
| $\varepsilon$ | $\varepsilon$ | $0$ |

**Example (product, worked).** For $Q_1 = 2 + 3\varepsilon$ and $Q_2 = 4 + 5\varepsilon$,

$$
Q_1 Q_2 = (2\cdot 4) + (2\cdot 5 + 3\cdot 4)\varepsilon = 8 + 22\varepsilon.
$$

The real parts multiply, and the infinitesimal part is $q_1\,q'_2 + q'_1\,q_2$; the cross terms do not interact, because $\varepsilon^2 = 0$.

**Example (squaring, worked).** For $Q = q + \varepsilon q'$, the square is

$$
Q^2 = q^2 + 2qq'\,\varepsilon.
$$

In particular $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon$ and $(\varepsilon)^2 = 0$.

### The Conjugate

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$, and

$$
(2 + 3\varepsilon)(2 - 3\varepsilon) = 4 + (-6 + 6)\varepsilon = 4.
$$

## The Two Involutions

### The Identity Involution

The identity map $\operatorname{id}(Q) = Q$ is an involutive algebra automorphism. Its fixed-point submodule is the whole algebra $\mathbb{D}'$, and the associated $\pm1$-eigenspace decomposition is the trivial one, with eigenvalue $+1$ everywhere.

### The Dual Conjugation

Dual conjugation is

$$
\bar{\cdot} : q + \varepsilon q' \longmapsto q - \varepsilon q'.
$$

**Example (worked).** $\overline{2 + 3\varepsilon} = 2 - 3\varepsilon$; applying it twice returns $2 + 3\varepsilon$, so $\bar{\bar Q} = Q$. It is an algebra automorphism: $\overline{Q_1 Q_2} = \bar Q_1\bar Q_2$, checked on the worked product by $\overline{8 + 22\varepsilon} = 8 - 22\varepsilon$ and $(2 - 3\varepsilon)(4 - 5\varepsilon) = 8 - 22\varepsilon$.

### The Fixed-Point Submodules

**Proposition.** The $+1$-eigenspace of dual conjugation is the real submodule

$$
R_{\mathbb{D}'} = \{Q : \bar Q = Q\} = \{q : q \in \mathbb{R}\},
$$

and the $-1$-eigenspace is the infinitesimal submodule

$$
\varepsilon R_{\mathbb{D}'} = \{Q : \bar Q = -Q\} = \{\varepsilon q' : q' \in \mathbb{R}\}.
$$

**Proof.** $\bar{q + \varepsilon q'} = q - \varepsilon q'$ equals $q + \varepsilon q'$ exactly when $q' = 0$, and equals $-(q + \varepsilon q')$ exactly when $q = 0$; the two sets are as displayed.

**Example (worked projections).** For $Q = 2 + 3\varepsilon$,

$$
\tfrac{1}{2}(Q + \bar Q) = 2, \qquad \tfrac{1}{2}(Q - \bar Q) = 3\varepsilon,
$$

and indeed $2 + 3\varepsilon = Q$.

### The Intersection

**Proposition.** $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$, and $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$.

**Proof.** An element of the intersection satisfies $q' = 0$ and $q = 0$, so it is zero. The sum decomposition is the worked projection identity above.

So the algebra has exactly **one** nontrivial involution, and the two submodules are the eigenspaces; the lattice degenerates to two submodules and the single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = 0$.

## The Nilpotents and the Maximal Ideal

### Squaring the Maximal Ideal

**Example (worked).** Every element of $\mathrm{M} = \varepsilon\mathbb{R}$ is nilpotent of index two:

$$
(3\varepsilon)^2 = 9\varepsilon^2 = 0, \qquad (-5\varepsilon)^2 = 25\varepsilon^2 = 0, \qquad (7\varepsilon)^2 = 0.
$$

So $\mathrm{M}^2 = 0$ and $\mathrm{M} \neq 0$: the maximal ideal is nilpotent of index exactly two.

**Example (worked).** A mixed element is never nilpotent: $(2 + 3\varepsilon)^2 = 4 + 12\varepsilon \neq 0$, and more generally $(q + \varepsilon q')^n = q^n + nq^{n-1}\varepsilon q'$, which vanishes only when $q = 0$.

### The Powers of an Element

**Proposition.** For every integer $n \geq 1$, $(q + \varepsilon q')^n = q^n + n\,q^{n-1}\varepsilon q'$, interpreted for $n = 1$ as the element itself.

**Proof.** Induction on $n$ using $(q + \varepsilon q')^n(q + \varepsilon q') = q^{n+1} + (n q^{n-1}q'\,q + q^n q')\varepsilon = q^{n+1} + (n+1)q^n \varepsilon q'$.

**Example (worked).** $(1 + \varepsilon)^{5} = 1 + 5\varepsilon$, and $(2 + \varepsilon)^3 = 8 + 12\varepsilon$.

## Explicit Zero-Divisor Pairs

### The General Pair

By *Dual-Numbers Zero Divisors* the zero divisors are exactly the nonzero elements of $\mathrm{M}$, that is, the elements $\varepsilon q'_1$ with $q'_1 \neq 0$, and any two of them multiply to zero:

$$
(\varepsilon q'_1)(\varepsilon q'_2) = q'_1 q'_2\,\varepsilon^2 = 0 \qquad \text{for all } q'_1, q'_2.
$$

### A Table

Each row is a pair of nonzero zero divisors whose product is zero; the product is computed in the last column.

| $Q_1$ | $Q_2$ | $Q_1 Q_2$ |
|---|---|---|
| $\varepsilon$ | $\varepsilon$ | $0$ |
| $2\varepsilon$ | $5\varepsilon$ | $0$ |
| $-3\varepsilon$ | $\varepsilon$ | $0$ |
| $7\varepsilon$ | $-4\varepsilon$ | $0$ |

The point is that the annihilation is not special to any pair: it holds for every pair of nonzero elements of the line $\mathrm{M}$. Equivalently, $\operatorname{Ann}(\varepsilon q'_1) = \mathrm{M}$ for every $q'_1 \neq 0$, so every nonzero zero divisor annihilates the entire punctured line.

**Example (worked, mixed pair).** The element $2 + 3\varepsilon$ is not a zero divisor and annihilates nothing nonzero:

$$
(2 + 3\varepsilon)(q + \varepsilon q') = 2 q + (2 q' + 3 q)\varepsilon,
$$

which vanishes only when $q = 0$ and $2q' + 3q = 0$, that is $q = q' = 0$.

## Units and Inverses, Worked

### Units

**Example (worked).** $Q = 2 + 3\varepsilon$ has real part $2 \neq 0$, so it is a unit. Its inverse is

$$
Q^{-1} = \frac{1}{2} - \frac{3}{4}\,\varepsilon,
$$

and the check is

$$
(2 + 3\varepsilon)\Bigl(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon\Bigr) = 1 + \Bigl(-\tfrac{3}{2} + \tfrac{3}{2}\Bigr)\varepsilon = 1.
$$

### Non-Units

**Example (worked).** $Q = 0 + 3\varepsilon$ has real part $0$, so it is not a unit. Any attempted inverse fails: if $(3\varepsilon)(q + \varepsilon q') = 3q\,\varepsilon = 1$, then $3q = 1$ and $0 = 1$, a contradiction.

**Example (worked).** $Q = -4 + \varepsilon$ has real part $-4 \neq 0$, so it is a unit, since the criterion is $q \neq 0$ and not $q > 0$:

$$
(-4 + \varepsilon)^{-1} = -\frac{1}{4} - \frac{1}{16}\varepsilon.
$$

### The Inverse Worked, in General

**Example (worked).** For $Q = q + \varepsilon q'$ with $q \neq 0$, the inverse formula gives

$$
Q^{-1} = \frac{1}{q} - \frac{q'}{q^2}\,\varepsilon,
$$

and the general check is

$$
(q + \varepsilon q')\Bigl(\frac{1}{q} - \frac{q'}{q^2}\varepsilon\Bigr) = 1 + \Bigl(-\frac{q'}{q} + \frac{q'}{q}\Bigr)\varepsilon = 1.
$$

## The Matrix Model and the Shear

### The Matrix of a Worked Product

By *Dual-Numbers Matrix Element Representation* the algebra embeds faithfully in $M_2(\mathbb{R})$ through

$$
\Phi(q + \varepsilon q') = \begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}.
$$

Worked, $\Phi(2 + 3\varepsilon) = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}$ and $\Phi(4 + 5\varepsilon) = \begin{pmatrix} 4 & 5 \\ 0 & 4 \end{pmatrix}$, and

$$
\Phi(2 + 3\varepsilon)\,\Phi(4 + 5\varepsilon) = \begin{pmatrix} 8 & 2\cdot 5 + 3\cdot 4 \\ 0 & 8 \end{pmatrix} = \begin{pmatrix} 8 & 22 \\ 0 & 8 \end{pmatrix} = \Phi(8 + 22\varepsilon),
$$

matching the coordinate product worked above. The matrix is upper triangular with equal diagonal entries, and $\Phi(1 + \varepsilon) = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

### Multiplication by a Unit Is a Shear

Let $Q_1 = q_1 + \varepsilon q'_1$ be a unit, so $q_1 \neq 0$, and write $s = q'_1/q_1$, giving $Q_1 = q_1(1 + s\varepsilon)$. Acting on $Q_2 = q_2 + \varepsilon q'_2$,

$$
Q_1 Q_2 = q_1(1 + s\varepsilon)(q_2 + \varepsilon q'_2) = q_1 q_2 + (q_1 q'_2 + q_1 s q_2)\varepsilon = q_1\bigl(q_2 + (q'_2 + s q_2)\varepsilon\bigr).
$$

In the coordinates $(q_2, q'_2)$ of $Q_2$ this is the linear map

$$
(q_2, q'_2) \longmapsto \bigl(q_1 q_2,\ q_1(q'_2 + s q_2)\bigr),
$$

a dilation by $q_1$ followed by the shear $(q_2, q'_2) \mapsto (q_2, q'_2 + s q_2)$; the shear alone is multiplication by $1 + s\varepsilon$, which fixes the real axis pointwise.

**Example (worked).** For $Q_1 = 1 + \varepsilon$ and $Q_2 = 2 + 5\varepsilon$,

$$
(1 + \varepsilon)(2 + 5\varepsilon) = 2 + (5 + 2)\varepsilon = 2 + 7\varepsilon,
$$

so the point $(2, 5)$ goes to $(2, 7)$, raised by the shear amount $s q_2 = 1 \cdot 2 = 2$.

**Example (worked).** For $Q_1 = 2 + 3\varepsilon$ one has $q_1 = 2$, $s = 3/2$, and for $Q_2 = 2 + 5\varepsilon$,

$$
(2 + 3\varepsilon)(2 + 5\varepsilon) = 4 + (10 + 6)\varepsilon = 4 + 16\varepsilon = 2\Bigl(2 + \bigl(5 + \tfrac{3}{2}\cdot 2\bigr)\varepsilon\Bigr),
$$

a dilation by $2$ of the sheared point $(2, 8)$.

## Worked Hyperbolic Elements

### The Two Factors of a Unit

Every unit factors as $Q = q(1 + s\varepsilon)$ with $q \neq 0$ and $s = q'/q$: the real factor $q$ is the scale and $1 + s\varepsilon$ the parabolic factor.

**Example (worked).** $2 + 3\varepsilon = 2\bigl(1 + \tfrac{3}{2}\varepsilon\bigr)$ and $-4 + \varepsilon = -4\bigl(1 - \tfrac{1}{4}\varepsilon\bigr)$.

### Powers of a Worked Element

**Example (worked).** For $Q = 2 + 3\varepsilon$,

$$
(2 + 3\varepsilon)^3 = 2^3 + 3\cdot 2^2 \cdot 3\,\varepsilon = 8 + 36\varepsilon,
$$

and in the factorised form $2^3\bigl(1 + \tfrac{3}{2}\varepsilon\bigr)^3 = 8\bigl(1 + 3\cdot\tfrac{3}{2}\varepsilon\bigr) = 8 + 36\varepsilon$, the two computations agreeing.

### The Hyperbolic Case Degenerates

In the split-complex algebra the units $a + jb$ satisfy $a^2 - b^2 = 1$ and form a hyperbola, a one-parameter multiplicative family with a genuine hyperbolic parameter; in the complex algebra the units form a circle. In $\mathbb{D}'$ the corresponding family of units is the pair of parallel lines $q = \pm 1$, and each line is carried by the parabolic family $1 + s\varepsilon$ with the additive parameter $s$. The hyperbola and the circle have both degenerated to lines, the hyperbolic parameter being replaced by the shear parameter; this is the arithmetic content of $\varepsilon^2 = 0$.

## Relation Between the Decompositions

The two decompositions of the dual-number algebra coincide, and the worked examples make the coincidence explicit.

- The **conjugate decomposition** is $\mathbb{D}' = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}$, from the eigenspaces of $\bar{\cdot}$; worked for $Q = 2 + 3\varepsilon$ as $Q = 2 + 3\varepsilon$.
- The **real–infinitesimal decomposition** is the same identity written as $Q = \operatorname{Re}(Q) + \operatorname{Inf}(Q)\varepsilon$.

There is no third decomposition, and no nontrivial Peirce decomposition: the only idempotents are $0$ and $1$, so the corners of *Dual-Numbers Ideals and the Maximal Ideal* are trivial. The single relation $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$ is the only intersection of the two submodules, and the worked example $2 + 3\varepsilon = Q$ is its arithmetic content.

## Summary

The worked computations in the dual-number algebra are these. The two involutions are the identity and dual conjugation; the identity has fixed set all of $\mathbb{D}'$, while dual conjugation has $+1$-eigenspace $R_{\mathbb{D}'} = \mathbb{R}$ and $-1$-eigenspace $\varepsilon R_{\mathbb{D}'} = \varepsilon\mathbb{R}$, meeting only in $0$. Every element of the maximal ideal is nilpotent of index two, $(\varepsilon q')^2 = 0$, while a mixed element has $(q + \varepsilon q')^n = q^n + n q^{n-1}\varepsilon q'$ and is never nilpotent unless $q = 0$. The zero divisors are the nonzero elements $\varepsilon q'$ of $\mathrm{M}$, and any two of them multiply to zero; for instance $(2\varepsilon)(5\varepsilon) = 0$. The criterion for a unit is $q \neq 0$, and the inverse is $q^{-1} - q^{-2}\varepsilon q'$; the check $(2 + 3\varepsilon)(\tfrac{1}{2} - \tfrac{3}{4}\varepsilon) = 1$ is the worked instance. Under the matrix model $\Phi(q + \varepsilon q') = \begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}$ the worked product $\Phi(2 + 3\varepsilon)\Phi(4 + 5\varepsilon) = \Phi(8 + 22\varepsilon)$ reproduces the coordinate product, and multiplication by the unit $q(1 + s\varepsilon)$ acts as the dilation by $q$ followed by the shear $(q, q') \mapsto (q, q' + s q)$. The two decompositions of the algebra coincide, and no nontrivial Peirce decomposition exists.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $Q = q + \varepsilon q'$ | General dual number |
| $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$ | Real and infinitesimal parts |
| $\bar{Q} = q - \varepsilon q'$ | Dual conjugation, the nontrivial involution |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, $\mathrm{M}^2 = 0$ |
| $\Phi(q + \varepsilon q') = \begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}$ | The faithful matrix model |
| $q(1 + s\varepsilon)$ | Factorisation of a unit, $s = q'/q$ |
| $(q, q') \mapsto (q, q' + s q)$ | The shear of multiplication by $1 + s\varepsilon$ |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the classical coordinate computations in the dual numbers and their geometry.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for worked computations in the dual, complex and split-complex algebras side by side.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the computed algebra of nilpotent extensions.
