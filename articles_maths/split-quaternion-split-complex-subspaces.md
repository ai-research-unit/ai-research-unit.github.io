
# __Split-Quaternion Split-Complex Subspaces__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ contains two copies of the split-complex numbers, namely the planes $\operatorname{span}\{1, e_2\}$ and $\operatorname{span}\{1, e_3\}$. Each is a commutative subalgebra isomorphic to $\mathbb{D} = \mathbb{R}[j]/(j^2 - 1)$, each carries its own pair of idempotents and its own pair of isotropic lines, and together they account for the reduction of the algebra to its split-complex pieces. This article studies them.

The split-complex subspaces are the split-quaternion analogues of the **centre** of the biquaternion algebra: in $\mathbb{B}$ the commutative, idempotent-bearing subalgebra is the centre $\mathbb{C}$, which is central. In $\mathbb{H}_{\mathrm{s}}$ the commutative, idempotent-bearing subalgebras are **not** central — the centre is only the scalar line $\mathbb{R}\cdot 1$ — so the module structure they give is a twisted one, and the contrast is the point of the article.

The article gives the two subalgebras, their bases, dimensions and defining conditions; their idempotents, which are exactly the standard idempotents $\tilde\pi_{1,2}$ for the first plane; the zero divisors they carry; the module structure of the algebra over each, with the twisted multiplication; and the comparison with the centre of $\mathbb{B}$. It closes with examples.

**Conventions.** The algebra $\mathbb{H}_{\mathrm{s}}$ has basis $1, e_1, e_2, e_3$ with $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1 e_2$, $e_1 e_2 = -e_2 e_1$, and norm $N(q_0 + q_1e_1 + q_2e_2 + q_3e_3) = q_0^2 + q_1^2 - q_2^2 - q_3^2$. The scalar subspace $S$ and the vector subspace $V$ are as in *Split-Quaternion Scalar and Vector Subspaces*. The split-complex numbers are $\mathbb{D} = \mathbb{R}[j]/(j^2-1) \cong \mathbb{R} \oplus \mathbb{R}$, an algebra over the commutative ring $\mathbb{R}$; their idempotents are $e_\pm = \tfrac{1}{2}(1 \pm j)$.

## Definition and Basis

**Definition.** The two **split-complex subspaces** of $\mathbb{H}_{\mathrm{s}}$ are

$$
\mathbb{D}_2 = \operatorname{span}\{1, e_2\}, \qquad \mathbb{D}_3 = \operatorname{span}\{1, e_3\}.
$$

Each is the $\mathbb{R}$-linear span of the scalar unit and one hyperbolic basis element.

**Proposition.** Each of $\mathbb{D}_2, \mathbb{D}_3$ is a two-dimensional commutative subalgebra with identity, isomorphic to $\mathbb{D}$ by $j \mapsto e_2$ and $j \mapsto e_3$ respectively. Their intersection and their relation to the scalar–vector splitting are

$$
\mathbb{D}_2 \cap \mathbb{D}_3 = S = \mathbb{R}\cdot 1, \qquad
\mathbb{D}_2 \cap V = \mathbb{R} e_2, \qquad \mathbb{D}_3 \cap V = \mathbb{R} e_3 .
$$

**Proof.** Since $e_2^2 = +1$ and $e_3^2 = +1$, each span is closed under multiplication and commutative, so each is a subalgebra, and the unique $\mathbb{R}$-algebra map $j \mapsto e_k$ is an isomorphism $\mathbb{D} \to \mathbb{D}_k$ because $j^2 = 1 = e_k^2$. An element of $\mathbb{D}_2 \cap \mathbb{D}_3$ has the form $q_0 + q_2e_2 = q_0' + q_3 e_3$, and linear independence of $1, e_2, e_3$ forces $q_2 = q_3 = 0$, so the intersection is $S$. The last two identities are read off the bases.

The two subalgebras together with the definite plane $\mathbb{R}[e_1] = \operatorname{span}\{1, e_1\}$ exhaust the coordinate planes through the scalar line. The third, $\mathbb{R}[e_1]$, is isomorphic to the complex numbers $\mathbb{C}$ because $e_1^2 = -1$, and it is definite, but the menu asks only for the two split-complex planes, and $\mathbb{R}[e_1]$ is recorded in *Split-Quaternion Algebra*.

## Algebra and Module Structure

### Idempotents of the Subspaces

Each split-complex subalgebra is isomorphic to $\mathbb{R} \oplus \mathbb{R}$ and therefore has exactly four idempotents: $0, 1$ and the two nontrivial ones $\tfrac{1}{2}(1 \pm j)$. In $\mathbb{H}_{\mathrm{s}}$ this gives

$$
\mathbb{D}_2: \quad \tilde\pi_1 = \tfrac{1}{2}(1 + e_2), \quad \tilde\pi_2 = \tfrac{1}{2}(1 - e_2),
$$

$$
\mathbb{D}_3: \quad v_+ = \tfrac{1}{2}(1 + e_3), \quad v_- = \tfrac{1}{2}(1 - e_3).
$$

The idempotents $\tilde\pi_{1,2}$ of the first plane are exactly the **standard idempotents** of the algebra, and the companion article *Split-Quaternion Idempotents and Projections* develops them; the pair $v_\pm$ plays the same role inside $\mathbb{D}_3$. In either plane the two idempotents are orthogonal and complete, $\tilde\pi_1\tilde\pi_2 = v_+v_- = 0$ and $\tilde\pi_1 + \tilde\pi_2 = v_+ + v_- = 1$, and both have norm zero, $N(\tilde\pi_{1,2}) = N(v_\pm) = 0$. Within its own plane each idempotent is central, because the plane is commutative; but it is not central in $\mathbb{H}_{\mathrm{s}}$, since $e_1 \tilde\pi_1 = \tfrac{1}{2}(e_1 + e_3) \neq \tfrac{1}{2}(e_1 - e_3) = \tilde\pi_1 e_1$.

### Subalgebra, Commutativity, Ring Structure

As abstract rings, $\mathbb{D}_2 \cong \mathbb{D}_3 \cong \mathbb{R} \oplus \mathbb{R}$: the map sending $q_0 + q_2 e_2$ to the pair $(q_0 + q_2, q_0 - q_2)$ is a ring isomorphism, inverse to $(r, s) \mapsto \tfrac{1}{2}(r+s) + \tfrac{1}{2}(r-s) e_2$. Hence each split-complex subspace is a product of two copies of the field $\mathbb{R}$; it has exactly two maximal ideals, the kernels of the two projections, which are the spans of the idempotents $\tilde\pi_{1,2}$. Neither subspace is a field, and each has zero divisors.

### Multiplication Tables

On the basis of $\mathbb{D}_2$ the products are $1 \cdot 1 = 1$, $1 \cdot e_2 = e_2$, $e_2 \cdot e_2 = 1$. On the basis of $\mathbb{D}_3$ the same table holds with $e_2$ replaced by $e_3$. The two subalgebras interact through the anticommutation $e_2 e_3 = -e_3 e_2 = -e_1$, and their set of products is the whole algebra: $\mathbb{D}_2 \mathbb{D}_3 = \mathbb{H}_{\mathrm{s}}$.

### Module Structure and the Twisted Multiplication

The algebra is a free module of rank $2$ over each split-complex subspace, on the left and on the right. For $\mathbb{D}_2$ the decomposition is

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{D}_2 \oplus \mathbb{D}_2 e_1, \qquad \mathbb{D}_2 e_1 = \operatorname{span}\{e_1, e_3\},
$$

a free left $\mathbb{D}_2$-module with basis $\{1, e_1\}$; the same decomposition is a free right $\mathbb{D}_2$-module with the same basis. The two module structures differ, and the difference is the twist. Since $e_1$ anticommutes with $e_2$, passing $e_1$ to the right of an element $A = q_0 + q_2 e_2 \in \mathbb{D}_2$ conjugates that element:

$$
e_1 A = \bar{A} e_1, \qquad \bar{A} = q_0 - q_2 e_2,
$$

where $\bar{\cdot}$ is the conjugation of the split-complex plane, the nontrivial involution of $\mathbb{D}$. Consequently the product in $\mathbb{H}_{\mathrm{s}}$, written in the $\mathbb{D}_2$-basis $\{1, e_1\}$ as $\tilde q = A_1 + A_2 e_1$ and $\tilde p = B_1 + B_2 e_1$ with $A_i, B_i \in \mathbb{D}_2$, is the **twisted multiplication**

$$
(A_1 + A_2 e_1)(B_1 + B_2 e_1)
= \big(A_1 B_1 - A_2 \bar{B_2}\big) + \big(A_1 B_2 + A_2 \bar{B_1}\big)e_1 .
$$

This is the multiplication of a quaternion-like algebra over the commutative ring $\mathbb{D}_2$, in which the anticommuting generator $e_1$ acts by the conjugation of the coefficient algebra. The same computation with $e_2$ in place of $e_1$ gives the rank-$2$ module structure over $\mathbb{D}_3$. Because $\mathbb{D}_2$ and $\mathbb{D}_3$ are not central, the algebra is a module and a bimodule over each, but not an algebra over either, and the twist $\bar{\cdot}$ is exactly what obstructs the algebra structure.

## The Split-Quaternion Norm

### Restriction

The split-quaternion norm restricts to each plane as the two-dimensional form

$$
N(q_0 + q_2 e_2) = q_0^2 - q_2^2, \qquad N(q_0 + q_3 e_3) = q_0^2 - q_3^2,
$$

of signature $(1,1)$. Each restriction is the hyperbolic or **Minkowski** form of the plane, indefinite and non-degenerate, and each is the form of the split-complex algebra itself.

### Units and Zero Divisors

In $\mathbb{D}_2$, an element $q_0 + q_2e_2$ is a unit of the algebra exactly when $q_0^2 \neq q_2^2$, with inverse $(q_0 - q_2e_2)/(q_0^2-q_2^2)$; the units form the two branches of the hyperbola $q_0^2 - q_2^2 \neq 0$. The non-units are the two isotropic lines

$$
\mathbb{R}(1 + e_2), \qquad \mathbb{R}(1 - e_2),
$$

on which $q_0 = \pm q_2$; every nonzero element of these lines is a zero divisor, and indeed $(1+e_2)(1-e_2) = 0$. The same statements hold in $\mathbb{D}_3$ with the isotropic lines $\mathbb{R}(1\pm e_3)$. The isotropic lines of the two planes, together with the scalar null direction, are the traces of the null cone of $N$ on the planes, and they are described in *Split-Quaternion Zero Divisors*.

**Proposition.** The zero divisors of $\mathbb{D}_2$ are exactly the nonzero elements of the two isotropic lines $\mathbb{R}(1 \pm e_2)$, and the zero divisors of $\mathbb{D}_3$ are exactly the nonzero elements of $\mathbb{R}(1 \pm e_3)$.

**Proof.** The split-quaternion norm of the plane has signature $(1,1)$, so its null set is the union of the two lines indicated, and an element is a unit if and only if its split-quaternion norm is nonzero, by the split-quaternion norm criterion of *Split-Quaternion Norm and Invertibility*; hence the non-units are exactly the nonzero null elements.

## The Structure of the Planes

Each plane is the span of two orthogonal idempotents. In $\mathbb{D}_2 = \operatorname{span}\{1, e_2\}$ the element $e_2$ is an involution, $e_2^2 = +1$, with eigenvectors $1 \pm e_2$ and eigenvalues $\pm 1$; in $\mathbb{D}_3 = \operatorname{span}\{1, e_3\}$ the element $e_3$ is an involution with eigenvectors $1 \pm e_3$. Hence each plane is the direct sum of the two idempotent lines,

$$
\tilde\pi_{1,2} = \tfrac{1}{2}(1 \pm e_2) \in \mathbb{D}_2, \qquad v_\pm = \tfrac{1}{2}(1 \pm e_3) \in \mathbb{D}_3,
$$

with $\tilde\pi_1 + \tilde\pi_2 = 1$, $\tilde\pi_1 \tilde\pi_2 = 0$ and $v_+ + v_- = 1$, $v_+ v_- = 0$. Each plane carries its own splitting of the identity, the first along the $e_2$-eigenlines and the second along the $e_3$-eigenlines, and each is a copy of $\mathbb{R} \oplus \mathbb{R}$; the two planes are the two distinct embeddings of the split-complex algebra that contain the scalar line.

## The Involutions on Them

Both subalgebras are invariant under the two algebra maps that fix the scalar line and send $e_2, e_3$ to themselves or their negatives.

| involution | on $\mathbb{D}_2$ | on $\mathbb{D}_3$ |
|---|---|---|
| conjugation $\bar{\cdot}$ | $1 \mapsto 1$, $e_2 \mapsto -e_2$ | $1 \mapsto 1$, $e_3 \mapsto -e_3$ |
| principal $\alpha$ | $1 \mapsto 1$, $e_2 \mapsto -e_2$ | $1 \mapsto 1$, $e_3 \mapsto e_3$ |
| reversal $\rho$ | $1 \mapsto 1$, $e_2 \mapsto e_2$ | $1 \mapsto 1$, $e_3 \mapsto -e_3$ |

On $\mathbb{D}_2$ the conjugation and the principal involution agree and are the nontrivial involution of the split-complex plane, while the reversal is the identity there; on $\mathbb{D}_3$ it is the conjugation and the reversal that agree, while the principal involution is the identity. In both planes the nontrivial involution swaps the two idempotents, $\tilde\pi_1 \leftrightarrow \tilde\pi_2$ and $v_+ \leftrightarrow v_-$, and swaps the two isotropic lines.

## Relations to the Other Subspaces

### Intersections

$$
\begin{aligned}
\mathbb{D}_2 \cap \mathbb{D}_3 &= S = \mathbb{R}\cdot 1, & \mathbb{D}_2 \cap V &= \mathbb{R} e_2, & \mathbb{D}_3 \cap V &= \mathbb{R} e_3, \\
\mathbb{D}_2 + \mathbb{D}_3 &= \operatorname{span}\{1, e_2, e_3\}, & \dim(\mathbb{D}_2 + \mathbb{D}_3) &= 3 .
\end{aligned}
$$

The sum $\mathbb{D}_2 + \mathbb{D}_3$ is not the whole algebra: it misses the line $\mathbb{R} e_1$, which is the intersection of $V$ with the definite plane $\mathbb{R}[e_1]$.

### The Coordinate Blocks

Together with the scalar line and the vector line complements, the two split-complex planes exhibit the algebra as built from its coordinate planes: $\mathbb{H}_{\mathrm{s}}$ is spanned by $S$, $\mathbb{R} e_1$, $\mathbb{R} e_2$, $\mathbb{R} e_3$, and the split-complex planes are $S \oplus \mathbb{R} e_2$ and $S \oplus \mathbb{R} e_3$. This is the **block decomposition** refined in *Split-Quaternion Relations Between Subspaces*.

## Comparison With the Centre of $\mathbb{B}$

The biquaternion algebra $\mathbb{B}$ is a $\mathbb{C}$-algebra: its centre $\mathbb{C} = \operatorname{span}\{1, i\}$ is a field and is central, and $\mathbb{B}$ is a free module of rank $4$ over it. The centre of $\mathbb{H}_{\mathrm{s}}$, by contrast, is only the one-dimensional scalar line $S = \mathbb{R}\cdot 1$, which is a field but too small to make the algebra an algebra over it in a non-trivial way. The subalgebras that bear the split-complex structure, $\mathbb{D}_2$ and $\mathbb{D}_3$, are commutative but **not** central; this is the precise sense in which the split-complex situation is the "non-central analogue" of the centre of $\mathbb{B}$. The centre of $\mathbb{B}$ is a field, so it has no idempotents other than $0$ and $1$; the split-complex planes are products $\mathbb{R} \oplus \mathbb{R}$, so they carry the nontrivial idempotents $\tilde\pi_{1,2}$ and $v_\pm$. The centre of $\mathbb{B}$ is developed in *Introduction to the Remarkable Subspaces*; the split-complex subalgebras are developed here.

## Examples

**Example (an idempotent of the first plane).** For $\tilde\pi_1 = \tfrac{1}{2}(1 + e_2)$ one has $\tilde\pi_1^2 = \tilde\pi_1$, with $e_2 \tilde\pi_1 = \tilde\pi_1$ and $\tilde\pi_2 \tilde\pi_1 = 0$; $N(\tilde\pi_1) = 0$, and $\tilde\pi_1$ is a zero divisor in $\mathbb{D}_2$ with $\tilde\pi_1 \tilde\pi_2 = 0$.

**Example (a unit of the second plane).** For $\tilde q = 2 + e_3$, the split-quaternion norm is $N = 4 - 1 = 3$, so $\tilde q$ is a unit with inverse $(2 - e_3)/3$.

**Example (the twisted multiplication).** Take $A_1 = 1$, $A_2 = e_2$, $B_1 = 1$, $B_2 = 0$ in $\mathbb{H}_{\mathrm{s}} = \mathbb{D}_2 \oplus \mathbb{D}_2 e_1$. Then $(1 + e_2 e_1)(1) = 1 + e_2 e_1 = 1 - e_1 e_2 = 1 - e_3$, while treating $e_1$ as commuting with $\mathbb{D}_2$ would give $1 + e_3$; the sign is the twist $e_1 e_2 = e_2^{\natural}\, e_1$. This is the concrete content of the twisted formula above.

**Example (the isotropic lines).** For the first plane, $(1 + e_2)(1 - e_2) = 0$; for the second, $(1 + e_3)(1 - e_3) = 0$. The four lines $\mathbb{R}(1\pm e_2)$, $\mathbb{R}(1\pm e_3)$ are the split-complex traces of the null cone.

## Summary

The split-quaternion algebra contains two commutative subalgebras $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ and $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$, each isomorphic to the split-complex numbers $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. They meet the scalar line in $\mathbb{R}\cdot 1$, meet the vector subspace in $\mathbb{R} e_2$ and $\mathbb{R} e_3$, and span together the three-dimensional space $\operatorname{span}\{1,e_2,e_3\}$.

The idempotents of $\mathbb{D}_2$ are the standard idempotents $\tilde\pi_{1,2} = \tfrac{1}{2}(1 \pm e_2)$, and those of $\mathbb{D}_3$ are $v_\pm = \tfrac{1}{2}(1 \pm e_3)$; in each plane they are central within the plane but not in the algebra. The split-quaternion norm restricts to $q_0^2 - q_2^2$ and $q_0^2 - q_3^2$, of signature $(1,1)$, and the zero divisors of each plane are the nonzero elements of its two isotropic lines $\mathbb{R}(1\pm e_2)$ and $\mathbb{R}(1\pm e_3)$. The algebra is a free rank-$2$ module over each plane, with the **twisted** multiplication in which the anticommuting generator acts through the conjugation of the coefficient plane; because the planes are not central, the structure is a module and not an algebra structure. This is the non-central analogue of the centre of the biquaternion algebra, which is central and a field and therefore carries no nontrivial idempotents.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\mathbb{D}$ | the split-complex numbers, $\mathbb{R}[j]/(j^2-1) \cong \mathbb{R}\oplus\mathbb{R}$ | *Split-Complex Algebra* |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | the first split-complex subspace | this article |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the second split-complex subspace | this article |
| $\tilde\pi_{1,2} = \tfrac{1}{2}(1\pm e_2)$ | the idempotents of $\mathbb{D}_2$ (standard idempotents) | *Split-Quaternion Idempotents and Projections* |
| $v_\pm = \tfrac{1}{2}(1\pm e_3)$ | the idempotents of $\mathbb{D}_3$ | this article |
| $e_\pm = \tfrac{1}{2}(1\pm j)$ | the idempotents of the abstract $\mathbb{D}$ | *Split-Complex Algebra* |
| $S = \mathbb{R}\cdot 1$, $V$ | the scalar and vector subspaces | *Split-Quaternion Scalar and Vector Subspaces* |
| $N(q_0+q_2e_2) = q_0^2-q_2^2$ | the form restricted to a split-complex plane, signature $(1,1)$ | this article |
| $\mathbb{R}(1\pm e_2)$, $\mathbb{R}(1\pm e_3)$ | the isotropic (zero-divisor) lines of the planes | *Split-Quaternion Zero Divisors* |
| $\bar{w}$ | the conjugation of a split-complex plane | this article |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the split-complex algebra and its realization inside low-dimensional Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the coquaternions and their split-complex subalgebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of a commutative algebra that is a product of fields, and for modules over a non-central subalgebra.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for hyperbolic planes and their isotropic lines.
