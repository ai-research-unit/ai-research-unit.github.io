
# __Split-Quaternion Scalar and Vector Subspaces__

## Introduction

The conjugation of the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is an involutive anti-automorphism, and an involution splits the algebra into its $+1$ and $-1$ eigenspaces. This article studies the two resulting subspaces: the **scalar subspace** $S$, the fixed space of the conjugation, and the **vector subspace** $V$, its anti-fixed space. Together they give the scalar–vector decomposition

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V,
$$

which is the coarsest decomposition of the algebra and the source of nearly every other structure in the category.

The article establishes the definitions and a basis for each subspace; shows that the two descriptions of $S$ and $V$ — as eigenspaces of the conjugation and as the scalar line and the span of the vector units — coincide; examines the algebra and module structure, in particular the failure of $V$ to be a subalgebra and its structure as a Lie algebra under the commutator; restricts the split-quaternion norm to each subspace and identifies the Minkowski form of signature $(2,1)$ on $V$; gives the matrix images of both; follows the three involutions through them; and records their relations with the remaining distinguished subspaces. It closes with worked examples.

**Conventions.** The algebra is $\mathbb{H}_{\mathrm{s}}$, with basis $1, e_1, e_2, e_3$, the relations $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1 e_2$ and $e_1 e_2 = -e_2 e_1$, and a general element $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$. The conjugation is $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$, the split-quaternion norm is $N(\tilde q) = \tilde q\tilde{q}^{\natural} = q_0^2 + q_1^2 - q_2^2 - q_3^2$ with polarisation $B$, and the principal involution $\alpha$ and the reversal $\rho$ are as in *Split-Quaternion Algebra*. The split-complex subalgebras are $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ and $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$.

## Definition and Basis

**Definition.** The **scalar subspace** and the **vector subspace** of $\mathbb{H}_{\mathrm{s}}$ are

$$
S = \mathbb{R}\cdot 1, \qquad V = \operatorname{span}\{e_1, e_2, e_3\}.
$$

Every element has a unique expansion $\tilde q = q_0 + \mathbf{v}$ with $q_0 \in S$ and $\mathbf{v} \in V$; the projection onto the first summand is the scalar part, $\operatorname{Sc}(\tilde q) = q_0$, and the projection onto the second is the vector part, $\operatorname{Vec}(\tilde q) = \mathbf{v} = q_1 e_1 + q_2 e_2 + q_3 e_3$.

**Proposition.** $S$ has real dimension $1$, with basis $\{1\}$; $V$ has real dimension $3$, with basis $\{e_1, e_2, e_3\}$; and $S \cap V = \{0\}$, so that $\mathbb{H}_{\mathrm{s}} = S \oplus V$ with $\dim_{\mathbb{R}}\mathbb{H}_{\mathrm{s}} = 1 + 3 = 4$.

**Proof.** The four basis elements $1, e_1, e_2, e_3$ are linearly independent over $\mathbb{R}$ by the definition of the algebra, so $\{1\}$ is a basis of $S$ and $\{e_1,e_2,e_3\}$ is a basis of $V$; an element of $S \cap V$ is a multiple of $1$ with zero vector part, hence zero.

## The Two Descriptions Coincide

The scalar and vector subspaces are exactly the eigenspaces of the conjugation.

**Proposition.** For every $\tilde q \in \mathbb{H}_{\mathrm{s}}$, the conjugation satisfies $\tilde{q}^{\natural} = \tilde q$ if and only if $\tilde q \in S$, and $\tilde{q}^{\natural} = -\tilde q$ if and only if $\tilde q \in V$. Hence the scalar–vector decomposition is the eigenspace decomposition

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V, \qquad S = \{\tilde q : \tilde{q}^{\natural} = \tilde q\}, \qquad V = \{\tilde q : \tilde{q}^{\natural} = -\tilde q\}.
$$

**Proof.** Since $\bar{1} = 1$ and $e_k^{\natural} = -e_k$, the conjugation acts as $+1$ on $S$ and as $-1$ on $V$; conversely, writing $\tilde q = q_0 + \mathbf{v}$, the condition $\tilde{q}^{\natural} = \tilde q$ reads $-2\mathbf{v} = 0$, i.e. $\mathbf{v} = 0$, and the condition $\tilde{q}^{\natural} = -\tilde q$ reads $2q_0 = 0$, i.e. $q_0 = 0$.

The scalar subspace is also the **centre** of the algebra. An element $\tilde q$ commutes with every element if and only if $\mathbf{v} = 0$: commuting with $e_1$ and $e_2$ gives $\mathbf{v}e_1 = e_1\mathbf{v}$ and $\mathbf{v}e_2 = e_2\mathbf{v}$, which force $q_2 = q_3 = 0$ and $q_1 = 0$ respectively, so $\tilde q = q_0$ is scalar. Hence

$$
Z(\mathbb{H}_{\mathrm{s}}) = S = \mathbb{R}\cdot 1 .
$$

The centre is therefore a field, namely $\mathbb{R}$, and $S$ is the only commutative two-sided piece of the algebra. This is developed in *Split-Quaternion Algebra*, §*The Centre and Simplicity*.

## Algebra and Module Structure

**The scalar subspace.** $S$ is a subalgebra, isomorphic to $\mathbb{R}$ by $q_0 \mapsto q_0$, and its product is $q_0 \cdot q_0' = q_0 q_0'$. Because it is the centre, $S$ multiplies into every subspace without sign change: $q_0 \tilde q = xa$ for all $\tilde q$, and multiplication by a scalar is scalar extension.

**The vector subspace is not a subalgebra.** The square of a vector leaves $V$: $e_1^2 = -1$ and $e_2^2 = +1$ are scalars, and $e_3^2 = +1$. In general, for $\mathbf{u}, \mathbf{v} \in V$ the product splits as

$$
\mathbf{u}\mathbf{v} = -B(\mathbf{u}, \mathbf{v}) \cdot 1 + \tfrac{1}{2}[\mathbf{u}, \mathbf{v}],
$$

with scalar part $-B(\mathbf{u},\mathbf{v})$ and the remainder $\tfrac{1}{2}[\mathbf{u},\mathbf{v}] \in V$; for instance $e_1 e_2 = e_3 \in V$ but $e_2 e_1 = -e_3$, while $e_1^2 = -1 \in S$. So $V$ is closed neither under the product nor under taking squares, and it is not a subalgebra of $\mathbb{H}_{\mathrm{s}}$.

**The vector subspace is a Lie algebra.** The commutator $[\tilde q,y] = \tilde q y - y\tilde q$ removes the scalar part, because $\mathbf{u}\mathbf{v} + \mathbf{v}\mathbf{u} = -2B(\mathbf{u},\mathbf{v})\cdot1$ makes the scalar parts of $\tilde q y$ and $y\tilde q$ equal, both being $-B(\tilde q,y)$. Hence $V$ is closed under the bracket:

$$
[e_1, e_2] = 2e_3, \qquad [e_2, e_3] = -2e_1, \qquad [e_3, e_1] = 2e_2 .
$$

The bracket is bilinear, alternating and satisfies the Jacobi identity because the product is associative; so $V$ is a three-dimensional real Lie algebra. With the generators $h = e_3$, $e = e_1 + e_2$, $f = e_1 - e_2$ one has $[h,e] = 2e$, $[h,f] = -2f$ and $[e,f] = -4h$, so a rescaling of $f$ makes $\{h, e, f\}$ a standard $\mathrm{SL}_2(\mathbb{R})$-triple, and the bracket algebra is

$$
V \cong \mathrm{SL}_2(\mathbb{R}).
$$

The scalar line is central and contributes nothing to the bracket, so the full Lie algebra is the direct sum $\mathrm{SL}_2(\mathbb{R}) \oplus \mathbb{R}$ of the bracket algebra on $V$ and the abelian scalar line.

**Module structure.** Both $S$ and $V$ are $\mathbb{R}$-vector spaces and are preserved by left and right multiplication by scalars; over the centre they are free modules of ranks $1$ and $3$. Multiplication by an element of the full algebra moves $V$ into $S \oplus V = \mathbb{H}_{\mathrm{s}}$, with the scalar part given by the bilinear form.

## The Split-Quaternion Norm

**On the scalar subspace.** For $\tilde q = q_0 \in S$ the split-quaternion norm is

$$
N(q_0) = q_0^2 \geq 0,
$$

a positive-definite form of rank $1$; it vanishes only at $q_0 = 0$, so every nonzero scalar is a unit and $S$ contains no zero divisor.

**On the vector subspace.** For $\mathbf{u} = q_1 e_1 + q_2 e_2 + q_3 e_3$ the restriction is

$$
N(\mathbf{u}) = q_1^2 - q_2^2 - q_3^2,
$$

a form of **signature $(2,1)$** in the basis $e_1, e_2, e_3$: one direction of square $+1$ and two of square $-1$. It is the three-dimensional **Minkowski form**, and it is indefinite and non-degenerate. Its null cone in $V$ is

$$
q_1^2 = q_2^2 + q_3^2,
$$

a cone over a circle of lines, and every nonzero element of it is a nonzero nilpotent, since for $\mathbf{u} \in V$ the square is $\mathbf{u}^2 = -N(\mathbf{u})$, so $\mathbf{u}^2 = 0$ exactly when $N(\mathbf{u}) = 0$.

**The trichotomy.** The nonzero vectors of $V$ fall into three classes according to the sign of the restricted form:

| class | condition | norm |
|---|---|---|
| timelike | $q_1^2 > q_2^2 + q_3^2$ | $N > 0$ |
| lightlike (isotropic) | $q_1^2 = q_2^2 + q_3^2$ | $N = 0$ |
| spacelike | $q_1^2 < q_2^2 + q_3^2$ | $N < 0$ |

The lightlike class is exactly the light cone, the spacelike class is its outside, and the timelike class is its inside; the three are the orbit-types of the indefinite form, and they are the reason the geometry on $V$ is Lorentzian rather than Euclidean.

**The full form.** The subspaces $S$ and $V$ are $B$-orthogonal, since $B(q_0, \mathbf{v}) = 0$ for $q_0 \in S$ and $\mathbf{v} \in V$, and the form on $\mathbb{H}_{\mathrm{s}}$ is the orthogonal direct sum of the two restrictions; in the basis $1, e_1, e_2, e_3$ it has signs $(+,+,-,-)$, so the full form has signature $(2,2)$. The scalar direction contributes $+1$, and among the vector directions $e_1$ contributes $+1$ while $e_2$ and $e_3$ contribute $-1$.

The restriction to $V$, of signature $(2,1)$, and not a definite form, is the root of the geometry of the category: the unit group of the algebra acts on $V$ as the Lorentz group of this form, and the hyperbolic geometry the system carries is the hyperbolic plane. This is developed in *Split-Quaternion Rotations and the Lorentz Group* and *Split-Quaternion Geometry*.

## The Lie Algebra of the Vector Subspace

The vector subspace $V$ is closed under the commutator $[\mathbf u, \mathbf v] = \mathbf u \mathbf v - \mathbf v \mathbf u$: the scalar part of a product of two vectors is $-B(\mathbf u, \mathbf v)$, so the commutator has zero scalar part and lies in $V$. The commutator is bilinear, alternating and satisfies the Jacobi identity, which is inherited from the associativity of the algebra; hence $V$ is a Lie algebra, and it is the three-dimensional simple real Lie algebra $\mathrm{SL}_2(\mathbb{R})$. The scalar line $S$ is the centre and multiplies into $V$ without a bracket contribution.

**Proposition.** With the generators $e_1, e_2, e_3$ the bracket reads

$$
[e_1, e_2] = 2e_3, \qquad [e_2, e_3] = -2e_1, \qquad [e_3, e_1] = 2e_2,
$$

so $V \cong \mathrm{SL}_2(\mathbb{R})$, and the split-quaternion norm $N$ on $V$, of signature $(2,1)$, is invariant under the adjoint action: $\operatorname{ad}_x$ is $N$-skew for every $x \in V$.

**Proof.** The bracket relations follow from the products $e_1e_2 = e_3$, $e_2e_3 = -e_1$, $e_3e_1 = e_2$ together with $e_2e_1 = -e_3$, $e_3e_2 = e_1$, $e_1e_3 = -e_2$. The Jacobi identity is $[[x,y],z] + [[y,z],x] + [[z,x],y] = 0$, an identity in every associative algebra, and the structure constants are those of $\mathrm{SL}_2(\mathbb{R})$. The invariance of $N$ is the identity $B([x,y],z) + B(y,[x,z]) = 0$, which follows from the associativity of the algebra and the multiplicativity $N(ab) = N(a)N(b)$ of the split-quaternion norm.

## The Involutions on Them

The three involutions of the algebra act on $S$ and $V$ by the following sign patterns.

| involution | on $S$ | on $V$ |
|---|---|---|
| conjugation ${}^{\natural}$ | $+1$ | $-1$ |
| principal $\alpha$ | $+1$ | $-1$ on $\operatorname{span}\{e_1,e_2\}$, $+1$ on $\mathbb{R}e_3$ |
| reversal $\rho$ | $+1$ | $+1$ on $\operatorname{span}\{e_1,e_2\}$, $-1$ on $\mathbb{R}e_3$ |

Both $S$ and $V$ are invariant under all three. The conjugation acts as a single scalar on each; the principal involution and the reversal further split $V$ into the plane $\operatorname{span}\{e_1,e_2\}$ and the line $\mathbb{R}e_3$, and they agree with the conjugation on the plane, where all three act as $-1$. This is the finest decomposition the three involutions produce, and it is developed in *Split-Quaternion Subspaces and the Involutions*.

## Relations to the Other Subspaces

The scalar and vector subspaces meet the remaining distinguished subspaces as follows.

### The Split-Complex Subalgebras

$$
S \cap \mathbb{D}_2 = \mathbb{R}\cdot 1, \qquad S \cap \mathbb{D}_3 = \mathbb{R}\cdot 1, \qquad
V \cap \mathbb{D}_2 = \mathbb{R} e_2, \qquad V \cap \mathbb{D}_3 = \mathbb{R} e_3 .
$$

So each split-complex subalgebra meets $S$ in the scalar line and $V$ in a single spacelike line; the plane $\operatorname{span}\{1,e_2\}$ is spanned by the scalar line and the $e_2$-line, and similarly for $\operatorname{span}\{1,e_3\}$.

### The Minimal Ideals

The minimal left ideals $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$ and the minimal right ideals $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ each meet $S$ and $V$:

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_+ \cap S = \{0\}, \qquad \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \cap V = \mathbb{R} e_1 \tilde\pi_+ = \mathbb{R}\cdot\tfrac{1}{2}(e_1 + e_3),
$$

and similarly for the other three ideals. The full intersections are in *Split-Quaternion Relations Between Subspaces*.

### The Decomposition

The scalar–vector decomposition is the coarsest of the decompositions of the algebra: it is the eigenspace decomposition of the conjugation, and the orthogonal splitting for the split-quaternion norm. Every finer decomposition — the split-complex decomposition, the idempotent decomposition, the common eigenspaces of the involutions — refines it.

## Examples

**Example (a scalar element).** For $\tilde q = 5$ the scalar part is $5$ and the vector part is $0$; the split-quaternion norm is $N(5) = 25$, and the element is a unit with inverse $1/5$.

**Example (a timelike vector).** For $\mathbf{u} = 2e_1$, the split-quaternion norm is $N = 4 > 0$, and the element is a unit with $\mathbf{u}^2 = -4$.

**Example (a lightlike vector).** For $\mathbf{u} = e_1 + e_3$, the split-quaternion norm is $N = 1 - 1 = 0$ and $\mathbf{u}^2 = 0$: the vector is a nilpotent. It is a zero divisor and not a unit.

**Example (a spacelike vector).** For $\mathbf{u} = e_2 + e_3$, the split-quaternion norm is $N = -1 - 1 = -2 < 0$ and $\mathbf{u}^2 = -N(\mathbf{u}) = 2$. The element is a unit of negative norm.

**Example (a generic element).** For $\tilde q = 3 - e_1 + 2e_2$, the scalar part is $3 \in S$ and the vector part is $-e_1 + 2e_2 \in V$, with $N(\tilde q) = 9 + 1 - 4 = 6$ and $\tilde q$ a unit.

## Summary

The scalar subspace $S = \mathbb{R}\cdot 1$ and the vector subspace $V = \operatorname{span}\{e_1,e_2,e_3\}$ are the $+1$ and $-1$ eigenspaces of the conjugation, of real dimensions $1$ and $3$, and they give the decomposition $\mathbb{H}_{\mathrm{s}} = S \oplus V$. The scalar subspace is the centre, a subalgebra isomorphic to $\mathbb{R}$; the vector subspace is not a subalgebra, since squares of vectors leave it, but it is closed under the commutator bracket and is a three-dimensional Lie algebra isomorphic to $\mathrm{SL}_2(\mathbb{R})$.

The split-quaternion norm restricts to $N(q_0) = q_0^2$ on $S$, positive definite, and to the Minkowski form $N(\mathbf{u}) = q_1^2 - q_2^2 - q_3^2$ of signature $(2,1)$ on $V$; the nonzero vectors of $V$ split into the timelike, lightlike and spacelike classes according to the sign. The scalar line is the centre and the vector subspace is the Lie algebra $\mathrm{SL}_2(\mathbb{R})$ under the commutator. The three involutions preserve both subspaces; the conjugation acts as a scalar on each, and the principal involution and reversal split $V$ into the common plane $\operatorname{span}\{e_1,e_2\}$ and the line $\mathbb{R}e_3$. The unit group acts on $V$ preserving the restricted form, which is the Lorentz action of *Split-Quaternion Rotations and the Lorentz Group*.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $S = \mathbb{R}\cdot 1$ | the scalar subspace, the centre, $\{\tilde q : \tilde{q}^{\natural}=\tilde q\}$ | this article |
| $V = \operatorname{span}\{e_1,e_2,e_3\}$ | the vector subspace, $\{\tilde q : \tilde{q}^{\natural}=-\tilde q\}$ | this article |
| $\operatorname{Sc}(\tilde q) = q_0$, $\operatorname{Vec}(\tilde q) = \mathbf{v}$ | the scalar and vector parts | this article |
| ${}^{\natural}$, $\alpha$, $\rho$ | conjugation, principal involution, reversal | *Split-Quaternion Algebra* |
| $N(\mathbf{u}) = q_1^2-q_2^2-q_3^2$ on $V$ | the Minkowski form of signature $(2,1)$ | this article |
| $B(\mathbf{u},\mathbf{v})$ | the polarised bilinear form | *Split-Quaternion Norm and Invertibility* |
| $[\tilde q,y] = \tilde q y-y\tilde q$ | the commutator bracket | this article |
| $V \cong \mathrm{SL}_2(\mathbb{R})$ | the Lie algebra of traceless matrices | this article |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$, $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the split-complex subalgebras | *Split-Quaternion Algebra* |
| timelike, lightlike, spacelike | the sign trichotomy on $V$ | this article |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the vector subspace of a Clifford algebra and its identification with $\mathrm{SL}_2(\mathbb{R})$.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Lie algebra of traceless matrices and its action on the Minkowski form.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, the inertia law and the Minkowski trichotomy.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split forms and their vector parts.
