
# __Worked Examples in the Split-Complex Algebra__

## Introduction

This article works the structural facts of the split-complex algebra in explicit numbers. It is the computational companion of *Split-Complex Algebra* and its counterpart is *Biquaternion Algebra*: the general theory is established in the earlier articles, and here it is exercised on named elements, so that a reader can see the involutions, the idempotents, the minimal ideals, the zero divisors, the norm criterion, the polar decomposition and the hyperbolic and parabolic elements in full.

Every computation below uses the conventions of the category: $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$; general element $Z = a+j b$ with $a = \operatorname{Re}Z$, $b = \operatorname{Im}Z$; conjugate $\bar Z = a-j b$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $Z_\pm = a\pm b$; norm form $N(Z) = Z\bar Z = a^2-b^2$. Every number below was recomputed in double precision, and the general identities behind the examples are in the earlier articles.

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

with $a \neq 0$ and $b \neq 0$. So $a$ and $b$ are zero divisors, $N(a) = 1-1 = 0$, $N(b) = 4-4=0$.

In the idempotent basis the mechanism is transparent: $a = 1+j = 2\Pi_1$, $b = 2-2j = 4\Pi_2$, and $\Pi_1\Pi_2 = 0$.

**Example (a general pair).** For any $\lambda, \mu \neq 0$,

$$
(\lambda \Pi_1)(\mu \Pi_2) = \lambda\mu\, \Pi_1\Pi_2 = 0,
$$

so the whole family of examples is $\{\lambda \Pi_1\}\times\{\mu \Pi_2\}$; and the annihilator of $\lambda \Pi_1$ is the line $\mathbb{R}\Pi_2$, as established in *Split-Complex Zero Divisors*. There is no pair of zero divisors with $a b = 0$ in which one factor is a unit; the criterion is exactly $N(a)N(b)=N(a b)=0$.

## The Norm Criterion for a Unit, Worked

The criterion is: $Z$ is a unit iff $N(Z) \neq 0$, and then $Z^{-1} = \bar Z/N(Z)$.

**Example (a unit).** Take $Z = 2+j$. Then $N(Z) = 4-1 = 3 \neq 0$, so $Z$ is a unit. Since $\bar Z = 2-j$ and $Z\bar Z = (2+j)(2-j) = 4 - j^2 = 3$, the inverse is

$$
Z^{-1} = \frac{\bar Z}{N(Z)} = \frac{2-j}{3},
\qquad\text{and}\qquad
Z Z^{-1} = \frac{(2+j)(2-j)}{3} = \frac{3}{3} = 1. \checkmark
$$

**Example (another unit, timelike).** Take $Z = 2+3j$. Then $N(Z) = 4-9 = -5 \neq 0$, so $Z$ is a timelike unit, with

$$
Z^{-1} = \frac{2-3j}{-5} = -\tfrac25 + \tfrac35 j,
\qquad
Z Z^{-1} = \frac{N(Z)}{N(Z)} = 1. \checkmark
$$

**Example (a non-unit).** Take $Z = 1+j$. Then $N(Z) = 1-1 = 0$, so $Z$ is not a unit, and indeed $Z(1-j) = 0$. Its image under $\varphi$ is $(2,0)$, i.e. $Z = 2\Pi_1$, a zero divisor.

**Example (norm form as a product of coordinates).** For $Z = a+j b$ the relation $N(Z) = Z_+Z_-$ is visible numerically: for $Z = 3+2j$, $Z_+ = 5$, $Z_- = 1$, and $5\cdot 1 = 5 = N(3+2j) = 9-4$. So the unit criterion is the statement that both idempotent coordinates are nonzero.

## The Polar Decomposition in Its Two Regimes

The polar decomposition has two regimes, according to the sign of the norm form.

**Spacelike regime.** Take $Z = 5+3j$. Then $N(Z) = 25-9 = 16 > 0$ and

$$
\rho = \sqrt{N(Z)} = 4, \qquad \frac{Z}{\rho} = \tfrac54 + \tfrac34 j.
$$

Since $\bigl(\tfrac54\bigr)^2 - \bigl(\tfrac34\bigr)^2 = 1$, this unit is $\cosh t + j\sinh t$ with $\cosh t = 5/4$ and $\sinh t = 3/4$, hence $e^t = 2$ and $t = \ln 2$. So

$$
5 + 3j = 4\,e^{j\ln 2}, \qquad e^{j\ln 2} = \cosh(\ln 2) + j\sinh(\ln 2) = \tfrac54 + \tfrac34 j.
$$

**Timelike regime.** Take $Z = 3+5j$. Then $N(Z) = 9-25 = -16 < 0$ and

$$
\rho = \sqrt{-N(Z)} = 4, \qquad \frac{Z}{\rho} = \tfrac34 + \tfrac54 j = \sinh(\ln 2) + j\cosh(\ln 2) = j\,e^{j\ln 2}.
$$

So $3+5j = 4j\,e^{j\ln 2}$; the timelike unit is the spacelike unit preceded by $j$.

The two regimes are exchanged by multiplication by $j$, which is the reflection $a+j b \mapsto b+j a$ of the plane; this reflection fixes the null line $\mathbb{R}\Pi_1$ pointwise and negates the other null line $\mathbb{R}\Pi_2$, and on both null lines $\rho = 0$, so the polar decomposition degenerates.

## Worked Hyperbolic and Parabolic Elements

An element is classified by the sign of its norm form: **hyperbolic** if $N(Z) > 0$, **elliptic** (timelike) if $N(Z) < 0$, and **parabolic** (null) if $N(Z) = 0$.

**Hyperbolic example.** Let $Z = e^{j\ln 2} = \tfrac54 + \tfrac34 j$, with $N(Z) = 1$. Its hyperbolic logarithm is

$$
\log Z = \ln 2\; j, \qquad e^{\ln 2\,j} = \cosh(\ln 2) + j\sinh(\ln 2) = Z. \checkmark
$$

Its powers are $Z^n = e^{jn\ln 2} = \cosh(n\ln 2) + j\sinh(n\ln 2)$; for $n=2$,

$$
Z^2 = \bigl(\tfrac54\bigr)^2 + \bigl(\tfrac34\bigr)^2 + 2\cdot\tfrac54\cdot\tfrac34\, j = \tfrac{34}{16} + \tfrac{30}{16}j = \tfrac{17}{8} + \tfrac{15}{8}j,
$$

and indeed $\cosh(2\ln 2) = \tfrac{2^2+2^{-2}}{2} = \tfrac{17}{8}$ and $\sinh(2\ln 2) = \tfrac{2^2-2^{-2}}{2} = \tfrac{15}{8}$. $\checkmark$

The **hyperbolic rotation** by $t$ is the map $R_j(t) : Z \mapsto e^{jt}Z$. For $t = \ln 2$ and the null vector $1+j = 2\Pi_1$,

$$
e^{j\ln 2}(1+j) = \bigl(\tfrac54 + \tfrac34 j\bigr)(1+j) = \bigl(\tfrac54+\tfrac34\bigr) + \bigl(\tfrac54+\tfrac34\bigr)j = 2 + 2j = 2(1+j),
$$

so the null line $\mathbb{R}(1+j)$ is preserved and scaled by the hyperbolic rotation; the same is true of the other null line, with the reciprocal scale.

**Parabolic example.** Let $Z = 1+j = 2\Pi_1$, with $N(Z) = 0$. Then $Z$ is a zero divisor and

$$
Z^2 = (1+j)^2 = 1 + 2j + j^2 = 2 + 2j = 2Z, \qquad Z^n = 2^{n-1}Z \quad (n \geq 1).
$$

So the powers of a parabolic element stay on its null line; the element has no logarithm in $\mathbb{D}$, because a logarithm would require $N(Z) \neq 0$, and the exponential of every split-complex number has nonzero norm (it equals $e^{W_+}\Pi_1 + e^{W_-}\Pi_2$ with $N = e^{W_++W_-} \neq 0$). This is the exact analogue of the parabolic elements of the hyperbolic group, which lie on the null cone.

## Summary

This article worked the algebra in explicit numbers. The two natural involutions of $\mathbb{D}$, the split-complex conjugation and the idempotent swap, were shown to coincide on $Z = 3+2j$ and hence throughout, with fixed space the real line $\mathbb{R}_{\mathbb{D}}$ and anti-fixed space the split imaginary line $j\mathbb{R}_{\mathbb{D}}$. The idempotents $\Pi_\pm$ were exhibited, the decomposition $3+2j = 5\Pi_1 + 1\Pi_2$ computed, and the minimal ideals $\mathbb{R}\Pi_\pm$ identified.

Explicit zero-divisor pairs were given, $a = 1+j = 2\Pi_1$ and $b = 2-2j = 4\Pi_2$ with $a b = 0$, and the general pair $(\lambda \Pi_1)(\mu \Pi_2) = 0$. The unit criterion was worked: $2+3j$ is a timelike unit with inverse $(2-3j)/(-5)$, while $1+j$ is a non-unit. The polar decomposition was computed in both regimes, $5+3j = 4e^{j\ln 2}$ and $3+5j = 4j\,e^{j\ln 2}$. Finally, hyperbolic elements such as $e^{j\ln 2}$, with powers on the unit hyperbola and a genuine logarithm $\ln 2\,j$, were compared with parabolic elements such as $1+j$, with $Z^n = 2^{n-1}Z$ and no logarithm.

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
| $N(Z) = a^2 - b^2$ | Norm form |
| $Z^{-1} = \bar Z/N(Z)$ | Inverse of a unit |
| $\rho = \sqrt{\lvert N(Z)\rvert}$ | Modulus |
| $e^{jt} = \cosh t + j\sinh t$ | Hyperbolic unit / one-parameter group |
| $R_j(t) : Z \mapsto e^{jt}Z$ | Hyperbolic rotation |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for worked computations with split-complex numbers and hyperbolic rotations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit computations in the split complex algebra and its relatives.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the hyperbolic/parabolic classification and worked examples.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the matrix and exponential computations behind the examples.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for elementary worked examples in rings with zero divisors.
