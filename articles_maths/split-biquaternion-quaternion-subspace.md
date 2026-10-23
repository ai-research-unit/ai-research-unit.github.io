
# __Split-Biquaternion Quaternion Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and four of the resulting fixed spaces are its distinguished real subspaces. This article treats the **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the fixed space of split complex conjugation: its definition, its basis, its algebra structure, the restriction of the split-biquaternion norm to it, its roots of $-1$ and its commutator, the action of the four involutions upon it, and its intersections with the other subspaces. The companions are *Split-Biquaternion Split-Complex Subspace*, *Split-Biquaternion Hermitian Subspace* and *Split-Biquaternion Anti-Hermitian Subspace*; the comparative tables are in *Split-Biquaternion Relations Between Subspaces* and *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article, and the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra. Throughout, elements are written $\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and ${}^{\flat} = -{}^{*}$. The split-biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$.

## Definition and Basis

**Definition.** The **quaternion subspace** is the fixed space of split complex conjugation,

$$
\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \bar{\tilde{Q}} = \tilde{Q} \right\},
$$

where split complex conjugation conjugates each coefficient, $Q_\mu \mapsto Q_{\bar{\mu}} = q_\mu - j q'_\mu$.

Since $\bar{\cdot}$ is an involution, it has eigenvalues $\pm 1$ and $\mathbb{H}_{\mathbb{D}}$ is the direct sum of its fixed space and its anti-fixed space, the anti-fixed space being $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$.

### The Condition in Coordinates

Comparing the two sides of $\bar{\tilde{Q}} = \tilde{Q}$ coefficient by coefficient, $Q_{\bar{\mu}} = Q_\mu$ means $q_\mu - j q'_\mu = q_\mu + j q'_\mu$, that is $q'_\mu = 0$ for each $\mu$. The subspace is therefore the set of elements with **real coefficients**,

$$
\tilde{Q} = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_\mu \in \mathbb{R}.
$$

### Basis and Dimension

**Proposition.** The quaternion subspace is a real vector space of dimension $4$, with basis $e_t, \vec e_x, \vec e_y, \vec e_z$. In real coordinates it is the coordinate plane $q'_t = q'_x = q'_y = q'_z = 0$.

**Proof.** The condition leaves the four real parameters $q_t, q_x, q_y, q_z$ free and removes the four split-imaginary parameters $q'_\mu$. The basis elements are linearly independent and span the set.

The subspace is a **real form** of the algebra in the sense that $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$: adjoining the central split complex scalars to the real quaternions recovers the whole algebra.

## Algebra Structure

### It Is a Subalgebra

**Proposition.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, and the map $\tilde{Q} \mapsto \tilde{Q}$ identifies it with the real quaternion algebra $\mathbb{H}$.

**Proof.** The product of two elements with real coefficients again has real coefficients, because the structure constants of the quaternion basis are real; the unit $e_t$ lies in the subspace. The identification with $\mathbb{H}$ on the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ is the identity map, and the multiplication is the quaternion multiplication.

It is one of exactly two of the four distinguished subspaces that are subalgebras, the other being the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$; and unlike that one it is **noncommutative**.

### It Is a Division Algebra

**Theorem.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a division algebra: every nonzero element is a unit, and there are no zero divisors in the subspace.

**Proof.** On the subspace the split-biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$, a strictly positive real number for $\tilde{Q} \neq 0$; a nonzero real norm is a unit of $\mathbb{D}$, so by the invertibility criterion the element is a unit, with inverse $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$. A zero divisor would have to be a nonzero non-unit, which does not exist.

So although the ambient algebra $\mathbb{H}_{\mathbb{D}}$ has many zero divisors, the quaternion subspace contains none of them; the zero divisors all have at least one vanishing idempotent component and hence cannot have all coefficients real and nonzero in the required way. This is developed in *Split-Biquaternion Zero Divisors*.

### The Centre

The centre of $\mathbb{H}_{\mathbb{D}}$ is the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, and its intersection with the quaternion subspace is the real line:

$$
\boxed{\;
\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{R}
\;}.
$$

Every split biquaternion is uniquely $\tilde{Q} = \tilde q + j\tilde q'$ with $\tilde q, \tilde q' \in \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, so

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j\,\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} , \qquad \mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \otimes_{\mathbb{R}} \mathbb{D} .
$$

### The Imaginary Units and the Roots of Minus One

The elements $\vec e_x, \vec e_y, \vec e_z$ lie in the subspace and satisfy $\vec e_\mu^2 = -1$. More generally, the **roots of $-1$** in the subspace are the pure quaternions of unit length,

$$
\xi = q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_x^2 + q_y^2 + q_z^2 = 1,
$$

which is a two-sphere $S^2$. The identity $\vec e_x \vec e_y = \vec e_z$ and its cyclic permutations hold inside the subspace, so the subspace contains the full quaternion multiplication of its imaginary units. The roots of $-1$ in the whole algebra $\mathbb{H}_{\mathbb{D}}$ form the larger set $S^2 \times S^2$ described in *Split-Biquaternion Roots of Minus One*; the subspace contributes the diagonal of that product.

### The Commutator

**Proposition.** For $\tilde{Q}_1 = q_t + \vec q$ and $\tilde{Q}_2 = q_{2t} + \vec v$ in the subspace, with $\vec q, \vec v$ pure,

$$
\boxed{\;
[\tilde{Q}_1, \tilde{Q}_2] = \tilde{Q}_1\tilde{Q}_2 - \tilde{Q}_2\tilde{Q}_1 = 2\, \vec q \times \vec v
\;},
$$

which is a pure quaternion in the subspace. The commutator subalgebra is the three-dimensional space of pure real quaternions,

$$
[\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}] = \mathbb{R} \vec e_x \oplus \mathbb{R} \vec e_y \oplus \mathbb{R} \vec e_z.
$$

**Proof.** The scalar parts cancel, and the remaining terms give $\vec q\vec v - \vec v\vec q = 2\,\vec q\times\vec v$, the standard quaternion identity. For the second statement, $\vec q\times\vec v$ ranges over all of $\mathbb{R}^3$ as $\vec q, \vec v$ vary, and the pure quaternions are three-dimensional.

Under the commutator the subspace is the Lie algebra $\mathrm{SO}(3)$ — the three-dimensional simple compact Lie algebra — a fact made precise in *Split-Biquaternion Exponential and Lie Group Structure*.

## The Split-Biquaternion Norm

**Proposition.** On the quaternion subspace the split-biquaternion norm is the ordinary quaternion norm,

$$
\boxed{\;
\langle\tilde{Q}\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}} q_\mu^2 = |\tilde{Q}|^2 \geq 0
\;},
$$

which is real and **positive definite**, vanishing only at $\tilde{Q} = 0$.

**Proof.** With $Q_\mu = q_\mu$ real, $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2 = \sum_\mu q_\mu^2$.

Among the four distinguished subspaces, the quaternion subspace is the one on which the split-biquaternion norm is positive definite; on the split complex subspace it is split-complex-valued and degenerate, and on the two sectors $\mathbb{M}_\pm$ it is positive definite, of signature $(4,0)$, the indefinite form on the sectors being the Hermitian form.

### Units and Idempotents

**Theorem.** For $\tilde{Q}$ in the quaternion subspace the following are equivalent: $\tilde{Q}$ is a unit; $\langle\tilde{Q}\rangle_{\natural} \neq 0$; $\tilde{Q} \neq 0$. The inverse is $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$.

**Proof.** The split-biquaternion norm is positive definite, so $\langle\tilde{Q}\rangle_{\natural} = 0$ only at the origin; the inverse formula is the standard quaternion inverse and is verified directly.

The **idempotents** of the subspace are the solutions of $\tilde{Q}^2 = \tilde{Q}$. Since the subspace is a division algebra, the only idempotents are $0$ and $1$: they are the trivial idempotents, and they lie in the centre. The four idempotents of $\mathbb{H}_{\mathbb{D}}$ are $0, \tilde\Pi_1, \tilde\Pi_2, 1$, and the two nontrivial ones lie in the split complex subspace, not here.

## The Image in the Two Halves

Under the idempotent-decomposition isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, an element with real coefficients has $\tilde q = \tilde{Q}$, $\tilde q' = 0$ in the decomposition $\tilde{Q} = \tilde q + j\tilde q'$, so

$$
\varphi(\tilde{Q}) = (\tilde{Q}, \tilde{Q}), \qquad \tilde{Q} \in \mathbb{H}.
$$

The image of the quaternion subspace is therefore the **diagonal** $\{(h, h) : h \in \mathbb{H}\}$, a subalgebra isomorphic to $\mathbb{H}$: under $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$, the quaternion subspace is the diagonal copy of $\mathbb{H}$.

## The Four Involutions on It

Each of the four involutions preserves the condition of real coefficients, so the subspace is invariant under all four. In the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ their matrices are diagonal:

| involution | action | matrix |
|---|---|---|
| ${}^{\natural}$ | quaternion conjugation | $\operatorname{diag}(1, -1, -1, -1)$ |
| $\bar{\cdot}$ | identity | $\operatorname{diag}(1, 1, 1, 1)$ |
| ${}^{*}$ | quaternion conjugation | $\operatorname{diag}(1, -1, -1, -1)$ |
| ${}^{\flat}$ | negative quaternion conjugation | $\operatorname{diag}(-1, 1, 1, 1)$ |

Split complex conjugation fixes the subspace pointwise, since it is the defining involution. Quaternion conjugation and Hermitian conjugation agree there — because ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and $\bar{\cdot}$ acts as the identity — and both act as the quaternion conjugation $q_t + \vec q \mapsto q_t - \vec q$. Anti-Hermitian conjugation is the negative of that. So of the four involutions two act trivially (on the subspace) and the other two act as the quaternion conjugation, whose fixed space inside the subspace is the real line $\mathbb{R}$.

## Relations to the Other Subspaces

The intersections of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ with the other distinguished subspaces are, with dimensions:

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+$ | $\mathbb{R}$ | $1$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-$ | $\mathbb{R} \vec e_x \oplus \mathbb{R} \vec e_y \oplus \mathbb{R} \vec e_z$ | $3$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathbb{R} \vec e_x \oplus \mathbb{R} \vec e_y \oplus \mathbb{R} \vec e_z$ | $3$ |

The subspace meets the split complex subspace and the Hermitian subspace each in the real line $\mathbb{R}$, the line of real scalars; it meets the anti-Hermitian subspace and the vector subspace each in the three-dimensional space of pure real quaternions. Consequently the quaternion subspace and the anti-Hermitian subspace together span a subspace of dimension $4 + 4 - 3 = 5$, not the whole algebra, while the quaternion and split complex subspaces together span $4 + 2 - 1 = 5$. The full intersection and sum tables are in *Split-Biquaternion Relations Between Subspaces*.

## The Analysis on the Quaternion Subspace

The quaternion subspace is a copy of the real quaternion algebra $\mathbb{H}$, a division algebra, so the function theory it carries is the one-variable quaternion analysis of *Quaternion Analysis*: a function of the quaternion variable $\tilde q = q_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ is regular when it satisfies the Cauchy–Riemann equation of *Quaternion Analysis*, and the harmonic functions are the solutions of the four-dimensional Laplace equation $\sum_{\mu\in\{t,x,y,z\}}\partial^2/\partial q_\mu^2 f = 0$. Embedded in $\mathbb{H}_{\mathbb{D}}$, the quaternion subspace inherits the restriction of the ambient Cauchy–Riemann operator of *Split-Biquaternion Analysis*, and on the quaternion subspace that operator is the quaternion Cauchy–Riemann operator above. This is the one subspace of the four on which the split-biquaternion norm is positive definite and the analytic theory is elliptic, exactly because the subspace is a division algebra.

## The Geometry of the Quaternion Subspace

As the fixed space of split complex conjugation, the quaternion subspace is the real form of the algebra, the axis of that involution, and geometrically the invariant four-plane of the corresponding linear involution of $\mathbb{R}^8$. Its own geometry is that of the quaternion algebra: the level set of unit norm is the round three-sphere $S^3$, of constant curvature one, the pure imaginary directions are the sphere $S^2$ of roots of $-1$ of *Quaternion Algebra*, and the motions it carries are the left and right multiplications $\tilde q\mapsto u \tilde q v$ with $u, v$ unit quaternions, giving the compact group $S^3\times S^3$ and the rotation group $SO(4)$ on the subspace. Both the Euclidean form and the Hermitian scalar form restrict to the same positive definite form of signature $(4,0)$, so the quaternion subspace is the definite core of the algebra.

## Summary

The quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed space of split complex conjugation, the set of elements with real coefficients; it is a real vector space of dimension $4$ with basis $e_t, \vec e_x, \vec e_y, \vec e_z$, a real form of the algebra. It is a subalgebra isomorphic to the real quaternion algebra $\mathbb{H}$, noncommutative and a **division algebra**: it contains no zero divisor, every nonzero element is a unit, and the split-biquaternion norm restricts to the positive definite quaternion norm $N = \sum_\mu q_\mu^2$, so $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$. Its roots of $-1$ are the unit pure quaternions $S^2$, it contains the quaternion imaginary units with $\vec e_x \vec e_y = \vec e_z$, and its commutator is $2\,\vec q\times\vec v$, a pure quaternion, so the commutator subalgebra is the three-dimensional space of pure quaternions and the subspace is the Lie algebra $\mathrm{SO}(3)$ under the bracket. The only idempotents it contains are $0$ and $1$; the nontrivial idempotents of the algebra lie in the split complex subspace. Its image under $\varphi$ is the diagonal copy of $\mathbb{H}$ in $\mathbb{H} \oplus \mathbb{H}$. Of the four involutions, split complex conjugation fixes it pointwise and quaternion and Hermitian conjugations both act as the quaternion conjugation; the subspace meets the split complex and Hermitian subspaces in $\mathbb{R}$ and the anti-Hermitian and vector subspaces in the space of pure real quaternions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | Element of the quaternion subspace, $q_\mu \in \mathbb{R}$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace, fixed space of $\bar{\cdot}$ |
| $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Anti-fixed space of $\bar{\cdot}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ | Positive definite quaternion norm on the subspace |
| $[\tilde{Q}_1, \tilde{Q}_2] = 2\,\vec q \times \vec v$ | Commutator, a pure quaternion |
| $S^2$ | The roots of $-1$ within the subspace, unit pure quaternions |
| $\varphi(\tilde{Q}) = (\tilde{Q}, \tilde{Q})$ | Diagonal image in $\mathbb{H} \oplus \mathbb{H}$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | The other distinguished subspaces |
| $\sum_\mu \partial^2/\partial q_\mu^2$ | Quaternion Laplace operator on the subspace |
| $SO(4)$, $S^3\times S^3$ | Rotations and unit group acting on the quaternion subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion algebra and the identity $[\vec q, \vec v] = 2\,\vec q\times\vec v$.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for real forms and the division property of the quaternions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the quaternion subspace of the split biquaternion algebra and the roots of $-1$.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lie algebra structure of the pure quaternions and the two-sphere of imaginary units.
