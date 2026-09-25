# __The Anti-Quaternion Subspace $i\mathbb{H}_{\mathbb{B}}$ as the Imaginary Sector__

## Introduction

This article is about the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, the anti-fixed space of complex conjugation.

$i\mathbb{H}_{\mathbb{B}}$ is the image of the quaternion algebra multiplied by the scalar imaginary. Its elements are the products $i\tilde{Q}$ with $\tilde{Q}$ a real quaternion, so every coefficient is imaginary and no coefficient is real. It is **not** a subalgebra, and its norm form is **negative definite**, negative in every direction. Multiplication of its elements does not close inside it: the product of two of its elements is an element with real coefficients.

The article describes the subspace on its own terms: its basis and parameters, its algebraic behaviour under multiplication and commutation, the reading that gives it its name, its Lie-algebraic structure, and the boost generators and complex-time axis it contains.

## Basic Definition and Properties

### Definition and Basis

Complex conjugation is the antilinear map that fixes the quaternion units and negates the scalar imaginary, $e_k^* = e_k$ and $i^* = -i$. The **anti-quaternion subspace** is its anti-fixed-point set:

$$
i\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^* = -\tilde{Q}\}.
$$

Explicitly, an element belongs to it if and only if all four coefficients in the quaternion basis are purely imaginary:

$$
\tilde{Q} = iq'_0\,e_0 + iq'_1\,e_1 + iq'_2\,e_2 + iq'_3\,e_3 = ict\,e_0 + ix'\,e_1 + iy'\,e_2 + iz'\,e_3, \qquad q'_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

A natural basis is

$$
\{i\,e_0,\; i\,e_1,\; i\,e_2,\; i\,e_3\},
$$

and as a real vector space $i\mathbb{H}_{\mathbb{B}}$ has dimension $4$. Equivalently, it is the set of products $i\tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$, so it is the image of the real quaternions under multiplication by the central scalar imaginary.

The parameter pattern is again the simplest possible, but inverted relative to the quaternion subspace: **all four** coefficients are imaginary, none is real. Each of the four complex coefficients $Q_\mu = q_\mu + iq'_\mu$ of a general biquaternion contributes its imaginary part, and the real parts are set to zero.

### The Defining Involution

The subspace is the **anti-fixed space** of **complex conjugation** $\tilde{Q}^*$: the elements with $\tilde{Q}^* = -\tilde{Q}$. Complex conjugation is the antilinear map that fixes the quaternion units and negates the scalar imaginary, $e_\mu^* = e_\mu$ and $i^* = -i$; it is an involution, $(\tilde{Q}^*)^* = \tilde{Q}$. Write the general biquaternion out in full, with the real and the imaginary part of each of its four coefficients,

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
| $\tilde{Q}^* = -\tilde{Q}$ requires | $q_0 = 0$ | free | $q_1 = 0$ | free | $q_2 = 0$ | free | $q_3 = 0$ | free |

**The anti-fixed space.** The two sides of $\tilde{Q}^* = -\tilde{Q}$ must agree in each of the four units $e_0, e_1, e_2, e_3$, and within a unit they must agree separately in the real and the imaginary part. That is four complex conditions, hence eight real ones, and they read

$$
q_0 - iq'_0 = -q_0 - iq'_0 \iff q_0 = 0, \qquad
q_k - iq'_k = -q_k - iq'_k \iff q_k = 0 \qquad (k = 1, 2, 3),
$$

one for each of the four coefficients. The solutions are the elements with $q_0 = q_1 = q_2 = q_3 = 0$, that is,

$$
\tilde{Q}^* = -\tilde{Q} \iff \tilde{Q} = iq'_0\,e_0 + iq'_1\,e_1 + iq'_2\,e_2 + iq'_3\,e_3 .
$$

**Conversely**, every element of this form is anti-fixed: its four coefficients $iq'_0, iq'_1, iq'_2, iq'_3$ are purely imaginary, so replacing $i$ by $-i$ in them negates each coefficient while leaving the quaternion units fixed, hence $\tilde{Q}^* = -\tilde{Q}$ term by term. The two directions together say that the displayed set is *exactly* the anti-fixed space. The coordinates that survive are the four $q'_0, q'_1, q'_2, q'_3$, which is the parametrisation recorded above: the anti-fixed space is this four-dimensional real subspace, carved out of the eight real coordinates by the four $\mathbb{R}$-linear equations $q_\mu = 0$ — the real part of every complex coefficient is killed, leaving the coefficients purely imaginary.

### Properties

**Not a subalgebra.** The product of two elements of $i\mathbb{H}_{\mathbb{B}}$ does **not** lie in $i\mathbb{H}_{\mathbb{B}}$. Two elementary cases show why. The square of an imaginary vector unit is real,

$$
(i\,e_1)^2 = (i\,e_2)^2 = (i\,e_3)^2 = +e_0,
$$

since the square of $i$ cancels the square of $e_k$; and a product of two distinct imaginary vector units is also real,

$$
(i\,e_1)(i\,e_2) = -e_3 .
$$

Both results are elements of the quaternion subspace, where all coefficients are real. In general,

$$
i\mathbb{H}_{\mathbb{B}} \cdot i\mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}},
$$

because $i^2 = -e_0$ is central and $\mathbb{H}_{\mathbb{B}}$ is a subalgebra. The subspace is therefore not closed under multiplication: it behaves like the imaginary part of a complex structure, whose products return to the real part.

**Negative definite norm form.** The norm form restricted to the subspace is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = (iq'_0)^2 + (iq'_1)^2 + (iq'_2)^2 + (iq'_3)^2 = -(q'^2_0 + q'^2_1 + q'^2_2 + q'^2_3),
$$

a **negative definite** quadratic form of signature $(0,4)$. Every direction is negative, and the form vanishes only at the origin.

**No zero divisors.** Because the form vanishes only at the origin, every nonzero element of the subspace is invertible in $\mathbb{B}$, with

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})},
$$

and no product $\tilde{Q}\tilde{R}$ of nonzero elements of the subspace vanishes. So the subspace inherits the division property of the quaternions even though it is not itself closed under multiplication: it is a *set* of invertible elements, not an algebra.

**Hermitian parts.** Under Hermitian conjugation the imaginary scalar unit is anti-Hermitian and the imaginary vector units are Hermitian,

$$
(i\,e_0)^\dagger = -i\,e_0, \qquad (i\,e_k)^\dagger = +i\,e_k \quad (k = 1,2,3),
$$

since conjugation composes quaternion conjugation, which fixes $ie_0$ and negates $ie_k$, with complex conjugation, which negates both. The assignment is the reverse of the one on the unit: here the imaginary scalar unit is anti-Hermitian and the imaginary vector units are Hermitian.

## Physical Meaning

The name is earned by a parameter pattern and by a conjugation.

**Imaginary coefficients.** Every element of $i\mathbb{H}_{\mathbb{B}}$ has four purely imaginary coefficients in the quaternion basis. It is precisely the part of the algebra that cannot be written without the scalar imaginary $i$: the product $i\tilde{Q}$ with $\tilde{Q}$ a real quaternion.

**Anti-fixed points.** The subspace is the anti-fixed-point set of complex conjugation, $\tilde{Q}^* = -\tilde{Q}$. Complex conjugation negates the imaginary unit, so the elements it reverses are exactly the elements proportional to $i$.

The physical reading follows from the negative definiteness. A quadratic form that is negative in every direction describes a geometry with no null directions and no light cone, and all of whose directions have the same character. Relabelling the imaginary time coefficient of the material four-vector space as a real one turns the Lorentzian signature $(3,1)$ into a Euclidean one, and the anti-quaternion subspace is the device the framework uses to carry the imaginary coefficients in that relabelled description. The absence of null directions is the algebraic reason there is no light cone in the Euclidean reading, just as the presence of null directions in the material sector is the reason there is one in the Lorentzian reading.

## Advanced Algebraic Properties

**Not a Lie subalgebra.** The commutator of two elements of $i\mathbb{H}_{\mathbb{B}}$ leaves the subspace. For example

$$
[i\,e_1, i\,e_2] = -2e_3,
$$

which is again real. So the anti-quaternion subspace is closed neither under products nor under commutators. Its bracket structure nevertheless closes on the whole algebra: the commutators of the imaginary vector units reproduce the rotation algebra, $[ie_1, ie_2] = -2e_3$ and cyclically.

**The Lorentz algebra.** The rotation generators of $\mathfrak{so}(1,3)$ are the pure vector units $e_1, e_2, e_3$; the **boost generators** are the imaginary vector units $i e_1, i e_2, i e_3$, which are exactly the three vector directions of $i\mathbb{H}_{\mathbb{B}}$. Their commutators reproduce the algebra, $[ie_1, ie_2] = -2e_3$ and cyclically, mixing the two families as the Lorentz algebra requires.

**Generators versus transformations.** It is worth distinguishing the generators from the transformations they generate, because the distinction is exactly the statement that $i\mathbb{H}_{\mathbb{B}}$ is not closed under exponentiation. Exponentiating the generator $i\psi\,\hat{\mathbf{u}}\cdot\mathbf{e}/2$ gives

$$
\exp\Big(\frac{i\psi}{2}\hat{\mathbf{u}}\cdot\mathbf{e}\Big) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}\cdot\mathbf{e},
$$

a **finite boost**, whose scalar part is real. A finite boost therefore has a real scalar coefficient and does not lie in $i\mathbb{H}_{\mathbb{B}}$: the subspace contains the infinitesimal generators of the boosts, and the boosts themselves are obtained by leaving it. The rapidity $\psi$ is the parameter along the boost direction, and the hyperbolic functions appear instead of the trigonometric ones because the corresponding directions of the norm form are negative.

## Examples

Two families of objects live in $i\mathbb{H}_{\mathbb{B}}$, and both are central to relativistic physics.

**The boost generators.** The **boost generators** of the Lorentz algebra are the imaginary vector units

$$
i\,e_1, \qquad i\,e_2, \qquad i\,e_3 .
$$

These are exactly the three vector directions of $i\mathbb{H}_{\mathbb{B}}$.

**The complex-time axis.** The imaginary scalar unit $ie_0$ is a basis element of $i\mathbb{H}_{\mathbb{B}}$ on its own, and it is the direction of the complex time coordinate: in the $ict$ convention the biquaternionic gradient begins with $e_0\partial_{ict}$, whose time direction is carried by $e_0$ with the imaginary unit in the coefficient. So the temporal axis of the $ict$ convention is the scalar direction of this subspace.

The two families together give the reading of $i\mathbb{H}_{\mathbb{B}}$ as the sector of imaginary scalars and imaginary vectors: the complex-time axis, and the boost generators that act on it.

## Summary

The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed-point set of complex conjugation, a four-dimensional real subspace of $\mathbb{B}$ spanned by $ie_0, ie_1, ie_2, ie_3$ with real coefficients, all of whose coefficients in the quaternion basis are purely imaginary. It is the image of the quaternion subspace under multiplication by the central scalar imaginary, and it shares with it only the origin.

It is neither a subalgebra nor a Lie subalgebra: the product of two of its elements, and the commutator of two of its elements, both have real coefficients and so lie outside it. Its norm form is negative definite of signature $(0,4)$, so it contains no zero divisors and every nonzero element of it is invertible, even though it is not closed under multiplication.

Physically it is the home of the **boost generators** $ie_1, ie_2, ie_3$ and of the complex-time axis $ie_0$. The generators lie in the subspace; the finite boosts do not, since exponentiation produces a real scalar part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $i\mathbb{H}_{\mathbb{B}}$ | Anti-quaternion subspace (imaginary sector): anti-fixed points of complex conjugation; all four coefficients purely imaginary |
| $q'_0, q'_1, q'_2, q'_3$ | Real parameters of an element, on $ie_0, ie_1, ie_2, ie_3$ |
| $ict\,e_0 + ix'\,e_1 + iy'\,e_2 + iz'\,e_3$ | The same element in physical coordinates; $q'_0 = ct$ and $(q'_1, q'_2, q'_3) = (x', y', z')$ |
| $(ie_k)^2 = +e_0$, $(ie_1)(ie_2) = -e_3$ | Products leave the subspace: $i\mathbb{H}_{\mathbb{B}} \cdot i\mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}}$ |
| $[ie_1, ie_2] = -2e_3$ | Commutators also leave the subspace |
| $N(\tilde{Q}) = -(q'^2_0 + q'^2_1 + q'^2_2 + q'^2_3)$ | Norm form; negative definite, signature $(0,4)$ |
| $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ | Inverse; exists for every nonzero element |
| $ie_1, ie_2, ie_3$ | Boost generators of the Lorentz algebra |
| $ie_0$ | Complex-time axis of the $ict$ convention |
| $\cosh(\psi/2) + i\sinh(\psi/2)\hat{\mathbf{u}}\cdot\mathbf{e}$ | Finite boost; has a real scalar part, so it is not in the subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion algebra, its complexification, and the Lorentz algebra.
- *Conventions in the Biquaternion Universe* and *Relations Between Subspaces*, the companion articles, for the notation and for the place of $i\mathbb{H}_{\mathbb{B}}$ among the six subspaces.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for boost generators and rotors in the spacetime algebra.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the Lorentz group and its generators.
- Gian Carlo Wick, "Properties of Bethe-Salpeter Wave Functions" (1954), for the rotation to imaginary time.
