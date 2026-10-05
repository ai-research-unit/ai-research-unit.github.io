# __Introduction to the Six Subspaces__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four conjugations, and each of them is an involution. Each one splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and the eight spaces so obtained reduce to six distinct subspaces, the **six distinguished subspaces** of $\mathbb{B}$. The conjugations themselves are not the subject of this article: their definitions, the group they form and the two spaces each defines are in *Biquaternions as a Vector Space over $\mathbb{C}$* and *Biquaternion Involution Lattice*.

This article treats the six subspaces themselves, one to a section. Each section gives the defining condition of the subspace, the coordinate condition it amounts to, the real basis that exhibits it and its real dimension, and closes with the part it plays. The table is the summary; the sections are the detail.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | role |
|---|---|---|---|---|
| the centre $\mathbb{C}_{\mathbb{B}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $e_0, ie_0$ | $2$ | the centre of the algebra, a field |
| the vector subspace $\mathrm{Vect}(\mathbb{B})$ | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $e_1, e_2, e_3, ie_1, ie_2, ie_3$ | $6$ | the kernel of the scalar part, a Lie algebra |
| the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0, e_1, e_2, e_3$ | $4$ | a division algebra |
| the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $ie_0, ie_1, ie_2, ie_3$ | $4$ | a module over $\mathbb{H}_{\mathbb{B}}$ |
| the Hermitian subspace $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0, ie_1, ie_2, ie_3$ | $4$ | a Jordan algebra |
| the anti-Hermitian subspace $\mathbb{M}_-$ | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_0, e_1, e_2, e_3$ | $4$ | a Lie algebra |

The six are pairwise distinct. Their relations — the coordinate blocks out of which they are built, their pairwise intersections, their sums, the action of the four conjugations and the action of the central imaginary unit — are the subject of *Comparison of the Six Subspaces*, and are not treated here. The algebra that each subspace carries is not treated here either: the product and its two halves, the Jordan algebra, the Lie algebra, the units, the zero divisors, the idempotents and projections, the ideals and the Peirce decomposition, the roots of minus one, the two matrix representations, the forms and the analysis are the business of the thematic articles of the group, each stated once for the six.

Nothing below is a physical statement. The elements are written $\tilde{Q}, \tilde{R}, \tilde{P}, \dots$, their complex coefficients $Q_0, Q_1, Q_2, Q_3$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$; no other coordinates are used.

## The Centre Subspace

**Definition.** The **centre subspace** $\mathbb{C}_{\mathbb{B}}$ is the fixed space of quaternion conjugation,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = \tilde{Q} \right\} .
$$

**Coordinate condition.** Writing $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ and comparing the two sides of $\tilde{Q}^{\natural} = \tilde{Q}$ coefficient by coefficient, the coefficient of $e_0$ gives no condition while the coefficient of $e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for $k = 1, 2, 3$. The subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_0e_0 , \qquad Q_0 \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $e_0, ie_0$ and $\dim_{\mathbb{R}}\mathbb{C}_{\mathbb{B}} = 2$. In the eight real coordinates it is the coordinate plane $q_1 = q_2 = q_3 = q'_1 = q'_2 = q'_3 = 0$.

**Role.** It is the centre of the algebra, the set of elements that commute with every element, and it is a commutative subalgebra isomorphic to $\mathbb{C}$; it is one of the two of the six that are closed under the product. Its elements are the **central elements**, written $Ae_0$ with $A \in \mathbb{C}$.

## The Vector Subspace

**Definition.** The **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the anti-fixed space of quaternion conjugation,

$$
\mathrm{Vect}(\mathbb{B}) = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** Comparing coefficients, the condition is $Q_0 = 0$: the scalar part vanishes, and the subspace is the kernel of the scalar-part functional $\operatorname{Sc}(\tilde{Q}) = Q_0 = \tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$,

$$
\tilde{Q} = Q_1e_1 + Q_2e_2 + Q_3e_3 , \qquad Q_1, Q_2, Q_3 \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $e_1, e_2, e_3, ie_1, ie_2, ie_3$ and $\dim_{\mathbb{R}}\mathrm{Vect}(\mathbb{B}) = 6$. It is the largest of the six, and the only one of dimension $6$.

**Role.** It is not a subalgebra, since the product of two pure vectors has a scalar part; it is closed under the commutator, the bracket of two pure vectors being twice their cross product. It splits into the real vector triple $\operatorname{span}\{e_1,e_2,e_3\}$ and the imaginary vector triple $\operatorname{span}\{ie_1,ie_2,ie_3\}$, and its elements are the **pure vectors**, written $\mathbf{Q}$.

## The Quaternion Subspace

**Definition.** The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation,

$$
\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be fixed by complex conjugation, that is, that each be real, $Q_\mu = q_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $e_0, e_1, e_2, e_3$ and $\dim_{\mathbb{R}}\mathbb{H}_{\mathbb{B}} = 4$. It is the copy of the real quaternion algebra inside $\mathbb{B}$.

**Role.** It is a subalgebra, the second of the two of the six that are closed under the product, and it is a division algebra: every non-zero element is a unit. It is the only one of the six that is non-commutative, and it is the image of the structure map $\mathbb{H} \to \mathbb{B}$, $h \mapsto he_0$.

## The Anti-Quaternion Subspace

**Definition.** The **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed space of complex conjugation,

$$
i\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be negated by complex conjugation, that is, that each be purely imaginary, $Q_\mu = iq'_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $ie_0, ie_1, ie_2, ie_3$ and $\dim_{\mathbb{R}}i\mathbb{H}_{\mathbb{B}} = 4$.

**Role.** Its elements are exactly the products $i\tilde{P}$ with $\tilde{P} \in \mathbb{H}_{\mathbb{B}}$, so the subspace is the image of $\mathbb{H}_{\mathbb{B}}$ under multiplication by the central imaginary unit. It is not a subalgebra — the product of two of its elements lands in the quaternion subspace — but it is a two-sided module over $\mathbb{H}_{\mathbb{B}}$. It splits into the imaginary scalar line $\mathbb{R}(ie_0)$ and the imaginary vector triple $\operatorname{span}\{ie_1,ie_2,ie_3\}$.

## The Hermitian Subspace

**Definition.** The **Hermitian subspace** $\mathbb{M}_+$ is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = \tilde{Q} \right\} , \qquad \tilde{Q}^{*} = \bar{\tilde{Q}}^{\natural} .
$$

**Coordinate condition.** Since ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, the condition is that the scalar coefficient be real while the three vector coefficients be purely imaginary,

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 , \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $e_0, ie_1, ie_2, ie_3$ and $\dim_{\mathbb{R}}\mathbb{M}_+ = 4$.

**Role.** It is not a subalgebra, but it is closed under the symmetrized product $\tilde{P} \bullet \tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$, which makes it a Jordan algebra. It is the set of elements with real scalar part and purely imaginary vector part.

## The Anti-Hermitian Subspace

**Definition.** The **anti-Hermitian subspace** $\mathbb{M}_-$ is the anti-fixed space of Hermitian conjugation, which is also the fixed space of the reversal $\flat = -{}^{*}$,

$$
\mathbb{M}_- = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = -\tilde{Q} \right\} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\flat} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is the reverse of the Hermitian one: the scalar coefficient is purely imaginary and the three vector coefficients are real,

$$
\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 , \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $ie_0, e_1, e_2, e_3$ and $\dim_{\mathbb{R}}\mathbb{M}_- = 4$.

**Role.** It is not a subalgebra and it is not closed under the symmetrized product; it is closed under the commutator, and it is a real Lie algebra of dimension four whose centre is the line $\mathbb{R}(ie_0)$. It is the set of elements with purely imaginary scalar part and real vector part, and it is the anti-fixed space of ${}^{*}$ as well as the fixed space of $\flat$.

## Summary

The biquaternion algebra carries four conjugations whose fixed and anti-fixed spaces reduce to six distinct subspaces, the six distinguished subspaces. The centre $\mathbb{C}_{\mathbb{B}}$, the fixed space of quaternion conjugation, is the set of elements with vanishing vector part, of real basis $e_0, ie_0$ and dimension $2$; it is the centre of the algebra and a field. The vector subspace $\mathrm{Vect}(\mathbb{B})$, the anti-fixed space of quaternion conjugation, is the kernel of the scalar part, of real basis $e_1, e_2, e_3, ie_1, ie_2, ie_3$ and dimension $6$; it is a Lie algebra and not a subalgebra. The quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the fixed space of complex conjugation, is the set of elements with real coefficients, of real basis $e_0, e_1, e_2, e_3$ and dimension $4$; it is a division subalgebra. The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the anti-fixed space of complex conjugation, is the set of elements with purely imaginary coefficients, of real basis $ie_0, ie_1, ie_2, ie_3$ and dimension $4$; it is a module over the quaternion subspace and not a subalgebra. The Hermitian subspace $\mathbb{M}_+$, the fixed space of Hermitian conjugation, is the set of elements with real scalar part and purely imaginary vector part, of real basis $e_0, ie_1, ie_2, ie_3$ and dimension $4$; it is a Jordan algebra under the symmetrized product. The anti-Hermitian subspace $\mathbb{M}_-$, the anti-fixed space of Hermitian conjugation and the fixed space of the reversal, is the set of elements with purely imaginary scalar part and real vector part, of real basis $ie_0, e_1, e_2, e_3$ and dimension $4$; it is a real Lie algebra. Exactly two of the six are closed under the product, the centre and the quaternion subspace, and both are division algebras. The six are pairwise distinct; their relations are collected in *Comparison of the Six Subspaces*, and the algebra each one carries belongs to the thematic articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0, e_1, e_2, e_3$ | the basis, with $e_0$ the unit and $e_k^2 = -e_0$ |
| $i$ | the central imaginary unit, $i^2 = -1$, commuting with every element |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a general biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | the complex coefficient of $e_\mu$, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $\operatorname{Sc}(\tilde{Q})$ | the scalar part $Q_0$, equal to $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$ |
| $\mathbb{C}_{\mathbb{B}}$ | the centre subspace, fixed by ${}^{\natural}$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, anti-fixed by ${}^{\natural}$ |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde{P} \bullet \tilde{Q}$ | the symmetrized product $\tfrac{1}{2}(\tilde{P}\tilde{Q} + \tilde{Q}\tilde{P})$ |

## Further Reading

- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the coordinate blocks, the intersections, the sums and the action of the conjugations on the six
- *The Six Subspaces and the Products* (`articles_maths/the-six-subspaces-and-the-products.md`), for the product of two elements of the six, tabulated
- *The Six Subspaces and the Jordan Algebra* (`articles_maths/the-six-subspaces-and-the-jordan-algebra.md`), for the symmetrized product and the Jordan subalgebras among the six
- *The Six Subspaces and the Lie Algebra* (`articles_maths/the-six-subspaces-and-the-lie-algebra.md`), for the commutator and the Lie subalgebras among the six
- *The Six Subspaces and the Units* (`articles_maths/the-six-subspaces-and-the-units.md`), for which elements of each of the six are units, and which of the six contain no nonzero zero divisor
- *The Six Subspaces and the Zero Divisors* (`articles_maths/the-six-subspaces-and-the-zero-divisors.md`), for the zero divisors of each of the six and for the two families, the square-zero pure ones and the non-pure ones that are multiples of idempotents
- *The Six Subspaces and the Idempotents and Projections* (`articles_maths/the-six-subspaces-and-the-idempotents-and-projections.md`), for the idempotents that lie in the six and for the projection they carry
- *The Six Subspaces and the Ideals* (`articles_maths/the-six-subspaces-and-the-ideals.md`), for the minimal one-sided ideals the six determine through their zero divisors and for the Peirce decomposition
- *The Six Subspaces and the Roots of Minus One* (`articles_maths/the-six-subspaces-and-the-roots-of-minus-one.md`), for which of the six contain a root of $-1$ and which roots
- *The Six Subspaces and the Two Matrix Representations* (`articles_maths/the-six-subspaces-and-the-two-matrix-representations.md`), for the six in the $2 \times 2$ model of the simple module and in the $4 \times 4$ regular model, and for the two invariants, trace and determinant
- *The Six Subspaces and the Forms* (`articles_maths/the-six-subspaces-and-the-forms.md`), for the bilinear, Hermitian and Krein pairings restricted to the six, the only orthogonal pair, and the isotropic lines and the minimal ideals
- *The Six Subspaces and the Analysis* (`articles_maths/the-six-subspaces-and-the-analysis.md`), for the variables and the operators on each of the six, the second-order operator as the operator of the norm, and the ellipticity dichotomy
- *Decompositions Along the Six Subspaces* (`articles_maths/decompositions-along-the-six-subspaces.md`), for the three eigenspace decompositions the conjugations cut out, one pair of subspaces to each
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, its basis, its conjugations and its coordinate systems
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four conjugations, the group they generate and the two spaces each defines
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the product and its scalar–vector form
- *Decomposition of the Multiplication* (`articles_maths/decomposition-of-the-multiplication.md`), for the two halves into which the product splits
- *Biquaternion Jordan Algebra* (`articles_maths/biquaternion-jordan-algebra.md`), for the symmetrized product and the trace form
- *Biquaternion Lie Algebra* (`articles_maths/biquaternion-lie-algebra.md`), for the commutator, the derived subalgebra and the adjoint maps
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the idempotents, the projections and the Peirce corners
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the one-sided ideals and the minimal left ideals
- *Modules over the Biquaternion Algebra* (`articles_maths/modules-over-the-biquaternion-algebra.md`), for the simple module $S$ and the Morita equivalence
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the null elements and their distribution
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the root sets and the bijection with the idempotents
- *Worked Examples in the Biquaternion Algebra* (`articles_maths/worked-examples-in-the-biquaternion-algebra.md`), for the basis products and the computed cases
