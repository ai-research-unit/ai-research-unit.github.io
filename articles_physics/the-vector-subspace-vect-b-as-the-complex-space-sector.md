# __The Vector Subspace $\mathrm{Vect}(\mathbb{B})$ as the Complex Space Sector__

## Introduction

This article is about the **vector subspace** $\mathrm{Vect}(\mathbb{B})$, the anti-fixed space of quaternion conjugation: the set of biquaternions with vanishing scalar part.

$\mathrm{Vect}(\mathbb{B})$ is spanned by the three vector units $e_1, e_2, e_3$ with complex coefficients, so its elements are the pure-vector biquaternions. It is six-dimensional over the reals but **three-dimensional over the complex numbers**, because multiplication by the scalar imaginary carries it into itself: it is a complex vector space, and this is what the name "complex space sector" records. It is not a subalgebra — the square of a vector unit is a scalar — but it **is** a Lie algebra, and in fact it is the algebra's derived subspace, spanned by all commutators. Its norm form is the complex quadratic form $z_1^2 + z_2^2 + z_3^2$, and it therefore has a complex null cone rather than a real one.

The article describes the subspace on its own terms: its definition and basis, its algebraic properties, the reading that gives it its name, its Lie-algebraic structure, and the physical objects it carries.

## Basic Definition and Properties

### Definition and Basis

The **vector subspace** of $\mathbb{B}$ is the set of elements with vanishing scalar part:

$$
\mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} \in \mathbb{B} : \mathrm{Sc}(\tilde{Q}) = 0\}.
$$

Since the quaternion basis separates the scalar direction $e_0$ from the three vector directions $e_k$, an element lies in the subspace if and only if its coefficient on $e_0$ vanishes. A natural basis is

$$
\{e_1,\; e_2,\; e_3,\; i\,e_1,\; i\,e_2,\; i\,e_3\},
$$

and a general element is

$$
\tilde{Q} = z_1\,e_1 + z_2\,e_2 + z_3\,e_3, \qquad z_k = q_k + i q'_k \in \mathbb{C}.
$$

As a real vector space $\mathrm{Vect}(\mathbb{B})$ has dimension $6$. Because each of the three directions carries a complex coefficient, it is more naturally read as a **complex** vector space with basis $\{e_1, e_2, e_3\}$ and complex dimension $3$. Multiplication by $i$ acts as the complex structure:

$$
i\,(z_1e_1 + z_2e_2 + z_3e_3) = (iz_1)e_1 + (iz_2)e_2 + (iz_3)e_3 \in \mathrm{Vect}(\mathbb{B}),
$$

so the subspace is closed under multiplication by the central scalar and is a $\mathbb{C}$-subspace, not merely an $\mathbb{R}$-subspace.

The parameter pattern carries six real parameters, the real and imaginary parts of the three complex coefficients of a general biquaternion on the vector directions, and the scalar coefficient is absent entirely. The vanishing of the scalar part is the defining condition:

$$
\tilde{Q} \in \mathrm{Vect}(\mathbb{B}) \iff \mathrm{Sc}(\tilde{Q}) = 0.
$$

### The Defining Involution

The subspace is the **anti-fixed space** of **quaternion conjugation** $\bar{\tilde{Q}}$, the map that fixes the unit and the scalar imaginary and negates the three vector units,

$$
e_0 \mapsto e_0, \qquad e_k \mapsto -e_k, \qquad i \mapsto i .
$$

It is an involution: $\overline{\bar{\tilde{Q}}} = \tilde{Q}$. Equivalently, the subspace is the kernel of the scalar part, $\mathrm{Sc}(\tilde{Q}) = 0$. Write the general biquaternion out in full, with the real and the imaginary part of each of its four coefficients,

$$
\tilde{Q} = (q_0 + iq'_0)\,e_0 + (q_1 + iq'_1)\,e_1 + (q_2 + iq'_2)\,e_2 + (q_3 + iq'_3)\,e_3, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The conjugation leaves every coefficient untouched and reverses the sign of each of the three vector units,

$$
\bar{\tilde{Q}} = (q_0 + iq'_0)\,e_0 - (q_1 + iq'_1)\,e_1 - (q_2 + iq'_2)\,e_2 - (q_3 + iq'_3)\,e_3 ,
$$

so that the scalar coefficient is untouched and every vector coefficient changes sign. Coordinate by coordinate,

| | $q_0$ | $q'_0$ | $q_1$ | $q'_1$ | $q_2$ | $q'_2$ | $q_3$ | $q'_3$ |
|---|---|---|---|---|---|---|---|---|
| image under $\bar{\cdot}$ | $q_0$ | $q'_0$ | $-q_1$ | $-q'_1$ | $-q_2$ | $-q'_2$ | $-q_3$ | $-q'_3$ |
| $\bar{\tilde{Q}} = -\tilde{Q}$ requires | $q_0 = 0$ | $q'_0 = 0$ | free | free | free | free | free | free |

**The anti-fixed space.** The two sides of $\bar{\tilde{Q}} = -\tilde{Q}$ must agree in each of the four units $e_0, e_1, e_2, e_3$, and within a unit they must agree separately in the real and the imaginary part. That is four complex conditions, hence eight real ones. The scalar unit gives

$$
q_0 + iq'_0 = -(q_0 + iq'_0) \iff q_0 + iq'_0 = 0 \iff q_0 = q'_0 = 0,
$$

killing both the real and the imaginary part of the scalar coefficient, while the condition from each of the three vector units is vacuous, $-(q_k + iq'_k) = -(q_k + iq'_k)$. The solutions are the elements with $q_0 = q'_0 = 0$, that is,

$$
\bar{\tilde{Q}} = -\tilde{Q} \iff \tilde{Q} = (q_1 + iq'_1)\,e_1 + (q_2 + iq'_2)\,e_2 + (q_3 + iq'_3)\,e_3 = z_1e_1 + z_2e_2 + z_3e_3 .
$$

**Conversely**, every element of this form is anti-fixed: its scalar coefficient vanishes, so the scalar term is absent from both sides, and each vector term is negated by the conjugation on the left and already carries the minus sign on the right,

$$
\bar{\tilde{Q}} = -(q_1 + iq'_1)\,e_1 - (q_2 + iq'_2)\,e_2 - (q_3 + iq'_3)\,e_3 = -\tilde{Q} .
$$

The two directions together say that the displayed set is *exactly* the anti-fixed space. The coordinates that survive are the six $q_k, q'_k$ of the vector part, which is the parametrisation recorded above, and the anti-fixed space is this six-dimensional real subspace, carved out of the eight real coordinates by the two $\mathbb{R}$-linear equations $q_0 = q'_0 = 0$ — equivalently, by the single complex equation $\mathrm{Sc}(\tilde{Q}) = 0$.

### Properties

**Not a subalgebra.** The square of a vector unit is a scalar,

$$
e_1^2 = e_2^2 = e_3^2 = -e_0,
$$

which lies outside the subspace. More generally the product of two pure-vector biquaternions has a scalar part equal to $-\mathbf{u}\cdot\mathbf{w}$ (with signs fixed by the conventions), so the subspace is not closed under multiplication. It is closed under multiplication by $i$, and it is closed under the commutator, but not under the product.

**Complex quadratic norm form.** Quaternion conjugation negates the vector part, so for a pure vector $\bar{\tilde{Q}} = -\tilde{Q}$ and the norm form is minus the square:

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = -\tilde{Q}^2 = (z_1^2 + z_2^2 + z_3^2)\,e_0 .
$$

This is the **complex orthogonal form** in three variables, not the Hermitian form $|z_1|^2 + |z_2|^2 + |z_3|^2$: it is $\mathbb{C}$-linear in each argument, and it takes complex values. It vanishes on the complex cone

$$
z_1^2 + z_2^2 + z_3^2 = 0,
$$

a cone of real dimension $4$ cut out of a space of real dimension $6$. The subspace therefore has zero divisors, and a nonzero element with vanishing norm can be written down at once: since $1^2 + i^2 = 0$, the element $e_1 + ie_2$ satisfies

$$
(e_1 + ie_2)^2 = e_1^2 + i(e_1e_2 + e_2e_1) + i^2e_2^2 = -e_0 + ie_3 - ie_3 + e_0 = 0,
$$

so it is nilpotent, and a fortiori a zero divisor. The nilpotent directions of the subspace are precisely the null directions of the complex form.

**No Hermitian structure.** Because the norm form is complex rather than Hermitian, the subspace carries no positive definite form of its own. Its directions are not divided into timelike and spacelike classes; instead they are divided into null and non-null with respect to a complex form, and the non-null directions have no ordering.

## Physical Meaning

The name records the defining property of the subspace: it is a **complex** vector space, not merely a real one.

**Three complex dimensions.** Multiplication by the central scalar imaginary carries $\mathrm{Vect}(\mathbb{B})$ into itself, so the six real dimensions organise into three complex ones, with basis $e_1, e_2, e_3$.

**The complex structure is physical.** The complex structure is not decorative. It is the Hodge dual on the field strength, the electric–magnetic duality rotation, and the algebraic device that combines the rotation generators and the boost generators into a single complex three-dimensional Lie algebra. A complex three-vector in this subspace is simultaneously a field configuration and a generator, which is exactly the role the sector plays in the physics of spin one.

## Advanced Algebraic Properties

**A Lie subalgebra.** The commutator of two pure vectors is again a pure vector, and the brackets close:

$$
[e_1, e_2] = 2e_3, \qquad [e_1, ie_2] = 2i\,e_3, \qquad [ie_1, ie_2] = -2e_3,
$$

together with the analogues obtained by cyclic permutation of $1,2,3$, and the vanishing brackets $[e_1, ie_1] = 0$. The three families — vector–vector, vector–imaginary vector, and imaginary vector–imaginary vector — all land back in the subspace, so $\mathrm{Vect}(\mathbb{B})$ is a Lie algebra of real dimension $6$ and complex dimension $3$ under the commutator bracket.

**The derived subspace.** The commutator is always traceless, so

$$
[\mathbb{B}, \mathbb{B}] \subseteq \mathrm{Vect}(\mathbb{B}),
$$

and in fact the two spaces coincide: the commutators of the basis elements span a space of real dimension $6$, which is the dimension of the subspace. So the vector subspace is exactly the derived subspace of $\mathbb{B}$ — the smallest subspace containing all commutators. This gives an intrinsic characterization of the subspace that does not mention the vector units at all: it is the set of elements that can be written as $[\tilde{Q},\tilde{Y}]$, equivalently the elements with vanishing scalar part.

**The Lorentz algebra.** The six real dimensions of the subspace also carry the generators of the Lorentz group: the three real vector units $e_1, e_2, e_3$ generate rotations, and the three imaginary vector units $ie_1, ie_2, ie_3$ generate boosts. Their brackets, listed above, are the brackets of the Lorentz algebra $\mathfrak{so}(1,3)$, written in the complex form in which rotations and boosts are the two real three-dimensional parts of a single complex three-dimensional algebra. The same object — a complex three-vector — therefore carries both the field strength and the generators of the transformations that rotate it, which is the reason the field strength is naturally a representation of the Lorentz group of a kind that a four-vector is not.

**The Hodge dual as the complex structure.** On the field-strength elements, the Hodge dual acts as multiplication by $-i$,

$$
\star\tilde{F} = -i\,\tilde{F},
$$

in the real-time convention where $\star^2 = -1$. The complex structure $i$ of the sector is thus not a formal device but the Hodge duality operation, and the real and imaginary parts of a complex vector in the subspace are an electric–magnetic pair related by duality. The duality rotation $\mathbf{V} \mapsto e^{-i\theta}\mathbf{V}$, which rotates the electric into the magnetic field, is multiplication by a unit complex number inside the same sector.

## Examples

Two physical objects live in the vector subspace, and they are of a different kind from the four-vectors.

**The field strength.** The electromagnetic field strength is an antisymmetric rank-two tensor, not a four-vector. Its six independent components, three electric and three magnetic, assemble into the **Riemann–Silberstein vector**

$$
\mathbf{V} = \mathbf{E} + ic\,\mathbf{B},
$$

whose three components are complex. The corresponding biquaternion is a pure-vector element of $\mathrm{Vect}(\mathbb{B})$, so the field strength lives in the sector, not in the four-vector sector. The complex coefficients are not a convenience: they are the three complex dimensions of the subspace, and the electric and magnetic parts are the real and imaginary parts of one complex object.

The complex null cone of the norm form has a physical reading in this picture. Its elements are the null field configurations, and the element $e_1 + ie_2$, whose square vanishes, is the algebraic prototype: the norm $\mathbf{V}\cdot\mathbf{V} = z_1^2 + z_2^2 + z_3^2$ is the complex combination of the two classical invariants of the electromagnetic field, $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ and $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$, so the vanishing of the norm form is the joint vanishing of both field invariants. Because the form is complex, its zero set is four-real-dimensional, which is why the null configurations are not a single cone of directions but a richer structure.

## Summary

The vector subspace $\mathrm{Vect}(\mathbb{B})$ is the set of biquaternions with vanishing scalar part, spanned over $\mathbb{R}$ by $e_1, e_2, e_3, ie_1, ie_2, ie_3$ and over $\mathbb{C}$ by $e_1, e_2, e_3$. It is a six-dimensional real space and a three-dimensional complex space.

It is not a subalgebra — the square of a vector unit is $-e_0$ — but it is a Lie subalgebra under the commutator, and in fact it is exactly the derived subspace $[\mathbb{B},\mathbb{B}]$, equivalently the set of elements with vanishing scalar part.

Its norm form is the complex quadratic form $z_1^2 + z_2^2 + z_3^2$, which is not Hermitian and not real-valued; it vanishes on a complex null cone of real dimension $4$, so the subspace contains zero divisors, the nilpotent element $e_1 + ie_2$ being the prototype. There is no positive definite or indefinite real form, and hence no timelike/spacelike division of directions.

Physically the subspace carries the **field strength** — the Riemann–Silberstein complex three-vector $\mathbf{E} + ic\mathbf{B}$ — and the **Lorentz generators**, the three rotations $e_k$ and the three boosts $ie_k$. The complex structure is the Hodge dual and the electric–magnetic duality rotation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathrm{Vect}(\mathbb{B})$ | Vector subspace (complex space sector): elements with vanishing scalar part |
| $\{e_1,e_2,e_3,ie_1,ie_2,ie_3\}$ | Real basis; complex dimension $3$, real dimension $6$ |
| $z_k = q_k + iq'_k$ | Complex coefficients on $e_k$; six real parameters $q_k, q'_k$ |
| $\mathrm{Sc}(\tilde{Q}) = 0$ | Defining condition: the scalar part vanishes |
| $e_k^2 = -e_0$ | Products leave the subspace: it is not a subalgebra |
| $[e_1,e_2] = 2e_3$, $[e_1,ie_2] = 2ie_3$, $[ie_1,ie_2] = -2e_3$ | Brackets close: a Lie subalgebra |
| $[\mathbb{B},\mathbb{B}] = \mathrm{Vect}(\mathbb{B})$ | The subspace is the derived subspace |
| $N(\tilde{Q}) = (z_1^2+z_2^2+z_3^2)e_0$ | Complex quadratic norm form; not Hermitian |
| $z_1^2+z_2^2+z_3^2 = 0$ | Complex null cone; real dimension $4$; zero divisors |
| $(e_1+ie_2)^2 = 0$ | Nilpotent element; prototype of the null cone |
| $\mathbf{V} = \mathbf{E} + ic\,\mathbf{B}$ | Riemann–Silberstein vector; the field strength |
| $\star\tilde{F} = -i\tilde{F}$ | Hodge dual as the complex structure |
| $e_k$, $ie_k$ | Rotation and boost generators of the Lorentz algebra |

## Further Reading

- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung" (1907), for the complex vector form of the electromagnetic field.
- Carsten A. Mead, *Collective Electrodynamics* (MIT, 2000), for a modern account of the Riemann–Silberstein vector.
- *Conventions in the Biquaternion Universe* and *Relations Between Subspaces*, the companion articles, for the notation and for the place of $\mathrm{Vect}(\mathbb{B})$ among the six subspaces.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for bivectors, the Hodge dual, and the Lorentz algebra in the spacetime algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the complexification of $\mathfrak{su}(2)$.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field strength.
