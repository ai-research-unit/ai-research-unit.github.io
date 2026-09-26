
# __The Three Two-Dimensional Algebras and the Three Kinds of Rotation__

## Introduction

The vector space $\mathbb{R}^2$ carries exactly three commutative unital algebra structures up to isomorphism, and the three have an interpretation in terms of rotations. Multiplication by an element of unit norm is a linear transformation of the plane; when the norm form is positive definite the transformation is an ordinary rotation, when it is indefinite it is a hyperbolic rotation, and when it is degenerate it is a parabolic rotation, a shear. The three cases are the complex numbers, the split complex numbers and the dual numbers, and the sign of the square of the generator — $-1$, $+1$ or $0$ — is what selects the geometry.

This article develops the three cases side by side: the algebra, its units, its norm form, the parametrisation of the group of norm-one units, the matrix of multiplication, the orbit of a point and the fixed lines. It then explains the two structural facts that make the picture what it is: multiplicative rotation belongs to dimension two because a multiplicative norm form on the plane has only the three possible signatures, and the same construction in dimension three forces one to give up commutativity, the smallest algebra that serves being the four-dimensional quaternions.

Throughout, the generator of the algebra is written $\omega$ with $\omega^2 = \sigma$, where $\sigma = -1$ for $\mathbb{C}$, $\sigma = +1$ for $\mathbb{D}$ and $\sigma = 0$ for $\mathbb{D}'$. A general element is $z = x + \omega y$ with $x, y \in \mathbb{R}$, and the three algebras are the quotient algebras

$$
\mathbb{C} = \frac{\mathbb{R}[\omega]}{(\omega^2+1)}, \qquad \mathbb{D} = \frac{\mathbb{R}[\omega]}{(\omega^2-1)}, \qquad \mathbb{D}' = \frac{\mathbb{R}[\omega]}{(\omega^2)} .
$$

The symbol $\mathbb{D}$ denotes the split complex numbers and $\mathbb{D}'$ the dual numbers, as fixed in the corpus.

## Multiplication by a Unit

Let $A$ be one of the three algebras and let $u = a + \omega b$ be a unit. Left multiplication by $u$,

$$
L_u(x + \omega y) = (a + \omega b)(x + \omega y) = (ax + \sigma by) + \omega\,(ay + bx),
$$

is an $\mathbb{R}$-linear map of $\mathbb{R}^2$. In the basis $(1, \omega)$ its matrix is

$$
M(u) = \begin{pmatrix} a & \sigma b \\ b & a \end{pmatrix},
\qquad
\det M(u) = a^2 - \sigma b^2 .
$$

The assignment $u \mapsto M(u)$ is an injective algebra homomorphism $A \to M_2(\mathbb{R})$, so multiplication by units realises the unit group $A^\times$ as a subgroup of $\mathrm{GL}_2(\mathbb{R})$.

**Definition.** The **norm form** of $A$ is

$$
N(x + \omega y) = x^2 - \sigma y^2 =
\begin{cases}
x^2 + y^2, & \sigma = -1, \\
x^2 - y^2, & \sigma = +1, \\
x^2, & \sigma = 0 .
\end{cases}
$$

It satisfies $N(uv) = N(u)N(v)$ and $\det M(u) = N(u)$, and the **rotation group** of $A$ is the group of norm-one elements

$$
G_A = \{u \in A : N(u) = 1\}.
$$

Multiplicativity makes $G_A$ a group, and for each $u \in G_A$ the map $L_u$ preserves the quadratic form $N$ on $\mathbb{R}^2$:

$$
N(u \cdot z) = N(u)N(z) = N(z), \qquad z \in A .
$$

So the three cases are the three signatures of a quadratic form in two variables: definite, indefinite and degenerate. That exhausts the possibilities, and it is why there are exactly three kinds of rotation of this kind.

## The Elliptic Case: The Complex Numbers

For $\sigma = -1$ the norm form is positive definite, $N = x^2 + y^2$, and it vanishes only at the origin; hence every nonzero complex number is a unit. The norm-one group is parametrised by the angle,

$$
u(\theta) = \cos\theta + i \sin\theta, \qquad N(u(\theta)) = \cos^2\theta + \sin^2\theta = 1,
$$

and $u(\theta)u(\phi) = u(\theta + \phi)$ by the addition formulas, so $G_{\mathbb{C}} = U(1) \cong \mathbb{R}/2\pi\mathbb{Z}$. The matrix of multiplication is

$$
M(u(\theta)) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \in SO(2),
$$

since $a = \cos\theta$, $b = \sin\theta$ and $\det M = 1$. The map $\theta \mapsto M(u(\theta))$ is an isomorphism $U(1) \cong SO(2)$: every determinant-one orthogonal transformation of the plane arises, and the parametrisation is the usual one.

**Orbits and fixed lines.** Multiplication by $u(\theta)$ preserves $N$, so it maps each circle $x^2 + y^2 = r^2$ to itself; the orbit of a point $z \neq 0$ is the circle of radius $|z|$. For $\theta$ not a multiple of $\pi$ the transformation has no real fixed line, because a real eigenvector would require $\sin\theta = 0$; the only fixed point is the origin. The group is compact, and the parametrisation is by an angle in a bounded interval.

## The Hyperbolic Case: The Split Complex Numbers

For $\sigma = +1$ the norm form is indefinite, $N = x^2 - y^2$, and it vanishes exactly on the two null lines $x = \pm y$; the elements on those lines, other than $0$, are the zero divisors of $\mathbb{D}$. The norm-one group is the hyperbola $x^2 - y^2 = 1$, which has two branches. On the branch $x > 0$ it is parametrised by the rapidity,

$$
u(t) = \cosh t + j \sinh t, \qquad N(u(t)) = \cosh^2 t - \sinh^2 t = 1,
$$

and $u(t)u(s) = u(t+s)$ by the addition formulas for the hyperbolic functions, so that branch is a copy of $\mathbb{R}$ and is the identity component of $G_{\mathbb{D}}$; the other branch is the negative of the first, and $G_{\mathbb{D}} \cong \mathbb{R} \times \mathbb{Z}/2\mathbb{Z}$. The matrix of multiplication is

$$
M(u(t)) = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}
\in SO(1,1),
$$

since $\det M = \cosh^2 t - \sinh^2 t = 1$ and the matrix preserves the form $x^2 - y^2$ of signature $(1,1)$. The one-parameter group $\{M(u(t))\}$ is the connected component of $SO(1,1)$, the hyperbolic rotation group, and $t$ is the rapidity: it is additive, but the parameter range is unbounded, and the group is non-compact.

**Orbits and fixed lines.** Multiplication by $u(t)$ preserves $x^2 - y^2$, so the orbit of a point with $x^2 - y^2 = r^2 \neq 0$ is the hyperbola $x^2 - y^2 = r^2$ within one of the four connected regions; the four null lines are the asymptotes. The two null lines are fixed: the idempotents

$$
e_+ = \tfrac{1}{2}(1 + j), \qquad e_- = \tfrac{1}{2}(1 - j)
$$

satisfy $u(t)e_+ = e^{t}e_+$ and $u(t)e_- = e^{-t}e_-$, so the lines $\mathbb{R}e_+$ and $\mathbb{R}e_-$ are fixed pointwise up to scaling. These are exactly the lines on which $N$ vanishes, and they are the null directions of the indefinite form.

## The Parabolic Case: The Dual Numbers

For $\sigma = 0$ the norm form is degenerate, $N = x^2$, and it vanishes on the whole line $x = 0$, which is the maximal ideal $(\varepsilon)$. The norm-one group consists of the elements with $x = \pm 1$, so it too has two branches, each a line. On the branch $x = 1$,

$$
u(t) = 1 + \varepsilon t, \qquad N(u(t)) = 1,
$$

and $u(t)u(s) = u(t+s)$ because $\varepsilon^2 = 0$; thus the identity component of $G_{\mathbb{D}'}$ is a copy of $\mathbb{R}$, and the second branch is $-(1 + \varepsilon t)$. The matrix of multiplication is

$$
M(u(t)) = \begin{pmatrix} 1 & 0 \\ t & 1 \end{pmatrix},
$$

a transvection, with $\det M = 1$. The one-parameter group of transvections is the parabolic rotation group, a copy of $(\mathbb{R},+)$; it is the degenerate limit of both the elliptic and the hyperbolic families as the quadratic form degenerates, and it is a unipotent group preserving the flag $0 \subset \mathbb{R}\varepsilon \subset \mathbb{D}'$.

The same one-parameter group is the shear group of the degenerate plane: the transvection $(x,y) \mapsto (x, tx+y)$ shears the second coordinate by an amount proportional to the first while fixing the first, exactly as the elliptic rotation mixes the two coordinates through a bounded periodic angle and the hyperbolic rotation mixes them through an unbounded parameter. The composition law is the distinguishing feature: the parameter is additive in all three cases, $u(t_1)u(t_2) = u(t_1 + t_2)$, and what separates the cases is the range over which the parameter runs — a circle of length $2\pi$ in the elliptic case, a line in the hyperbolic case, and a line of unipotent transformations in the parabolic case. It is that additive law, with the parameter range left unrestricted, that makes the shear the parabolic member of the trichotomy of angle-addition laws.

**Orbits and fixed lines.** Multiplication by $u(t)$ sends $(x,y)$ to $(x, tx + y)$; the orbit of a point with $x \neq 0$ is the horizontal line through it, and the orbit of a point of the axis $x = 0$ is the point itself. The line $\mathbb{R}\varepsilon$ is fixed pointwise, and it is precisely the degenerate direction of the form, namely the set where $N$ vanishes. There is no second fixed line, and the parameter is unbounded.

## The Three Together

The three cases differ in every feature that the quadratic form controls.

| | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ |
|---|---|---|---|
| generator square $\sigma$ | $-1$ | $+1$ | $0$ |
| norm form $N$ | $x^2+y^2$ | $x^2-y^2$ | $x^2$ |
| signature | $(2,0)$ definite | $(1,1)$ indefinite | $(1,0)$ degenerate |
| zero divisors | none | on $x=\pm y$ | on $x=0$ |
| $G_A = \{u : N(u)=1\}$ | $U(1)\cong SO(2)$, connected | two branches; identity component $\cong SO(1,1)_0$ | two branches; identity component the transvections |
| matrix | $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$ | $\begin{pmatrix} a & b \\ b & a\end{pmatrix}$ | $\begin{pmatrix} a & 0 \\ b & a\end{pmatrix}$ |
| orbit of a generic point | circle | hyperbola | horizontal line |
| fixed lines | none | two null lines | one null line |
| group | compact | non-compact | non-compact, unipotent |

The definite case gives a compact rotation group with no fixed direction and closed orbits; the indefinite case gives a non-compact group with two fixed null directions and open orbits; the degenerate case gives a unipotent group with one fixed null direction and orbits that are lines. In every case the fixed directions are the directions on which the norm form vanishes, and the rotation is norm-preserving by multiplicativity.

## The Classification of the Two-Dimensional Algebras

The three cases are not merely three examples; they are all the examples.

**Theorem (classification in dimension two).** Let $A$ be a two-dimensional commutative unital associative algebra over $\mathbb{R}$. Then $A$ is isomorphic to exactly one of $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$.

*Proof.* Write $A = \mathbb{R}\cdot 1 \oplus V$ with $V$ one-dimensional, and choose a generator $\omega$ spanning $V$. Then $\omega^2 = p\cdot 1 + c\,\omega$ for some $p, c \in \mathbb{R}$, so $A \cong \mathbb{R}[\omega]/(\omega^2 - p\omega - c)$ and $A$ is determined up to isomorphism by the polynomial $\omega^2 - p\omega - c$, hence by the sign of its discriminant $p^2 + 4c$. If $p^2 + 4c < 0$ the polynomial is irreducible over $\mathbb{R}$ and

$$
A \cong \mathbb{R}[\omega]/(\omega^2+1) = \mathbb{C};
$$

if $p^2+4c > 0$ the polynomial has two distinct real roots and $A \cong \mathbb{R}\times\mathbb{R} \cong \mathbb{D}$; if $p^2 + 4c = 0$ the polynomial is a square, $(\omega - p/2)^2 = 0$ after completing the square, so $A \cong \mathbb{R}[\omega]/(\omega^2) = \mathbb{D}'$. $\square$

The three kinds of rotation therefore exhaust the rotations implemented by multiplication in the plane, and the type of the rotation is the sign of the discriminant of the quadratic form: positive definite gives elliptic, indefinite gives hyperbolic, degenerate gives parabolic.

## Why Three Dimensions Force Non-Commutativity

The plane admits three multiplicative rotation theories; the next dimension does not admit any commutative one.

**Theorem (no commutative rotation theory in dimension three).** There is no three-dimensional commutative unital real division algebra. More generally, if $A$ is a finite-dimensional real algebra with a multiplicative norm form that is positive definite, then $\dim_\mathbb{R} A \in \{1, 2, 4, 8\}$, with the cases $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ (Hurwitz).

*Proof.* A commutative unital real algebra that is a division algebra is a field extension of $\mathbb{R}$ of finite degree equal to its dimension. Every finite field extension of $\mathbb{R}$ has degree at most $2$, because every real polynomial of odd degree has a real root, so every element of the extension has minimal polynomial of degree $1$ or $2$ and the only irreducible polynomials are the linear ones and the quadratics with negative discriminant; hence the degree is at most $2$. The Hurwitz statement is the classical theorem on composition algebras, valid without commutativity; the only positive-dimensional real composition algebras are $\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O}$. $\square$

So a commutative algebra cannot implement rotations in $\mathbb{R}^3$; the smallest algebra that can is the four-dimensional, non-commutative quaternion algebra $\mathbb{H}$. The rotations of $\mathbb{R}^3$ are obtained by letting the unit quaternions act on the imaginary subspace $\operatorname{Im}\mathbb{H} = \mathbb{R}^3$ by conjugation.

**Theorem (the quaternion rotation group).** For a unit quaternion $q$ the map

$$
\rho_q(p) = q\,p\,q^{-1}, \qquad p \in \operatorname{Im}\mathbb{H},
$$

is a rotation of $\operatorname{Im}\mathbb{H} \cong \mathbb{R}^3$, and $q \mapsto \rho_q$ is a surjective group homomorphism $S^3 \to SO(3)$ with kernel $\{\pm 1\}$; hence $SO(3) \cong S^3/\{\pm 1\}$.

*Proof.* Multiplication by a unit preserves the norm $N(p) = p\bar p$, so $\rho_q$ is norm-preserving; it fixes the real part, since it fixes the scalars, so it preserves $\operatorname{Im}\mathbb{H}$; and it is an isometry of a three-dimensional space, hence an orthogonal transformation. Its determinant is $+1$ because $q \mapsto \rho_q$ is continuous and $S^3$ is connected, the value at $q = 1$ being the identity. Surjectivity and the kernel are the standard facts of the quaternion representation of rotations. $\square$

The three two-dimensional theories thus sit at the bottom of a hierarchy: the commutative cases are exactly the two-dimensional composition algebras, and passing to three dimensions forces one to give up commutativity and to use the quaternion algebra, whose unit group double-covers the rotation group.

## Summary

The three two-dimensional commutative unital real algebras are $\mathbb{C} = \mathbb{R}[\omega]/(\omega^2+1)$, $\mathbb{D} = \mathbb{R}[\omega]/(\omega^2-1)$ and $\mathbb{D}' = \mathbb{R}[\omega]/(\omega^2)$, and the sign of $\omega^2$ selects the geometry. Multiplication by a unit $u = a + \omega b$ is the linear map with matrix $\begin{pmatrix} a & \sigma b \\ b & a\end{pmatrix}$, of determinant $N(u) = a^2 - \sigma b^2$, and the **norm form** is multiplicative; the **rotation group** $G_A = \{u : N(u)=1\}$ is therefore a group of norm-preserving transformations. For $\mathbb{C}$ the form is definite, $G_A \cong U(1) \cong SO(2)$ with the elliptic matrix $\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$, orbits circles and no fixed line. For $\mathbb{D}$ the form is indefinite of signature $(1,1)$, the identity component of $G_A$ is $\mathbb{R} \cong SO(1,1)_0$ with the hyperbolic matrix $\begin{pmatrix}\cosh t & \sinh t\\ \sinh t & \cosh t\end{pmatrix}$, orbits hyperbolas and the two null lines fixed. For $\mathbb{D}'$ the form is degenerate, the identity component of $G_A$ is $\mathbb{R}$ with the transvection $\begin{pmatrix}1&0\\t&1\end{pmatrix}$, the parabolic rotation, orbits horizontal lines and the single null line fixed. A two-dimensional commutative unital real algebra is one of the three, by the sign of the discriminant of its defining quadratic, so the three kinds of rotation are exhaustive.

Passing to dimension three is impossible in the commutative setting: there is no three-dimensional commutative real division algebra, and the Hurwitz theorem restricts positive-definite multiplicative norms to dimensions $1, 2, 4, 8$. The rotations of $\mathbb{R}^3$ are instead obtained from the non-commutative quaternions, acting by conjugation $\rho_q(p) = qpq^{-1}$ on the imaginary subspace, with $SO(3) \cong S^3/\{\pm 1\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\omega$ | Generator of a two-dimensional algebra, $\omega^2 = \sigma$ |
| $\sigma$ | $-1$ for $\mathbb{C}$, $+1$ for $\mathbb{D}$, $0$ for $\mathbb{D}'$ |
| $i, j, \varepsilon$ | Generators of $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ |
| $z = x+\omega y$ | General element |
| $L_u$ | Left multiplication by $u$ |
| $M(u) = \begin{pmatrix} a & \sigma b\\ b & a\end{pmatrix}$ | Matrix of $L_u$ in the basis $(1,\omega)$ |
| $N(x+\omega y) = x^2 - \sigma y^2$ | Norm form, multiplicative |
| $G_A = \{u : N(u)=1\}$ | Rotation group |
| $u(\theta), u(t)$ | Parametrisations by angle and by rapidity |
| $e_\pm = \tfrac{1}{2}(1\pm j)$ | Idempotents of $\mathbb{D}$, spanning the null lines |
| $SO(2), SO(1,1)$ | Elliptic and hyperbolic rotation groups |
| $(\mathbb{R},+)$ | Parabolic rotation group, the transvections and shears |
| $S^3 = \{q\in\mathbb{H} : N(q)=1\}$ | Unit quaternions |
| $\rho_q(p) = qpq^{-1}$ | Rotation of $\operatorname{Im}\mathbb{H}$ by a unit quaternion |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge, 1995), for the orthogonal and unitary groups attached to quadratic forms and the split cases.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the composition-algebra classification and the quaternion rotation group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2nd ed. 2001), for the split and degenerate geometries and their rotation groups.
- Israel M. Gelfand, Mikhail M. Kapranov and Andrei V. Zelevinsky, *Discriminants, Resultants and Multidimensional Determinants* (Birkhäuser, 1994), for the discriminant classification of low-dimensional algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the classification of the two-dimensional algebras.
