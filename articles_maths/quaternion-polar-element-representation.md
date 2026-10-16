
# __Quaternion Polar Element Representation__

## Introduction

This article is about the **polar representation** of a quaternion: the statement that every nonzero quaternion is the product of a non-negative real scale and a unit quaternion, and that this product is unique.

The subject is elementary, and that is the point. In each algebra an element is written as a scale, possibly a central phase, possibly a hyperbolic factor, and a rotor, and the number of factors present is a property of the algebra, not a choice. In $\mathbb{H}$ exactly two of those four factors exist. Establishing that here, in the case where nothing can go wrong, fixes the vocabulary and the counting used by the three companion articles, where much can.

The plan is as follows. The modulus and the unit quaternion are defined, and existence and uniqueness are proved. The exponential, or axis-angle, form of the unit factor is derived from the power series. The two degenerate cases (the real quaternions and their negatives) are separated from the generic case. The matrix counterpart of the decomposition is recorded, since the same statement in $M_2(\mathbb{C})$ is the classical polar decomposition of a matrix. Worked examples with explicit numbers close the mathematical part.

The conventions and the symbols are those of *Quaternion Algebra* and of the corpus (*Conventions in Mathematics*); the symbols this article uses are collected in §*Summary of Notation*.

No physics is invoked. Every numerical value displayed below was recomputed in double precision.

## The Modulus and the Unit Factor

### The Two Factors

The polar representation of a quaternion is the following statement.

**Definition.** Let $\tilde q \in \mathbb{H}$, $\tilde q \neq 0$. The **polar representation** of $\tilde q$ is the writing

$$
\tilde q = r\,\tilde u_{\mathrm r}, \qquad r \in \mathbb{R}, \quad r > 0, \qquad \tilde u_{\mathrm r} \in \mathbb{H}, \quad \langle\tilde u_{\mathrm r}\rangle_{\natural} = 1,
$$

in which $r$ is the **modulus** of $\tilde q$ and $\tilde u_{\mathrm r}$ is its **unit factor**.

The second factor is a **unit element**, an element of norm one for the norm in view (*Conventions in Mathematics*, §*The Unitary Convention*); the norm in view is the quaternion norm $\langle\cdot\rangle_{\natural}$, so the unit factor is the unit sphere $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$, the group $\mathrm{Sp}(1)$. The phrase names the norm-one elements and not every invertible element: the **group of units** $\mathbb{H}^\times$ of the algebra is the wider set of nonzero quaternions, and the two senses of the word are kept apart throughout.

The definition names the two factors before anything is proved about them, so that the two propositions below have definite objects to be about. The modulus is a real number and carries one parameter. The unit factor is a quaternion constrained by one real equation, $\langle\tilde u_{\mathrm r}\rangle_{\natural} = 1$, so it carries three parameters out of the four of a general quaternion. The two counts add to four, which is the real dimension of the algebra, and this additivity is the first instance of a pattern the companion articles follow.

### The Modulus from the Quaternion Norm

The quaternion norm is

$$
\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = \sum_{\mu=0}^{3} q_\mu^2.
$$

It is the sum of four squares, so $\langle\tilde q\rangle_{\natural} > 0$ for every $\tilde q \neq 0$, and it vanishes only at $\tilde q = 0$. The modulus is its square root:

$$
r = \sqrt{\langle\tilde q\rangle_{\natural}}.
$$

Because $\langle\tilde q\rangle_{\natural}$ is strictly positive on the nonzero elements, the square root is a strictly positive real number, with no sign choice and no branch choice. The requirement $r > 0$ in the definition is therefore met automatically, and the modulus is forced. In the companion articles the corresponding object is a square root of the quaternion norm taken in a larger ring, a complex or split-complex number, and there the branch and the vanishing of the quaternion norm both demand attention. In $\mathbb{H}$ neither does.

The modulus is multiplicative, because the quaternion norm is: for any two quaternions,

$$
r(p\tilde q) = r(p)\,r(\tilde q).
$$

### The Unit Factor

The unit factor is

$$
\tilde u_{\mathrm r} = \frac{\tilde q}{r} = \frac{\tilde q}{\sqrt{\langle\tilde q\rangle_{\natural}}}.
$$

It is a quaternion of norm $1$. The set of such quaternions,

$$
\mathrm{Sp}(1) = \{\tilde u_{\mathrm r} \in \mathbb{H} : \langle\tilde u_{\mathrm r}\rangle_{\natural} = \tilde u_{\mathrm r}\tilde u_{\mathrm r}^{\natural} = 1\},
$$

is the unit sphere $\mathrm{Sp}(1)$ of unit real quaternions in $\mathbb{H} \cong \mathbb{R}^4$, a compact three-dimensional manifold, and it is a group under multiplication: if $\langle\tilde u_{\mathrm r}\rangle_{\natural} = \langle\tilde v\rangle_{\natural} = 1$ then $\langle\tilde u_{\mathrm r}\tilde v\rangle_{\natural} = \langle\tilde u_{\mathrm r}\rangle_{\natural}\langle\tilde v\rangle_{\natural} = 1$ by multiplicativity, and $\tilde u_{\mathrm r}^{-1} = \tilde u_{\mathrm r}^{\natural}$ has the same norm. The unit factor is a group element, which is what makes it a rotor in the sense of the companion articles: it acts on the vector part of the algebra by conjugation and preserves the quaternion norm there.

### Existence and Uniqueness

**Theorem.** Every nonzero quaternion $\tilde q$ has exactly one polar representation.

*Existence.* Put $r = \sqrt{\langle\tilde q\rangle_{\natural}}$ and $\tilde u_{\mathrm r} = \tilde q/r$. Since $\langle\tilde q\rangle_{\natural} > 0$, the number $r$ is a positive real, and

$$
\langle\tilde u_{\mathrm r}\rangle_{\natural} = N\!\left(\frac{\tilde q}{r}\right) = \frac{\langle\tilde q\rangle_{\natural}}{r^2} = 1
$$

because $\langle\lambda \tilde q\rangle_{\natural} = \lambda^2 \langle\tilde q\rangle_{\natural}$ for real $\lambda$. Hence $\tilde q = r \tilde u_{\mathrm r}$ with $r > 0$ and $\langle\tilde u_{\mathrm r}\rangle_{\natural} = 1$.

*Uniqueness.* Suppose $\tilde q = r \tilde u_{\mathrm r} = r' \tilde u_{\mathrm r}'$ with $r, r' > 0$ and $\langle\tilde u_{\mathrm r}\rangle_{\natural} = \langle\tilde u_{\mathrm r}'\rangle_{\natural} = 1$. Taking norms gives $r^2 = \langle\tilde q\rangle_{\natural} = r'^2$, so $r = r'$ because both are positive, and then $\tilde u_{\mathrm r} = \tilde q/r = \tilde u_{\mathrm r}'$. Hence the modulus and the unit factor are both determined by $\tilde q$.

The uniqueness holds with no sign ambiguity. Here the constraint $r > 0$ alone removes the ambiguity, because the quaternion norm is positive definite.

### What the Two Factors Are

The two factors carry distinct information, and separating them is the whole content of the decomposition.

| factor | range | parameters | what it is |
|---|---|---|---|
| $r$ | $(0, \infty)$ | $1$ | the scale, rigid on the vector part under $\tilde q \mapsto \lambda \tilde q$ |
| $\tilde u_{\mathrm r}$ | $\mathrm{Sp}(1)$ | $3$ | the rotor, a group element acting by conjugation |

The scale commutes with everything, and it is the whole of the algebra's centre on the positive side: the centre of $\mathbb{H}$ is $\mathbb{R}$, so a real scalar is the only central object available. The rotor is the non-central part of the element, and it is compact: $\mathrm{Sp}(1)$ is a closed bounded manifold, with no hyperbolic direction in it. The two statements together say that a quaternion is a positive central scale times a compact rotor, and nothing else.

## The Unit Factor and the Exponential

### The Word as Exponentials

The word $\tilde q = r\,\tilde u_{\mathrm r}$ is the product of two exponentials, the modulus and the unit factor:

$$
\tilde q = \exp(\ln\sqrt{N})\,\exp\Bigl(\mu\tfrac{\theta}{2}\Bigr), \qquad r = \sqrt{\langle\tilde q\rangle_{\natural}} > 0,
$$

with $\mu$ a unit pure quaternion, a point of the axis sphere $\mathcal{A}$ of unit vectors of $\mathbb{R}^3$, and $\theta$ the rotation angle, twice the angle of the unit factor.

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | modulus | $1$ | $\exp(\ln\sqrt{N})$ | hyperbolic | $\sqrt{N}$ | $r = \sqrt{\langle\tilde q\rangle_{\natural}} > 0$ | — |
| 2 | $\tilde u_{\mathrm r}$ | unit factor | $3$ | $\exp\bigl(\mu\tfrac{\theta}{2}\bigr)$ | trigonometric | $\cos\tfrac{\theta}{2} + \mu\sin\tfrac{\theta}{2}$ | $\theta \in [0,2\pi]$, $\mu \in \mathcal{A}$ | $\mu$ |

The modulus exponent $\ln\sqrt N$ is a real scalar of the centre, and the unit-factor exponent $\mu\tfrac{\theta}{2}$ has the unit pure quaternion $\mu$ as its root, of square $-e_0$; the first is hyperbolic and the second trigonometric. Only the trigonometric row is occupied by a non-scalar element: the roots of $+e_0$ are $\pm e_0$ alone, and there is no nilpotent, since $\mathbb{H}$ is a division algebra. A unit quaternion other than $\pm e_0$ is therefore always $\exp(\mu t)$ with $\mu$ a unit pure quaternion, never hyperbolic and never parabolic. The unit factor is the exponential of the angle only as a class, since $\exp(\mu\tfrac{\theta}{2})$ has period $4\pi$ in $\theta$, and its axis is unique only away from the two central points $\pm e_0$. The two exponents commute, so the word is order-free, and because there is no second non-central direction in the algebra, the two exponentials **amalgamate into one**, $\tilde q = \exp(\ln\sqrt N\,e_0 + \mu\tfrac{\theta}{2})$.

### The Unit Pure Quaternions

Write a quaternion as $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $\vec q = q_1e_1+q_2e_2+q_3e_3$ its vector part. A quaternion is **pure** if its scalar part vanishes, and the pure quaternions are the three-dimensional subspace $\operatorname{Im}\mathbb{H} = \operatorname{span}\{e_1,e_2,e_3\}$.

For $\vec q$ pure, the square is a scalar:

$$
\vec q^2 = -\left(q_1^2+q_2^2+q_3^2\right)e_0 = -\langle \vec q\rangle_{\natural}\,e_0,
$$

because the products of distinct units cancel in pairs, $e_2e_3 = -e_3e_2$ and so on. In particular a pure quaternion $\mu$ with $\langle \mu\rangle_{\natural} = 1$ satisfies $\mu^2 = -e_0$: the unit pure quaternions are exactly the roots of $-e_0$, and they form the two-sphere $\mathcal{A}$ (the axis sphere, the unit vectors of $\mathbb{R}^3$) inside $\operatorname{Im}\mathbb{H}$. This is the quaternion analogue of the single pair $\pm i$ of the complex numbers, and it is the object that the complex case replaces by a sign choice.

### The Exponential of a Pure Quaternion

**Proposition.** Let $\mu$ be a unit pure quaternion and let $t \in \mathbb{R}$. Then

$$
\exp(\mu t) = e_0\cos t + \mu\sin t.
$$

*Proof.* Compute the powers: $\mu^2 = -e_0$ gives $\mu^{2k} = (-1)^k e_0$ and $\mu^{2k+1} = (-1)^k\mu$. The exponential is defined by the convergent series $\exp(\tilde q) = \sum_{n\ge0}\tilde q^n/n!$, so

$$
\exp(\mu t) = \sum_{k\ge0}\frac{\mu^{2k}t^{2k}}{(2k)!} + \sum_{k\ge0}\frac{\mu^{2k+1}t^{2k+1}}{(2k+1)!} = e_0\sum_{k\ge0}\frac{(-1)^kt^{2k}}{(2k)!} + \mu\sum_{k\ge0}\frac{(-1)^kt^{2k+1}}{(2k+1)!},
$$

and the two series are the cosine and the sine.

The result is the Euler formula of the quaternions, with the same proof and one extra parameter: the role of the imaginary unit is played by any point of the axis sphere $\mathcal{A}$.

### The Quotient of Two Orthogonal Unit Quaternions

**Lemma.** Let $p, \tilde q \in \mathbb{H}$ be orthogonal as vectors of $\mathbb{R}^4$, that is $\sum_\mu p_\mu q_\mu = 0$. Then $p\tilde{q}^{\natural}$ is pure, so the quotient $p/\tilde q$ is pure. If in addition $\langle p\rangle_{\natural} = \langle\tilde q\rangle_{\natural} = 1$ then $p/\tilde q$ is a unit pure quaternion, hence a root of $-e_0$.

*Proof.* The scalar part of $p\tilde{q}^{\natural}$ is $\sum_\mu p_\mu q_\mu$, which is the Euclidean inner product, so it vanishes exactly when $p$ and $\tilde q$ are orthogonal; the quotient is $p/\tilde q = p\tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$, a real multiple of $p\tilde{q}^{\natural}$ when $\tilde q$ is a unit, and a real multiple of a pure quaternion is pure. Finally $\langle p/\tilde q\rangle_{\natural} = \langle p\rangle_{\natural}/\langle\tilde q\rangle_{\natural} = 1$, and a unit pure quaternion satisfies $\mu^2 = -e_0$ by the first proposition of this section.

For example $p = e_1$ and $\tilde q = e_2$ are orthogonal and of norm one, and $p/\tilde q = e_1e_2^{\natural} = -e_3$, a unit pure quaternion.

### The Axis and the Angle of the Unit Factor

Every unit quaternion is an exponential of this kind, and the exponent is read off from its parts.

**Proposition.** Let $\tilde u_{\mathrm r}$ be a unit quaternion with $\vec q_a \neq 0$, and put

$$
\mu = \frac{\vec q_a}{|\vec q_a|}, \qquad \theta = 2\arccos(u_0) \in (0,2\pi),
$$

where $|\vec q_a| = \sqrt{\langle \vec q_a\rangle_{\natural}}$. Then $\mu$ is a unit pure quaternion, and

$$
\tilde u_{\mathrm r} = \exp\Bigl(\mu\tfrac{\theta}{2}\Bigr).
$$

*Proof.* Since $\langle\tilde u_{\mathrm r}\rangle_{\natural} = 1$, one has $u_0^2 + |\vec q_a|^2 = 1$, so $u_0 \in (-1,1)$ when $\vec q_a\neq0$ and $\theta$ is well defined with $\cos\tfrac{\theta}{2} = u_0 > -1$ and $\sin\tfrac{\theta}{2} = |\vec q_a| > 0$. Then $e_0\cos\tfrac{\theta}{2}+\mu\sin\tfrac{\theta}{2} = u_0e_0 + \vec q_a = \tilde u_{\mathrm r}$, and the previous proposition applies.

The unit vector $\mu$ is the **axis** of the unit factor and $\theta$ is its **rotation angle**, twice the angle of the unit factor. The angle of the unit factor is taken in $[0,\pi]$, the full range of the arccosine, and the rotation angle in $[0,2\pi]$; no quotient is involved: the pair $(\mu,\theta)$ with $\mu\in \mathcal{A}$ and $\theta\in(0,2\pi)$ is in bijection with the unit quaternions of non-zero vector part.

The restriction on the angle is a property of the algebra and not a convention. Sangwine, Ell and Le Bihan state it in the quaternion polar form: the argument is confined to $[0,\pi)$ because the modulus of the vector part is always taken to be positive, there being no convenient way to define an orientation in three-dimensional space that would fix the sign of the vector part; consequently a negated angle is expressed by negating the axis, not the angle, and any numerical evaluation of the angle returns a value in $[0,\pi)$. In the notation used here the sign needs no such rescue, since the rotation angle $\theta = 2\arccos(u_0)$ carries it and ranges over $(0,2\pi)$ for $\vec q_a\neq0$, the angle of the unit factor being $\theta/2$; the two endpoints $\theta = 0$ and $\theta = 2\pi$ are the real quaternions, where it is the axis and not the angle that degenerates.

### The Half-Angle and the Rotation

The exponential is also written with the rotation angle halved,

$$
\tilde u_{\mathrm r} = \exp\Bigl(\mu\frac{\theta}{2}\Bigr) = \left(\exp\left(\mu\frac{\theta}{4}\right)\right)^{2},
$$

using the additivity of the exponential for commuting arguments, which $\mu\tfrac{\theta}{2}$ and $\mu\tfrac{\theta}{2}$ certainly are. The element $\exp(\mu\tfrac{\theta}{4})$ is the half-angle rotor, the square root of $\tilde u_{\mathrm r}$. Under the conjugation action $\vec q \mapsto \tilde u_{\mathrm r} \vec q \tilde u_{\mathrm r}^{-1}$ on the vector part, the square root acts as the rotation of angle $\tfrac{\theta}{2}$ about the axis $\mu$, so the unit factor itself acts as the rotation of angle $\theta$; this is the content of the companion article *Quaternion Rotations and Reflections*, and it is the reason the unit factor is called a rotor. The form also exhibits the double cover: the rotation angles $\theta$ and $\theta+2\pi$ are the same rotation, but they give $\exp(\mu\tfrac{\theta}{2})$ and $-\exp(\mu\tfrac{\theta}{2})$, the two opposite unit quaternions, so $\mathrm{Sp}(1)$ covers the rotation group two to one.

## The Matrix Picture

### The Isomorphism with $M_2(\mathbb{C})$

The algebra $\mathbb{H}$ embeds in the algebra of two-by-two complex matrices. Fix the isomorphism by

$$
\iota(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix}, \qquad
\iota(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0\end{pmatrix}, \qquad
\iota(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}, \qquad
\iota(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i\end{pmatrix},
$$

which is the matrix representation of *Quaternion 2x2 Matrix Element Representation*, read on the real coefficients. On a general quaternion the map is

$$
\iota(\tilde q) = \begin{pmatrix} q_0 - iq_3 & -iq_1-q_2 \\ -iq_1+q_2 & q_0+iq_3\end{pmatrix},
$$

and two identities hold. The determinant is the quaternion norm,

$$
\det\iota(\tilde q) = q_0^2+q_1^2+q_2^2+q_3^2 = \langle\tilde q\rangle_{\natural},
$$

and the image of the unit sphere is the special unitary group,

$$
\iota\big(\mathrm{Sp}(1)\big) = SU(2).
$$

### The Classical Polar Decomposition

Under $\iota$, the quaternion polar representation $\tilde q = r\tilde u_{\mathrm r}$ becomes the statement that a nonzero matrix $\iota(\tilde q)$ with $\det \neq 0$ is the product of a positive scalar and a special unitary matrix, $\iota(\tilde q) = r\,\iota(\tilde u_{\mathrm r})$ with $r = \sqrt{\det\iota(\tilde q)}$ and $\iota(\tilde u_{\mathrm r})\in SU(2)$. This is the polar decomposition of $\iota(\tilde q)$ into a positive Hermitian factor and a unitary factor, in the degenerate case where the positive Hermitian factor is a scalar multiple of the identity.

For reference, in the four-dimensional real regular representation the determinant is the square of the quaternion norm and the trace is four times the scalar part, so the same representation reads $r = (\det)^{\frac14}$ there. The two matrix readings of the quaternion algebra belong to *Quaternion 2x2 Matrix Element Representation* and *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$*, and are recalled here only to identify the classical statement.

## The Algorithm and Worked Examples

### A Generic Quaternion

Take

$$
\tilde q = e_0 + 2e_1 + 3e_2 + 4e_3.
$$

The quaternion norm is $\langle\tilde q\rangle_{\natural} = 1+4+9+16 = 30$, so the modulus is

$$
r = \sqrt{30} = 5.477225575\ldots,
$$

and the unit factor and its parts are

$$
\tilde u_{\mathrm r} = \frac{\tilde q}{\sqrt{30}} = 0.182574186\,e_0 + 0.365148372\,e_1 + 0.547722558\,e_2 + 0.730296743\,e_3,
$$

$$
\theta = 2\arccos\!\left(\frac{1}{\sqrt{30}}\right) = 2.774384634\ \text{rad} \approx 158.96^\circ,
\qquad
\mu = \frac{2e_1+3e_2+4e_3}{\sqrt{29}} = 0.371390676\,e_1+0.557086015\,e_2+0.742781353\,e_3.
$$

The reconstruction $\tilde u_{\mathrm r} = e_0\cos\tfrac{\theta}{2}+\mu\sin\tfrac{\theta}{2}$ was checked in double precision and agrees with $\tilde u_{\mathrm r}$ to $6.4\times10^{-16}$ in each of the four coefficients.

### A Second Worked Element

**Example.** For

$$
\tilde q = 1+2e_1-e_2+3e_3
$$

the quaternion norm is $\langle\tilde q\rangle_{\natural} = 1+4+1+9 = 15$, so the modulus is $r = \sqrt{15}$ and the unit factor is

$$
\tilde u_{\mathrm r} = \frac{\tilde q}{r} = \frac{1+2e_1-e_2+3e_3}{\sqrt{15}}.
$$

Its exponential form uses

$$
\cos\tfrac{\theta}{2} = \frac{q_0}{r} = \frac{1}{\sqrt{15}}, \qquad \sin\tfrac{\theta}{2} = \frac{|\vec q|}{r} = \frac{\sqrt{14}}{\sqrt{15}}, \qquad \mu = \frac{\vec q}{|\vec q|} = \frac{2e_1-e_2+3e_3}{\sqrt{14}},
$$

so that $\tilde u_{\mathrm r} = \cos\tfrac{\theta}{2}+\mu\sin\tfrac{\theta}{2} = \exp\bigl(\mu\tfrac{\theta}{2}\bigr)$ with $\theta = 2\arccos(1/\sqrt{15})$ and $\mu$ a unit pure quaternion.

### The Three Degenerate Shapes

| $\tilde q$ | $\langle\tilde q\rangle_{\natural}$ | $r$ | $\tilde u_{\mathrm r}$ | $(\mu,\theta)$ |
|---|---|---|---|---|
| $2e_0$ | $4$ | $2$ | $e_0$ | axis undefined, $\theta = 0$ |
| $-3e_0$ | $9$ | $3$ | $-e_0$ | axis undefined, $\theta = 2\pi$ |
| $e_1$ | $1$ | $1$ | $e_1$ | $\mu = e_1$, $\theta = \pi$ |
| $e_0+e_1$ | $2$ | $\sqrt{2}$ | $(e_0+e_1)/\sqrt{2}$ | $\mu = e_1$, $\theta = \pi/2$ |

The third line is a pure quaternion of unit length: its scalar part vanishes, so $\theta = \pi$ exactly and the modulus is one. The fourth is the rotor of a quarter turn about $e_1$, and its square is $e_1$, which is the check $\tilde u_{\mathrm r}^2 = \exp(\mu\theta) = e_1$ of the doubling rule.

### Two Quaternions with the Same Rotor

The decomposition separates the scale from the rotor, and the separation is exact: for real $\lambda > 0$,

$$
\lambda \tilde q = (\lambda r)\,\tilde u_{\mathrm r},
$$

with the same unit factor. Conversely $\tilde q$ and $-\tilde q$ have the same modulus and opposite unit factors, $\tilde u_{\mathrm r}$ and $-\tilde u_{\mathrm r}$, and the two unit factors produce the same rotation of the vector part, which is the double cover of the rotation group in the form in which it appears in this algebra.

## Degenerate Cases and the Relation to the Partial Forms

### The Real Quaternions

A quaternion is real if its vector part vanishes, $\tilde q = q_0e_0$. Then $\langle\tilde q\rangle_{\natural} = q_0^2$, the modulus is $r = |q_0|$, and the unit factor is $\tilde u_{\mathrm r} = \pm e_0$ with the sign of $q_0$.

The polar representation is unaffected: it still exists and is still unique, because the theorem above never used the vector part. What degenerates is the exponential form. For $\tilde u_{\mathrm r} = e_0$ the rotation angle is $\theta = 0$ and for $\tilde u_{\mathrm r} = -e_0$ it is $\theta = 2\pi$, and in both cases the axis is not determined by $\tilde u_{\mathrm r}$: every unit pure quaternion $\mu$ gives $\exp(\mu\cdot0) = e_0$ and $\exp(\mu\pi) = -e_0$. The set of pairs $(\mu,\theta)$ with $\theta$ fixed at $0$ or $2\pi$ and $\mu$ arbitrary therefore collapses to a single quaternion, and the exponential parametrisation is many-to-one exactly on the two real points of $\mathrm{Sp}(1)$.

### The Absence of a Boost and of a Central Phase

Two of the four factors that the companion articles carry are absent from the quaternion algebra, and the reasons are algebraic rather than conventional.

The centre of $\mathbb{H}$ is $\mathbb{R}$, whose unit circle is $\{\pm e_0\}$, and both points are already accounted for by the unit factor. There is no room for a central phase distinct from a sign.

In $\mathbb{H}$ no such element is available: if $\tilde q^2 = e_0$ then $(\tilde q-e_0)(\tilde q+e_0) = 0$, and since $\mathbb{H}$ is a division algebra one factor vanishes, so $\tilde q = \pm e_0$. The hyperbolic line of a hyperbolic rotation does not exist, and the only elements of norm one whose square is a positive real are $\pm e_0$.

### A Third Polar Form: the Cayley–Dickson Form

The table of quaternion representations in Sangwine, Ell and Le Bihan carries, besides the Cartesian form, the complex form $a+\mu b$, and the two forms used here, a **Cayley–Dickson polar form**,

This is a third polar form for a quaternion, and it is not the decomposition proved in this article. There the modulus is a non-negative real and the argument a real angle; here both are elements of a plane spanned by $e_0$ and one chosen pure unit, a subalgebra isomorphic to $\mathbb{C}$ that is nevertheless not the centre of $\mathbb{H}$ and depends on the choice of that unit. The three forms answer different questions. The decomposition into a real scale and a unit quaternion is unique and is the subject of this article; the axis-angle form is the exponential of a pure quaternion; and the Cayley–Dickson form writes the same element with a modulus and an argument drawn from a complex-like subalgebra. The form is recorded here so that the two forms developed in this article are not taken for an exhaustive list.

## Summary

Every nonzero quaternion $\tilde q$ has exactly one polar representation $\tilde q = r \tilde u_{\mathrm r}$, with modulus $r = \sqrt{\langle\tilde q\rangle_{\natural}} > 0$ and unit factor $\tilde u_{\mathrm r} = \tilde q/r$ of norm one. The modulus is a positive central scale and the unit factor is an element of the compact group $\mathrm{Sp}(1)$; their parameter counts, one and three, add to the real dimension four of the algebra. The unit factor is an exponential $\tilde u_{\mathrm r} = \exp(\mu\tfrac{\theta}{2})$ of a unit pure quaternion, the axis, times a real rotation angle in $[0,2\pi]$, and the parametrisation is unique except at $\tilde u_{\mathrm r} = \pm e_0$, where the axis is undetermined. In the matrix model the statement is the polar decomposition of a matrix into a positive scalar and a special unitary factor. The central phase is absent because the centre of $\mathbb{H}$ is $\mathbb{R}$, and the hyperbolic factor is absent because $\mathbb{H}$ is a division algebra and the equation $\tilde q^2 = e_0$ has only the solutions $\pm e_0$. The modulus-and-rotor and axis-angle forms are not the only polar forms a quaternion admits: the Cayley–Dickson form carries a modulus and an argument drawn from the degenerate quaternion subalgebra $a+ia'$, and its existence is recorded in the last subsection of the degenerate cases.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | a quaternion, $q_0$ its scalar part, $\vec q$ its vector part |
| $\tilde{q}^{\natural}$ | the quaternion conjugate, $q_0 - \vec q$ |
| $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = \sum_\mu q_\mu^2$ | the quaternion norm, strictly positive on nonzero elements |
| $r = \sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus, a positive real |
| $\tilde u_{\mathrm r} = \tilde q/r$ | the unit factor, of norm one |
| $\mathrm{Sp}(1)$ | the group of unit quaternions |
| $\operatorname{Im}\mathbb{H}$ | the pure quaternions, $\operatorname{span}\{e_1,e_2,e_3\}$ |
| $\mu$ | a unit pure quaternion, a root of $-e_0$, the axis |
| $\theta$ | the rotation angle, in $[0,2\pi]$ |
| $\iota$ | the isomorphism $\mathbb{H}\to M_2(\mathbb{C})$ on the real coefficients |

## Further Reading

- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* **30** (2020), for the trichotomy of the exponential and the quotient of two orthogonal unit quaternions.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the quaternion polar representation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the quaternion exponential, the unit sphere and the matrix picture.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the unit quaternions, the exponential and the covering of the rotation group.
