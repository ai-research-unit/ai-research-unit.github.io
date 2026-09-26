# __Biquaternion Vector Subspace__

## Introduction

Of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, the **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the largest: the only one of dimension six. It is the anti-fixed space of quaternion conjugation, the kernel of the scalar-part functional, the derived subspace spanned by the commutators, and the Lie algebra of the unit-norm group; these four descriptions are proved below to coincide. It is not a subalgebra, its elements have central squares, and the zero divisors it contains are exactly the null elements with respect to the norm form.

As in the companion articles, everything here is algebraic and nothing is physical: the elements are written $\tilde{Q}, \tilde{R}$, their coefficients $Q_0, \dots, Q_3$ with $Q_\mu = q_\mu + i q'_\mu$, and no further coordinates are introduced. The other five subspaces are treated in *Biquaternion Centre Subspace*, *Biquaternion Quaternion Subspace*, *Biquaternion Anti-Quaternion Subspace*, *Biquaternion Hermitian Subspace* and *Biquaternion Anti-Hermitian Subspace*.

## Definition and Basis

### The Defining Involution

**Definition.** The **vector subspace** is the anti-fixed space of quaternion conjugation,

$$
\mathrm{Vect}(\mathbb{B}) = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = -\tilde{Q} \right\} ,
$$

with $\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3$.

Together with the centre subspace it gives the **scalar–vector decomposition** $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, the eigenspace decomposition of $\bar{\cdot}$ for the eigenvalues $+1$ and $-1$.

### The Condition in Coordinates

Comparing $\bar{\tilde{Q}} = -\tilde{Q}$ coefficient by coefficient, the three vector coefficients impose $Q_k = -(-Q_k)$ for $k = 1, 2, 3$, which is no condition at all, while the scalar coefficient imposes $Q_0 = -Q_0$, that is $Q_0 = 0$:

$$
\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3 , \qquad Q_1, Q_2, Q_3 \in \mathbb{C} .
$$

The vector subspace is thus the set of elements of **vanishing scalar part**, the elements the corpus calls **pure** in the theory of the zero divisors.

### Basis and Dimension

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is a real vector space of dimension $6$, with basis

$$
e_1, \ e_2, \ e_3, \ ie_1, \ ie_2, \ ie_3 ,
$$

and it splits as the direct sum of the **real vectors** and the **imaginary vectors**,

$$
\mathrm{Vect}(\mathbb{B}) = \operatorname{span}\{e_1, e_2, e_3\} \oplus \operatorname{span}\{ie_1, ie_2, ie_3\} ,
$$

two three-dimensional real subspaces.

**Proof.** The three complex coefficients $Q_k$ are six real parameters; the six displayed elements are independent over $\mathbb{R}$ and span the set. $\square$

The two summands are precisely two of the four coordinate blocks of the algebra: $\operatorname{span}\{e_1, e_2, e_3\}$ is also the intersection of the vector subspace with the quaternion subspace and with the anti-Hermitian subspace, and $\operatorname{span}\{ie_1, ie_2, ie_3\}$ is also its intersection with the anti-quaternion subspace and with the Hermitian subspace.

## The Four Descriptions Coincide

### It Is the Kernel of the Scalar Part

**Proposition.** $\mathrm{Vect}(\mathbb{B}) = \ker \operatorname{Sc}$, where $\operatorname{Sc}(\tilde{Q}) = Q_0 = \tfrac{1}{2}(\tilde{Q} + \bar{\tilde{Q}})$.

**Proof.** Immediate from the coordinate condition $Q_0 = 0$, and the second expression is the projection onto the fixed space of $\bar{\cdot}$ along the anti-fixed space. $\square$

### It Is the Derived Subspace

**Theorem.** $\mathrm{Vect}(\mathbb{B}) = [\mathbb{B}, \mathbb{B}]$, the complex span of the commutators $\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q}$.

**Proof.** For the basis elements, $[e_j, e_k] = 2 e_{j \times k}$ when $j \neq k$ in cyclic order and $[e_j, e_k] = 0$ when $j = k$, and the products with $i$ are obtained by complex linearity; every bracket is therefore traceless, so $[\mathbb{B}, \mathbb{B}] \subseteq \mathrm{Vect}(\mathbb{B})$. Conversely $e_1 = \tfrac12 [e_2, e_3]$ and its cyclic analogues give the three real vector units as brackets, and $ie_k = i e_k$ is then a complex multiple of a bracket; the six basis elements of the subspace lie in $[\mathbb{B}, \mathbb{B}]$, which therefore contains it. $\square$

### It Is the Lie Algebra of the Unit-Norm Group

**Theorem.** Let $\tilde{X} \in \mathbb{B}$ and let $\Phi$ be the matrix realization. Then $\tilde{X} \in \mathrm{Vect}(\mathbb{B})$ if and only if the one-parameter family $t \mapsto \Phi^{-1}\!\left(e^{t\Phi(\tilde{X})}\right)$ lies in the norm-one group $\{\tilde{Q} : N(\tilde{Q}) = 1\}$ for all real $t$.

**Proof.** $\det \Phi(\tilde{Q}) = N(\tilde{Q})$, and $\det e^{M} = e^{\operatorname{Tr}M}$ for every matrix $M$, so the norm form of the exponential is $e^{t\operatorname{Tr}\Phi(\tilde{X})}$; this equals $1$ for all $t$ exactly when $\operatorname{Tr}\Phi(\tilde{X}) = 0$, and $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$ vanishes exactly on the vector subspace. $\square$

The proposition identifies $\mathrm{Vect}(\mathbb{B})$ with the Lie algebra of the unit-norm group, which is $\mathfrak{sl}(2, \mathbb{C})$ in the matrix picture; the same statement appears in *Biquaternion Exponential and Lie Group Structure* from the side of the group.

## Algebra and Module Structure

### It Is Not a Subalgebra

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is not closed under multiplication.

**Proof.** $e_1^2 = -e_0$ has scalar part $-1$ and therefore does not lie in the subspace. $\square$

The failure is systematic rather than exceptional: the product of two vector elements has a scalar part given by the dot product of their coefficient vectors, as the next proposition records. What does hold is the following structural statement.

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is closed under the commutator; it is therefore a Lie subalgebra of $\mathbb{B}$ as a complex Lie algebra, of dimension $3$ over $\mathbb{C}$ and $6$ over $\mathbb{R}$.

**Proof.** The bracket is traceless by the theorem above, and it is bilinear and alternating; the bracket relations $[e_j, e_k] = 2e_{j \times k}$ and $[e_j, ie_k] = 2i e_{j \times k}$ close on the six basis elements. $\square$

### The Product of Two Vector Elements

**Theorem.** Let $\tilde{Q} = \sum_{k=1}^{3} Q_k e_k$ and $\tilde{R} = \sum_{k=1}^{3} R_k e_k$ be elements of the vector subspace, and write $\mathbf{Q} = (Q_1, Q_2, Q_3)$, $\mathbf{R} = (R_1, R_2, R_3)$ for their coefficient triples. Then

$$
(\mathbf{Q}, \mathbf{R}) = \sum_{k=1}^{3} Q_k R_k , \qquad \mathbf{Q} \times \mathbf{R} = \left(Q_2 R_3 - Q_3 R_2, \ Q_3 R_1 - Q_1 R_3, \ Q_1 R_2 - Q_2 R_1\right) ,
$$

$$
\tilde{Q}\tilde{R} = -(\mathbf{Q}, \mathbf{R}) e_0 + \sum_{k=1}^{3} (\mathbf{Q} \times \mathbf{R})_k e_k .
$$

**Proof.** Expansion of the product with $e_j e_k = -\delta_{jk} e_0 + \varepsilon_{jkl} e_l$ gives the two terms shown. $\square$

Three consequences are read off at once. First, the product of two vector elements lies in the vector subspace exactly when the dot product $(\mathbf{Q}, \mathbf{R})$ vanishes; otherwise it has a non-zero scalar part. Second, the commutator is twice the cross product, $\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2 \sum_k (\mathbf{Q}\times\mathbf{R})_k e_k$, so the Lie structure of the subspace is that of the complex three-space under the cross product. Third, the **square of a vector element is central**:

$$
\tilde{Q}^2 = -N(\tilde{Q}) e_0 , \qquad N(\tilde{Q}) = Q_1^2 + Q_2^2 + Q_3^2 ,
$$

because the cross product of a triple with itself vanishes. Every element of the vector subspace therefore satisfies the quadratic identity $\tilde{Q}^2 + N(\tilde{Q}) e_0 = 0$, and its powers are the powers of the central element $-N(\tilde{Q})e_0$.

### Modules over the Other Subspaces

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is not a module over the quaternion subspace: for $h \in \mathbb{H}_{\mathbb{B}}$ and $\tilde{Q} \in \mathrm{Vect}(\mathbb{B})$ the scalar part of $h\tilde{Q}$ is $-\sum_{k} h_k Q_k$, which does not vanish in general. It is not a module over the anti-quaternion subspace either, for the same reason with $h$ replaced by $ih'$. It is a module over the centre subspace.

**Proof.** The scalar part of $h\tilde{Q}$ is read from the product formula, and it vanishes for all pairs only in the degenerate cases $h = 0$ or $Q = 0$; the centre is contained in the commuting elements and acts by scalar extension. $\square$

## The Norm Form

**Proposition.** On the vector subspace the norm form is the complex bilinear form in the three coefficients,

$$
N(\tilde{Q}) = Q_1^2 + Q_2^2 + Q_3^2 ,
$$

complex-valued in general, with real restriction of signature $(3, 3)$ in the basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$, since $N(e_k) = 1$ and $N(ie_k) = -1$.

**Proof.** Substituting $Q_0 = 0$ in $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ leaves the three terms; the signs of the real basis vectors are computed from $(ie_k)^2 = i^2 e_k^2 = -(-1) = 1$ for the norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$. $\square$

Like the centre subspace and unlike the four others, the vector subspace is a subspace on which the norm form is not real-valued. Its **null elements** are the solutions of $Q_1^2 + Q_2^2 + Q_3^2 = 0$, a complex cone through the origin of real dimension four.

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} \in \mathrm{Vect}(\mathbb{B})$ the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q}$ is not a zero divisor. The zero divisors are exactly the null elements, $\tilde{Q} \neq 0$ with $N(\tilde{Q}) = 0$.

**Proof.** The general invertibility criterion gives the equivalence of the first two; for the third, if $N(\tilde{Q}) \neq 0$ then $\tilde{Q}$ has the inverse $-\bar{\tilde{Q}}/N(\tilde{Q})$, since $\tilde{Q}^2 = -N(\tilde{Q})e_0$ implies $\bar{\tilde{Q}} = -\tilde{Q}$ and hence $\tilde{Q}(-\bar{\tilde{Q}}/N(\tilde{Q})) = -\tilde{Q}(-\tilde{Q})/N(\tilde{Q}) = \tilde{Q}^2/N(\tilde{Q}) = -e_0$; and if $N(\tilde{Q}) = 0$ then $\tilde{Q}^2 = 0$ with $\tilde{Q} \neq 0$, so $\tilde{Q}$ annihilates itself. $\square$

**Corollary.** Every null vector is nilpotent of index two: $\tilde{Q}^2 = 0$ but $\tilde{Q} \neq 0$. The vector subspace contains no idempotent other than $0$.

**Proof.** The first statement is the square formula with $N(\tilde{Q}) = 0$. For the second, if $\tilde{Q} \in \mathrm{Vect}(\mathbb{B})$ satisfies $\tilde{Q}^2 = \tilde{Q}$, then $-\tilde{Q} = N(\tilde{Q})e_0$ by the square formula, so $\tilde{Q}$ is both a vector element and a central one; the intersection of the two subspaces is the origin, whence $\tilde{Q} = 0$. $\square$

The zero divisors of the vector subspace are called the **pure zero divisors** in *Biquaternion Zero Divisors*, which develops the classification and the two families of the algebra as a whole.

## The Matrix Image

**Proposition.** Under the matrix realization $\Phi$,

$$
\Phi\!\left(\mathrm{Vect}(\mathbb{B})\right) = \left\{ M \in M_2(\mathbb{C}) : \operatorname{Tr} M = 0 \right\} = \mathfrak{sl}(2, \mathbb{C}) .
$$

**Proof.** $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$, so the trace vanishes exactly when the scalar part does. $\square$

In the coefficients the image reads

$$
\Phi(\tilde{Q}) = \begin{pmatrix} -iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & iQ_3 \end{pmatrix} ,
$$

the general traceless matrix. The determinant of the image is the norm form, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$, so the null elements are exactly the singular traceless matrices, and the nilpotent ones are the rank-one elements with zero square, in agreement with the nilpotency proved above.

## The Four Involutions on It

In the basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$ the four involutions act diagonally:

| involution | matrix | sign pattern |
|---|---|---|
| $\bar{\cdot}$ | $-\mathrm{id}$ | all six signs negative |
| ${}^{*}$ | $\operatorname{diag}(1,1,1,-1,-1,-1)$ | real vectors fixed, imaginary vectors negated |
| ${}^{\dagger}$ | $\operatorname{diag}(-1,-1,-1,1,1,1)$ | real vectors negated, imaginary vectors fixed |
| $\flat$ | $\operatorname{diag}(1,1,1,-1,-1,-1)$ | as ${}^{*}$ |

The subspace is invariant under all four. Quaternion conjugation acts as the negative of the identity, which is the defining property of the subspace; complex conjugation exchanges the two coordinate blocks it contains, so it does not preserve either $\operatorname{span}\{e_k\}$ or $\operatorname{span}\{ie_k\}$ separately — those two are preserved by $\dagger$ and by $\flat$ in the exchanged roles.

## Relations to the Other Five Subspaces

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{C}_{\mathbb{B}}$ | $\{0\}$ | $0$ |
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{e_1, e_2, e_3\}$ | $3$ |
| $\mathrm{Vect}(\mathbb{B}) \cap i\mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{ie_1, ie_2, ie_3\}$ | $3$ |
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_+$ | $\operatorname{span}\{ie_1, ie_2, ie_3\}$ | $3$ |
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_-$ | $\operatorname{span}\{e_1, e_2, e_3\}$ | $3$ |

The vector subspace is complementary to the centre, $\mathbb{B} = \mathrm{Vect}(\mathbb{B}) \oplus \mathbb{C}_{\mathbb{B}}$, and with each of the other four its sum has dimension $7$, so the pair spans all but one real dimension and no other pair is a decomposition. The four intersections of dimension three are the four coordinate blocks of the algebra away from the scalar lines; the pattern is recorded in *Biquaternion Relations Between Subspaces*.

## Examples

### The Product of Two Vector Units

Take $\tilde{Q} = e_1$ and $\tilde{R} = e_2$. Their coefficient triples are $(1, 0, 0)$ and $(0, 1, 0)$, with $(\mathbf{Q}, \mathbf{R}) = 0$ and $\mathbf{Q}\times\mathbf{R} = (0, 0, 1)$, so

$$
e_1 e_2 = e_3 \in \mathrm{Vect}(\mathbb{B}) , \qquad [e_1, e_2] = 2e_3 .
$$

Take instead $\tilde{Q} = \tilde{R} = e_1$: the dot product is $1$ and the cross product vanishes, so

$$
e_1^2 = -e_0 \notin \mathrm{Vect}(\mathbb{B}) .
$$

The two computations are the two faces of the product formula, and together they show that the subspace is closed under neither multiplication nor squaring.

### A Non-Null Vector

For $\tilde{Q} = e_1 + e_2$ one has $N(\tilde{Q}) = 2$, so $\tilde{Q}$ is a unit with $\tilde{Q}^2 = -2e_0$ and

$$
\tilde{Q}^{-1} = -\frac{\bar{\tilde{Q}}}{2} = \frac{e_1 + e_2}{2} ,
$$

which is again a vector element; the inverse of a non-null vector stays in the subspace, as the formula for the inverse of a pure element requires.

### A Null Vector and Its Matrix

For $\tilde{Q} = e_1 + ie_2$ one has $N(\tilde{Q}) = 1 + i^2 = 0$, so $\tilde{Q}$ is a zero divisor, and indeed

$$
\tilde{Q}^2 = -N(\tilde{Q})e_0 = 0 , \qquad \tilde{Q} \neq 0 ,
$$

so $\tilde{Q}$ is its own annihilator. Its matrix image is

$$
\Phi(\tilde{Q}) = \begin{pmatrix} 0 & -2i \\ 0 & 0 \end{pmatrix} ,
$$

of rank one and square zero, the Jordan block of size two in nilpotent form. The example exhibits the coincidence of three conditions that hold only on the vector subspace among the six: purity of the element, nullity of the norm form, and nilpotency of index two.

### An Imaginary Vector and the Cross Product

For $\tilde{Q} = e_1$ and $\tilde{R} = ie_2$, the product is

$$
e_1 \cdot ie_2 = i e_3 \in \mathrm{Vect}(\mathbb{B}) , \qquad [e_1, ie_2] = 2ie_3 ,
$$

with vanishing dot product of the triples $(1, 0, 0)$ and $(0, i, 0)$. The bracket relations with a factor $i$ are the complexification of the real ones and are the reason the Lie algebra of the subspace is $\mathfrak{sl}(2, \mathbb{C})$ over $\mathbb{C}$ while its real form $\operatorname{span}\{e_1,e_2,e_3\}$ is $\mathfrak{su}(2)$.

## Summary

The vector subspace $\mathrm{Vect}(\mathbb{B})$ is the anti-fixed space of quaternion conjugation, the set of elements of vanishing scalar part, a real vector space of dimension $6$ with basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$, splitting into the real and imaginary vectors. It is simultaneously the kernel of the scalar-part functional, the derived subspace $[\mathbb{B}, \mathbb{B}]$, and the Lie algebra of the unit-norm group; its matrix image is $\mathfrak{sl}(2,\mathbb{C})$. It is not a subalgebra and not a module over the quaternion or anti-quaternion subspaces, but it is closed under the commutator, where the bracket is twice the cross product of the coefficient triples. The square of a vector element is central, $\tilde{Q}^2 = -N(\tilde{Q})e_0$, so null elements are nilpotent and units have their inverses in the subspace. The norm form restricts to $Q_1^2+Q_2^2+Q_3^2$, complex-valued, of real signature $(3,3)$; the zero divisors are exactly the null elements. Quaternion conjugation acts as minus the identity, complex conjugation exchanges the two coordinate blocks it contains, and all four involutions preserve the subspace. It is complementary to the centre, and its intersections with the other four subspaces are three-dimensional.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, $\{\tilde{Q} : \bar{\tilde{Q}} = -\tilde{Q}\}$ |
| $\operatorname{Sc}$ | the scalar-part functional, $\operatorname{Sc}(\tilde{Q}) = Q_0$ |
| $\mathbf{Q} = (Q_1,Q_2,Q_3)$ | the coefficient triple of a vector element |
| $(\mathbf{Q},\mathbf{R})$ | the complex bilinear dot product |
| $\mathbf{Q}\times\mathbf{R}$ | the complex bilinear cross product |
| $\operatorname{span}\{e_1,e_2,e_3\}$ | the real vectors |
| $\operatorname{span}\{ie_1,ie_2,ie_3\}$ | the imaginary vectors |
| $[\mathbb{B},\mathbb{B}]$ | the derived subspace, equal to $\mathrm{Vect}(\mathbb{B})$ |
| $N(\tilde{Q}) = Q_1^2+Q_2^2+Q_3^2$ | the norm form on the subspace |
| $\mathfrak{sl}(2,\mathbb{C})$ | the matrix image of the subspace |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$ | the four involutions |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the multiplication of $\mathbb{B}$ and the scalar–vector decomposition
- *Biquaternion Centre Subspace* (`articles_maths/biquaternion-centre-subspace.md`), the fixed companion of the present subspace
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the pure and non-pure zero divisors and the two families of the algebra
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the intersections, the sums and the coordinate blocks of the six
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions and the two spaces each defines
- *Biquaternion Exponential and Lie Group Structure* (`articles_maths/biquaternion-exponential-and-lie-group-structure.md`), for the Lie algebra of the group of units and of the norm-one group
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm form and the invertibility criterion
- *The Orthogonal Lie Algebra* (`articles_maths/the-orthogonal-lie-algebra.md`), for the cross-product Lie structure in its general setting
