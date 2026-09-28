
# __Worked Examples in the Split-Complex Algebra__

## Introduction

This article works the structural facts of the split-complex algebra in explicit numbers. It is the computational companion of *Split-Complex Algebra* and its counterpart is *Biquaternion Algebra*: the general theory is established in the earlier articles, and here it is exercised on named elements, so that a reader can see the involutions, the idempotents, the minimal ideals, the zero divisors and the hyperbolic and parabolic elements in full. The norm, the unit criterion and the polar decomposition are a form and a distance and belong to *Split-Complex Norm and Invertibility* and to *Split-Complex Polar Representation*; the examples below use only the algebra.

Every computation below uses the conventions of the category: $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$; general element $Z = a+j b$ with $a = \operatorname{Re}Z$, $b = \operatorname{Im}Z$; conjugate $\bar Z = a-j b$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $Z_\pm = a\pm b$. Every number below was recomputed in double precision, and the general identities behind the examples are in the earlier articles.

## The Two Involutions and Their Fixed Spaces

The algebra carries two natural involutions: the split-complex conjugation $\bar{Z}$, and the idempotent conjugation (the swap) $\tilde{Z} = (a-b)\Pi_1 + (a+b)\Pi_2$. The first computation is that on $\mathbb{D}$ they coincide.

**Example.** Take $Z = 3+2j$. Then

$$
\bar Z = 3 - 2j,
$$

while

$$
\tilde Z = (3-2)\Pi_1 + (3+2)\Pi_2 = 1\cdot\tfrac{1+j}{2} + 5\cdot\tfrac{1-j}{2} = \tfrac{1+5}{2} + \tfrac{1-5}{2}j = 3 - 2j.
$$

So $\tilde Z = \bar Z$ for this element; since the identity is polynomial in $Z$, it holds for every $Z$. The two involutions are one and the same map.

**The fixed spaces.** An element is fixed by $\bar{\cdot}$ iff $a-j b = a+j b$, i.e. $b=0$; the fixed space is

$$
\mathbb{R}_{\mathbb{D}} = \{a : a \in \mathbb{R}\},
$$

the real line. An element is anti-fixed iff $a=0$; the anti-fixed space is

$$
j\mathbb{R}_{\mathbb{D}} = \{j b : b \in \mathbb{R}\},
$$

the split imaginary line. For $Z = 3+2j$ the projections are $Z_r = \tfrac12(Z+\bar Z) = 3$ and $j Z_i = \tfrac12(Z-\bar Z) = 2j$, so $Z = 3 + 2j$ recovers the coordinates.

## The Idempotents and the Two Minimal Ideals

The idempotents are $\Pi_1 = \tfrac12(1+j)$ and $\Pi_2 = \tfrac12(1-j)$, with

$$
\Pi_1^2 = \Pi_1, \qquad \Pi_2^2 = \Pi_2, \qquad \Pi_1\Pi_2 = 0, \qquad \Pi_1 + \Pi_2 = 1.
$$

**Example.** Decompose $Z = 3+2j$ in the idempotent basis:

$$
Z_+ = a+b = 5, \qquad Z_- = a-b = 1, \qquad Z = 5\Pi_1 + 1\Pi_2
= 5\cdot\tfrac{1+j}{2} + 1\cdot\tfrac{1-j}{2} = 3 + 2j. \checkmark
$$

The two components $Z_\pm = Z\Pi_\pm$ are

$$
Z\Pi_1 = 5\Pi_1 = \tfrac{5}{2}(1+j), \qquad Z\Pi_2 = 1\Pi_2 = \tfrac{1}{2}(1-j).
$$

The **minimal ideals** are the lines

$$
\mathbb{R}\Pi_1 = \{(t,t) : t \in \mathbb{R}\}, \qquad \mathbb{R}\Pi_2 = \{(t,-t) : t \in \mathbb{R}\},
$$

in the coordinates $(a,b)$; their product is zero, and $\mathbb{D} = \mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$. The isomorphism with $\mathbb{R}\oplus\mathbb{R}$ is realised numerically by $\varphi(3+2j) = (5, 1)$; the multiplication is componentwise, $\varphi(ZW) = (Z_+W_+, Z_-W_-)$.

## Explicit Zero-Divisor Pairs

The zero divisors are the nonzero points of the two null lines; any two elements supported on opposite idempotents annihilate.

**Example (a pair).** Take

$$
a = 1+j, \qquad b = 2-2j.
$$

Then

$$
a b = (1+j)(2-2j) = 2(1+j)(1-j) = 2(1-j^2) = 0,
$$

with $a \neq 0$ and $b \neq 0$. So $a$ and $b$ are zero divisors; each is a non-zero multiple of an idempotent.

In the idempotent basis the mechanism is transparent: $a = 1+j = 2\Pi_1$, $b = 2-2j = 4\Pi_2$, and $\Pi_1\Pi_2 = 0$.

**Example (a general pair).** For any $\lambda, \mu \neq 0$,

$$
(\lambda \Pi_1)(\mu \Pi_2) = \lambda\mu\, \Pi_1\Pi_2 = 0,
$$

so the whole family of examples is $\{\lambda \Pi_1\}\times\{\mu \Pi_2\}$; and the annihilator of $\lambda \Pi_1$ is the line $\mathbb{R}\Pi_2$, as established in *Split-Complex Zero Divisors*. There is no pair of zero divisors with $a b = 0$ in which one factor is a unit; the criterion is that each factor lies on one of the two null lines.

## Worked Hyperbolic and Parabolic Elements

An element of $\mathbb{D}$ is classified by the signs of its two idempotent coordinates: a **hyperbolic** element is a unit with $Z_+Z_- > 0$, the coordinates having the same sign; an **elliptic** element is a unit with $Z_+Z_- < 0$, the coordinates having opposite signs; a **parabolic** element is a non-zero element with $Z_+Z_- = 0$, that is, a zero divisor. The product $Z_+Z_-$ is the algebraic reading of the quadratic form of *Split-Complex Norm and Invertibility*, and its sign is preserved under multiplication; the names are the hyperbolic, elliptic and parabolic classes of the unit group.

**Hyperbolic example.** Let $Z = \tfrac54 + \tfrac34 j$. Its coordinates are

$$
Z_+ = a+b = 2, \qquad Z_- = a-b = \tfrac12, \qquad Z_+Z_- = 1 > 0,
$$

so $Z$ is a hyperbolic unit, and indeed $Z = 2\Pi_1 + \tfrac12\Pi_2$. Its powers are computed in the idempotent basis, where multiplication is componentwise:

$$
Z^n = 2^n\Pi_1 + 2^{-n}\Pi_2 = \frac{2^n+2^{-n}}{2} + \frac{2^n-2^{-n}}{2}\,j,
$$

so the powers stay in the hyperbolic class and satisfy $Z^m Z^n = Z^{m+n}$. For $n=2$,

$$
Z^2 = \tfrac{17}{8} + \tfrac{15}{8}j,
$$

and indeed $Z Z = (\tfrac54)(\tfrac54) + (\tfrac34)(\tfrac34) + 2\cdot\tfrac54\cdot\tfrac34\,j = \tfrac{34}{16} + \tfrac{30}{16}j$, an ordinary multiplication in the basis $1, j$. $\checkmark$

**Parabolic example.** Let $Z = 1+j = 2\Pi_1$, with coordinates $Z_+ = 2$, $Z_- = 0$, so $Z$ is parabolic (a zero divisor). Then

$$
Z^2 = (1+j)^2 = 1 + 2j + j^2 = 2 + 2j = 2Z, \qquad Z^n = 2^{n-1}Z \quad (n \geq 1),
$$

which is the same computation in the idempotent basis, $Z^n = 2^n\Pi_1 = 2^{n-1}Z$. So the powers of a parabolic element stay on its null line. The element has no inverse, because $Z_- = 0$; the algebraic unit criterion of *Split-Complex Algebra* fails at it. This is the exact algebraic analogue of the parabolic elements of the hyperbolic group, which lie on the null cone.

## Summary

This article worked the algebra in explicit numbers. The two natural involutions of $\mathbb{D}$, the split-complex conjugation and the idempotent swap, were shown to coincide on $Z = 3+2j$ and hence throughout, with fixed space the real line $\mathbb{R}_{\mathbb{D}}$ and anti-fixed space the split imaginary line $j\mathbb{R}_{\mathbb{D}}$. The idempotents $\Pi_\pm$ were exhibited, the decomposition $3+2j = 5\Pi_1 + 1\Pi_2$ computed, and the minimal ideals $\mathbb{R}\Pi_\pm$ identified.

Explicit zero-divisor pairs were given, $a = 1+j = 2\Pi_1$ and $b = 2-2j = 4\Pi_2$ with $a b = 0$, and the general pair $(\lambda \Pi_1)(\mu \Pi_2) = 0$. Finally, the hyperbolic element $Z = \tfrac54 + \tfrac34 j$, of coordinates $(2, \tfrac12)$ and powers $Z^n = 2^n\Pi_1 + 2^{-n}\Pi_2$, was compared with the parabolic element $1+j$, of coordinates $(2,0)$, with $Z^n = 2^{n-1}Z$ and no inverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | General split complex number |
| $\bar Z = a - j b$ | Split-complex conjugation (unique non-trivial involution) |
| $\tilde Z = (a-b)\Pi_1 + (a+b)\Pi_2$ | Idempotent conjugation; equal to $\bar Z$ |
| $\mathbb{R}_{\mathbb{D}}, j\mathbb{R}_{\mathbb{D}}$ | Fixed and anti-fixed spaces of the involution |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents |
| $Z_\pm = a\pm b$ | Idempotent coordinates, $Z = Z_+\Pi_1 + Z_-\Pi_2$ |
| $\mathbb{R}\Pi_1, \mathbb{R}\Pi_2$ | Minimal ideals / null lines |
| $Z_+Z_-$ | Product of the idempotent coordinates; its sign classes the unit |
| $\mathbb{D}^\times$ | Group of units, the elements with both coordinates nonzero |
| hyperbolic, elliptic, parabolic | Unit with $Z_+Z_- > 0$, unit with $Z_+Z_- < 0$, zero divisor with $Z_+Z_- = 0$ |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for worked computations with split-complex numbers and hyperbolic rotations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit computations in the split complex algebra and its relatives.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the hyperbolic/parabolic classification and worked examples.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the matrix and exponential computations behind the examples.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for elementary worked examples in rings with zero divisors.
