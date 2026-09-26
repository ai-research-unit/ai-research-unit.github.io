# __Biquaternion Centre Subspace__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four linear involutions, and each of them splits $\mathbb{B}$ into a fixed space and an anti-fixed space. Six of the eight spaces so obtained are four- or six-dimensional and are called the **six distinguished subspaces** of $\mathbb{B}$. This article treats the smallest of them, the **centre subspace** $\mathbb{C}_{\mathbb{B}}$, on its own: its definition, its basis, its algebra and module structure, the restriction of the norm form to it, its matrix image, and the action of the four involutions upon it. The other five are treated in the companion articles *Biquaternion Vector Subspace*, *Biquaternion Quaternion Subspace*, *Biquaternion Anti-Quaternion Subspace*, *Biquaternion Hermitian Subspace* and *Biquaternion Anti-Hermitian Subspace*; their relations with one another are collected in *Biquaternion Relations Between Subspaces*, and the involutions themselves in *Biquaternion Involution Lattice*.

Nothing below is a physical statement. The elements are written $\tilde{Q}, \tilde{R}, \tilde{P}, \dots$, their complex coefficients $Q_0, Q_1, Q_2, Q_3$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$; no other coordinates are used.

## Definition and Basis

### The Defining Involution

**Definition.** The **centre subspace** is the fixed space of quaternion conjugation,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = \tilde{Q} \right\} ,
$$

where quaternion conjugation is $\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3$.

Since $\bar{\cdot}$ is an involution, it has eigenvalues $\pm 1$ and $\mathbb{B}$ is the direct sum of its fixed space and its anti-fixed space; the anti-fixed space is the vector subspace $\mathrm{Vect}(\mathbb{B})$, treated in the companion article.

### The Condition in Coordinates

Writing $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ and comparing the two sides of $\bar{\tilde{Q}} = \tilde{Q}$ coefficient by coefficient:

- the coefficient of $e_0$ gives $Q_0 = Q_0$, which is no condition;
- the coefficient of $e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for each $k = 1, 2, 3$.

The centre subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_0 e_0 , \qquad Q_0 \in \mathbb{C} .
$$

### Basis and Dimension

**Proposition.** The centre subspace is a real vector space of dimension $2$, with basis $e_0, ie_0$. In terms of the real coordinates of $\mathbb{B}$ it is the coordinate plane

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} : q_1 = q_2 = q_3 = q'_1 = q'_2 = q'_3 = 0 \right\} ,
$$

in which the two free parameters are $q_0$ and $q'_0$.

**Proof.** The four complex coefficients of $\tilde{Q}$ reduce to $Q_0$ alone, and a complex number is a real pair, $Q_0 = q_0 + i q'_0$; the two elements $e_0$ and $ie_0$ are linearly independent over $\mathbb{R}$ and span the set. $\square$

The dimension count is recorded once and used throughout: of the six distinguished subspaces, $\mathbb{C}_{\mathbb{B}}$ is the only one of dimension $2$, the vector subspace $\mathrm{Vect}(\mathbb{B})$ is the only one of dimension $6$, and the remaining four are of dimension $4$.

## Algebra and Module Structure

### It Is the Centre of the Algebra

**Theorem.** $\mathbb{C}_{\mathbb{B}}$ is the centre of $\mathbb{B}$,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{X} \in \mathbb{B} : \tilde{X}\tilde{Q} = \tilde{Q}\tilde{X} \ \text{for every} \ \tilde{Q} \in \mathbb{B} \right\} .
$$

**Proof.** An element commutes with every other element if and only if it commutes with the basis elements $e_1, e_2, e_3$, and $Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ commutes with all three precisely when $Q_1 = Q_2 = Q_3 = 0$; the central elements are then the $\mathbb{C}$-multiples of $e_0$, which is the fixed space of $\bar{\cdot}$ computed above. $\square$

The two names of the subspace are therefore the same object described in two ways: it is the fixed space of one involution, and it is the centre of the algebra. Its elements are the **central elements**, and in the corpus's notation a central element is written $z e_0$ with $z \in \mathbb{C}$, or $\rho e_0$ when a modulus is in play.

### Subalgebra, Commutativity, Field Structure

**Proposition.** $\mathbb{C}_{\mathbb{B}}$ is a subalgebra of $\mathbb{B}$, it is commutative, and as a real algebra it is isomorphic to $\mathbb{C}$ by $Q_0 e_0 \mapsto Q_0$.

**Proof.** For two central elements, $Q_0 e_0 \cdot R_0 e_0 = (Q_0 R_0) e_0$, which lies in the subspace; commutativity is the commutativity of $\mathbb{C}$; and the displayed map is a bijective ring homomorphism because $e_0$ is the unit. $\square$

It is one of exactly two of the six distinguished subspaces that are subalgebras, the other being the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. Both are division algebras: $\mathbb{C}_{\mathbb{B}}$ is a field and $\mathbb{H}_{\mathbb{B}}$ is a division algebra. The centre subspace is also the only commutative one of the six.

### Ideals and Modules

Being the centre and a field, $\mathbb{C}_{\mathbb{B}}$ supports the simplest possible module and ideal structure: $\mathbb{B}$ is a free module of rank four over $\mathbb{C}_{\mathbb{B}}$, with basis $e_0, e_1, e_2, e_3$; and $\mathbb{C}_{\mathbb{B}}$ is not a proper two-sided ideal of $\mathbb{B}$, since $\mathbb{B}$ is simple and its only two-sided ideals are $0$ and $\mathbb{B}$ itself. The one-sided ideal theory of $\mathbb{B}$ is developed in *Biquaternion Ideals and Peirce Decomposition* and involves the idempotents, not the centre.

### Multiplication Tables

The products within the subspace and the products with the vector units that generate the whole algebra are

| product | value | product | value |
|---|---|---|---|
| $e_0 \cdot e_0$ | $e_0$ | $e_0 \cdot e_k$ | $e_k$ |
| $(ie_0) \cdot e_0$ | $ie_0$ | $(ie_0) \cdot e_k$ | $ie_k$ |
| $e_0 \cdot (ie_0)$ | $ie_0$ | $e_k \cdot e_0$ | $e_k$ |

for $k = 1, 2, 3$. The table is the statement that $\mathbb{C}_{\mathbb{B}}$ multiplies into every subspace and is multiplied into by every subspace, with no sign change: multiplication by a central element is a scalar extension, and the four subspaces $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ and the two sectors are all modules over $\mathbb{C}_{\mathbb{B}}$.

## The Norm Form

### Restriction

**Proposition.** On the centre subspace the norm form is the square of the coefficient,

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = Q_0^2 , \qquad \tilde{Q} = Q_0 e_0 .
$$

**Proof.** $\bar{\tilde{Q}} = \tilde{Q}$ on the subspace, so $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \tilde{Q}^2 = Q_0^2 e_0$, read as the scalar $Q_0^2$. $\square$

Two features are worth isolating, because they differ from the other five subspaces. First, $N$ takes **complex** values on $\mathbb{C}_{\mathbb{B}}$: it is real on $\mathbb{R}e_0$ and on $i\mathbb{R}e_0$ separately, but $Q_0^2$ is not real for a general complex $Q_0$. Second, its real restriction to the real two-plane is the form $\operatorname{diag}(1, -1)$ in the basis $e_0, ie_0$, since $N(e_0) = 1$ and $N(ie_0) = -1$. The centre subspace is thus one of the two subspaces on which the norm form is not real-valued, the other being the vector subspace.

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} = Q_0 e_0$, the following are equivalent:

1. $\tilde{Q}$ is a unit;
2. $N(\tilde{Q}) \neq 0$;
3. $Q_0 \neq 0$.

The inverse is $\tilde{Q}^{-1} = Q_0^{-1} e_0 = \dfrac{Q_0^{*}}{|Q_0|^2} e_0$.

**Proof.** $N(Q_0e_0) = Q_0^2$ vanishes exactly when $Q_0 = 0$; the inverse formula is verified directly, $Q_0 e_0 \cdot (Q_0^{-1} e_0) = e_0$, and $Q_0^{-1} = Q_0^{*}/|Q_0|^2$ is the standard expression of the complex inverse. $\square$

**Corollary.** The only zero divisor in $\mathbb{C}_{\mathbb{B}}$ is $0$, and the only non-unit is $0$.

**Proof.** A zero divisor is a non-zero element of zero norm form; on the subspace $N(\tilde{Q}) = Q_0^2$, which vanishes only at $Q_0 = 0$. $\square$

The corollary is the statement that $\mathbb{C}_{\mathbb{B}}$ is a field, and it is the reason the centre subspace carries none of the degeneracy phenomena — null elements, idempotents of zero norm form, unbounded families — that the vector subspace and the polar representation exhibit. The **idempotents** of the subspace are the solutions of $Q_0^2 = Q_0$, namely $Q_0 \in \{0, 1\}$: the zero element and the unit. In particular $\mathbb{C}_{\mathbb{B}}$ contains no non-trivial idempotent, while $\mathbb{B}$ contains many, all of them away from the centre.

## The Matrix Image

Under the matrix realization $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Representation*, an element of the centre subspace has image

$$
\Phi(Q_0 e_0) = \begin{pmatrix} Q_0 & 0 \\ 0 & Q_0 \end{pmatrix} = Q_0 I .
$$

**Proposition.** The image of $\mathbb{C}_{\mathbb{B}}$ is the set of scalar matrices, and the invariants of the image are

$$
\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0 , \qquad \det\Phi(\tilde{Q}) = Q_0^2 = N(\tilde{Q}) .
$$

**Proof.** Substituting $Q_1 = Q_2 = Q_3 = 0$ in the general matrix of the isomorphism leaves a diagonal matrix with equal entries; the trace and determinant are then immediate, and the determinant agrees with the norm form as it must, since $\det\Phi = N$ on the whole algebra. $\square$

The trace statement is the matrix form of the definition of the vector subspace as well: $\mathbb{C}_{\mathbb{B}}$ is not characterized by the trace, but its complement $\mathrm{Vect}(\mathbb{B})$ is, being exactly the traceless elements. The image of the centre is the subalgebra of scalar matrices, that is, the centre of $M_2(\mathbb{C})$, which is what the algebra isomorphism must do with the centre of $\mathbb{B}$.

## The Four Involutions on It

The four involutions of the algebra are quaternion conjugation $\bar{\cdot}$, complex conjugation ${}^{*}$, Hermitian conjugation ${}^{\dagger} = {}^{*} \circ \bar{\cdot} = \bar{\cdot} \circ {}^{*}$, and reversal $\flat = -\dagger$. Their action on $\mathbb{C}_{\mathbb{B}}$, in the basis $e_0, ie_0$, is diagonal:

| involution | $\tilde{Q} = Q_0e_0$ | matrix on $e_0, ie_0$ |
|---|---|---|
| $\bar{\cdot}$ | $Q_0 e_0$ | $\operatorname{diag}(1, 1)$ |
| ${}^{*}$ | $Q_0^{*} e_0$ | $\operatorname{diag}(1, -1)$ |
| ${}^{\dagger}$ | $Q_0^{*} e_0$ | $\operatorname{diag}(1, -1)$ |
| $\flat$ | $-Q_0^{*} e_0$ | $\operatorname{diag}(-1, 1)$ |

The subspace is invariant under all four, since each of them preserves the conditions $Q_1 = Q_2 = Q_3 = 0$; and the table has a content that is worth stating separately: **complex conjugation acts on the centre subspace as the non-trivial involution of $\mathbb{C}$**, exchanging the two real directions $e_0$ and $ie_0$. That is the only one of the four involutions that acts non-trivially on the centre, and it is the reason ${}^{*}$ is not an inner automorphism of $\mathbb{B}$: an inner automorphism fixes the centre pointwise, while ${}^{*}$ acts on it by the Galois involution $i \mapsto -i$. The point is developed in *Biquaternion Involution Lattice* and in *Biquaternion Automorphisms and Derivations*.

## Relations to the Other Five Subspaces

The intersections of $\mathbb{C}_{\mathbb{B}}$ with the other five distinguished subspaces are, with dimensions,

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B})$ | $\{0\}$ | $0$ |
| $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}}$ | $\mathbb{R} e_0$ | $1$ |
| $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{R} e_0$ | $1$ |
| $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_+$ | $\mathbb{R} e_0$ | $1$ |
| $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_-$ | $i\mathbb{R} e_0$ | $1$ |

The two lines $\mathbb{R}e_0$ and $i\mathbb{R}e_0$ that appear are the **coordinate blocks** of the algebra; the centre subspace is their direct sum,

$$
\mathbb{C}_{\mathbb{B}} = \mathbb{R}e_0 \oplus i\mathbb{R}e_0 ,
$$

the first line being its intersection with the quaternion and Hermitian subspaces at once, the second its intersection with the anti-quaternion and anti-Hermitian subspaces at once. This is the pattern that *Biquaternion Relations Between Subspaces* records for all six subspaces. The centre subspace is complementary to the vector subspace, $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, which is the scalar–vector decomposition of the algebra; with each of the other four subspaces it has intersection of dimension one, so none of those pairs spans $\mathbb{B}$.

## Examples

### A Central Element and Its Invariants

Take $\tilde{Q} = (3 + 4i)e_0$. Its norm form is

$$
N(\tilde{Q}) = (3+4i)^2 = -7 + 24i , \qquad |N(\tilde{Q})| = 25 = |3+4i|^2 ,
$$

so $\tilde{Q}$ is a unit, with inverse $\tilde{Q}^{-1} = \frac{3-4i}{25} e_0$. Its matrix image is $(3+4i)I$, of trace $6 + 8i$ and determinant $-7 + 24i$, in agreement with $\operatorname{Tr}\Phi = 2Q_0$ and $\det\Phi = N$. Complex conjugation acts on it by $\tilde{Q}^{*} = (3-4i)e_0$, which is a different element of the subspace; quaternion and Hermitian conjugations leave it unchanged, since $Q_1 = Q_2 = Q_3 = 0$ makes $\bar{\tilde{Q}} = \tilde{Q}^{\dagger} = \tilde{Q}$.

### The Unit and the Idempotents

The element $e_0$ has norm form $1$ and is the unit of the algebra; $ie_0$ has norm form $-1$ and satisfies $(ie_0)^2 = -e_0$, so the subspace contains the copy of the imaginary unit. The idempotents of $\mathbb{C}_{\mathbb{B}}$ are $0$ and $e_0$ only: the equation $Q_0^2 = Q_0$ has no other complex solution. No non-trivial idempotent of $\mathbb{B}$ is therefore central. The standard pair of non-trivial idempotents is

$$
\frac{e_0 + ie_1}{2} , \qquad \frac{e_0 - ie_1}{2} ,
$$

of scalar part $\tfrac12$, of zero norm form, and lying in the Hermitian subspace — so the idempotents that generate the minimal left ideals of $\mathbb{B}$ are constructed in the sector rather than in the centre, and the centre supplies only the two trivial ones.

### A Central Element Is Blind to the Left Multiplication

For the central element $\tilde{Q} = (1+i)e_0$, left and right multiplication by $\tilde{Q}$ coincide, and the operators are

$$
L_{\tilde{Q}}(x) = \tilde{Q}x = (1+i)x = R_{\tilde{Q}}(x) .
$$

The regular representations therefore agree on the centre, and $L_{ze_0}$ is the single operator $(1+i)\operatorname{id}$ on the eight-dimensional real space $\mathbb{B}$: a rotation by $\pi/4$ composed with a dilation by $\sqrt{2}$ on each of the four complex coordinate planes. The example is the arithmetic behind the statement that the centre acts by scalar extension, and it is the reason the central factor drops out of the operator representations of the algebra, as recorded in *Biquaternion Operator Representation*.

## Summary

The centre subspace $\mathbb{C}_{\mathbb{B}}$ is the fixed space of quaternion conjugation, the set of elements $\tilde{Q} = Q_0 e_0$ with vanishing vector part, a real vector space of dimension $2$ with basis $e_0, ie_0$. It coincides with the centre of the algebra; it is a commutative subalgebra, isomorphic to $\mathbb{C}$; it is one of the two subalgebras among the six distinguished subspaces and the only commutative one. Multiplication by its elements acts as scalar extension on every other subspace. The norm form restricts to $N = Q_0^2$, complex-valued on the subspace, of real signature $(1, 1)$; the units are exactly the elements with $Q_0 \neq 0$, they are all invertible, and there are no zero divisors except $0$. Its matrix image is the set of scalar matrices, with $2Q_0$ the trace and $Q_0^2$ the determinant. Of the four involutions, quaternion conjugation and Hermitian conjugation fix it pointwise, reversal negates it up to complex conjugation, and complex conjugation acts as the non-trivial involution $i \mapsto -i$ — the one action that no inner automorphism can reproduce. Its intersection with the vector subspace is the origin, and its intersections with each of the remaining four subspaces are the two coordinate lines $\mathbb{R}e_0$ and $i\mathbb{R}e_0$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, of real dimension $8$ |
| $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | a general element, $Q_\mu \in \mathbb{C}$ |
| $Q_\mu = q_\mu + iq'_\mu$ | the real and imaginary parts of a coefficient |
| $\mathbb{C}_{\mathbb{B}}$ | the centre subspace, the fixed space of quaternion conjugation |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the anti-fixed space of quaternion conjugation |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | the norm form |
| $\Phi$ | the isomorphism $\mathbb{B} \to M_2(\mathbb{C})$ |
| $\mathbb{R}e_0$, $i\mathbb{R}e_0$ | the two coordinate lines of the centre subspace |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the multiplication of $\mathbb{B}$, the three decompositions and the definitions of the six subspaces
- *Biquaternion Vector Subspace* (`articles_maths/biquaternion-vector-subspace.md`), the anti-fixed companion of the present subspace
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the intersections, the sums and the coordinate blocks of the six together
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions, their composition law and the two spaces each of them defines
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm form on the whole algebra and the invertibility criterion
- *Biquaternion 2×2 Matrix Representation* (`articles_maths/biquaternion-2x2-matrix-representation.md`), for the isomorphism $\Phi$ and the matrix picture of the subspaces
- *Jordan Algebras* (`articles_maths/jordan-algebras.md`), for the symmetrized product that gives the Hermitian subspace its algebraic structure
