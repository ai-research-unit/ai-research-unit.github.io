# __Biquaternion Vector Subspace__

## Introduction

Of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, the **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the largest: the only one of dimension six. It is the anti-fixed space of quaternion conjugation, the kernel of the scalar-part functional, the derived subspace spanned by the commutators, and the Lie algebra of the unit-norm group; these four descriptions are proved below to coincide. It is not a subalgebra, its elements have central squares, and the zero divisors it contains are exactly the null elements with respect to the biquaternion norm.

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

**Proof.** The three complex coefficients $Q_k$ are six real parameters; the six displayed elements are independent over $\mathbb{R}$ and span the set.

The two summands are precisely two of the four coordinate blocks of the algebra: $\operatorname{span}\{e_1, e_2, e_3\}$ is also the intersection of the vector subspace with the quaternion subspace and with the anti-Hermitian subspace, and $\operatorname{span}\{ie_1, ie_2, ie_3\}$ is also its intersection with the anti-quaternion subspace and with the Hermitian subspace.

## The Four Descriptions Coincide

### It Is the Kernel of the Scalar Part

**Proposition.** $\mathrm{Vect}(\mathbb{B}) = \ker \operatorname{Sc}$, where $\operatorname{Sc}(\tilde{Q}) = Q_0 = \tfrac{1}{2}(\tilde{Q} + \bar{\tilde{Q}})$.

**Proof.** Immediate from the coordinate condition $Q_0 = 0$, and the second expression is the projection onto the fixed space of $\bar{\cdot}$ along the anti-fixed space.

### It Is the Derived Subspace

**Theorem.** $\mathrm{Vect}(\mathbb{B}) = [\mathbb{B}, \mathbb{B}]$, the complex span of the commutators $\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q}$.

**Proof.** For the basis elements, $[e_j, e_k] = 2 e_{j \times k}$ when $j \neq k$ in cyclic order and $[e_j, e_k] = 0$ when $j = k$, and the products with $i$ are obtained by complex linearity; every bracket is therefore traceless, so $[\mathbb{B}, \mathbb{B}] \subseteq \mathrm{Vect}(\mathbb{B})$. Conversely $e_1 = \tfrac12 [e_2, e_3]$ and its cyclic analogues give the three real vector units as brackets, and $ie_k = i e_k$ is then a complex multiple of a bracket; the six basis elements of the subspace lie in $[\mathbb{B}, \mathbb{B}]$, which therefore contains it.

### It Is the Lie Algebra of the Unit-Norm Group

**Theorem.** The vector subspace is the Lie algebra of the norm-one group $\{\tilde{Q} : N(\tilde{Q}) = 1\}$: it is the tangent space at $e_0$ of that group.

**Proof.** The norm-one group is a smooth subgroup of the units, so its Lie algebra is its tangent space at the identity, and an element $\tilde{Q}$ lies in that tangent space exactly when the derivative at $t = 0$ of $t \mapsto N(e_0 + t\tilde{Q})$ vanishes. By multiplicativity of the biquaternion norm,

$$
N(e_0 + t\tilde{Q}) = (e_0 + t\tilde{Q})(e_0 + t\bar{\tilde{Q}}) = e_0 + t\bigl(\tilde{Q} + \bar{\tilde{Q}}\bigr) + t^2 N(\tilde{Q}) ,
$$

whose linear coefficient is $\tilde{Q} + \bar{\tilde{Q}} = 2\operatorname{Sc}(\tilde{Q})$; this vanishes exactly on the vector subspace.

The proposition identifies $\mathrm{Vect}(\mathbb{B})$ with the Lie algebra of the norm-one group, a statement developed in *Biquaternion Lie Algebra* from the side of the group.

## Algebra and Module Structure

### It Is Not a Subalgebra

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is not closed under multiplication.

**Proof.** $e_1^2 = -e_0$ has scalar part $-1$ and therefore does not lie in the subspace.

The failure is systematic rather than exceptional: the product of two vector elements has a scalar part given by the dot product of their coefficient vectors, as the next proposition records. What does hold is the following structural statement.

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is closed under the commutator; it is therefore a Lie subalgebra of $\mathbb{B}$ as a complex Lie algebra, of dimension $3$ over $\mathbb{C}$ and $6$ over $\mathbb{R}$.

**Proof.** The bracket is traceless by the theorem above, and it is bilinear and alternating; the bracket relations $[e_j, e_k] = 2e_{j \times k}$ and $[e_j, ie_k] = 2i e_{j \times k}$ close on the six basis elements.

### The Product of Two Vector Elements

**Theorem.** Let $\tilde{Q} = \sum_{k=1}^{3} Q_k e_k$ and $\tilde{R} = \sum_{k=1}^{3} R_k e_k$ be elements of the vector subspace, and write $\mathbf{Q} = (Q_1, Q_2, Q_3)$, $\mathbf{R} = (R_1, R_2, R_3)$ for their coefficient triples. Then

$$
(\mathbf{Q}, \mathbf{R}) = \sum_{k=1}^{3} Q_k R_k , \qquad \mathbf{Q} \times \mathbf{R} = \left(Q_2 R_3 - Q_3 R_2, \ Q_3 R_1 - Q_1 R_3, \ Q_1 R_2 - Q_2 R_1\right) ,
$$

$$
\tilde{Q}\tilde{R} = -(\mathbf{Q}, \mathbf{R}) e_0 + \sum_{k=1}^{3} (\mathbf{Q} \times \mathbf{R})_k e_k .
$$

**Proof.** Expansion of the product with $e_j e_k = -\delta_{jk} e_0 + \varepsilon_{jkl} e_l$ gives the two terms shown.

Three consequences are read off at once. First, the product of two vector elements lies in the vector subspace exactly when the dot product $(\mathbf{Q}, \mathbf{R})$ vanishes; otherwise it has a non-zero scalar part. Second, the commutator is twice the cross product, $\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2 \sum_k (\mathbf{Q}\times\mathbf{R})_k e_k$, so the Lie structure of the subspace is that of the complex three-space under the cross product. Third, the **square of a vector element is central**:

$$
\tilde{Q}^2 = -N(\tilde{Q}) e_0 , \qquad N(\tilde{Q}) = Q_1^2 + Q_2^2 + Q_3^2 ,
$$

because the cross product of a triple with itself vanishes. Every element of the vector subspace therefore satisfies the quadratic identity $\tilde{Q}^2 + N(\tilde{Q}) e_0 = 0$, and its powers are the powers of the central element $-N(\tilde{Q})e_0$.

### Modules over the Other Subspaces

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is not a module over the quaternion subspace: for $h \in \mathbb{H}_{\mathbb{B}}$ and $\tilde{Q} \in \mathrm{Vect}(\mathbb{B})$ the scalar part of $h\tilde{Q}$ is $-\sum_{k} h_k Q_k$, which does not vanish in general. It is not a module over the anti-quaternion subspace either, for the same reason with $h$ replaced by $ih'$. It is a module over the centre subspace.

**Proof.** The scalar part of $h\tilde{Q}$ is read from the product formula, and it vanishes for all pairs only in the degenerate cases $h = 0$ or $Q = 0$; the centre is contained in the commuting elements and acts by scalar extension.

## The Biquaternion Norm

**Proposition.** On the vector subspace the biquaternion norm is the complex bilinear form in the three coefficients,

$$
N(\tilde{Q}) = Q_1^2 + Q_2^2 + Q_3^2 ,
$$

complex-valued in general, with real restriction of signature $(3, 3)$ in the basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$, since $N(e_k) = 1$ and $N(ie_k) = -1$.

**Proof.** Substituting $Q_0 = 0$ in $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ leaves the three terms; the signs of the real basis vectors are computed from $(ie_k)^2 = i^2 e_k^2 = -(-1) = 1$ for the biquaternion norm $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$.

Like the centre subspace and unlike the four others, the vector subspace is a subspace on which the biquaternion norm is not real-valued. Its **null elements** are the solutions of $Q_1^2 + Q_2^2 + Q_3^2 = 0$, a complex cone through the origin of real dimension four.

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} \in \mathrm{Vect}(\mathbb{B})$ the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q}$ is not a zero divisor. The zero divisors are exactly the null elements, $\tilde{Q} \neq 0$ with $N(\tilde{Q}) = 0$.

**Proof.** The general invertibility criterion gives the equivalence of the first two; for the third, if $N(\tilde{Q}) \neq 0$ then $\tilde{Q}$ has the inverse $-\bar{\tilde{Q}}/N(\tilde{Q})$, since $\tilde{Q}^2 = -N(\tilde{Q})e_0$ implies $\bar{\tilde{Q}} = -\tilde{Q}$ and hence $\tilde{Q}(-\bar{\tilde{Q}}/N(\tilde{Q})) = -\tilde{Q}(-\tilde{Q})/N(\tilde{Q}) = \tilde{Q}^2/N(\tilde{Q}) = -e_0$; and if $N(\tilde{Q}) = 0$ then $\tilde{Q}^2 = 0$ with $\tilde{Q} \neq 0$, so $\tilde{Q}$ annihilates itself.

**Corollary.** Every null vector is nilpotent of index two: $\tilde{Q}^2 = 0$ but $\tilde{Q} \neq 0$. The vector subspace contains no idempotent other than $0$.

**Proof.** The first statement is the square formula with $N(\tilde{Q}) = 0$. For the second, if $\tilde{Q} \in \mathrm{Vect}(\mathbb{B})$ satisfies $\tilde{Q}^2 = \tilde{Q}$, then $-\tilde{Q} = N(\tilde{Q})e_0$ by the square formula, so $\tilde{Q}$ is both a vector element and a central one; the intersection of the two subspaces is the origin, whence $\tilde{Q} = 0$.

The zero divisors of the vector subspace are called the **pure zero divisors** in *Biquaternion Zero Divisors*, which develops the classification and the two families of the algebra as a whole.

## The Four Involutions on It

In the basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$ the four involutions act diagonally:

| involution | matrix | sign pattern |
|---|---|---|
| $\bar{\cdot}$ | $-\mathrm{id}$ | all six signs negative |
| ${}^{*}$ | $\operatorname{diag}(1,1,1,-1,-1,-1)$ | real vectors fixed, imaginary vectors negated |
| ${}^{\dagger}$ | $\operatorname{diag}(-1,-1,-1,1,1,1)$ | real vectors negated, imaginary vectors fixed |
| $\flat$ | $\operatorname{diag}(1,1,1,-1,-1,-1)$ | as ${}^{*}$ |

The subspace is invariant under all four. Quaternion conjugation acts as the negative of the identity, which is the defining property of the subspace; complex conjugation preserves the two coordinate blocks it contains, fixing $\operatorname{span}\{e_k\}$ and negating $\operatorname{span}\{ie_k\}$, and Hermitian conjugation preserves them with the two roles exchanged, negating the first and fixing the second; reversal acts as complex conjugation does.

## Relations to the Other Five Subspaces

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{C}_{\mathbb{B}}$ | $\{0\}$ | $0$ |
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{e_1, e_2, e_3\}$ | $3$ |
| $\mathrm{Vect}(\mathbb{B}) \cap i\mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{ie_1, ie_2, ie_3\}$ | $3$ |
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_+$ | $\operatorname{span}\{ie_1, ie_2, ie_3\}$ | $3$ |
| $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_-$ | $\operatorname{span}\{e_1, e_2, e_3\}$ | $3$ |

The vector subspace is complementary to the centre, $\mathbb{B} = \mathrm{Vect}(\mathbb{B}) \oplus \mathbb{C}_{\mathbb{B}}$, and with each of the other four its sum has dimension $7$, so the pair spans all but one real dimension and no other pair is a decomposition. The four intersections of dimension three are the four coordinate blocks of the algebra away from the scalar lines; the pattern is recorded in *Biquaternion Relations Between Subspaces*.

## The Subspace in the Algebra

The section places the subspace among the particular cases that the Algebra articles treat one by one — the idempotents, the ideals and the Peirce decomposition, the roots of minus one, the zero divisors and the commutator bracket — each stated for the subspace and referred to its article.

### Idempotents

**Proposition.** The vector subspace contains no idempotent other than $0$.

**Proof.** Write an idempotent as $\tilde\Pi = \Pi_0 e_0 + \boldsymbol\Pi$. If $\boldsymbol\Pi = 0$ the idempotent is $0$ or $e_0$, neither of which is pure; if $\boldsymbol\Pi \neq 0$ the equation $2\Pi_0\boldsymbol\Pi = \boldsymbol\Pi$ of *Biquaternion Idempotents and Projections* gives $\Pi_0 = \tfrac12 \neq 0$, so the scalar part does not vanish and the idempotent is not in $\mathrm{Vect}(\mathbb{B})$.

What the subspace does contribute to the idempotent theory is the *off-diagonal* half of the Peirce decomposition: the elements

$$
\tilde T = \tfrac12(ie_1 - e_2), \qquad \tilde S = \tfrac12(ie_1 + e_2)
$$

of *Biquaternion Ideals and Peirce Decomposition* are pure vectors with $\tilde T^2 = \tilde S^2 = 0$, and they span the two off-diagonal Peirce corners. The diagonal corners, and with them the idempotents themselves, lie elsewhere: the vector subspace carries the nilpotent corners and none of the projections.

### Ideals and the Peirce Decomposition

**Proposition.** $\mathrm{Vect}(\mathbb{B})$ is neither a two-sided ideal of $\mathbb{B}$ nor a one-sided ideal.

**Proof.** Since $\mathbb{B}$ is simple its two-sided ideals are $0$ and $\mathbb{B}$, and the vector subspace, of dimension $6$, is neither. Nor is it one-sided: $e_1 \in \mathrm{Vect}(\mathbb{B})$ while $e_1 \cdot e_1 = -e_0 \notin \mathrm{Vect}(\mathbb{B})$, so neither $\mathbb{B}\,\mathrm{Vect}(\mathbb{B})$ nor $\mathrm{Vect}(\mathbb{B})\,\mathbb{B}$ is contained in $\mathrm{Vect}(\mathbb{B})$.

So the vector subspace is a piece of the algebra that the ideal lattice does not see; what it carries is the off-diagonal part of the Peirce decomposition, computed above, and the derived subalgebra of the Lie theory, below. As a module it is free of rank three over the centre, $\mathrm{Vect}(\mathbb{B}) = \mathbb{C}_{\mathbb{B}}\,e_1 \oplus \mathbb{C}_{\mathbb{B}}\,e_2 \oplus \mathbb{C}_{\mathbb{B}}\,e_3$.

### The Roots of Minus One

**Proposition.** Every root of $-1$ other than the two trivial roots lies in $\mathrm{Vect}(\mathbb{B})$; the trivial roots $\pm i$ are the only roots outside it.

**Proof.** By the reduction of *Biquaternion Roots of Minus One*, a root is either trivial, $\xi = \pm i$, or pure; and $\mathrm{Vect}(\mathbb{B})$ is exactly the set of elements of vanishing scalar part.

The vector subspace therefore contains the whole two-real-dimensional family of real roots $\pm\mu$, with $\mu$ a unit element of $\operatorname{span}_\mathbb{R}\{e_1,e_2,e_3\}$, and the whole four-real-dimensional family of non-trivial roots $b\mu + d\nu i$. The real roots lie in the real vector triple, while a non-trivial root mixes a real and an imaginary vector direction and lies in none of the two vector triples alone. These are exactly the roots that generate the non-central idempotents — the Hermitian family from the real roots and the third family from the non-trivial ones — so the vector subspace is where the roots of the algebra live.

### Zero Divisors

**Proposition.** The zero divisors of $\mathrm{Vect}(\mathbb{B})$ are exactly the non-zero nilpotents, and they are the pure family in its entirety.

**Proof.** For $\tilde{Q} = Q_1e_1 + Q_2e_2 + Q_3e_3$ one has $\bar{\tilde{Q}} = -\tilde{Q}$ and $\tilde{Q}^2 = -\bigl(\sum_k Q_k^2\bigr)e_0$, so $\tilde{Q}\bar{\tilde{Q}} = \sum_k Q_k^2$ and the criterion $\tilde{Q}\bar{\tilde{Q}} = 0$ reads $\sum_k Q_k^2 = 0$; in that case $\tilde{Q}^2 = 0$.

This is the pure case, the nilpotent cone, of *Biquaternion Zero Divisors*: a complex cone of complex dimension $2$ and real dimension $4$, whose elements have vanishing scalar part, as against the non-pure family of complex multiples of idempotents. The vector subspace is the only one of the six whose zero divisors are all nilpotent — the sectors have null zero divisors that are not nilpotent, and the centre, the quaternion and the anti-quaternion subspaces have none.

### The Lie Algebra Structure

The vector subspace is the derived subalgebra of the Lie algebra,

$$
[\mathrm{G},\mathrm{G}] = \mathrm{B}_0 = \operatorname{span}_{\mathbb{C}}\{e_1,e_2,e_3\} = \mathrm{Vect}(\mathbb{B}) ,
$$

of complex dimension $3$ and real dimension $6$; it is the trace-free part, $\mathrm{Tr}(\tilde{Q}) = 2Q_0 = 0$, it is closed under the bracket, and on it the bracket is twice the cross product, $[\mathbf{P},\mathbf{Q}] = 2\,\mathbf{P}\times\mathbf{Q}$ under the identification $\mathrm{Vect}(\mathbb{B}) \cong \mathbb{C}^3$. Over $\mathbb{R}$ it splits into the rotation subalgebra

$$
\mathrm{K} = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\} = \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-
$$

and the hyperbolic directions $\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\} = i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$, two non-isomorphic real Lie algebras; the algebra is not solvable, since its derived subalgebra is the whole trace-free part. The quotient $\mathrm{G}/[\mathrm{G},\mathrm{G}]$ is the centre. The details are in *Biquaternion Lie Algebra*.

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
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{2} = -\frac{e_1 + e_2}{2} ,
$$

which is again a vector element; the inverse of a non-null vector stays in the subspace, as the formula for the inverse of a pure element requires.

### A Null Vector

For $\tilde{Q} = e_1 + ie_2$ one has $N(\tilde{Q}) = 1 + i^2 = 0$, so $\tilde{Q}$ is a zero divisor, and indeed

$$
\tilde{Q}^2 = -N(\tilde{Q})e_0 = 0 , \qquad \tilde{Q} \neq 0 ,
$$

so $\tilde{Q}$ is its own annihilator. The example exhibits the coincidence of three conditions that hold only on the vector subspace among the six: purity of the element, nullity of the biquaternion norm, and nilpotency of index two.

### An Imaginary Vector and the Cross Product

For $\tilde{Q} = e_1$ and $\tilde{R} = ie_2$, the product is

$$
e_1 \cdot ie_2 = i e_3 \in \mathrm{Vect}(\mathbb{B}) , \qquad [e_1, ie_2] = 2ie_3 ,
$$

with vanishing dot product of the triples $(1, 0, 0)$ and $(0, i, 0)$. The bracket relations with a factor $i$ are the complexification of the real ones.

## Summary

The vector subspace $\mathrm{Vect}(\mathbb{B})$ is the anti-fixed space of quaternion conjugation, the set of elements of vanishing scalar part, a real vector space of dimension $6$ with basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$, splitting into the real and imaginary vectors. It is simultaneously the kernel of the scalar-part functional, the derived subspace $[\mathbb{B}, \mathbb{B}]$, and the Lie algebra of the unit-norm group. It is not a subalgebra and not a module over the quaternion or anti-quaternion subspaces, but it is closed under the commutator, where the bracket is twice the cross product of the coefficient triples. The square of a vector element is central, $\tilde{Q}^2 = -N(\tilde{Q})e_0$, so null elements are nilpotent and units have their inverses in the subspace. The biquaternion norm restricts to $Q_1^2+Q_2^2+Q_3^2$, complex-valued, of real signature $(3,3)$; the zero divisors are exactly the null elements. Quaternion conjugation acts as minus the identity, complex conjugation fixes the coordinate block $\operatorname{span}\{e_k\}$ and negates $\operatorname{span}\{ie_k\}$, and all four involutions preserve the subspace. It is complementary to the centre, and its intersections with the other four subspaces are three-dimensional. In the algebra of particular cases the vector subspace carries no idempotent but the origin but does carry the two nilpotent Peirce corners $\tilde T, \tilde S$, it is no ideal of any kind, it contains every root of $-1$ except the two trivial points, it carries the pure (nilpotent) family of zero divisors, and it is the derived subalgebra $[\mathrm{G},\mathrm{G}]$ of the Lie algebra.

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
| $N(\tilde{Q}) = Q_1^2+Q_2^2+Q_3^2$ | the biquaternion norm on the subspace |
| $\tilde T, \tilde S$ | the off-diagonal Peirce elements $\tfrac12(ie_1 \mp e_2)$, nilpotents of the subspace |
| $\xi$, $\tilde\Pi$ | a root of $-1$ and an idempotent of $\mathbb{B}$ |
| $\mathrm{K}$ | the rotation subalgebra $\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$ | the four involutions |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the multiplication of $\mathbb{B}$ and the scalar–vector decomposition
- *Biquaternion Centre Subspace* (`articles_maths/biquaternion-centre-subspace.md`), the fixed companion of the present subspace
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the classification whose non-trivial idempotents all lie outside the subspace
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the off-diagonal Peirce corners $\tilde T, \tilde S$ that the subspace carries
- *Biquaternion Roots of Minus One* (`articles_maths/biquaternion-roots-of-minus-one.md`), for the roots, all of them but $\pm i$ lying in the subspace
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the pure and non-pure zero divisors and the two families of the algebra
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the intersections, the sums and the coordinate blocks of the six
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions and the two spaces each defines
- *Biquaternion Lie Algebra* (`articles_maths/biquaternion-lie-algebra.md`) and *Biquaternion Lie Group and Exponential Structure* (`articles_maths/biquaternion-lie-group-and-exponential-structure.md`), for the Lie algebra of the group of units and of the norm-one group
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the biquaternion norm and the invertibility criterion
- *The Orthogonal Lie Algebra* (`articles_maths/the-orthogonal-lie-algebra.md`), for the cross-product Lie structure in its general setting
