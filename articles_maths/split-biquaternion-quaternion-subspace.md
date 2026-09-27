
# __Split-Biquaternion Quaternion Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and four of the resulting fixed spaces are its distinguished real subspaces. This article treats the **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the fixed space of split complex conjugation: its definition, its basis, its algebra structure, the restriction of the norm form to it, its roots of $-1$ and its commutator, the action of the four involutions upon it, and its intersections with the other subspaces. The companions are *Split-Biquaternion Split-Complex Subspace*, *Split-Biquaternion Hermitian Subspace* and *Split-Biquaternion Anti-Hermitian Subspace*; the comparative tables are in *Split-Biquaternion Relations Between Subspaces* and *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article, and the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra. Throughout, elements are written $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (split complex), ${}^{\dagger} = {}^{*}\circ\bar{\cdot}$ and ${}^{\flat} = -{}^{\dagger}$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$.

## Definition and Basis

**Definition.** The **quaternion subspace** is the fixed space of split complex conjugation,

$$
\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^{*} = \tilde{Q} \right\},
$$

where split complex conjugation conjugates each coefficient, $Q_\mu \mapsto Q_\mu^{*} = q_\mu - j q'_\mu$.

Since ${}^{*}$ is an involution, it has eigenvalues $\pm 1$ and $\mathbb{H}_{\mathbb{D}}$ is the direct sum of its fixed space and its anti-fixed space, the anti-fixed space being $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$.

### The Condition in Coordinates

Comparing the two sides of $\tilde{Q}^{*} = \tilde{Q}$ coefficient by coefficient, $Q_\mu^{*} = Q_\mu$ means $q_\mu - j q'_\mu = q_\mu + j q'_\mu$, that is $q'_\mu = 0$ for each $\mu$. The subspace is therefore the set of elements with **real coefficients**,

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

### Basis and Dimension

**Proposition.** The quaternion subspace is a real vector space of dimension $4$, with basis $e_0, e_1, e_2, e_3$. In real coordinates it is the coordinate plane $q'_0 = q'_1 = q'_2 = q'_3 = 0$.

**Proof.** The condition leaves the four real parameters $q_0, q_1, q_2, q_3$ free and removes the four split-imaginary parameters $q'_\mu$. The basis elements are linearly independent and span the set. $\square$

The subspace is a **real form** of the algebra in the sense that $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$: adjoining the central split complex scalars to the real quaternions recovers the whole algebra.

## Algebra Structure

### It Is a Subalgebra

**Proposition.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, and the map $\tilde{Q} \mapsto \tilde{Q}$ identifies it with the real quaternion algebra $\mathbb{H}$.

**Proof.** The product of two elements with real coefficients again has real coefficients, because the structure constants of the quaternion basis are real; the unit $e_0$ lies in the subspace. The identification with $\mathbb{H}$ on the basis $e_0, e_1, e_2, e_3$ is the identity map, and the multiplication is the quaternion multiplication. $\square$

It is one of exactly two of the four distinguished subspaces that are subalgebras, the other being the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$; and unlike that one it is **noncommutative**.

### It Is a Division Algebra

**Theorem.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a division algebra: every nonzero element is a unit, and there are no zero divisors in the subspace.

**Proof.** On the subspace the norm form is $N(\tilde{Q}) = \sum_\mu q_\mu^2$, a strictly positive real number for $\tilde{Q} \neq 0$; a nonzero real norm is a unit of $\mathbb{D}$, so by the invertibility criterion the element is a unit, with inverse $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$. A zero divisor would have to be a nonzero non-unit, which does not exist. $\square$

So although the ambient algebra $\mathbb{H}_{\mathbb{D}}$ has many zero divisors, the quaternion subspace contains none of them; the zero divisors all have at least one vanishing idempotent component and hence cannot have all coefficients real and nonzero in the required way. This is developed in *Split-Biquaternion Zero Divisors*.

### The Centre

The centre of $\mathbb{H}_{\mathbb{D}}$ is the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, and its intersection with the quaternion subspace is the real line:

$$
\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{R}.
$$

Every split biquaternion is uniquely $\tilde{Q} = \tilde{Q}_r + j\tilde{Q}_i$ with $\tilde{Q}_r, \tilde{Q}_i \in \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, so

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j\,\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} , \qquad \mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \otimes_{\mathbb{R}} \mathbb{D} .
$$

### The Imaginary Units and the Roots of Minus One

The elements $e_1, e_2, e_3$ lie in the subspace and satisfy $e_k^2 = -1$. More generally, the **roots of $-1$** in the subspace are the pure quaternions of unit length,

$$
\xi = q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_1^2 + q_2^2 + q_3^2 = 1,
$$

which is a two-sphere $S^2$. The identity $e_1 e_2 = e_3$ and its cyclic permutations hold inside the subspace, so the subspace contains the full quaternion multiplication of its imaginary units. The roots of $-1$ in the whole algebra $\mathbb{H}_{\mathbb{D}}$ form the larger set $S^2 \times S^2$ described in *Split-Biquaternion Roots of Minus One*; the subspace contributes the diagonal of that product.

### The Commutator

**Proposition.** For $\tilde{Q} = q_0 + \mathbf{u}$ and $\tilde{R} = r_0 + \mathbf{v}$ in the subspace, with $\mathbf{u}, \mathbf{v}$ pure,

$$
[\tilde{Q}, \tilde{R}] = \tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2\, \mathbf{u} \times \mathbf{v},
$$

which is a pure quaternion in the subspace. The commutator subalgebra is the three-dimensional space of pure real quaternions,

$$
[\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}] = \mathbb{R} e_1 \oplus \mathbb{R} e_2 \oplus \mathbb{R} e_3.
$$

**Proof.** The scalar parts cancel, and the remaining terms give $\mathbf{u}\mathbf{v} - \mathbf{v}\mathbf{u} = 2\,\mathbf{u}\times\mathbf{v}$, the standard quaternion identity. For the second statement, $\mathbf{u}\times\mathbf{v}$ ranges over all of $\mathbb{R}^3$ as $\mathbf{u}, \mathbf{v}$ vary, and the pure quaternions are three-dimensional. $\square$

Under the commutator the subspace is the Lie algebra $\mathfrak{so}(3)$ — the three-dimensional simple compact Lie algebra — a fact made precise in *Split-Biquaternion Exponential and Lie Group Structure*.

## The Norm Form

**Proposition.** On the quaternion subspace the norm form is the ordinary quaternion norm,

$$
N(\tilde{Q}) = \sum_{\mu=0}^{3} q_\mu^2 = |\tilde{Q}|^2 \geq 0,
$$

which is real and **positive definite**, vanishing only at $\tilde{Q} = 0$.

**Proof.** With $Q_\mu = q_\mu$ real, $N(\tilde{Q}) = \sum_\mu Q_\mu^2 = \sum_\mu q_\mu^2$. $\square$

Among the four distinguished subspaces, the quaternion subspace is the one on which the norm form is positive definite; on the split complex subspace it is split-complex-valued and degenerate, and on the two sectors $\mathbb{M}_\pm$ it is positive definite, of signature $(4,0)$, the indefinite form on the sectors being the Hermitian form.

### Units and Idempotents

**Theorem.** For $\tilde{Q}$ in the quaternion subspace the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q} \neq 0$. The inverse is $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$.

**Proof.** The norm form is positive definite, so $N(\tilde{Q}) = 0$ only at the origin; the inverse formula is the standard quaternion inverse and is verified directly. $\square$

The **idempotents** of the subspace are the solutions of $\tilde{Q}^2 = \tilde{Q}$. Since the subspace is a division algebra, the only idempotents are $0$ and $1$: they are the trivial idempotents, and they lie in the centre. The four idempotents of $\mathbb{H}_{\mathbb{D}}$ are $0, \tilde\Pi_+, \tilde\Pi_-, 1$, and the two nontrivial ones lie in the split complex subspace, not here.

## The Image in the Two Halves

Under the idempotent-decomposition isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, an element with real coefficients has $A = \tilde{Q}$, $B = 0$ in the split complex decomposition $\tilde{Q} = A + jB$, so

$$
\varphi(\tilde{Q}) = (\tilde{Q}, \tilde{Q}), \qquad \tilde{Q} \in \mathbb{H}.
$$

The image of the quaternion subspace is therefore the **diagonal** $\{(h, h) : h \in \mathbb{H}\}$, a subalgebra isomorphic to $\mathbb{H}$: under $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$, the quaternion subspace is the diagonal copy of $\mathbb{H}$.

## The Four Involutions on It

Each of the four involutions preserves the condition of real coefficients, so the subspace is invariant under all four. In the basis $e_0, e_1, e_2, e_3$ their matrices are diagonal:

| involution | action | matrix |
|---|---|---|
| $\bar{\cdot}$ | quaternion conjugation | $\operatorname{diag}(1, -1, -1, -1)$ |
| ${}^{*}$ | identity | $\operatorname{diag}(1, 1, 1, 1)$ |
| ${}^{\dagger}$ | quaternion conjugation | $\operatorname{diag}(1, -1, -1, -1)$ |
| ${}^{\flat}$ | negative quaternion conjugation | $\operatorname{diag}(-1, 1, 1, 1)$ |

Split complex conjugation fixes the subspace pointwise, since it is the defining involution. Quaternion conjugation and Hermitian conjugation agree there — because $\dagger = {}^{*}\circ\bar{\cdot}$ and ${}^{*}$ acts as the identity — and both act as the quaternion conjugation $q_0 + \mathbf{u} \mapsto q_0 - \mathbf{u}$. Anti-Hermitian conjugation is the negative of that. So of the four involutions two act trivially (on the subspace) and the other two act as the quaternion conjugation, whose fixed space inside the subspace is the real line $\mathbb{R}$.

## Relations to the Other Subspaces

The intersections of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ with the other distinguished subspaces are, with dimensions:

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+$ | $\mathbb{R}$ | $1$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-$ | $\mathbb{R} e_1 \oplus \mathbb{R} e_2 \oplus \mathbb{R} e_3$ | $3$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathbb{R} e_1 \oplus \mathbb{R} e_2 \oplus \mathbb{R} e_3$ | $3$ |

The subspace meets the split complex subspace and the Hermitian subspace each in the real line $\mathbb{R}$, the line of real scalars; it meets the anti-Hermitian subspace and the vector subspace each in the three-dimensional space of pure real quaternions. Consequently the quaternion subspace and the anti-Hermitian subspace together span a subspace of dimension $4 + 4 - 3 = 5$, not the whole algebra, while the quaternion and split complex subspaces together span $4 + 2 - 1 = 5$. The full intersection and sum tables are in *Split-Biquaternion Relations Between Subspaces*.

## Summary

The quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed space of split complex conjugation, the set of elements with real coefficients; it is a real vector space of dimension $4$ with basis $e_0, e_1, e_2, e_3$, a real form of the algebra. It is a subalgebra isomorphic to the real quaternion algebra $\mathbb{H}$, noncommutative and a **division algebra**: it contains no zero divisor, every nonzero element is a unit, and the norm form restricts to the positive definite quaternion norm $N = \sum_\mu q_\mu^2$, so $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$. Its roots of $-1$ are the unit pure quaternions $S^2$, it contains the quaternion imaginary units with $e_1 e_2 = e_3$, and its commutator is $2\,\mathbf{u}\times\mathbf{v}$, a pure quaternion, so the commutator subalgebra is the three-dimensional space of pure quaternions and the subspace is the Lie algebra $\mathfrak{so}(3)$ under the bracket. The only idempotents it contains are $0$ and $1$; the nontrivial idempotents of the algebra lie in the split complex subspace. Its image under $\varphi$ is the diagonal copy of $\mathbb{H}$ in $\mathbb{H} \oplus \mathbb{H}$. Of the four involutions, split complex conjugation fixes it pointwise and quaternion and Hermitian conjugations both act as the quaternion conjugation; the subspace meets the split complex and Hermitian subspaces in $\mathbb{R}$ and the anti-Hermitian and vector subspaces in the space of pure real quaternions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Element of the quaternion subspace, $q_\mu \in \mathbb{R}$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace, fixed space of ${}^{*}$ |
| $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Anti-fixed space of ${}^{*}$ |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | The four conjugations |
| $N(\tilde{Q}) = \sum_\mu q_\mu^2$ | Positive definite quaternion norm on the subspace |
| $[\tilde{Q}, \tilde{R}] = 2\,\mathbf{u} \times \mathbf{v}$ | Commutator, a pure quaternion |
| $S^2$ | The roots of $-1$ within the subspace, unit pure quaternions |
| $\varphi(\tilde{Q}) = (\tilde{Q}, \tilde{Q})$ | Diagonal image in $\mathbb{H} \oplus \mathbb{H}$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | The other distinguished subspaces |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion algebra and the identity $[\mathbf{u}, \mathbf{v}] = 2\,\mathbf{u}\times\mathbf{v}$.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for real forms and the division property of the quaternions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the quaternion subspace of the split biquaternion algebra and the roots of $-1$.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lie algebra structure of the pure quaternions and the two-sphere of imaginary units.
