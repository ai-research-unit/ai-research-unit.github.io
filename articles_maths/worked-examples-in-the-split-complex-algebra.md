
# __Worked Examples in the Split-Complex Algebra__

## Introduction

This article works the structural facts of the split-complex algebra in explicit numbers. It is the computational companion of *Split-Complex Algebra*: the general theory is established in the earlier articles, and here it is exercised on named elements, so that a reader can see the involutions, the idempotents, the minimal ideals, the zero divisors and the hyperbolic and parabolic elements in full. The norm, the unit criterion and the polar decomposition are a form and a distance and belong to *Norm and Invertibility in the General Split-Complex Algebra* and to *Modulus–Unit Polar Decomposition of Split-Complex Numbers*; the examples below use only the algebra.

Every computation below uses the conventions of the category: $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$; general element $Q = q+jq'$ with $q = \operatorname{Re}Q$, $q' = \operatorname{Im}Q$; conjugate $\bar Q = q-jq'$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $Q_\pm = q\pm q'$.

## The Two Involutions and Their Fixed Spaces

The algebra carries two involutions: the split-complex conjugation $\bar{Q}$, and the idempotent conjugation (the swap) $\tilde{Q} = (q-q')\Pi_+ + (q+q')\Pi_-$. The first computation is that on $\mathbb{D}$ they coincide.

**Example.** Take $Q = 3+2j$. Then

$$
\bar Q = 3 - 2j,
$$

while

$$
Q = (3-2)\Pi_+ + (3+2)\Pi_- = 1\cdot\tfrac{1+j}{2} + 5\cdot\tfrac{1-j}{2} = \tfrac{1+5}{2} + \tfrac{1-5}{2}j = 3 - 2j.
$$

So $Q = \bar Q$ for this element; since the identity is polynomial in $Q$, it holds for every $Q$. The two involutions are one and the same map.

**The fixed spaces.** An element is fixed by $\bar{\cdot}$ iff $q-j q' = q+j q'$, i.e. $q'=0$; the fixed space is

$$
\mathbb{R}_{\mathbb{D}} = \{q : q \in \mathbb{R}\},
$$

the real line. An element is anti-fixed iff $q=0$; the anti-fixed space is

$$
j\mathbb{R}_{\mathbb{D}} = \{j q' : q' \in \mathbb{R}\},
$$

the split imaginary line. For $Q = 3+2j$ the projections are $Q_r = \tfrac12(Q+\bar Q) = 3$ and $j Q_i = \tfrac12(Q-\bar Q) = 2j$, so $Q = 3 + 2j$ recovers the coordinates.

## The Idempotents and the Two Minimal Ideals

The idempotents are $\Pi_+ = \tfrac12(1+j)$ and $\Pi_- = \tfrac12(1-j)$, with

$$
\Pi_+^2 = \Pi_+, \qquad \Pi_-^2 = \Pi_-, \qquad \Pi_+\Pi_- = 0, \qquad \Pi_+ + \Pi_- = 1.
$$

**Example.** Decompose $Q = 3+2j$ in the idempotent basis:

$$
Q_+ = q+q' = 5, \qquad Q_- = q-q' = 1, \qquad Q = 5\Pi_+ + 1\Pi_-
= 5\cdot\tfrac{1+j}{2} + 1\cdot\tfrac{1-j}{2} = 3 + 2j. \checkmark
$$

The two components $Q_\pm = Q\Pi_\pm$ are

$$
Q\Pi_+ = 5\Pi_+ = \tfrac{5}{2}(1+j), \qquad Q\Pi_- = 1\Pi_- = \tfrac{1}{2}(1-j).
$$

The **minimal ideals** are the lines

$$
\mathbb{R}\Pi_+ = \{(t,t) : t \in \mathbb{R}\}, \qquad \mathbb{R}\Pi_- = \{(t,-t) : t \in \mathbb{R}\},
$$

in the coordinates $(q,q')$; their product is zero, and $\mathbb{D} = \mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$. The isomorphism with $\mathbb{R}\oplus\mathbb{R}$ is realised numerically by $\varphi(3+2j) = (5, 1)$; the multiplication is componentwise, $\varphi(QB) = (Q_+B_+, Q_-B_-)$.

## Explicit Zero-Divisor Pairs

The zero divisors are the nonzero points of the two null lines; any two elements supported on opposite idempotents annihilate.

**Example (a pair).** Take

$$
Q_1 = 1+j, \qquad Q_2 = 2-2j.
$$

Then

$$
Q_1 Q_2 = (1+j)(2-2j) = 2(1+j)(1-j) = 2(1-j^2) = 0,
$$

with $Q_1 \neq 0$ and $Q_2 \neq 0$. So $Q_1$ and $Q_2$ are zero divisors; each is a non-zero multiple of an idempotent.

In the idempotent basis the mechanism is transparent: $Q_1 = 1+j = 2\Pi_+$, $Q_2 = 2-2j = 4\Pi_-$, and $\Pi_+\Pi_- = 0$.

**Example (a general pair).** For any $\lambda, \mu \neq 0$,

$$
(\lambda \Pi_+)(\mu \Pi_-) = \lambda\mu\, \Pi_+\Pi_- = 0,
$$

so the whole family of examples is $\{\lambda \Pi_+\}\times\{\mu \Pi_-\}$; and the annihilator of $\lambda \Pi_+$ is the line $\mathbb{R}\Pi_-$, as established in *Zero Divisors of the Split-Complex Algebra*. There is no pair of zero divisors with $a b = 0$ in which one factor is a unit; the criterion is that each factor lies on one of the two null lines.

## Worked Hyperbolic and Parabolic Elements

An element of $\mathbb{D}$ is classified by the signs of its two idempotent coordinates: a **hyperbolic** element is a unit with $Q_+Q_- > 0$, the coordinates having the same sign; an **elliptic** element is a unit with $Q_+Q_- < 0$, the coordinates having opposite signs; a **parabolic** element is a non-zero element with $Q_+Q_- = 0$, that is, a zero divisor. The product $Q_+Q_-$ is the algebraic reading of the quadratic form of *Norm and Invertibility in the General Split-Complex Algebra*, and its sign is preserved under multiplication; the names are the hyperbolic, elliptic and parabolic classes of the unit group.

**Hyperbolic example.** Let $Q = \tfrac54 + \tfrac34 j$. Its coordinates are

$$
Q_+ = q+q' = 2, \qquad Q_- = q-q' = \tfrac12, \qquad Q_+Q_- = 1 > 0,
$$

so $Q$ is a hyperbolic unit, and indeed $Q = 2\Pi_+ + \tfrac12\Pi_-$. Its powers are computed in the idempotent basis, where multiplication is componentwise:

$$
Q^n = 2^n\Pi_+ + 2^{-n}\Pi_- = \frac{2^n+2^{-n}}{2} + \frac{2^n-2^{-n}}{2}\,j,
$$

so the powers stay in the hyperbolic class and satisfy $Q^m Q^n = Q^{m+n}$. For $n=2$,

$$
Q^2 = \tfrac{17}{8} + \tfrac{15}{8}j,
$$

and indeed $Q Q = (\tfrac54)(\tfrac54) + (\tfrac34)(\tfrac34) + 2\cdot\tfrac54\cdot\tfrac34\,j = \tfrac{34}{16} + \tfrac{30}{16}j$, an ordinary multiplication in the basis $1, j$. $\checkmark$

**Parabolic example.** Let $Q = 1+j = 2\Pi_+$, with coordinates $Q_+ = 2$, $Q_- = 0$, so $Q$ is parabolic (a zero divisor). Then

$$
Q^2 = (1+j)^2 = 1 + 2j + j^2 = 2 + 2j = 2Q, \qquad Q^n = 2^{n-1}Q \quad (n \geq 1),
$$

which is the same computation in the idempotent basis, $Q^n = 2^n\Pi_+ = 2^{n-1}Q$. So the powers of a parabolic element stay on its null line. The element has no inverse, because $Q_- = 0$; the algebraic unit criterion of *Split-Complex Algebra* fails at it. This is the exact algebraic analogue of the parabolic elements of the hyperbolic group, which lie on the null cone.

## Summary

This article worked the algebra in explicit numbers. The two involutions of $\mathbb{D}$, the split-complex conjugation and the idempotent swap, were shown to coincide on $Q = 3+2j$ and hence throughout, with fixed space the real line $\mathbb{R}_{\mathbb{D}}$ and anti-fixed space the split imaginary line $j\mathbb{R}_{\mathbb{D}}$. The idempotents $\Pi_\pm$ were exhibited, the decomposition $3+2j = 5\Pi_+ + 1\Pi_-$ computed, and the minimal ideals $\mathbb{R}\Pi_\pm$ identified.

Explicit zero-divisor pairs were given, $Q_1 = 1+j = 2\Pi_+$ and $Q_2 = 2-2j = 4\Pi_-$ with $Q_1Q_2 = 0$, and the general pair $(\lambda \Pi_+)(\mu \Pi_-) = 0$. Finally, the hyperbolic element $Q = \tfrac54 + \tfrac34 j$, of coordinates $(2, \tfrac12)$ and powers $Q^n = 2^n\Pi_+ + 2^{-n}\Pi_-$, was compared with the parabolic element $1+j$, of coordinates $(2,0)$, with $Q^n = 2^{n-1}Q$ and no inverse.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q = q + j q'$ | General split complex number |
| $\bar Q = q - j q'$ | Split-complex conjugation (unique non-trivial involution) |
| $Q = (q-q')\Pi_+ + (q+q')\Pi_-$ | Idempotent conjugation; equal to $\bar Q$ |
| $\mathbb{R}_{\mathbb{D}}, j\mathbb{R}_{\mathbb{D}}$ | Fixed and anti-fixed spaces of the involution |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents |
| $Q_\pm = q\pm q'$ | Idempotent coordinates, $Q = Q_+\Pi_+ + Q_-\Pi_-$ |
| $\mathbb{R}\Pi_+, \mathbb{R}\Pi_-$ | Minimal ideals / null lines |
| $Q_+Q_-$ | Product of the idempotent coordinates; its sign classes the unit |
| $\mathbb{D}^\times$ | Group of units, the elements with both coordinates nonzero |
| hyperbolic, elliptic, parabolic | Unit with $Q_+Q_- > 0$, unit with $Q_+Q_- < 0$, zero divisor with $Q_+Q_- = 0$ |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for worked computations with split-complex numbers and hyperbolic rotations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit computations in the split complex algebra and its relatives.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the hyperbolic/parabolic classification and worked examples.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the matrix and exponential computations behind the examples.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for elementary worked examples in rings with zero divisors.
