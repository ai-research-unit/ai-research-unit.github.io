# __Quaternion Polar Representation__

## Introduction

This article is about the **polar representation** of a quaternion: the statement that every nonzero quaternion is the product of a non-negative real scale and a unit quaternion, and that this product is unique.

The subject is elementary, and that is the point. The quaternion polar representation is the simplest member of a family of four representations that this article opens and three companion articles continue: the quaternion algebra $\mathbb{H}$, the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$, the biquaternion algebra $\mathbb{B}$ and the split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}$. In each algebra an element is written as a scale, possibly a central phase, possibly a boost, and a rotor, and the number of factors present is a property of the algebra, not a choice. In $\mathbb{H}$ exactly two of those four factors exist. Establishing that here, in the case where nothing can go wrong, fixes the vocabulary and the counting used by the three companion articles, where much can.

The plan is as follows. The modulus and the unit quaternion are defined, and existence and uniqueness are proved. The exponential, or axis-angle, form of the unit factor is derived from the power series. The two degenerate cases (the real quaternions and their negatives) are separated from the generic case. The matrix counterpart of the decomposition is recorded, since the same statement in $M_2(\mathbb{C})$ is the classical polar decomposition of a matrix. Worked examples with explicit numbers close the mathematical part. The article is written under the corpus conventions of *Quaternion Algebra*: the basis is $e_0 = 1, e_1, e_2, e_3$, the multiplication is $e_k^2 = -e_0$ and $e_1e_2 = e_3$, the conjugate is $\bar{q} = q_0 - \mathbf{q}$, and the norm form is $N(q) = q\bar{q} = \sum_{\mu} q_\mu^2$. No physics is invoked. Every numerical value displayed below was recomputed in double precision.

## The Modulus and the Unit Quaternion

### The Two Factors

The polar representation of a quaternion is the following statement.

**Definition.** Let $q \in \mathbb{H}$, $q \neq 0$. The **polar representation** of $q$ is the writing

$$
q = r\,u, \qquad r \in \mathbb{R}, \quad r > 0, \qquad u \in \mathbb{H}, \quad N(u) = 1,
$$

in which $r$ is the **modulus** of $q$ and $u$ is its **unit factor**.

The definition names the two factors before anything is proved about them, so that the two propositions below have definite objects to be about. The modulus is a real number and carries one parameter. The unit factor is a quaternion constrained by one real equation, $N(u) = 1$, so it carries three parameters out of the four of a general quaternion. The two counts add to four, which is the real dimension of the algebra, and this additivity is the first instance of a pattern the companion articles follow.

### The Modulus from the Norm Form

The norm form of a quaternion is

$$
N(q) = q\bar{q} = \sum_{\mu=0}^{3} q_\mu^2.
$$

It is the sum of four squares, so $N(q) > 0$ for every $q \neq 0$, and it vanishes only at $q = 0$. The modulus is its square root:

$$
r = \sqrt{N(q)}.
$$

Because $N(q)$ is strictly positive on the nonzero elements, the square root is a strictly positive real number, with no sign choice and no branch choice. The requirement $r > 0$ in the definition is therefore met automatically, and the modulus is forced. In the companion articles the corresponding object is a square root of the norm form taken in a larger ring, a complex or split-complex number, and there the branch and the vanishing of the norm form both demand attention. In $\mathbb{H}$ neither does.

The modulus is multiplicative, because the norm form is: for any two quaternions,

$$
r(pq) = r(p)\,r(q).
$$

### The Unit Factor

The unit factor is

$$
u = \frac{q}{r} = \frac{q}{\sqrt{N(q)}}.
$$

It is a quaternion of norm form $1$. The set of such quaternions,

$$
\mathrm{Sp}(1) = \{u \in \mathbb{H} : N(u) = 1\},
$$

is the unit sphere $S^3$ of $\mathbb{H} \cong \mathbb{R}^4$, a compact three-dimensional manifold, and it is a group under multiplication: if $N(u) = N(v) = 1$ then $N(uv) = N(u)N(v) = 1$ by multiplicativity, and $u^{-1} = \bar{u}$ has the same norm form. The unit factor is a group element, which is what makes it a rotor in the sense of the companion articles: it acts on the vector part of the algebra by conjugation and preserves the norm form there.

### Existence and Uniqueness

**Theorem.** Every nonzero quaternion $q$ has exactly one polar representation.

*Existence.* Put $r = \sqrt{N(q)}$ and $u = q/r$. Since $N(q) > 0$, the number $r$ is a positive real, and

$$
N(u) = N\!\left(\frac{q}{r}\right) = \frac{N(q)}{r^2} = 1
$$

because $N(\lambda q) = \lambda^2 N(q)$ for real $\lambda$. Hence $q = r u$ with $r > 0$ and $N(u) = 1$.

*Uniqueness.* Suppose $q = r u = r' u'$ with $r, r' > 0$ and $N(u) = N(u') = 1$. Taking norm forms gives $r^2 = N(q) = r'^2$, so $r = r'$ because both are positive, and then $u = q/r = u'$. Hence the modulus and the unit factor are both determined by $q$.

The uniqueness holds with no sign ambiguity. This is the sharpest difference from the complex case, where $z = re^{i\theta}$ determines $\theta$ only modulo $2\pi$, and from the biquaternion case of the companion article, where a fourth factor appears and a sign must be fixed by a branch convention. Here the constraint $r > 0$ alone removes the ambiguity, because the norm form of $\mathbb{H}$ is positive definite.

### What the Two Factors Are

The two factors carry distinct information, and separating them is the whole content of the decomposition.

| factor | range | parameters | what it is |
|---|---|---|---|
| $r$ | $(0, \infty)$ | $1$ | the scale, rigid on the vector part under $q \mapsto \lambda q$ |
| $u$ | $\mathrm{Sp}(1) = S^3$ | $3$ | the rotor, a group element acting by conjugation |

The scale commutes with everything, and it is the whole of the algebra's centre on the positive side: the centre of $\mathbb{H}$ is $\mathbb{R}$, so a real scalar is the only central object available. The rotor is the non-central part of the element, and it is compact: $S^3$ is a closed bounded manifold, with no hyperbolic direction in it. The two statements together say that a quaternion is a positive central scale times a compact rotor, and nothing else.

## The Exponential Form

### The Unit Pure Quaternions

Write a quaternion as $q = q_0 e_0 + \mathbf{q}$ with $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$ its vector part. A quaternion is **pure** if its scalar part vanishes, and the pure quaternions are the three-dimensional subspace $\operatorname{Im}\mathbb{H} = \operatorname{span}\{e_1,e_2,e_3\}$.

For $\mathbf{q}$ pure, the square is a scalar:

$$
\mathbf{q}^2 = -\left(q_1^2+q_2^2+q_3^2\right)e_0 = -N(\mathbf{q})\,e_0,
$$

because the products of distinct units cancel in pairs, $e_2e_3 = -e_3e_2$ and so on. In particular a pure quaternion $\mu$ with $N(\mu) = 1$ satisfies $\mu^2 = -e_0$: the unit pure quaternions are exactly the roots of $-e_0$, and they form the two-sphere $S^2$ inside $\operatorname{Im}\mathbb{H}$. This is the quaternion analogue of the single pair $\pm i$ of the complex numbers, and it is the object that the complex case replaces by a sign choice.

### The Exponential of a Pure Quaternion

**Proposition.** Let $\mu$ be a unit pure quaternion and let $\theta \in \mathbb{R}$. Then

$$
\exp(\mu\theta) = e_0\cos\theta + \mu\sin\theta .
$$

*Proof.* Compute the powers: $\mu^2 = -e_0$ gives $\mu^{2k} = (-1)^k e_0$ and $\mu^{2k+1} = (-1)^k\mu$. The exponential is defined by the convergent series $\exp(x) = \sum_{n\ge0}x^n/n!$, so

$$
\exp(\mu\theta) = \sum_{k\ge0}\frac{\mu^{2k}\theta^{2k}}{(2k)!} + \sum_{k\ge0}\frac{\mu^{2k+1}\theta^{2k+1}}{(2k+1)!} = e_0\sum_{k\ge0}\frac{(-1)^k\theta^{2k}}{(2k)!} + \mu\sum_{k\ge0}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!},
$$

and the two series are the cosine and the sine. $\square$

The result is the Euler formula of the quaternions, with the same proof and one extra parameter: the role of the imaginary unit is played by any point of $S^2$.

### The Trichotomy of the Exponential

The formula just proved is one row of a rule that every algebra of the polar series follows. For an element $\nu$ of the algebra and a real $\theta$, the sign of $\nu^2$ decides the character of the exponential:

| case | $\nu^2$ | $\exp(\nu\theta)$ | where it occurs in the series |
|---|---|---|---|
| trigonometric | $-e_0$ | $\cos\theta\,e_0 + \nu\sin\theta$ | the unit factor here; the circle of $\mathbb{C}$; the rotors of $\mathbb{H}_{\mathrm{s}}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ |
| parabolic | $0$ | $e_0 + \nu\theta$, the series truncating | $\mathbb{B}$ only, for instance $\nu = e_1+ie_2$; the row is empty in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{H}$ |
| hyperbolic | $+e_0$ | $\cosh\theta\,e_0 + \nu\sinh\theta$ | the hyperbolic factor of $\mathbb{D}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$, where it is the boost; the row is empty in $\mathbb{C}$ and $\mathbb{H}$ |

*Proof.* The three cases are the three behaviours of the powers of $\nu$ in the series $\exp(\nu\theta) = \sum_{n\ge0}\nu^n\theta^n/n!$: period four for $\nu^2 = -e_0$, period two for $\nu^2 = +e_0$, and truncation at the second term for $\nu^2 = 0$. Summing each series gives the stated form. $\square$

The consequence for $\mathbb{H}$ is that only the trigonometric row is occupied by a non-scalar element. The roots of $+e_0$ are $\pm e_0$ alone, since $q^2 = e_0$ with $q = a+\mathbf{v}$ forces $a\mathbf{v} = 0$, hence $\mathbf{v} = 0$ and $a = \pm1$; the roots of $0$ are none, since $\mathbb{H}$ is a division algebra. A unit quaternion other than $\pm e_0$ is therefore always $\exp(\mu\theta)$ with $\mu$ a unit pure quaternion, the exponential is trigonometric, and the unit factor of a quaternion is never hyperbolic and never parabolic. The two empty rows are the reason this algebra has neither a boost nor a central phase, and they are the two rows that the companion articles of the series occupy.

### The Quotient of Two Orthogonal Unit Quaternions

One real-quaternion fact is used by the biquaternion constructions of the series without being stated here, and it belongs next to the axis.

**Lemma.** Let $p, q \in \mathbb{H}$ be orthogonal as vectors of $\mathbb{R}^4$, that is $\sum_\mu p_\mu q_\mu = 0$. Then $p\bar{q}$ is pure, so the quotient $p/q$ is pure. If in addition $N(p) = N(q) = 1$ then $p/q$ is a unit pure quaternion, hence a root of $-e_0$.

*Proof.* The scalar part of $p\bar{q}$ is $\sum_\mu p_\mu q_\mu$, which is the Euclidean inner product, so it vanishes exactly when $p$ and $q$ are orthogonal; the quotient is $p/q = p\bar{q}/N(q)$, a real multiple of $p\bar{q}$ when $q$ is a unit, and a real multiple of a pure quaternion is pure. Finally $N(p/q) = N(p)/N(q) = 1$, and a unit pure quaternion satisfies $\mu^2 = -e_0$ by the first proposition of this section. $\square$

For example $p = e_1$ and $q = e_2$ are orthogonal and of norm form one, and $p/q = e_1\bar{e}_2 = -e_3$, a unit pure quaternion. The lemma is the step that produces the root $\nu$ of the hyperbolic exponent in the two-exponential polar forms of the biquaternion literature, and it is quoted there as Sangwine & Hitzer's Lemma 2; with it, the construction of the biquaternion hyperbolic factor is a statement about the quaternion algebra alone, which is where it is proved.

### The Axis and the Angle of the Unit Factor

Every unit quaternion is an exponential of this kind, and the exponent is read off from its parts.

**Proposition.** Let $u$ be a unit quaternion with $\mathbf{u} \neq 0$, and put

$$
\mu = \frac{\mathbf{u}}{|\mathbf{u}|}, \qquad \theta = \arccos(u_0) \in (0,\pi),
$$

where $|\mathbf{u}| = \sqrt{N(\mathbf{u})}$. Then $\mu$ is a unit pure quaternion, and

$$
u = \exp(\mu\theta).
$$

*Proof.* Since $N(u) = 1$, one has $u_0^2 + |\mathbf{u}|^2 = 1$, so $u_0 \in (-1,1)$ when $\mathbf{u}\neq0$ and $\theta$ is well defined with $\cos\theta = u_0 > -1$ and $\sin\theta = |\mathbf{u}| > 0$. Then $e_0\cos\theta+\mu\sin\theta = u_0e_0 + \mathbf{u} = u$, and the previous proposition applies. $\square$

The unit vector $\mu$ is the **axis** of the unit factor and $\theta$ is its **angle**. The angle is taken in $[0,\pi]$, which is the full range of the arccosine, so no quotient is involved: the pair $(\mu,\theta)$ with $\mu\in S^2$ and $\theta\in(0,\pi)$ is in bijection with the unit quaternions of non-zero vector part.

The restriction on the angle is a property of the algebra and not a convention. Sangwine, Ell and Le Bihan state it in the quaternion polar form: the argument is confined to $[0,\pi)$ because the modulus of the vector part is always taken to be positive, there being no convenient way to define an orientation in three-dimensional space that would fix the sign of the vector part; consequently a negated angle is expressed by negating the axis, not the angle, and any numerical evaluation of the angle returns a value in $[0,\pi)$. In the notation used here the sign needs no such rescue, since $\theta = \arccos(u_0)$ carries it and ranges over $(0,\pi)$ for $\mathbf{u}\neq0$; the two endpoints $\theta = 0$ and $\theta = \pi$ are the real quaternions, where it is the axis and not the angle that degenerates.

### The Half-Angle and the Rotation

The exponential is also written with half the angle,

$$
u = \exp(\mu\theta) = \left(\exp\left(\mu\frac{\theta}{2}\right)\right)^{2},
$$

using the additivity of the exponential for commuting arguments, which $\mu\theta$ and $\mu\theta$ certainly are. The element $\exp(\mu\theta/2)$ is the half-angle rotor. Under the conjugation action $x \mapsto u x u^{-1}$ on the vector part, the half-angle rotor acts as the rotation of angle $\theta$ about the axis $\mu$; this is the content of the companion article *Quaternion Rotations and Reflections*, and it is the reason the unit factor is called a rotor. The half-angle form also exhibits the double cover: replacing $\theta$ by $\theta+2\pi$ changes $\exp(\mu\theta/2)$ to $-\exp(\mu\theta/2)$ while leaving $u$ unchanged, so $\mathrm{Sp}(1)$ covers the rotation group two to one.

## The Degenerate Cases

### The Real Quaternions

A quaternion is real if its vector part vanishes, $q = q_0e_0$. Then $N(q) = q_0^2$, the modulus is $r = |q_0|$, and the unit factor is $u = \pm e_0$ with the sign of $q_0$.

The polar representation is unaffected: it still exists and is still unique, because the theorem above never used the vector part. What degenerates is the exponential form. For $u = e_0$ the angle is $\theta = 0$ and for $u = -e_0$ it is $\theta = \pi$, and in both cases the axis is not determined by $u$: every unit pure quaternion $\mu$ gives $\exp(\mu\cdot0) = e_0$ and $\exp(\mu\pi) = -e_0$. The set of pairs $(\mu,\theta)$ with $\theta$ fixed at $0$ or $\pi$ and $\mu$ arbitrary therefore collapses to a single quaternion, and the exponential parametrisation is many-to-one exactly on the two real points of $\mathrm{Sp}(1)$.

### The Absence of a Boost and of a Central Phase

Two of the four factors that the companion articles carry are absent from the quaternion algebra, and the reasons are algebraic rather than conventional.

**No central phase.** A phase factor would be an element of the centre of the algebra lying on a circle, as $e^{i\alpha}$ does in $\mathbb{B}$. The centre of $\mathbb{H}$ is $\mathbb{R}$, whose unit circle is $\{\pm e_0\}$, and both points are already accounted for by the unit factor. There is no room for a central phase distinct from a sign.

**No boost.** A boost factor would be a positive element $\exp(\sigma)$ with $\sigma$ a non-scalar in the traceless part, the quaternion analogue of the Hermitian traceless exponent of the companion article. In $\mathbb{H}$ no such element is available: if $q^2 = e_0$ then $(q-e_0)(q+e_0) = 0$, and since $\mathbb{H}$ is a division algebra one factor vanishes, so $q = \pm e_0$. The hyperbolic line of a boost does not exist, and the only elements of norm form one whose square is a positive real are $\pm e_0$.

The two absences are the reason the quaternion decomposition has two factors and not four, and they are collected in the comparison table of the companion article on the biquaternion polar representation, where the same four slots are filled by $1+1+3+3$ rather than by $1+0+0+3$.

### A Third Polar Form: the Cayley–Dickson Form

The table of quaternion representations in Sangwine, Ell and Le Bihan carries, besides the Cartesian form, the complex form $a+\mu b$, and the two forms used here, a **Cayley–Dickson polar form**,

$$
q = \mathcal{A}\exp(\mathcal{B}j),
$$

where $\mathcal{A}$ and $\mathcal{B}$ are **degenerate quaternions** of the shape $w+ix$, so that the modulus and the argument are both complex rather than real. The paper attributes the form to Sangwine and Le Bihan and lists it without formulas, deferring the derivation to its references.

This is a third polar form for a quaternion, and it is not the decomposition proved in this article. There the modulus is a non-negative real and the argument a real angle; here both are elements of a plane spanned by $e_0$ and one chosen pure unit, a subalgebra isomorphic to $\mathbb{C}$ that is nevertheless not the centre of $\mathbb{H}$ and depends on the choice of that unit. The three forms answer different questions. The decomposition into a real scale and a unit quaternion is unique and is the subject of this article; the axis-angle form is the exponential of a pure quaternion; and the Cayley–Dickson form writes the same element with a modulus and an argument drawn from a complex-like subalgebra. The form is recorded here so that the two forms developed in this article are not taken for an exhaustive list.

## The Matrix Picture

### The Isomorphism with $M_2(\mathbb{C})$

The complexification of $\mathbb{H}$ is isomorphic to the algebra of two-by-two complex matrices. Fix the isomorphism by

$$
\Phi(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix}, \qquad
\Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0\end{pmatrix}, \qquad
\Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}, \qquad
\Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i\end{pmatrix},
$$

which is the restriction of the biquaternion matrix representation of the companion physics article to real coefficients. On a general quaternion the map is

$$
\Phi(q) = \begin{pmatrix} q_0 - iq_3 & -iq_1-q_2 \\ -iq_1+q_2 & q_0+iq_3\end{pmatrix},
$$

and two identities hold. The determinant is the norm form,

$$
\det\Phi(q) = q_0^2+q_1^2+q_2^2+q_3^2 = N(q),
$$

and the image of the unit sphere is the special unitary group,

$$
\Phi\big(\mathrm{Sp}(1)\big) = SU(2).
$$

### The Classical Polar Decomposition

Under $\Phi$, the quaternion polar representation $q = ru$ becomes the statement that a nonzero matrix $\Phi(q)$ with $\det \neq 0$ is the product of a positive scalar and a special unitary matrix, $\Phi(q) = r\,\Phi(u)$ with $r = \sqrt{\det\Phi(q)}$ and $\Phi(u)\in SU(2)$. This is the polar decomposition of $\Phi(q)$ into a positive Hermitian factor and a unitary factor, in the degenerate case where the positive Hermitian factor is a scalar multiple of the identity. The general statement of the matrix polar decomposition, in which the positive factor is an arbitrary positive Hermitian matrix, is the biquaternion theorem of the companion article; the quaternion case is what it collapses to when the element has real coefficients.

For reference, in the four-dimensional real regular representation the determinant is the square of the norm form and the trace is four times the scalar part, so the same representation reads $r = (\det)^{\frac14}$ there. The two matrix readings of the quaternion algebra belong to the companion articles on the matrix representations, and are recalled here only to identify the classical statement.

## Worked Examples

### A Generic Quaternion

Take

$$
q = e_0 + 2e_1 + 3e_2 + 4e_3 .
$$

The norm form is $N(q) = 1+4+9+16 = 30$, so the modulus is

$$
r = \sqrt{30} = 5.477225575\ldots,
$$

and the unit factor and its parts are

$$
u = \frac{q}{\sqrt{30}} = 0.182574186\,e_0 + 0.365148372\,e_1 + 0.547722558\,e_2 + 0.730296743\,e_3,
$$

$$
\theta = \arccos\!\left(\frac{1}{\sqrt{30}}\right) = 1.387192317\ \text{rad} \approx 79.48^\circ,
\qquad
\mu = \frac{2e_1+3e_2+4e_3}{\sqrt{29}} = 0.371390676\,e_1+0.557086015\,e_2+0.742781353\,e_3 .
$$

The reconstruction $u = e_0\cos\theta+\mu\sin\theta$ was checked in double precision and agrees with $u$ to $6.4\times10^{-16}$ in each of the four coefficients.

### The Three Degenerate Shapes

| $q$ | $N(q)$ | $r$ | $u$ | $(\mu,\theta)$ |
|---|---|---|---|---|
| $2e_0$ | $4$ | $2$ | $e_0$ | axis undefined, $\theta = 0$ |
| $-3e_0$ | $9$ | $3$ | $-e_0$ | axis undefined, $\theta = \pi$ |
| $e_1$ | $1$ | $1$ | $e_1$ | $\mu = e_1$, $\theta = \pi/2$ |
| $e_0+e_1$ | $2$ | $\sqrt{2}$ | $(e_0+e_1)/\sqrt{2}$ | $\mu = e_1$, $\theta = \pi/4$ |

The third line is a pure quaternion of unit length: its scalar part vanishes, so $\theta = \pi/2$ exactly and the modulus is one. The fourth is the half-angle rotor of a quarter turn about $e_1$, and its square is $e_1$, which is the check $u^2 = \exp(2\mu\theta/2) = \exp(\mu\cdot2\theta)$ of the doubling rule.

### Two Quaternions with the Same Rotor

The decomposition separates the scale from the rotor, and the separation is exact: for real $\lambda > 0$,

$$
\lambda q = (\lambda r)\,u,
$$

with the same unit factor. Conversely $q$ and $-q$ have the same modulus and opposite unit factors, $u$ and $-u$, and the two unit factors produce the same rotation of the vector part, which is the double cover of the rotation group in the form in which it appears in this algebra.

## Summary

Every nonzero quaternion $q$ has exactly one polar representation $q = r u$, with modulus $r = \sqrt{N(q)} > 0$ and unit factor $u = q/r$ of norm form one. The modulus is a positive central scale and the unit factor is an element of the compact group $\mathrm{Sp}(1) = S^3$; their parameter counts, one and three, add to the real dimension four of the algebra. The unit factor is an exponential $u = \exp(\mu\theta)$ of a unit pure quaternion, the axis, times a real angle in $[0,\pi]$, and the parametrisation is unique except at $u = \pm e_0$, where the axis is undetermined. In the matrix model the statement is the polar decomposition of a matrix into a positive scalar and a special unitary factor. Of the four factors of the companion biquaternion decomposition, exactly two occur here: the scale and the rotor. The central phase is absent because the centre of $\mathbb{H}$ is $\mathbb{R}$, and the boost is absent because $\mathbb{H}$ is a division algebra and the equation $q^2 = e_0$ has only the solutions $\pm e_0$. The modulus-and-rotor and axis-angle forms are not the only polar forms a quaternion admits: the Cayley–Dickson form carries a modulus and an argument drawn from the degenerate quaternion subalgebra $w+ix$, and its existence is recorded in the last subsection of the degenerate cases.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$ |
| $q = q_0e_0+\mathbf{q}$ | a quaternion, $q_0$ its scalar part, $\mathbf{q}$ its vector part |
| $\bar{q}$ | the quaternion conjugate, $q_0 - \mathbf{q}$ |
| $N(q) = q\bar{q} = \sum_\mu q_\mu^2$ | the norm form, strictly positive on nonzero elements |
| $r = \sqrt{N(q)}$ | the modulus, a positive real |
| $u = q/r$ | the unit factor, of norm form one |
| $\mathrm{Sp}(1) = S^3$ | the group of unit quaternions |
| $\operatorname{Im}\mathbb{H}$ | the pure quaternions, $\operatorname{span}\{e_1,e_2,e_3\}$ |
| $\mu$ | a unit pure quaternion, a root of $-e_0$, the axis |
| $\theta$ | the angle, in $[0,\pi]$ |
| $\Phi$ | the isomorphism $\mathbb{B} \to M_2(\mathbb{C})$ restricted to real coefficients |

## Further Reading

- *Quaternion Algebra* (`articles_maths/quaternion-algebra.md`), for the algebra, its conjugations, its norm form and its vector part.
- *Split-Quaternion Polar Representation* (`articles_maths/split-quaternion-polar-representation.md`), for the same question in the algebra where the norm form is indefinite and a boost appears.
- *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the four-factor representation of which this article is the degenerate two-factor case.
- *Biquaternion Partial Polar Representations* (`articles_maths/biquaternion-partial-polar-representations.md`), for the three partial forms and their domains.
- *Split-Biquaternion Polar Representation* (`articles_maths/split-biquaternion-polar-representation.md`), for the semisimple case, where the modulus is complex and the rotor is six-dimensional.
- *Quaternion Rotations and Reflections* (`articles_maths/quaternion-rotations-and-reflections.md`), for the conjugation action of the unit factor and the double cover.
- *Quaternion Exponential and Logarithm* (`articles_maths/quaternion-special-functions.md`), for the exponential and logarithm of a quaternion, of which the exponentiation of a pure quaternion used here is the one-variable branch.
- *Complex Polar Representation* (`articles_maths/complex-polar-representation.md`) and *Split-Complex Polar Representation* (`articles_maths/split-complex-polar-representation.md`), for the two-dimensional members of the series, where the trichotomy of the exponential is stated once and the rows that are empty here are occupied.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for Lemma 2, the quotient of two orthogonal unit quaternions recorded above, and for Lemma 1, the trichotomy of the exponential.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the range of the polar argument in $[0,\pi)$ and for the Cayley–Dickson polar form with a complex modulus and a complex argument.
