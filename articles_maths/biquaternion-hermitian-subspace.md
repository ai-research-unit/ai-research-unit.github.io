# __Biquaternion Hermitian Subspace__

## Introduction

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed space of Hermitian conjugation: the elements of $\mathbb{B}$ with real scalar part and purely imaginary vector part. It is four-dimensional, it is not a subalgebra, and it is one of the four subspaces on which the norm form is real. On it that form is indefinite of signature $(1,3)$, and the elements of zero norm form form a cone; this is what makes the subspace the richest of the six from the point of view of quadratic forms, and the reason it carries the idempotents and the isotropic directions of the algebra.

Three structures coexist on $\mathbb{M}_+$: the vector-space structure with the quadratic form of signature $(1,3)$; a **Jordan algebra** structure under the symmetrized product, inherited from the Hermitian matrices; and a Lie-theoretic relation with the anti-Hermitian subspace, into which the commutator of two of its elements falls. The article sets out all three.

As in the companion articles, all statements are algebraic, and the notation is that of the coefficient decomposition $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ with $Q_\mu = q_\mu + iq'_\mu$.

## Definition and Basis

### The Defining Involution

**Definition.** The **Hermitian subspace** is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\dagger} = \tilde{Q} \right\} , \qquad \tilde{Q}^{\dagger} = \bar{\tilde{Q}}^{*} = Q_0^{*}e_0 - Q_1^{*}e_1 - Q_2^{*}e_2 - Q_3^{*}e_3 .
$$

Its complementary space, the anti-fixed space of $\dagger$, is the anti-Hermitian subspace $\mathbb{M}_-$, and $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ is the **Hermitian decomposition** of the algebra.

### The Condition in Coordinates

Comparing $\tilde{Q}^{\dagger} = \tilde{Q}$ coefficient by coefficient:

- $Q_0^{*} = Q_0$, so the scalar coefficient $Q_0 = q_0$ is real;
- $-Q_k^{*} = Q_k$, that is $Q_k^{*} = -Q_k$, so each vector coefficient $Q_k = iq'_k$ is purely imaginary.

The subspace is therefore

$$
\mathbb{M}_+ = \left\{ \tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 : \ q_0, q'_1, q'_2, q'_3 \in \mathbb{R} \right\} ,
$$

the real scalar part together with the imaginary vector part.

### Basis and Dimension

**Proposition.** $\mathbb{M}_+$ is a real vector space of dimension $4$, with basis $e_0, ie_1, ie_2, ie_3$, splitting along the two coordinate blocks it meets,

$$
\mathbb{M}_+ = \mathbb{R}e_0 \oplus \operatorname{span}\{ie_1, ie_2, ie_3\} .
$$

**Proof.** One real scalar parameter and three real vector parameters; the four basis elements are independent over $\mathbb{R}$. $\square$

## Algebra and Module Structure

### It Is Not a Subalgebra

**Proposition.** The product of two elements of $\mathbb{M}_+$ lies in $\mathbb{M}_+$ only under a condition, and the subspace is not closed under multiplication.

**Proof.** For $\tilde{Q} = q_0e_0 + i\mathbf{q}'$ and $\tilde{R} = r_0e_0 + i\mathbf{r}'$ the product formula gives

$$
\tilde{Q}\tilde{R} = \left(q_0r_0 + (\mathbf{q}', \mathbf{r}')\right)e_0 + i\left(q_0\mathbf{r}' + r_0\mathbf{q}'\right) - \mathbf{q}'\times\mathbf{r}' ,
$$

whose last term $-\mathbf{q}'\times\mathbf{r}'$ is a **real** vector, outside the imaginary vector triple unless it vanishes. The product therefore lies in $\mathbb{M}_+$ exactly when $\mathbf{q}'\times\mathbf{r}' = 0$, that is when the two vector parts are parallel, and the simplest counterexample is $\tilde{Q} = ie_1$, $\tilde{R} = ie_2$, whose product is $(ie_1)(ie_2) = i^2e_1e_2 = -e_3$, a real vector. $\square$

The product formula has a compact rewriting that is worth recording, because it displays the two mechanisms at work — a symmetric and an antisymmetric one:

$$
\tilde{Q}\tilde{R} = \tfrac{1}{2}\left(\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q}\right) + \tfrac{1}{2}\left[\tilde{Q}, \tilde{R}\right] .
$$

### The Commutator Lands in the Anti-Hermitian Subspace

**Theorem.** For $\tilde{Q}, \tilde{R} \in \mathbb{M}_+$ one has $\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} \in \mathbb{M}_-$.

**Proof.** $\dagger$ reverses the order of a product and is the identity on $\mathbb{M}_+$, so $(\tilde{Q}\tilde{R})^{\dagger} = \tilde{R}\tilde{Q}$; hence $(\tilde{Q}\tilde{R}-\tilde{R}\tilde{Q})^{\dagger} = \tilde{R}\tilde{Q}-\tilde{Q}\tilde{R} = -(\tilde{Q}\tilde{R}-\tilde{R}\tilde{Q})$, which is the defining condition of the anti-Hermitian subspace. $\square$

In the formula of the previous paragraph this is the statement that the symmetric part is Hermitian and the antisymmetric part anti-Hermitian, as it must be. The corresponding statement in the other direction is proved in *Biquaternion Anti-Hermitian Subspace*.

### It Is a Jordan Algebra

**Theorem.** $\mathbb{M}_+$ is closed under the **symmetrized product**

$$
\tilde{Q} \circ \tilde{R} = \tfrac{1}{2}\left(\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q}\right) ,
$$

and with this product it is a Jordan algebra over $\mathbb{R}$, commutative, of degree two, isomorphic through $\Phi$ to the Jordan algebra $H_2(\mathbb{C})$ of Hermitian $2 \times 2$ complex matrices.

**Proof.** $(\tilde{Q}\tilde{R}+\tilde{R}\tilde{Q})^{\dagger} = \tilde{R}\tilde{Q} + \tilde{Q}\tilde{R}$, so the symmetrized product of two Hermitian elements is Hermitian; commutativity is built into the definition; and $\Phi$ is an algebra isomorphism of $\mathbb{B}$ onto $M_2(\mathbb{C})$ carrying $\mathbb{M}_+$ onto the Hermitian matrices, through which the symmetrized product becomes $\tfrac12(AB+BA)$. $\square$

Two consequences are read off. First, the subspace is **closed under powers**: $\tilde{Q}^2 = \tilde{Q} \circ \tilde{Q} \in \mathbb{M}_+$, and by induction every positive power of a Hermitian element is Hermitian. Second, the subspace is power-associative but not associative, which is exactly the Jordan axiom pattern; the general theory is in *Jordan Algebras*.

### The Square and Higher Powers

**Proposition.** For $\tilde{Q} = q_0e_0 + i\mathbf{q}'$ one has

$$
\tilde{Q}^2 = \left(q_0^2 + (\mathbf{q}', \mathbf{q}')\right)e_0 + 2iq_0\mathbf{q}' ,
$$

so the square of a Hermitian element is Hermitian, its scalar part is the sum of two squares $q_0^2 + (\mathbf{q}', \mathbf{q}') \geq 0$, and for $\tilde{Q} = i\mathbf{q}'$ a pure imaginary vector the square is central,

$$
(i\mathbf{q}')^2 = (\mathbf{q}', \mathbf{q}')\, e_0 = -N(i\mathbf{q}')\, e_0 .
$$

**Proof.** Expanding $(q_0e_0+i\mathbf{q}')^2$ with $\mathbf{q}'^2 = -(\mathbf{q}',\mathbf{q}')e_0$ and using the centrality of $i$ gives the stated scalar and vector parts; the pure case is $q_0 = 0$, and the norm form of an imaginary vector is $-(\mathbf{q}',\mathbf{q}')$. $\square$

### Modules

$\mathbb{M}_+$ is a module over the centre subspace, which acts by scalar extension; it is not a module over the quaternion subspace, since the product of $e_1 \in \mathbb{H}_{\mathbb{B}}$ with $ie_1 \in \mathbb{M}_+$ is $ie_1^2 = -ie_0 \notin \mathbb{M}_+$; and it is not a module over $\mathbb{H}_{\mathbb{B}}$ on the right either, by the same computation. Its role as a module is therefore limited to the central one, while its role as a product space is the Jordan one above.

## The Norm Form

### Restriction and Signature

**Theorem.** On the Hermitian subspace the norm form is the real quadratic form

$$
N(\tilde{Q}) = q_0^2 - \left((q'_1)^2 + (q'_2)^2 + (q'_3)^2\right) , \qquad \tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 ,
$$

of signature $(1,3)$; it is real, indefinite, positive on the central line and negative on the imaginary vector triple, and its associated symmetric bilinear form is

$$
B(\tilde{Q}, \tilde{R}) = \tfrac{1}{2}\left(N(\tilde{Q}+\tilde{R}) - N(\tilde{Q}) - N(\tilde{R})\right) = q_0 r_0 - (\mathbf{q}', \mathbf{r}') .
$$

**Proof.** Substituting $Q_0 = q_0$ and $Q_k = iq'_k$ in $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ gives $q_0^2 - \sum_k (q'_k)^2$, and the signs of the four basis elements $e_0, ie_1, ie_2, ie_3$ are $+,-,-,-$. Polarization gives the displayed bilinear form. $\square$

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} \in \mathbb{M}_+$ the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q}$ is not a zero divisor. The zero divisors are exactly the non-zero elements of the **isotropic cone**

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2 ,
$$

a cone of real dimension three, and no zero divisor of the subspace is nilpotent.

**Proof.** The equivalence of the first two conditions is the general criterion, and the third follows from it because the identity $\tilde{Q}\tilde{R} = 0$ forces $N(\tilde{Q})N(\tilde{R}) = 0$. For the nilpotency statement, $\tilde{Q}^2 = 0$ requires both $q_0^2 + (\mathbf{q}',\mathbf{q}') = 0$ and $q_0\mathbf{q}' = 0$ by the square formula, whence $q_0 = 0$ and $\mathbf{q}' = 0$. $\square$

The second half of the theorem is the sharpest difference between this subspace and the vector subspace: both contain zero divisors, but the zero divisors of the vector subspace are nilpotent, while those of $\mathbb{M}_+$ are not, and their squares are non-zero Hermitian elements with positive scalar part.

### The Idempotents

**Theorem.** The non-zero idempotents of $\mathbb{M}_+$ are exactly the elements

$$
\tilde{E} = \frac{e_0 + i\hat{\mathbf{u}}}{2} , \qquad \hat{\mathbf{u}} \in \operatorname{span}\{e_1,e_2,e_3\}, \ |\hat{\mathbf{u}}| = 1 ,
$$

together with $e_0$; each of them has zero norm form, and any two with opposite directions are orthogonal, $\tilde{E}_{+}\tilde{E}_{-} = 0$.

**Proof.** Let $\tilde{Q} = q_0e_0 + i\mathbf{q}'$ satisfy $\tilde{Q}^2 = \tilde{Q}$. Comparing the square formula with $\tilde{Q}$ gives $q_0^2 + (\mathbf{q}',\mathbf{q}') = q_0$ and $2q_0\mathbf{q}' = \mathbf{q}'$. If $\mathbf{q}' = 0$ then $q_0 \in \{0,1\}$, and if $\mathbf{q}' \neq 0$ then $q_0 = \tfrac12$ and $(\mathbf{q}',\mathbf{q}') = \tfrac14$, which is the displayed family; the orthogonality is $\left(\tfrac{e_0+i\hat{\mathbf{u}}}{2}\right)\left(\tfrac{e_0-i\hat{\mathbf{u}}}{2}\right) = \tfrac14(e_0 - (i\hat{\mathbf{u}})^2 + i\hat{\mathbf{u}} - i\hat{\mathbf{u}}) = \tfrac14(e_0 - e_0) = 0$. $\square$

The family is a two-sphere's worth of mutually orthogonal idempotent pairs, and it is the source of the two minimal left ideals of the algebra: a primitive idempotent of $\mathbb{B}$ is a minimal idempotent of $\mathbb{M}_+$ up to a central phase, as developed in *Biquaternion Ideals and Peirce Decomposition*.

## The Matrix Image

**Proposition.** Under the matrix realization,

$$
\Phi\!\left(\mathbb{M}_+\right) = \left\{ M \in M_2(\mathbb{C}) : M = M^{\dagger} \right\} ,
$$

the Hermitian matrices, and on this image

$$
\operatorname{Tr}\Phi(\tilde{Q}) = 2q_0 \in \mathbb{R} , \qquad \det\Phi(\tilde{Q}) = N(\tilde{Q}) \in \mathbb{R} .
$$

**Proof.** The fixed space of $\dagger$ on $\mathbb{B}$ is carried by the isomorphism onto the fixed space of the conjugate transpose on $M_2(\mathbb{C})$, by the compatibility of $\Phi$ with the involutions; the trace and the determinant are those of the general matrix with real scalar and imaginary vector coefficients, both real. $\square$

As an example, $\Phi(e_0 + ie_1) = \begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix}$, a Hermitian matrix of rank one, determinant zero and square equal to twice itself, so that half of it is an idempotent — the matrix form of the theorem above. The trace and determinant statements identify the subspace with the Jordan algebra $H_2(\mathbb{C})$ through the standard trace and determinant of the matrix picture.

## The Four Involutions on It

In the basis $e_0, ie_1, ie_2, ie_3$:

| involution | matrix | effect |
|---|---|---|
| $\bar{\cdot}$ | $\operatorname{diag}(1,-1,-1,-1)$ | negates the vector part |
| ${}^{*}$ | $\operatorname{diag}(1,-1,-1,-1)$ | negates the vector part |
| ${}^{\dagger}$ | $+\mathrm{id}$ | the identity, by definition of the subspace |
| $\flat$ | $-\mathrm{id}$ | minus the identity |

The subspace is invariant under all four. The first two rows coincide: on a Hermitian element quaternion and complex conjugation have the same effect, which is the compatibility $\dagger = {}^{*}\circ\bar{\cdot}$ read on the fixed space of $\dagger$. Reversal negates the subspace, and the subspace it fixes is $\mathbb{M}_-$.

## Relations to the Other Five Subspaces

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{M}_+ \cap \mathbb{C}_{\mathbb{B}}$ | $\mathbb{R}e_0$ | $1$ |
| $\mathbb{M}_+ \cap \mathrm{Vect}(\mathbb{B})$ | $\operatorname{span}\{ie_1,ie_2,ie_3\}$ | $3$ |
| $\mathbb{M}_+ \cap \mathbb{H}_{\mathbb{B}}$ | $\mathbb{R}e_0$ | $1$ |
| $\mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{ie_1,ie_2,ie_3\}$ | $3$ |
| $\mathbb{M}_+ \cap \mathbb{M}_-$ | $\{0\}$ | $0$ |

The subspace is complementary to $\mathbb{M}_-$, and its decomposition along the coordinate blocks is $\mathbb{M}_+ = \mathbb{R}e_0 \oplus \operatorname{span}\{ie_1,ie_2,ie_3\}$: the scalar line is shared with the centre and the quaternion subspaces, the imaginary triple with the anti-quaternion subspace and with the vector subspace. Its sums with the centre and with $i\mathbb{H}_{\mathbb{B}}$ have dimension $5$, and its sums with the vector subspace and with $\mathbb{H}_{\mathbb{B}}$ have dimension $7$; only the pair with $\mathbb{M}_-$ spans the algebra.

## Examples

### A Unit, a Null Element, an Idempotent

Take $\tilde{Q} = e_0 + ie_1$. Its norm form is $N(\tilde{Q}) = 1 - 1 = 0$, so it is a zero divisor and lies on the isotropic cone, and

$$
\tilde{Q}^2 = (1+1)e_0 + 2i e_1 = 2\tilde{Q} , \qquad \frac{\tilde{Q}}{2} = \frac{e_0+ie_1}{2} ,
$$

so half of it is an idempotent, consistent with $\tilde{Q}^2 = 2\tilde{Q}$ and with the classification: the idempotent $\tilde{Q}/2$ has scalar part $\tfrac12$ and its imaginary vector part is a unit vector. Its matrix image is the rank-one Hermitian matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix}$. Take instead $\tilde{Q} = e_0$: norm form $1$, a unit of inverse $e_0$; and $\tilde{Q} = ie_1$: norm form $-1$, also a unit, with inverse $\tilde{Q}$ itself because $\tilde{Q}^2 = e_0$.

### An Orthogonal Idempotent Pair

With $\hat{\mathbf{u}} = e_1$ the two idempotents are

$$
\tilde{E}_+ = \frac{e_0+ie_1}{2} , \qquad \tilde{E}_- = \frac{e_0-ie_1}{2} , \qquad \tilde{E}_+\tilde{E}_- = 0 , \qquad \tilde{E}_+ + \tilde{E}_- = e_0 ,
$$

a decomposition of the unit of the algebra into two orthogonal idempotents of the subspace. This is the pair that generates the two minimal left ideals, and it shows that the idempotents of the algebra are not to be found in the centre or in the vector subspace: the centre has only $e_0$ and the vector subspace none at all.

### A Rigid Element

For $\hat{\mathbf{u}} = \cos\varphi\, e_1 + \sin\varphi\, e_2$ the idempotent $\tilde{E} = \tfrac12(e_0 + i\hat{\mathbf{u}})$ has matrix image

$$
\Phi(\tilde{E}) = \frac{1}{2}\begin{pmatrix} 1 & \sin\varphi + i\cos\varphi \\ \sin\varphi - i\cos\varphi & 1 \end{pmatrix} ,
$$

of trace $1$ and determinant $0$: a rank-one projector. The whole two-sphere of unit vectors $\hat{\mathbf{u}}$ thus gives a two-sphere of projectors, and two of them are orthogonal exactly when their directions are opposite. The family is the algebraic skeleton of the two minimal left ideals and of the Peirce decomposition of the algebra.

### An Element Not on the Cone and Its Inverse

For $\tilde{Q} = 2e_0 + i(e_1 + e_2)$ one has $N(\tilde{Q}) = 4 - 2 = 2$, so $\tilde{Q}$ is a unit with

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})} = \frac{2e_0 - i(e_1+e_2)}{2} = e_0 - \frac{i(e_1+e_2)}{2} ,
$$

again in the subspace, since quaternion conjugation preserves $\mathbb{M}_+$ and the norm form is a real scalar. The inverse of a Hermitian element of non-zero norm form is Hermitian, and the units of the subspace therefore form a group of dimension four.

## Summary

The Hermitian subspace $\mathbb{M}_+$ is the fixed space of Hermitian conjugation, the set of elements with real scalar part and imaginary vector part, a real vector space of dimension $4$ with basis $e_0, ie_1, ie_2, ie_3$ and decomposition $\mathbb{R}e_0 \oplus \operatorname{span}\{ie_1,ie_2,ie_3\}$. It is not a subalgebra, but it is closed under the symmetrized product, with which it is a Jordan algebra of degree two isomorphic to the Hermitian $2\times2$ matrices; it is closed under powers; and its commutator lands in the anti-Hermitian subspace. The norm form restricts to the real form $q_0^2 - ((q'_1)^2+(q'_2)^2+(q'_3)^2)$ of signature $(1,3)$, so the units are the elements off the isotropic cone $q_0^2 = (q'_1)^2+(q'_2)^2+(q'_3)^2$; the zero divisors are exactly the non-zero elements of the cone, and none of them is nilpotent. The non-trivial idempotents are the elements $\tfrac12(e_0 + i\hat{\mathbf{u}})$ with $\hat{\mathbf{u}}$ a unit real vector, of zero norm form, forming a two-sphere of orthogonal pairs; one such pair sums to the unit and generates the two minimal left ideals. The matrix image is the set of Hermitian matrices, with trace $2q_0$ and determinant $N$. Complex conjugation and quaternion conjugation both negate the vector part, Hermitian conjugation fixes the subspace, and reversal negates it. It is complementary to $\mathbb{M}_-$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{M}_+$ | the Hermitian subspace, $\{\tilde{Q} : \tilde{Q}^{\dagger} = \tilde{Q}\}$ |
| $\mathbb{M}_-$ | the anti-Hermitian subspace, the complementary subspace |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and vector subspaces |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $q_0$ | the real scalar part |
| $\mathbf{q}' = (q'_1,q'_2,q'_3)$ | the real vector parameters of the imaginary vector part |
| $N(\tilde{Q})$ | the norm form, $q_0^2 - (\mathbf{q}',\mathbf{q}')$ on the subspace |
| $B$ | the symmetric bilinear form polarizing $N$ |
| $\tilde{Q} \circ \tilde{R}$ | the symmetrized product, $\tfrac12(\tilde{Q}\tilde{R}+\tilde{R}\tilde{Q})$ |
| $H_2(\mathbb{C})$ | the Jordan algebra of Hermitian $2\times2$ complex matrices |
| $\hat{\mathbf{u}}$ | a unit real vector, used to parametrize the idempotents |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$ | the four involutions |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the Hermitian decomposition, the norm form and the quadratic forms of the algebra
- *Biquaternion Anti-Hermitian Subspace* (`articles_maths/biquaternion-anti-hermitian-subspace.md`), the complementary subspace, into which the commutator maps
- *Jordan Algebras* (`articles_maths/jordan-algebras.md`), for the symmetrized product, the Jordan identity and the structure of Hermitian matrix algebras
- *Special and Exceptional Jordan Algebras* (`articles_maths/special-and-exceptional-jordan-algebras.md`), for the position of $H_2(\mathbb{C})$ among the matrix Jordan algebras
- *Quadratic Forms over Algebras and Norm Forms* (`articles_maths/quadratic-forms-over-algebras-and-norm-forms.md`), for quadratic forms of signature $(1,3)$ and norm forms over algebras
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the primitive idempotents and the minimal left ideals
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the intersections, the sums and the coordinate blocks of the six
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions and their fixed spaces
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm form, its multiplicativity and the invertibility criterion
