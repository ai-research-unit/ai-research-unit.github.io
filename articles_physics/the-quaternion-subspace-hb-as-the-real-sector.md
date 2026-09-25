# __The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$ as the Real Sector__

## Introduction

This article is about the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, the fixed space of complex conjugation.

$\mathbb{H}_{\mathbb{B}}$ is the image of the quaternion algebra itself inside $\mathbb{B}$. It is spanned by the four basis elements with real coefficients, so a general element of it is a quaternion in the ordinary sense. Its defining feature is that it is a **subalgebra**, and in fact a **division algebra**: every nonzero element has an inverse, and there are no zero divisors. It is also the sector in which the scalar imaginary $i$ plays no role at all, and this is what the name "real sector" records — in both of the senses that the word "real" carries here, real coefficients and fixed points of the real conjugation.

The article describes the subspace on its own terms: its basis and parameters, its algebraic properties, the reading that gives it its name, its unit group and Lie algebra, and the rotation rotors it contains.

## Basic Definition and Properties

### Definition and Basis

Complex conjugation is the antilinear map that fixes the quaternion units and negates the scalar imaginary,

$$
e_k^* = e_k, \qquad i^* = -i .
$$

The **quaternion subspace** is its fixed-point set:

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^* = \tilde{Q}\}.
$$

Explicitly, an element belongs to it if and only if all four coefficients in the quaternion basis are real:

$$
\tilde{Q} = q_0\,e_0 + q_1\,e_1 + q_2\,e_2 + q_3\,e_3 = (ct')\,e_0 + x\,e_1 + y\,e_2 + z\,e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

A natural basis is

$$
\{e_0,\; e_1,\; e_2,\; e_3\},
$$

and as a real vector space $\mathbb{H}_{\mathbb{B}}$ has dimension $4$. Equivalently, since $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the subspace is the image of the inclusion $\mathbb{H} \hookrightarrow \mathbb{B}$, $h \mapsto 1\otimes h$.

The parameter pattern is the simplest possible: **all four** coefficients are real, and none carries the scalar imaginary. Each of the four complex coefficients $Q_\mu = q_\mu + iq'_\mu$ of a general biquaternion contributes its real part, and the imaginary parts are set to zero.

### The Defining Involution

The subspace is the fixed space of **complex conjugation** $\tilde{Q}^*$, the antilinear map that fixes the quaternion units and negates the scalar imaginary, $e_\mu^* = e_\mu$ and $i^* = -i$. It is an involution: $(\tilde{Q}^*)^* = \tilde{Q}$. Write the general biquaternion out in full, with the real and the imaginary part of each of its four coefficients,

$$
\tilde{Q} = (q_0 + iq'_0)\,e_0 + (q_1 + iq'_1)\,e_1 + (q_2 + iq'_2)\,e_2 + (q_3 + iq'_3)\,e_3, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

Complex conjugation replaces $i$ by $-i$ in every coefficient and leaves all four units fixed, so it acts coefficient by coefficient,

$$
\tilde{Q}^* = (q_0 - iq'_0)\,e_0 + (q_1 - iq'_1)\,e_1 + (q_2 - iq'_2)\,e_2 + (q_3 - iq'_3)\,e_3 ,
$$

so that every imaginary part changes sign and every real part is left alone. Coordinate by coordinate,

| | $q_0$ | $q'_0$ | $q_1$ | $q'_1$ | $q_2$ | $q'_2$ | $q_3$ | $q'_3$ |
|---|---|---|---|---|---|---|---|---|
| image under $*$ | $q_0$ | $-q'_0$ | $q_1$ | $-q'_1$ | $q_2$ | $-q'_2$ | $q_3$ | $-q'_3$ |
| $\tilde{Q}^* = \tilde{Q}$ requires | free | $q'_0 = 0$ | free | $q'_1 = 0$ | free | $q'_2 = 0$ | free | $q'_3 = 0$ |

**The fixed space.** The two sides of $\tilde{Q}^* = \tilde{Q}$ must agree in each of the four units $e_0, e_1, e_2, e_3$, and within a unit they must agree separately in the real and the imaginary part. That is four complex conditions, hence eight real ones, and they read

$$
q_0 - iq'_0 = q_0 + iq'_0 \iff q'_0 = 0, \qquad
q_k - iq'_k = q_k + iq'_k \iff q'_k = 0 \qquad (k = 1, 2, 3),
$$

one for each of the four coefficients. The solutions are the elements with $q'_0 = q'_1 = q'_2 = q'_3 = 0$, that is,

$$
\tilde{Q}^* = \tilde{Q} \iff \tilde{Q} = q_0\,e_0 + q_1\,e_1 + q_2\,e_2 + q_3\,e_3 .
$$

**Conversely**, every element of this form is fixed: its four coefficients $q_0, q_1, q_2, q_3$ are real, so replacing $i$ by $-i$ in them changes nothing, and each quaternion unit is fixed by the conjugation, hence $\tilde{Q}^* = \tilde{Q}$ term by term. The two directions together say that the displayed set is *exactly* the fixed space. The coordinates that survive are the four $q_0, q_1, q_2, q_3$, which is the parametrisation recorded above: the fixed space is exactly the set of elements whose four coefficients are real, carved out of the eight real coordinates by the four equations $q'_\mu = 0$.

### Properties

**Subalgebra.** The subspace is closed under multiplication: the product of two elements of $\mathbb{H}_{\mathbb{B}}$ is again in $\mathbb{H}_{\mathbb{B}}$, because complex conjugation is a homomorphism on products and fixes each factor. Its multiplication table is that of the quaternions:

| product | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

The diagonal is $-e_0$ for the three vector units, $e_k^2 = -e_0$, and the off-diagonal entries are antisymmetric, $e_je_k = -e_ke_j$ for $j \neq k$, with the cyclic products $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$. The subspace is therefore non-commutative.

**Division algebra.** The norm form restricted to the subspace is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = q_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

a **positive definite** quadratic form of signature $(4,0)$. Since $N(\tilde{Q}) = 0$ forces $\tilde{Q} = 0$, every nonzero element is invertible, with

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})},
$$

and there are no zero divisors: a product $\tilde{Q}\tilde{R}$ can vanish only if one factor does. The vanishing of the norm form here cuts out only the origin: the subspace has no light cone.

**Frobenius.** The quaternion algebra is the only four-dimensional real division algebra up to isomorphism. The subspace is therefore not merely *a* division algebra: as a real algebra it is *the* four-dimensional one.

**Hermitian parts.** Under Hermitian conjugation, which composes quaternion conjugation with complex conjugation, the unit is fixed and the three vector units change sign,

$$
e_0^\dagger = e_0, \qquad e_k^\dagger = -e_k \quad (k = 1,2,3).
$$

So the scalar direction of the subspace is Hermitian and the three vector directions are anti-Hermitian. This is the algebraic statement that a real scalar is Hermitian while a real spatial direction is not.

**Not closed under the central scalar.** Multiplication by $i$ takes the subspace out of itself: the product $i\tilde{Q}$ of $i$ with a nonzero element $\tilde{Q}$ of the subspace lies outside it. The condition of belonging to $\mathbb{H}_{\mathbb{B}}$ is therefore $\mathbb{R}$-linear and not $\mathbb{C}$-linear, which is exactly what one expects of a sector defined by a conjugation.

## Physical Meaning

The name "real sector" is earned in two ways at once, and it is worth separating them.

**Real coefficients.** Every element of $\mathbb{H}_{\mathbb{B}}$ has four real coefficients in the quaternion basis. No coefficient carries the scalar imaginary $i$. The sector is therefore the part of the algebra that can be written without ever invoking the complex unit — which is precisely the image of the real quaternion algebra $\mathbb{H}$ under the inclusion $\mathbb{H} \hookrightarrow \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

**Real conjugation.** The subspace is the fixed-point set of complex conjugation. In the algebra of the framework, complex conjugation is the conjugation that plays the role of the "real structure", and its fixed points are what the framework calls real. The two readings coincide because complex conjugation acts by negating $i$: an element with real coefficients is exactly an element it fixes.

The physical reading follows from the first of these. In the $ict$ convention the time component of a four-vector is imaginary, $ict$, and it is the imaginary unit that produces the Lorentzian signature $(3,1)$. Inside $\mathbb{H}_{\mathbb{B}}$ that unit is not available, so the norm form is the positive definite form of signature $(4,0)$, the geometry has no light cone, and no direction is singled out as time. This is a **Euclidean** four-dimensional geometry, and it is exactly what the Wick rotation produces: relabelling the imaginary time coefficient $ict$ as a real one turns the material four-vector space into $\mathbb{H}_{\mathbb{B}}$, with the Lorentzian signature traded for a Euclidean one. In this precise sense the real sector is the Euclidean, or Wick-rotated, read of the four-vector space, and the division property of the quaternions is the algebraic reason the Euclidean picture has no null directions.

## Advanced Algebraic Properties

**The unit group.** The elements of unit norm form, $N(\tilde{Q}) = e_0$, are the **unit quaternions**. In coordinates they form the unit sphere

$$
q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1,
$$

a three-dimensional sphere. That is precisely the group $SU(2)$, so the unit group of $\mathbb{H}_{\mathbb{B}}$ is the sphere $S^3$, isomorphic to $SU(2)$.

**The Lie algebra.** The three pure vector units $e_1, e_2, e_3$ are the infinitesimal generators of these rotations. They are anti-Hermitian and satisfy $e_k^2 = -e_0$, and their commutators close on themselves,

$$
[e_1, e_2] = 2e_3, \qquad [e_2, e_3] = 2e_1, \qquad [e_3, e_1] = 2e_2,
$$

which is the rotation algebra $\mathfrak{su}(2)$ up to the factor $2$. So the subspace carries both the finite rotations and their Lie algebra, entirely within itself.

## Examples

**The rotation rotors.** The unit quaternions act on the subspace itself by conjugation, $\tilde{Q} \mapsto \tilde{U}\tilde{Q}\tilde{U}^{-1}$, and this action preserves the norm form. Because the group is $SU(2)$, the action on the three-dimensional space of pure vectors is a rotation: the unit quaternions are the **rotation rotors**, and they furnish the double cover of the rotation group. Concretely, a rotation through an angle $\theta$ about the unit vector $\hat{\mathbf{n}}$ is effected by

$$
\tilde{U} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{\mathbf{n}}\cdot\mathbf{e},
$$

a unit quaternion whose scalar part is the cosine of the half-angle. The appearance of the half-angle is the familiar sign ambiguity of the spinor cover, and it is a property of the sector: the rotors form a sphere, not a projective space.

## Summary

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation, a four-dimensional real subspace of $\mathbb{B}$ spanned by $e_0, e_1, e_2, e_3$ with real coefficients. It is a subalgebra, and as a real algebra it is the unique four-dimensional division algebra. Its norm form is positive definite of signature $(4,0)$; numerically it is the sum of squares $q_0^2 + q_1^2 + q_2^2 + q_3^2$, which never vanishes on a nonzero element. Every nonzero element is invertible, with $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$, and there are no zero divisors and no light cone.

Its unit group is the sphere $S^3 \cong SU(2)$, the group of rotation rotors, which acts on the subspace by conjugation; the pure vector units $e_1, e_2, e_3$ are the rotation generators, closing under commutation as $\mathfrak{su}(2)$.

The physical reading of the sector is the Euclidean one: with the scalar imaginary unavailable inside it, the four-dimensional geometry it carries has no distinguished time direction, and the Wick rotation is exactly the relabelling that turns the Lorentzian four-vector space into this sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace (real sector): fixed points of complex conjugation; all four coefficients real |
| $q_0, q_1, q_2, q_3$ | Real parameters of an element of $\mathbb{H}_{\mathbb{B}}$, on $e_0, e_1, e_2, e_3$ |
| $(ct')\,e_0 + x\,e_1 + y\,e_2 + z\,e_3$ | The same element in physical coordinates; $q_0 = ct'$ and $(q_1, q_2, q_3) = (x, y, z)$ |
| $e_k^2 = -e_0$, $e_1e_2 = e_3$ | Quaternion multiplication rules |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = q_0^2 + q_1^2 + q_2^2 + q_3^2$ | Norm form; positive definite, signature $(4,0)$ |
| $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ | Inverse; exists for every nonzero element |
| $S^3 \cong SU(2)$ | Unit group; the rotation rotors |
| $\tilde{U} = \cos(\theta/2) + \sin(\theta/2)\hat{\mathbf{n}}\cdot\mathbf{e}$ | Rotation rotor through $\theta$ about $\hat{\mathbf{n}}$ |
| $\mathfrak{su}(2)$ | Lie algebra of the pure vector units $e_k$ |
| $\mathbb{R}$-linear but not $\mathbb{C}$-linear | The subspace is carried out of itself by multiplication by $i$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original algebra.
- Ferdinand Georg Frobenius, "Über lineare Substitutionen und bilineare Formen" (1878), for the classification of real division algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion algebra.
- *Conventions in the Biquaternion Universe* and *Relations Between Subspaces*, the companion articles, for the notation and for the place of $\mathbb{H}_{\mathbb{B}}$ among the six subspaces.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for rotors and the double cover of the rotation group.
- Gian Carlo Wick, "Properties of Bethe-Salpeter Wave Functions" (1954), for the rotation to imaginary time.
