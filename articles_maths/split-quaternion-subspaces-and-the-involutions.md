
# __Split-Quaternion Subspaces and the Involutions__

## Introduction

Three linear involutions act on the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$: the conjugation ${}^{\natural}$, the principal involution $\alpha$, and the reversal $\rho$. Each cuts the algebra into its $+1$ and $-1$ eigenspaces, and the three decompositions together refine the algebra into the pieces on which the analysis of *Split-Quaternion Analysis* is carried out. This article studies the involutions, their individual eigenspaces, and their common eigenspaces — the finest decomposition they produce.

The article gives the three involutions and their general properties of linearity and (anti-)automorphism type; the two composition relations among them; the eigenspaces of each involution taken separately; the common eigenspaces of the commuting pair $(\alpha, \rho)$, which is the finest decomposition; the reason one two-dimensional piece of that decomposition does not split further; and the relation to the operators the analysis places on the pieces. The group that the three involutions generate, and the lattice of their fixed spaces, are the subject of the companion article *Split-Quaternion Involution Lattice*.

**Conventions.** A split-quaternion is $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$, with $\vec e_x^2 = -1$, $\vec e_y^2 = +1$, $\vec e_z = \vec e_x \vec e_y$, $\vec e_x \vec e_y = -\vec e_y \vec e_x$; the split-quaternion norm is $\langle\tilde q\rangle_{\natural} = q_t^2 + q_x^2 - q_y^2 - q_z^2$. The scalar and vector subspaces are $S = \mathbb{R}\cdot 1$ and $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$, and the split-complex subalgebras are $\mathbb{D}_2 = \operatorname{span}\{1,\vec e_y\}$, $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$, as in *Split-Quaternion Scalar and Vector Subspaces* and *Split-Quaternion Split-Complex Subspaces*.

## The Three Involutions

**Definition.** The **conjugation** is the map ${}^{\natural}$ with

$$
\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z .
$$

The **principal involution** $\alpha$ is the algebra homomorphism defined on the generators by

$$
\alpha(\vec e_x) = -\vec e_x, \qquad \alpha(\vec e_y) = -\vec e_y, \qquad \alpha(\vec e_z) = \vec e_z,
$$

and the **reversal** $\rho$ is the algebra anti-homomorphism defined by

$$
\rho(\vec e_x) = \vec e_x, \qquad \rho(\vec e_y) = \vec e_y, \qquad \rho(\vec e_z) = -\vec e_z .
$$

On a general element,

$$
\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z, \quad
\alpha(\tilde q) = q_t - q_x \vec e_x - q_y \vec e_y + q_z \vec e_z, \quad
\rho(\tilde q) = q_t + q_x \vec e_x + q_y \vec e_y - q_z \vec e_z .
$$

### Linearity and Antilinearity, Automorphism and Anti-Automorphism

All three maps are $\mathbb{R}$-linear involutions: each fixes $\mathbb{R}$ pointwise and satisfies $T^2 = \operatorname{id}$. They differ in how they treat the product.

**Proposition.**

- $\alpha$ is an $\mathbb{R}$-**algebra automorphism**: $\alpha(\tilde q_1 \tilde q_2) = \alpha(\tilde q_1)\alpha(\tilde q_2)$ and $\alpha(1) = 1$.
- $\rho$ is an $\mathbb{R}$-**algebra anti-automorphism**: $\rho(\tilde q_1 \tilde q_2) = \rho(\tilde q_2)\rho(\tilde q_1)$ and $\rho(1) = 1$.
- ${}^{\natural}$ is an $\mathbb{R}$-algebra anti-automorphism as well: $(\tilde q_1 \tilde q_2)^{\natural} = \tilde q_2^{\natural}\,\tilde q_1^{\natural}$ and $\bar{1} = 1$.

**Proof.** For $\alpha$, it is defined on generators, where the relations are preserved: $\alpha(\vec e_x)^2 = (-\vec e_x)^2 = -1$, $\alpha(\vec e_y)^2 = (-\vec e_y)^2 = +1$, and $\alpha(\vec e_z) = \vec e_z = \vec e_x \vec e_y = \alpha(\vec e_x)\alpha(\vec e_y)$, since $(-\vec e_x)(-\vec e_y) = \vec e_x \vec e_y$; so $\alpha$ extends to an automorphism. For $\rho$, the products reverse: $\rho(\vec e_x \vec e_y) = \rho(\vec e_z) = -\vec e_z$, while $\rho(\vec e_y)\rho(\vec e_x) = \vec e_y \vec e_x = -\vec e_z$, and the other products are similar, so $\rho$ is an anti-automorphism. The conjugation is the composite $\tilde{q}^{\natural} = \alpha(\rho(\tilde q)) = \rho(\alpha(\tilde q))$, computed below, and the composite of an automorphism with an anti-automorphism is an anti-automorphism.

In components $\tilde q = q_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$ the three involutions act by their sign patterns:

$$
\tilde{q}^{\natural} = q_t - q_x\vec e_x - q_y\vec e_y - q_z\vec e_z, \quad
\alpha(\tilde q) = q_t - q_x\vec e_x - q_y\vec e_y + q_z\vec e_z, \quad
\rho(\tilde q) = q_t + q_x\vec e_x + q_y\vec e_y - q_z\vec e_z .
$$

### Composition

The three involutions satisfy the **composition relations**

$$
\tilde{q}^{\natural} = \alpha(\rho(\tilde q)) = \rho(\alpha(\tilde q)),
$$

so that, as maps, ${}^{\natural} = \alpha\rho = \rho\alpha$. Equivalently, $\alpha{}^{\natural} = \rho$ and $\rho{}^{\natural} = \alpha$. In particular $\alpha$ and $\rho$ commute, and the set $\{\operatorname{id}, \alpha, \rho, {}^{\natural}\}$ is closed under composition with every element of order two; it is the Klein four-group. The structure of this group and the way it permutes its members are developed in *Split-Quaternion Involution Lattice*.

## The Eigenspaces of Each Involution

Each involution $T$ with $T^2 = \operatorname{id}$ is diagonalisable with eigenvalues $\pm 1$, and the algebra splits as the direct sum of its $+1$ and $-1$ eigenspaces.

### The Conjugation

$$
S = \{\tilde q : \tilde{q}^{\natural} = \tilde q\} = \mathbb{R}\cdot 1, \qquad V = \{\tilde q : \tilde{q}^{\natural} = -\tilde q\} = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}.
$$

The fixed space is the scalar line, of dimension $1$; the anti-fixed space is the vector subspace, of dimension $3$. This is the scalar–vector decomposition of *Split-Quaternion Scalar and Vector Subspaces*.

### The Principal Involution

$$
\{\tilde q : \alpha(\tilde q) = \tilde q\} = \operatorname{span}\{1, \vec e_z\} = \mathbb{D}_3, \qquad \{\tilde q : \alpha(\tilde q) = -\tilde q\} = \operatorname{span}\{\vec e_x, \vec e_y\}.
$$

Both eigenspaces have dimension $2$. The fixed space is the split-complex plane $\mathbb{D}_3$; the anti-fixed space is the plane $\operatorname{span}\{\vec e_x,\vec e_y\}$, which carries the hyperbolic form $q_x^2 - q_y^2$ of signature $(1,1)$ and is spanned by the two basis elements that anticommute into $\pm \vec e_z$.

### The Reversal

$$
\{\tilde q : \rho(\tilde q) = \tilde q\} = \operatorname{span}\{1, \vec e_x, \vec e_y\}, \qquad \{\tilde q : \rho(\tilde q) = -\tilde q\} = \mathbb{R} \vec e_z .
$$

The fixed space has dimension $3$, and the anti-fixed space is the single line $\mathbb{R} \vec e_z$.

### Summary Table

| involution | $+1$ eigenspace | dimension | $-1$ eigenspace | dimension |
|---|---|---|---|---|
| ${}^{\natural}$ | $S = \mathbb{R}\cdot 1$ | $1$ | $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $3$ |
| $\alpha$ | $\operatorname{span}\{1,\vec e_z\} = \mathbb{D}_3$ | $2$ | $\operatorname{span}\{\vec e_x,\vec e_y\}$ | $2$ |
| $\rho$ | $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ | $3$ | $\mathbb{R} \vec e_z$ | $1$ |

## The Common Eigenspaces

Because $\alpha$ and $\rho$ commute, they are simultaneously diagonalisable, and the algebra decomposes into the four common eigenspaces of the pair $(\alpha, \rho)$, indexed by the sign pairs.

**Theorem.** The common eigenspaces of $\alpha$ and $\rho$ are

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R}\cdot 1 \;\oplus\; \operatorname{span}\{\vec e_x, \vec e_y\} \;\oplus\; \mathbb{R} \vec e_z,
$$

of dimensions $1, 2, 1$, on which the sign pair $(\alpha, \rho)$ takes the values $(+,+)$, $(-,+)$ and $(+,-)$ respectively. The sign pair $(-,-)$ does not occur.

**Proof.** The common $(+,+)$ space is the intersection of the two fixed spaces $\mathbb{D}_3 \cap \operatorname{span}\{1,\vec e_x,\vec e_y\}$, which consists of elements $q_t + q_z \vec e_z = q_t + q_x \vec e_x + q_y \vec e_y$; linear independence forces $q_z = 0$ and $q_x = q_y = 0$, giving $\mathbb{R}\cdot 1$. The $(-,+)$ space is $\operatorname{span}\{\vec e_x,\vec e_y\} \cap \operatorname{span}\{1,\vec e_x,\vec e_y\} = \operatorname{span}\{\vec e_x,\vec e_y\}$. The $(+,-)$ space is $\mathbb{D}_3 \cap \mathbb{R} \vec e_z = \mathbb{R} \vec e_z$. The $(-,-)$ space is $\operatorname{span}\{\vec e_x,\vec e_y\} \cap \mathbb{R} \vec e_z = \{0\}$. The three nonzero summands have dimensions $1 + 2 + 1 = 4$, so they exhaust $\mathbb{H}_{\mathrm{s}}$.

### The Triple Sign Pattern

Since the conjugation is the composite $\alpha\rho$, it acts on each common eigenspace of $(\alpha,\rho)$ by the product of the two signs. The three pieces are therefore also common eigenspaces of all three involutions, with sign patterns

$$
\mathbb{R}\cdot 1 : (+,+,+), \qquad \operatorname{span}\{\vec e_x,\vec e_y\} : (-,-,+), \qquad \mathbb{R} \vec e_z : (-,+,-),
$$

the entries being the signs of $({}^{\natural}, \alpha, \rho)$. The sign pattern $(-,-,-)$ does not occur, and neither does $(+,+,-)$; among the eight patterns, exactly those three with $\text{sign}({}^{\natural}) = \text{sign}(\alpha)\text{sign}(\rho)$ are realised, one per piece. This is the finest decomposition of the algebra produced by the three involutions, and it is the one used in *Split-Quaternion Relations Between Subspaces* and *Split-Quaternion Involution Lattice*.

### Why the Plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ Does Not Split

The plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ is the largest piece of the common decomposition, of dimension $2$, and none of the three involutions splits it. The reason is that all three act on it by a single scalar: the conjugation acts as $-1$ on the whole of $V \supseteq \operatorname{span}\{\vec e_x,\vec e_y\}$; the principal involution acts as $-1$ because $\alpha(\vec e_x) = -\vec e_x$ and $\alpha(\vec e_y) = -\vec e_y$; and the reversal acts as $+1$ because $\rho(\vec e_x) = \vec e_x$ and $\rho(\vec e_y) = \vec e_y$. An eigenspace of a linear involution carries no further structure that the involution can detect — it acts by one number — so no combination of these involutions can separate $\vec e_x$ from $\vec e_y$. The two directions are distinguished only by structures external to the involution group: the sign of the split-quaternion norm ($\langle \vec e_x\rangle_{\natural} = +1$, $\langle \vec e_y\rangle_{\natural} = -1$), which belongs to the geometry, and the split-complex subalgebra structure, since $1$ and $\vec e_y$ span $\mathbb{D}_2$ while $\vec e_x$ alone generates the definite plane $\mathbb{R}[\vec e_x] \cong \mathbb{C}$. The involution group is blind to that distinction, and the plane is the irreducible piece for it.

## The Reduction of the Labelled Spaces

The decomposition classifies each of the distinguished subspaces by the signs of the involutions on it:

| subspace | ${}^{\natural}$ | $\alpha$ | $\rho$ |
|---|---|---|---|
| $\mathbb{R}\cdot 1$ | $+$ | $+$ | $+$ |
| $\mathbb{R} \vec e_x$ | $-$ | $-$ | $+$ |
| $\mathbb{R} \vec e_y$ | $-$ | $-$ | $+$ |
| $\mathbb{R} \vec e_z$ | $-$ | $+$ | $-$ |
| $\operatorname{span}\{\vec e_x,\vec e_y\}$ | $-$ | $-$ | $+$ |
| $\mathbb{D}_2$ | mixed | mixed | $+$ |
| $\mathbb{D}_3$ | mixed | $+$ | mixed |
| $S \oplus V$ | mixed | mixed | mixed |

The table shows the reduction: the lines $\mathbb{R} \vec e_x$ and $\mathbb{R} \vec e_y$ carry the same sign pattern $(-,-,+)$ as their span, which is why they cannot be separated by the involutions, while the line $\mathbb{R} \vec e_z$ carries the distinct pattern $(-,+,-)$ and is thus the unique line isolated by the involutions.

## The Analysis on the Subspaces

Each involution splits the algebra into a **Hermitian part** (the $+1$ eigenspace) and an **anti-Hermitian part** (the $-1$ eigenspace), and the analysis associates a first-order operator to each part, with the inherited form fixing the type of the operator.

**The conjugation.** The split is $S \oplus V$; the Hermitian part $S$ carries the single derivative $\partial/\partial q_t$, and the anti-Hermitian part $V$ carries the vector operator $D = \vec e_x \partial/\partial q_x + \vec e_y \partial/\partial q_y + \vec e_z \partial/\partial q_z$. The square $D^2$ is the wave operator of the restricted form.

**The principal involution.** The split is $\mathbb{D}_3 \oplus \operatorname{span}\{\vec e_x,\vec e_y\}$. The Hermitian part is the split-complex plane $\mathbb{D}_3$ with form $q_t^2 - q_z^2$ of signature $(1,1)$; the anti-Hermitian part is the plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ with form $q_x^2 - q_y^2$, also of signature $(1,1)$. Each is a hyperbolic plane carrying a one-dimensional wave operator.

**The reversal.** The split is $\operatorname{span}\{1,\vec e_x,\vec e_y\} \oplus \mathbb{R} \vec e_z$. The Hermitian part has form $q_t^2 + q_x^2 - q_y^2$ of signature $(2,1)$ and carries a three-dimensional wave operator; the anti-Hermitian part is the line $\mathbb{R} \vec e_z$ with the negative-definite form $-q_z^2$ and carries the single derivative $\partial/\partial q_z$.

The type of each operator — elliptic or hyperbolic — is determined by the signature of the form on the piece and by nothing else, and the characteristic variety of a hyperbolic operator is exactly the zero divisor set of the piece. The full development is in *Split-Quaternion Analysis*.

## Examples

**Example (an element with a clean sign pattern).** For $\tilde q = \vec e_z$ the triple sign pattern is $({}^{\natural},\alpha,\rho) = (-,+,-)$: indeed $\vec e_z^{\natural} = -\vec e_z$, $\alpha(\vec e_z) = \vec e_z$, $\rho(\vec e_z) = -\vec e_z$. The line $\mathbb{R} \vec e_z$ is thus the unique line fixed by $\alpha$ and negated by $\rho$.

**Example (an element with the mixed plane pattern).** For $\tilde q = \vec e_x + \vec e_y$, the image under the involutions is $\tilde{q}^{\natural} = -\vec e_x - \vec e_y$, $\alpha(\tilde q) = -\vec e_x - \vec e_y$, $\rho(\tilde q) = \vec e_x + \vec e_y$, so the triple sign pattern is $(-,-,+)$, the same as for $\vec e_x$ and for $\vec e_y$ separately. The three vectors $\vec e_x, \vec e_y, \vec e_x + \vec e_y$ are all in the same common eigenspace, which exhibits the failure to split the plane.

**Example (composition).** For $\tilde q = \vec e_x + \vec e_z$: $\alpha(\rho(\tilde q)) = \alpha(\vec e_x - \vec e_z) = -\vec e_x - \vec e_z = \tilde{q}^{\natural}$, and $\rho(\alpha(\tilde q)) = \rho(-\vec e_x + \vec e_z) = -\vec e_x - \vec e_z = \tilde{q}^{\natural}$, verifying ${}^{\natural} = \alpha\rho = \rho\alpha$ on this element.

**Example (the three involutions on a general element).** For $\tilde q = 1 + \vec e_x + \vec e_y + \vec e_z$ the three images are $\tilde{q}^{\natural} = 1 - \vec e_x - \vec e_y - \vec e_z$, $\alpha(\tilde q) = 1 - \vec e_x - \vec e_y + \vec e_z$ and $\rho(\tilde q) = 1 + \vec e_x + \vec e_y - \vec e_z$, exhibiting the sign patterns $(+,+,+)$ for the scalar, $(-,-,-)$ for the conjugation, $(-,-,+)$ for the principal involution and $(+,+,-)$ for the reversal.

## Summary

Three $\mathbb{R}$-linear involutions act on $\mathbb{H}_{\mathrm{s}}$: the conjugation ${}^{\natural}$ (an anti-automorphism), the principal involution $\alpha$ (an automorphism), and the reversal $\rho$ (an anti-automorphism). They satisfy ${}^{\natural} = \alpha\rho = \rho\alpha$, so $\alpha$ and $\rho$ commute and the three generate the Klein four-group.

Each involution splits the algebra into its $+1$ and $-1$ eigenspaces: the conjugation gives $S$ (dimension $1$) and $V$ (dimension $3$); the principal involution gives the split-complex plane $\operatorname{span}\{1,\vec e_z\}$ and the plane $\operatorname{span}\{\vec e_x,\vec e_y\}$, both of dimension $2$; the reversal gives the three-dimensional space $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ and the line $\mathbb{R} \vec e_z$. The common eigenspaces of the commuting pair $(\alpha,\rho)$ give the finest decomposition

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R}\cdot 1 \oplus \operatorname{span}\{\vec e_x,\vec e_y\} \oplus \mathbb{R} \vec e_z,
$$

with triple sign patterns $({}^{\natural},\alpha,\rho)$ equal to $(+,+,+)$, $(-,-,+)$ and $(-,+,-)$. The plane $\operatorname{span}\{\vec e_x,\vec e_y\}$ does not split, because all three involutions act on it by a single scalar; only the split-quaternion norm and the subalgebra structure distinguish $\vec e_x$ from $\vec e_y$. Each eigenspace carries the operator of *Split-Quaternion Analysis*, of type fixed by the signature of the inherited form.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| ${}^{\natural}$ | the conjugation, $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ | *Split-Quaternion Algebra* |
| $\alpha$ | the principal involution, $\alpha(\vec e_x)=-\vec e_x$, $\alpha(\vec e_y)=-\vec e_y$, $\alpha(\vec e_z)=\vec e_z$ | *Split-Quaternion Algebra* |
| $\rho$ | the reversal, $\rho(\vec e_x)=\vec e_x$, $\rho(\vec e_y)=\vec e_y$, $\rho(\vec e_z)=-\vec e_z$ | *Split-Quaternion Algebra* |
| $S = \mathbb{R}\cdot 1$ | the $+1$ eigenspace of the conjugation | *Split-Quaternion Scalar and Vector Subspaces* |
| $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | the $-1$ eigenspace of the conjugation | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathbb{D}_2, \mathbb{D}_3$ | the split-complex subspaces $\operatorname{span}\{1,\vec e_y\}$, $\operatorname{span}\{1,\vec e_z\}$ | *Split-Quaternion Split-Complex Subspaces* |
| $\operatorname{span}\{\vec e_x,\vec e_y\}$ | the unsplittable common $(-,-,+)$ piece | this article |
| $D = \vec e_x\partial/\partial q_x + \vec e_y\partial/\partial q_y + \vec e_z\partial/\partial q_z$ | the vector operator on $V$ | *Split-Quaternion Analysis* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for involutions, their eigenspace decompositions and the Peirce-type decompositions they induce.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the grading and reversal involutions of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the conjugation, reversal and grade involutions and their composition rules.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the general theory of involutions on an algebra and their fixed subspaces.
