
# __Split-Quaternion Split-Complex Subspaces__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ contains two copies of the split-complex numbers, namely the planes $\operatorname{span}\{1, \vec e_y\}$ and $\operatorname{span}\{1, \vec e_z\}$. Each is a commutative subalgebra isomorphic to $\mathbb{D} = \mathbb{R}[j]/(j^2 - 1)$, each carries its own pair of idempotents and its own pair of isotropic lines, and together they account for the reduction of the algebra to its split-complex pieces. This article studies them.

The split-complex subspaces are the split-quaternion analogues of the **centre** of the biquaternion algebra: in $\mathbb{B}$ the commutative, idempotent-bearing subalgebra is the centre $\mathbb{C}$, which is central. In $\mathbb{H}_{\mathrm{s}}$ the commutative, idempotent-bearing subalgebras are **not** central — the centre is only the scalar line $\mathbb{R}\cdot 1$ — so the module structure they give is a twisted one, and the contrast is the point of the article.

The article gives the two subalgebras, their bases, dimensions and defining conditions; their idempotents, which are exactly the standard idempotents $\tilde\pi_{1,2}$ for the first plane; the zero divisors they carry; the module structure of the algebra over each, with the twisted multiplication; and the comparison with the centre of $\mathbb{B}$. It closes with examples.

**Conventions.** The algebra $\mathbb{H}_{\mathrm{s}}$ has basis $1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_x^2 = -1$, $\vec e_y^2 = +1$, $\vec e_z = \vec e_x \vec e_y$, $\vec e_x \vec e_y = -\vec e_y \vec e_x$, and norm $\langle q_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z\rangle_{\natural} = q_t^2 + q_x^2 - q_y^2 - q_z^2$. The scalar subspace $S$ and the vector subspace $V$ are as in *Split-Quaternion Scalar and Vector Subspaces*. The split-complex numbers are $\mathbb{D} = \mathbb{R}[j]/(j^2-1) \cong \mathbb{R} \oplus \mathbb{R}$, an algebra over the commutative ring $\mathbb{R}$; their idempotents are $\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$.

## Definition and Basis

**Definition.** The two **split-complex subspaces** of $\mathbb{H}_{\mathrm{s}}$ are

$$
\mathbb{D}_2 = \operatorname{span}\{1, \vec e_y\}, \qquad \mathbb{D}_3 = \operatorname{span}\{1, \vec e_z\}.
$$

Each is the $\mathbb{R}$-linear span of the scalar unit and one hyperbolic basis element.

**Proposition.** Each of $\mathbb{D}_2, \mathbb{D}_3$ is a two-dimensional commutative subalgebra with identity, isomorphic to $\mathbb{D}$ by $j \mapsto \vec e_y$ and $j \mapsto \vec e_z$ respectively. Their intersection and their relation to the scalar–vector splitting are

$$
\mathbb{D}_2 \cap \mathbb{D}_3 = S = \mathbb{R}\cdot 1, \qquad
\mathbb{D}_2 \cap V = \mathbb{R} \vec e_y, \qquad \mathbb{D}_3 \cap V = \mathbb{R} \vec e_z .
$$

**Proof.** Since $\vec e_y^2 = +1$ and $\vec e_z^2 = +1$, each span is closed under multiplication and commutative, so each is a subalgebra, and the unique $\mathbb{R}$-algebra map $j \mapsto \vec e_k$ is an isomorphism $\mathbb{D} \to \mathbb{D}_k$ because $j^2 = 1 = \vec e_k^2$. An element of $\mathbb{D}_2 \cap \mathbb{D}_3$ has the form $q_t + q_y\vec e_y = q_t + q_z \vec e_z$, and linear independence of $1, \vec e_y, \vec e_z$ forces $q_y = q_z = 0$, so the intersection is $S$. The last two identities are read off the bases.

The two subalgebras together with the definite plane $\mathbb{R}[\vec e_x] = \operatorname{span}\{1, \vec e_x\}$ exhaust the coordinate planes through the scalar line. The third, $\mathbb{R}[\vec e_x]$, is isomorphic to the complex numbers $\mathbb{C}$ because $\vec e_x^2 = -1$, and it is definite, but the menu asks only for the two split-complex planes, and $\mathbb{R}[\vec e_x]$ is recorded in *Split-Quaternion Algebra*.

## Algebra and Module Structure

### Idempotents of the Subspaces

Each split-complex subalgebra is isomorphic to $\mathbb{R} \oplus \mathbb{R}$ and therefore has exactly four idempotents: $0, 1$ and the two nontrivial ones $\tfrac{1}{2}(1 \pm j)$. In $\mathbb{H}_{\mathrm{s}}$ this gives

$$
\mathbb{D}_2: \quad \tilde\pi_1 = \tfrac{1}{2}(1 + \vec e_y), \quad \tilde\pi_2 = \tfrac{1}{2}(1 - \vec e_y),
$$

$$
\mathbb{D}_3: \quad v_+ = \tfrac{1}{2}(1 + \vec e_z), \quad v_- = \tfrac{1}{2}(1 - \vec e_z).
$$

The idempotents $\tilde\pi_{1,2}$ of the first plane are exactly the **standard idempotents** of the algebra, and the companion article *Split-Quaternion Idempotents and Projections* develops them; the pair $v_\pm$ plays the same role inside $\mathbb{D}_3$. In either plane the two idempotents are orthogonal and complete, $\tilde\pi_1\tilde\pi_2 = v_+v_- = 0$ and $\tilde\pi_1 + \tilde\pi_2 = v_+ + v_- = 1$, and both have norm zero, $\langle\tilde\pi_{1,2}\rangle_{\natural} = \langle v_\pm\rangle_{\natural} = 0$. Within its own plane each idempotent is central, because the plane is commutative; but it is not central in $\mathbb{H}_{\mathrm{s}}$, since $\vec e_x \tilde\pi_1 = \tfrac{1}{2}(\vec e_x + \vec e_z) \neq \tfrac{1}{2}(\vec e_x - \vec e_z) = \tilde\pi_1 \vec e_x$.

### Subalgebra, Commutativity, Ring Structure

As abstract rings, $\mathbb{D}_2 \cong \mathbb{D}_3 \cong \mathbb{R} \oplus \mathbb{R}$: the map sending $q_t + q_y \vec e_y$ to the pair $(q_t + q_y, q_t - q_y)$ is a ring isomorphism, inverse to $(r, s) \mapsto \tfrac{1}{2}(r+s) + \tfrac{1}{2}(r-s) \vec e_y$. Hence each split-complex subspace is a product of two copies of the field $\mathbb{R}$; it has exactly two maximal ideals, the kernels of the two projections, which are the spans of the idempotents $\tilde\pi_{1,2}$. Neither subspace is a field, and each has zero divisors.

### Multiplication Tables

On the basis of $\mathbb{D}_2$ the products are $1 \cdot 1 = 1$, $1 \cdot \vec e_y = \vec e_y$, $\vec e_y \cdot \vec e_y = 1$. On the basis of $\mathbb{D}_3$ the same table holds with $\vec e_y$ replaced by $\vec e_z$. The two subalgebras interact through the anticommutation $\vec e_y \vec e_z = -\vec e_z \vec e_y = -\vec e_x$, and their set of products is the whole algebra: $\mathbb{D}_2 \mathbb{D}_3 = \mathbb{H}_{\mathrm{s}}$.

### Module Structure and the Twisted Multiplication

The algebra is a free module of rank $2$ over each split-complex subspace, on the left and on the right. For $\mathbb{D}_2$ the decomposition is

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{D}_2 \oplus \mathbb{D}_2 \vec e_x, \qquad \mathbb{D}_2 \vec e_x = \operatorname{span}\{\vec e_x, \vec e_z\},
$$

a free left $\mathbb{D}_2$-module with basis $\{1, \vec e_x\}$; the same decomposition is a free right $\mathbb{D}_2$-module with the same basis. The two module structures differ, and the difference is the twist. Since $\vec e_x$ anticommutes with $\vec e_y$, passing $\vec e_x$ to the right of an element $A = q_t + q_y \vec e_y \in \mathbb{D}_2$ conjugates that element:

$$
\vec e_x A = \bar{A} \vec e_x, \qquad \bar{A} = q_t - q_y \vec e_y,
$$

where $\bar{\cdot}$ is the conjugation of the split-complex plane, the nontrivial involution of $\mathbb{D}$. Consequently the product in $\mathbb{H}_{\mathrm{s}}$, written in the $\mathbb{D}_2$-basis $\{1, \vec e_x\}$ as $\tilde q_1 = A_1 + A_2 \vec e_x$ and $\tilde q_2 = B_1 + B_2 \vec e_x$ with $A_i, B_i \in \mathbb{D}_2$, is the **twisted multiplication**

$$
(A_1 + A_2 \vec e_x)(B_1 + B_2 \vec e_x)
= \big(A_1 B_1 - A_2 \bar{B_2}\big) + \big(A_1 B_2 + A_2 \bar{B_1}\big)\vec e_x .
$$

This is the multiplication of a quaternion-like algebra over the commutative ring $\mathbb{D}_2$, in which the anticommuting generator $\vec e_x$ acts by the conjugation of the coefficient algebra. The same computation with $\vec e_y$ in place of $\vec e_x$ gives the rank-$2$ module structure over $\mathbb{D}_3$. Because $\mathbb{D}_2$ and $\mathbb{D}_3$ are not central, the algebra is a module and a bimodule over each, but not an algebra over either, and the twist $\bar{\cdot}$ is exactly what obstructs the algebra structure.

## The Split-Quaternion Norm

### Restriction

The split-quaternion norm restricts to each plane as the two-dimensional form

$$
\langle q_t + q_y \vec e_y\rangle_{\natural} = q_t^2 - q_y^2, \qquad \langle q_t + q_z \vec e_z\rangle_{\natural} = q_t^2 - q_z^2,
$$

of signature $(1,1)$. Each restriction is the hyperbolic or **Minkowski** form of the plane, indefinite and non-degenerate, and each is the form of the split-complex algebra itself.

### Units and Zero Divisors

In $\mathbb{D}_2$, an element $q_t + q_y\vec e_y$ is a unit of the algebra exactly when $q_t^2 \neq q_y^2$, with inverse $(q_t - q_y\vec e_y)/(q_t^2-q_y^2)$; the units form the two branches of the hyperbola $q_t^2 - q_y^2 \neq 0$. The non-units are the two isotropic lines

$$
\mathbb{R}(1 + \vec e_y), \qquad \mathbb{R}(1 - \vec e_y),
$$

on which $q_t = \pm q_y$; every nonzero element of these lines is a zero divisor, and indeed $(1+\vec e_y)(1-\vec e_y) = 0$. The same statements hold in $\mathbb{D}_3$ with the isotropic lines $\mathbb{R}(1\pm \vec e_z)$. The isotropic lines of the two planes, together with the scalar null direction, are the traces of the null cone of $\langle\cdot\rangle_{\natural}$ on the planes, and they are described in *Split-Quaternion Zero Divisors*.

**Proposition.** The zero divisors of $\mathbb{D}_2$ are exactly the nonzero elements of the two isotropic lines $\mathbb{R}(1 \pm \vec e_y)$, and the zero divisors of $\mathbb{D}_3$ are exactly the nonzero elements of $\mathbb{R}(1 \pm \vec e_z)$.

**Proof.** The split-quaternion norm of the plane has signature $(1,1)$, so its null set is the union of the two lines indicated, and an element is a unit if and only if its split-quaternion norm is nonzero, by the split-quaternion norm criterion of *Split-Quaternion Norm and Invertibility*; hence the non-units are exactly the nonzero null elements.

## The Structure of the Planes

Each plane is the span of two orthogonal idempotents. In $\mathbb{D}_2 = \operatorname{span}\{1, \vec e_y\}$ the element $\vec e_y$ is an involution, $\vec e_y^2 = +1$, with eigenvectors $1 \pm \vec e_y$ and eigenvalues $\pm 1$; in $\mathbb{D}_3 = \operatorname{span}\{1, \vec e_z\}$ the element $\vec e_z$ is an involution with eigenvectors $1 \pm \vec e_z$. Hence each plane is the direct sum of the two idempotent lines,

$$
\tilde\pi_{1,2} = \tfrac{1}{2}(1 \pm \vec e_y) \in \mathbb{D}_2, \qquad v_\pm = \tfrac{1}{2}(1 \pm \vec e_z) \in \mathbb{D}_3,
$$

with $\tilde\pi_1 + \tilde\pi_2 = 1$, $\tilde\pi_1 \tilde\pi_2 = 0$ and $v_+ + v_- = 1$, $v_+ v_- = 0$. Each plane carries its own splitting of the identity, the first along the $\vec e_y$-eigenlines and the second along the $\vec e_z$-eigenlines, and each is a copy of $\mathbb{R} \oplus \mathbb{R}$; the two planes are the two distinct embeddings of the split-complex algebra that contain the scalar line.

## The Involutions on Them

Both subalgebras are invariant under the two algebra maps that fix the scalar line and send $\vec e_y, \vec e_z$ to themselves or their negatives.

| involution | on $\mathbb{D}_2$ | on $\mathbb{D}_3$ |
|---|---|---|
| conjugation $\bar{\cdot}$ | $1 \mapsto 1$, $\vec e_y \mapsto -\vec e_y$ | $1 \mapsto 1$, $\vec e_z \mapsto -\vec e_z$ |
| principal $\alpha$ | $1 \mapsto 1$, $\vec e_y \mapsto -\vec e_y$ | $1 \mapsto 1$, $\vec e_z \mapsto \vec e_z$ |
| reversal $\rho$ | $1 \mapsto 1$, $\vec e_y \mapsto \vec e_y$ | $1 \mapsto 1$, $\vec e_z \mapsto -\vec e_z$ |

On $\mathbb{D}_2$ the conjugation and the principal involution agree and are the nontrivial involution of the split-complex plane, while the reversal is the identity there; on $\mathbb{D}_3$ it is the conjugation and the reversal that agree, while the principal involution is the identity. In both planes the nontrivial involution swaps the two idempotents, $\tilde\pi_1 \leftrightarrow \tilde\pi_2$ and $v_+ \leftrightarrow v_-$, and swaps the two isotropic lines.

## Relations to the Other Subspaces

### Intersections

$$
\begin{aligned}
\mathbb{D}_2 \cap \mathbb{D}_3 &= S = \mathbb{R}\cdot 1, & \mathbb{D}_2 \cap V &= \mathbb{R} \vec e_y, & \mathbb{D}_3 \cap V &= \mathbb{R} \vec e_z, \\
\mathbb{D}_2 + \mathbb{D}_3 &= \operatorname{span}\{1, \vec e_y, \vec e_z\}, & \dim(\mathbb{D}_2 + \mathbb{D}_3) &= 3 .
\end{aligned}
$$

The sum $\mathbb{D}_2 + \mathbb{D}_3$ is not the whole algebra: it misses the line $\mathbb{R} \vec e_x$, which is the intersection of $V$ with the definite plane $\mathbb{R}[\vec e_x]$.

### The Coordinate Blocks

Together with the scalar line and the vector line complements, the two split-complex planes exhibit the algebra as built from its coordinate planes: $\mathbb{H}_{\mathrm{s}}$ is spanned by $S$, $\mathbb{R} \vec e_x$, $\mathbb{R} \vec e_y$, $\mathbb{R} \vec e_z$, and the split-complex planes are $S \oplus \mathbb{R} \vec e_y$ and $S \oplus \mathbb{R} \vec e_z$. This is the **block decomposition** refined in *Split-Quaternion Relations Between Subspaces*.

## Comparison With the Centre of $\mathbb{B}$

The biquaternion algebra $\mathbb{B}$ is a $\mathbb{C}$-algebra: its centre $\mathbb{C} = \operatorname{span}\{1, i\}$ is a field and is central, and $\mathbb{B}$ is a free module of rank $4$ over it. The centre of $\mathbb{H}_{\mathrm{s}}$, by contrast, is only the one-dimensional scalar line $S = \mathbb{R}\cdot 1$, which is a field but too small to make the algebra an algebra over it in a non-trivial way. The subalgebras that bear the split-complex structure, $\mathbb{D}_2$ and $\mathbb{D}_3$, are commutative but **not** central; this is the precise sense in which the split-complex situation is the "non-central analogue" of the centre of $\mathbb{B}$. The centre of $\mathbb{B}$ is a field, so it has no idempotents other than $0$ and $1$; the split-complex planes are products $\mathbb{R} \oplus \mathbb{R}$, so they carry the nontrivial idempotents $\tilde\pi_{1,2}$ and $v_\pm$. The centre of $\mathbb{B}$ is developed in *Introduction to the Remarkable Subspaces*; the split-complex subalgebras are developed here.

## Examples

**Example (an idempotent of the first plane).** For $\tilde\pi_1 = \tfrac{1}{2}(1 + \vec e_y)$ one has $\tilde\pi_1^2 = \tilde\pi_1$, with $\vec e_y \tilde\pi_1 = \tilde\pi_1$ and $\tilde\pi_2 \tilde\pi_1 = 0$; $\langle\tilde\pi_1\rangle_{\natural} = 0$, and $\tilde\pi_1$ is a zero divisor in $\mathbb{D}_2$ with $\tilde\pi_1 \tilde\pi_2 = 0$.

**Example (a unit of the second plane).** For $\tilde q = 2 + \vec e_z$, the split-quaternion norm is $N = 4 - 1 = 3$, so $\tilde q$ is a unit with inverse $(2 - \vec e_z)/3$.

**Example (the twisted multiplication).** Take $A_1 = 1$, $A_2 = \vec e_y$, $B_1 = 1$, $B_2 = 0$ in $\mathbb{H}_{\mathrm{s}} = \mathbb{D}_2 \oplus \mathbb{D}_2 \vec e_x$. Then $(1 + \vec e_y \vec e_x)(1) = 1 + \vec e_y \vec e_x = 1 - \vec e_x \vec e_y = 1 - \vec e_z$, while treating $\vec e_x$ as commuting with $\mathbb{D}_2$ would give $1 + \vec e_z$; the sign is the twist $\vec e_x \vec e_y = \vec e_y^{\natural}\, \vec e_x$. This is the concrete content of the twisted formula above.

**Example (the isotropic lines).** For the first plane, $(1 + \vec e_y)(1 - \vec e_y) = 0$; for the second, $(1 + \vec e_z)(1 - \vec e_z) = 0$. The four lines $\mathbb{R}(1\pm \vec e_y)$, $\mathbb{R}(1\pm \vec e_z)$ are the split-complex traces of the null cone.

## Summary

The split-quaternion algebra contains two commutative subalgebras $\mathbb{D}_2 = \operatorname{span}\{1,\vec e_y\}$ and $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$, each isomorphic to the split-complex numbers $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. They meet the scalar line in $\mathbb{R}\cdot 1$, meet the vector subspace in $\mathbb{R} \vec e_y$ and $\mathbb{R} \vec e_z$, and span together the three-dimensional space $\operatorname{span}\{1,\vec e_y,\vec e_z\}$.

The idempotents of $\mathbb{D}_2$ are the standard idempotents $\tilde\pi_{1,2} = \tfrac{1}{2}(1 \pm \vec e_y)$, and those of $\mathbb{D}_3$ are $v_\pm = \tfrac{1}{2}(1 \pm \vec e_z)$; in each plane they are central within the plane but not in the algebra. The split-quaternion norm restricts to $q_t^2 - q_y^2$ and $q_t^2 - q_z^2$, of signature $(1,1)$, and the zero divisors of each plane are the nonzero elements of its two isotropic lines $\mathbb{R}(1\pm \vec e_y)$ and $\mathbb{R}(1\pm \vec e_z)$. The algebra is a free rank-$2$ module over each plane, with the **twisted** multiplication in which the anticommuting generator acts through the conjugation of the coefficient plane; because the planes are not central, the structure is a module and not an algebra structure. This is the non-central analogue of the centre of the biquaternion algebra, which is central and a field and therefore carries no nontrivial idempotents.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\mathbb{D}$ | the split-complex numbers, $\mathbb{R}[j]/(j^2-1) \cong \mathbb{R}\oplus\mathbb{R}$ | *Split-Complex Algebra* |
| $\mathbb{D}_2 = \operatorname{span}\{1,\vec e_y\}$ | the first split-complex subspace | this article |
| $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$ | the second split-complex subspace | this article |
| $\tilde\pi_{1,2} = \tfrac{1}{2}(1\pm \vec e_y)$ | the idempotents of $\mathbb{D}_2$ (standard idempotents) | *Split-Quaternion Idempotents and Projections* |
| $v_\pm = \tfrac{1}{2}(1\pm \vec e_z)$ | the idempotents of $\mathbb{D}_3$ | this article |
| $\Pi_{1,2} = \tfrac{1}{2}(1\pm j)$ | the idempotents of the abstract $\mathbb{D}$ | *Split-Complex Algebra* |
| $S = \mathbb{R}\cdot 1$, $V$ | the scalar and vector subspaces | *Split-Quaternion Scalar and Vector Subspaces* |
| $\langle q_t+q_y\vec e_y\rangle_{\natural} = q_t^2-q_y^2$ | the form restricted to a split-complex plane, signature $(1,1)$ | this article |
| $\mathbb{R}(1\pm \vec e_y)$, $\mathbb{R}(1\pm \vec e_z)$ | the isotropic (zero-divisor) lines of the planes | *Split-Quaternion Zero Divisors* |
| $\bar{w}$ | the conjugation of a split-complex plane | this article |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the split-complex algebra and its realization inside low-dimensional Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the coquaternions and their split-complex subalgebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of a commutative algebra that is a product of fields, and for modules over a non-central subalgebra.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for hyperbolic planes and their isotropic lines.
