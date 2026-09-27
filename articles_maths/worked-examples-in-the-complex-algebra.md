
# __Worked Examples in the Complex Algebra__

## Introduction

This article is the computed companion to the structural articles of the complex algebra. Where *Complex Algebra* states the definitions and proves the general properties, and *Complex Subspaces*, *Complex Norm and Invertibility*, *Complex Polar Representation* and *Complex Automorphisms and Derivations* develop them, the present article exhibits every one of those structures on explicit elements, so that the general statements can be read against a concrete computation.

The elements used throughout are

$$
Z = 3 + 4i, \qquad W = 1 - 2i,
$$

chosen because their arithmetic is exact and their norm forms are small squares and small integers: $N(Z) = 25$ and $N(W) = 5$, so that the inverse, the polar decomposition and the Galois action all display rational data. Where a statement needs a degenerate example, the element $0$ and the real and imaginary points of the previous articles are used. The conventions are those of *Complex Algebra*: basis $1$, $i$, $i^2 = -1$, involution $\bar{Z} = a - bi$, norm form $N(Z) = Z\bar{Z} = a^2+b^2$.

Every numerical value below is recomputed exactly; where a trigonometric value is not rational it is given to the stated number of decimals and the exact replacement is indicated.

## The Algebra on Concrete Elements

**Sum, difference and product.** With $Z = 3+4i$ and $W = 1-2i$,

$$
Z + W = 4 + 2i, \qquad Z - W = 2 + 6i,
$$

and, applying $(a+bi)(c+di) = (ac-bd) + (ad+bc)i$,

$$
Z W = (3+4i)(1-2i) = (3\cdot 1 - 4\cdot(-2)) + (3\cdot(-2) + 4\cdot 1)i = 11 - 2i .
$$

The reversed product is

$$
W Z = (1-2i)(3+4i) = (1\cdot 3 - (-2)\cdot 4) + (1\cdot 4 + (-2)\cdot 3)i = 11 - 2i,
$$

equal to $ZW$, the concrete form of commutativity.

**Powers and the norm under multiplication.** The square of $Z$ is

$$
Z^2 = (3+4i)^2 = 9 + 24i + 16 i^2 = -7 + 24i,
$$

with

$$
N(Z^2) = (-7)^2 + 24^2 = 49 + 576 = 625 = 25^2 = N(Z)^2,
$$

the multiplicativity of the norm form on a single element. In the same way $N(ZW) = N(11-2i) = 121+4 = 125 = 25 \cdot 5 = N(Z) N(W)$.

**Associativity and distributivity** are illustrated by the two products above agreeing and by $(Z+W)^2 = Z^2 + 2ZW + W^2$, which is a computation of the same rules and needs no separate display.

## The Two Involutions on Concrete Elements

The complex algebra carries the identity and complex conjugation.

**The identity.** $\operatorname{id}(Z) = 3+4i = Z$ and $\operatorname{id}(W) = W$. The identity fixes every element.

**Complex conjugation.** $\bar{Z} = 3-4i$ and $\bar{W} = 1+2i$. Conjugation is an involution:

$$
\overline{\bar{Z}} = \overline{3-4i} = 3+4i = Z,
$$

and it is an automorphism of the algebra:

$$
\overline{Z W} = \overline{11-2i} = 11+2i, \qquad \bar{Z}\,\bar{W} = (3-4i)(1+2i) = 3 + 6i - 4i - 8i^2 = 11 + 2i,
$$

the two values agreeing. In particular the norm form is invariant: $N(\bar{Z}) = 3^2 + (-4)^2 = 25 = N(Z)$.

| element | $\operatorname{id}$ | $\bar{\cdot}$ | $\bar{\cdot}$ applied twice |
|---|---|---|---|
| $Z = 3+4i$ | $3+4i$ | $3-4i$ | $3+4i$ |
| $W = 1-2i$ | $1-2i$ | $1+2i$ | $1-2i$ |
| $ZW = 11-2i$ | $11-2i$ | $11+2i$ | $11-2i$ |

## The Two Subspaces on Concrete Elements

The fixed-point subspace of conjugation is the real axis $\mathbb{R}_{\mathbb{C}}$, and its anti-fixed subspace is the imaginary axis $i\mathbb{R}_{\mathbb{C}}$.

**The real subspace.** An element is fixed by conjugation exactly when its imaginary part vanishes. For $Z$ and $W$,

$$
\bar{Z} = Z \iff 3-4i = 3+4i \iff 4 = 0, \quad \text{false},
$$

so $Z \notin \mathbb{R}_{\mathbb{C}}$; the real element $3$ and the real scalar part of $W$, namely $1$, do lie in $\mathbb{R}_{\mathbb{C}}$, with $\overline{3} = 3$.

**The imaginary subspace.** An element is anti-fixed exactly when its real part vanishes. For $Z$ and $W$,

$$
\bar{Z} = -Z \iff 3-4i = -3-4i \iff 3 = 0, \quad \text{false},
$$

so $Z \notin i\mathbb{R}_{\mathbb{C}}$; the imaginary multiples $4i$ and $-2i$ do lie in $i\mathbb{R}_{\mathbb{C}}$, with $\overline{4i} = -4i$.

**A product leaving the subspace.** The product of the two anti-fixed elements $4i$ and $-2i$ is

$$
(4i)(-2i) = -8 i^2 = 8 \in \mathbb{R}_{\mathbb{C}},
$$

which is fixed and not anti-fixed, exhibiting the failure of $i\mathbb{R}_{\mathbb{C}}$ to be closed under multiplication.

## The Decompositions, Worked

**The real and imaginary parts.** The eigencomponents of conjugation are

$$
Z_+ = \tfrac{1}{2}(Z + \bar{Z}) = \tfrac{1}{2}\bigl((3+4i)+(3-4i)\bigr) = 3 \in \mathbb{R}_{\mathbb{C}},
$$

$$
Z_- = \tfrac{1}{2}(Z - \bar{Z}) = \tfrac{1}{2}\bigl((3+4i)-(3-4i)\bigr) = 4i \in i\mathbb{R}_{\mathbb{C}},
$$

with $Z_+ + Z_- = 3+4i = Z$. For $W$ the same computation gives $W_+ = 1$ and $W_- = -2i$, again summing to $W$. The two subspaces meet only in $0$: the element $Z_+ = 3$ is not a multiple of $i$ unless $3 = 0$.

**The norm form on the pieces.** $N(Z_+) = 3^2 = 9$ and $N(Z_-) = 4^2 = 16$, and

$$
N(Z_+) + N(Z_-) = 9 + 16 = 25 = N(Z),
$$

the Pythagorean instance of the definite decomposition; for $W$, $N(W_+) + N(W_-) = 1 + 4 = 5 = N(W)$.

## The Norm Criterion for a Unit, Worked

**A unit.** The norm form of $Z$ is $N(Z) = 3^2 + 4^2 = 25 \neq 0$, so $Z$ is a unit, and the inverse formula gives

$$
Z^{-1} = \frac{\bar{Z}}{N(Z)} = \frac{3-4i}{25} = 0.12 - 0.16 i .
$$

The verification is exact:

$$
Z Z^{-1} = (3+4i)\left(\frac{3}{25} - \frac{4}{25} i\right) = \frac{(3+4i)(3-4i)}{25} = \frac{25}{25} = 1 .
$$

**A second unit.** $N(W) = 1^2 + (-2)^2 = 5 \neq 0$, so $W$ is a unit, and

$$
W^{-1} = \frac{\bar{W}}{N(W)} = \frac{1+2i}{5} = 0.2 + 0.4 i, \qquad W W^{-1} = \frac{(1-2i)(1+2i)}{5} = \frac{5}{5} = 1 .
$$

**The criterion in the product.** The product $ZW = 11-2i$ has $N(ZW) = 125 \neq 0$ and is a unit, consistent with the general fact that the product of two units is a unit. Its inverse is computed in the two ways and the results agree:

$$
(ZW)^{-1} = W^{-1} Z^{-1} = (0.2+0.4i)(0.12-0.16i) = (0.024+0.064) + (0.048-0.032)i = 0.088 + 0.016 i,
$$

$$
(ZW)^{-1} = \frac{\overline{ZW}}{N(ZW)} = \frac{11+2i}{125} = 0.088 + 0.016 i .
$$

**The non-units.** The only element of vanishing norm form is $0$, since $a^2+b^2 = 0$ forces $a = b = 0$. The zero-divisor class is empty, and there is no nonzero worked example of it.

## The Polar Decomposition, Worked

**The element $Z$.** The modulus is $r = \sqrt{N(Z)} = 5$ and the unit factor is

$$
u = \frac{Z}{r} = \frac{3+4i}{5} = 0.6 + 0.8 i, \qquad N(u) = \frac{N(Z)}{r^2} = \frac{25}{25} = 1,
$$

so $u$ lies on the unit circle. Its argument is

$$
\theta = \arg Z = \arctan\frac{4}{3} = 0.9272952180 \ \text{rad} = 53.13010235^\circ,
$$

and the reconstruction $u = \cos\theta + i\sin\theta$ gives $0.6 + 0.8 i$ to machine precision. The polar form is therefore $Z = 5(0.6+0.8i) = 5 e^{i\theta}$.

**The doubling of the angle.** Squaring the unit factor,

$$
u^2 = (0.6+0.8i)^2 = 0.36 + 0.96 i + 0.64 i^2 = -0.28 + 0.96 i,
$$

which is $e^{2i\theta} = \cos 2\theta + i\sin 2\theta$ with $2\theta = 1.8545904360$ rad, since $\cos 2\theta = -0.28$ and $\sin 2\theta = 0.96$.

**The element $W$.** Here $r = \sqrt{N(W)} = \sqrt{5}$ and

$$
u = \frac{1-2i}{\sqrt{5}} = 0.4472135955 - 0.8944271910 i, \qquad \theta = \arg W = \arctan(-2) = -1.1071487178 \ \text{rad},
$$

with $u = \cos\theta + i\sin\theta$ and $\theta$ on the principal branch $(-\pi,\pi]$. Squaring gives $u^2 = -0.6 - 0.8i$, which is $e^{2i\theta}$ at $2\theta = -2.2142974356$ rad.

**Uniqueness.** The modulus is unique and positive, and the unit factor is unique; only the angle is a class, in $\mathbb{R}/2\pi\mathbb{Z}$.

## The Galois Action, Worked

The unique nontrivial $\mathbb{R}$-automorphism of $\mathbb{C}$ is complex conjugation, written $\sigma = \bar{\cdot}$, and *Complex Automorphisms and Derivations* and *Galois Theory of ℂ/ℝ* treat its automorphism theory. On the worked elements,

$$
\sigma(Z) = \bar{Z} = 3-4i, \qquad \sigma(W) = \bar{W} = 1+2i, \qquad \sigma(ZW) = \overline{11-2i} = 11+2i .
$$

The automorphism property is exhibited by

$$
\sigma(Z)\sigma(W) = (3-4i)(1+2i) = 3+6i-4i-8i^2 = 11+2i = \sigma(ZW),
$$

and the norm form is preserved, $N(\sigma(Z)) = 25 = N(Z)$. The fixed points are exactly the real axis: $\sigma(Z) = Z$ would require $4 = 0$, so $Z$ is moved; $\sigma(3) = 3$ and $\sigma$ fixes every real number. The action is not $\mathbb{C}$-linear: $\sigma(i\cdot 1) = -i$ while $i\,\sigma(1) = i$, so $\sigma$ conjugates the scalar $i$, which is the concrete form of the conjugate-linearity of complex conjugation over $\mathbb{C}$.

## Summary

The article exhibits the structures of the complex algebra on the elements $Z = 3+4i$ and $W = 1-2i$. Their product is $ZW = 11-2i$ and their square norms are $N(Z) = 25$, $N(W) = 5$, $N(ZW) = 125$, so the norm form is multiplicative on the worked pair. The identity and complex conjugation are the two involutions; conjugation sends $Z$ to $3-4i$ and $W$ to $1+2i$, is an involution and an algebra automorphism, and fixes exactly the real axis while negating the imaginary axis.

The eigencomponents of conjugation are $Z_+ = 3 \in \mathbb{R}_{\mathbb{C}}$ and $Z_- = 4i \in i\mathbb{R}_{\mathbb{C}}$, with $N(Z_+)+N(Z_-) = N(Z)$; the product $(4i)(-2i) = 8$ is real and shows that the imaginary subspace is not closed. Both worked elements are units, with inverses $Z^{-1} = (3-4i)/25$ and $W^{-1} = (1+2i)/5$, and $(ZW)^{-1} = \overline{ZW}/125 = (11+2i)/125$; there is no nonzero non-unit because the norm form is definite. The polar decompositions are $Z = 5(0.6+0.8i)$ at $\theta = \arctan(4/3)$ and $W = \sqrt{5}(0.4472-0.8944i)$ at $\theta = \arctan(-2)$, and the doubling $u^2 = e^{2i\theta}$ was checked in both cases. The Galois action $\sigma = \bar{\cdot}$ preserves the product and the norm form on the worked elements and is conjugate-linear over $\mathbb{C}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Z = 3+4i$, $W = 1-2i$ | the two worked elements |
| $\operatorname{id}, \bar{\cdot}$ | the identity and complex conjugation |
| $\sigma = \bar{\cdot}$ | the nontrivial $\mathbb{R}$-automorphism, the Galois action |
| $Z_\pm = \tfrac12(Z \pm \bar{Z})$ | the eigencomponents of conjugation |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary subspaces |
| $N(Z) = Z\bar{Z} = a^2+b^2$ | the norm form |
| $Z^{-1} = \bar{Z}/N(Z)$ | the inverse of a nonzero element |
| $r = \sqrt{N(Z)}$, $u = Z/r$, $\theta = \arg Z$ | the polar data, $Z = ru = re^{i\theta}$ |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the geometry of the plane and worked computational examples.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the worked multiplication rules.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for elementary computational practice with complex numbers and field automorphisms.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the polar decomposition and the rotation interpretation of multiplication.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the norm, the modulus and the polar form.
