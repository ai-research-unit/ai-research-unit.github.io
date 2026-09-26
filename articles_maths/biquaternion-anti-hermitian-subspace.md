# __Biquaternion Anti-Hermitian Subspace__

## Introduction

The **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed space of reversal, equivalently the anti-fixed space of Hermitian conjugation: the elements of $\mathbb{B}$ whose scalar part is purely imaginary and whose vector part is real. It is the image of the Hermitian subspace under multiplication by the central imaginary unit, the two together decomposing the algebra. It is not a subalgebra; it is closed under the commutator and its symmetrized product lands in $\mathbb{M}_+$; and the norm form on it is real, of signature $(3,1)$, so that its zero divisors form an isotropic cone.

The article parallels *Biquaternion Hermitian Subspace*, to which it is tied by the central imaginary unit at every step: the products, the quadratic form, the idempotents and the involutions of the two subspaces correspond, with a sign turned each time. The notation is as in the companion articles.

## Definition and Basis

### The Defining Involution

**Definition.** The **anti-Hermitian subspace** is

$$
\mathbb{M}_- = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\flat} = \tilde{Q} \right\} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\dagger} = -\tilde{Q} \right\} ,
$$

where $\flat = -\dagger$ is the reversal, $\tilde{Q}^{\flat} = -Q_0^{*}e_0 + Q_1^{*}e_1 + Q_2^{*}e_2 + Q_3^{*}e_3$. Both descriptions define the same subspace because $\flat$ and $\dagger$ have the same eigenspaces with the signs exchanged.

### The Condition in Coordinates

Comparing $\tilde{Q}^{\dagger} = -\tilde{Q}$ coefficient by coefficient:

- $-Q_0^{*} = Q_0$, so $Q_0 = iq'_0$ is purely imaginary;
- $Q_k^{*} = Q_k$, so each vector coefficient $Q_k = q_k$ is real.

The subspace is therefore

$$
\mathbb{M}_- = \left\{ \tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 : \ q'_0, q_1, q_2, q_3 \in \mathbb{R} \right\} ,
$$

the imaginary scalar part together with the real vector part.

### Basis and Dimension

**Proposition.** $\mathbb{M}_-$ is a real vector space of dimension $4$, with basis $ie_0, e_1, e_2, e_3$, and it decomposes along the coordinate blocks it meets,

$$
\mathbb{M}_- = i\mathbb{R}e_0 \oplus \operatorname{span}\{e_1,e_2,e_3\} .
$$

Moreover $\mathbb{M}_- = i\,\mathbb{M}_+$: multiplication by the central imaginary unit maps the Hermitian subspace isomorphically onto the anti-Hermitian one, and $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$.

**Proof.** Four real parameters with the four displayed basis elements independent over $\mathbb{R}$; for the last part, $i(q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3) = iq_0e_0 - q'_1e_1 - q'_2e_2 - q'_3e_3$, which is of the stated form, and the map is bijective. $\square$

## Algebra and Module Structure

### It Is Not a Subalgebra

**Proposition.** For $\tilde{Q} = iq'_0e_0 + \mathbf{q}$ and $\tilde{R} = ir'_0e_0 + \mathbf{r}$ with $\mathbf{q}, \mathbf{r}$ real vectors,

$$
\tilde{Q}\tilde{R} = \left(-q'_0r'_0 - (\mathbf{q},\mathbf{r})\right)e_0 + i\left(q'_0\mathbf{r} + r'_0\mathbf{q}\right) + \mathbf{q}\times\mathbf{r} ,
$$

and the product lies in $\mathbb{M}_-$ exactly when its scalar part vanishes and its vector part is real, that is when

$$
(\mathbf{q},\mathbf{r}) + q'_0r'_0 = 0 \qquad \text{and} \qquad q'_0\mathbf{r} + r'_0\mathbf{q} = 0 .
$$

**Proof.** The scalar term is real for every pair, so it lies in $\mathbb{M}_-$ only when it is zero — that is the first equation; the vector part is the sum of the real vector $\mathbf{q}\times\mathbf{r}$ and the imaginary vector $i(q'_0\mathbf{r}+r'_0\mathbf{q})$, so it is real exactly when the second equation holds. $\square$

The two conditions are independent: $e_1e_2 = e_3$ satisfies both and lies in the subspace, while $e_1^2 = -e_0$ fails the first, its scalar part being real. So the subspace is closed under neither multiplication nor squaring.

### The Symmetrized Product Lands in the Hermitian Subspace

**Theorem.** For $\tilde{Q}, \tilde{R} \in \mathbb{M}_-$ one has $\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q} \in \mathbb{M}_+$, and $\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} \in \mathbb{M}_-$.

**Proof.** $\dagger$ reverses products and equals $-\mathrm{id}$ on $\mathbb{M}_-$, so $(\tilde{Q}\tilde{R})^{\dagger} = \tilde{R}^{\dagger}\tilde{Q}^{\dagger} = \tilde{Q}\tilde{R}$; hence $\tilde{Q}\tilde{R}$ is Hermitian, and the same holds for $\tilde{R}\tilde{Q}$, giving the first statement. For the second, $(\tilde{Q}\tilde{R}-\tilde{R}\tilde{Q})^{\dagger} = \tilde{Q}\tilde{R}-\tilde{R}\tilde{Q} = -(\tilde{Q}\tilde{R}-\tilde{R}\tilde{Q})$, using the anti-commutation just proved. $\square$

The theorem is the mirror image of the corresponding statement for $\mathbb{M}_+$: there the commutator falls into $\mathbb{M}_-$ and the symmetrized product stays, here the roles are exchanged. Both are instances of the same identity, $\dagger$ reversing products and acting on each subspace by a sign.

### It Is a Lie Subalgebra

**Theorem.** With the commutator, $\mathbb{M}_-$ is a real Lie algebra of dimension four, isomorphic to $\mathbb{R} \oplus \mathfrak{su}(2)$; the central line $i\mathbb{R}e_0$ is an abelian ideal and the quotient is the three-dimensional cross-product Lie algebra of the real vectors.

**Proof.** The subspace is closed under the commutator by the theorem above; the brackets with the central element vanish, $[ie_0, \tilde{Q}] = 0$; and on the real vector triple the bracket is twice the cross product, $[e_j,e_k] = 2e_{j\times k}$, which is $\mathfrak{su}(2)$ up to the factor. $\square$

### Modules and the Correspondence with $\mathbb{M}_+$

$\mathbb{M}_-$ is a module over the centre subspace, and it is not a module over the quaternion subspace, since $e_1 \cdot ie_0 = ie_1$ leaves the subspace. The correspondence with $\mathbb{M}_+$ through multiplication by $i$ is an isomorphism of real vector spaces and reverses the two products in the following sense: for $\tilde{Q}, \tilde{R} \in \mathbb{M}_+$,

$$
(i\tilde{Q})(i\tilde{R}) = -\tilde{Q}\tilde{R} , \qquad (i\tilde{Q}) \circ (i\tilde{R}) = -(\tilde{Q}\circ\tilde{R}) ,
$$

so the symmetrized product of two elements of $\mathbb{M}_-$ is minus the symmetrized product of the corresponding Hermitian elements, and the Jordan algebra structure of $\mathbb{M}_+$ is transported to a Jordan structure on $\mathbb{M}_-$ with the sign of the product reversed.

### The Square

**Proposition.** For $\tilde{Q} = iq'_0e_0 + \mathbf{q}$ with $\mathbf{q}$ a real vector,

$$
\tilde{Q}^2 = -\left((q'_0)^2 + |\mathbf{q}|^2\right)e_0 + 2iq'_0\mathbf{q} \in \mathbb{M}_+ .
$$

In particular the scalar part of the square is negative definite, and $\tilde{Q}^2$ is never the unit: the anti-Hermitian subspace contains no root of plus one.

**Proof.** Expanding with $\mathbf{q}^2 = -|\mathbf{q}|^2e_0$ and the centrality of $i$ gives the displayed element, whose scalar part is $-\left((q'_0)^2+|\mathbf{q}|^2\right) \leq 0$ and whose vector part is imaginary, so it lies in $\mathbb{M}_+$; the scalar part cannot equal $1$, so $\tilde{Q}^2 \neq e_0$, and it vanishes only for $\tilde{Q} = 0$. $\square$

## The Norm Form

### Restriction and Signature

**Theorem.** On the anti-Hermitian subspace the norm form is the real quadratic form

$$
N(\tilde{Q}) = (q_1^2 + q_2^2 + q_3^2) - (q'_0)^2 , \qquad \tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 ,
$$

of signature $(3,1)$, related to the Hermitian case by $N(i\tilde{P}) = -N(\tilde{P})$ for $\tilde{P} \in \mathbb{M}_+$. Its polar form is $B(\tilde{Q},\tilde{R}) = (\mathbf{q},\mathbf{r}) - q'_0r'_0$.

**Proof.** Substituting $Q_0 = iq'_0$ and $Q_k = q_k$ in $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ gives $(iq'_0)^2 + \sum_k q_k^2 = -(q'_0)^2 + |\mathbf{q}|^2$; the signs of the basis elements $ie_0, e_1, e_2, e_3$ are $-,-,+,\dots$ — that is, $-1$ on the central imaginary line and $+1$ on the three real vector directions. The relation to the Hermitian case is the centrality of $i$ together with $i^2 = -1$. $\square$

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} \in \mathbb{M}_-$ the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q}$ is not a zero divisor. The zero divisors are exactly the non-zero elements of the **isotropic cone**

$$
q_1^2 + q_2^2 + q_3^2 = (q'_0)^2 ,
$$

of real dimension three, and none of them is nilpotent.

**Proof.** The equivalence of the first two conditions is the general criterion, and the identity $\tilde{Q}\tilde{R} = 0$ forces $N(\tilde{Q})N(\tilde{R}) = 0$, giving the third. For the nilpotency statement, the square formula shows that $\tilde{Q}^2 = 0$ requires both the scalar part $-\left((q'_0)^2+|\mathbf{q}|^2\right)$ and the vector part $2q'_0\mathbf{q}$ to vanish, hence $\tilde{Q} = 0$. $\square$

An example of a zero-divisor pair is given by the images under multiplication by $i$ of an orthogonal pair of idempotents of $\mathbb{M}_+$: with $\tilde{E}_+ = \tfrac12(e_0+ie_1)$ and $\tilde{E}_- = \tfrac12(e_0-ie_1)$ one has

$$
(i\tilde{E}_+)(i\tilde{E}_-) = -\tilde{E}_+\tilde{E}_- = 0 , \qquad i\tilde{E}_\pm = \frac{ie_0 \mp e_1}{2} \in \mathbb{M}_- ,
$$

so the nilpotent-free zero divisors of the subspace are produced by the orthogonal idempotents of the Hermitian subspace, transported by $i$.

### The Roots of Minus One

**Proposition.** Inside $\mathbb{M}_-$ the roots of minus one are

$$
\left\{ \tilde{Q} : \tilde{Q}^2 = -e_0 \right\} = \left\{ iq'_0e_0 + \mathbf{q} : (q'_0)^2 + |\mathbf{q}|^2 = 1 , \ q'_0\mathbf{q} = 0 \right\} ,
$$

which is the disjoint union of the unit sphere in $\operatorname{span}\{e_1,e_2,e_3\}$ and the two elements $\pm ie_0$. There is no root of plus one.

**Proof.** The square formula gives $\tilde{Q}^2 = -\left((q'_0)^2+|\mathbf{q}|^2\right)e_0 + 2iq'_0\mathbf{q}$; the equation $\tilde{Q}^2 = -e_0$ requires $q'_0\mathbf{q} = 0$ and $(q'_0)^2+|\mathbf{q}|^2 = 1$, whose solutions are $q'_0 = 0$ with $|\mathbf{q}| = 1$, or $\mathbf{q} = 0$ with $q'_0 = \pm1$. The equation $\tilde{Q}^2 = e_0$ would require the scalar part $-\left((q'_0)^2+|\mathbf{q}|^2\right)$ to equal $1$, which is impossible. $\square$

The statement is the exact counterpart of the Hermitian case, where the roots of plus one are the unit sphere of the imaginary vector triple together with the pair $\pm e_0$, and there is no root of minus one: multiplication by $i$ maps the roots of plus one in $\mathbb{M}_+$ bijectively onto the roots of minus one in $\mathbb{M}_-$, sending the sphere of imaginary unit vectors to the sphere of real unit vectors and the pair $\pm e_0$ to the pair $\pm ie_0$. Each of the two sectors therefore carries a two-sphere together with two isolated points of roots of one sign, and no root of the other sign.

## The Matrix Image

**Proposition.** Under the matrix realization,

$$
\Phi\!\left(\mathbb{M}_-\right) = \left\{ M \in M_2(\mathbb{C}) : M = -M^{\dagger} \right\} ,
$$

the anti-Hermitian matrices, that is $i$ times the Hermitian ones, and

$$
\operatorname{Tr}\Phi(\tilde{Q}) = 2iq'_0 , \qquad \det\Phi(\tilde{Q}) = N(\tilde{Q}) \in \mathbb{R} .
$$

**Proof.** The anti-fixed space of $\dagger$ corresponds under the isomorphism to the anti-fixed space of the conjugate transpose; the trace of the general matrix with imaginary scalar and real vector coefficients is $2iq'_0$ and its determinant is the norm form, which is real on the subspace by the theorem above. $\square$

As an instance, $\Phi(ie_0 + e_1) = \begin{pmatrix} i & -i \\ -i & i\end{pmatrix}$, an anti-Hermitian matrix of trace $2i$ and determinant $-(q'_0)^2 + q_1^2 = 0$ — a singular anti-Hermitian matrix, corresponding to the null element $ie_0 + e_1$ of the cone.

## The Four Involutions on It

In the basis $ie_0, e_1, e_2, e_3$:

| involution | matrix | effect |
|---|---|---|
| $\bar{\cdot}$ | $\operatorname{diag}(1,-1,-1,-1)$ | negates the real vector part |
| ${}^{*}$ | $\operatorname{diag}(-1,1,1,1)$ | negates the central imaginary line |
| ${}^{\dagger}$ | $-\mathrm{id}$ | minus the identity |
| $\flat$ | $+\mathrm{id}$ | the identity, by definition of the subspace |

The subspace is invariant under all four. Reversal fixes it pointwise, which is its defining property; Hermitian conjugation acts as its negative; complex conjugation negates the central imaginary line and fixes the real vectors; and quaternion conjugation does the opposite, negating the real vectors and fixing the central line. The rows are consistent with $\dagger = {}^{*}\circ\bar{\cdot}$ and $\flat = -\dagger$.

## Relations to the Other Five Subspaces

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{M}_- \cap \mathbb{C}_{\mathbb{B}}$ | $i\mathbb{R}e_0$ | $1$ |
| $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{B})$ | $\operatorname{span}\{e_1,e_2,e_3\}$ | $3$ |
| $\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{e_1,e_2,e_3\}$ | $3$ |
| $\mathbb{M}_- \cap i\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{R}e_0$ | $1$ |
| $\mathbb{M}_- \cap \mathbb{M}_+$ | $\{0\}$ | $0$ |

The subspace is complementary to $\mathbb{M}_+$, and its decomposition along the coordinate blocks is $\mathbb{M}_- = i\mathbb{R}e_0 \oplus \operatorname{span}\{e_1,e_2,e_3\}$: the imaginary scalar line is shared with the centre and anti-quaternion subspaces, the real vector triple with the quaternion and vector subspaces. Its sums with the centre and with $\mathbb{H}_{\mathbb{B}}$ have dimension $5$, and its sums with the vector subspace and with $i\mathbb{H}_{\mathbb{B}}$ have dimension $7$; only the pair with $\mathbb{M}_+$ spans the algebra.

## Examples

### A Unit, a Null Element, an Inverse

Take $\tilde{Q} = e_1 + ie_0$. Its norm form is $N(\tilde{Q}) = 1 - 1 = 0$, so it is a zero divisor on the cone, and

$$
\tilde{Q}^2 = -(1+1)e_0 + 2i e_1 = -2e_0 + 2ie_1 ,
$$

a Hermitian element with negative scalar part, and not a multiple of $\tilde{Q}$: the element is not an idempotent and no multiple of it is one, in contrast with the Hermitian case. Its matrix image is $\begin{pmatrix} 2i & -i \\ -i & 0\end{pmatrix}$, of rank one. Take instead $\tilde{Q} = ie_0 + e_1 + e_2$: then $N(\tilde{Q}) = 2 - 1 = 1$, a unit with

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})} = ie_0 - e_1 - e_2 ,
$$

again in the subspace, since quaternion conjugation preserves it and the norm form is real.

### A Zero-Divisor Pair

With $\tilde{P} = \tfrac12(ie_0 - e_1)$ and $\tilde{R} = \tfrac12(ie_0 + e_1)$, both in the subspace, one has

$$
\tilde{P}\tilde{R} = \frac{(ie_0-e_1)(ie_0+e_1)}{4} = \frac{i^2e_0 + ie_0e_1 - e_1ie_0 - e_1^2}{4} = \frac{-e_0 + ie_1 - ie_1 + e_0}{4} = 0 ,
$$

a zero-divisor pair of null elements, transported by $i$ from the orthogonal idempotents of the Hermitian subspace. The computation exhibits at once the two mechanisms: the cancellation of the scalar parts through the signs and the cancellation of the vector parts through the anti-commuting products.

### A Lie Bracket

For $\tilde{Q} = e_1$ and $\tilde{R} = e_2$, both in the subspace,

$$
[\tilde{Q}, \tilde{R}] = e_1e_2 - e_2e_1 = e_3 + e_3 = 2e_3 \in \mathbb{M}_- ,
$$

and for $\tilde{Q} = ie_0$ the bracket with any element vanishes, $[ie_0, \tilde{R}] = 0$, since $ie_0$ is central. The two computations are the abelian ideal and the quotient of the structure theorem.

## Summary

The anti-Hermitian subspace $\mathbb{M}_-$ is the fixed space of reversal, equivalently the anti-fixed space of Hermitian conjugation, the set of elements with imaginary scalar part and real vector part: a real vector space of dimension $4$ with basis $ie_0, e_1, e_2, e_3$, equal to $i\mathbb{M}_+$ and complementary to $\mathbb{M}_+$. It is not a subalgebra; its symmetrized product lands in $\mathbb{M}_+$ while its commutator stays inside, so that it is a real Lie algebra $\mathbb{R} \oplus \mathfrak{su}(2)$ with the central imaginary line as an abelian ideal. The square of one of its elements is always Hermitian, with negative definite scalar part, so the subspace contains no root of plus one; its roots of minus one are the unit sphere of the real vector triple together with the two elements $\pm ie_0$. The norm form restricts to $|\mathbf{q}|^2 - (q'_0)^2$, real of signature $(3,1)$, the negative of the Hermitian form; the units are the elements off the isotropic cone $|\mathbf{q}|^2 = (q'_0)^2$, the zero divisors are the non-zero elements of the cone, and none of them is nilpotent. Its matrix image is the set of anti-Hermitian matrices, with trace $2iq'_0$ and determinant $N$. Reversal fixes the subspace, Hermitian conjugation negates it, complex conjugation negates the central line, and quaternion conjugation negates the real vector triple. Its decomposition along the coordinate blocks is $i\mathbb{R}e_0 \oplus \operatorname{span}\{e_1,e_2,e_3\}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{M}_-$ | the anti-Hermitian subspace, $\{\tilde{Q} : \tilde{Q}^{\flat} = \tilde{Q}\}$ |
| $\mathbb{M}_+$ | the Hermitian subspace, the complementary subspace |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and vector subspaces |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $q'_0$ | the imaginary scalar parameter |
| $\mathbf{q} = (q_1,q_2,q_3)$ | the real vector part |
| $N(\tilde{Q})$ | the norm form, $|\mathbf{q}|^2-(q'_0)^2$ on the subspace |
| $B$ | the symmetric bilinear form polarizing $N$ |
| $\flat = -\dagger$ | the reversal |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$ | the four involutions |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the Hermitian decomposition, the norm form and the four involutions
- *Biquaternion Hermitian Subspace* (`articles_maths/biquaternion-hermitian-subspace.md`), the complementary subspace and its Jordan structure
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the intersections, the sums and the coordinate blocks of the six
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions, the composition law and the lattice of fixed spaces
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the two families of zero divisors and the associated idempotents
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm form, the group of units and the invertibility criterion
- *The Orthogonal Lie Algebra* (`articles_maths/the-orthogonal-lie-algebra.md`), for the Lie algebras attached to a quadratic form of signature $(3,1)$
