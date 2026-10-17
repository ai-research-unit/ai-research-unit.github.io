
# __Split-Quaternion Scalar and Vector Subspaces__

## Introduction

The conjugation of the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is an involutive anti-automorphism, and an involution splits the algebra into its $+1$ and $-1$ eigenspaces. This article studies the two resulting subspaces: the **scalar subspace** $S$, the fixed space of the conjugation, and the **vector subspace** $V$, its anti-fixed space. Together they give the scalar–vector decomposition

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V,
$$

which is the coarsest decomposition of the algebra and the source of nearly every other structure in the category.

The article establishes the definitions and a basis for each subspace; shows that the two descriptions of $S$ and $V$ — as eigenspaces of the conjugation and as the scalar line and the span of the vector units — coincide; examines the algebra and module structure, in particular the failure of $V$ to be a subalgebra and its structure as a Lie algebra under the commutator; restricts the split-quaternion norm to each subspace and identifies the Minkowski form of signature $(2,1)$ on $V$; gives the matrix images of both; follows the three involutions through them; and records their relations with the remaining distinguished subspaces. It closes with worked examples.

**Conventions.** The algebra is $\mathbb{H}_{\mathrm{s}}$, with basis $1, \vec e_x, \vec e_y, \vec e_z$, the relations $\vec e_x^2 = -e_t$, $\vec e_y^2 = +e_t$, $\vec e_z = \vec e_x \vec e_y$ and $\vec e_x \vec e_y = -\vec e_y \vec e_x$, and a general element $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$. The conjugation is $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$, the split-quaternion norm is $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = q_t^2 + q_x^2 - q_y^2 - q_z^2$ with polarisation $\langle\cdot,\cdot\rangle_{\natural}$, and the principal involution $\alpha$ and the reversal $\rho$ are as in *Split-Quaternion Algebra*. The split-complex subalgebras are $\mathbb{D}_2 = \operatorname{span}\{1,\vec e_y\}$ and $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$.

## Definition and Basis

**Definition.** The **scalar subspace** and the **vector subspace** of $\mathbb{H}_{\mathrm{s}}$ are

$$
S = \mathbb{R}\cdot 1, \qquad V = \operatorname{span}\{\vec e_x, \vec e_y, \vec e_z\}.
$$

Every element has a unique expansion $\tilde q = q_t + \vec v$ with $q_t \in S$ and $\vec v \in V$; the projection onto the first summand is the scalar part, $\operatorname{Sc}(\tilde q) = q_t$, and the projection onto the second is the vector part, $\operatorname{Vec}(\tilde q) = \vec v = q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$.

**Proposition.** $S$ has real dimension $1$, with basis $\{1\}$; $V$ has real dimension $3$, with basis $\{\vec e_x, \vec e_y, \vec e_z\}$; and $S \cap V = \{0\}$, so that $\mathbb{H}_{\mathrm{s}} = S \oplus V$ with $\dim_{\mathbb{R}}\mathbb{H}_{\mathrm{s}} = 1 + 3 = 4$.

**Proof.** The four basis elements $1, \vec e_x, \vec e_y, \vec e_z$ are linearly independent over $\mathbb{R}$ by the definition of the algebra, so $\{1\}$ is a basis of $S$ and $\{\vec e_x,\vec e_y,\vec e_z\}$ is a basis of $V$; an element of $S \cap V$ is a multiple of $1$ with zero vector part, hence zero.

## The Two Descriptions Coincide

The scalar and vector subspaces are exactly the eigenspaces of the conjugation.

**Proposition.** For every $\tilde q \in \mathbb{H}_{\mathrm{s}}$, the conjugation satisfies $\tilde{q}^{\natural} = \tilde q$ if and only if $\tilde q \in S$, and $\tilde{q}^{\natural} = -\tilde q$ if and only if $\tilde q \in V$. Hence the scalar–vector decomposition is the eigenspace decomposition

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V, \qquad S = \{\tilde q : \tilde{q}^{\natural} = \tilde q\}, \qquad V = \{\tilde q : \tilde{q}^{\natural} = -\tilde q\}.
$$

**Proof.** Since $\bar{1} = 1$ and $\vec e_\mu^{\natural} = -\vec e_\mu$, the conjugation acts as $+1$ on $S$ and as $-1$ on $V$; conversely, writing $\tilde q = q_t + \vec v$, the condition $\tilde{q}^{\natural} = \tilde q$ reads $-2\vec v = 0$, i.e. $\vec v = 0$, and the condition $\tilde{q}^{\natural} = -\tilde q$ reads $2q_t = 0$, i.e. $q_t = 0$.

The scalar subspace is also the **centre** of the algebra. An element $\tilde q$ commutes with every element if and only if $\vec v = 0$: commuting with $\vec e_x$ and $\vec e_y$ gives $\vec v \vec e_x = \vec e_x \vec v$ and $\vec v \vec e_y = \vec e_y \vec v$, which force $q_y = q_z = 0$ and $q_x = 0$ respectively, so $\tilde q = q_t$ is scalar. Hence

$$
Z(\mathbb{H}_{\mathrm{s}}) = S = \mathbb{R}\cdot 1 .
$$

The centre is therefore a field, namely $\mathbb{R}$, and $S$ is the only commutative two-sided piece of the algebra. This is developed in *Split-Quaternion Algebra*, §*The Centre and Simplicity*.

## Algebra and Module Structure

**The scalar subspace.** $S$ is a subalgebra, isomorphic to $\mathbb{R}$ by $q_t \mapsto q_t$, and its product is $q_{1t} \cdot q_{2t} = q_{1t} q_{2t}$. Because it is the centre, $S$ multiplies into every subspace without sign change: $q_t \tilde q = \tilde q q_t$ for all $\tilde q$, and multiplication by a scalar is scalar extension.

**The vector subspace is not a subalgebra.** The square of a vector leaves $V$: $\vec e_x^2 = -e_t$ and $\vec e_y^2 = +e_t$ are scalars, and $\vec e_z^2 = +e_t$. In general, for $\vec q, \vec q_1 \in V$ the product splits as

$$
\vec q\vec q_1 = -B(\vec q, \vec q_1) \cdot 1 + \tfrac{1}{2}[\vec q, \vec q_1],
$$

with scalar part $-B(\vec q,\vec q_1)$ and the remainder $\tfrac{1}{2}[\vec q,\vec q_1] \in V$; for instance $\vec e_x \vec e_y = \vec e_z \in V$ but $\vec e_y \vec e_x = -\vec e_z$, while $\vec e_x^2 = -e_t \in S$. So $V$ is closed neither under the product nor under taking squares, and it is not a subalgebra of $\mathbb{H}_{\mathrm{s}}$.

**The vector subspace is a Lie algebra.** The commutator $[\tilde q_1,\tilde q_2] = \tilde q_1 \tilde q_2 - \tilde q_2\tilde q_1$ removes the scalar part, because $\vec q\vec q_1 + \vec q_1\vec q = -2B(\vec q,\vec q_1)\cdot1$ makes the scalar parts of $\tilde q_1 \tilde q_2$ and $\tilde q_2\tilde q_1$ equal, both being $-\langle\tilde q_1,\tilde q_2\rangle$. Hence $V$ is closed under the bracket:

$$
[\vec e_x, \vec e_y] = 2\vec e_z, \qquad [\vec e_y, \vec e_z] = -2\vec e_x, \qquad [\vec e_z, \vec e_x] = 2\vec e_y .
$$

The bracket is bilinear, alternating and satisfies the Jacobi identity because the product is associative; so $V$ is a three-dimensional real Lie algebra. With the generators $h = \vec e_z$, $e = \vec e_x + \vec e_y$, $f = \vec e_x - \vec e_y$ one has $[h,e] = 2e$, $[h,f] = -2f$ and $[e,f] = -4h$, so a rescaling of $f$ makes $\{h, e, f\}$ a standard $\mathrm{SL}_2(\mathbb{R})$-triple, and the bracket algebra is

$$
V \cong \mathrm{SL}_2(\mathbb{R}).
$$

The scalar line is central and contributes nothing to the bracket, so the full Lie algebra is the direct sum $\mathrm{SL}_2(\mathbb{R}) \oplus \mathbb{R}$ of the bracket algebra on $V$ and the abelian scalar line.

**Module structure.** Both $S$ and $V$ are $\mathbb{R}$-vector spaces and are preserved by left and right multiplication by scalars; over the centre they are free modules of ranks $1$ and $3$. Multiplication by an element of the full algebra moves $V$ into $S \oplus V = \mathbb{H}_{\mathrm{s}}$, with the scalar part given by the bilinear form.

## The Split-Quaternion Norm

**On the scalar subspace.** For $\tilde q = q_t \in S$ the split-quaternion norm is

$$
\langle q_t\rangle_{\natural} = q_t^2 \geq 0,
$$

a positive-definite form of rank $1$; it vanishes only at $q_t = 0$, so every nonzero scalar is a unit and $S$ contains no zero divisor.

**On the vector subspace.** For $\vec q = q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ the restriction is

$$
\langle \vec q\rangle_{\natural} = q_x^2 - q_y^2 - q_z^2,
$$

a form of **signature $(2,1)$** in the basis $\vec e_x, \vec e_y, \vec e_z$: one direction of square $+1$ and two of square $-1$. It is the three-dimensional **Minkowski form**, and it is indefinite and non-degenerate. Its null cone in $V$ is

$$
q_x^2 = q_y^2 + q_z^2,
$$

a cone over a circle of lines, and every nonzero element of it is a nonzero nilpotent, since for $\vec q \in V$ the square is $\vec q^2 = -\langle \vec q\rangle_{\natural}$, so $\vec q^2 = 0$ exactly when $\langle \vec q\rangle_{\natural} = 0$.

**The trichotomy.** The nonzero vectors of $V$ fall into three classes according to the sign of the restricted form:

| class | condition | norm |
|---|---|---|
| timelike | $q_x^2 > q_y^2 + q_z^2$ | $N > 0$ |
| lightlike (isotropic) | $q_x^2 = q_y^2 + q_z^2$ | $N = 0$ |
| spacelike | $q_x^2 < q_y^2 + q_z^2$ | $N < 0$ |

The lightlike class is exactly the light cone, the spacelike class is its outside, and the timelike class is its inside; the three are the orbit-types of the indefinite form, and they are the reason the geometry on $V$ is Lorentzian rather than Euclidean.

**The full form.** The subspaces $S$ and $V$ are $\langle\cdot,\cdot\rangle_{\natural}$-orthogonal, since $\langle q_t, \vec q\rangle_{\natural} = 0$ for $q_t \in S$ and $\vec q \in V$, and the form on $\mathbb{H}_{\mathrm{s}}$ is the orthogonal direct sum of the two restrictions; in the basis $1, \vec e_x, \vec e_y, \vec e_z$ it has signs $(+,+,-,-)$, so the full form has signature $(2,2)$. The scalar direction contributes $+1$, and among the vector directions $\vec e_x$ contributes $+1$ while $\vec e_y$ and $\vec e_z$ contribute $-1$.

The restriction to $V$, of signature $(2,1)$, and not a definite form, is the root of the geometry of the category: the unit group of the algebra acts on $V$ as the Lorentz group of this form, and the hyperbolic geometry the system carries is the hyperbolic plane. This is developed in *Split-Quaternion Rotations and the Lorentz Group* and *Split-Quaternion Geometry*.

## The Lie Algebra of the Vector Subspace

The vector subspace $V$ is closed under the commutator $[\vec q, \vec q_1] = \vec q \vec q_1 - \vec q_1 \vec q$: the scalar part of a product of two vectors is $-B(\vec q, \vec q_1)$, so the commutator has zero scalar part and lies in $V$. The commutator is bilinear, alternating and satisfies the Jacobi identity, which is inherited from the associativity of the algebra; hence $V$ is a Lie algebra, and it is the three-dimensional simple real Lie algebra $\mathrm{SL}_2(\mathbb{R})$. The scalar line $S$ is the centre and multiplies into $V$ without a bracket contribution.

**Proposition.** With the generators $\vec e_x, \vec e_y, \vec e_z$ the bracket reads

$$
[\vec e_x, \vec e_y] = 2\vec e_z, \qquad [\vec e_y, \vec e_z] = -2\vec e_x, \qquad [\vec e_z, \vec e_x] = 2\vec e_y,
$$

so $V \cong \mathrm{SL}_2(\mathbb{R})$, and the split-quaternion norm $\langle\cdot\rangle_{\natural}$ on $V$, of signature $(2,1)$, is invariant under the adjoint action: $\operatorname{ad}_{\tilde q}$ is $\langle\cdot\rangle_{\natural}$-skew for every $\tilde q \in V$.

**Proof.** The bracket relations follow from the products $\vec e_x \vec e_y = \vec e_z$, $\vec e_y \vec e_z = -\vec e_x$, $\vec e_z \vec e_x = \vec e_y$ together with $\vec e_y \vec e_x = -\vec e_z$, $\vec e_z \vec e_y = \vec e_x$, $\vec e_x \vec e_z = -\vec e_y$. The Jacobi identity is $[[\tilde q_1,\tilde q_2],\tilde q_3] + [[\tilde q_2,\tilde q_3],\tilde q_1] + [[\tilde q_3,\tilde q_1],\tilde q_2] = 0$, an identity in every associative algebra, and the structure constants are those of $\mathrm{SL}_2(\mathbb{R})$. The invariance of $\langle\cdot\rangle_{\natural}$ is the identity $\langle[\tilde q_1,\tilde q_2],\tilde q_3\rangle + \langle\tilde q_2,[\tilde q_1,\tilde q_3]\rangle = 0$, which follows from the associativity of the algebra and the multiplicativity $\langle ab\rangle_{\natural} = \langle a\rangle_{\natural}\langle b\rangle_{\natural}$ of the split-quaternion norm.

## The Involutions on Them

The three involutions of the algebra act on $S$ and $V$ by the following sign patterns.

| involution | on $S$ | on $V$ |
|---|---|---|
| conjugation ${}^{\natural}$ | $+1$ | $-1$ |
| principal $\alpha$ | $+1$ | $-1$ on $\operatorname{span}\{\vec e_x,\vec e_y\}$, $+1$ on $\mathbb{R}\vec e_z$ |
| reversal $\rho$ | $+1$ | $+1$ on $\operatorname{span}\{\vec e_x,\vec e_y\}$, $-1$ on $\mathbb{R}\vec e_z$ |

Both $S$ and $V$ are invariant under all three. The conjugation acts as a single scalar on each; the principal involution and the reversal further split $V$ into the plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ and the line $\mathbb{R}\vec e_z$, and they agree with the conjugation on the plane, where all three act as $-1$. This is the finest decomposition the three involutions produce, and it is developed in *Split-Quaternion Subspaces and the Involutions*.

## Relations to the Other Subspaces

The scalar and vector subspaces meet the remaining distinguished subspaces as follows.

### The Split-Complex Subalgebras

$$
S \cap \mathbb{D}_2 = \mathbb{R}\cdot 1, \qquad S \cap \mathbb{D}_3 = \mathbb{R}\cdot 1, \qquad
V \cap \mathbb{D}_2 = \mathbb{R} \vec e_y, \qquad V \cap \mathbb{D}_3 = \mathbb{R} \vec e_z .
$$

So each split-complex subalgebra meets $S$ in the scalar line and $V$ in a single spacelike line; the plane $\operatorname{span}\{1,\vec e_y\}$ is spanned by the scalar line and the $\vec e_y$-line, and similarly for $\operatorname{span}\{1,\vec e_z\}$.

### The Minimal Ideals

The minimal left ideals $\mathbb{H}_{\mathrm{s}} \tilde\pi_{1,2}$ and the minimal right ideals $\tilde\pi_{1,2} \mathbb{H}_{\mathrm{s}}$ each meet $S$ and $V$:

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_1 \cap S = \{0\}, \qquad \mathbb{H}_{\mathrm{s}} \tilde\pi_1 \cap V = \mathbb{R} \vec e_x \tilde\pi_1 = \mathbb{R}\cdot\tfrac{1}{2}(\vec e_x + \vec e_z),
$$

and similarly for the other three ideals. The full intersections are in *Split-Quaternion Relations Between Subspaces*.

### The Decomposition

The scalar–vector decomposition is the coarsest of the decompositions of the algebra: it is the eigenspace decomposition of the conjugation, and the orthogonal splitting for the split-quaternion norm. Every finer decomposition — the split-complex decomposition, the idempotent decomposition, the common eigenspaces of the involutions — refines it.

## Examples

**Example (a scalar element).** For $\tilde q = 5$ the scalar part is $5$ and the vector part is $0$; the split-quaternion norm is $\langle 5\rangle_{\natural} = 25$, and the element is a unit with inverse $1/5$.

**Example (a timelike vector).** For $\vec q = 2\vec e_x$, the split-quaternion norm is $N = 4 > 0$, and the element is a unit with $\vec q^2 = -4$.

**Example (a lightlike vector).** For $\vec q = \vec e_x + \vec e_z$, the split-quaternion norm is $N = 1 - 1 = 0$ and $\vec q^2 = 0$: the vector is a nilpotent. It is a zero divisor and not a unit.

**Example (a spacelike vector).** For $\vec q = \vec e_y + \vec e_z$, the split-quaternion norm is $N = -1 - 1 = -2 < 0$ and $\vec q^2 = -\langle \vec q\rangle_{\natural} = 2$. The element is a unit of negative norm.

**Example (a generic element).** For $\tilde q = 3 - \vec e_x + 2\vec e_y$, the scalar part is $3 \in S$ and the vector part is $-\vec e_x + 2\vec e_y \in V$, with $\langle\tilde q\rangle_{\natural} = 9 + 1 - 4 = 6$ and $\tilde q$ a unit.

## Summary

The scalar subspace $S = \mathbb{R}\cdot 1$ and the vector subspace $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ are the $+1$ and $-1$ eigenspaces of the conjugation, of real dimensions $1$ and $3$, and they give the decomposition $\mathbb{H}_{\mathrm{s}} = S \oplus V$. The scalar subspace is the centre, a subalgebra isomorphic to $\mathbb{R}$; the vector subspace is not a subalgebra, since squares of vectors leave it, but it is closed under the commutator bracket and is a three-dimensional Lie algebra isomorphic to $\mathrm{SL}_2(\mathbb{R})$.

The split-quaternion norm restricts to $\langle q_t\rangle_{\natural} = q_t^2$ on $S$, positive definite, and to the Minkowski form $\langle \vec q\rangle_{\natural} = q_x^2 - q_y^2 - q_z^2$ of signature $(2,1)$ on $V$; the nonzero vectors of $V$ split into the timelike, lightlike and spacelike classes according to the sign. The scalar line is the centre and the vector subspace is the Lie algebra $\mathrm{SL}_2(\mathbb{R})$ under the commutator. The three involutions preserve both subspaces; the conjugation acts as a scalar on each, and the principal involution and reversal split $V$ into the common plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ and the line $\mathbb{R}\vec e_z$. The unit group acts on $V$ preserving the restricted form, which is the Lorentz action of *Split-Quaternion Rotations and the Lorentz Group*.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $S = \mathbb{R}\cdot 1$ | the scalar subspace, the centre, $\{\tilde q : \tilde{q}^{\natural}=\tilde q\}$ | this article |
| $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | the vector subspace, $\{\tilde q : \tilde{q}^{\natural}=-\tilde q\}$ | this article |
| $\operatorname{Sc}(\tilde q) = q_t$, $\operatorname{Vec}(\tilde q) = \vec v$ | the scalar and vector parts | this article |
| ${}^{\natural}$, $\alpha$, $\rho$ | conjugation, principal involution, reversal | *Split-Quaternion Algebra* |
| $\langle \vec q\rangle_{\natural} = q_x^2-q_y^2-q_z^2$ on $V$ | the Minkowski form of signature $(2,1)$ | this article |
| $B(\vec q,\vec q_1)$ | the polarised bilinear form | *Split-Quaternion Norm and Invertibility* |
| $[\tilde q_1,\tilde q_2] = \tilde q_1 \tilde q_2-\tilde q_2\tilde q_1$ | the commutator bracket | this article |
| $V \cong \mathrm{SL}_2(\mathbb{R})$ | the Lie algebra of traceless matrices | this article |
| $\mathbb{D}_2 = \operatorname{span}\{1,\vec e_y\}$, $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$ | the split-complex subalgebras | *Split-Quaternion Algebra* |
| timelike, lightlike, spacelike | the sign trichotomy on $V$ | this article |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the vector subspace of a Clifford algebra and its identification with $\mathrm{SL}_2(\mathbb{R})$.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Lie algebra of traceless matrices and its action on the Minkowski form.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, the inertia law and the Minkowski trichotomy.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split forms and their vector parts.
