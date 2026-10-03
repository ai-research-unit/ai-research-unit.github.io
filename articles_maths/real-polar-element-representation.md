
# __Real Polar Element Representation__

## Introduction

This article is about the **polar representation** of a real number: the statement that every nonzero real number is the product of a positive real scale and a sign, and the description of the sign factor as an element of the two-element group.

The subject is elementary, and its place in this blog is that of the base case. The polar representation is developed here for the one-dimensional algebra $\mathbb{R}$, in the companion article *Complex Polar Element Representation* for the two-dimensional definite algebra $\mathbb{C}$, and in the companion articles on the polar representations of the split-complex, quaternion, split-quaternion, biquaternion and split-biquaternion algebras. The family decomposes every element of every one of these algebras into the same four **slots** — a scale, a central phase, a boost and a rotor — and which slots are occupied is a property of the algebra. In $\mathbb{R}$ exactly two slots are occupied, the scale and the compact slot, the latter filled by the discrete sign group, and the algebra is the smallest case of the pattern: no branch choice, no boost, no zero divisors, no boundary, and only one continuous parameter.

The plan is as follows. The modulus and the sign factor are defined, and existence and uniqueness are proved. The sign factor is then described through the exponential, and the exponential is organised by the trichotomy $\nu^2 = -1$, $0$, $+1$ that governs every algebra of the family: the sign of the square of the exponent determines whether the exponential is trigonometric, parabolic or hyperbolic, and it is the same rule in $\mathbb{R}$, in $\mathbb{C}$ and in the biquaternion algebra. The two factors are then identified with two rows of that trichotomy, the absent slots are accounted for, and the group of units, the matrix picture and worked examples close the article. The conventions are those of *Real Algebra*: the basis is $e_0 = 1$, the sole involution is the identity, and the norm is $N(a) = a\,a = a^2$. Every numerical value displayed below is exact.

## The Modulus and the Sign Factor

### The Two Factors

**Definition.** Let $a \in \mathbb{R}$, $a \neq 0$. The **polar representation** of $a$ is the writing

$$
a = r\,\sigma, \qquad r \in \mathbb{R}, \quad r > 0, \qquad \sigma \in \mathbb{R}, \quad \sigma^2 = 1,
$$

in which $r$ is the **modulus** of $a$ and $\sigma$ is its **sign factor**.

The definition names the two factors before anything is proved about them, so that the propositions below have definite objects to be about. The modulus carries one real parameter. The sign factor is constrained by the equation $\sigma^2 = 1$, which is the two-point set $\{\pm1\}$, so it carries no continuous parameter. The counts add to the real dimension of the algebra, $1 + 0 = 1$, and this additivity is the pattern the whole family follows.

### The Modulus from the Norm

The norm of a real number is

$$
N(a) = a\,a = a^2.
$$

It is a single square, so $N(a) > 0$ for every $a \neq 0$ and $N(a) = 0$ only at $a = 0$; the modulus is

$$
r = \sqrt{N(a)} = |a|.
$$

Because the norm is strictly positive off the origin, the square root is a strictly positive real number with no sign choice and no branch choice. The requirement $r > 0$ is therefore met automatically and the modulus is forced. In the companion articles the corresponding object is a square root of an indefinite real form or of a complex number, and there the sign and the branch both demand attention; in $\mathbb{R}$ neither does.

The modulus is multiplicative, because the norm is: $r(ab) = r(a)r(b)$, and also $r(\lambda a) = |\lambda|\,r(a)$ for real $\lambda$.

### The Sign Factor and the Two-Point Set

The sign factor is

$$
\sigma = \frac{a}{r} = \frac{a}{|a|} = \operatorname{sgn} a .
$$

It lies on the **two-point set**

$$
\{\pm1\} = \{\sigma \in \mathbb{R} : N(\sigma) = 1\},
$$

which is a group under multiplication, since $N(\sigma\tau) = N(\sigma)N(\tau) = 1$ and $N(\sigma^{-1}) = N(\sigma) = 1$ when $N(\sigma) = 1$, and which is compact, being a finite closed subset of $\mathbb{R}$. It is the **orthogonal group of the line**, written $O(1)$: the real $1\times1$ matrices of norm one are exactly $[\pm1]$, because a $1\times1$ matrix $[g]$ preserves the form $N$ exactly when $g^2 = 1$. The group $O(1) \cong \mathbb{Z}/2$ has two elements, the identity $+1$ and the reflection $-1$.

The sign factor is the element that acts: multiplication by $-1$ is the reflection of the line through the origin, and multiplication by $+1$ is the identity. In the complex case the corresponding unit factor is the circle $U(1)$, which is connected; here the group $O(1)$ is discrete, and it is the component group of the unit group.

### Existence and Uniqueness

**Theorem.** Every nonzero real number $a$ has exactly one polar representation.

*Existence.* Put $r = \sqrt{N(a)}$ and $\sigma = a/r$. Since $N(a) > 0$, the number $r$ is positive, and $N(\sigma) = N(a)/r^2 = 1$ because $N(\lambda a) = \lambda^2N(a)$ for real $\lambda$. Hence $a = r\sigma$ with $r > 0$ and $\sigma^2 = 1$.

*Uniqueness.* Suppose $a = r\sigma = r'\sigma'$ with $r, r' > 0$ and $\sigma^2 = (\sigma')^2 = 1$. Taking norms gives $r^2 = N(a) = (r')^2$, so $r = r'$ because both are positive, and then $\sigma = a/r = \sigma'$.

The pair of factors is therefore unique, with no sign ambiguity and no branch ambiguity. What is *not* unique is a coordinate for the sign factor: the sign has no continuous coordinate at all, because the group is finite, and the discrete alternative is the whole of what the exponential can offer. This is the base case of the non-uniqueness of the exponential coordinate that appears from $\mathbb{C}$ onward, where the coordinate of the unit factor is a class modulo $2\pi$.

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

*Proof.* The exponential is the series $\exp(\nu\theta) = \sum_{n\ge0}\nu^n\theta^n/n!$, and the hypothesis on $\nu^2$ makes the powers periodic, truncated or monotone. For $\nu^2 = -e_0$ the even powers alternate as $(-1)^k e_0$ and the odd powers as $(-1)^k\nu$, and the two partial series are the cosine and the sine. For $\nu^2 = 0$ every power from the second onward vanishes and the series is its first two terms. For $\nu^2 = +e_0$ the even powers are $e_0$ and the odd powers are $\nu$ without alternation, and the two series are the hyperbolic cosine and the hyperbolic sine.

The trichotomy is a statement about the *sign of the square of the exponent*, not about the algebra. Which of the three rows are non-empty is a statement about the algebra, and the answer is what distinguishes the members of the family from one another.

### The Roots of $\pm1$ in $\mathbb{R}$

| equation | solutions in $\mathbb{R}$ | count | row of the trichotomy |
|---|---|---|---|
| $\nu^2 = -e_0$ | none | $0$ | trigonometric: empty |
| $\nu^2 = 0$ | $\nu = 0$ only | $1$ | parabolic: degenerate, $\exp = e_0$ |
| $\nu^2 = +e_0$ | $\nu = \pm 1$ | $2$ | hyperbolic: the real exponential |

The table is the complete classification of the exponentials of $\mathbb{R}$. The two roots of $+1$ are the two points of the sign group, and in $\mathbb{R}$ every root of $+1$ has norm one, because $N(a) = a^2$; these two points are the whole root set. The split-complex algebra, whose roots of $+1$ number four, is the first in the family where this set is larger than two points, and the biquaternion algebra is the first where they form a complex surface. The roots of $-1$ are absent here, and their absence is the statement that $\mathbb{R}$ has no continuous rotation, no continuous phase and no continuous rotor; the compact slot is filled by the discrete sign group alone.

### The Sign Factor as an Exponential

The sign factor $\sigma$ has norm one, so its modulus is one. It therefore satisfies $\sigma = \pm1$, and the two cases are reached as follows.

- **The identity component.** The positive root $\nu = +1$ has signature $+1$, so the hyperbolic row gives $\exp(\theta) = \cosh\theta + \sinh\theta = e^{\theta} > 0$ for $\theta \in \mathbb{R}$; this is the positive scale. In particular $\exp(0) = +1 = \sigma$ for the identity sign.
- **The nontrivial component.** The negative root $\nu = -1$ gives $\exp(-\theta) = e^{-\theta} > 0$, again a positive scale and not the element $-1$. The element $\sigma = -1$ is therefore **not** in the image of the exponential of the algebra: $\exp(\mathbb{R}) = \mathbb{R}_{>0}$ throughout.

The exponential of the real algebra is thus the positive ray alone, and the sign factor is not produced by it. The correct statement of the exponential form is therefore

$$
a = r\,\sigma = \exp(t)\,\sigma, \qquad t = \ln r \in \mathbb{R}, \qquad \sigma \in \{\pm1\} = O(1),
$$

in which the continuous part is the exponential and the discrete part is the sign. The reconstruction is exact: for $a = -\tfrac{3}{4}$, $r = \tfrac{3}{4}$, $t = \ln\tfrac{3}{4}$ and $\sigma = -1$, and $\exp(t)\sigma = \tfrac{3}{4}\cdot(-1) = a$. The kernel of the exponential is trivial,

$$
\exp(t) = 1 \iff t = 0, \qquad \ker\exp = \{0\},
$$

in contrast with the complex case, where the kernel is the discrete lattice $2\pi i\,\mathbb{Z}$. The exponential of the real algebra is injective, and this injectivity is why the sign must be carried separately. The pair $(t, \sigma)$ is unique, because the logarithm is unique on the positive reals and the sign is determined; the exponential therefore supplies a canonical continuous coordinate on the identity component, and the sign is the discrete coordinate of the component.

## What the Two Factors Are

### Position and Signature

Two independent dichotomies classify the directions of an algebra of the family. The first is **position**: with respect to the involution, a direction is *fixed* if $\operatorname{id}(\nu) = \nu$ and *anti-fixed* if $\operatorname{id}(\nu) = -\nu$. The second is **signature**: the sign of $\nu^2$. The two dichotomies are independent. In $\mathbb{R}$ every element is fixed, the anti-fixed direction being only $0$, and the two factors are the following.

| factor | range | position | signature | parameters | what it is |
|---|---|---|---|---|---|
| $r$ | $(0,\infty)$ | fixed | $\nu^2 = +e_0$ | $1$ | the scale, central, non-compact |
| $\sigma$ | $\{\pm1\}$ | fixed | $\nu^2 = +e_0$ | $0$ | the sign, central, compact and discrete |

The verification is immediate in the basis: $1$ is fixed and $1^2 = +e_0$, so the scale direction has position fixed and signature $+1$; the sign direction is the same element $1$ up to the two signs, and it is fixed as well. Both rows of the table are therefore in the fixed subspace, and the anti-fixed subspace contributes nothing. Unlike the complex case, where the second factor is the anti-fixed imaginary direction, here both factors have the same position and the same signature; they differ in the sign and in whether they carry a continuous parameter.

### The Two Slots and the Two Absent Ones

The four slots of the family are the scale, the central phase, the boost and the rotor. In $\mathbb{R}$ the scale is the continuous fixed slot, and the second occupied slot is the compact slot, which in $\mathbb{R}$ is discrete and carries the sign. The remaining two slots are absent, for the following reasons.

**No boost, and no continuous rotor or phase.** A boost would be a unit factor of hyperbolic signature, $\exp(\nu\phi)$ with $\nu^2 = +e_0$ **off** the fixed subspace, and a rotor or phase would be a unit factor of trigonometric signature, $\exp(\nu\theta)$ with $\nu^2 = -e_0$. In $\mathbb{R}$ the only elements with $\nu^2 = +e_0$ are $\nu = \pm1$, which are fixed: their exponentials are the positive real numbers $e^{\pm\phi}$, already counted as the scale, so there is no non-fixed hyperbolic direction and no boost. The trigonometric row is empty outright, because no element of $\mathbb{R}$ squares to $-1$; so there is no trigonometric direction at all, hence no continuous rotor and no continuous central phase, and the compact slot is filled by the discrete sign group alone, the two roots of $+1$ being its elements. The unit group contains exactly one continuous one-parameter subgroup, the scale.

**The sign is the whole compact part.** In the complex algebra the second factor is the connected circle $U(1)$, and the group of units is connected. Here the second factor is the disconnected group $O(1) = \{\pm1\}$, and it is the component group of $\mathbb{R}^\times$. The two-dimensional definite case is the first in which the second factor is connected, and the passage from $O(1)$ to $U(1)$ is the first place the family acquires a nontrivial continuous compact factor.

### No Boundary

The polar representation of $\mathbb{R}$ has no boundary: it holds on $\mathbb{R}\setminus\{0\}$ and the only excluded element is the origin. The reason is the definiteness of the norm. If $a \neq 0$ then $N(a) > 0$, so $r > 0$ and $\sigma = a/r$ is defined; there is no element with $N(a) = 0$ other than zero, and so there is no set on which the modulus vanishes while the element does not. The split-complex algebra is the first in the family where this fails, the first where a nonzero element can have a vanishing modulus, and the first where the polar representation must be restricted to a cone complement.

**The parametrisation as a homeomorphism.** The parametrisation of the unit group by the two factors,

$$
\Phi : \mathbb{R}_{>0} \times \{\pm1\} \longrightarrow \mathbb{R}^\times, \qquad \Phi(r, \sigma) = r\sigma,
$$

is a bijective local homeomorphism, and a homeomorphism onto $\mathbb{R}^\times$ because the sign coordinate is discrete and the map is continuous with continuous inverse $(|a|, \operatorname{sgn}a)$; its image is all of $\mathbb{R}^\times$. It fails to cover exactly the complement $\mathbb{R}\setminus\mathbb{R}^\times = \{0\}$, a single point rather than a hypersurface, and the sign group $\{\pm1\}$ is finite, so neither the scale variable nor the sign variable has a boundary. In the biquaternion algebra the same parametrisation fails on the null cone, a real algebraic variety of real dimension $6$, which is the genuine boundary of the polar representation and carries the link of the null cone; the real case has no such set, because the norm is definite and the zero-divisor class is empty. The absent null cone and the absent link are the mathematical content of the definiteness of $\mathbb{R}$.

**The boundary as ends.** The scale coordinate $r = |a|$ runs over $(0,\infty)$, whose two ends are $0$ and $+\infty$; the end at $0$ is the removed origin, and the end at $+\infty$ is one of the two ends of the line. The sign coordinate is finite, so it contributes no end. The only boundary of the polar representation is thus the single point at the end $r = 0$, where the norm vanishes.

## The Group of Units and the Sign Group

The group of units of $\mathbb{R}$ is $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$, and it is the direct product of the two factors,

$$
\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}, \qquad a \longmapsto \bigl(|a|,\ \operatorname{sgn}a\bigr),
$$

which is the polar representation read as a group isomorphism. The first factor is one-dimensional and non-compact, the second is finite and compact, and the isomorphism is the reason the parameter counts of the polar representation are one and zero.

The group of units is **disconnected**, with two components:

$$
\pi_0(\mathbb{R}^\times) \cong \{\pm1\} = O(1), \qquad \mathbb{R}^\times = \mathbb{R}_{>0} \sqcup \mathbb{R}_{<0}.
$$

The identity component is the positive ray $\mathbb{R}_{>0} = \exp(\mathbb{R})$, and the nontrivial component is its negative $-\mathbb{R}_{>0}$. The sign group is therefore the group of components, $\{\pm1\} \cong \mathbb{R}^\times/\mathbb{R}_{>0}$, and it is identified with the orthogonal group $O(1)$ of the line. In the complex case the second factor $U(1)$ is connected, so $\mathbb{C}^\times$ has one component; the passage from two components to one is the first effect of the two-dimensional definite case.

Inversion in the polar coordinates reads $\iota(r\sigma) = r^{-1}\sigma$, inverting the scale and fixing the sign; the two components are each stable under inversion, and the fixed points of inversion are $\pm1$.

## The Matrix Picture

### Multiplication by the Sign as a Reflection

In the basis $\{e_0\}$ a real number is the single coordinate $a$, and multiplication by $a$ is the linear map

$$
M_a = [\,a\,] = a\,I, \qquad I = [\,1\,],
$$

the $1\times1$ Cayley matrix. The determinant and the trace are

$$
\det M_a = a, \qquad \operatorname{tr}M_a = a.
$$

The sign factor $\sigma = -1$ acts by the matrix $[-1]$, which is the **reflection** of the line through the origin; the sign factor $\sigma = +1$ acts by the identity $[1]$. The two matrices $\pm I$ are exactly the orthogonal group $O(1)$ of the line, and the norm is their determinant squared: the reflection $[-1]$ has $\det[-1] = -1$ and $N(-1) = 1$. The group $O(1)$ is the set of $1\times1$ matrices preserving $N$, and it is the sign group; its identity component is $\{+1\} = SO(1)$, the special orthogonal group, and the quotient $O(1)/SO(1) \cong \{\pm1\}$ is the same two-element group.

### The Reading of Each Factor

| factor | matrix | determinant | isometry type |
|---|---|---|---|
| $r$ | $[r]$, $r > 0$ | $r$ | similarity of ratio $r$ |
| $\sigma = -1$ | $[-1]$ | $-1$ | reflection through the origin |
| $\sigma = +1$ | $[1]$ | $1$ | identity |
| $a = r\sigma$ | $[a]$ | $a$ | signed similarity: reflection and scaling |

Every nonzero real number is a signed similarity of the line, and the polar representation is the splitting of that signed similarity into its scaling and its reflection parts. This is the precise sense in which the real polar representation is the one-dimensional case of the matrix polar decomposition, where the positive definite factor is the scalar $rI$ and the orthogonal factor is $\pm I$; in the complex case the orthogonal factor is a rotation, and from the biquaternion case onward it becomes a genuine unitary factor and the positive factor a genuine boost.

## Worked Examples

### A Generic Real Number

Take $a = -\tfrac{3}{4}$. Then $N(a) = \tfrac{9}{16}$, so

$$
r = \sqrt{\tfrac{9}{16}} = \tfrac{3}{4}, \qquad \sigma = \frac{-3/4}{3/4} = -1, \qquad r\sigma = \tfrac{3}{4}\cdot(-1) = -\tfrac{3}{4} = a .
$$

The modulus is positive and the sign is the nontrivial element of the sign group; the reconstruction is exact.

### The Degenerate Shapes

| $a$ | $N(a)$ | $r$ | $\sigma$ | exponential coordinate |
|---|---|---|---|---|
| $4$ | $16$ | $4$ | $+1$ | $\ln 4$ |
| $-\tfrac{3}{4}$ | $\tfrac{9}{16}$ | $\tfrac{3}{4}$ | $-1$ | $\ln\tfrac{3}{4}$ |
| $1$ | $1$ | $1$ | $+1$ | $0$ |
| $-1$ | $1$ | $1$ | $-1$ | $0$ |
| $0$ | $0$ | — | — | — |

The first two lines are a positive and a negative number: same modulus shape, opposite signs. The third and fourth lines are the two elements of the sign group itself, of modulus one; they are the fixed points of the polar decomposition, $a = \sigma$ with $r = 1$. The last line is the origin, the unique excluded element. The exponential coordinate of a positive number is its logarithm, and the sign is carried beside it; the coordinate of $-1$ is $0$ as for $+1$, because the sign is not in the image of the exponential.

### The Kernel of the Exponential

The exponential of the real algebra is injective,

$$
e^{t_1} = e^{t_2} \iff t_1 = t_2,
$$

so its kernel is $\{0\}$ and the continuous coordinate of a positive element is unique. The non-uniqueness that the complex and higher cases exhibit is absent here: the only ambiguity is the sign, which is a discrete choice and not a kernel element. In this sense the real algebra is the one member of the family whose continuous exponential coordinate is canonical.

## Comparison with the Other Members of the Series

| algebra | norm | modulus | unit factor | occupied slots | unit group |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $a^2$, definite | $\sqrt{N} = \lvert a\rvert$, positive real | $\operatorname{sgn}a \in \{\pm1\}$ | scale, compact sign (rotor and phase together, discrete) | two components, $\mathbb{R}_{>0}\times O(1)$ |
| $\mathbb{C}$ | $u^2+v^2$, definite | $\sqrt{N}$, positive real | $e^{i\theta}$, $\theta$ mod $2\pi$ | scale, circle (rotation and central phase together) | connected, $\mathbb{R}_{>0}\times U(1)$ |
| $\mathbb{D}$ | $u^2-v^2$, indefinite | $\sqrt{\lvert N\rvert}$, positive real | $e^{\phi j}$ or $je^{\phi j}$ | scale, hyperbola (rotation and boost together) | four components, non-compact |
| $\mathbb{H}$ | sum of four squares | $\sqrt{N}$, positive real | $S^3$ rotor | scale, rotor | non-compact, $\mathbb{R}_{>0}\times S^3$ |
| $\mathbb{B}$ | complex, $N = q\bar{q}$ | $\sqrt{N}$, branch of the square root | boost and rotor, phase central | scale, central phase, boost, rotor | non-compact |

The progression is the progression of the trichotomy. In $\mathbb{R}$ only the hyperbolic row is occupied, and it produces the scale; the trigonometric row is empty and the second factor is the discrete sign group, the compact slot in its discrete form. In $\mathbb{C}$ the trigonometric row is occupied by the unit factor for the first time, and the unit factor is a connected circle. In $\mathbb{D}$ the hyperbolic row is occupied instead, and the unit group is no longer compact. From $\mathbb{H}$ onward the roots of $-1$ form a positive-dimensional set and the unit factor acquires an axis; from $\mathbb{B}$ onward both a trigonometric and a hyperbolic factor occur at once, and the word in which they are written becomes part of the statement. The one-dimensional algebra $\mathbb{R}$ is the case in which none of that can happen, which is why it is treated first.

## Summary

Every nonzero real number has exactly one polar representation $a = r\sigma$, with modulus $r = \sqrt{N(a)} = |a| > 0$ and sign $\sigma = a/|a| \in \{\pm1\}$. The modulus is fixed and of signature $+1$ and carries one parameter; the sign is fixed, discrete and carries none; the counts add to the real dimension one. The sign group is $O(1) \cong \mathbb{Z}/2$, the orthogonal group of the line, and its two elements are the two components of $\mathbb{R}^\times = \mathbb{R}_{>0}\times\{\pm1\}$, which is why the real unit group is disconnected while the complex one is connected.

The exponential of the real algebra is governed by the trichotomy $\nu^2 = -1, 0, +1$: the trigonometric row is empty, so there is no continuous rotor and no continuous phase; the parabolic row contains only $\nu = 0$, so it is degenerate; and the hyperbolic row contains $\nu = \pm1$, whose exponentials are the positive ray $\exp(\mathbb{R}) = \mathbb{R}_{>0}$. The nontrivial sign $\sigma = -1$ is therefore not an exponential, and the exponential form of the representation reads $a = \exp(t)\sigma$ with $t = \ln|a|$ and $\sigma \in O(1)$; the kernel of the exponential is trivial. Of the four slots of the family — scale, central phase, boost, rotor — exactly two are occupied, the scale and the compact slot, and the second is discrete. The norm is definite, so there are no zero divisors and the polar representation has no boundary: the origin is the only excluded element. In the matrix picture the statement is the splitting of the signed similarity $[a]$ into the scalar $[r]$ and the reflection $[\sigma]$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, basis $e_0 = 1$, sole involution the identity |
| $a$ | a real number |
| $N(a) = a^2$ | the norm, positive definite |
| $r = \sqrt{N(a)} = \lvert a\rvert$ | the modulus, a positive real |
| $\sigma = \operatorname{sgn}a = a/\lvert a\rvert$ | the sign factor, an element of $\{\pm1\}$ |
| $\{\pm1\} = O(1) \cong \mathbb{Z}/2$ | the sign group, the orthogonal group of the line |
| $a = r\sigma$ | the polar representation |
| $a = \exp(t)\sigma$, $t = \ln\lvert a\rvert$ | the exponential form, with the sign carried separately |
| $\Phi(r,\sigma) = r\sigma$ | the parametrisation of the unit group by scale and sign |
| $\nu$ | the exponent direction, classified by $\nu^2 = -e_0$, $0$ or $+e_0$ |
| $\mathbb{R}^\times = \mathbb{R}_{>0}\sqcup\mathbb{R}_{<0}$ | the group of units, two components |
| $M_a = [a]$ | the $1\times1$ Cayley matrix of multiplication by $a$ |
| $\exp(\mathbb{R}) = \mathbb{R}_{>0}$, $\ker\exp = \{0\}$ | the image and kernel of the exponential |

## Further Reading

- Edmund Landau, *Grundlagen der Analysis* (Akademische Verlagsgesellschaft, 1930), for the order of $\mathbb{R}$, the absolute value and the sign of an element.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for the absolute value as a multiplicative norm and the logarithm.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd edition (Springer, 2015), for the exponential map, its image and its kernel in the one-dimensional case.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the circle and the sign group as the base cases of the compact orthogonal groups.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the passage from the sign decomposition of the line to the polar decomposition of the plane.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the determinant, the orthogonal group and the polar decomposition in the one-dimensional matrix algebra.
