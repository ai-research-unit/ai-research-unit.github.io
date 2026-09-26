# __Complex Polar Representation__

## Introduction

This article is about the **polar representation** of a complex number: the statement that every nonzero complex number is the product of a positive real scale and a unit complex number, and the description of the unit factor as an exponential.

The subject is elementary, and its place in this blog is that of the base case. The polar representation is developed here for the two-dimensional definite algebra $\mathbb{C}$, in the companion article *Split-Complex Polar Representation* for the two-dimensional indefinite algebra $\mathbb{D}$, and in the four companion articles on the polar representations of the quaternion, split-quaternion, biquaternion and split-biquaternion algebras. The family decomposes every element of every one of these algebras into the same four **slots** — a scale, a central phase, a boost and a rotor — and which slots are occupied is a property of the algebra. In $\mathbb{C}$ exactly two slots are occupied, and one of them does double duty, so the algebra is the smallest case in which the pattern is already visible without any of the difficulties that come later: no branch choice, no boost, no zero divisors, no boundary.

The plan is as follows. The modulus and the unit factor are defined, and existence and uniqueness are proved. The unit factor is then described as an exponential, and the exponential is organised by the trichotomy $\nu^2 = -1$, $0$, $+1$ that governs every algebra of the family: the sign of the square of the exponent determines whether the exponential is trigonometric, parabolic or hyperbolic, and it is the same rule in $\mathbb{C}$, in $\mathbb{D}$ and in the biquaternion algebra. The two factors are then identified with the two halves of that trichotomy, the absent slots are accounted for, and the group of units, the matrix picture and worked examples close the article. The conventions are those of *Complex Algebra*: the basis is $e_0 = 1$, $e_1 = i$, the multiplication is $e_1e_1 = -e_0$, the conjugate is $\bar{z} = a - bi$, and the norm form is $N(z) = z\bar{z} = a^2 + b^2$. Every numerical value displayed below was recomputed in double precision.

## The Modulus and the Unit Factor

### The Two Factors

**Definition.** Let $z \in \mathbb{C}$, $z \neq 0$. The **polar representation** of $z$ is the writing

$$
z = r\,u, \qquad r \in \mathbb{R}, \quad r > 0, \qquad u \in \mathbb{C}, \quad N(u) = 1,
$$

in which $r$ is the **modulus** of $z$ and $u$ is its **unit factor**.

The definition names the two factors before anything is proved about them, so that the propositions below have definite objects to be about. The modulus carries one real parameter. The unit factor is constrained by one real equation, $N(u) = 1$, which is the circle, so it carries one parameter out of the two of a general complex number. The counts add to the real dimension of the algebra, and this additivity is the pattern the whole family follows.

### The Modulus from the Norm Form

The norm form of a complex number is

$$
N(z) = z\bar{z} = a^2 + b^2.
$$

It is a sum of two squares, so $N(z) > 0$ for every $z \neq 0$ and $N(z) = 0$ only at $z = 0$; the modulus is

$$
r = \sqrt{N(z)} = |z|.
$$

Because the norm form is strictly positive off the origin, the square root is a strictly positive real number with no sign choice and no branch choice. The requirement $r > 0$ is therefore met automatically and the modulus is forced. In the companion articles the corresponding object is a square root of an indefinite real form or of a complex number, and there the sign and the branch both demand attention; in $\mathbb{C}$ neither does.

The modulus is multiplicative, because the norm form is: $r(zw) = r(z)r(w)$, and also $r(\lambda z) = |\lambda| r(z)$ for real $\lambda$.

### The Unit Factor and the Circle

The unit factor is

$$
u = \frac{z}{r} = \frac{z}{|z|}.
$$

It lies on the **unit circle**

$$
U(1) = \{u \in \mathbb{C} : N(u) = 1\},
$$

which is a group under multiplication, since $N(uv) = N(u)N(v) = 1$ and $N(u^{-1}) = 1$ when $N(u) = 1$, and which is compact, being a closed bounded subset of $\mathbb{C} \cong \mathbb{R}^2$. The unit factor is the element that acts: multiplication by $u$ is a rotation of the plane through the angle of $u$, which is the content of the companion article *Rotations and Reflections in the Complex Plane*.

### Existence and Uniqueness

**Theorem.** Every nonzero complex number $z$ has exactly one polar representation.

*Existence.* Put $r = \sqrt{N(z)}$ and $u = z/r$. Since $N(z) > 0$, the number $r$ is a positive real, and $N(u) = N(z)/r^2 = 1$ because $N(\lambda z) = \lambda^2N(z)$ for real $\lambda$. Hence $z = ru$ with $r > 0$ and $N(u) = 1$.

*Uniqueness.* Suppose $z = ru = r'u'$ with $r, r' > 0$ and $N(u) = N(u') = 1$. Taking norm forms gives $r^2 = N(z) = r'^2$, so $r = r'$ because both are positive, and then $u = z/r = u'$. $\square$

The pair of factors is therefore unique, with no sign ambiguity and no branch ambiguity. What is *not* unique is the coordinate that will be used for the unit factor: the angle of $u$ is determined only modulo $2\pi$, so the representation $z = r e^{i\theta}$ determines the number $\theta$ only as a class in $\mathbb{R}/2\pi\mathbb{Z}$. This is the first of the two differences from the quaternion case, where the axis-angle coordinate of the rotor is unique, and it is a property of the exponential and not of the factorisation: two different coordinates give the same unit factor.

## The Exponential Form

### The Trichotomy of the Exponential

Every algebra of the family contains elements $\nu$ of three kinds, classified by the square:

$$
\nu^2 = -e_0 \qquad\text{(roots of }-1\text{)}, \qquad \nu^2 = 0 \qquad\text{(nilpotent)}, \qquad \nu^2 = +e_0 \qquad\text{(roots of }+1\text{)},
$$

and the exponential of $\nu\theta$ is trigonometric, parabolic or hyperbolic accordingly. This is one computation with three cases, and it is the rule that the whole family follows.

**Proposition.** Let $\nu$ be an element of a real algebra of the family and let $\theta \in \mathbb{R}$. Then the exponential of $\nu\theta$ is given by the case

| case | $\nu^2$ | $\exp(\nu\theta)$ | the summands |
|---|---|---|---|
| trigonometric | $-e_0$ | $\cos\theta\,e_0 + \nu\sin\theta$ | a cosine and a sine |
| parabolic | $0$ | $e_0 + \nu\theta$ (the series truncates) | $1$ and a linear term |
| hyperbolic | $+e_0$ | $\cosh\theta\,e_0 + \nu\sinh\theta$ | a hyperbolic cosine and a hyperbolic sine |

*Proof.* The exponential is the series $\exp(\nu\theta) = \sum_{n\ge0}\nu^n\theta^n/n!$, and the hypothesis on $\nu^2$ makes the powers periodic, truncated or monotone. For $\nu^2 = -e_0$ the even powers alternate as $(-1)^k e_0$ and the odd powers as $(-1)^k\nu$, and the two partial series are the cosine and the sine. For $\nu^2 = 0$ every power from the second onward vanishes and the series is its first two terms. For $\nu^2 = +e_0$ the even powers are $e_0$ and the odd powers are $\nu$ without alternation, and the two series are the hyperbolic cosine and the hyperbolic sine. $\square$

The trichotomy is a statement about the *sign of the square of the exponent*, not about the algebra. Which of the three rows are non-empty is a statement about the algebra, and the answer is what distinguishes the members of the family from one another.

### The Roots of $\pm 1$ in $\mathbb{C}$

| equation | solutions in $\mathbb{C}$ | count | row of the trichotomy |
|---|---|---|---|
| $\nu^2 = -e_0$ | $\nu = \pm i$ | $2$ | trigonometric: the circle |
| $\nu^2 = 0$ | $\nu = 0$ only | $1$ | parabolic: degenerate, $\exp = e_0$ |
| $\nu^2 = +e_0$ | $\nu = \pm 1$ | $2$ | hyperbolic: the real exponential |

The table is the complete classification of the exponentials of $\mathbb{C}$. The two roots of $-1$ are the two points of the circle that lie on the imaginary axis, and in $\mathbb{C}$ they are the *only* roots of $-1$ of modulus one: the quaternion algebra, whose roots of $-1$ form a two-sphere, is the first case in the family where this set is larger than two points, and the biquaternion algebra is the first where it is a complex surface.

### The Unit Factor as an Exponential

Since $N(u) = 1$, the unit factor cannot be a nontrivial real scalar, so it is not in the hyperbolic row. It is therefore

$$
u = \exp(i\theta) = \cos\theta\,e_0 + i\sin\theta, \qquad \theta \in \mathbb{R},
$$

the trigonometric row, and the polar representation reads

$$
z = r\,e^{i\theta}, \qquad r = \sqrt{N(z)} > 0, \qquad \theta \in (-\pi,\pi] \ \text{mod}\ 2\pi,
$$

which is the classical form. The reconstruction is exact:

$$
z = 3 + 4i: \qquad r = 5, \qquad \theta = \arctan\tfrac{4}{3} = 0.9272952180016122, \qquad r e^{i\theta} - z = O(10^{-16}).
$$

The angle $\theta$ is the coordinate of the unit factor, and the map $\theta \mapsto e^{i\theta}$ is a group homomorphism $\mathbb{R} \to U(1)$ whose kernel is $2\pi\mathbb{Z}$. The kernel is nontrivial, which is exactly the non-uniqueness of the coordinate, and the image is the whole circle, which is the surjectivity of the exponential onto the unit factor.

## What the Two Factors Are

### Position and Signature

Two independent dichotomies classify the directions of an algebra of the family. The first is **position**: with respect to the conjugation, a direction is *Hermitian* if $\bar{\nu} = \nu$ and *anti-Hermitian* if $\bar{\nu} = -\nu$. The second is **signature**: the sign of $\nu^2$. The two dichotomies are independent, and the unit factor of an algebra is the exponential of a direction that is Hermitian or anti-Hermitian and has signature $-1$, $0$ or $+1$. In $\mathbb{C}$ the two factors are the following.

| factor | range | position | signature | parameters | what it is |
|---|---|---|---|---|---|
| $r$ | $(0,\infty)$ | Hermitian | $\nu^2 = +e_0$ | $1$ | the scale, central, non-compact |
| $u$ | $U(1)$ | anti-Hermitian | $\nu^2 = -e_0$ | $1$ | the unit factor, central, compact |

The verification is immediate in the basis: $i$ is anti-Hermitian, $\bar{i} = -i$, and $i^2 = -e_0$, so the unit direction of the circle has position anti-Hermitian and signature $-1$; the real axis is the Hermitian part, and its unit direction $1$ has signature $+1$. The two rows of the table therefore exhaust the algebra: the Hermitian axis is the scale, the anti-Hermitian axis is the circle, and there is nothing else.

### The Two Slots and the Two Absent Ones

The four slots of the family are the scale, the central phase, the boost and the rotor. In $\mathbb{C}$ the scale is the Hermitian slot, and the second occupied slot is the anti-Hermitian one, which carries the unit factor. The remaining two slots are absent, for the following reasons.

**No boost.** A boost would be a unit factor of hyperbolic signature, $\exp(\nu\phi)$ with $\nu^2 = +e_0$ off the centre, and in $\mathbb{C}$ the only elements with $\nu^2 = +e_0$ are $\nu = \pm 1$, which are central: their exponentials are the real numbers $e^{\pm\phi}$, already counted as the scale. There is no non-central hyperbolic direction, so no boost, and the group of units contains no non-compact one-parameter subgroup other than the scale.

**The central phase is the rotation.** In the biquaternion algebra the central phase $e^{i\alpha}$ and the rotor are different factors, the phase being central and the rotor not. In $\mathbb{C}$ the algebra is commutative, so *every* element is central, and the two slots collapse into one: the circle is at the same time the rotation factor and the central phase. This is why the two-dimensional definite case cannot display the phase and the rotor separately, and why the physics articles of the corpus, which read the central phase as the $ict$ of the material sector, read it in the circle of $\mathbb{C}$.

### No Boundary

The polar representation of $\mathbb{C}$ has no boundary: it holds on $\mathbb{C}\setminus\{0\}$ and the only excluded element is the origin. The reason is the definiteness of the norm form. If $z \neq 0$ then $N(z) > 0$, so $r > 0$ and $u = z/r$ is defined; there is no element with $N(z) = 0$ other than zero, and so there is no set on which the modulus vanishes while the element does not. The companion article on the split-complex algebra is the first in the family where this fails, the first where a nonzero element can have a vanishing modulus, and the first where the polar representation must be restricted to a cone complement.

## The Group of Units and the Circle

The group of units of $\mathbb{C}$ is $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$, and it is the direct product of the two factors,

$$
\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1), \qquad z \longmapsto \big(|z|,\ z/|z|\big),
$$

which is the polar representation read as a group isomorphism. Both factors are one-dimensional, the first non-compact and the second compact, and the isomorphism is the reason the parameter counts of the polar representation are one and one.

The exponential restricted to the imaginary axis is a surjective homomorphism with kernel $2\pi\mathbb{Z}$, so

$$
U(1) \cong \mathbb{R}/2\pi\mathbb{Z},
$$

as a group, and also as a one-dimensional compact Lie group, of real dimension one. Multiplication by a unit is a rotation of the plane, $z \mapsto uz$ preserving the Euclidean norm, so $U(1)$ is identified with $SO(2)$; the identification is an isomorphism of groups and a covering map of degree one, in contrast with the double covers that appear from the quaternion algebra onwards. The exponential of the real axis is the positive scale, $\exp(\mathbb{R}) = \mathbb{R}_{>0}$, which is a one-dimensional non-compact group, and the two exponentials together exhaust the group of units:

$$
\mathbb{C}^\times = \exp(\mathbb{R})\cdot\exp(i\mathbb{R}).
$$

## The Matrix Picture

### Multiplication by $i$ as a Complex Structure

In the real basis $\{e_0,e_1\}$ a complex number is the pair $(a,b)$, and multiplication by $z = a+bi$ is the linear map

$$
M_z = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} = a\,I + b\,J, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I .
$$

The matrix $J$ is the **complex structure**: multiplication by $i$ is $J$, and $J^2 = -I$ is the matrix form of $i^2 = -e_0$, so the trigonometric row of the trichotomy is the row $J^2 = -I$ of the matrix picture. The determinant and the trace are

$$
\det M_z = a^2 + b^2 = N(z), \qquad \operatorname{tr}M_z = 2a,
$$

so the norm form is the determinant and the modulus is the square root of the determinant, $r = \sqrt{\det M_z}$. The polar representation $z = ru$ becomes in the matrix picture the factorisation

$$
M_z = r\,M_u, \qquad M_u = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \in SO(2),
$$

with $r = \sqrt{\det M_z}$: the polar decomposition of a matrix of the shape $M_z$, in the special case where the positive Hermitian factor is a scalar multiple of the identity. In the matrix polar decomposition of a general invertible matrix the positive factor is an arbitrary positive definite symmetric matrix; here the element has only the two-dimensional family $a I + bJ$ available, and inside that family the positive definite part is necessarily the scalar $rI$. The general statement is the biquaternion theorem of the companion article, where the positive factor is a genuine boost and not a scalar.

### The Reading of Each Factor

| factor | matrix | determinant | isometry type |
|---|---|---|---|
| $r$ | $rI$, $r > 0$ | $r^2$ | similarity of ratio $r$ |
| $e^{i\theta}$ | rotation by $\theta$ | $1$ | orientation-preserving isometry |
| $z = re^{i\theta}$ | conformal matrix | $r^2$ | similarity: rotation and scaling |

Every nonzero complex number is a similarity of the plane, oriented and with ratio $r$, and the polar representation is the unique splitting of that similarity into its scaling and its rotation parts. This is the precise sense in which the complex polar representation is the two-dimensional case of the matrix polar decomposition, and it is the matrix reading of the table of positions and signatures of the previous section.

## Worked Examples

### A Generic Complex Number

Take $z = 3 + 4i$. Then $N(z) = 9 + 16 = 25$, so

$$
r = \sqrt{25} = 5, \qquad u = \frac{3+4i}{5} = 0.6 + 0.8i, \qquad \theta = \arctan\frac{4}{3} = 0.9272952180016122 .
$$

The reconstruction $u = \cos\theta + i\sin\theta$ gives $0.6000000000000001 + 0.7999999999999999\,i$ and agrees with $u$ to $1.1\times10^{-16}$ in each coefficient. The angle lies in $(0,\pi/2)$, the first quadrant, as it must for a number with both parts positive.

### The Degenerate Shapes

| $z$ | $N(z)$ | $r$ | $u$ | $\theta$ |
|---|---|---|---|---|
| $2$ | $4$ | $2$ | $1$ | $0$ |
| $-3$ | $9$ | $3$ | $-1$ | $\pi$ |
| $5i$ | $25$ | $5$ | $i$ | $\pi/2$ |
| $1+i$ | $2$ | $\sqrt{2}$ | $(1+i)/\sqrt{2}$ | $\pi/4$ |

The first two lines are the real numbers, positive and negative: their unit factor is $\pm1$ and their angle is $0$ or $\pi$ on the chosen branch. The third line is a purely imaginary number of modulus five, at the angle $\pi/2$ exactly. The fourth line is the principal diagonal, at the angle $\pi/4$ exactly, and its square is $i$, which is the check $u^2 = e^{i2\theta}$ of the doubling of the angle.

### The Kernel of the Exponential

The unit factor is a point of the circle and the angle is not. Two angles differing by $2\pi$ give the same unit factor:

$$
e^{i\cdot 0} = 1, \qquad e^{i\cdot 2\pi} = 1 - 2.4\times10^{-16}i,
$$

so the reconstruction from an angle is stable to machine precision and the angle of a given unit factor is a class modulo $2\pi$. The polar representation of a fixed $z$ is unique; a *coordinate system* for the unit factor is not, and every table of angles of the corpus must be read with that quantifier understood.

## Comparison with the Other Members of the Series

| algebra | norm form | modulus | unit factor | occupied slots | unit group |
|---|---|---|---|---|---|
| $\mathbb{C}$ | $a^2+b^2$, definite | $\sqrt{N}$, positive real | $e^{i\theta}$, $\theta$ mod $2\pi$ | scale, circle (rotation and central phase together) | compact, $\mathbb{R}/2\pi\mathbb{Z}$ |
| $\mathbb{D}$ | $a^2-b^2$, indefinite | $\sqrt{|N|}$, positive real | $e^{\phi j}$ or $je^{\phi j}$ | scale, hyperbola (rotation and boost together) | four components, non-compact |
| $\mathbb{H}$ | sum of four squares | $\sqrt{N}$, positive real | $S^3$ rotor | scale, rotor | compact |
| $\mathbb{H}_{\mathrm{s}}$ | indefinite, signature $(2,2)$ | $\sqrt{|N|}$ with two regimes | two-component unit group | scale, rotor, boost | non-compact |
| $\mathbb{B}$ | complex, $N = q\bar{q}$ | $\sqrt{N}$, branch of the square root | boost and rotor, phase central | scale, central phase, boost, rotor | non-compact |

The progression is the progression of the trichotomy. In $\mathbb{C}$ only the trigonometric row is occupied by the unit factor, and it is compact. In $\mathbb{D}$ the hyperbolic row is occupied instead, and the unit group is no longer compact. From $\mathbb{H}$ onward the roots of $-1$ form a positive-dimensional set and the unit factor acquires an axis; from $\mathbb{B}$ onward both a trigonometric and a hyperbolic factor occur at once, and the word in which they are written becomes part of the statement. The two-dimensional algebra $\mathbb{C}$ is the case in which none of that can happen, which is why it is treated first.

## Summary

Every nonzero complex number has exactly one polar representation $z = ru$, with modulus $r = \sqrt{N(z)} > 0$ and unit factor $u = z/r$ on the circle. The modulus is central and Hermitian of signature $+1$ and carries one parameter; the unit factor is central and anti-Hermitian of signature $-1$ and carries one parameter; the counts add to the real dimension two. The unit factor is the exponential $u = \exp(i\theta)$ of an anti-Hermitian element of signature $-1$, which is the trigonometric row of the trichotomy $\nu^2 = -1, 0, +1$, and its coordinate $\theta$ is a class modulo $2\pi$, the kernel of the exponential. Of the four slots of the family — scale, central phase, boost, rotor — exactly two are occupied, and because $\mathbb{C}$ is commutative the circle serves as both the rotation factor and the central phase. The hyperbolic row of the trichotomy contains only the central elements $\pm1$ and so produces the scale rather than a boost, and the parabolic row contains only $\nu = 0$ and so produces nothing. The norm form is definite, so there are no zero divisors and the polar representation has no boundary: the origin is the only excluded element. In the matrix picture the statement is the polar decomposition of a conformal matrix into a scalar and a rotation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $e_0 = 1$, $e_1 = i$, $i^2 = -e_0$ |
| $z = a + bi$ | a complex number, $a$ its real part, $b$ its imaginary part |
| $\bar{z} = a - bi$ | the complex conjugate |
| $N(z) = z\bar{z} = a^2+b^2$ | the norm form, positive definite |
| $r = \sqrt{N(z)} = |z|$ | the modulus, a positive real |
| $u = z/r$ | the unit factor, $N(u) = 1$ |
| $U(1)$ | the unit circle, a compact group, identified with $SO(2)$ |
| $\theta$ | the angle, a class in $\mathbb{R}/2\pi\mathbb{Z}$ |
| $\nu$ | the exponent direction, classified by $\nu^2 = -e_0$, $0$ or $+e_0$ |
| $J$ | the complex structure, multiplication by $i$, $J^2 = -I$ |
| $M_z$ | the $2\times2$ real matrix $aI + bJ$ of multiplication by $z$ |

## Further Reading

- *Complex Algebra* (`articles_maths/complex-algebra.md`), for the algebra, its conjugation, its norm form and its two fixed-point subspaces.
- *The Complex Numbers* (`articles_maths/the-complex-numbers.md`), for the construction of $\mathbb{C}$ and its algebraic properties.
- *Split-Complex Polar Representation* (`articles_maths/split-complex-polar-representation.md`), for the same question in the two-dimensional algebra where the norm form is indefinite, the unit factor is hyperbolic and a boundary appears.
- *Rotations and Reflections in the Complex Plane* (`articles_maths/rotations-and-reflections-in-the-complex-plane.md`), for multiplication by a unit as a plane rotation and the identification $U(1) = SO(2)$.
- *Quaternion Polar Representation* (`articles_maths/quaternion-polar-representation.md`), for the first case in which the unit factor acquires an axis.
- *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the four-slot representation of which this article is the two-slot base case.
- *Complex Representations* (`articles_maths/complex-representations.md`), for the representation theory of $\mathbb{C}$ as an algebra over $\mathbb{R}$.
- *Complex Special Functions* (`articles_maths/complex-special-functions.md`), for the exponential and the trigonometric and hyperbolic functions on which the trichotomy of this article rests.
